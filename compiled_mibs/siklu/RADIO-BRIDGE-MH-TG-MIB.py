# SNMP MIB module (RADIO-BRIDGE-MH-TG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siklu\mhtg\RADIO-BRIDGE-MH-TG-MIB

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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(radioBridgeRoot,) = mibBuilder.importSymbols(
    "RADIO-BRIDGE-MIB",
    "radioBridgeRoot")

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

rbTgMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 35)
)
if mibBuilder.loadTexts:
    rbTgMIB.setRevisions(
        ("2023-02-15 14:05",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RbTgAdminStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asUp", 1),
          ("asDown", 2))
    )



class RbTgRadioNodeAssignedName(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )



class RbTgRadioSectorIndex(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class RbTgRadioNodeLocalRole(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rnlrInitiator", 1),
          ("rnlrResponder", 2))
    )



class RbTgRadioMcs(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )



class RbTgRadioTxPowerIndex(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 31),
    )



class RbTgRadioRfLinkSpeed(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3800),
    )



class RbTgRadioBeamIndex(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 119),
    )



class RbTgRadioBeamAngle(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-180, 180),
    )



class RbTgRadioActiveTilesCount(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class RbTgRadioGolayIndex(TextualConvention, Integer32):
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
        *(("rgiUnspecified", 0),
          ("rgiVal1", 1),
          ("rgiVal2", 2))
    )



class RbTgRadioDnResponderNodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rdrntDn", 1),
          ("rdrntCn", 2))
    )



class RbTgRadioDnControlSuperframe(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("rdcs0", 0),
          ("rdcs1", 1),
          ("rdcsUnspecified", 10))
    )



class RbTgRadioDnSectorBitmap(TextualConvention, Gauge32):
    status = "current"
    displayHint = "b"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )



class RbTgRadioDnLinkState(TextualConvention, Integer32):
    status = "current"
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
        *(("rdlsConnected", 1),
          ("rdlsLinkAdminDown", 2),
          ("rdlsSectorAdminDown", 3),
          ("rdlsWaitingUpstreamConnection", 4),
          ("rdlsWaitingInQueue", 5),
          ("rdlsWaitingPolarityPeriod", 6),
          ("rdlsIgnition", 7))
    )



# MIB Managed Objects in the order of their OIDs

_RbTgMIBObjects_ObjectIdentity = ObjectIdentity
rbTgMIBObjects = _RbTgMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1)
)
_RbTgRadioCommon_ObjectIdentity = ObjectIdentity
rbTgRadioCommon = _RbTgRadioCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1)
)
_RbTgRcNodeConfig_ObjectIdentity = ObjectIdentity
rbTgRcNodeConfig = _RbTgRcNodeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 1)
)
_RbTgRcSectorsConfig_ObjectIdentity = ObjectIdentity
rbTgRcSectorsConfig = _RbTgRcSectorsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 2)
)
_RbTgRcLinks_ObjectIdentity = ObjectIdentity
rbTgRcLinks = _RbTgRcLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3)
)
_RbTgRcLinksActiveTable_Object = MibTable
rbTgRcLinksActiveTable = _RbTgRcLinksActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rbTgRcLinksActiveTable.setStatus("current")
_RbTgRcLinksActiveEntry_Object = MibTableRow
rbTgRcLinksActiveEntry = _RbTgRcLinksActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1)
)
rbTgRcLinksActiveEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveIfIndex"),
)
if mibBuilder.loadTexts:
    rbTgRcLinksActiveEntry.setStatus("current")
_RbTgRcLinksActiveIfIndex_Type = InterfaceIndex
_RbTgRcLinksActiveIfIndex_Object = MibTableColumn
rbTgRcLinksActiveIfIndex = _RbTgRcLinksActiveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 1),
    _RbTgRcLinksActiveIfIndex_Type()
)
rbTgRcLinksActiveIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveIfIndex.setStatus("current")
_RbTgRcLinksActiveRemoteName_Type = RbTgRadioNodeAssignedName
_RbTgRcLinksActiveRemoteName_Object = MibTableColumn
rbTgRcLinksActiveRemoteName = _RbTgRcLinksActiveRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 2),
    _RbTgRcLinksActiveRemoteName_Type()
)
rbTgRcLinksActiveRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveRemoteName.setStatus("current")
_RbTgRcLinksActiveActualRemoteSector_Type = RbTgRadioSectorIndex
_RbTgRcLinksActiveActualRemoteSector_Object = MibTableColumn
rbTgRcLinksActiveActualRemoteSector = _RbTgRcLinksActiveActualRemoteSector_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 3),
    _RbTgRcLinksActiveActualRemoteSector_Type()
)
rbTgRcLinksActiveActualRemoteSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveActualRemoteSector.setStatus("current")
_RbTgRcLinksActiveActualLocalSector_Type = RbTgRadioSectorIndex
_RbTgRcLinksActiveActualLocalSector_Object = MibTableColumn
rbTgRcLinksActiveActualLocalSector = _RbTgRcLinksActiveActualLocalSector_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 4),
    _RbTgRcLinksActiveActualLocalSector_Type()
)
rbTgRcLinksActiveActualLocalSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveActualLocalSector.setStatus("current")
_RbTgRcLinksActiveLocalRole_Type = RbTgRadioNodeLocalRole
_RbTgRcLinksActiveLocalRole_Object = MibTableColumn
rbTgRcLinksActiveLocalRole = _RbTgRcLinksActiveLocalRole_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 5),
    _RbTgRcLinksActiveLocalRole_Type()
)
rbTgRcLinksActiveLocalRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveLocalRole.setStatus("current")
_RbTgRcLinksActiveLinkUptime_Type = TimeTicks
_RbTgRcLinksActiveLinkUptime_Object = MibTableColumn
rbTgRcLinksActiveLinkUptime = _RbTgRcLinksActiveLinkUptime_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 6),
    _RbTgRcLinksActiveLinkUptime_Type()
)
rbTgRcLinksActiveLinkUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveLinkUptime.setStatus("current")


class _RbTgRcLinksActiveRssi_Type(Integer32):
    """Custom type rbTgRcLinksActiveRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 0),
    )


_RbTgRcLinksActiveRssi_Type.__name__ = "Integer32"
_RbTgRcLinksActiveRssi_Object = MibTableColumn
rbTgRcLinksActiveRssi = _RbTgRcLinksActiveRssi_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 7),
    _RbTgRcLinksActiveRssi_Type()
)
rbTgRcLinksActiveRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveRssi.setStatus("current")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveRssi.setUnits("dBm")
_RbTgRcLinksActiveSnr_Type = DisplayString
_RbTgRcLinksActiveSnr_Object = MibTableColumn
rbTgRcLinksActiveSnr = _RbTgRcLinksActiveSnr_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 8),
    _RbTgRcLinksActiveSnr_Type()
)
rbTgRcLinksActiveSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveSnr.setStatus("current")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveSnr.setUnits("dB")
_RbTgRcLinksActiveMcsRx_Type = RbTgRadioMcs
_RbTgRcLinksActiveMcsRx_Object = MibTableColumn
rbTgRcLinksActiveMcsRx = _RbTgRcLinksActiveMcsRx_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 9),
    _RbTgRcLinksActiveMcsRx_Type()
)
rbTgRcLinksActiveMcsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveMcsRx.setStatus("current")
_RbTgRcLinksActiveMcsTx_Type = RbTgRadioMcs
_RbTgRcLinksActiveMcsTx_Object = MibTableColumn
rbTgRcLinksActiveMcsTx = _RbTgRcLinksActiveMcsTx_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 10),
    _RbTgRcLinksActiveMcsTx_Type()
)
rbTgRcLinksActiveMcsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveMcsTx.setStatus("current")
_RbTgRcLinksActiveRxPer_Type = DisplayString
_RbTgRcLinksActiveRxPer_Object = MibTableColumn
rbTgRcLinksActiveRxPer = _RbTgRcLinksActiveRxPer_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 11),
    _RbTgRcLinksActiveRxPer_Type()
)
rbTgRcLinksActiveRxPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveRxPer.setStatus("current")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveRxPer.setUnits("Percentage")
_RbTgRcLinksActiveTxPer_Type = DisplayString
_RbTgRcLinksActiveTxPer_Object = MibTableColumn
rbTgRcLinksActiveTxPer = _RbTgRcLinksActiveTxPer_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 12),
    _RbTgRcLinksActiveTxPer_Type()
)
rbTgRcLinksActiveTxPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveTxPer.setStatus("current")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveTxPer.setUnits("Percentage")
_RbTgRcLinksActiveTxPowerIndex_Type = RbTgRadioTxPowerIndex
_RbTgRcLinksActiveTxPowerIndex_Object = MibTableColumn
rbTgRcLinksActiveTxPowerIndex = _RbTgRcLinksActiveTxPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 13),
    _RbTgRcLinksActiveTxPowerIndex_Type()
)
rbTgRcLinksActiveTxPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveTxPowerIndex.setStatus("current")
_RbTgRcLinksActiveSpeedRx_Type = RbTgRadioRfLinkSpeed
_RbTgRcLinksActiveSpeedRx_Object = MibTableColumn
rbTgRcLinksActiveSpeedRx = _RbTgRcLinksActiveSpeedRx_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 14),
    _RbTgRcLinksActiveSpeedRx_Type()
)
rbTgRcLinksActiveSpeedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveSpeedRx.setStatus("current")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveSpeedRx.setUnits("Mbps")
_RbTgRcLinksActiveSpeedTx_Type = RbTgRadioRfLinkSpeed
_RbTgRcLinksActiveSpeedTx_Object = MibTableColumn
rbTgRcLinksActiveSpeedTx = _RbTgRcLinksActiveSpeedTx_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 15),
    _RbTgRcLinksActiveSpeedTx_Type()
)
rbTgRcLinksActiveSpeedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveSpeedTx.setStatus("current")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveSpeedTx.setUnits("Mbps")
_RbTgRcLinksActiveBeamIndexRx_Type = RbTgRadioBeamIndex
_RbTgRcLinksActiveBeamIndexRx_Object = MibTableColumn
rbTgRcLinksActiveBeamIndexRx = _RbTgRcLinksActiveBeamIndexRx_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 16),
    _RbTgRcLinksActiveBeamIndexRx_Type()
)
rbTgRcLinksActiveBeamIndexRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveBeamIndexRx.setStatus("current")
_RbTgRcLinksActiveBeamAzimuthRx_Type = RbTgRadioBeamAngle
_RbTgRcLinksActiveBeamAzimuthRx_Object = MibTableColumn
rbTgRcLinksActiveBeamAzimuthRx = _RbTgRcLinksActiveBeamAzimuthRx_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 17),
    _RbTgRcLinksActiveBeamAzimuthRx_Type()
)
rbTgRcLinksActiveBeamAzimuthRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveBeamAzimuthRx.setStatus("current")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveBeamAzimuthRx.setUnits("Degrees")
_RbTgRcLinksActiveBeamElevationRx_Type = RbTgRadioBeamAngle
_RbTgRcLinksActiveBeamElevationRx_Object = MibTableColumn
rbTgRcLinksActiveBeamElevationRx = _RbTgRcLinksActiveBeamElevationRx_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 18),
    _RbTgRcLinksActiveBeamElevationRx_Type()
)
rbTgRcLinksActiveBeamElevationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveBeamElevationRx.setStatus("current")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveBeamElevationRx.setUnits("Degrees")
_RbTgRcLinksActiveActiveTileCountRx_Type = RbTgRadioActiveTilesCount
_RbTgRcLinksActiveActiveTileCountRx_Object = MibTableColumn
rbTgRcLinksActiveActiveTileCountRx = _RbTgRcLinksActiveActiveTileCountRx_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 19),
    _RbTgRcLinksActiveActiveTileCountRx_Type()
)
rbTgRcLinksActiveActiveTileCountRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveActiveTileCountRx.setStatus("current")
_RbTgRcLinksActiveBeamIndexTx_Type = RbTgRadioBeamIndex
_RbTgRcLinksActiveBeamIndexTx_Object = MibTableColumn
rbTgRcLinksActiveBeamIndexTx = _RbTgRcLinksActiveBeamIndexTx_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 20),
    _RbTgRcLinksActiveBeamIndexTx_Type()
)
rbTgRcLinksActiveBeamIndexTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveBeamIndexTx.setStatus("current")
_RbTgRcLinksActiveBeamAzimuthTx_Type = RbTgRadioBeamAngle
_RbTgRcLinksActiveBeamAzimuthTx_Object = MibTableColumn
rbTgRcLinksActiveBeamAzimuthTx = _RbTgRcLinksActiveBeamAzimuthTx_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 21),
    _RbTgRcLinksActiveBeamAzimuthTx_Type()
)
rbTgRcLinksActiveBeamAzimuthTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveBeamAzimuthTx.setStatus("current")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveBeamAzimuthTx.setUnits("Degrees")
_RbTgRcLinksActiveBeamElevationTx_Type = RbTgRadioBeamAngle
_RbTgRcLinksActiveBeamElevationTx_Object = MibTableColumn
rbTgRcLinksActiveBeamElevationTx = _RbTgRcLinksActiveBeamElevationTx_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 22),
    _RbTgRcLinksActiveBeamElevationTx_Type()
)
rbTgRcLinksActiveBeamElevationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveBeamElevationTx.setStatus("current")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveBeamElevationTx.setUnits("Degrees")
_RbTgRcLinksActiveActiveTileCountTx_Type = RbTgRadioActiveTilesCount
_RbTgRcLinksActiveActiveTileCountTx_Object = MibTableColumn
rbTgRcLinksActiveActiveTileCountTx = _RbTgRcLinksActiveActiveTileCountTx_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 23),
    _RbTgRcLinksActiveActiveTileCountTx_Type()
)
rbTgRcLinksActiveActiveTileCountTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveActiveTileCountTx.setStatus("current")
_RbTgRcLinksActiveCounterRxOk_Type = Counter64
_RbTgRcLinksActiveCounterRxOk_Object = MibTableColumn
rbTgRcLinksActiveCounterRxOk = _RbTgRcLinksActiveCounterRxOk_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 24),
    _RbTgRcLinksActiveCounterRxOk_Type()
)
rbTgRcLinksActiveCounterRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveCounterRxOk.setStatus("current")
_RbTgRcLinksActiveCounterTxOk_Type = Counter64
_RbTgRcLinksActiveCounterTxOk_Object = MibTableColumn
rbTgRcLinksActiveCounterTxOk = _RbTgRcLinksActiveCounterTxOk_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 25),
    _RbTgRcLinksActiveCounterTxOk_Type()
)
rbTgRcLinksActiveCounterTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveCounterTxOk.setStatus("current")
_RbTgRcLinksActiveCounterRxFail_Type = Counter64
_RbTgRcLinksActiveCounterRxFail_Object = MibTableColumn
rbTgRcLinksActiveCounterRxFail = _RbTgRcLinksActiveCounterRxFail_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 26),
    _RbTgRcLinksActiveCounterRxFail_Type()
)
rbTgRcLinksActiveCounterRxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveCounterRxFail.setStatus("current")
_RbTgRcLinksActiveCounterTxFail_Type = Counter64
_RbTgRcLinksActiveCounterTxFail_Object = MibTableColumn
rbTgRcLinksActiveCounterTxFail = _RbTgRcLinksActiveCounterTxFail_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 27),
    _RbTgRcLinksActiveCounterTxFail_Type()
)
rbTgRcLinksActiveCounterTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveCounterTxFail.setStatus("current")
_RbTgRcLinksActiveCounterRxHcsFail_Type = Counter64
_RbTgRcLinksActiveCounterRxHcsFail_Object = MibTableColumn
rbTgRcLinksActiveCounterRxHcsFail = _RbTgRcLinksActiveCounterRxHcsFail_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 28),
    _RbTgRcLinksActiveCounterRxHcsFail_Type()
)
rbTgRcLinksActiveCounterRxHcsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveCounterRxHcsFail.setStatus("current")
_RbTgRcLinksActiveCounterTxFailures_Type = Counter64
_RbTgRcLinksActiveCounterTxFailures_Object = MibTableColumn
rbTgRcLinksActiveCounterTxFailures = _RbTgRcLinksActiveCounterTxFailures_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 29),
    _RbTgRcLinksActiveCounterTxFailures_Type()
)
rbTgRcLinksActiveCounterTxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveCounterTxFailures.setStatus("current")
_RbTgRcLinksActiveCounterRxFailures_Type = Counter64
_RbTgRcLinksActiveCounterRxFailures_Object = MibTableColumn
rbTgRcLinksActiveCounterRxFailures = _RbTgRcLinksActiveCounterRxFailures_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 30),
    _RbTgRcLinksActiveCounterRxFailures_Type()
)
rbTgRcLinksActiveCounterRxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveCounterRxFailures.setStatus("current")
_RbTgRcLinksActiveCounterRxDropBufSize_Type = Counter64
_RbTgRcLinksActiveCounterRxDropBufSize_Object = MibTableColumn
rbTgRcLinksActiveCounterRxDropBufSize = _RbTgRcLinksActiveCounterRxDropBufSize_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 31),
    _RbTgRcLinksActiveCounterRxDropBufSize_Type()
)
rbTgRcLinksActiveCounterRxDropBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveCounterRxDropBufSize.setStatus("current")
_RbTgRcLinksActiveCounterRxDropEncryptionFail_Type = Counter64
_RbTgRcLinksActiveCounterRxDropEncryptionFail_Object = MibTableColumn
rbTgRcLinksActiveCounterRxDropEncryptionFail = _RbTgRcLinksActiveCounterRxDropEncryptionFail_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 32),
    _RbTgRcLinksActiveCounterRxDropEncryptionFail_Type()
)
rbTgRcLinksActiveCounterRxDropEncryptionFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveCounterRxDropEncryptionFail.setStatus("current")
_RbTgRcLinksActiveCounterRxDropRaMismatch_Type = Counter64
_RbTgRcLinksActiveCounterRxDropRaMismatch_Object = MibTableColumn
rbTgRcLinksActiveCounterRxDropRaMismatch = _RbTgRcLinksActiveCounterRxDropRaMismatch_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 33),
    _RbTgRcLinksActiveCounterRxDropRaMismatch_Type()
)
rbTgRcLinksActiveCounterRxDropRaMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveCounterRxDropRaMismatch.setStatus("current")
_RbTgRcLinksActiveCounterRxDropUnexpected_Type = Counter64
_RbTgRcLinksActiveCounterRxDropUnexpected_Object = MibTableColumn
rbTgRcLinksActiveCounterRxDropUnexpected = _RbTgRcLinksActiveCounterRxDropUnexpected_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 1, 3, 1, 1, 34),
    _RbTgRcLinksActiveCounterRxDropUnexpected_Type()
)
rbTgRcLinksActiveCounterRxDropUnexpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRcLinksActiveCounterRxDropUnexpected.setStatus("current")
_RbTgRadioDn_ObjectIdentity = ObjectIdentity
rbTgRadioDn = _RbTgRadioDn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2)
)
_RbTgRdNodeConfig_ObjectIdentity = ObjectIdentity
rbTgRdNodeConfig = _RbTgRdNodeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 1)
)
_RbTgRdSectorsConfig_ObjectIdentity = ObjectIdentity
rbTgRdSectorsConfig = _RbTgRdSectorsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 2)
)
_RbTgRdLinks_ObjectIdentity = ObjectIdentity
rbTgRdLinks = _RbTgRdLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 3)
)
_RbTgRdLinksConfiguredTable_Object = MibTable
rbTgRdLinksConfiguredTable = _RbTgRdLinksConfiguredTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    rbTgRdLinksConfiguredTable.setStatus("current")
_RbTgRdLinksConfiguredEntry_Object = MibTableRow
rbTgRdLinksConfiguredEntry = _RbTgRdLinksConfiguredEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 3, 1, 1)
)
rbTgRdLinksConfiguredEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MH-TG-MIB", "rbTgRdLinksConfiguredIfIndex"),
)
if mibBuilder.loadTexts:
    rbTgRdLinksConfiguredEntry.setStatus("current")
_RbTgRdLinksConfiguredIfIndex_Type = InterfaceIndex
_RbTgRdLinksConfiguredIfIndex_Object = MibTableColumn
rbTgRdLinksConfiguredIfIndex = _RbTgRdLinksConfiguredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 3, 1, 1, 1),
    _RbTgRdLinksConfiguredIfIndex_Type()
)
rbTgRdLinksConfiguredIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRdLinksConfiguredIfIndex.setStatus("current")
_RbTgRdLinksConfiguredRemoteName_Type = RbTgRadioNodeAssignedName
_RbTgRdLinksConfiguredRemoteName_Object = MibTableColumn
rbTgRdLinksConfiguredRemoteName = _RbTgRdLinksConfiguredRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 3, 1, 1, 2),
    _RbTgRdLinksConfiguredRemoteName_Type()
)
rbTgRdLinksConfiguredRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRdLinksConfiguredRemoteName.setStatus("current")
_RbTgRdLinksConfiguredResponderNodeType_Type = RbTgRadioDnResponderNodeType
_RbTgRdLinksConfiguredResponderNodeType_Object = MibTableColumn
rbTgRdLinksConfiguredResponderNodeType = _RbTgRdLinksConfiguredResponderNodeType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 3, 1, 1, 3),
    _RbTgRdLinksConfiguredResponderNodeType_Type()
)
rbTgRdLinksConfiguredResponderNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRdLinksConfiguredResponderNodeType.setStatus("current")
_RbTgRdLinksConfiguredControlSuperframe_Type = RbTgRadioDnControlSuperframe
_RbTgRdLinksConfiguredControlSuperframe_Object = MibTableColumn
rbTgRdLinksConfiguredControlSuperframe = _RbTgRdLinksConfiguredControlSuperframe_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 3, 1, 1, 4),
    _RbTgRdLinksConfiguredControlSuperframe_Type()
)
rbTgRdLinksConfiguredControlSuperframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRdLinksConfiguredControlSuperframe.setStatus("current")
_RbTgRdLinksConfiguredAdminStatus_Type = RbTgAdminStatus
_RbTgRdLinksConfiguredAdminStatus_Object = MibTableColumn
rbTgRdLinksConfiguredAdminStatus = _RbTgRdLinksConfiguredAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 3, 1, 1, 5),
    _RbTgRdLinksConfiguredAdminStatus_Type()
)
rbTgRdLinksConfiguredAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRdLinksConfiguredAdminStatus.setStatus("current")
_RbTgRdLinksConfiguredLocalSectorBitmap_Type = RbTgRadioDnSectorBitmap
_RbTgRdLinksConfiguredLocalSectorBitmap_Object = MibTableColumn
rbTgRdLinksConfiguredLocalSectorBitmap = _RbTgRdLinksConfiguredLocalSectorBitmap_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 3, 1, 1, 6),
    _RbTgRdLinksConfiguredLocalSectorBitmap_Type()
)
rbTgRdLinksConfiguredLocalSectorBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRdLinksConfiguredLocalSectorBitmap.setStatus("current")
_RbTgRdLinksConfiguredRemoteSectorBitmap_Type = RbTgRadioDnSectorBitmap
_RbTgRdLinksConfiguredRemoteSectorBitmap_Object = MibTableColumn
rbTgRdLinksConfiguredRemoteSectorBitmap = _RbTgRdLinksConfiguredRemoteSectorBitmap_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 3, 1, 1, 7),
    _RbTgRdLinksConfiguredRemoteSectorBitmap_Type()
)
rbTgRdLinksConfiguredRemoteSectorBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRdLinksConfiguredRemoteSectorBitmap.setStatus("current")
_RbTgRdLinksConfiguredLinkState_Type = RbTgRadioDnLinkState
_RbTgRdLinksConfiguredLinkState_Object = MibTableColumn
rbTgRdLinksConfiguredLinkState = _RbTgRdLinksConfiguredLinkState_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 3, 1, 1, 8),
    _RbTgRdLinksConfiguredLinkState_Type()
)
rbTgRdLinksConfiguredLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRdLinksConfiguredLinkState.setStatus("current")
_RbTgRdLinksConfiguredTxGolayIndex_Type = RbTgRadioGolayIndex
_RbTgRdLinksConfiguredTxGolayIndex_Object = MibTableColumn
rbTgRdLinksConfiguredTxGolayIndex = _RbTgRdLinksConfiguredTxGolayIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 3, 1, 1, 9),
    _RbTgRdLinksConfiguredTxGolayIndex_Type()
)
rbTgRdLinksConfiguredTxGolayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRdLinksConfiguredTxGolayIndex.setStatus("current")
_RbTgRdLinksConfiguredRxGolayIndex_Type = RbTgRadioGolayIndex
_RbTgRdLinksConfiguredRxGolayIndex_Object = MibTableColumn
rbTgRdLinksConfiguredRxGolayIndex = _RbTgRdLinksConfiguredRxGolayIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 35, 1, 2, 3, 1, 1, 10),
    _RbTgRdLinksConfiguredRxGolayIndex_Type()
)
rbTgRdLinksConfiguredRxGolayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTgRdLinksConfiguredRxGolayIndex.setStatus("current")
_RbTgGroups_ObjectIdentity = ObjectIdentity
rbTgGroups = _RbTgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 35, 2)
)

# Managed Objects groups

rbTgGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31926, 35, 2, 1)
)
rbTgGeneralGroup.setObjects(
      *(("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveSpeedRx"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveSpeedTx"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveSnr"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveMcsRx"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveMcsTx"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveTxPer"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveRxPer"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveTxPowerIndex"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveBeamAzimuthTx"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveBeamElevationTx"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveActiveTileCountTx"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveBeamIndexRx"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveBeamAzimuthRx"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveBeamElevationRx"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveActiveTileCountRx"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveBeamIndexTx"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveCounterRxOk"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveCounterTxOk"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveCounterTxFail"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveCounterRxFail"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveCounterRxHcsFail"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveCounterTxFailures"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveCounterRxFailures"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveCounterRxDropBufSize"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveCounterRxDropEncryptionFail"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveCounterRxDropRaMismatch"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveCounterRxDropUnexpected"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRdLinksConfiguredIfIndex"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveActualRemoteSector"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveActualLocalSector"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveLocalRole"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveLinkUptime"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRdLinksConfiguredResponderNodeType"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRdLinksConfiguredControlSuperframe"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRdLinksConfiguredAdminStatus"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRdLinksConfiguredLocalSectorBitmap"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRdLinksConfiguredRemoteSectorBitmap"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRdLinksConfiguredLinkState"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRdLinksConfiguredTxGolayIndex"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRdLinksConfiguredRxGolayIndex"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveRssi"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveIfIndex"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRcLinksActiveRemoteName"),
        ("RADIO-BRIDGE-MH-TG-MIB", "rbTgRdLinksConfiguredRemoteName"))
)
if mibBuilder.loadTexts:
    rbTgGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIO-BRIDGE-MH-TG-MIB",
    **{"RbTgAdminStatus": RbTgAdminStatus,
       "RbTgRadioNodeAssignedName": RbTgRadioNodeAssignedName,
       "RbTgRadioSectorIndex": RbTgRadioSectorIndex,
       "RbTgRadioNodeLocalRole": RbTgRadioNodeLocalRole,
       "RbTgRadioMcs": RbTgRadioMcs,
       "RbTgRadioTxPowerIndex": RbTgRadioTxPowerIndex,
       "RbTgRadioRfLinkSpeed": RbTgRadioRfLinkSpeed,
       "RbTgRadioBeamIndex": RbTgRadioBeamIndex,
       "RbTgRadioBeamAngle": RbTgRadioBeamAngle,
       "RbTgRadioActiveTilesCount": RbTgRadioActiveTilesCount,
       "RbTgRadioGolayIndex": RbTgRadioGolayIndex,
       "RbTgRadioDnResponderNodeType": RbTgRadioDnResponderNodeType,
       "RbTgRadioDnControlSuperframe": RbTgRadioDnControlSuperframe,
       "RbTgRadioDnSectorBitmap": RbTgRadioDnSectorBitmap,
       "RbTgRadioDnLinkState": RbTgRadioDnLinkState,
       "rbTgMIB": rbTgMIB,
       "rbTgMIBObjects": rbTgMIBObjects,
       "rbTgRadioCommon": rbTgRadioCommon,
       "rbTgRcNodeConfig": rbTgRcNodeConfig,
       "rbTgRcSectorsConfig": rbTgRcSectorsConfig,
       "rbTgRcLinks": rbTgRcLinks,
       "rbTgRcLinksActiveTable": rbTgRcLinksActiveTable,
       "rbTgRcLinksActiveEntry": rbTgRcLinksActiveEntry,
       "rbTgRcLinksActiveIfIndex": rbTgRcLinksActiveIfIndex,
       "rbTgRcLinksActiveRemoteName": rbTgRcLinksActiveRemoteName,
       "rbTgRcLinksActiveActualRemoteSector": rbTgRcLinksActiveActualRemoteSector,
       "rbTgRcLinksActiveActualLocalSector": rbTgRcLinksActiveActualLocalSector,
       "rbTgRcLinksActiveLocalRole": rbTgRcLinksActiveLocalRole,
       "rbTgRcLinksActiveLinkUptime": rbTgRcLinksActiveLinkUptime,
       "rbTgRcLinksActiveRssi": rbTgRcLinksActiveRssi,
       "rbTgRcLinksActiveSnr": rbTgRcLinksActiveSnr,
       "rbTgRcLinksActiveMcsRx": rbTgRcLinksActiveMcsRx,
       "rbTgRcLinksActiveMcsTx": rbTgRcLinksActiveMcsTx,
       "rbTgRcLinksActiveRxPer": rbTgRcLinksActiveRxPer,
       "rbTgRcLinksActiveTxPer": rbTgRcLinksActiveTxPer,
       "rbTgRcLinksActiveTxPowerIndex": rbTgRcLinksActiveTxPowerIndex,
       "rbTgRcLinksActiveSpeedRx": rbTgRcLinksActiveSpeedRx,
       "rbTgRcLinksActiveSpeedTx": rbTgRcLinksActiveSpeedTx,
       "rbTgRcLinksActiveBeamIndexRx": rbTgRcLinksActiveBeamIndexRx,
       "rbTgRcLinksActiveBeamAzimuthRx": rbTgRcLinksActiveBeamAzimuthRx,
       "rbTgRcLinksActiveBeamElevationRx": rbTgRcLinksActiveBeamElevationRx,
       "rbTgRcLinksActiveActiveTileCountRx": rbTgRcLinksActiveActiveTileCountRx,
       "rbTgRcLinksActiveBeamIndexTx": rbTgRcLinksActiveBeamIndexTx,
       "rbTgRcLinksActiveBeamAzimuthTx": rbTgRcLinksActiveBeamAzimuthTx,
       "rbTgRcLinksActiveBeamElevationTx": rbTgRcLinksActiveBeamElevationTx,
       "rbTgRcLinksActiveActiveTileCountTx": rbTgRcLinksActiveActiveTileCountTx,
       "rbTgRcLinksActiveCounterRxOk": rbTgRcLinksActiveCounterRxOk,
       "rbTgRcLinksActiveCounterTxOk": rbTgRcLinksActiveCounterTxOk,
       "rbTgRcLinksActiveCounterRxFail": rbTgRcLinksActiveCounterRxFail,
       "rbTgRcLinksActiveCounterTxFail": rbTgRcLinksActiveCounterTxFail,
       "rbTgRcLinksActiveCounterRxHcsFail": rbTgRcLinksActiveCounterRxHcsFail,
       "rbTgRcLinksActiveCounterTxFailures": rbTgRcLinksActiveCounterTxFailures,
       "rbTgRcLinksActiveCounterRxFailures": rbTgRcLinksActiveCounterRxFailures,
       "rbTgRcLinksActiveCounterRxDropBufSize": rbTgRcLinksActiveCounterRxDropBufSize,
       "rbTgRcLinksActiveCounterRxDropEncryptionFail": rbTgRcLinksActiveCounterRxDropEncryptionFail,
       "rbTgRcLinksActiveCounterRxDropRaMismatch": rbTgRcLinksActiveCounterRxDropRaMismatch,
       "rbTgRcLinksActiveCounterRxDropUnexpected": rbTgRcLinksActiveCounterRxDropUnexpected,
       "rbTgRadioDn": rbTgRadioDn,
       "rbTgRdNodeConfig": rbTgRdNodeConfig,
       "rbTgRdSectorsConfig": rbTgRdSectorsConfig,
       "rbTgRdLinks": rbTgRdLinks,
       "rbTgRdLinksConfiguredTable": rbTgRdLinksConfiguredTable,
       "rbTgRdLinksConfiguredEntry": rbTgRdLinksConfiguredEntry,
       "rbTgRdLinksConfiguredIfIndex": rbTgRdLinksConfiguredIfIndex,
       "rbTgRdLinksConfiguredRemoteName": rbTgRdLinksConfiguredRemoteName,
       "rbTgRdLinksConfiguredResponderNodeType": rbTgRdLinksConfiguredResponderNodeType,
       "rbTgRdLinksConfiguredControlSuperframe": rbTgRdLinksConfiguredControlSuperframe,
       "rbTgRdLinksConfiguredAdminStatus": rbTgRdLinksConfiguredAdminStatus,
       "rbTgRdLinksConfiguredLocalSectorBitmap": rbTgRdLinksConfiguredLocalSectorBitmap,
       "rbTgRdLinksConfiguredRemoteSectorBitmap": rbTgRdLinksConfiguredRemoteSectorBitmap,
       "rbTgRdLinksConfiguredLinkState": rbTgRdLinksConfiguredLinkState,
       "rbTgRdLinksConfiguredTxGolayIndex": rbTgRdLinksConfiguredTxGolayIndex,
       "rbTgRdLinksConfiguredRxGolayIndex": rbTgRdLinksConfiguredRxGolayIndex,
       "rbTgGroups": rbTgGroups,
       "rbTgGeneralGroup": rbTgGeneralGroup}
)
