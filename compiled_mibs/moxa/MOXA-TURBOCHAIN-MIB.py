# SNMP MIB module (MOXA-TURBOCHAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\moxa\MOXA-TURBOCHAIN-MIB

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

(layer2Redundancy,) = mibBuilder.importSymbols(
    "MOXA-SWITCHING-MIB",
    "layer2Redundancy")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mxTurboChain = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 5)
)
if mibBuilder.loadTexts:
    mxTurboChain.setRevisions(
        ("2022-02-17 00:00",
         "2019-06-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TurboChainConfiguration_ObjectIdentity = ObjectIdentity
turboChainConfiguration = _TurboChainConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 5, 1)
)
_TurboChainConfigEnable_Type = TruthValue
_TurboChainConfigEnable_Object = MibScalar
turboChainConfigEnable = _TurboChainConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 5, 1, 1),
    _TurboChainConfigEnable_Type()
)
turboChainConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboChainConfigEnable.setStatus("current")


class _TurboChainConfigRole_Type(Integer32):
    """Custom type turboChainConfigRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("head", 1),
          ("member", 2),
          ("tail", 3))
    )


_TurboChainConfigRole_Type.__name__ = "Integer32"
_TurboChainConfigRole_Object = MibScalar
turboChainConfigRole = _TurboChainConfigRole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 5, 1, 2),
    _TurboChainConfigRole_Type()
)
turboChainConfigRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboChainConfigRole.setStatus("current")
_TurboChainConfigInterface_Type = OctetString
_TurboChainConfigInterface_Object = MibScalar
turboChainConfigInterface = _TurboChainConfigInterface_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 5, 1, 3),
    _TurboChainConfigInterface_Type()
)
turboChainConfigInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboChainConfigInterface.setStatus("current")
_TurboChainStatus_ObjectIdentity = ObjectIdentity
turboChainStatus = _TurboChainStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 5, 2)
)


class _TurboChainStatPrimaryInterfaceStatus_Type(Integer32):
    """Custom type turboChainStatPrimaryInterfaceStatus based on Integer32"""
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
        *(("initiated", 0),
          ("linkDown", 1),
          ("listening", 2),
          ("blocking", 3),
          ("forwarding", 4),
          ("disabled", 5))
    )


_TurboChainStatPrimaryInterfaceStatus_Type.__name__ = "Integer32"
_TurboChainStatPrimaryInterfaceStatus_Object = MibScalar
turboChainStatPrimaryInterfaceStatus = _TurboChainStatPrimaryInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 5, 2, 1),
    _TurboChainStatPrimaryInterfaceStatus_Type()
)
turboChainStatPrimaryInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboChainStatPrimaryInterfaceStatus.setStatus("current")


class _TurboChainStatSecondaryInterfaceStatus_Type(Integer32):
    """Custom type turboChainStatSecondaryInterfaceStatus based on Integer32"""
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
        *(("initiated", 0),
          ("linkDown", 1),
          ("listening", 2),
          ("blocking", 3),
          ("forwarding", 4),
          ("disabled", 5))
    )


_TurboChainStatSecondaryInterfaceStatus_Type.__name__ = "Integer32"
_TurboChainStatSecondaryInterfaceStatus_Object = MibScalar
turboChainStatSecondaryInterfaceStatus = _TurboChainStatSecondaryInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 5, 2, 2),
    _TurboChainStatSecondaryInterfaceStatus_Type()
)
turboChainStatSecondaryInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboChainStatSecondaryInterfaceStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-TURBOCHAIN-MIB",
    **{"mxTurboChain": mxTurboChain,
       "turboChainConfiguration": turboChainConfiguration,
       "turboChainConfigEnable": turboChainConfigEnable,
       "turboChainConfigRole": turboChainConfigRole,
       "turboChainConfigInterface": turboChainConfigInterface,
       "turboChainStatus": turboChainStatus,
       "turboChainStatPrimaryInterfaceStatus": turboChainStatPrimaryInterfaceStatus,
       "turboChainStatSecondaryInterfaceStatus": turboChainStatSecondaryInterfaceStatus}
)
