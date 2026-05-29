# SNMP MIB module (ALPHACOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zenitel\ALPHACOM-MIB

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

stentofon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26122)
)
if mibBuilder.loadTexts:
    stentofon.setRevisions(
        ("2011-11-30 16:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Alphacom_ObjectIdentity = ObjectIdentity
alphacom = _Alphacom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 1)
)
_Amc_ObjectIdentity = ObjectIdentity
amc = _Amc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 1, 1)
)


class _NodeState_Type(Integer32):
    """Custom type nodeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NodeState_Type.__name__ = "Integer32"
_NodeState_Object = MibScalar
nodeState = _NodeState_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 1, 1),
    _NodeState_Type()
)
nodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeState.setStatus("current")
_Rtp_ObjectIdentity = ObjectIdentity
rtp = _Rtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 1, 2)
)
_RtpStatisticsTable_Object = MibTable
rtpStatisticsTable = _RtpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rtpStatisticsTable.setStatus("current")
_RtpStatisticsEntry_Object = MibTableRow
rtpStatisticsEntry = _RtpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 2, 1, 1)
)
rtpStatisticsEntry.setIndexNames(
    (0, "ALPHACOM-MIB", "rtpStatIndex"),
)
if mibBuilder.loadTexts:
    rtpStatisticsEntry.setStatus("current")
_RtpStatIndex_Type = Unsigned32
_RtpStatIndex_Object = MibTableColumn
rtpStatIndex = _RtpStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 2, 1, 1, 1),
    _RtpStatIndex_Type()
)
rtpStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtpStatIndex.setStatus("current")
_RtpFromNode_Type = Unsigned32
_RtpFromNode_Object = MibTableColumn
rtpFromNode = _RtpFromNode_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 2, 1, 1, 2),
    _RtpFromNode_Type()
)
rtpFromNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpFromNode.setStatus("current")
_RtpToNode_Type = Unsigned32
_RtpToNode_Object = MibTableColumn
rtpToNode = _RtpToNode_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 2, 1, 1, 3),
    _RtpToNode_Type()
)
rtpToNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpToNode.setStatus("current")
_RtpStreamTime_Type = Counter32
_RtpStreamTime_Object = MibTableColumn
rtpStreamTime = _RtpStreamTime_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 2, 1, 1, 4),
    _RtpStreamTime_Type()
)
rtpStreamTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStreamTime.setStatus("current")
_RtpConnectons_Type = Counter32
_RtpConnectons_Object = MibTableColumn
rtpConnectons = _RtpConnectons_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 2, 1, 1, 5),
    _RtpConnectons_Type()
)
rtpConnectons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpConnectons.setStatus("current")
_RtpTxPackets_Type = Counter32
_RtpTxPackets_Object = MibTableColumn
rtpTxPackets = _RtpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 2, 1, 1, 6),
    _RtpTxPackets_Type()
)
rtpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpTxPackets.setStatus("current")
_RtpRxPackets_Type = Counter32
_RtpRxPackets_Object = MibTableColumn
rtpRxPackets = _RtpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 2, 1, 1, 7),
    _RtpRxPackets_Type()
)
rtpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRxPackets.setStatus("current")
_RtpRxLate_Type = Counter32
_RtpRxLate_Object = MibTableColumn
rtpRxLate = _RtpRxLate_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 2, 1, 1, 8),
    _RtpRxLate_Type()
)
rtpRxLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRxLate.setStatus("current")
_RtpRxLost_Type = Counter32
_RtpRxLost_Object = MibTableColumn
rtpRxLost = _RtpRxLost_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 2, 1, 1, 9),
    _RtpRxLost_Type()
)
rtpRxLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRxLost.setStatus("current")
_RtpJitter_Type = Unsigned32
_RtpJitter_Object = MibTableColumn
rtpJitter = _RtpJitter_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 2, 1, 1, 10),
    _RtpJitter_Type()
)
rtpJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpJitter.setStatus("current")
_RtpDelay_Type = Unsigned32
_RtpDelay_Object = MibTableColumn
rtpDelay = _RtpDelay_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 2, 1, 1, 11),
    _RtpDelay_Type()
)
rtpDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpDelay.setStatus("current")
_AlarmObjects_ObjectIdentity = ObjectIdentity
alarmObjects = _AlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 1, 10)
)


class _ManagedObjectClass_Type(DisplayString):
    """Custom type managedObjectClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ManagedObjectClass_Type.__name__ = "DisplayString"
_ManagedObjectClass_Object = MibScalar
managedObjectClass = _ManagedObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 10, 1),
    _ManagedObjectClass_Type()
)
managedObjectClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    managedObjectClass.setStatus("current")


class _ManagedObjectInstance_Type(DisplayString):
    """Custom type managedObjectInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ManagedObjectInstance_Type.__name__ = "DisplayString"
_ManagedObjectInstance_Object = MibScalar
managedObjectInstance = _ManagedObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 10, 2),
    _ManagedObjectInstance_Type()
)
managedObjectInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    managedObjectInstance.setStatus("current")


class _Severity_Type(Integer32):
    """Custom type severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("indeterminate", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("info", 5),
          ("cleared", 6))
    )


_Severity_Type.__name__ = "Integer32"
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 10, 3),
    _Severity_Type()
)
severity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    severity.setStatus("current")


class _Timestamp_Type(DisplayString):
    """Custom type timestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Timestamp_Type.__name__ = "DisplayString"
_Timestamp_Object = MibScalar
timestamp = _Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 10, 4),
    _Timestamp_Type()
)
timestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    timestamp.setStatus("current")
_Description_Type = OctetString
_Description_Object = MibScalar
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 26122, 1, 10, 5),
    _Description_Type()
)
description.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    description.setStatus("current")
_AlarmNotifications_ObjectIdentity = ObjectIdentity
alarmNotifications = _AlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26122, 1, 11)
)

# Managed Objects groups


# Notification objects

logEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 1, 11, 1000)
)
logEvent.setObjects(
      *(("ALPHACOM-MIB", "managedObjectClass"),
        ("ALPHACOM-MIB", "managedObjectInstance"),
        ("ALPHACOM-MIB", "severity"),
        ("ALPHACOM-MIB", "timestamp"),
        ("ALPHACOM-MIB", "description"))
)
if mibBuilder.loadTexts:
    logEvent.setStatus(
        "current"
    )

debugLogEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 1, 11, 1001)
)
debugLogEvent.setObjects(
      *(("ALPHACOM-MIB", "managedObjectClass"),
        ("ALPHACOM-MIB", "managedObjectInstance"),
        ("ALPHACOM-MIB", "severity"),
        ("ALPHACOM-MIB", "timestamp"),
        ("ALPHACOM-MIB", "description"))
)
if mibBuilder.loadTexts:
    debugLogEvent.setStatus(
        "current"
    )

systemLogEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 1, 11, 1002)
)
systemLogEvent.setObjects(
      *(("ALPHACOM-MIB", "managedObjectClass"),
        ("ALPHACOM-MIB", "managedObjectInstance"),
        ("ALPHACOM-MIB", "severity"),
        ("ALPHACOM-MIB", "timestamp"),
        ("ALPHACOM-MIB", "description"))
)
if mibBuilder.loadTexts:
    systemLogEvent.setStatus(
        "current"
    )

callLogEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 26122, 1, 11, 1003)
)
callLogEvent.setObjects(
      *(("ALPHACOM-MIB", "managedObjectClass"),
        ("ALPHACOM-MIB", "managedObjectInstance"),
        ("ALPHACOM-MIB", "severity"),
        ("ALPHACOM-MIB", "timestamp"),
        ("ALPHACOM-MIB", "description"))
)
if mibBuilder.loadTexts:
    callLogEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALPHACOM-MIB",
    **{"stentofon": stentofon,
       "alphacom": alphacom,
       "amc": amc,
       "nodeState": nodeState,
       "rtp": rtp,
       "rtpStatisticsTable": rtpStatisticsTable,
       "rtpStatisticsEntry": rtpStatisticsEntry,
       "rtpStatIndex": rtpStatIndex,
       "rtpFromNode": rtpFromNode,
       "rtpToNode": rtpToNode,
       "rtpStreamTime": rtpStreamTime,
       "rtpConnectons": rtpConnectons,
       "rtpTxPackets": rtpTxPackets,
       "rtpRxPackets": rtpRxPackets,
       "rtpRxLate": rtpRxLate,
       "rtpRxLost": rtpRxLost,
       "rtpJitter": rtpJitter,
       "rtpDelay": rtpDelay,
       "alarmObjects": alarmObjects,
       "managedObjectClass": managedObjectClass,
       "managedObjectInstance": managedObjectInstance,
       "severity": severity,
       "timestamp": timestamp,
       "description": description,
       "alarmNotifications": alarmNotifications,
       "logEvent": logEvent,
       "debugLogEvent": debugLogEvent,
       "systemLogEvent": systemLogEvent,
       "callLogEvent": callLogEvent}
)
