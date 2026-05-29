# SNMP MIB module (PRVT-L2TUNNELING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-L2TUNNELING-MIB

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

(serviceAccessSwitch,) = mibBuilder.importSymbols(
    "PRVT-QOS-MIB",
    "serviceAccessSwitch")

(sapBaseInfoEntry,
 sapEncapValue,
 sapPortId,
 sdpId,
 sdpInfoEntry,
 svcId) = mibBuilder.importSymbols(
    "PRVT-SERV-MIB",
    "sapBaseInfoEntry",
    "sapEncapValue",
    "sapPortId",
    "sdpId",
    "sdpInfoEntry",
    "svcId")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

prvtL2TunnelingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3)
)
if mibBuilder.loadTexts:
    prvtL2TunnelingMIB.setRevisions(
        ("2009-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtL2TunnNotifications_ObjectIdentity = ObjectIdentity
prvtL2TunnNotifications = _PrvtL2TunnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 0)
)
_PrvtL2TunnObjects_ObjectIdentity = ObjectIdentity
prvtL2TunnObjects = _PrvtL2TunnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1)
)


class _PrvtL2TunnEnable_Type(Integer32):
    """Custom type prvtL2TunnEnable based on Integer32"""
    defaultValue = 2

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


_PrvtL2TunnEnable_Type.__name__ = "Integer32"
_PrvtL2TunnEnable_Object = MibScalar
prvtL2TunnEnable = _PrvtL2TunnEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 1),
    _PrvtL2TunnEnable_Type()
)
prvtL2TunnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtL2TunnEnable.setStatus("current")
_PrvtL2TunnProfileTable_Object = MibTable
prvtL2TunnProfileTable = _PrvtL2TunnProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 2)
)
if mibBuilder.loadTexts:
    prvtL2TunnProfileTable.setStatus("current")
_PrvtL2TunnProfileEntry_Object = MibTableRow
prvtL2TunnProfileEntry = _PrvtL2TunnProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 2, 1)
)
prvtL2TunnProfileEntry.setIndexNames(
    (0, "PRVT-L2TUNNELING-MIB", "prvtL2TunnProfileName"),
)
if mibBuilder.loadTexts:
    prvtL2TunnProfileEntry.setStatus("current")


class _PrvtL2TunnProfileName_Type(OctetString):
    """Custom type prvtL2TunnProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(33, 33),
    )
    fixed_length = 33


_PrvtL2TunnProfileName_Type.__name__ = "OctetString"
_PrvtL2TunnProfileName_Object = MibTableColumn
prvtL2TunnProfileName = _PrvtL2TunnProfileName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 2, 1, 1),
    _PrvtL2TunnProfileName_Type()
)
prvtL2TunnProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtL2TunnProfileName.setStatus("current")
_PrvtL2TunnProfileRowStatus_Type = RowStatus
_PrvtL2TunnProfileRowStatus_Object = MibTableColumn
prvtL2TunnProfileRowStatus = _PrvtL2TunnProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 2, 1, 2),
    _PrvtL2TunnProfileRowStatus_Type()
)
prvtL2TunnProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtL2TunnProfileRowStatus.setStatus("current")
_PrvtL2ProtocolsTable_Object = MibTable
prvtL2ProtocolsTable = _PrvtL2ProtocolsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 3)
)
if mibBuilder.loadTexts:
    prvtL2ProtocolsTable.setStatus("current")
_PrvtL2ProtocolsEntry_Object = MibTableRow
prvtL2ProtocolsEntry = _PrvtL2ProtocolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 3, 1)
)
prvtL2ProtocolsEntry.setIndexNames(
    (0, "PRVT-L2TUNNELING-MIB", "prvtL2ProtocolName"),
)
if mibBuilder.loadTexts:
    prvtL2ProtocolsEntry.setStatus("current")


class _PrvtL2ProtocolName_Type(OctetString):
    """Custom type prvtL2ProtocolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_PrvtL2ProtocolName_Type.__name__ = "OctetString"
_PrvtL2ProtocolName_Object = MibTableColumn
prvtL2ProtocolName = _PrvtL2ProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 3, 1, 1),
    _PrvtL2ProtocolName_Type()
)
prvtL2ProtocolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtL2ProtocolName.setStatus("current")


class _PrvtL2ProtocolEthertype_Type(Integer32):
    """Custom type prvtL2ProtocolEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrvtL2ProtocolEthertype_Type.__name__ = "Integer32"
_PrvtL2ProtocolEthertype_Object = MibTableColumn
prvtL2ProtocolEthertype = _PrvtL2ProtocolEthertype_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 3, 1, 2),
    _PrvtL2ProtocolEthertype_Type()
)
prvtL2ProtocolEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtL2ProtocolEthertype.setStatus("current")
_PrvtL2ProtocolMAC_Type = OctetString
_PrvtL2ProtocolMAC_Object = MibTableColumn
prvtL2ProtocolMAC = _PrvtL2ProtocolMAC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 3, 1, 3),
    _PrvtL2ProtocolMAC_Type()
)
prvtL2ProtocolMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtL2ProtocolMAC.setStatus("current")
_PrvtL2ReplaceMAC_Type = OctetString
_PrvtL2ReplaceMAC_Object = MibTableColumn
prvtL2ReplaceMAC = _PrvtL2ReplaceMAC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 3, 1, 4),
    _PrvtL2ReplaceMAC_Type()
)
prvtL2ReplaceMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtL2ReplaceMAC.setStatus("current")
_PrvtL2ProtocolRowStatus_Type = RowStatus
_PrvtL2ProtocolRowStatus_Object = MibTableColumn
prvtL2ProtocolRowStatus = _PrvtL2ProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 3, 1, 5),
    _PrvtL2ProtocolRowStatus_Type()
)
prvtL2ProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtL2ProtocolRowStatus.setStatus("current")
_PrvtL2TunnProfMapProtoTable_Object = MibTable
prvtL2TunnProfMapProtoTable = _PrvtL2TunnProfMapProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 4)
)
if mibBuilder.loadTexts:
    prvtL2TunnProfMapProtoTable.setStatus("current")
_PrvtL2TunnProfMapProtoEntry_Object = MibTableRow
prvtL2TunnProfMapProtoEntry = _PrvtL2TunnProfMapProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 4, 1)
)
prvtL2TunnProfMapProtoEntry.setIndexNames(
    (0, "PRVT-L2TUNNELING-MIB", "prvtL2TunnProfileName"),
    (0, "PRVT-L2TUNNELING-MIB", "prvtL2ProtocolName"),
)
if mibBuilder.loadTexts:
    prvtL2TunnProfMapProtoEntry.setStatus("current")


class _PrvtL2TunnAction_Type(Integer32):
    """Custom type prvtL2TunnAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 1),
          ("discard", 2))
    )


_PrvtL2TunnAction_Type.__name__ = "Integer32"
_PrvtL2TunnAction_Object = MibTableColumn
prvtL2TunnAction = _PrvtL2TunnAction_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 4, 1, 1),
    _PrvtL2TunnAction_Type()
)
prvtL2TunnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtL2TunnAction.setStatus("current")
_PrvtL2TunnSAPPointsTable_Object = MibTable
prvtL2TunnSAPPointsTable = _PrvtL2TunnSAPPointsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 5)
)
if mibBuilder.loadTexts:
    prvtL2TunnSAPPointsTable.setStatus("current")
_PrvtL2TunnSAPPointsEntry_Object = MibTableRow
prvtL2TunnSAPPointsEntry = _PrvtL2TunnSAPPointsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    prvtL2TunnSAPPointsEntry.setStatus("current")


class _ProfileSAP_Type(OctetString):
    """Custom type profileSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(33, 33),
    )
    fixed_length = 33


_ProfileSAP_Type.__name__ = "OctetString"
_ProfileSAP_Object = MibTableColumn
profileSAP = _ProfileSAP_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 5, 1, 1),
    _ProfileSAP_Type()
)
profileSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileSAP.setStatus("current")
_PrvtL2TunnSDPPointsTable_Object = MibTable
prvtL2TunnSDPPointsTable = _PrvtL2TunnSDPPointsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 6)
)
if mibBuilder.loadTexts:
    prvtL2TunnSDPPointsTable.setStatus("current")
_PrvtL2TunnSDPPointsEntry_Object = MibTableRow
prvtL2TunnSDPPointsEntry = _PrvtL2TunnSDPPointsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    prvtL2TunnSDPPointsEntry.setStatus("current")


class _ProfileSDP_Type(OctetString):
    """Custom type profileSDP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(33, 33),
    )
    fixed_length = 33


_ProfileSDP_Type.__name__ = "OctetString"
_ProfileSDP_Object = MibTableColumn
profileSDP = _ProfileSDP_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 6, 1, 1),
    _ProfileSDP_Type()
)
profileSDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileSDP.setStatus("current")


class _PrvtL2TunnClearStatistics_Type(Integer32):
    """Custom type prvtL2TunnClearStatistics based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1))
    )


_PrvtL2TunnClearStatistics_Type.__name__ = "Integer32"
_PrvtL2TunnClearStatistics_Object = MibScalar
prvtL2TunnClearStatistics = _PrvtL2TunnClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 7),
    _PrvtL2TunnClearStatistics_Type()
)
prvtL2TunnClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtL2TunnClearStatistics.setStatus("current")
_PrvtL2TunnSapStatisticsTable_Object = MibTable
prvtL2TunnSapStatisticsTable = _PrvtL2TunnSapStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 8)
)
if mibBuilder.loadTexts:
    prvtL2TunnSapStatisticsTable.setStatus("current")
_PrvtL2TunnSapStatisticsEntry_Object = MibTableRow
prvtL2TunnSapStatisticsEntry = _PrvtL2TunnSapStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 8, 1)
)
prvtL2TunnSapStatisticsEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "svcId"),
    (0, "PRVT-SERV-MIB", "sapPortId"),
    (0, "PRVT-SERV-MIB", "sapEncapValue"),
    (0, "PRVT-L2TUNNELING-MIB", "prvtL2ProtocolName"),
)
if mibBuilder.loadTexts:
    prvtL2TunnSapStatisticsEntry.setStatus("current")
_L2TunnSapRxPackets_Type = Counter32
_L2TunnSapRxPackets_Object = MibTableColumn
l2TunnSapRxPackets = _L2TunnSapRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 8, 1, 1),
    _L2TunnSapRxPackets_Type()
)
l2TunnSapRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TunnSapRxPackets.setStatus("current")
_L2TunnSapTxPackets_Type = Counter32
_L2TunnSapTxPackets_Object = MibTableColumn
l2TunnSapTxPackets = _L2TunnSapTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 8, 1, 2),
    _L2TunnSapTxPackets_Type()
)
l2TunnSapTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TunnSapTxPackets.setStatus("current")
_PrvtL2TunnSdpStatisticsTable_Object = MibTable
prvtL2TunnSdpStatisticsTable = _PrvtL2TunnSdpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 9)
)
if mibBuilder.loadTexts:
    prvtL2TunnSdpStatisticsTable.setStatus("current")
_PrvtL2TunnSdpStatisticsEntry_Object = MibTableRow
prvtL2TunnSdpStatisticsEntry = _PrvtL2TunnSdpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 9, 1)
)
prvtL2TunnSdpStatisticsEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "svcId"),
    (0, "PRVT-SERV-MIB", "sdpId"),
    (0, "PRVT-L2TUNNELING-MIB", "prvtL2ProtocolName"),
)
if mibBuilder.loadTexts:
    prvtL2TunnSdpStatisticsEntry.setStatus("current")
_L2TunnSdpRxPackets_Type = Counter32
_L2TunnSdpRxPackets_Object = MibTableColumn
l2TunnSdpRxPackets = _L2TunnSdpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 9, 1, 1),
    _L2TunnSdpRxPackets_Type()
)
l2TunnSdpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TunnSdpRxPackets.setStatus("current")
_L2TunnSdpTxPackets_Type = Counter32
_L2TunnSdpTxPackets_Object = MibTableColumn
l2TunnSdpTxPackets = _L2TunnSdpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 1, 9, 1, 2),
    _L2TunnSdpTxPackets_Type()
)
l2TunnSdpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2TunnSdpTxPackets.setStatus("current")
_PrvtL2TunnConformance_ObjectIdentity = ObjectIdentity
prvtL2TunnConformance = _PrvtL2TunnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 2)
)
_PrvtL2TunnCompliances_ObjectIdentity = ObjectIdentity
prvtL2TunnCompliances = _PrvtL2TunnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 2, 1)
)
_PrvtL2TunnGroups_ObjectIdentity = ObjectIdentity
prvtL2TunnGroups = _PrvtL2TunnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 2, 2)
)
sapBaseInfoEntry.registerAugmentions(
    ("PRVT-L2TUNNELING-MIB",
     "prvtL2TunnSAPPointsEntry")
)
prvtL2TunnSAPPointsEntry.setIndexNames(*sapBaseInfoEntry.getIndexNames())
sdpInfoEntry.registerAugmentions(
    ("PRVT-L2TUNNELING-MIB",
     "prvtL2TunnSDPPointsEntry")
)
prvtL2TunnSDPPointsEntry.setIndexNames(*sdpInfoEntry.getIndexNames())

# Managed Objects groups

prvtL2TunnProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 2, 2, 1)
)
prvtL2TunnProtocolGroup.setObjects(
      *(("PRVT-L2TUNNELING-MIB", "prvtL2ProtocolName"),
        ("PRVT-L2TUNNELING-MIB", "prvtL2ReplaceMAC"),
        ("PRVT-L2TUNNELING-MIB", "prvtL2ProtocolEthertype"),
        ("PRVT-L2TUNNELING-MIB", "prvtL2ProtocolMAC"),
        ("PRVT-L2TUNNELING-MIB", "prvtL2ReplaceMAC"),
        ("PRVT-L2TUNNELING-MIB", "prvtL2ProtocolRowStatus"))
)
if mibBuilder.loadTexts:
    prvtL2TunnProtocolGroup.setStatus("current")

prvtL2TunnProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 2, 2, 2)
)
prvtL2TunnProfileGroup.setObjects(
      *(("PRVT-L2TUNNELING-MIB", "prvtL2TunnEnable"),
        ("PRVT-L2TUNNELING-MIB", "prvtL2TunnProfileName"),
        ("PRVT-L2TUNNELING-MIB", "prvtL2TunnProfileRowStatus"))
)
if mibBuilder.loadTexts:
    prvtL2TunnProfileGroup.setStatus("current")

prvtL2TunnPointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 2, 2, 3)
)
prvtL2TunnPointGroup.setObjects(
      *(("PRVT-L2TUNNELING-MIB", "prvtL2TunnAction"),
        ("PRVT-L2TUNNELING-MIB", "profileSDP"),
        ("PRVT-L2TUNNELING-MIB", "profileSAP"),
        ("PRVT-L2TUNNELING-MIB", "l2TunnSapRxPackets"),
        ("PRVT-L2TUNNELING-MIB", "l2TunnSapTxPackets"),
        ("PRVT-L2TUNNELING-MIB", "l2TunnSdpRxPackets"),
        ("PRVT-L2TUNNELING-MIB", "l2TunnSdpTxPackets"))
)
if mibBuilder.loadTexts:
    prvtL2TunnPointGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

prvtL2TunnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 7, 3, 2, 1, 1)
)
prvtL2TunnCompliance.setObjects(
      *(("PRVT-L2TUNNELING-MIB", "prvtL2TunnProtocolGroup"),
        ("PRVT-L2TUNNELING-MIB", "prvtL2TunnProfileGroup"),
        ("PRVT-L2TUNNELING-MIB", "prvtL2TunnPointGroup"))
)
if mibBuilder.loadTexts:
    prvtL2TunnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-L2TUNNELING-MIB",
    **{"prvtL2TunnelingMIB": prvtL2TunnelingMIB,
       "prvtL2TunnNotifications": prvtL2TunnNotifications,
       "prvtL2TunnObjects": prvtL2TunnObjects,
       "prvtL2TunnEnable": prvtL2TunnEnable,
       "prvtL2TunnProfileTable": prvtL2TunnProfileTable,
       "prvtL2TunnProfileEntry": prvtL2TunnProfileEntry,
       "prvtL2TunnProfileName": prvtL2TunnProfileName,
       "prvtL2TunnProfileRowStatus": prvtL2TunnProfileRowStatus,
       "prvtL2ProtocolsTable": prvtL2ProtocolsTable,
       "prvtL2ProtocolsEntry": prvtL2ProtocolsEntry,
       "prvtL2ProtocolName": prvtL2ProtocolName,
       "prvtL2ProtocolEthertype": prvtL2ProtocolEthertype,
       "prvtL2ProtocolMAC": prvtL2ProtocolMAC,
       "prvtL2ReplaceMAC": prvtL2ReplaceMAC,
       "prvtL2ProtocolRowStatus": prvtL2ProtocolRowStatus,
       "prvtL2TunnProfMapProtoTable": prvtL2TunnProfMapProtoTable,
       "prvtL2TunnProfMapProtoEntry": prvtL2TunnProfMapProtoEntry,
       "prvtL2TunnAction": prvtL2TunnAction,
       "prvtL2TunnSAPPointsTable": prvtL2TunnSAPPointsTable,
       "prvtL2TunnSAPPointsEntry": prvtL2TunnSAPPointsEntry,
       "profileSAP": profileSAP,
       "prvtL2TunnSDPPointsTable": prvtL2TunnSDPPointsTable,
       "prvtL2TunnSDPPointsEntry": prvtL2TunnSDPPointsEntry,
       "profileSDP": profileSDP,
       "prvtL2TunnClearStatistics": prvtL2TunnClearStatistics,
       "prvtL2TunnSapStatisticsTable": prvtL2TunnSapStatisticsTable,
       "prvtL2TunnSapStatisticsEntry": prvtL2TunnSapStatisticsEntry,
       "l2TunnSapRxPackets": l2TunnSapRxPackets,
       "l2TunnSapTxPackets": l2TunnSapTxPackets,
       "prvtL2TunnSdpStatisticsTable": prvtL2TunnSdpStatisticsTable,
       "prvtL2TunnSdpStatisticsEntry": prvtL2TunnSdpStatisticsEntry,
       "l2TunnSdpRxPackets": l2TunnSdpRxPackets,
       "l2TunnSdpTxPackets": l2TunnSdpTxPackets,
       "prvtL2TunnConformance": prvtL2TunnConformance,
       "prvtL2TunnCompliances": prvtL2TunnCompliances,
       "prvtL2TunnCompliance": prvtL2TunnCompliance,
       "prvtL2TunnGroups": prvtL2TunnGroups,
       "prvtL2TunnProtocolGroup": prvtL2TunnProtocolGroup,
       "prvtL2TunnProfileGroup": prvtL2TunnProfileGroup,
       "prvtL2TunnPointGroup": prvtL2TunnPointGroup}
)
