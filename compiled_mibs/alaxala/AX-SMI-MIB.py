# SNMP MIB module (AX-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-SMI-MIB

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

alaxala = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839)
)
if mibBuilder.loadTexts:
    alaxala.setRevisions(
        ("2015-12-25 00:00",
         "2014-05-12 00:00",
         "2013-04-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaxalaProductId_ObjectIdentity = ObjectIdentity
alaxalaProductId = _AlaxalaProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 1)
)
_AxRouter_ObjectIdentity = ObjectIdentity
axRouter = _AxRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 1, 1)
)
_Ax8600r_ObjectIdentity = ObjectIdentity
ax8600r = _Ax8600r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 1, 1, 19)
)
_AxSwitch_ObjectIdentity = ObjectIdentity
axSwitch = _AxSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2)
)
_Ax8600s_ObjectIdentity = ObjectIdentity
ax8600s = _Ax8600s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 19)
)
_Ax8300s_ObjectIdentity = ObjectIdentity
ax8300s = _Ax8300s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 22)
)
_AlaxalaMib_ObjectIdentity = ObjectIdentity
alaxalaMib = _AlaxalaMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2)
)
_AxEx_ObjectIdentity = ObjectIdentity
axEx = _AxEx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4)
)
_AxMib_ObjectIdentity = ObjectIdentity
axMib = _AxMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-SMI-MIB",
    **{"alaxala": alaxala,
       "alaxalaProductId": alaxalaProductId,
       "axRouter": axRouter,
       "ax8600r": ax8600r,
       "axSwitch": axSwitch,
       "ax8600s": ax8600s,
       "ax8300s": ax8300s,
       "alaxalaMib": alaxalaMib,
       "axEx": axEx,
       "axMib": axMib}
)
