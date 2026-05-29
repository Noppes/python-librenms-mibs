# SNMP MIB module (HH3C-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-DHCP-SERVER-MIB

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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cDHCPServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101)
)
if mibBuilder.loadTexts:
    hh3cDHCPServer.setRevisions(
        ("2009-05-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDHCPServerObjects_ObjectIdentity = ObjectIdentity
hh3cDHCPServerObjects = _Hh3cDHCPServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 1)
)
_Hh3cDHCPServerIPPoolUsage_Type = Integer32
_Hh3cDHCPServerIPPoolUsage_Object = MibScalar
hh3cDHCPServerIPPoolUsage = _Hh3cDHCPServerIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 1),
    _Hh3cDHCPServerIPPoolUsage_Type()
)
hh3cDHCPServerIPPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPServerIPPoolUsage.setStatus("current")
_Hh3cDHCPServerReqTimes_Type = Counter32
_Hh3cDHCPServerReqTimes_Object = MibScalar
hh3cDHCPServerReqTimes = _Hh3cDHCPServerReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 2),
    _Hh3cDHCPServerReqTimes_Type()
)
hh3cDHCPServerReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPServerReqTimes.setStatus("current")
_Hh3cDHCPServerReqSuccessTimes_Type = Counter32
_Hh3cDHCPServerReqSuccessTimes_Object = MibScalar
hh3cDHCPServerReqSuccessTimes = _Hh3cDHCPServerReqSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 3),
    _Hh3cDHCPServerReqSuccessTimes_Type()
)
hh3cDHCPServerReqSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPServerReqSuccessTimes.setStatus("current")


class _Hh3cDHCPServerAvgIpUseThreshold_Type(Integer32):
    """Custom type hh3cDHCPServerAvgIpUseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDHCPServerAvgIpUseThreshold_Type.__name__ = "Integer32"
_Hh3cDHCPServerAvgIpUseThreshold_Object = MibScalar
hh3cDHCPServerAvgIpUseThreshold = _Hh3cDHCPServerAvgIpUseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 4),
    _Hh3cDHCPServerAvgIpUseThreshold_Type()
)
hh3cDHCPServerAvgIpUseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPServerAvgIpUseThreshold.setStatus("current")


class _Hh3cDHCPServerMaxIpUseThreshold_Type(Integer32):
    """Custom type hh3cDHCPServerMaxIpUseThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDHCPServerMaxIpUseThreshold_Type.__name__ = "Integer32"
_Hh3cDHCPServerMaxIpUseThreshold_Object = MibScalar
hh3cDHCPServerMaxIpUseThreshold = _Hh3cDHCPServerMaxIpUseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 5),
    _Hh3cDHCPServerMaxIpUseThreshold_Type()
)
hh3cDHCPServerMaxIpUseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPServerMaxIpUseThreshold.setStatus("current")


class _Hh3cDHCPServerAllocateThreshold_Type(Integer32):
    """Custom type hh3cDHCPServerAllocateThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDHCPServerAllocateThreshold_Type.__name__ = "Integer32"
_Hh3cDHCPServerAllocateThreshold_Object = MibScalar
hh3cDHCPServerAllocateThreshold = _Hh3cDHCPServerAllocateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 6),
    _Hh3cDHCPServerAllocateThreshold_Type()
)
hh3cDHCPServerAllocateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPServerAllocateThreshold.setStatus("current")
_Hh3cDHCPServerTables_ObjectIdentity = ObjectIdentity
hh3cDHCPServerTables = _Hh3cDHCPServerTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2)
)


class _Hh3cDHCPServerPoolName_Type(OctetString):
    """Custom type hh3cDHCPServerPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDHCPServerPoolName_Type.__name__ = "OctetString"
_Hh3cDHCPServerPoolName_Object = MibScalar
hh3cDHCPServerPoolName = _Hh3cDHCPServerPoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 1),
    _Hh3cDHCPServerPoolName_Type()
)
hh3cDHCPServerPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDHCPServerPoolName.setStatus("current")
_Hh3cDHCPSrvGlobalPoolTable_Object = MibTable
hh3cDHCPSrvGlobalPoolTable = _Hh3cDHCPSrvGlobalPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolTable.setStatus("current")
_Hh3cDHCPSrvGlobalPoolEntry_Object = MibTableRow
hh3cDHCPSrvGlobalPoolEntry = _Hh3cDHCPSrvGlobalPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2, 1)
)
hh3cDHCPSrvGlobalPoolEntry.setIndexNames(
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolEntry.setStatus("current")


class _Hh3cDHCPSrvGlobalPoolName_Type(OctetString):
    """Custom type hh3cDHCPSrvGlobalPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDHCPSrvGlobalPoolName_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlobalPoolName_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolName = _Hh3cDHCPSrvGlobalPoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2, 1, 1),
    _Hh3cDHCPSrvGlobalPoolName_Type()
)
hh3cDHCPSrvGlobalPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolName.setStatus("current")
_Hh3cDHCPSrvGlobalPoolRowStatus_Type = RowStatus
_Hh3cDHCPSrvGlobalPoolRowStatus_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolRowStatus = _Hh3cDHCPSrvGlobalPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2, 1, 2),
    _Hh3cDHCPSrvGlobalPoolRowStatus_Type()
)
hh3cDHCPSrvGlobalPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolRowStatus.setStatus("current")
_Hh3cDHCPSrvGlobalPoolConfigTable_Object = MibTable
hh3cDHCPSrvGlobalPoolConfigTable = _Hh3cDHCPSrvGlobalPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolConfigTable.setStatus("current")
_Hh3cDHCPSrvGlobalPoolConfigEntry_Object = MibTableRow
hh3cDHCPSrvGlobalPoolConfigEntry = _Hh3cDHCPSrvGlobalPoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1)
)
hh3cDHCPSrvGlobalPoolConfigEntry.setIndexNames(
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolConfigEntry.setStatus("current")


class _Hh3cDHCPSrvGlobalPoolType_Type(Integer32):
    """Custom type hh3cDHCPSrvGlobalPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("host", 1),
          ("network", 2))
    )


_Hh3cDHCPSrvGlobalPoolType_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlobalPoolType_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolType = _Hh3cDHCPSrvGlobalPoolType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 1),
    _Hh3cDHCPSrvGlobalPoolType_Type()
)
hh3cDHCPSrvGlobalPoolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolType.setStatus("current")
_Hh3cDHCPSrvGlobalPoolNetwork_Type = IpAddress
_Hh3cDHCPSrvGlobalPoolNetwork_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolNetwork = _Hh3cDHCPSrvGlobalPoolNetwork_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 2),
    _Hh3cDHCPSrvGlobalPoolNetwork_Type()
)
hh3cDHCPSrvGlobalPoolNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolNetwork.setStatus("current")
_Hh3cDHCPSrvGlobalPoolNetworkMask_Type = IpAddress
_Hh3cDHCPSrvGlobalPoolNetworkMask_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolNetworkMask = _Hh3cDHCPSrvGlobalPoolNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 3),
    _Hh3cDHCPSrvGlobalPoolNetworkMask_Type()
)
hh3cDHCPSrvGlobalPoolNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolNetworkMask.setStatus("current")
_Hh3cDHCPSrvGlobalPoolHostIPAddr_Type = IpAddress
_Hh3cDHCPSrvGlobalPoolHostIPAddr_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolHostIPAddr = _Hh3cDHCPSrvGlobalPoolHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 4),
    _Hh3cDHCPSrvGlobalPoolHostIPAddr_Type()
)
hh3cDHCPSrvGlobalPoolHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolHostIPAddr.setStatus("current")
_Hh3cDHCPSrvGlobalPoolHostMask_Type = IpAddress
_Hh3cDHCPSrvGlobalPoolHostMask_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolHostMask = _Hh3cDHCPSrvGlobalPoolHostMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 5),
    _Hh3cDHCPSrvGlobalPoolHostMask_Type()
)
hh3cDHCPSrvGlobalPoolHostMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolHostMask.setStatus("current")
_Hh3cDHCPSrvGlobalPoolHostHAddr_Type = MacAddress
_Hh3cDHCPSrvGlobalPoolHostHAddr_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolHostHAddr = _Hh3cDHCPSrvGlobalPoolHostHAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 6),
    _Hh3cDHCPSrvGlobalPoolHostHAddr_Type()
)
hh3cDHCPSrvGlobalPoolHostHAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolHostHAddr.setStatus("current")


class _Hh3cDHCPSrvGlobalPoolCfgUndoFlag_Type(Integer32):
    """Custom type hh3cDHCPSrvGlobalPoolCfgUndoFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undonetworkip", 1),
          ("undohostip", 2),
          ("undohosthaddr", 3))
    )


_Hh3cDHCPSrvGlobalPoolCfgUndoFlag_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlobalPoolCfgUndoFlag_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolCfgUndoFlag = _Hh3cDHCPSrvGlobalPoolCfgUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 7),
    _Hh3cDHCPSrvGlobalPoolCfgUndoFlag_Type()
)
hh3cDHCPSrvGlobalPoolCfgUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolCfgUndoFlag.setStatus("current")
_Hh3cDHCPSrvGlobalPoolStartAddr_Type = IpAddress
_Hh3cDHCPSrvGlobalPoolStartAddr_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolStartAddr = _Hh3cDHCPSrvGlobalPoolStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 8),
    _Hh3cDHCPSrvGlobalPoolStartAddr_Type()
)
hh3cDHCPSrvGlobalPoolStartAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolStartAddr.setStatus("current")
_Hh3cDHCPSrvGlobalPoolEndAddr_Type = IpAddress
_Hh3cDHCPSrvGlobalPoolEndAddr_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolEndAddr = _Hh3cDHCPSrvGlobalPoolEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 9),
    _Hh3cDHCPSrvGlobalPoolEndAddr_Type()
)
hh3cDHCPSrvGlobalPoolEndAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolEndAddr.setStatus("current")


class _Hh3cDHCPSrvGlobalPoolAllocObject_Type(Integer32):
    """Custom type hh3cDHCPSrvGlobalPoolAllocObject based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("user", 0),
          ("admin", 1))
    )


_Hh3cDHCPSrvGlobalPoolAllocObject_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlobalPoolAllocObject_Object = MibTableColumn
hh3cDHCPSrvGlobalPoolAllocObject = _Hh3cDHCPSrvGlobalPoolAllocObject_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 10),
    _Hh3cDHCPSrvGlobalPoolAllocObject_Type()
)
hh3cDHCPSrvGlobalPoolAllocObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolAllocObject.setStatus("current")
_Hh3cDHCPSrvGlobalPoolParaTable_Object = MibTable
hh3cDHCPSrvGlobalPoolParaTable = _Hh3cDHCPSrvGlobalPoolParaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolParaTable.setStatus("current")
_Hh3cDHCPSrvGlobalPoolParaEntry_Object = MibTableRow
hh3cDHCPSrvGlobalPoolParaEntry = _Hh3cDHCPSrvGlobalPoolParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1)
)
hh3cDHCPSrvGlobalPoolParaEntry.setIndexNames(
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolParaEntry.setStatus("current")


class _Hh3cDHCPSrvGlbPoolLeaseDay_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolLeaseDay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_Hh3cDHCPSrvGlbPoolLeaseDay_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolLeaseDay_Object = MibTableColumn
hh3cDHCPSrvGlbPoolLeaseDay = _Hh3cDHCPSrvGlbPoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 1),
    _Hh3cDHCPSrvGlbPoolLeaseDay_Type()
)
hh3cDHCPSrvGlbPoolLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolLeaseDay.setStatus("current")


class _Hh3cDHCPSrvGlbPoolLeaseHour_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolLeaseHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hh3cDHCPSrvGlbPoolLeaseHour_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolLeaseHour_Object = MibTableColumn
hh3cDHCPSrvGlbPoolLeaseHour = _Hh3cDHCPSrvGlbPoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 2),
    _Hh3cDHCPSrvGlbPoolLeaseHour_Type()
)
hh3cDHCPSrvGlbPoolLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolLeaseHour.setStatus("current")


class _Hh3cDHCPSrvGlbPoolLeaseMinute_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolLeaseMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Hh3cDHCPSrvGlbPoolLeaseMinute_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolLeaseMinute_Object = MibTableColumn
hh3cDHCPSrvGlbPoolLeaseMinute = _Hh3cDHCPSrvGlbPoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 3),
    _Hh3cDHCPSrvGlbPoolLeaseMinute_Type()
)
hh3cDHCPSrvGlbPoolLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolLeaseMinute.setStatus("current")


class _Hh3cDHCPSrvGlbPoolLeaseUnlimited_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolLeaseUnlimited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("unlimited", 1))
    )


_Hh3cDHCPSrvGlbPoolLeaseUnlimited_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolLeaseUnlimited_Object = MibTableColumn
hh3cDHCPSrvGlbPoolLeaseUnlimited = _Hh3cDHCPSrvGlbPoolLeaseUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 4),
    _Hh3cDHCPSrvGlbPoolLeaseUnlimited_Type()
)
hh3cDHCPSrvGlbPoolLeaseUnlimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolLeaseUnlimited.setStatus("current")


class _Hh3cDHCPSrvGlbPoolDomainName_Type(OctetString):
    """Custom type hh3cDHCPSrvGlbPoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDHCPSrvGlbPoolDomainName_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlbPoolDomainName_Object = MibTableColumn
hh3cDHCPSrvGlbPoolDomainName = _Hh3cDHCPSrvGlbPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 5),
    _Hh3cDHCPSrvGlbPoolDomainName_Type()
)
hh3cDHCPSrvGlbPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolDomainName.setStatus("current")


class _Hh3cDHCPSrvGlbPoolCliGWIPStr_Type(OctetString):
    """Custom type hh3cDHCPSrvGlbPoolCliGWIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSrvGlbPoolCliGWIPStr_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlbPoolCliGWIPStr_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliGWIPStr = _Hh3cDHCPSrvGlbPoolCliGWIPStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 6),
    _Hh3cDHCPSrvGlbPoolCliGWIPStr_Type()
)
hh3cDHCPSrvGlbPoolCliGWIPStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliGWIPStr.setStatus("current")
_Hh3cDHCPSrvGlbPoolCliGWIPUndo_Type = IpAddress
_Hh3cDHCPSrvGlbPoolCliGWIPUndo_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliGWIPUndo = _Hh3cDHCPSrvGlbPoolCliGWIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 7),
    _Hh3cDHCPSrvGlbPoolCliGWIPUndo_Type()
)
hh3cDHCPSrvGlbPoolCliGWIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliGWIPUndo.setStatus("current")


class _Hh3cDHCPSrvGlbPoolCliDNSIPStr_Type(OctetString):
    """Custom type hh3cDHCPSrvGlbPoolCliDNSIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSrvGlbPoolCliDNSIPStr_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlbPoolCliDNSIPStr_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliDNSIPStr = _Hh3cDHCPSrvGlbPoolCliDNSIPStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 8),
    _Hh3cDHCPSrvGlbPoolCliDNSIPStr_Type()
)
hh3cDHCPSrvGlbPoolCliDNSIPStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliDNSIPStr.setStatus("current")
_Hh3cDHCPSrvGlbPoolCliDNSIPUndo_Type = IpAddress
_Hh3cDHCPSrvGlbPoolCliDNSIPUndo_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliDNSIPUndo = _Hh3cDHCPSrvGlbPoolCliDNSIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 9),
    _Hh3cDHCPSrvGlbPoolCliDNSIPUndo_Type()
)
hh3cDHCPSrvGlbPoolCliDNSIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliDNSIPUndo.setStatus("current")


class _Hh3cDHCPSrvGlbPoolCliNetbiosType_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolCliNetbiosType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("bnode", 1),
          ("pnode", 2),
          ("mnode", 4),
          ("hnode", 8))
    )


_Hh3cDHCPSrvGlbPoolCliNetbiosType_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolCliNetbiosType_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliNetbiosType = _Hh3cDHCPSrvGlbPoolCliNetbiosType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 10),
    _Hh3cDHCPSrvGlbPoolCliNetbiosType_Type()
)
hh3cDHCPSrvGlbPoolCliNetbiosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliNetbiosType.setStatus("current")


class _Hh3cDHCPSrvGlbPoolCliNbnsIPStr_Type(OctetString):
    """Custom type hh3cDHCPSrvGlbPoolCliNbnsIPStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSrvGlbPoolCliNbnsIPStr_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlbPoolCliNbnsIPStr_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliNbnsIPStr = _Hh3cDHCPSrvGlbPoolCliNbnsIPStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 11),
    _Hh3cDHCPSrvGlbPoolCliNbnsIPStr_Type()
)
hh3cDHCPSrvGlbPoolCliNbnsIPStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliNbnsIPStr.setStatus("current")
_Hh3cDHCPSrvGlbPoolCliNbnsIPUndo_Type = IpAddress
_Hh3cDHCPSrvGlbPoolCliNbnsIPUndo_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliNbnsIPUndo = _Hh3cDHCPSrvGlbPoolCliNbnsIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 12),
    _Hh3cDHCPSrvGlbPoolCliNbnsIPUndo_Type()
)
hh3cDHCPSrvGlbPoolCliNbnsIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliNbnsIPUndo.setStatus("current")


class _Hh3cDHCPSrvGlbPoolParaUndoFlag_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolParaUndoFlag based on Integer32"""
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
        *(("undoDomain", 1),
          ("undoLease", 2),
          ("undoGateway", 3),
          ("undoDns", 4),
          ("undoNbns", 5),
          ("undoNbType", 6))
    )


_Hh3cDHCPSrvGlbPoolParaUndoFlag_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolParaUndoFlag_Object = MibTableColumn
hh3cDHCPSrvGlbPoolParaUndoFlag = _Hh3cDHCPSrvGlbPoolParaUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 13),
    _Hh3cDHCPSrvGlbPoolParaUndoFlag_Type()
)
hh3cDHCPSrvGlbPoolParaUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolParaUndoFlag.setStatus("current")


class _Hh3cDHCPSrvGlbPoolIPInUseReset_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolIPInUseReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cDHCPSrvGlbPoolIPInUseReset_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolIPInUseReset_Object = MibTableColumn
hh3cDHCPSrvGlbPoolIPInUseReset = _Hh3cDHCPSrvGlbPoolIPInUseReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 14),
    _Hh3cDHCPSrvGlbPoolIPInUseReset_Type()
)
hh3cDHCPSrvGlbPoolIPInUseReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolIPInUseReset.setStatus("current")
_Hh3cDHCPSrvGlbPoolLeaseTime_Type = TimeTicks
_Hh3cDHCPSrvGlbPoolLeaseTime_Object = MibTableColumn
hh3cDHCPSrvGlbPoolLeaseTime = _Hh3cDHCPSrvGlbPoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 15),
    _Hh3cDHCPSrvGlbPoolLeaseTime_Type()
)
hh3cDHCPSrvGlbPoolLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolLeaseTime.setStatus("current")
_Hh3cDHCPSrvGlbPoolPrimaryDNSIP_Type = IpAddress
_Hh3cDHCPSrvGlbPoolPrimaryDNSIP_Object = MibTableColumn
hh3cDHCPSrvGlbPoolPrimaryDNSIP = _Hh3cDHCPSrvGlbPoolPrimaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 16),
    _Hh3cDHCPSrvGlbPoolPrimaryDNSIP_Type()
)
hh3cDHCPSrvGlbPoolPrimaryDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolPrimaryDNSIP.setStatus("current")
_Hh3cDHCPSrvGlbPoolSecondaryDNSIP_Type = IpAddress
_Hh3cDHCPSrvGlbPoolSecondaryDNSIP_Object = MibTableColumn
hh3cDHCPSrvGlbPoolSecondaryDNSIP = _Hh3cDHCPSrvGlbPoolSecondaryDNSIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 17),
    _Hh3cDHCPSrvGlbPoolSecondaryDNSIP_Type()
)
hh3cDHCPSrvGlbPoolSecondaryDNSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolSecondaryDNSIP.setStatus("current")


class _Hh3cDHCPSrvGlbPoolLeaseSecond_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolLeaseSecond based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Hh3cDHCPSrvGlbPoolLeaseSecond_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolLeaseSecond_Object = MibTableColumn
hh3cDHCPSrvGlbPoolLeaseSecond = _Hh3cDHCPSrvGlbPoolLeaseSecond_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 18),
    _Hh3cDHCPSrvGlbPoolLeaseSecond_Type()
)
hh3cDHCPSrvGlbPoolLeaseSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolLeaseSecond.setStatus("current")


class _Hh3cDHCPSrvGlbPoolLeaseTimeSec_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolLeaseTimeSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 31622399),
    )


_Hh3cDHCPSrvGlbPoolLeaseTimeSec_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolLeaseTimeSec_Object = MibTableColumn
hh3cDHCPSrvGlbPoolLeaseTimeSec = _Hh3cDHCPSrvGlbPoolLeaseTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 19),
    _Hh3cDHCPSrvGlbPoolLeaseTimeSec_Type()
)
hh3cDHCPSrvGlbPoolLeaseTimeSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolLeaseTimeSec.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolLeaseTimeSec.setUnits("seconds")
_Hh3cDHCPSrvGlbPoolCliGWIPAddr_Type = IpAddress
_Hh3cDHCPSrvGlbPoolCliGWIPAddr_Object = MibTableColumn
hh3cDHCPSrvGlbPoolCliGWIPAddr = _Hh3cDHCPSrvGlbPoolCliGWIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 20),
    _Hh3cDHCPSrvGlbPoolCliGWIPAddr_Type()
)
hh3cDHCPSrvGlbPoolCliGWIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolCliGWIPAddr.setStatus("current")
_Hh3cDHCPSrvGlobalPoolOptionTable_Object = MibTable
hh3cDHCPSrvGlobalPoolOptionTable = _Hh3cDHCPSrvGlobalPoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolOptionTable.setStatus("current")
_Hh3cDHCPSrvGlobalPoolOptionEntry_Object = MibTableRow
hh3cDHCPSrvGlobalPoolOptionEntry = _Hh3cDHCPSrvGlobalPoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1)
)
hh3cDHCPSrvGlobalPoolOptionEntry.setIndexNames(
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"),
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlbPoolOptCode"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolOptionEntry.setStatus("current")


class _Hh3cDHCPSrvGlbPoolOptCode_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolOptCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Hh3cDHCPSrvGlbPoolOptCode_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolOptCode_Object = MibTableColumn
hh3cDHCPSrvGlbPoolOptCode = _Hh3cDHCPSrvGlbPoolOptCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 1),
    _Hh3cDHCPSrvGlbPoolOptCode_Type()
)
hh3cDHCPSrvGlbPoolOptCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolOptCode.setStatus("current")


class _Hh3cDHCPSrvGlbPoolOptType_Type(Integer32):
    """Custom type hh3cDHCPSrvGlbPoolOptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2),
          ("ip", 3))
    )


_Hh3cDHCPSrvGlbPoolOptType_Type.__name__ = "Integer32"
_Hh3cDHCPSrvGlbPoolOptType_Object = MibTableColumn
hh3cDHCPSrvGlbPoolOptType = _Hh3cDHCPSrvGlbPoolOptType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 2),
    _Hh3cDHCPSrvGlbPoolOptType_Type()
)
hh3cDHCPSrvGlbPoolOptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolOptType.setStatus("current")


class _Hh3cDHCPSrvGlbPoolOptAscii_Type(OctetString):
    """Custom type hh3cDHCPSrvGlbPoolOptAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDHCPSrvGlbPoolOptAscii_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlbPoolOptAscii_Object = MibTableColumn
hh3cDHCPSrvGlbPoolOptAscii = _Hh3cDHCPSrvGlbPoolOptAscii_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 3),
    _Hh3cDHCPSrvGlbPoolOptAscii_Type()
)
hh3cDHCPSrvGlbPoolOptAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolOptAscii.setStatus("current")


class _Hh3cDHCPSrvGlbPoolOptHexString_Type(OctetString):
    """Custom type hh3cDHCPSrvGlbPoolOptHexString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 573),
    )


_Hh3cDHCPSrvGlbPoolOptHexString_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlbPoolOptHexString_Object = MibTableColumn
hh3cDHCPSrvGlbPoolOptHexString = _Hh3cDHCPSrvGlbPoolOptHexString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 4),
    _Hh3cDHCPSrvGlbPoolOptHexString_Type()
)
hh3cDHCPSrvGlbPoolOptHexString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolOptHexString.setStatus("current")


class _Hh3cDHCPSrvGlbPoolOptIPString_Type(OctetString):
    """Custom type hh3cDHCPSrvGlbPoolOptIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSrvGlbPoolOptIPString_Type.__name__ = "OctetString"
_Hh3cDHCPSrvGlbPoolOptIPString_Object = MibTableColumn
hh3cDHCPSrvGlbPoolOptIPString = _Hh3cDHCPSrvGlbPoolOptIPString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 5),
    _Hh3cDHCPSrvGlbPoolOptIPString_Type()
)
hh3cDHCPSrvGlbPoolOptIPString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolOptIPString.setStatus("current")
_Hh3cDHCPSrvGlbPoolOptRowStatus_Type = RowStatus
_Hh3cDHCPSrvGlbPoolOptRowStatus_Object = MibTableColumn
hh3cDHCPSrvGlbPoolOptRowStatus = _Hh3cDHCPSrvGlbPoolOptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 6),
    _Hh3cDHCPSrvGlbPoolOptRowStatus_Type()
)
hh3cDHCPSrvGlbPoolOptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolOptRowStatus.setStatus("current")
_Hh3cDHCPSrvGlobalPoolStatTable_Object = MibTable
hh3cDHCPSrvGlobalPoolStatTable = _Hh3cDHCPSrvGlobalPoolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolStatTable.setStatus("current")
_Hh3cDHCPSrvGlobalPoolStatEntry_Object = MibTableRow
hh3cDHCPSrvGlobalPoolStatEntry = _Hh3cDHCPSrvGlobalPoolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1)
)
hh3cDHCPSrvGlobalPoolStatEntry.setIndexNames(
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlobalPoolStatEntry.setStatus("current")
_Hh3cDHCPSrvGlbPoolIPPoolUsage_Type = Integer32
_Hh3cDHCPSrvGlbPoolIPPoolUsage_Object = MibTableColumn
hh3cDHCPSrvGlbPoolIPPoolUsage = _Hh3cDHCPSrvGlbPoolIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 1),
    _Hh3cDHCPSrvGlbPoolIPPoolUsage_Type()
)
hh3cDHCPSrvGlbPoolIPPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolIPPoolUsage.setStatus("current")
_Hh3cDHCPSrvGlbPoolReqTimes_Type = Counter32
_Hh3cDHCPSrvGlbPoolReqTimes_Object = MibTableColumn
hh3cDHCPSrvGlbPoolReqTimes = _Hh3cDHCPSrvGlbPoolReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 2),
    _Hh3cDHCPSrvGlbPoolReqTimes_Type()
)
hh3cDHCPSrvGlbPoolReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolReqTimes.setStatus("current")
_Hh3cDHCPSrvGlbPoolSuccessTimes_Type = Counter32
_Hh3cDHCPSrvGlbPoolSuccessTimes_Object = MibTableColumn
hh3cDHCPSrvGlbPoolSuccessTimes = _Hh3cDHCPSrvGlbPoolSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 3),
    _Hh3cDHCPSrvGlbPoolSuccessTimes_Type()
)
hh3cDHCPSrvGlbPoolSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolSuccessTimes.setStatus("current")
_Hh3cDHCPSrvGlbPoolDiscoverTimes_Type = Counter32
_Hh3cDHCPSrvGlbPoolDiscoverTimes_Object = MibTableColumn
hh3cDHCPSrvGlbPoolDiscoverTimes = _Hh3cDHCPSrvGlbPoolDiscoverTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 4),
    _Hh3cDHCPSrvGlbPoolDiscoverTimes_Type()
)
hh3cDHCPSrvGlbPoolDiscoverTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolDiscoverTimes.setStatus("current")
_Hh3cDHCPSrvGlbPoolOfferTimes_Type = Counter32
_Hh3cDHCPSrvGlbPoolOfferTimes_Object = MibTableColumn
hh3cDHCPSrvGlbPoolOfferTimes = _Hh3cDHCPSrvGlbPoolOfferTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 5),
    _Hh3cDHCPSrvGlbPoolOfferTimes_Type()
)
hh3cDHCPSrvGlbPoolOfferTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolOfferTimes.setStatus("current")
_Hh3cDHCPSrvGlbPoolACKTimes_Type = Counter32
_Hh3cDHCPSrvGlbPoolACKTimes_Object = MibTableColumn
hh3cDHCPSrvGlbPoolACKTimes = _Hh3cDHCPSrvGlbPoolACKTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 6),
    _Hh3cDHCPSrvGlbPoolACKTimes_Type()
)
hh3cDHCPSrvGlbPoolACKTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolACKTimes.setStatus("current")
_Hh3cDHCPSrvGlbPoolTotalIpNum_Type = Counter32
_Hh3cDHCPSrvGlbPoolTotalIpNum_Object = MibTableColumn
hh3cDHCPSrvGlbPoolTotalIpNum = _Hh3cDHCPSrvGlbPoolTotalIpNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 7),
    _Hh3cDHCPSrvGlbPoolTotalIpNum_Type()
)
hh3cDHCPSrvGlbPoolTotalIpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolTotalIpNum.setStatus("current")
_Hh3cDHCPSrvGlbPoolInUsedIpNum_Type = Counter32
_Hh3cDHCPSrvGlbPoolInUsedIpNum_Object = MibTableColumn
hh3cDHCPSrvGlbPoolInUsedIpNum = _Hh3cDHCPSrvGlbPoolInUsedIpNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 8),
    _Hh3cDHCPSrvGlbPoolInUsedIpNum_Type()
)
hh3cDHCPSrvGlbPoolInUsedIpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSrvGlbPoolInUsedIpNum.setStatus("current")
_Hh3cDHCPSvrOptionGroupTable_Object = MibTable
hh3cDHCPSvrOptionGroupTable = _Hh3cDHCPSvrOptionGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cDHCPSvrOptionGroupTable.setStatus("current")
_Hh3cDHCPSvrOptionGroupEntry_Object = MibTableRow
hh3cDHCPSvrOptionGroupEntry = _Hh3cDHCPSvrOptionGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 7, 1)
)
hh3cDHCPSvrOptionGroupEntry.setIndexNames(
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSvrOptionGroupIndex"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSvrOptionGroupEntry.setStatus("current")


class _Hh3cDHCPSvrOptionGroupIndex_Type(Integer32):
    """Custom type hh3cDHCPSvrOptionGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDHCPSvrOptionGroupIndex_Type.__name__ = "Integer32"
_Hh3cDHCPSvrOptionGroupIndex_Object = MibTableColumn
hh3cDHCPSvrOptionGroupIndex = _Hh3cDHCPSvrOptionGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 7, 1, 1),
    _Hh3cDHCPSvrOptionGroupIndex_Type()
)
hh3cDHCPSvrOptionGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSvrOptionGroupIndex.setStatus("current")
_Hh3cDHCPSvrOptionGroupRowstatus_Type = RowStatus
_Hh3cDHCPSvrOptionGroupRowstatus_Object = MibTableColumn
hh3cDHCPSvrOptionGroupRowstatus = _Hh3cDHCPSvrOptionGroupRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 7, 1, 2),
    _Hh3cDHCPSvrOptionGroupRowstatus_Type()
)
hh3cDHCPSvrOptionGroupRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSvrOptionGroupRowstatus.setStatus("current")
_Hh3cDHCPSvrOptionTable_Object = MibTable
hh3cDHCPSvrOptionTable = _Hh3cDHCPSvrOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cDHCPSvrOptionTable.setStatus("current")
_Hh3cDHCPSvrOptionEntry_Object = MibTableRow
hh3cDHCPSvrOptionEntry = _Hh3cDHCPSvrOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 8, 1)
)
hh3cDHCPSvrOptionEntry.setIndexNames(
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSvrOptionGroupIndex"),
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSvrOptionCode"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSvrOptionEntry.setStatus("current")


class _Hh3cDHCPSvrOptionCode_Type(Integer32):
    """Custom type hh3cDHCPSvrOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Hh3cDHCPSvrOptionCode_Type.__name__ = "Integer32"
_Hh3cDHCPSvrOptionCode_Object = MibTableColumn
hh3cDHCPSvrOptionCode = _Hh3cDHCPSvrOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 8, 1, 1),
    _Hh3cDHCPSvrOptionCode_Type()
)
hh3cDHCPSvrOptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSvrOptionCode.setStatus("current")


class _Hh3cDHCPSvrOptionType_Type(Integer32):
    """Custom type hh3cDHCPSvrOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2),
          ("ip", 3))
    )


_Hh3cDHCPSvrOptionType_Type.__name__ = "Integer32"
_Hh3cDHCPSvrOptionType_Object = MibTableColumn
hh3cDHCPSvrOptionType = _Hh3cDHCPSvrOptionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 8, 1, 2),
    _Hh3cDHCPSvrOptionType_Type()
)
hh3cDHCPSvrOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSvrOptionType.setStatus("current")


class _Hh3cDHCPSvrOptionAsciiString_Type(OctetString):
    """Custom type hh3cDHCPSvrOptionAsciiString based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDHCPSvrOptionAsciiString_Type.__name__ = "OctetString"
_Hh3cDHCPSvrOptionAsciiString_Object = MibTableColumn
hh3cDHCPSvrOptionAsciiString = _Hh3cDHCPSvrOptionAsciiString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 8, 1, 3),
    _Hh3cDHCPSvrOptionAsciiString_Type()
)
hh3cDHCPSvrOptionAsciiString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSvrOptionAsciiString.setStatus("current")


class _Hh3cDHCPSvrOptionHexString_Type(OctetString):
    """Custom type hh3cDHCPSvrOptionHexString based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 573),
    )


_Hh3cDHCPSvrOptionHexString_Type.__name__ = "OctetString"
_Hh3cDHCPSvrOptionHexString_Object = MibTableColumn
hh3cDHCPSvrOptionHexString = _Hh3cDHCPSvrOptionHexString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 8, 1, 4),
    _Hh3cDHCPSvrOptionHexString_Type()
)
hh3cDHCPSvrOptionHexString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSvrOptionHexString.setStatus("current")


class _Hh3cDHCPSvrOptionIPString_Type(OctetString):
    """Custom type hh3cDHCPSvrOptionIPString based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSvrOptionIPString_Type.__name__ = "OctetString"
_Hh3cDHCPSvrOptionIPString_Object = MibTableColumn
hh3cDHCPSvrOptionIPString = _Hh3cDHCPSvrOptionIPString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 8, 1, 5),
    _Hh3cDHCPSvrOptionIPString_Type()
)
hh3cDHCPSvrOptionIPString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSvrOptionIPString.setStatus("current")
_Hh3cDHCPSvrOptionRowstatus_Type = RowStatus
_Hh3cDHCPSvrOptionRowstatus_Object = MibTableColumn
hh3cDHCPSvrOptionRowstatus = _Hh3cDHCPSvrOptionRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 8, 1, 6),
    _Hh3cDHCPSvrOptionRowstatus_Type()
)
hh3cDHCPSvrOptionRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSvrOptionRowstatus.setStatus("current")
_Hh3cDHCPSvrVerifyMacTable_Object = MibTable
hh3cDHCPSvrVerifyMacTable = _Hh3cDHCPSvrVerifyMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 9)
)
if mibBuilder.loadTexts:
    hh3cDHCPSvrVerifyMacTable.setStatus("current")
_Hh3cDHCPSvrVerifyMacEntry_Object = MibTableRow
hh3cDHCPSvrVerifyMacEntry = _Hh3cDHCPSvrVerifyMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 9, 1)
)
hh3cDHCPSvrVerifyMacEntry.setIndexNames(
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSvrVerifyMacEntry.setStatus("current")


class _Hh3cDHCPSvrVerifyMacSwitch_Type(Integer32):
    """Custom type hh3cDHCPSvrVerifyMacSwitch based on Integer32"""
    defaultValue = 2

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


_Hh3cDHCPSvrVerifyMacSwitch_Type.__name__ = "Integer32"
_Hh3cDHCPSvrVerifyMacSwitch_Object = MibTableColumn
hh3cDHCPSvrVerifyMacSwitch = _Hh3cDHCPSvrVerifyMacSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 9, 1, 1),
    _Hh3cDHCPSvrVerifyMacSwitch_Type()
)
hh3cDHCPSvrVerifyMacSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSvrVerifyMacSwitch.setStatus("current")
_Hh3cDHCPSvrPoolMacTable_Object = MibTable
hh3cDHCPSvrPoolMacTable = _Hh3cDHCPSvrPoolMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 10)
)
if mibBuilder.loadTexts:
    hh3cDHCPSvrPoolMacTable.setStatus("current")
_Hh3cDHCPSvrPoolMacEntry_Object = MibTableRow
hh3cDHCPSvrPoolMacEntry = _Hh3cDHCPSvrPoolMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 10, 1)
)
hh3cDHCPSvrPoolMacEntry.setIndexNames(
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"),
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSvrPoolMac"),
    (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSvrPoolMacMask"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSvrPoolMacEntry.setStatus("current")
_Hh3cDHCPSvrPoolMac_Type = MacAddress
_Hh3cDHCPSvrPoolMac_Object = MibTableColumn
hh3cDHCPSvrPoolMac = _Hh3cDHCPSvrPoolMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 10, 1, 1),
    _Hh3cDHCPSvrPoolMac_Type()
)
hh3cDHCPSvrPoolMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSvrPoolMac.setStatus("current")
_Hh3cDHCPSvrPoolMacMask_Type = MacAddress
_Hh3cDHCPSvrPoolMacMask_Object = MibTableColumn
hh3cDHCPSvrPoolMacMask = _Hh3cDHCPSvrPoolMacMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 10, 1, 2),
    _Hh3cDHCPSvrPoolMacMask_Type()
)
hh3cDHCPSvrPoolMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSvrPoolMacMask.setStatus("current")


class _Hh3cDHCPSvrPoolMacOptIndex_Type(Integer32):
    """Custom type hh3cDHCPSvrPoolMacOptIndex based on Integer32"""
    defaultValue = 0


_Hh3cDHCPSvrPoolMacOptIndex_Type.__name__ = "Integer32"
_Hh3cDHCPSvrPoolMacOptIndex_Object = MibTableColumn
hh3cDHCPSvrPoolMacOptIndex = _Hh3cDHCPSvrPoolMacOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 10, 1, 3),
    _Hh3cDHCPSvrPoolMacOptIndex_Type()
)
hh3cDHCPSvrPoolMacOptIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSvrPoolMacOptIndex.setStatus("current")
_Hh3cDHCPSvrPoolMacRowstatus_Type = RowStatus
_Hh3cDHCPSvrPoolMacRowstatus_Object = MibTableColumn
hh3cDHCPSvrPoolMacRowstatus = _Hh3cDHCPSvrPoolMacRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 10, 1, 4),
    _Hh3cDHCPSvrPoolMacRowstatus_Type()
)
hh3cDHCPSvrPoolMacRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSvrPoolMacRowstatus.setStatus("current")
_Hh3cDHCPServerTraps_ObjectIdentity = ObjectIdentity
hh3cDHCPServerTraps = _Hh3cDHCPServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3)
)
_Hh3cDHCPServerTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cDHCPServerTrapPrefix = _Hh3cDHCPServerTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0)
)
_Hh3cDHCPServerTrapObjects_ObjectIdentity = ObjectIdentity
hh3cDHCPServerTrapObjects = _Hh3cDHCPServerTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 1)
)
_Hh3cDHCPServerFirstTrapTime_Type = TimeTicks
_Hh3cDHCPServerFirstTrapTime_Object = MibScalar
hh3cDHCPServerFirstTrapTime = _Hh3cDHCPServerFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 1, 1),
    _Hh3cDHCPServerFirstTrapTime_Type()
)
hh3cDHCPServerFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDHCPServerFirstTrapTime.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cDHCPServerAddrExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 1)
)
hh3cDHCPServerAddrExhaust.setObjects(
      *(("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName"),
        ("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cDHCPServerAddrExhaust.setStatus(
        "current"
    )

hh3cDHCPServerAddrExhaustRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 2)
)
hh3cDHCPServerAddrExhaustRecover.setObjects(
      *(("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName"),
        ("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cDHCPServerAddrExhaustRecover.setStatus(
        "current"
    )

hh3cDHCPServerAvgIpUsageOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 3)
)
hh3cDHCPServerAvgIpUsageOverflow.setObjects(
    ("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName")
)
if mibBuilder.loadTexts:
    hh3cDHCPServerAvgIpUsageOverflow.setStatus(
        "current"
    )

hh3cDHCPServerMaxIpUsageOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 4)
)
hh3cDHCPServerMaxIpUsageOverflow.setObjects(
    ("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName")
)
if mibBuilder.loadTexts:
    hh3cDHCPServerMaxIpUsageOverflow.setStatus(
        "current"
    )

hh3cDHCPServerAllocateOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 5)
)
if mibBuilder.loadTexts:
    hh3cDHCPServerAllocateOverflow.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DHCP-SERVER-MIB",
    **{"hh3cDHCPServer": hh3cDHCPServer,
       "hh3cDHCPServerObjects": hh3cDHCPServerObjects,
       "hh3cDHCPServerIPPoolUsage": hh3cDHCPServerIPPoolUsage,
       "hh3cDHCPServerReqTimes": hh3cDHCPServerReqTimes,
       "hh3cDHCPServerReqSuccessTimes": hh3cDHCPServerReqSuccessTimes,
       "hh3cDHCPServerAvgIpUseThreshold": hh3cDHCPServerAvgIpUseThreshold,
       "hh3cDHCPServerMaxIpUseThreshold": hh3cDHCPServerMaxIpUseThreshold,
       "hh3cDHCPServerAllocateThreshold": hh3cDHCPServerAllocateThreshold,
       "hh3cDHCPServerTables": hh3cDHCPServerTables,
       "hh3cDHCPServerPoolName": hh3cDHCPServerPoolName,
       "hh3cDHCPSrvGlobalPoolTable": hh3cDHCPSrvGlobalPoolTable,
       "hh3cDHCPSrvGlobalPoolEntry": hh3cDHCPSrvGlobalPoolEntry,
       "hh3cDHCPSrvGlobalPoolName": hh3cDHCPSrvGlobalPoolName,
       "hh3cDHCPSrvGlobalPoolRowStatus": hh3cDHCPSrvGlobalPoolRowStatus,
       "hh3cDHCPSrvGlobalPoolConfigTable": hh3cDHCPSrvGlobalPoolConfigTable,
       "hh3cDHCPSrvGlobalPoolConfigEntry": hh3cDHCPSrvGlobalPoolConfigEntry,
       "hh3cDHCPSrvGlobalPoolType": hh3cDHCPSrvGlobalPoolType,
       "hh3cDHCPSrvGlobalPoolNetwork": hh3cDHCPSrvGlobalPoolNetwork,
       "hh3cDHCPSrvGlobalPoolNetworkMask": hh3cDHCPSrvGlobalPoolNetworkMask,
       "hh3cDHCPSrvGlobalPoolHostIPAddr": hh3cDHCPSrvGlobalPoolHostIPAddr,
       "hh3cDHCPSrvGlobalPoolHostMask": hh3cDHCPSrvGlobalPoolHostMask,
       "hh3cDHCPSrvGlobalPoolHostHAddr": hh3cDHCPSrvGlobalPoolHostHAddr,
       "hh3cDHCPSrvGlobalPoolCfgUndoFlag": hh3cDHCPSrvGlobalPoolCfgUndoFlag,
       "hh3cDHCPSrvGlobalPoolStartAddr": hh3cDHCPSrvGlobalPoolStartAddr,
       "hh3cDHCPSrvGlobalPoolEndAddr": hh3cDHCPSrvGlobalPoolEndAddr,
       "hh3cDHCPSrvGlobalPoolAllocObject": hh3cDHCPSrvGlobalPoolAllocObject,
       "hh3cDHCPSrvGlobalPoolParaTable": hh3cDHCPSrvGlobalPoolParaTable,
       "hh3cDHCPSrvGlobalPoolParaEntry": hh3cDHCPSrvGlobalPoolParaEntry,
       "hh3cDHCPSrvGlbPoolLeaseDay": hh3cDHCPSrvGlbPoolLeaseDay,
       "hh3cDHCPSrvGlbPoolLeaseHour": hh3cDHCPSrvGlbPoolLeaseHour,
       "hh3cDHCPSrvGlbPoolLeaseMinute": hh3cDHCPSrvGlbPoolLeaseMinute,
       "hh3cDHCPSrvGlbPoolLeaseUnlimited": hh3cDHCPSrvGlbPoolLeaseUnlimited,
       "hh3cDHCPSrvGlbPoolDomainName": hh3cDHCPSrvGlbPoolDomainName,
       "hh3cDHCPSrvGlbPoolCliGWIPStr": hh3cDHCPSrvGlbPoolCliGWIPStr,
       "hh3cDHCPSrvGlbPoolCliGWIPUndo": hh3cDHCPSrvGlbPoolCliGWIPUndo,
       "hh3cDHCPSrvGlbPoolCliDNSIPStr": hh3cDHCPSrvGlbPoolCliDNSIPStr,
       "hh3cDHCPSrvGlbPoolCliDNSIPUndo": hh3cDHCPSrvGlbPoolCliDNSIPUndo,
       "hh3cDHCPSrvGlbPoolCliNetbiosType": hh3cDHCPSrvGlbPoolCliNetbiosType,
       "hh3cDHCPSrvGlbPoolCliNbnsIPStr": hh3cDHCPSrvGlbPoolCliNbnsIPStr,
       "hh3cDHCPSrvGlbPoolCliNbnsIPUndo": hh3cDHCPSrvGlbPoolCliNbnsIPUndo,
       "hh3cDHCPSrvGlbPoolParaUndoFlag": hh3cDHCPSrvGlbPoolParaUndoFlag,
       "hh3cDHCPSrvGlbPoolIPInUseReset": hh3cDHCPSrvGlbPoolIPInUseReset,
       "hh3cDHCPSrvGlbPoolLeaseTime": hh3cDHCPSrvGlbPoolLeaseTime,
       "hh3cDHCPSrvGlbPoolPrimaryDNSIP": hh3cDHCPSrvGlbPoolPrimaryDNSIP,
       "hh3cDHCPSrvGlbPoolSecondaryDNSIP": hh3cDHCPSrvGlbPoolSecondaryDNSIP,
       "hh3cDHCPSrvGlbPoolLeaseSecond": hh3cDHCPSrvGlbPoolLeaseSecond,
       "hh3cDHCPSrvGlbPoolLeaseTimeSec": hh3cDHCPSrvGlbPoolLeaseTimeSec,
       "hh3cDHCPSrvGlbPoolCliGWIPAddr": hh3cDHCPSrvGlbPoolCliGWIPAddr,
       "hh3cDHCPSrvGlobalPoolOptionTable": hh3cDHCPSrvGlobalPoolOptionTable,
       "hh3cDHCPSrvGlobalPoolOptionEntry": hh3cDHCPSrvGlobalPoolOptionEntry,
       "hh3cDHCPSrvGlbPoolOptCode": hh3cDHCPSrvGlbPoolOptCode,
       "hh3cDHCPSrvGlbPoolOptType": hh3cDHCPSrvGlbPoolOptType,
       "hh3cDHCPSrvGlbPoolOptAscii": hh3cDHCPSrvGlbPoolOptAscii,
       "hh3cDHCPSrvGlbPoolOptHexString": hh3cDHCPSrvGlbPoolOptHexString,
       "hh3cDHCPSrvGlbPoolOptIPString": hh3cDHCPSrvGlbPoolOptIPString,
       "hh3cDHCPSrvGlbPoolOptRowStatus": hh3cDHCPSrvGlbPoolOptRowStatus,
       "hh3cDHCPSrvGlobalPoolStatTable": hh3cDHCPSrvGlobalPoolStatTable,
       "hh3cDHCPSrvGlobalPoolStatEntry": hh3cDHCPSrvGlobalPoolStatEntry,
       "hh3cDHCPSrvGlbPoolIPPoolUsage": hh3cDHCPSrvGlbPoolIPPoolUsage,
       "hh3cDHCPSrvGlbPoolReqTimes": hh3cDHCPSrvGlbPoolReqTimes,
       "hh3cDHCPSrvGlbPoolSuccessTimes": hh3cDHCPSrvGlbPoolSuccessTimes,
       "hh3cDHCPSrvGlbPoolDiscoverTimes": hh3cDHCPSrvGlbPoolDiscoverTimes,
       "hh3cDHCPSrvGlbPoolOfferTimes": hh3cDHCPSrvGlbPoolOfferTimes,
       "hh3cDHCPSrvGlbPoolACKTimes": hh3cDHCPSrvGlbPoolACKTimes,
       "hh3cDHCPSrvGlbPoolTotalIpNum": hh3cDHCPSrvGlbPoolTotalIpNum,
       "hh3cDHCPSrvGlbPoolInUsedIpNum": hh3cDHCPSrvGlbPoolInUsedIpNum,
       "hh3cDHCPSvrOptionGroupTable": hh3cDHCPSvrOptionGroupTable,
       "hh3cDHCPSvrOptionGroupEntry": hh3cDHCPSvrOptionGroupEntry,
       "hh3cDHCPSvrOptionGroupIndex": hh3cDHCPSvrOptionGroupIndex,
       "hh3cDHCPSvrOptionGroupRowstatus": hh3cDHCPSvrOptionGroupRowstatus,
       "hh3cDHCPSvrOptionTable": hh3cDHCPSvrOptionTable,
       "hh3cDHCPSvrOptionEntry": hh3cDHCPSvrOptionEntry,
       "hh3cDHCPSvrOptionCode": hh3cDHCPSvrOptionCode,
       "hh3cDHCPSvrOptionType": hh3cDHCPSvrOptionType,
       "hh3cDHCPSvrOptionAsciiString": hh3cDHCPSvrOptionAsciiString,
       "hh3cDHCPSvrOptionHexString": hh3cDHCPSvrOptionHexString,
       "hh3cDHCPSvrOptionIPString": hh3cDHCPSvrOptionIPString,
       "hh3cDHCPSvrOptionRowstatus": hh3cDHCPSvrOptionRowstatus,
       "hh3cDHCPSvrVerifyMacTable": hh3cDHCPSvrVerifyMacTable,
       "hh3cDHCPSvrVerifyMacEntry": hh3cDHCPSvrVerifyMacEntry,
       "hh3cDHCPSvrVerifyMacSwitch": hh3cDHCPSvrVerifyMacSwitch,
       "hh3cDHCPSvrPoolMacTable": hh3cDHCPSvrPoolMacTable,
       "hh3cDHCPSvrPoolMacEntry": hh3cDHCPSvrPoolMacEntry,
       "hh3cDHCPSvrPoolMac": hh3cDHCPSvrPoolMac,
       "hh3cDHCPSvrPoolMacMask": hh3cDHCPSvrPoolMacMask,
       "hh3cDHCPSvrPoolMacOptIndex": hh3cDHCPSvrPoolMacOptIndex,
       "hh3cDHCPSvrPoolMacRowstatus": hh3cDHCPSvrPoolMacRowstatus,
       "hh3cDHCPServerTraps": hh3cDHCPServerTraps,
       "hh3cDHCPServerTrapPrefix": hh3cDHCPServerTrapPrefix,
       "hh3cDHCPServerAddrExhaust": hh3cDHCPServerAddrExhaust,
       "hh3cDHCPServerAddrExhaustRecover": hh3cDHCPServerAddrExhaustRecover,
       "hh3cDHCPServerAvgIpUsageOverflow": hh3cDHCPServerAvgIpUsageOverflow,
       "hh3cDHCPServerMaxIpUsageOverflow": hh3cDHCPServerMaxIpUsageOverflow,
       "hh3cDHCPServerAllocateOverflow": hh3cDHCPServerAllocateOverflow,
       "hh3cDHCPServerTrapObjects": hh3cDHCPServerTrapObjects,
       "hh3cDHCPServerFirstTrapTime": hh3cDHCPServerFirstTrapTime}
)
