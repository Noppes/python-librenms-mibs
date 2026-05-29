# SNMP MIB module (GRANDSTREAM-GWN-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\grandstream\GRANDSTREAM-GWN-PRODUCTS-MIB

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

(gwnProducts,) = mibBuilder.importSymbols(
    "GRANDSTREAM-GWN-ROOT-MIB",
    "gwnProducts")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

gwnAp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 1)
)

gwnRouter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 2)
)

gwnProductsCommonSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GwnSystemInfo_ObjectIdentity = ObjectIdentity
gwnSystemInfo = _GwnSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42397, 1, 3, 1)
)
_GwnDeviceModel_Type = DisplayString
_GwnDeviceModel_Object = MibScalar
gwnDeviceModel = _GwnDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 3, 1, 1),
    _GwnDeviceModel_Type()
)
gwnDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnDeviceModel.setStatus("current")
_GwnDeviceName_Type = DisplayString
_GwnDeviceName_Object = MibScalar
gwnDeviceName = _GwnDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 3, 1, 2),
    _GwnDeviceName_Type()
)
gwnDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnDeviceName.setStatus("current")
_GwnDeviceMac_Type = DisplayString
_GwnDeviceMac_Object = MibScalar
gwnDeviceMac = _GwnDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 3, 1, 3),
    _GwnDeviceMac_Type()
)
gwnDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnDeviceMac.setStatus("current")
_GwnDeviceVersion_Type = DisplayString
_GwnDeviceVersion_Object = MibScalar
gwnDeviceVersion = _GwnDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 3, 1, 4),
    _GwnDeviceVersion_Type()
)
gwnDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnDeviceVersion.setStatus("current")
_GwnDeviceIPv4Address_Type = DisplayString
_GwnDeviceIPv4Address_Object = MibScalar
gwnDeviceIPv4Address = _GwnDeviceIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 3, 1, 5),
    _GwnDeviceIPv4Address_Type()
)
gwnDeviceIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnDeviceIPv4Address.setStatus("current")
_GwnDeviceIPv6Address_Type = DisplayString
_GwnDeviceIPv6Address_Object = MibScalar
gwnDeviceIPv6Address = _GwnDeviceIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 3, 1, 6),
    _GwnDeviceIPv6Address_Type()
)
gwnDeviceIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnDeviceIPv6Address.setStatus("current")
_GwnDeviceUptime_Type = Counter32
_GwnDeviceUptime_Object = MibScalar
gwnDeviceUptime = _GwnDeviceUptime_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 3, 1, 7),
    _GwnDeviceUptime_Type()
)
gwnDeviceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnDeviceUptime.setStatus("current")
_GwnSnmpUptime_Type = TimeTicks
_GwnSnmpUptime_Object = MibScalar
gwnSnmpUptime = _GwnSnmpUptime_Object(
    (1, 3, 6, 1, 4, 1, 42397, 1, 3, 1, 8),
    _GwnSnmpUptime_Type()
)
gwnSnmpUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwnSnmpUptime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GRANDSTREAM-GWN-PRODUCTS-MIB",
    **{"gwnAp": gwnAp,
       "gwnRouter": gwnRouter,
       "gwnProductsCommonSystem": gwnProductsCommonSystem,
       "gwnSystemInfo": gwnSystemInfo,
       "gwnDeviceModel": gwnDeviceModel,
       "gwnDeviceName": gwnDeviceName,
       "gwnDeviceMac": gwnDeviceMac,
       "gwnDeviceVersion": gwnDeviceVersion,
       "gwnDeviceIPv4Address": gwnDeviceIPv4Address,
       "gwnDeviceIPv6Address": gwnDeviceIPv6Address,
       "gwnDeviceUptime": gwnDeviceUptime,
       "gwnSnmpUptime": gwnSnmpUptime}
)
