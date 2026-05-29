# SNMP MIB module (AX-LOGIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-LOGIN-MIB

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

axLogin = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52)
)
if mibBuilder.loadTexts:
    axLogin.setRevisions(
        ("2013-02-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxLoginName_Type = DisplayString
_AxLoginName_Object = MibScalar
axLoginName = _AxLoginName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 1),
    _AxLoginName_Type()
)
axLoginName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axLoginName.setStatus("current")
_AxLoginTime_Type = DisplayString
_AxLoginTime_Object = MibScalar
axLoginTime = _AxLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 2),
    _AxLoginTime_Type()
)
axLoginTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axLoginTime.setStatus("current")
_AxLogoutTime_Type = DisplayString
_AxLogoutTime_Object = MibScalar
axLogoutTime = _AxLogoutTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 3),
    _AxLogoutTime_Type()
)
axLogoutTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axLogoutTime.setStatus("current")
_AxLoginFailureTime_Type = DisplayString
_AxLoginFailureTime_Object = MibScalar
axLoginFailureTime = _AxLoginFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 4),
    _AxLoginFailureTime_Type()
)
axLoginFailureTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axLoginFailureTime.setStatus("current")
_AxLoginLocation_Type = DisplayString
_AxLoginLocation_Object = MibScalar
axLoginLocation = _AxLoginLocation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 5),
    _AxLoginLocation_Type()
)
axLoginLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axLoginLocation.setStatus("current")
_AxLoginLine_Type = DisplayString
_AxLoginLine_Object = MibScalar
axLoginLine = _AxLoginLine_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 6),
    _AxLoginLine_Type()
)
axLoginLine.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axLoginLine.setStatus("current")


class _AxLogoutStatus_Type(Integer32):
    """Custom type axLogoutStatus based on Integer32"""
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
        *(("error", 1),
          ("success", 2),
          ("timeout", 3),
          ("disconnect", 4),
          ("force", 5))
    )


_AxLogoutStatus_Type.__name__ = "Integer32"
_AxLogoutStatus_Object = MibScalar
axLogoutStatus = _AxLogoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 7),
    _AxLogoutStatus_Type()
)
axLogoutStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axLogoutStatus.setStatus("current")
_AxLoginTrap_ObjectIdentity = ObjectIdentity
axLoginTrap = _AxLoginTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 10)
)
_AxLoginTrapPrefix_ObjectIdentity = ObjectIdentity
axLoginTrapPrefix = _AxLoginTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 10, 0)
)
_AxLoginConformance_ObjectIdentity = ObjectIdentity
axLoginConformance = _AxLoginConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 1000)
)
_AxLoginCompliances_ObjectIdentity = ObjectIdentity
axLoginCompliances = _AxLoginCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 1000, 1)
)
_AxLoginGroups_ObjectIdentity = ObjectIdentity
axLoginGroups = _AxLoginGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 1000, 2)
)

# Managed Objects groups

axLoginGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 1000, 2, 1)
)
axLoginGroup.setObjects(
      *(("AX-LOGIN-MIB", "axLoginName"),
        ("AX-LOGIN-MIB", "axLoginTime"),
        ("AX-LOGIN-MIB", "axLogoutTime"),
        ("AX-LOGIN-MIB", "axLoginFailureTime"),
        ("AX-LOGIN-MIB", "axLoginLocation"),
        ("AX-LOGIN-MIB", "axLoginLine"),
        ("AX-LOGIN-MIB", "axLogoutStatus"))
)
if mibBuilder.loadTexts:
    axLoginGroup.setStatus("current")


# Notification objects

axLoginSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 10, 0, 1)
)
axLoginSuccessTrap.setObjects(
      *(("AX-LOGIN-MIB", "axLoginName"),
        ("AX-LOGIN-MIB", "axLoginTime"),
        ("AX-LOGIN-MIB", "axLoginLocation"),
        ("AX-LOGIN-MIB", "axLoginLine"))
)
if mibBuilder.loadTexts:
    axLoginSuccessTrap.setStatus(
        "current"
    )

axLoginFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 10, 0, 2)
)
axLoginFailureTrap.setObjects(
      *(("AX-LOGIN-MIB", "axLoginName"),
        ("AX-LOGIN-MIB", "axLoginFailureTime"),
        ("AX-LOGIN-MIB", "axLoginLocation"),
        ("AX-LOGIN-MIB", "axLoginLine"))
)
if mibBuilder.loadTexts:
    axLoginFailureTrap.setStatus(
        "current"
    )

axLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 10, 0, 3)
)
axLogoutTrap.setObjects(
      *(("AX-LOGIN-MIB", "axLoginName"),
        ("AX-LOGIN-MIB", "axLoginTime"),
        ("AX-LOGIN-MIB", "axLogoutTime"),
        ("AX-LOGIN-MIB", "axLoginLocation"),
        ("AX-LOGIN-MIB", "axLoginLine"),
        ("AX-LOGIN-MIB", "axLogoutStatus"))
)
if mibBuilder.loadTexts:
    axLogoutTrap.setStatus(
        "current"
    )


# Notifications groups

axLoginNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 1000, 2, 10)
)
axLoginNotificationGroup.setObjects(
      *(("AX-LOGIN-MIB", "axLoginSuccessTrap"),
        ("AX-LOGIN-MIB", "axLoginFailureTrap"),
        ("AX-LOGIN-MIB", "axLogoutTrap"))
)
if mibBuilder.loadTexts:
    axLoginNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

axLoginCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 52, 1000, 1, 1)
)
axLoginCompliance.setObjects(
      *(("AX-LOGIN-MIB", "axLoginGroup"),
        ("AX-LOGIN-MIB", "axLoginNotificationGroup"))
)
if mibBuilder.loadTexts:
    axLoginCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-LOGIN-MIB",
    **{"axLogin": axLogin,
       "axLoginName": axLoginName,
       "axLoginTime": axLoginTime,
       "axLogoutTime": axLogoutTime,
       "axLoginFailureTime": axLoginFailureTime,
       "axLoginLocation": axLoginLocation,
       "axLoginLine": axLoginLine,
       "axLogoutStatus": axLogoutStatus,
       "axLoginTrap": axLoginTrap,
       "axLoginTrapPrefix": axLoginTrapPrefix,
       "axLoginSuccessTrap": axLoginSuccessTrap,
       "axLoginFailureTrap": axLoginFailureTrap,
       "axLogoutTrap": axLogoutTrap,
       "axLoginConformance": axLoginConformance,
       "axLoginCompliances": axLoginCompliances,
       "axLoginCompliance": axLoginCompliance,
       "axLoginGroups": axLoginGroups,
       "axLoginGroup": axLoginGroup,
       "axLoginNotificationGroup": axLoginNotificationGroup}
)
