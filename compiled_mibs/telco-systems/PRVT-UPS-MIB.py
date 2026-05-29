# SNMP MIB module (PRVT-UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-UPS-MIB

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

prvtUPSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 103)
)
if mibBuilder.loadTexts:
    prvtUPSMib.setRevisions(
        ("2008-01-01 00:00",
         "2005-02-16 00:00",
         "2003-05-08 00:00",
         "2002-01-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtUPSNotifications_ObjectIdentity = ObjectIdentity
prvtUPSNotifications = _PrvtUPSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 0)
)
_UpsStatus_ObjectIdentity = ObjectIdentity
upsStatus = _UpsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1)
)


class _UpsConnectedStatus_Type(Integer32):
    """Custom type upsConnectedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_UpsConnectedStatus_Type.__name__ = "Integer32"
_UpsConnectedStatus_Object = MibScalar
upsConnectedStatus = _UpsConnectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1, 1),
    _UpsConnectedStatus_Type()
)
upsConnectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConnectedStatus.setStatus("current")


class _UpsLinePowerStatus_Type(Integer32):
    """Custom type upsLinePowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("fromExternalConnection", 2),
          ("fromInternalBattery", 3))
    )


_UpsLinePowerStatus_Type.__name__ = "Integer32"
_UpsLinePowerStatus_Object = MibScalar
upsLinePowerStatus = _UpsLinePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1, 2),
    _UpsLinePowerStatus_Type()
)
upsLinePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsLinePowerStatus.setStatus("current")


class _UpsBatteryStorageStatus_Type(Integer32):
    """Custom type upsBatteryStorageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("moreThan30Minutes", 2),
          ("lessThan30Minutes", 3))
    )


_UpsBatteryStorageStatus_Type.__name__ = "Integer32"
_UpsBatteryStorageStatus_Object = MibScalar
upsBatteryStorageStatus = _UpsBatteryStorageStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1, 3),
    _UpsBatteryStorageStatus_Type()
)
upsBatteryStorageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryStorageStatus.setStatus("current")


class _UpsInternalStatus_Type(Integer32):
    """Custom type upsInternalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ok", 2),
          ("failure", 3))
    )


_UpsInternalStatus_Type.__name__ = "Integer32"
_UpsInternalStatus_Object = MibScalar
upsInternalStatus = _UpsInternalStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 1, 4),
    _UpsInternalStatus_Type()
)
upsInternalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInternalStatus.setStatus("current")
_PrvtUPSConformance_ObjectIdentity = ObjectIdentity
prvtUPSConformance = _PrvtUPSConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 2)
)
_PrvtUPSMIBGroups_ObjectIdentity = ObjectIdentity
prvtUPSMIBGroups = _PrvtUPSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 2, 2)
)

# Managed Objects groups


# Notification objects

upsStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 0, 1)
)
upsStatusChange.setObjects(
      *(("PRVT-UPS-MIB", "upsConnectedStatus"),
        ("PRVT-UPS-MIB", "upsLinePowerStatus"),
        ("PRVT-UPS-MIB", "upsBatteryStorageStatus"),
        ("PRVT-UPS-MIB", "upsInternalStatus"))
)
if mibBuilder.loadTexts:
    upsStatusChange.setStatus(
        "current"
    )


# Notifications groups

prvtUPSNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 103, 2, 2, 3)
)
prvtUPSNotificationGroup.setObjects(
    ("PRVT-UPS-MIB", "upsStatusChange")
)
if mibBuilder.loadTexts:
    prvtUPSNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-UPS-MIB",
    **{"prvtUPSMib": prvtUPSMib,
       "prvtUPSNotifications": prvtUPSNotifications,
       "upsStatusChange": upsStatusChange,
       "upsStatus": upsStatus,
       "upsConnectedStatus": upsConnectedStatus,
       "upsLinePowerStatus": upsLinePowerStatus,
       "upsBatteryStorageStatus": upsBatteryStorageStatus,
       "upsInternalStatus": upsInternalStatus,
       "prvtUPSConformance": prvtUPSConformance,
       "prvtUPSMIBGroups": prvtUPSMIBGroups,
       "prvtUPSNotificationGroup": prvtUPSNotificationGroup}
)
