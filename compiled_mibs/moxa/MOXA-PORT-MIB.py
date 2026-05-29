# SNMP MIB module (MOXA-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\moxa\MOXA-PORT-MIB

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

(portInterface,) = mibBuilder.importSymbols(
    "MOXA-SWITCHING-MIB",
    "portInterface")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mxPort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1)
)
if mibBuilder.loadTexts:
    mxPort.setRevisions(
        ("2022-03-09 00:00",
         "2019-06-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortFuncMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("poe", 0),
          ("ptp", 1))
    )


# MIB Managed Objects in the order of their OIDs

_PortConfiguration_ObjectIdentity = ObjectIdentity
portConfiguration = _PortConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1)
)
_PortConfigTable_Object = MibTable
portConfigTable = _PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    portConfigTable.setStatus("current")
_PortConfigEntry_Object = MibTableRow
portConfigEntry = _PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1, 1, 1)
)
portConfigEntry.setIndexNames(
    (0, "MOXA-PORT-MIB", "portConfigIndex"),
)
if mibBuilder.loadTexts:
    portConfigEntry.setStatus("current")


class _PortConfigIndex_Type(Integer32):
    """Custom type portConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortConfigIndex_Type.__name__ = "Integer32"
_PortConfigIndex_Object = MibTableColumn
portConfigIndex = _PortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1, 1, 1, 1),
    _PortConfigIndex_Type()
)
portConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigIndex.setStatus("current")
_PortConfigDescription_Type = DisplayString
_PortConfigDescription_Object = MibTableColumn
portConfigDescription = _PortConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1, 1, 1, 2),
    _PortConfigDescription_Type()
)
portConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDescription.setStatus("current")


class _PortConfigMode_Type(Integer32):
    """Custom type portConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("noNegotiation", 2))
    )


_PortConfigMode_Type.__name__ = "Integer32"
_PortConfigMode_Object = MibTableColumn
portConfigMode = _PortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1, 1, 1, 3),
    _PortConfigMode_Type()
)
portConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMode.setStatus("current")


class _PortConfigDuplex_Type(Integer32):
    """Custom type portConfigDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_PortConfigDuplex_Type.__name__ = "Integer32"
_PortConfigDuplex_Object = MibTableColumn
portConfigDuplex = _PortConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1, 1, 1, 4),
    _PortConfigDuplex_Type()
)
portConfigDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDuplex.setStatus("current")


class _PortConfigSpeed_Type(Integer32):
    """Custom type portConfigSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("tenMBPS", 1),
          ("hundredMBPS", 2),
          ("oneGB", 3),
          ("tenGB", 4),
          ("fortyGB", 5),
          ("fiftysixGB", 6),
          ("twothousandfivehundredMBPS", 7))
    )


_PortConfigSpeed_Type.__name__ = "Integer32"
_PortConfigSpeed_Object = MibTableColumn
portConfigSpeed = _PortConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1, 1, 1, 5),
    _PortConfigSpeed_Type()
)
portConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigSpeed.setStatus("current")


class _PortConfigMdiOrMdixCap_Type(Integer32):
    """Custom type portConfigMdiOrMdixCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdix", 3))
    )


_PortConfigMdiOrMdixCap_Type.__name__ = "Integer32"
_PortConfigMdiOrMdixCap_Object = MibTableColumn
portConfigMdiOrMdixCap = _PortConfigMdiOrMdixCap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1, 1, 1, 6),
    _PortConfigMdiOrMdixCap_Type()
)
portConfigMdiOrMdixCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMdiOrMdixCap.setStatus("current")
_PortConfigSystemLinkUpDelayEnable_Type = TruthValue
_PortConfigSystemLinkUpDelayEnable_Object = MibScalar
portConfigSystemLinkUpDelayEnable = _PortConfigSystemLinkUpDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1, 2),
    _PortConfigSystemLinkUpDelayEnable_Type()
)
portConfigSystemLinkUpDelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigSystemLinkUpDelayEnable.setStatus("current")
_PortConfigLinkUpDelayTable_Object = MibTable
portConfigLinkUpDelayTable = _PortConfigLinkUpDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    portConfigLinkUpDelayTable.setStatus("current")
_PortConfigLinkUpDelayEntry_Object = MibTableRow
portConfigLinkUpDelayEntry = _PortConfigLinkUpDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1, 3, 1)
)
portConfigLinkUpDelayEntry.setIndexNames(
    (0, "MOXA-PORT-MIB", "portConfigLinkUpDelayIndex"),
)
if mibBuilder.loadTexts:
    portConfigLinkUpDelayEntry.setStatus("current")
_PortConfigLinkUpDelayIndex_Type = Integer32
_PortConfigLinkUpDelayIndex_Object = MibTableColumn
portConfigLinkUpDelayIndex = _PortConfigLinkUpDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1, 3, 1, 1),
    _PortConfigLinkUpDelayIndex_Type()
)
portConfigLinkUpDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigLinkUpDelayIndex.setStatus("current")
_PortConfigLinkUpDelayEnable_Type = TruthValue
_PortConfigLinkUpDelayEnable_Object = MibTableColumn
portConfigLinkUpDelayEnable = _PortConfigLinkUpDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1, 3, 1, 2),
    _PortConfigLinkUpDelayEnable_Type()
)
portConfigLinkUpDelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigLinkUpDelayEnable.setStatus("current")


class _PortConfigLinkUpDelayTimer_Type(Unsigned32):
    """Custom type portConfigLinkUpDelayTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PortConfigLinkUpDelayTimer_Type.__name__ = "Unsigned32"
_PortConfigLinkUpDelayTimer_Object = MibTableColumn
portConfigLinkUpDelayTimer = _PortConfigLinkUpDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 1, 3, 1, 3),
    _PortConfigLinkUpDelayTimer_Type()
)
portConfigLinkUpDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigLinkUpDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    portConfigLinkUpDelayTimer.setUnits("seconds")
_PortStatus_ObjectIdentity = ObjectIdentity
portStatus = _PortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 2)
)
_PortStatTable_Object = MibTable
portStatTable = _PortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    portStatTable.setStatus("current")
_PortStatEntry_Object = MibTableRow
portStatEntry = _PortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 2, 1, 1)
)
portStatEntry.setIndexNames(
    (0, "MOXA-PORT-MIB", "portStatIndex"),
)
if mibBuilder.loadTexts:
    portStatEntry.setStatus("current")


class _PortStatIndex_Type(Integer32):
    """Custom type portStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortStatIndex_Type.__name__ = "Integer32"
_PortStatIndex_Object = MibTableColumn
portStatIndex = _PortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 2, 1, 1, 1),
    _PortStatIndex_Type()
)
portStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatIndex.setStatus("current")
_PortStatMediaType_Type = DisplayString
_PortStatMediaType_Object = MibTableColumn
portStatMediaType = _PortStatMediaType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 2, 1, 1, 2),
    _PortStatMediaType_Type()
)
portStatMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatMediaType.setStatus("current")


class _PortStatState_Type(Integer32):
    """Custom type portStatState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6))
    )


_PortStatState_Type.__name__ = "Integer32"
_PortStatState_Object = MibTableColumn
portStatState = _PortStatState_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 2, 1, 1, 3),
    _PortStatState_Type()
)
portStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatState.setStatus("current")


class _PortStatMdiOrMdixCap_Type(Integer32):
    """Custom type portStatMdiOrMdixCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 1),
          ("mdix", 2),
          ("invalid", 3))
    )


_PortStatMdiOrMdixCap_Type.__name__ = "Integer32"
_PortStatMdiOrMdixCap_Object = MibTableColumn
portStatMdiOrMdixCap = _PortStatMdiOrMdixCap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 2, 1, 1, 4),
    _PortStatMdiOrMdixCap_Type()
)
portStatMdiOrMdixCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatMdiOrMdixCap.setStatus("current")
_PortStatFunction_Type = PortFuncMap
_PortStatFunction_Object = MibTableColumn
portStatFunction = _PortStatFunction_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 2, 1, 1, 5),
    _PortStatFunction_Type()
)
portStatFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatFunction.setStatus("current")
_PortStatLinkUpDelayTable_Object = MibTable
portStatLinkUpDelayTable = _PortStatLinkUpDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    portStatLinkUpDelayTable.setStatus("current")
_PortStatLinkUpDelayEntry_Object = MibTableRow
portStatLinkUpDelayEntry = _PortStatLinkUpDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 2, 2, 1)
)
portStatLinkUpDelayEntry.setIndexNames(
    (0, "MOXA-PORT-MIB", "portStatLinkUpDelayIndex"),
)
if mibBuilder.loadTexts:
    portStatLinkUpDelayEntry.setStatus("current")
_PortStatLinkUpDelayIndex_Type = Integer32
_PortStatLinkUpDelayIndex_Object = MibTableColumn
portStatLinkUpDelayIndex = _PortStatLinkUpDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 2, 2, 1, 1),
    _PortStatLinkUpDelayIndex_Type()
)
portStatLinkUpDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatLinkUpDelayIndex.setStatus("current")
_PortStatLinkUpDelayRemainingTime_Type = Unsigned32
_PortStatLinkUpDelayRemainingTime_Object = MibTableColumn
portStatLinkUpDelayRemainingTime = _PortStatLinkUpDelayRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 1, 1, 2, 2, 1, 2),
    _PortStatLinkUpDelayRemainingTime_Type()
)
portStatLinkUpDelayRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatLinkUpDelayRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    portStatLinkUpDelayRemainingTime.setUnits("seconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-PORT-MIB",
    **{"PortFuncMap": PortFuncMap,
       "mxPort": mxPort,
       "portConfiguration": portConfiguration,
       "portConfigTable": portConfigTable,
       "portConfigEntry": portConfigEntry,
       "portConfigIndex": portConfigIndex,
       "portConfigDescription": portConfigDescription,
       "portConfigMode": portConfigMode,
       "portConfigDuplex": portConfigDuplex,
       "portConfigSpeed": portConfigSpeed,
       "portConfigMdiOrMdixCap": portConfigMdiOrMdixCap,
       "portConfigSystemLinkUpDelayEnable": portConfigSystemLinkUpDelayEnable,
       "portConfigLinkUpDelayTable": portConfigLinkUpDelayTable,
       "portConfigLinkUpDelayEntry": portConfigLinkUpDelayEntry,
       "portConfigLinkUpDelayIndex": portConfigLinkUpDelayIndex,
       "portConfigLinkUpDelayEnable": portConfigLinkUpDelayEnable,
       "portConfigLinkUpDelayTimer": portConfigLinkUpDelayTimer,
       "portStatus": portStatus,
       "portStatTable": portStatTable,
       "portStatEntry": portStatEntry,
       "portStatIndex": portStatIndex,
       "portStatMediaType": portStatMediaType,
       "portStatState": portStatState,
       "portStatMdiOrMdixCap": portStatMdiOrMdixCap,
       "portStatFunction": portStatFunction,
       "portStatLinkUpDelayTable": portStatLinkUpDelayTable,
       "portStatLinkUpDelayEntry": portStatLinkUpDelayEntry,
       "portStatLinkUpDelayIndex": portStatLinkUpDelayIndex,
       "portStatLinkUpDelayRemainingTime": portStatLinkUpDelayRemainingTime}
)
