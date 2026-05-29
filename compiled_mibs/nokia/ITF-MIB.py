# SNMP MIB module (ITF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ITF-MIB

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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(interfaces,) = mibBuilder.importSymbols(
    "IF-MIB",
    "interfaces")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class OwnerString(OctetString):
    """Custom type OwnerString based on OctetString"""




class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""




class InterfaceIndexOrZero(Integer32):
    """Custom type InterfaceIndexOrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IfNumber_Type = Integer32
_IfNumber_Object = MibScalar
ifNumber = _IfNumber_Object(
    (1, 3, 6, 1, 2, 1, 2, 1),
    _IfNumber_Type()
)
ifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifNumber.setStatus("mandatory")
_IfTable_Object = MibTable
ifTable = _IfTable_Object(
    (1, 3, 6, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ifTable.setStatus("mandatory")
_IfEntry_Object = MibTableRow
ifEntry = _IfEntry_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1)
)
ifEntry.setIndexNames(
    (0, "ITF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifEntry.setStatus("mandatory")
_IfIndex_Type = InterfaceIndex
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndex.setStatus("mandatory")
_IfDescr_Type = DisplayString
_IfDescr_Object = MibTableColumn
ifDescr = _IfDescr_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 2),
    _IfDescr_Type()
)
ifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDescr.setStatus("mandatory")
_IfType_Type = IANAifType
_IfType_Object = MibTableColumn
ifType = _IfType_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 3),
    _IfType_Type()
)
ifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifType.setStatus("mandatory")
_IfMtu_Type = Integer32
_IfMtu_Object = MibTableColumn
ifMtu = _IfMtu_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 4),
    _IfMtu_Type()
)
ifMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMtu.setStatus("mandatory")
_IfSpeed_Type = Gauge32
_IfSpeed_Object = MibTableColumn
ifSpeed = _IfSpeed_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 5),
    _IfSpeed_Type()
)
ifSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSpeed.setStatus("mandatory")
_IfPhysAddress_Type = PhysAddress
_IfPhysAddress_Object = MibTableColumn
ifPhysAddress = _IfPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 6),
    _IfPhysAddress_Type()
)
ifPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysAddress.setStatus("mandatory")


class _IfAdminStatus_Type(Integer32):
    """Custom type ifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_IfAdminStatus_Type.__name__ = "Integer32"
_IfAdminStatus_Object = MibTableColumn
ifAdminStatus = _IfAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 7),
    _IfAdminStatus_Type()
)
ifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAdminStatus.setStatus("mandatory")


class _IfOperStatus_Type(Integer32):
    """Custom type ifOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5))
    )


_IfOperStatus_Type.__name__ = "Integer32"
_IfOperStatus_Object = MibTableColumn
ifOperStatus = _IfOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 8),
    _IfOperStatus_Type()
)
ifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOperStatus.setStatus("mandatory")
_IfLastChange_Type = TimeTicks
_IfLastChange_Object = MibTableColumn
ifLastChange = _IfLastChange_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 9),
    _IfLastChange_Type()
)
ifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLastChange.setStatus("mandatory")
_IfInOctets_Type = Counter32
_IfInOctets_Object = MibTableColumn
ifInOctets = _IfInOctets_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 10),
    _IfInOctets_Type()
)
ifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInOctets.setStatus("mandatory")
_IfInUcastPkts_Type = Counter32
_IfInUcastPkts_Object = MibTableColumn
ifInUcastPkts = _IfInUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 11),
    _IfInUcastPkts_Type()
)
ifInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInUcastPkts.setStatus("mandatory")
_IfInNUcastPkts_Type = Counter32
_IfInNUcastPkts_Object = MibTableColumn
ifInNUcastPkts = _IfInNUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 12),
    _IfInNUcastPkts_Type()
)
ifInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInNUcastPkts.setStatus("deprecated")
_IfInDiscards_Type = Counter32
_IfInDiscards_Object = MibTableColumn
ifInDiscards = _IfInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 13),
    _IfInDiscards_Type()
)
ifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInDiscards.setStatus("mandatory")
_IfInErrors_Type = Counter32
_IfInErrors_Object = MibTableColumn
ifInErrors = _IfInErrors_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 14),
    _IfInErrors_Type()
)
ifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInErrors.setStatus("mandatory")
_IfInUnknownProtos_Type = Counter32
_IfInUnknownProtos_Object = MibTableColumn
ifInUnknownProtos = _IfInUnknownProtos_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 15),
    _IfInUnknownProtos_Type()
)
ifInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInUnknownProtos.setStatus("mandatory")
_IfOutOctets_Type = Counter32
_IfOutOctets_Object = MibTableColumn
ifOutOctets = _IfOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 16),
    _IfOutOctets_Type()
)
ifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutOctets.setStatus("mandatory")
_IfOutUcastPkts_Type = Counter32
_IfOutUcastPkts_Object = MibTableColumn
ifOutUcastPkts = _IfOutUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 17),
    _IfOutUcastPkts_Type()
)
ifOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutUcastPkts.setStatus("mandatory")
_IfOutNUcastPkts_Type = Counter32
_IfOutNUcastPkts_Object = MibTableColumn
ifOutNUcastPkts = _IfOutNUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 18),
    _IfOutNUcastPkts_Type()
)
ifOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutNUcastPkts.setStatus("deprecated")
_IfOutDiscards_Type = Counter32
_IfOutDiscards_Object = MibTableColumn
ifOutDiscards = _IfOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 19),
    _IfOutDiscards_Type()
)
ifOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutDiscards.setStatus("mandatory")
_IfOutErrors_Type = Counter32
_IfOutErrors_Object = MibTableColumn
ifOutErrors = _IfOutErrors_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 20),
    _IfOutErrors_Type()
)
ifOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutErrors.setStatus("mandatory")
_IfOutQLen_Type = Gauge32
_IfOutQLen_Object = MibTableColumn
ifOutQLen = _IfOutQLen_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 21),
    _IfOutQLen_Type()
)
ifOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutQLen.setStatus("deprecated")
_IfSpecific_Type = ObjectIdentifier
_IfSpecific_Object = MibTableColumn
ifSpecific = _IfSpecific_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 22),
    _IfSpecific_Type()
)
ifSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSpecific.setStatus("deprecated")
_IfMIB_ObjectIdentity = ObjectIdentity
ifMIB = _IfMIB_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 31)
)
_IfMIBObjects_ObjectIdentity = ObjectIdentity
ifMIBObjects = _IfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 31, 1)
)
_IfXTable_Object = MibTable
ifXTable = _IfXTable_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1)
)
if mibBuilder.loadTexts:
    ifXTable.setStatus("mandatory")
_IfXEntry_Object = MibTableRow
ifXEntry = _IfXEntry_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1)
)
ifXEntry.setIndexNames(
    (0, "ITF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifXEntry.setStatus("mandatory")
_IfName_Type = DisplayString
_IfName_Object = MibTableColumn
ifName = _IfName_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 1),
    _IfName_Type()
)
ifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifName.setStatus("mandatory")
_IfInMulticastPkts_Type = Counter32
_IfInMulticastPkts_Object = MibTableColumn
ifInMulticastPkts = _IfInMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 2),
    _IfInMulticastPkts_Type()
)
ifInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInMulticastPkts.setStatus("mandatory")
_IfInBroadcastPkts_Type = Counter32
_IfInBroadcastPkts_Object = MibTableColumn
ifInBroadcastPkts = _IfInBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 3),
    _IfInBroadcastPkts_Type()
)
ifInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInBroadcastPkts.setStatus("mandatory")
_IfOutMulticastPkts_Type = Counter32
_IfOutMulticastPkts_Object = MibTableColumn
ifOutMulticastPkts = _IfOutMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 4),
    _IfOutMulticastPkts_Type()
)
ifOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutMulticastPkts.setStatus("mandatory")
_IfOutBroadcastPkts_Type = Counter32
_IfOutBroadcastPkts_Object = MibTableColumn
ifOutBroadcastPkts = _IfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 5),
    _IfOutBroadcastPkts_Type()
)
ifOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutBroadcastPkts.setStatus("mandatory")


class _IfHCInOctets_Type(OctetString):
    """Custom type ifHCInOctets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_IfHCInOctets_Type.__name__ = "OctetString"
_IfHCInOctets_Object = MibTableColumn
ifHCInOctets = _IfHCInOctets_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 6),
    _IfHCInOctets_Type()
)
ifHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCInOctets.setStatus("mandatory")


class _IfHCInUcastPkts_Type(OctetString):
    """Custom type ifHCInUcastPkts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_IfHCInUcastPkts_Type.__name__ = "OctetString"
_IfHCInUcastPkts_Object = MibTableColumn
ifHCInUcastPkts = _IfHCInUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 7),
    _IfHCInUcastPkts_Type()
)
ifHCInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCInUcastPkts.setStatus("mandatory")


class _IfHCInMulticastPkts_Type(OctetString):
    """Custom type ifHCInMulticastPkts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_IfHCInMulticastPkts_Type.__name__ = "OctetString"
_IfHCInMulticastPkts_Object = MibTableColumn
ifHCInMulticastPkts = _IfHCInMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 8),
    _IfHCInMulticastPkts_Type()
)
ifHCInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCInMulticastPkts.setStatus("mandatory")


class _IfHCInBroadcastPkts_Type(OctetString):
    """Custom type ifHCInBroadcastPkts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_IfHCInBroadcastPkts_Type.__name__ = "OctetString"
_IfHCInBroadcastPkts_Object = MibTableColumn
ifHCInBroadcastPkts = _IfHCInBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 9),
    _IfHCInBroadcastPkts_Type()
)
ifHCInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCInBroadcastPkts.setStatus("mandatory")


class _IfHCOutOctets_Type(OctetString):
    """Custom type ifHCOutOctets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_IfHCOutOctets_Type.__name__ = "OctetString"
_IfHCOutOctets_Object = MibTableColumn
ifHCOutOctets = _IfHCOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 10),
    _IfHCOutOctets_Type()
)
ifHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCOutOctets.setStatus("mandatory")


class _IfHCOutUcastPkts_Type(OctetString):
    """Custom type ifHCOutUcastPkts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_IfHCOutUcastPkts_Type.__name__ = "OctetString"
_IfHCOutUcastPkts_Object = MibTableColumn
ifHCOutUcastPkts = _IfHCOutUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 11),
    _IfHCOutUcastPkts_Type()
)
ifHCOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCOutUcastPkts.setStatus("mandatory")


class _IfHCOutMulticastPkts_Type(OctetString):
    """Custom type ifHCOutMulticastPkts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_IfHCOutMulticastPkts_Type.__name__ = "OctetString"
_IfHCOutMulticastPkts_Object = MibTableColumn
ifHCOutMulticastPkts = _IfHCOutMulticastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 12),
    _IfHCOutMulticastPkts_Type()
)
ifHCOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCOutMulticastPkts.setStatus("mandatory")


class _IfHCOutBroadcastPkts_Type(OctetString):
    """Custom type ifHCOutBroadcastPkts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_IfHCOutBroadcastPkts_Type.__name__ = "OctetString"
_IfHCOutBroadcastPkts_Object = MibTableColumn
ifHCOutBroadcastPkts = _IfHCOutBroadcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 13),
    _IfHCOutBroadcastPkts_Type()
)
ifHCOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCOutBroadcastPkts.setStatus("mandatory")


class _IfLinkUpDownTrapEnable_Type(Integer32):
    """Custom type ifLinkUpDownTrapEnable based on Integer32"""
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


_IfLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_IfLinkUpDownTrapEnable_Object = MibTableColumn
ifLinkUpDownTrapEnable = _IfLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 14),
    _IfLinkUpDownTrapEnable_Type()
)
ifLinkUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifLinkUpDownTrapEnable.setStatus("mandatory")
_IfHighSpeed_Type = Gauge32
_IfHighSpeed_Object = MibTableColumn
ifHighSpeed = _IfHighSpeed_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 15),
    _IfHighSpeed_Type()
)
ifHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHighSpeed.setStatus("mandatory")
_IfPromiscuousMode_Type = TruthValue
_IfPromiscuousMode_Object = MibTableColumn
ifPromiscuousMode = _IfPromiscuousMode_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 16),
    _IfPromiscuousMode_Type()
)
ifPromiscuousMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPromiscuousMode.setStatus("mandatory")
_IfConnectorPresent_Type = TruthValue
_IfConnectorPresent_Object = MibTableColumn
ifConnectorPresent = _IfConnectorPresent_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 17),
    _IfConnectorPresent_Type()
)
ifConnectorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifConnectorPresent.setStatus("mandatory")
_IfAlias_Type = DisplayString
_IfAlias_Object = MibTableColumn
ifAlias = _IfAlias_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 18),
    _IfAlias_Type()
)
ifAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAlias.setStatus("mandatory")
_IfCounterDiscontinuityTime_Type = Integer32
_IfCounterDiscontinuityTime_Object = MibTableColumn
ifCounterDiscontinuityTime = _IfCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 19),
    _IfCounterDiscontinuityTime_Type()
)
ifCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCounterDiscontinuityTime.setStatus("mandatory")
_IfStackTable_Object = MibTable
ifStackTable = _IfStackTable_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 2)
)
if mibBuilder.loadTexts:
    ifStackTable.setStatus("mandatory")
_IfStackEntry_Object = MibTableRow
ifStackEntry = _IfStackEntry_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 2, 1)
)
ifStackEntry.setIndexNames(
    (0, "ITF-MIB", "ifStackHigherLayer"),
    (0, "ITF-MIB", "ifStackLowerLayer"),
)
if mibBuilder.loadTexts:
    ifStackEntry.setStatus("mandatory")
_IfStackHigherLayer_Type = Integer32
_IfStackHigherLayer_Object = MibTableColumn
ifStackHigherLayer = _IfStackHigherLayer_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 2, 1, 1),
    _IfStackHigherLayer_Type()
)
ifStackHigherLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifStackHigherLayer.setStatus("mandatory")
_IfStackLowerLayer_Type = Integer32
_IfStackLowerLayer_Object = MibTableColumn
ifStackLowerLayer = _IfStackLowerLayer_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 2, 1, 2),
    _IfStackLowerLayer_Type()
)
ifStackLowerLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifStackLowerLayer.setStatus("mandatory")
_IfStackStatus_Type = RowStatus
_IfStackStatus_Object = MibTableColumn
ifStackStatus = _IfStackStatus_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 2, 1, 3),
    _IfStackStatus_Type()
)
ifStackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStackStatus.setStatus("mandatory")
_IfTestTable_Object = MibTable
ifTestTable = _IfTestTable_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3)
)
if mibBuilder.loadTexts:
    ifTestTable.setStatus("optional")
_IfTestEntry_Object = MibTableRow
ifTestEntry = _IfTestEntry_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1)
)
ifTestEntry.setIndexNames(
    (0, "ITF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifTestEntry.setStatus("optional")
_IfTestId_Type = TestAndIncr
_IfTestId_Object = MibTableColumn
ifTestId = _IfTestId_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 1),
    _IfTestId_Type()
)
ifTestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTestId.setStatus("optional")


class _IfTestStatus_Type(Integer32):
    """Custom type ifTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInUse", 1),
          ("inUse", 2))
    )


_IfTestStatus_Type.__name__ = "Integer32"
_IfTestStatus_Object = MibTableColumn
ifTestStatus = _IfTestStatus_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 2),
    _IfTestStatus_Type()
)
ifTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTestStatus.setStatus("optional")
_IfTestType_Type = AutonomousType
_IfTestType_Object = MibTableColumn
ifTestType = _IfTestType_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 3),
    _IfTestType_Type()
)
ifTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTestType.setStatus("optional")


class _IfTestResult_Type(Integer32):
    """Custom type ifTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("success", 2),
          ("inProgress", 3),
          ("notSupported", 4),
          ("unAbleToRun", 5),
          ("aborted", 6),
          ("failed", 7))
    )


_IfTestResult_Type.__name__ = "Integer32"
_IfTestResult_Object = MibTableColumn
ifTestResult = _IfTestResult_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 4),
    _IfTestResult_Type()
)
ifTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTestResult.setStatus("optional")
_IfTestCode_Type = ObjectIdentifier
_IfTestCode_Object = MibTableColumn
ifTestCode = _IfTestCode_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 5),
    _IfTestCode_Type()
)
ifTestCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTestCode.setStatus("optional")
_IfTestOwner_Type = OwnerString
_IfTestOwner_Object = MibTableColumn
ifTestOwner = _IfTestOwner_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 6),
    _IfTestOwner_Type()
)
ifTestOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTestOwner.setStatus("optional")
_IfRcvAddressTable_Object = MibTable
ifRcvAddressTable = _IfRcvAddressTable_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 4)
)
if mibBuilder.loadTexts:
    ifRcvAddressTable.setStatus("mandatory")
_IfRcvAddressEntry_Object = MibTableRow
ifRcvAddressEntry = _IfRcvAddressEntry_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 4, 1)
)
ifRcvAddressEntry.setIndexNames(
    (0, "ITF-MIB", "ifIndex"),
    (0, "ITF-MIB", "ifRcvAddressAddress"),
)
if mibBuilder.loadTexts:
    ifRcvAddressEntry.setStatus("mandatory")


class _IfRcvAddressAddress_Type(PhysAddress):
    """Custom type ifRcvAddressAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_IfRcvAddressAddress_Type.__name__ = "PhysAddress"
_IfRcvAddressAddress_Object = MibTableColumn
ifRcvAddressAddress = _IfRcvAddressAddress_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 4, 1, 1),
    _IfRcvAddressAddress_Type()
)
ifRcvAddressAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifRcvAddressAddress.setStatus("mandatory")
_IfRcvAddressStatus_Type = RowStatus
_IfRcvAddressStatus_Object = MibTableColumn
ifRcvAddressStatus = _IfRcvAddressStatus_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 4, 1, 2),
    _IfRcvAddressStatus_Type()
)
ifRcvAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifRcvAddressStatus.setStatus("mandatory")


class _IfRcvAddressType_Type(Integer32):
    """Custom type ifRcvAddressType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("volatile", 2),
          ("nonVolatile", 3))
    )


_IfRcvAddressType_Type.__name__ = "Integer32"
_IfRcvAddressType_Object = MibTableColumn
ifRcvAddressType = _IfRcvAddressType_Object(
    (1, 3, 6, 1, 2, 1, 31, 1, 4, 1, 3),
    _IfRcvAddressType_Type()
)
ifRcvAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifRcvAddressType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITF-MIB",
    **{"OwnerString": OwnerString,
       "InterfaceIndex": InterfaceIndex,
       "InterfaceIndexOrZero": InterfaceIndexOrZero,
       "ifNumber": ifNumber,
       "ifTable": ifTable,
       "ifEntry": ifEntry,
       "ifIndex": ifIndex,
       "ifDescr": ifDescr,
       "ifType": ifType,
       "ifMtu": ifMtu,
       "ifSpeed": ifSpeed,
       "ifPhysAddress": ifPhysAddress,
       "ifAdminStatus": ifAdminStatus,
       "ifOperStatus": ifOperStatus,
       "ifLastChange": ifLastChange,
       "ifInOctets": ifInOctets,
       "ifInUcastPkts": ifInUcastPkts,
       "ifInNUcastPkts": ifInNUcastPkts,
       "ifInDiscards": ifInDiscards,
       "ifInErrors": ifInErrors,
       "ifInUnknownProtos": ifInUnknownProtos,
       "ifOutOctets": ifOutOctets,
       "ifOutUcastPkts": ifOutUcastPkts,
       "ifOutNUcastPkts": ifOutNUcastPkts,
       "ifOutDiscards": ifOutDiscards,
       "ifOutErrors": ifOutErrors,
       "ifOutQLen": ifOutQLen,
       "ifSpecific": ifSpecific,
       "ifMIB": ifMIB,
       "ifMIBObjects": ifMIBObjects,
       "ifXTable": ifXTable,
       "ifXEntry": ifXEntry,
       "ifName": ifName,
       "ifInMulticastPkts": ifInMulticastPkts,
       "ifInBroadcastPkts": ifInBroadcastPkts,
       "ifOutMulticastPkts": ifOutMulticastPkts,
       "ifOutBroadcastPkts": ifOutBroadcastPkts,
       "ifHCInOctets": ifHCInOctets,
       "ifHCInUcastPkts": ifHCInUcastPkts,
       "ifHCInMulticastPkts": ifHCInMulticastPkts,
       "ifHCInBroadcastPkts": ifHCInBroadcastPkts,
       "ifHCOutOctets": ifHCOutOctets,
       "ifHCOutUcastPkts": ifHCOutUcastPkts,
       "ifHCOutMulticastPkts": ifHCOutMulticastPkts,
       "ifHCOutBroadcastPkts": ifHCOutBroadcastPkts,
       "ifLinkUpDownTrapEnable": ifLinkUpDownTrapEnable,
       "ifHighSpeed": ifHighSpeed,
       "ifPromiscuousMode": ifPromiscuousMode,
       "ifConnectorPresent": ifConnectorPresent,
       "ifAlias": ifAlias,
       "ifCounterDiscontinuityTime": ifCounterDiscontinuityTime,
       "ifStackTable": ifStackTable,
       "ifStackEntry": ifStackEntry,
       "ifStackHigherLayer": ifStackHigherLayer,
       "ifStackLowerLayer": ifStackLowerLayer,
       "ifStackStatus": ifStackStatus,
       "ifTestTable": ifTestTable,
       "ifTestEntry": ifTestEntry,
       "ifTestId": ifTestId,
       "ifTestStatus": ifTestStatus,
       "ifTestType": ifTestType,
       "ifTestResult": ifTestResult,
       "ifTestCode": ifTestCode,
       "ifTestOwner": ifTestOwner,
       "ifRcvAddressTable": ifRcvAddressTable,
       "ifRcvAddressEntry": ifRcvAddressEntry,
       "ifRcvAddressAddress": ifRcvAddressAddress,
       "ifRcvAddressStatus": ifRcvAddressStatus,
       "ifRcvAddressType": ifRcvAddressType}
)
