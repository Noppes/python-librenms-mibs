# SNMP MIB module (FIBROLAN-MIB-LTA41MA-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-LTA41MA-V2

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

flLta41ma_V2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21)
)


# Types definitions



class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )




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
_FlLta41ma_V2MIBConformance_ObjectIdentity = ObjectIdentity
flLta41ma_V2MIBConformance = _FlLta41ma_V2MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 1)
)
_FlLta41ma_V2MIBCompliances_ObjectIdentity = ObjectIdentity
flLta41ma_V2MIBCompliances = _FlLta41ma_V2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 1, 1)
)
_FlLta41ma_V2MIBGroups_ObjectIdentity = ObjectIdentity
flLta41ma_V2MIBGroups = _FlLta41ma_V2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 1, 2)
)
_FlLta41ma_V2Global_ObjectIdentity = ObjectIdentity
flLta41ma_V2Global = _FlLta41ma_V2Global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10)
)
_FlLta41ma_V2GlobalConfigTable_Object = MibTable
flLta41ma_V2GlobalConfigTable = _FlLta41ma_V2GlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1)
)
if mibBuilder.loadTexts:
    flLta41ma_V2GlobalConfigTable.setStatus("current")
_FlLta41ma_V2GlobalConfigEntry_Object = MibTableRow
flLta41ma_V2GlobalConfigEntry = _FlLta41ma_V2GlobalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1, 1)
)
flLta41ma_V2GlobalConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2GlobalConfigEntry.setStatus("current")


class _FlLta41ma_V2GlobalBufferShare_Type(Integer32):
    """Custom type flLta41ma_V2GlobalBufferShare based on Integer32"""
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


_FlLta41ma_V2GlobalBufferShare_Type.__name__ = "Integer32"
_FlLta41ma_V2GlobalBufferShare_Object = MibTableColumn
flLta41ma_V2GlobalBufferShare = _FlLta41ma_V2GlobalBufferShare_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1, 1, 2),
    _FlLta41ma_V2GlobalBufferShare_Type()
)
flLta41ma_V2GlobalBufferShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2GlobalBufferShare.setStatus("current")


class _FlLta41ma_V2GlobalMulticastProtection_Type(Integer32):
    """Custom type flLta41ma_V2GlobalMulticastProtection based on Integer32"""
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


_FlLta41ma_V2GlobalMulticastProtection_Type.__name__ = "Integer32"
_FlLta41ma_V2GlobalMulticastProtection_Object = MibTableColumn
flLta41ma_V2GlobalMulticastProtection = _FlLta41ma_V2GlobalMulticastProtection_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1, 1, 3),
    _FlLta41ma_V2GlobalMulticastProtection_Type()
)
flLta41ma_V2GlobalMulticastProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2GlobalMulticastProtection.setStatus("current")


class _FlLta41ma_V2GlobalBroadcastRate_Type(Integer32):
    """Custom type flLta41ma_V2GlobalBroadcastRate based on Integer32"""
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
        *(("pct5", 1),
          ("pct10", 2),
          ("pct15", 3),
          ("pct20", 4),
          ("pct25", 5))
    )


_FlLta41ma_V2GlobalBroadcastRate_Type.__name__ = "Integer32"
_FlLta41ma_V2GlobalBroadcastRate_Object = MibTableColumn
flLta41ma_V2GlobalBroadcastRate = _FlLta41ma_V2GlobalBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1, 1, 4),
    _FlLta41ma_V2GlobalBroadcastRate_Type()
)
flLta41ma_V2GlobalBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2GlobalBroadcastRate.setStatus("current")


class _FlLta41ma_V2GlobalMaxPacketSize_Type(Integer32):
    """Custom type flLta41ma_V2GlobalMaxPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bytes1522", 1),
          ("bytes1536", 2),
          ("bytes1916", 3))
    )


_FlLta41ma_V2GlobalMaxPacketSize_Type.__name__ = "Integer32"
_FlLta41ma_V2GlobalMaxPacketSize_Object = MibTableColumn
flLta41ma_V2GlobalMaxPacketSize = _FlLta41ma_V2GlobalMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1, 1, 5),
    _FlLta41ma_V2GlobalMaxPacketSize_Type()
)
flLta41ma_V2GlobalMaxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2GlobalMaxPacketSize.setStatus("current")


class _FlLta41ma_V2GlobalSleLogic_Type(Integer32):
    """Custom type flLta41ma_V2GlobalSleLogic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("or", 1),
          ("and", 2))
    )


_FlLta41ma_V2GlobalSleLogic_Type.__name__ = "Integer32"
_FlLta41ma_V2GlobalSleLogic_Object = MibTableColumn
flLta41ma_V2GlobalSleLogic = _FlLta41ma_V2GlobalSleLogic_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1, 1, 6),
    _FlLta41ma_V2GlobalSleLogic_Type()
)
flLta41ma_V2GlobalSleLogic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2GlobalSleLogic.setStatus("current")


class _FlLta41ma_V2GlobalSlePort1_Type(Integer32):
    """Custom type flLta41ma_V2GlobalSlePort1 based on Integer32"""
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


_FlLta41ma_V2GlobalSlePort1_Type.__name__ = "Integer32"
_FlLta41ma_V2GlobalSlePort1_Object = MibTableColumn
flLta41ma_V2GlobalSlePort1 = _FlLta41ma_V2GlobalSlePort1_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1, 1, 7),
    _FlLta41ma_V2GlobalSlePort1_Type()
)
flLta41ma_V2GlobalSlePort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2GlobalSlePort1.setStatus("current")


class _FlLta41ma_V2GlobalSlePort2_Type(Integer32):
    """Custom type flLta41ma_V2GlobalSlePort2 based on Integer32"""
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


_FlLta41ma_V2GlobalSlePort2_Type.__name__ = "Integer32"
_FlLta41ma_V2GlobalSlePort2_Object = MibTableColumn
flLta41ma_V2GlobalSlePort2 = _FlLta41ma_V2GlobalSlePort2_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1, 1, 8),
    _FlLta41ma_V2GlobalSlePort2_Type()
)
flLta41ma_V2GlobalSlePort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2GlobalSlePort2.setStatus("current")


class _FlLta41ma_V2GlobalSlePort3_Type(Integer32):
    """Custom type flLta41ma_V2GlobalSlePort3 based on Integer32"""
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


_FlLta41ma_V2GlobalSlePort3_Type.__name__ = "Integer32"
_FlLta41ma_V2GlobalSlePort3_Object = MibTableColumn
flLta41ma_V2GlobalSlePort3 = _FlLta41ma_V2GlobalSlePort3_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1, 1, 9),
    _FlLta41ma_V2GlobalSlePort3_Type()
)
flLta41ma_V2GlobalSlePort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2GlobalSlePort3.setStatus("current")


class _FlLta41ma_V2GlobalSlePort4_Type(Integer32):
    """Custom type flLta41ma_V2GlobalSlePort4 based on Integer32"""
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


_FlLta41ma_V2GlobalSlePort4_Type.__name__ = "Integer32"
_FlLta41ma_V2GlobalSlePort4_Object = MibTableColumn
flLta41ma_V2GlobalSlePort4 = _FlLta41ma_V2GlobalSlePort4_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1, 1, 10),
    _FlLta41ma_V2GlobalSlePort4_Type()
)
flLta41ma_V2GlobalSlePort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2GlobalSlePort4.setStatus("current")


class _FlLta41ma_V2RestartDevice_Type(Integer32):
    """Custom type flLta41ma_V2RestartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("restart", 2))
    )


_FlLta41ma_V2RestartDevice_Type.__name__ = "Integer32"
_FlLta41ma_V2RestartDevice_Object = MibTableColumn
flLta41ma_V2RestartDevice = _FlLta41ma_V2RestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1, 1, 11),
    _FlLta41ma_V2RestartDevice_Type()
)
flLta41ma_V2RestartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2RestartDevice.setStatus("current")


class _FlLta41ma_V2RestoreDefaults_Type(Integer32):
    """Custom type flLta41ma_V2RestoreDefaults based on Integer32"""
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


_FlLta41ma_V2RestoreDefaults_Type.__name__ = "Integer32"
_FlLta41ma_V2RestoreDefaults_Object = MibTableColumn
flLta41ma_V2RestoreDefaults = _FlLta41ma_V2RestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1, 1, 12),
    _FlLta41ma_V2RestoreDefaults_Type()
)
flLta41ma_V2RestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2RestoreDefaults.setStatus("current")
_FlLta41ma_V2Temperature_Type = Integer32
_FlLta41ma_V2Temperature_Object = MibTableColumn
flLta41ma_V2Temperature = _FlLta41ma_V2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1, 1, 13),
    _FlLta41ma_V2Temperature_Type()
)
flLta41ma_V2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2Temperature.setStatus("current")
_FlLta41ma_V2FirmRevision_Type = DisplayString
_FlLta41ma_V2FirmRevision_Object = MibTableColumn
flLta41ma_V2FirmRevision = _FlLta41ma_V2FirmRevision_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 10, 1, 1, 14),
    _FlLta41ma_V2FirmRevision_Type()
)
flLta41ma_V2FirmRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2FirmRevision.setStatus("current")
_FlLta41ma_V2Ports_ObjectIdentity = ObjectIdentity
flLta41ma_V2Ports = _FlLta41ma_V2Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20)
)
_FlLta41ma_V2PortsConfigTable_Object = MibTable
flLta41ma_V2PortsConfigTable = _FlLta41ma_V2PortsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1)
)
if mibBuilder.loadTexts:
    flLta41ma_V2PortsConfigTable.setStatus("current")
_FlLta41ma_V2PortConfigEntry_Object = MibTableRow
flLta41ma_V2PortConfigEntry = _FlLta41ma_V2PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1, 1)
)
flLta41ma_V2PortConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortNumber"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2PortConfigEntry.setStatus("current")


class _FlLta41ma_V2PortNumber_Type(Integer32):
    """Custom type flLta41ma_V2PortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FlLta41ma_V2PortNumber_Type.__name__ = "Integer32"
_FlLta41ma_V2PortNumber_Object = MibTableColumn
flLta41ma_V2PortNumber = _FlLta41ma_V2PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1, 1, 1),
    _FlLta41ma_V2PortNumber_Type()
)
flLta41ma_V2PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2PortNumber.setStatus("current")


class _FlLta41ma_V2PortType_Type(Integer32):
    """Custom type flLta41ma_V2PortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tp", 1),
          ("fo", 2))
    )


_FlLta41ma_V2PortType_Type.__name__ = "Integer32"
_FlLta41ma_V2PortType_Object = MibTableColumn
flLta41ma_V2PortType = _FlLta41ma_V2PortType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1, 1, 2),
    _FlLta41ma_V2PortType_Type()
)
flLta41ma_V2PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2PortType.setStatus("current")


class _FlLta41ma_V2PortLink_Type(Integer32):
    """Custom type flLta41ma_V2PortLink based on Integer32"""
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


_FlLta41ma_V2PortLink_Type.__name__ = "Integer32"
_FlLta41ma_V2PortLink_Object = MibTableColumn
flLta41ma_V2PortLink = _FlLta41ma_V2PortLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1, 1, 3),
    _FlLta41ma_V2PortLink_Type()
)
flLta41ma_V2PortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2PortLink.setStatus("current")
_FlLta41ma_V2PortDescription_Type = DisplayString
_FlLta41ma_V2PortDescription_Object = MibTableColumn
flLta41ma_V2PortDescription = _FlLta41ma_V2PortDescription_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1, 1, 4),
    _FlLta41ma_V2PortDescription_Type()
)
flLta41ma_V2PortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortDescription.setStatus("current")


class _FlLta41ma_V2PortAutoNego_Type(Integer32):
    """Custom type flLta41ma_V2PortAutoNego based on Integer32"""
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


_FlLta41ma_V2PortAutoNego_Type.__name__ = "Integer32"
_FlLta41ma_V2PortAutoNego_Object = MibTableColumn
flLta41ma_V2PortAutoNego = _FlLta41ma_V2PortAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1, 1, 5),
    _FlLta41ma_V2PortAutoNego_Type()
)
flLta41ma_V2PortAutoNego.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortAutoNego.setStatus("current")


class _FlLta41ma_V2PortDuplex_Type(Integer32):
    """Custom type flLta41ma_V2PortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hdx", 1),
          ("fdx", 2),
          ("n-a", 3))
    )


_FlLta41ma_V2PortDuplex_Type.__name__ = "Integer32"
_FlLta41ma_V2PortDuplex_Object = MibTableColumn
flLta41ma_V2PortDuplex = _FlLta41ma_V2PortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1, 1, 6),
    _FlLta41ma_V2PortDuplex_Type()
)
flLta41ma_V2PortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortDuplex.setStatus("current")


class _FlLta41ma_V2PortDatarate_Type(Integer32):
    """Custom type flLta41ma_V2PortDatarate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("m10", 1),
          ("m100", 2),
          ("n-a", 3))
    )


_FlLta41ma_V2PortDatarate_Type.__name__ = "Integer32"
_FlLta41ma_V2PortDatarate_Object = MibTableColumn
flLta41ma_V2PortDatarate = _FlLta41ma_V2PortDatarate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1, 1, 7),
    _FlLta41ma_V2PortDatarate_Type()
)
flLta41ma_V2PortDatarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortDatarate.setStatus("current")


class _FlLta41ma_V2PortEnabled_Type(Integer32):
    """Custom type flLta41ma_V2PortEnabled based on Integer32"""
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


_FlLta41ma_V2PortEnabled_Type.__name__ = "Integer32"
_FlLta41ma_V2PortEnabled_Object = MibTableColumn
flLta41ma_V2PortEnabled = _FlLta41ma_V2PortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1, 1, 8),
    _FlLta41ma_V2PortEnabled_Type()
)
flLta41ma_V2PortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortEnabled.setStatus("current")


class _FlLta41ma_V2PortAutoCross_Type(Integer32):
    """Custom type flLta41ma_V2PortAutoCross based on Integer32"""
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


_FlLta41ma_V2PortAutoCross_Type.__name__ = "Integer32"
_FlLta41ma_V2PortAutoCross_Object = MibTableColumn
flLta41ma_V2PortAutoCross = _FlLta41ma_V2PortAutoCross_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1, 1, 9),
    _FlLta41ma_V2PortAutoCross_Type()
)
flLta41ma_V2PortAutoCross.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortAutoCross.setStatus("current")


class _FlLta41ma_V2PortMdix_Type(Integer32):
    """Custom type flLta41ma_V2PortMdix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 1),
          ("mdix", 2))
    )


_FlLta41ma_V2PortMdix_Type.__name__ = "Integer32"
_FlLta41ma_V2PortMdix_Object = MibTableColumn
flLta41ma_V2PortMdix = _FlLta41ma_V2PortMdix_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1, 1, 10),
    _FlLta41ma_V2PortMdix_Type()
)
flLta41ma_V2PortMdix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortMdix.setStatus("current")


class _FlLta41ma_V2PortFef_Type(Integer32):
    """Custom type flLta41ma_V2PortFef based on Integer32"""
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


_FlLta41ma_V2PortFef_Type.__name__ = "Integer32"
_FlLta41ma_V2PortFef_Object = MibTableColumn
flLta41ma_V2PortFef = _FlLta41ma_V2PortFef_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1, 1, 11),
    _FlLta41ma_V2PortFef_Type()
)
flLta41ma_V2PortFef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortFef.setStatus("current")


class _FlLta41ma_V2PortReset_Type(Integer32):
    """Custom type flLta41ma_V2PortReset based on Integer32"""
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


_FlLta41ma_V2PortReset_Type.__name__ = "Integer32"
_FlLta41ma_V2PortReset_Object = MibTableColumn
flLta41ma_V2PortReset = _FlLta41ma_V2PortReset_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1, 1, 12),
    _FlLta41ma_V2PortReset_Type()
)
flLta41ma_V2PortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortReset.setStatus("current")


class _FlLta41ma_V2PortBroadcastProtection_Type(Integer32):
    """Custom type flLta41ma_V2PortBroadcastProtection based on Integer32"""
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


_FlLta41ma_V2PortBroadcastProtection_Type.__name__ = "Integer32"
_FlLta41ma_V2PortBroadcastProtection_Object = MibTableColumn
flLta41ma_V2PortBroadcastProtection = _FlLta41ma_V2PortBroadcastProtection_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 1, 1, 13),
    _FlLta41ma_V2PortBroadcastProtection_Type()
)
flLta41ma_V2PortBroadcastProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortBroadcastProtection.setStatus("current")
_FlLta41ma_V2PortsBwConfigTable_Object = MibTable
flLta41ma_V2PortsBwConfigTable = _FlLta41ma_V2PortsBwConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 2)
)
if mibBuilder.loadTexts:
    flLta41ma_V2PortsBwConfigTable.setStatus("current")
_FlLta41ma_V2PortBwConfigEntry_Object = MibTableRow
flLta41ma_V2PortBwConfigEntry = _FlLta41ma_V2PortBwConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 2, 1)
)
flLta41ma_V2PortBwConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortNumber"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2PortBwConfigEntry.setStatus("current")


class _FlLta41ma_V2PortRxHighBw_Type(Integer32):
    """Custom type flLta41ma_V2PortRxHighBw based on Integer32"""
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


_FlLta41ma_V2PortRxHighBw_Type.__name__ = "Integer32"
_FlLta41ma_V2PortRxHighBw_Object = MibTableColumn
flLta41ma_V2PortRxHighBw = _FlLta41ma_V2PortRxHighBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 2, 1, 1),
    _FlLta41ma_V2PortRxHighBw_Type()
)
flLta41ma_V2PortRxHighBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortRxHighBw.setStatus("current")


class _FlLta41ma_V2PortTxHighBw_Type(Integer32):
    """Custom type flLta41ma_V2PortTxHighBw based on Integer32"""
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


_FlLta41ma_V2PortTxHighBw_Type.__name__ = "Integer32"
_FlLta41ma_V2PortTxHighBw_Object = MibTableColumn
flLta41ma_V2PortTxHighBw = _FlLta41ma_V2PortTxHighBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 2, 1, 2),
    _FlLta41ma_V2PortTxHighBw_Type()
)
flLta41ma_V2PortTxHighBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortTxHighBw.setStatus("current")


class _FlLta41ma_V2PortRxLowBw_Type(Integer32):
    """Custom type flLta41ma_V2PortRxLowBw based on Integer32"""
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


_FlLta41ma_V2PortRxLowBw_Type.__name__ = "Integer32"
_FlLta41ma_V2PortRxLowBw_Object = MibTableColumn
flLta41ma_V2PortRxLowBw = _FlLta41ma_V2PortRxLowBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 2, 1, 3),
    _FlLta41ma_V2PortRxLowBw_Type()
)
flLta41ma_V2PortRxLowBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortRxLowBw.setStatus("current")


class _FlLta41ma_V2PortTxLowBw_Type(Integer32):
    """Custom type flLta41ma_V2PortTxLowBw based on Integer32"""
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


_FlLta41ma_V2PortTxLowBw_Type.__name__ = "Integer32"
_FlLta41ma_V2PortTxLowBw_Object = MibTableColumn
flLta41ma_V2PortTxLowBw = _FlLta41ma_V2PortTxLowBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 2, 1, 4),
    _FlLta41ma_V2PortTxLowBw_Type()
)
flLta41ma_V2PortTxLowBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortTxLowBw.setStatus("current")


class _FlLta41ma_V2PortRxDiffBw_Type(Integer32):
    """Custom type flLta41ma_V2PortRxDiffBw based on Integer32"""
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


_FlLta41ma_V2PortRxDiffBw_Type.__name__ = "Integer32"
_FlLta41ma_V2PortRxDiffBw_Object = MibTableColumn
flLta41ma_V2PortRxDiffBw = _FlLta41ma_V2PortRxDiffBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 2, 1, 5),
    _FlLta41ma_V2PortRxDiffBw_Type()
)
flLta41ma_V2PortRxDiffBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortRxDiffBw.setStatus("current")


class _FlLta41ma_V2PortRxHighFlowControl_Type(Integer32):
    """Custom type flLta41ma_V2PortRxHighFlowControl based on Integer32"""
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


_FlLta41ma_V2PortRxHighFlowControl_Type.__name__ = "Integer32"
_FlLta41ma_V2PortRxHighFlowControl_Object = MibTableColumn
flLta41ma_V2PortRxHighFlowControl = _FlLta41ma_V2PortRxHighFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 2, 1, 6),
    _FlLta41ma_V2PortRxHighFlowControl_Type()
)
flLta41ma_V2PortRxHighFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortRxHighFlowControl.setStatus("current")


class _FlLta41ma_V2PortRxLowFlowControl_Type(Integer32):
    """Custom type flLta41ma_V2PortRxLowFlowControl based on Integer32"""
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


_FlLta41ma_V2PortRxLowFlowControl_Type.__name__ = "Integer32"
_FlLta41ma_V2PortRxLowFlowControl_Object = MibTableColumn
flLta41ma_V2PortRxLowFlowControl = _FlLta41ma_V2PortRxLowFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 2, 1, 7),
    _FlLta41ma_V2PortRxLowFlowControl_Type()
)
flLta41ma_V2PortRxLowFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortRxLowFlowControl.setStatus("current")


class _FlLta41ma_V2PortTxDiffBw_Type(Integer32):
    """Custom type flLta41ma_V2PortTxDiffBw based on Integer32"""
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


_FlLta41ma_V2PortTxDiffBw_Type.__name__ = "Integer32"
_FlLta41ma_V2PortTxDiffBw_Object = MibTableColumn
flLta41ma_V2PortTxDiffBw = _FlLta41ma_V2PortTxDiffBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 20, 2, 1, 8),
    _FlLta41ma_V2PortTxDiffBw_Type()
)
flLta41ma_V2PortTxDiffBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortTxDiffBw.setStatus("current")
_FlLta41ma_V2Vlan_ObjectIdentity = ObjectIdentity
flLta41ma_V2Vlan = _FlLta41ma_V2Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30)
)
_FlLta41ma_V2VlanGlobalTable_Object = MibTable
flLta41ma_V2VlanGlobalTable = _FlLta41ma_V2VlanGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 1)
)
if mibBuilder.loadTexts:
    flLta41ma_V2VlanGlobalTable.setStatus("current")
_FlLta41ma_V2VlanGlobalEntry_Object = MibTableRow
flLta41ma_V2VlanGlobalEntry = _FlLta41ma_V2VlanGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 1, 1)
)
flLta41ma_V2VlanGlobalEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2VlanGlobalEntry.setStatus("current")


class _FlLta41ma_V2Vlan8021q_Type(Integer32):
    """Custom type flLta41ma_V2Vlan8021q based on Integer32"""
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


_FlLta41ma_V2Vlan8021q_Type.__name__ = "Integer32"
_FlLta41ma_V2Vlan8021q_Object = MibTableColumn
flLta41ma_V2Vlan8021q = _FlLta41ma_V2Vlan8021q_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 1, 1, 1),
    _FlLta41ma_V2Vlan8021q_Type()
)
flLta41ma_V2Vlan8021q.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2Vlan8021q.setStatus("current")


class _FlLta41ma_V2VlanNullVidReplace_Type(Integer32):
    """Custom type flLta41ma_V2VlanNullVidReplace based on Integer32"""
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


_FlLta41ma_V2VlanNullVidReplace_Type.__name__ = "Integer32"
_FlLta41ma_V2VlanNullVidReplace_Object = MibTableColumn
flLta41ma_V2VlanNullVidReplace = _FlLta41ma_V2VlanNullVidReplace_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 1, 1, 2),
    _FlLta41ma_V2VlanNullVidReplace_Type()
)
flLta41ma_V2VlanNullVidReplace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2VlanNullVidReplace.setStatus("current")


class _FlLta41ma_V2CreateDefaultVlans_Type(Integer32):
    """Custom type flLta41ma_V2CreateDefaultVlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("create", 2))
    )


_FlLta41ma_V2CreateDefaultVlans_Type.__name__ = "Integer32"
_FlLta41ma_V2CreateDefaultVlans_Object = MibTableColumn
flLta41ma_V2CreateDefaultVlans = _FlLta41ma_V2CreateDefaultVlans_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 1, 1, 3),
    _FlLta41ma_V2CreateDefaultVlans_Type()
)
flLta41ma_V2CreateDefaultVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2CreateDefaultVlans.setStatus("current")


class _FlLta41ma_V2DeleteAllVlans_Type(Integer32):
    """Custom type flLta41ma_V2DeleteAllVlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("delete", 2))
    )


_FlLta41ma_V2DeleteAllVlans_Type.__name__ = "Integer32"
_FlLta41ma_V2DeleteAllVlans_Object = MibTableColumn
flLta41ma_V2DeleteAllVlans = _FlLta41ma_V2DeleteAllVlans_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 1, 1, 4),
    _FlLta41ma_V2DeleteAllVlans_Type()
)
flLta41ma_V2DeleteAllVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2DeleteAllVlans.setStatus("current")
_FlLta41ma_V2VlansTable_Object = MibTable
flLta41ma_V2VlansTable = _FlLta41ma_V2VlansTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 10)
)
if mibBuilder.loadTexts:
    flLta41ma_V2VlansTable.setStatus("current")
_FlLta41ma_V2VlanEntry_Object = MibTableRow
flLta41ma_V2VlanEntry = _FlLta41ma_V2VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 10, 1)
)
flLta41ma_V2VlanEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2VlanFid"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2VlanEntry.setStatus("current")


class _FlLta41ma_V2VlanFid_Type(Integer32):
    """Custom type flLta41ma_V2VlanFid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FlLta41ma_V2VlanFid_Type.__name__ = "Integer32"
_FlLta41ma_V2VlanFid_Object = MibTableColumn
flLta41ma_V2VlanFid = _FlLta41ma_V2VlanFid_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 10, 1, 1),
    _FlLta41ma_V2VlanFid_Type()
)
flLta41ma_V2VlanFid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2VlanFid.setStatus("current")


class _FlLta41ma_V2VlanVid_Type(Integer32):
    """Custom type flLta41ma_V2VlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_FlLta41ma_V2VlanVid_Type.__name__ = "Integer32"
_FlLta41ma_V2VlanVid_Object = MibTableColumn
flLta41ma_V2VlanVid = _FlLta41ma_V2VlanVid_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 10, 1, 2),
    _FlLta41ma_V2VlanVid_Type()
)
flLta41ma_V2VlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2VlanVid.setStatus("current")
_FlLta41ma_V2VlanName_Type = DisplayString
_FlLta41ma_V2VlanName_Object = MibTableColumn
flLta41ma_V2VlanName = _FlLta41ma_V2VlanName_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 10, 1, 3),
    _FlLta41ma_V2VlanName_Type()
)
flLta41ma_V2VlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2VlanName.setStatus("current")


class _FlLta41ma_V2VlanPort1Member_Type(Integer32):
    """Custom type flLta41ma_V2VlanPort1Member based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("native", 2),
          ("tagged", 3))
    )


_FlLta41ma_V2VlanPort1Member_Type.__name__ = "Integer32"
_FlLta41ma_V2VlanPort1Member_Object = MibTableColumn
flLta41ma_V2VlanPort1Member = _FlLta41ma_V2VlanPort1Member_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 10, 1, 4),
    _FlLta41ma_V2VlanPort1Member_Type()
)
flLta41ma_V2VlanPort1Member.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2VlanPort1Member.setStatus("current")


class _FlLta41ma_V2VlanPort2Member_Type(Integer32):
    """Custom type flLta41ma_V2VlanPort2Member based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("native", 2),
          ("tagged", 3))
    )


_FlLta41ma_V2VlanPort2Member_Type.__name__ = "Integer32"
_FlLta41ma_V2VlanPort2Member_Object = MibTableColumn
flLta41ma_V2VlanPort2Member = _FlLta41ma_V2VlanPort2Member_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 10, 1, 5),
    _FlLta41ma_V2VlanPort2Member_Type()
)
flLta41ma_V2VlanPort2Member.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2VlanPort2Member.setStatus("current")


class _FlLta41ma_V2VlanPort3Member_Type(Integer32):
    """Custom type flLta41ma_V2VlanPort3Member based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("native", 2),
          ("tagged", 3))
    )


_FlLta41ma_V2VlanPort3Member_Type.__name__ = "Integer32"
_FlLta41ma_V2VlanPort3Member_Object = MibTableColumn
flLta41ma_V2VlanPort3Member = _FlLta41ma_V2VlanPort3Member_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 10, 1, 6),
    _FlLta41ma_V2VlanPort3Member_Type()
)
flLta41ma_V2VlanPort3Member.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2VlanPort3Member.setStatus("current")


class _FlLta41ma_V2VlanPort4Member_Type(Integer32):
    """Custom type flLta41ma_V2VlanPort4Member based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("native", 2),
          ("tagged", 3))
    )


_FlLta41ma_V2VlanPort4Member_Type.__name__ = "Integer32"
_FlLta41ma_V2VlanPort4Member_Object = MibTableColumn
flLta41ma_V2VlanPort4Member = _FlLta41ma_V2VlanPort4Member_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 10, 1, 7),
    _FlLta41ma_V2VlanPort4Member_Type()
)
flLta41ma_V2VlanPort4Member.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2VlanPort4Member.setStatus("current")


class _FlLta41ma_V2VlanPort5Member_Type(Integer32):
    """Custom type flLta41ma_V2VlanPort5Member based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("native", 2),
          ("tagged", 3))
    )


_FlLta41ma_V2VlanPort5Member_Type.__name__ = "Integer32"
_FlLta41ma_V2VlanPort5Member_Object = MibTableColumn
flLta41ma_V2VlanPort5Member = _FlLta41ma_V2VlanPort5Member_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 10, 1, 8),
    _FlLta41ma_V2VlanPort5Member_Type()
)
flLta41ma_V2VlanPort5Member.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2VlanPort5Member.setStatus("current")
_FlLta41ma_V2VlanTableStatus_Type = EntryStatus
_FlLta41ma_V2VlanTableStatus_Object = MibTableColumn
flLta41ma_V2VlanTableStatus = _FlLta41ma_V2VlanTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 10, 1, 9),
    _FlLta41ma_V2VlanTableStatus_Type()
)
flLta41ma_V2VlanTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2VlanTableStatus.setStatus("current")
_FlLta41ma_V2PortsVlanConfigTable_Object = MibTable
flLta41ma_V2PortsVlanConfigTable = _FlLta41ma_V2PortsVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 20)
)
if mibBuilder.loadTexts:
    flLta41ma_V2PortsVlanConfigTable.setStatus("current")
_FlLta41ma_V2PortVlanConfigEntry_Object = MibTableRow
flLta41ma_V2PortVlanConfigEntry = _FlLta41ma_V2PortVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 20, 1)
)
flLta41ma_V2PortVlanConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortNumber"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2PortVlanConfigEntry.setStatus("current")


class _FlLta41ma_V2PortIngressFilter_Type(Integer32):
    """Custom type flLta41ma_V2PortIngressFilter based on Integer32"""
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


_FlLta41ma_V2PortIngressFilter_Type.__name__ = "Integer32"
_FlLta41ma_V2PortIngressFilter_Object = MibTableColumn
flLta41ma_V2PortIngressFilter = _FlLta41ma_V2PortIngressFilter_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 20, 1, 1),
    _FlLta41ma_V2PortIngressFilter_Type()
)
flLta41ma_V2PortIngressFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortIngressFilter.setStatus("current")


class _FlLta41ma_V2PortTagInsertion_Type(Integer32):
    """Custom type flLta41ma_V2PortTagInsertion based on Integer32"""
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


_FlLta41ma_V2PortTagInsertion_Type.__name__ = "Integer32"
_FlLta41ma_V2PortTagInsertion_Object = MibTableColumn
flLta41ma_V2PortTagInsertion = _FlLta41ma_V2PortTagInsertion_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 20, 1, 2),
    _FlLta41ma_V2PortTagInsertion_Type()
)
flLta41ma_V2PortTagInsertion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortTagInsertion.setStatus("current")


class _FlLta41ma_V2PortTagRemoval_Type(Integer32):
    """Custom type flLta41ma_V2PortTagRemoval based on Integer32"""
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


_FlLta41ma_V2PortTagRemoval_Type.__name__ = "Integer32"
_FlLta41ma_V2PortTagRemoval_Object = MibTableColumn
flLta41ma_V2PortTagRemoval = _FlLta41ma_V2PortTagRemoval_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 20, 1, 3),
    _FlLta41ma_V2PortTagRemoval_Type()
)
flLta41ma_V2PortTagRemoval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortTagRemoval.setStatus("current")


class _FlLta41ma_V2PortVid_Type(Integer32):
    """Custom type flLta41ma_V2PortVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_FlLta41ma_V2PortVid_Type.__name__ = "Integer32"
_FlLta41ma_V2PortVid_Object = MibTableColumn
flLta41ma_V2PortVid = _FlLta41ma_V2PortVid_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 20, 1, 4),
    _FlLta41ma_V2PortVid_Type()
)
flLta41ma_V2PortVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortVid.setStatus("current")


class _FlLta41ma_V2PortDiscardNonPvid_Type(Integer32):
    """Custom type flLta41ma_V2PortDiscardNonPvid based on Integer32"""
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


_FlLta41ma_V2PortDiscardNonPvid_Type.__name__ = "Integer32"
_FlLta41ma_V2PortDiscardNonPvid_Object = MibTableColumn
flLta41ma_V2PortDiscardNonPvid = _FlLta41ma_V2PortDiscardNonPvid_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 30, 20, 1, 5),
    _FlLta41ma_V2PortDiscardNonPvid_Type()
)
flLta41ma_V2PortDiscardNonPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortDiscardNonPvid.setStatus("current")
_FlLta41ma_V2Priority_ObjectIdentity = ObjectIdentity
flLta41ma_V2Priority = _FlLta41ma_V2Priority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40)
)
_FlLta41ma_V2QoSGlobalTable_Object = MibTable
flLta41ma_V2QoSGlobalTable = _FlLta41ma_V2QoSGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40, 1)
)
if mibBuilder.loadTexts:
    flLta41ma_V2QoSGlobalTable.setStatus("current")
_FlLta41ma_V2QosGlobalEntry_Object = MibTableRow
flLta41ma_V2QosGlobalEntry = _FlLta41ma_V2QosGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40, 1, 1)
)
flLta41ma_V2QosGlobalEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2QosGlobalEntry.setStatus("current")


class _FlLta41ma_V28021pBase_Type(Integer32):
    """Custom type flLta41ma_V28021pBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FlLta41ma_V28021pBase_Type.__name__ = "Integer32"
_FlLta41ma_V28021pBase_Object = MibTableColumn
flLta41ma_V28021pBase = _FlLta41ma_V28021pBase_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40, 1, 1, 1),
    _FlLta41ma_V28021pBase_Type()
)
flLta41ma_V28021pBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V28021pBase.setStatus("current")


class _FlLta41ma_V2PriorityRatio_Type(Integer32):
    """Custom type flLta41ma_V2PriorityRatio based on Integer32"""
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
        *(("alwaysHi", 1),
          ("ratio10-1", 2),
          ("ratio5-1", 3),
          ("ratio2-1", 4))
    )


_FlLta41ma_V2PriorityRatio_Type.__name__ = "Integer32"
_FlLta41ma_V2PriorityRatio_Object = MibTableColumn
flLta41ma_V2PriorityRatio = _FlLta41ma_V2PriorityRatio_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40, 1, 1, 2),
    _FlLta41ma_V2PriorityRatio_Type()
)
flLta41ma_V2PriorityRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PriorityRatio.setStatus("current")
_FlLta41ma_V2DscpTable_Object = MibTable
flLta41ma_V2DscpTable = _FlLta41ma_V2DscpTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40, 10)
)
if mibBuilder.loadTexts:
    flLta41ma_V2DscpTable.setStatus("current")
_FlLta41ma_V2DscpEntry_Object = MibTableRow
flLta41ma_V2DscpEntry = _FlLta41ma_V2DscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40, 10, 1)
)
flLta41ma_V2DscpEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2DscpCode"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2DscpEntry.setStatus("current")


class _FlLta41ma_V2DscpCode_Type(Integer32):
    """Custom type flLta41ma_V2DscpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FlLta41ma_V2DscpCode_Type.__name__ = "Integer32"
_FlLta41ma_V2DscpCode_Object = MibTableColumn
flLta41ma_V2DscpCode = _FlLta41ma_V2DscpCode_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40, 10, 1, 1),
    _FlLta41ma_V2DscpCode_Type()
)
flLta41ma_V2DscpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2DscpCode.setStatus("current")


class _FlLta41ma_V2DscpCodePriority_Type(Integer32):
    """Custom type flLta41ma_V2DscpCodePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_FlLta41ma_V2DscpCodePriority_Type.__name__ = "Integer32"
_FlLta41ma_V2DscpCodePriority_Object = MibTableColumn
flLta41ma_V2DscpCodePriority = _FlLta41ma_V2DscpCodePriority_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40, 10, 1, 2),
    _FlLta41ma_V2DscpCodePriority_Type()
)
flLta41ma_V2DscpCodePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2DscpCodePriority.setStatus("current")
_FlLta41ma_V2PortsPriorityConfigTable_Object = MibTable
flLta41ma_V2PortsPriorityConfigTable = _FlLta41ma_V2PortsPriorityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40, 20)
)
if mibBuilder.loadTexts:
    flLta41ma_V2PortsPriorityConfigTable.setStatus("current")
_FlLta41ma_V2PortPriorityConfigEntry_Object = MibTableRow
flLta41ma_V2PortPriorityConfigEntry = _FlLta41ma_V2PortPriorityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40, 20, 1)
)
flLta41ma_V2PortPriorityConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortNumber"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2PortPriorityConfigEntry.setStatus("current")


class _FlLta41ma_V2PortPriority_Type(Integer32):
    """Custom type flLta41ma_V2PortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_FlLta41ma_V2PortPriority_Type.__name__ = "Integer32"
_FlLta41ma_V2PortPriority_Object = MibTableColumn
flLta41ma_V2PortPriority = _FlLta41ma_V2PortPriority_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40, 20, 1, 1),
    _FlLta41ma_V2PortPriority_Type()
)
flLta41ma_V2PortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortPriority.setStatus("current")


class _FlLta41ma_V2Port8021pClassification_Type(Integer32):
    """Custom type flLta41ma_V2Port8021pClassification based on Integer32"""
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


_FlLta41ma_V2Port8021pClassification_Type.__name__ = "Integer32"
_FlLta41ma_V2Port8021pClassification_Object = MibTableColumn
flLta41ma_V2Port8021pClassification = _FlLta41ma_V2Port8021pClassification_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40, 20, 1, 2),
    _FlLta41ma_V2Port8021pClassification_Type()
)
flLta41ma_V2Port8021pClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2Port8021pClassification.setStatus("current")


class _FlLta41ma_V2PortDiffServClassification_Type(Integer32):
    """Custom type flLta41ma_V2PortDiffServClassification based on Integer32"""
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


_FlLta41ma_V2PortDiffServClassification_Type.__name__ = "Integer32"
_FlLta41ma_V2PortDiffServClassification_Object = MibTableColumn
flLta41ma_V2PortDiffServClassification = _FlLta41ma_V2PortDiffServClassification_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40, 20, 1, 3),
    _FlLta41ma_V2PortDiffServClassification_Type()
)
flLta41ma_V2PortDiffServClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortDiffServClassification.setStatus("current")


class _FlLta41ma_V2PortUserPriority_Type(Integer32):
    """Custom type flLta41ma_V2PortUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FlLta41ma_V2PortUserPriority_Type.__name__ = "Integer32"
_FlLta41ma_V2PortUserPriority_Object = MibTableColumn
flLta41ma_V2PortUserPriority = _FlLta41ma_V2PortUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 40, 20, 1, 4),
    _FlLta41ma_V2PortUserPriority_Type()
)
flLta41ma_V2PortUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2PortUserPriority.setStatus("current")
_FlLta41ma_V2Mac_ObjectIdentity = ObjectIdentity
flLta41ma_V2Mac = _FlLta41ma_V2Mac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50)
)
_FlLta41ma_V2MacAddressGlobalTable_Object = MibTable
flLta41ma_V2MacAddressGlobalTable = _FlLta41ma_V2MacAddressGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 1)
)
if mibBuilder.loadTexts:
    flLta41ma_V2MacAddressGlobalTable.setStatus("current")
_FlLta41ma_V2MacAddressGlobalEntry_Object = MibTableRow
flLta41ma_V2MacAddressGlobalEntry = _FlLta41ma_V2MacAddressGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 1, 1)
)
flLta41ma_V2MacAddressGlobalEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2MacAddressGlobalEntry.setStatus("current")


class _FlLta41ma_V2ClearDynamicMacTable_Type(Integer32):
    """Custom type flLta41ma_V2ClearDynamicMacTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlLta41ma_V2ClearDynamicMacTable_Type.__name__ = "Integer32"
_FlLta41ma_V2ClearDynamicMacTable_Object = MibTableColumn
flLta41ma_V2ClearDynamicMacTable = _FlLta41ma_V2ClearDynamicMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 1, 1, 1),
    _FlLta41ma_V2ClearDynamicMacTable_Type()
)
flLta41ma_V2ClearDynamicMacTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2ClearDynamicMacTable.setStatus("current")


class _FlLta41ma_V2ClearStaticMacTable_Type(Integer32):
    """Custom type flLta41ma_V2ClearStaticMacTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlLta41ma_V2ClearStaticMacTable_Type.__name__ = "Integer32"
_FlLta41ma_V2ClearStaticMacTable_Object = MibTableColumn
flLta41ma_V2ClearStaticMacTable = _FlLta41ma_V2ClearStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 1, 1, 2),
    _FlLta41ma_V2ClearStaticMacTable_Type()
)
flLta41ma_V2ClearStaticMacTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2ClearStaticMacTable.setStatus("current")


class _FlLta41ma_V2MacLinkDownFlush_Type(Integer32):
    """Custom type flLta41ma_V2MacLinkDownFlush based on Integer32"""
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


_FlLta41ma_V2MacLinkDownFlush_Type.__name__ = "Integer32"
_FlLta41ma_V2MacLinkDownFlush_Object = MibTableColumn
flLta41ma_V2MacLinkDownFlush = _FlLta41ma_V2MacLinkDownFlush_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 1, 1, 3),
    _FlLta41ma_V2MacLinkDownFlush_Type()
)
flLta41ma_V2MacLinkDownFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2MacLinkDownFlush.setStatus("current")
_FlLta41ma_V2DynamicMacTable_Object = MibTable
flLta41ma_V2DynamicMacTable = _FlLta41ma_V2DynamicMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 10)
)
if mibBuilder.loadTexts:
    flLta41ma_V2DynamicMacTable.setStatus("current")
_FlLta41ma_V2DynamicMacEntry_Object = MibTableRow
flLta41ma_V2DynamicMacEntry = _FlLta41ma_V2DynamicMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 10, 1)
)
flLta41ma_V2DynamicMacEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2DynamicEntryNumber"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2DynamicMacEntry.setStatus("current")


class _FlLta41ma_V2DynamicEntryNumber_Type(Integer32):
    """Custom type flLta41ma_V2DynamicEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FlLta41ma_V2DynamicEntryNumber_Type.__name__ = "Integer32"
_FlLta41ma_V2DynamicEntryNumber_Object = MibTableColumn
flLta41ma_V2DynamicEntryNumber = _FlLta41ma_V2DynamicEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 10, 1, 1),
    _FlLta41ma_V2DynamicEntryNumber_Type()
)
flLta41ma_V2DynamicEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2DynamicEntryNumber.setStatus("current")
_FlLta41ma_V2DynamicMacAddress_Type = DisplayString
_FlLta41ma_V2DynamicMacAddress_Object = MibTableColumn
flLta41ma_V2DynamicMacAddress = _FlLta41ma_V2DynamicMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 10, 1, 2),
    _FlLta41ma_V2DynamicMacAddress_Type()
)
flLta41ma_V2DynamicMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2DynamicMacAddress.setStatus("current")
_FlLta41ma_V2SrcPort_Type = Integer32
_FlLta41ma_V2SrcPort_Object = MibTableColumn
flLta41ma_V2SrcPort = _FlLta41ma_V2SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 10, 1, 3),
    _FlLta41ma_V2SrcPort_Type()
)
flLta41ma_V2SrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2SrcPort.setStatus("current")


class _FlLta41ma_V2DynamicFid_Type(Integer32):
    """Custom type flLta41ma_V2DynamicFid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FlLta41ma_V2DynamicFid_Type.__name__ = "Integer32"
_FlLta41ma_V2DynamicFid_Object = MibTableColumn
flLta41ma_V2DynamicFid = _FlLta41ma_V2DynamicFid_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 10, 1, 4),
    _FlLta41ma_V2DynamicFid_Type()
)
flLta41ma_V2DynamicFid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2DynamicFid.setStatus("current")
_FlLta41ma_V2StaticMacTable_Object = MibTable
flLta41ma_V2StaticMacTable = _FlLta41ma_V2StaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 20)
)
if mibBuilder.loadTexts:
    flLta41ma_V2StaticMacTable.setStatus("current")
_FlLta41ma_V2StaticMacEntry_Object = MibTableRow
flLta41ma_V2StaticMacEntry = _FlLta41ma_V2StaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 20, 1)
)
flLta41ma_V2StaticMacEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2StaticEntryNumber"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2StaticMacEntry.setStatus("current")


class _FlLta41ma_V2StaticEntryNumber_Type(Integer32):
    """Custom type flLta41ma_V2StaticEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FlLta41ma_V2StaticEntryNumber_Type.__name__ = "Integer32"
_FlLta41ma_V2StaticEntryNumber_Object = MibTableColumn
flLta41ma_V2StaticEntryNumber = _FlLta41ma_V2StaticEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 20, 1, 1),
    _FlLta41ma_V2StaticEntryNumber_Type()
)
flLta41ma_V2StaticEntryNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2StaticEntryNumber.setStatus("current")
_FlLta41ma_V2StaticMacAddress_Type = DisplayString
_FlLta41ma_V2StaticMacAddress_Object = MibTableColumn
flLta41ma_V2StaticMacAddress = _FlLta41ma_V2StaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 20, 1, 2),
    _FlLta41ma_V2StaticMacAddress_Type()
)
flLta41ma_V2StaticMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2StaticMacAddress.setStatus("current")


class _FlLta41ma_V2FwdPort1_Type(Integer32):
    """Custom type flLta41ma_V2FwdPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FlLta41ma_V2FwdPort1_Type.__name__ = "Integer32"
_FlLta41ma_V2FwdPort1_Object = MibTableColumn
flLta41ma_V2FwdPort1 = _FlLta41ma_V2FwdPort1_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 20, 1, 3),
    _FlLta41ma_V2FwdPort1_Type()
)
flLta41ma_V2FwdPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2FwdPort1.setStatus("current")


class _FlLta41ma_V2FwdPort2_Type(Integer32):
    """Custom type flLta41ma_V2FwdPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FlLta41ma_V2FwdPort2_Type.__name__ = "Integer32"
_FlLta41ma_V2FwdPort2_Object = MibTableColumn
flLta41ma_V2FwdPort2 = _FlLta41ma_V2FwdPort2_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 20, 1, 4),
    _FlLta41ma_V2FwdPort2_Type()
)
flLta41ma_V2FwdPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2FwdPort2.setStatus("current")


class _FlLta41ma_V2FwdPort3_Type(Integer32):
    """Custom type flLta41ma_V2FwdPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FlLta41ma_V2FwdPort3_Type.__name__ = "Integer32"
_FlLta41ma_V2FwdPort3_Object = MibTableColumn
flLta41ma_V2FwdPort3 = _FlLta41ma_V2FwdPort3_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 20, 1, 5),
    _FlLta41ma_V2FwdPort3_Type()
)
flLta41ma_V2FwdPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2FwdPort3.setStatus("current")


class _FlLta41ma_V2FwdPort4_Type(Integer32):
    """Custom type flLta41ma_V2FwdPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FlLta41ma_V2FwdPort4_Type.__name__ = "Integer32"
_FlLta41ma_V2FwdPort4_Object = MibTableColumn
flLta41ma_V2FwdPort4 = _FlLta41ma_V2FwdPort4_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 20, 1, 6),
    _FlLta41ma_V2FwdPort4_Type()
)
flLta41ma_V2FwdPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2FwdPort4.setStatus("current")


class _FlLta41ma_V2FwdPort5_Type(Integer32):
    """Custom type flLta41ma_V2FwdPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FlLta41ma_V2FwdPort5_Type.__name__ = "Integer32"
_FlLta41ma_V2FwdPort5_Object = MibTableColumn
flLta41ma_V2FwdPort5 = _FlLta41ma_V2FwdPort5_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 20, 1, 7),
    _FlLta41ma_V2FwdPort5_Type()
)
flLta41ma_V2FwdPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2FwdPort5.setStatus("current")


class _FlLta41ma_V2Fid_Type(Integer32):
    """Custom type flLta41ma_V2Fid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FlLta41ma_V2Fid_Type.__name__ = "Integer32"
_FlLta41ma_V2Fid_Object = MibTableColumn
flLta41ma_V2Fid = _FlLta41ma_V2Fid_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 20, 1, 8),
    _FlLta41ma_V2Fid_Type()
)
flLta41ma_V2Fid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2Fid.setStatus("current")


class _FlLta41ma_V2StaticUseFid_Type(Integer32):
    """Custom type flLta41ma_V2StaticUseFid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FlLta41ma_V2StaticUseFid_Type.__name__ = "Integer32"
_FlLta41ma_V2StaticUseFid_Object = MibTableColumn
flLta41ma_V2StaticUseFid = _FlLta41ma_V2StaticUseFid_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 20, 1, 9),
    _FlLta41ma_V2StaticUseFid_Type()
)
flLta41ma_V2StaticUseFid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2StaticUseFid.setStatus("current")
_FlLta41ma_V2StaticMacTableStatus_Type = EntryStatus
_FlLta41ma_V2StaticMacTableStatus_Object = MibTableColumn
flLta41ma_V2StaticMacTableStatus = _FlLta41ma_V2StaticMacTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 50, 20, 1, 10),
    _FlLta41ma_V2StaticMacTableStatus_Type()
)
flLta41ma_V2StaticMacTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2StaticMacTableStatus.setStatus("current")
_FlLta41ma_V2Statistics_ObjectIdentity = ObjectIdentity
flLta41ma_V2Statistics = _FlLta41ma_V2Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60)
)
_FlLta41ma_V2RxErrorPacketsTable_Object = MibTable
flLta41ma_V2RxErrorPacketsTable = _FlLta41ma_V2RxErrorPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 10)
)
if mibBuilder.loadTexts:
    flLta41ma_V2RxErrorPacketsTable.setStatus("current")
_FlLta41ma_V2RxErrorPacketsEntry_Object = MibTableRow
flLta41ma_V2RxErrorPacketsEntry = _FlLta41ma_V2RxErrorPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 10, 1)
)
flLta41ma_V2RxErrorPacketsEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortNumber"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2RxErrorPacketsEntry.setStatus("current")
_FlLta41ma_V2RxUndersizePackets_Type = Counter32
_FlLta41ma_V2RxUndersizePackets_Object = MibTableColumn
flLta41ma_V2RxUndersizePackets = _FlLta41ma_V2RxUndersizePackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 10, 1, 1),
    _FlLta41ma_V2RxUndersizePackets_Type()
)
flLta41ma_V2RxUndersizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2RxUndersizePackets.setStatus("current")
_FlLta41ma_V2RxFragmentPackets_Type = Counter32
_FlLta41ma_V2RxFragmentPackets_Object = MibTableColumn
flLta41ma_V2RxFragmentPackets = _FlLta41ma_V2RxFragmentPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 10, 1, 2),
    _FlLta41ma_V2RxFragmentPackets_Type()
)
flLta41ma_V2RxFragmentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2RxFragmentPackets.setStatus("current")
_FlLta41ma_V2RxOversizePackets_Type = Counter32
_FlLta41ma_V2RxOversizePackets_Object = MibTableColumn
flLta41ma_V2RxOversizePackets = _FlLta41ma_V2RxOversizePackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 10, 1, 3),
    _FlLta41ma_V2RxOversizePackets_Type()
)
flLta41ma_V2RxOversizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2RxOversizePackets.setStatus("current")
_FlLta41ma_V2RxCrcErrorPackets_Type = Counter32
_FlLta41ma_V2RxCrcErrorPackets_Object = MibTableColumn
flLta41ma_V2RxCrcErrorPackets = _FlLta41ma_V2RxCrcErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 10, 1, 4),
    _FlLta41ma_V2RxCrcErrorPackets_Type()
)
flLta41ma_V2RxCrcErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2RxCrcErrorPackets.setStatus("current")
_FlLta41ma_V2RxAlignmentErrorPackets_Type = Counter32
_FlLta41ma_V2RxAlignmentErrorPackets_Object = MibTableColumn
flLta41ma_V2RxAlignmentErrorPackets = _FlLta41ma_V2RxAlignmentErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 10, 1, 5),
    _FlLta41ma_V2RxAlignmentErrorPackets_Type()
)
flLta41ma_V2RxAlignmentErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2RxAlignmentErrorPackets.setStatus("current")


class _FlLta41ma_V2RxRefreshCounters_Type(Integer32):
    """Custom type flLta41ma_V2RxRefreshCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("refresh", 2))
    )


_FlLta41ma_V2RxRefreshCounters_Type.__name__ = "Integer32"
_FlLta41ma_V2RxRefreshCounters_Object = MibTableColumn
flLta41ma_V2RxRefreshCounters = _FlLta41ma_V2RxRefreshCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 10, 1, 6),
    _FlLta41ma_V2RxRefreshCounters_Type()
)
flLta41ma_V2RxRefreshCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2RxRefreshCounters.setStatus("current")


class _FlLta41ma_V2RxClearCounters_Type(Integer32):
    """Custom type flLta41ma_V2RxClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlLta41ma_V2RxClearCounters_Type.__name__ = "Integer32"
_FlLta41ma_V2RxClearCounters_Object = MibTableColumn
flLta41ma_V2RxClearCounters = _FlLta41ma_V2RxClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 10, 1, 7),
    _FlLta41ma_V2RxClearCounters_Type()
)
flLta41ma_V2RxClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2RxClearCounters.setStatus("current")
_FlLta41ma_V2RxGoodPacketsTable_Object = MibTable
flLta41ma_V2RxGoodPacketsTable = _FlLta41ma_V2RxGoodPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 20)
)
if mibBuilder.loadTexts:
    flLta41ma_V2RxGoodPacketsTable.setStatus("current")
_FlLta41ma_V2RxGoodPacketsEntry_Object = MibTableRow
flLta41ma_V2RxGoodPacketsEntry = _FlLta41ma_V2RxGoodPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 20, 1)
)
flLta41ma_V2RxGoodPacketsEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortNumber"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2RxGoodPacketsEntry.setStatus("current")
_FlLta41ma_V2RxUnicastPackets_Type = Counter32
_FlLta41ma_V2RxUnicastPackets_Object = MibTableColumn
flLta41ma_V2RxUnicastPackets = _FlLta41ma_V2RxUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 20, 1, 1),
    _FlLta41ma_V2RxUnicastPackets_Type()
)
flLta41ma_V2RxUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2RxUnicastPackets.setStatus("current")
_FlLta41ma_V2RxMulticastPackets_Type = Counter32
_FlLta41ma_V2RxMulticastPackets_Object = MibTableColumn
flLta41ma_V2RxMulticastPackets = _FlLta41ma_V2RxMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 20, 1, 2),
    _FlLta41ma_V2RxMulticastPackets_Type()
)
flLta41ma_V2RxMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2RxMulticastPackets.setStatus("current")
_FlLta41ma_V2RxBroadcastPackets_Type = Counter32
_FlLta41ma_V2RxBroadcastPackets_Object = MibTableColumn
flLta41ma_V2RxBroadcastPackets = _FlLta41ma_V2RxBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 20, 1, 3),
    _FlLta41ma_V2RxBroadcastPackets_Type()
)
flLta41ma_V2RxBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2RxBroadcastPackets.setStatus("current")
_FlLta41ma_V2RxMacControlPackets_Type = Counter32
_FlLta41ma_V2RxMacControlPackets_Object = MibTableColumn
flLta41ma_V2RxMacControlPackets = _FlLta41ma_V2RxMacControlPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 20, 1, 4),
    _FlLta41ma_V2RxMacControlPackets_Type()
)
flLta41ma_V2RxMacControlPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2RxMacControlPackets.setStatus("current")
_FlLta41ma_V2RxPausePackets_Type = Counter32
_FlLta41ma_V2RxPausePackets_Object = MibTableColumn
flLta41ma_V2RxPausePackets = _FlLta41ma_V2RxPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 20, 1, 5),
    _FlLta41ma_V2RxPausePackets_Type()
)
flLta41ma_V2RxPausePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2RxPausePackets.setStatus("current")


class _FlLta41ma_V2RxRefreshGoodCounters_Type(Integer32):
    """Custom type flLta41ma_V2RxRefreshGoodCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("refresh", 2))
    )


_FlLta41ma_V2RxRefreshGoodCounters_Type.__name__ = "Integer32"
_FlLta41ma_V2RxRefreshGoodCounters_Object = MibTableColumn
flLta41ma_V2RxRefreshGoodCounters = _FlLta41ma_V2RxRefreshGoodCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 20, 1, 6),
    _FlLta41ma_V2RxRefreshGoodCounters_Type()
)
flLta41ma_V2RxRefreshGoodCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2RxRefreshGoodCounters.setStatus("current")


class _FlLta41ma_V2RxClearGoodCounters_Type(Integer32):
    """Custom type flLta41ma_V2RxClearGoodCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlLta41ma_V2RxClearGoodCounters_Type.__name__ = "Integer32"
_FlLta41ma_V2RxClearGoodCounters_Object = MibTableColumn
flLta41ma_V2RxClearGoodCounters = _FlLta41ma_V2RxClearGoodCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 20, 1, 7),
    _FlLta41ma_V2RxClearGoodCounters_Type()
)
flLta41ma_V2RxClearGoodCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2RxClearGoodCounters.setStatus("current")
_FlLta41ma_V2TxGoodPacketsTable_Object = MibTable
flLta41ma_V2TxGoodPacketsTable = _FlLta41ma_V2TxGoodPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 30)
)
if mibBuilder.loadTexts:
    flLta41ma_V2TxGoodPacketsTable.setStatus("current")
_FlLta41ma_V2TxGoodPacketsEntry_Object = MibTableRow
flLta41ma_V2TxGoodPacketsEntry = _FlLta41ma_V2TxGoodPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 30, 1)
)
flLta41ma_V2TxGoodPacketsEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortNumber"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2TxGoodPacketsEntry.setStatus("current")
_FlLta41ma_V2TxUnicastPackets_Type = Counter32
_FlLta41ma_V2TxUnicastPackets_Object = MibTableColumn
flLta41ma_V2TxUnicastPackets = _FlLta41ma_V2TxUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 30, 1, 1),
    _FlLta41ma_V2TxUnicastPackets_Type()
)
flLta41ma_V2TxUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2TxUnicastPackets.setStatus("current")
_FlLta41ma_V2TxMulticastPackets_Type = Counter32
_FlLta41ma_V2TxMulticastPackets_Object = MibTableColumn
flLta41ma_V2TxMulticastPackets = _FlLta41ma_V2TxMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 30, 1, 2),
    _FlLta41ma_V2TxMulticastPackets_Type()
)
flLta41ma_V2TxMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2TxMulticastPackets.setStatus("current")
_FlLta41ma_V2TxBroadcastPackets_Type = Counter32
_FlLta41ma_V2TxBroadcastPackets_Object = MibTableColumn
flLta41ma_V2TxBroadcastPackets = _FlLta41ma_V2TxBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 30, 1, 3),
    _FlLta41ma_V2TxBroadcastPackets_Type()
)
flLta41ma_V2TxBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2TxBroadcastPackets.setStatus("current")
_FlLta41ma_V2TxPausePackets_Type = Counter32
_FlLta41ma_V2TxPausePackets_Object = MibTableColumn
flLta41ma_V2TxPausePackets = _FlLta41ma_V2TxPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 30, 1, 4),
    _FlLta41ma_V2TxPausePackets_Type()
)
flLta41ma_V2TxPausePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2TxPausePackets.setStatus("current")


class _FlLta41ma_V2TxRefreshGoodCounters_Type(Integer32):
    """Custom type flLta41ma_V2TxRefreshGoodCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("refresh", 2))
    )


_FlLta41ma_V2TxRefreshGoodCounters_Type.__name__ = "Integer32"
_FlLta41ma_V2TxRefreshGoodCounters_Object = MibTableColumn
flLta41ma_V2TxRefreshGoodCounters = _FlLta41ma_V2TxRefreshGoodCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 30, 1, 5),
    _FlLta41ma_V2TxRefreshGoodCounters_Type()
)
flLta41ma_V2TxRefreshGoodCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2TxRefreshGoodCounters.setStatus("current")


class _FlLta41ma_V2TxClearGoodCounters_Type(Integer32):
    """Custom type flLta41ma_V2TxClearGoodCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlLta41ma_V2TxClearGoodCounters_Type.__name__ = "Integer32"
_FlLta41ma_V2TxClearGoodCounters_Object = MibTableColumn
flLta41ma_V2TxClearGoodCounters = _FlLta41ma_V2TxClearGoodCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 30, 1, 6),
    _FlLta41ma_V2TxClearGoodCounters_Type()
)
flLta41ma_V2TxClearGoodCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2TxClearGoodCounters.setStatus("current")
_FlLta41ma_V2RxTotalPacketsTable_Object = MibTable
flLta41ma_V2RxTotalPacketsTable = _FlLta41ma_V2RxTotalPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 40)
)
if mibBuilder.loadTexts:
    flLta41ma_V2RxTotalPacketsTable.setStatus("current")
_FlLta41ma_V2RxTotalPacketsEntry_Object = MibTableRow
flLta41ma_V2RxTotalPacketsEntry = _FlLta41ma_V2RxTotalPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 40, 1)
)
flLta41ma_V2RxTotalPacketsEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortNumber"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2RxTotalPacketsEntry.setStatus("current")
_FlLta41ma_V2RxDroppedPackets_Type = Counter32
_FlLta41ma_V2RxDroppedPackets_Object = MibTableColumn
flLta41ma_V2RxDroppedPackets = _FlLta41ma_V2RxDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 40, 1, 1),
    _FlLta41ma_V2RxDroppedPackets_Type()
)
flLta41ma_V2RxDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2RxDroppedPackets.setStatus("current")
_FlLta41ma_V2Rx64BytesPackets_Type = Counter32
_FlLta41ma_V2Rx64BytesPackets_Object = MibTableColumn
flLta41ma_V2Rx64BytesPackets = _FlLta41ma_V2Rx64BytesPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 40, 1, 2),
    _FlLta41ma_V2Rx64BytesPackets_Type()
)
flLta41ma_V2Rx64BytesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2Rx64BytesPackets.setStatus("current")
_FlLta41ma_V2Rx65_127BytesPackets_Type = Counter32
_FlLta41ma_V2Rx65_127BytesPackets_Object = MibTableColumn
flLta41ma_V2Rx65_127BytesPackets = _FlLta41ma_V2Rx65_127BytesPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 40, 1, 3),
    _FlLta41ma_V2Rx65_127BytesPackets_Type()
)
flLta41ma_V2Rx65_127BytesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2Rx65_127BytesPackets.setStatus("current")
_FlLta41ma_V2Rx128_255BytesPackets_Type = Counter32
_FlLta41ma_V2Rx128_255BytesPackets_Object = MibTableColumn
flLta41ma_V2Rx128_255BytesPackets = _FlLta41ma_V2Rx128_255BytesPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 40, 1, 4),
    _FlLta41ma_V2Rx128_255BytesPackets_Type()
)
flLta41ma_V2Rx128_255BytesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2Rx128_255BytesPackets.setStatus("current")
_FlLta41ma_V2Rx256_511BytesPackets_Type = Counter32
_FlLta41ma_V2Rx256_511BytesPackets_Object = MibTableColumn
flLta41ma_V2Rx256_511BytesPackets = _FlLta41ma_V2Rx256_511BytesPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 40, 1, 5),
    _FlLta41ma_V2Rx256_511BytesPackets_Type()
)
flLta41ma_V2Rx256_511BytesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2Rx256_511BytesPackets.setStatus("current")
_FlLta41ma_V2Rx512_1023BytesPackets_Type = Counter32
_FlLta41ma_V2Rx512_1023BytesPackets_Object = MibTableColumn
flLta41ma_V2Rx512_1023BytesPackets = _FlLta41ma_V2Rx512_1023BytesPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 40, 1, 6),
    _FlLta41ma_V2Rx512_1023BytesPackets_Type()
)
flLta41ma_V2Rx512_1023BytesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2Rx512_1023BytesPackets.setStatus("current")
_FlLta41ma_V2Rx1024_MaxBytesPackets_Type = Counter32
_FlLta41ma_V2Rx1024_MaxBytesPackets_Object = MibTableColumn
flLta41ma_V2Rx1024_MaxBytesPackets = _FlLta41ma_V2Rx1024_MaxBytesPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 40, 1, 7),
    _FlLta41ma_V2Rx1024_MaxBytesPackets_Type()
)
flLta41ma_V2Rx1024_MaxBytesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2Rx1024_MaxBytesPackets.setStatus("current")


class _FlLta41ma_V2RxRefreshTotalCounters_Type(Integer32):
    """Custom type flLta41ma_V2RxRefreshTotalCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("refresh", 2))
    )


_FlLta41ma_V2RxRefreshTotalCounters_Type.__name__ = "Integer32"
_FlLta41ma_V2RxRefreshTotalCounters_Object = MibTableColumn
flLta41ma_V2RxRefreshTotalCounters = _FlLta41ma_V2RxRefreshTotalCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 40, 1, 8),
    _FlLta41ma_V2RxRefreshTotalCounters_Type()
)
flLta41ma_V2RxRefreshTotalCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2RxRefreshTotalCounters.setStatus("current")


class _FlLta41ma_V2RxClearTotalCounters_Type(Integer32):
    """Custom type flLta41ma_V2RxClearTotalCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlLta41ma_V2RxClearTotalCounters_Type.__name__ = "Integer32"
_FlLta41ma_V2RxClearTotalCounters_Object = MibTableColumn
flLta41ma_V2RxClearTotalCounters = _FlLta41ma_V2RxClearTotalCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 40, 1, 9),
    _FlLta41ma_V2RxClearTotalCounters_Type()
)
flLta41ma_V2RxClearTotalCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2RxClearTotalCounters.setStatus("current")
_FlLta41ma_V2TxTotalPacketsTable_Object = MibTable
flLta41ma_V2TxTotalPacketsTable = _FlLta41ma_V2TxTotalPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 50)
)
if mibBuilder.loadTexts:
    flLta41ma_V2TxTotalPacketsTable.setStatus("current")
_FlLta41ma_V2TxTotalPacketsEntry_Object = MibTableRow
flLta41ma_V2TxTotalPacketsEntry = _FlLta41ma_V2TxTotalPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 50, 1)
)
flLta41ma_V2TxTotalPacketsEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortNumber"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2TxTotalPacketsEntry.setStatus("current")
_FlLta41ma_V2TxDroppedPackets_Type = Counter32
_FlLta41ma_V2TxDroppedPackets_Object = MibTableColumn
flLta41ma_V2TxDroppedPackets = _FlLta41ma_V2TxDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 50, 1, 1),
    _FlLta41ma_V2TxDroppedPackets_Type()
)
flLta41ma_V2TxDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2TxDroppedPackets.setStatus("current")


class _FlLta41ma_V2TxRefreshTotalCounters_Type(Integer32):
    """Custom type flLta41ma_V2TxRefreshTotalCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("refresh", 2))
    )


_FlLta41ma_V2TxRefreshTotalCounters_Type.__name__ = "Integer32"
_FlLta41ma_V2TxRefreshTotalCounters_Object = MibTableColumn
flLta41ma_V2TxRefreshTotalCounters = _FlLta41ma_V2TxRefreshTotalCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 50, 1, 2),
    _FlLta41ma_V2TxRefreshTotalCounters_Type()
)
flLta41ma_V2TxRefreshTotalCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2TxRefreshTotalCounters.setStatus("current")


class _FlLta41ma_V2TxClearTotalCounters_Type(Integer32):
    """Custom type flLta41ma_V2TxClearTotalCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlLta41ma_V2TxClearTotalCounters_Type.__name__ = "Integer32"
_FlLta41ma_V2TxClearTotalCounters_Object = MibTableColumn
flLta41ma_V2TxClearTotalCounters = _FlLta41ma_V2TxClearTotalCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 50, 1, 3),
    _FlLta41ma_V2TxClearTotalCounters_Type()
)
flLta41ma_V2TxClearTotalCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2TxClearTotalCounters.setStatus("current")
_FlLta41ma_V2TxCollisionsTable_Object = MibTable
flLta41ma_V2TxCollisionsTable = _FlLta41ma_V2TxCollisionsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 60)
)
if mibBuilder.loadTexts:
    flLta41ma_V2TxCollisionsTable.setStatus("current")
_FlLta41ma_V2TxCollisionsEntry_Object = MibTableRow
flLta41ma_V2TxCollisionsEntry = _FlLta41ma_V2TxCollisionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 60, 1)
)
flLta41ma_V2TxCollisionsEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortNumber"),
)
if mibBuilder.loadTexts:
    flLta41ma_V2TxCollisionsEntry.setStatus("current")
_FlLta41ma_V2TxTotalCols_Type = Counter32
_FlLta41ma_V2TxTotalCols_Object = MibTableColumn
flLta41ma_V2TxTotalCols = _FlLta41ma_V2TxTotalCols_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 60, 1, 1),
    _FlLta41ma_V2TxTotalCols_Type()
)
flLta41ma_V2TxTotalCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2TxTotalCols.setStatus("current")
_FlLta41ma_V2TxLateCols_Type = Counter32
_FlLta41ma_V2TxLateCols_Object = MibTableColumn
flLta41ma_V2TxLateCols = _FlLta41ma_V2TxLateCols_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 60, 1, 2),
    _FlLta41ma_V2TxLateCols_Type()
)
flLta41ma_V2TxLateCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2TxLateCols.setStatus("current")
_FlLta41ma_V2TxExcessiveCols_Type = Counter32
_FlLta41ma_V2TxExcessiveCols_Object = MibTableColumn
flLta41ma_V2TxExcessiveCols = _FlLta41ma_V2TxExcessiveCols_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 60, 1, 3),
    _FlLta41ma_V2TxExcessiveCols_Type()
)
flLta41ma_V2TxExcessiveCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2TxExcessiveCols.setStatus("current")
_FlLta41ma_V2TxSingleCols_Type = Counter32
_FlLta41ma_V2TxSingleCols_Object = MibTableColumn
flLta41ma_V2TxSingleCols = _FlLta41ma_V2TxSingleCols_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 60, 1, 4),
    _FlLta41ma_V2TxSingleCols_Type()
)
flLta41ma_V2TxSingleCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2TxSingleCols.setStatus("current")
_FlLta41ma_V2TxMultipleCols_Type = Counter32
_FlLta41ma_V2TxMultipleCols_Object = MibTableColumn
flLta41ma_V2TxMultipleCols = _FlLta41ma_V2TxMultipleCols_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 60, 1, 5),
    _FlLta41ma_V2TxMultipleCols_Type()
)
flLta41ma_V2TxMultipleCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41ma_V2TxMultipleCols.setStatus("current")


class _FlLta41ma_V2TxRefreshColCounters_Type(Integer32):
    """Custom type flLta41ma_V2TxRefreshColCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("refresh", 2))
    )


_FlLta41ma_V2TxRefreshColCounters_Type.__name__ = "Integer32"
_FlLta41ma_V2TxRefreshColCounters_Object = MibTableColumn
flLta41ma_V2TxRefreshColCounters = _FlLta41ma_V2TxRefreshColCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 60, 1, 6),
    _FlLta41ma_V2TxRefreshColCounters_Type()
)
flLta41ma_V2TxRefreshColCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2TxRefreshColCounters.setStatus("current")


class _FlLta41ma_V2TxClearColCounters_Type(Integer32):
    """Custom type flLta41ma_V2TxClearColCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlLta41ma_V2TxClearColCounters_Type.__name__ = "Integer32"
_FlLta41ma_V2TxClearColCounters_Object = MibTableColumn
flLta41ma_V2TxClearColCounters = _FlLta41ma_V2TxClearColCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 60, 60, 1, 7),
    _FlLta41ma_V2TxClearColCounters_Type()
)
flLta41ma_V2TxClearColCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41ma_V2TxClearColCounters.setStatus("current")

# Managed Objects groups

flLta41ma_V2GlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 1, 2, 1)
)
flLta41ma_V2GlobalGroup.setObjects(
      *(("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2GlobalBufferShare"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2GlobalMulticastProtection"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2GlobalBroadcastRate"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2GlobalMaxPacketSize"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2GlobalSleLogic"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2GlobalSlePort1"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2GlobalSlePort2"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2GlobalSlePort3"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2GlobalSlePort4"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RestartDevice"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RestoreDefaults"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2Temperature"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2FirmRevision"))
)
if mibBuilder.loadTexts:
    flLta41ma_V2GlobalGroup.setStatus("current")

flLta41ma_V2PortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 1, 2, 2)
)
flLta41ma_V2PortsGroup.setObjects(
      *(("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortNumber"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortType"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortLink"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortDescription"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortAutoNego"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortDuplex"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortDatarate"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortEnabled"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortAutoCross"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortMdix"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortFef"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortReset"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortBroadcastProtection"))
)
if mibBuilder.loadTexts:
    flLta41ma_V2PortsGroup.setStatus("current")

flLta41ma_V2PortsBwConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 1, 2, 3)
)
flLta41ma_V2PortsBwConfigGroup.setObjects(
      *(("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortRxHighBw"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortTxHighBw"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortRxLowBw"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortTxLowBw"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortRxDiffBw"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortRxHighFlowControl"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortRxLowFlowControl"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortTxDiffBw"))
)
if mibBuilder.loadTexts:
    flLta41ma_V2PortsBwConfigGroup.setStatus("current")

flLta41ma_V2VlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 1, 2, 4)
)
flLta41ma_V2VlanConfigGroup.setObjects(
      *(("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2Vlan8021q"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2VlanNullVidReplace"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2CreateDefaultVlans"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2DeleteAllVlans"))
)
if mibBuilder.loadTexts:
    flLta41ma_V2VlanConfigGroup.setStatus("current")

flLta41ma_V2VlanTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 1, 2, 5)
)
flLta41ma_V2VlanTableGroup.setObjects(
      *(("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2VlanFid"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2VlanVid"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2VlanName"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2VlanPort1Member"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2VlanPort2Member"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2VlanPort3Member"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2VlanPort4Member"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2VlanPort5Member"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2VlanTableStatus"))
)
if mibBuilder.loadTexts:
    flLta41ma_V2VlanTableGroup.setStatus("current")

flLta41ma_V2VlanPortsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 1, 2, 6)
)
flLta41ma_V2VlanPortsConfigGroup.setObjects(
      *(("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortIngressFilter"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortTagInsertion"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortTagRemoval"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortVid"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortDiscardNonPvid"))
)
if mibBuilder.loadTexts:
    flLta41ma_V2VlanPortsConfigGroup.setStatus("current")

flLta41ma_V2PriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 1, 2, 7)
)
flLta41ma_V2PriorityGroup.setObjects(
      *(("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PriorityRatio"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V28021pBase"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2DscpCode"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2DscpCodePriority"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortPriority"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2Port8021pClassification"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortDiffServClassification"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortUserPriority"))
)
if mibBuilder.loadTexts:
    flLta41ma_V2PriorityGroup.setStatus("current")

flLta41ma_V2MacGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 1, 2, 8)
)
flLta41ma_V2MacGroup.setObjects(
      *(("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2ClearDynamicMacTable"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2ClearStaticMacTable"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2DynamicEntryNumber"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2DynamicMacAddress"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2SrcPort"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2DynamicFid"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2StaticEntryNumber"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2StaticMacAddress"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2FwdPort1"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2FwdPort2"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2FwdPort3"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2FwdPort4"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2FwdPort5"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2Fid"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2StaticUseFid"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2StaticMacTableStatus"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2MacLinkDownFlush"))
)
if mibBuilder.loadTexts:
    flLta41ma_V2MacGroup.setStatus("current")

flLta41ma_V2StatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 1, 2, 9)
)
flLta41ma_V2StatisticsGroup.setObjects(
      *(("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2ClearDynamicMacTable"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxUndersizePackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxFragmentPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxOversizePackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxCrcErrorPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxAlignmentErrorPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxRefreshCounters"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxClearCounters"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxUnicastPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxMulticastPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxBroadcastPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxMacControlPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxPausePackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxRefreshGoodCounters"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxClearGoodCounters"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxUnicastPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxMulticastPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxBroadcastPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxPausePackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxRefreshGoodCounters"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxClearGoodCounters"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxDroppedPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2Rx64BytesPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2Rx65-127BytesPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2Rx128-255BytesPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2Rx256-511BytesPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2Rx512-1023BytesPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2Rx1024-MaxBytesPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxRefreshTotalCounters"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2RxClearTotalCounters"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxDroppedPackets"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxRefreshTotalCounters"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxClearTotalCounters"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxTotalCols"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxLateCols"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxExcessiveCols"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxSingleCols"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxMultipleCols"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxRefreshColCounters"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2TxClearColCounters"))
)
if mibBuilder.loadTexts:
    flLta41ma_V2StatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flLta41ma_V2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 1, 1, 1)
)
flLta41ma_V2MIBCompliance.setObjects(
      *(("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2GlobalGroup"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortsGroup"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PortsBwConfigGroup"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2VlanConfigGroup"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2VlanTableGroup"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2VlanPortsConfigGroup"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2PriorityGroup"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2MacGroup"),
        ("FIBROLAN-MIB-LTA41MA-V2", "flLta41ma-V2StatisticsGroup"))
)
if mibBuilder.loadTexts:
    flLta41ma_V2MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-LTA41MA-V2",
    **{"EntryStatus": EntryStatus,
       "fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMaRemoteDevice": flMaRemoteDevice,
       "flLta41ma-V2": flLta41ma_V2,
       "flLta41ma-V2MIBConformance": flLta41ma_V2MIBConformance,
       "flLta41ma-V2MIBCompliances": flLta41ma_V2MIBCompliances,
       "flLta41ma-V2MIBCompliance": flLta41ma_V2MIBCompliance,
       "flLta41ma-V2MIBGroups": flLta41ma_V2MIBGroups,
       "flLta41ma-V2GlobalGroup": flLta41ma_V2GlobalGroup,
       "flLta41ma-V2PortsGroup": flLta41ma_V2PortsGroup,
       "flLta41ma-V2PortsBwConfigGroup": flLta41ma_V2PortsBwConfigGroup,
       "flLta41ma-V2VlanConfigGroup": flLta41ma_V2VlanConfigGroup,
       "flLta41ma-V2VlanTableGroup": flLta41ma_V2VlanTableGroup,
       "flLta41ma-V2VlanPortsConfigGroup": flLta41ma_V2VlanPortsConfigGroup,
       "flLta41ma-V2PriorityGroup": flLta41ma_V2PriorityGroup,
       "flLta41ma-V2MacGroup": flLta41ma_V2MacGroup,
       "flLta41ma-V2StatisticsGroup": flLta41ma_V2StatisticsGroup,
       "flLta41ma-V2Global": flLta41ma_V2Global,
       "flLta41ma-V2GlobalConfigTable": flLta41ma_V2GlobalConfigTable,
       "flLta41ma-V2GlobalConfigEntry": flLta41ma_V2GlobalConfigEntry,
       "flLta41ma-V2GlobalBufferShare": flLta41ma_V2GlobalBufferShare,
       "flLta41ma-V2GlobalMulticastProtection": flLta41ma_V2GlobalMulticastProtection,
       "flLta41ma-V2GlobalBroadcastRate": flLta41ma_V2GlobalBroadcastRate,
       "flLta41ma-V2GlobalMaxPacketSize": flLta41ma_V2GlobalMaxPacketSize,
       "flLta41ma-V2GlobalSleLogic": flLta41ma_V2GlobalSleLogic,
       "flLta41ma-V2GlobalSlePort1": flLta41ma_V2GlobalSlePort1,
       "flLta41ma-V2GlobalSlePort2": flLta41ma_V2GlobalSlePort2,
       "flLta41ma-V2GlobalSlePort3": flLta41ma_V2GlobalSlePort3,
       "flLta41ma-V2GlobalSlePort4": flLta41ma_V2GlobalSlePort4,
       "flLta41ma-V2RestartDevice": flLta41ma_V2RestartDevice,
       "flLta41ma-V2RestoreDefaults": flLta41ma_V2RestoreDefaults,
       "flLta41ma-V2Temperature": flLta41ma_V2Temperature,
       "flLta41ma-V2FirmRevision": flLta41ma_V2FirmRevision,
       "flLta41ma-V2Ports": flLta41ma_V2Ports,
       "flLta41ma-V2PortsConfigTable": flLta41ma_V2PortsConfigTable,
       "flLta41ma-V2PortConfigEntry": flLta41ma_V2PortConfigEntry,
       "flLta41ma-V2PortNumber": flLta41ma_V2PortNumber,
       "flLta41ma-V2PortType": flLta41ma_V2PortType,
       "flLta41ma-V2PortLink": flLta41ma_V2PortLink,
       "flLta41ma-V2PortDescription": flLta41ma_V2PortDescription,
       "flLta41ma-V2PortAutoNego": flLta41ma_V2PortAutoNego,
       "flLta41ma-V2PortDuplex": flLta41ma_V2PortDuplex,
       "flLta41ma-V2PortDatarate": flLta41ma_V2PortDatarate,
       "flLta41ma-V2PortEnabled": flLta41ma_V2PortEnabled,
       "flLta41ma-V2PortAutoCross": flLta41ma_V2PortAutoCross,
       "flLta41ma-V2PortMdix": flLta41ma_V2PortMdix,
       "flLta41ma-V2PortFef": flLta41ma_V2PortFef,
       "flLta41ma-V2PortReset": flLta41ma_V2PortReset,
       "flLta41ma-V2PortBroadcastProtection": flLta41ma_V2PortBroadcastProtection,
       "flLta41ma-V2PortsBwConfigTable": flLta41ma_V2PortsBwConfigTable,
       "flLta41ma-V2PortBwConfigEntry": flLta41ma_V2PortBwConfigEntry,
       "flLta41ma-V2PortRxHighBw": flLta41ma_V2PortRxHighBw,
       "flLta41ma-V2PortTxHighBw": flLta41ma_V2PortTxHighBw,
       "flLta41ma-V2PortRxLowBw": flLta41ma_V2PortRxLowBw,
       "flLta41ma-V2PortTxLowBw": flLta41ma_V2PortTxLowBw,
       "flLta41ma-V2PortRxDiffBw": flLta41ma_V2PortRxDiffBw,
       "flLta41ma-V2PortRxHighFlowControl": flLta41ma_V2PortRxHighFlowControl,
       "flLta41ma-V2PortRxLowFlowControl": flLta41ma_V2PortRxLowFlowControl,
       "flLta41ma-V2PortTxDiffBw": flLta41ma_V2PortTxDiffBw,
       "flLta41ma-V2Vlan": flLta41ma_V2Vlan,
       "flLta41ma-V2VlanGlobalTable": flLta41ma_V2VlanGlobalTable,
       "flLta41ma-V2VlanGlobalEntry": flLta41ma_V2VlanGlobalEntry,
       "flLta41ma-V2Vlan8021q": flLta41ma_V2Vlan8021q,
       "flLta41ma-V2VlanNullVidReplace": flLta41ma_V2VlanNullVidReplace,
       "flLta41ma-V2CreateDefaultVlans": flLta41ma_V2CreateDefaultVlans,
       "flLta41ma-V2DeleteAllVlans": flLta41ma_V2DeleteAllVlans,
       "flLta41ma-V2VlansTable": flLta41ma_V2VlansTable,
       "flLta41ma-V2VlanEntry": flLta41ma_V2VlanEntry,
       "flLta41ma-V2VlanFid": flLta41ma_V2VlanFid,
       "flLta41ma-V2VlanVid": flLta41ma_V2VlanVid,
       "flLta41ma-V2VlanName": flLta41ma_V2VlanName,
       "flLta41ma-V2VlanPort1Member": flLta41ma_V2VlanPort1Member,
       "flLta41ma-V2VlanPort2Member": flLta41ma_V2VlanPort2Member,
       "flLta41ma-V2VlanPort3Member": flLta41ma_V2VlanPort3Member,
       "flLta41ma-V2VlanPort4Member": flLta41ma_V2VlanPort4Member,
       "flLta41ma-V2VlanPort5Member": flLta41ma_V2VlanPort5Member,
       "flLta41ma-V2VlanTableStatus": flLta41ma_V2VlanTableStatus,
       "flLta41ma-V2PortsVlanConfigTable": flLta41ma_V2PortsVlanConfigTable,
       "flLta41ma-V2PortVlanConfigEntry": flLta41ma_V2PortVlanConfigEntry,
       "flLta41ma-V2PortIngressFilter": flLta41ma_V2PortIngressFilter,
       "flLta41ma-V2PortTagInsertion": flLta41ma_V2PortTagInsertion,
       "flLta41ma-V2PortTagRemoval": flLta41ma_V2PortTagRemoval,
       "flLta41ma-V2PortVid": flLta41ma_V2PortVid,
       "flLta41ma-V2PortDiscardNonPvid": flLta41ma_V2PortDiscardNonPvid,
       "flLta41ma-V2Priority": flLta41ma_V2Priority,
       "flLta41ma-V2QoSGlobalTable": flLta41ma_V2QoSGlobalTable,
       "flLta41ma-V2QosGlobalEntry": flLta41ma_V2QosGlobalEntry,
       "flLta41ma-V28021pBase": flLta41ma_V28021pBase,
       "flLta41ma-V2PriorityRatio": flLta41ma_V2PriorityRatio,
       "flLta41ma-V2DscpTable": flLta41ma_V2DscpTable,
       "flLta41ma-V2DscpEntry": flLta41ma_V2DscpEntry,
       "flLta41ma-V2DscpCode": flLta41ma_V2DscpCode,
       "flLta41ma-V2DscpCodePriority": flLta41ma_V2DscpCodePriority,
       "flLta41ma-V2PortsPriorityConfigTable": flLta41ma_V2PortsPriorityConfigTable,
       "flLta41ma-V2PortPriorityConfigEntry": flLta41ma_V2PortPriorityConfigEntry,
       "flLta41ma-V2PortPriority": flLta41ma_V2PortPriority,
       "flLta41ma-V2Port8021pClassification": flLta41ma_V2Port8021pClassification,
       "flLta41ma-V2PortDiffServClassification": flLta41ma_V2PortDiffServClassification,
       "flLta41ma-V2PortUserPriority": flLta41ma_V2PortUserPriority,
       "flLta41ma-V2Mac": flLta41ma_V2Mac,
       "flLta41ma-V2MacAddressGlobalTable": flLta41ma_V2MacAddressGlobalTable,
       "flLta41ma-V2MacAddressGlobalEntry": flLta41ma_V2MacAddressGlobalEntry,
       "flLta41ma-V2ClearDynamicMacTable": flLta41ma_V2ClearDynamicMacTable,
       "flLta41ma-V2ClearStaticMacTable": flLta41ma_V2ClearStaticMacTable,
       "flLta41ma-V2MacLinkDownFlush": flLta41ma_V2MacLinkDownFlush,
       "flLta41ma-V2DynamicMacTable": flLta41ma_V2DynamicMacTable,
       "flLta41ma-V2DynamicMacEntry": flLta41ma_V2DynamicMacEntry,
       "flLta41ma-V2DynamicEntryNumber": flLta41ma_V2DynamicEntryNumber,
       "flLta41ma-V2DynamicMacAddress": flLta41ma_V2DynamicMacAddress,
       "flLta41ma-V2SrcPort": flLta41ma_V2SrcPort,
       "flLta41ma-V2DynamicFid": flLta41ma_V2DynamicFid,
       "flLta41ma-V2StaticMacTable": flLta41ma_V2StaticMacTable,
       "flLta41ma-V2StaticMacEntry": flLta41ma_V2StaticMacEntry,
       "flLta41ma-V2StaticEntryNumber": flLta41ma_V2StaticEntryNumber,
       "flLta41ma-V2StaticMacAddress": flLta41ma_V2StaticMacAddress,
       "flLta41ma-V2FwdPort1": flLta41ma_V2FwdPort1,
       "flLta41ma-V2FwdPort2": flLta41ma_V2FwdPort2,
       "flLta41ma-V2FwdPort3": flLta41ma_V2FwdPort3,
       "flLta41ma-V2FwdPort4": flLta41ma_V2FwdPort4,
       "flLta41ma-V2FwdPort5": flLta41ma_V2FwdPort5,
       "flLta41ma-V2Fid": flLta41ma_V2Fid,
       "flLta41ma-V2StaticUseFid": flLta41ma_V2StaticUseFid,
       "flLta41ma-V2StaticMacTableStatus": flLta41ma_V2StaticMacTableStatus,
       "flLta41ma-V2Statistics": flLta41ma_V2Statistics,
       "flLta41ma-V2RxErrorPacketsTable": flLta41ma_V2RxErrorPacketsTable,
       "flLta41ma-V2RxErrorPacketsEntry": flLta41ma_V2RxErrorPacketsEntry,
       "flLta41ma-V2RxUndersizePackets": flLta41ma_V2RxUndersizePackets,
       "flLta41ma-V2RxFragmentPackets": flLta41ma_V2RxFragmentPackets,
       "flLta41ma-V2RxOversizePackets": flLta41ma_V2RxOversizePackets,
       "flLta41ma-V2RxCrcErrorPackets": flLta41ma_V2RxCrcErrorPackets,
       "flLta41ma-V2RxAlignmentErrorPackets": flLta41ma_V2RxAlignmentErrorPackets,
       "flLta41ma-V2RxRefreshCounters": flLta41ma_V2RxRefreshCounters,
       "flLta41ma-V2RxClearCounters": flLta41ma_V2RxClearCounters,
       "flLta41ma-V2RxGoodPacketsTable": flLta41ma_V2RxGoodPacketsTable,
       "flLta41ma-V2RxGoodPacketsEntry": flLta41ma_V2RxGoodPacketsEntry,
       "flLta41ma-V2RxUnicastPackets": flLta41ma_V2RxUnicastPackets,
       "flLta41ma-V2RxMulticastPackets": flLta41ma_V2RxMulticastPackets,
       "flLta41ma-V2RxBroadcastPackets": flLta41ma_V2RxBroadcastPackets,
       "flLta41ma-V2RxMacControlPackets": flLta41ma_V2RxMacControlPackets,
       "flLta41ma-V2RxPausePackets": flLta41ma_V2RxPausePackets,
       "flLta41ma-V2RxRefreshGoodCounters": flLta41ma_V2RxRefreshGoodCounters,
       "flLta41ma-V2RxClearGoodCounters": flLta41ma_V2RxClearGoodCounters,
       "flLta41ma-V2TxGoodPacketsTable": flLta41ma_V2TxGoodPacketsTable,
       "flLta41ma-V2TxGoodPacketsEntry": flLta41ma_V2TxGoodPacketsEntry,
       "flLta41ma-V2TxUnicastPackets": flLta41ma_V2TxUnicastPackets,
       "flLta41ma-V2TxMulticastPackets": flLta41ma_V2TxMulticastPackets,
       "flLta41ma-V2TxBroadcastPackets": flLta41ma_V2TxBroadcastPackets,
       "flLta41ma-V2TxPausePackets": flLta41ma_V2TxPausePackets,
       "flLta41ma-V2TxRefreshGoodCounters": flLta41ma_V2TxRefreshGoodCounters,
       "flLta41ma-V2TxClearGoodCounters": flLta41ma_V2TxClearGoodCounters,
       "flLta41ma-V2RxTotalPacketsTable": flLta41ma_V2RxTotalPacketsTable,
       "flLta41ma-V2RxTotalPacketsEntry": flLta41ma_V2RxTotalPacketsEntry,
       "flLta41ma-V2RxDroppedPackets": flLta41ma_V2RxDroppedPackets,
       "flLta41ma-V2Rx64BytesPackets": flLta41ma_V2Rx64BytesPackets,
       "flLta41ma-V2Rx65-127BytesPackets": flLta41ma_V2Rx65_127BytesPackets,
       "flLta41ma-V2Rx128-255BytesPackets": flLta41ma_V2Rx128_255BytesPackets,
       "flLta41ma-V2Rx256-511BytesPackets": flLta41ma_V2Rx256_511BytesPackets,
       "flLta41ma-V2Rx512-1023BytesPackets": flLta41ma_V2Rx512_1023BytesPackets,
       "flLta41ma-V2Rx1024-MaxBytesPackets": flLta41ma_V2Rx1024_MaxBytesPackets,
       "flLta41ma-V2RxRefreshTotalCounters": flLta41ma_V2RxRefreshTotalCounters,
       "flLta41ma-V2RxClearTotalCounters": flLta41ma_V2RxClearTotalCounters,
       "flLta41ma-V2TxTotalPacketsTable": flLta41ma_V2TxTotalPacketsTable,
       "flLta41ma-V2TxTotalPacketsEntry": flLta41ma_V2TxTotalPacketsEntry,
       "flLta41ma-V2TxDroppedPackets": flLta41ma_V2TxDroppedPackets,
       "flLta41ma-V2TxRefreshTotalCounters": flLta41ma_V2TxRefreshTotalCounters,
       "flLta41ma-V2TxClearTotalCounters": flLta41ma_V2TxClearTotalCounters,
       "flLta41ma-V2TxCollisionsTable": flLta41ma_V2TxCollisionsTable,
       "flLta41ma-V2TxCollisionsEntry": flLta41ma_V2TxCollisionsEntry,
       "flLta41ma-V2TxTotalCols": flLta41ma_V2TxTotalCols,
       "flLta41ma-V2TxLateCols": flLta41ma_V2TxLateCols,
       "flLta41ma-V2TxExcessiveCols": flLta41ma_V2TxExcessiveCols,
       "flLta41ma-V2TxSingleCols": flLta41ma_V2TxSingleCols,
       "flLta41ma-V2TxMultipleCols": flLta41ma_V2TxMultipleCols,
       "flLta41ma-V2TxRefreshColCounters": flLta41ma_V2TxRefreshColCounters,
       "flLta41ma-V2TxClearColCounters": flLta41ma_V2TxClearColCounters}
)
