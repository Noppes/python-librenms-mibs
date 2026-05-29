# SNMP MIB module (AVIAT-SWMANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\aviat-wtm\AVIAT-SWMANAGEMENT-MIB

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(aviatModules,) = mibBuilder.importSymbols(
    "STXN-GLOBALREGISTER-MIB",
    "aviatModules")


# MODULE-IDENTITY

aviatSwManagementModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11)
)
if mibBuilder.loadTexts:
    aviatSwManagementModule.setRevisions(
        ("2014-01-21 01:57",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AviatSwManagementConf_ObjectIdentity = ObjectIdentity
aviatSwManagementConf = _AviatSwManagementConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 1)
)
_AviatSwManagementGroups_ObjectIdentity = ObjectIdentity
aviatSwManagementGroups = _AviatSwManagementGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 1, 1)
)
_AviatSwManagementCompliance_ObjectIdentity = ObjectIdentity
aviatSwManagementCompliance = _AviatSwManagementCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 1, 2)
)
_AviatSwManagementMIBObjects_ObjectIdentity = ObjectIdentity
aviatSwManagementMIBObjects = _AviatSwManagementMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2)
)
_AviatSwResetObjects_ObjectIdentity = ObjectIdentity
aviatSwResetObjects = _AviatSwResetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 1)
)


class _AviatSmSoftReset_Type(Integer32):
    """Custom type aviatSmSoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetNone", 0),
          ("resetSoft", 1),
          ("resetHard", 2))
    )


_AviatSmSoftReset_Type.__name__ = "Integer32"
_AviatSmSoftReset_Object = MibScalar
aviatSmSoftReset = _AviatSmSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 1, 1),
    _AviatSmSoftReset_Type()
)
aviatSmSoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatSmSoftReset.setStatus("current")
_AviatSwLoadObjects_ObjectIdentity = ObjectIdentity
aviatSwLoadObjects = _AviatSwLoadObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2)
)


class _AviatSmLoadControl_Type(Integer32):
    """Custom type aviatSmLoadControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("abort", 0),
          ("load", 1),
          ("activate", 2),
          ("loadAndActivate", 3),
          ("rollback", 4),
          ("forceLoad", 5))
    )


_AviatSmLoadControl_Type.__name__ = "Integer32"
_AviatSmLoadControl_Object = MibScalar
aviatSmLoadControl = _AviatSmLoadControl_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 1),
    _AviatSmLoadControl_Type()
)
aviatSmLoadControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatSmLoadControl.setStatus("current")


class _AviatSmLoadStatus_Type(Integer32):
    """Custom type aviatSmLoadStatus based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("abort", 0),
          ("load", 1),
          ("commit", 2),
          ("activate", 3),
          ("rollback", 4),
          ("idle", 5),
          ("loadOk", 6),
          ("activateOk", 7),
          ("rollbackOk", 8),
          ("compatibilityError", 9),
          ("loadError", 10),
          ("activateError", 11),
          ("rollbackError", 12),
          ("waitingToActivate", 13),
          ("sameVersion", 14))
    )


_AviatSmLoadStatus_Type.__name__ = "Integer32"
_AviatSmLoadStatus_Object = MibScalar
aviatSmLoadStatus = _AviatSmLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 2),
    _AviatSmLoadStatus_Type()
)
aviatSmLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatSmLoadStatus.setStatus("current")


class _AviatSmLoadRollbackDuration_Type(Integer32):
    """Custom type aviatSmLoadRollbackDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AviatSmLoadRollbackDuration_Type.__name__ = "Integer32"
_AviatSmLoadRollbackDuration_Object = MibScalar
aviatSmLoadRollbackDuration = _AviatSmLoadRollbackDuration_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 3),
    _AviatSmLoadRollbackDuration_Type()
)
aviatSmLoadRollbackDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatSmLoadRollbackDuration.setStatus("current")


class _AviatSmLoadRollbackTimer_Type(Integer32):
    """Custom type aviatSmLoadRollbackTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AviatSmLoadRollbackTimer_Type.__name__ = "Integer32"
_AviatSmLoadRollbackTimer_Object = MibScalar
aviatSmLoadRollbackTimer = _AviatSmLoadRollbackTimer_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 4),
    _AviatSmLoadRollbackTimer_Type()
)
aviatSmLoadRollbackTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatSmLoadRollbackTimer.setStatus("current")


class _AviatSmLoadActivateWaitDuration_Type(Integer32):
    """Custom type aviatSmLoadActivateWaitDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AviatSmLoadActivateWaitDuration_Type.__name__ = "Integer32"
_AviatSmLoadActivateWaitDuration_Object = MibScalar
aviatSmLoadActivateWaitDuration = _AviatSmLoadActivateWaitDuration_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 5),
    _AviatSmLoadActivateWaitDuration_Type()
)
aviatSmLoadActivateWaitDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatSmLoadActivateWaitDuration.setStatus("current")


class _AviatSmLoadActivateWaitTimer_Type(Integer32):
    """Custom type aviatSmLoadActivateWaitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AviatSmLoadActivateWaitTimer_Type.__name__ = "Integer32"
_AviatSmLoadActivateWaitTimer_Object = MibScalar
aviatSmLoadActivateWaitTimer = _AviatSmLoadActivateWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 6),
    _AviatSmLoadActivateWaitTimer_Type()
)
aviatSmLoadActivateWaitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatSmLoadActivateWaitTimer.setStatus("current")
_AviatSmLoadActivateTime_Type = DateAndTime
_AviatSmLoadActivateTime_Object = MibScalar
aviatSmLoadActivateTime = _AviatSmLoadActivateTime_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 7),
    _AviatSmLoadActivateTime_Type()
)
aviatSmLoadActivateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatSmLoadActivateTime.setStatus("current")


class _AviatSmLoadUri_Type(DisplayString):
    """Custom type aviatSmLoadUri based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AviatSmLoadUri_Type.__name__ = "DisplayString"
_AviatSmLoadUri_Object = MibScalar
aviatSmLoadUri = _AviatSmLoadUri_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 8),
    _AviatSmLoadUri_Type()
)
aviatSmLoadUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatSmLoadUri.setStatus("current")


class _AviatSmLoadProgress_Type(Integer32):
    """Custom type aviatSmLoadProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AviatSmLoadProgress_Type.__name__ = "Integer32"
_AviatSmLoadProgress_Object = MibScalar
aviatSmLoadProgress = _AviatSmLoadProgress_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 9),
    _AviatSmLoadProgress_Type()
)
aviatSmLoadProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatSmLoadProgress.setStatus("current")
_AviatSwDetailsObjects_ObjectIdentity = ObjectIdentity
aviatSwDetailsObjects = _AviatSwDetailsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 3)
)


class _AviatSmDetailsVersion_Type(DisplayString):
    """Custom type aviatSmDetailsVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AviatSmDetailsVersion_Type.__name__ = "DisplayString"
_AviatSmDetailsVersion_Object = MibScalar
aviatSmDetailsVersion = _AviatSmDetailsVersion_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 3, 1),
    _AviatSmDetailsVersion_Type()
)
aviatSmDetailsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatSmDetailsVersion.setStatus("current")


class _AviatSmDetailsInactiveVersion_Type(DisplayString):
    """Custom type aviatSmDetailsInactiveVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AviatSmDetailsInactiveVersion_Type.__name__ = "DisplayString"
_AviatSmDetailsInactiveVersion_Object = MibScalar
aviatSmDetailsInactiveVersion = _AviatSmDetailsInactiveVersion_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 3, 2),
    _AviatSmDetailsInactiveVersion_Type()
)
aviatSmDetailsInactiveVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatSmDetailsInactiveVersion.setStatus("current")

# Managed Objects groups

aviatSwResetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 1, 1, 1)
)
aviatSwResetGroup.setObjects(
    ("AVIAT-SWMANAGEMENT-MIB", "aviatSmSoftReset")
)
if mibBuilder.loadTexts:
    aviatSwResetGroup.setStatus("current")

aviatSwLoadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 1, 1, 2)
)
aviatSwLoadGroup.setObjects(
      *(("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadControl"),
        ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadStatus"),
        ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadRollbackDuration"),
        ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadRollbackTimer"),
        ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadActivateWaitDuration"),
        ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadActivateWaitTimer"),
        ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadActivateTime"),
        ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadUri"),
        ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadProgress"))
)
if mibBuilder.loadTexts:
    aviatSwLoadGroup.setStatus("current")

aviatSwDetailsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 1, 1, 3)
)
aviatSwDetailsGroup.setObjects(
      *(("AVIAT-SWMANAGEMENT-MIB", "aviatSmDetailsVersion"),
        ("AVIAT-SWMANAGEMENT-MIB", "aviatSmDetailsInactiveVersion"))
)
if mibBuilder.loadTexts:
    aviatSwDetailsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aviatSwManagementComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2509, 9, 11, 1, 2, 1)
)
aviatSwManagementComplV1.setObjects(
      *(("AVIAT-SWMANAGEMENT-MIB", "aviatSwResetGroup"),
        ("AVIAT-SWMANAGEMENT-MIB", "aviatSwLoadGroup"),
        ("AVIAT-SWMANAGEMENT-MIB", "aviatSwDetailsGroup"))
)
if mibBuilder.loadTexts:
    aviatSwManagementComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVIAT-SWMANAGEMENT-MIB",
    **{"aviatSwManagementModule": aviatSwManagementModule,
       "aviatSwManagementConf": aviatSwManagementConf,
       "aviatSwManagementGroups": aviatSwManagementGroups,
       "aviatSwResetGroup": aviatSwResetGroup,
       "aviatSwLoadGroup": aviatSwLoadGroup,
       "aviatSwDetailsGroup": aviatSwDetailsGroup,
       "aviatSwManagementCompliance": aviatSwManagementCompliance,
       "aviatSwManagementComplV1": aviatSwManagementComplV1,
       "aviatSwManagementMIBObjects": aviatSwManagementMIBObjects,
       "aviatSwResetObjects": aviatSwResetObjects,
       "aviatSmSoftReset": aviatSmSoftReset,
       "aviatSwLoadObjects": aviatSwLoadObjects,
       "aviatSmLoadControl": aviatSmLoadControl,
       "aviatSmLoadStatus": aviatSmLoadStatus,
       "aviatSmLoadRollbackDuration": aviatSmLoadRollbackDuration,
       "aviatSmLoadRollbackTimer": aviatSmLoadRollbackTimer,
       "aviatSmLoadActivateWaitDuration": aviatSmLoadActivateWaitDuration,
       "aviatSmLoadActivateWaitTimer": aviatSmLoadActivateWaitTimer,
       "aviatSmLoadActivateTime": aviatSmLoadActivateTime,
       "aviatSmLoadUri": aviatSmLoadUri,
       "aviatSmLoadProgress": aviatSmLoadProgress,
       "aviatSwDetailsObjects": aviatSwDetailsObjects,
       "aviatSmDetailsVersion": aviatSmDetailsVersion,
       "aviatSmDetailsInactiveVersion": aviatSmDetailsInactiveVersion}
)
