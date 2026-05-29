# SNMP MIB module (ARRIS-D5-ENT-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\d5\ARRIS-D5-ENT-CHASSIS-MIB

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

(entPhysicalEntry,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalEntry",
    "entPhysicalIndex")

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

arrisEntChassisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6)
)
if mibBuilder.loadTexts:
    arrisEntChassisMIB.setRevisions(
        ("2005-12-07 00:00",
         "2010-09-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CardType(TextualConvention, Integer32):
    status = "current"
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
        *(("notApplicable", 0),
          ("mon", 1),
          ("wan", 2),
          ("qam", 3),
          ("doc", 4),
          ("powermodule", 5),
          ("fan", 6))
    )



class AdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("up", 1),
          ("down", 2))
    )



class OperationalState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("is", 1),
          ("oos", 2))
    )



class OperationalSubState(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("manual", 1),
          ("fault", 2),
          ("fwPump", 3),
          ("initializing", 4),
          ("alarm", 5),
          ("unequipped", 6),
          ("detecting", 7),
          ("upgrading", 8),
          ("diagnostic", 9))
    )



class SlotOwner(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("wan7", 7),
          ("wan8", 8))
    )



# MIB Managed Objects in the order of their OIDs

_ArrisEntChassisObjects_ObjectIdentity = ObjectIdentity
arrisEntChassisObjects = _ArrisEntChassisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 1)
)
_ArrisEntTable_Object = MibTable
arrisEntTable = _ArrisEntTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    arrisEntTable.setStatus("current")
_ArrisEntEntry_Object = MibTableRow
arrisEntEntry = _ArrisEntEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    arrisEntEntry.setStatus("current")
_ArrisEntProvCardType_Type = CardType
_ArrisEntProvCardType_Object = MibTableColumn
arrisEntProvCardType = _ArrisEntProvCardType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 1, 1, 1, 1),
    _ArrisEntProvCardType_Type()
)
arrisEntProvCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisEntProvCardType.setStatus("current")
_ArrisEntDetCardType_Type = CardType
_ArrisEntDetCardType_Object = MibTableColumn
arrisEntDetCardType = _ArrisEntDetCardType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 1, 1, 1, 2),
    _ArrisEntDetCardType_Type()
)
arrisEntDetCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisEntDetCardType.setStatus("current")
_ArrisEntAdminState_Type = AdminState
_ArrisEntAdminState_Object = MibTableColumn
arrisEntAdminState = _ArrisEntAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 1, 1, 1, 3),
    _ArrisEntAdminState_Type()
)
arrisEntAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisEntAdminState.setStatus("current")
_ArrisEntOperState_Type = OperationalState
_ArrisEntOperState_Object = MibTableColumn
arrisEntOperState = _ArrisEntOperState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 1, 1, 1, 4),
    _ArrisEntOperState_Type()
)
arrisEntOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisEntOperState.setStatus("current")
_ArrisEntOperSubState_Type = OperationalSubState
_ArrisEntOperSubState_Object = MibTableColumn
arrisEntOperSubState = _ArrisEntOperSubState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 1, 1, 1, 5),
    _ArrisEntOperSubState_Type()
)
arrisEntOperSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisEntOperSubState.setStatus("current")


class _ArrisEntProductCode_Type(OctetString):
    """Custom type arrisEntProductCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisEntProductCode_Type.__name__ = "OctetString"
_ArrisEntProductCode_Object = MibTableColumn
arrisEntProductCode = _ArrisEntProductCode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 1, 1, 1, 6),
    _ArrisEntProductCode_Type()
)
arrisEntProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisEntProductCode.setStatus("current")


class _ArrisEntProductRev_Type(OctetString):
    """Custom type arrisEntProductRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisEntProductRev_Type.__name__ = "OctetString"
_ArrisEntProductRev_Object = MibTableColumn
arrisEntProductRev = _ArrisEntProductRev_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 1, 1, 1, 7),
    _ArrisEntProductRev_Type()
)
arrisEntProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisEntProductRev.setStatus("current")
_ArrisEntSlotOwner_Type = SlotOwner
_ArrisEntSlotOwner_Object = MibTableColumn
arrisEntSlotOwner = _ArrisEntSlotOwner_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 1, 1, 1, 8),
    _ArrisEntSlotOwner_Type()
)
arrisEntSlotOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisEntSlotOwner.setStatus("current")
_ArrisEntChassisConformance_ObjectIdentity = ObjectIdentity
arrisEntChassisConformance = _ArrisEntChassisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 2)
)
_ArrisEntChassisGroups_ObjectIdentity = ObjectIdentity
arrisEntChassisGroups = _ArrisEntChassisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 2, 1)
)
_ArrisEntChassisCompliances_ObjectIdentity = ObjectIdentity
arrisEntChassisCompliances = _ArrisEntChassisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 2, 2)
)
entPhysicalEntry.registerAugmentions(
    ("ARRIS-D5-ENT-CHASSIS-MIB",
     "arrisEntEntry")
)
arrisEntEntry.setIndexNames(*entPhysicalEntry.getIndexNames())

# Managed Objects groups

arrisEntChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 2, 1, 1)
)
arrisEntChassisGroup.setObjects(
      *(("ARRIS-D5-ENT-CHASSIS-MIB", "arrisEntProvCardType"),
        ("ARRIS-D5-ENT-CHASSIS-MIB", "arrisEntDetCardType"),
        ("ARRIS-D5-ENT-CHASSIS-MIB", "arrisEntAdminState"),
        ("ARRIS-D5-ENT-CHASSIS-MIB", "arrisEntOperState"),
        ("ARRIS-D5-ENT-CHASSIS-MIB", "arrisEntOperSubState"),
        ("ARRIS-D5-ENT-CHASSIS-MIB", "arrisEntSlotOwner"))
)
if mibBuilder.loadTexts:
    arrisEntChassisGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arrisEntChassisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 6, 2, 2, 1)
)
arrisEntChassisCompliance.setObjects(
    ("ARRIS-D5-ENT-CHASSIS-MIB", "arrisEntChassisGroup")
)
if mibBuilder.loadTexts:
    arrisEntChassisCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-D5-ENT-CHASSIS-MIB",
    **{"CardType": CardType,
       "AdminState": AdminState,
       "OperationalState": OperationalState,
       "OperationalSubState": OperationalSubState,
       "SlotOwner": SlotOwner,
       "arrisEntChassisMIB": arrisEntChassisMIB,
       "arrisEntChassisObjects": arrisEntChassisObjects,
       "arrisEntTable": arrisEntTable,
       "arrisEntEntry": arrisEntEntry,
       "arrisEntProvCardType": arrisEntProvCardType,
       "arrisEntDetCardType": arrisEntDetCardType,
       "arrisEntAdminState": arrisEntAdminState,
       "arrisEntOperState": arrisEntOperState,
       "arrisEntOperSubState": arrisEntOperSubState,
       "arrisEntProductCode": arrisEntProductCode,
       "arrisEntProductRev": arrisEntProductRev,
       "arrisEntSlotOwner": arrisEntSlotOwner,
       "arrisEntChassisConformance": arrisEntChassisConformance,
       "arrisEntChassisGroups": arrisEntChassisGroups,
       "arrisEntChassisGroup": arrisEntChassisGroup,
       "arrisEntChassisCompliances": arrisEntChassisCompliances,
       "arrisEntChassisCompliance": arrisEntChassisCompliance}
)
