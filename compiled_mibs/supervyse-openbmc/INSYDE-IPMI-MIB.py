# SNMP MIB module (INSYDE-IPMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\supervyse-openbmc\INSYDE-IPMI-MIB

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

insyde = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45065)
)
if mibBuilder.loadTexts:
    insyde.setRevisions(
        ("2017-10-03 14:00",
         "2009-03-20 11:50")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Web_ObjectIdentity = ObjectIdentity
web = _Web_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45065, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45065, 1, 1)
)
_SystemInfo_Type = DisplayString
_SystemInfo_Object = MibScalar
systemInfo = _SystemInfo_Object(
    (1, 3, 6, 1, 4, 1, 45065, 1, 1, 1),
    _SystemInfo_Type()
)
systemInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemInfo.setStatus("current")


class _HostPwrStatus_Type(Integer32):
    """Custom type hostPwrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1),
          ("Reset", 2))
    )


_HostPwrStatus_Type.__name__ = "Integer32"
_HostPwrStatus_Object = MibScalar
hostPwrStatus = _HostPwrStatus_Object(
    (1, 3, 6, 1, 4, 1, 45065, 1, 1, 1, 1),
    _HostPwrStatus_Type()
)
hostPwrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostPwrStatus.setStatus("current")
_BmcFWBLDTime_Type = DisplayString
_BmcFWBLDTime_Object = MibScalar
bmcFWBLDTime = _BmcFWBLDTime_Object(
    (1, 3, 6, 1, 4, 1, 45065, 1, 1, 1, 2),
    _BmcFWBLDTime_Type()
)
bmcFWBLDTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcFWBLDTime.setStatus("current")
_BmcFWversion_Type = DisplayString
_BmcFWversion_Object = MibScalar
bmcFWversion = _BmcFWversion_Object(
    (1, 3, 6, 1, 4, 1, 45065, 1, 1, 1, 3),
    _BmcFWversion_Type()
)
bmcFWversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmcFWversion.setStatus("current")
_BakBmcFWversion_Type = DisplayString
_BakBmcFWversion_Object = MibScalar
bakBmcFWversion = _BakBmcFWversion_Object(
    (1, 3, 6, 1, 4, 1, 45065, 1, 1, 1, 4),
    _BakBmcFWversion_Type()
)
bakBmcFWversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bakBmcFWversion.setStatus("current")
_BuildID_Type = DisplayString
_BuildID_Object = MibScalar
buildID = _BuildID_Object(
    (1, 3, 6, 1, 4, 1, 45065, 1, 1, 1, 5),
    _BuildID_Type()
)
buildID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buildID.setStatus("current")
_BaseboardSN_Type = DisplayString
_BaseboardSN_Object = MibScalar
baseboardSN = _BaseboardSN_Object(
    (1, 3, 6, 1, 4, 1, 45065, 1, 1, 1, 6),
    _BaseboardSN_Type()
)
baseboardSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseboardSN.setStatus("current")


class _SysLEDStatus_Type(Integer32):
    """Custom type sysLEDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Off", 0),
          ("On", 1),
          ("Blink", 2))
    )


_SysLEDStatus_Type.__name__ = "Integer32"
_SysLEDStatus_Object = MibScalar
sysLEDStatus = _SysLEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 45065, 1, 1, 1, 8),
    _SysLEDStatus_Type()
)
sysLEDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLEDStatus.setStatus("current")
_ServerHealth_ObjectIdentity = ObjectIdentity
serverHealth = _ServerHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45065, 1, 2)
)
_SensorTable_Object = MibTable
sensorTable = _SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 45065, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sensorTable.setStatus("current")
_SensorEntry_Object = MibTableRow
sensorEntry = _SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 45065, 1, 2, 1, 1)
)
sensorEntry.setIndexNames(
    (0, "INSYDE-IPMI-MIB", "sensorNumber"),
)
if mibBuilder.loadTexts:
    sensorEntry.setStatus("current")


class _SensorNumber_Type(Integer32):
    """Custom type sensorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SensorNumber_Type.__name__ = "Integer32"
_SensorNumber_Object = MibTableColumn
sensorNumber = _SensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 45065, 1, 2, 1, 1, 1),
    _SensorNumber_Type()
)
sensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorNumber.setStatus("current")
_SensorHumanReading_Type = DisplayString
_SensorHumanReading_Object = MibTableColumn
sensorHumanReading = _SensorHumanReading_Object(
    (1, 3, 6, 1, 4, 1, 45065, 1, 2, 1, 1, 13),
    _SensorHumanReading_Type()
)
sensorHumanReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorHumanReading.setStatus("current")
_SensorName_Type = DisplayString
_SensorName_Object = MibTableColumn
sensorName = _SensorName_Object(
    (1, 3, 6, 1, 4, 1, 45065, 1, 2, 1, 1, 22),
    _SensorName_Type()
)
sensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INSYDE-IPMI-MIB",
    **{"insyde": insyde,
       "web": web,
       "system": system,
       "systemInfo": systemInfo,
       "hostPwrStatus": hostPwrStatus,
       "bmcFWBLDTime": bmcFWBLDTime,
       "bmcFWversion": bmcFWversion,
       "bakBmcFWversion": bakBmcFWversion,
       "buildID": buildID,
       "baseboardSN": baseboardSN,
       "sysLEDStatus": sysLEDStatus,
       "serverHealth": serverHealth,
       "sensorTable": sensorTable,
       "sensorEntry": sensorEntry,
       "sensorNumber": sensorNumber,
       "sensorHumanReading": sensorHumanReading,
       "sensorName": sensorName}
)
