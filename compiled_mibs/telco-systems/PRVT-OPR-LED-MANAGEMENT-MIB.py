# SNMP MIB module (PRVT-OPR-LED-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-OPR-LED-MANAGEMENT-MIB

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

prvtOprLedMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 110)
)
if mibBuilder.loadTexts:
    prvtOprLedMgmtMIB.setRevisions(
        ("2006-07-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LedValues(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("green-stable", 1),
          ("green-blinking", 2),
          ("amber-stable", 3),
          ("amber-blinking", 4),
          ("red-stable", 5),
          ("red-blinking", 6))
    )



# MIB Managed Objects in the order of their OIDs

_PrvtOprLedMgmtObjects_ObjectIdentity = ObjectIdentity
prvtOprLedMgmtObjects = _PrvtOprLedMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 1)
)


class _PrvtOprLedSatus_Type(LedValues):
    """Custom type prvtOprLedSatus based on LedValues"""
    defaultValue = 1


_PrvtOprLedSatus_Type.__name__ = "LedValues"
_PrvtOprLedSatus_Object = MibScalar
prvtOprLedSatus = _PrvtOprLedSatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 1, 1),
    _PrvtOprLedSatus_Type()
)
prvtOprLedSatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtOprLedSatus.setStatus("current")
_PrvtOprLedMgmtNotifications_ObjectIdentity = ObjectIdentity
prvtOprLedMgmtNotifications = _PrvtOprLedMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 2)
)
_PrvtOprLedMgmtConformance_ObjectIdentity = ObjectIdentity
prvtOprLedMgmtConformance = _PrvtOprLedMgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-OPR-LED-MANAGEMENT-MIB",
    **{"LedValues": LedValues,
       "prvtOprLedMgmtMIB": prvtOprLedMgmtMIB,
       "prvtOprLedMgmtObjects": prvtOprLedMgmtObjects,
       "prvtOprLedSatus": prvtOprLedSatus,
       "prvtOprLedMgmtNotifications": prvtOprLedMgmtNotifications,
       "prvtOprLedMgmtConformance": prvtOprLedMgmtConformance}
)
