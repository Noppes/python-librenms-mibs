# SNMP MIB module (ROSMGMT-COMMON-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\raisecom\ROSMGMT-COMMON-MANAGEMENT-MIB

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

(rosMgmt,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "rosMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rosMgmtCommonManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 2)
)
if mibBuilder.loadTexts:
    rosMgmtCommonManagement.setRevisions(
        ("2020-04-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RosMgmtCommonFunctionGroup_ObjectIdentity = ObjectIdentity
rosMgmtCommonFunctionGroup = _RosMgmtCommonFunctionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 2, 1)
)
_RosMgmtCommonNotifications_ObjectIdentity = ObjectIdentity
rosMgmtCommonNotifications = _RosMgmtCommonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 2, 1, 0)
)
_RosMgmtCommonObjects_ObjectIdentity = ObjectIdentity
rosMgmtCommonObjects = _RosMgmtCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 2, 1, 1)
)
_RosMgmtLoadcfg_ObjectIdentity = ObjectIdentity
rosMgmtLoadcfg = _RosMgmtLoadcfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 2, 1, 1, 1)
)
_RosMgmtLoadcfgScalar_ObjectIdentity = ObjectIdentity
rosMgmtLoadcfgScalar = _RosMgmtLoadcfgScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 2, 1, 1, 1, 1)
)


class _RosMgmtConfigLoadOperation_Type(Integer32):
    """Custom type rosMgmtConfigLoadOperation based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("saving", 2),
          ("erasing", 3),
          ("reboot", 4),
          ("restore", 5),
          ("reload", 6),
          ("backupsaving", 7),
          ("cpoyStaConf2BackConf", 8),
          ("cpoyBackConf2StaConf", 9),
          ("switStaConfBackConf", 10),
          ("backuperasing", 11),
          ("eraseStartupconfig", 12),
          ("eraseStartupconfigAll", 13),
          ("savingall", 14))
    )


_RosMgmtConfigLoadOperation_Type.__name__ = "Integer32"
_RosMgmtConfigLoadOperation_Object = MibScalar
rosMgmtConfigLoadOperation = _RosMgmtConfigLoadOperation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 2, 1, 1, 1, 1, 1),
    _RosMgmtConfigLoadOperation_Type()
)
rosMgmtConfigLoadOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtConfigLoadOperation.setStatus("current")


class _RosMgmtConfigLoadNotificationOnCompletion_Type(TruthValue):
    """Custom type rosMgmtConfigLoadNotificationOnCompletion based on TruthValue"""
    defaultValue = 2


_RosMgmtConfigLoadNotificationOnCompletion_Type.__name__ = "TruthValue"
_RosMgmtConfigLoadNotificationOnCompletion_Object = MibScalar
rosMgmtConfigLoadNotificationOnCompletion = _RosMgmtConfigLoadNotificationOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 2, 1, 1, 1, 1, 2),
    _RosMgmtConfigLoadNotificationOnCompletion_Type()
)
rosMgmtConfigLoadNotificationOnCompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtConfigLoadNotificationOnCompletion.setStatus("current")


class _RosMgmtConfigLoadState_Type(Integer32):
    """Custom type rosMgmtConfigLoadState based on Integer32"""
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
        *(("ready", 1),
          ("running", 2),
          ("successful", 3),
          ("failed", 4))
    )


_RosMgmtConfigLoadState_Type.__name__ = "Integer32"
_RosMgmtConfigLoadState_Object = MibScalar
rosMgmtConfigLoadState = _RosMgmtConfigLoadState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 2, 1, 1, 1, 1, 3),
    _RosMgmtConfigLoadState_Type()
)
rosMgmtConfigLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rosMgmtConfigLoadState.setStatus("current")
_RosMgmtAutoWrite_ObjectIdentity = ObjectIdentity
rosMgmtAutoWrite = _RosMgmtAutoWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 2, 1, 1, 2)
)


class _RosMgmtAutoWritecfgEnable_Type(EnableVar):
    """Custom type rosMgmtAutoWritecfgEnable based on EnableVar"""
    defaultValue = 1


_RosMgmtAutoWritecfgEnable_Type.__name__ = "EnableVar"
_RosMgmtAutoWritecfgEnable_Object = MibScalar
rosMgmtAutoWritecfgEnable = _RosMgmtAutoWritecfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 2, 1, 1, 2, 1),
    _RosMgmtAutoWritecfgEnable_Type()
)
rosMgmtAutoWritecfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAutoWritecfgEnable.setStatus("current")
_RosMgmtAutoWritecfgInterval_Type = Integer32
_RosMgmtAutoWritecfgInterval_Object = MibScalar
rosMgmtAutoWritecfgInterval = _RosMgmtAutoWritecfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 60, 2, 1, 1, 2, 2),
    _RosMgmtAutoWritecfgInterval_Type()
)
rosMgmtAutoWritecfgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rosMgmtAutoWritecfgInterval.setStatus("current")
_RosMgmtCommonConformance_ObjectIdentity = ObjectIdentity
rosMgmtCommonConformance = _RosMgmtCommonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60, 2, 1, 2)
)

# Managed Objects groups


# Notification objects

rosMgmtConfigLoadCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 60, 2, 1, 0, 1)
)
rosMgmtConfigLoadCompletion.setObjects(
      *(("ROSMGMT-COMMON-MANAGEMENT-MIB", "rosMgmtConfigLoadOperation"),
        ("ROSMGMT-COMMON-MANAGEMENT-MIB", "rosMgmtConfigLoadState"))
)
if mibBuilder.loadTexts:
    rosMgmtConfigLoadCompletion.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROSMGMT-COMMON-MANAGEMENT-MIB",
    **{"rosMgmtCommonManagement": rosMgmtCommonManagement,
       "rosMgmtCommonFunctionGroup": rosMgmtCommonFunctionGroup,
       "rosMgmtCommonNotifications": rosMgmtCommonNotifications,
       "rosMgmtConfigLoadCompletion": rosMgmtConfigLoadCompletion,
       "rosMgmtCommonObjects": rosMgmtCommonObjects,
       "rosMgmtLoadcfg": rosMgmtLoadcfg,
       "rosMgmtLoadcfgScalar": rosMgmtLoadcfgScalar,
       "rosMgmtConfigLoadOperation": rosMgmtConfigLoadOperation,
       "rosMgmtConfigLoadNotificationOnCompletion": rosMgmtConfigLoadNotificationOnCompletion,
       "rosMgmtConfigLoadState": rosMgmtConfigLoadState,
       "rosMgmtAutoWrite": rosMgmtAutoWrite,
       "rosMgmtAutoWritecfgEnable": rosMgmtAutoWritecfgEnable,
       "rosMgmtAutoWritecfgInterval": rosMgmtAutoWritecfgInterval,
       "rosMgmtCommonConformance": rosMgmtCommonConformance}
)
