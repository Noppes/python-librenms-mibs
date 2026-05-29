# SNMP MIB module (SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sagemcom\SESSION-MIB

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

(SagemBoolean,) = mibBuilder.importSymbols(
    "EQUIPMENT-MIB",
    "SagemBoolean")

(sagemDr,) = mibBuilder.importSymbols(
    "SAGEM-DR-MIB",
    "sagemDr")

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

session = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 201)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _TLock_Type(Integer32):
    """Custom type tLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_TLock_Type.__name__ = "Integer32"
_TLock_Object = MibScalar
tLock = _TLock_Object(
    (1, 3, 6, 1, 4, 1, 1038, 201, 1),
    _TLock_Type()
)
tLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tLock.setStatus("current")
_SessionIp_Type = IpAddress
_SessionIp_Object = MibScalar
sessionIp = _SessionIp_Object(
    (1, 3, 6, 1, 4, 1, 1038, 201, 2),
    _SessionIp_Type()
)
sessionIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionIp.setStatus("current")


class _SessionType_Type(Integer32):
    """Custom type sessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("snmp", 1),
          ("http", 2),
          ("telnet", 3),
          ("vt100", 4),
          ("tpiEmulated", 5))
    )


_SessionType_Type.__name__ = "Integer32"
_SessionType_Object = MibScalar
sessionType = _SessionType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 201, 3),
    _SessionType_Type()
)
sessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionType.setStatus("current")


class _TLockDefault_Type(Integer32):
    """Custom type tLockDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_TLockDefault_Type.__name__ = "Integer32"
_TLockDefault_Object = MibScalar
tLockDefault = _TLockDefault_Object(
    (1, 3, 6, 1, 4, 1, 1038, 201, 5),
    _TLockDefault_Type()
)
tLockDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tLockDefault.setStatus("current")


class _TInactivity_Type(Integer32):
    """Custom type tInactivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TInactivity_Type.__name__ = "Integer32"
_TInactivity_Object = MibScalar
tInactivity = _TInactivity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 201, 6),
    _TInactivity_Type()
)
tInactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tInactivity.setStatus("current")
_SavePending_Type = SagemBoolean
_SavePending_Object = MibScalar
savePending = _SavePending_Object(
    (1, 3, 6, 1, 4, 1, 1038, 201, 20),
    _SavePending_Type()
)
savePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    savePending.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SESSION-MIB",
    **{"session": session,
       "tLock": tLock,
       "sessionIp": sessionIp,
       "sessionType": sessionType,
       "tLockDefault": tLockDefault,
       "tInactivity": tInactivity,
       "savePending": savePending}
)
