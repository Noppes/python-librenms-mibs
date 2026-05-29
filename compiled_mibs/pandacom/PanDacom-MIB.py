# SNMP MIB module (PanDacom-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pandacom\PanDacom-MIB

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

panDacom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3652)
)
if mibBuilder.loadTexts:
    panDacom.setRevisions(
        ("2019-06-06 00:00",
         "2017-03-26 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FixedDiv100(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"


# MIB Managed Objects in the order of their OIDs

_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 0)
)


class _Descr_Type(DisplayString):
    """Custom type descr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Descr_Type.__name__ = "DisplayString"
_Descr_Object = MibScalar
descr = _Descr_Object(
    (1, 3, 6, 1, 4, 1, 3652, 0, 100),
    _Descr_Type()
)
descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    descr.setStatus("current")
_Slot_Type = Integer32
_Slot_Object = MibScalar
slot = _Slot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 0, 101),
    _Slot_Type()
)
slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slot.setStatus("current")
_Port_Type = Integer32
_Port_Object = MibScalar
port = _Port_Object(
    (1, 3, 6, 1, 4, 1, 3652, 0, 102),
    _Port_Type()
)
port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port.setStatus("current")
_IFCard_Type = Integer32
_IFCard_Object = MibScalar
iFCard = _IFCard_Object(
    (1, 3, 6, 1, 4, 1, 3652, 0, 103),
    _IFCard_Type()
)
iFCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iFCard.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PanDacom-MIB",
    **{"FixedDiv100": FixedDiv100,
       "panDacom": panDacom,
       "traps": traps,
       "descr": descr,
       "slot": slot,
       "port": port,
       "iFCard": iFCard}
)
