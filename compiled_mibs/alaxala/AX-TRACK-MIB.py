# SNMP MIB module (AX-TRACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-TRACK-MIB

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

(axMib,) = mibBuilder.importSymbols(
    "AX-SMI-MIB",
    "axMib")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

axTrack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40)
)
if mibBuilder.loadTexts:
    axTrack.setRevisions(
        ("2017-01-25 00:01",
         "2014-03-12 00:01")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxTrackGeneralGroup_ObjectIdentity = ObjectIdentity
axTrackGeneralGroup = _AxTrackGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 1)
)
_AxTrackGeneralLastChange_Type = TimeTicks
_AxTrackGeneralLastChange_Object = MibScalar
axTrackGeneralLastChange = _AxTrackGeneralLastChange_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 1, 1),
    _AxTrackGeneralLastChange_Type()
)
axTrackGeneralLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTrackGeneralLastChange.setStatus("current")
_AxTrackTraps_ObjectIdentity = ObjectIdentity
axTrackTraps = _AxTrackTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 2)
)
_AxTrackTrapsPrefix_ObjectIdentity = ObjectIdentity
axTrackTrapsPrefix = _AxTrackTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 2, 0)
)
_AxTrackTable_Object = MibTable
axTrackTable = _AxTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 3)
)
if mibBuilder.loadTexts:
    axTrackTable.setStatus("current")
_AxTrackEntry_Object = MibTableRow
axTrackEntry = _AxTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 3, 1)
)
axTrackEntry.setIndexNames(
    (0, "AX-TRACK-MIB", "axTrackId"),
)
if mibBuilder.loadTexts:
    axTrackEntry.setStatus("current")
_AxTrackId_Type = Integer32
_AxTrackId_Object = MibTableColumn
axTrackId = _AxTrackId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 3, 1, 1),
    _AxTrackId_Type()
)
axTrackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTrackId.setStatus("current")
_AxTrackName_Type = OctetString
_AxTrackName_Object = MibTableColumn
axTrackName = _AxTrackName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 3, 1, 2),
    _AxTrackName_Type()
)
axTrackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTrackName.setStatus("current")


class _AxTrackState_Type(Integer32):
    """Custom type axTrackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AxTrackState_Type.__name__ = "Integer32"
_AxTrackState_Object = MibTableColumn
axTrackState = _AxTrackState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 3, 1, 3),
    _AxTrackState_Type()
)
axTrackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTrackState.setStatus("current")


class _AxTrackOperation_Type(Integer32):
    """Custom type axTrackOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2),
          ("disable", 3))
    )


_AxTrackOperation_Type.__name__ = "Integer32"
_AxTrackOperation_Object = MibTableColumn
axTrackOperation = _AxTrackOperation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 3, 1, 4),
    _AxTrackOperation_Type()
)
axTrackOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTrackOperation.setStatus("current")


class _AxTrackType_Type(Integer32):
    """Custom type axTrackType based on Integer32"""
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
        *(("bfd", 1),
          ("icmp", 2),
          ("interface", 3),
          ("list", 4))
    )


_AxTrackType_Type.__name__ = "Integer32"
_AxTrackType_Object = MibTableColumn
axTrackType = _AxTrackType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 3, 1, 5),
    _AxTrackType_Type()
)
axTrackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTrackType.setStatus("current")


class _AxTrackListType_Type(Integer32):
    """Custom type axTrackListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("and", 1),
          ("or", 2))
    )


_AxTrackListType_Type.__name__ = "Integer32"
_AxTrackListType_Object = MibTableColumn
axTrackListType = _AxTrackListType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 3, 1, 6),
    _AxTrackListType_Type()
)
axTrackListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTrackListType.setStatus("current")
_AxTrackVrfIndex_Type = Integer32
_AxTrackVrfIndex_Object = MibTableColumn
axTrackVrfIndex = _AxTrackVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 3, 1, 7),
    _AxTrackVrfIndex_Type()
)
axTrackVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTrackVrfIndex.setStatus("current")
_AxTrackAddressType_Type = InetAddressType
_AxTrackAddressType_Object = MibTableColumn
axTrackAddressType = _AxTrackAddressType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 3, 1, 8),
    _AxTrackAddressType_Type()
)
axTrackAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTrackAddressType.setStatus("current")
_AxTrackAddress_Type = InetAddress
_AxTrackAddress_Object = MibTableColumn
axTrackAddress = _AxTrackAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 3, 1, 9),
    _AxTrackAddress_Type()
)
axTrackAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTrackAddress.setStatus("current")
_AxTrackIfIndex_Type = InterfaceIndexOrZero
_AxTrackIfIndex_Object = MibTableColumn
axTrackIfIndex = _AxTrackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 3, 1, 10),
    _AxTrackIfIndex_Type()
)
axTrackIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTrackIfIndex.setStatus("current")
_AxTrackConformance_ObjectIdentity = ObjectIdentity
axTrackConformance = _AxTrackConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 1000)
)
_AxTrackCompliances_ObjectIdentity = ObjectIdentity
axTrackCompliances = _AxTrackCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 1000, 1)
)
_AxTrackGroups_ObjectIdentity = ObjectIdentity
axTrackGroups = _AxTrackGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 1000, 2)
)

# Managed Objects groups

axTrackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 1000, 2, 1)
)
axTrackGroup.setObjects(
      *(("AX-TRACK-MIB", "axTrackGeneralLastChange"),
        ("AX-TRACK-MIB", "axTrackId"),
        ("AX-TRACK-MIB", "axTrackName"),
        ("AX-TRACK-MIB", "axTrackState"),
        ("AX-TRACK-MIB", "axTrackOperation"),
        ("AX-TRACK-MIB", "axTrackType"),
        ("AX-TRACK-MIB", "axTrackListType"),
        ("AX-TRACK-MIB", "axTrackVrfIndex"),
        ("AX-TRACK-MIB", "axTrackAddressType"),
        ("AX-TRACK-MIB", "axTrackAddress"),
        ("AX-TRACK-MIB", "axTrackIfIndex"))
)
if mibBuilder.loadTexts:
    axTrackGroup.setStatus("current")


# Notification objects

axTrackStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 2, 0, 1)
)
axTrackStateUp.setObjects(
      *(("AX-TRACK-MIB", "axTrackId"),
        ("AX-TRACK-MIB", "axTrackName"),
        ("AX-TRACK-MIB", "axTrackState"),
        ("AX-TRACK-MIB", "axTrackOperation"),
        ("AX-TRACK-MIB", "axTrackType"),
        ("AX-TRACK-MIB", "axTrackListType"),
        ("AX-TRACK-MIB", "axTrackVrfIndex"),
        ("AX-TRACK-MIB", "axTrackAddressType"),
        ("AX-TRACK-MIB", "axTrackAddress"),
        ("AX-TRACK-MIB", "axTrackIfIndex"))
)
if mibBuilder.loadTexts:
    axTrackStateUp.setStatus(
        "current"
    )

axTrackStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 2, 0, 2)
)
axTrackStateDown.setObjects(
      *(("AX-TRACK-MIB", "axTrackId"),
        ("AX-TRACK-MIB", "axTrackName"),
        ("AX-TRACK-MIB", "axTrackState"),
        ("AX-TRACK-MIB", "axTrackOperation"),
        ("AX-TRACK-MIB", "axTrackType"),
        ("AX-TRACK-MIB", "axTrackListType"),
        ("AX-TRACK-MIB", "axTrackVrfIndex"),
        ("AX-TRACK-MIB", "axTrackAddressType"),
        ("AX-TRACK-MIB", "axTrackAddress"),
        ("AX-TRACK-MIB", "axTrackIfIndex"))
)
if mibBuilder.loadTexts:
    axTrackStateDown.setStatus(
        "current"
    )


# Notifications groups

axTrackNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 1000, 2, 10)
)
axTrackNotificationGroup.setObjects(
      *(("AX-TRACK-MIB", "axTrackStateUp"),
        ("AX-TRACK-MIB", "axTrackStateDown"))
)
if mibBuilder.loadTexts:
    axTrackNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

axTrackCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 40, 1000, 1, 1)
)
axTrackCompliance.setObjects(
      *(("AX-TRACK-MIB", "axTrackGroup"),
        ("AX-TRACK-MIB", "axTrackNotificationGroup"))
)
if mibBuilder.loadTexts:
    axTrackCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-TRACK-MIB",
    **{"axTrack": axTrack,
       "axTrackGeneralGroup": axTrackGeneralGroup,
       "axTrackGeneralLastChange": axTrackGeneralLastChange,
       "axTrackTraps": axTrackTraps,
       "axTrackTrapsPrefix": axTrackTrapsPrefix,
       "axTrackStateUp": axTrackStateUp,
       "axTrackStateDown": axTrackStateDown,
       "axTrackTable": axTrackTable,
       "axTrackEntry": axTrackEntry,
       "axTrackId": axTrackId,
       "axTrackName": axTrackName,
       "axTrackState": axTrackState,
       "axTrackOperation": axTrackOperation,
       "axTrackType": axTrackType,
       "axTrackListType": axTrackListType,
       "axTrackVrfIndex": axTrackVrfIndex,
       "axTrackAddressType": axTrackAddressType,
       "axTrackAddress": axTrackAddress,
       "axTrackIfIndex": axTrackIfIndex,
       "axTrackConformance": axTrackConformance,
       "axTrackCompliances": axTrackCompliances,
       "axTrackCompliance": axTrackCompliance,
       "axTrackGroups": axTrackGroups,
       "axTrackGroup": axTrackGroup,
       "axTrackNotificationGroup": axTrackNotificationGroup}
)
