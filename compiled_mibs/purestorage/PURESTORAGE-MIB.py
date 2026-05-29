# SNMP MIB module (PURESTORAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\purestorage\PURESTORAGE-MIB

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

purestorage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40482)
)
if mibBuilder.loadTexts:
    purestorage.setRevisions(
        ("2012-09-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PureSystem_ObjectIdentity = ObjectIdentity
pureSystem = _PureSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40482, 1)
)
if mibBuilder.loadTexts:
    pureSystem.setStatus("current")
_PureNotifications_ObjectIdentity = ObjectIdentity
pureNotifications = _PureNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40482, 2)
)
if mibBuilder.loadTexts:
    pureNotifications.setStatus("current")
_PureObjects_ObjectIdentity = ObjectIdentity
pureObjects = _PureObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40482, 3)
)
if mibBuilder.loadTexts:
    pureObjects.setStatus("current")
_PureProductName_Type = OctetString
_PureProductName_Object = MibScalar
pureProductName = _PureProductName_Object(
    (1, 3, 6, 1, 4, 1, 40482, 3, 1),
    _PureProductName_Type()
)
pureProductName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pureProductName.setStatus("current")
_PureProductVersion_Type = OctetString
_PureProductVersion_Object = MibScalar
pureProductVersion = _PureProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 40482, 3, 2),
    _PureProductVersion_Type()
)
pureProductVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pureProductVersion.setStatus("current")
_PureHost_Type = OctetString
_PureHost_Object = MibScalar
pureHost = _PureHost_Object(
    (1, 3, 6, 1, 4, 1, 40482, 3, 3),
    _PureHost_Type()
)
pureHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pureHost.setStatus("current")
_PureAlertCode_Type = Integer32
_PureAlertCode_Object = MibScalar
pureAlertCode = _PureAlertCode_Object(
    (1, 3, 6, 1, 4, 1, 40482, 3, 4),
    _PureAlertCode_Type()
)
pureAlertCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pureAlertCode.setStatus("current")
_PureAlertSubject_Type = OctetString
_PureAlertSubject_Object = MibScalar
pureAlertSubject = _PureAlertSubject_Object(
    (1, 3, 6, 1, 4, 1, 40482, 3, 5),
    _PureAlertSubject_Type()
)
pureAlertSubject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pureAlertSubject.setStatus("current")
_PureAlertBody_Type = OctetString
_PureAlertBody_Object = MibScalar
pureAlertBody = _PureAlertBody_Object(
    (1, 3, 6, 1, 4, 1, 40482, 3, 6),
    _PureAlertBody_Type()
)
pureAlertBody.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pureAlertBody.setStatus("current")
_PureAlertReminder_Type = Integer32
_PureAlertReminder_Object = MibScalar
pureAlertReminder = _PureAlertReminder_Object(
    (1, 3, 6, 1, 4, 1, 40482, 3, 7),
    _PureAlertReminder_Type()
)
pureAlertReminder.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pureAlertReminder.setStatus("current")
_PurePerformance_ObjectIdentity = ObjectIdentity
purePerformance = _PurePerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40482, 4)
)
if mibBuilder.loadTexts:
    purePerformance.setStatus("current")
_PureArrayReadBandwidth_Type = Integer32
_PureArrayReadBandwidth_Object = MibScalar
pureArrayReadBandwidth = _PureArrayReadBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 40482, 4, 1),
    _PureArrayReadBandwidth_Type()
)
pureArrayReadBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pureArrayReadBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    pureArrayReadBandwidth.setUnits("B/s")
_PureArrayWriteBandwidth_Type = Integer32
_PureArrayWriteBandwidth_Object = MibScalar
pureArrayWriteBandwidth = _PureArrayWriteBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 40482, 4, 2),
    _PureArrayWriteBandwidth_Type()
)
pureArrayWriteBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pureArrayWriteBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    pureArrayWriteBandwidth.setUnits("B/s")
_PureArrayReadIOPS_Type = Integer32
_PureArrayReadIOPS_Object = MibScalar
pureArrayReadIOPS = _PureArrayReadIOPS_Object(
    (1, 3, 6, 1, 4, 1, 40482, 4, 3),
    _PureArrayReadIOPS_Type()
)
pureArrayReadIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pureArrayReadIOPS.setStatus("current")
if mibBuilder.loadTexts:
    pureArrayReadIOPS.setUnits("op/s")
_PureArrayWriteIOPS_Type = Integer32
_PureArrayWriteIOPS_Object = MibScalar
pureArrayWriteIOPS = _PureArrayWriteIOPS_Object(
    (1, 3, 6, 1, 4, 1, 40482, 4, 4),
    _PureArrayWriteIOPS_Type()
)
pureArrayWriteIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pureArrayWriteIOPS.setStatus("current")
if mibBuilder.loadTexts:
    pureArrayWriteIOPS.setUnits("op/s")
_PureArrayReadLatency_Type = Integer32
_PureArrayReadLatency_Object = MibScalar
pureArrayReadLatency = _PureArrayReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 40482, 4, 5),
    _PureArrayReadLatency_Type()
)
pureArrayReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pureArrayReadLatency.setStatus("current")
if mibBuilder.loadTexts:
    pureArrayReadLatency.setUnits("us/op")
_PureArrayWriteLatency_Type = Integer32
_PureArrayWriteLatency_Object = MibScalar
pureArrayWriteLatency = _PureArrayWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 40482, 4, 6),
    _PureArrayWriteLatency_Type()
)
pureArrayWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pureArrayWriteLatency.setStatus("current")
if mibBuilder.loadTexts:
    pureArrayWriteLatency.setUnits("us/op")
_PureExperimental_ObjectIdentity = ObjectIdentity
pureExperimental = _PureExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40482, 700)
)
if mibBuilder.loadTexts:
    pureExperimental.setStatus("current")

# Managed Objects groups


# Notification objects

pureInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40482, 2, 50)
)
pureInfoTrap.setObjects(
      *(("PURESTORAGE-MIB", "pureProductName"),
        ("PURESTORAGE-MIB", "pureProductVersion"),
        ("PURESTORAGE-MIB", "pureHost"),
        ("PURESTORAGE-MIB", "pureAlertCode"),
        ("PURESTORAGE-MIB", "pureAlertSubject"),
        ("PURESTORAGE-MIB", "pureAlertBody"))
)
if mibBuilder.loadTexts:
    pureInfoTrap.setStatus(
        "current"
    )

pureWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40482, 2, 51)
)
pureWarningTrap.setObjects(
      *(("PURESTORAGE-MIB", "pureProductName"),
        ("PURESTORAGE-MIB", "pureProductVersion"),
        ("PURESTORAGE-MIB", "pureHost"),
        ("PURESTORAGE-MIB", "pureAlertCode"),
        ("PURESTORAGE-MIB", "pureAlertSubject"),
        ("PURESTORAGE-MIB", "pureAlertBody"))
)
if mibBuilder.loadTexts:
    pureWarningTrap.setStatus(
        "current"
    )

pureCriticalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40482, 2, 52)
)
pureCriticalTrap.setObjects(
      *(("PURESTORAGE-MIB", "pureProductName"),
        ("PURESTORAGE-MIB", "pureProductVersion"),
        ("PURESTORAGE-MIB", "pureHost"),
        ("PURESTORAGE-MIB", "pureAlertCode"),
        ("PURESTORAGE-MIB", "pureAlertSubject"),
        ("PURESTORAGE-MIB", "pureAlertBody"))
)
if mibBuilder.loadTexts:
    pureCriticalTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PURESTORAGE-MIB",
    **{"purestorage": purestorage,
       "pureSystem": pureSystem,
       "pureNotifications": pureNotifications,
       "pureInfoTrap": pureInfoTrap,
       "pureWarningTrap": pureWarningTrap,
       "pureCriticalTrap": pureCriticalTrap,
       "pureObjects": pureObjects,
       "pureProductName": pureProductName,
       "pureProductVersion": pureProductVersion,
       "pureHost": pureHost,
       "pureAlertCode": pureAlertCode,
       "pureAlertSubject": pureAlertSubject,
       "pureAlertBody": pureAlertBody,
       "pureAlertReminder": pureAlertReminder,
       "purePerformance": purePerformance,
       "pureArrayReadBandwidth": pureArrayReadBandwidth,
       "pureArrayWriteBandwidth": pureArrayWriteBandwidth,
       "pureArrayReadIOPS": pureArrayReadIOPS,
       "pureArrayWriteIOPS": pureArrayWriteIOPS,
       "pureArrayReadLatency": pureArrayReadLatency,
       "pureArrayWriteLatency": pureArrayWriteLatency,
       "pureExperimental": pureExperimental}
)
