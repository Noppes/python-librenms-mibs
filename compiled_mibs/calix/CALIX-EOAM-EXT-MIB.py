# SNMP MIB module (CALIX-EOAM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\calix\CALIX-EOAM-EXT-MIB

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

(Dot1agCfmCcmInterval,
 Dot1agCfmIdPermission,
 Dot1agCfmMDLevel,
 Dot1agCfmMepId,
 Dot1agCfmMepIdOrZero,
 Dot1agCfmMpDirection,
 Dot1agCfmPbbComponentIdentifier,
 dot1agCfmLtrReceiveOrder,
 dot1agCfmLtrSeqNumber,
 dot1agCfmMaComponentId,
 dot1agCfmMaIndex,
 dot1agCfmMaMepListIdentifier,
 dot1agCfmMdIndex,
 dot1agCfmMepDbRMepIdentifier,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmCcmInterval",
    "Dot1agCfmIdPermission",
    "Dot1agCfmMDLevel",
    "Dot1agCfmMepId",
    "Dot1agCfmMepIdOrZero",
    "Dot1agCfmMpDirection",
    "Dot1agCfmPbbComponentIdentifier",
    "dot1agCfmLtrReceiveOrder",
    "dot1agCfmLtrSeqNumber",
    "dot1agCfmMaComponentId",
    "dot1agCfmMaIndex",
    "dot1agCfmMaMepListIdentifier",
    "dot1agCfmMdIndex",
    "dot1agCfmMepDbRMepIdentifier",
    "dot1agCfmMepIdentifier")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(LldpChassisId,
 LldpChassisIdSubtype,
 LldpPortId,
 LldpPortIdSubtype) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype",
    "LldpPortId",
    "LldpPortIdSubtype")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TAddress,
 TDomain,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

calixEoamExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CalixEoamEnableType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )



class CalixSoamLmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("dual", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CalixEoamExtConfig_ObjectIdentity = ObjectIdentity
calixEoamExtConfig = _CalixEoamExtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1)
)
_CalixSoamExtMegTable_Object = MibTable
calixSoamExtMegTable = _CalixSoamExtMegTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 1)
)
if mibBuilder.loadTexts:
    calixSoamExtMegTable.setStatus("current")
_CalixSoamExtMegEntry_Object = MibTableRow
calixSoamExtMegEntry = _CalixSoamExtMegEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 1, 1)
)
calixSoamExtMegEntry.setIndexNames(
    (0, "CALIX-EOAM-EXT-MIB", "calixSoamExtMegIdentifier"),
)
if mibBuilder.loadTexts:
    calixSoamExtMegEntry.setStatus("current")


class _CalixSoamExtMegIdentifier_Type(Unsigned32):
    """Custom type calixSoamExtMegIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CalixSoamExtMegIdentifier_Type.__name__ = "Unsigned32"
_CalixSoamExtMegIdentifier_Object = MibTableColumn
calixSoamExtMegIdentifier = _CalixSoamExtMegIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 1, 1, 1),
    _CalixSoamExtMegIdentifier_Type()
)
calixSoamExtMegIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    calixSoamExtMegIdentifier.setStatus("current")


class _CalixSoamExtMegName_Type(OctetString):
    """Custom type calixSoamExtMegName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_CalixSoamExtMegName_Type.__name__ = "OctetString"
_CalixSoamExtMegName_Object = MibTableColumn
calixSoamExtMegName = _CalixSoamExtMegName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 1, 1, 2),
    _CalixSoamExtMegName_Type()
)
calixSoamExtMegName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMegName.setStatus("current")


class _CalixSoamExtMegLevel_Type(Dot1agCfmMDLevel):
    """Custom type calixSoamExtMegLevel based on Dot1agCfmMDLevel"""
    defaultValue = 0


_CalixSoamExtMegLevel_Type.__name__ = "Dot1agCfmMDLevel"
_CalixSoamExtMegLevel_Object = MibTableColumn
calixSoamExtMegLevel = _CalixSoamExtMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 1, 1, 3),
    _CalixSoamExtMegLevel_Type()
)
calixSoamExtMegLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMegLevel.setStatus("current")


class _CalixSoamExtMegCcmInterval_Type(Dot1agCfmCcmInterval):
    """Custom type calixSoamExtMegCcmInterval based on Dot1agCfmCcmInterval"""
    defaultValue = 4


_CalixSoamExtMegCcmInterval_Type.__name__ = "Dot1agCfmCcmInterval"
_CalixSoamExtMegCcmInterval_Object = MibTableColumn
calixSoamExtMegCcmInterval = _CalixSoamExtMegCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 1, 1, 4),
    _CalixSoamExtMegCcmInterval_Type()
)
calixSoamExtMegCcmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMegCcmInterval.setStatus("current")


class _CalixSoamExtMegVid_Type(Unsigned32):
    """Custom type calixSoamExtMegVid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CalixSoamExtMegVid_Type.__name__ = "Unsigned32"
_CalixSoamExtMegVid_Object = MibTableColumn
calixSoamExtMegVid = _CalixSoamExtMegVid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 1, 1, 5),
    _CalixSoamExtMegVid_Type()
)
calixSoamExtMegVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMegVid.setStatus("current")
_CalixSoamExtMegAutoDiscovery_Type = CalixEoamEnableType
_CalixSoamExtMegAutoDiscovery_Object = MibTableColumn
calixSoamExtMegAutoDiscovery = _CalixSoamExtMegAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 1, 1, 6),
    _CalixSoamExtMegAutoDiscovery_Type()
)
calixSoamExtMegAutoDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMegAutoDiscovery.setStatus("current")
_CalixSoamExtMegAutoDiscoveryTimeout_Type = Unsigned32
_CalixSoamExtMegAutoDiscoveryTimeout_Object = MibTableColumn
calixSoamExtMegAutoDiscoveryTimeout = _CalixSoamExtMegAutoDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 1, 1, 7),
    _CalixSoamExtMegAutoDiscoveryTimeout_Type()
)
calixSoamExtMegAutoDiscoveryTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMegAutoDiscoveryTimeout.setStatus("current")
_CalixSoamExtMegCciInterworking_Type = CalixEoamEnableType
_CalixSoamExtMegCciInterworking_Object = MibTableColumn
calixSoamExtMegCciInterworking = _CalixSoamExtMegCciInterworking_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 1, 1, 8),
    _CalixSoamExtMegCciInterworking_Type()
)
calixSoamExtMegCciInterworking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMegCciInterworking.setStatus("current")


class _CalixSoamExtMegIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type calixSoamExtMegIdPermission based on Dot1agCfmIdPermission"""
    defaultValue = 1


_CalixSoamExtMegIdPermission_Type.__name__ = "Dot1agCfmIdPermission"
_CalixSoamExtMegIdPermission_Object = MibTableColumn
calixSoamExtMegIdPermission = _CalixSoamExtMegIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 1, 1, 9),
    _CalixSoamExtMegIdPermission_Type()
)
calixSoamExtMegIdPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMegIdPermission.setStatus("current")
_CalixSoamExtMegRowStatus_Type = RowStatus
_CalixSoamExtMegRowStatus_Object = MibTableColumn
calixSoamExtMegRowStatus = _CalixSoamExtMegRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 1, 1, 10),
    _CalixSoamExtMegRowStatus_Type()
)
calixSoamExtMegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMegRowStatus.setStatus("current")
_CalixSoamExtMipTable_Object = MibTable
calixSoamExtMipTable = _CalixSoamExtMipTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 2)
)
if mibBuilder.loadTexts:
    calixSoamExtMipTable.setStatus("current")
_CalixSoamExtMipEntry_Object = MibTableRow
calixSoamExtMipEntry = _CalixSoamExtMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 2, 1)
)
calixSoamExtMipEntry.setIndexNames(
    (0, "CALIX-EOAM-EXT-MIB", "calixSoamExtMegIdentifier"),
    (0, "CALIX-EOAM-EXT-MIB", "calixSoamExtMipIdentifier"),
)
if mibBuilder.loadTexts:
    calixSoamExtMipEntry.setStatus("current")


class _CalixSoamExtMipIdentifier_Type(Unsigned32):
    """Custom type calixSoamExtMipIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CalixSoamExtMipIdentifier_Type.__name__ = "Unsigned32"
_CalixSoamExtMipIdentifier_Object = MibTableColumn
calixSoamExtMipIdentifier = _CalixSoamExtMipIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 2, 1, 1),
    _CalixSoamExtMipIdentifier_Type()
)
calixSoamExtMipIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    calixSoamExtMipIdentifier.setStatus("current")
_CalixSoamExtMipIfIndex_Type = InterfaceIndex
_CalixSoamExtMipIfIndex_Object = MibTableColumn
calixSoamExtMipIfIndex = _CalixSoamExtMipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 2, 1, 3),
    _CalixSoamExtMipIfIndex_Type()
)
calixSoamExtMipIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMipIfIndex.setStatus("current")
_CalixSoamExtMipAdminState_Type = CalixEoamEnableType
_CalixSoamExtMipAdminState_Object = MibTableColumn
calixSoamExtMipAdminState = _CalixSoamExtMipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 2, 1, 4),
    _CalixSoamExtMipAdminState_Type()
)
calixSoamExtMipAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMipAdminState.setStatus("current")
_CalixSoamExtMipMacAddress_Type = MacAddress
_CalixSoamExtMipMacAddress_Object = MibTableColumn
calixSoamExtMipMacAddress = _CalixSoamExtMipMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 2, 1, 5),
    _CalixSoamExtMipMacAddress_Type()
)
calixSoamExtMipMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMipMacAddress.setStatus("current")
_CalixSoamExtMipResetStat_Type = TruthValue
_CalixSoamExtMipResetStat_Object = MibTableColumn
calixSoamExtMipResetStat = _CalixSoamExtMipResetStat_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 2, 1, 6),
    _CalixSoamExtMipResetStat_Type()
)
calixSoamExtMipResetStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMipResetStat.setStatus("current")
_CalixSoamExtMipRowStatus_Type = RowStatus
_CalixSoamExtMipRowStatus_Object = MibTableColumn
calixSoamExtMipRowStatus = _CalixSoamExtMipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 2, 1, 7),
    _CalixSoamExtMipRowStatus_Type()
)
calixSoamExtMipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMipRowStatus.setStatus("current")
_CalixSoamExtMipStatsTable_Object = MibTable
calixSoamExtMipStatsTable = _CalixSoamExtMipStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 3)
)
if mibBuilder.loadTexts:
    calixSoamExtMipStatsTable.setStatus("current")
_CalixSoamExtMipStatsEntry_Object = MibTableRow
calixSoamExtMipStatsEntry = _CalixSoamExtMipStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 3, 1)
)
calixSoamExtMipStatsEntry.setIndexNames(
    (0, "CALIX-EOAM-EXT-MIB", "calixSoamExtMegIdentifier"),
    (0, "CALIX-EOAM-EXT-MIB", "calixSoamExtMipIdentifier"),
)
if mibBuilder.loadTexts:
    calixSoamExtMipStatsEntry.setStatus("current")
_CalixSoamExtMipStatsDirection_Type = Dot1agCfmMpDirection
_CalixSoamExtMipStatsDirection_Object = MibTableColumn
calixSoamExtMipStatsDirection = _CalixSoamExtMipStatsDirection_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 3, 1, 1),
    _CalixSoamExtMipStatsDirection_Type()
)
calixSoamExtMipStatsDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMipStatsDirection.setStatus("current")
_CalixSoamExtMipStatsLbmIn_Type = Counter32
_CalixSoamExtMipStatsLbmIn_Object = MibTableColumn
calixSoamExtMipStatsLbmIn = _CalixSoamExtMipStatsLbmIn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 3, 1, 2),
    _CalixSoamExtMipStatsLbmIn_Type()
)
calixSoamExtMipStatsLbmIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMipStatsLbmIn.setStatus("current")
_CalixSoamExtMipStatsLbrOut_Type = Counter32
_CalixSoamExtMipStatsLbrOut_Object = MibTableColumn
calixSoamExtMipStatsLbrOut = _CalixSoamExtMipStatsLbrOut_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 3, 1, 3),
    _CalixSoamExtMipStatsLbrOut_Type()
)
calixSoamExtMipStatsLbrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMipStatsLbrOut.setStatus("current")
_CalixSoamExtMipStatsLtmIn_Type = Counter32
_CalixSoamExtMipStatsLtmIn_Object = MibTableColumn
calixSoamExtMipStatsLtmIn = _CalixSoamExtMipStatsLtmIn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 3, 1, 4),
    _CalixSoamExtMipStatsLtmIn_Type()
)
calixSoamExtMipStatsLtmIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMipStatsLtmIn.setStatus("current")
_CalixSoamExtMipStatsLtmForwarded_Type = Counter32
_CalixSoamExtMipStatsLtmForwarded_Object = MibTableColumn
calixSoamExtMipStatsLtmForwarded = _CalixSoamExtMipStatsLtmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 3, 1, 5),
    _CalixSoamExtMipStatsLtmForwarded_Type()
)
calixSoamExtMipStatsLtmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMipStatsLtmForwarded.setStatus("current")
_CalixSoamExtMipStatsLtrOut_Type = Counter32
_CalixSoamExtMipStatsLtrOut_Object = MibTableColumn
calixSoamExtMipStatsLtrOut = _CalixSoamExtMipStatsLtrOut_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 3, 1, 6),
    _CalixSoamExtMipStatsLtrOut_Type()
)
calixSoamExtMipStatsLtrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMipStatsLtrOut.setStatus("current")
_CalixSoamExtMipStatsLbmInvalidSenderId_Type = Counter32
_CalixSoamExtMipStatsLbmInvalidSenderId_Object = MibTableColumn
calixSoamExtMipStatsLbmInvalidSenderId = _CalixSoamExtMipStatsLbmInvalidSenderId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 3, 1, 7),
    _CalixSoamExtMipStatsLbmInvalidSenderId_Type()
)
calixSoamExtMipStatsLbmInvalidSenderId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMipStatsLbmInvalidSenderId.setStatus("current")
_CalixSoamExtMipStatsDiscards_Type = Counter32
_CalixSoamExtMipStatsDiscards_Object = MibTableColumn
calixSoamExtMipStatsDiscards = _CalixSoamExtMipStatsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 3, 1, 8),
    _CalixSoamExtMipStatsDiscards_Type()
)
calixSoamExtMipStatsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMipStatsDiscards.setStatus("current")
_CalixSoamExtMipStatsResetStat_Type = TruthValue
_CalixSoamExtMipStatsResetStat_Object = MibTableColumn
calixSoamExtMipStatsResetStat = _CalixSoamExtMipStatsResetStat_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 3, 1, 9),
    _CalixSoamExtMipStatsResetStat_Type()
)
calixSoamExtMipStatsResetStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMipStatsResetStat.setStatus("current")
_CalixSoamExtMepDmExtTable_Object = MibTable
calixSoamExtMepDmExtTable = _CalixSoamExtMepDmExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4)
)
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtTable.setStatus("current")
_CalixSoamExtMepDmExtEntry_Object = MibTableRow
calixSoamExtMepDmExtEntry = _CalixSoamExtMepDmExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1)
)
calixSoamExtMepDmExtEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtEntry.setStatus("current")
_CalixSoamExtMepDmExtActive_Type = CalixEoamEnableType
_CalixSoamExtMepDmExtActive_Object = MibTableColumn
calixSoamExtMepDmExtActive = _CalixSoamExtMepDmExtActive_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 1),
    _CalixSoamExtMepDmExtActive_Type()
)
calixSoamExtMepDmExtActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtActive.setStatus("current")
_CalixSoamExtMepDmExtDestMacAddress_Type = MacAddress
_CalixSoamExtMepDmExtDestMacAddress_Object = MibTableColumn
calixSoamExtMepDmExtDestMacAddress = _CalixSoamExtMepDmExtDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 2),
    _CalixSoamExtMepDmExtDestMacAddress_Type()
)
calixSoamExtMepDmExtDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtDestMacAddress.setStatus("current")
_CalixSoamExtMepDmExtDestMepId_Type = Dot1agCfmMepIdOrZero
_CalixSoamExtMepDmExtDestMepId_Object = MibTableColumn
calixSoamExtMepDmExtDestMepId = _CalixSoamExtMepDmExtDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 3),
    _CalixSoamExtMepDmExtDestMepId_Type()
)
calixSoamExtMepDmExtDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtDestMepId.setStatus("current")
_CalixSoamExtMepDmExtDestIsMepId_Type = TruthValue
_CalixSoamExtMepDmExtDestIsMepId_Object = MibTableColumn
calixSoamExtMepDmExtDestIsMepId = _CalixSoamExtMepDmExtDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 4),
    _CalixSoamExtMepDmExtDestIsMepId_Type()
)
calixSoamExtMepDmExtDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtDestIsMepId.setStatus("current")


class _CalixSoamExtMepDmExtClassOfService_Type(Unsigned32):
    """Custom type calixSoamExtMepDmExtClassOfService based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CalixSoamExtMepDmExtClassOfService_Type.__name__ = "Unsigned32"
_CalixSoamExtMepDmExtClassOfService_Object = MibTableColumn
calixSoamExtMepDmExtClassOfService = _CalixSoamExtMepDmExtClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 5),
    _CalixSoamExtMepDmExtClassOfService_Type()
)
calixSoamExtMepDmExtClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtClassOfService.setStatus("current")


class _CalixSoamExtMepDmExtDmPeriod_Type(Integer32):
    """Custom type calixSoamExtMepDmExtDmPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dm1sec", 3),
          ("dm10sec", 4))
    )


_CalixSoamExtMepDmExtDmPeriod_Type.__name__ = "Integer32"
_CalixSoamExtMepDmExtDmPeriod_Object = MibTableColumn
calixSoamExtMepDmExtDmPeriod = _CalixSoamExtMepDmExtDmPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 6),
    _CalixSoamExtMepDmExtDmPeriod_Type()
)
calixSoamExtMepDmExtDmPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtDmPeriod.setStatus("current")


class _CalixSoamExtMepDmExtMaxRtdThrSet_Type(Unsigned32):
    """Custom type calixSoamExtMepDmExtMaxRtdThrSet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CalixSoamExtMepDmExtMaxRtdThrSet_Type.__name__ = "Unsigned32"
_CalixSoamExtMepDmExtMaxRtdThrSet_Object = MibTableColumn
calixSoamExtMepDmExtMaxRtdThrSet = _CalixSoamExtMepDmExtMaxRtdThrSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 7),
    _CalixSoamExtMepDmExtMaxRtdThrSet_Type()
)
calixSoamExtMepDmExtMaxRtdThrSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtMaxRtdThrSet.setStatus("current")


class _CalixSoamExtMepDmExtMaxRtdThrClr_Type(Unsigned32):
    """Custom type calixSoamExtMepDmExtMaxRtdThrClr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CalixSoamExtMepDmExtMaxRtdThrClr_Type.__name__ = "Unsigned32"
_CalixSoamExtMepDmExtMaxRtdThrClr_Object = MibTableColumn
calixSoamExtMepDmExtMaxRtdThrClr = _CalixSoamExtMepDmExtMaxRtdThrClr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 8),
    _CalixSoamExtMepDmExtMaxRtdThrClr_Type()
)
calixSoamExtMepDmExtMaxRtdThrClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtMaxRtdThrClr.setStatus("current")


class _CalixSoamExtMepDmExtAvgRtdThrSet_Type(Unsigned32):
    """Custom type calixSoamExtMepDmExtAvgRtdThrSet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CalixSoamExtMepDmExtAvgRtdThrSet_Type.__name__ = "Unsigned32"
_CalixSoamExtMepDmExtAvgRtdThrSet_Object = MibTableColumn
calixSoamExtMepDmExtAvgRtdThrSet = _CalixSoamExtMepDmExtAvgRtdThrSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 9),
    _CalixSoamExtMepDmExtAvgRtdThrSet_Type()
)
calixSoamExtMepDmExtAvgRtdThrSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtAvgRtdThrSet.setStatus("current")


class _CalixSoamExtMepDmExtAvgRtdThrClr_Type(Unsigned32):
    """Custom type calixSoamExtMepDmExtAvgRtdThrClr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CalixSoamExtMepDmExtAvgRtdThrClr_Type.__name__ = "Unsigned32"
_CalixSoamExtMepDmExtAvgRtdThrClr_Object = MibTableColumn
calixSoamExtMepDmExtAvgRtdThrClr = _CalixSoamExtMepDmExtAvgRtdThrClr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 10),
    _CalixSoamExtMepDmExtAvgRtdThrClr_Type()
)
calixSoamExtMepDmExtAvgRtdThrClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtAvgRtdThrClr.setStatus("current")


class _CalixSoamExtMepDmExtMaxRtdVarThrSet_Type(Unsigned32):
    """Custom type calixSoamExtMepDmExtMaxRtdVarThrSet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CalixSoamExtMepDmExtMaxRtdVarThrSet_Type.__name__ = "Unsigned32"
_CalixSoamExtMepDmExtMaxRtdVarThrSet_Object = MibTableColumn
calixSoamExtMepDmExtMaxRtdVarThrSet = _CalixSoamExtMepDmExtMaxRtdVarThrSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 11),
    _CalixSoamExtMepDmExtMaxRtdVarThrSet_Type()
)
calixSoamExtMepDmExtMaxRtdVarThrSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtMaxRtdVarThrSet.setStatus("current")


class _CalixSoamExtMepDmExtMaxRtdVarThrClr_Type(Unsigned32):
    """Custom type calixSoamExtMepDmExtMaxRtdVarThrClr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CalixSoamExtMepDmExtMaxRtdVarThrClr_Type.__name__ = "Unsigned32"
_CalixSoamExtMepDmExtMaxRtdVarThrClr_Object = MibTableColumn
calixSoamExtMepDmExtMaxRtdVarThrClr = _CalixSoamExtMepDmExtMaxRtdVarThrClr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 12),
    _CalixSoamExtMepDmExtMaxRtdVarThrClr_Type()
)
calixSoamExtMepDmExtMaxRtdVarThrClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtMaxRtdVarThrClr.setStatus("current")


class _CalixSoamExtMepDmExtAvgRtdVarThrSet_Type(Unsigned32):
    """Custom type calixSoamExtMepDmExtAvgRtdVarThrSet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CalixSoamExtMepDmExtAvgRtdVarThrSet_Type.__name__ = "Unsigned32"
_CalixSoamExtMepDmExtAvgRtdVarThrSet_Object = MibTableColumn
calixSoamExtMepDmExtAvgRtdVarThrSet = _CalixSoamExtMepDmExtAvgRtdVarThrSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 13),
    _CalixSoamExtMepDmExtAvgRtdVarThrSet_Type()
)
calixSoamExtMepDmExtAvgRtdVarThrSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtAvgRtdVarThrSet.setStatus("current")


class _CalixSoamExtMepDmExtAvgRtdVarThrClr_Type(Unsigned32):
    """Custom type calixSoamExtMepDmExtAvgRtdVarThrClr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CalixSoamExtMepDmExtAvgRtdVarThrClr_Type.__name__ = "Unsigned32"
_CalixSoamExtMepDmExtAvgRtdVarThrClr_Object = MibTableColumn
calixSoamExtMepDmExtAvgRtdVarThrClr = _CalixSoamExtMepDmExtAvgRtdVarThrClr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 14),
    _CalixSoamExtMepDmExtAvgRtdVarThrClr_Type()
)
calixSoamExtMepDmExtAvgRtdVarThrClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtAvgRtdVarThrClr.setStatus("current")
_CalixSoamExtMepDmExtAvgRoundTripDelay_Type = Unsigned32
_CalixSoamExtMepDmExtAvgRoundTripDelay_Object = MibTableColumn
calixSoamExtMepDmExtAvgRoundTripDelay = _CalixSoamExtMepDmExtAvgRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 15),
    _CalixSoamExtMepDmExtAvgRoundTripDelay_Type()
)
calixSoamExtMepDmExtAvgRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtAvgRoundTripDelay.setStatus("current")
_CalixSoamExtMepDmExtMinRoundTripDelay_Type = Unsigned32
_CalixSoamExtMepDmExtMinRoundTripDelay_Object = MibTableColumn
calixSoamExtMepDmExtMinRoundTripDelay = _CalixSoamExtMepDmExtMinRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 16),
    _CalixSoamExtMepDmExtMinRoundTripDelay_Type()
)
calixSoamExtMepDmExtMinRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtMinRoundTripDelay.setStatus("current")
_CalixSoamExtMepDmExtMaxRoundTripDelay_Type = Unsigned32
_CalixSoamExtMepDmExtMaxRoundTripDelay_Object = MibTableColumn
calixSoamExtMepDmExtMaxRoundTripDelay = _CalixSoamExtMepDmExtMaxRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 17),
    _CalixSoamExtMepDmExtMaxRoundTripDelay_Type()
)
calixSoamExtMepDmExtMaxRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtMaxRoundTripDelay.setStatus("current")
_CalixSoamExtMepDmExtAvgRoundTripDelayVariation_Type = Unsigned32
_CalixSoamExtMepDmExtAvgRoundTripDelayVariation_Object = MibTableColumn
calixSoamExtMepDmExtAvgRoundTripDelayVariation = _CalixSoamExtMepDmExtAvgRoundTripDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 18),
    _CalixSoamExtMepDmExtAvgRoundTripDelayVariation_Type()
)
calixSoamExtMepDmExtAvgRoundTripDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtAvgRoundTripDelayVariation.setStatus("current")
_CalixSoamExtMepDmExtMinRoundTripDelayVariation_Type = Unsigned32
_CalixSoamExtMepDmExtMinRoundTripDelayVariation_Object = MibTableColumn
calixSoamExtMepDmExtMinRoundTripDelayVariation = _CalixSoamExtMepDmExtMinRoundTripDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 19),
    _CalixSoamExtMepDmExtMinRoundTripDelayVariation_Type()
)
calixSoamExtMepDmExtMinRoundTripDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtMinRoundTripDelayVariation.setStatus("current")
_CalixSoamExtMepDmExtMaxRoundTripDelayVariation_Type = Unsigned32
_CalixSoamExtMepDmExtMaxRoundTripDelayVariation_Object = MibTableColumn
calixSoamExtMepDmExtMaxRoundTripDelayVariation = _CalixSoamExtMepDmExtMaxRoundTripDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 20),
    _CalixSoamExtMepDmExtMaxRoundTripDelayVariation_Type()
)
calixSoamExtMepDmExtMaxRoundTripDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtMaxRoundTripDelayVariation.setStatus("current")
_CalixSoamExtMepDmExtAvgRoundTripProcessingDelay_Type = Unsigned32
_CalixSoamExtMepDmExtAvgRoundTripProcessingDelay_Object = MibTableColumn
calixSoamExtMepDmExtAvgRoundTripProcessingDelay = _CalixSoamExtMepDmExtAvgRoundTripProcessingDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 21),
    _CalixSoamExtMepDmExtAvgRoundTripProcessingDelay_Type()
)
calixSoamExtMepDmExtAvgRoundTripProcessingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtAvgRoundTripProcessingDelay.setStatus("current")
_CalixSoamExtMepDmExtMinRoundTripProcessingDelay_Type = Unsigned32
_CalixSoamExtMepDmExtMinRoundTripProcessingDelay_Object = MibTableColumn
calixSoamExtMepDmExtMinRoundTripProcessingDelay = _CalixSoamExtMepDmExtMinRoundTripProcessingDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 22),
    _CalixSoamExtMepDmExtMinRoundTripProcessingDelay_Type()
)
calixSoamExtMepDmExtMinRoundTripProcessingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtMinRoundTripProcessingDelay.setStatus("current")
_CalixSoamExtMepDmExtMaxRoundTripProcessingDelay_Type = Unsigned32
_CalixSoamExtMepDmExtMaxRoundTripProcessingDelay_Object = MibTableColumn
calixSoamExtMepDmExtMaxRoundTripProcessingDelay = _CalixSoamExtMepDmExtMaxRoundTripProcessingDelay_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 23),
    _CalixSoamExtMepDmExtMaxRoundTripProcessingDelay_Type()
)
calixSoamExtMepDmExtMaxRoundTripProcessingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtMaxRoundTripProcessingDelay.setStatus("current")
_CalixSoamExtMepDmExtDataLength_Type = Unsigned32
_CalixSoamExtMepDmExtDataLength_Object = MibTableColumn
calixSoamExtMepDmExtDataLength = _CalixSoamExtMepDmExtDataLength_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 24),
    _CalixSoamExtMepDmExtDataLength_Type()
)
calixSoamExtMepDmExtDataLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtDataLength.setStatus("current")
_CalixSoamExtMepDmExtDataPattern_Type = Unsigned32
_CalixSoamExtMepDmExtDataPattern_Object = MibTableColumn
calixSoamExtMepDmExtDataPattern = _CalixSoamExtMepDmExtDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 4, 1, 25),
    _CalixSoamExtMepDmExtDataPattern_Type()
)
calixSoamExtMepDmExtDataPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepDmExtDataPattern.setStatus("current")
_CalixSoamExtMepLmExtTable_Object = MibTable
calixSoamExtMepLmExtTable = _CalixSoamExtMepLmExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5)
)
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtTable.setStatus("current")
_CalixSoamExtMepLmExtEntry_Object = MibTableRow
calixSoamExtMepLmExtEntry = _CalixSoamExtMepLmExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1)
)
calixSoamExtMepLmExtEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtEntry.setStatus("current")
_CalixSoamExtMepLmExtActive_Type = CalixEoamEnableType
_CalixSoamExtMepLmExtActive_Object = MibTableColumn
calixSoamExtMepLmExtActive = _CalixSoamExtMepLmExtActive_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 1),
    _CalixSoamExtMepLmExtActive_Type()
)
calixSoamExtMepLmExtActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtActive.setStatus("current")
_CalixSoamExtMepLmExtDestMacAddress_Type = MacAddress
_CalixSoamExtMepLmExtDestMacAddress_Object = MibTableColumn
calixSoamExtMepLmExtDestMacAddress = _CalixSoamExtMepLmExtDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 2),
    _CalixSoamExtMepLmExtDestMacAddress_Type()
)
calixSoamExtMepLmExtDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtDestMacAddress.setStatus("current")
_CalixSoamExtMepLmExtDestMepId_Type = Dot1agCfmMepIdOrZero
_CalixSoamExtMepLmExtDestMepId_Object = MibTableColumn
calixSoamExtMepLmExtDestMepId = _CalixSoamExtMepLmExtDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 3),
    _CalixSoamExtMepLmExtDestMepId_Type()
)
calixSoamExtMepLmExtDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtDestMepId.setStatus("current")
_CalixSoamExtMepLmExtDestIsMepId_Type = TruthValue
_CalixSoamExtMepLmExtDestIsMepId_Object = MibTableColumn
calixSoamExtMepLmExtDestIsMepId = _CalixSoamExtMepLmExtDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 4),
    _CalixSoamExtMepLmExtDestIsMepId_Type()
)
calixSoamExtMepLmExtDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtDestIsMepId.setStatus("current")
_CalixSoamExtMepLmExtLmType_Type = CalixSoamLmType
_CalixSoamExtMepLmExtLmType_Object = MibTableColumn
calixSoamExtMepLmExtLmType = _CalixSoamExtMepLmExtLmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 5),
    _CalixSoamExtMepLmExtLmType_Type()
)
calixSoamExtMepLmExtLmType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtLmType.setStatus("current")


class _CalixSoamExtMepLmExtClassOfService_Type(Unsigned32):
    """Custom type calixSoamExtMepLmExtClassOfService based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CalixSoamExtMepLmExtClassOfService_Type.__name__ = "Unsigned32"
_CalixSoamExtMepLmExtClassOfService_Object = MibTableColumn
calixSoamExtMepLmExtClassOfService = _CalixSoamExtMepLmExtClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 6),
    _CalixSoamExtMepLmExtClassOfService_Type()
)
calixSoamExtMepLmExtClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtClassOfService.setStatus("current")


class _CalixSoamExtMepLmExtLmPeriod_Type(Integer32):
    """Custom type calixSoamExtMepLmExtLmPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lm100ms", 1),
          ("lm1sec", 2),
          ("lm10sec", 3))
    )


_CalixSoamExtMepLmExtLmPeriod_Type.__name__ = "Integer32"
_CalixSoamExtMepLmExtLmPeriod_Object = MibTableColumn
calixSoamExtMepLmExtLmPeriod = _CalixSoamExtMepLmExtLmPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 7),
    _CalixSoamExtMepLmExtLmPeriod_Type()
)
calixSoamExtMepLmExtLmPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtLmPeriod.setStatus("current")


class _CalixSoamExtMepLmExtMaxNearEndLossThrSet_Type(Unsigned32):
    """Custom type calixSoamExtMepLmExtMaxNearEndLossThrSet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CalixSoamExtMepLmExtMaxNearEndLossThrSet_Type.__name__ = "Unsigned32"
_CalixSoamExtMepLmExtMaxNearEndLossThrSet_Object = MibTableColumn
calixSoamExtMepLmExtMaxNearEndLossThrSet = _CalixSoamExtMepLmExtMaxNearEndLossThrSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 8),
    _CalixSoamExtMepLmExtMaxNearEndLossThrSet_Type()
)
calixSoamExtMepLmExtMaxNearEndLossThrSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtMaxNearEndLossThrSet.setStatus("current")


class _CalixSoamExtMepLmExtMaxNearEndLossThrClr_Type(Unsigned32):
    """Custom type calixSoamExtMepLmExtMaxNearEndLossThrClr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CalixSoamExtMepLmExtMaxNearEndLossThrClr_Type.__name__ = "Unsigned32"
_CalixSoamExtMepLmExtMaxNearEndLossThrClr_Object = MibTableColumn
calixSoamExtMepLmExtMaxNearEndLossThrClr = _CalixSoamExtMepLmExtMaxNearEndLossThrClr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 9),
    _CalixSoamExtMepLmExtMaxNearEndLossThrClr_Type()
)
calixSoamExtMepLmExtMaxNearEndLossThrClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtMaxNearEndLossThrClr.setStatus("current")


class _CalixSoamExtMepLmExtAvgNearEndLossThrSet_Type(Unsigned32):
    """Custom type calixSoamExtMepLmExtAvgNearEndLossThrSet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CalixSoamExtMepLmExtAvgNearEndLossThrSet_Type.__name__ = "Unsigned32"
_CalixSoamExtMepLmExtAvgNearEndLossThrSet_Object = MibTableColumn
calixSoamExtMepLmExtAvgNearEndLossThrSet = _CalixSoamExtMepLmExtAvgNearEndLossThrSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 10),
    _CalixSoamExtMepLmExtAvgNearEndLossThrSet_Type()
)
calixSoamExtMepLmExtAvgNearEndLossThrSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtAvgNearEndLossThrSet.setStatus("current")


class _CalixSoamExtMepLmExtAvgNearEndLossThrClr_Type(Unsigned32):
    """Custom type calixSoamExtMepLmExtAvgNearEndLossThrClr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CalixSoamExtMepLmExtAvgNearEndLossThrClr_Type.__name__ = "Unsigned32"
_CalixSoamExtMepLmExtAvgNearEndLossThrClr_Object = MibTableColumn
calixSoamExtMepLmExtAvgNearEndLossThrClr = _CalixSoamExtMepLmExtAvgNearEndLossThrClr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 11),
    _CalixSoamExtMepLmExtAvgNearEndLossThrClr_Type()
)
calixSoamExtMepLmExtAvgNearEndLossThrClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtAvgNearEndLossThrClr.setStatus("current")


class _CalixSoamExtMepLmExtMaxFarEndLossThrSet_Type(Unsigned32):
    """Custom type calixSoamExtMepLmExtMaxFarEndLossThrSet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CalixSoamExtMepLmExtMaxFarEndLossThrSet_Type.__name__ = "Unsigned32"
_CalixSoamExtMepLmExtMaxFarEndLossThrSet_Object = MibTableColumn
calixSoamExtMepLmExtMaxFarEndLossThrSet = _CalixSoamExtMepLmExtMaxFarEndLossThrSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 12),
    _CalixSoamExtMepLmExtMaxFarEndLossThrSet_Type()
)
calixSoamExtMepLmExtMaxFarEndLossThrSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtMaxFarEndLossThrSet.setStatus("current")


class _CalixSoamExtMepLmExtMaxFarEndLossThrClr_Type(Unsigned32):
    """Custom type calixSoamExtMepLmExtMaxFarEndLossThrClr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CalixSoamExtMepLmExtMaxFarEndLossThrClr_Type.__name__ = "Unsigned32"
_CalixSoamExtMepLmExtMaxFarEndLossThrClr_Object = MibTableColumn
calixSoamExtMepLmExtMaxFarEndLossThrClr = _CalixSoamExtMepLmExtMaxFarEndLossThrClr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 13),
    _CalixSoamExtMepLmExtMaxFarEndLossThrClr_Type()
)
calixSoamExtMepLmExtMaxFarEndLossThrClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtMaxFarEndLossThrClr.setStatus("current")


class _CalixSoamExtMepLmExtAvgFarEndLossThrSet_Type(Unsigned32):
    """Custom type calixSoamExtMepLmExtAvgFarEndLossThrSet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CalixSoamExtMepLmExtAvgFarEndLossThrSet_Type.__name__ = "Unsigned32"
_CalixSoamExtMepLmExtAvgFarEndLossThrSet_Object = MibTableColumn
calixSoamExtMepLmExtAvgFarEndLossThrSet = _CalixSoamExtMepLmExtAvgFarEndLossThrSet_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 14),
    _CalixSoamExtMepLmExtAvgFarEndLossThrSet_Type()
)
calixSoamExtMepLmExtAvgFarEndLossThrSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtAvgFarEndLossThrSet.setStatus("current")


class _CalixSoamExtMepLmExtAvgFarEndLossThrClr_Type(Unsigned32):
    """Custom type calixSoamExtMepLmExtAvgFarEndLossThrClr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CalixSoamExtMepLmExtAvgFarEndLossThrClr_Type.__name__ = "Unsigned32"
_CalixSoamExtMepLmExtAvgFarEndLossThrClr_Object = MibTableColumn
calixSoamExtMepLmExtAvgFarEndLossThrClr = _CalixSoamExtMepLmExtAvgFarEndLossThrClr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 15),
    _CalixSoamExtMepLmExtAvgFarEndLossThrClr_Type()
)
calixSoamExtMepLmExtAvgFarEndLossThrClr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtAvgFarEndLossThrClr.setStatus("current")
_CalixSoamExtMepLmExtNearEndLostPkts_Type = Counter32
_CalixSoamExtMepLmExtNearEndLostPkts_Object = MibTableColumn
calixSoamExtMepLmExtNearEndLostPkts = _CalixSoamExtMepLmExtNearEndLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 16),
    _CalixSoamExtMepLmExtNearEndLostPkts_Type()
)
calixSoamExtMepLmExtNearEndLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtNearEndLostPkts.setStatus("current")
_CalixSoamExtMepLmExtNearEndLossRatio_Type = Unsigned32
_CalixSoamExtMepLmExtNearEndLossRatio_Object = MibTableColumn
calixSoamExtMepLmExtNearEndLossRatio = _CalixSoamExtMepLmExtNearEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 17),
    _CalixSoamExtMepLmExtNearEndLossRatio_Type()
)
calixSoamExtMepLmExtNearEndLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtNearEndLossRatio.setStatus("current")
_CalixSoamExtMepLmExtMaxNearEndLossRatio_Type = Unsigned32
_CalixSoamExtMepLmExtMaxNearEndLossRatio_Object = MibTableColumn
calixSoamExtMepLmExtMaxNearEndLossRatio = _CalixSoamExtMepLmExtMaxNearEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 18),
    _CalixSoamExtMepLmExtMaxNearEndLossRatio_Type()
)
calixSoamExtMepLmExtMaxNearEndLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtMaxNearEndLossRatio.setStatus("current")
_CalixSoamExtMepLmExtMinNearEndLossRatio_Type = Unsigned32
_CalixSoamExtMepLmExtMinNearEndLossRatio_Object = MibTableColumn
calixSoamExtMepLmExtMinNearEndLossRatio = _CalixSoamExtMepLmExtMinNearEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 19),
    _CalixSoamExtMepLmExtMinNearEndLossRatio_Type()
)
calixSoamExtMepLmExtMinNearEndLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtMinNearEndLossRatio.setStatus("current")
_CalixSoamExtMepLmExtAvgNearEndLossRatio_Type = Unsigned32
_CalixSoamExtMepLmExtAvgNearEndLossRatio_Object = MibTableColumn
calixSoamExtMepLmExtAvgNearEndLossRatio = _CalixSoamExtMepLmExtAvgNearEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 20),
    _CalixSoamExtMepLmExtAvgNearEndLossRatio_Type()
)
calixSoamExtMepLmExtAvgNearEndLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtAvgNearEndLossRatio.setStatus("current")
_CalixSoamExtMepLmExtFarEndLostPkts_Type = Counter32
_CalixSoamExtMepLmExtFarEndLostPkts_Object = MibTableColumn
calixSoamExtMepLmExtFarEndLostPkts = _CalixSoamExtMepLmExtFarEndLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 21),
    _CalixSoamExtMepLmExtFarEndLostPkts_Type()
)
calixSoamExtMepLmExtFarEndLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtFarEndLostPkts.setStatus("current")
_CalixSoamExtMepLmExtFarEndLossRatio_Type = Unsigned32
_CalixSoamExtMepLmExtFarEndLossRatio_Object = MibTableColumn
calixSoamExtMepLmExtFarEndLossRatio = _CalixSoamExtMepLmExtFarEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 22),
    _CalixSoamExtMepLmExtFarEndLossRatio_Type()
)
calixSoamExtMepLmExtFarEndLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtFarEndLossRatio.setStatus("current")
_CalixSoamExtMepLmExtMaxFarEndLossRatio_Type = Unsigned32
_CalixSoamExtMepLmExtMaxFarEndLossRatio_Object = MibTableColumn
calixSoamExtMepLmExtMaxFarEndLossRatio = _CalixSoamExtMepLmExtMaxFarEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 23),
    _CalixSoamExtMepLmExtMaxFarEndLossRatio_Type()
)
calixSoamExtMepLmExtMaxFarEndLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtMaxFarEndLossRatio.setStatus("current")
_CalixSoamExtMepLmExtMinFarEndLossRatio_Type = Unsigned32
_CalixSoamExtMepLmExtMinFarEndLossRatio_Object = MibTableColumn
calixSoamExtMepLmExtMinFarEndLossRatio = _CalixSoamExtMepLmExtMinFarEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 24),
    _CalixSoamExtMepLmExtMinFarEndLossRatio_Type()
)
calixSoamExtMepLmExtMinFarEndLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtMinFarEndLossRatio.setStatus("current")
_CalixSoamExtMepLmExtAvgFarEndLossRatio_Type = Unsigned32
_CalixSoamExtMepLmExtAvgFarEndLossRatio_Object = MibTableColumn
calixSoamExtMepLmExtAvgFarEndLossRatio = _CalixSoamExtMepLmExtAvgFarEndLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 5, 1, 25),
    _CalixSoamExtMepLmExtAvgFarEndLossRatio_Type()
)
calixSoamExtMepLmExtAvgFarEndLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepLmExtAvgFarEndLossRatio.setStatus("current")
_CalixSoamExtMepMcastLoopbackSessionTable_Object = MibTable
calixSoamExtMepMcastLoopbackSessionTable = _CalixSoamExtMepMcastLoopbackSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 6)
)
if mibBuilder.loadTexts:
    calixSoamExtMepMcastLoopbackSessionTable.setStatus("current")
_CalixSoamExtMepMcastLoopbackSessionEntry_Object = MibTableRow
calixSoamExtMepMcastLoopbackSessionEntry = _CalixSoamExtMepMcastLoopbackSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 6, 1)
)
calixSoamExtMepMcastLoopbackSessionEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    calixSoamExtMepMcastLoopbackSessionEntry.setStatus("current")


class _CalixSoamExtMepMcastLoopbackSessionStatus_Type(Integer32):
    """Custom type calixSoamExtMepMcastLoopbackSessionStatus based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("activate", 4),
          ("failed", 5))
    )


_CalixSoamExtMepMcastLoopbackSessionStatus_Type.__name__ = "Integer32"
_CalixSoamExtMepMcastLoopbackSessionStatus_Object = MibTableColumn
calixSoamExtMepMcastLoopbackSessionStatus = _CalixSoamExtMepMcastLoopbackSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 6, 1, 1),
    _CalixSoamExtMepMcastLoopbackSessionStatus_Type()
)
calixSoamExtMepMcastLoopbackSessionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepMcastLoopbackSessionStatus.setStatus("current")
_CalixSoamExtMepMcastLoopbackSessionReplies_Type = Unsigned32
_CalixSoamExtMepMcastLoopbackSessionReplies_Object = MibTableColumn
calixSoamExtMepMcastLoopbackSessionReplies = _CalixSoamExtMepMcastLoopbackSessionReplies_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 6, 1, 2),
    _CalixSoamExtMepMcastLoopbackSessionReplies_Type()
)
calixSoamExtMepMcastLoopbackSessionReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepMcastLoopbackSessionReplies.setStatus("current")
_CalixSoamExtMepMcastLoopbackResultsTable_Object = MibTable
calixSoamExtMepMcastLoopbackResultsTable = _CalixSoamExtMepMcastLoopbackResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 7)
)
if mibBuilder.loadTexts:
    calixSoamExtMepMcastLoopbackResultsTable.setStatus("current")
_CalixSoamExtMepMcastLoopbackResultsEntry_Object = MibTableRow
calixSoamExtMepMcastLoopbackResultsEntry = _CalixSoamExtMepMcastLoopbackResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 7, 1)
)
calixSoamExtMepMcastLoopbackResultsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "CALIX-EOAM-EXT-MIB", "calixSoamExtMepMcastLoopbackResultsIndex"),
)
if mibBuilder.loadTexts:
    calixSoamExtMepMcastLoopbackResultsEntry.setStatus("current")
_CalixSoamExtMepMcastLoopbackResultsIndex_Type = Unsigned32
_CalixSoamExtMepMcastLoopbackResultsIndex_Object = MibTableColumn
calixSoamExtMepMcastLoopbackResultsIndex = _CalixSoamExtMepMcastLoopbackResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 7, 1, 1),
    _CalixSoamExtMepMcastLoopbackResultsIndex_Type()
)
calixSoamExtMepMcastLoopbackResultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    calixSoamExtMepMcastLoopbackResultsIndex.setStatus("current")
_CalixSoamExtMepMcastLoopbackResultsMacAddress_Type = MacAddress
_CalixSoamExtMepMcastLoopbackResultsMacAddress_Object = MibTableColumn
calixSoamExtMepMcastLoopbackResultsMacAddress = _CalixSoamExtMepMcastLoopbackResultsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 7, 1, 2),
    _CalixSoamExtMepMcastLoopbackResultsMacAddress_Type()
)
calixSoamExtMepMcastLoopbackResultsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepMcastLoopbackResultsMacAddress.setStatus("current")
_CalixSoamExtMepStatsExtTable_Object = MibTable
calixSoamExtMepStatsExtTable = _CalixSoamExtMepStatsExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8)
)
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtTable.setStatus("current")
_CalixSoamExtMepStatsExtEntry_Object = MibTableRow
calixSoamExtMepStatsExtEntry = _CalixSoamExtMepStatsExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1)
)
calixSoamExtMepStatsExtEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtEntry.setStatus("current")
_CalixSoamExtMepStatsExtCcmRdiSent_Type = Counter32
_CalixSoamExtMepStatsExtCcmRdiSent_Object = MibTableColumn
calixSoamExtMepStatsExtCcmRdiSent = _CalixSoamExtMepStatsExtCcmRdiSent_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 1),
    _CalixSoamExtMepStatsExtCcmRdiSent_Type()
)
calixSoamExtMepStatsExtCcmRdiSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtCcmRdiSent.setStatus("current")
_CalixSoamExtMepStatsExtCcmReceived_Type = Counter32
_CalixSoamExtMepStatsExtCcmReceived_Object = MibTableColumn
calixSoamExtMepStatsExtCcmReceived = _CalixSoamExtMepStatsExtCcmReceived_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 2),
    _CalixSoamExtMepStatsExtCcmReceived_Type()
)
calixSoamExtMepStatsExtCcmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtCcmReceived.setStatus("current")
_CalixSoamExtMepStatsExtCcmInvalidSenderId_Type = Counter32
_CalixSoamExtMepStatsExtCcmInvalidSenderId_Object = MibTableColumn
calixSoamExtMepStatsExtCcmInvalidSenderId = _CalixSoamExtMepStatsExtCcmInvalidSenderId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 3),
    _CalixSoamExtMepStatsExtCcmInvalidSenderId_Type()
)
calixSoamExtMepStatsExtCcmInvalidSenderId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtCcmInvalidSenderId.setStatus("current")
_CalixSoamExtMepStatsExtCcmInvalidPortStatus_Type = Counter32
_CalixSoamExtMepStatsExtCcmInvalidPortStatus_Object = MibTableColumn
calixSoamExtMepStatsExtCcmInvalidPortStatus = _CalixSoamExtMepStatsExtCcmInvalidPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 4),
    _CalixSoamExtMepStatsExtCcmInvalidPortStatus_Type()
)
calixSoamExtMepStatsExtCcmInvalidPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtCcmInvalidPortStatus.setStatus("current")
_CalixSoamExtMepStatsExtCcmInvalidIfStatus_Type = Counter32
_CalixSoamExtMepStatsExtCcmInvalidIfStatus_Object = MibTableColumn
calixSoamExtMepStatsExtCcmInvalidIfStatus = _CalixSoamExtMepStatsExtCcmInvalidIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 5),
    _CalixSoamExtMepStatsExtCcmInvalidIfStatus_Type()
)
calixSoamExtMepStatsExtCcmInvalidIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtCcmInvalidIfStatus.setStatus("current")
_CalixSoamExtMepStatsExtCcmRdiReceived_Type = Counter32
_CalixSoamExtMepStatsExtCcmRdiReceived_Object = MibTableColumn
calixSoamExtMepStatsExtCcmRdiReceived = _CalixSoamExtMepStatsExtCcmRdiReceived_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 6),
    _CalixSoamExtMepStatsExtCcmRdiReceived_Type()
)
calixSoamExtMepStatsExtCcmRdiReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtCcmRdiReceived.setStatus("current")
_CalixSoamExtMepStatsExtLbmReceived_Type = Counter32
_CalixSoamExtMepStatsExtLbmReceived_Object = MibTableColumn
calixSoamExtMepStatsExtLbmReceived = _CalixSoamExtMepStatsExtLbmReceived_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 7),
    _CalixSoamExtMepStatsExtLbmReceived_Type()
)
calixSoamExtMepStatsExtLbmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtLbmReceived.setStatus("current")
_CalixSoamExtMepStatsExtLbmSent_Type = Counter32
_CalixSoamExtMepStatsExtLbmSent_Object = MibTableColumn
calixSoamExtMepStatsExtLbmSent = _CalixSoamExtMepStatsExtLbmSent_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 8),
    _CalixSoamExtMepStatsExtLbmSent_Type()
)
calixSoamExtMepStatsExtLbmSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtLbmSent.setStatus("current")
_CalixSoamExtMepStatsExtLbmInvalidSenderId_Type = Counter32
_CalixSoamExtMepStatsExtLbmInvalidSenderId_Object = MibTableColumn
calixSoamExtMepStatsExtLbmInvalidSenderId = _CalixSoamExtMepStatsExtLbmInvalidSenderId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 9),
    _CalixSoamExtMepStatsExtLbmInvalidSenderId_Type()
)
calixSoamExtMepStatsExtLbmInvalidSenderId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtLbmInvalidSenderId.setStatus("current")
_CalixSoamExtMepStatsExtLbrInvalidSenderId_Type = Counter32
_CalixSoamExtMepStatsExtLbrInvalidSenderId_Object = MibTableColumn
calixSoamExtMepStatsExtLbrInvalidSenderId = _CalixSoamExtMepStatsExtLbrInvalidSenderId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 10),
    _CalixSoamExtMepStatsExtLbrInvalidSenderId_Type()
)
calixSoamExtMepStatsExtLbrInvalidSenderId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtLbrInvalidSenderId.setStatus("current")
_CalixSoamExtMepStatsExtLtmReceived_Type = Counter32
_CalixSoamExtMepStatsExtLtmReceived_Object = MibTableColumn
calixSoamExtMepStatsExtLtmReceived = _CalixSoamExtMepStatsExtLtmReceived_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 11),
    _CalixSoamExtMepStatsExtLtmReceived_Type()
)
calixSoamExtMepStatsExtLtmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtLtmReceived.setStatus("current")
_CalixSoamExtMepStatsExtLtmSent_Type = Counter32
_CalixSoamExtMepStatsExtLtmSent_Object = MibTableColumn
calixSoamExtMepStatsExtLtmSent = _CalixSoamExtMepStatsExtLtmSent_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 12),
    _CalixSoamExtMepStatsExtLtmSent_Type()
)
calixSoamExtMepStatsExtLtmSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtLtmSent.setStatus("current")
_CalixSoamExtMepStatsExtLtrInvalidMac_Type = Counter32
_CalixSoamExtMepStatsExtLtrInvalidMac_Object = MibTableColumn
calixSoamExtMepStatsExtLtrInvalidMac = _CalixSoamExtMepStatsExtLtrInvalidMac_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 13),
    _CalixSoamExtMepStatsExtLtrInvalidMac_Type()
)
calixSoamExtMepStatsExtLtrInvalidMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtLtrInvalidMac.setStatus("current")
_CalixSoamExtMepStatsExtLtrReceived_Type = Counter32
_CalixSoamExtMepStatsExtLtrReceived_Object = MibTableColumn
calixSoamExtMepStatsExtLtrReceived = _CalixSoamExtMepStatsExtLtrReceived_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 14),
    _CalixSoamExtMepStatsExtLtrReceived_Type()
)
calixSoamExtMepStatsExtLtrReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtLtrReceived.setStatus("current")
_CalixSoamExtMepStatsExtLtrSent_Type = Counter32
_CalixSoamExtMepStatsExtLtrSent_Object = MibTableColumn
calixSoamExtMepStatsExtLtrSent = _CalixSoamExtMepStatsExtLtrSent_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 15),
    _CalixSoamExtMepStatsExtLtrSent_Type()
)
calixSoamExtMepStatsExtLtrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtLtrSent.setStatus("current")
_CalixSoamExtMepStatsExtLmmReceived_Type = Counter32
_CalixSoamExtMepStatsExtLmmReceived_Object = MibTableColumn
calixSoamExtMepStatsExtLmmReceived = _CalixSoamExtMepStatsExtLmmReceived_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 16),
    _CalixSoamExtMepStatsExtLmmReceived_Type()
)
calixSoamExtMepStatsExtLmmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtLmmReceived.setStatus("current")
_CalixSoamExtMepStatsExtLmmSent_Type = Counter32
_CalixSoamExtMepStatsExtLmmSent_Object = MibTableColumn
calixSoamExtMepStatsExtLmmSent = _CalixSoamExtMepStatsExtLmmSent_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 17),
    _CalixSoamExtMepStatsExtLmmSent_Type()
)
calixSoamExtMepStatsExtLmmSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtLmmSent.setStatus("current")
_CalixSoamExtMepStatsExtLmrReceived_Type = Counter32
_CalixSoamExtMepStatsExtLmrReceived_Object = MibTableColumn
calixSoamExtMepStatsExtLmrReceived = _CalixSoamExtMepStatsExtLmrReceived_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 18),
    _CalixSoamExtMepStatsExtLmrReceived_Type()
)
calixSoamExtMepStatsExtLmrReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtLmrReceived.setStatus("current")
_CalixSoamExtMepStatsExtLmrSent_Type = Counter32
_CalixSoamExtMepStatsExtLmrSent_Object = MibTableColumn
calixSoamExtMepStatsExtLmrSent = _CalixSoamExtMepStatsExtLmrSent_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 19),
    _CalixSoamExtMepStatsExtLmrSent_Type()
)
calixSoamExtMepStatsExtLmrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtLmrSent.setStatus("current")
_CalixSoamExtMepStatsExtDmmReceived_Type = Counter32
_CalixSoamExtMepStatsExtDmmReceived_Object = MibTableColumn
calixSoamExtMepStatsExtDmmReceived = _CalixSoamExtMepStatsExtDmmReceived_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 20),
    _CalixSoamExtMepStatsExtDmmReceived_Type()
)
calixSoamExtMepStatsExtDmmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtDmmReceived.setStatus("current")
_CalixSoamExtMepStatsExtDmmSent_Type = Counter32
_CalixSoamExtMepStatsExtDmmSent_Object = MibTableColumn
calixSoamExtMepStatsExtDmmSent = _CalixSoamExtMepStatsExtDmmSent_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 21),
    _CalixSoamExtMepStatsExtDmmSent_Type()
)
calixSoamExtMepStatsExtDmmSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtDmmSent.setStatus("current")
_CalixSoamExtMepStatsExtDmrReceived_Type = Counter32
_CalixSoamExtMepStatsExtDmrReceived_Object = MibTableColumn
calixSoamExtMepStatsExtDmrReceived = _CalixSoamExtMepStatsExtDmrReceived_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 22),
    _CalixSoamExtMepStatsExtDmrReceived_Type()
)
calixSoamExtMepStatsExtDmrReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtDmrReceived.setStatus("current")
_CalixSoamExtMepStatsExtDmrSent_Type = Counter32
_CalixSoamExtMepStatsExtDmrSent_Object = MibTableColumn
calixSoamExtMepStatsExtDmrSent = _CalixSoamExtMepStatsExtDmrSent_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 23),
    _CalixSoamExtMepStatsExtDmrSent_Type()
)
calixSoamExtMepStatsExtDmrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtDmrSent.setStatus("current")
_CalixSoamExtMepStatsExtResetStat_Type = TruthValue
_CalixSoamExtMepStatsExtResetStat_Object = MibTableColumn
calixSoamExtMepStatsExtResetStat = _CalixSoamExtMepStatsExtResetStat_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 8, 1, 24),
    _CalixSoamExtMepStatsExtResetStat_Type()
)
calixSoamExtMepStatsExtResetStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtMepStatsExtResetStat.setStatus("current")
_CalixSoamExtMepUcastLoopbackResultsTable_Object = MibTable
calixSoamExtMepUcastLoopbackResultsTable = _CalixSoamExtMepUcastLoopbackResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 9)
)
if mibBuilder.loadTexts:
    calixSoamExtMepUcastLoopbackResultsTable.setStatus("current")
_CalixSoamExtMepUcastLoopbackResultsEntry_Object = MibTableRow
calixSoamExtMepUcastLoopbackResultsEntry = _CalixSoamExtMepUcastLoopbackResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 9, 1)
)
calixSoamExtMepUcastLoopbackResultsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    calixSoamExtMepUcastLoopbackResultsEntry.setStatus("current")
_CalixSoamExtMepUcastLoopbackResultsLbmFirstSeqNumber_Type = Unsigned32
_CalixSoamExtMepUcastLoopbackResultsLbmFirstSeqNumber_Object = MibTableColumn
calixSoamExtMepUcastLoopbackResultsLbmFirstSeqNumber = _CalixSoamExtMepUcastLoopbackResultsLbmFirstSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 9, 1, 1),
    _CalixSoamExtMepUcastLoopbackResultsLbmFirstSeqNumber_Type()
)
calixSoamExtMepUcastLoopbackResultsLbmFirstSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepUcastLoopbackResultsLbmFirstSeqNumber.setStatus("current")
_CalixSoamExtMepUcastLoopbackResultsDestMacAddress_Type = MacAddress
_CalixSoamExtMepUcastLoopbackResultsDestMacAddress_Object = MibTableColumn
calixSoamExtMepUcastLoopbackResultsDestMacAddress = _CalixSoamExtMepUcastLoopbackResultsDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 9, 1, 2),
    _CalixSoamExtMepUcastLoopbackResultsDestMacAddress_Type()
)
calixSoamExtMepUcastLoopbackResultsDestMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepUcastLoopbackResultsDestMacAddress.setStatus("current")


class _CalixSoamExtMepUcastLoopbackResultsStatus_Type(Integer32):
    """Custom type calixSoamExtMepUcastLoopbackResultsStatus based on Integer32"""
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
        *(("none", 0),
          ("inProgress", 1),
          ("failed", 2),
          ("succeeded", 3))
    )


_CalixSoamExtMepUcastLoopbackResultsStatus_Type.__name__ = "Integer32"
_CalixSoamExtMepUcastLoopbackResultsStatus_Object = MibTableColumn
calixSoamExtMepUcastLoopbackResultsStatus = _CalixSoamExtMepUcastLoopbackResultsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 9, 1, 3),
    _CalixSoamExtMepUcastLoopbackResultsStatus_Type()
)
calixSoamExtMepUcastLoopbackResultsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepUcastLoopbackResultsStatus.setStatus("current")
_CalixSoamExtMepUcastLoopbackResultsLbmOut_Type = Counter32
_CalixSoamExtMepUcastLoopbackResultsLbmOut_Object = MibTableColumn
calixSoamExtMepUcastLoopbackResultsLbmOut = _CalixSoamExtMepUcastLoopbackResultsLbmOut_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 9, 1, 4),
    _CalixSoamExtMepUcastLoopbackResultsLbmOut_Type()
)
calixSoamExtMepUcastLoopbackResultsLbmOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepUcastLoopbackResultsLbmOut.setStatus("current")
_CalixSoamExtMepUcastLoopbackResultsLbrIn_Type = Counter32
_CalixSoamExtMepUcastLoopbackResultsLbrIn_Object = MibTableColumn
calixSoamExtMepUcastLoopbackResultsLbrIn = _CalixSoamExtMepUcastLoopbackResultsLbrIn_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 9, 1, 5),
    _CalixSoamExtMepUcastLoopbackResultsLbrIn_Type()
)
calixSoamExtMepUcastLoopbackResultsLbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixSoamExtMepUcastLoopbackResultsLbrIn.setStatus("current")
_CalixSoamExtCfgTable_Object = MibTable
calixSoamExtCfgTable = _CalixSoamExtCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10)
)
if mibBuilder.loadTexts:
    calixSoamExtCfgTable.setStatus("current")
_CalixSoamExtCfgEntry_Object = MibTableRow
calixSoamExtCfgEntry = _CalixSoamExtCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1)
)
calixSoamExtCfgEntry.setIndexNames(
    (0, "CALIX-EOAM-EXT-MIB", "calixSoamExtCfgIndex"),
)
if mibBuilder.loadTexts:
    calixSoamExtCfgEntry.setStatus("current")
_CalixSoamExtCfgIndex_Type = Unsigned32
_CalixSoamExtCfgIndex_Object = MibTableColumn
calixSoamExtCfgIndex = _CalixSoamExtCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 1),
    _CalixSoamExtCfgIndex_Type()
)
calixSoamExtCfgIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgIndex.setStatus("current")
_CalixSoamExtCfgAdminState_Type = CalixEoamEnableType
_CalixSoamExtCfgAdminState_Object = MibTableColumn
calixSoamExtCfgAdminState = _CalixSoamExtCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 2),
    _CalixSoamExtCfgAdminState_Type()
)
calixSoamExtCfgAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgAdminState.setStatus("current")
_CalixSoamExtCfgPermission_Type = Dot1agCfmIdPermission
_CalixSoamExtCfgPermission_Object = MibTableColumn
calixSoamExtCfgPermission = _CalixSoamExtCfgPermission_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 3),
    _CalixSoamExtCfgPermission_Type()
)
calixSoamExtCfgPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgPermission.setStatus("current")
_CalixSoamExtCfgChassisIdSubtype_Type = LldpChassisIdSubtype
_CalixSoamExtCfgChassisIdSubtype_Object = MibTableColumn
calixSoamExtCfgChassisIdSubtype = _CalixSoamExtCfgChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 4),
    _CalixSoamExtCfgChassisIdSubtype_Type()
)
calixSoamExtCfgChassisIdSubtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgChassisIdSubtype.setStatus("current")
_CalixSoamExtCfgChassisId_Type = LldpChassisId
_CalixSoamExtCfgChassisId_Object = MibTableColumn
calixSoamExtCfgChassisId = _CalixSoamExtCfgChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 5),
    _CalixSoamExtCfgChassisId_Type()
)
calixSoamExtCfgChassisId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgChassisId.setStatus("current")
_CalixSoamExtCfgManAddressDomain_Type = TDomain
_CalixSoamExtCfgManAddressDomain_Object = MibTableColumn
calixSoamExtCfgManAddressDomain = _CalixSoamExtCfgManAddressDomain_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 6),
    _CalixSoamExtCfgManAddressDomain_Type()
)
calixSoamExtCfgManAddressDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgManAddressDomain.setStatus("current")
_CalixSoamExtCfgManAddress_Type = TAddress
_CalixSoamExtCfgManAddress_Object = MibTableColumn
calixSoamExtCfgManAddress = _CalixSoamExtCfgManAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 7),
    _CalixSoamExtCfgManAddress_Type()
)
calixSoamExtCfgManAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgManAddress.setStatus("current")
_CalixSoamExtCfgCcmOptTlvSenderId_Type = CalixEoamEnableType
_CalixSoamExtCfgCcmOptTlvSenderId_Object = MibTableColumn
calixSoamExtCfgCcmOptTlvSenderId = _CalixSoamExtCfgCcmOptTlvSenderId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 8),
    _CalixSoamExtCfgCcmOptTlvSenderId_Type()
)
calixSoamExtCfgCcmOptTlvSenderId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgCcmOptTlvSenderId.setStatus("current")
_CalixSoamExtCfgCcmOptTlvPortStatus_Type = CalixEoamEnableType
_CalixSoamExtCfgCcmOptTlvPortStatus_Object = MibTableColumn
calixSoamExtCfgCcmOptTlvPortStatus = _CalixSoamExtCfgCcmOptTlvPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 9),
    _CalixSoamExtCfgCcmOptTlvPortStatus_Type()
)
calixSoamExtCfgCcmOptTlvPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgCcmOptTlvPortStatus.setStatus("current")
_CalixSoamExtCfgCcmOptTlvIfStatus_Type = CalixEoamEnableType
_CalixSoamExtCfgCcmOptTlvIfStatus_Object = MibTableColumn
calixSoamExtCfgCcmOptTlvIfStatus = _CalixSoamExtCfgCcmOptTlvIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 10),
    _CalixSoamExtCfgCcmOptTlvIfStatus_Type()
)
calixSoamExtCfgCcmOptTlvIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgCcmOptTlvIfStatus.setStatus("current")
_CalixSoamExtCfgLtmOptTlvSenderId_Type = CalixEoamEnableType
_CalixSoamExtCfgLtmOptTlvSenderId_Object = MibTableColumn
calixSoamExtCfgLtmOptTlvSenderId = _CalixSoamExtCfgLtmOptTlvSenderId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 11),
    _CalixSoamExtCfgLtmOptTlvSenderId_Type()
)
calixSoamExtCfgLtmOptTlvSenderId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgLtmOptTlvSenderId.setStatus("current")
_CalixSoamExtCfgLbmOptTlvSenderId_Type = CalixEoamEnableType
_CalixSoamExtCfgLbmOptTlvSenderId_Object = MibTableColumn
calixSoamExtCfgLbmOptTlvSenderId = _CalixSoamExtCfgLbmOptTlvSenderId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 12),
    _CalixSoamExtCfgLbmOptTlvSenderId_Type()
)
calixSoamExtCfgLbmOptTlvSenderId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgLbmOptTlvSenderId.setStatus("current")
_CalixSoamExtCfgLbmOptTlvIfStatus_Type = CalixEoamEnableType
_CalixSoamExtCfgLbmOptTlvIfStatus_Object = MibTableColumn
calixSoamExtCfgLbmOptTlvIfStatus = _CalixSoamExtCfgLbmOptTlvIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 13),
    _CalixSoamExtCfgLbmOptTlvIfStatus_Type()
)
calixSoamExtCfgLbmOptTlvIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgLbmOptTlvIfStatus.setStatus("current")
_CalixSoamExtCfgLbmOptTlvData_Type = CalixEoamEnableType
_CalixSoamExtCfgLbmOptTlvData_Object = MibTableColumn
calixSoamExtCfgLbmOptTlvData = _CalixSoamExtCfgLbmOptTlvData_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 14),
    _CalixSoamExtCfgLbmOptTlvData_Type()
)
calixSoamExtCfgLbmOptTlvData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgLbmOptTlvData.setStatus("current")
_CalixSoamExtCfgDmmOptTlvData_Type = CalixEoamEnableType
_CalixSoamExtCfgDmmOptTlvData_Object = MibTableColumn
calixSoamExtCfgDmmOptTlvData = _CalixSoamExtCfgDmmOptTlvData_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 10, 1, 15),
    _CalixSoamExtCfgDmmOptTlvData_Type()
)
calixSoamExtCfgDmmOptTlvData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixSoamExtCfgDmmOptTlvData.setStatus("current")
_CalixLoamExtCfgTable_Object = MibTable
calixLoamExtCfgTable = _CalixLoamExtCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 11)
)
if mibBuilder.loadTexts:
    calixLoamExtCfgTable.setStatus("current")
_CalixLoamExtCfgEntry_Object = MibTableRow
calixLoamExtCfgEntry = _CalixLoamExtCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 11, 1)
)
calixLoamExtCfgEntry.setIndexNames(
    (0, "CALIX-EOAM-EXT-MIB", "calixLoamExtCfgIndex"),
)
if mibBuilder.loadTexts:
    calixLoamExtCfgEntry.setStatus("current")
_CalixLoamExtCfgIndex_Type = Unsigned32
_CalixLoamExtCfgIndex_Object = MibTableColumn
calixLoamExtCfgIndex = _CalixLoamExtCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 11, 1, 1),
    _CalixLoamExtCfgIndex_Type()
)
calixLoamExtCfgIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixLoamExtCfgIndex.setStatus("current")
_CalixLoamExtCfgAdminState_Type = CalixEoamEnableType
_CalixLoamExtCfgAdminState_Object = MibTableColumn
calixLoamExtCfgAdminState = _CalixLoamExtCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 11, 1, 2),
    _CalixLoamExtCfgAdminState_Type()
)
calixLoamExtCfgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calixLoamExtCfgAdminState.setStatus("current")
_CalixRfc2544CfgTable_Object = MibTable
calixRfc2544CfgTable = _CalixRfc2544CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 12)
)
if mibBuilder.loadTexts:
    calixRfc2544CfgTable.setStatus("current")
_CalixRfc2544CfgEntry_Object = MibTableRow
calixRfc2544CfgEntry = _CalixRfc2544CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 12, 1)
)
calixRfc2544CfgEntry.setIndexNames(
    (0, "CALIX-EOAM-EXT-MIB", "calixRfc2544CfgIndex"),
)
if mibBuilder.loadTexts:
    calixRfc2544CfgEntry.setStatus("current")
_CalixRfc2544CfgIndex_Type = Unsigned32
_CalixRfc2544CfgIndex_Object = MibTableColumn
calixRfc2544CfgIndex = _CalixRfc2544CfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 12, 1, 1),
    _CalixRfc2544CfgIndex_Type()
)
calixRfc2544CfgIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixRfc2544CfgIndex.setStatus("current")
_CalixRfc2544CfgAdminState_Type = CalixEoamEnableType
_CalixRfc2544CfgAdminState_Object = MibTableColumn
calixRfc2544CfgAdminState = _CalixRfc2544CfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 12, 1, 2),
    _CalixRfc2544CfgAdminState_Type()
)
calixRfc2544CfgAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    calixRfc2544CfgAdminState.setStatus("current")
_CalixRfc2544CfgIfIndex_Type = InterfaceIndex
_CalixRfc2544CfgIfIndex_Object = MibTableColumn
calixRfc2544CfgIfIndex = _CalixRfc2544CfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 12, 1, 3),
    _CalixRfc2544CfgIfIndex_Type()
)
calixRfc2544CfgIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calixRfc2544CfgIfIndex.setStatus("current")
_CalixRfc2544CfgVlanId_Type = VlanId
_CalixRfc2544CfgVlanId_Object = MibTableColumn
calixRfc2544CfgVlanId = _CalixRfc2544CfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 12, 1, 4),
    _CalixRfc2544CfgVlanId_Type()
)
calixRfc2544CfgVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calixRfc2544CfgVlanId.setStatus("current")
_CalixRfc2544CfgMacAddress_Type = MacAddress
_CalixRfc2544CfgMacAddress_Object = MibTableColumn
calixRfc2544CfgMacAddress = _CalixRfc2544CfgMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 99, 1, 12, 1, 5),
    _CalixRfc2544CfgMacAddress_Type()
)
calixRfc2544CfgMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calixRfc2544CfgMacAddress.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CALIX-EOAM-EXT-MIB",
    **{"CalixEoamEnableType": CalixEoamEnableType,
       "CalixSoamLmType": CalixSoamLmType,
       "calixEoamExtMIB": calixEoamExtMIB,
       "calixEoamExtConfig": calixEoamExtConfig,
       "calixSoamExtMegTable": calixSoamExtMegTable,
       "calixSoamExtMegEntry": calixSoamExtMegEntry,
       "calixSoamExtMegIdentifier": calixSoamExtMegIdentifier,
       "calixSoamExtMegName": calixSoamExtMegName,
       "calixSoamExtMegLevel": calixSoamExtMegLevel,
       "calixSoamExtMegCcmInterval": calixSoamExtMegCcmInterval,
       "calixSoamExtMegVid": calixSoamExtMegVid,
       "calixSoamExtMegAutoDiscovery": calixSoamExtMegAutoDiscovery,
       "calixSoamExtMegAutoDiscoveryTimeout": calixSoamExtMegAutoDiscoveryTimeout,
       "calixSoamExtMegCciInterworking": calixSoamExtMegCciInterworking,
       "calixSoamExtMegIdPermission": calixSoamExtMegIdPermission,
       "calixSoamExtMegRowStatus": calixSoamExtMegRowStatus,
       "calixSoamExtMipTable": calixSoamExtMipTable,
       "calixSoamExtMipEntry": calixSoamExtMipEntry,
       "calixSoamExtMipIdentifier": calixSoamExtMipIdentifier,
       "calixSoamExtMipIfIndex": calixSoamExtMipIfIndex,
       "calixSoamExtMipAdminState": calixSoamExtMipAdminState,
       "calixSoamExtMipMacAddress": calixSoamExtMipMacAddress,
       "calixSoamExtMipResetStat": calixSoamExtMipResetStat,
       "calixSoamExtMipRowStatus": calixSoamExtMipRowStatus,
       "calixSoamExtMipStatsTable": calixSoamExtMipStatsTable,
       "calixSoamExtMipStatsEntry": calixSoamExtMipStatsEntry,
       "calixSoamExtMipStatsDirection": calixSoamExtMipStatsDirection,
       "calixSoamExtMipStatsLbmIn": calixSoamExtMipStatsLbmIn,
       "calixSoamExtMipStatsLbrOut": calixSoamExtMipStatsLbrOut,
       "calixSoamExtMipStatsLtmIn": calixSoamExtMipStatsLtmIn,
       "calixSoamExtMipStatsLtmForwarded": calixSoamExtMipStatsLtmForwarded,
       "calixSoamExtMipStatsLtrOut": calixSoamExtMipStatsLtrOut,
       "calixSoamExtMipStatsLbmInvalidSenderId": calixSoamExtMipStatsLbmInvalidSenderId,
       "calixSoamExtMipStatsDiscards": calixSoamExtMipStatsDiscards,
       "calixSoamExtMipStatsResetStat": calixSoamExtMipStatsResetStat,
       "calixSoamExtMepDmExtTable": calixSoamExtMepDmExtTable,
       "calixSoamExtMepDmExtEntry": calixSoamExtMepDmExtEntry,
       "calixSoamExtMepDmExtActive": calixSoamExtMepDmExtActive,
       "calixSoamExtMepDmExtDestMacAddress": calixSoamExtMepDmExtDestMacAddress,
       "calixSoamExtMepDmExtDestMepId": calixSoamExtMepDmExtDestMepId,
       "calixSoamExtMepDmExtDestIsMepId": calixSoamExtMepDmExtDestIsMepId,
       "calixSoamExtMepDmExtClassOfService": calixSoamExtMepDmExtClassOfService,
       "calixSoamExtMepDmExtDmPeriod": calixSoamExtMepDmExtDmPeriod,
       "calixSoamExtMepDmExtMaxRtdThrSet": calixSoamExtMepDmExtMaxRtdThrSet,
       "calixSoamExtMepDmExtMaxRtdThrClr": calixSoamExtMepDmExtMaxRtdThrClr,
       "calixSoamExtMepDmExtAvgRtdThrSet": calixSoamExtMepDmExtAvgRtdThrSet,
       "calixSoamExtMepDmExtAvgRtdThrClr": calixSoamExtMepDmExtAvgRtdThrClr,
       "calixSoamExtMepDmExtMaxRtdVarThrSet": calixSoamExtMepDmExtMaxRtdVarThrSet,
       "calixSoamExtMepDmExtMaxRtdVarThrClr": calixSoamExtMepDmExtMaxRtdVarThrClr,
       "calixSoamExtMepDmExtAvgRtdVarThrSet": calixSoamExtMepDmExtAvgRtdVarThrSet,
       "calixSoamExtMepDmExtAvgRtdVarThrClr": calixSoamExtMepDmExtAvgRtdVarThrClr,
       "calixSoamExtMepDmExtAvgRoundTripDelay": calixSoamExtMepDmExtAvgRoundTripDelay,
       "calixSoamExtMepDmExtMinRoundTripDelay": calixSoamExtMepDmExtMinRoundTripDelay,
       "calixSoamExtMepDmExtMaxRoundTripDelay": calixSoamExtMepDmExtMaxRoundTripDelay,
       "calixSoamExtMepDmExtAvgRoundTripDelayVariation": calixSoamExtMepDmExtAvgRoundTripDelayVariation,
       "calixSoamExtMepDmExtMinRoundTripDelayVariation": calixSoamExtMepDmExtMinRoundTripDelayVariation,
       "calixSoamExtMepDmExtMaxRoundTripDelayVariation": calixSoamExtMepDmExtMaxRoundTripDelayVariation,
       "calixSoamExtMepDmExtAvgRoundTripProcessingDelay": calixSoamExtMepDmExtAvgRoundTripProcessingDelay,
       "calixSoamExtMepDmExtMinRoundTripProcessingDelay": calixSoamExtMepDmExtMinRoundTripProcessingDelay,
       "calixSoamExtMepDmExtMaxRoundTripProcessingDelay": calixSoamExtMepDmExtMaxRoundTripProcessingDelay,
       "calixSoamExtMepDmExtDataLength": calixSoamExtMepDmExtDataLength,
       "calixSoamExtMepDmExtDataPattern": calixSoamExtMepDmExtDataPattern,
       "calixSoamExtMepLmExtTable": calixSoamExtMepLmExtTable,
       "calixSoamExtMepLmExtEntry": calixSoamExtMepLmExtEntry,
       "calixSoamExtMepLmExtActive": calixSoamExtMepLmExtActive,
       "calixSoamExtMepLmExtDestMacAddress": calixSoamExtMepLmExtDestMacAddress,
       "calixSoamExtMepLmExtDestMepId": calixSoamExtMepLmExtDestMepId,
       "calixSoamExtMepLmExtDestIsMepId": calixSoamExtMepLmExtDestIsMepId,
       "calixSoamExtMepLmExtLmType": calixSoamExtMepLmExtLmType,
       "calixSoamExtMepLmExtClassOfService": calixSoamExtMepLmExtClassOfService,
       "calixSoamExtMepLmExtLmPeriod": calixSoamExtMepLmExtLmPeriod,
       "calixSoamExtMepLmExtMaxNearEndLossThrSet": calixSoamExtMepLmExtMaxNearEndLossThrSet,
       "calixSoamExtMepLmExtMaxNearEndLossThrClr": calixSoamExtMepLmExtMaxNearEndLossThrClr,
       "calixSoamExtMepLmExtAvgNearEndLossThrSet": calixSoamExtMepLmExtAvgNearEndLossThrSet,
       "calixSoamExtMepLmExtAvgNearEndLossThrClr": calixSoamExtMepLmExtAvgNearEndLossThrClr,
       "calixSoamExtMepLmExtMaxFarEndLossThrSet": calixSoamExtMepLmExtMaxFarEndLossThrSet,
       "calixSoamExtMepLmExtMaxFarEndLossThrClr": calixSoamExtMepLmExtMaxFarEndLossThrClr,
       "calixSoamExtMepLmExtAvgFarEndLossThrSet": calixSoamExtMepLmExtAvgFarEndLossThrSet,
       "calixSoamExtMepLmExtAvgFarEndLossThrClr": calixSoamExtMepLmExtAvgFarEndLossThrClr,
       "calixSoamExtMepLmExtNearEndLostPkts": calixSoamExtMepLmExtNearEndLostPkts,
       "calixSoamExtMepLmExtNearEndLossRatio": calixSoamExtMepLmExtNearEndLossRatio,
       "calixSoamExtMepLmExtMaxNearEndLossRatio": calixSoamExtMepLmExtMaxNearEndLossRatio,
       "calixSoamExtMepLmExtMinNearEndLossRatio": calixSoamExtMepLmExtMinNearEndLossRatio,
       "calixSoamExtMepLmExtAvgNearEndLossRatio": calixSoamExtMepLmExtAvgNearEndLossRatio,
       "calixSoamExtMepLmExtFarEndLostPkts": calixSoamExtMepLmExtFarEndLostPkts,
       "calixSoamExtMepLmExtFarEndLossRatio": calixSoamExtMepLmExtFarEndLossRatio,
       "calixSoamExtMepLmExtMaxFarEndLossRatio": calixSoamExtMepLmExtMaxFarEndLossRatio,
       "calixSoamExtMepLmExtMinFarEndLossRatio": calixSoamExtMepLmExtMinFarEndLossRatio,
       "calixSoamExtMepLmExtAvgFarEndLossRatio": calixSoamExtMepLmExtAvgFarEndLossRatio,
       "calixSoamExtMepMcastLoopbackSessionTable": calixSoamExtMepMcastLoopbackSessionTable,
       "calixSoamExtMepMcastLoopbackSessionEntry": calixSoamExtMepMcastLoopbackSessionEntry,
       "calixSoamExtMepMcastLoopbackSessionStatus": calixSoamExtMepMcastLoopbackSessionStatus,
       "calixSoamExtMepMcastLoopbackSessionReplies": calixSoamExtMepMcastLoopbackSessionReplies,
       "calixSoamExtMepMcastLoopbackResultsTable": calixSoamExtMepMcastLoopbackResultsTable,
       "calixSoamExtMepMcastLoopbackResultsEntry": calixSoamExtMepMcastLoopbackResultsEntry,
       "calixSoamExtMepMcastLoopbackResultsIndex": calixSoamExtMepMcastLoopbackResultsIndex,
       "calixSoamExtMepMcastLoopbackResultsMacAddress": calixSoamExtMepMcastLoopbackResultsMacAddress,
       "calixSoamExtMepStatsExtTable": calixSoamExtMepStatsExtTable,
       "calixSoamExtMepStatsExtEntry": calixSoamExtMepStatsExtEntry,
       "calixSoamExtMepStatsExtCcmRdiSent": calixSoamExtMepStatsExtCcmRdiSent,
       "calixSoamExtMepStatsExtCcmReceived": calixSoamExtMepStatsExtCcmReceived,
       "calixSoamExtMepStatsExtCcmInvalidSenderId": calixSoamExtMepStatsExtCcmInvalidSenderId,
       "calixSoamExtMepStatsExtCcmInvalidPortStatus": calixSoamExtMepStatsExtCcmInvalidPortStatus,
       "calixSoamExtMepStatsExtCcmInvalidIfStatus": calixSoamExtMepStatsExtCcmInvalidIfStatus,
       "calixSoamExtMepStatsExtCcmRdiReceived": calixSoamExtMepStatsExtCcmRdiReceived,
       "calixSoamExtMepStatsExtLbmReceived": calixSoamExtMepStatsExtLbmReceived,
       "calixSoamExtMepStatsExtLbmSent": calixSoamExtMepStatsExtLbmSent,
       "calixSoamExtMepStatsExtLbmInvalidSenderId": calixSoamExtMepStatsExtLbmInvalidSenderId,
       "calixSoamExtMepStatsExtLbrInvalidSenderId": calixSoamExtMepStatsExtLbrInvalidSenderId,
       "calixSoamExtMepStatsExtLtmReceived": calixSoamExtMepStatsExtLtmReceived,
       "calixSoamExtMepStatsExtLtmSent": calixSoamExtMepStatsExtLtmSent,
       "calixSoamExtMepStatsExtLtrInvalidMac": calixSoamExtMepStatsExtLtrInvalidMac,
       "calixSoamExtMepStatsExtLtrReceived": calixSoamExtMepStatsExtLtrReceived,
       "calixSoamExtMepStatsExtLtrSent": calixSoamExtMepStatsExtLtrSent,
       "calixSoamExtMepStatsExtLmmReceived": calixSoamExtMepStatsExtLmmReceived,
       "calixSoamExtMepStatsExtLmmSent": calixSoamExtMepStatsExtLmmSent,
       "calixSoamExtMepStatsExtLmrReceived": calixSoamExtMepStatsExtLmrReceived,
       "calixSoamExtMepStatsExtLmrSent": calixSoamExtMepStatsExtLmrSent,
       "calixSoamExtMepStatsExtDmmReceived": calixSoamExtMepStatsExtDmmReceived,
       "calixSoamExtMepStatsExtDmmSent": calixSoamExtMepStatsExtDmmSent,
       "calixSoamExtMepStatsExtDmrReceived": calixSoamExtMepStatsExtDmrReceived,
       "calixSoamExtMepStatsExtDmrSent": calixSoamExtMepStatsExtDmrSent,
       "calixSoamExtMepStatsExtResetStat": calixSoamExtMepStatsExtResetStat,
       "calixSoamExtMepUcastLoopbackResultsTable": calixSoamExtMepUcastLoopbackResultsTable,
       "calixSoamExtMepUcastLoopbackResultsEntry": calixSoamExtMepUcastLoopbackResultsEntry,
       "calixSoamExtMepUcastLoopbackResultsLbmFirstSeqNumber": calixSoamExtMepUcastLoopbackResultsLbmFirstSeqNumber,
       "calixSoamExtMepUcastLoopbackResultsDestMacAddress": calixSoamExtMepUcastLoopbackResultsDestMacAddress,
       "calixSoamExtMepUcastLoopbackResultsStatus": calixSoamExtMepUcastLoopbackResultsStatus,
       "calixSoamExtMepUcastLoopbackResultsLbmOut": calixSoamExtMepUcastLoopbackResultsLbmOut,
       "calixSoamExtMepUcastLoopbackResultsLbrIn": calixSoamExtMepUcastLoopbackResultsLbrIn,
       "calixSoamExtCfgTable": calixSoamExtCfgTable,
       "calixSoamExtCfgEntry": calixSoamExtCfgEntry,
       "calixSoamExtCfgIndex": calixSoamExtCfgIndex,
       "calixSoamExtCfgAdminState": calixSoamExtCfgAdminState,
       "calixSoamExtCfgPermission": calixSoamExtCfgPermission,
       "calixSoamExtCfgChassisIdSubtype": calixSoamExtCfgChassisIdSubtype,
       "calixSoamExtCfgChassisId": calixSoamExtCfgChassisId,
       "calixSoamExtCfgManAddressDomain": calixSoamExtCfgManAddressDomain,
       "calixSoamExtCfgManAddress": calixSoamExtCfgManAddress,
       "calixSoamExtCfgCcmOptTlvSenderId": calixSoamExtCfgCcmOptTlvSenderId,
       "calixSoamExtCfgCcmOptTlvPortStatus": calixSoamExtCfgCcmOptTlvPortStatus,
       "calixSoamExtCfgCcmOptTlvIfStatus": calixSoamExtCfgCcmOptTlvIfStatus,
       "calixSoamExtCfgLtmOptTlvSenderId": calixSoamExtCfgLtmOptTlvSenderId,
       "calixSoamExtCfgLbmOptTlvSenderId": calixSoamExtCfgLbmOptTlvSenderId,
       "calixSoamExtCfgLbmOptTlvIfStatus": calixSoamExtCfgLbmOptTlvIfStatus,
       "calixSoamExtCfgLbmOptTlvData": calixSoamExtCfgLbmOptTlvData,
       "calixSoamExtCfgDmmOptTlvData": calixSoamExtCfgDmmOptTlvData,
       "calixLoamExtCfgTable": calixLoamExtCfgTable,
       "calixLoamExtCfgEntry": calixLoamExtCfgEntry,
       "calixLoamExtCfgIndex": calixLoamExtCfgIndex,
       "calixLoamExtCfgAdminState": calixLoamExtCfgAdminState,
       "calixRfc2544CfgTable": calixRfc2544CfgTable,
       "calixRfc2544CfgEntry": calixRfc2544CfgEntry,
       "calixRfc2544CfgIndex": calixRfc2544CfgIndex,
       "calixRfc2544CfgAdminState": calixRfc2544CfgAdminState,
       "calixRfc2544CfgIfIndex": calixRfc2544CfgIfIndex,
       "calixRfc2544CfgVlanId": calixRfc2544CfgVlanId,
       "calixRfc2544CfgMacAddress": calixRfc2544CfgMacAddress}
)
