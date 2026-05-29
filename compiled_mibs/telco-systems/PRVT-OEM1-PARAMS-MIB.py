# SNMP MIB module (PRVT-OEM1-PARAMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-OEM1-PARAMS-MIB

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

prvtOem1ParamsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110)
)
if mibBuilder.loadTexts:
    prvtOem1ParamsMIB.setRevisions(
        ("2006-12-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtOem1ParamsObjects_ObjectIdentity = ObjectIdentity
prvtOem1ParamsObjects = _PrvtOem1ParamsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1)
)
_PrvtSerialNumber_Type = DisplayString
_PrvtSerialNumber_Object = MibScalar
prvtSerialNumber = _PrvtSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 1),
    _PrvtSerialNumber_Type()
)
prvtSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSerialNumber.setStatus("current")
_PrvtAssemblyNumber_Type = DisplayString
_PrvtAssemblyNumber_Object = MibScalar
prvtAssemblyNumber = _PrvtAssemblyNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 2),
    _PrvtAssemblyNumber_Type()
)
prvtAssemblyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtAssemblyNumber.setStatus("current")
_PrvtHardwareRevision_Type = DisplayString
_PrvtHardwareRevision_Object = MibScalar
prvtHardwareRevision = _PrvtHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 3),
    _PrvtHardwareRevision_Type()
)
prvtHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtHardwareRevision.setStatus("current")
_PrvtSwitchRevision_Type = DisplayString
_PrvtSwitchRevision_Object = MibScalar
prvtSwitchRevision = _PrvtSwitchRevision_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 4),
    _PrvtSwitchRevision_Type()
)
prvtSwitchRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSwitchRevision.setStatus("current")
_PrvtSwitchVersion_Type = DisplayString
_PrvtSwitchVersion_Object = MibScalar
prvtSwitchVersion = _PrvtSwitchVersion_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 5),
    _PrvtSwitchVersion_Type()
)
prvtSwitchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSwitchVersion.setStatus("current")
_PrvtSwitchEdition_Type = DisplayString
_PrvtSwitchEdition_Object = MibScalar
prvtSwitchEdition = _PrvtSwitchEdition_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 6),
    _PrvtSwitchEdition_Type()
)
prvtSwitchEdition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSwitchEdition.setStatus("current")
_PrvtSwitchRepair_Type = DisplayString
_PrvtSwitchRepair_Object = MibScalar
prvtSwitchRepair = _PrvtSwitchRepair_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 7),
    _PrvtSwitchRepair_Type()
)
prvtSwitchRepair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSwitchRepair.setStatus("current")
_PrvtHardwareAddress_Type = DisplayString
_PrvtHardwareAddress_Object = MibScalar
prvtHardwareAddress = _PrvtHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 8),
    _PrvtHardwareAddress_Type()
)
prvtHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtHardwareAddress.setStatus("current")
_PrvtCabinetRow_Type = DisplayString
_PrvtCabinetRow_Object = MibScalar
prvtCabinetRow = _PrvtCabinetRow_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 9),
    _PrvtCabinetRow_Type()
)
prvtCabinetRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCabinetRow.setStatus("current")
_PrvtCabinetColumn_Type = DisplayString
_PrvtCabinetColumn_Object = MibScalar
prvtCabinetColumn = _PrvtCabinetColumn_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 10),
    _PrvtCabinetColumn_Type()
)
prvtCabinetColumn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCabinetColumn.setStatus("current")
_PrvtChassisVerticalDeviation_Type = DisplayString
_PrvtChassisVerticalDeviation_Object = MibScalar
prvtChassisVerticalDeviation = _PrvtChassisVerticalDeviation_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 11),
    _PrvtChassisVerticalDeviation_Type()
)
prvtChassisVerticalDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtChassisVerticalDeviation.setStatus("current")
_PrvtChassisHorizontalDeviatioin_Type = DisplayString
_PrvtChassisHorizontalDeviatioin_Object = MibScalar
prvtChassisHorizontalDeviatioin = _PrvtChassisHorizontalDeviatioin_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 12),
    _PrvtChassisHorizontalDeviatioin_Type()
)
prvtChassisHorizontalDeviatioin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtChassisHorizontalDeviatioin.setStatus("current")
_PrvtCabinetHMSNumber_Type = DisplayString
_PrvtCabinetHMSNumber_Object = MibScalar
prvtCabinetHMSNumber = _PrvtCabinetHMSNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 13),
    _PrvtCabinetHMSNumber_Type()
)
prvtCabinetHMSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCabinetHMSNumber.setStatus("current")
_PrvtSubrackHMSNumber_Type = DisplayString
_PrvtSubrackHMSNumber_Object = MibScalar
prvtSubrackHMSNumber = _PrvtSubrackHMSNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 14),
    _PrvtSubrackHMSNumber_Type()
)
prvtSubrackHMSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSubrackHMSNumber.setStatus("current")
_PrvtModelNumber_Type = Integer32
_PrvtModelNumber_Object = MibScalar
prvtModelNumber = _PrvtModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 15),
    _PrvtModelNumber_Type()
)
prvtModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtModelNumber.setStatus("current")
_PrvtPluginUID_Type = Integer32
_PrvtPluginUID_Object = MibScalar
prvtPluginUID = _PrvtPluginUID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 1, 16),
    _PrvtPluginUID_Type()
)
prvtPluginUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPluginUID.setStatus("current")
_PrvtOem1ParamsNotifications_ObjectIdentity = ObjectIdentity
prvtOem1ParamsNotifications = _PrvtOem1ParamsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 2)
)
_PrvtOem1ParamsConformance_ObjectIdentity = ObjectIdentity
prvtOem1ParamsConformance = _PrvtOem1ParamsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 2110, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-OEM1-PARAMS-MIB",
    **{"prvtOem1ParamsMIB": prvtOem1ParamsMIB,
       "prvtOem1ParamsObjects": prvtOem1ParamsObjects,
       "prvtSerialNumber": prvtSerialNumber,
       "prvtAssemblyNumber": prvtAssemblyNumber,
       "prvtHardwareRevision": prvtHardwareRevision,
       "prvtSwitchRevision": prvtSwitchRevision,
       "prvtSwitchVersion": prvtSwitchVersion,
       "prvtSwitchEdition": prvtSwitchEdition,
       "prvtSwitchRepair": prvtSwitchRepair,
       "prvtHardwareAddress": prvtHardwareAddress,
       "prvtCabinetRow": prvtCabinetRow,
       "prvtCabinetColumn": prvtCabinetColumn,
       "prvtChassisVerticalDeviation": prvtChassisVerticalDeviation,
       "prvtChassisHorizontalDeviatioin": prvtChassisHorizontalDeviatioin,
       "prvtCabinetHMSNumber": prvtCabinetHMSNumber,
       "prvtSubrackHMSNumber": prvtSubrackHMSNumber,
       "prvtModelNumber": prvtModelNumber,
       "prvtPluginUID": prvtPluginUID,
       "prvtOem1ParamsNotifications": prvtOem1ParamsNotifications,
       "prvtOem1ParamsConformance": prvtOem1ParamsConformance}
)
