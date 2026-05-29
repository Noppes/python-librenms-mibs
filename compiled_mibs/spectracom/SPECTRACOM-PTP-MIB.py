# SNMP MIB module (SPECTRACOM-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\spectracom\SPECTRACOM-PTP-MIB

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(specModules,
 specProducts) = mibBuilder.importSymbols(
    "SPECTRACOM-GLOBAL-REG-MIB",
    "specModules",
    "specProducts")


# MODULE-IDENTITY

spectracomPtpMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 1, 6)
)
if mibBuilder.loadTexts:
    spectracomPtpMibModule.setRevisions(
        ("2022-01-07 00:00",
         "2013-06-17 14:53",
         "2011-03-21 00:00",
         "2011-01-25 00:00",
         "2011-01-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PtpSnmpObjs_ObjectIdentity = ObjectIdentity
ptpSnmpObjs = _PtpSnmpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4)
)
_PtpStatusObjs_ObjectIdentity = ObjectIdentity
ptpStatusObjs = _PtpStatusObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1)
)
_PtpStatusTable_Object = MibTable
ptpStatusTable = _PtpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ptpStatusTable.setStatus("current")
_PtpStatusTableEntry_Object = MibTableRow
ptpStatusTableEntry = _PtpStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1)
)
ptpStatusTableEntry.setIndexNames(
    (0, "SPECTRACOM-PTP-MIB", "ptpStatusRow"),
)
if mibBuilder.loadTexts:
    ptpStatusTableEntry.setStatus("current")


class _PtpStatusRow_Type(Unsigned32):
    """Custom type ptpStatusRow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PtpStatusRow_Type.__name__ = "Unsigned32"
_PtpStatusRow_Object = MibTableColumn
ptpStatusRow = _PtpStatusRow_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 1),
    _PtpStatusRow_Type()
)
ptpStatusRow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpStatusRow.setStatus("current")


class _PtpStatusInstance_Type(Unsigned32):
    """Custom type ptpStatusInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PtpStatusInstance_Type.__name__ = "Unsigned32"
_PtpStatusInstance_Object = MibTableColumn
ptpStatusInstance = _PtpStatusInstance_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 2),
    _PtpStatusInstance_Type()
)
ptpStatusInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusInstance.setStatus("current")


class _PtpStatusReference_Type(DisplayString):
    """Custom type ptpStatusReference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_PtpStatusReference_Type.__name__ = "DisplayString"
_PtpStatusReference_Object = MibTableColumn
ptpStatusReference = _PtpStatusReference_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 3),
    _PtpStatusReference_Type()
)
ptpStatusReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusReference.setStatus("current")


class _PtpStatusNetworkIp_Type(DisplayString):
    """Custom type ptpStatusNetworkIp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_PtpStatusNetworkIp_Type.__name__ = "DisplayString"
_PtpStatusNetworkIp_Object = MibTableColumn
ptpStatusNetworkIp = _PtpStatusNetworkIp_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 4),
    _PtpStatusNetworkIp_Type()
)
ptpStatusNetworkIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusNetworkIp.setStatus("current")


class _PtpStatusNetworkNetmask_Type(DisplayString):
    """Custom type ptpStatusNetworkNetmask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_PtpStatusNetworkNetmask_Type.__name__ = "DisplayString"
_PtpStatusNetworkNetmask_Object = MibTableColumn
ptpStatusNetworkNetmask = _PtpStatusNetworkNetmask_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 5),
    _PtpStatusNetworkNetmask_Type()
)
ptpStatusNetworkNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusNetworkNetmask.setStatus("current")


class _PtpStatusNetworkGateway_Type(DisplayString):
    """Custom type ptpStatusNetworkGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_PtpStatusNetworkGateway_Type.__name__ = "DisplayString"
_PtpStatusNetworkGateway_Object = MibTableColumn
ptpStatusNetworkGateway = _PtpStatusNetworkGateway_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 6),
    _PtpStatusNetworkGateway_Type()
)
ptpStatusNetworkGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusNetworkGateway.setStatus("current")


class _PtpStatusNetworkTransportProtocol_Type(DisplayString):
    """Custom type ptpStatusNetworkTransportProtocol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_PtpStatusNetworkTransportProtocol_Type.__name__ = "DisplayString"
_PtpStatusNetworkTransportProtocol_Object = MibTableColumn
ptpStatusNetworkTransportProtocol = _PtpStatusNetworkTransportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 7),
    _PtpStatusNetworkTransportProtocol_Type()
)
ptpStatusNetworkTransportProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusNetworkTransportProtocol.setStatus("current")
_PtpStatusNetworkTtl_Type = Integer32
_PtpStatusNetworkTtl_Object = MibTableColumn
ptpStatusNetworkTtl = _PtpStatusNetworkTtl_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 8),
    _PtpStatusNetworkTtl_Type()
)
ptpStatusNetworkTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusNetworkTtl.setStatus("current")
_PtpStatusNetworkDomainNumber_Type = Integer32
_PtpStatusNetworkDomainNumber_Object = MibTableColumn
ptpStatusNetworkDomainNumber = _PtpStatusNetworkDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 9),
    _PtpStatusNetworkDomainNumber_Type()
)
ptpStatusNetworkDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusNetworkDomainNumber.setStatus("current")
_PtpStatusPortNumber_Type = Integer32
_PtpStatusPortNumber_Object = MibTableColumn
ptpStatusPortNumber = _PtpStatusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 10),
    _PtpStatusPortNumber_Type()
)
ptpStatusPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusPortNumber.setStatus("current")


class _PtpStatusPortState_Type(DisplayString):
    """Custom type ptpStatusPortState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_PtpStatusPortState_Type.__name__ = "DisplayString"
_PtpStatusPortState_Object = MibTableColumn
ptpStatusPortState = _PtpStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 11),
    _PtpStatusPortState_Type()
)
ptpStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusPortState.setStatus("current")


class _PtpStatusClockIdentity_Type(DisplayString):
    """Custom type ptpStatusClockIdentity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )
    fixed_length = 24


_PtpStatusClockIdentity_Type.__name__ = "DisplayString"
_PtpStatusClockIdentity_Object = MibTableColumn
ptpStatusClockIdentity = _PtpStatusClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 12),
    _PtpStatusClockIdentity_Type()
)
ptpStatusClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusClockIdentity.setStatus("current")


class _PtpStatusClockMode_Type(DisplayString):
    """Custom type ptpStatusClockMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_PtpStatusClockMode_Type.__name__ = "DisplayString"
_PtpStatusClockMode_Object = MibTableColumn
ptpStatusClockMode = _PtpStatusClockMode_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 13),
    _PtpStatusClockMode_Type()
)
ptpStatusClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusClockMode.setStatus("current")


class _PtpStatusClockClass_Type(Integer32):
    """Custom type ptpStatusClockClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              52,
              187,
              248,
              255)
        )
    )
    namedValues = NamedValues(
        *(("sync", 6),
          ("holdoverInSpec", 7),
          ("holdoverOutSpec1", 52),
          ("holdoverOutSpec2", 187),
          ("nosync", 248),
          ("unknown", 255))
    )


_PtpStatusClockClass_Type.__name__ = "Integer32"
_PtpStatusClockClass_Object = MibTableColumn
ptpStatusClockClass = _PtpStatusClockClass_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 14),
    _PtpStatusClockClass_Type()
)
ptpStatusClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusClockClass.setStatus("current")


class _PtpStatusClockAccuracy_Type(DisplayString):
    """Custom type ptpStatusClockAccuracy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_PtpStatusClockAccuracy_Type.__name__ = "DisplayString"
_PtpStatusClockAccuracy_Object = MibTableColumn
ptpStatusClockAccuracy = _PtpStatusClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 15),
    _PtpStatusClockAccuracy_Type()
)
ptpStatusClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusClockAccuracy.setStatus("current")


class _PtpStatusProtocolGmClockClass_Type(Integer32):
    """Custom type ptpStatusProtocolGmClockClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              52,
              187,
              248,
              255)
        )
    )
    namedValues = NamedValues(
        *(("sync", 6),
          ("holdoverInSpec", 7),
          ("holdoverOutSpec1", 52),
          ("holdoverOutSpec2", 187),
          ("nosync", 248),
          ("unknown", 255))
    )


_PtpStatusProtocolGmClockClass_Type.__name__ = "Integer32"
_PtpStatusProtocolGmClockClass_Object = MibTableColumn
ptpStatusProtocolGmClockClass = _PtpStatusProtocolGmClockClass_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 16),
    _PtpStatusProtocolGmClockClass_Type()
)
ptpStatusProtocolGmClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusProtocolGmClockClass.setStatus("current")


class _PtpStatusProtocolGmClockAccuracy_Type(DisplayString):
    """Custom type ptpStatusProtocolGmClockAccuracy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_PtpStatusProtocolGmClockAccuracy_Type.__name__ = "DisplayString"
_PtpStatusProtocolGmClockAccuracy_Object = MibTableColumn
ptpStatusProtocolGmClockAccuracy = _PtpStatusProtocolGmClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 17),
    _PtpStatusProtocolGmClockAccuracy_Type()
)
ptpStatusProtocolGmClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusProtocolGmClockAccuracy.setStatus("current")


class _PtpStatusProtocolOneStep_Type(Integer32):
    """Custom type ptpStatusProtocolOneStep based on Integer32"""
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


_PtpStatusProtocolOneStep_Type.__name__ = "Integer32"
_PtpStatusProtocolOneStep_Object = MibTableColumn
ptpStatusProtocolOneStep = _PtpStatusProtocolOneStep_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 18),
    _PtpStatusProtocolOneStep_Type()
)
ptpStatusProtocolOneStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusProtocolOneStep.setStatus("current")
_PtpStatusProtocolAnnounceReceptionTimeOut_Type = Integer32
_PtpStatusProtocolAnnounceReceptionTimeOut_Object = MibTableColumn
ptpStatusProtocolAnnounceReceptionTimeOut = _PtpStatusProtocolAnnounceReceptionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 19),
    _PtpStatusProtocolAnnounceReceptionTimeOut_Type()
)
ptpStatusProtocolAnnounceReceptionTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusProtocolAnnounceReceptionTimeOut.setStatus("current")
_PtpStatusProtocolLogAnnounceInterval_Type = Integer32
_PtpStatusProtocolLogAnnounceInterval_Object = MibTableColumn
ptpStatusProtocolLogAnnounceInterval = _PtpStatusProtocolLogAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 20),
    _PtpStatusProtocolLogAnnounceInterval_Type()
)
ptpStatusProtocolLogAnnounceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusProtocolLogAnnounceInterval.setStatus("current")
_PtpStatusProtocolLogSyncInterval_Type = Integer32
_PtpStatusProtocolLogSyncInterval_Object = MibTableColumn
ptpStatusProtocolLogSyncInterval = _PtpStatusProtocolLogSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 21),
    _PtpStatusProtocolLogSyncInterval_Type()
)
ptpStatusProtocolLogSyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusProtocolLogSyncInterval.setStatus("current")
_PtpStatusProtocolLogDelayRequestInterval_Type = Integer32
_PtpStatusProtocolLogDelayRequestInterval_Object = MibTableColumn
ptpStatusProtocolLogDelayRequestInterval = _PtpStatusProtocolLogDelayRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 22),
    _PtpStatusProtocolLogDelayRequestInterval_Type()
)
ptpStatusProtocolLogDelayRequestInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusProtocolLogDelayRequestInterval.setStatus("current")
_PtpStatusProtocolLogPeerDelayRequestInterval_Type = Integer32
_PtpStatusProtocolLogPeerDelayRequestInterval_Object = MibTableColumn
ptpStatusProtocolLogPeerDelayRequestInterval = _PtpStatusProtocolLogPeerDelayRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 23),
    _PtpStatusProtocolLogPeerDelayRequestInterval_Type()
)
ptpStatusProtocolLogPeerDelayRequestInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusProtocolLogPeerDelayRequestInterval.setStatus("current")


class _PtpStatusProtocolDelayMechanism_Type(DisplayString):
    """Custom type ptpStatusProtocolDelayMechanism based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_PtpStatusProtocolDelayMechanism_Type.__name__ = "DisplayString"
_PtpStatusProtocolDelayMechanism_Object = MibTableColumn
ptpStatusProtocolDelayMechanism = _PtpStatusProtocolDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 1, 1, 1, 24),
    _PtpStatusProtocolDelayMechanism_Type()
)
ptpStatusProtocolDelayMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpStatusProtocolDelayMechanism.setStatus("current")
_PtpConformance_ObjectIdentity = ObjectIdentity
ptpConformance = _PtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 90)
)
_PtpCompliances_ObjectIdentity = ObjectIdentity
ptpCompliances = _PtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 90, 1)
)
_PtpGroups_ObjectIdentity = ObjectIdentity
ptpGroups = _PtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 90, 2)
)

# Managed Objects groups

ptpObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 90, 2, 1)
)
ptpObjectsGroup.setObjects(
      *(("SPECTRACOM-PTP-MIB", "ptpStatusInstance"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusReference"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusNetworkIp"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusNetworkNetmask"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusNetworkGateway"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusNetworkTransportProtocol"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusNetworkTtl"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusNetworkDomainNumber"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusPortNumber"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusPortState"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusClockIdentity"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusClockMode"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusClockClass"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusClockAccuracy"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusProtocolOneStep"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusProtocolGmClockClass"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusProtocolGmClockAccuracy"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusProtocolAnnounceReceptionTimeOut"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusProtocolLogAnnounceInterval"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusProtocolLogSyncInterval"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusProtocolLogDelayRequestInterval"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusProtocolLogPeerDelayRequestInterval"),
        ("SPECTRACOM-PTP-MIB", "ptpStatusProtocolDelayMechanism"))
)
if mibBuilder.loadTexts:
    ptpObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ptpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18837, 3, 4, 90, 1, 1)
)
ptpCompliance.setObjects(
    ("SPECTRACOM-PTP-MIB", "ptpObjectsGroup")
)
if mibBuilder.loadTexts:
    ptpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPECTRACOM-PTP-MIB",
    **{"spectracomPtpMibModule": spectracomPtpMibModule,
       "ptpSnmpObjs": ptpSnmpObjs,
       "ptpStatusObjs": ptpStatusObjs,
       "ptpStatusTable": ptpStatusTable,
       "ptpStatusTableEntry": ptpStatusTableEntry,
       "ptpStatusRow": ptpStatusRow,
       "ptpStatusInstance": ptpStatusInstance,
       "ptpStatusReference": ptpStatusReference,
       "ptpStatusNetworkIp": ptpStatusNetworkIp,
       "ptpStatusNetworkNetmask": ptpStatusNetworkNetmask,
       "ptpStatusNetworkGateway": ptpStatusNetworkGateway,
       "ptpStatusNetworkTransportProtocol": ptpStatusNetworkTransportProtocol,
       "ptpStatusNetworkTtl": ptpStatusNetworkTtl,
       "ptpStatusNetworkDomainNumber": ptpStatusNetworkDomainNumber,
       "ptpStatusPortNumber": ptpStatusPortNumber,
       "ptpStatusPortState": ptpStatusPortState,
       "ptpStatusClockIdentity": ptpStatusClockIdentity,
       "ptpStatusClockMode": ptpStatusClockMode,
       "ptpStatusClockClass": ptpStatusClockClass,
       "ptpStatusClockAccuracy": ptpStatusClockAccuracy,
       "ptpStatusProtocolGmClockClass": ptpStatusProtocolGmClockClass,
       "ptpStatusProtocolGmClockAccuracy": ptpStatusProtocolGmClockAccuracy,
       "ptpStatusProtocolOneStep": ptpStatusProtocolOneStep,
       "ptpStatusProtocolAnnounceReceptionTimeOut": ptpStatusProtocolAnnounceReceptionTimeOut,
       "ptpStatusProtocolLogAnnounceInterval": ptpStatusProtocolLogAnnounceInterval,
       "ptpStatusProtocolLogSyncInterval": ptpStatusProtocolLogSyncInterval,
       "ptpStatusProtocolLogDelayRequestInterval": ptpStatusProtocolLogDelayRequestInterval,
       "ptpStatusProtocolLogPeerDelayRequestInterval": ptpStatusProtocolLogPeerDelayRequestInterval,
       "ptpStatusProtocolDelayMechanism": ptpStatusProtocolDelayMechanism,
       "ptpConformance": ptpConformance,
       "ptpCompliances": ptpCompliances,
       "ptpCompliance": ptpCompliance,
       "ptpGroups": ptpGroups,
       "ptpObjectsGroup": ptpObjectsGroup}
)
