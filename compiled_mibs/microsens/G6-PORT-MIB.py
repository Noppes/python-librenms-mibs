# SNMP MIB module (G6-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\microsens\G6-PORT-MIB

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

_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81)
)
_ConfigTable_Object = MibTable
configTable = _ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1)
)
if mibBuilder.loadTexts:
    configTable.setStatus("current")
_ConfigEntry_Object = MibTableRow
configEntry = _ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1)
)
configEntry.setIndexNames(
    (0, "G6-PORT-MIB", "configPortIndex"),
)
if mibBuilder.loadTexts:
    configEntry.setStatus("current")


class _ConfigPortIndex_Type(Integer32):
    """Custom type configPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_ConfigPortIndex_Type.__name__ = "Integer32"
_ConfigPortIndex_Object = MibTableColumn
configPortIndex = _ConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1, 1),
    _ConfigPortIndex_Type()
)
configPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configPortIndex.setStatus("current")
_ConfigAlias_Type = DisplayString
_ConfigAlias_Object = MibTableColumn
configAlias = _ConfigAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1, 2),
    _ConfigAlias_Type()
)
configAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAlias.setStatus("current")


class _ConfigPortOperation_Type(Integer32):
    """Custom type configPortOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigPortOperation_Type.__name__ = "Integer32"
_ConfigPortOperation_Object = MibTableColumn
configPortOperation = _ConfigPortOperation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1, 3),
    _ConfigPortOperation_Type()
)
configPortOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortOperation.setStatus("current")


class _ConfigRole_Type(Integer32):
    """Custom type configRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("local", 1),
          ("uplink", 2),
          ("downlink", 3))
    )


_ConfigRole_Type.__name__ = "Integer32"
_ConfigRole_Object = MibTableColumn
configRole = _ConfigRole_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1, 4),
    _ConfigRole_Type()
)
configRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRole.setStatus("current")


class _ConfigSpeed_Type(Integer32):
    """Custom type configSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ms10Mbit", 0),
          ("ms100Mbit", 1),
          ("ms1000Mbit", 2),
          ("sfpAuto", 3))
    )


_ConfigSpeed_Type.__name__ = "Integer32"
_ConfigSpeed_Object = MibTableColumn
configSpeed = _ConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1, 5),
    _ConfigSpeed_Type()
)
configSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSpeed.setStatus("current")


class _ConfigMtu_Type(Integer32):
    """Custom type configMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ms1522Byte", 0),
          ("ms2048Byte", 1),
          ("ms10240Byte", 2))
    )


_ConfigMtu_Type.__name__ = "Integer32"
_ConfigMtu_Object = MibTableColumn
configMtu = _ConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1, 6),
    _ConfigMtu_Type()
)
configMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMtu.setStatus("current")


class _ConfigLoopProtection_Type(Integer32):
    """Custom type configLoopProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigLoopProtection_Type.__name__ = "Integer32"
_ConfigLoopProtection_Object = MibTableColumn
configLoopProtection = _ConfigLoopProtection_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1, 7),
    _ConfigLoopProtection_Type()
)
configLoopProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configLoopProtection.setStatus("current")


class _ConfigAutoNegotiation_Type(Integer32):
    """Custom type configAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigAutoNegotiation_Type.__name__ = "Integer32"
_ConfigAutoNegotiation_Object = MibTableColumn
configAutoNegotiation = _ConfigAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1, 8),
    _ConfigAutoNegotiation_Type()
)
configAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAutoNegotiation.setStatus("current")


class _ConfigFullDuplex_Type(Integer32):
    """Custom type configFullDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigFullDuplex_Type.__name__ = "Integer32"
_ConfigFullDuplex_Object = MibTableColumn
configFullDuplex = _ConfigFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1, 9),
    _ConfigFullDuplex_Type()
)
configFullDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFullDuplex.setStatus("current")


class _ConfigFlowcontrol_Type(Integer32):
    """Custom type configFlowcontrol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigFlowcontrol_Type.__name__ = "Integer32"
_ConfigFlowcontrol_Object = MibTableColumn
configFlowcontrol = _ConfigFlowcontrol_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1, 10),
    _ConfigFlowcontrol_Type()
)
configFlowcontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFlowcontrol.setStatus("current")


class _ConfigMdiMode_Type(Integer32):
    """Custom type configMdiMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("forceMdiStd", 1),
          ("forceMdix", 2))
    )


_ConfigMdiMode_Type.__name__ = "Integer32"
_ConfigMdiMode_Object = MibTableColumn
configMdiMode = _ConfigMdiMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1, 11),
    _ConfigMdiMode_Type()
)
configMdiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMdiMode.setStatus("current")


class _ConfigEnergyEfficiency_Type(Integer32):
    """Custom type configEnergyEfficiency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigEnergyEfficiency_Type.__name__ = "Integer32"
_ConfigEnergyEfficiency_Object = MibTableColumn
configEnergyEfficiency = _ConfigEnergyEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1, 12),
    _ConfigEnergyEfficiency_Type()
)
configEnergyEfficiency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEnergyEfficiency.setStatus("current")


class _ConfigDualMediaMode_Type(Integer32):
    """Custom type configDualMediaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiberPriority", 0),
          ("copperPriority", 1),
          ("forceFiber", 2),
          ("forceCopper", 3))
    )


_ConfigDualMediaMode_Type.__name__ = "Integer32"
_ConfigDualMediaMode_Object = MibTableColumn
configDualMediaMode = _ConfigDualMediaMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1, 13),
    _ConfigDualMediaMode_Type()
)
configDualMediaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDualMediaMode.setStatus("current")


class _ConfigAllowedOutgoingPorts_Type(OctetString):
    """Custom type configAllowedOutgoingPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ConfigAllowedOutgoingPorts_Type.__name__ = "OctetString"
_ConfigAllowedOutgoingPorts_Object = MibTableColumn
configAllowedOutgoingPorts = _ConfigAllowedOutgoingPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 1, 1, 14),
    _ConfigAllowedOutgoingPorts_Type()
)
configAllowedOutgoingPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAllowedOutgoingPorts.setStatus("current")
_MonitorTable_Object = MibTable
monitorTable = _MonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 2)
)
if mibBuilder.loadTexts:
    monitorTable.setStatus("current")
_MonitorEntry_Object = MibTableRow
monitorEntry = _MonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 2, 1)
)
monitorEntry.setIndexNames(
    (0, "G6-PORT-MIB", "monitorIndex"),
)
if mibBuilder.loadTexts:
    monitorEntry.setStatus("current")


class _MonitorIndex_Type(Integer32):
    """Custom type monitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_MonitorIndex_Type.__name__ = "Integer32"
_MonitorIndex_Object = MibTableColumn
monitorIndex = _MonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 2, 1, 1),
    _MonitorIndex_Type()
)
monitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    monitorIndex.setStatus("current")


class _MonitorMode_Type(Integer32):
    """Custom type monitorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("txOnly", 1),
          ("rxOnly", 2),
          ("rxAndTx", 3))
    )


_MonitorMode_Type.__name__ = "Integer32"
_MonitorMode_Object = MibTableColumn
monitorMode = _MonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 2, 1, 2),
    _MonitorMode_Type()
)
monitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorMode.setStatus("current")


class _MonitorSource_Type(OctetString):
    """Custom type monitorSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_MonitorSource_Type.__name__ = "OctetString"
_MonitorSource_Object = MibTableColumn
monitorSource = _MonitorSource_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 2, 1, 3),
    _MonitorSource_Type()
)
monitorSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorSource.setStatus("current")


class _MonitorDestination_Type(Integer32):
    """Custom type monitorDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MonitorDestination_Type.__name__ = "Integer32"
_MonitorDestination_Object = MibTableColumn
monitorDestination = _MonitorDestination_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 2, 1, 4),
    _MonitorDestination_Type()
)
monitorDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorDestination.setStatus("current")
_PortRestartPort_Type = DisplayString
_PortRestartPort_Object = MibScalar
portRestartPort = _PortRestartPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 3),
    _PortRestartPort_Type()
)
portRestartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portRestartPort.setStatus("current")


class _PortUplinkPorts_Type(OctetString):
    """Custom type portUplinkPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_PortUplinkPorts_Type.__name__ = "OctetString"
_PortUplinkPorts_Object = MibScalar
portUplinkPorts = _PortUplinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 100),
    _PortUplinkPorts_Type()
)
portUplinkPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portUplinkPorts.setStatus("current")


class _PortDownlinkPorts_Type(OctetString):
    """Custom type portDownlinkPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_PortDownlinkPorts_Type.__name__ = "OctetString"
_PortDownlinkPorts_Object = MibScalar
portDownlinkPorts = _PortDownlinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 101),
    _PortDownlinkPorts_Type()
)
portDownlinkPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDownlinkPorts.setStatus("current")
_StatusTable_Object = MibTable
statusTable = _StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102)
)
if mibBuilder.loadTexts:
    statusTable.setStatus("current")
_StatusEntry_Object = MibTableRow
statusEntry = _StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1)
)
statusEntry.setIndexNames(
    (0, "G6-PORT-MIB", "statusPortIndex"),
)
if mibBuilder.loadTexts:
    statusEntry.setStatus("current")


class _StatusPortIndex_Type(Integer32):
    """Custom type statusPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_StatusPortIndex_Type.__name__ = "Integer32"
_StatusPortIndex_Object = MibTableColumn
statusPortIndex = _StatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 1),
    _StatusPortIndex_Type()
)
statusPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    statusPortIndex.setStatus("current")


class _StatusLinkUp_Type(Integer32):
    """Custom type statusLinkUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_StatusLinkUp_Type.__name__ = "Integer32"
_StatusLinkUp_Object = MibTableColumn
statusLinkUp = _StatusLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 2),
    _StatusLinkUp_Type()
)
statusLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusLinkUp.setStatus("current")
_StatusLastLinkChange_Type = DisplayString
_StatusLastLinkChange_Object = MibTableColumn
statusLastLinkChange = _StatusLastLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 3),
    _StatusLastLinkChange_Type()
)
statusLastLinkChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusLastLinkChange.setStatus("current")


class _StatusLinkState_Type(Integer32):
    """Custom type statusLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 0),
          ("blocking", 1),
          ("learning", 2),
          ("forwarding", 3),
          ("unauthVlan", 4))
    )


_StatusLinkState_Type.__name__ = "Integer32"
_StatusLinkState_Object = MibTableColumn
statusLinkState = _StatusLinkState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 4),
    _StatusLinkState_Type()
)
statusLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusLinkState.setStatus("current")


class _StatusRxActivity_Type(Integer32):
    """Custom type statusRxActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_StatusRxActivity_Type.__name__ = "Integer32"
_StatusRxActivity_Object = MibTableColumn
statusRxActivity = _StatusRxActivity_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 5),
    _StatusRxActivity_Type()
)
statusRxActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRxActivity.setStatus("current")


class _StatusTxActivity_Type(Integer32):
    """Custom type statusTxActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_StatusTxActivity_Type.__name__ = "Integer32"
_StatusTxActivity_Object = MibTableColumn
statusTxActivity = _StatusTxActivity_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 6),
    _StatusTxActivity_Type()
)
statusTxActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusTxActivity.setStatus("current")


class _StatusMediaUsed_Type(Integer32):
    """Custom type statusMediaUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("copper", 1),
          ("fiber", 2))
    )


_StatusMediaUsed_Type.__name__ = "Integer32"
_StatusMediaUsed_Object = MibTableColumn
statusMediaUsed = _StatusMediaUsed_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 7),
    _StatusMediaUsed_Type()
)
statusMediaUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMediaUsed.setStatus("current")


class _StatusSpeedUsed_Type(Integer32):
    """Custom type statusSpeedUsed based on Integer32"""
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
        *(("down", 0),
          ("ms10Mbit", 1),
          ("ms100Mbit", 2),
          ("ms1000Mbit", 3),
          ("ms2500Mbit", 4),
          ("ms5Gbit", 5),
          ("ms10Gbit", 6))
    )


_StatusSpeedUsed_Type.__name__ = "Integer32"
_StatusSpeedUsed_Object = MibTableColumn
statusSpeedUsed = _StatusSpeedUsed_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 8),
    _StatusSpeedUsed_Type()
)
statusSpeedUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSpeedUsed.setStatus("current")


class _StatusLoopedPort_Type(OctetString):
    """Custom type statusLoopedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_StatusLoopedPort_Type.__name__ = "OctetString"
_StatusLoopedPort_Object = MibTableColumn
statusLoopedPort = _StatusLoopedPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 9),
    _StatusLoopedPort_Type()
)
statusLoopedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusLoopedPort.setStatus("current")


class _StatusFullDuplexUsed_Type(Integer32):
    """Custom type statusFullDuplexUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("full", 1),
          ("half", 2))
    )


_StatusFullDuplexUsed_Type.__name__ = "Integer32"
_StatusFullDuplexUsed_Object = MibTableColumn
statusFullDuplexUsed = _StatusFullDuplexUsed_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 10),
    _StatusFullDuplexUsed_Type()
)
statusFullDuplexUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFullDuplexUsed.setStatus("current")


class _StatusFlowcontrolUsed_Type(Integer32):
    """Custom type statusFlowcontrolUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_StatusFlowcontrolUsed_Type.__name__ = "Integer32"
_StatusFlowcontrolUsed_Object = MibTableColumn
statusFlowcontrolUsed = _StatusFlowcontrolUsed_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 11),
    _StatusFlowcontrolUsed_Type()
)
statusFlowcontrolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFlowcontrolUsed.setStatus("current")


class _StatusMdiUsed_Type(Integer32):
    """Custom type statusMdiUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_StatusMdiUsed_Type.__name__ = "Integer32"
_StatusMdiUsed_Object = MibTableColumn
statusMdiUsed = _StatusMdiUsed_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 12),
    _StatusMdiUsed_Type()
)
statusMdiUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMdiUsed.setStatus("current")


class _StatusEeeActive_Type(Integer32):
    """Custom type statusEeeActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_StatusEeeActive_Type.__name__ = "Integer32"
_StatusEeeActive_Object = MibTableColumn
statusEeeActive = _StatusEeeActive_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 13),
    _StatusEeeActive_Type()
)
statusEeeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEeeActive.setStatus("current")


class _StatusBlockingAlgorithm_Type(Bits):
    """Custom type statusBlockingAlgorithm based on Bits"""
    namedValues = NamedValues(
        *(("portIsEnabled", 0),
          ("ms8021xApplies", 1),
          ("rstpApplies", 2),
          ("ringApplies", 3),
          ("couplingApplies", 4),
          ("loopPreventionApplies", 5),
          ("macAuthApplies", 6),
          ("bpduGuardApplies", 7),
          ("dhcpFilterApplies", 8))
    )

_StatusBlockingAlgorithm_Type.__name__ = "Bits"
_StatusBlockingAlgorithm_Object = MibTableColumn
statusBlockingAlgorithm = _StatusBlockingAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 14),
    _StatusBlockingAlgorithm_Type()
)
statusBlockingAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusBlockingAlgorithm.setStatus("current")


class _StatusLearningAlgorithm_Type(Bits):
    """Custom type statusLearningAlgorithm based on Bits"""
    namedValues = NamedValues(
        *(("portIsEnabled", 0),
          ("ms8021xApplies", 1),
          ("rstpApplies", 2),
          ("ringApplies", 3),
          ("couplingApplies", 4),
          ("loopPreventionApplies", 5),
          ("macAuthApplies", 6),
          ("bpduGuardApplies", 7),
          ("dhcpFilterApplies", 8))
    )

_StatusLearningAlgorithm_Type.__name__ = "Bits"
_StatusLearningAlgorithm_Object = MibTableColumn
statusLearningAlgorithm = _StatusLearningAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 15),
    _StatusLearningAlgorithm_Type()
)
statusLearningAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusLearningAlgorithm.setStatus("current")


class _StatusForwardingAlgorithm_Type(Bits):
    """Custom type statusForwardingAlgorithm based on Bits"""
    namedValues = NamedValues(
        *(("portIsEnabled", 0),
          ("ms8021xApplies", 1),
          ("rstpApplies", 2),
          ("ringApplies", 3),
          ("couplingApplies", 4),
          ("loopPreventionApplies", 5),
          ("macAuthApplies", 6),
          ("bpduGuardApplies", 7),
          ("dhcpFilterApplies", 8))
    )

_StatusForwardingAlgorithm_Type.__name__ = "Bits"
_StatusForwardingAlgorithm_Object = MibTableColumn
statusForwardingAlgorithm = _StatusForwardingAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 16),
    _StatusForwardingAlgorithm_Type()
)
statusForwardingAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusForwardingAlgorithm.setStatus("current")


class _StatusUnauthorizedAlgorithm_Type(Bits):
    """Custom type statusUnauthorizedAlgorithm based on Bits"""
    namedValues = NamedValues(
        *(("portIsEnabled", 0),
          ("ms8021xApplies", 1),
          ("rstpApplies", 2),
          ("ringApplies", 3),
          ("couplingApplies", 4),
          ("loopPreventionApplies", 5),
          ("macAuthApplies", 6),
          ("bpduGuardApplies", 7),
          ("dhcpFilterApplies", 8))
    )

_StatusUnauthorizedAlgorithm_Type.__name__ = "Bits"
_StatusUnauthorizedAlgorithm_Object = MibTableColumn
statusUnauthorizedAlgorithm = _StatusUnauthorizedAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 81, 102, 1, 17),
    _StatusUnauthorizedAlgorithm_Type()
)
statusUnauthorizedAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusUnauthorizedAlgorithm.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-PORT-MIB",
    **{"device": device,
       "port": port,
       "configTable": configTable,
       "configEntry": configEntry,
       "configPortIndex": configPortIndex,
       "configAlias": configAlias,
       "configPortOperation": configPortOperation,
       "configRole": configRole,
       "configSpeed": configSpeed,
       "configMtu": configMtu,
       "configLoopProtection": configLoopProtection,
       "configAutoNegotiation": configAutoNegotiation,
       "configFullDuplex": configFullDuplex,
       "configFlowcontrol": configFlowcontrol,
       "configMdiMode": configMdiMode,
       "configEnergyEfficiency": configEnergyEfficiency,
       "configDualMediaMode": configDualMediaMode,
       "configAllowedOutgoingPorts": configAllowedOutgoingPorts,
       "monitorTable": monitorTable,
       "monitorEntry": monitorEntry,
       "monitorIndex": monitorIndex,
       "monitorMode": monitorMode,
       "monitorSource": monitorSource,
       "monitorDestination": monitorDestination,
       "portRestartPort": portRestartPort,
       "portUplinkPorts": portUplinkPorts,
       "portDownlinkPorts": portDownlinkPorts,
       "statusTable": statusTable,
       "statusEntry": statusEntry,
       "statusPortIndex": statusPortIndex,
       "statusLinkUp": statusLinkUp,
       "statusLastLinkChange": statusLastLinkChange,
       "statusLinkState": statusLinkState,
       "statusRxActivity": statusRxActivity,
       "statusTxActivity": statusTxActivity,
       "statusMediaUsed": statusMediaUsed,
       "statusSpeedUsed": statusSpeedUsed,
       "statusLoopedPort": statusLoopedPort,
       "statusFullDuplexUsed": statusFullDuplexUsed,
       "statusFlowcontrolUsed": statusFlowcontrolUsed,
       "statusMdiUsed": statusMdiUsed,
       "statusEeeActive": statusEeeActive,
       "statusBlockingAlgorithm": statusBlockingAlgorithm,
       "statusLearningAlgorithm": statusLearningAlgorithm,
       "statusForwardingAlgorithm": statusForwardingAlgorithm,
       "statusUnauthorizedAlgorithm": statusUnauthorizedAlgorithm}
)
