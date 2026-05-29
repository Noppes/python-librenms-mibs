# SNMP MIB module (PRVT-MAC-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-MAC-SECURITY-MIB

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtMacSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109)
)
if mibBuilder.loadTexts:
    prvtMacSecurityMIB.setRevisions(
        ("2010-03-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrvtMacSecLrnProfileNameType(TextualConvention, OctetString):
    status = "current"
    displayHint = "30t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )



class PrvtMacSecWatermarkActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("log", 3),
          ("trap", 4))
    )



class PrvtMacSecSecurityActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operationalShutdown", 1),
          ("trap", 2))
    )



class PrvtMacSecPolicyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portSecurity", 1),
          ("portLimit", 2))
    )



class PrvtMacSecEntryStateType(TextualConvention, Integer32):
    status = "current"
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
        *(("noViolation", 1),
          ("watermarkReached", 2),
          ("maxMacCountReached", 3),
          ("errorState", 4))
    )



# MIB Managed Objects in the order of their OIDs

_PrvtMacSecNotifications_ObjectIdentity = ObjectIdentity
prvtMacSecNotifications = _PrvtMacSecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 0)
)
_PrvtMacSecObjects_ObjectIdentity = ObjectIdentity
prvtMacSecObjects = _PrvtMacSecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1)
)
_PrvtMacSecLrnProfTable_Object = MibTable
prvtMacSecLrnProfTable = _PrvtMacSecLrnProfTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 1)
)
if mibBuilder.loadTexts:
    prvtMacSecLrnProfTable.setStatus("current")
_PrvtMacSecLrnProfEntry_Object = MibTableRow
prvtMacSecLrnProfEntry = _PrvtMacSecLrnProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 1, 1)
)
prvtMacSecLrnProfEntry.setIndexNames(
    (0, "PRVT-MAC-SECURITY-MIB", "prvtMacSecLrnProfName"),
)
if mibBuilder.loadTexts:
    prvtMacSecLrnProfEntry.setStatus("current")
_PrvtMacSecLrnProfName_Type = PrvtMacSecLrnProfileNameType
_PrvtMacSecLrnProfName_Object = MibTableColumn
prvtMacSecLrnProfName = _PrvtMacSecLrnProfName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 1, 1, 1),
    _PrvtMacSecLrnProfName_Type()
)
prvtMacSecLrnProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtMacSecLrnProfName.setStatus("current")
_PrvtMacSecLrnProfRowStatus_Type = RowStatus
_PrvtMacSecLrnProfRowStatus_Object = MibTableColumn
prvtMacSecLrnProfRowStatus = _PrvtMacSecLrnProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 1, 1, 2),
    _PrvtMacSecLrnProfRowStatus_Type()
)
prvtMacSecLrnProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMacSecLrnProfRowStatus.setStatus("current")
_PrvtMacSecLrnProfPolicy_Type = PrvtMacSecPolicyType
_PrvtMacSecLrnProfPolicy_Object = MibTableColumn
prvtMacSecLrnProfPolicy = _PrvtMacSecLrnProfPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 1, 1, 3),
    _PrvtMacSecLrnProfPolicy_Type()
)
prvtMacSecLrnProfPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMacSecLrnProfPolicy.setStatus("current")


class _PrvtMacSecLrnProfMaxMacCount_Type(Unsigned32):
    """Custom type prvtMacSecLrnProfMaxMacCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_PrvtMacSecLrnProfMaxMacCount_Type.__name__ = "Unsigned32"
_PrvtMacSecLrnProfMaxMacCount_Object = MibTableColumn
prvtMacSecLrnProfMaxMacCount = _PrvtMacSecLrnProfMaxMacCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 1, 1, 4),
    _PrvtMacSecLrnProfMaxMacCount_Type()
)
prvtMacSecLrnProfMaxMacCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMacSecLrnProfMaxMacCount.setStatus("current")
_PrvtMacSecLrnProfIgnoreFiltered_Type = TruthValue
_PrvtMacSecLrnProfIgnoreFiltered_Object = MibTableColumn
prvtMacSecLrnProfIgnoreFiltered = _PrvtMacSecLrnProfIgnoreFiltered_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 1, 1, 5),
    _PrvtMacSecLrnProfIgnoreFiltered_Type()
)
prvtMacSecLrnProfIgnoreFiltered.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMacSecLrnProfIgnoreFiltered.setStatus("current")
_PrvtMacSecLrnProfAction_Type = PrvtMacSecSecurityActionType
_PrvtMacSecLrnProfAction_Object = MibTableColumn
prvtMacSecLrnProfAction = _PrvtMacSecLrnProfAction_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 1, 1, 6),
    _PrvtMacSecLrnProfAction_Type()
)
prvtMacSecLrnProfAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMacSecLrnProfAction.setStatus("current")
_PrvtMacSecLrnProfWatermarkAction_Type = PrvtMacSecWatermarkActionType
_PrvtMacSecLrnProfWatermarkAction_Object = MibTableColumn
prvtMacSecLrnProfWatermarkAction = _PrvtMacSecLrnProfWatermarkAction_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 1, 1, 7),
    _PrvtMacSecLrnProfWatermarkAction_Type()
)
prvtMacSecLrnProfWatermarkAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMacSecLrnProfWatermarkAction.setStatus("current")


class _PrvtMacSecLrnProfWatermarkCount_Type(Unsigned32):
    """Custom type prvtMacSecLrnProfWatermarkCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_PrvtMacSecLrnProfWatermarkCount_Type.__name__ = "Unsigned32"
_PrvtMacSecLrnProfWatermarkCount_Object = MibTableColumn
prvtMacSecLrnProfWatermarkCount = _PrvtMacSecLrnProfWatermarkCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 1, 1, 8),
    _PrvtMacSecLrnProfWatermarkCount_Type()
)
prvtMacSecLrnProfWatermarkCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMacSecLrnProfWatermarkCount.setStatus("current")
_PrvtMacSecIfTable_Object = MibTable
prvtMacSecIfTable = _PrvtMacSecIfTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 2)
)
if mibBuilder.loadTexts:
    prvtMacSecIfTable.setStatus("current")
_PrvtMacSecIfEntry_Object = MibTableRow
prvtMacSecIfEntry = _PrvtMacSecIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 2, 1)
)
prvtMacSecIfEntry.setIndexNames(
    (0, "PRVT-MAC-SECURITY-MIB", "prvtMacSecIfName"),
)
if mibBuilder.loadTexts:
    prvtMacSecIfEntry.setStatus("current")
_PrvtMacSecIfName_Type = OctetString
_PrvtMacSecIfName_Object = MibTableColumn
prvtMacSecIfName = _PrvtMacSecIfName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 2, 1, 1),
    _PrvtMacSecIfName_Type()
)
prvtMacSecIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtMacSecIfName.setStatus("current")
_PrvtMacSecIfRowStatus_Type = RowStatus
_PrvtMacSecIfRowStatus_Object = MibTableColumn
prvtMacSecIfRowStatus = _PrvtMacSecIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 2, 1, 2),
    _PrvtMacSecIfRowStatus_Type()
)
prvtMacSecIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMacSecIfRowStatus.setStatus("current")
_PrvtMacSecIfProfile_Type = PrvtMacSecLrnProfileNameType
_PrvtMacSecIfProfile_Object = MibTableColumn
prvtMacSecIfProfile = _PrvtMacSecIfProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 2, 1, 3),
    _PrvtMacSecIfProfile_Type()
)
prvtMacSecIfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMacSecIfProfile.setStatus("current")
_PrvtMacSecIfCurrMacCount_Type = Unsigned32
_PrvtMacSecIfCurrMacCount_Object = MibTableColumn
prvtMacSecIfCurrMacCount = _PrvtMacSecIfCurrMacCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 2, 1, 4),
    _PrvtMacSecIfCurrMacCount_Type()
)
prvtMacSecIfCurrMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMacSecIfCurrMacCount.setStatus("current")
_PrvtMacSecIfState_Type = PrvtMacSecEntryStateType
_PrvtMacSecIfState_Object = MibTableColumn
prvtMacSecIfState = _PrvtMacSecIfState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 1, 2, 1, 5),
    _PrvtMacSecIfState_Type()
)
prvtMacSecIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMacSecIfState.setStatus("current")

# Managed Objects groups


# Notification objects

portSecurityWmarkViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 0, 1)
)
portSecurityWmarkViolation.setObjects(
    ("PRVT-MAC-SECURITY-MIB", "prvtMacSecIfName")
)
if mibBuilder.loadTexts:
    portSecurityWmarkViolation.setStatus(
        "current"
    )

portSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 109, 0, 2)
)
portSecurityViolation.setObjects(
    ("PRVT-MAC-SECURITY-MIB", "prvtMacSecIfName")
)
if mibBuilder.loadTexts:
    portSecurityViolation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-MAC-SECURITY-MIB",
    **{"PrvtMacSecLrnProfileNameType": PrvtMacSecLrnProfileNameType,
       "PrvtMacSecWatermarkActionType": PrvtMacSecWatermarkActionType,
       "PrvtMacSecSecurityActionType": PrvtMacSecSecurityActionType,
       "PrvtMacSecPolicyType": PrvtMacSecPolicyType,
       "PrvtMacSecEntryStateType": PrvtMacSecEntryStateType,
       "prvtMacSecurityMIB": prvtMacSecurityMIB,
       "prvtMacSecNotifications": prvtMacSecNotifications,
       "portSecurityWmarkViolation": portSecurityWmarkViolation,
       "portSecurityViolation": portSecurityViolation,
       "prvtMacSecObjects": prvtMacSecObjects,
       "prvtMacSecLrnProfTable": prvtMacSecLrnProfTable,
       "prvtMacSecLrnProfEntry": prvtMacSecLrnProfEntry,
       "prvtMacSecLrnProfName": prvtMacSecLrnProfName,
       "prvtMacSecLrnProfRowStatus": prvtMacSecLrnProfRowStatus,
       "prvtMacSecLrnProfPolicy": prvtMacSecLrnProfPolicy,
       "prvtMacSecLrnProfMaxMacCount": prvtMacSecLrnProfMaxMacCount,
       "prvtMacSecLrnProfIgnoreFiltered": prvtMacSecLrnProfIgnoreFiltered,
       "prvtMacSecLrnProfAction": prvtMacSecLrnProfAction,
       "prvtMacSecLrnProfWatermarkAction": prvtMacSecLrnProfWatermarkAction,
       "prvtMacSecLrnProfWatermarkCount": prvtMacSecLrnProfWatermarkCount,
       "prvtMacSecIfTable": prvtMacSecIfTable,
       "prvtMacSecIfEntry": prvtMacSecIfEntry,
       "prvtMacSecIfName": prvtMacSecIfName,
       "prvtMacSecIfRowStatus": prvtMacSecIfRowStatus,
       "prvtMacSecIfProfile": prvtMacSecIfProfile,
       "prvtMacSecIfCurrMacCount": prvtMacSecIfCurrMacCount,
       "prvtMacSecIfState": prvtMacSecIfState}
)
