# SNMP MIB module (HH3C-LLDP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-LLDP-EXT-MIB

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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(LldpManAddrIfSubtype,
 LldpPortNumber,
 lldpRemIndex,
 lldpRemLocalPortNum,
 lldpRemManAddr,
 lldpRemManAddrSubtype,
 lldpRemTimeMark) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpManAddrIfSubtype",
    "LldpPortNumber",
    "lldpRemIndex",
    "lldpRemLocalPortNum",
    "lldpRemManAddr",
    "lldpRemManAddrSubtype",
    "lldpRemTimeMark")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3clldp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100)
)
if mibBuilder.loadTexts:
    hh3clldp.setRevisions(
        ("2019-09-17 00:00",
         "2019-03-07 00:00",
         "2015-09-01 00:00",
         "2009-03-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3clldpObjects_ObjectIdentity = ObjectIdentity
hh3clldpObjects = _Hh3clldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1)
)
_Hh3clldpConfiguration_ObjectIdentity = ObjectIdentity
hh3clldpConfiguration = _Hh3clldpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1)
)
_Hh3clldpAdminStatus_Type = TruthValue
_Hh3clldpAdminStatus_Object = MibScalar
hh3clldpAdminStatus = _Hh3clldpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 1),
    _Hh3clldpAdminStatus_Type()
)
hh3clldpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3clldpAdminStatus.setStatus("current")
_Hh3clldpComplianceCDPStatus_Type = TruthValue
_Hh3clldpComplianceCDPStatus_Object = MibScalar
hh3clldpComplianceCDPStatus = _Hh3clldpComplianceCDPStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 2),
    _Hh3clldpComplianceCDPStatus_Type()
)
hh3clldpComplianceCDPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3clldpComplianceCDPStatus.setStatus("current")
_Hh3clldpPortConfigTable_Object = MibTable
hh3clldpPortConfigTable = _Hh3clldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3clldpPortConfigTable.setStatus("current")
_Hh3clldpPortConfigEntry_Object = MibTableRow
hh3clldpPortConfigEntry = _Hh3clldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 3, 1)
)
hh3clldpPortConfigEntry.setIndexNames(
    (0, "HH3C-LLDP-EXT-MIB", "hh3clldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    hh3clldpPortConfigEntry.setStatus("current")
_Hh3clldpPortConfigPortNum_Type = LldpPortNumber
_Hh3clldpPortConfigPortNum_Object = MibTableColumn
hh3clldpPortConfigPortNum = _Hh3clldpPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 3, 1, 1),
    _Hh3clldpPortConfigPortNum_Type()
)
hh3clldpPortConfigPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3clldpPortConfigPortNum.setStatus("current")


class _Hh3clldpPortConfigCDPComplianceStatus_Type(Integer32):
    """Custom type hh3clldpPortConfigCDPComplianceStatus based on Integer32"""
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
        *(("txAndRx", 1),
          ("disabled", 2),
          ("rx", 3))
    )


_Hh3clldpPortConfigCDPComplianceStatus_Type.__name__ = "Integer32"
_Hh3clldpPortConfigCDPComplianceStatus_Object = MibTableColumn
hh3clldpPortConfigCDPComplianceStatus = _Hh3clldpPortConfigCDPComplianceStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 3, 1, 2),
    _Hh3clldpPortConfigCDPComplianceStatus_Type()
)
hh3clldpPortConfigCDPComplianceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3clldpPortConfigCDPComplianceStatus.setStatus("current")
_Hh3clldpPortConfigValidationAction_Type = Integer32
_Hh3clldpPortConfigValidationAction_Object = MibTableColumn
hh3clldpPortConfigValidationAction = _Hh3clldpPortConfigValidationAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 3, 1, 3),
    _Hh3clldpPortConfigValidationAction_Type()
)
hh3clldpPortConfigValidationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3clldpPortConfigValidationAction.setStatus("current")
_Hh3clldpPortConfigAgingAction_Type = Integer32
_Hh3clldpPortConfigAgingAction_Object = MibTableColumn
hh3clldpPortConfigAgingAction = _Hh3clldpPortConfigAgingAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 3, 1, 4),
    _Hh3clldpPortConfigAgingAction_Type()
)
hh3clldpPortConfigAgingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3clldpPortConfigAgingAction.setStatus("current")
_Hh3clldpNbIdentityTable_Object = MibTable
hh3clldpNbIdentityTable = _Hh3clldpNbIdentityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hh3clldpNbIdentityTable.setStatus("current")
_Hh3clldpNbIdentityEntry_Object = MibTableRow
hh3clldpNbIdentityEntry = _Hh3clldpNbIdentityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 4, 1)
)
hh3clldpNbIdentityEntry.setIndexNames(
    (0, "HH3C-LLDP-EXT-MIB", "hh3clldpNbIdentityPortNum"),
)
if mibBuilder.loadTexts:
    hh3clldpNbIdentityEntry.setStatus("current")
_Hh3clldpNbIdentityPortNum_Type = LldpPortNumber
_Hh3clldpNbIdentityPortNum_Object = MibTableColumn
hh3clldpNbIdentityPortNum = _Hh3clldpNbIdentityPortNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 4, 1, 1),
    _Hh3clldpNbIdentityPortNum_Type()
)
hh3clldpNbIdentityPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3clldpNbIdentityPortNum.setStatus("current")


class _Hh3clldpNbIdentityChassisIDSubtype_Type(Integer32):
    """Custom type hh3clldpNbIdentityChassisIDSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("portComponent", 3),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("interfaceName", 6),
          ("local", 7))
    )


_Hh3clldpNbIdentityChassisIDSubtype_Type.__name__ = "Integer32"
_Hh3clldpNbIdentityChassisIDSubtype_Object = MibTableColumn
hh3clldpNbIdentityChassisIDSubtype = _Hh3clldpNbIdentityChassisIDSubtype_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 4, 1, 2),
    _Hh3clldpNbIdentityChassisIDSubtype_Type()
)
hh3clldpNbIdentityChassisIDSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3clldpNbIdentityChassisIDSubtype.setStatus("current")


class _Hh3clldpNbIdentityChassisID_Type(OctetString):
    """Custom type hh3clldpNbIdentityChassisID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3clldpNbIdentityChassisID_Type.__name__ = "OctetString"
_Hh3clldpNbIdentityChassisID_Object = MibTableColumn
hh3clldpNbIdentityChassisID = _Hh3clldpNbIdentityChassisID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 4, 1, 3),
    _Hh3clldpNbIdentityChassisID_Type()
)
hh3clldpNbIdentityChassisID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3clldpNbIdentityChassisID.setStatus("current")


class _Hh3clldpNbIdentityPortIDSubtype_Type(Integer32):
    """Custom type hh3clldpNbIdentityPortIDSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("interfaceAlias", 1),
          ("portComponent", 2),
          ("macAddress", 3),
          ("networkAddress", 4),
          ("interfaceName", 5),
          ("agentCircuitId", 6),
          ("local", 7))
    )


_Hh3clldpNbIdentityPortIDSubtype_Type.__name__ = "Integer32"
_Hh3clldpNbIdentityPortIDSubtype_Object = MibTableColumn
hh3clldpNbIdentityPortIDSubtype = _Hh3clldpNbIdentityPortIDSubtype_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 4, 1, 4),
    _Hh3clldpNbIdentityPortIDSubtype_Type()
)
hh3clldpNbIdentityPortIDSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3clldpNbIdentityPortIDSubtype.setStatus("current")


class _Hh3clldpNbIdentityPortID_Type(OctetString):
    """Custom type hh3clldpNbIdentityPortID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3clldpNbIdentityPortID_Type.__name__ = "OctetString"
_Hh3clldpNbIdentityPortID_Object = MibTableColumn
hh3clldpNbIdentityPortID = _Hh3clldpNbIdentityPortID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 4, 1, 5),
    _Hh3clldpNbIdentityPortID_Type()
)
hh3clldpNbIdentityPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3clldpNbIdentityPortID.setStatus("current")
_Hh3clldpNbIdentityRowStatus_Type = RowStatus
_Hh3clldpNbIdentityRowStatus_Object = MibTableColumn
hh3clldpNbIdentityRowStatus = _Hh3clldpNbIdentityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 4, 1, 6),
    _Hh3clldpNbIdentityRowStatus_Type()
)
hh3clldpNbIdentityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3clldpNbIdentityRowStatus.setStatus("current")
_Hh3clldpPortStatusTable_Object = MibTable
hh3clldpPortStatusTable = _Hh3clldpPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hh3clldpPortStatusTable.setStatus("current")
_Hh3clldpPortStatusEntry_Object = MibTableRow
hh3clldpPortStatusEntry = _Hh3clldpPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 5, 1)
)
hh3clldpPortStatusEntry.setIndexNames(
    (0, "HH3C-LLDP-EXT-MIB", "hh3clldpPortStatusPortNum"),
)
if mibBuilder.loadTexts:
    hh3clldpPortStatusEntry.setStatus("current")
_Hh3clldpPortStatusPortNum_Type = LldpPortNumber
_Hh3clldpPortStatusPortNum_Object = MibTableColumn
hh3clldpPortStatusPortNum = _Hh3clldpPortStatusPortNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 5, 1, 1),
    _Hh3clldpPortStatusPortNum_Type()
)
hh3clldpPortStatusPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3clldpPortStatusPortNum.setStatus("current")
_Hh3clldpPortValidationStatus_Type = Integer32
_Hh3clldpPortValidationStatus_Object = MibTableColumn
hh3clldpPortValidationStatus = _Hh3clldpPortValidationStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 5, 1, 2),
    _Hh3clldpPortValidationStatus_Type()
)
hh3clldpPortValidationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3clldpPortValidationStatus.setStatus("current")
_Hh3clldpPortAgingStatus_Type = Integer32
_Hh3clldpPortAgingStatus_Object = MibTableColumn
hh3clldpPortAgingStatus = _Hh3clldpPortAgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 5, 1, 3),
    _Hh3clldpPortAgingStatus_Type()
)
hh3clldpPortAgingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3clldpPortAgingStatus.setStatus("current")
_Hh3clldpRemoteSystemsData_ObjectIdentity = ObjectIdentity
hh3clldpRemoteSystemsData = _Hh3clldpRemoteSystemsData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 2)
)
_Hh3clldpRemManAddrTable_Object = MibTable
hh3clldpRemManAddrTable = _Hh3clldpRemManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3clldpRemManAddrTable.setStatus("current")
_Hh3clldpRemManAddrEntry_Object = MibTableRow
hh3clldpRemManAddrEntry = _Hh3clldpRemManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 2, 1, 1)
)
hh3clldpRemManAddrEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
    (0, "LLDP-MIB", "lldpRemManAddrSubtype"),
    (0, "LLDP-MIB", "lldpRemManAddr"),
)
if mibBuilder.loadTexts:
    hh3clldpRemManAddrEntry.setStatus("current")
_Hh3clldpRemManAddrSubtype_Type = AddressFamilyNumbers
_Hh3clldpRemManAddrSubtype_Object = MibTableColumn
hh3clldpRemManAddrSubtype = _Hh3clldpRemManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 2, 1, 1, 1),
    _Hh3clldpRemManAddrSubtype_Type()
)
hh3clldpRemManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3clldpRemManAddrSubtype.setStatus("current")


class _Hh3clldpRemManAddr_Type(OctetString):
    """Custom type hh3clldpRemManAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3clldpRemManAddr_Type.__name__ = "OctetString"
_Hh3clldpRemManAddr_Object = MibTableColumn
hh3clldpRemManAddr = _Hh3clldpRemManAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 2, 1, 1, 2),
    _Hh3clldpRemManAddr_Type()
)
hh3clldpRemManAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3clldpRemManAddr.setStatus("current")
_Hh3clldpRemManAddrIfSubtype_Type = LldpManAddrIfSubtype
_Hh3clldpRemManAddrIfSubtype_Object = MibTableColumn
hh3clldpRemManAddrIfSubtype = _Hh3clldpRemManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 2, 1, 1, 3),
    _Hh3clldpRemManAddrIfSubtype_Type()
)
hh3clldpRemManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3clldpRemManAddrIfSubtype.setStatus("current")
_Hh3clldpRemManAddrIfId_Type = Integer32
_Hh3clldpRemManAddrIfId_Object = MibTableColumn
hh3clldpRemManAddrIfId = _Hh3clldpRemManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 2, 1, 1, 4),
    _Hh3clldpRemManAddrIfId_Type()
)
hh3clldpRemManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3clldpRemManAddrIfId.setStatus("current")
_Hh3clldpRemManAddrOID_Type = ObjectIdentifier
_Hh3clldpRemManAddrOID_Object = MibTableColumn
hh3clldpRemManAddrOID = _Hh3clldpRemManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 2, 1, 1, 5),
    _Hh3clldpRemManAddrOID_Type()
)
hh3clldpRemManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3clldpRemManAddrOID.setStatus("current")
_Hh3clldpNotifications_ObjectIdentity = ObjectIdentity
hh3clldpNotifications = _Hh3clldpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 2)
)
_Hh3clldpPortStatusTrap_ObjectIdentity = ObjectIdentity
hh3clldpPortStatusTrap = _Hh3clldpPortStatusTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3clldpValidationStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 2, 0, 1)
)
hh3clldpValidationStatusChange.setObjects(
      *(("HH3C-LLDP-EXT-MIB", "hh3clldpPortStatusPortNum"),
        ("HH3C-LLDP-EXT-MIB", "hh3clldpPortValidationStatus"))
)
if mibBuilder.loadTexts:
    hh3clldpValidationStatusChange.setStatus(
        "current"
    )

hh3clldpAgingStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 2, 0, 2)
)
hh3clldpAgingStatusChange.setObjects(
      *(("HH3C-LLDP-EXT-MIB", "hh3clldpPortStatusPortNum"),
        ("HH3C-LLDP-EXT-MIB", "hh3clldpPortAgingStatus"))
)
if mibBuilder.loadTexts:
    hh3clldpAgingStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LLDP-EXT-MIB",
    **{"hh3clldp": hh3clldp,
       "hh3clldpObjects": hh3clldpObjects,
       "hh3clldpConfiguration": hh3clldpConfiguration,
       "hh3clldpAdminStatus": hh3clldpAdminStatus,
       "hh3clldpComplianceCDPStatus": hh3clldpComplianceCDPStatus,
       "hh3clldpPortConfigTable": hh3clldpPortConfigTable,
       "hh3clldpPortConfigEntry": hh3clldpPortConfigEntry,
       "hh3clldpPortConfigPortNum": hh3clldpPortConfigPortNum,
       "hh3clldpPortConfigCDPComplianceStatus": hh3clldpPortConfigCDPComplianceStatus,
       "hh3clldpPortConfigValidationAction": hh3clldpPortConfigValidationAction,
       "hh3clldpPortConfigAgingAction": hh3clldpPortConfigAgingAction,
       "hh3clldpNbIdentityTable": hh3clldpNbIdentityTable,
       "hh3clldpNbIdentityEntry": hh3clldpNbIdentityEntry,
       "hh3clldpNbIdentityPortNum": hh3clldpNbIdentityPortNum,
       "hh3clldpNbIdentityChassisIDSubtype": hh3clldpNbIdentityChassisIDSubtype,
       "hh3clldpNbIdentityChassisID": hh3clldpNbIdentityChassisID,
       "hh3clldpNbIdentityPortIDSubtype": hh3clldpNbIdentityPortIDSubtype,
       "hh3clldpNbIdentityPortID": hh3clldpNbIdentityPortID,
       "hh3clldpNbIdentityRowStatus": hh3clldpNbIdentityRowStatus,
       "hh3clldpPortStatusTable": hh3clldpPortStatusTable,
       "hh3clldpPortStatusEntry": hh3clldpPortStatusEntry,
       "hh3clldpPortStatusPortNum": hh3clldpPortStatusPortNum,
       "hh3clldpPortValidationStatus": hh3clldpPortValidationStatus,
       "hh3clldpPortAgingStatus": hh3clldpPortAgingStatus,
       "hh3clldpRemoteSystemsData": hh3clldpRemoteSystemsData,
       "hh3clldpRemManAddrTable": hh3clldpRemManAddrTable,
       "hh3clldpRemManAddrEntry": hh3clldpRemManAddrEntry,
       "hh3clldpRemManAddrSubtype": hh3clldpRemManAddrSubtype,
       "hh3clldpRemManAddr": hh3clldpRemManAddr,
       "hh3clldpRemManAddrIfSubtype": hh3clldpRemManAddrIfSubtype,
       "hh3clldpRemManAddrIfId": hh3clldpRemManAddrIfId,
       "hh3clldpRemManAddrOID": hh3clldpRemManAddrOID,
       "hh3clldpNotifications": hh3clldpNotifications,
       "hh3clldpPortStatusTrap": hh3clldpPortStatusTrap,
       "hh3clldpValidationStatusChange": hh3clldpValidationStatusChange,
       "hh3clldpAgingStatusChange": hh3clldpAgingStatusChange}
)
