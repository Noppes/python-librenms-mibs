# SNMP MIB module (FIBROLAN-MIB-DEVICECONVERTER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-DEVICECONVERTER

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

(flMsChassisModuleMvIndex,
 flMsChassisMvIndex) = mibBuilder.importSymbols(
    "FIBROLAN-MIB-METRO-STAR-MV",
    "flMsChassisModuleMvIndex",
    "flMsChassisMvIndex")

(flMsModuleMvChannelIndex,) = mibBuilder.importSymbols(
    "FIBROLAN-MIB-MSMODULE",
    "flMsModuleMvChannelIndex")

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

flConverter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fibrolan_ObjectIdentity = ObjectIdentity
fibrolan = _Fibrolan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467)
)
_FibrolanSNMP_ObjectIdentity = ObjectIdentity
fibrolanSNMP = _FibrolanSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100)
)
_FlMaRemoteDevice_ObjectIdentity = ObjectIdentity
flMaRemoteDevice = _FlMaRemoteDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50)
)
_FlConverterMIBConformance_ObjectIdentity = ObjectIdentity
flConverterMIBConformance = _FlConverterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 1)
)
_FlConverterMIBCompliances_ObjectIdentity = ObjectIdentity
flConverterMIBCompliances = _FlConverterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 1, 1)
)
_FlConverterMIBGroups_ObjectIdentity = ObjectIdentity
flConverterMIBGroups = _FlConverterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 1, 2)
)
_FlConverterDevice_ObjectIdentity = ObjectIdentity
flConverterDevice = _FlConverterDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 10)
)
_FlConverterDeviceConfigTable_Object = MibTable
flConverterDeviceConfigTable = _FlConverterDeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 10, 1)
)
if mibBuilder.loadTexts:
    flConverterDeviceConfigTable.setStatus("current")
_FlConverterDeviceConfigEntry_Object = MibTableRow
flConverterDeviceConfigEntry = _FlConverterDeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 10, 1, 1)
)
flConverterDeviceConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
)
if mibBuilder.loadTexts:
    flConverterDeviceConfigEntry.setStatus("current")


class _FlConverterDeviceReset_Type(Integer32):
    """Custom type flConverterDeviceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_FlConverterDeviceReset_Type.__name__ = "Integer32"
_FlConverterDeviceReset_Object = MibTableColumn
flConverterDeviceReset = _FlConverterDeviceReset_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 10, 1, 1, 2),
    _FlConverterDeviceReset_Type()
)
flConverterDeviceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flConverterDeviceReset.setStatus("current")


class _FlConverterDeviceRestoreDefaults_Type(Integer32):
    """Custom type flConverterDeviceRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("restore", 2))
    )


_FlConverterDeviceRestoreDefaults_Type.__name__ = "Integer32"
_FlConverterDeviceRestoreDefaults_Object = MibTableColumn
flConverterDeviceRestoreDefaults = _FlConverterDeviceRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 10, 1, 1, 3),
    _FlConverterDeviceRestoreDefaults_Type()
)
flConverterDeviceRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flConverterDeviceRestoreDefaults.setStatus("current")
_FlConverterDeviceFirmRevision_Type = DisplayString
_FlConverterDeviceFirmRevision_Object = MibTableColumn
flConverterDeviceFirmRevision = _FlConverterDeviceFirmRevision_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 10, 1, 1, 4),
    _FlConverterDeviceFirmRevision_Type()
)
flConverterDeviceFirmRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flConverterDeviceFirmRevision.setStatus("current")
_FlConverterDeviceSerialNumber_Type = DisplayString
_FlConverterDeviceSerialNumber_Object = MibTableColumn
flConverterDeviceSerialNumber = _FlConverterDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 10, 1, 1, 5),
    _FlConverterDeviceSerialNumber_Type()
)
flConverterDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flConverterDeviceSerialNumber.setStatus("current")
_FlConverterDeviceTemperature_Type = Integer32
_FlConverterDeviceTemperature_Object = MibTableColumn
flConverterDeviceTemperature = _FlConverterDeviceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 10, 1, 1, 6),
    _FlConverterDeviceTemperature_Type()
)
flConverterDeviceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flConverterDeviceTemperature.setStatus("current")
_FlConverterChannel_ObjectIdentity = ObjectIdentity
flConverterChannel = _FlConverterChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 20)
)
_FlConverterChannelConfigTable_Object = MibTable
flConverterChannelConfigTable = _FlConverterChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 20, 1)
)
if mibBuilder.loadTexts:
    flConverterChannelConfigTable.setStatus("current")
_FlConverterChannelConfigEntry_Object = MibTableRow
flConverterChannelConfigEntry = _FlConverterChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 20, 1, 1)
)
flConverterChannelConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-DEVICECONVERTER", "flConverterChannelConfigIndex"),
)
if mibBuilder.loadTexts:
    flConverterChannelConfigEntry.setStatus("current")
_FlConverterChannelConfigIndex_Type = Integer32
_FlConverterChannelConfigIndex_Object = MibTableColumn
flConverterChannelConfigIndex = _FlConverterChannelConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 20, 1, 1, 1),
    _FlConverterChannelConfigIndex_Type()
)
flConverterChannelConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flConverterChannelConfigIndex.setStatus("current")


class _FlConverterTpLink_Type(Integer32):
    """Custom type flConverterTpLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("killed", 3))
    )


_FlConverterTpLink_Type.__name__ = "Integer32"
_FlConverterTpLink_Object = MibTableColumn
flConverterTpLink = _FlConverterTpLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 20, 1, 1, 2),
    _FlConverterTpLink_Type()
)
flConverterTpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flConverterTpLink.setStatus("current")


class _FlConverterFoLink_Type(Integer32):
    """Custom type flConverterFoLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlConverterFoLink_Type.__name__ = "Integer32"
_FlConverterFoLink_Object = MibTableColumn
flConverterFoLink = _FlConverterFoLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 20, 1, 1, 3),
    _FlConverterFoLink_Type()
)
flConverterFoLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flConverterFoLink.setStatus("current")
_FlConverterPortDescription_Type = DisplayString
_FlConverterPortDescription_Object = MibTableColumn
flConverterPortDescription = _FlConverterPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 20, 1, 1, 4),
    _FlConverterPortDescription_Type()
)
flConverterPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flConverterPortDescription.setStatus("current")


class _FlConverterDuplex_Type(Integer32):
    """Custom type flConverterDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdx", 1),
          ("fdx", 2))
    )


_FlConverterDuplex_Type.__name__ = "Integer32"
_FlConverterDuplex_Object = MibTableColumn
flConverterDuplex = _FlConverterDuplex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 20, 1, 1, 5),
    _FlConverterDuplex_Type()
)
flConverterDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flConverterDuplex.setStatus("current")


class _FlConverterTpAutoNego_Type(Integer32):
    """Custom type flConverterTpAutoNego based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_FlConverterTpAutoNego_Type.__name__ = "Integer32"
_FlConverterTpAutoNego_Object = MibTableColumn
flConverterTpAutoNego = _FlConverterTpAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 20, 1, 1, 6),
    _FlConverterTpAutoNego_Type()
)
flConverterTpAutoNego.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flConverterTpAutoNego.setStatus("current")


class _FlConverterTpDatarate_Type(Integer32):
    """Custom type flConverterTpDatarate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("m10", 1),
          ("m100", 2))
    )


_FlConverterTpDatarate_Type.__name__ = "Integer32"
_FlConverterTpDatarate_Object = MibTableColumn
flConverterTpDatarate = _FlConverterTpDatarate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 20, 1, 1, 7),
    _FlConverterTpDatarate_Type()
)
flConverterTpDatarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flConverterTpDatarate.setStatus("current")


class _FlConverterUpstreamBw_Type(Integer32):
    """Custom type flConverterUpstreamBw based on Integer32"""
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
              20,
              30,
              40,
              50,
              60,
              70,
              80,
              90,
              100,
              129,
              130)
        )
    )
    namedValues = NamedValues(
        *(("m01", 1),
          ("m02", 2),
          ("m03", 3),
          ("m04", 4),
          ("m05", 5),
          ("m06", 6),
          ("m07", 7),
          ("m08", 8),
          ("m09", 9),
          ("m10", 10),
          ("m20", 20),
          ("m30", 30),
          ("m40", 40),
          ("m50", 50),
          ("m60", 60),
          ("m70", 70),
          ("m80", 80),
          ("m90", 90),
          ("m100", 100),
          ("k256", 129),
          ("k512", 130))
    )


_FlConverterUpstreamBw_Type.__name__ = "Integer32"
_FlConverterUpstreamBw_Object = MibTableColumn
flConverterUpstreamBw = _FlConverterUpstreamBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 20, 1, 1, 8),
    _FlConverterUpstreamBw_Type()
)
flConverterUpstreamBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flConverterUpstreamBw.setStatus("current")


class _FlConverterEnableTpPort_Type(Integer32):
    """Custom type flConverterEnableTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlConverterEnableTpPort_Type.__name__ = "Integer32"
_FlConverterEnableTpPort_Object = MibTableColumn
flConverterEnableTpPort = _FlConverterEnableTpPort_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 20, 1, 1, 9),
    _FlConverterEnableTpPort_Type()
)
flConverterEnableTpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flConverterEnableTpPort.setStatus("current")


class _FlConverterPause_Type(Integer32):
    """Custom type flConverterPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlConverterPause_Type.__name__ = "Integer32"
_FlConverterPause_Object = MibTableColumn
flConverterPause = _FlConverterPause_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 20, 1, 1, 10),
    _FlConverterPause_Type()
)
flConverterPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flConverterPause.setStatus("current")


class _FlConverterFo2TpFp_Type(Integer32):
    """Custom type flConverterFo2TpFp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlConverterFo2TpFp_Type.__name__ = "Integer32"
_FlConverterFo2TpFp_Object = MibTableColumn
flConverterFo2TpFp = _FlConverterFo2TpFp_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 20, 1, 1, 11),
    _FlConverterFo2TpFp_Type()
)
flConverterFo2TpFp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flConverterFo2TpFp.setStatus("current")

# Managed Objects groups

flConverterDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 1, 2, 1)
)
flConverterDeviceGroup.setObjects(
      *(("FIBROLAN-MIB-DEVICECONVERTER", "flConverterDeviceReset"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterDeviceRestoreDefaults"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterDeviceFirmRevision"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterDeviceSerialNumber"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterDeviceTemperature"))
)
if mibBuilder.loadTexts:
    flConverterDeviceGroup.setStatus("current")

flConverterChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 1, 2, 2)
)
flConverterChannelGroup.setObjects(
      *(("FIBROLAN-MIB-DEVICECONVERTER", "flConverterChannelConfigIndex"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterTpLink"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterFoLink"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterPortDescription"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterDuplex"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterTpAutoNego"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterTpDatarate"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterUpstreamBw"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterEnableTpPort"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterPause"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterFo2TpFp"))
)
if mibBuilder.loadTexts:
    flConverterChannelGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flConverterMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 10, 1, 1, 1)
)
flConverterMIBCompliance.setObjects(
      *(("FIBROLAN-MIB-DEVICECONVERTER", "flConverterDeviceGroup"),
        ("FIBROLAN-MIB-DEVICECONVERTER", "flConverterChannelGroup"))
)
if mibBuilder.loadTexts:
    flConverterMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-DEVICECONVERTER",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMaRemoteDevice": flMaRemoteDevice,
       "flConverter": flConverter,
       "flConverterMIBConformance": flConverterMIBConformance,
       "flConverterMIBCompliances": flConverterMIBCompliances,
       "flConverterMIBCompliance": flConverterMIBCompliance,
       "flConverterMIBGroups": flConverterMIBGroups,
       "flConverterDeviceGroup": flConverterDeviceGroup,
       "flConverterChannelGroup": flConverterChannelGroup,
       "flConverterDevice": flConverterDevice,
       "flConverterDeviceConfigTable": flConverterDeviceConfigTable,
       "flConverterDeviceConfigEntry": flConverterDeviceConfigEntry,
       "flConverterDeviceReset": flConverterDeviceReset,
       "flConverterDeviceRestoreDefaults": flConverterDeviceRestoreDefaults,
       "flConverterDeviceFirmRevision": flConverterDeviceFirmRevision,
       "flConverterDeviceSerialNumber": flConverterDeviceSerialNumber,
       "flConverterDeviceTemperature": flConverterDeviceTemperature,
       "flConverterChannel": flConverterChannel,
       "flConverterChannelConfigTable": flConverterChannelConfigTable,
       "flConverterChannelConfigEntry": flConverterChannelConfigEntry,
       "flConverterChannelConfigIndex": flConverterChannelConfigIndex,
       "flConverterTpLink": flConverterTpLink,
       "flConverterFoLink": flConverterFoLink,
       "flConverterPortDescription": flConverterPortDescription,
       "flConverterDuplex": flConverterDuplex,
       "flConverterTpAutoNego": flConverterTpAutoNego,
       "flConverterTpDatarate": flConverterTpDatarate,
       "flConverterUpstreamBw": flConverterUpstreamBw,
       "flConverterEnableTpPort": flConverterEnableTpPort,
       "flConverterPause": flConverterPause,
       "flConverterFo2TpFp": flConverterFo2TpFp}
)
