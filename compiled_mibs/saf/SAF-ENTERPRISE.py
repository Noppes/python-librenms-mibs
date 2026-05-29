# SNMP MIB module (SAF-ENTERPRISE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\saf\SAF-ENTERPRISE

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

saf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7571)
)
if mibBuilder.loadTexts:
    saf.setRevisions(
        ("2015-11-12 00:00",
         "2007-04-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tehnika_ObjectIdentity = ObjectIdentity
tehnika = _Tehnika_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100)
)
if mibBuilder.loadTexts:
    tehnika.setStatus("current")
_MicrowaveRadio_ObjectIdentity = ObjectIdentity
microwaveRadio = _MicrowaveRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1)
)
_PointToPoint_ObjectIdentity = ObjectIdentity
pointToPoint = _PointToPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 1, 1)
)
_Microwave_ObjectIdentity = ObjectIdentity
microwave = _Microwave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 2)
)
_Aranet_ObjectIdentity = ObjectIdentity
aranet = _Aranet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 3)
)
_ControlDevice_ObjectIdentity = ObjectIdentity
controlDevice = _ControlDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7571, 100, 64)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAF-ENTERPRISE",
    **{"saf": saf,
       "tehnika": tehnika,
       "microwaveRadio": microwaveRadio,
       "pointToPoint": pointToPoint,
       "microwave": microwave,
       "aranet": aranet,
       "controlDevice": controlDevice}
)
