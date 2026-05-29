# SNMP MIB module (AXS-AX4630S-TRAP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX4630S-MIB

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

(ax4630s,
 ax4630sChassisIndex,
 ax4630sNifBoardSlotIndex,
 ax4630sSystemMsgAdditionalCode,
 ax4630sSystemMsgEventCode,
 ax4630sSystemMsgEventInterfaceID,
 ax4630sSystemMsgEventPoint,
 ax4630sSystemMsgLevel,
 ax4630sSystemMsgText,
 ax4630sSystemMsgTimeStamp,
 ax4630sSystemMsgType,
 ax4630sTemperatureState,
 ax4630sTemperatureStatusDescr,
 ax4630sTemperatureStatusIndex,
 ax4630sTemperatureStatusValue,
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
 axsUlrPairedPortIfIndex,
 axsUlrPortIfIndex) = mibBuilder.importSymbols(
    "AX4630S",
    "ax4630s",
    "ax4630sChassisIndex",
    "ax4630sNifBoardSlotIndex",
    "ax4630sSystemMsgAdditionalCode",
    "ax4630sSystemMsgEventCode",
    "ax4630sSystemMsgEventInterfaceID",
    "ax4630sSystemMsgEventPoint",
    "ax4630sSystemMsgLevel",
    "ax4630sSystemMsgText",
    "ax4630sSystemMsgTimeStamp",
    "ax4630sSystemMsgType",
    "ax4630sTemperatureState",
    "ax4630sTemperatureStatusDescr",
    "ax4630sTemperatureStatusIndex",
    "ax4630sTemperatureStatusValue",
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

ax4630sSystemMsgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 1)
)
ax4630sSystemMsgTrap.setObjects(
      *(("AX4630S", "ax4630sSystemMsgType"),
        ("AX4630S", "ax4630sSystemMsgTimeStamp"),
        ("AX4630S", "ax4630sSystemMsgLevel"),
        ("AX4630S", "ax4630sSystemMsgEventPoint"),
        ("AX4630S", "ax4630sSystemMsgEventInterfaceID"),
        ("AX4630S", "ax4630sSystemMsgEventCode"),
        ("AX4630S", "ax4630sSystemMsgAdditionalCode"),
        ("AX4630S", "ax4630sSystemMsgText"))
)
if mibBuilder.loadTexts:
    ax4630sSystemMsgTrap.setStatus(
        ""
    )

ax4630sTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 4)
)
ax4630sTemperatureTrap.setObjects(
      *(("AX4630S", "ax4630sChassisIndex"),
        ("AX4630S", "ax4630sTemperatureStatusIndex"),
        ("AX4630S", "ax4630sTemperatureStatusDescr"),
        ("AX4630S", "ax4630sTemperatureStatusValue"),
        ("AX4630S", "ax4630sTemperatureState"))
)
if mibBuilder.loadTexts:
    ax4630sTemperatureTrap.setStatus(
        ""
    )

ax4630sGsrpStateTransitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 6)
)
ax4630sGsrpStateTransitionTrap.setObjects(
      *(("AX4630S", "axsGsrpGroupId"),
        ("AX4630S", "axsGsrpVlanGroupId"),
        ("AX4630S", "axsGsrpState"))
)
if mibBuilder.loadTexts:
    ax4630sGsrpStateTransitionTrap.setStatus(
        ""
    )

ax4630sAirFanStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 8)
)
if mibBuilder.loadTexts:
    ax4630sAirFanStopTrap.setStatus(
        ""
    )

ax4630sPowerSupplyFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 9)
)
if mibBuilder.loadTexts:
    ax4630sPowerSupplyFailureTrap.setStatus(
        ""
    )

ax4630sLoginSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 10)
)
ax4630sLoginSuccessTrap.setObjects(
      *(("AX4630S", "axsLoginName"),
        ("AX4630S", "axsLoginTime"),
        ("AX4630S", "axsLoginLocation"),
        ("AX4630S", "axsLoginLine"))
)
if mibBuilder.loadTexts:
    ax4630sLoginSuccessTrap.setStatus(
        ""
    )

ax4630sLoginFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 11)
)
ax4630sLoginFailureTrap.setObjects(
      *(("AX4630S", "axsLoginName"),
        ("AX4630S", "axsLoginFailureTime"),
        ("AX4630S", "axsLoginLocation"),
        ("AX4630S", "axsLoginLine"))
)
if mibBuilder.loadTexts:
    ax4630sLoginFailureTrap.setStatus(
        ""
    )

ax4630sLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 12)
)
ax4630sLogoutTrap.setObjects(
      *(("AX4630S", "axsLoginName"),
        ("AX4630S", "axsLoginTime"),
        ("AX4630S", "axsLogoutTime"),
        ("AX4630S", "axsLoginLocation"),
        ("AX4630S", "axsLoginLine"),
        ("AX4630S", "axsLogoutStatus"))
)
if mibBuilder.loadTexts:
    ax4630sLogoutTrap.setStatus(
        ""
    )

ax4630sMemoryUsageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 13)
)
if mibBuilder.loadTexts:
    ax4630sMemoryUsageTrap.setStatus(
        ""
    )

ax4630sFrameErrorReceiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 18)
)
ax4630sFrameErrorReceiveTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax4630sFrameErrorReceiveTrap.setStatus(
        ""
    )

ax4630sFrameErrorSendTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 19)
)
ax4630sFrameErrorSendTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax4630sFrameErrorSendTrap.setStatus(
        ""
    )

ax4630sBroadcastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 20)
)
ax4630sBroadcastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax4630sBroadcastStormDetectTrap.setStatus(
        ""
    )

ax4630sMulticastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 21)
)
ax4630sMulticastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax4630sMulticastStormDetectTrap.setStatus(
        ""
    )

ax4630sUnicastStormDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 22)
)
ax4630sUnicastStormDetectTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax4630sUnicastStormDetectTrap.setStatus(
        ""
    )

ax4630sBroadcastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 23)
)
ax4630sBroadcastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax4630sBroadcastStormPortInactivateTrap.setStatus(
        ""
    )

ax4630sMulticastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 24)
)
ax4630sMulticastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax4630sMulticastStormPortInactivateTrap.setStatus(
        ""
    )

ax4630sUnicastStormPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 25)
)
ax4630sUnicastStormPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax4630sUnicastStormPortInactivateTrap.setStatus(
        ""
    )

ax4630sBroadcastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 26)
)
ax4630sBroadcastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax4630sBroadcastStormRecoverTrap.setStatus(
        ""
    )

ax4630sMulticastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 27)
)
ax4630sMulticastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax4630sMulticastStormRecoverTrap.setStatus(
        ""
    )

ax4630sUnicastStormRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 28)
)
ax4630sUnicastStormRecoverTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax4630sUnicastStormRecoverTrap.setStatus(
        ""
    )

ax4630sEfmoamUdldPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 29)
)
ax4630sEfmoamUdldPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax4630sEfmoamUdldPortInactivateTrap.setStatus(
        ""
    )

ax4630sEfmoamLoopDetectPortInactivateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 30)
)
ax4630sEfmoamLoopDetectPortInactivateTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ax4630sEfmoamLoopDetectPortInactivateTrap.setStatus(
        ""
    )

ax4630sAxrpStateTransitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 36)
)
ax4630sAxrpStateTransitionTrap.setObjects(
      *(("AX4630S", "axsAxrpGroupRingId"),
        ("AX4630S", "axsAxrpGroupMode"),
        ("AX4630S", "axsAxrpGroupRingAttribute"),
        ("AX4630S", "axsAxrpGroupMonitoringState"))
)
if mibBuilder.loadTexts:
    ax4630sAxrpStateTransitionTrap.setStatus(
        ""
    )

ax4630sAxrpRingport1MonitoringStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 37)
)
ax4630sAxrpRingport1MonitoringStartTrap.setObjects(
      *(("AX4630S", "axsAxrpGroupRingId"),
        ("AX4630S", "axsAxrpGroupMode"),
        ("AX4630S", "axsAxrpGroupRingAttribute"),
        ("AX4630S", "axsAxrpGroupRingport1"))
)
if mibBuilder.loadTexts:
    ax4630sAxrpRingport1MonitoringStartTrap.setStatus(
        ""
    )

ax4630sAxrpRingport1DownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 38)
)
ax4630sAxrpRingport1DownTrap.setObjects(
      *(("AX4630S", "axsAxrpGroupRingId"),
        ("AX4630S", "axsAxrpGroupMode"),
        ("AX4630S", "axsAxrpGroupRingAttribute"),
        ("AX4630S", "axsAxrpGroupRingport1"))
)
if mibBuilder.loadTexts:
    ax4630sAxrpRingport1DownTrap.setStatus(
        ""
    )

ax4630sAxrpRingport2MonitoringStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 39)
)
ax4630sAxrpRingport2MonitoringStartTrap.setObjects(
      *(("AX4630S", "axsAxrpGroupRingId"),
        ("AX4630S", "axsAxrpGroupMode"),
        ("AX4630S", "axsAxrpGroupRingAttribute"),
        ("AX4630S", "axsAxrpGroupRingport2"))
)
if mibBuilder.loadTexts:
    ax4630sAxrpRingport2MonitoringStartTrap.setStatus(
        ""
    )

ax4630sAxrpRingport2DownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 40)
)
ax4630sAxrpRingport2DownTrap.setObjects(
      *(("AX4630S", "axsAxrpGroupRingId"),
        ("AX4630S", "axsAxrpGroupMode"),
        ("AX4630S", "axsAxrpGroupRingAttribute"),
        ("AX4630S", "axsAxrpGroupRingport2"))
)
if mibBuilder.loadTexts:
    ax4630sAxrpRingport2DownTrap.setStatus(
        ""
    )

ax4630sAxrpMultiFaultDetectionStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 41)
)
ax4630sAxrpMultiFaultDetectionStartTrap.setObjects(
      *(("AX4630S", "axsAxrpGroupRingId"),
        ("AX4630S", "axsAxrpGroupMode"),
        ("AX4630S", "axsAxrpGroupRingAttribute"))
)
if mibBuilder.loadTexts:
    ax4630sAxrpMultiFaultDetectionStartTrap.setStatus(
        ""
    )

ax4630sAxrpMultiFaultDetectionStateTransitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 42)
)
ax4630sAxrpMultiFaultDetectionStateTransitionTrap.setObjects(
      *(("AX4630S", "axsAxrpGroupRingId"),
        ("AX4630S", "axsAxrpGroupMode"),
        ("AX4630S", "axsAxrpGroupRingAttribute"),
        ("AX4630S", "axsAxrpGroupMultiFaultDetectionState"))
)
if mibBuilder.loadTexts:
    ax4630sAxrpMultiFaultDetectionStateTransitionTrap.setStatus(
        ""
    )

ax4630sL2ldLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 51)
)
ax4630sL2ldLinkDown.setObjects(
      *(("AX4630S", "axsL2ldPortIfIndex"),
        ("AX4630S", "axsL2ldPortSourcePortIfindex"),
        ("AX4630S", "axsL2ldPortDestinationPortIfindex"),
        ("AX4630S", "axsL2ldPortSourceVlan"))
)
if mibBuilder.loadTexts:
    ax4630sL2ldLinkDown.setStatus(
        ""
    )

ax4630sL2ldLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 52)
)
ax4630sL2ldLinkUp.setObjects(
    ("AX4630S", "axsL2ldPortIfIndex")
)
if mibBuilder.loadTexts:
    ax4630sL2ldLinkUp.setStatus(
        ""
    )

ax4630sL2ldLoopDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 53)
)
ax4630sL2ldLoopDetection.setObjects(
      *(("AX4630S", "axsL2ldPortIndex"),
        ("AX4630S", "axsL2ldPortIfIndex"),
        ("AX4630S", "axsL2ldPortSourcePortIfindex"),
        ("AX4630S", "axsL2ldPortSourceVlan"))
)
if mibBuilder.loadTexts:
    ax4630sL2ldLoopDetection.setStatus(
        ""
    )

ax4630sUlrChangeSecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 87)
)
ax4630sUlrChangeSecondary.setObjects(
      *(("AX4630S", "axsUlrPortIfIndex"),
        ("AX4630S", "axsUlrPairedPortIfIndex"))
)
if mibBuilder.loadTexts:
    ax4630sUlrChangeSecondary.setStatus(
        ""
    )

ax4630sUlrChangePrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 88)
)
ax4630sUlrChangePrimary.setObjects(
      *(("AX4630S", "axsUlrPortIfIndex"),
        ("AX4630S", "axsUlrPairedPortIfIndex"))
)
if mibBuilder.loadTexts:
    ax4630sUlrChangePrimary.setStatus(
        ""
    )

ax4630sUlrActivePortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 1, 2, 20, 0, 89)
)
ax4630sUlrActivePortDown.setObjects(
      *(("AX4630S", "axsUlrPortIfIndex"),
        ("AX4630S", "axsUlrPairedPortIfIndex"))
)
if mibBuilder.loadTexts:
    ax4630sUlrActivePortDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AXS-AX4630S-TRAP",
    **{"ax4630sSystemMsgTrap": ax4630sSystemMsgTrap,
       "ax4630sTemperatureTrap": ax4630sTemperatureTrap,
       "ax4630sGsrpStateTransitionTrap": ax4630sGsrpStateTransitionTrap,
       "ax4630sAirFanStopTrap": ax4630sAirFanStopTrap,
       "ax4630sPowerSupplyFailureTrap": ax4630sPowerSupplyFailureTrap,
       "ax4630sLoginSuccessTrap": ax4630sLoginSuccessTrap,
       "ax4630sLoginFailureTrap": ax4630sLoginFailureTrap,
       "ax4630sLogoutTrap": ax4630sLogoutTrap,
       "ax4630sMemoryUsageTrap": ax4630sMemoryUsageTrap,
       "ax4630sFrameErrorReceiveTrap": ax4630sFrameErrorReceiveTrap,
       "ax4630sFrameErrorSendTrap": ax4630sFrameErrorSendTrap,
       "ax4630sBroadcastStormDetectTrap": ax4630sBroadcastStormDetectTrap,
       "ax4630sMulticastStormDetectTrap": ax4630sMulticastStormDetectTrap,
       "ax4630sUnicastStormDetectTrap": ax4630sUnicastStormDetectTrap,
       "ax4630sBroadcastStormPortInactivateTrap": ax4630sBroadcastStormPortInactivateTrap,
       "ax4630sMulticastStormPortInactivateTrap": ax4630sMulticastStormPortInactivateTrap,
       "ax4630sUnicastStormPortInactivateTrap": ax4630sUnicastStormPortInactivateTrap,
       "ax4630sBroadcastStormRecoverTrap": ax4630sBroadcastStormRecoverTrap,
       "ax4630sMulticastStormRecoverTrap": ax4630sMulticastStormRecoverTrap,
       "ax4630sUnicastStormRecoverTrap": ax4630sUnicastStormRecoverTrap,
       "ax4630sEfmoamUdldPortInactivateTrap": ax4630sEfmoamUdldPortInactivateTrap,
       "ax4630sEfmoamLoopDetectPortInactivateTrap": ax4630sEfmoamLoopDetectPortInactivateTrap,
       "ax4630sAxrpStateTransitionTrap": ax4630sAxrpStateTransitionTrap,
       "ax4630sAxrpRingport1MonitoringStartTrap": ax4630sAxrpRingport1MonitoringStartTrap,
       "ax4630sAxrpRingport1DownTrap": ax4630sAxrpRingport1DownTrap,
       "ax4630sAxrpRingport2MonitoringStartTrap": ax4630sAxrpRingport2MonitoringStartTrap,
       "ax4630sAxrpRingport2DownTrap": ax4630sAxrpRingport2DownTrap,
       "ax4630sAxrpMultiFaultDetectionStartTrap": ax4630sAxrpMultiFaultDetectionStartTrap,
       "ax4630sAxrpMultiFaultDetectionStateTransitionTrap": ax4630sAxrpMultiFaultDetectionStateTransitionTrap,
       "ax4630sL2ldLinkDown": ax4630sL2ldLinkDown,
       "ax4630sL2ldLinkUp": ax4630sL2ldLinkUp,
       "ax4630sL2ldLoopDetection": ax4630sL2ldLoopDetection,
       "ax4630sUlrChangeSecondary": ax4630sUlrChangeSecondary,
       "ax4630sUlrChangePrimary": ax4630sUlrChangePrimary,
       "ax4630sUlrActivePortDown": ax4630sUlrActivePortDown}
)
