# SNMP MIB module (MOXA-TURBORINGV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\moxa\MOXA-TURBORINGV2-MIB

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

(layer2Redundancy,) = mibBuilder.importSymbols(
    "MOXA-SWITCHING-MIB",
    "layer2Redundancy")

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

mxTrv2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4)
)
if mibBuilder.loadTexts:
    mxTrv2.setRevisions(
        ("2022-02-17 00:00",
         "2019-06-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TR2PortStatus(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("linkDown", 6))
    )



class CouplingPortStatus(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("linkDown", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Trv2Notification_ObjectIdentity = ObjectIdentity
trv2Notification = _Trv2Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 0)
)
_Trv2Configuration_ObjectIdentity = ObjectIdentity
trv2Configuration = _Trv2Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 1)
)
_Trv2ConfigEnable_Type = TruthValue
_Trv2ConfigEnable_Object = MibScalar
trv2ConfigEnable = _Trv2ConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 1, 1),
    _Trv2ConfigEnable_Type()
)
trv2ConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trv2ConfigEnable.setStatus("current")
_Trv2ConfigRingTable_Object = MibTable
trv2ConfigRingTable = _Trv2ConfigRingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    trv2ConfigRingTable.setStatus("current")
_Trv2ConfigRingEntry_Object = MibTableRow
trv2ConfigRingEntry = _Trv2ConfigRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 1, 2, 1)
)
trv2ConfigRingEntry.setIndexNames(
    (0, "MOXA-TURBORINGV2-MIB", "trv2ConfigRingTableEntryIndex"),
)
if mibBuilder.loadTexts:
    trv2ConfigRingEntry.setStatus("current")
_Trv2ConfigRingTableEntryIndex_Type = Integer32
_Trv2ConfigRingTableEntryIndex_Object = MibTableColumn
trv2ConfigRingTableEntryIndex = _Trv2ConfigRingTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 1, 2, 1, 1),
    _Trv2ConfigRingTableEntryIndex_Type()
)
trv2ConfigRingTableEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trv2ConfigRingTableEntryIndex.setStatus("current")
_Trv2ConfigRingTableEntryEnable_Type = TruthValue
_Trv2ConfigRingTableEntryEnable_Object = MibTableColumn
trv2ConfigRingTableEntryEnable = _Trv2ConfigRingTableEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 1, 2, 1, 2),
    _Trv2ConfigRingTableEntryEnable_Type()
)
trv2ConfigRingTableEntryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trv2ConfigRingTableEntryEnable.setStatus("current")
_Trv2ConfigRingTableEntryMasterSetup_Type = TruthValue
_Trv2ConfigRingTableEntryMasterSetup_Object = MibTableColumn
trv2ConfigRingTableEntryMasterSetup = _Trv2ConfigRingTableEntryMasterSetup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 1, 2, 1, 3),
    _Trv2ConfigRingTableEntryMasterSetup_Type()
)
trv2ConfigRingTableEntryMasterSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trv2ConfigRingTableEntryMasterSetup.setStatus("current")
_Trv2ConfigRingTableEntryInterface_Type = OctetString
_Trv2ConfigRingTableEntryInterface_Object = MibTableColumn
trv2ConfigRingTableEntryInterface = _Trv2ConfigRingTableEntryInterface_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 1, 2, 1, 4),
    _Trv2ConfigRingTableEntryInterface_Type()
)
trv2ConfigRingTableEntryInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trv2ConfigRingTableEntryInterface.setStatus("current")
_Trv2ConfigCoupling_ObjectIdentity = ObjectIdentity
trv2ConfigCoupling = _Trv2ConfigCoupling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 1, 3)
)
_Trv2ConfigCouplingEnable_Type = TruthValue
_Trv2ConfigCouplingEnable_Object = MibScalar
trv2ConfigCouplingEnable = _Trv2ConfigCouplingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 1, 3, 1),
    _Trv2ConfigCouplingEnable_Type()
)
trv2ConfigCouplingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trv2ConfigCouplingEnable.setStatus("current")


class _Trv2ConfigCouplingMode_Type(Integer32):
    """Custom type trv2ConfigCouplingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("couplingBackup", 1),
          ("couplingPrimary", 2))
    )


_Trv2ConfigCouplingMode_Type.__name__ = "Integer32"
_Trv2ConfigCouplingMode_Object = MibScalar
trv2ConfigCouplingMode = _Trv2ConfigCouplingMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 1, 3, 2),
    _Trv2ConfigCouplingMode_Type()
)
trv2ConfigCouplingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trv2ConfigCouplingMode.setStatus("current")
_Trv2ConfigCouplingPort_Type = Integer32
_Trv2ConfigCouplingPort_Object = MibScalar
trv2ConfigCouplingPort = _Trv2ConfigCouplingPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 1, 3, 3),
    _Trv2ConfigCouplingPort_Type()
)
trv2ConfigCouplingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trv2ConfigCouplingPort.setStatus("current")
_Trv2Status_ObjectIdentity = ObjectIdentity
trv2Status = _Trv2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 2)
)
_Trv2StatRingTable_Object = MibTable
trv2StatRingTable = _Trv2StatRingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    trv2StatRingTable.setStatus("current")
_Trv2StatRingEntry_Object = MibTableRow
trv2StatRingEntry = _Trv2StatRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 2, 1, 1)
)
trv2StatRingEntry.setIndexNames(
    (0, "MOXA-TURBORINGV2-MIB", "trv2StatRingTableEntryIndex"),
)
if mibBuilder.loadTexts:
    trv2StatRingEntry.setStatus("current")
_Trv2StatRingTableEntryIndex_Type = Integer32
_Trv2StatRingTableEntryIndex_Object = MibTableColumn
trv2StatRingTableEntryIndex = _Trv2StatRingTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 2, 1, 1, 1),
    _Trv2StatRingTableEntryIndex_Type()
)
trv2StatRingTableEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trv2StatRingTableEntryIndex.setStatus("current")
_Trv2StatRingTableEntryMasterStatus_Type = TruthValue
_Trv2StatRingTableEntryMasterStatus_Object = MibTableColumn
trv2StatRingTableEntryMasterStatus = _Trv2StatRingTableEntryMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 2, 1, 1, 2),
    _Trv2StatRingTableEntryMasterStatus_Type()
)
trv2StatRingTableEntryMasterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trv2StatRingTableEntryMasterStatus.setStatus("current")
_Trv2StatRingTableEntryDesignatedMaster_Type = MacAddress
_Trv2StatRingTableEntryDesignatedMaster_Object = MibTableColumn
trv2StatRingTableEntryDesignatedMaster = _Trv2StatRingTableEntryDesignatedMaster_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 2, 1, 1, 3),
    _Trv2StatRingTableEntryDesignatedMaster_Type()
)
trv2StatRingTableEntryDesignatedMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trv2StatRingTableEntryDesignatedMaster.setStatus("current")
_Trv2StatRingTableEntryFirstRingPort_Type = TR2PortStatus
_Trv2StatRingTableEntryFirstRingPort_Object = MibTableColumn
trv2StatRingTableEntryFirstRingPort = _Trv2StatRingTableEntryFirstRingPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 2, 1, 1, 4),
    _Trv2StatRingTableEntryFirstRingPort_Type()
)
trv2StatRingTableEntryFirstRingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trv2StatRingTableEntryFirstRingPort.setStatus("current")
_Trv2StatRingTableEntrySecondRingPort_Type = TR2PortStatus
_Trv2StatRingTableEntrySecondRingPort_Object = MibTableColumn
trv2StatRingTableEntrySecondRingPort = _Trv2StatRingTableEntrySecondRingPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 2, 1, 1, 5),
    _Trv2StatRingTableEntrySecondRingPort_Type()
)
trv2StatRingTableEntrySecondRingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trv2StatRingTableEntrySecondRingPort.setStatus("current")


class _Trv2StatRingTableEntryBrokenStatus_Type(Integer32):
    """Custom type trv2StatRingTableEntryBrokenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("normal", 1),
          ("broken", 2))
    )


_Trv2StatRingTableEntryBrokenStatus_Type.__name__ = "Integer32"
_Trv2StatRingTableEntryBrokenStatus_Object = MibTableColumn
trv2StatRingTableEntryBrokenStatus = _Trv2StatRingTableEntryBrokenStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 2, 1, 1, 6),
    _Trv2StatRingTableEntryBrokenStatus_Type()
)
trv2StatRingTableEntryBrokenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trv2StatRingTableEntryBrokenStatus.setStatus("current")
_Trv2StatCoupling_ObjectIdentity = ObjectIdentity
trv2StatCoupling = _Trv2StatCoupling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 2, 2)
)
_Trv2StatCouplingPortStatus_Type = CouplingPortStatus
_Trv2StatCouplingPortStatus_Object = MibScalar
trv2StatCouplingPortStatus = _Trv2StatCouplingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 2, 2, 1),
    _Trv2StatCouplingPortStatus_Type()
)
trv2StatCouplingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trv2StatCouplingPortStatus.setStatus("current")

# Managed Objects groups


# Notification objects

trv2NotifyMasterChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 0, 1)
)
trv2NotifyMasterChanged.setObjects(
    ("MOXA-TURBORINGV2-MIB", "trv2StatRingTableEntryIndex")
)
if mibBuilder.loadTexts:
    trv2NotifyMasterChanged.setStatus(
        "current"
    )

trv2NotifyMasterMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 0, 2)
)
trv2NotifyMasterMismatch.setObjects(
    ("MOXA-TURBORINGV2-MIB", "trv2StatRingTableEntryIndex")
)
if mibBuilder.loadTexts:
    trv2NotifyMasterMismatch.setStatus(
        "current"
    )

trv2NotifyCouplingChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 603, 3, 4, 0, 3)
)
if mibBuilder.loadTexts:
    trv2NotifyCouplingChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-TURBORINGV2-MIB",
    **{"TR2PortStatus": TR2PortStatus,
       "CouplingPortStatus": CouplingPortStatus,
       "mxTrv2": mxTrv2,
       "trv2Notification": trv2Notification,
       "trv2NotifyMasterChanged": trv2NotifyMasterChanged,
       "trv2NotifyMasterMismatch": trv2NotifyMasterMismatch,
       "trv2NotifyCouplingChanged": trv2NotifyCouplingChanged,
       "trv2Configuration": trv2Configuration,
       "trv2ConfigEnable": trv2ConfigEnable,
       "trv2ConfigRingTable": trv2ConfigRingTable,
       "trv2ConfigRingEntry": trv2ConfigRingEntry,
       "trv2ConfigRingTableEntryIndex": trv2ConfigRingTableEntryIndex,
       "trv2ConfigRingTableEntryEnable": trv2ConfigRingTableEntryEnable,
       "trv2ConfigRingTableEntryMasterSetup": trv2ConfigRingTableEntryMasterSetup,
       "trv2ConfigRingTableEntryInterface": trv2ConfigRingTableEntryInterface,
       "trv2ConfigCoupling": trv2ConfigCoupling,
       "trv2ConfigCouplingEnable": trv2ConfigCouplingEnable,
       "trv2ConfigCouplingMode": trv2ConfigCouplingMode,
       "trv2ConfigCouplingPort": trv2ConfigCouplingPort,
       "trv2Status": trv2Status,
       "trv2StatRingTable": trv2StatRingTable,
       "trv2StatRingEntry": trv2StatRingEntry,
       "trv2StatRingTableEntryIndex": trv2StatRingTableEntryIndex,
       "trv2StatRingTableEntryMasterStatus": trv2StatRingTableEntryMasterStatus,
       "trv2StatRingTableEntryDesignatedMaster": trv2StatRingTableEntryDesignatedMaster,
       "trv2StatRingTableEntryFirstRingPort": trv2StatRingTableEntryFirstRingPort,
       "trv2StatRingTableEntrySecondRingPort": trv2StatRingTableEntrySecondRingPort,
       "trv2StatRingTableEntryBrokenStatus": trv2StatRingTableEntryBrokenStatus,
       "trv2StatCoupling": trv2StatCoupling,
       "trv2StatCouplingPortStatus": trv2StatCouplingPortStatus}
)
