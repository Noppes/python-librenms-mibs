# SNMP MIB module (MOXA-SWITCHING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\moxa\MOXA-SWITCHING-MIB

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

switching = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603)
)
if mibBuilder.loadTexts:
    switching.setRevisions(
        ("2022-02-17 00:00",
         "2019-06-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(TextualConvention, OctetString):
    status = "current"


class Timeout(TextualConvention, Integer32):
    status = "current"
    displayHint = "d4"


# MIB Managed Objects in the order of their OIDs

_Moxa_ObjectIdentity = ObjectIdentity
moxa = _Moxa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691)
)
_PortInterface_ObjectIdentity = ObjectIdentity
portInterface = _PortInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1)
)
_BasicLayer2_ObjectIdentity = ObjectIdentity
basicLayer2 = _BasicLayer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 2)
)
_Layer2Redundancy_ObjectIdentity = ObjectIdentity
layer2Redundancy = _Layer2Redundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3)
)
_Layer2Security_ObjectIdentity = ObjectIdentity
layer2Security = _Layer2Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 4)
)
_Layer2Diagnosic_ObjectIdentity = ObjectIdentity
layer2Diagnosic = _Layer2Diagnosic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5)
)
_Layer3Diagnosic_ObjectIdentity = ObjectIdentity
layer3Diagnosic = _Layer3Diagnosic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 6)
)
_Layer2Multicast_ObjectIdentity = ObjectIdentity
layer2Multicast = _Layer2Multicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 7)
)
_Layer3Multicast_ObjectIdentity = ObjectIdentity
layer3Multicast = _Layer3Multicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-SWITCHING-MIB",
    **{"PortList": PortList,
       "Timeout": Timeout,
       "moxa": moxa,
       "switching": switching,
       "portInterface": portInterface,
       "basicLayer2": basicLayer2,
       "layer2Redundancy": layer2Redundancy,
       "layer2Security": layer2Security,
       "layer2Diagnosic": layer2Diagnosic,
       "layer3Diagnosic": layer3Diagnosic,
       "layer2Multicast": layer2Multicast,
       "layer3Multicast": layer3Multicast}
)
