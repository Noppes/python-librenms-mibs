# SNMP MIB module (G6-FACTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\microsens\G6-FACTORY-MIB

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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

device = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1)
)
if mibBuilder.loadTexts:
    device.setRevisions(
        ("2023-02-14 11:27",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Factory_ObjectIdentity = ObjectIdentity
factory = _Factory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32)
)
_FactoryArticleNumber_Type = DisplayString
_FactoryArticleNumber_Object = MibScalar
factoryArticleNumber = _FactoryArticleNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 1),
    _FactoryArticleNumber_Type()
)
factoryArticleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryArticleNumber.setStatus("current")
_FactorySerialNumber_Type = DisplayString
_FactorySerialNumber_Object = MibScalar
factorySerialNumber = _FactorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 2),
    _FactorySerialNumber_Type()
)
factorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factorySerialNumber.setStatus("current")
_FactoryDeviceMac_Type = MacAddress
_FactoryDeviceMac_Object = MibScalar
factoryDeviceMac = _FactoryDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 3),
    _FactoryDeviceMac_Type()
)
factoryDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryDeviceMac.setStatus("current")


class _FactoryNumberOfMacs_Type(Integer32):
    """Custom type factoryNumberOfMacs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FactoryNumberOfMacs_Type.__name__ = "Integer32"
_FactoryNumberOfMacs_Object = MibScalar
factoryNumberOfMacs = _FactoryNumberOfMacs_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 4),
    _FactoryNumberOfMacs_Type()
)
factoryNumberOfMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryNumberOfMacs.setStatus("current")
_FactoryHardwareVersion_Type = DisplayString
_FactoryHardwareVersion_Object = MibScalar
factoryHardwareVersion = _FactoryHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 5),
    _FactoryHardwareVersion_Type()
)
factoryHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryHardwareVersion.setStatus("current")
_FactoryBoardId_Type = Unsigned32
_FactoryBoardId_Object = MibScalar
factoryBoardId = _FactoryBoardId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 6),
    _FactoryBoardId_Type()
)
factoryBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryBoardId.setStatus("current")
_FactoryProjectNumber_Type = DisplayString
_FactoryProjectNumber_Object = MibScalar
factoryProjectNumber = _FactoryProjectNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 7),
    _FactoryProjectNumber_Type()
)
factoryProjectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryProjectNumber.setStatus("current")


class _FactoryMechanicalFeatures_Type(Bits):
    """Custom type factoryMechanicalFeatures based on Bits"""
    namedValues = NamedValues(
        *(("desktop", 0),
          ("rail", 1),
          ("ductVertical", 2),
          ("ductHorizontal", 3),
          ("rack", 4),
          ("stackable", 5),
          ("unused6", 6),
          ("unused7", 7),
          ("dc", 8),
          ("ac", 9),
          ("dualPwr", 10),
          ("unused11", 11),
          ("extTemp", 12),
          ("extSupply", 13),
          ("exSecure", 14),
          ("unused15", 15),
          ("unused16", 16),
          ("microSd", 17),
          ("sdcard", 18),
          ("internalMemory", 19),
          ("unused20", 20),
          ("unused21", 21),
          ("ip30", 22),
          ("ip42", 23),
          ("ip44", 24),
          ("ip55", 25),
          ("ip67", 26),
          ("unused27", 27),
          ("unused28", 28),
          ("unused29", 29),
          ("unused30", 30),
          ("unused31", 31))
    )

_FactoryMechanicalFeatures_Type.__name__ = "Bits"
_FactoryMechanicalFeatures_Object = MibScalar
factoryMechanicalFeatures = _FactoryMechanicalFeatures_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 8),
    _FactoryMechanicalFeatures_Type()
)
factoryMechanicalFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryMechanicalFeatures.setStatus("current")


class _FactoryHardwareFeatures_Type(Bits):
    """Custom type factoryHardwareFeatures based on Bits"""
    namedValues = NamedValues(
        *(("poePlus", 0),
          ("poePse", 1),
          ("poePd", 2),
          ("unused3", 3),
          ("railway", 4),
          ("substation", 5),
          ("eee", 6),
          ("synce", 7),
          ("ms1588", 8),
          ("usb", 9),
          ("relays", 10),
          ("rtc", 11),
          ("max100m", 12),
          ("unused13", 13),
          ("unused14", 14),
          ("csfp", 15),
          ("sfp", 16),
          ("lc", 17),
          ("sc", 18),
          ("st", 19),
          ("e2000", 20),
          ("slc", 21),
          ("unused22", 22),
          ("unused23", 23),
          ("unused24", 24),
          ("unused25", 25),
          ("unused26", 26),
          ("unused27", 27),
          ("unused28", 28),
          ("unused29", 29),
          ("unused30", 30),
          ("unused31", 31))
    )

_FactoryHardwareFeatures_Type.__name__ = "Bits"
_FactoryHardwareFeatures_Object = MibScalar
factoryHardwareFeatures = _FactoryHardwareFeatures_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 9),
    _FactoryHardwareFeatures_Type()
)
factoryHardwareFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryHardwareFeatures.setStatus("current")
_FactoryCompanyName_Type = DisplayString
_FactoryCompanyName_Object = MibScalar
factoryCompanyName = _FactoryCompanyName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 10),
    _FactoryCompanyName_Type()
)
factoryCompanyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryCompanyName.setStatus("current")
_FactoryCompanyShort_Type = DisplayString
_FactoryCompanyShort_Object = MibScalar
factoryCompanyShort = _FactoryCompanyShort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 11),
    _FactoryCompanyShort_Type()
)
factoryCompanyShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryCompanyShort.setStatus("current")
_FactoryWebLink_Type = DisplayString
_FactoryWebLink_Object = MibScalar
factoryWebLink = _FactoryWebLink_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 12),
    _FactoryWebLink_Type()
)
factoryWebLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryWebLink.setStatus("current")
_FactoryWebDescription_Type = DisplayString
_FactoryWebDescription_Object = MibScalar
factoryWebDescription = _FactoryWebDescription_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 13),
    _FactoryWebDescription_Type()
)
factoryWebDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    factoryWebDescription.setStatus("current")
_FactoryCustomInfo_Type = DisplayString
_FactoryCustomInfo_Object = MibScalar
factoryCustomInfo = _FactoryCustomInfo_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 14),
    _FactoryCustomInfo_Type()
)
factoryCustomInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    factoryCustomInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-FACTORY-MIB",
    **{"device": device,
       "factory": factory,
       "factoryArticleNumber": factoryArticleNumber,
       "factorySerialNumber": factorySerialNumber,
       "factoryDeviceMac": factoryDeviceMac,
       "factoryNumberOfMacs": factoryNumberOfMacs,
       "factoryHardwareVersion": factoryHardwareVersion,
       "factoryBoardId": factoryBoardId,
       "factoryProjectNumber": factoryProjectNumber,
       "factoryMechanicalFeatures": factoryMechanicalFeatures,
       "factoryHardwareFeatures": factoryHardwareFeatures,
       "factoryCompanyName": factoryCompanyName,
       "factoryCompanyShort": factoryCompanyShort,
       "factoryWebLink": factoryWebLink,
       "factoryWebDescription": factoryWebDescription,
       "factoryCustomInfo": factoryCustomInfo}
)
