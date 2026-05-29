# SNMP MIB module (ZONE-DEFENSE-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\ZONE-DEFENSE-MGMT-MIB

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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swZoneDefenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 92)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwZoneDefenseMIBObjects_ObjectIdentity = ObjectIdentity
swZoneDefenseMIBObjects = _SwZoneDefenseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1)
)
_SwZoneDefenseTable_Object = MibTable
swZoneDefenseTable = _SwZoneDefenseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 1)
)
if mibBuilder.loadTexts:
    swZoneDefenseTable.setStatus("current")
_SwZoneDefenseEntry_Object = MibTableRow
swZoneDefenseEntry = _SwZoneDefenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 1, 1)
)
swZoneDefenseEntry.setIndexNames(
    (0, "ZONE-DEFENSE-MGMT-MIB", "swZoneDefenseAddress"),
)
if mibBuilder.loadTexts:
    swZoneDefenseEntry.setStatus("current")
_SwZoneDefenseAddress_Type = IpAddress
_SwZoneDefenseAddress_Object = MibTableColumn
swZoneDefenseAddress = _SwZoneDefenseAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 1, 1, 1),
    _SwZoneDefenseAddress_Type()
)
swZoneDefenseAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swZoneDefenseAddress.setStatus("current")
_SwZoneDefenseRowStatus_Type = RowStatus
_SwZoneDefenseRowStatus_Object = MibTableColumn
swZoneDefenseRowStatus = _SwZoneDefenseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 1, 1, 2),
    _SwZoneDefenseRowStatus_Type()
)
swZoneDefenseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swZoneDefenseRowStatus.setStatus("current")


class _SwZoneDefenseProtocol_Type(Integer32):
    """Custom type swZoneDefenseProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("icmp", 2),
          ("tcp", 3),
          ("udp", 4))
    )


_SwZoneDefenseProtocol_Type.__name__ = "Integer32"
_SwZoneDefenseProtocol_Object = MibTableColumn
swZoneDefenseProtocol = _SwZoneDefenseProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 1, 1, 3),
    _SwZoneDefenseProtocol_Type()
)
swZoneDefenseProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swZoneDefenseProtocol.setStatus("current")


class _SwZoneDefenseDstPort_Type(Integer32):
    """Custom type swZoneDefenseDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SwZoneDefenseDstPort_Type.__name__ = "Integer32"
_SwZoneDefenseDstPort_Object = MibTableColumn
swZoneDefenseDstPort = _SwZoneDefenseDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 1, 1, 4),
    _SwZoneDefenseDstPort_Type()
)
swZoneDefenseDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swZoneDefenseDstPort.setStatus("current")
_SwZoneDefenseMacTable_Object = MibTable
swZoneDefenseMacTable = _SwZoneDefenseMacTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 2)
)
if mibBuilder.loadTexts:
    swZoneDefenseMacTable.setStatus("current")
_SwZoneDefenseMacEntry_Object = MibTableRow
swZoneDefenseMacEntry = _SwZoneDefenseMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 2, 1)
)
swZoneDefenseMacEntry.setIndexNames(
    (0, "ZONE-DEFENSE-MGMT-MIB", "swZoneDefenseMacAddress"),
)
if mibBuilder.loadTexts:
    swZoneDefenseMacEntry.setStatus("current")
_SwZoneDefenseMacAddress_Type = MacAddress
_SwZoneDefenseMacAddress_Object = MibTableColumn
swZoneDefenseMacAddress = _SwZoneDefenseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 2, 1, 1),
    _SwZoneDefenseMacAddress_Type()
)
swZoneDefenseMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swZoneDefenseMacAddress.setStatus("current")
_SwZoneDefenseMacRowStatus_Type = RowStatus
_SwZoneDefenseMacRowStatus_Object = MibTableColumn
swZoneDefenseMacRowStatus = _SwZoneDefenseMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 2, 1, 2),
    _SwZoneDefenseMacRowStatus_Type()
)
swZoneDefenseMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swZoneDefenseMacRowStatus.setStatus("current")


class _SwZoneDefenseMacProtocol_Type(Integer32):
    """Custom type swZoneDefenseMacProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("icmp", 2),
          ("tcp", 3),
          ("udp", 4))
    )


_SwZoneDefenseMacProtocol_Type.__name__ = "Integer32"
_SwZoneDefenseMacProtocol_Object = MibTableColumn
swZoneDefenseMacProtocol = _SwZoneDefenseMacProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 2, 1, 3),
    _SwZoneDefenseMacProtocol_Type()
)
swZoneDefenseMacProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swZoneDefenseMacProtocol.setStatus("current")


class _SwZoneDefenseMacDstPort_Type(Integer32):
    """Custom type swZoneDefenseMacDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_SwZoneDefenseMacDstPort_Type.__name__ = "Integer32"
_SwZoneDefenseMacDstPort_Object = MibTableColumn
swZoneDefenseMacDstPort = _SwZoneDefenseMacDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 2, 1, 4),
    _SwZoneDefenseMacDstPort_Type()
)
swZoneDefenseMacDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swZoneDefenseMacDstPort.setStatus("current")


class _SwZoneDefenseStatus_Type(Integer32):
    """Custom type swZoneDefenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwZoneDefenseStatus_Type.__name__ = "Integer32"
_SwZoneDefenseStatus_Object = MibScalar
swZoneDefenseStatus = _SwZoneDefenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 3),
    _SwZoneDefenseStatus_Type()
)
swZoneDefenseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swZoneDefenseStatus.setStatus("current")
_SwZoneDefenseRemains_Type = Integer32
_SwZoneDefenseRemains_Object = MibScalar
swZoneDefenseRemains = _SwZoneDefenseRemains_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 4),
    _SwZoneDefenseRemains_Type()
)
swZoneDefenseRemains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swZoneDefenseRemains.setStatus("current")
_SwZoneDefenseIpRemains_Type = Integer32
_SwZoneDefenseIpRemains_Object = MibScalar
swZoneDefenseIpRemains = _SwZoneDefenseIpRemains_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 5),
    _SwZoneDefenseIpRemains_Type()
)
swZoneDefenseIpRemains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swZoneDefenseIpRemains.setStatus("current")
_SwZoneDefenseMacRemains_Type = Integer32
_SwZoneDefenseMacRemains_Object = MibScalar
swZoneDefenseMacRemains = _SwZoneDefenseMacRemains_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 92, 1, 6),
    _SwZoneDefenseMacRemains_Type()
)
swZoneDefenseMacRemains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swZoneDefenseMacRemains.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZONE-DEFENSE-MGMT-MIB",
    **{"swZoneDefenseMIB": swZoneDefenseMIB,
       "swZoneDefenseMIBObjects": swZoneDefenseMIBObjects,
       "swZoneDefenseTable": swZoneDefenseTable,
       "swZoneDefenseEntry": swZoneDefenseEntry,
       "swZoneDefenseAddress": swZoneDefenseAddress,
       "swZoneDefenseRowStatus": swZoneDefenseRowStatus,
       "swZoneDefenseProtocol": swZoneDefenseProtocol,
       "swZoneDefenseDstPort": swZoneDefenseDstPort,
       "swZoneDefenseMacTable": swZoneDefenseMacTable,
       "swZoneDefenseMacEntry": swZoneDefenseMacEntry,
       "swZoneDefenseMacAddress": swZoneDefenseMacAddress,
       "swZoneDefenseMacRowStatus": swZoneDefenseMacRowStatus,
       "swZoneDefenseMacProtocol": swZoneDefenseMacProtocol,
       "swZoneDefenseMacDstPort": swZoneDefenseMacDstPort,
       "swZoneDefenseStatus": swZoneDefenseStatus,
       "swZoneDefenseRemains": swZoneDefenseRemains,
       "swZoneDefenseIpRemains": swZoneDefenseIpRemains,
       "swZoneDefenseMacRemains": swZoneDefenseMacRemains}
)
