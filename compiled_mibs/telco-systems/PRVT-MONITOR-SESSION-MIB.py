# SNMP MIB module (PRVT-MONITOR-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-MONITOR-SESSION-MIB

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

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

prvtMonitorSessionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000)
)
if mibBuilder.loadTexts:
    prvtMonitorSessionMib.setRevisions(
        ("2011-05-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Direction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2))
    )



# MIB Managed Objects in the order of their OIDs

_PrvtMonitorSessionNotification_ObjectIdentity = ObjectIdentity
prvtMonitorSessionNotification = _PrvtMonitorSessionNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 0)
)
_PrvtMonitorSessionObjects_ObjectIdentity = ObjectIdentity
prvtMonitorSessionObjects = _PrvtMonitorSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1)
)
_PrvtMonitorSessionTable_Object = MibTable
prvtMonitorSessionTable = _PrvtMonitorSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 1)
)
if mibBuilder.loadTexts:
    prvtMonitorSessionTable.setStatus("current")
_PrvtMonitorSessionEntry_Object = MibTableRow
prvtMonitorSessionEntry = _PrvtMonitorSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 1, 1)
)
prvtMonitorSessionEntry.setIndexNames(
    (0, "PRVT-MONITOR-SESSION-MIB", "prvtMonitorSessionDirection"),
)
if mibBuilder.loadTexts:
    prvtMonitorSessionEntry.setStatus("current")
_PrvtMonitorSessionDirection_Type = Direction
_PrvtMonitorSessionDirection_Object = MibTableColumn
prvtMonitorSessionDirection = _PrvtMonitorSessionDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 1, 1, 1),
    _PrvtMonitorSessionDirection_Type()
)
prvtMonitorSessionDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtMonitorSessionDirection.setStatus("current")
_PrvtMonitorSessionSource_Type = PortList
_PrvtMonitorSessionSource_Object = MibTableColumn
prvtMonitorSessionSource = _PrvtMonitorSessionSource_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 1, 1, 2),
    _PrvtMonitorSessionSource_Type()
)
prvtMonitorSessionSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtMonitorSessionSource.setStatus("current")
_PrvtMonitorSessionDestination_Type = Integer32
_PrvtMonitorSessionDestination_Object = MibTableColumn
prvtMonitorSessionDestination = _PrvtMonitorSessionDestination_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 1, 1, 3),
    _PrvtMonitorSessionDestination_Type()
)
prvtMonitorSessionDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtMonitorSessionDestination.setStatus("current")
_PrvtAnalyzerVLANTagTable_Object = MibTable
prvtAnalyzerVLANTagTable = _PrvtAnalyzerVLANTagTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 2)
)
if mibBuilder.loadTexts:
    prvtAnalyzerVLANTagTable.setStatus("current")
_PrvtAnalyzerVLANTagEntry_Object = MibTableRow
prvtAnalyzerVLANTagEntry = _PrvtAnalyzerVLANTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 2, 1)
)
prvtAnalyzerVLANTagEntry.setIndexNames(
    (0, "PRVT-MONITOR-SESSION-MIB", "prvtMonitorSessionDirection"),
)
if mibBuilder.loadTexts:
    prvtAnalyzerVLANTagEntry.setStatus("current")


class _PrvtAnalyzerVLANTagEnable_Type(Integer32):
    """Custom type prvtAnalyzerVLANTagEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PrvtAnalyzerVLANTagEnable_Type.__name__ = "Integer32"
_PrvtAnalyzerVLANTagEnable_Object = MibTableColumn
prvtAnalyzerVLANTagEnable = _PrvtAnalyzerVLANTagEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 2, 1, 1),
    _PrvtAnalyzerVLANTagEnable_Type()
)
prvtAnalyzerVLANTagEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtAnalyzerVLANTagEnable.setStatus("current")


class _PrvtAnalyzerVLANTagVID_Type(Integer32):
    """Custom type prvtAnalyzerVLANTagVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_PrvtAnalyzerVLANTagVID_Type.__name__ = "Integer32"
_PrvtAnalyzerVLANTagVID_Object = MibTableColumn
prvtAnalyzerVLANTagVID = _PrvtAnalyzerVLANTagVID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 2, 1, 2),
    _PrvtAnalyzerVLANTagVID_Type()
)
prvtAnalyzerVLANTagVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtAnalyzerVLANTagVID.setStatus("current")
_PrvtAnalyzerVLANTagEtherType_Type = DisplayString
_PrvtAnalyzerVLANTagEtherType_Object = MibTableColumn
prvtAnalyzerVLANTagEtherType = _PrvtAnalyzerVLANTagEtherType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 2, 1, 3),
    _PrvtAnalyzerVLANTagEtherType_Type()
)
prvtAnalyzerVLANTagEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtAnalyzerVLANTagEtherType.setStatus("current")


class _PrvtAnalyzerVLANTagCFI_Type(Integer32):
    """Custom type prvtAnalyzerVLANTagCFI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("set", 1))
    )


_PrvtAnalyzerVLANTagCFI_Type.__name__ = "Integer32"
_PrvtAnalyzerVLANTagCFI_Object = MibTableColumn
prvtAnalyzerVLANTagCFI = _PrvtAnalyzerVLANTagCFI_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 2, 1, 4),
    _PrvtAnalyzerVLANTagCFI_Type()
)
prvtAnalyzerVLANTagCFI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtAnalyzerVLANTagCFI.setStatus("current")


class _PrvtAnalyzerVLANTagVPT_Type(Integer32):
    """Custom type prvtAnalyzerVLANTagVPT based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("vpt-value0", 0),
          ("vpt-value1", 1),
          ("vpt-value2", 2),
          ("vpt-value3", 3),
          ("vpt-value4", 4),
          ("vpt-value5", 5),
          ("vpt-value6", 6),
          ("vpt-value7", 7),
          ("undefined", 8))
    )


_PrvtAnalyzerVLANTagVPT_Type.__name__ = "Integer32"
_PrvtAnalyzerVLANTagVPT_Object = MibTableColumn
prvtAnalyzerVLANTagVPT = _PrvtAnalyzerVLANTagVPT_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 1, 2, 1, 5),
    _PrvtAnalyzerVLANTagVPT_Type()
)
prvtAnalyzerVLANTagVPT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtAnalyzerVLANTagVPT.setStatus("current")
_PrvtMonitorSessionConformance_ObjectIdentity = ObjectIdentity
prvtMonitorSessionConformance = _PrvtMonitorSessionConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 2)
)
_PrvtMonitorSessionCompliances_ObjectIdentity = ObjectIdentity
prvtMonitorSessionCompliances = _PrvtMonitorSessionCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 2, 1)
)
_PrvtMonitorSessionGroups_ObjectIdentity = ObjectIdentity
prvtMonitorSessionGroups = _PrvtMonitorSessionGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 2, 2)
)

# Managed Objects groups

prvtMonitorSessionMirroredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 2, 2, 1)
)
prvtMonitorSessionMirroredGroup.setObjects(
    ("PRVT-MONITOR-SESSION-MIB", "prvtMonitorSessionSource")
)
if mibBuilder.loadTexts:
    prvtMonitorSessionMirroredGroup.setStatus("current")

prvtMonitorSessionAnalyzerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 2, 2, 2)
)
prvtMonitorSessionAnalyzerGroup.setObjects(
      *(("PRVT-MONITOR-SESSION-MIB", "prvtMonitorSessionDestination"),
        ("PRVT-MONITOR-SESSION-MIB", "prvtAnalyzerVLANTagEnable"))
)
if mibBuilder.loadTexts:
    prvtMonitorSessionAnalyzerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

prvtMonitorSessionCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 1000, 2, 1, 1)
)
prvtMonitorSessionCompliance.setObjects(
      *(("PRVT-MONITOR-SESSION-MIB", "prvtMonitorSessionMirroredGroup"),
        ("PRVT-MONITOR-SESSION-MIB", "prvtMonitorSessionAnalyzerGroup"))
)
if mibBuilder.loadTexts:
    prvtMonitorSessionCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-MONITOR-SESSION-MIB",
    **{"Direction": Direction,
       "prvtMonitorSessionMib": prvtMonitorSessionMib,
       "prvtMonitorSessionNotification": prvtMonitorSessionNotification,
       "prvtMonitorSessionObjects": prvtMonitorSessionObjects,
       "prvtMonitorSessionTable": prvtMonitorSessionTable,
       "prvtMonitorSessionEntry": prvtMonitorSessionEntry,
       "prvtMonitorSessionDirection": prvtMonitorSessionDirection,
       "prvtMonitorSessionSource": prvtMonitorSessionSource,
       "prvtMonitorSessionDestination": prvtMonitorSessionDestination,
       "prvtAnalyzerVLANTagTable": prvtAnalyzerVLANTagTable,
       "prvtAnalyzerVLANTagEntry": prvtAnalyzerVLANTagEntry,
       "prvtAnalyzerVLANTagEnable": prvtAnalyzerVLANTagEnable,
       "prvtAnalyzerVLANTagVID": prvtAnalyzerVLANTagVID,
       "prvtAnalyzerVLANTagEtherType": prvtAnalyzerVLANTagEtherType,
       "prvtAnalyzerVLANTagCFI": prvtAnalyzerVLANTagCFI,
       "prvtAnalyzerVLANTagVPT": prvtAnalyzerVLANTagVPT,
       "prvtMonitorSessionConformance": prvtMonitorSessionConformance,
       "prvtMonitorSessionCompliances": prvtMonitorSessionCompliances,
       "prvtMonitorSessionCompliance": prvtMonitorSessionCompliance,
       "prvtMonitorSessionGroups": prvtMonitorSessionGroups,
       "prvtMonitorSessionMirroredGroup": prvtMonitorSessionMirroredGroup,
       "prvtMonitorSessionAnalyzerGroup": prvtMonitorSessionAnalyzerGroup}
)
