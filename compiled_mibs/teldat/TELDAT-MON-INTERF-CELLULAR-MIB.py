# SNMP MIB module (TELDAT-MON-INTERF-CELLULAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teldat\TELDAT-MON-INTERF-CELLULAR-MIB

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

(telProdNpMonInterfRouter,) = mibBuilder.importSymbols(
    "TELDAT-SW-STRUCTURE-MIB",
    "telProdNpMonInterfRouter")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TelProdNpMonInterfCellular_ObjectIdentity = ObjectIdentity
telProdNpMonInterfCellular = _TelProdNpMonInterfCellular_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18)
)
_TeldatCellularInfoInterfaceTable_Object = MibTable
teldatCellularInfoInterfaceTable = _TeldatCellularInfoInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1)
)
if mibBuilder.loadTexts:
    teldatCellularInfoInterfaceTable.setStatus("mandatory")
_TeldatCellularInfoInterfaceEntry_Object = MibTableRow
teldatCellularInfoInterfaceEntry = _TeldatCellularInfoInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1)
)
teldatCellularInfoInterfaceEntry.setIndexNames(
    (0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularInfoInterfaceIndex"),
)
if mibBuilder.loadTexts:
    teldatCellularInfoInterfaceEntry.setStatus("mandatory")


class _TeldatCellularInfoInterfaceIndex_Type(Integer32):
    """Custom type teldatCellularInfoInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TeldatCellularInfoInterfaceIndex_Type.__name__ = "Integer32"
_TeldatCellularInfoInterfaceIndex_Object = MibTableColumn
teldatCellularInfoInterfaceIndex = _TeldatCellularInfoInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 1),
    _TeldatCellularInfoInterfaceIndex_Type()
)
teldatCellularInfoInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularInfoInterfaceIndex.setStatus("mandatory")
_TeldatCellularInfoInterfaceModuleManufacturer_Type = DisplayString
_TeldatCellularInfoInterfaceModuleManufacturer_Object = MibTableColumn
teldatCellularInfoInterfaceModuleManufacturer = _TeldatCellularInfoInterfaceModuleManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 2),
    _TeldatCellularInfoInterfaceModuleManufacturer_Type()
)
teldatCellularInfoInterfaceModuleManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularInfoInterfaceModuleManufacturer.setStatus("mandatory")
_TeldatCellularInfoInterfaceModuleModel_Type = DisplayString
_TeldatCellularInfoInterfaceModuleModel_Object = MibTableColumn
teldatCellularInfoInterfaceModuleModel = _TeldatCellularInfoInterfaceModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 3),
    _TeldatCellularInfoInterfaceModuleModel_Type()
)
teldatCellularInfoInterfaceModuleModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularInfoInterfaceModuleModel.setStatus("mandatory")
_TeldatCellularInfoInterfaceModuleFirmware_Type = DisplayString
_TeldatCellularInfoInterfaceModuleFirmware_Object = MibTableColumn
teldatCellularInfoInterfaceModuleFirmware = _TeldatCellularInfoInterfaceModuleFirmware_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 4),
    _TeldatCellularInfoInterfaceModuleFirmware_Type()
)
teldatCellularInfoInterfaceModuleFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularInfoInterfaceModuleFirmware.setStatus("mandatory")
_TeldatCellularInfoInterfaceModuleIMEI_Type = DisplayString
_TeldatCellularInfoInterfaceModuleIMEI_Object = MibTableColumn
teldatCellularInfoInterfaceModuleIMEI = _TeldatCellularInfoInterfaceModuleIMEI_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 5),
    _TeldatCellularInfoInterfaceModuleIMEI_Type()
)
teldatCellularInfoInterfaceModuleIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularInfoInterfaceModuleIMEI.setStatus("mandatory")
_TeldatCellularInfoInterfaceModuleIMSI_Type = DisplayString
_TeldatCellularInfoInterfaceModuleIMSI_Object = MibTableColumn
teldatCellularInfoInterfaceModuleIMSI = _TeldatCellularInfoInterfaceModuleIMSI_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 6),
    _TeldatCellularInfoInterfaceModuleIMSI_Type()
)
teldatCellularInfoInterfaceModuleIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularInfoInterfaceModuleIMSI.setStatus("mandatory")
_TeldatCellularInfoInterfaceSIMId_Type = DisplayString
_TeldatCellularInfoInterfaceSIMId_Object = MibTableColumn
teldatCellularInfoInterfaceSIMId = _TeldatCellularInfoInterfaceSIMId_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 7),
    _TeldatCellularInfoInterfaceSIMId_Type()
)
teldatCellularInfoInterfaceSIMId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularInfoInterfaceSIMId.setStatus("mandatory")
_TeldatCellularInfoInterfaceSIMIcc_Type = DisplayString
_TeldatCellularInfoInterfaceSIMIcc_Object = MibTableColumn
teldatCellularInfoInterfaceSIMIcc = _TeldatCellularInfoInterfaceSIMIcc_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 1, 1, 8),
    _TeldatCellularInfoInterfaceSIMIcc_Type()
)
teldatCellularInfoInterfaceSIMIcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularInfoInterfaceSIMIcc.setStatus("mandatory")
_TeldatCellularStatObject_ObjectIdentity = ObjectIdentity
teldatCellularStatObject = _TeldatCellularStatObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3)
)
_TeldatCellularStateInterfaceTable_Object = MibTable
teldatCellularStateInterfaceTable = _TeldatCellularStateInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1)
)
if mibBuilder.loadTexts:
    teldatCellularStateInterfaceTable.setStatus("mandatory")
_TeldatCellularStateInterfaceEntry_Object = MibTableRow
teldatCellularStateInterfaceEntry = _TeldatCellularStateInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1)
)
teldatCellularStateInterfaceEntry.setIndexNames(
    (0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularStateInterfaceIndex"),
)
if mibBuilder.loadTexts:
    teldatCellularStateInterfaceEntry.setStatus("mandatory")


class _TeldatCellularStateInterfaceIndex_Type(Integer32):
    """Custom type teldatCellularStateInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TeldatCellularStateInterfaceIndex_Type.__name__ = "Integer32"
_TeldatCellularStateInterfaceIndex_Object = MibTableColumn
teldatCellularStateInterfaceIndex = _TeldatCellularStateInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 1),
    _TeldatCellularStateInterfaceIndex_Type()
)
teldatCellularStateInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateInterfaceIndex.setStatus("mandatory")
_TeldatCellularStateInterfaceState_Type = DisplayString
_TeldatCellularStateInterfaceState_Object = MibTableColumn
teldatCellularStateInterfaceState = _TeldatCellularStateInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 2),
    _TeldatCellularStateInterfaceState_Type()
)
teldatCellularStateInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateInterfaceState.setStatus("mandatory")
_TeldatCellularStateInterfaceDropPing_Type = Gauge32
_TeldatCellularStateInterfaceDropPing_Object = MibTableColumn
teldatCellularStateInterfaceDropPing = _TeldatCellularStateInterfaceDropPing_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 3),
    _TeldatCellularStateInterfaceDropPing_Type()
)
teldatCellularStateInterfaceDropPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateInterfaceDropPing.setStatus("mandatory")
_TeldatCellularStateInterfaceDropTrace_Type = Gauge32
_TeldatCellularStateInterfaceDropTrace_Object = MibTableColumn
teldatCellularStateInterfaceDropTrace = _TeldatCellularStateInterfaceDropTrace_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 4),
    _TeldatCellularStateInterfaceDropTrace_Type()
)
teldatCellularStateInterfaceDropTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateInterfaceDropTrace.setStatus("mandatory")
_TeldatCellularStateInterfaceDropTraffic_Type = Gauge32
_TeldatCellularStateInterfaceDropTraffic_Object = MibTableColumn
teldatCellularStateInterfaceDropTraffic = _TeldatCellularStateInterfaceDropTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 5),
    _TeldatCellularStateInterfaceDropTraffic_Type()
)
teldatCellularStateInterfaceDropTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateInterfaceDropTraffic.setStatus("mandatory")
_TeldatCellularStateInterfaceTConnTime_Type = Gauge32
_TeldatCellularStateInterfaceTConnTime_Object = MibTableColumn
teldatCellularStateInterfaceTConnTime = _TeldatCellularStateInterfaceTConnTime_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 6),
    _TeldatCellularStateInterfaceTConnTime_Type()
)
teldatCellularStateInterfaceTConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateInterfaceTConnTime.setStatus("mandatory")
_TeldatCellularStateInterfaceCConnTime_Type = Gauge32
_TeldatCellularStateInterfaceCConnTime_Object = MibTableColumn
teldatCellularStateInterfaceCConnTime = _TeldatCellularStateInterfaceCConnTime_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 7),
    _TeldatCellularStateInterfaceCConnTime_Type()
)
teldatCellularStateInterfaceCConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateInterfaceCConnTime.setStatus("mandatory")
_TeldatCellularStateInterfaceCurDial_Type = DisplayString
_TeldatCellularStateInterfaceCurDial_Object = MibTableColumn
teldatCellularStateInterfaceCurDial = _TeldatCellularStateInterfaceCurDial_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 8),
    _TeldatCellularStateInterfaceCurDial_Type()
)
teldatCellularStateInterfaceCurDial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateInterfaceCurDial.setStatus("mandatory")
_TeldatCellularStateInterfaceNCall_Type = Gauge32
_TeldatCellularStateInterfaceNCall_Object = MibTableColumn
teldatCellularStateInterfaceNCall = _TeldatCellularStateInterfaceNCall_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 9),
    _TeldatCellularStateInterfaceNCall_Type()
)
teldatCellularStateInterfaceNCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateInterfaceNCall.setStatus("mandatory")
_TeldatCellularStateInterfaceDestination_Type = DisplayString
_TeldatCellularStateInterfaceDestination_Object = MibTableColumn
teldatCellularStateInterfaceDestination = _TeldatCellularStateInterfaceDestination_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 10),
    _TeldatCellularStateInterfaceDestination_Type()
)
teldatCellularStateInterfaceDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateInterfaceDestination.setStatus("mandatory")
_TeldatCellularStateInterfaceTime2Sp_Type = Gauge32
_TeldatCellularStateInterfaceTime2Sp_Object = MibTableColumn
teldatCellularStateInterfaceTime2Sp = _TeldatCellularStateInterfaceTime2Sp_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 1, 1, 11),
    _TeldatCellularStateInterfaceTime2Sp_Type()
)
teldatCellularStateInterfaceTime2Sp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateInterfaceTime2Sp.setStatus("mandatory")
_TeldatCellularStateMobileTable_Object = MibTable
teldatCellularStateMobileTable = _TeldatCellularStateMobileTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2)
)
if mibBuilder.loadTexts:
    teldatCellularStateMobileTable.setStatus("mandatory")
_TeldatCellularStateMobileEntry_Object = MibTableRow
teldatCellularStateMobileEntry = _TeldatCellularStateMobileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1)
)
teldatCellularStateMobileEntry.setIndexNames(
    (0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularStateMobileIndex"),
)
if mibBuilder.loadTexts:
    teldatCellularStateMobileEntry.setStatus("mandatory")


class _TeldatCellularStateMobileIndex_Type(Integer32):
    """Custom type teldatCellularStateMobileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TeldatCellularStateMobileIndex_Type.__name__ = "Integer32"
_TeldatCellularStateMobileIndex_Object = MibTableColumn
teldatCellularStateMobileIndex = _TeldatCellularStateMobileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 1),
    _TeldatCellularStateMobileIndex_Type()
)
teldatCellularStateMobileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileIndex.setStatus("mandatory")


class _TeldatCellularStateMobileRegistrationState_Type(Integer32):
    """Custom type teldatCellularStateMobileRegistrationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("searching", 0),
          ("home-network", 1),
          ("attaching", 2),
          ("denied", 3),
          ("unknown", 4),
          ("roaming", 5))
    )


_TeldatCellularStateMobileRegistrationState_Type.__name__ = "Integer32"
_TeldatCellularStateMobileRegistrationState_Object = MibTableColumn
teldatCellularStateMobileRegistrationState = _TeldatCellularStateMobileRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 2),
    _TeldatCellularStateMobileRegistrationState_Type()
)
teldatCellularStateMobileRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileRegistrationState.setStatus("mandatory")
_TeldatCellularStateMobilePublicLandMobileNtwCode_Type = Integer32
_TeldatCellularStateMobilePublicLandMobileNtwCode_Object = MibTableColumn
teldatCellularStateMobilePublicLandMobileNtwCode = _TeldatCellularStateMobilePublicLandMobileNtwCode_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 3),
    _TeldatCellularStateMobilePublicLandMobileNtwCode_Type()
)
teldatCellularStateMobilePublicLandMobileNtwCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobilePublicLandMobileNtwCode.setStatus("mandatory")
_TeldatCellularStateMobileCellLocationAreaCode_Type = Gauge32
_TeldatCellularStateMobileCellLocationAreaCode_Object = MibTableColumn
teldatCellularStateMobileCellLocationAreaCode = _TeldatCellularStateMobileCellLocationAreaCode_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 4),
    _TeldatCellularStateMobileCellLocationAreaCode_Type()
)
teldatCellularStateMobileCellLocationAreaCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileCellLocationAreaCode.setStatus("mandatory")
_TeldatCellularStateMobileCellId_Type = Gauge32
_TeldatCellularStateMobileCellId_Object = MibTableColumn
teldatCellularStateMobileCellId = _TeldatCellularStateMobileCellId_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 5),
    _TeldatCellularStateMobileCellId_Type()
)
teldatCellularStateMobileCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileCellId.setStatus("mandatory")
_TeldatCellularStateMobileRadioTechnology_Type = DisplayString
_TeldatCellularStateMobileRadioTechnology_Object = MibTableColumn
teldatCellularStateMobileRadioTechnology = _TeldatCellularStateMobileRadioTechnology_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 6),
    _TeldatCellularStateMobileRadioTechnology_Type()
)
teldatCellularStateMobileRadioTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileRadioTechnology.setStatus("mandatory")
_TeldatCellularStateMobileRadioBand_Type = DisplayString
_TeldatCellularStateMobileRadioBand_Object = MibTableColumn
teldatCellularStateMobileRadioBand = _TeldatCellularStateMobileRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 7),
    _TeldatCellularStateMobileRadioBand_Type()
)
teldatCellularStateMobileRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileRadioBand.setStatus("mandatory")
_TeldatCellularStateMobileRxSignalCodePwr_Type = Integer32
_TeldatCellularStateMobileRxSignalCodePwr_Object = MibTableColumn
teldatCellularStateMobileRxSignalCodePwr = _TeldatCellularStateMobileRxSignalCodePwr_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 8),
    _TeldatCellularStateMobileRxSignalCodePwr_Type()
)
teldatCellularStateMobileRxSignalCodePwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileRxSignalCodePwr.setStatus("mandatory")
_TeldatCellularStateMobileEnergyChipByPwrdnsty_Type = Integer32
_TeldatCellularStateMobileEnergyChipByPwrdnsty_Object = MibTableColumn
teldatCellularStateMobileEnergyChipByPwrdnsty = _TeldatCellularStateMobileEnergyChipByPwrdnsty_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 9),
    _TeldatCellularStateMobileEnergyChipByPwrdnsty_Type()
)
teldatCellularStateMobileEnergyChipByPwrdnsty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileEnergyChipByPwrdnsty.setStatus("mandatory")
_TeldatCellularStateMobileSignalQuality_Type = Integer32
_TeldatCellularStateMobileSignalQuality_Object = MibTableColumn
teldatCellularStateMobileSignalQuality = _TeldatCellularStateMobileSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 10),
    _TeldatCellularStateMobileSignalQuality_Type()
)
teldatCellularStateMobileSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileSignalQuality.setStatus("mandatory")
_TeldatCellularStateMobileTemperature_Type = Integer32
_TeldatCellularStateMobileTemperature_Object = MibTableColumn
teldatCellularStateMobileTemperature = _TeldatCellularStateMobileTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 11),
    _TeldatCellularStateMobileTemperature_Type()
)
teldatCellularStateMobileTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileTemperature.setStatus("mandatory")
_TeldatCellularStateMobileRxPackets_Type = Gauge32
_TeldatCellularStateMobileRxPackets_Object = MibTableColumn
teldatCellularStateMobileRxPackets = _TeldatCellularStateMobileRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 12),
    _TeldatCellularStateMobileRxPackets_Type()
)
teldatCellularStateMobileRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileRxPackets.setStatus("mandatory")
_TeldatCellularStateMobileRxBytes_Type = Gauge32
_TeldatCellularStateMobileRxBytes_Object = MibTableColumn
teldatCellularStateMobileRxBytes = _TeldatCellularStateMobileRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 13),
    _TeldatCellularStateMobileRxBytes_Type()
)
teldatCellularStateMobileRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileRxBytes.setStatus("mandatory")
_TeldatCellularStateMobileTxPackets_Type = Gauge32
_TeldatCellularStateMobileTxPackets_Object = MibTableColumn
teldatCellularStateMobileTxPackets = _TeldatCellularStateMobileTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 14),
    _TeldatCellularStateMobileTxPackets_Type()
)
teldatCellularStateMobileTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileTxPackets.setStatus("mandatory")
_TeldatCellularStateMobileTxBytes_Type = Gauge32
_TeldatCellularStateMobileTxBytes_Object = MibTableColumn
teldatCellularStateMobileTxBytes = _TeldatCellularStateMobileTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 15),
    _TeldatCellularStateMobileTxBytes_Type()
)
teldatCellularStateMobileTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileTxBytes.setStatus("mandatory")
_TeldatCellularStateMobileRxBpsLast1s_Type = Gauge32
_TeldatCellularStateMobileRxBpsLast1s_Object = MibTableColumn
teldatCellularStateMobileRxBpsLast1s = _TeldatCellularStateMobileRxBpsLast1s_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 16),
    _TeldatCellularStateMobileRxBpsLast1s_Type()
)
teldatCellularStateMobileRxBpsLast1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileRxBpsLast1s.setStatus("mandatory")
_TeldatCellularStateMobileTxBpsLast1s_Type = Gauge32
_TeldatCellularStateMobileTxBpsLast1s_Object = MibTableColumn
teldatCellularStateMobileTxBpsLast1s = _TeldatCellularStateMobileTxBpsLast1s_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 17),
    _TeldatCellularStateMobileTxBpsLast1s_Type()
)
teldatCellularStateMobileTxBpsLast1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileTxBpsLast1s.setStatus("mandatory")
_TeldatCellularStateMobileRxBpsLast1m_Type = Gauge32
_TeldatCellularStateMobileRxBpsLast1m_Object = MibTableColumn
teldatCellularStateMobileRxBpsLast1m = _TeldatCellularStateMobileRxBpsLast1m_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 18),
    _TeldatCellularStateMobileRxBpsLast1m_Type()
)
teldatCellularStateMobileRxBpsLast1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileRxBpsLast1m.setStatus("mandatory")
_TeldatCellularStateMobileTxBpsLast1m_Type = Gauge32
_TeldatCellularStateMobileTxBpsLast1m_Object = MibTableColumn
teldatCellularStateMobileTxBpsLast1m = _TeldatCellularStateMobileTxBpsLast1m_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 19),
    _TeldatCellularStateMobileTxBpsLast1m_Type()
)
teldatCellularStateMobileTxBpsLast1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileTxBpsLast1m.setStatus("mandatory")
_TeldatCellularStateMobileRxBpsLast5m_Type = Gauge32
_TeldatCellularStateMobileRxBpsLast5m_Object = MibTableColumn
teldatCellularStateMobileRxBpsLast5m = _TeldatCellularStateMobileRxBpsLast5m_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 20),
    _TeldatCellularStateMobileRxBpsLast5m_Type()
)
teldatCellularStateMobileRxBpsLast5m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileRxBpsLast5m.setStatus("mandatory")
_TeldatCellularStateMobileTxBpsLast5m_Type = Gauge32
_TeldatCellularStateMobileTxBpsLast5m_Object = MibTableColumn
teldatCellularStateMobileTxBpsLast5m = _TeldatCellularStateMobileTxBpsLast5m_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 21),
    _TeldatCellularStateMobileTxBpsLast5m_Type()
)
teldatCellularStateMobileTxBpsLast5m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileTxBpsLast5m.setStatus("mandatory")
_TeldatCellularStateMobileRxRSRP_Type = Integer32
_TeldatCellularStateMobileRxRSRP_Object = MibTableColumn
teldatCellularStateMobileRxRSRP = _TeldatCellularStateMobileRxRSRP_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 22),
    _TeldatCellularStateMobileRxRSRP_Type()
)
teldatCellularStateMobileRxRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileRxRSRP.setStatus("mandatory")
_TeldatCellularStateMobileRxRSRQ_Type = Integer32
_TeldatCellularStateMobileRxRSRQ_Object = MibTableColumn
teldatCellularStateMobileRxRSRQ = _TeldatCellularStateMobileRxRSRQ_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 23),
    _TeldatCellularStateMobileRxRSRQ_Type()
)
teldatCellularStateMobileRxRSRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileRxRSRQ.setStatus("mandatory")
_TeldatCellularStateMobileRxSINR_Type = Integer32
_TeldatCellularStateMobileRxSINR_Object = MibTableColumn
teldatCellularStateMobileRxSINR = _TeldatCellularStateMobileRxSINR_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 24),
    _TeldatCellularStateMobileRxSINR_Type()
)
teldatCellularStateMobileRxSINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileRxSINR.setStatus("mandatory")
_TeldatCellularStateMobileLTECellId_Type = Gauge32
_TeldatCellularStateMobileLTECellId_Object = MibTableColumn
teldatCellularStateMobileLTECellId = _TeldatCellularStateMobileLTECellId_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 2, 1, 25),
    _TeldatCellularStateMobileLTECellId_Type()
)
teldatCellularStateMobileLTECellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularStateMobileLTECellId.setStatus("mandatory")
_TeldatCellularSIMMngTable_Object = MibTable
teldatCellularSIMMngTable = _TeldatCellularSIMMngTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3)
)
if mibBuilder.loadTexts:
    teldatCellularSIMMngTable.setStatus("mandatory")
_TeldatCellularSIMMngEntry_Object = MibTableRow
teldatCellularSIMMngEntry = _TeldatCellularSIMMngEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1)
)
teldatCellularSIMMngEntry.setIndexNames(
    (0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularSIMMngIndex"),
)
if mibBuilder.loadTexts:
    teldatCellularSIMMngEntry.setStatus("mandatory")


class _TeldatCellularSIMMngIndex_Type(Integer32):
    """Custom type teldatCellularSIMMngIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TeldatCellularSIMMngIndex_Type.__name__ = "Integer32"
_TeldatCellularSIMMngIndex_Object = MibTableColumn
teldatCellularSIMMngIndex = _TeldatCellularSIMMngIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 1),
    _TeldatCellularSIMMngIndex_Type()
)
teldatCellularSIMMngIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularSIMMngIndex.setStatus("mandatory")


class _TeldatCellularSIMMngCurrentSIMSocket_Type(Integer32):
    """Custom type teldatCellularSIMMngCurrentSIMSocket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("external-socket1", 0),
          ("internal-socket2", 1))
    )


_TeldatCellularSIMMngCurrentSIMSocket_Type.__name__ = "Integer32"
_TeldatCellularSIMMngCurrentSIMSocket_Object = MibTableColumn
teldatCellularSIMMngCurrentSIMSocket = _TeldatCellularSIMMngCurrentSIMSocket_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 2),
    _TeldatCellularSIMMngCurrentSIMSocket_Type()
)
teldatCellularSIMMngCurrentSIMSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularSIMMngCurrentSIMSocket.setStatus("mandatory")


class _TeldatCellularSIMMngMainSIMSocket_Type(Integer32):
    """Custom type teldatCellularSIMMngMainSIMSocket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("external-socket1", 0),
          ("internal-socket2", 1))
    )


_TeldatCellularSIMMngMainSIMSocket_Type.__name__ = "Integer32"
_TeldatCellularSIMMngMainSIMSocket_Object = MibTableColumn
teldatCellularSIMMngMainSIMSocket = _TeldatCellularSIMMngMainSIMSocket_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 3),
    _TeldatCellularSIMMngMainSIMSocket_Type()
)
teldatCellularSIMMngMainSIMSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularSIMMngMainSIMSocket.setStatus("mandatory")


class _TeldatCellularSIMMngSupervisionSIMSocket_Type(Integer32):
    """Custom type teldatCellularSIMMngSupervisionSIMSocket based on Integer32"""
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


_TeldatCellularSIMMngSupervisionSIMSocket_Type.__name__ = "Integer32"
_TeldatCellularSIMMngSupervisionSIMSocket_Object = MibTableColumn
teldatCellularSIMMngSupervisionSIMSocket = _TeldatCellularSIMMngSupervisionSIMSocket_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 4),
    _TeldatCellularSIMMngSupervisionSIMSocket_Type()
)
teldatCellularSIMMngSupervisionSIMSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularSIMMngSupervisionSIMSocket.setStatus("mandatory")
_TeldatCellularSIMMngSIMImsiInfoSocket1_Type = DisplayString
_TeldatCellularSIMMngSIMImsiInfoSocket1_Object = MibTableColumn
teldatCellularSIMMngSIMImsiInfoSocket1 = _TeldatCellularSIMMngSIMImsiInfoSocket1_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 5),
    _TeldatCellularSIMMngSIMImsiInfoSocket1_Type()
)
teldatCellularSIMMngSIMImsiInfoSocket1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularSIMMngSIMImsiInfoSocket1.setStatus("mandatory")
_TeldatCellularSIMMngSIMIdInfoSocket1_Type = DisplayString
_TeldatCellularSIMMngSIMIdInfoSocket1_Object = MibTableColumn
teldatCellularSIMMngSIMIdInfoSocket1 = _TeldatCellularSIMMngSIMIdInfoSocket1_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 6),
    _TeldatCellularSIMMngSIMIdInfoSocket1_Type()
)
teldatCellularSIMMngSIMIdInfoSocket1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularSIMMngSIMIdInfoSocket1.setStatus("mandatory")
_TeldatCellularSIMMngSIMImsiInfoSocket2_Type = DisplayString
_TeldatCellularSIMMngSIMImsiInfoSocket2_Object = MibTableColumn
teldatCellularSIMMngSIMImsiInfoSocket2 = _TeldatCellularSIMMngSIMImsiInfoSocket2_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 7),
    _TeldatCellularSIMMngSIMImsiInfoSocket2_Type()
)
teldatCellularSIMMngSIMImsiInfoSocket2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularSIMMngSIMImsiInfoSocket2.setStatus("mandatory")
_TeldatCellularSIMMngSIMIdInfoSocket2_Type = DisplayString
_TeldatCellularSIMMngSIMIdInfoSocket2_Object = MibTableColumn
teldatCellularSIMMngSIMIdInfoSocket2 = _TeldatCellularSIMMngSIMIdInfoSocket2_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 3, 1, 8),
    _TeldatCellularSIMMngSIMIdInfoSocket2_Type()
)
teldatCellularSIMMngSIMIdInfoSocket2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularSIMMngSIMIdInfoSocket2.setStatus("mandatory")
_TeldatCellularProfDialTable_Object = MibTable
teldatCellularProfDialTable = _TeldatCellularProfDialTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4)
)
if mibBuilder.loadTexts:
    teldatCellularProfDialTable.setStatus("mandatory")
_TeldatCellularProfDialEntry_Object = MibTableRow
teldatCellularProfDialEntry = _TeldatCellularProfDialEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1)
)
teldatCellularProfDialEntry.setIndexNames(
    (0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularProfDialIfcIndex"),
)
if mibBuilder.loadTexts:
    teldatCellularProfDialEntry.setStatus("mandatory")


class _TeldatCellularProfDialIfcIndex_Type(Integer32):
    """Custom type teldatCellularProfDialIfcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TeldatCellularProfDialIfcIndex_Type.__name__ = "Integer32"
_TeldatCellularProfDialIfcIndex_Object = MibTableColumn
teldatCellularProfDialIfcIndex = _TeldatCellularProfDialIfcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 1),
    _TeldatCellularProfDialIfcIndex_Type()
)
teldatCellularProfDialIfcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularProfDialIfcIndex.setStatus("mandatory")
_TeldatCellularProfDialName1_Type = DisplayString
_TeldatCellularProfDialName1_Object = MibTableColumn
teldatCellularProfDialName1 = _TeldatCellularProfDialName1_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 2),
    _TeldatCellularProfDialName1_Type()
)
teldatCellularProfDialName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularProfDialName1.setStatus("mandatory")
_TeldatCellularProfDialAPN1_Type = DisplayString
_TeldatCellularProfDialAPN1_Object = MibTableColumn
teldatCellularProfDialAPN1 = _TeldatCellularProfDialAPN1_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 3),
    _TeldatCellularProfDialAPN1_Type()
)
teldatCellularProfDialAPN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularProfDialAPN1.setStatus("mandatory")
_TeldatCellularProfDialName2_Type = DisplayString
_TeldatCellularProfDialName2_Object = MibTableColumn
teldatCellularProfDialName2 = _TeldatCellularProfDialName2_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 4),
    _TeldatCellularProfDialName2_Type()
)
teldatCellularProfDialName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularProfDialName2.setStatus("mandatory")
_TeldatCellularProfDialAPN2_Type = DisplayString
_TeldatCellularProfDialAPN2_Object = MibTableColumn
teldatCellularProfDialAPN2 = _TeldatCellularProfDialAPN2_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 4, 1, 5),
    _TeldatCellularProfDialAPN2_Type()
)
teldatCellularProfDialAPN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularProfDialAPN2.setStatus("mandatory")
_TeldatCellularRecChangesTable_Object = MibTable
teldatCellularRecChangesTable = _TeldatCellularRecChangesTable_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5)
)
if mibBuilder.loadTexts:
    teldatCellularRecChangesTable.setStatus("mandatory")
_TeldatCellularRecChangesEntry_Object = MibTableRow
teldatCellularRecChangesEntry = _TeldatCellularRecChangesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5, 1)
)
teldatCellularRecChangesEntry.setIndexNames(
    (0, "TELDAT-MON-INTERF-CELLULAR-MIB", "teldatCellularRecChangesIfcIndex"),
)
if mibBuilder.loadTexts:
    teldatCellularRecChangesEntry.setStatus("mandatory")


class _TeldatCellularRecChangesIfcIndex_Type(Integer32):
    """Custom type teldatCellularRecChangesIfcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TeldatCellularRecChangesIfcIndex_Type.__name__ = "Integer32"
_TeldatCellularRecChangesIfcIndex_Object = MibTableColumn
teldatCellularRecChangesIfcIndex = _TeldatCellularRecChangesIfcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5, 1, 1),
    _TeldatCellularRecChangesIfcIndex_Type()
)
teldatCellularRecChangesIfcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularRecChangesIfcIndex.setStatus("mandatory")
_TeldatCellularRecChangesPLMNTimeStamp_Type = DisplayString
_TeldatCellularRecChangesPLMNTimeStamp_Object = MibTableColumn
teldatCellularRecChangesPLMNTimeStamp = _TeldatCellularRecChangesPLMNTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5, 1, 2),
    _TeldatCellularRecChangesPLMNTimeStamp_Type()
)
teldatCellularRecChangesPLMNTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularRecChangesPLMNTimeStamp.setStatus("mandatory")
_TeldatCellularRecChangesPLMNCode_Type = DisplayString
_TeldatCellularRecChangesPLMNCode_Object = MibTableColumn
teldatCellularRecChangesPLMNCode = _TeldatCellularRecChangesPLMNCode_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 2, 2, 18, 3, 5, 1, 3),
    _TeldatCellularRecChangesPLMNCode_Type()
)
teldatCellularRecChangesPLMNCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCellularRecChangesPLMNCode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELDAT-MON-INTERF-CELLULAR-MIB",
    **{"telProdNpMonInterfCellular": telProdNpMonInterfCellular,
       "teldatCellularInfoInterfaceTable": teldatCellularInfoInterfaceTable,
       "teldatCellularInfoInterfaceEntry": teldatCellularInfoInterfaceEntry,
       "teldatCellularInfoInterfaceIndex": teldatCellularInfoInterfaceIndex,
       "teldatCellularInfoInterfaceModuleManufacturer": teldatCellularInfoInterfaceModuleManufacturer,
       "teldatCellularInfoInterfaceModuleModel": teldatCellularInfoInterfaceModuleModel,
       "teldatCellularInfoInterfaceModuleFirmware": teldatCellularInfoInterfaceModuleFirmware,
       "teldatCellularInfoInterfaceModuleIMEI": teldatCellularInfoInterfaceModuleIMEI,
       "teldatCellularInfoInterfaceModuleIMSI": teldatCellularInfoInterfaceModuleIMSI,
       "teldatCellularInfoInterfaceSIMId": teldatCellularInfoInterfaceSIMId,
       "teldatCellularInfoInterfaceSIMIcc": teldatCellularInfoInterfaceSIMIcc,
       "teldatCellularStatObject": teldatCellularStatObject,
       "teldatCellularStateInterfaceTable": teldatCellularStateInterfaceTable,
       "teldatCellularStateInterfaceEntry": teldatCellularStateInterfaceEntry,
       "teldatCellularStateInterfaceIndex": teldatCellularStateInterfaceIndex,
       "teldatCellularStateInterfaceState": teldatCellularStateInterfaceState,
       "teldatCellularStateInterfaceDropPing": teldatCellularStateInterfaceDropPing,
       "teldatCellularStateInterfaceDropTrace": teldatCellularStateInterfaceDropTrace,
       "teldatCellularStateInterfaceDropTraffic": teldatCellularStateInterfaceDropTraffic,
       "teldatCellularStateInterfaceTConnTime": teldatCellularStateInterfaceTConnTime,
       "teldatCellularStateInterfaceCConnTime": teldatCellularStateInterfaceCConnTime,
       "teldatCellularStateInterfaceCurDial": teldatCellularStateInterfaceCurDial,
       "teldatCellularStateInterfaceNCall": teldatCellularStateInterfaceNCall,
       "teldatCellularStateInterfaceDestination": teldatCellularStateInterfaceDestination,
       "teldatCellularStateInterfaceTime2Sp": teldatCellularStateInterfaceTime2Sp,
       "teldatCellularStateMobileTable": teldatCellularStateMobileTable,
       "teldatCellularStateMobileEntry": teldatCellularStateMobileEntry,
       "teldatCellularStateMobileIndex": teldatCellularStateMobileIndex,
       "teldatCellularStateMobileRegistrationState": teldatCellularStateMobileRegistrationState,
       "teldatCellularStateMobilePublicLandMobileNtwCode": teldatCellularStateMobilePublicLandMobileNtwCode,
       "teldatCellularStateMobileCellLocationAreaCode": teldatCellularStateMobileCellLocationAreaCode,
       "teldatCellularStateMobileCellId": teldatCellularStateMobileCellId,
       "teldatCellularStateMobileRadioTechnology": teldatCellularStateMobileRadioTechnology,
       "teldatCellularStateMobileRadioBand": teldatCellularStateMobileRadioBand,
       "teldatCellularStateMobileRxSignalCodePwr": teldatCellularStateMobileRxSignalCodePwr,
       "teldatCellularStateMobileEnergyChipByPwrdnsty": teldatCellularStateMobileEnergyChipByPwrdnsty,
       "teldatCellularStateMobileSignalQuality": teldatCellularStateMobileSignalQuality,
       "teldatCellularStateMobileTemperature": teldatCellularStateMobileTemperature,
       "teldatCellularStateMobileRxPackets": teldatCellularStateMobileRxPackets,
       "teldatCellularStateMobileRxBytes": teldatCellularStateMobileRxBytes,
       "teldatCellularStateMobileTxPackets": teldatCellularStateMobileTxPackets,
       "teldatCellularStateMobileTxBytes": teldatCellularStateMobileTxBytes,
       "teldatCellularStateMobileRxBpsLast1s": teldatCellularStateMobileRxBpsLast1s,
       "teldatCellularStateMobileTxBpsLast1s": teldatCellularStateMobileTxBpsLast1s,
       "teldatCellularStateMobileRxBpsLast1m": teldatCellularStateMobileRxBpsLast1m,
       "teldatCellularStateMobileTxBpsLast1m": teldatCellularStateMobileTxBpsLast1m,
       "teldatCellularStateMobileRxBpsLast5m": teldatCellularStateMobileRxBpsLast5m,
       "teldatCellularStateMobileTxBpsLast5m": teldatCellularStateMobileTxBpsLast5m,
       "teldatCellularStateMobileRxRSRP": teldatCellularStateMobileRxRSRP,
       "teldatCellularStateMobileRxRSRQ": teldatCellularStateMobileRxRSRQ,
       "teldatCellularStateMobileRxSINR": teldatCellularStateMobileRxSINR,
       "teldatCellularStateMobileLTECellId": teldatCellularStateMobileLTECellId,
       "teldatCellularSIMMngTable": teldatCellularSIMMngTable,
       "teldatCellularSIMMngEntry": teldatCellularSIMMngEntry,
       "teldatCellularSIMMngIndex": teldatCellularSIMMngIndex,
       "teldatCellularSIMMngCurrentSIMSocket": teldatCellularSIMMngCurrentSIMSocket,
       "teldatCellularSIMMngMainSIMSocket": teldatCellularSIMMngMainSIMSocket,
       "teldatCellularSIMMngSupervisionSIMSocket": teldatCellularSIMMngSupervisionSIMSocket,
       "teldatCellularSIMMngSIMImsiInfoSocket1": teldatCellularSIMMngSIMImsiInfoSocket1,
       "teldatCellularSIMMngSIMIdInfoSocket1": teldatCellularSIMMngSIMIdInfoSocket1,
       "teldatCellularSIMMngSIMImsiInfoSocket2": teldatCellularSIMMngSIMImsiInfoSocket2,
       "teldatCellularSIMMngSIMIdInfoSocket2": teldatCellularSIMMngSIMIdInfoSocket2,
       "teldatCellularProfDialTable": teldatCellularProfDialTable,
       "teldatCellularProfDialEntry": teldatCellularProfDialEntry,
       "teldatCellularProfDialIfcIndex": teldatCellularProfDialIfcIndex,
       "teldatCellularProfDialName1": teldatCellularProfDialName1,
       "teldatCellularProfDialAPN1": teldatCellularProfDialAPN1,
       "teldatCellularProfDialName2": teldatCellularProfDialName2,
       "teldatCellularProfDialAPN2": teldatCellularProfDialAPN2,
       "teldatCellularRecChangesTable": teldatCellularRecChangesTable,
       "teldatCellularRecChangesEntry": teldatCellularRecChangesEntry,
       "teldatCellularRecChangesIfcIndex": teldatCellularRecChangesIfcIndex,
       "teldatCellularRecChangesPLMNTimeStamp": teldatCellularRecChangesPLMNTimeStamp,
       "teldatCellularRecChangesPLMNCode": teldatCellularRecChangesPLMNCode}
)
