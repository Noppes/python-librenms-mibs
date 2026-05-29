# SNMP MIB module (TELESTE-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teleste\TELESTE-COMMON-MIB

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

(DateAndTime,
 TPhysAddress,
 Uint16,
 common) = mibBuilder.importSymbols(
    "TELESTE-ROOT-MIB",
    "DateAndTime",
    "TPhysAddress",
    "Uint16",
    "common")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Element_ObjectIdentity = ObjectIdentity
element = _Element_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1)
)
_ElementInformation_ObjectIdentity = ObjectIdentity
elementInformation = _ElementInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 1)
)
_ElementName_Type = DisplayString
_ElementName_Object = MibScalar
elementName = _ElementName_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 1),
    _ElementName_Type()
)
elementName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elementName.setStatus("mandatory")


class _ElementStructure_Type(Integer32):
    """Custom type elementStructure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("compact", 2),
          ("modular", 3))
    )


_ElementStructure_Type.__name__ = "Integer32"
_ElementStructure_Object = MibScalar
elementStructure = _ElementStructure_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 2),
    _ElementStructure_Type()
)
elementStructure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elementStructure.setStatus("mandatory")
_ElementConfigChangeCode_Type = Integer32
_ElementConfigChangeCode_Object = MibScalar
elementConfigChangeCode = _ElementConfigChangeCode_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 3),
    _ElementConfigChangeCode_Type()
)
elementConfigChangeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elementConfigChangeCode.setStatus("optional")
_ElementResetCount_Type = Integer32
_ElementResetCount_Object = MibScalar
elementResetCount = _ElementResetCount_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 4),
    _ElementResetCount_Type()
)
elementResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elementResetCount.setStatus("optional")
_ElementTotalUpTime_Type = Integer32
_ElementTotalUpTime_Object = MibScalar
elementTotalUpTime = _ElementTotalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 5),
    _ElementTotalUpTime_Type()
)
elementTotalUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elementTotalUpTime.setStatus("mandatory")
_ElementLatitude_Type = Integer32
_ElementLatitude_Object = MibScalar
elementLatitude = _ElementLatitude_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 6),
    _ElementLatitude_Type()
)
elementLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elementLatitude.setStatus("optional")
_ElementLongitude_Type = Integer32
_ElementLongitude_Object = MibScalar
elementLongitude = _ElementLongitude_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 7),
    _ElementLongitude_Type()
)
elementLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elementLongitude.setStatus("optional")
_ElementAltitude_Type = Integer32
_ElementAltitude_Object = MibScalar
elementAltitude = _ElementAltitude_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 1, 8),
    _ElementAltitude_Type()
)
elementAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elementAltitude.setStatus("optional")
_ElementStatus_ObjectIdentity = ObjectIdentity
elementStatus = _ElementStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 2)
)


class _StatusGeneral_Type(Integer32):
    """Custom type statusGeneral based on Integer32"""
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
        *(("normal", 1),
          ("notification", 2),
          ("warning", 3),
          ("alarm", 4))
    )


_StatusGeneral_Type.__name__ = "Integer32"
_StatusGeneral_Object = MibScalar
statusGeneral = _StatusGeneral_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 1),
    _StatusGeneral_Type()
)
statusGeneral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusGeneral.setStatus("mandatory")


class _StatusBusMaster_Type(Integer32):
    """Custom type statusBusMaster based on Integer32"""
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
        *(("slaveOnly", 1),
          ("configuredSlave", 2),
          ("currentlySlave", 3),
          ("currentlyMaster", 4))
    )


_StatusBusMaster_Type.__name__ = "Integer32"
_StatusBusMaster_Object = MibScalar
statusBusMaster = _StatusBusMaster_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 2),
    _StatusBusMaster_Type()
)
statusBusMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusBusMaster.setStatus("optional")


class _StatusLmt_Type(Integer32):
    """Custom type statusLmt based on Integer32"""
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
        *(("noLmtInterface", 1),
          ("stateUnknown", 2),
          ("notConnected", 3),
          ("connected", 4))
    )


_StatusLmt_Type.__name__ = "Integer32"
_StatusLmt_Object = MibScalar
statusLmt = _StatusLmt_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 3),
    _StatusLmt_Type()
)
statusLmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusLmt.setStatus("optional")


class _StatusLid_Type(Integer32):
    """Custom type statusLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noLid", 1),
          ("closed", 2),
          ("open", 3))
    )


_StatusLid_Type.__name__ = "Integer32"
_StatusLid_Object = MibScalar
statusLid = _StatusLid_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 4),
    _StatusLid_Type()
)
statusLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusLid.setStatus("optional")


class _StatusTemperature_Type(Integer32):
    """Custom type statusTemperature based on Integer32"""
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
        *(("tempNormal", 1),
          ("tempHIHI", 2),
          ("tempHi", 3),
          ("tempLo", 4),
          ("tempLOLO", 5))
    )


_StatusTemperature_Type.__name__ = "Integer32"
_StatusTemperature_Object = MibScalar
statusTemperature = _StatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 5),
    _StatusTemperature_Type()
)
statusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusTemperature.setStatus("optional")


class _StatusFan_Type(Integer32):
    """Custom type statusFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fanNormal", 1),
          ("fanFailure", 2))
    )


_StatusFan_Type.__name__ = "Integer32"
_StatusFan_Object = MibScalar
statusFan = _StatusFan_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 6),
    _StatusFan_Type()
)
statusFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFan.setStatus("mandatory")


class _StatusHardware_Type(Integer32):
    """Custom type statusHardware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hwNormal", 1),
          ("hwFailure", 2))
    )


_StatusHardware_Type.__name__ = "Integer32"
_StatusHardware_Object = MibScalar
statusHardware = _StatusHardware_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 7),
    _StatusHardware_Type()
)
statusHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusHardware.setStatus("mandatory")


class _StatusSoftware_Type(Integer32):
    """Custom type statusSoftware based on Integer32"""
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
        *(("swNormal", 1),
          ("swFailure", 2),
          ("swMissing", 3),
          ("swInitialising", 4))
    )


_StatusSoftware_Type.__name__ = "Integer32"
_StatusSoftware_Object = MibScalar
statusSoftware = _StatusSoftware_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 8),
    _StatusSoftware_Type()
)
statusSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSoftware.setStatus("mandatory")


class _StatusSettings_Type(Integer32):
    """Custom type statusSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("settingsStable", 1),
          ("settingsChanged", 2),
          ("settingsNotAvailable", 3))
    )


_StatusSettings_Type.__name__ = "Integer32"
_StatusSettings_Object = MibScalar
statusSettings = _StatusSettings_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 2, 9),
    _StatusSettings_Type()
)
statusSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSettings.setStatus("mandatory")
_ElementControl_ObjectIdentity = ObjectIdentity
elementControl = _ElementControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3)
)


class _ControlResetElement_Type(Integer32):
    """Custom type controlResetElement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("hardReset", 2),
          ("softReset", 3))
    )


_ControlResetElement_Type.__name__ = "Integer32"
_ControlResetElement_Object = MibScalar
controlResetElement = _ControlResetElement_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 1),
    _ControlResetElement_Type()
)
controlResetElement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlResetElement.setStatus("mandatory")


class _ControlBusMasterAdminState_Type(Integer32):
    """Custom type controlBusMasterAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_ControlBusMasterAdminState_Type.__name__ = "Integer32"
_ControlBusMasterAdminState_Object = MibScalar
controlBusMasterAdminState = _ControlBusMasterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 2),
    _ControlBusMasterAdminState_Type()
)
controlBusMasterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlBusMasterAdminState.setStatus("optional")


class _ControlAlarmDetection_Type(Integer32):
    """Custom type controlAlarmDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("restart", 3))
    )


_ControlAlarmDetection_Type.__name__ = "Integer32"
_ControlAlarmDetection_Object = MibScalar
controlAlarmDetection = _ControlAlarmDetection_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 3),
    _ControlAlarmDetection_Type()
)
controlAlarmDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlAlarmDetection.setStatus("mandatory")
_ControlMaxNumberTrapReceivers_Type = Integer32
_ControlMaxNumberTrapReceivers_Object = MibScalar
controlMaxNumberTrapReceivers = _ControlMaxNumberTrapReceivers_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 4),
    _ControlMaxNumberTrapReceivers_Type()
)
controlMaxNumberTrapReceivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlMaxNumberTrapReceivers.setStatus("mandatory")
_ControlTrapReceiverTable_Object = MibTable
controlTrapReceiverTable = _ControlTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 5)
)
if mibBuilder.loadTexts:
    controlTrapReceiverTable.setStatus("optional")
_ControlTrapReceiverEntry_Object = MibTableRow
controlTrapReceiverEntry = _ControlTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 5, 1)
)
controlTrapReceiverEntry.setIndexNames(
    (0, "TELESTE-COMMON-MIB", "receiverEntryId"),
)
if mibBuilder.loadTexts:
    controlTrapReceiverEntry.setStatus("optional")


class _ReceiverEntryId_Type(Integer32):
    """Custom type receiverEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ReceiverEntryId_Type.__name__ = "Integer32"
_ReceiverEntryId_Object = MibTableColumn
receiverEntryId = _ReceiverEntryId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 5, 1, 1),
    _ReceiverEntryId_Type()
)
receiverEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receiverEntryId.setStatus("mandatory")
_ReceiverAddress_Type = IpAddress
_ReceiverAddress_Object = MibTableColumn
receiverAddress = _ReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 5, 1, 2),
    _ReceiverAddress_Type()
)
receiverAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverAddress.setStatus("mandatory")


class _ReceiverPort_Type(Integer32):
    """Custom type receiverPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ReceiverPort_Type.__name__ = "Integer32"
_ReceiverPort_Object = MibTableColumn
receiverPort = _ReceiverPort_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 5, 1, 3),
    _ReceiverPort_Type()
)
receiverPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverPort.setStatus("mandatory")
_ReceiverCommunity_Type = DisplayString
_ReceiverCommunity_Object = MibTableColumn
receiverCommunity = _ReceiverCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 5, 1, 4),
    _ReceiverCommunity_Type()
)
receiverCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverCommunity.setStatus("mandatory")


class _ControlTrapSending_Type(Integer32):
    """Custom type controlTrapSending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ControlTrapSending_Type.__name__ = "Integer32"
_ControlTrapSending_Object = MibScalar
controlTrapSending = _ControlTrapSending_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 6),
    _ControlTrapSending_Type()
)
controlTrapSending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTrapSending.setStatus("optional")
_ControlTrapInterval_Type = Integer32
_ControlTrapInterval_Object = MibScalar
controlTrapInterval = _ControlTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 7),
    _ControlTrapInterval_Type()
)
controlTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTrapInterval.setStatus("optional")
_ControlTrapLifeTime_Type = Integer32
_ControlTrapLifeTime_Object = MibScalar
controlTrapLifeTime = _ControlTrapLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 8),
    _ControlTrapLifeTime_Type()
)
controlTrapLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTrapLifeTime.setStatus("optional")
_ControlAlarmOnDelay_Type = Integer32
_ControlAlarmOnDelay_Object = MibScalar
controlAlarmOnDelay = _ControlAlarmOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 9),
    _ControlAlarmOnDelay_Type()
)
controlAlarmOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlAlarmOnDelay.setStatus("optional")
_ControlAlarmOffDelay_Type = Integer32
_ControlAlarmOffDelay_Object = MibScalar
controlAlarmOffDelay = _ControlAlarmOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 10),
    _ControlAlarmOffDelay_Type()
)
controlAlarmOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlAlarmOffDelay.setStatus("optional")
_ControlTrapDelay_Type = Integer32
_ControlTrapDelay_Object = MibScalar
controlTrapDelay = _ControlTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 3, 11),
    _ControlTrapDelay_Type()
)
controlTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTrapDelay.setStatus("optional")
_ElementProductKey_ObjectIdentity = ObjectIdentity
elementProductKey = _ElementProductKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4)
)
_ProductKeyNumberOfKeys_Type = Integer32
_ProductKeyNumberOfKeys_Object = MibScalar
productKeyNumberOfKeys = _ProductKeyNumberOfKeys_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 4),
    _ProductKeyNumberOfKeys_Type()
)
productKeyNumberOfKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productKeyNumberOfKeys.setStatus("optional")
_ProductKeyTable_Object = MibTable
productKeyTable = _ProductKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5)
)
if mibBuilder.loadTexts:
    productKeyTable.setStatus("mandatory")
_ProductKeyEntry_Object = MibTableRow
productKeyEntry = _ProductKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5, 1)
)
productKeyEntry.setIndexNames(
    (0, "TELESTE-COMMON-MIB", "productKeyIndex"),
)
if mibBuilder.loadTexts:
    productKeyEntry.setStatus("mandatory")


class _ProductKeyIndex_Type(Integer32):
    """Custom type productKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ProductKeyIndex_Type.__name__ = "Integer32"
_ProductKeyIndex_Object = MibTableColumn
productKeyIndex = _ProductKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5, 1, 1),
    _ProductKeyIndex_Type()
)
productKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productKeyIndex.setStatus("mandatory")
_ProductKeyValue_Type = OctetString
_ProductKeyValue_Object = MibTableColumn
productKeyValue = _ProductKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5, 1, 2),
    _ProductKeyValue_Type()
)
productKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    productKeyValue.setStatus("mandatory")
_ProductKeyMask_Type = OctetString
_ProductKeyMask_Object = MibTableColumn
productKeyMask = _ProductKeyMask_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5, 1, 3),
    _ProductKeyMask_Type()
)
productKeyMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productKeyMask.setStatus("mandatory")


class _ProductKeyStatus_Type(Integer32):
    """Custom type productKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keyInvalid", 1),
          ("keyValid", 2))
    )


_ProductKeyStatus_Type.__name__ = "Integer32"
_ProductKeyStatus_Object = MibTableColumn
productKeyStatus = _ProductKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5, 1, 4),
    _ProductKeyStatus_Type()
)
productKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productKeyStatus.setStatus("mandatory")


class _ProductKeyCipher_Type(Integer32):
    """Custom type productKeyCipher based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cipherOther", 1),
          ("cipherBlowFish", 2),
          ("cipherXXTEA", 3))
    )


_ProductKeyCipher_Type.__name__ = "Integer32"
_ProductKeyCipher_Object = MibTableColumn
productKeyCipher = _ProductKeyCipher_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5, 1, 5),
    _ProductKeyCipher_Type()
)
productKeyCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productKeyCipher.setStatus("mandatory")
_ProductKeyNumberOfFeatures_Type = Integer32
_ProductKeyNumberOfFeatures_Object = MibTableColumn
productKeyNumberOfFeatures = _ProductKeyNumberOfFeatures_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 5, 1, 6),
    _ProductKeyNumberOfFeatures_Type()
)
productKeyNumberOfFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productKeyNumberOfFeatures.setStatus("mandatory")
_ProductKeyFeatureTable_Object = MibTable
productKeyFeatureTable = _ProductKeyFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 6)
)
if mibBuilder.loadTexts:
    productKeyFeatureTable.setStatus("mandatory")
_ProductKeyFeatureEntry_Object = MibTableRow
productKeyFeatureEntry = _ProductKeyFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 6, 1)
)
productKeyFeatureEntry.setIndexNames(
    (0, "TELESTE-COMMON-MIB", "productKeyIndex"),
    (0, "TELESTE-COMMON-MIB", "productKeyFeatureIndex"),
)
if mibBuilder.loadTexts:
    productKeyFeatureEntry.setStatus("mandatory")


class _ProductKeyFeatureIndex_Type(Integer32):
    """Custom type productKeyFeatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ProductKeyFeatureIndex_Type.__name__ = "Integer32"
_ProductKeyFeatureIndex_Object = MibTableColumn
productKeyFeatureIndex = _ProductKeyFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 6, 1, 1),
    _ProductKeyFeatureIndex_Type()
)
productKeyFeatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productKeyFeatureIndex.setStatus("mandatory")
_ProductKeyFeatureName_Type = OctetString
_ProductKeyFeatureName_Object = MibTableColumn
productKeyFeatureName = _ProductKeyFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 6, 1, 2),
    _ProductKeyFeatureName_Type()
)
productKeyFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productKeyFeatureName.setStatus("mandatory")


class _ProductKeyFeatureEnable_Type(Integer32):
    """Custom type productKeyFeatureEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("featureDisable", 1),
          ("featureEnable", 2))
    )


_ProductKeyFeatureEnable_Type.__name__ = "Integer32"
_ProductKeyFeatureEnable_Object = MibTableColumn
productKeyFeatureEnable = _ProductKeyFeatureEnable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 6, 1, 3),
    _ProductKeyFeatureEnable_Type()
)
productKeyFeatureEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productKeyFeatureEnable.setStatus("mandatory")
_ProductKeyFeatureExpirationTime_Type = Integer32
_ProductKeyFeatureExpirationTime_Object = MibTableColumn
productKeyFeatureExpirationTime = _ProductKeyFeatureExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 1, 4, 6, 1, 4),
    _ProductKeyFeatureExpirationTime_Type()
)
productKeyFeatureExpirationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productKeyFeatureExpirationTime.setStatus("mandatory")
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2)
)
_ModuleInformation_ObjectIdentity = ObjectIdentity
moduleInformation = _ModuleInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1)
)
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 1)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("mandatory")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 1, 1)
)
moduleEntry.setIndexNames(
    (0, "TELESTE-COMMON-MIB", "moduleId"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("mandatory")


class _ModuleId_Type(Integer32):
    """Custom type moduleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ModuleId_Type.__name__ = "Integer32"
_ModuleId_Object = MibTableColumn
moduleId = _ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 1, 1, 1),
    _ModuleId_Type()
)
moduleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleId.setStatus("mandatory")
_ModuleName_Type = DisplayString
_ModuleName_Object = MibTableColumn
moduleName = _ModuleName_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 1, 1, 2),
    _ModuleName_Type()
)
moduleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleName.setStatus("optional")
_ModuleHwType_Type = DisplayString
_ModuleHwType_Object = MibTableColumn
moduleHwType = _ModuleHwType_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 1, 1, 3),
    _ModuleHwType_Type()
)
moduleHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHwType.setStatus("mandatory")
_ModuleRackNo_Type = Integer32
_ModuleRackNo_Object = MibTableColumn
moduleRackNo = _ModuleRackNo_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 1, 1, 4),
    _ModuleRackNo_Type()
)
moduleRackNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleRackNo.setStatus("optional")
_ModuleSlotNo_Type = Integer32
_ModuleSlotNo_Object = MibTableColumn
moduleSlotNo = _ModuleSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 1, 1, 5),
    _ModuleSlotNo_Type()
)
moduleSlotNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleSlotNo.setStatus("optional")
_ModuleDetailTable_Object = MibTable
moduleDetailTable = _ModuleDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2)
)
if mibBuilder.loadTexts:
    moduleDetailTable.setStatus("mandatory")
_ModuleDetailEntry_Object = MibTableRow
moduleDetailEntry = _ModuleDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1)
)
moduleDetailEntry.setIndexNames(
    (0, "TELESTE-COMMON-MIB", "moduleId"),
)
if mibBuilder.loadTexts:
    moduleDetailEntry.setStatus("mandatory")
_ModuleMacAddress_Type = TPhysAddress
_ModuleMacAddress_Object = MibTableColumn
moduleMacAddress = _ModuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 1),
    _ModuleMacAddress_Type()
)
moduleMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleMacAddress.setStatus("optional")
_ModuleBusAddress_Type = Integer32
_ModuleBusAddress_Object = MibTableColumn
moduleBusAddress = _ModuleBusAddress_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 2),
    _ModuleBusAddress_Type()
)
moduleBusAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBusAddress.setStatus("optional")
_ModuleAppDate_Type = DateAndTime
_ModuleAppDate_Object = MibTableColumn
moduleAppDate = _ModuleAppDate_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 3),
    _ModuleAppDate_Type()
)
moduleAppDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAppDate.setStatus("mandatory")
_ModuleAppVersion_Type = DisplayString
_ModuleAppVersion_Object = MibTableColumn
moduleAppVersion = _ModuleAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 4),
    _ModuleAppVersion_Type()
)
moduleAppVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAppVersion.setStatus("mandatory")
_ModuleBiosDate_Type = DateAndTime
_ModuleBiosDate_Object = MibTableColumn
moduleBiosDate = _ModuleBiosDate_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 5),
    _ModuleBiosDate_Type()
)
moduleBiosDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBiosDate.setStatus("mandatory")
_ModuleBiosVersion_Type = DisplayString
_ModuleBiosVersion_Object = MibTableColumn
moduleBiosVersion = _ModuleBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 6),
    _ModuleBiosVersion_Type()
)
moduleBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBiosVersion.setStatus("mandatory")
_ModuleHwSerialNumber_Type = DisplayString
_ModuleHwSerialNumber_Object = MibTableColumn
moduleHwSerialNumber = _ModuleHwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 7),
    _ModuleHwSerialNumber_Type()
)
moduleHwSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHwSerialNumber.setStatus("mandatory")
_ModuleHwVersion_Type = DisplayString
_ModuleHwVersion_Object = MibTableColumn
moduleHwVersion = _ModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 1, 2, 1, 8),
    _ModuleHwVersion_Type()
)
moduleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHwVersion.setStatus("mandatory")
_ModuleStatus_ObjectIdentity = ObjectIdentity
moduleStatus = _ModuleStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 2)
)
_ModuleStatusTable_Object = MibTable
moduleStatusTable = _ModuleStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 2, 1)
)
if mibBuilder.loadTexts:
    moduleStatusTable.setStatus("mandatory")
_ModuleStatusEntry_Object = MibTableRow
moduleStatusEntry = _ModuleStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 2, 1, 1)
)
moduleStatusEntry.setIndexNames(
    (0, "TELESTE-COMMON-MIB", "moduleId"),
)
if mibBuilder.loadTexts:
    moduleStatusEntry.setStatus("mandatory")


class _StatusResetCause_Type(Integer32):
    """Custom type statusResetCause based on Integer32"""
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
        *(("unknown", 1),
          ("selfReset", 2),
          ("powerReset", 3),
          ("commandedReset", 4),
          ("softdownloadReset", 5))
    )


_StatusResetCause_Type.__name__ = "Integer32"
_StatusResetCause_Object = MibTableColumn
statusResetCause = _StatusResetCause_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 2, 1, 1, 1),
    _StatusResetCause_Type()
)
statusResetCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusResetCause.setStatus("mandatory")
_StatusRunningSwImage_Type = Integer32
_StatusRunningSwImage_Object = MibTableColumn
statusRunningSwImage = _StatusRunningSwImage_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 2, 1, 1, 2),
    _StatusRunningSwImage_Type()
)
statusRunningSwImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRunningSwImage.setStatus("mandatory")


class _StatusInternalTemperature_Type(Integer32):
    """Custom type statusInternalTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 1300),
    )


_StatusInternalTemperature_Type.__name__ = "Integer32"
_StatusInternalTemperature_Object = MibTableColumn
statusInternalTemperature = _StatusInternalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 2, 1, 1, 3),
    _StatusInternalTemperature_Type()
)
statusInternalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusInternalTemperature.setStatus("mandatory")


class _StatusLidStatus_Type(Integer32):
    """Custom type statusLidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noLid", 1),
          ("closed", 2),
          ("open", 3))
    )


_StatusLidStatus_Type.__name__ = "Integer32"
_StatusLidStatus_Object = MibTableColumn
statusLidStatus = _StatusLidStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 2, 1, 1, 4),
    _StatusLidStatus_Type()
)
statusLidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusLidStatus.setStatus("optional")
_StatusRestartCounter_Type = Counter32
_StatusRestartCounter_Object = MibTableColumn
statusRestartCounter = _StatusRestartCounter_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 2, 1, 1, 5),
    _StatusRestartCounter_Type()
)
statusRestartCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRestartCounter.setStatus("optional")
_ModuleControl_ObjectIdentity = ObjectIdentity
moduleControl = _ModuleControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3)
)
_ModuleControlTable_Object = MibTable
moduleControlTable = _ModuleControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1)
)
if mibBuilder.loadTexts:
    moduleControlTable.setStatus("optional")
_ModuleControlEntry_Object = MibTableRow
moduleControlEntry = _ModuleControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1)
)
moduleControlEntry.setIndexNames(
    (0, "TELESTE-COMMON-MIB", "moduleId"),
)
if mibBuilder.loadTexts:
    moduleControlEntry.setStatus("optional")


class _ControlLedUsage_Type(Integer32):
    """Custom type controlLedUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("alwaysOn", 2),
          ("offWhenLidClosed", 3))
    )


_ControlLedUsage_Type.__name__ = "Integer32"
_ControlLedUsage_Object = MibTableColumn
controlLedUsage = _ControlLedUsage_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 1),
    _ControlLedUsage_Type()
)
controlLedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlLedUsage.setStatus("optional")


class _ControlMarkState_Type(Integer32):
    """Custom type controlMarkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("on", 2),
          ("off", 3))
    )


_ControlMarkState_Type.__name__ = "Integer32"
_ControlMarkState_Object = MibTableColumn
controlMarkState = _ControlMarkState_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 2),
    _ControlMarkState_Type()
)
controlMarkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlMarkState.setStatus("optional")


class _ControlReset_Type(Integer32):
    """Custom type controlReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("hardReset", 2),
          ("softReset", 3))
    )


_ControlReset_Type.__name__ = "Integer32"
_ControlReset_Object = MibTableColumn
controlReset = _ControlReset_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 3),
    _ControlReset_Type()
)
controlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlReset.setStatus("optional")
_ControlTempLimitHiHi_Type = Integer32
_ControlTempLimitHiHi_Object = MibTableColumn
controlTempLimitHiHi = _ControlTempLimitHiHi_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 4),
    _ControlTempLimitHiHi_Type()
)
controlTempLimitHiHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTempLimitHiHi.setStatus("optional")
_ControlTempLimitHi_Type = Integer32
_ControlTempLimitHi_Object = MibTableColumn
controlTempLimitHi = _ControlTempLimitHi_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 5),
    _ControlTempLimitHi_Type()
)
controlTempLimitHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTempLimitHi.setStatus("optional")
_ControlTempLimitLo_Type = Integer32
_ControlTempLimitLo_Object = MibTableColumn
controlTempLimitLo = _ControlTempLimitLo_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 7),
    _ControlTempLimitLo_Type()
)
controlTempLimitLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTempLimitLo.setStatus("optional")
_ControlTempLimitLoLo_Type = Integer32
_ControlTempLimitLoLo_Object = MibTableColumn
controlTempLimitLoLo = _ControlTempLimitLoLo_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 8),
    _ControlTempLimitLoLo_Type()
)
controlTempLimitLoLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTempLimitLoLo.setStatus("optional")
_ControlTempDeadBand_Type = Integer32
_ControlTempDeadBand_Object = MibTableColumn
controlTempDeadBand = _ControlTempDeadBand_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 9),
    _ControlTempDeadBand_Type()
)
controlTempDeadBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlTempDeadBand.setStatus("optional")


class _ControlInternalAppAccess_Type(Integer32):
    """Custom type controlInternalAppAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowIntControl", 1),
          ("denyIntControl", 2))
    )


_ControlInternalAppAccess_Type.__name__ = "Integer32"
_ControlInternalAppAccess_Object = MibTableColumn
controlInternalAppAccess = _ControlInternalAppAccess_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 10),
    _ControlInternalAppAccess_Type()
)
controlInternalAppAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlInternalAppAccess.setStatus("optional")


class _ControlLocalAccess_Type(Integer32):
    """Custom type controlLocalAccess based on Integer32"""
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


_ControlLocalAccess_Type.__name__ = "Integer32"
_ControlLocalAccess_Object = MibTableColumn
controlLocalAccess = _ControlLocalAccess_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 1, 1, 11),
    _ControlLocalAccess_Type()
)
controlLocalAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlLocalAccess.setStatus("optional")
_ModuleSWUpdateTable_Object = MibTable
moduleSWUpdateTable = _ModuleSWUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 2)
)
if mibBuilder.loadTexts:
    moduleSWUpdateTable.setStatus("optional")
_ModuleSWUpdateEntry_Object = MibTableRow
moduleSWUpdateEntry = _ModuleSWUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 2, 1)
)
moduleSWUpdateEntry.setIndexNames(
    (0, "TELESTE-COMMON-MIB", "moduleId"),
)
if mibBuilder.loadTexts:
    moduleSWUpdateEntry.setStatus("optional")


class _SWUpdateControl_Type(Integer32):
    """Custom type sWUpdateControl based on Integer32"""
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
        *(("updateIdle", 1),
          ("updateRunning", 2),
          ("updateFailed", 3),
          ("updateStart", 4))
    )


_SWUpdateControl_Type.__name__ = "Integer32"
_SWUpdateControl_Object = MibTableColumn
sWUpdateControl = _SWUpdateControl_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 2, 1, 1),
    _SWUpdateControl_Type()
)
sWUpdateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sWUpdateControl.setStatus("optional")
_SwUpdateURL_Type = DisplayString
_SwUpdateURL_Object = MibTableColumn
swUpdateURL = _SwUpdateURL_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 2, 1, 2),
    _SwUpdateURL_Type()
)
swUpdateURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUpdateURL.setStatus("optional")
_SWUpdateFileName_Type = DisplayString
_SWUpdateFileName_Object = MibTableColumn
sWUpdateFileName = _SWUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 2, 1, 3),
    _SWUpdateFileName_Type()
)
sWUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sWUpdateFileName.setStatus("optional")
_SWUpdateStatus_Type = DisplayString
_SWUpdateStatus_Object = MibTableColumn
sWUpdateStatus = _SWUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 3, 2, 1, 4),
    _SWUpdateStatus_Type()
)
sWUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sWUpdateStatus.setStatus("optional")
_ModuleRegistry_ObjectIdentity = ObjectIdentity
moduleRegistry = _ModuleRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4)
)
_ModuleSizeOfTable_Object = MibTable
moduleSizeOfTable = _ModuleSizeOfTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 1)
)
if mibBuilder.loadTexts:
    moduleSizeOfTable.setStatus("optional")
_ModuleSizeOfEntry_Object = MibTableRow
moduleSizeOfEntry = _ModuleSizeOfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 1, 1)
)
moduleSizeOfEntry.setIndexNames(
    (0, "TELESTE-COMMON-MIB", "moduleId"),
)
if mibBuilder.loadTexts:
    moduleSizeOfEntry.setStatus("optional")
_SizeOfRegistry_Type = Integer32
_SizeOfRegistry_Object = MibTableColumn
sizeOfRegistry = _SizeOfRegistry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 1, 1, 1),
    _SizeOfRegistry_Type()
)
sizeOfRegistry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sizeOfRegistry.setStatus("mandatory")
_SizeOfRepairlog_Type = Integer32
_SizeOfRepairlog_Object = MibTableColumn
sizeOfRepairlog = _SizeOfRepairlog_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 1, 1, 2),
    _SizeOfRepairlog_Type()
)
sizeOfRepairlog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sizeOfRepairlog.setStatus("optional")
_SizeOfNotebook_Type = Integer32
_SizeOfNotebook_Object = MibTableColumn
sizeOfNotebook = _SizeOfNotebook_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 1, 1, 3),
    _SizeOfNotebook_Type()
)
sizeOfNotebook.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sizeOfNotebook.setStatus("optional")
_ModuleRegistryTable_Object = MibTable
moduleRegistryTable = _ModuleRegistryTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 2)
)
if mibBuilder.loadTexts:
    moduleRegistryTable.setStatus("optional")
_ModuleRegistryEntry_Object = MibTableRow
moduleRegistryEntry = _ModuleRegistryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 2, 1)
)
moduleRegistryEntry.setIndexNames(
    (0, "TELESTE-COMMON-MIB", "moduleId"),
    (0, "TELESTE-COMMON-MIB", "regIndex"),
)
if mibBuilder.loadTexts:
    moduleRegistryEntry.setStatus("optional")


class _RegIndex_Type(Integer32):
    """Custom type regIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RegIndex_Type.__name__ = "Integer32"
_RegIndex_Object = MibTableColumn
regIndex = _RegIndex_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 2, 1, 1),
    _RegIndex_Type()
)
regIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regIndex.setStatus("optional")
_RegName_Type = DisplayString
_RegName_Object = MibTableColumn
regName = _RegName_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 2, 1, 2),
    _RegName_Type()
)
regName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regName.setStatus("optional")
_RegValue_Type = DisplayString
_RegValue_Object = MibTableColumn
regValue = _RegValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 2, 1, 3),
    _RegValue_Type()
)
regValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regValue.setStatus("optional")
_ModuleRepairLogTable_Object = MibTable
moduleRepairLogTable = _ModuleRepairLogTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 3)
)
if mibBuilder.loadTexts:
    moduleRepairLogTable.setStatus("optional")
_ModuleRepairLogEntry_Object = MibTableRow
moduleRepairLogEntry = _ModuleRepairLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 3, 1)
)
moduleRepairLogEntry.setIndexNames(
    (0, "TELESTE-COMMON-MIB", "moduleId"),
    (0, "TELESTE-COMMON-MIB", "repairIndex"),
)
if mibBuilder.loadTexts:
    moduleRepairLogEntry.setStatus("optional")


class _RepairIndex_Type(Integer32):
    """Custom type repairIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_RepairIndex_Type.__name__ = "Integer32"
_RepairIndex_Object = MibTableColumn
repairIndex = _RepairIndex_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 3, 1, 1),
    _RepairIndex_Type()
)
repairIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repairIndex.setStatus("optional")
_RepairDate_Type = DisplayString
_RepairDate_Object = MibTableColumn
repairDate = _RepairDate_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 3, 1, 2),
    _RepairDate_Type()
)
repairDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repairDate.setStatus("optional")


class _RepairReasonCode_Type(OctetString):
    """Custom type repairReasonCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RepairReasonCode_Type.__name__ = "OctetString"
_RepairReasonCode_Object = MibTableColumn
repairReasonCode = _RepairReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 3, 1, 3),
    _RepairReasonCode_Type()
)
repairReasonCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repairReasonCode.setStatus("optional")


class _RepairNameCode_Type(OctetString):
    """Custom type repairNameCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RepairNameCode_Type.__name__ = "OctetString"
_RepairNameCode_Object = MibTableColumn
repairNameCode = _RepairNameCode_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 3, 1, 4),
    _RepairNameCode_Type()
)
repairNameCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repairNameCode.setStatus("optional")
_RepairComment_Type = DisplayString
_RepairComment_Object = MibTableColumn
repairComment = _RepairComment_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 3, 1, 5),
    _RepairComment_Type()
)
repairComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repairComment.setStatus("optional")
_ModuleNotebookTable_Object = MibTable
moduleNotebookTable = _ModuleNotebookTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 4)
)
if mibBuilder.loadTexts:
    moduleNotebookTable.setStatus("optional")
_ModuleNotebookEntry_Object = MibTableRow
moduleNotebookEntry = _ModuleNotebookEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 4, 1)
)
moduleNotebookEntry.setIndexNames(
    (0, "TELESTE-COMMON-MIB", "moduleId"),
    (0, "TELESTE-COMMON-MIB", "notebookLineNumber"),
)
if mibBuilder.loadTexts:
    moduleNotebookEntry.setStatus("optional")


class _NotebookLineNumber_Type(Integer32):
    """Custom type notebookLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NotebookLineNumber_Type.__name__ = "Integer32"
_NotebookLineNumber_Object = MibTableColumn
notebookLineNumber = _NotebookLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 4, 1, 1),
    _NotebookLineNumber_Type()
)
notebookLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notebookLineNumber.setStatus("optional")


class _NotebookLineText_Type(OctetString):
    """Custom type notebookLineText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NotebookLineText_Type.__name__ = "OctetString"
_NotebookLineText_Object = MibTableColumn
notebookLineText = _NotebookLineText_Object(
    (1, 3, 6, 1, 4, 1, 3715, 99, 2, 4, 4, 1, 2),
    _NotebookLineText_Type()
)
notebookLineText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    notebookLineText.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELESTE-COMMON-MIB",
    **{"element": element,
       "elementInformation": elementInformation,
       "elementName": elementName,
       "elementStructure": elementStructure,
       "elementConfigChangeCode": elementConfigChangeCode,
       "elementResetCount": elementResetCount,
       "elementTotalUpTime": elementTotalUpTime,
       "elementLatitude": elementLatitude,
       "elementLongitude": elementLongitude,
       "elementAltitude": elementAltitude,
       "elementStatus": elementStatus,
       "statusGeneral": statusGeneral,
       "statusBusMaster": statusBusMaster,
       "statusLmt": statusLmt,
       "statusLid": statusLid,
       "statusTemperature": statusTemperature,
       "statusFan": statusFan,
       "statusHardware": statusHardware,
       "statusSoftware": statusSoftware,
       "statusSettings": statusSettings,
       "elementControl": elementControl,
       "controlResetElement": controlResetElement,
       "controlBusMasterAdminState": controlBusMasterAdminState,
       "controlAlarmDetection": controlAlarmDetection,
       "controlMaxNumberTrapReceivers": controlMaxNumberTrapReceivers,
       "controlTrapReceiverTable": controlTrapReceiverTable,
       "controlTrapReceiverEntry": controlTrapReceiverEntry,
       "receiverEntryId": receiverEntryId,
       "receiverAddress": receiverAddress,
       "receiverPort": receiverPort,
       "receiverCommunity": receiverCommunity,
       "controlTrapSending": controlTrapSending,
       "controlTrapInterval": controlTrapInterval,
       "controlTrapLifeTime": controlTrapLifeTime,
       "controlAlarmOnDelay": controlAlarmOnDelay,
       "controlAlarmOffDelay": controlAlarmOffDelay,
       "controlTrapDelay": controlTrapDelay,
       "elementProductKey": elementProductKey,
       "productKeyNumberOfKeys": productKeyNumberOfKeys,
       "productKeyTable": productKeyTable,
       "productKeyEntry": productKeyEntry,
       "productKeyIndex": productKeyIndex,
       "productKeyValue": productKeyValue,
       "productKeyMask": productKeyMask,
       "productKeyStatus": productKeyStatus,
       "productKeyCipher": productKeyCipher,
       "productKeyNumberOfFeatures": productKeyNumberOfFeatures,
       "productKeyFeatureTable": productKeyFeatureTable,
       "productKeyFeatureEntry": productKeyFeatureEntry,
       "productKeyFeatureIndex": productKeyFeatureIndex,
       "productKeyFeatureName": productKeyFeatureName,
       "productKeyFeatureEnable": productKeyFeatureEnable,
       "productKeyFeatureExpirationTime": productKeyFeatureExpirationTime,
       "module": module,
       "moduleInformation": moduleInformation,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleId": moduleId,
       "moduleName": moduleName,
       "moduleHwType": moduleHwType,
       "moduleRackNo": moduleRackNo,
       "moduleSlotNo": moduleSlotNo,
       "moduleDetailTable": moduleDetailTable,
       "moduleDetailEntry": moduleDetailEntry,
       "moduleMacAddress": moduleMacAddress,
       "moduleBusAddress": moduleBusAddress,
       "moduleAppDate": moduleAppDate,
       "moduleAppVersion": moduleAppVersion,
       "moduleBiosDate": moduleBiosDate,
       "moduleBiosVersion": moduleBiosVersion,
       "moduleHwSerialNumber": moduleHwSerialNumber,
       "moduleHwVersion": moduleHwVersion,
       "moduleStatus": moduleStatus,
       "moduleStatusTable": moduleStatusTable,
       "moduleStatusEntry": moduleStatusEntry,
       "statusResetCause": statusResetCause,
       "statusRunningSwImage": statusRunningSwImage,
       "statusInternalTemperature": statusInternalTemperature,
       "statusLidStatus": statusLidStatus,
       "statusRestartCounter": statusRestartCounter,
       "moduleControl": moduleControl,
       "moduleControlTable": moduleControlTable,
       "moduleControlEntry": moduleControlEntry,
       "controlLedUsage": controlLedUsage,
       "controlMarkState": controlMarkState,
       "controlReset": controlReset,
       "controlTempLimitHiHi": controlTempLimitHiHi,
       "controlTempLimitHi": controlTempLimitHi,
       "controlTempLimitLo": controlTempLimitLo,
       "controlTempLimitLoLo": controlTempLimitLoLo,
       "controlTempDeadBand": controlTempDeadBand,
       "controlInternalAppAccess": controlInternalAppAccess,
       "controlLocalAccess": controlLocalAccess,
       "moduleSWUpdateTable": moduleSWUpdateTable,
       "moduleSWUpdateEntry": moduleSWUpdateEntry,
       "sWUpdateControl": sWUpdateControl,
       "swUpdateURL": swUpdateURL,
       "sWUpdateFileName": sWUpdateFileName,
       "sWUpdateStatus": sWUpdateStatus,
       "moduleRegistry": moduleRegistry,
       "moduleSizeOfTable": moduleSizeOfTable,
       "moduleSizeOfEntry": moduleSizeOfEntry,
       "sizeOfRegistry": sizeOfRegistry,
       "sizeOfRepairlog": sizeOfRepairlog,
       "sizeOfNotebook": sizeOfNotebook,
       "moduleRegistryTable": moduleRegistryTable,
       "moduleRegistryEntry": moduleRegistryEntry,
       "regIndex": regIndex,
       "regName": regName,
       "regValue": regValue,
       "moduleRepairLogTable": moduleRepairLogTable,
       "moduleRepairLogEntry": moduleRepairLogEntry,
       "repairIndex": repairIndex,
       "repairDate": repairDate,
       "repairReasonCode": repairReasonCode,
       "repairNameCode": repairNameCode,
       "repairComment": repairComment,
       "moduleNotebookTable": moduleNotebookTable,
       "moduleNotebookEntry": moduleNotebookEntry,
       "notebookLineNumber": notebookLineNumber,
       "notebookLineText": notebookLineText}
)
