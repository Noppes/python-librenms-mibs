# SNMP MIB module (FIBROLAN-MIB-LTA41xE1-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-LTA41xE1-V2

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

(flLta41ma_V2GlobalConfigEntry,) = mibBuilder.importSymbols(
    "FIBROLAN-MIB-LTA41MA-V2",
    "flLta41ma-V2GlobalConfigEntry")

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

flLta41xE1_V2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100)
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
_FlLta41ma_V2_ObjectIdentity = ObjectIdentity
flLta41ma_V2 = _FlLta41ma_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21)
)
_FlLta41xE1_V2MIBConformance_ObjectIdentity = ObjectIdentity
flLta41xE1_V2MIBConformance = _FlLta41xE1_V2MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 1)
)
_FlLta41xE1_V2MIBCompliances_ObjectIdentity = ObjectIdentity
flLta41xE1_V2MIBCompliances = _FlLta41xE1_V2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 1, 1)
)
_FlLta41xE1_V2MIBGroups_ObjectIdentity = ObjectIdentity
flLta41xE1_V2MIBGroups = _FlLta41xE1_V2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 1, 2)
)
_FlLta41xE1_V2Ports_ObjectIdentity = ObjectIdentity
flLta41xE1_V2Ports = _FlLta41xE1_V2Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10)
)
_FlLta41xE1_V2PortsGeneralTable_Object = MibTable
flLta41xE1_V2PortsGeneralTable = _FlLta41xE1_V2PortsGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 1)
)
if mibBuilder.loadTexts:
    flLta41xE1_V2PortsGeneralTable.setStatus("current")
_FlLta41xE1_V2PortsEntry_Object = MibTableRow
flLta41xE1_V2PortsEntry = _FlLta41xE1_V2PortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 1, 1)
)
if mibBuilder.loadTexts:
    flLta41xE1_V2PortsEntry.setStatus("current")


class _FlLta41xE1_V2ResetPorts_Type(Integer32):
    """Custom type flLta41xE1_V2ResetPorts based on Integer32"""
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


_FlLta41xE1_V2ResetPorts_Type.__name__ = "Integer32"
_FlLta41xE1_V2ResetPorts_Object = MibTableColumn
flLta41xE1_V2ResetPorts = _FlLta41xE1_V2ResetPorts_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 1, 1, 1),
    _FlLta41xE1_V2ResetPorts_Type()
)
flLta41xE1_V2ResetPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41xE1_V2ResetPorts.setStatus("current")


class _FlLta41xE1_V2RestorePortsDef_Type(Integer32):
    """Custom type flLta41xE1_V2RestorePortsDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("restore", 2))
    )


_FlLta41xE1_V2RestorePortsDef_Type.__name__ = "Integer32"
_FlLta41xE1_V2RestorePortsDef_Object = MibTableColumn
flLta41xE1_V2RestorePortsDef = _FlLta41xE1_V2RestorePortsDef_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 1, 1, 2),
    _FlLta41xE1_V2RestorePortsDef_Type()
)
flLta41xE1_V2RestorePortsDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41xE1_V2RestorePortsDef.setStatus("current")
_FlLta41xE1_V2PortsStatusTable_Object = MibTable
flLta41xE1_V2PortsStatusTable = _FlLta41xE1_V2PortsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 2)
)
if mibBuilder.loadTexts:
    flLta41xE1_V2PortsStatusTable.setStatus("current")
_FlLta41xE1_V2PortsStatusEntry_Object = MibTableRow
flLta41xE1_V2PortsStatusEntry = _FlLta41xE1_V2PortsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 2, 1)
)
flLta41xE1_V2PortsStatusEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2PortIndex"),
)
if mibBuilder.loadTexts:
    flLta41xE1_V2PortsStatusEntry.setStatus("current")


class _FlLta41xE1_V2PortIndex_Type(Integer32):
    """Custom type flLta41xE1_V2PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FlLta41xE1_V2PortIndex_Type.__name__ = "Integer32"
_FlLta41xE1_V2PortIndex_Object = MibTableColumn
flLta41xE1_V2PortIndex = _FlLta41xE1_V2PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 2, 1, 1),
    _FlLta41xE1_V2PortIndex_Type()
)
flLta41xE1_V2PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41xE1_V2PortIndex.setStatus("current")


class _FlLta41xE1_V2Signal_Type(Integer32):
    """Custom type flLta41xE1_V2Signal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("los", 1),
          ("on", 2))
    )


_FlLta41xE1_V2Signal_Type.__name__ = "Integer32"
_FlLta41xE1_V2Signal_Object = MibTableColumn
flLta41xE1_V2Signal = _FlLta41xE1_V2Signal_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 2, 1, 2),
    _FlLta41xE1_V2Signal_Type()
)
flLta41xE1_V2Signal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41xE1_V2Signal.setStatus("current")


class _FlLta41xE1_V2RemoteSignal_Type(Integer32):
    """Custom type flLta41xE1_V2RemoteSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("los", 1),
          ("on", 2))
    )


_FlLta41xE1_V2RemoteSignal_Type.__name__ = "Integer32"
_FlLta41xE1_V2RemoteSignal_Object = MibTableColumn
flLta41xE1_V2RemoteSignal = _FlLta41xE1_V2RemoteSignal_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 2, 1, 3),
    _FlLta41xE1_V2RemoteSignal_Type()
)
flLta41xE1_V2RemoteSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41xE1_V2RemoteSignal.setStatus("current")


class _FlLta41xE1_V2Ais_Type(Integer32):
    """Custom type flLta41xE1_V2Ais based on Integer32"""
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


_FlLta41xE1_V2Ais_Type.__name__ = "Integer32"
_FlLta41xE1_V2Ais_Object = MibTableColumn
flLta41xE1_V2Ais = _FlLta41xE1_V2Ais_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 2, 1, 4),
    _FlLta41xE1_V2Ais_Type()
)
flLta41xE1_V2Ais.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flLta41xE1_V2Ais.setStatus("current")


class _FlLta41xE1_V2Output_Type(Integer32):
    """Custom type flLta41xE1_V2Output based on Integer32"""
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


_FlLta41xE1_V2Output_Type.__name__ = "Integer32"
_FlLta41xE1_V2Output_Object = MibTableColumn
flLta41xE1_V2Output = _FlLta41xE1_V2Output_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 2, 1, 5),
    _FlLta41xE1_V2Output_Type()
)
flLta41xE1_V2Output.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41xE1_V2Output.setStatus("current")


class _FlLta41xE1_V2Input_Type(Integer32):
    """Custom type flLta41xE1_V2Input based on Integer32"""
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


_FlLta41xE1_V2Input_Type.__name__ = "Integer32"
_FlLta41xE1_V2Input_Object = MibTableColumn
flLta41xE1_V2Input = _FlLta41xE1_V2Input_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 2, 1, 6),
    _FlLta41xE1_V2Input_Type()
)
flLta41xE1_V2Input.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41xE1_V2Input.setStatus("current")


class _FlLta41xE1_V2Taos_Type(Integer32):
    """Custom type flLta41xE1_V2Taos based on Integer32"""
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


_FlLta41xE1_V2Taos_Type.__name__ = "Integer32"
_FlLta41xE1_V2Taos_Object = MibTableColumn
flLta41xE1_V2Taos = _FlLta41xE1_V2Taos_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 2, 1, 7),
    _FlLta41xE1_V2Taos_Type()
)
flLta41xE1_V2Taos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41xE1_V2Taos.setStatus("current")


class _FlLta41xE1_V2UserLoopback_Type(Integer32):
    """Custom type flLta41xE1_V2UserLoopback based on Integer32"""
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


_FlLta41xE1_V2UserLoopback_Type.__name__ = "Integer32"
_FlLta41xE1_V2UserLoopback_Object = MibTableColumn
flLta41xE1_V2UserLoopback = _FlLta41xE1_V2UserLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 2, 1, 8),
    _FlLta41xE1_V2UserLoopback_Type()
)
flLta41xE1_V2UserLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41xE1_V2UserLoopback.setStatus("current")


class _FlLta41xE1_V2RemoteAnalogLB_Type(Integer32):
    """Custom type flLta41xE1_V2RemoteAnalogLB based on Integer32"""
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


_FlLta41xE1_V2RemoteAnalogLB_Type.__name__ = "Integer32"
_FlLta41xE1_V2RemoteAnalogLB_Object = MibTableColumn
flLta41xE1_V2RemoteAnalogLB = _FlLta41xE1_V2RemoteAnalogLB_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 2, 1, 9),
    _FlLta41xE1_V2RemoteAnalogLB_Type()
)
flLta41xE1_V2RemoteAnalogLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41xE1_V2RemoteAnalogLB.setStatus("current")


class _FlLta41xE1_V2RemoteDigitalLB_Type(Integer32):
    """Custom type flLta41xE1_V2RemoteDigitalLB based on Integer32"""
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


_FlLta41xE1_V2RemoteDigitalLB_Type.__name__ = "Integer32"
_FlLta41xE1_V2RemoteDigitalLB_Object = MibTableColumn
flLta41xE1_V2RemoteDigitalLB = _FlLta41xE1_V2RemoteDigitalLB_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 2, 1, 10),
    _FlLta41xE1_V2RemoteDigitalLB_Type()
)
flLta41xE1_V2RemoteDigitalLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41xE1_V2RemoteDigitalLB.setStatus("current")
_FlLta41xE1_V2PortDescription_Type = DisplayString
_FlLta41xE1_V2PortDescription_Object = MibTableColumn
flLta41xE1_V2PortDescription = _FlLta41xE1_V2PortDescription_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 10, 2, 1, 11),
    _FlLta41xE1_V2PortDescription_Type()
)
flLta41xE1_V2PortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flLta41xE1_V2PortDescription.setStatus("current")
flLta41ma_V2GlobalConfigEntry.registerAugmentions(
    ("FIBROLAN-MIB-LTA41xE1-V2",
     "flLta41xE1-V2PortsEntry")
)
flLta41xE1_V2PortsEntry.setIndexNames(*flLta41ma_V2GlobalConfigEntry.getIndexNames())

# Managed Objects groups

flLta41xE1_V2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 1, 2, 1)
)
flLta41xE1_V2Group.setObjects(
      *(("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2ResetPorts"),
        ("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2RestorePortsDef"))
)
if mibBuilder.loadTexts:
    flLta41xE1_V2Group.setStatus("current")

flLta41xE1_V2PortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 1, 2, 2)
)
flLta41xE1_V2PortsGroup.setObjects(
      *(("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2PortIndex"),
        ("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2Signal"),
        ("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2RemoteSignal"),
        ("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2Ais"),
        ("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2Output"),
        ("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2Input"),
        ("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2Taos"),
        ("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2UserLoopback"),
        ("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2RemoteAnalogLB"),
        ("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2RemoteDigitalLB"),
        ("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2PortDescription"))
)
if mibBuilder.loadTexts:
    flLta41xE1_V2PortsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flLta41xE1_V2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 21, 100, 1, 1, 1)
)
flLta41xE1_V2MIBCompliance.setObjects(
      *(("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2Group"),
        ("FIBROLAN-MIB-LTA41xE1-V2", "flLta41xE1-V2PortsGroup"))
)
if mibBuilder.loadTexts:
    flLta41xE1_V2MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-LTA41xE1-V2",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMaRemoteDevice": flMaRemoteDevice,
       "flLta41ma-V2": flLta41ma_V2,
       "flLta41xE1-V2": flLta41xE1_V2,
       "flLta41xE1-V2MIBConformance": flLta41xE1_V2MIBConformance,
       "flLta41xE1-V2MIBCompliances": flLta41xE1_V2MIBCompliances,
       "flLta41xE1-V2MIBCompliance": flLta41xE1_V2MIBCompliance,
       "flLta41xE1-V2MIBGroups": flLta41xE1_V2MIBGroups,
       "flLta41xE1-V2Group": flLta41xE1_V2Group,
       "flLta41xE1-V2PortsGroup": flLta41xE1_V2PortsGroup,
       "flLta41xE1-V2Ports": flLta41xE1_V2Ports,
       "flLta41xE1-V2PortsGeneralTable": flLta41xE1_V2PortsGeneralTable,
       "flLta41xE1-V2PortsEntry": flLta41xE1_V2PortsEntry,
       "flLta41xE1-V2ResetPorts": flLta41xE1_V2ResetPorts,
       "flLta41xE1-V2RestorePortsDef": flLta41xE1_V2RestorePortsDef,
       "flLta41xE1-V2PortsStatusTable": flLta41xE1_V2PortsStatusTable,
       "flLta41xE1-V2PortsStatusEntry": flLta41xE1_V2PortsStatusEntry,
       "flLta41xE1-V2PortIndex": flLta41xE1_V2PortIndex,
       "flLta41xE1-V2Signal": flLta41xE1_V2Signal,
       "flLta41xE1-V2RemoteSignal": flLta41xE1_V2RemoteSignal,
       "flLta41xE1-V2Ais": flLta41xE1_V2Ais,
       "flLta41xE1-V2Output": flLta41xE1_V2Output,
       "flLta41xE1-V2Input": flLta41xE1_V2Input,
       "flLta41xE1-V2Taos": flLta41xE1_V2Taos,
       "flLta41xE1-V2UserLoopback": flLta41xE1_V2UserLoopback,
       "flLta41xE1-V2RemoteAnalogLB": flLta41xE1_V2RemoteAnalogLB,
       "flLta41xE1-V2RemoteDigitalLB": flLta41xE1_V2RemoteDigitalLB,
       "flLta41xE1-V2PortDescription": flLta41xE1_V2PortDescription}
)
