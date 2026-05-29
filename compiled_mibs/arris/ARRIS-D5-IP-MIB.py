# SNMP MIB module (ARRIS-D5-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\d5\ARRIS-D5-IP-MIB

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

(arrisD5UEQam,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisD5UEQam")

(igmpCacheEntry,
 igmpInterfaceEntry) = mibBuilder.importSymbols(
    "IGMP-STD-MIB",
    "igmpCacheEntry",
    "igmpInterfaceEntry")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arrisD5UEQamIpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_D5IpDefaultRoute_Type = InetAddress
_D5IpDefaultRoute_Object = MibScalar
d5IpDefaultRoute = _D5IpDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 1),
    _D5IpDefaultRoute_Type()
)
d5IpDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5IpDefaultRoute.setStatus("current")
_D5IpGratuitousArpEnabled_Type = TruthValue
_D5IpGratuitousArpEnabled_Object = MibScalar
d5IpGratuitousArpEnabled = _D5IpGratuitousArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 2),
    _D5IpGratuitousArpEnabled_Type()
)
d5IpGratuitousArpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5IpGratuitousArpEnabled.setStatus("current")
_D5IpGratuitousArpPeriod_Type = Unsigned32
_D5IpGratuitousArpPeriod_Object = MibScalar
d5IpGratuitousArpPeriod = _D5IpGratuitousArpPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 3),
    _D5IpGratuitousArpPeriod_Type()
)
d5IpGratuitousArpPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5IpGratuitousArpPeriod.setStatus("current")
_D5IpIgmpCacheExtTable_Object = MibTable
d5IpIgmpCacheExtTable = _D5IpIgmpCacheExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 4)
)
if mibBuilder.loadTexts:
    d5IpIgmpCacheExtTable.setStatus("current")
_D5IpIgmpCacheExtEntry_Object = MibTableRow
d5IpIgmpCacheExtEntry = _D5IpIgmpCacheExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 4, 1)
)
if mibBuilder.loadTexts:
    d5IpIgmpCacheExtEntry.setStatus("current")
_IgmpCacheSource1_Type = IpAddress
_IgmpCacheSource1_Object = MibTableColumn
igmpCacheSource1 = _IgmpCacheSource1_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 4, 1, 1),
    _IgmpCacheSource1_Type()
)
igmpCacheSource1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCacheSource1.setStatus("current")


class _IgmpCacheSource1Status_Type(Integer32):
    """Custom type igmpCacheSource1Status based on Integer32"""
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
        *(("ifDown", 1),
          ("candidate", 2),
          ("streaming", 3),
          ("waiting", 4),
          ("undefined", 5))
    )


_IgmpCacheSource1Status_Type.__name__ = "Integer32"
_IgmpCacheSource1Status_Object = MibTableColumn
igmpCacheSource1Status = _IgmpCacheSource1Status_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 4, 1, 2),
    _IgmpCacheSource1Status_Type()
)
igmpCacheSource1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheSource1Status.setStatus("current")


class _IgmpCacheSource1Type_Type(Integer32):
    """Custom type igmpCacheSource1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("static", 1),
          ("dynamic", 2))
    )


_IgmpCacheSource1Type_Type.__name__ = "Integer32"
_IgmpCacheSource1Type_Object = MibTableColumn
igmpCacheSource1Type = _IgmpCacheSource1Type_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 4, 1, 3),
    _IgmpCacheSource1Type_Type()
)
igmpCacheSource1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheSource1Type.setStatus("current")
_IgmpCacheSource2_Type = IpAddress
_IgmpCacheSource2_Object = MibTableColumn
igmpCacheSource2 = _IgmpCacheSource2_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 4, 1, 4),
    _IgmpCacheSource2_Type()
)
igmpCacheSource2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCacheSource2.setStatus("current")


class _IgmpCacheSource2Status_Type(Integer32):
    """Custom type igmpCacheSource2Status based on Integer32"""
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
        *(("ifDown", 1),
          ("candidate", 2),
          ("streaming", 3),
          ("waiting", 4),
          ("undefined", 5))
    )


_IgmpCacheSource2Status_Type.__name__ = "Integer32"
_IgmpCacheSource2Status_Object = MibTableColumn
igmpCacheSource2Status = _IgmpCacheSource2Status_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 4, 1, 5),
    _IgmpCacheSource2Status_Type()
)
igmpCacheSource2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheSource2Status.setStatus("current")


class _IgmpCacheSource2Type_Type(Integer32):
    """Custom type igmpCacheSource2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("static", 1),
          ("dynamic", 2))
    )


_IgmpCacheSource2Type_Type.__name__ = "Integer32"
_IgmpCacheSource2Type_Object = MibTableColumn
igmpCacheSource2Type = _IgmpCacheSource2Type_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 4, 1, 6),
    _IgmpCacheSource2Type_Type()
)
igmpCacheSource2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheSource2Type.setStatus("current")
_IgmpCacheSource3_Type = IpAddress
_IgmpCacheSource3_Object = MibTableColumn
igmpCacheSource3 = _IgmpCacheSource3_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 4, 1, 7),
    _IgmpCacheSource3_Type()
)
igmpCacheSource3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCacheSource3.setStatus("current")


class _IgmpCacheSource3Status_Type(Integer32):
    """Custom type igmpCacheSource3Status based on Integer32"""
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
        *(("ifDown", 1),
          ("candidate", 2),
          ("streaming", 3),
          ("waiting", 4),
          ("undefined", 5))
    )


_IgmpCacheSource3Status_Type.__name__ = "Integer32"
_IgmpCacheSource3Status_Object = MibTableColumn
igmpCacheSource3Status = _IgmpCacheSource3Status_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 4, 1, 8),
    _IgmpCacheSource3Status_Type()
)
igmpCacheSource3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheSource3Status.setStatus("current")


class _IgmpCacheSource3Type_Type(Integer32):
    """Custom type igmpCacheSource3Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("static", 1),
          ("dynamic", 2))
    )


_IgmpCacheSource3Type_Type.__name__ = "Integer32"
_IgmpCacheSource3Type_Object = MibTableColumn
igmpCacheSource3Type = _IgmpCacheSource3Type_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 4, 1, 9),
    _IgmpCacheSource3Type_Type()
)
igmpCacheSource3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheSource3Type.setStatus("current")
_D5IpIgmpInterfaceExtTable_Object = MibTable
d5IpIgmpInterfaceExtTable = _D5IpIgmpInterfaceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 5)
)
if mibBuilder.loadTexts:
    d5IpIgmpInterfaceExtTable.setStatus("current")
_D5IpIgmpInterfaceExtEntry_Object = MibTableRow
d5IpIgmpInterfaceExtEntry = _D5IpIgmpInterfaceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 5, 1)
)
if mibBuilder.loadTexts:
    d5IpIgmpInterfaceExtEntry.setStatus("current")
_IgmpInterfaceExtVersion2QuerierTimer_Type = TimeTicks
_IgmpInterfaceExtVersion2QuerierTimer_Object = MibTableColumn
igmpInterfaceExtVersion2QuerierTimer = _IgmpInterfaceExtVersion2QuerierTimer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1, 5, 1, 1),
    _IgmpInterfaceExtVersion2QuerierTimer_Type()
)
igmpInterfaceExtVersion2QuerierTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceExtVersion2QuerierTimer.setStatus("current")
igmpCacheEntry.registerAugmentions(
    ("ARRIS-D5-IP-MIB",
     "d5IpIgmpCacheExtEntry")
)
d5IpIgmpCacheExtEntry.setIndexNames(*igmpCacheEntry.getIndexNames())
igmpInterfaceEntry.registerAugmentions(
    ("ARRIS-D5-IP-MIB",
     "d5IpIgmpInterfaceExtEntry")
)
d5IpIgmpInterfaceExtEntry.setIndexNames(*igmpInterfaceEntry.getIndexNames())

# Managed Objects groups

arrisD5UEQamIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 15, 1)
)
arrisD5UEQamIpGroup.setObjects(
      *(("ARRIS-D5-IP-MIB", "d5IpDefaultRoute"),
        ("ARRIS-D5-IP-MIB", "d5IpGratuitousArpEnabled"),
        ("ARRIS-D5-IP-MIB", "d5IpGratuitousArpPeriod"))
)
if mibBuilder.loadTexts:
    arrisD5UEQamIpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-D5-IP-MIB",
    **{"arrisD5UEQamIpMib": arrisD5UEQamIpMib,
       "arrisD5UEQamIpGroup": arrisD5UEQamIpGroup,
       "d5IpDefaultRoute": d5IpDefaultRoute,
       "d5IpGratuitousArpEnabled": d5IpGratuitousArpEnabled,
       "d5IpGratuitousArpPeriod": d5IpGratuitousArpPeriod,
       "d5IpIgmpCacheExtTable": d5IpIgmpCacheExtTable,
       "d5IpIgmpCacheExtEntry": d5IpIgmpCacheExtEntry,
       "igmpCacheSource1": igmpCacheSource1,
       "igmpCacheSource1Status": igmpCacheSource1Status,
       "igmpCacheSource1Type": igmpCacheSource1Type,
       "igmpCacheSource2": igmpCacheSource2,
       "igmpCacheSource2Status": igmpCacheSource2Status,
       "igmpCacheSource2Type": igmpCacheSource2Type,
       "igmpCacheSource3": igmpCacheSource3,
       "igmpCacheSource3Status": igmpCacheSource3Status,
       "igmpCacheSource3Type": igmpCacheSource3Type,
       "d5IpIgmpInterfaceExtTable": d5IpIgmpInterfaceExtTable,
       "d5IpIgmpInterfaceExtEntry": d5IpIgmpInterfaceExtEntry,
       "igmpInterfaceExtVersion2QuerierTimer": igmpInterfaceExtVersion2QuerierTimer}
)
