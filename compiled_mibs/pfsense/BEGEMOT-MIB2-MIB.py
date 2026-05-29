# SNMP MIB module (BEGEMOT-MIB2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pfsense\BEGEMOT-MIB2-MIB

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

(begemotIp,) = mibBuilder.importSymbols(
    "BEGEMOT-IP-MIB",
    "begemotIp")

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

begemotMib2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 3, 1)
)
if mibBuilder.loadTexts:
    begemotMib2.setRevisions(
        ("2009-08-03 00:00",
         "2006-02-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BegemotIfMaxspeed_Type = Counter64
_BegemotIfMaxspeed_Object = MibScalar
begemotIfMaxspeed = _BegemotIfMaxspeed_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 1),
    _BegemotIfMaxspeed_Type()
)
begemotIfMaxspeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotIfMaxspeed.setStatus("current")
if mibBuilder.loadTexts:
    begemotIfMaxspeed.setUnits("bps")
_BegemotIfPoll_Type = TimeTicks
_BegemotIfPoll_Object = MibScalar
begemotIfPoll = _BegemotIfPoll_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 2),
    _BegemotIfPoll_Type()
)
begemotIfPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotIfPoll.setStatus("current")
_BegemotIfForcePoll_Type = TimeTicks
_BegemotIfForcePoll_Object = MibScalar
begemotIfForcePoll = _BegemotIfForcePoll_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 3),
    _BegemotIfForcePoll_Type()
)
begemotIfForcePoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotIfForcePoll.setStatus("current")


class _BegemotIfDataPoll_Type(TimeTicks):
    """Custom type begemotIfDataPoll based on TimeTicks"""
    defaultValue = 100


_BegemotIfDataPoll_Type.__name__ = "TimeTicks"
_BegemotIfDataPoll_Object = MibScalar
begemotIfDataPoll = _BegemotIfDataPoll_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 4),
    _BegemotIfDataPoll_Type()
)
begemotIfDataPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotIfDataPoll.setStatus("current")
if mibBuilder.loadTexts:
    begemotIfDataPoll.setUnits("deciseconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BEGEMOT-MIB2-MIB",
    **{"begemotMib2": begemotMib2,
       "begemotIfMaxspeed": begemotIfMaxspeed,
       "begemotIfPoll": begemotIfPoll,
       "begemotIfForcePoll": begemotIfForcePoll,
       "begemotIfDataPoll": begemotIfDataPoll}
)
