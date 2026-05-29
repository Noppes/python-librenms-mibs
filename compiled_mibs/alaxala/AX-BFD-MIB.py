# SNMP MIB module (AX-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-BFD-MIB

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

(BfdCtrlDestPortNumberTC,
 BfdCtrlSourcePortNumberTC,
 BfdDiagTC,
 BfdIntervalTC,
 BfdMultiplierTC,
 BfdSessAuthenticationTypeTC,
 BfdSessIndexTC,
 BfdSessOperModeTC,
 BfdSessStateTC,
 BfdSessTypeTC,
 BfdSessionAuthenticationKeyTC) = mibBuilder.importSymbols(
    "AX-BFD-TC-MIB",
    "BfdCtrlDestPortNumberTC",
    "BfdCtrlSourcePortNumberTC",
    "BfdDiagTC",
    "BfdIntervalTC",
    "BfdMultiplierTC",
    "BfdSessAuthenticationTypeTC",
    "BfdSessIndexTC",
    "BfdSessOperModeTC",
    "BfdSessStateTC",
    "BfdSessTypeTC",
    "BfdSessionAuthenticationKeyTC")

(axMib,) = mibBuilder.importSymbols(
    "AX-SMI-MIB",
    "axMib")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

axBfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201)
)
if mibBuilder.loadTexts:
    axBfdMIB.setRevisions(
        ("2016-10-13 00:00",
         "2014-07-09 00:01")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxBfdNotifications_ObjectIdentity = ObjectIdentity
axBfdNotifications = _AxBfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 0)
)
_AxBfdObjects_ObjectIdentity = ObjectIdentity
axBfdObjects = _AxBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1)
)
_AxBfdScalarObjects_ObjectIdentity = ObjectIdentity
axBfdScalarObjects = _AxBfdScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 1)
)


class _AxBfdAdminStatus_Type(Integer32):
    """Custom type axBfdAdminStatus based on Integer32"""
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


_AxBfdAdminStatus_Type.__name__ = "Integer32"
_AxBfdAdminStatus_Object = MibScalar
axBfdAdminStatus = _AxBfdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 1, 1),
    _AxBfdAdminStatus_Type()
)
axBfdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    axBfdAdminStatus.setStatus("current")
_AxBfdSessNotificationsEnable_Type = TruthValue
_AxBfdSessNotificationsEnable_Object = MibScalar
axBfdSessNotificationsEnable = _AxBfdSessNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 1, 2),
    _AxBfdSessNotificationsEnable_Type()
)
axBfdSessNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    axBfdSessNotificationsEnable.setStatus("current")
_AxBfdSessTable_Object = MibTable
axBfdSessTable = _AxBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2)
)
if mibBuilder.loadTexts:
    axBfdSessTable.setStatus("current")
_AxBfdSessEntry_Object = MibTableRow
axBfdSessEntry = _AxBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1)
)
axBfdSessEntry.setIndexNames(
    (0, "AX-BFD-MIB", "axBfdSessIndex"),
)
if mibBuilder.loadTexts:
    axBfdSessEntry.setStatus("current")
_AxBfdSessIndex_Type = BfdSessIndexTC
_AxBfdSessIndex_Object = MibTableColumn
axBfdSessIndex = _AxBfdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 1),
    _AxBfdSessIndex_Type()
)
axBfdSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axBfdSessIndex.setStatus("current")


class _AxBfdSessVersionNumber_Type(Unsigned32):
    """Custom type axBfdSessVersionNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AxBfdSessVersionNumber_Type.__name__ = "Unsigned32"
_AxBfdSessVersionNumber_Object = MibTableColumn
axBfdSessVersionNumber = _AxBfdSessVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 2),
    _AxBfdSessVersionNumber_Type()
)
axBfdSessVersionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessVersionNumber.setStatus("current")
_AxBfdSessType_Type = BfdSessTypeTC
_AxBfdSessType_Object = MibTableColumn
axBfdSessType = _AxBfdSessType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 3),
    _AxBfdSessType_Type()
)
axBfdSessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessType.setStatus("current")


class _AxBfdSessDiscriminator_Type(Unsigned32):
    """Custom type axBfdSessDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AxBfdSessDiscriminator_Type.__name__ = "Unsigned32"
_AxBfdSessDiscriminator_Object = MibTableColumn
axBfdSessDiscriminator = _AxBfdSessDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 4),
    _AxBfdSessDiscriminator_Type()
)
axBfdSessDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessDiscriminator.setStatus("current")


class _AxBfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type axBfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_AxBfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_AxBfdSessRemoteDiscr_Object = MibTableColumn
axBfdSessRemoteDiscr = _AxBfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 5),
    _AxBfdSessRemoteDiscr_Type()
)
axBfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessRemoteDiscr.setStatus("current")
_AxBfdSessDestinationUdpPort_Type = BfdCtrlDestPortNumberTC
_AxBfdSessDestinationUdpPort_Object = MibTableColumn
axBfdSessDestinationUdpPort = _AxBfdSessDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 6),
    _AxBfdSessDestinationUdpPort_Type()
)
axBfdSessDestinationUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessDestinationUdpPort.setStatus("current")
_AxBfdSessSourceUdpPort_Type = BfdCtrlSourcePortNumberTC
_AxBfdSessSourceUdpPort_Object = MibTableColumn
axBfdSessSourceUdpPort = _AxBfdSessSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 7),
    _AxBfdSessSourceUdpPort_Type()
)
axBfdSessSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessSourceUdpPort.setStatus("current")
_AxBfdSessEchoSourceUdpPort_Type = InetPortNumber
_AxBfdSessEchoSourceUdpPort_Object = MibTableColumn
axBfdSessEchoSourceUdpPort = _AxBfdSessEchoSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 8),
    _AxBfdSessEchoSourceUdpPort_Type()
)
axBfdSessEchoSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessEchoSourceUdpPort.setStatus("current")


class _AxBfdSessAdminStatus_Type(Integer32):
    """Custom type axBfdSessAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("start", 2))
    )


_AxBfdSessAdminStatus_Type.__name__ = "Integer32"
_AxBfdSessAdminStatus_Object = MibTableColumn
axBfdSessAdminStatus = _AxBfdSessAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 9),
    _AxBfdSessAdminStatus_Type()
)
axBfdSessAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessAdminStatus.setStatus("current")
_AxBfdSessState_Type = BfdSessStateTC
_AxBfdSessState_Object = MibTableColumn
axBfdSessState = _AxBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 10),
    _AxBfdSessState_Type()
)
axBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessState.setStatus("current")
_AxBfdSessRemoteHeardFlag_Type = TruthValue
_AxBfdSessRemoteHeardFlag_Object = MibTableColumn
axBfdSessRemoteHeardFlag = _AxBfdSessRemoteHeardFlag_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 11),
    _AxBfdSessRemoteHeardFlag_Type()
)
axBfdSessRemoteHeardFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessRemoteHeardFlag.setStatus("current")
_AxBfdSessDiag_Type = BfdDiagTC
_AxBfdSessDiag_Object = MibTableColumn
axBfdSessDiag = _AxBfdSessDiag_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 12),
    _AxBfdSessDiag_Type()
)
axBfdSessDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessDiag.setStatus("current")
_AxBfdSessOperMode_Type = BfdSessOperModeTC
_AxBfdSessOperMode_Object = MibTableColumn
axBfdSessOperMode = _AxBfdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 13),
    _AxBfdSessOperMode_Type()
)
axBfdSessOperMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessOperMode.setStatus("current")
_AxBfdSessDemandModeDesiredFlag_Type = TruthValue
_AxBfdSessDemandModeDesiredFlag_Object = MibTableColumn
axBfdSessDemandModeDesiredFlag = _AxBfdSessDemandModeDesiredFlag_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 14),
    _AxBfdSessDemandModeDesiredFlag_Type()
)
axBfdSessDemandModeDesiredFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessDemandModeDesiredFlag.setStatus("current")
_AxBfdSessControlPlaneIndepFlag_Type = TruthValue
_AxBfdSessControlPlaneIndepFlag_Object = MibTableColumn
axBfdSessControlPlaneIndepFlag = _AxBfdSessControlPlaneIndepFlag_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 15),
    _AxBfdSessControlPlaneIndepFlag_Type()
)
axBfdSessControlPlaneIndepFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessControlPlaneIndepFlag.setStatus("current")
_AxBfdSessMultipointFlag_Type = TruthValue
_AxBfdSessMultipointFlag_Object = MibTableColumn
axBfdSessMultipointFlag = _AxBfdSessMultipointFlag_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 16),
    _AxBfdSessMultipointFlag_Type()
)
axBfdSessMultipointFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessMultipointFlag.setStatus("current")
_AxBfdSessInterface_Type = InterfaceIndexOrZero
_AxBfdSessInterface_Object = MibTableColumn
axBfdSessInterface = _AxBfdSessInterface_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 17),
    _AxBfdSessInterface_Type()
)
axBfdSessInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessInterface.setStatus("current")
_AxBfdSessApplicationId_Type = Unsigned32
_AxBfdSessApplicationId_Object = MibTableColumn
axBfdSessApplicationId = _AxBfdSessApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 18),
    _AxBfdSessApplicationId_Type()
)
axBfdSessApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessApplicationId.setStatus("current")
_AxBfdSessSrcAddrType_Type = InetAddressType
_AxBfdSessSrcAddrType_Object = MibTableColumn
axBfdSessSrcAddrType = _AxBfdSessSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 19),
    _AxBfdSessSrcAddrType_Type()
)
axBfdSessSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessSrcAddrType.setStatus("current")
_AxBfdSessSrcAddr_Type = InetAddress
_AxBfdSessSrcAddr_Object = MibTableColumn
axBfdSessSrcAddr = _AxBfdSessSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 20),
    _AxBfdSessSrcAddr_Type()
)
axBfdSessSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessSrcAddr.setStatus("current")
_AxBfdSessDstAddrType_Type = InetAddressType
_AxBfdSessDstAddrType_Object = MibTableColumn
axBfdSessDstAddrType = _AxBfdSessDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 21),
    _AxBfdSessDstAddrType_Type()
)
axBfdSessDstAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessDstAddrType.setStatus("current")
_AxBfdSessDstAddr_Type = InetAddress
_AxBfdSessDstAddr_Object = MibTableColumn
axBfdSessDstAddr = _AxBfdSessDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 22),
    _AxBfdSessDstAddr_Type()
)
axBfdSessDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessDstAddr.setStatus("current")
_AxBfdSessGTSM_Type = TruthValue
_AxBfdSessGTSM_Object = MibTableColumn
axBfdSessGTSM = _AxBfdSessGTSM_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 23),
    _AxBfdSessGTSM_Type()
)
axBfdSessGTSM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessGTSM.setStatus("current")


class _AxBfdSessGTSMTTL_Type(Unsigned32):
    """Custom type axBfdSessGTSMTTL based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AxBfdSessGTSMTTL_Type.__name__ = "Unsigned32"
_AxBfdSessGTSMTTL_Object = MibTableColumn
axBfdSessGTSMTTL = _AxBfdSessGTSMTTL_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 24),
    _AxBfdSessGTSMTTL_Type()
)
axBfdSessGTSMTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessGTSMTTL.setStatus("current")
_AxBfdSessDesiredMinTxInterval_Type = BfdIntervalTC
_AxBfdSessDesiredMinTxInterval_Object = MibTableColumn
axBfdSessDesiredMinTxInterval = _AxBfdSessDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 25),
    _AxBfdSessDesiredMinTxInterval_Type()
)
axBfdSessDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessDesiredMinTxInterval.setStatus("current")
_AxBfdSessReqMinRxInterval_Type = BfdIntervalTC
_AxBfdSessReqMinRxInterval_Object = MibTableColumn
axBfdSessReqMinRxInterval = _AxBfdSessReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 26),
    _AxBfdSessReqMinRxInterval_Type()
)
axBfdSessReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessReqMinRxInterval.setStatus("current")
_AxBfdSessReqMinEchoRxInterval_Type = BfdIntervalTC
_AxBfdSessReqMinEchoRxInterval_Object = MibTableColumn
axBfdSessReqMinEchoRxInterval = _AxBfdSessReqMinEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 27),
    _AxBfdSessReqMinEchoRxInterval_Type()
)
axBfdSessReqMinEchoRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessReqMinEchoRxInterval.setStatus("current")
_AxBfdSessDetectMult_Type = BfdMultiplierTC
_AxBfdSessDetectMult_Object = MibTableColumn
axBfdSessDetectMult = _AxBfdSessDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 28),
    _AxBfdSessDetectMult_Type()
)
axBfdSessDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessDetectMult.setStatus("current")
_AxBfdSessNegotiatedInterval_Type = BfdIntervalTC
_AxBfdSessNegotiatedInterval_Object = MibTableColumn
axBfdSessNegotiatedInterval = _AxBfdSessNegotiatedInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 29),
    _AxBfdSessNegotiatedInterval_Type()
)
axBfdSessNegotiatedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessNegotiatedInterval.setStatus("current")
_AxBfdSessNegotiatedEchoInterval_Type = BfdIntervalTC
_AxBfdSessNegotiatedEchoInterval_Object = MibTableColumn
axBfdSessNegotiatedEchoInterval = _AxBfdSessNegotiatedEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 30),
    _AxBfdSessNegotiatedEchoInterval_Type()
)
axBfdSessNegotiatedEchoInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessNegotiatedEchoInterval.setStatus("current")
_AxBfdSessNegotiatedDetectMult_Type = BfdMultiplierTC
_AxBfdSessNegotiatedDetectMult_Object = MibTableColumn
axBfdSessNegotiatedDetectMult = _AxBfdSessNegotiatedDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 31),
    _AxBfdSessNegotiatedDetectMult_Type()
)
axBfdSessNegotiatedDetectMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessNegotiatedDetectMult.setStatus("current")
_AxBfdSessAuthPresFlag_Type = TruthValue
_AxBfdSessAuthPresFlag_Object = MibTableColumn
axBfdSessAuthPresFlag = _AxBfdSessAuthPresFlag_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 32),
    _AxBfdSessAuthPresFlag_Type()
)
axBfdSessAuthPresFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessAuthPresFlag.setStatus("current")
_AxBfdSessAuthenticationType_Type = BfdSessAuthenticationTypeTC
_AxBfdSessAuthenticationType_Object = MibTableColumn
axBfdSessAuthenticationType = _AxBfdSessAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 33),
    _AxBfdSessAuthenticationType_Type()
)
axBfdSessAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessAuthenticationType.setStatus("current")


class _AxBfdSessAuthenticationKeyID_Type(Integer32):
    """Custom type axBfdSessAuthenticationKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_AxBfdSessAuthenticationKeyID_Type.__name__ = "Integer32"
_AxBfdSessAuthenticationKeyID_Object = MibTableColumn
axBfdSessAuthenticationKeyID = _AxBfdSessAuthenticationKeyID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 34),
    _AxBfdSessAuthenticationKeyID_Type()
)
axBfdSessAuthenticationKeyID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessAuthenticationKeyID.setStatus("current")
_AxBfdSessAuthenticationKey_Type = BfdSessionAuthenticationKeyTC
_AxBfdSessAuthenticationKey_Object = MibTableColumn
axBfdSessAuthenticationKey = _AxBfdSessAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 35),
    _AxBfdSessAuthenticationKey_Type()
)
axBfdSessAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessAuthenticationKey.setStatus("current")
_AxBfdSessStorageType_Type = StorageType
_AxBfdSessStorageType_Object = MibTableColumn
axBfdSessStorageType = _AxBfdSessStorageType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 36),
    _AxBfdSessStorageType_Type()
)
axBfdSessStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessStorageType.setStatus("current")
_AxBfdSessRowStatus_Type = RowStatus
_AxBfdSessRowStatus_Object = MibTableColumn
axBfdSessRowStatus = _AxBfdSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 2, 1, 37),
    _AxBfdSessRowStatus_Type()
)
axBfdSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessRowStatus.setStatus("current")
_AxBfdSessPerfTable_Object = MibTable
axBfdSessPerfTable = _AxBfdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3)
)
if mibBuilder.loadTexts:
    axBfdSessPerfTable.setStatus("current")
_AxBfdSessPerfEntry_Object = MibTableRow
axBfdSessPerfEntry = _AxBfdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1)
)
if mibBuilder.loadTexts:
    axBfdSessPerfEntry.setStatus("current")
_AxBfdSessPerfCtrlPktIn_Type = Counter32
_AxBfdSessPerfCtrlPktIn_Object = MibTableColumn
axBfdSessPerfCtrlPktIn = _AxBfdSessPerfCtrlPktIn_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 1),
    _AxBfdSessPerfCtrlPktIn_Type()
)
axBfdSessPerfCtrlPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfCtrlPktIn.setStatus("current")
_AxBfdSessPerfCtrlPktOut_Type = Counter32
_AxBfdSessPerfCtrlPktOut_Object = MibTableColumn
axBfdSessPerfCtrlPktOut = _AxBfdSessPerfCtrlPktOut_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 2),
    _AxBfdSessPerfCtrlPktOut_Type()
)
axBfdSessPerfCtrlPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfCtrlPktOut.setStatus("current")
_AxBfdSessPerfCtrlPktDrop_Type = Counter32
_AxBfdSessPerfCtrlPktDrop_Object = MibTableColumn
axBfdSessPerfCtrlPktDrop = _AxBfdSessPerfCtrlPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 3),
    _AxBfdSessPerfCtrlPktDrop_Type()
)
axBfdSessPerfCtrlPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfCtrlPktDrop.setStatus("current")
_AxBfdSessPerfCtrlPktDropLastTime_Type = TimeStamp
_AxBfdSessPerfCtrlPktDropLastTime_Object = MibTableColumn
axBfdSessPerfCtrlPktDropLastTime = _AxBfdSessPerfCtrlPktDropLastTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 4),
    _AxBfdSessPerfCtrlPktDropLastTime_Type()
)
axBfdSessPerfCtrlPktDropLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfCtrlPktDropLastTime.setStatus("current")
_AxBfdSessPerfEchoPktIn_Type = Counter32
_AxBfdSessPerfEchoPktIn_Object = MibTableColumn
axBfdSessPerfEchoPktIn = _AxBfdSessPerfEchoPktIn_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 5),
    _AxBfdSessPerfEchoPktIn_Type()
)
axBfdSessPerfEchoPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfEchoPktIn.setStatus("current")
_AxBfdSessPerfEchoPktOut_Type = Counter32
_AxBfdSessPerfEchoPktOut_Object = MibTableColumn
axBfdSessPerfEchoPktOut = _AxBfdSessPerfEchoPktOut_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 6),
    _AxBfdSessPerfEchoPktOut_Type()
)
axBfdSessPerfEchoPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfEchoPktOut.setStatus("current")
_AxBfdSessPerfEchoPktDrop_Type = Counter32
_AxBfdSessPerfEchoPktDrop_Object = MibTableColumn
axBfdSessPerfEchoPktDrop = _AxBfdSessPerfEchoPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 7),
    _AxBfdSessPerfEchoPktDrop_Type()
)
axBfdSessPerfEchoPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfEchoPktDrop.setStatus("current")
_AxBfdSessPerfEchoPktDropLastTime_Type = TimeStamp
_AxBfdSessPerfEchoPktDropLastTime_Object = MibTableColumn
axBfdSessPerfEchoPktDropLastTime = _AxBfdSessPerfEchoPktDropLastTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 8),
    _AxBfdSessPerfEchoPktDropLastTime_Type()
)
axBfdSessPerfEchoPktDropLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfEchoPktDropLastTime.setStatus("current")
_AxBfdSessUpTime_Type = TimeStamp
_AxBfdSessUpTime_Object = MibTableColumn
axBfdSessUpTime = _AxBfdSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 9),
    _AxBfdSessUpTime_Type()
)
axBfdSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessUpTime.setStatus("current")
_AxBfdSessPerfLastSessDownTime_Type = TimeStamp
_AxBfdSessPerfLastSessDownTime_Object = MibTableColumn
axBfdSessPerfLastSessDownTime = _AxBfdSessPerfLastSessDownTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 10),
    _AxBfdSessPerfLastSessDownTime_Type()
)
axBfdSessPerfLastSessDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfLastSessDownTime.setStatus("current")
_AxBfdSessPerfLastCommLostDiag_Type = BfdDiagTC
_AxBfdSessPerfLastCommLostDiag_Object = MibTableColumn
axBfdSessPerfLastCommLostDiag = _AxBfdSessPerfLastCommLostDiag_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 11),
    _AxBfdSessPerfLastCommLostDiag_Type()
)
axBfdSessPerfLastCommLostDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfLastCommLostDiag.setStatus("current")
_AxBfdSessPerfSessUpCount_Type = Counter32
_AxBfdSessPerfSessUpCount_Object = MibTableColumn
axBfdSessPerfSessUpCount = _AxBfdSessPerfSessUpCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 12),
    _AxBfdSessPerfSessUpCount_Type()
)
axBfdSessPerfSessUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfSessUpCount.setStatus("current")
_AxBfdSessPerfDiscTime_Type = TimeStamp
_AxBfdSessPerfDiscTime_Object = MibTableColumn
axBfdSessPerfDiscTime = _AxBfdSessPerfDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 13),
    _AxBfdSessPerfDiscTime_Type()
)
axBfdSessPerfDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfDiscTime.setStatus("current")
_AxBfdSessPerfCtrlPktInHC_Type = Counter64
_AxBfdSessPerfCtrlPktInHC_Object = MibTableColumn
axBfdSessPerfCtrlPktInHC = _AxBfdSessPerfCtrlPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 14),
    _AxBfdSessPerfCtrlPktInHC_Type()
)
axBfdSessPerfCtrlPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfCtrlPktInHC.setStatus("current")
_AxBfdSessPerfCtrlPktOutHC_Type = Counter64
_AxBfdSessPerfCtrlPktOutHC_Object = MibTableColumn
axBfdSessPerfCtrlPktOutHC = _AxBfdSessPerfCtrlPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 15),
    _AxBfdSessPerfCtrlPktOutHC_Type()
)
axBfdSessPerfCtrlPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfCtrlPktOutHC.setStatus("current")
_AxBfdSessPerfCtrlPktDropHC_Type = Counter64
_AxBfdSessPerfCtrlPktDropHC_Object = MibTableColumn
axBfdSessPerfCtrlPktDropHC = _AxBfdSessPerfCtrlPktDropHC_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 16),
    _AxBfdSessPerfCtrlPktDropHC_Type()
)
axBfdSessPerfCtrlPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfCtrlPktDropHC.setStatus("current")
_AxBfdSessPerfEchoPktInHC_Type = Counter64
_AxBfdSessPerfEchoPktInHC_Object = MibTableColumn
axBfdSessPerfEchoPktInHC = _AxBfdSessPerfEchoPktInHC_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 17),
    _AxBfdSessPerfEchoPktInHC_Type()
)
axBfdSessPerfEchoPktInHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfEchoPktInHC.setStatus("current")
_AxBfdSessPerfEchoPktOutHC_Type = Counter64
_AxBfdSessPerfEchoPktOutHC_Object = MibTableColumn
axBfdSessPerfEchoPktOutHC = _AxBfdSessPerfEchoPktOutHC_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 18),
    _AxBfdSessPerfEchoPktOutHC_Type()
)
axBfdSessPerfEchoPktOutHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfEchoPktOutHC.setStatus("current")
_AxBfdSessPerfEchoPktDropHC_Type = Counter64
_AxBfdSessPerfEchoPktDropHC_Object = MibTableColumn
axBfdSessPerfEchoPktDropHC = _AxBfdSessPerfEchoPktDropHC_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 3, 1, 19),
    _AxBfdSessPerfEchoPktDropHC_Type()
)
axBfdSessPerfEchoPktDropHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessPerfEchoPktDropHC.setStatus("current")
_AxBfdSessDiscMapTable_Object = MibTable
axBfdSessDiscMapTable = _AxBfdSessDiscMapTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 4)
)
if mibBuilder.loadTexts:
    axBfdSessDiscMapTable.setStatus("current")
_AxBfdSessDiscMapEntry_Object = MibTableRow
axBfdSessDiscMapEntry = _AxBfdSessDiscMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 4, 1)
)
axBfdSessDiscMapEntry.setIndexNames(
    (0, "AX-BFD-MIB", "axBfdSessDiscriminator"),
)
if mibBuilder.loadTexts:
    axBfdSessDiscMapEntry.setStatus("current")
_AxBfdSessDiscMapIndex_Type = BfdSessIndexTC
_AxBfdSessDiscMapIndex_Object = MibTableColumn
axBfdSessDiscMapIndex = _AxBfdSessDiscMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 4, 1, 1),
    _AxBfdSessDiscMapIndex_Type()
)
axBfdSessDiscMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessDiscMapIndex.setStatus("current")
_AxBfdSessDiscMapStorageType_Type = StorageType
_AxBfdSessDiscMapStorageType_Object = MibTableColumn
axBfdSessDiscMapStorageType = _AxBfdSessDiscMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 4, 1, 2),
    _AxBfdSessDiscMapStorageType_Type()
)
axBfdSessDiscMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessDiscMapStorageType.setStatus("current")
_AxBfdSessDiscMapRowStatus_Type = RowStatus
_AxBfdSessDiscMapRowStatus_Object = MibTableColumn
axBfdSessDiscMapRowStatus = _AxBfdSessDiscMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 4, 1, 3),
    _AxBfdSessDiscMapRowStatus_Type()
)
axBfdSessDiscMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessDiscMapRowStatus.setStatus("current")
_AxBfdSessIpMapTable_Object = MibTable
axBfdSessIpMapTable = _AxBfdSessIpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 5)
)
if mibBuilder.loadTexts:
    axBfdSessIpMapTable.setStatus("current")
_AxBfdSessIpMapEntry_Object = MibTableRow
axBfdSessIpMapEntry = _AxBfdSessIpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 5, 1)
)
axBfdSessIpMapEntry.setIndexNames(
    (0, "AX-BFD-MIB", "axBfdSessInterface"),
    (0, "AX-BFD-MIB", "axBfdSessApplicationId"),
    (0, "AX-BFD-MIB", "axBfdSessSrcAddrType"),
    (0, "AX-BFD-MIB", "axBfdSessSrcAddr"),
    (0, "AX-BFD-MIB", "axBfdSessDstAddrType"),
    (0, "AX-BFD-MIB", "axBfdSessDstAddr"),
)
if mibBuilder.loadTexts:
    axBfdSessIpMapEntry.setStatus("current")
_AxBfdSessIpMapIndex_Type = BfdSessIndexTC
_AxBfdSessIpMapIndex_Object = MibTableColumn
axBfdSessIpMapIndex = _AxBfdSessIpMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 5, 1, 1),
    _AxBfdSessIpMapIndex_Type()
)
axBfdSessIpMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBfdSessIpMapIndex.setStatus("current")
_AxBfdSessIpMapStorageType_Type = StorageType
_AxBfdSessIpMapStorageType_Object = MibTableColumn
axBfdSessIpMapStorageType = _AxBfdSessIpMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 5, 1, 2),
    _AxBfdSessIpMapStorageType_Type()
)
axBfdSessIpMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessIpMapStorageType.setStatus("current")
_AxBfdSessIpMapRowStatus_Type = RowStatus
_AxBfdSessIpMapRowStatus_Object = MibTableColumn
axBfdSessIpMapRowStatus = _AxBfdSessIpMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1, 5, 1, 3),
    _AxBfdSessIpMapRowStatus_Type()
)
axBfdSessIpMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axBfdSessIpMapRowStatus.setStatus("current")
_AxBfdConformance_ObjectIdentity = ObjectIdentity
axBfdConformance = _AxBfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1000)
)
_AxBfdCompliances_ObjectIdentity = ObjectIdentity
axBfdCompliances = _AxBfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1000, 1)
)
_AxBfdGroups_ObjectIdentity = ObjectIdentity
axBfdGroups = _AxBfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1000, 2)
)
axBfdSessEntry.registerAugmentions(
    ("AX-BFD-MIB",
     "axBfdSessPerfEntry")
)
axBfdSessPerfEntry.setIndexNames(*axBfdSessEntry.getIndexNames())

# Managed Objects groups

axBfdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1000, 2, 1)
)
axBfdGroup.setObjects(
      *(("AX-BFD-MIB", "axBfdAdminStatus"),
        ("AX-BFD-MIB", "axBfdSessNotificationsEnable"),
        ("AX-BFD-MIB", "axBfdSessVersionNumber"),
        ("AX-BFD-MIB", "axBfdSessType"),
        ("AX-BFD-MIB", "axBfdSessDiscriminator"),
        ("AX-BFD-MIB", "axBfdSessRemoteDiscr"),
        ("AX-BFD-MIB", "axBfdSessDestinationUdpPort"),
        ("AX-BFD-MIB", "axBfdSessSourceUdpPort"),
        ("AX-BFD-MIB", "axBfdSessEchoSourceUdpPort"),
        ("AX-BFD-MIB", "axBfdSessAdminStatus"),
        ("AX-BFD-MIB", "axBfdSessState"),
        ("AX-BFD-MIB", "axBfdSessRemoteHeardFlag"),
        ("AX-BFD-MIB", "axBfdSessDiag"),
        ("AX-BFD-MIB", "axBfdSessOperMode"),
        ("AX-BFD-MIB", "axBfdSessDemandModeDesiredFlag"),
        ("AX-BFD-MIB", "axBfdSessControlPlaneIndepFlag"),
        ("AX-BFD-MIB", "axBfdSessMultipointFlag"),
        ("AX-BFD-MIB", "axBfdSessInterface"),
        ("AX-BFD-MIB", "axBfdSessApplicationId"),
        ("AX-BFD-MIB", "axBfdSessSrcAddrType"),
        ("AX-BFD-MIB", "axBfdSessSrcAddr"),
        ("AX-BFD-MIB", "axBfdSessDstAddrType"),
        ("AX-BFD-MIB", "axBfdSessDstAddr"),
        ("AX-BFD-MIB", "axBfdSessGTSM"),
        ("AX-BFD-MIB", "axBfdSessGTSMTTL"),
        ("AX-BFD-MIB", "axBfdSessDesiredMinTxInterval"),
        ("AX-BFD-MIB", "axBfdSessReqMinRxInterval"),
        ("AX-BFD-MIB", "axBfdSessReqMinEchoRxInterval"),
        ("AX-BFD-MIB", "axBfdSessDetectMult"),
        ("AX-BFD-MIB", "axBfdSessNegotiatedInterval"),
        ("AX-BFD-MIB", "axBfdSessNegotiatedEchoInterval"),
        ("AX-BFD-MIB", "axBfdSessNegotiatedDetectMult"),
        ("AX-BFD-MIB", "axBfdSessAuthPresFlag"),
        ("AX-BFD-MIB", "axBfdSessAuthenticationType"),
        ("AX-BFD-MIB", "axBfdSessAuthenticationKeyID"),
        ("AX-BFD-MIB", "axBfdSessAuthenticationKey"),
        ("AX-BFD-MIB", "axBfdSessStorageType"),
        ("AX-BFD-MIB", "axBfdSessRowStatus"),
        ("AX-BFD-MIB", "axBfdSessPerfCtrlPktIn"),
        ("AX-BFD-MIB", "axBfdSessPerfCtrlPktOut"),
        ("AX-BFD-MIB", "axBfdSessPerfCtrlPktDrop"),
        ("AX-BFD-MIB", "axBfdSessPerfCtrlPktDropLastTime"),
        ("AX-BFD-MIB", "axBfdSessPerfEchoPktIn"),
        ("AX-BFD-MIB", "axBfdSessPerfEchoPktOut"),
        ("AX-BFD-MIB", "axBfdSessPerfEchoPktDrop"),
        ("AX-BFD-MIB", "axBfdSessPerfEchoPktDropLastTime"),
        ("AX-BFD-MIB", "axBfdSessUpTime"),
        ("AX-BFD-MIB", "axBfdSessPerfLastSessDownTime"),
        ("AX-BFD-MIB", "axBfdSessPerfLastCommLostDiag"),
        ("AX-BFD-MIB", "axBfdSessPerfSessUpCount"),
        ("AX-BFD-MIB", "axBfdSessPerfDiscTime"),
        ("AX-BFD-MIB", "axBfdSessPerfCtrlPktInHC"),
        ("AX-BFD-MIB", "axBfdSessPerfCtrlPktOutHC"),
        ("AX-BFD-MIB", "axBfdSessPerfCtrlPktDropHC"),
        ("AX-BFD-MIB", "axBfdSessPerfEchoPktInHC"),
        ("AX-BFD-MIB", "axBfdSessPerfEchoPktOutHC"),
        ("AX-BFD-MIB", "axBfdSessPerfEchoPktDropHC"),
        ("AX-BFD-MIB", "axBfdSessDiscMapIndex"),
        ("AX-BFD-MIB", "axBfdSessDiscMapStorageType"),
        ("AX-BFD-MIB", "axBfdSessDiscMapRowStatus"),
        ("AX-BFD-MIB", "axBfdSessIpMapIndex"),
        ("AX-BFD-MIB", "axBfdSessIpMapStorageType"),
        ("AX-BFD-MIB", "axBfdSessIpMapRowStatus"))
)
if mibBuilder.loadTexts:
    axBfdGroup.setStatus("current")


# Notification objects

axBfdSessUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 0, 1)
)
axBfdSessUp.setObjects(
      *(("AX-BFD-MIB", "axBfdSessDiag"),
        ("AX-BFD-MIB", "axBfdSessDiag"))
)
if mibBuilder.loadTexts:
    axBfdSessUp.setStatus(
        "current"
    )

axBfdSessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 0, 2)
)
axBfdSessDown.setObjects(
      *(("AX-BFD-MIB", "axBfdSessDiag"),
        ("AX-BFD-MIB", "axBfdSessDiag"))
)
if mibBuilder.loadTexts:
    axBfdSessDown.setStatus(
        "current"
    )


# Notifications groups

axBfdNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1000, 2, 10)
)
axBfdNotificationGroup.setObjects(
      *(("AX-BFD-MIB", "axBfdSessUp"),
        ("AX-BFD-MIB", "axBfdSessDown"))
)
if mibBuilder.loadTexts:
    axBfdNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

axBfdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 201, 1000, 1, 1)
)
axBfdCompliance.setObjects(
      *(("AX-BFD-MIB", "axBfdGroup"),
        ("AX-BFD-MIB", "axBfdNotificationGroup"))
)
if mibBuilder.loadTexts:
    axBfdCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-BFD-MIB",
    **{"axBfdMIB": axBfdMIB,
       "axBfdNotifications": axBfdNotifications,
       "axBfdSessUp": axBfdSessUp,
       "axBfdSessDown": axBfdSessDown,
       "axBfdObjects": axBfdObjects,
       "axBfdScalarObjects": axBfdScalarObjects,
       "axBfdAdminStatus": axBfdAdminStatus,
       "axBfdSessNotificationsEnable": axBfdSessNotificationsEnable,
       "axBfdSessTable": axBfdSessTable,
       "axBfdSessEntry": axBfdSessEntry,
       "axBfdSessIndex": axBfdSessIndex,
       "axBfdSessVersionNumber": axBfdSessVersionNumber,
       "axBfdSessType": axBfdSessType,
       "axBfdSessDiscriminator": axBfdSessDiscriminator,
       "axBfdSessRemoteDiscr": axBfdSessRemoteDiscr,
       "axBfdSessDestinationUdpPort": axBfdSessDestinationUdpPort,
       "axBfdSessSourceUdpPort": axBfdSessSourceUdpPort,
       "axBfdSessEchoSourceUdpPort": axBfdSessEchoSourceUdpPort,
       "axBfdSessAdminStatus": axBfdSessAdminStatus,
       "axBfdSessState": axBfdSessState,
       "axBfdSessRemoteHeardFlag": axBfdSessRemoteHeardFlag,
       "axBfdSessDiag": axBfdSessDiag,
       "axBfdSessOperMode": axBfdSessOperMode,
       "axBfdSessDemandModeDesiredFlag": axBfdSessDemandModeDesiredFlag,
       "axBfdSessControlPlaneIndepFlag": axBfdSessControlPlaneIndepFlag,
       "axBfdSessMultipointFlag": axBfdSessMultipointFlag,
       "axBfdSessInterface": axBfdSessInterface,
       "axBfdSessApplicationId": axBfdSessApplicationId,
       "axBfdSessSrcAddrType": axBfdSessSrcAddrType,
       "axBfdSessSrcAddr": axBfdSessSrcAddr,
       "axBfdSessDstAddrType": axBfdSessDstAddrType,
       "axBfdSessDstAddr": axBfdSessDstAddr,
       "axBfdSessGTSM": axBfdSessGTSM,
       "axBfdSessGTSMTTL": axBfdSessGTSMTTL,
       "axBfdSessDesiredMinTxInterval": axBfdSessDesiredMinTxInterval,
       "axBfdSessReqMinRxInterval": axBfdSessReqMinRxInterval,
       "axBfdSessReqMinEchoRxInterval": axBfdSessReqMinEchoRxInterval,
       "axBfdSessDetectMult": axBfdSessDetectMult,
       "axBfdSessNegotiatedInterval": axBfdSessNegotiatedInterval,
       "axBfdSessNegotiatedEchoInterval": axBfdSessNegotiatedEchoInterval,
       "axBfdSessNegotiatedDetectMult": axBfdSessNegotiatedDetectMult,
       "axBfdSessAuthPresFlag": axBfdSessAuthPresFlag,
       "axBfdSessAuthenticationType": axBfdSessAuthenticationType,
       "axBfdSessAuthenticationKeyID": axBfdSessAuthenticationKeyID,
       "axBfdSessAuthenticationKey": axBfdSessAuthenticationKey,
       "axBfdSessStorageType": axBfdSessStorageType,
       "axBfdSessRowStatus": axBfdSessRowStatus,
       "axBfdSessPerfTable": axBfdSessPerfTable,
       "axBfdSessPerfEntry": axBfdSessPerfEntry,
       "axBfdSessPerfCtrlPktIn": axBfdSessPerfCtrlPktIn,
       "axBfdSessPerfCtrlPktOut": axBfdSessPerfCtrlPktOut,
       "axBfdSessPerfCtrlPktDrop": axBfdSessPerfCtrlPktDrop,
       "axBfdSessPerfCtrlPktDropLastTime": axBfdSessPerfCtrlPktDropLastTime,
       "axBfdSessPerfEchoPktIn": axBfdSessPerfEchoPktIn,
       "axBfdSessPerfEchoPktOut": axBfdSessPerfEchoPktOut,
       "axBfdSessPerfEchoPktDrop": axBfdSessPerfEchoPktDrop,
       "axBfdSessPerfEchoPktDropLastTime": axBfdSessPerfEchoPktDropLastTime,
       "axBfdSessUpTime": axBfdSessUpTime,
       "axBfdSessPerfLastSessDownTime": axBfdSessPerfLastSessDownTime,
       "axBfdSessPerfLastCommLostDiag": axBfdSessPerfLastCommLostDiag,
       "axBfdSessPerfSessUpCount": axBfdSessPerfSessUpCount,
       "axBfdSessPerfDiscTime": axBfdSessPerfDiscTime,
       "axBfdSessPerfCtrlPktInHC": axBfdSessPerfCtrlPktInHC,
       "axBfdSessPerfCtrlPktOutHC": axBfdSessPerfCtrlPktOutHC,
       "axBfdSessPerfCtrlPktDropHC": axBfdSessPerfCtrlPktDropHC,
       "axBfdSessPerfEchoPktInHC": axBfdSessPerfEchoPktInHC,
       "axBfdSessPerfEchoPktOutHC": axBfdSessPerfEchoPktOutHC,
       "axBfdSessPerfEchoPktDropHC": axBfdSessPerfEchoPktDropHC,
       "axBfdSessDiscMapTable": axBfdSessDiscMapTable,
       "axBfdSessDiscMapEntry": axBfdSessDiscMapEntry,
       "axBfdSessDiscMapIndex": axBfdSessDiscMapIndex,
       "axBfdSessDiscMapStorageType": axBfdSessDiscMapStorageType,
       "axBfdSessDiscMapRowStatus": axBfdSessDiscMapRowStatus,
       "axBfdSessIpMapTable": axBfdSessIpMapTable,
       "axBfdSessIpMapEntry": axBfdSessIpMapEntry,
       "axBfdSessIpMapIndex": axBfdSessIpMapIndex,
       "axBfdSessIpMapStorageType": axBfdSessIpMapStorageType,
       "axBfdSessIpMapRowStatus": axBfdSessIpMapRowStatus,
       "axBfdConformance": axBfdConformance,
       "axBfdCompliances": axBfdCompliances,
       "axBfdCompliance": axBfdCompliance,
       "axBfdGroups": axBfdGroups,
       "axBfdGroup": axBfdGroup,
       "axBfdNotificationGroup": axBfdNotificationGroup}
)
