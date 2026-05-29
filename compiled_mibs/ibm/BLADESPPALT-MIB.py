# SNMP MIB module (BLADESPPALT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ibm\BLADESPPALT-MIB

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_SupportProcessor_ObjectIdentity = ObjectIdentity
supportProcessor = _SupportProcessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 158)
)
_MmRemoteSupTrapMIB_ObjectIdentity = ObjectIdentity
mmRemoteSupTrapMIB = _MmRemoteSupTrapMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3)
)
_RemoteSupTrapMibObjects_ObjectIdentity = ObjectIdentity
remoteSupTrapMibObjects = _RemoteSupTrapMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1)
)
_SpTrapInfo_ObjectIdentity = ObjectIdentity
spTrapInfo = _SpTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1)
)
_SpTrapDateTime_Type = DisplayString
_SpTrapDateTime_Object = MibScalar
spTrapDateTime = _SpTrapDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 1),
    _SpTrapDateTime_Type()
)
spTrapDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapDateTime.setStatus("mandatory")
_SpTrapAppId_Type = DisplayString
_SpTrapAppId_Object = MibScalar
spTrapAppId = _SpTrapAppId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 2),
    _SpTrapAppId_Type()
)
spTrapAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapAppId.setStatus("mandatory")
_SpTrapSpTxtId_Type = DisplayString
_SpTrapSpTxtId_Object = MibScalar
spTrapSpTxtId = _SpTrapSpTxtId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 3),
    _SpTrapSpTxtId_Type()
)
spTrapSpTxtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapSpTxtId.setStatus("mandatory")
_SpTrapSysUuid_Type = DisplayString
_SpTrapSysUuid_Object = MibScalar
spTrapSysUuid = _SpTrapSysUuid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 4),
    _SpTrapSysUuid_Type()
)
spTrapSysUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapSysUuid.setStatus("mandatory")
_SpTrapSysSern_Type = DisplayString
_SpTrapSysSern_Object = MibScalar
spTrapSysSern = _SpTrapSysSern_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 5),
    _SpTrapSysSern_Type()
)
spTrapSysSern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapSysSern.setStatus("mandatory")


class _SpTrapAppType_Type(Integer32):
    """Custom type spTrapAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SpTrapAppType_Type.__name__ = "Integer32"
_SpTrapAppType_Object = MibScalar
spTrapAppType = _SpTrapAppType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 6),
    _SpTrapAppType_Type()
)
spTrapAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapAppType.setStatus("mandatory")


class _SpTrapPriority_Type(Integer32):
    """Custom type spTrapPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SpTrapPriority_Type.__name__ = "Integer32"
_SpTrapPriority_Object = MibScalar
spTrapPriority = _SpTrapPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 7),
    _SpTrapPriority_Type()
)
spTrapPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapPriority.setStatus("mandatory")
_SpTrapMsgText_Type = DisplayString
_SpTrapMsgText_Object = MibScalar
spTrapMsgText = _SpTrapMsgText_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 8),
    _SpTrapMsgText_Type()
)
spTrapMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapMsgText.setStatus("mandatory")
_SpTrapHostContact_Type = DisplayString
_SpTrapHostContact_Object = MibScalar
spTrapHostContact = _SpTrapHostContact_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 9),
    _SpTrapHostContact_Type()
)
spTrapHostContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapHostContact.setStatus("mandatory")
_SpTrapHostLocation_Type = DisplayString
_SpTrapHostLocation_Object = MibScalar
spTrapHostLocation = _SpTrapHostLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 10),
    _SpTrapHostLocation_Type()
)
spTrapHostLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapHostLocation.setStatus("mandatory")
_SpTrapBladeName_Type = DisplayString
_SpTrapBladeName_Object = MibScalar
spTrapBladeName = _SpTrapBladeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 11),
    _SpTrapBladeName_Type()
)
spTrapBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapBladeName.setStatus("mandatory")
_SpTrapBladeSern_Type = DisplayString
_SpTrapBladeSern_Object = MibScalar
spTrapBladeSern = _SpTrapBladeSern_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 12),
    _SpTrapBladeSern_Type()
)
spTrapBladeSern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapBladeSern.setStatus("mandatory")
_SpTrapBladeUuid_Type = DisplayString
_SpTrapBladeUuid_Object = MibScalar
spTrapBladeUuid = _SpTrapBladeUuid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 13),
    _SpTrapBladeUuid_Type()
)
spTrapBladeUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapBladeUuid.setStatus("mandatory")


class _SpTrapEvtName_Type(Unsigned32):
    """Custom type spTrapEvtName based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SpTrapEvtName_Type.__name__ = "Unsigned32"
_SpTrapEvtName_Object = MibScalar
spTrapEvtName = _SpTrapEvtName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 14),
    _SpTrapEvtName_Type()
)
spTrapEvtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapEvtName.setStatus("mandatory")
_SpTrapSourceId_Type = DisplayString
_SpTrapSourceId_Object = MibScalar
spTrapSourceId = _SpTrapSourceId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 15),
    _SpTrapSourceId_Type()
)
spTrapSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapSourceId.setStatus("mandatory")


class _SpTrapCallHomeFlag_Type(Unsigned32):
    """Custom type spTrapCallHomeFlag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SpTrapCallHomeFlag_Type.__name__ = "Unsigned32"
_SpTrapCallHomeFlag_Object = MibScalar
spTrapCallHomeFlag = _SpTrapCallHomeFlag_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 16),
    _SpTrapCallHomeFlag_Type()
)
spTrapCallHomeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapCallHomeFlag.setStatus("mandatory")
_SpTrapSysIPAddress_Type = DisplayString
_SpTrapSysIPAddress_Object = MibScalar
spTrapSysIPAddress = _SpTrapSysIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 17),
    _SpTrapSysIPAddress_Type()
)
spTrapSysIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapSysIPAddress.setStatus("mandatory")
_SpTrapSysMachineModel_Type = DisplayString
_SpTrapSysMachineModel_Object = MibScalar
spTrapSysMachineModel = _SpTrapSysMachineModel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 18),
    _SpTrapSysMachineModel_Type()
)
spTrapSysMachineModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapSysMachineModel.setStatus("mandatory")
_SpTrapBladeMachineModel_Type = DisplayString
_SpTrapBladeMachineModel_Object = MibScalar
spTrapBladeMachineModel = _SpTrapBladeMachineModel_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 19),
    _SpTrapBladeMachineModel_Type()
)
spTrapBladeMachineModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapBladeMachineModel.setStatus("mandatory")
_SpTrapBladeFRUSerialNumber_Type = DisplayString
_SpTrapBladeFRUSerialNumber_Object = MibScalar
spTrapBladeFRUSerialNumber = _SpTrapBladeFRUSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 20),
    _SpTrapBladeFRUSerialNumber_Type()
)
spTrapBladeFRUSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapBladeFRUSerialNumber.setStatus("mandatory")
_SpTrapBladeEvtName_Type = DisplayString
_SpTrapBladeEvtName_Object = MibScalar
spTrapBladeEvtName = _SpTrapBladeEvtName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 21),
    _SpTrapBladeEvtName_Type()
)
spTrapBladeEvtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapBladeEvtName.setStatus("mandatory")
_SpBladeEventDataSource_Type = DisplayString
_SpBladeEventDataSource_Object = MibScalar
spBladeEventDataSource = _SpBladeEventDataSource_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 22),
    _SpBladeEventDataSource_Type()
)
spBladeEventDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spBladeEventDataSource.setStatus("mandatory")
_SpTrapAuxData_Type = DisplayString
_SpTrapAuxData_Object = MibScalar
spTrapAuxData = _SpTrapAuxData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 23),
    _SpTrapAuxData_Type()
)
spTrapAuxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapAuxData.setStatus("mandatory")
_SpTrapComponentID_Type = DisplayString
_SpTrapComponentID_Object = MibScalar
spTrapComponentID = _SpTrapComponentID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 24),
    _SpTrapComponentID_Type()
)
spTrapComponentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapComponentID.setStatus("mandatory")
_SpTrapComponentFRUInfo_Type = DisplayString
_SpTrapComponentFRUInfo_Object = MibScalar
spTrapComponentFRUInfo = _SpTrapComponentFRUInfo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 25),
    _SpTrapComponentFRUInfo_Type()
)
spTrapComponentFRUInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapComponentFRUInfo.setStatus("mandatory")
_SpTrapChassisName_Type = DisplayString
_SpTrapChassisName_Object = MibScalar
spTrapChassisName = _SpTrapChassisName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 26),
    _SpTrapChassisName_Type()
)
spTrapChassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapChassisName.setStatus("mandatory")
_SpTrapSysRoomId_Type = DisplayString
_SpTrapSysRoomId_Object = MibScalar
spTrapSysRoomId = _SpTrapSysRoomId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 27),
    _SpTrapSysRoomId_Type()
)
spTrapSysRoomId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapSysRoomId.setStatus("mandatory")
_SpTrapSysRackId_Type = DisplayString
_SpTrapSysRackId_Object = MibScalar
spTrapSysRackId = _SpTrapSysRackId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 28),
    _SpTrapSysRackId_Type()
)
spTrapSysRackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapSysRackId.setStatus("mandatory")


class _SpTrapSysRackU_Type(Unsigned32):
    """Custom type spTrapSysRackU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SpTrapSysRackU_Type.__name__ = "Unsigned32"
_SpTrapSysRackU_Object = MibScalar
spTrapSysRackU = _SpTrapSysRackU_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 29),
    _SpTrapSysRackU_Type()
)
spTrapSysRackU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapSysRackU.setStatus("mandatory")


class _SpTrapServiceableEventFlag_Type(Unsigned32):
    """Custom type spTrapServiceableEventFlag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SpTrapServiceableEventFlag_Type.__name__ = "Unsigned32"
_SpTrapServiceableEventFlag_Object = MibScalar
spTrapServiceableEventFlag = _SpTrapServiceableEventFlag_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 30),
    _SpTrapServiceableEventFlag_Type()
)
spTrapServiceableEventFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spTrapServiceableEventFlag.setStatus("mandatory")


class _SpLogSequenceNum_Type(Unsigned32):
    """Custom type spLogSequenceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SpLogSequenceNum_Type.__name__ = "Unsigned32"
_SpLogSequenceNum_Object = MibScalar
spLogSequenceNum = _SpLogSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 31),
    _SpLogSequenceNum_Type()
)
spLogSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spLogSequenceNum.setStatus("mandatory")
_SpCimMsgID_Type = DisplayString
_SpCimMsgID_Object = MibScalar
spCimMsgID = _SpCimMsgID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 32),
    _SpCimMsgID_Type()
)
spCimMsgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spCimMsgID.setStatus("mandatory")
_SpCimMsgPrefix_Type = DisplayString
_SpCimMsgPrefix_Object = MibScalar
spCimMsgPrefix = _SpCimMsgPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 33),
    _SpCimMsgPrefix_Type()
)
spCimMsgPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spCimMsgPrefix.setStatus("mandatory")


class _SpEventCorrelator_Type(Unsigned32):
    """Custom type spEventCorrelator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SpEventCorrelator_Type.__name__ = "Unsigned32"
_SpEventCorrelator_Object = MibScalar
spEventCorrelator = _SpEventCorrelator_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 1, 1, 34),
    _SpEventCorrelator_Type()
)
spEventCorrelator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spEventCorrelator.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mmTrapTempC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 0)
)
mmTrapTempC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapTempC.setStatus(
        ""
    )

mmTrapVoltC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 1)
)
mmTrapVoltC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapVoltC.setStatus(
        ""
    )

mmTrapTampC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 2)
)
mmTrapTampC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapTampC.setStatus(
        ""
    )

mmTrapMffC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 3)
)
mmTrapMffC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapMffC.setStatus(
        ""
    )

mmTrapPsC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 4)
)
mmTrapPsC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapPsC.setStatus(
        ""
    )

mTrapHdC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 5)
)
mTrapHdC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mTrapHdC.setStatus(
        ""
    )

mmTrapVrmC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 6)
)
mmTrapVrmC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapVrmC.setStatus(
        ""
    )

mmTrapLogFullN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 7)
)
mmTrapLogFullN.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapLogFullN.setStatus(
        ""
    )

mmTrapRdpsN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 10)
)
mmTrapRdpsN.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapRdpsN.setStatus(
        ""
    )

mmTrapSffC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 11)
)
mmTrapSffC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapSffC.setStatus(
        ""
    )

mmTrapTempN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 12)
)
mmTrapTempN.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapTempN.setStatus(
        ""
    )

mmTrapVoltN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 13)
)
mmTrapVoltN.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"))
)
if mibBuilder.loadTexts:
    mmTrapVoltN.setStatus(
        ""
    )

mmTrapSecDvS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 15)
)
mmTrapSecDvS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapSecDvS.setStatus(
        ""
    )

mmTrapPostToS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 20)
)
mmTrapPostToS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapPostToS.setStatus(
        ""
    )

mmTrapOsToS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 21)
)
mmTrapOsToS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapOsToS.setStatus(
        ""
    )

mmTrapAppS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 22)
)
mmTrapAppS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapAppS.setStatus(
        ""
    )

mmTrapPoffS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 23)
)
mmTrapPoffS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapPoffS.setStatus(
        ""
    )

mmTrapPonS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 24)
)
mmTrapPonS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapPonS.setStatus(
        ""
    )

mmTrapBootS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 25)
)
mmTrapBootS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapBootS.setStatus(
        ""
    )

mmTrapLdrToS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 26)
)
mmTrapLdrToS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapLdrToS.setStatus(
        ""
    )

mmTrapPFAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 27)
)
mmTrapPFAS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapPFAS.setStatus(
        ""
    )

mmTrapRemoteLoginS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 30)
)
mmTrapRemoteLoginS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapRemoteLoginS.setStatus(
        ""
    )

mmTrapMsC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 31)
)
mmTrapMsC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapMsC.setStatus(
        ""
    )

mmTrapRmN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 32)
)
mmTrapRmN.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapRmN.setStatus(
        ""
    )

mmTrapKVMSwitchS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 33)
)
mmTrapKVMSwitchS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapKVMSwitchS.setStatus(
        ""
    )

mmTrapSysInvS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 34)
)
mmTrapSysInvS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapSysInvS.setStatus(
        ""
    )

mmTrapSysLogS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 35)
)
mmTrapSysLogS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapSysLogS.setStatus(
        ""
    )

mmTrapIhcC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 36)
)
mmTrapIhcC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapIhcC.setStatus(
        ""
    )

mmTrapNwChangeS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 37)
)
mmTrapNwChangeS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapNwChangeS.setStatus(
        ""
    )

mmTrapBlThrS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 39)
)
mmTrapBlThrS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapBlThrS.setStatus(
        ""
    )

mmTrapPwrMgntS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 40)
)
mmTrapPwrMgntS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapPwrMgntS.setStatus(
        ""
    )

mmTrapBladeC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 128)
)
mmTrapBladeC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapBladeC.setStatus(
        ""
    )

mmTrapIOC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 129)
)
mmTrapIOC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapIOC.setStatus(
        ""
    )

mmTrapChassisC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 130)
)
mmTrapChassisC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapChassisC.setStatus(
        ""
    )

mmTrapStorageC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 131)
)
mmTrapStorageC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapStorageC.setStatus(
        ""
    )

mmTrapFanC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 133)
)
mmTrapFanC.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapFanC.setStatus(
        ""
    )

mmTrapBladeN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 160)
)
mmTrapBladeN.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapBladeN.setStatus(
        ""
    )

mmTrapION = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 161)
)
mmTrapION.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapION.setStatus(
        ""
    )

mmTrapChassisN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 162)
)
mmTrapChassisN.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapChassisN.setStatus(
        ""
    )

mmTrapStorageN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 163)
)
mmTrapStorageN.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapStorageN.setStatus(
        ""
    )

mmTrapPowerN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 164)
)
mmTrapPowerN.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapPowerN.setStatus(
        ""
    )

mmTrapFanN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 165)
)
mmTrapFanN.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapFanN.setStatus(
        ""
    )

mmTrapBladeS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 176)
)
mmTrapBladeS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapBladeS.setStatus(
        ""
    )

mmTrapIOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 177)
)
mmTrapIOS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapIOS.setStatus(
        ""
    )

mmTrapChassisS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 178)
)
mmTrapChassisS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapChassisS.setStatus(
        ""
    )

mmTrapStorageS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 179)
)
mmTrapStorageS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapStorageS.setStatus(
        ""
    )

mmTrapPowerS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 180)
)
mmTrapPowerS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapPowerS.setStatus(
        ""
    )

mmTrapFanS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 181)
)
mmTrapFanS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapFanS.setStatus(
        ""
    )

mmTrapPwrDOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 3, 0, 182)
)
mmTrapPwrDOS.setObjects(
      *(("BLADESPPALT-MIB", "spTrapDateTime"),
        ("BLADESPPALT-MIB", "spTrapAppId"),
        ("BLADESPPALT-MIB", "spTrapSpTxtId"),
        ("BLADESPPALT-MIB", "spTrapSysUuid"),
        ("BLADESPPALT-MIB", "spTrapSysSern"),
        ("BLADESPPALT-MIB", "spTrapAppType"),
        ("BLADESPPALT-MIB", "spTrapPriority"),
        ("BLADESPPALT-MIB", "spTrapMsgText"),
        ("BLADESPPALT-MIB", "spTrapHostContact"),
        ("BLADESPPALT-MIB", "spTrapHostLocation"),
        ("BLADESPPALT-MIB", "spTrapBladeName"),
        ("BLADESPPALT-MIB", "spTrapBladeSern"),
        ("BLADESPPALT-MIB", "spTrapBladeUuid"),
        ("BLADESPPALT-MIB", "spTrapEvtName"),
        ("BLADESPPALT-MIB", "spTrapSourceId"),
        ("BLADESPPALT-MIB", "spTrapCallHomeFlag"),
        ("BLADESPPALT-MIB", "spTrapSysIPAddress"),
        ("BLADESPPALT-MIB", "spTrapSysMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeMachineModel"),
        ("BLADESPPALT-MIB", "spTrapBladeFRUSerialNumber"),
        ("BLADESPPALT-MIB", "spTrapBladeEvtName"),
        ("BLADESPPALT-MIB", "spBladeEventDataSource"),
        ("BLADESPPALT-MIB", "spTrapAuxData"),
        ("BLADESPPALT-MIB", "spTrapComponentID"),
        ("BLADESPPALT-MIB", "spTrapComponentFRUInfo"),
        ("BLADESPPALT-MIB", "spTrapChassisName"),
        ("BLADESPPALT-MIB", "spTrapSysRoomId"),
        ("BLADESPPALT-MIB", "spTrapSysRackId"),
        ("BLADESPPALT-MIB", "spTrapSysRackU"),
        ("BLADESPPALT-MIB", "spTrapServiceableEventFlag"),
        ("BLADESPPALT-MIB", "spLogSequenceNum"),
        ("BLADESPPALT-MIB", "spCimMsgID"),
        ("BLADESPPALT-MIB", "spCimMsgPrefix"),
        ("BLADESPPALT-MIB", "spEventCorrelator"))
)
if mibBuilder.loadTexts:
    mmTrapPwrDOS.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLADESPPALT-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "supportProcessor": supportProcessor,
       "mmRemoteSupTrapMIB": mmRemoteSupTrapMIB,
       "mmTrapTempC": mmTrapTempC,
       "mmTrapVoltC": mmTrapVoltC,
       "mmTrapTampC": mmTrapTampC,
       "mmTrapMffC": mmTrapMffC,
       "mmTrapPsC": mmTrapPsC,
       "mTrapHdC": mTrapHdC,
       "mmTrapVrmC": mmTrapVrmC,
       "mmTrapLogFullN": mmTrapLogFullN,
       "mmTrapRdpsN": mmTrapRdpsN,
       "mmTrapSffC": mmTrapSffC,
       "mmTrapTempN": mmTrapTempN,
       "mmTrapVoltN": mmTrapVoltN,
       "mmTrapSecDvS": mmTrapSecDvS,
       "mmTrapPostToS": mmTrapPostToS,
       "mmTrapOsToS": mmTrapOsToS,
       "mmTrapAppS": mmTrapAppS,
       "mmTrapPoffS": mmTrapPoffS,
       "mmTrapPonS": mmTrapPonS,
       "mmTrapBootS": mmTrapBootS,
       "mmTrapLdrToS": mmTrapLdrToS,
       "mmTrapPFAS": mmTrapPFAS,
       "mmTrapRemoteLoginS": mmTrapRemoteLoginS,
       "mmTrapMsC": mmTrapMsC,
       "mmTrapRmN": mmTrapRmN,
       "mmTrapKVMSwitchS": mmTrapKVMSwitchS,
       "mmTrapSysInvS": mmTrapSysInvS,
       "mmTrapSysLogS": mmTrapSysLogS,
       "mmTrapIhcC": mmTrapIhcC,
       "mmTrapNwChangeS": mmTrapNwChangeS,
       "mmTrapBlThrS": mmTrapBlThrS,
       "mmTrapPwrMgntS": mmTrapPwrMgntS,
       "mmTrapBladeC": mmTrapBladeC,
       "mmTrapIOC": mmTrapIOC,
       "mmTrapChassisC": mmTrapChassisC,
       "mmTrapStorageC": mmTrapStorageC,
       "mmTrapFanC": mmTrapFanC,
       "mmTrapBladeN": mmTrapBladeN,
       "mmTrapION": mmTrapION,
       "mmTrapChassisN": mmTrapChassisN,
       "mmTrapStorageN": mmTrapStorageN,
       "mmTrapPowerN": mmTrapPowerN,
       "mmTrapFanN": mmTrapFanN,
       "mmTrapBladeS": mmTrapBladeS,
       "mmTrapIOS": mmTrapIOS,
       "mmTrapChassisS": mmTrapChassisS,
       "mmTrapStorageS": mmTrapStorageS,
       "mmTrapPowerS": mmTrapPowerS,
       "mmTrapFanS": mmTrapFanS,
       "mmTrapPwrDOS": mmTrapPwrDOS,
       "remoteSupTrapMibObjects": remoteSupTrapMibObjects,
       "spTrapInfo": spTrapInfo,
       "spTrapDateTime": spTrapDateTime,
       "spTrapAppId": spTrapAppId,
       "spTrapSpTxtId": spTrapSpTxtId,
       "spTrapSysUuid": spTrapSysUuid,
       "spTrapSysSern": spTrapSysSern,
       "spTrapAppType": spTrapAppType,
       "spTrapPriority": spTrapPriority,
       "spTrapMsgText": spTrapMsgText,
       "spTrapHostContact": spTrapHostContact,
       "spTrapHostLocation": spTrapHostLocation,
       "spTrapBladeName": spTrapBladeName,
       "spTrapBladeSern": spTrapBladeSern,
       "spTrapBladeUuid": spTrapBladeUuid,
       "spTrapEvtName": spTrapEvtName,
       "spTrapSourceId": spTrapSourceId,
       "spTrapCallHomeFlag": spTrapCallHomeFlag,
       "spTrapSysIPAddress": spTrapSysIPAddress,
       "spTrapSysMachineModel": spTrapSysMachineModel,
       "spTrapBladeMachineModel": spTrapBladeMachineModel,
       "spTrapBladeFRUSerialNumber": spTrapBladeFRUSerialNumber,
       "spTrapBladeEvtName": spTrapBladeEvtName,
       "spBladeEventDataSource": spBladeEventDataSource,
       "spTrapAuxData": spTrapAuxData,
       "spTrapComponentID": spTrapComponentID,
       "spTrapComponentFRUInfo": spTrapComponentFRUInfo,
       "spTrapChassisName": spTrapChassisName,
       "spTrapSysRoomId": spTrapSysRoomId,
       "spTrapSysRackId": spTrapSysRackId,
       "spTrapSysRackU": spTrapSysRackU,
       "spTrapServiceableEventFlag": spTrapServiceableEventFlag,
       "spLogSequenceNum": spLogSequenceNum,
       "spCimMsgID": spCimMsgID,
       "spCimMsgPrefix": spCimMsgPrefix,
       "spEventCorrelator": spEventCorrelator}
)
