# SNMP MIB module (ACD-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\accedian\ACD-PORT-MIB

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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acdPort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9)
)
if mibBuilder.loadTexts:
    acdPort.setRevisions(
        ("2016-09-23 01:00",
         "2016-05-26 01:00",
         "2016-03-15 01:00",
         "2014-11-13 01:00",
         "2014-06-23 01:00",
         "2011-10-10 01:00",
         "2010-10-01 01:00",
         "2008-05-01 01:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdPortMIBObjects_ObjectIdentity = ObjectIdentity
acdPortMIBObjects = _AcdPortMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1)
)
_AcdPortConfig_ObjectIdentity = ObjectIdentity
acdPortConfig = _AcdPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1)
)
_AcdPortConfigTable_Object = MibTable
acdPortConfigTable = _AcdPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acdPortConfigTable.setStatus("current")
_AcdPortConfigEntry_Object = MibTableRow
acdPortConfigEntry = _AcdPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1)
)
acdPortConfigEntry.setIndexNames(
    (0, "ACD-PORT-MIB", "acdPortConfigIndex"),
)
if mibBuilder.loadTexts:
    acdPortConfigEntry.setStatus("current")


class _AcdPortConfigIndex_Type(Unsigned32):
    """Custom type acdPortConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdPortConfigIndex_Type.__name__ = "Unsigned32"
_AcdPortConfigIndex_Object = MibTableColumn
acdPortConfigIndex = _AcdPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 1),
    _AcdPortConfigIndex_Type()
)
acdPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPortConfigIndex.setStatus("current")


class _AcdPortConfigName_Type(DisplayString):
    """Custom type acdPortConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdPortConfigName_Type.__name__ = "DisplayString"
_AcdPortConfigName_Object = MibTableColumn
acdPortConfigName = _AcdPortConfigName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 2),
    _AcdPortConfigName_Type()
)
acdPortConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigName.setStatus("current")


class _AcdPortConfigAlias_Type(DisplayString):
    """Custom type acdPortConfigAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AcdPortConfigAlias_Type.__name__ = "DisplayString"
_AcdPortConfigAlias_Object = MibTableColumn
acdPortConfigAlias = _AcdPortConfigAlias_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 3),
    _AcdPortConfigAlias_Type()
)
acdPortConfigAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigAlias.setStatus("current")
_AcdPortConfigMacAddress_Type = MacAddress
_AcdPortConfigMacAddress_Object = MibTableColumn
acdPortConfigMacAddress = _AcdPortConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 4),
    _AcdPortConfigMacAddress_Type()
)
acdPortConfigMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortConfigMacAddress.setStatus("current")
_AcdPortConfigConnectorId_Type = ObjectIdentifier
_AcdPortConfigConnectorId_Object = MibTableColumn
acdPortConfigConnectorId = _AcdPortConfigConnectorId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 5),
    _AcdPortConfigConnectorId_Type()
)
acdPortConfigConnectorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortConfigConnectorId.setStatus("current")
_AcdPortConfigState_Type = TruthValue
_AcdPortConfigState_Object = MibTableColumn
acdPortConfigState = _AcdPortConfigState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 6),
    _AcdPortConfigState_Type()
)
acdPortConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigState.setStatus("current")
_AcdPortConfigMtu_Type = Unsigned32
_AcdPortConfigMtu_Object = MibTableColumn
acdPortConfigMtu = _AcdPortConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 7),
    _AcdPortConfigMtu_Type()
)
acdPortConfigMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigMtu.setStatus("current")
_AcdPortConfigAutoNegoState_Type = TruthValue
_AcdPortConfigAutoNegoState_Object = MibTableColumn
acdPortConfigAutoNegoState = _AcdPortConfigAutoNegoState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 8),
    _AcdPortConfigAutoNegoState_Type()
)
acdPortConfigAutoNegoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigAutoNegoState.setStatus("current")
_AcdPortConfigSpeed_Type = Unsigned32
_AcdPortConfigSpeed_Object = MibTableColumn
acdPortConfigSpeed = _AcdPortConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 9),
    _AcdPortConfigSpeed_Type()
)
acdPortConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigSpeed.setStatus("current")


class _AcdPortConfigDuplex_Type(Integer32):
    """Custom type acdPortConfigDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_AcdPortConfigDuplex_Type.__name__ = "Integer32"
_AcdPortConfigDuplex_Object = MibTableColumn
acdPortConfigDuplex = _AcdPortConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 10),
    _AcdPortConfigDuplex_Type()
)
acdPortConfigDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigDuplex.setStatus("current")


class _AcdPortConfigMdi_Type(Integer32):
    """Custom type acdPortConfigMdi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoMdi", 1),
          ("mdi", 2),
          ("mdix", 3))
    )


_AcdPortConfigMdi_Type.__name__ = "Integer32"
_AcdPortConfigMdi_Object = MibTableColumn
acdPortConfigMdi = _AcdPortConfigMdi_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 11),
    _AcdPortConfigMdi_Type()
)
acdPortConfigMdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigMdi.setStatus("current")


class _AcdPortConfigPauseMode_Type(Integer32):
    """Custom type acdPortConfigPauseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("local", 2),
          ("forward", 3))
    )


_AcdPortConfigPauseMode_Type.__name__ = "Integer32"
_AcdPortConfigPauseMode_Object = MibTableColumn
acdPortConfigPauseMode = _AcdPortConfigPauseMode_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 12),
    _AcdPortConfigPauseMode_Type()
)
acdPortConfigPauseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigPauseMode.setStatus("current")


class _AcdPortConfigAdvertisement_Type(Bits):
    """Custom type acdPortConfigAdvertisement based on Bits"""
    namedValues = NamedValues(
        *(("bHalfDuplex10Mbps", 0),
          ("bFullDuplex10Mbps", 1),
          ("bHalfDuplex100Mbps", 2),
          ("bFullDuplex100Mbps", 3),
          ("bHalfDuplex1Gbps", 4),
          ("bFullDuplex1Gbps", 5),
          ("bPauseSymmetric", 6),
          ("bPauseAsymmetric", 7))
    )

_AcdPortConfigAdvertisement_Type.__name__ = "Bits"
_AcdPortConfigAdvertisement_Object = MibTableColumn
acdPortConfigAdvertisement = _AcdPortConfigAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 13),
    _AcdPortConfigAdvertisement_Type()
)
acdPortConfigAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigAdvertisement.setStatus("current")
_AcdPortConfigForceTxOn_Type = TruthValue
_AcdPortConfigForceTxOn_Object = MibTableColumn
acdPortConfigForceTxOn = _AcdPortConfigForceTxOn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 14),
    _AcdPortConfigForceTxOn_Type()
)
acdPortConfigForceTxOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigForceTxOn.setStatus("current")


class _AcdPortConfigLaserMode_Type(Integer32):
    """Custom type acdPortConfigLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_AcdPortConfigLaserMode_Type.__name__ = "Integer32"
_AcdPortConfigLaserMode_Object = MibTableColumn
acdPortConfigLaserMode = _AcdPortConfigLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 15),
    _AcdPortConfigLaserMode_Type()
)
acdPortConfigLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigLaserMode.setStatus("current")
_AcdPortStatus_ObjectIdentity = ObjectIdentity
acdPortStatus = _AcdPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2)
)
_AcdPortStatusTable_Object = MibTable
acdPortStatusTable = _AcdPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    acdPortStatusTable.setStatus("current")
_AcdPortStatusEntry_Object = MibTableRow
acdPortStatusEntry = _AcdPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1)
)
acdPortStatusEntry.setIndexNames(
    (0, "ACD-PORT-MIB", "acdPortStatusIndex"),
)
if mibBuilder.loadTexts:
    acdPortStatusEntry.setStatus("current")


class _AcdPortStatusIndex_Type(Unsigned32):
    """Custom type acdPortStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdPortStatusIndex_Type.__name__ = "Unsigned32"
_AcdPortStatusIndex_Object = MibTableColumn
acdPortStatusIndex = _AcdPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 1),
    _AcdPortStatusIndex_Type()
)
acdPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPortStatusIndex.setStatus("current")
_AcdPortStatusSpeed_Type = Unsigned32
_AcdPortStatusSpeed_Object = MibTableColumn
acdPortStatusSpeed = _AcdPortStatusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 2),
    _AcdPortStatusSpeed_Type()
)
acdPortStatusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusSpeed.setStatus("current")


class _AcdPortStatusDuplex_Type(Integer32):
    """Custom type acdPortStatusDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_AcdPortStatusDuplex_Type.__name__ = "Integer32"
_AcdPortStatusDuplex_Object = MibTableColumn
acdPortStatusDuplex = _AcdPortStatusDuplex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 3),
    _AcdPortStatusDuplex_Type()
)
acdPortStatusDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusDuplex.setStatus("current")


class _AcdPortStatusMdi_Type(Integer32):
    """Custom type acdPortStatusMdi based on Integer32"""
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


_AcdPortStatusMdi_Type.__name__ = "Integer32"
_AcdPortStatusMdi_Object = MibTableColumn
acdPortStatusMdi = _AcdPortStatusMdi_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 4),
    _AcdPortStatusMdi_Type()
)
acdPortStatusMdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusMdi.setStatus("current")
_AcdPortStatusTxPause_Type = TruthValue
_AcdPortStatusTxPause_Object = MibTableColumn
acdPortStatusTxPause = _AcdPortStatusTxPause_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 5),
    _AcdPortStatusTxPause_Type()
)
acdPortStatusTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusTxPause.setStatus("current")
_AcdPortStatusRxPause_Type = TruthValue
_AcdPortStatusRxPause_Object = MibTableColumn
acdPortStatusRxPause = _AcdPortStatusRxPause_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 6),
    _AcdPortStatusRxPause_Type()
)
acdPortStatusRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusRxPause.setStatus("current")


class _AcdPortStatusLinkPartnerAbility_Type(Bits):
    """Custom type acdPortStatusLinkPartnerAbility based on Bits"""
    namedValues = NamedValues(
        *(("bHalfDuplex10Mbps", 0),
          ("bFullDuplex10Mbps", 1),
          ("bHalfDuplex100Mbps", 2),
          ("bFullDuplex100Mbps", 3),
          ("bHalfDuplex1Gbps", 4),
          ("bFullDuplex1Gbps", 5),
          ("bPauseSymmetric", 6),
          ("bPauseAsymmetric", 7))
    )

_AcdPortStatusLinkPartnerAbility_Type.__name__ = "Bits"
_AcdPortStatusLinkPartnerAbility_Object = MibTableColumn
acdPortStatusLinkPartnerAbility = _AcdPortStatusLinkPartnerAbility_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 7),
    _AcdPortStatusLinkPartnerAbility_Type()
)
acdPortStatusLinkPartnerAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusLinkPartnerAbility.setStatus("current")
_AcdPortStatusLinkStatus_Type = TruthValue
_AcdPortStatusLinkStatus_Object = MibTableColumn
acdPortStatusLinkStatus = _AcdPortStatusLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 8),
    _AcdPortStatusLinkStatus_Type()
)
acdPortStatusLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusLinkStatus.setStatus("current")


class _AcdPortStatusMedia_Type(Bits):
    """Custom type acdPortStatusMedia based on Bits"""
    namedValues = NamedValues(
        *(("bOther", 0),
          ("bAUI", 1),
          ("b10base5", 2),
          ("bFoirl", 3),
          ("b10base2", 4),
          ("b10baseT", 5),
          ("b10baseFP", 6),
          ("b10baseFB", 7),
          ("b10baseFL", 8),
          ("b10broad36", 9),
          ("b10baseTHD", 10),
          ("b10baseTFD", 11),
          ("b10baseFLHD", 12),
          ("b10baseFLFD", 13),
          ("b100baseT4", 14),
          ("b100baseTXHD", 15),
          ("b100baseTXFD", 16),
          ("b100baseFXHD", 17),
          ("b100baseFXFD", 18),
          ("b100baseT2HD", 19),
          ("b100baseT2FD", 20),
          ("b1000baseXHD", 21),
          ("b1000baseXFD", 22),
          ("b1000baseLXHD", 23),
          ("b1000baseLXFD", 24),
          ("b1000baseSXHD", 25),
          ("b1000baseSXFD", 26),
          ("b1000baseCXHD", 27),
          ("b1000baseCXFD", 28),
          ("b1000baseTHD", 29),
          ("b1000baseTFD", 30))
    )

_AcdPortStatusMedia_Type.__name__ = "Bits"
_AcdPortStatusMedia_Object = MibTableColumn
acdPortStatusMedia = _AcdPortStatusMedia_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 9),
    _AcdPortStatusMedia_Type()
)
acdPortStatusMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusMedia.setStatus("current")
_AcdPortStatusIsMonitor_Type = TruthValue
_AcdPortStatusIsMonitor_Object = MibTableColumn
acdPortStatusIsMonitor = _AcdPortStatusIsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 10),
    _AcdPortStatusIsMonitor_Type()
)
acdPortStatusIsMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusIsMonitor.setStatus("current")
_AcdPortStatusIsManagement_Type = TruthValue
_AcdPortStatusIsManagement_Object = MibTableColumn
acdPortStatusIsManagement = _AcdPortStatusIsManagement_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 11),
    _AcdPortStatusIsManagement_Type()
)
acdPortStatusIsManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusIsManagement.setStatus("current")
_AcdPortStatusIsSFP_Type = TruthValue
_AcdPortStatusIsSFP_Object = MibTableColumn
acdPortStatusIsSFP = _AcdPortStatusIsSFP_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 12),
    _AcdPortStatusIsSFP_Type()
)
acdPortStatusIsSFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusIsSFP.setStatus("current")
_AcdPortStatusIsFiber_Type = TruthValue
_AcdPortStatusIsFiber_Object = MibTableColumn
acdPortStatusIsFiber = _AcdPortStatusIsFiber_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 13),
    _AcdPortStatusIsFiber_Type()
)
acdPortStatusIsFiber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusIsFiber.setStatus("current")
_AcdPortStats_ObjectIdentity = ObjectIdentity
acdPortStats = _AcdPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3)
)
_AcdPortTxStatsTable_Object = MibTable
acdPortTxStatsTable = _AcdPortTxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    acdPortTxStatsTable.setStatus("current")
_AcdPortTxStatsEntry_Object = MibTableRow
acdPortTxStatsEntry = _AcdPortTxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1)
)
acdPortTxStatsEntry.setIndexNames(
    (0, "ACD-PORT-MIB", "acdPortTxStatsIndex"),
)
if mibBuilder.loadTexts:
    acdPortTxStatsEntry.setStatus("current")


class _AcdPortTxStatsIndex_Type(Unsigned32):
    """Custom type acdPortTxStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdPortTxStatsIndex_Type.__name__ = "Unsigned32"
_AcdPortTxStatsIndex_Object = MibTableColumn
acdPortTxStatsIndex = _AcdPortTxStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 1),
    _AcdPortTxStatsIndex_Type()
)
acdPortTxStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPortTxStatsIndex.setStatus("current")


class _AcdPortTxStatsSupportBits_Type(Bits):
    """Custom type acdPortTxStatsSupportBits based on Bits"""
    namedValues = NamedValues(
        *(("bBytesGood", 0),
          ("bBytesTotal", 1),
          ("bUnicastPkts", 2),
          ("bMulticastPkts", 3),
          ("bBroadcastPkts", 4),
          ("bPauseFrames", 5),
          ("bTaggedFrames", 6),
          ("bCRCErrors", 7),
          ("bDeferred", 8),
          ("bExcessiveDeferrals", 9),
          ("bSingleCollisions", 10),
          ("bMultipleCollisions", 11),
          ("bExcessiveCollisions", 12),
          ("bLateCollisions", 13),
          ("bNormalCollisions", 14),
          ("bFifoErrors", 15),
          ("bPkts64", 16),
          ("bPkts65to127", 17),
          ("bPkts128to255", 18),
          ("bPkts256to511", 19),
          ("bPkts512to1023", 20),
          ("bPkts1024to1518", 21),
          ("bPkts1519to2047", 22),
          ("bPkts2048to4095", 23),
          ("bPkts4096to8191", 24),
          ("bPkts8192andMore", 25),
          ("bPktsLarge", 26),
          ("bL1Rate", 27),
          ("bL1Percent", 28),
          ("bL2Rate", 29))
    )

_AcdPortTxStatsSupportBits_Type.__name__ = "Bits"
_AcdPortTxStatsSupportBits_Object = MibTableColumn
acdPortTxStatsSupportBits = _AcdPortTxStatsSupportBits_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 2),
    _AcdPortTxStatsSupportBits_Type()
)
acdPortTxStatsSupportBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsSupportBits.setStatus("current")
_AcdPortTxStatsBytesGood_Type = Counter64
_AcdPortTxStatsBytesGood_Object = MibTableColumn
acdPortTxStatsBytesGood = _AcdPortTxStatsBytesGood_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 3),
    _AcdPortTxStatsBytesGood_Type()
)
acdPortTxStatsBytesGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsBytesGood.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsBytesGood.setUnits("Octets")
_AcdPortTxStatsBytesTotal_Type = Counter64
_AcdPortTxStatsBytesTotal_Object = MibTableColumn
acdPortTxStatsBytesTotal = _AcdPortTxStatsBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 4),
    _AcdPortTxStatsBytesTotal_Type()
)
acdPortTxStatsBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsBytesTotal.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsBytesTotal.setUnits("Octets")
_AcdPortTxStatsUnicastPkts_Type = Counter64
_AcdPortTxStatsUnicastPkts_Object = MibTableColumn
acdPortTxStatsUnicastPkts = _AcdPortTxStatsUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 5),
    _AcdPortTxStatsUnicastPkts_Type()
)
acdPortTxStatsUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsUnicastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsUnicastPkts.setUnits("Packets")
_AcdPortTxStatsMulticastPkts_Type = Counter64
_AcdPortTxStatsMulticastPkts_Object = MibTableColumn
acdPortTxStatsMulticastPkts = _AcdPortTxStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 6),
    _AcdPortTxStatsMulticastPkts_Type()
)
acdPortTxStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsMulticastPkts.setUnits("Packets")
_AcdPortTxStatsBroadcastPkts_Type = Counter64
_AcdPortTxStatsBroadcastPkts_Object = MibTableColumn
acdPortTxStatsBroadcastPkts = _AcdPortTxStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 7),
    _AcdPortTxStatsBroadcastPkts_Type()
)
acdPortTxStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsBroadcastPkts.setUnits("Packets")
_AcdPortTxStatsPauseFrames_Type = Counter64
_AcdPortTxStatsPauseFrames_Object = MibTableColumn
acdPortTxStatsPauseFrames = _AcdPortTxStatsPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 8),
    _AcdPortTxStatsPauseFrames_Type()
)
acdPortTxStatsPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPauseFrames.setUnits("Packets")
_AcdPortTxStatsTaggedFrames_Type = Counter64
_AcdPortTxStatsTaggedFrames_Object = MibTableColumn
acdPortTxStatsTaggedFrames = _AcdPortTxStatsTaggedFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 9),
    _AcdPortTxStatsTaggedFrames_Type()
)
acdPortTxStatsTaggedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsTaggedFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsTaggedFrames.setUnits("Packets")
_AcdPortTxStatsCRCErrors_Type = Counter64
_AcdPortTxStatsCRCErrors_Object = MibTableColumn
acdPortTxStatsCRCErrors = _AcdPortTxStatsCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 10),
    _AcdPortTxStatsCRCErrors_Type()
)
acdPortTxStatsCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsCRCErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsCRCErrors.setUnits("Packets")
_AcdPortTxStatsDeferred_Type = Counter64
_AcdPortTxStatsDeferred_Object = MibTableColumn
acdPortTxStatsDeferred = _AcdPortTxStatsDeferred_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 11),
    _AcdPortTxStatsDeferred_Type()
)
acdPortTxStatsDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsDeferred.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsDeferred.setUnits("Packets")
_AcdPortTxStatsExcessiveDeferrals_Type = Counter64
_AcdPortTxStatsExcessiveDeferrals_Object = MibTableColumn
acdPortTxStatsExcessiveDeferrals = _AcdPortTxStatsExcessiveDeferrals_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 12),
    _AcdPortTxStatsExcessiveDeferrals_Type()
)
acdPortTxStatsExcessiveDeferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsExcessiveDeferrals.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsExcessiveDeferrals.setUnits("Packets")
_AcdPortTxStatsSingleCollisions_Type = Counter64
_AcdPortTxStatsSingleCollisions_Object = MibTableColumn
acdPortTxStatsSingleCollisions = _AcdPortTxStatsSingleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 13),
    _AcdPortTxStatsSingleCollisions_Type()
)
acdPortTxStatsSingleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsSingleCollisions.setStatus("current")
_AcdPortTxStatsMultipleCollisions_Type = Counter64
_AcdPortTxStatsMultipleCollisions_Object = MibTableColumn
acdPortTxStatsMultipleCollisions = _AcdPortTxStatsMultipleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 14),
    _AcdPortTxStatsMultipleCollisions_Type()
)
acdPortTxStatsMultipleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsMultipleCollisions.setStatus("current")
_AcdPortTxStatsExcessiveCollisions_Type = Counter64
_AcdPortTxStatsExcessiveCollisions_Object = MibTableColumn
acdPortTxStatsExcessiveCollisions = _AcdPortTxStatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 15),
    _AcdPortTxStatsExcessiveCollisions_Type()
)
acdPortTxStatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsExcessiveCollisions.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsExcessiveCollisions.setUnits("Packets")
_AcdPortTxStatsLateCollisions_Type = Counter64
_AcdPortTxStatsLateCollisions_Object = MibTableColumn
acdPortTxStatsLateCollisions = _AcdPortTxStatsLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 16),
    _AcdPortTxStatsLateCollisions_Type()
)
acdPortTxStatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsLateCollisions.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsLateCollisions.setUnits("Packets")
_AcdPortTxStatsNormalCollisions_Type = Counter64
_AcdPortTxStatsNormalCollisions_Object = MibTableColumn
acdPortTxStatsNormalCollisions = _AcdPortTxStatsNormalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 17),
    _AcdPortTxStatsNormalCollisions_Type()
)
acdPortTxStatsNormalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsNormalCollisions.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsNormalCollisions.setUnits("Packets")
_AcdPortTxStatsFifoErrors_Type = Counter64
_AcdPortTxStatsFifoErrors_Object = MibTableColumn
acdPortTxStatsFifoErrors = _AcdPortTxStatsFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 18),
    _AcdPortTxStatsFifoErrors_Type()
)
acdPortTxStatsFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsFifoErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsFifoErrors.setUnits("Packets")
_AcdPortTxStatsPkts64_Type = Counter64
_AcdPortTxStatsPkts64_Object = MibTableColumn
acdPortTxStatsPkts64 = _AcdPortTxStatsPkts64_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 19),
    _AcdPortTxStatsPkts64_Type()
)
acdPortTxStatsPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts64.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts64.setUnits("Packets")
_AcdPortTxStatsPkts65to127_Type = Counter64
_AcdPortTxStatsPkts65to127_Object = MibTableColumn
acdPortTxStatsPkts65to127 = _AcdPortTxStatsPkts65to127_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 20),
    _AcdPortTxStatsPkts65to127_Type()
)
acdPortTxStatsPkts65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts65to127.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts65to127.setUnits("Packets")
_AcdPortTxStatsPkts128to255_Type = Counter64
_AcdPortTxStatsPkts128to255_Object = MibTableColumn
acdPortTxStatsPkts128to255 = _AcdPortTxStatsPkts128to255_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 21),
    _AcdPortTxStatsPkts128to255_Type()
)
acdPortTxStatsPkts128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts128to255.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts128to255.setUnits("Packets")
_AcdPortTxStatsPkts256to511_Type = Counter64
_AcdPortTxStatsPkts256to511_Object = MibTableColumn
acdPortTxStatsPkts256to511 = _AcdPortTxStatsPkts256to511_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 22),
    _AcdPortTxStatsPkts256to511_Type()
)
acdPortTxStatsPkts256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts256to511.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts256to511.setUnits("Packets")
_AcdPortTxStatsPkts512to1023_Type = Counter64
_AcdPortTxStatsPkts512to1023_Object = MibTableColumn
acdPortTxStatsPkts512to1023 = _AcdPortTxStatsPkts512to1023_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 23),
    _AcdPortTxStatsPkts512to1023_Type()
)
acdPortTxStatsPkts512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts512to1023.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts512to1023.setUnits("Packets")
_AcdPortTxStatsPkts1024to1518_Type = Counter64
_AcdPortTxStatsPkts1024to1518_Object = MibTableColumn
acdPortTxStatsPkts1024to1518 = _AcdPortTxStatsPkts1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 24),
    _AcdPortTxStatsPkts1024to1518_Type()
)
acdPortTxStatsPkts1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts1024to1518.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts1024to1518.setUnits("Packets")
_AcdPortTxStatsPkts1519to2047_Type = Counter64
_AcdPortTxStatsPkts1519to2047_Object = MibTableColumn
acdPortTxStatsPkts1519to2047 = _AcdPortTxStatsPkts1519to2047_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 25),
    _AcdPortTxStatsPkts1519to2047_Type()
)
acdPortTxStatsPkts1519to2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts1519to2047.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts1519to2047.setUnits("Packets")
_AcdPortTxStatsPkts2048to4095_Type = Counter64
_AcdPortTxStatsPkts2048to4095_Object = MibTableColumn
acdPortTxStatsPkts2048to4095 = _AcdPortTxStatsPkts2048to4095_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 26),
    _AcdPortTxStatsPkts2048to4095_Type()
)
acdPortTxStatsPkts2048to4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts2048to4095.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts2048to4095.setUnits("Packets")
_AcdPortTxStatsPkts4096to8191_Type = Counter64
_AcdPortTxStatsPkts4096to8191_Object = MibTableColumn
acdPortTxStatsPkts4096to8191 = _AcdPortTxStatsPkts4096to8191_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 27),
    _AcdPortTxStatsPkts4096to8191_Type()
)
acdPortTxStatsPkts4096to8191.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts4096to8191.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts4096to8191.setUnits("Packets")
_AcdPortTxStatsPkts8192andMore_Type = Counter64
_AcdPortTxStatsPkts8192andMore_Object = MibTableColumn
acdPortTxStatsPkts8192andMore = _AcdPortTxStatsPkts8192andMore_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 28),
    _AcdPortTxStatsPkts8192andMore_Type()
)
acdPortTxStatsPkts8192andMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts8192andMore.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts8192andMore.setUnits("Packets")
_AcdPortTxStatsPktsLarge_Type = Counter64
_AcdPortTxStatsPktsLarge_Object = MibTableColumn
acdPortTxStatsPktsLarge = _AcdPortTxStatsPktsLarge_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 29),
    _AcdPortTxStatsPktsLarge_Type()
)
acdPortTxStatsPktsLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPktsLarge.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPktsLarge.setUnits("Packets")
_AcdPortTxL1Rate_Type = Gauge32
_AcdPortTxL1Rate_Object = MibTableColumn
acdPortTxL1Rate = _AcdPortTxL1Rate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 30),
    _AcdPortTxL1Rate_Type()
)
acdPortTxL1Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxL1Rate.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxL1Rate.setUnits("Mbps")
_AcdPortTxL1Percent_Type = Gauge32
_AcdPortTxL1Percent_Object = MibTableColumn
acdPortTxL1Percent = _AcdPortTxL1Percent_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 31),
    _AcdPortTxL1Percent_Type()
)
acdPortTxL1Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxL1Percent.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxL1Percent.setUnits("%")
_AcdPortTxL2Rate_Type = Gauge32
_AcdPortTxL2Rate_Object = MibTableColumn
acdPortTxL2Rate = _AcdPortTxL2Rate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 32),
    _AcdPortTxL2Rate_Type()
)
acdPortTxL2Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxL2Rate.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxL2Rate.setUnits("Mbps")
_AcdPortRxStatsTable_Object = MibTable
acdPortRxStatsTable = _AcdPortRxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2)
)
if mibBuilder.loadTexts:
    acdPortRxStatsTable.setStatus("current")
_AcdPortRxStatsEntry_Object = MibTableRow
acdPortRxStatsEntry = _AcdPortRxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1)
)
acdPortRxStatsEntry.setIndexNames(
    (0, "ACD-PORT-MIB", "acdPortRxStatsIndex"),
)
if mibBuilder.loadTexts:
    acdPortRxStatsEntry.setStatus("current")


class _AcdPortRxStatsIndex_Type(Unsigned32):
    """Custom type acdPortRxStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdPortRxStatsIndex_Type.__name__ = "Unsigned32"
_AcdPortRxStatsIndex_Object = MibTableColumn
acdPortRxStatsIndex = _AcdPortRxStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 1),
    _AcdPortRxStatsIndex_Type()
)
acdPortRxStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPortRxStatsIndex.setStatus("current")


class _AcdPortRxStatsSupportBits_Type(Bits):
    """Custom type acdPortRxStatsSupportBits based on Bits"""
    namedValues = NamedValues(
        *(("bBytesGood", 0),
          ("bBytesTotal", 1),
          ("bRxStatsShortOk", 2),
          ("bRxStatsShortBad", 3),
          ("bRxStatsLongOk", 4),
          ("bRxStatsLongBad", 5),
          ("bUnicastPkts", 6),
          ("bMulticastPkts", 7),
          ("bBroadcastPkts", 8),
          ("bPauseFrames", 9),
          ("bTaggedFrames", 10),
          ("bCRCErrors", 11),
          ("bAlignErrors", 12),
          ("bRuntFrames", 13),
          ("bLengthErrors", 14),
          ("bFalseCRS", 15),
          ("bPhyErrors", 16),
          ("bFifoErrors", 17),
          ("bIgnored", 18),
          ("bBadOpcode", 19),
          ("bPkts64", 20),
          ("bPkts65to127", 21),
          ("bPkts128to255", 22),
          ("bPkts256to511", 23),
          ("bPkts512to1023", 24),
          ("bPkts1024to1518", 25),
          ("bPkts1519to2047", 26),
          ("bPkts2048to4095", 27),
          ("bPkts4096to8191", 28),
          ("bPkts8192andMore", 29),
          ("bPktsLarge", 30))
    )

_AcdPortRxStatsSupportBits_Type.__name__ = "Bits"
_AcdPortRxStatsSupportBits_Object = MibTableColumn
acdPortRxStatsSupportBits = _AcdPortRxStatsSupportBits_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 2),
    _AcdPortRxStatsSupportBits_Type()
)
acdPortRxStatsSupportBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsSupportBits.setStatus("current")
_AcdPortRxStatsBytesGood_Type = Counter64
_AcdPortRxStatsBytesGood_Object = MibTableColumn
acdPortRxStatsBytesGood = _AcdPortRxStatsBytesGood_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 3),
    _AcdPortRxStatsBytesGood_Type()
)
acdPortRxStatsBytesGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsBytesGood.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsBytesGood.setUnits("Octets")
_AcdPortRxStatsBytesTotal_Type = Counter64
_AcdPortRxStatsBytesTotal_Object = MibTableColumn
acdPortRxStatsBytesTotal = _AcdPortRxStatsBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 4),
    _AcdPortRxStatsBytesTotal_Type()
)
acdPortRxStatsBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsBytesTotal.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsBytesTotal.setUnits("Octets")
_AcdPortRxStatsShortOk_Type = Counter64
_AcdPortRxStatsShortOk_Object = MibTableColumn
acdPortRxStatsShortOk = _AcdPortRxStatsShortOk_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 5),
    _AcdPortRxStatsShortOk_Type()
)
acdPortRxStatsShortOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsShortOk.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsShortOk.setUnits("Packets")
_AcdPortRxStatsShortBad_Type = Counter64
_AcdPortRxStatsShortBad_Object = MibTableColumn
acdPortRxStatsShortBad = _AcdPortRxStatsShortBad_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 6),
    _AcdPortRxStatsShortBad_Type()
)
acdPortRxStatsShortBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsShortBad.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsShortBad.setUnits("Packets")
_AcdPortRxStatsLongOk_Type = Counter64
_AcdPortRxStatsLongOk_Object = MibTableColumn
acdPortRxStatsLongOk = _AcdPortRxStatsLongOk_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 7),
    _AcdPortRxStatsLongOk_Type()
)
acdPortRxStatsLongOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsLongOk.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsLongOk.setUnits("Packets")
_AcdPortRxStatsLongBad_Type = Counter64
_AcdPortRxStatsLongBad_Object = MibTableColumn
acdPortRxStatsLongBad = _AcdPortRxStatsLongBad_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 8),
    _AcdPortRxStatsLongBad_Type()
)
acdPortRxStatsLongBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsLongBad.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsLongBad.setUnits("Packets")
_AcdPortRxStatsUnicastPkts_Type = Counter64
_AcdPortRxStatsUnicastPkts_Object = MibTableColumn
acdPortRxStatsUnicastPkts = _AcdPortRxStatsUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 9),
    _AcdPortRxStatsUnicastPkts_Type()
)
acdPortRxStatsUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsUnicastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsUnicastPkts.setUnits("Packets")
_AcdPortRxStatsMulticastPkts_Type = Counter64
_AcdPortRxStatsMulticastPkts_Object = MibTableColumn
acdPortRxStatsMulticastPkts = _AcdPortRxStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 10),
    _AcdPortRxStatsMulticastPkts_Type()
)
acdPortRxStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsMulticastPkts.setUnits("Packets")
_AcdPortRxStatsBroadcastPkts_Type = Counter64
_AcdPortRxStatsBroadcastPkts_Object = MibTableColumn
acdPortRxStatsBroadcastPkts = _AcdPortRxStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 11),
    _AcdPortRxStatsBroadcastPkts_Type()
)
acdPortRxStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsBroadcastPkts.setUnits("Packets")
_AcdPortRxStatsPauseFrames_Type = Counter64
_AcdPortRxStatsPauseFrames_Object = MibTableColumn
acdPortRxStatsPauseFrames = _AcdPortRxStatsPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 12),
    _AcdPortRxStatsPauseFrames_Type()
)
acdPortRxStatsPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPauseFrames.setUnits("Packets")
_AcdPortRxStatsTaggedFrames_Type = Counter64
_AcdPortRxStatsTaggedFrames_Object = MibTableColumn
acdPortRxStatsTaggedFrames = _AcdPortRxStatsTaggedFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 13),
    _AcdPortRxStatsTaggedFrames_Type()
)
acdPortRxStatsTaggedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsTaggedFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsTaggedFrames.setUnits("Packets")
_AcdPortRxStatsCRCErrors_Type = Counter64
_AcdPortRxStatsCRCErrors_Object = MibTableColumn
acdPortRxStatsCRCErrors = _AcdPortRxStatsCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 14),
    _AcdPortRxStatsCRCErrors_Type()
)
acdPortRxStatsCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsCRCErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsCRCErrors.setUnits("Packets")
_AcdPortRxStatsAlignErrors_Type = Counter64
_AcdPortRxStatsAlignErrors_Object = MibTableColumn
acdPortRxStatsAlignErrors = _AcdPortRxStatsAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 15),
    _AcdPortRxStatsAlignErrors_Type()
)
acdPortRxStatsAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsAlignErrors.setUnits("Packets")
_AcdPortRxStatsRuntFrames_Type = Counter64
_AcdPortRxStatsRuntFrames_Object = MibTableColumn
acdPortRxStatsRuntFrames = _AcdPortRxStatsRuntFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 16),
    _AcdPortRxStatsRuntFrames_Type()
)
acdPortRxStatsRuntFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsRuntFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsRuntFrames.setUnits("Packets")
_AcdPortRxStatsLengthErrors_Type = Counter64
_AcdPortRxStatsLengthErrors_Object = MibTableColumn
acdPortRxStatsLengthErrors = _AcdPortRxStatsLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 17),
    _AcdPortRxStatsLengthErrors_Type()
)
acdPortRxStatsLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsLengthErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsLengthErrors.setUnits("Packets")
_AcdPortRxStatsFalseCRS_Type = Counter64
_AcdPortRxStatsFalseCRS_Object = MibTableColumn
acdPortRxStatsFalseCRS = _AcdPortRxStatsFalseCRS_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 18),
    _AcdPortRxStatsFalseCRS_Type()
)
acdPortRxStatsFalseCRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsFalseCRS.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsFalseCRS.setUnits("Packets")
_AcdPortRxStatsPhyErrors_Type = Counter64
_AcdPortRxStatsPhyErrors_Object = MibTableColumn
acdPortRxStatsPhyErrors = _AcdPortRxStatsPhyErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 19),
    _AcdPortRxStatsPhyErrors_Type()
)
acdPortRxStatsPhyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPhyErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPhyErrors.setUnits("Packets")
_AcdPortRxStatsFifoErrors_Type = Counter64
_AcdPortRxStatsFifoErrors_Object = MibTableColumn
acdPortRxStatsFifoErrors = _AcdPortRxStatsFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 20),
    _AcdPortRxStatsFifoErrors_Type()
)
acdPortRxStatsFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsFifoErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsFifoErrors.setUnits("Packets")
_AcdPortRxStatsIgnored_Type = Counter64
_AcdPortRxStatsIgnored_Object = MibTableColumn
acdPortRxStatsIgnored = _AcdPortRxStatsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 21),
    _AcdPortRxStatsIgnored_Type()
)
acdPortRxStatsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsIgnored.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsIgnored.setUnits("Packets")
_AcdPortRxStatsBadOpcode_Type = Counter64
_AcdPortRxStatsBadOpcode_Object = MibTableColumn
acdPortRxStatsBadOpcode = _AcdPortRxStatsBadOpcode_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 22),
    _AcdPortRxStatsBadOpcode_Type()
)
acdPortRxStatsBadOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsBadOpcode.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsBadOpcode.setUnits("Packets")
_AcdPortRxStatsPkts64_Type = Counter64
_AcdPortRxStatsPkts64_Object = MibTableColumn
acdPortRxStatsPkts64 = _AcdPortRxStatsPkts64_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 23),
    _AcdPortRxStatsPkts64_Type()
)
acdPortRxStatsPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts64.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts64.setUnits("Packets")
_AcdPortRxStatsPkts65to127_Type = Counter64
_AcdPortRxStatsPkts65to127_Object = MibTableColumn
acdPortRxStatsPkts65to127 = _AcdPortRxStatsPkts65to127_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 24),
    _AcdPortRxStatsPkts65to127_Type()
)
acdPortRxStatsPkts65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts65to127.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts65to127.setUnits("Packets")
_AcdPortRxStatsPkts128to255_Type = Counter64
_AcdPortRxStatsPkts128to255_Object = MibTableColumn
acdPortRxStatsPkts128to255 = _AcdPortRxStatsPkts128to255_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 25),
    _AcdPortRxStatsPkts128to255_Type()
)
acdPortRxStatsPkts128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts128to255.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts128to255.setUnits("Packets")
_AcdPortRxStatsPkts256to511_Type = Counter64
_AcdPortRxStatsPkts256to511_Object = MibTableColumn
acdPortRxStatsPkts256to511 = _AcdPortRxStatsPkts256to511_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 26),
    _AcdPortRxStatsPkts256to511_Type()
)
acdPortRxStatsPkts256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts256to511.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts256to511.setUnits("Packets")
_AcdPortRxStatsPkts512to1023_Type = Counter64
_AcdPortRxStatsPkts512to1023_Object = MibTableColumn
acdPortRxStatsPkts512to1023 = _AcdPortRxStatsPkts512to1023_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 27),
    _AcdPortRxStatsPkts512to1023_Type()
)
acdPortRxStatsPkts512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts512to1023.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts512to1023.setUnits("Packets")
_AcdPortRxStatsPkts1024to1518_Type = Counter64
_AcdPortRxStatsPkts1024to1518_Object = MibTableColumn
acdPortRxStatsPkts1024to1518 = _AcdPortRxStatsPkts1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 28),
    _AcdPortRxStatsPkts1024to1518_Type()
)
acdPortRxStatsPkts1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts1024to1518.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts1024to1518.setUnits("Packets")
_AcdPortRxStatsPkts1519to2047_Type = Counter64
_AcdPortRxStatsPkts1519to2047_Object = MibTableColumn
acdPortRxStatsPkts1519to2047 = _AcdPortRxStatsPkts1519to2047_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 29),
    _AcdPortRxStatsPkts1519to2047_Type()
)
acdPortRxStatsPkts1519to2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts1519to2047.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts1519to2047.setUnits("Packets")
_AcdPortRxStatsPkts2048to4095_Type = Counter64
_AcdPortRxStatsPkts2048to4095_Object = MibTableColumn
acdPortRxStatsPkts2048to4095 = _AcdPortRxStatsPkts2048to4095_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 30),
    _AcdPortRxStatsPkts2048to4095_Type()
)
acdPortRxStatsPkts2048to4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts2048to4095.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts2048to4095.setUnits("Packets")
_AcdPortRxStatsPkts4096to8191_Type = Counter64
_AcdPortRxStatsPkts4096to8191_Object = MibTableColumn
acdPortRxStatsPkts4096to8191 = _AcdPortRxStatsPkts4096to8191_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 31),
    _AcdPortRxStatsPkts4096to8191_Type()
)
acdPortRxStatsPkts4096to8191.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts4096to8191.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts4096to8191.setUnits("Packets")
_AcdPortRxStatsPkts8192andMore_Type = Counter64
_AcdPortRxStatsPkts8192andMore_Object = MibTableColumn
acdPortRxStatsPkts8192andMore = _AcdPortRxStatsPkts8192andMore_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 32),
    _AcdPortRxStatsPkts8192andMore_Type()
)
acdPortRxStatsPkts8192andMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts8192andMore.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts8192andMore.setUnits("Packets")
_AcdPortRxStatsPktsLarge_Type = Counter64
_AcdPortRxStatsPktsLarge_Object = MibTableColumn
acdPortRxStatsPktsLarge = _AcdPortRxStatsPktsLarge_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 33),
    _AcdPortRxStatsPktsLarge_Type()
)
acdPortRxStatsPktsLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPktsLarge.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPktsLarge.setUnits("Packets")
_AcdPortRxL1Rate_Type = Gauge32
_AcdPortRxL1Rate_Object = MibTableColumn
acdPortRxL1Rate = _AcdPortRxL1Rate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 34),
    _AcdPortRxL1Rate_Type()
)
acdPortRxL1Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxL1Rate.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxL1Rate.setUnits("Mbps")
_AcdPortRxL1Percent_Type = Gauge32
_AcdPortRxL1Percent_Object = MibTableColumn
acdPortRxL1Percent = _AcdPortRxL1Percent_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 35),
    _AcdPortRxL1Percent_Type()
)
acdPortRxL1Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxL1Percent.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxL1Percent.setUnits("%")
_AcdPortRxL2Rate_Type = Gauge32
_AcdPortRxL2Rate_Object = MibTableColumn
acdPortRxL2Rate = _AcdPortRxL2Rate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 36),
    _AcdPortRxL2Rate_Type()
)
acdPortRxL2Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxL2Rate.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxL2Rate.setUnits("Mbps")


class _AcdPortRxStatsSupportBitsExt_Type(Bits):
    """Custom type acdPortRxStatsSupportBitsExt based on Bits"""
    namedValues = NamedValues(
        *(("bL1Rate", 0),
          ("bL1Percent", 1),
          ("bL2Rate", 2))
    )

_AcdPortRxStatsSupportBitsExt_Type.__name__ = "Bits"
_AcdPortRxStatsSupportBitsExt_Object = MibTableColumn
acdPortRxStatsSupportBitsExt = _AcdPortRxStatsSupportBitsExt_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 37),
    _AcdPortRxStatsSupportBitsExt_Type()
)
acdPortRxStatsSupportBitsExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsSupportBitsExt.setStatus("current")
_AcdPortStatsSumTable_Object = MibTable
acdPortStatsSumTable = _AcdPortStatsSumTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 3)
)
if mibBuilder.loadTexts:
    acdPortStatsSumTable.setStatus("current")
_AcdPortStatsSumEntry_Object = MibTableRow
acdPortStatsSumEntry = _AcdPortStatsSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 3, 1)
)
acdPortStatsSumEntry.setIndexNames(
    (0, "ACD-PORT-MIB", "acdPortStatsSumIndex"),
)
if mibBuilder.loadTexts:
    acdPortStatsSumEntry.setStatus("current")


class _AcdPortStatsSumIndex_Type(Unsigned32):
    """Custom type acdPortStatsSumIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdPortStatsSumIndex_Type.__name__ = "Unsigned32"
_AcdPortStatsSumIndex_Object = MibTableColumn
acdPortStatsSumIndex = _AcdPortStatsSumIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 3, 1, 1),
    _AcdPortStatsSumIndex_Type()
)
acdPortStatsSumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPortStatsSumIndex.setStatus("current")


class _AcdPortStatsSumName_Type(DisplayString):
    """Custom type acdPortStatsSumName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdPortStatsSumName_Type.__name__ = "DisplayString"
_AcdPortStatsSumName_Object = MibTableColumn
acdPortStatsSumName = _AcdPortStatsSumName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 3, 1, 2),
    _AcdPortStatsSumName_Type()
)
acdPortStatsSumName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatsSumName.setStatus("current")
_AcdPortStatsSumTXPkt_Type = Counter64
_AcdPortStatsSumTXPkt_Object = MibTableColumn
acdPortStatsSumTXPkt = _AcdPortStatsSumTXPkt_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 3, 1, 3),
    _AcdPortStatsSumTXPkt_Type()
)
acdPortStatsSumTXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatsSumTXPkt.setStatus("current")
if mibBuilder.loadTexts:
    acdPortStatsSumTXPkt.setUnits("Packets")
_AcdPortStatsSumTXErr_Type = Counter64
_AcdPortStatsSumTXErr_Object = MibTableColumn
acdPortStatsSumTXErr = _AcdPortStatsSumTXErr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 3, 1, 4),
    _AcdPortStatsSumTXErr_Type()
)
acdPortStatsSumTXErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatsSumTXErr.setStatus("current")
if mibBuilder.loadTexts:
    acdPortStatsSumTXErr.setUnits("Packets")
_AcdPortStatsSumRXPkt_Type = Counter64
_AcdPortStatsSumRXPkt_Object = MibTableColumn
acdPortStatsSumRXPkt = _AcdPortStatsSumRXPkt_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 3, 1, 5),
    _AcdPortStatsSumRXPkt_Type()
)
acdPortStatsSumRXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatsSumRXPkt.setStatus("current")
if mibBuilder.loadTexts:
    acdPortStatsSumRXPkt.setUnits("Packets")
_AcdPortStatsSumRXErr_Type = Counter64
_AcdPortStatsSumRXErr_Object = MibTableColumn
acdPortStatsSumRXErr = _AcdPortStatsSumRXErr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 3, 1, 6),
    _AcdPortStatsSumRXErr_Type()
)
acdPortStatsSumRXErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatsSumRXErr.setStatus("current")
if mibBuilder.loadTexts:
    acdPortStatsSumRXErr.setUnits("Packets")
_AcdPortTableTid_ObjectIdentity = ObjectIdentity
acdPortTableTid = _AcdPortTableTid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 4)
)
_AcdPortConfigTableLastChangeTid_Type = Unsigned32
_AcdPortConfigTableLastChangeTid_Object = MibScalar
acdPortConfigTableLastChangeTid = _AcdPortConfigTableLastChangeTid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 4, 1),
    _AcdPortConfigTableLastChangeTid_Type()
)
acdPortConfigTableLastChangeTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortConfigTableLastChangeTid.setStatus("current")
_AcdPortHistStats_ObjectIdentity = ObjectIdentity
acdPortHistStats = _AcdPortHistStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5)
)
_AcdPortTxHistStatsTable_Object = MibTable
acdPortTxHistStatsTable = _AcdPortTxHistStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1)
)
if mibBuilder.loadTexts:
    acdPortTxHistStatsTable.setStatus("current")
_AcdPortTxHistStatsEntry_Object = MibTableRow
acdPortTxHistStatsEntry = _AcdPortTxHistStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1)
)
acdPortTxHistStatsEntry.setIndexNames(
    (0, "ACD-PORT-MIB", "acdPortTxHistStatsIndex"),
    (0, "ACD-PORT-MIB", "acdPortTxHistStatsSampleIndex"),
)
if mibBuilder.loadTexts:
    acdPortTxHistStatsEntry.setStatus("current")


class _AcdPortTxHistStatsIndex_Type(Unsigned32):
    """Custom type acdPortTxHistStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdPortTxHistStatsIndex_Type.__name__ = "Unsigned32"
_AcdPortTxHistStatsIndex_Object = MibTableColumn
acdPortTxHistStatsIndex = _AcdPortTxHistStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 1),
    _AcdPortTxHistStatsIndex_Type()
)
acdPortTxHistStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsIndex.setStatus("current")
_AcdPortTxHistStatsSampleIndex_Type = Unsigned32
_AcdPortTxHistStatsSampleIndex_Object = MibTableColumn
acdPortTxHistStatsSampleIndex = _AcdPortTxHistStatsSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 2),
    _AcdPortTxHistStatsSampleIndex_Type()
)
acdPortTxHistStatsSampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsSampleIndex.setStatus("current")


class _AcdPortTxHistStatsStatus_Type(Integer32):
    """Custom type acdPortTxHistStatsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_AcdPortTxHistStatsStatus_Type.__name__ = "Integer32"
_AcdPortTxHistStatsStatus_Object = MibTableColumn
acdPortTxHistStatsStatus = _AcdPortTxHistStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 3),
    _AcdPortTxHistStatsStatus_Type()
)
acdPortTxHistStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsStatus.setStatus("current")
_AcdPortTxHistStatsDuration_Type = Unsigned32
_AcdPortTxHistStatsDuration_Object = MibTableColumn
acdPortTxHistStatsDuration = _AcdPortTxHistStatsDuration_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 4),
    _AcdPortTxHistStatsDuration_Type()
)
acdPortTxHistStatsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsDuration.setStatus("current")
_AcdPortTxHistStatsIntervalEnd_Type = DateAndTime
_AcdPortTxHistStatsIntervalEnd_Object = MibTableColumn
acdPortTxHistStatsIntervalEnd = _AcdPortTxHistStatsIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 5),
    _AcdPortTxHistStatsIntervalEnd_Type()
)
acdPortTxHistStatsIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsIntervalEnd.setStatus("current")


class _AcdPortTxHistStatsSupportBits_Type(Bits):
    """Custom type acdPortTxHistStatsSupportBits based on Bits"""
    namedValues = NamedValues(
        *(("bBytesGood", 0),
          ("bBytesTotal", 1),
          ("bUnicastPkts", 2),
          ("bMulticastPkts", 3),
          ("bBroadcastPkts", 4),
          ("bPauseFrames", 5),
          ("bTaggedFrames", 6),
          ("bCRCErrors", 7),
          ("bDeferred", 8),
          ("bExcessiveDeferrals", 9),
          ("bSingleCollisions", 10),
          ("bMultipleCollisions", 11),
          ("bExcessiveCollisions", 12),
          ("bLateCollisions", 13),
          ("bNormalCollisions", 14),
          ("bFifoErrors", 15),
          ("bPkts64", 16),
          ("bPkts65to127", 17),
          ("bPkts128to255", 18),
          ("bPkts256to511", 19),
          ("bPkts512to1023", 20),
          ("bPkts1024to1518", 21),
          ("bPkts1519to2047", 22),
          ("bPkts2048to4095", 23),
          ("bPkts4096to8191", 24),
          ("bPkts8192andMore", 25),
          ("bPktsLarge", 26),
          ("bL1Rate", 27),
          ("bL1Percent", 28),
          ("bL2Rate", 29))
    )

_AcdPortTxHistStatsSupportBits_Type.__name__ = "Bits"
_AcdPortTxHistStatsSupportBits_Object = MibTableColumn
acdPortTxHistStatsSupportBits = _AcdPortTxHistStatsSupportBits_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 6),
    _AcdPortTxHistStatsSupportBits_Type()
)
acdPortTxHistStatsSupportBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsSupportBits.setStatus("current")
_AcdPortTxHistStatsBytesGood_Type = Counter64
_AcdPortTxHistStatsBytesGood_Object = MibTableColumn
acdPortTxHistStatsBytesGood = _AcdPortTxHistStatsBytesGood_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 7),
    _AcdPortTxHistStatsBytesGood_Type()
)
acdPortTxHistStatsBytesGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsBytesGood.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsBytesGood.setUnits("Octets")
_AcdPortTxHistStatsBytesTotal_Type = Counter64
_AcdPortTxHistStatsBytesTotal_Object = MibTableColumn
acdPortTxHistStatsBytesTotal = _AcdPortTxHistStatsBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 8),
    _AcdPortTxHistStatsBytesTotal_Type()
)
acdPortTxHistStatsBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsBytesTotal.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsBytesTotal.setUnits("Octets")
_AcdPortTxHistStatsUnicastPkts_Type = Counter64
_AcdPortTxHistStatsUnicastPkts_Object = MibTableColumn
acdPortTxHistStatsUnicastPkts = _AcdPortTxHistStatsUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 9),
    _AcdPortTxHistStatsUnicastPkts_Type()
)
acdPortTxHistStatsUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsUnicastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsUnicastPkts.setUnits("Packets")
_AcdPortTxHistStatsMulticastPkts_Type = Counter64
_AcdPortTxHistStatsMulticastPkts_Object = MibTableColumn
acdPortTxHistStatsMulticastPkts = _AcdPortTxHistStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 10),
    _AcdPortTxHistStatsMulticastPkts_Type()
)
acdPortTxHistStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsMulticastPkts.setUnits("Packets")
_AcdPortTxHistStatsBroadcastPkts_Type = Counter64
_AcdPortTxHistStatsBroadcastPkts_Object = MibTableColumn
acdPortTxHistStatsBroadcastPkts = _AcdPortTxHistStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 11),
    _AcdPortTxHistStatsBroadcastPkts_Type()
)
acdPortTxHistStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsBroadcastPkts.setUnits("Packets")
_AcdPortTxHistStatsPauseFrames_Type = Counter64
_AcdPortTxHistStatsPauseFrames_Object = MibTableColumn
acdPortTxHistStatsPauseFrames = _AcdPortTxHistStatsPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 12),
    _AcdPortTxHistStatsPauseFrames_Type()
)
acdPortTxHistStatsPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPauseFrames.setUnits("Packets")
_AcdPortTxHistStatsTaggedFrames_Type = Counter64
_AcdPortTxHistStatsTaggedFrames_Object = MibTableColumn
acdPortTxHistStatsTaggedFrames = _AcdPortTxHistStatsTaggedFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 13),
    _AcdPortTxHistStatsTaggedFrames_Type()
)
acdPortTxHistStatsTaggedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsTaggedFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsTaggedFrames.setUnits("Packets")
_AcdPortTxHistStatsCRCErrors_Type = Counter64
_AcdPortTxHistStatsCRCErrors_Object = MibTableColumn
acdPortTxHistStatsCRCErrors = _AcdPortTxHistStatsCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 14),
    _AcdPortTxHistStatsCRCErrors_Type()
)
acdPortTxHistStatsCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsCRCErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsCRCErrors.setUnits("Packets")
_AcdPortTxHistStatsDeferred_Type = Counter64
_AcdPortTxHistStatsDeferred_Object = MibTableColumn
acdPortTxHistStatsDeferred = _AcdPortTxHistStatsDeferred_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 15),
    _AcdPortTxHistStatsDeferred_Type()
)
acdPortTxHistStatsDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsDeferred.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsDeferred.setUnits("Packets")
_AcdPortTxHistStatsExcessiveDeferrals_Type = Counter64
_AcdPortTxHistStatsExcessiveDeferrals_Object = MibTableColumn
acdPortTxHistStatsExcessiveDeferrals = _AcdPortTxHistStatsExcessiveDeferrals_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 16),
    _AcdPortTxHistStatsExcessiveDeferrals_Type()
)
acdPortTxHistStatsExcessiveDeferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsExcessiveDeferrals.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsExcessiveDeferrals.setUnits("Packets")
_AcdPortTxHistStatsSingleCollisions_Type = Counter64
_AcdPortTxHistStatsSingleCollisions_Object = MibTableColumn
acdPortTxHistStatsSingleCollisions = _AcdPortTxHistStatsSingleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 17),
    _AcdPortTxHistStatsSingleCollisions_Type()
)
acdPortTxHistStatsSingleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsSingleCollisions.setStatus("current")
_AcdPortTxHistStatsMultipleCollisions_Type = Counter64
_AcdPortTxHistStatsMultipleCollisions_Object = MibTableColumn
acdPortTxHistStatsMultipleCollisions = _AcdPortTxHistStatsMultipleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 18),
    _AcdPortTxHistStatsMultipleCollisions_Type()
)
acdPortTxHistStatsMultipleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsMultipleCollisions.setStatus("current")
_AcdPortTxHistStatsExcessiveCollisions_Type = Counter64
_AcdPortTxHistStatsExcessiveCollisions_Object = MibTableColumn
acdPortTxHistStatsExcessiveCollisions = _AcdPortTxHistStatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 19),
    _AcdPortTxHistStatsExcessiveCollisions_Type()
)
acdPortTxHistStatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsExcessiveCollisions.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsExcessiveCollisions.setUnits("Packets")
_AcdPortTxHistStatsLateCollisions_Type = Counter64
_AcdPortTxHistStatsLateCollisions_Object = MibTableColumn
acdPortTxHistStatsLateCollisions = _AcdPortTxHistStatsLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 20),
    _AcdPortTxHistStatsLateCollisions_Type()
)
acdPortTxHistStatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsLateCollisions.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsLateCollisions.setUnits("Packets")
_AcdPortTxHistStatsNormalCollisions_Type = Counter64
_AcdPortTxHistStatsNormalCollisions_Object = MibTableColumn
acdPortTxHistStatsNormalCollisions = _AcdPortTxHistStatsNormalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 21),
    _AcdPortTxHistStatsNormalCollisions_Type()
)
acdPortTxHistStatsNormalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsNormalCollisions.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsNormalCollisions.setUnits("Packets")
_AcdPortTxHistStatsFifoErrors_Type = Counter64
_AcdPortTxHistStatsFifoErrors_Object = MibTableColumn
acdPortTxHistStatsFifoErrors = _AcdPortTxHistStatsFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 22),
    _AcdPortTxHistStatsFifoErrors_Type()
)
acdPortTxHistStatsFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsFifoErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsFifoErrors.setUnits("Packets")
_AcdPortTxHistStatsPkts64_Type = Counter64
_AcdPortTxHistStatsPkts64_Object = MibTableColumn
acdPortTxHistStatsPkts64 = _AcdPortTxHistStatsPkts64_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 23),
    _AcdPortTxHistStatsPkts64_Type()
)
acdPortTxHistStatsPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts64.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts64.setUnits("Packets")
_AcdPortTxHistStatsPkts65to127_Type = Counter64
_AcdPortTxHistStatsPkts65to127_Object = MibTableColumn
acdPortTxHistStatsPkts65to127 = _AcdPortTxHistStatsPkts65to127_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 24),
    _AcdPortTxHistStatsPkts65to127_Type()
)
acdPortTxHistStatsPkts65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts65to127.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts65to127.setUnits("Packets")
_AcdPortTxHistStatsPkts128to255_Type = Counter64
_AcdPortTxHistStatsPkts128to255_Object = MibTableColumn
acdPortTxHistStatsPkts128to255 = _AcdPortTxHistStatsPkts128to255_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 25),
    _AcdPortTxHistStatsPkts128to255_Type()
)
acdPortTxHistStatsPkts128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts128to255.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts128to255.setUnits("Packets")
_AcdPortTxHistStatsPkts256to511_Type = Counter64
_AcdPortTxHistStatsPkts256to511_Object = MibTableColumn
acdPortTxHistStatsPkts256to511 = _AcdPortTxHistStatsPkts256to511_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 26),
    _AcdPortTxHistStatsPkts256to511_Type()
)
acdPortTxHistStatsPkts256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts256to511.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts256to511.setUnits("Packets")
_AcdPortTxHistStatsPkts512to1023_Type = Counter64
_AcdPortTxHistStatsPkts512to1023_Object = MibTableColumn
acdPortTxHistStatsPkts512to1023 = _AcdPortTxHistStatsPkts512to1023_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 27),
    _AcdPortTxHistStatsPkts512to1023_Type()
)
acdPortTxHistStatsPkts512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts512to1023.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts512to1023.setUnits("Packets")
_AcdPortTxHistStatsPkts1024to1518_Type = Counter64
_AcdPortTxHistStatsPkts1024to1518_Object = MibTableColumn
acdPortTxHistStatsPkts1024to1518 = _AcdPortTxHistStatsPkts1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 28),
    _AcdPortTxHistStatsPkts1024to1518_Type()
)
acdPortTxHistStatsPkts1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts1024to1518.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts1024to1518.setUnits("Packets")
_AcdPortTxHistStatsPkts1519to2047_Type = Counter64
_AcdPortTxHistStatsPkts1519to2047_Object = MibTableColumn
acdPortTxHistStatsPkts1519to2047 = _AcdPortTxHistStatsPkts1519to2047_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 29),
    _AcdPortTxHistStatsPkts1519to2047_Type()
)
acdPortTxHistStatsPkts1519to2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts1519to2047.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts1519to2047.setUnits("Packets")
_AcdPortTxHistStatsPkts2048to4095_Type = Counter64
_AcdPortTxHistStatsPkts2048to4095_Object = MibTableColumn
acdPortTxHistStatsPkts2048to4095 = _AcdPortTxHistStatsPkts2048to4095_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 30),
    _AcdPortTxHistStatsPkts2048to4095_Type()
)
acdPortTxHistStatsPkts2048to4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts2048to4095.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts2048to4095.setUnits("Packets")
_AcdPortTxHistStatsPkts4096to8191_Type = Counter64
_AcdPortTxHistStatsPkts4096to8191_Object = MibTableColumn
acdPortTxHistStatsPkts4096to8191 = _AcdPortTxHistStatsPkts4096to8191_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 31),
    _AcdPortTxHistStatsPkts4096to8191_Type()
)
acdPortTxHistStatsPkts4096to8191.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts4096to8191.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts4096to8191.setUnits("Packets")
_AcdPortTxHistStatsPkts8192andMore_Type = Counter64
_AcdPortTxHistStatsPkts8192andMore_Object = MibTableColumn
acdPortTxHistStatsPkts8192andMore = _AcdPortTxHistStatsPkts8192andMore_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 32),
    _AcdPortTxHistStatsPkts8192andMore_Type()
)
acdPortTxHistStatsPkts8192andMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts8192andMore.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPkts8192andMore.setUnits("Packets")
_AcdPortTxHistStatsPktsLarge_Type = Counter64
_AcdPortTxHistStatsPktsLarge_Object = MibTableColumn
acdPortTxHistStatsPktsLarge = _AcdPortTxHistStatsPktsLarge_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 33),
    _AcdPortTxHistStatsPktsLarge_Type()
)
acdPortTxHistStatsPktsLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPktsLarge.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPktsLarge.setUnits("Packets")
_AcdPortTxHistStatsPackets_Type = Counter64
_AcdPortTxHistStatsPackets_Object = MibTableColumn
acdPortTxHistStatsPackets = _AcdPortTxHistStatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 34),
    _AcdPortTxHistStatsPackets_Type()
)
acdPortTxHistStatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPackets.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPackets.setUnits("Packets")
_AcdPortTxHistStatsPktsErrors_Type = Counter64
_AcdPortTxHistStatsPktsErrors_Object = MibTableColumn
acdPortTxHistStatsPktsErrors = _AcdPortTxHistStatsPktsErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 35),
    _AcdPortTxHistStatsPktsErrors_Type()
)
acdPortTxHistStatsPktsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPktsErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistStatsPktsErrors.setUnits("Packets")
_AcdPortTxHistL1Rate_Type = Gauge32
_AcdPortTxHistL1Rate_Object = MibTableColumn
acdPortTxHistL1Rate = _AcdPortTxHistL1Rate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 36),
    _AcdPortTxHistL1Rate_Type()
)
acdPortTxHistL1Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistL1Rate.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistL1Rate.setUnits("Mbps")
_AcdPortTxHistL1Percent_Type = Gauge32
_AcdPortTxHistL1Percent_Object = MibTableColumn
acdPortTxHistL1Percent = _AcdPortTxHistL1Percent_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 37),
    _AcdPortTxHistL1Percent_Type()
)
acdPortTxHistL1Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistL1Percent.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistL1Percent.setUnits("%")
_AcdPortTxHistL2Rate_Type = Gauge32
_AcdPortTxHistL2Rate_Object = MibTableColumn
acdPortTxHistL2Rate = _AcdPortTxHistL2Rate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 1, 1, 38),
    _AcdPortTxHistL2Rate_Type()
)
acdPortTxHistL2Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxHistL2Rate.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxHistL2Rate.setUnits("Mbps")
_AcdPortRxHistStatsTable_Object = MibTable
acdPortRxHistStatsTable = _AcdPortRxHistStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2)
)
if mibBuilder.loadTexts:
    acdPortRxHistStatsTable.setStatus("current")
_AcdPortRxHistStatsEntry_Object = MibTableRow
acdPortRxHistStatsEntry = _AcdPortRxHistStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1)
)
acdPortRxHistStatsEntry.setIndexNames(
    (0, "ACD-PORT-MIB", "acdPortRxHistStatsIndex"),
    (0, "ACD-PORT-MIB", "acdPortRxHistStatsSampleIndex"),
)
if mibBuilder.loadTexts:
    acdPortRxHistStatsEntry.setStatus("current")


class _AcdPortRxHistStatsIndex_Type(Unsigned32):
    """Custom type acdPortRxHistStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdPortRxHistStatsIndex_Type.__name__ = "Unsigned32"
_AcdPortRxHistStatsIndex_Object = MibTableColumn
acdPortRxHistStatsIndex = _AcdPortRxHistStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 1),
    _AcdPortRxHistStatsIndex_Type()
)
acdPortRxHistStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsIndex.setStatus("current")
_AcdPortRxHistStatsSampleIndex_Type = Unsigned32
_AcdPortRxHistStatsSampleIndex_Object = MibTableColumn
acdPortRxHistStatsSampleIndex = _AcdPortRxHistStatsSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 2),
    _AcdPortRxHistStatsSampleIndex_Type()
)
acdPortRxHistStatsSampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsSampleIndex.setStatus("current")


class _AcdPortRxHistStatsStatus_Type(Integer32):
    """Custom type acdPortRxHistStatsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_AcdPortRxHistStatsStatus_Type.__name__ = "Integer32"
_AcdPortRxHistStatsStatus_Object = MibTableColumn
acdPortRxHistStatsStatus = _AcdPortRxHistStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 3),
    _AcdPortRxHistStatsStatus_Type()
)
acdPortRxHistStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsStatus.setStatus("current")
_AcdPortRxHistStatsDuration_Type = Unsigned32
_AcdPortRxHistStatsDuration_Object = MibTableColumn
acdPortRxHistStatsDuration = _AcdPortRxHistStatsDuration_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 4),
    _AcdPortRxHistStatsDuration_Type()
)
acdPortRxHistStatsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsDuration.setStatus("current")
_AcdPortRxHistStatsIntervalEnd_Type = DateAndTime
_AcdPortRxHistStatsIntervalEnd_Object = MibTableColumn
acdPortRxHistStatsIntervalEnd = _AcdPortRxHistStatsIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 5),
    _AcdPortRxHistStatsIntervalEnd_Type()
)
acdPortRxHistStatsIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsIntervalEnd.setStatus("current")


class _AcdPortRxHistStatsSupportBits_Type(Bits):
    """Custom type acdPortRxHistStatsSupportBits based on Bits"""
    namedValues = NamedValues(
        *(("bBytesGood", 0),
          ("bBytesTotal", 1),
          ("bRxStatsShortOk", 2),
          ("bRxStatsShortBad", 3),
          ("bRxStatsLongOk", 4),
          ("bRxStatsLongBad", 5),
          ("bUnicastPkts", 6),
          ("bMulticastPkts", 7),
          ("bBroadcastPkts", 8),
          ("bPauseFrames", 9),
          ("bTaggedFrames", 10),
          ("bCRCErrors", 11),
          ("bAlignErrors", 12),
          ("bRuntFrames", 13),
          ("bLengthErrors", 14),
          ("bFalseCRS", 15),
          ("bPhyErrors", 16),
          ("bFifoErrors", 17),
          ("bIgnored", 18),
          ("bBadOpcode", 19),
          ("bPkts64", 20),
          ("bPkts65to127", 21),
          ("bPkts128to255", 22),
          ("bPkts256to511", 23),
          ("bPkts512to1023", 24),
          ("bPkts1024to1518", 25),
          ("bPkts1519to2047", 26),
          ("bPkts2048to4095", 27),
          ("bPkts4096to8191", 28),
          ("bPkts8192andMore", 29),
          ("bPktsLarge", 30))
    )

_AcdPortRxHistStatsSupportBits_Type.__name__ = "Bits"
_AcdPortRxHistStatsSupportBits_Object = MibTableColumn
acdPortRxHistStatsSupportBits = _AcdPortRxHistStatsSupportBits_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 6),
    _AcdPortRxHistStatsSupportBits_Type()
)
acdPortRxHistStatsSupportBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsSupportBits.setStatus("current")
_AcdPortRxHistStatsBytesGood_Type = Counter64
_AcdPortRxHistStatsBytesGood_Object = MibTableColumn
acdPortRxHistStatsBytesGood = _AcdPortRxHistStatsBytesGood_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 7),
    _AcdPortRxHistStatsBytesGood_Type()
)
acdPortRxHistStatsBytesGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsBytesGood.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsBytesGood.setUnits("Octets")
_AcdPortRxHistStatsBytesTotal_Type = Counter64
_AcdPortRxHistStatsBytesTotal_Object = MibTableColumn
acdPortRxHistStatsBytesTotal = _AcdPortRxHistStatsBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 8),
    _AcdPortRxHistStatsBytesTotal_Type()
)
acdPortRxHistStatsBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsBytesTotal.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsBytesTotal.setUnits("Octets")
_AcdPortRxHistStatsShortOk_Type = Counter64
_AcdPortRxHistStatsShortOk_Object = MibTableColumn
acdPortRxHistStatsShortOk = _AcdPortRxHistStatsShortOk_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 9),
    _AcdPortRxHistStatsShortOk_Type()
)
acdPortRxHistStatsShortOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsShortOk.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsShortOk.setUnits("Packets")
_AcdPortRxHistStatsShortBad_Type = Counter64
_AcdPortRxHistStatsShortBad_Object = MibTableColumn
acdPortRxHistStatsShortBad = _AcdPortRxHistStatsShortBad_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 10),
    _AcdPortRxHistStatsShortBad_Type()
)
acdPortRxHistStatsShortBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsShortBad.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsShortBad.setUnits("Packets")
_AcdPortRxHistStatsLongOk_Type = Counter64
_AcdPortRxHistStatsLongOk_Object = MibTableColumn
acdPortRxHistStatsLongOk = _AcdPortRxHistStatsLongOk_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 11),
    _AcdPortRxHistStatsLongOk_Type()
)
acdPortRxHistStatsLongOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsLongOk.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsLongOk.setUnits("Packets")
_AcdPortRxHistStatsLongBad_Type = Counter64
_AcdPortRxHistStatsLongBad_Object = MibTableColumn
acdPortRxHistStatsLongBad = _AcdPortRxHistStatsLongBad_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 12),
    _AcdPortRxHistStatsLongBad_Type()
)
acdPortRxHistStatsLongBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsLongBad.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsLongBad.setUnits("Packets")
_AcdPortRxHistStatsUnicastPkts_Type = Counter64
_AcdPortRxHistStatsUnicastPkts_Object = MibTableColumn
acdPortRxHistStatsUnicastPkts = _AcdPortRxHistStatsUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 13),
    _AcdPortRxHistStatsUnicastPkts_Type()
)
acdPortRxHistStatsUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsUnicastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsUnicastPkts.setUnits("Packets")
_AcdPortRxHistStatsMulticastPkts_Type = Counter64
_AcdPortRxHistStatsMulticastPkts_Object = MibTableColumn
acdPortRxHistStatsMulticastPkts = _AcdPortRxHistStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 14),
    _AcdPortRxHistStatsMulticastPkts_Type()
)
acdPortRxHistStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsMulticastPkts.setUnits("Packets")
_AcdPortRxHistStatsBroadcastPkts_Type = Counter64
_AcdPortRxHistStatsBroadcastPkts_Object = MibTableColumn
acdPortRxHistStatsBroadcastPkts = _AcdPortRxHistStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 15),
    _AcdPortRxHistStatsBroadcastPkts_Type()
)
acdPortRxHistStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsBroadcastPkts.setUnits("Packets")
_AcdPortRxHistStatsPauseFrames_Type = Counter64
_AcdPortRxHistStatsPauseFrames_Object = MibTableColumn
acdPortRxHistStatsPauseFrames = _AcdPortRxHistStatsPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 16),
    _AcdPortRxHistStatsPauseFrames_Type()
)
acdPortRxHistStatsPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPauseFrames.setUnits("Packets")
_AcdPortRxHistStatsTaggedFrames_Type = Counter64
_AcdPortRxHistStatsTaggedFrames_Object = MibTableColumn
acdPortRxHistStatsTaggedFrames = _AcdPortRxHistStatsTaggedFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 17),
    _AcdPortRxHistStatsTaggedFrames_Type()
)
acdPortRxHistStatsTaggedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsTaggedFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsTaggedFrames.setUnits("Packets")
_AcdPortRxHistStatsCRCErrors_Type = Counter64
_AcdPortRxHistStatsCRCErrors_Object = MibTableColumn
acdPortRxHistStatsCRCErrors = _AcdPortRxHistStatsCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 18),
    _AcdPortRxHistStatsCRCErrors_Type()
)
acdPortRxHistStatsCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsCRCErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsCRCErrors.setUnits("Packets")
_AcdPortRxHistStatsAlignErrors_Type = Counter64
_AcdPortRxHistStatsAlignErrors_Object = MibTableColumn
acdPortRxHistStatsAlignErrors = _AcdPortRxHistStatsAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 19),
    _AcdPortRxHistStatsAlignErrors_Type()
)
acdPortRxHistStatsAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsAlignErrors.setUnits("Packets")
_AcdPortRxHistStatsRuntFrames_Type = Counter64
_AcdPortRxHistStatsRuntFrames_Object = MibTableColumn
acdPortRxHistStatsRuntFrames = _AcdPortRxHistStatsRuntFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 20),
    _AcdPortRxHistStatsRuntFrames_Type()
)
acdPortRxHistStatsRuntFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsRuntFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsRuntFrames.setUnits("Packets")
_AcdPortRxHistStatsLengthErrors_Type = Counter64
_AcdPortRxHistStatsLengthErrors_Object = MibTableColumn
acdPortRxHistStatsLengthErrors = _AcdPortRxHistStatsLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 21),
    _AcdPortRxHistStatsLengthErrors_Type()
)
acdPortRxHistStatsLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsLengthErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsLengthErrors.setUnits("Packets")
_AcdPortRxHistStatsFalseCRS_Type = Counter64
_AcdPortRxHistStatsFalseCRS_Object = MibTableColumn
acdPortRxHistStatsFalseCRS = _AcdPortRxHistStatsFalseCRS_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 22),
    _AcdPortRxHistStatsFalseCRS_Type()
)
acdPortRxHistStatsFalseCRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsFalseCRS.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsFalseCRS.setUnits("Packets")
_AcdPortRxHistStatsPhyErrors_Type = Counter64
_AcdPortRxHistStatsPhyErrors_Object = MibTableColumn
acdPortRxHistStatsPhyErrors = _AcdPortRxHistStatsPhyErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 23),
    _AcdPortRxHistStatsPhyErrors_Type()
)
acdPortRxHistStatsPhyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPhyErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPhyErrors.setUnits("Packets")
_AcdPortRxHistStatsFifoErrors_Type = Counter64
_AcdPortRxHistStatsFifoErrors_Object = MibTableColumn
acdPortRxHistStatsFifoErrors = _AcdPortRxHistStatsFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 24),
    _AcdPortRxHistStatsFifoErrors_Type()
)
acdPortRxHistStatsFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsFifoErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsFifoErrors.setUnits("Packets")
_AcdPortRxHistStatsIgnored_Type = Counter64
_AcdPortRxHistStatsIgnored_Object = MibTableColumn
acdPortRxHistStatsIgnored = _AcdPortRxHistStatsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 25),
    _AcdPortRxHistStatsIgnored_Type()
)
acdPortRxHistStatsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsIgnored.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsIgnored.setUnits("Packets")
_AcdPortRxHistStatsBadOpcode_Type = Counter64
_AcdPortRxHistStatsBadOpcode_Object = MibTableColumn
acdPortRxHistStatsBadOpcode = _AcdPortRxHistStatsBadOpcode_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 26),
    _AcdPortRxHistStatsBadOpcode_Type()
)
acdPortRxHistStatsBadOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsBadOpcode.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsBadOpcode.setUnits("Packets")
_AcdPortRxHistStatsPkts64_Type = Counter64
_AcdPortRxHistStatsPkts64_Object = MibTableColumn
acdPortRxHistStatsPkts64 = _AcdPortRxHistStatsPkts64_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 27),
    _AcdPortRxHistStatsPkts64_Type()
)
acdPortRxHistStatsPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts64.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts64.setUnits("Packets")
_AcdPortRxHistStatsPkts65to127_Type = Counter64
_AcdPortRxHistStatsPkts65to127_Object = MibTableColumn
acdPortRxHistStatsPkts65to127 = _AcdPortRxHistStatsPkts65to127_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 28),
    _AcdPortRxHistStatsPkts65to127_Type()
)
acdPortRxHistStatsPkts65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts65to127.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts65to127.setUnits("Packets")
_AcdPortRxHistStatsPkts128to255_Type = Counter64
_AcdPortRxHistStatsPkts128to255_Object = MibTableColumn
acdPortRxHistStatsPkts128to255 = _AcdPortRxHistStatsPkts128to255_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 29),
    _AcdPortRxHistStatsPkts128to255_Type()
)
acdPortRxHistStatsPkts128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts128to255.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts128to255.setUnits("Packets")
_AcdPortRxHistStatsPkts256to511_Type = Counter64
_AcdPortRxHistStatsPkts256to511_Object = MibTableColumn
acdPortRxHistStatsPkts256to511 = _AcdPortRxHistStatsPkts256to511_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 30),
    _AcdPortRxHistStatsPkts256to511_Type()
)
acdPortRxHistStatsPkts256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts256to511.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts256to511.setUnits("Packets")
_AcdPortRxHistStatsPkts512to1023_Type = Counter64
_AcdPortRxHistStatsPkts512to1023_Object = MibTableColumn
acdPortRxHistStatsPkts512to1023 = _AcdPortRxHistStatsPkts512to1023_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 31),
    _AcdPortRxHistStatsPkts512to1023_Type()
)
acdPortRxHistStatsPkts512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts512to1023.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts512to1023.setUnits("Packets")
_AcdPortRxHistStatsPkts1024to1518_Type = Counter64
_AcdPortRxHistStatsPkts1024to1518_Object = MibTableColumn
acdPortRxHistStatsPkts1024to1518 = _AcdPortRxHistStatsPkts1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 32),
    _AcdPortRxHistStatsPkts1024to1518_Type()
)
acdPortRxHistStatsPkts1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts1024to1518.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts1024to1518.setUnits("Packets")
_AcdPortRxHistStatsPkts1519to2047_Type = Counter64
_AcdPortRxHistStatsPkts1519to2047_Object = MibTableColumn
acdPortRxHistStatsPkts1519to2047 = _AcdPortRxHistStatsPkts1519to2047_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 33),
    _AcdPortRxHistStatsPkts1519to2047_Type()
)
acdPortRxHistStatsPkts1519to2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts1519to2047.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts1519to2047.setUnits("Packets")
_AcdPortRxHistStatsPkts2048to4095_Type = Counter64
_AcdPortRxHistStatsPkts2048to4095_Object = MibTableColumn
acdPortRxHistStatsPkts2048to4095 = _AcdPortRxHistStatsPkts2048to4095_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 34),
    _AcdPortRxHistStatsPkts2048to4095_Type()
)
acdPortRxHistStatsPkts2048to4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts2048to4095.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts2048to4095.setUnits("Packets")
_AcdPortRxHistStatsPkts4096to8191_Type = Counter64
_AcdPortRxHistStatsPkts4096to8191_Object = MibTableColumn
acdPortRxHistStatsPkts4096to8191 = _AcdPortRxHistStatsPkts4096to8191_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 35),
    _AcdPortRxHistStatsPkts4096to8191_Type()
)
acdPortRxHistStatsPkts4096to8191.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts4096to8191.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts4096to8191.setUnits("Packets")
_AcdPortRxHistStatsPkts8192andMore_Type = Counter64
_AcdPortRxHistStatsPkts8192andMore_Object = MibTableColumn
acdPortRxHistStatsPkts8192andMore = _AcdPortRxHistStatsPkts8192andMore_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 36),
    _AcdPortRxHistStatsPkts8192andMore_Type()
)
acdPortRxHistStatsPkts8192andMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts8192andMore.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPkts8192andMore.setUnits("Packets")
_AcdPortRxHistStatsPktsLarge_Type = Counter64
_AcdPortRxHistStatsPktsLarge_Object = MibTableColumn
acdPortRxHistStatsPktsLarge = _AcdPortRxHistStatsPktsLarge_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 37),
    _AcdPortRxHistStatsPktsLarge_Type()
)
acdPortRxHistStatsPktsLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPktsLarge.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPktsLarge.setUnits("Packets")
_AcdPortRxHistStatsPackets_Type = Counter64
_AcdPortRxHistStatsPackets_Object = MibTableColumn
acdPortRxHistStatsPackets = _AcdPortRxHistStatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 38),
    _AcdPortRxHistStatsPackets_Type()
)
acdPortRxHistStatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPackets.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPackets.setUnits("Packets")
_AcdPortRxHistStatsPktsErrors_Type = Counter64
_AcdPortRxHistStatsPktsErrors_Object = MibTableColumn
acdPortRxHistStatsPktsErrors = _AcdPortRxHistStatsPktsErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 39),
    _AcdPortRxHistStatsPktsErrors_Type()
)
acdPortRxHistStatsPktsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPktsErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistStatsPktsErrors.setUnits("Packets")
_AcdPortRxHistL1Rate_Type = Gauge32
_AcdPortRxHistL1Rate_Object = MibTableColumn
acdPortRxHistL1Rate = _AcdPortRxHistL1Rate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 40),
    _AcdPortRxHistL1Rate_Type()
)
acdPortRxHistL1Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistL1Rate.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistL1Rate.setUnits("Mbps")
_AcdPortRxHistL1Percent_Type = Gauge32
_AcdPortRxHistL1Percent_Object = MibTableColumn
acdPortRxHistL1Percent = _AcdPortRxHistL1Percent_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 41),
    _AcdPortRxHistL1Percent_Type()
)
acdPortRxHistL1Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistL1Percent.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistL1Percent.setUnits("%")
_AcdPortRxHistL2Rate_Type = Gauge32
_AcdPortRxHistL2Rate_Object = MibTableColumn
acdPortRxHistL2Rate = _AcdPortRxHistL2Rate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 42),
    _AcdPortRxHistL2Rate_Type()
)
acdPortRxHistL2Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistL2Rate.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxHistL2Rate.setUnits("Mbps")


class _AcdPortRxHistStatsSupportBitsExt_Type(Bits):
    """Custom type acdPortRxHistStatsSupportBitsExt based on Bits"""
    namedValues = NamedValues(
        *(("bL1Rate", 0),
          ("bL1Percent", 1),
          ("bL2Rate", 2))
    )

_AcdPortRxHistStatsSupportBitsExt_Type.__name__ = "Bits"
_AcdPortRxHistStatsSupportBitsExt_Object = MibTableColumn
acdPortRxHistStatsSupportBitsExt = _AcdPortRxHistStatsSupportBitsExt_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 5, 2, 1, 43),
    _AcdPortRxHistStatsSupportBitsExt_Type()
)
acdPortRxHistStatsSupportBitsExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxHistStatsSupportBitsExt.setStatus("current")
_AcdPortConformance_ObjectIdentity = ObjectIdentity
acdPortConformance = _AcdPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2)
)
_AcdPortCompliances_ObjectIdentity = ObjectIdentity
acdPortCompliances = _AcdPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 1)
)
_AcdPortGroups_ObjectIdentity = ObjectIdentity
acdPortGroups = _AcdPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2)
)

# Managed Objects groups

acdPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2, 1)
)
acdPortConfigGroup.setObjects(
      *(("ACD-PORT-MIB", "acdPortConfigName"),
        ("ACD-PORT-MIB", "acdPortConfigAlias"),
        ("ACD-PORT-MIB", "acdPortConfigMacAddress"),
        ("ACD-PORT-MIB", "acdPortConfigConnectorId"),
        ("ACD-PORT-MIB", "acdPortConfigState"),
        ("ACD-PORT-MIB", "acdPortConfigMtu"),
        ("ACD-PORT-MIB", "acdPortConfigAutoNegoState"),
        ("ACD-PORT-MIB", "acdPortConfigSpeed"),
        ("ACD-PORT-MIB", "acdPortConfigDuplex"),
        ("ACD-PORT-MIB", "acdPortConfigMdi"),
        ("ACD-PORT-MIB", "acdPortConfigPauseMode"),
        ("ACD-PORT-MIB", "acdPortConfigAdvertisement"),
        ("ACD-PORT-MIB", "acdPortConfigForceTxOn"),
        ("ACD-PORT-MIB", "acdPortConfigLaserMode"))
)
if mibBuilder.loadTexts:
    acdPortConfigGroup.setStatus("current")

acdPortStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2, 2)
)
acdPortStatusGroup.setObjects(
      *(("ACD-PORT-MIB", "acdPortStatusSpeed"),
        ("ACD-PORT-MIB", "acdPortStatusDuplex"),
        ("ACD-PORT-MIB", "acdPortStatusMdi"),
        ("ACD-PORT-MIB", "acdPortStatusTxPause"),
        ("ACD-PORT-MIB", "acdPortStatusRxPause"),
        ("ACD-PORT-MIB", "acdPortStatusLinkPartnerAbility"),
        ("ACD-PORT-MIB", "acdPortStatusLinkStatus"),
        ("ACD-PORT-MIB", "acdPortStatusMedia"),
        ("ACD-PORT-MIB", "acdPortStatusIsMonitor"),
        ("ACD-PORT-MIB", "acdPortStatusIsManagement"),
        ("ACD-PORT-MIB", "acdPortStatusIsSFP"),
        ("ACD-PORT-MIB", "acdPortStatusIsFiber"))
)
if mibBuilder.loadTexts:
    acdPortStatusGroup.setStatus("current")

acdPortTxStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2, 3)
)
acdPortTxStatsGroup.setObjects(
      *(("ACD-PORT-MIB", "acdPortTxStatsSupportBits"),
        ("ACD-PORT-MIB", "acdPortTxStatsBytesGood"),
        ("ACD-PORT-MIB", "acdPortTxStatsBytesTotal"),
        ("ACD-PORT-MIB", "acdPortTxStatsUnicastPkts"),
        ("ACD-PORT-MIB", "acdPortTxStatsMulticastPkts"),
        ("ACD-PORT-MIB", "acdPortTxStatsBroadcastPkts"),
        ("ACD-PORT-MIB", "acdPortTxStatsPauseFrames"),
        ("ACD-PORT-MIB", "acdPortTxStatsTaggedFrames"),
        ("ACD-PORT-MIB", "acdPortTxStatsCRCErrors"),
        ("ACD-PORT-MIB", "acdPortTxStatsDeferred"),
        ("ACD-PORT-MIB", "acdPortTxStatsExcessiveDeferrals"),
        ("ACD-PORT-MIB", "acdPortTxStatsSingleCollisions"),
        ("ACD-PORT-MIB", "acdPortTxStatsMultipleCollisions"),
        ("ACD-PORT-MIB", "acdPortTxStatsExcessiveCollisions"),
        ("ACD-PORT-MIB", "acdPortTxStatsLateCollisions"),
        ("ACD-PORT-MIB", "acdPortTxStatsNormalCollisions"),
        ("ACD-PORT-MIB", "acdPortTxStatsFifoErrors"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts64"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts65to127"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts128to255"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts256to511"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts512to1023"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts1024to1518"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts1519to2047"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts2048to4095"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts4096to8191"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts8192andMore"),
        ("ACD-PORT-MIB", "acdPortTxStatsPktsLarge"),
        ("ACD-PORT-MIB", "acdPortTxL1Rate"),
        ("ACD-PORT-MIB", "acdPortTxL1Percent"),
        ("ACD-PORT-MIB", "acdPortTxL2Rate"))
)
if mibBuilder.loadTexts:
    acdPortTxStatsGroup.setStatus("current")

acdPortRxStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2, 4)
)
acdPortRxStatsGroup.setObjects(
      *(("ACD-PORT-MIB", "acdPortRxStatsSupportBits"),
        ("ACD-PORT-MIB", "acdPortRxStatsBytesGood"),
        ("ACD-PORT-MIB", "acdPortRxStatsBytesTotal"),
        ("ACD-PORT-MIB", "acdPortRxStatsShortOk"),
        ("ACD-PORT-MIB", "acdPortRxStatsShortBad"),
        ("ACD-PORT-MIB", "acdPortRxStatsLongOk"),
        ("ACD-PORT-MIB", "acdPortRxStatsLongBad"),
        ("ACD-PORT-MIB", "acdPortRxStatsUnicastPkts"),
        ("ACD-PORT-MIB", "acdPortRxStatsMulticastPkts"),
        ("ACD-PORT-MIB", "acdPortRxStatsBroadcastPkts"),
        ("ACD-PORT-MIB", "acdPortRxStatsPauseFrames"),
        ("ACD-PORT-MIB", "acdPortRxStatsTaggedFrames"),
        ("ACD-PORT-MIB", "acdPortRxStatsCRCErrors"),
        ("ACD-PORT-MIB", "acdPortRxStatsAlignErrors"),
        ("ACD-PORT-MIB", "acdPortRxStatsRuntFrames"),
        ("ACD-PORT-MIB", "acdPortRxStatsLengthErrors"),
        ("ACD-PORT-MIB", "acdPortRxStatsFalseCRS"),
        ("ACD-PORT-MIB", "acdPortRxStatsPhyErrors"),
        ("ACD-PORT-MIB", "acdPortRxStatsFifoErrors"),
        ("ACD-PORT-MIB", "acdPortRxStatsIgnored"),
        ("ACD-PORT-MIB", "acdPortRxStatsBadOpcode"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts64"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts65to127"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts128to255"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts256to511"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts512to1023"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts1024to1518"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts1519to2047"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts2048to4095"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts4096to8191"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts8192andMore"),
        ("ACD-PORT-MIB", "acdPortRxStatsPktsLarge"),
        ("ACD-PORT-MIB", "acdPortRxL1Rate"),
        ("ACD-PORT-MIB", "acdPortRxL1Percent"),
        ("ACD-PORT-MIB", "acdPortRxL2Rate"),
        ("ACD-PORT-MIB", "acdPortRxStatsSupportBitsExt"))
)
if mibBuilder.loadTexts:
    acdPortRxStatsGroup.setStatus("current")

acdPortTidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2, 5)
)
acdPortTidGroup.setObjects(
    ("ACD-PORT-MIB", "acdPortConfigTableLastChangeTid")
)
if mibBuilder.loadTexts:
    acdPortTidGroup.setStatus("current")

acdPortTxHistStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2, 6)
)
acdPortTxHistStatsGroup.setObjects(
      *(("ACD-PORT-MIB", "acdPortTxHistStatsIndex"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsSampleIndex"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsStatus"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsDuration"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsIntervalEnd"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsSupportBits"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsBytesGood"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsBytesTotal"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsUnicastPkts"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsMulticastPkts"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsBroadcastPkts"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsPauseFrames"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsTaggedFrames"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsCRCErrors"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsDeferred"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsExcessiveDeferrals"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsSingleCollisions"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsMultipleCollisions"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsExcessiveCollisions"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsLateCollisions"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsNormalCollisions"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsFifoErrors"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsPkts64"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsPkts65to127"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsPkts128to255"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsPkts256to511"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsPkts512to1023"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsPkts1024to1518"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsPkts1519to2047"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsPkts2048to4095"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsPkts4096to8191"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsPkts8192andMore"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsPktsLarge"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsPackets"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsPktsErrors"),
        ("ACD-PORT-MIB", "acdPortTxHistL1Rate"),
        ("ACD-PORT-MIB", "acdPortTxHistL1Percent"),
        ("ACD-PORT-MIB", "acdPortTxHistL2Rate"))
)
if mibBuilder.loadTexts:
    acdPortTxHistStatsGroup.setStatus("current")

acdPortRxHistStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2, 7)
)
acdPortRxHistStatsGroup.setObjects(
      *(("ACD-PORT-MIB", "acdPortRxHistStatsIndex"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsSampleIndex"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsStatus"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsDuration"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsIntervalEnd"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsSupportBits"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsBytesGood"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsBytesTotal"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsShortOk"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsShortBad"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsLongOk"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsLongBad"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsUnicastPkts"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsMulticastPkts"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsBroadcastPkts"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPauseFrames"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsTaggedFrames"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsCRCErrors"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsAlignErrors"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsRuntFrames"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsLengthErrors"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsFalseCRS"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPhyErrors"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsFifoErrors"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsIgnored"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsBadOpcode"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPkts64"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPkts65to127"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPkts128to255"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPkts256to511"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPkts512to1023"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPkts1024to1518"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPkts1519to2047"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPkts2048to4095"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPkts4096to8191"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPkts8192andMore"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPktsLarge"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPackets"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsPktsErrors"),
        ("ACD-PORT-MIB", "acdPortRxHistL1Rate"),
        ("ACD-PORT-MIB", "acdPortRxHistL1Percent"),
        ("ACD-PORT-MIB", "acdPortRxHistL2Rate"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsSupportBitsExt"))
)
if mibBuilder.loadTexts:
    acdPortRxHistStatsGroup.setStatus("current")

acdPortStatsSumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2, 8)
)
acdPortStatsSumGroup.setObjects(
      *(("ACD-PORT-MIB", "acdPortStatsSumName"),
        ("ACD-PORT-MIB", "acdPortStatsSumTXPkt"),
        ("ACD-PORT-MIB", "acdPortStatsSumTXErr"),
        ("ACD-PORT-MIB", "acdPortStatsSumRXPkt"),
        ("ACD-PORT-MIB", "acdPortStatsSumRXErr"))
)
if mibBuilder.loadTexts:
    acdPortStatsSumGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 1, 1)
)
acdPortCompliance.setObjects(
      *(("ACD-PORT-MIB", "acdPortConfigGroup"),
        ("ACD-PORT-MIB", "acdPortStatusGroup"),
        ("ACD-PORT-MIB", "acdPortTxStatsGroup"),
        ("ACD-PORT-MIB", "acdPortRxStatsGroup"),
        ("ACD-PORT-MIB", "acdPortTidGroup"),
        ("ACD-PORT-MIB", "acdPortTxHistStatsGroup"),
        ("ACD-PORT-MIB", "acdPortRxHistStatsGroup"),
        ("ACD-PORT-MIB", "acdPortStatsSumGroup"))
)
if mibBuilder.loadTexts:
    acdPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-PORT-MIB",
    **{"acdPort": acdPort,
       "acdPortMIBObjects": acdPortMIBObjects,
       "acdPortConfig": acdPortConfig,
       "acdPortConfigTable": acdPortConfigTable,
       "acdPortConfigEntry": acdPortConfigEntry,
       "acdPortConfigIndex": acdPortConfigIndex,
       "acdPortConfigName": acdPortConfigName,
       "acdPortConfigAlias": acdPortConfigAlias,
       "acdPortConfigMacAddress": acdPortConfigMacAddress,
       "acdPortConfigConnectorId": acdPortConfigConnectorId,
       "acdPortConfigState": acdPortConfigState,
       "acdPortConfigMtu": acdPortConfigMtu,
       "acdPortConfigAutoNegoState": acdPortConfigAutoNegoState,
       "acdPortConfigSpeed": acdPortConfigSpeed,
       "acdPortConfigDuplex": acdPortConfigDuplex,
       "acdPortConfigMdi": acdPortConfigMdi,
       "acdPortConfigPauseMode": acdPortConfigPauseMode,
       "acdPortConfigAdvertisement": acdPortConfigAdvertisement,
       "acdPortConfigForceTxOn": acdPortConfigForceTxOn,
       "acdPortConfigLaserMode": acdPortConfigLaserMode,
       "acdPortStatus": acdPortStatus,
       "acdPortStatusTable": acdPortStatusTable,
       "acdPortStatusEntry": acdPortStatusEntry,
       "acdPortStatusIndex": acdPortStatusIndex,
       "acdPortStatusSpeed": acdPortStatusSpeed,
       "acdPortStatusDuplex": acdPortStatusDuplex,
       "acdPortStatusMdi": acdPortStatusMdi,
       "acdPortStatusTxPause": acdPortStatusTxPause,
       "acdPortStatusRxPause": acdPortStatusRxPause,
       "acdPortStatusLinkPartnerAbility": acdPortStatusLinkPartnerAbility,
       "acdPortStatusLinkStatus": acdPortStatusLinkStatus,
       "acdPortStatusMedia": acdPortStatusMedia,
       "acdPortStatusIsMonitor": acdPortStatusIsMonitor,
       "acdPortStatusIsManagement": acdPortStatusIsManagement,
       "acdPortStatusIsSFP": acdPortStatusIsSFP,
       "acdPortStatusIsFiber": acdPortStatusIsFiber,
       "acdPortStats": acdPortStats,
       "acdPortTxStatsTable": acdPortTxStatsTable,
       "acdPortTxStatsEntry": acdPortTxStatsEntry,
       "acdPortTxStatsIndex": acdPortTxStatsIndex,
       "acdPortTxStatsSupportBits": acdPortTxStatsSupportBits,
       "acdPortTxStatsBytesGood": acdPortTxStatsBytesGood,
       "acdPortTxStatsBytesTotal": acdPortTxStatsBytesTotal,
       "acdPortTxStatsUnicastPkts": acdPortTxStatsUnicastPkts,
       "acdPortTxStatsMulticastPkts": acdPortTxStatsMulticastPkts,
       "acdPortTxStatsBroadcastPkts": acdPortTxStatsBroadcastPkts,
       "acdPortTxStatsPauseFrames": acdPortTxStatsPauseFrames,
       "acdPortTxStatsTaggedFrames": acdPortTxStatsTaggedFrames,
       "acdPortTxStatsCRCErrors": acdPortTxStatsCRCErrors,
       "acdPortTxStatsDeferred": acdPortTxStatsDeferred,
       "acdPortTxStatsExcessiveDeferrals": acdPortTxStatsExcessiveDeferrals,
       "acdPortTxStatsSingleCollisions": acdPortTxStatsSingleCollisions,
       "acdPortTxStatsMultipleCollisions": acdPortTxStatsMultipleCollisions,
       "acdPortTxStatsExcessiveCollisions": acdPortTxStatsExcessiveCollisions,
       "acdPortTxStatsLateCollisions": acdPortTxStatsLateCollisions,
       "acdPortTxStatsNormalCollisions": acdPortTxStatsNormalCollisions,
       "acdPortTxStatsFifoErrors": acdPortTxStatsFifoErrors,
       "acdPortTxStatsPkts64": acdPortTxStatsPkts64,
       "acdPortTxStatsPkts65to127": acdPortTxStatsPkts65to127,
       "acdPortTxStatsPkts128to255": acdPortTxStatsPkts128to255,
       "acdPortTxStatsPkts256to511": acdPortTxStatsPkts256to511,
       "acdPortTxStatsPkts512to1023": acdPortTxStatsPkts512to1023,
       "acdPortTxStatsPkts1024to1518": acdPortTxStatsPkts1024to1518,
       "acdPortTxStatsPkts1519to2047": acdPortTxStatsPkts1519to2047,
       "acdPortTxStatsPkts2048to4095": acdPortTxStatsPkts2048to4095,
       "acdPortTxStatsPkts4096to8191": acdPortTxStatsPkts4096to8191,
       "acdPortTxStatsPkts8192andMore": acdPortTxStatsPkts8192andMore,
       "acdPortTxStatsPktsLarge": acdPortTxStatsPktsLarge,
       "acdPortTxL1Rate": acdPortTxL1Rate,
       "acdPortTxL1Percent": acdPortTxL1Percent,
       "acdPortTxL2Rate": acdPortTxL2Rate,
       "acdPortRxStatsTable": acdPortRxStatsTable,
       "acdPortRxStatsEntry": acdPortRxStatsEntry,
       "acdPortRxStatsIndex": acdPortRxStatsIndex,
       "acdPortRxStatsSupportBits": acdPortRxStatsSupportBits,
       "acdPortRxStatsBytesGood": acdPortRxStatsBytesGood,
       "acdPortRxStatsBytesTotal": acdPortRxStatsBytesTotal,
       "acdPortRxStatsShortOk": acdPortRxStatsShortOk,
       "acdPortRxStatsShortBad": acdPortRxStatsShortBad,
       "acdPortRxStatsLongOk": acdPortRxStatsLongOk,
       "acdPortRxStatsLongBad": acdPortRxStatsLongBad,
       "acdPortRxStatsUnicastPkts": acdPortRxStatsUnicastPkts,
       "acdPortRxStatsMulticastPkts": acdPortRxStatsMulticastPkts,
       "acdPortRxStatsBroadcastPkts": acdPortRxStatsBroadcastPkts,
       "acdPortRxStatsPauseFrames": acdPortRxStatsPauseFrames,
       "acdPortRxStatsTaggedFrames": acdPortRxStatsTaggedFrames,
       "acdPortRxStatsCRCErrors": acdPortRxStatsCRCErrors,
       "acdPortRxStatsAlignErrors": acdPortRxStatsAlignErrors,
       "acdPortRxStatsRuntFrames": acdPortRxStatsRuntFrames,
       "acdPortRxStatsLengthErrors": acdPortRxStatsLengthErrors,
       "acdPortRxStatsFalseCRS": acdPortRxStatsFalseCRS,
       "acdPortRxStatsPhyErrors": acdPortRxStatsPhyErrors,
       "acdPortRxStatsFifoErrors": acdPortRxStatsFifoErrors,
       "acdPortRxStatsIgnored": acdPortRxStatsIgnored,
       "acdPortRxStatsBadOpcode": acdPortRxStatsBadOpcode,
       "acdPortRxStatsPkts64": acdPortRxStatsPkts64,
       "acdPortRxStatsPkts65to127": acdPortRxStatsPkts65to127,
       "acdPortRxStatsPkts128to255": acdPortRxStatsPkts128to255,
       "acdPortRxStatsPkts256to511": acdPortRxStatsPkts256to511,
       "acdPortRxStatsPkts512to1023": acdPortRxStatsPkts512to1023,
       "acdPortRxStatsPkts1024to1518": acdPortRxStatsPkts1024to1518,
       "acdPortRxStatsPkts1519to2047": acdPortRxStatsPkts1519to2047,
       "acdPortRxStatsPkts2048to4095": acdPortRxStatsPkts2048to4095,
       "acdPortRxStatsPkts4096to8191": acdPortRxStatsPkts4096to8191,
       "acdPortRxStatsPkts8192andMore": acdPortRxStatsPkts8192andMore,
       "acdPortRxStatsPktsLarge": acdPortRxStatsPktsLarge,
       "acdPortRxL1Rate": acdPortRxL1Rate,
       "acdPortRxL1Percent": acdPortRxL1Percent,
       "acdPortRxL2Rate": acdPortRxL2Rate,
       "acdPortRxStatsSupportBitsExt": acdPortRxStatsSupportBitsExt,
       "acdPortStatsSumTable": acdPortStatsSumTable,
       "acdPortStatsSumEntry": acdPortStatsSumEntry,
       "acdPortStatsSumIndex": acdPortStatsSumIndex,
       "acdPortStatsSumName": acdPortStatsSumName,
       "acdPortStatsSumTXPkt": acdPortStatsSumTXPkt,
       "acdPortStatsSumTXErr": acdPortStatsSumTXErr,
       "acdPortStatsSumRXPkt": acdPortStatsSumRXPkt,
       "acdPortStatsSumRXErr": acdPortStatsSumRXErr,
       "acdPortTableTid": acdPortTableTid,
       "acdPortConfigTableLastChangeTid": acdPortConfigTableLastChangeTid,
       "acdPortHistStats": acdPortHistStats,
       "acdPortTxHistStatsTable": acdPortTxHistStatsTable,
       "acdPortTxHistStatsEntry": acdPortTxHistStatsEntry,
       "acdPortTxHistStatsIndex": acdPortTxHistStatsIndex,
       "acdPortTxHistStatsSampleIndex": acdPortTxHistStatsSampleIndex,
       "acdPortTxHistStatsStatus": acdPortTxHistStatsStatus,
       "acdPortTxHistStatsDuration": acdPortTxHistStatsDuration,
       "acdPortTxHistStatsIntervalEnd": acdPortTxHistStatsIntervalEnd,
       "acdPortTxHistStatsSupportBits": acdPortTxHistStatsSupportBits,
       "acdPortTxHistStatsBytesGood": acdPortTxHistStatsBytesGood,
       "acdPortTxHistStatsBytesTotal": acdPortTxHistStatsBytesTotal,
       "acdPortTxHistStatsUnicastPkts": acdPortTxHistStatsUnicastPkts,
       "acdPortTxHistStatsMulticastPkts": acdPortTxHistStatsMulticastPkts,
       "acdPortTxHistStatsBroadcastPkts": acdPortTxHistStatsBroadcastPkts,
       "acdPortTxHistStatsPauseFrames": acdPortTxHistStatsPauseFrames,
       "acdPortTxHistStatsTaggedFrames": acdPortTxHistStatsTaggedFrames,
       "acdPortTxHistStatsCRCErrors": acdPortTxHistStatsCRCErrors,
       "acdPortTxHistStatsDeferred": acdPortTxHistStatsDeferred,
       "acdPortTxHistStatsExcessiveDeferrals": acdPortTxHistStatsExcessiveDeferrals,
       "acdPortTxHistStatsSingleCollisions": acdPortTxHistStatsSingleCollisions,
       "acdPortTxHistStatsMultipleCollisions": acdPortTxHistStatsMultipleCollisions,
       "acdPortTxHistStatsExcessiveCollisions": acdPortTxHistStatsExcessiveCollisions,
       "acdPortTxHistStatsLateCollisions": acdPortTxHistStatsLateCollisions,
       "acdPortTxHistStatsNormalCollisions": acdPortTxHistStatsNormalCollisions,
       "acdPortTxHistStatsFifoErrors": acdPortTxHistStatsFifoErrors,
       "acdPortTxHistStatsPkts64": acdPortTxHistStatsPkts64,
       "acdPortTxHistStatsPkts65to127": acdPortTxHistStatsPkts65to127,
       "acdPortTxHistStatsPkts128to255": acdPortTxHistStatsPkts128to255,
       "acdPortTxHistStatsPkts256to511": acdPortTxHistStatsPkts256to511,
       "acdPortTxHistStatsPkts512to1023": acdPortTxHistStatsPkts512to1023,
       "acdPortTxHistStatsPkts1024to1518": acdPortTxHistStatsPkts1024to1518,
       "acdPortTxHistStatsPkts1519to2047": acdPortTxHistStatsPkts1519to2047,
       "acdPortTxHistStatsPkts2048to4095": acdPortTxHistStatsPkts2048to4095,
       "acdPortTxHistStatsPkts4096to8191": acdPortTxHistStatsPkts4096to8191,
       "acdPortTxHistStatsPkts8192andMore": acdPortTxHistStatsPkts8192andMore,
       "acdPortTxHistStatsPktsLarge": acdPortTxHistStatsPktsLarge,
       "acdPortTxHistStatsPackets": acdPortTxHistStatsPackets,
       "acdPortTxHistStatsPktsErrors": acdPortTxHistStatsPktsErrors,
       "acdPortTxHistL1Rate": acdPortTxHistL1Rate,
       "acdPortTxHistL1Percent": acdPortTxHistL1Percent,
       "acdPortTxHistL2Rate": acdPortTxHistL2Rate,
       "acdPortRxHistStatsTable": acdPortRxHistStatsTable,
       "acdPortRxHistStatsEntry": acdPortRxHistStatsEntry,
       "acdPortRxHistStatsIndex": acdPortRxHistStatsIndex,
       "acdPortRxHistStatsSampleIndex": acdPortRxHistStatsSampleIndex,
       "acdPortRxHistStatsStatus": acdPortRxHistStatsStatus,
       "acdPortRxHistStatsDuration": acdPortRxHistStatsDuration,
       "acdPortRxHistStatsIntervalEnd": acdPortRxHistStatsIntervalEnd,
       "acdPortRxHistStatsSupportBits": acdPortRxHistStatsSupportBits,
       "acdPortRxHistStatsBytesGood": acdPortRxHistStatsBytesGood,
       "acdPortRxHistStatsBytesTotal": acdPortRxHistStatsBytesTotal,
       "acdPortRxHistStatsShortOk": acdPortRxHistStatsShortOk,
       "acdPortRxHistStatsShortBad": acdPortRxHistStatsShortBad,
       "acdPortRxHistStatsLongOk": acdPortRxHistStatsLongOk,
       "acdPortRxHistStatsLongBad": acdPortRxHistStatsLongBad,
       "acdPortRxHistStatsUnicastPkts": acdPortRxHistStatsUnicastPkts,
       "acdPortRxHistStatsMulticastPkts": acdPortRxHistStatsMulticastPkts,
       "acdPortRxHistStatsBroadcastPkts": acdPortRxHistStatsBroadcastPkts,
       "acdPortRxHistStatsPauseFrames": acdPortRxHistStatsPauseFrames,
       "acdPortRxHistStatsTaggedFrames": acdPortRxHistStatsTaggedFrames,
       "acdPortRxHistStatsCRCErrors": acdPortRxHistStatsCRCErrors,
       "acdPortRxHistStatsAlignErrors": acdPortRxHistStatsAlignErrors,
       "acdPortRxHistStatsRuntFrames": acdPortRxHistStatsRuntFrames,
       "acdPortRxHistStatsLengthErrors": acdPortRxHistStatsLengthErrors,
       "acdPortRxHistStatsFalseCRS": acdPortRxHistStatsFalseCRS,
       "acdPortRxHistStatsPhyErrors": acdPortRxHistStatsPhyErrors,
       "acdPortRxHistStatsFifoErrors": acdPortRxHistStatsFifoErrors,
       "acdPortRxHistStatsIgnored": acdPortRxHistStatsIgnored,
       "acdPortRxHistStatsBadOpcode": acdPortRxHistStatsBadOpcode,
       "acdPortRxHistStatsPkts64": acdPortRxHistStatsPkts64,
       "acdPortRxHistStatsPkts65to127": acdPortRxHistStatsPkts65to127,
       "acdPortRxHistStatsPkts128to255": acdPortRxHistStatsPkts128to255,
       "acdPortRxHistStatsPkts256to511": acdPortRxHistStatsPkts256to511,
       "acdPortRxHistStatsPkts512to1023": acdPortRxHistStatsPkts512to1023,
       "acdPortRxHistStatsPkts1024to1518": acdPortRxHistStatsPkts1024to1518,
       "acdPortRxHistStatsPkts1519to2047": acdPortRxHistStatsPkts1519to2047,
       "acdPortRxHistStatsPkts2048to4095": acdPortRxHistStatsPkts2048to4095,
       "acdPortRxHistStatsPkts4096to8191": acdPortRxHistStatsPkts4096to8191,
       "acdPortRxHistStatsPkts8192andMore": acdPortRxHistStatsPkts8192andMore,
       "acdPortRxHistStatsPktsLarge": acdPortRxHistStatsPktsLarge,
       "acdPortRxHistStatsPackets": acdPortRxHistStatsPackets,
       "acdPortRxHistStatsPktsErrors": acdPortRxHistStatsPktsErrors,
       "acdPortRxHistL1Rate": acdPortRxHistL1Rate,
       "acdPortRxHistL1Percent": acdPortRxHistL1Percent,
       "acdPortRxHistL2Rate": acdPortRxHistL2Rate,
       "acdPortRxHistStatsSupportBitsExt": acdPortRxHistStatsSupportBitsExt,
       "acdPortConformance": acdPortConformance,
       "acdPortCompliances": acdPortCompliances,
       "acdPortCompliance": acdPortCompliance,
       "acdPortGroups": acdPortGroups,
       "acdPortConfigGroup": acdPortConfigGroup,
       "acdPortStatusGroup": acdPortStatusGroup,
       "acdPortTxStatsGroup": acdPortTxStatsGroup,
       "acdPortRxStatsGroup": acdPortRxStatsGroup,
       "acdPortTidGroup": acdPortTidGroup,
       "acdPortTxHistStatsGroup": acdPortTxHistStatsGroup,
       "acdPortRxHistStatsGroup": acdPortRxHistStatsGroup,
       "acdPortStatsSumGroup": acdPortStatsSumGroup}
)
