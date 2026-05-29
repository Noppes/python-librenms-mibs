# SNMP MIB module (PRVT-SWITCH-FIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-SWITCH-FIB-MIB

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

(ipNetToMediaIfIndex,
 ipNetToMediaNetAddress,
 ipNetToMediaPhysAddress) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipNetToMediaIfIndex",
    "ipNetToMediaNetAddress",
    "ipNetToMediaPhysAddress")

(ipSwitch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "ipSwitch")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtSwitchFIBMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3)
)
if mibBuilder.loadTexts:
    prvtSwitchFIBMib.setRevisions(
        ("2008-01-01 00:00",
         "2005-02-18 00:00",
         "2003-05-08 00:00",
         "2002-05-21 09:59",
         "2001-01-21 09:59")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtSwitchFIBNotifications_ObjectIdentity = ObjectIdentity
prvtSwitchFIBNotifications = _PrvtSwitchFIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 0)
)
_Fib_ObjectIdentity = ObjectIdentity
fib = _Fib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1)
)
_FibTable_Object = MibTable
fibTable = _FibTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fibTable.setStatus("current")
_FibEntry_Object = MibTableRow
fibEntry = _FibEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1)
)
fibEntry.setIndexNames(
    (0, "PRVT-SWITCH-FIB-MIB", "fibIP"),
    (0, "PRVT-SWITCH-FIB-MIB", "fibMask"),
)
if mibBuilder.loadTexts:
    fibEntry.setStatus("current")
_FibIP_Type = IpAddress
_FibIP_Object = MibTableColumn
fibIP = _FibIP_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 1),
    _FibIP_Type()
)
fibIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibIP.setStatus("current")
_FibMask_Type = IpAddress
_FibMask_Object = MibTableColumn
fibMask = _FibMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 2),
    _FibMask_Type()
)
fibMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibMask.setStatus("current")


class _FibProtocol_Type(Integer32):
    """Custom type fibProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              13,
              14,
              15,
              16,
              100)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("direct", 2),
          ("static", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("ospf", 13),
          ("bgp", 14),
          ("arp", 15),
          ("remote", 16),
          ("unknown", 100))
    )


_FibProtocol_Type.__name__ = "Integer32"
_FibProtocol_Object = MibTableColumn
fibProtocol = _FibProtocol_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 3),
    _FibProtocol_Type()
)
fibProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibProtocol.setStatus("current")
_FibNextHop_Type = IpAddress
_FibNextHop_Object = MibTableColumn
fibNextHop = _FibNextHop_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 4),
    _FibNextHop_Type()
)
fibNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibNextHop.setStatus("current")
_FibNextHopMac_Type = MacAddress
_FibNextHopMac_Object = MibTableColumn
fibNextHopMac = _FibNextHopMac_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 5),
    _FibNextHopMac_Type()
)
fibNextHopMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibNextHopMac.setStatus("current")
_FibVID_Type = Integer32
_FibVID_Object = MibTableColumn
fibVID = _FibVID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 6),
    _FibVID_Type()
)
fibVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibVID.setStatus("current")
_FibOutPort_Type = Integer32
_FibOutPort_Object = MibTableColumn
fibOutPort = _FibOutPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 7),
    _FibOutPort_Type()
)
fibOutPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibOutPort.setStatus("current")


class _FibPriority_Type(Integer32):
    """Custom type fibPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FibPriority_Type.__name__ = "Integer32"
_FibPriority_Object = MibTableColumn
fibPriority = _FibPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 8),
    _FibPriority_Type()
)
fibPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibPriority.setStatus("current")


class _FibDiscardabilty_Type(Integer32):
    """Custom type fibDiscardabilty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nondiscard", 0),
          ("discard", 1))
    )


_FibDiscardabilty_Type.__name__ = "Integer32"
_FibDiscardabilty_Object = MibTableColumn
fibDiscardabilty = _FibDiscardabilty_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 9),
    _FibDiscardabilty_Type()
)
fibDiscardabilty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibDiscardabilty.setStatus("current")


class _FibDSCP_Type(OctetString):
    """Custom type fibDSCP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_FibDSCP_Type.__name__ = "OctetString"
_FibDSCP_Object = MibTableColumn
fibDSCP = _FibDSCP_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 10),
    _FibDSCP_Type()
)
fibDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibDSCP.setStatus("current")
_FibRowStatus_Type = RowStatus
_FibRowStatus_Object = MibTableColumn
fibRowStatus = _FibRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 1, 1, 1, 11),
    _FibRowStatus_Type()
)
fibRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibRowStatus.setStatus("current")
_PrvtSwitchFIBConformance_ObjectIdentity = ObjectIdentity
prvtSwitchFIBConformance = _PrvtSwitchFIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 3)
)
_PrvtSwitchFIBMIBGroups_ObjectIdentity = ObjectIdentity
prvtSwitchFIBMIBGroups = _PrvtSwitchFIBMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 3, 2)
)

# Managed Objects groups


# Notification objects

newIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 0, 1)
)
newIP.setObjects(
      *(("IP-MIB", "ipNetToMediaIfIndex"),
        ("IP-MIB", "ipNetToMediaPhysAddress"),
        ("IP-MIB", "ipNetToMediaNetAddress"))
)
if mibBuilder.loadTexts:
    newIP.setStatus(
        "current"
    )


# Notifications groups

prvtSwitchFIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 3, 3, 2, 3)
)
prvtSwitchFIBNotificationGroup.setObjects(
    ("PRVT-SWITCH-FIB-MIB", "newIP")
)
if mibBuilder.loadTexts:
    prvtSwitchFIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-SWITCH-FIB-MIB",
    **{"prvtSwitchFIBMib": prvtSwitchFIBMib,
       "prvtSwitchFIBNotifications": prvtSwitchFIBNotifications,
       "newIP": newIP,
       "fib": fib,
       "fibTable": fibTable,
       "fibEntry": fibEntry,
       "fibIP": fibIP,
       "fibMask": fibMask,
       "fibProtocol": fibProtocol,
       "fibNextHop": fibNextHop,
       "fibNextHopMac": fibNextHopMac,
       "fibVID": fibVID,
       "fibOutPort": fibOutPort,
       "fibPriority": fibPriority,
       "fibDiscardabilty": fibDiscardabilty,
       "fibDSCP": fibDSCP,
       "fibRowStatus": fibRowStatus,
       "prvtSwitchFIBConformance": prvtSwitchFIBConformance,
       "prvtSwitchFIBMIBGroups": prvtSwitchFIBMIBGroups,
       "prvtSwitchFIBNotificationGroup": prvtSwitchFIBNotificationGroup}
)
