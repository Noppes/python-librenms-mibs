# SNMP MIB module (AXS-AX3660S-TRAP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX3660S-MIB

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

(ax3660s,
 ax3660sChassisIndex,
 ax3660sSystemMsgAdditionalCode,
 ax3660sSystemMsgEventCode,
 ax3660sSystemMsgEventInterfaceID,
 ax3660sSystemMsgEventPoint,
 ax3660sSystemMsgLevel,
 ax3660sSystemMsgText,
 ax3660sSystemMsgTimeStamp,
 ax3660sSystemMsgType,
 ax3660sTemperatureState,
 ax3660sTemperatureStatusDescr,
 ax3660sTemperatureStatusIndex,
 ax3660sTemperatureStatusValue,
 axsAxrpGroupMode,
 axsAxrpGroupMonitoringState,
 axsAxrpGroupMultiFaultDetectionState,
 axsAxrpGroupRingAttribute,
 axsAxrpGroupRingId,
 axsAxrpGroupRingport1,
 axsAxrpGroupRingport2,
 axsGsrpGroupId,
 axsGsrpState,
 axsGsrpVlanGroupId,
 axsL2ldPortDestinationPortIfindex,
 axsL2ldPortIfIndex,
 axsL2ldPortIndex,
 axsL2ldPortSourcePortIfindex,
 axsL2ldPortSourceVlan,
 axsLoginFailureTime,
 axsLoginLine,
 axsLoginLocation,
 axsLoginName,
 axsLoginTime,
 axsLogoutStatus,
 axsLogoutTime,
 axsQosFlowStatsInListName,
 axsQosFlowStatsInSequenceNumber,
 axsUlrPairedPortIfIndex,
 axsUlrPortIfIndex) = mibBuilder.importSymbols(
    "AX3660S",
    "ax3660s",
    "ax3660sChassisIndex",
    "ax3660sSystemMsgAdditionalCode",
    "ax3660sSystemMsgEventCode",
    "ax3660sSystemMsgEventInterfaceID",
    "ax3660sSystemMsgEventPoint",
    "ax3660sSystemMsgLevel",
    "ax3660sSystemMsgText",
    "ax3660sSystemMsgTimeStamp",
    "ax3660sSystemMsgType",
    "ax3660sTemperatureState",
    "ax3660sTemperatureStatusDescr",
    "ax3660sTemperatureStatusIndex",
    "ax3660sTemperatureStatusValue",
    "axsAxrpGroupMode",
    "axsAxrpGroupMonitoringState",
    "axsAxrpGroupMultiFaultDetectionState",
    "axsAxrpGroupRingAttribute",
    "axsAxrpGroupRingId",
    "axsAxrpGroupRingport1",
    "axsAxrpGroupRingport2",
    "axsGsrpGroupId",
    "axsGsrpState",
    "axsGsrpVlanGroupId",
    "axsL2ldPortDestinationPortIfindex",
    "axsL2ldPortIfIndex",
    "axsL2ldPortIndex",
    "axsL2ldPortSourcePortIfindex",
    "axsL2ldPortSourceVlan",
    "axsLoginFailureTime",
    "axsLoginLine",
    "axsLoginLocation",
    "axsLoginName",
    "axsLoginTime",
    "axsLogoutStatus",
    "axsLogoutTime",
    "axsQosFlowStatsInListName",
    "axsQosFlowStatsInSequenceNumber",
    "axsUlrPairedPortIfIndex",
    "axsUlrPortIfIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# Managed Objects groups


# Notification objects

ax3660sSystemMsgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 1)
)
ax3660sSystemMsgTrap.setObjects(
      *(("AX3660S", "ax3660sSystemMsgType"),
        ("AX3660S", "ax3660sSystemMsgTimeStamp"),
        ("AX3660S", "ax3660sSystemMsgLevel"),
        ("AX3660S", "ax3660sSystemMsgEventPoint"),
        ("AX3660S", "ax3660sSystemMsgEventInterfaceID"),
        ("AX3660S", "ax3660sSystemMsgEventCode"),
        ("AX3660S", "ax3660sSystemMsgAdditionalCode"),
        ("AX3660S", "ax3660sSystemMsgText"))
)
if mibBuilder.loadTexts:
    ax3660sSystemMsgTrap.setStatus(
        ""
    )

ax3660sTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 4)
)
ax3660sTemperatureTrap.setObjects(
      *(("AX3660S", "ax3660sChassisIndex"),
        ("AX3660S", "ax3660sTemperatureStatusIndex"),
        ("AX3660S", "ax3660sTemperatureStatusDescr"),
        ("AX3660S", "ax3660sTemperatureStatusValue"),
        ("AX3660S", "ax3660sTemperatureState"))
)
if mibBuilder.loadTexts:
    ax3660sTemperatureTrap.setStatus(
        ""
    )

ax3660sGsrpStateTransitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 6)
)
ax3660sGsrpStateTransitionTrap.setObjects(
      *(("AX3660S", "axsGsrpGroupId"),
        ("AX3660S", "axsGsrpVlanGroupId"),
        ("AX3660S", "axsGsrpState"))
)
if mibBuilder.loadTexts:
    ax3660sGsrpStateTransitionTrap.setStatus(
        ""
    )

ax3660sAirFanStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 8)
)
if mibBuilder.loadTexts:
    ax3660sAirFanStopTrap.setStatus(
        ""
    )

ax3660sPowerSupplyFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 9)
)
if mibBuilder.loadTexts:
    ax3660sPowerSupplyFailureTrap.setStatus(
        ""
    )

ax3660sLoginSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 10)
)
ax3660sLoginSuccessTrap.setObjects(
      *(("AX3660S", "axsLoginName"),
        ("AX3660S", "axsLoginTime"),
        ("AX3660S", "axsLoginLocation"),
        ("AX3660S", "axsLoginLine"))
)
if mibBuilder.loadTexts:
    ax3660sLoginSuccessTrap.setStatus(
        ""
    )

ax3660sLoginFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 11)
)
ax3660sLoginFailureTrap.setObjects(
      *(("AX3660S", "axsLoginName"),
        ("AX3660S", "axsLoginFailureTime"),
        ("AX3660S", "axsLoginLocation"),
        ("AX3660S", "axsLoginLine"))
)
if mibBuilder.loadTexts:
    ax3660sLoginFailureTrap.setStatus(
        ""
    )

ax3660sLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 12)
)
ax3660sLogoutTrap.setObjects(
      *(("AX3660S", "axsLoginName"),
        ("AX3660S", "axsLoginTime"),
        ("AX3660S", "axsLogoutTime"),
        ("AX3660S", "axsLoginLocation"),
        ("AX3660S", "axsLoginLine"),
        ("AX3660S", "axsLogoutStatus"))
)
if mibBuilder.loadTexts:
    ax3660sLogoutTrap.setStatus(
        ""
    )

ax3660sMemoryUsageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 13)
)
if mibBuilder.loadTexts:
    ax3660sMemoryUsageTrap.setStatus(
        ""
    )

ax3660sFrameErrorReceiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 18)
)
ax3660sFrameErrorReceiveTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax3660sFrameErrorReceiveTrap.setStatus(
        ""
    )

ax3660sFrameErrorSendTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 19)
)
ax3660sFrameErrorSendTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax3660sFrameErrorSendTrap.setStatus(
        ""
    )

ax3660sBroadcastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 20)
)
ax3660sBroadcastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax3660sBroadcastStormDetectTrap.setStatus(
        ""
    )

ax3660sMulticastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 21)
)
ax3660sMulticastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax3660sMulticastStormDetectTrap.setStatus(
        ""
    )

ax3660sUnicastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 22)
)
ax3660sUnicastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax3660sUnicastStormDetectTrap.setStatus(
        ""
    )

ax3660sBroadcastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 23)
)
ax3660sBroadcastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax3660sBroadcastStormPortInactivateTrap.setStatus(
        ""
    )

ax3660sMulticastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 24)
)
ax3660sMulticastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax3660sMulticastStormPortInactivateTrap.setStatus(
        ""
    )

ax3660sUnicastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 25)
)
ax3660sUnicastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax3660sUnicastStormPortInactivateTrap.setStatus(
        ""
    )

ax3660sBroadcastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 26)
)
ax3660sBroadcastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax3660sBroadcastStormRecoverTrap.setStatus(
        ""
    )

ax3660sMulticastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 27)
)
ax3660sMulticastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax3660sMulticastStormRecoverTrap.setStatus(
        ""
    )

ax3660sUnicastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 28)
)
ax3660sUnicastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax3660sUnicastStormRecoverTrap.setStatus(
        ""
    )

ax3660sEfmoamUdldPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 29)
)
ax3660sEfmoamUdldPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax3660sEfmoamUdldPortInactivateTrap.setStatus(
        ""
    )

ax3660sEfmoamLoopDetectPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 30)
)
ax3660sEfmoamLoopDetectPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax3660sEfmoamLoopDetectPortInactivateTrap.setStatus(
        ""
    )

ax3660sAxrpStateTransitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 36)
)
ax3660sAxrpStateTransitionTrap.setObjects(
      *(("AX3660S", "axsAxrpGroupRingId"),
        ("AX3660S", "axsAxrpGroupMode"),
        ("AX3660S", "axsAxrpGroupRingAttribute"),
        ("AX3660S", "axsAxrpGroupMonitoringState"))
)
if mibBuilder.loadTexts:
    ax3660sAxrpStateTransitionTrap.setStatus(
        ""
    )

ax3660sAxrpRingport1MonitoringStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 37)
)
ax3660sAxrpRingport1MonitoringStartTrap.setObjects(
      *(("AX3660S", "axsAxrpGroupRingId"),
        ("AX3660S", "axsAxrpGroupMode"),
        ("AX3660S", "axsAxrpGroupRingAttribute"),
        ("AX3660S", "axsAxrpGroupRingport1"))
)
if mibBuilder.loadTexts:
    ax3660sAxrpRingport1MonitoringStartTrap.setStatus(
        ""
    )

ax3660sAxrpRingport1DownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 38)
)
ax3660sAxrpRingport1DownTrap.setObjects(
      *(("AX3660S", "axsAxrpGroupRingId"),
        ("AX3660S", "axsAxrpGroupMode"),
        ("AX3660S", "axsAxrpGroupRingAttribute"),
        ("AX3660S", "axsAxrpGroupRingport1"))
)
if mibBuilder.loadTexts:
    ax3660sAxrpRingport1DownTrap.setStatus(
        ""
    )

ax3660sAxrpRingport2MonitoringStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 39)
)
ax3660sAxrpRingport2MonitoringStartTrap.setObjects(
      *(("AX3660S", "axsAxrpGroupRingId"),
        ("AX3660S", "axsAxrpGroupMode"),
        ("AX3660S", "axsAxrpGroupRingAttribute"),
        ("AX3660S", "axsAxrpGroupRingport2"))
)
if mibBuilder.loadTexts:
    ax3660sAxrpRingport2MonitoringStartTrap.setStatus(
        ""
    )

ax3660sAxrpRingport2DownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 40)
)
ax3660sAxrpRingport2DownTrap.setObjects(
      *(("AX3660S", "axsAxrpGroupRingId"),
        ("AX3660S", "axsAxrpGroupMode"),
        ("AX3660S", "axsAxrpGroupRingAttribute"),
        ("AX3660S", "axsAxrpGroupRingport2"))
)
if mibBuilder.loadTexts:
    ax3660sAxrpRingport2DownTrap.setStatus(
        ""
    )

ax3660sAxrpMultiFaultDetectionStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 41)
)
ax3660sAxrpMultiFaultDetectionStartTrap.setObjects(
      *(("AX3660S", "axsAxrpGroupRingId"),
        ("AX3660S", "axsAxrpGroupMode"),
        ("AX3660S", "axsAxrpGroupRingAttribute"))
)
if mibBuilder.loadTexts:
    ax3660sAxrpMultiFaultDetectionStartTrap.setStatus(
        ""
    )

ax3660sAxrpMultiFaultDetectionStateTransitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 42)
)
ax3660sAxrpMultiFaultDetectionStateTransitionTrap.setObjects(
      *(("AX3660S", "axsAxrpGroupRingId"),
        ("AX3660S", "axsAxrpGroupMode"),
        ("AX3660S", "axsAxrpGroupRingAttribute"),
        ("AX3660S", "axsAxrpGroupMultiFaultDetectionState"))
)
if mibBuilder.loadTexts:
    ax3660sAxrpMultiFaultDetectionStateTransitionTrap.setStatus(
        ""
    )

ax3660sL2ldLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 51)
)
ax3660sL2ldLinkDown.setObjects(
      *(("AX3660S", "axsL2ldPortIfIndex"),
        ("AX3660S", "axsL2ldPortSourcePortIfindex"),
        ("AX3660S", "axsL2ldPortDestinationPortIfindex"),
        ("AX3660S", "axsL2ldPortSourceVlan"))
)
if mibBuilder.loadTexts:
    ax3660sL2ldLinkDown.setStatus(
        ""
    )

ax3660sL2ldLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 52)
)
ax3660sL2ldLinkUp.setObjects(
    ("AX3660S", "axsL2ldPortIfIndex")
)
if mibBuilder.loadTexts:
    ax3660sL2ldLinkUp.setStatus(
        ""
    )

ax3660sL2ldLoopDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 53)
)
ax3660sL2ldLoopDetection.setObjects(
      *(("AX3660S", "axsL2ldPortIndex"),
        ("AX3660S", "axsL2ldPortIfIndex"),
        ("AX3660S", "axsL2ldPortSourcePortIfindex"),
        ("AX3660S", "axsL2ldPortSourceVlan"))
)
if mibBuilder.loadTexts:
    ax3660sL2ldLoopDetection.setStatus(
        ""
    )

ax3660sUlrChangeSecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 87)
)
ax3660sUlrChangeSecondary.setObjects(
      *(("AX3660S", "axsUlrPortIfIndex"),
        ("AX3660S", "axsUlrPairedPortIfIndex"))
)
if mibBuilder.loadTexts:
    ax3660sUlrChangeSecondary.setStatus(
        ""
    )

ax3660sUlrChangePrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 88)
)
ax3660sUlrChangePrimary.setObjects(
      *(("AX3660S", "axsUlrPortIfIndex"),
        ("AX3660S", "axsUlrPairedPortIfIndex"))
)
if mibBuilder.loadTexts:
    ax3660sUlrChangePrimary.setStatus(
        ""
    )

ax3660sUlrActivePortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 89)
)
ax3660sUlrActivePortDown.setObjects(
      *(("AX3660S", "axsUlrPortIfIndex"),
        ("AX3660S", "axsUlrPairedPortIfIndex"))
)
if mibBuilder.loadTexts:
    ax3660sUlrActivePortDown.setStatus(
        ""
    )

ax3660sQosFlowListRateAlarmExceedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 90)
)
ax3660sQosFlowListRateAlarmExceedTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("AX3660S", "axsQosFlowStatsInListName"),
        ("AX3660S", "axsQosFlowStatsInSequenceNumber"))
)
if mibBuilder.loadTexts:
    ax3660sQosFlowListRateAlarmExceedTrap.setStatus(
        ""
    )

ax3660sQosFlowListRateAlarmConformTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 24, 0, 91)
)
ax3660sQosFlowListRateAlarmConformTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("AX3660S", "axsQosFlowStatsInListName"),
        ("AX3660S", "axsQosFlowStatsInSequenceNumber"))
)
if mibBuilder.loadTexts:
    ax3660sQosFlowListRateAlarmConformTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AXS-AX3660S-TRAP",
    **{"ax3660sSystemMsgTrap": ax3660sSystemMsgTrap,
       "ax3660sTemperatureTrap": ax3660sTemperatureTrap,
       "ax3660sGsrpStateTransitionTrap": ax3660sGsrpStateTransitionTrap,
       "ax3660sAirFanStopTrap": ax3660sAirFanStopTrap,
       "ax3660sPowerSupplyFailureTrap": ax3660sPowerSupplyFailureTrap,
       "ax3660sLoginSuccessTrap": ax3660sLoginSuccessTrap,
       "ax3660sLoginFailureTrap": ax3660sLoginFailureTrap,
       "ax3660sLogoutTrap": ax3660sLogoutTrap,
       "ax3660sMemoryUsageTrap": ax3660sMemoryUsageTrap,
       "ax3660sFrameErrorReceiveTrap": ax3660sFrameErrorReceiveTrap,
       "ax3660sFrameErrorSendTrap": ax3660sFrameErrorSendTrap,
       "ax3660sBroadcastStormDetectTrap": ax3660sBroadcastStormDetectTrap,
       "ax3660sMulticastStormDetectTrap": ax3660sMulticastStormDetectTrap,
       "ax3660sUnicastStormDetectTrap": ax3660sUnicastStormDetectTrap,
       "ax3660sBroadcastStormPortInactivateTrap": ax3660sBroadcastStormPortInactivateTrap,
       "ax3660sMulticastStormPortInactivateTrap": ax3660sMulticastStormPortInactivateTrap,
       "ax3660sUnicastStormPortInactivateTrap": ax3660sUnicastStormPortInactivateTrap,
       "ax3660sBroadcastStormRecoverTrap": ax3660sBroadcastStormRecoverTrap,
       "ax3660sMulticastStormRecoverTrap": ax3660sMulticastStormRecoverTrap,
       "ax3660sUnicastStormRecoverTrap": ax3660sUnicastStormRecoverTrap,
       "ax3660sEfmoamUdldPortInactivateTrap": ax3660sEfmoamUdldPortInactivateTrap,
       "ax3660sEfmoamLoopDetectPortInactivateTrap": ax3660sEfmoamLoopDetectPortInactivateTrap,
       "ax3660sAxrpStateTransitionTrap": ax3660sAxrpStateTransitionTrap,
       "ax3660sAxrpRingport1MonitoringStartTrap": ax3660sAxrpRingport1MonitoringStartTrap,
       "ax3660sAxrpRingport1DownTrap": ax3660sAxrpRingport1DownTrap,
       "ax3660sAxrpRingport2MonitoringStartTrap": ax3660sAxrpRingport2MonitoringStartTrap,
       "ax3660sAxrpRingport2DownTrap": ax3660sAxrpRingport2DownTrap,
       "ax3660sAxrpMultiFaultDetectionStartTrap": ax3660sAxrpMultiFaultDetectionStartTrap,
       "ax3660sAxrpMultiFaultDetectionStateTransitionTrap": ax3660sAxrpMultiFaultDetectionStateTransitionTrap,
       "ax3660sL2ldLinkDown": ax3660sL2ldLinkDown,
       "ax3660sL2ldLinkUp": ax3660sL2ldLinkUp,
       "ax3660sL2ldLoopDetection": ax3660sL2ldLoopDetection,
       "ax3660sUlrChangeSecondary": ax3660sUlrChangeSecondary,
       "ax3660sUlrChangePrimary": ax3660sUlrChangePrimary,
       "ax3660sUlrActivePortDown": ax3660sUlrActivePortDown,
       "ax3660sQosFlowListRateAlarmExceedTrap": ax3660sQosFlowListRateAlarmExceedTrap,
       "ax3660sQosFlowListRateAlarmConformTrap": ax3660sQosFlowListRateAlarmConformTrap}
)
