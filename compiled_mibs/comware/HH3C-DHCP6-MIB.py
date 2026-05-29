# SNMP MIB module (HH3C-DHCP6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-DHCP6-MIB

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

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cDhcp6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179)
)
if mibBuilder.loadTexts:
    hh3cDhcp6.setRevisions(
        ("2021-04-30 00:00",
         "2021-02-08 00:00",
         "2019-12-12 00:00",
         "2018-11-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDhcp6Server2Tables_ObjectIdentity = ObjectIdentity
hh3cDhcp6Server2Tables = _Hh3cDhcp6Server2Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1)
)
_Hh3cDhcp6Server2PoolTable_Object = MibTable
hh3cDhcp6Server2PoolTable = _Hh3cDhcp6Server2PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolTable.setStatus("current")
_Hh3cDhcp6Server2PoolEntry_Object = MibTableRow
hh3cDhcp6Server2PoolEntry = _Hh3cDhcp6Server2PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1)
)
hh3cDhcp6Server2PoolEntry.setIndexNames(
    (0, "HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolEntry.setStatus("current")


class _Hh3cDhcp6Server2PoolIndex_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cDhcp6Server2PoolIndex_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolIndex_Object = MibTableColumn
hh3cDhcp6Server2PoolIndex = _Hh3cDhcp6Server2PoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 1),
    _Hh3cDhcp6Server2PoolIndex_Type()
)
hh3cDhcp6Server2PoolIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolIndex.setStatus("current")


class _Hh3cDhcp6Server2PoolName_Type(OctetString):
    """Custom type hh3cDhcp6Server2PoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDhcp6Server2PoolName_Type.__name__ = "OctetString"
_Hh3cDhcp6Server2PoolName_Object = MibTableColumn
hh3cDhcp6Server2PoolName = _Hh3cDhcp6Server2PoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 2),
    _Hh3cDhcp6Server2PoolName_Type()
)
hh3cDhcp6Server2PoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolName.setStatus("current")
_Hh3cDhcp6Server2PoolRowStatus_Type = RowStatus
_Hh3cDhcp6Server2PoolRowStatus_Object = MibTableColumn
hh3cDhcp6Server2PoolRowStatus = _Hh3cDhcp6Server2PoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 3),
    _Hh3cDhcp6Server2PoolRowStatus_Type()
)
hh3cDhcp6Server2PoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolRowStatus.setStatus("current")


class _Hh3cDhcp6Server2PoolVpnName_Type(OctetString):
    """Custom type hh3cDhcp6Server2PoolVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cDhcp6Server2PoolVpnName_Type.__name__ = "OctetString"
_Hh3cDhcp6Server2PoolVpnName_Object = MibTableColumn
hh3cDhcp6Server2PoolVpnName = _Hh3cDhcp6Server2PoolVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 4),
    _Hh3cDhcp6Server2PoolVpnName_Type()
)
hh3cDhcp6Server2PoolVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolVpnName.setStatus("current")


class _Hh3cDhcp6Server2PoolType_Type(Integer32):
    """Custom type hh3cDhcp6Server2PoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("basLocal", 6),
          ("basRemote", 7),
          ("odap", 9))
    )


_Hh3cDhcp6Server2PoolType_Type.__name__ = "Integer32"
_Hh3cDhcp6Server2PoolType_Object = MibTableColumn
hh3cDhcp6Server2PoolType = _Hh3cDhcp6Server2PoolType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 5),
    _Hh3cDhcp6Server2PoolType_Type()
)
hh3cDhcp6Server2PoolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolType.setStatus("current")
_Hh3cDhcp6Server2PoolNetwork_Type = InetAddressIPv6
_Hh3cDhcp6Server2PoolNetwork_Object = MibTableColumn
hh3cDhcp6Server2PoolNetwork = _Hh3cDhcp6Server2PoolNetwork_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 6),
    _Hh3cDhcp6Server2PoolNetwork_Type()
)
hh3cDhcp6Server2PoolNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolNetwork.setStatus("current")


class _Hh3cDhcp6Server2PoolNetworkMask_Type(Integer32):
    """Custom type hh3cDhcp6Server2PoolNetworkMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Hh3cDhcp6Server2PoolNetworkMask_Type.__name__ = "Integer32"
_Hh3cDhcp6Server2PoolNetworkMask_Object = MibTableColumn
hh3cDhcp6Server2PoolNetworkMask = _Hh3cDhcp6Server2PoolNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 7),
    _Hh3cDhcp6Server2PoolNetworkMask_Type()
)
hh3cDhcp6Server2PoolNetworkMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolNetworkMask.setStatus("current")


class _Hh3cDhcp6Server2PoolNetworkPdNum_Type(Integer32):
    """Custom type hh3cDhcp6Server2PoolNetworkPdNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Hh3cDhcp6Server2PoolNetworkPdNum_Type.__name__ = "Integer32"
_Hh3cDhcp6Server2PoolNetworkPdNum_Object = MibTableColumn
hh3cDhcp6Server2PoolNetworkPdNum = _Hh3cDhcp6Server2PoolNetworkPdNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 8),
    _Hh3cDhcp6Server2PoolNetworkPdNum_Type()
)
hh3cDhcp6Server2PoolNetworkPdNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolNetworkPdNum.setStatus("current")
_Hh3cDhcp6Server2PoolSubPdAddr_Type = InetAddressIPv6
_Hh3cDhcp6Server2PoolSubPdAddr_Object = MibTableColumn
hh3cDhcp6Server2PoolSubPdAddr = _Hh3cDhcp6Server2PoolSubPdAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 9),
    _Hh3cDhcp6Server2PoolSubPdAddr_Type()
)
hh3cDhcp6Server2PoolSubPdAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolSubPdAddr.setStatus("current")


class _Hh3cDhcp6Server2PoolSubPdLength_Type(Integer32):
    """Custom type hh3cDhcp6Server2PoolSubPdLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Hh3cDhcp6Server2PoolSubPdLength_Type.__name__ = "Integer32"
_Hh3cDhcp6Server2PoolSubPdLength_Object = MibTableColumn
hh3cDhcp6Server2PoolSubPdLength = _Hh3cDhcp6Server2PoolSubPdLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 10),
    _Hh3cDhcp6Server2PoolSubPdLength_Type()
)
hh3cDhcp6Server2PoolSubPdLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolSubPdLength.setStatus("current")


class _Hh3cDhcp6Server2PoolNetPreTime_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolNetPreTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 4294967295),
    )


_Hh3cDhcp6Server2PoolNetPreTime_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolNetPreTime_Object = MibTableColumn
hh3cDhcp6Server2PoolNetPreTime = _Hh3cDhcp6Server2PoolNetPreTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 11),
    _Hh3cDhcp6Server2PoolNetPreTime_Type()
)
hh3cDhcp6Server2PoolNetPreTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolNetPreTime.setStatus("current")


class _Hh3cDhcp6Server2PoolNetValTime_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolNetValTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 4294967295),
    )


_Hh3cDhcp6Server2PoolNetValTime_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolNetValTime_Object = MibTableColumn
hh3cDhcp6Server2PoolNetValTime = _Hh3cDhcp6Server2PoolNetValTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 12),
    _Hh3cDhcp6Server2PoolNetValTime_Type()
)
hh3cDhcp6Server2PoolNetValTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolNetValTime.setStatus("current")
_Hh3cDhcp6Server2PoolNetExport_Type = TruthValue
_Hh3cDhcp6Server2PoolNetExport_Object = MibTableColumn
hh3cDhcp6Server2PoolNetExport = _Hh3cDhcp6Server2PoolNetExport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 13),
    _Hh3cDhcp6Server2PoolNetExport_Type()
)
hh3cDhcp6Server2PoolNetExport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolNetExport.setStatus("current")


class _Hh3cDhcp6Server2PoolNetPrefer_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolNetPrefer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cDhcp6Server2PoolNetPrefer_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolNetPrefer_Object = MibTableColumn
hh3cDhcp6Server2PoolNetPrefer = _Hh3cDhcp6Server2PoolNetPrefer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 14),
    _Hh3cDhcp6Server2PoolNetPrefer_Type()
)
hh3cDhcp6Server2PoolNetPrefer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolNetPrefer.setStatus("current")


class _Hh3cDhcp6Server2PoolNetTag_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolNetTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cDhcp6Server2PoolNetTag_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolNetTag_Object = MibTableColumn
hh3cDhcp6Server2PoolNetTag = _Hh3cDhcp6Server2PoolNetTag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 15),
    _Hh3cDhcp6Server2PoolNetTag_Type()
)
hh3cDhcp6Server2PoolNetTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolNetTag.setStatus("current")
_Hh3cDhcp6Server2PoolNaStartAddr_Type = InetAddressIPv6
_Hh3cDhcp6Server2PoolNaStartAddr_Object = MibTableColumn
hh3cDhcp6Server2PoolNaStartAddr = _Hh3cDhcp6Server2PoolNaStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 16),
    _Hh3cDhcp6Server2PoolNaStartAddr_Type()
)
hh3cDhcp6Server2PoolNaStartAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolNaStartAddr.setStatus("current")
_Hh3cDhcp6Server2PoolNaEndAddr_Type = InetAddressIPv6
_Hh3cDhcp6Server2PoolNaEndAddr_Object = MibTableColumn
hh3cDhcp6Server2PoolNaEndAddr = _Hh3cDhcp6Server2PoolNaEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 17),
    _Hh3cDhcp6Server2PoolNaEndAddr_Type()
)
hh3cDhcp6Server2PoolNaEndAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolNaEndAddr.setStatus("current")


class _Hh3cDhcp6Server2PoolNaPreTime_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolNaPreTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 4294967295),
    )


_Hh3cDhcp6Server2PoolNaPreTime_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolNaPreTime_Object = MibTableColumn
hh3cDhcp6Server2PoolNaPreTime = _Hh3cDhcp6Server2PoolNaPreTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 18),
    _Hh3cDhcp6Server2PoolNaPreTime_Type()
)
hh3cDhcp6Server2PoolNaPreTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolNaPreTime.setStatus("current")


class _Hh3cDhcp6Server2PoolNaValTime_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolNaValTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 4294967295),
    )


_Hh3cDhcp6Server2PoolNaValTime_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolNaValTime_Object = MibTableColumn
hh3cDhcp6Server2PoolNaValTime = _Hh3cDhcp6Server2PoolNaValTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 19),
    _Hh3cDhcp6Server2PoolNaValTime_Type()
)
hh3cDhcp6Server2PoolNaValTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolNaValTime.setStatus("current")
_Hh3cDhcp6Server2PoolTaStartAddr_Type = InetAddressIPv6
_Hh3cDhcp6Server2PoolTaStartAddr_Object = MibTableColumn
hh3cDhcp6Server2PoolTaStartAddr = _Hh3cDhcp6Server2PoolTaStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 20),
    _Hh3cDhcp6Server2PoolTaStartAddr_Type()
)
hh3cDhcp6Server2PoolTaStartAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolTaStartAddr.setStatus("current")
_Hh3cDhcp6Server2PoolTaEndAddr_Type = InetAddressIPv6
_Hh3cDhcp6Server2PoolTaEndAddr_Object = MibTableColumn
hh3cDhcp6Server2PoolTaEndAddr = _Hh3cDhcp6Server2PoolTaEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 21),
    _Hh3cDhcp6Server2PoolTaEndAddr_Type()
)
hh3cDhcp6Server2PoolTaEndAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolTaEndAddr.setStatus("current")


class _Hh3cDhcp6Server2PoolTaPreTime_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolTaPreTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 4294967295),
    )


_Hh3cDhcp6Server2PoolTaPreTime_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolTaPreTime_Object = MibTableColumn
hh3cDhcp6Server2PoolTaPreTime = _Hh3cDhcp6Server2PoolTaPreTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 22),
    _Hh3cDhcp6Server2PoolTaPreTime_Type()
)
hh3cDhcp6Server2PoolTaPreTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolTaPreTime.setStatus("current")


class _Hh3cDhcp6Server2PoolTaValTime_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolTaValTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 4294967295),
    )


_Hh3cDhcp6Server2PoolTaValTime_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolTaValTime_Object = MibTableColumn
hh3cDhcp6Server2PoolTaValTime = _Hh3cDhcp6Server2PoolTaValTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 23),
    _Hh3cDhcp6Server2PoolTaValTime_Type()
)
hh3cDhcp6Server2PoolTaValTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolTaValTime.setStatus("current")


class _Hh3cDhcp6Server2PoolPrefixPool_Type(Integer32):
    """Custom type hh3cDhcp6Server2PoolPrefixPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Hh3cDhcp6Server2PoolPrefixPool_Type.__name__ = "Integer32"
_Hh3cDhcp6Server2PoolPrefixPool_Object = MibTableColumn
hh3cDhcp6Server2PoolPrefixPool = _Hh3cDhcp6Server2PoolPrefixPool_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 24),
    _Hh3cDhcp6Server2PoolPrefixPool_Type()
)
hh3cDhcp6Server2PoolPrefixPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPrefixPool.setStatus("current")


class _Hh3cDhcp6Server2PoolPdPreTime_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolPdPreTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 4294967295),
    )


_Hh3cDhcp6Server2PoolPdPreTime_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolPdPreTime_Object = MibTableColumn
hh3cDhcp6Server2PoolPdPreTime = _Hh3cDhcp6Server2PoolPdPreTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 25),
    _Hh3cDhcp6Server2PoolPdPreTime_Type()
)
hh3cDhcp6Server2PoolPdPreTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPdPreTime.setStatus("current")


class _Hh3cDhcp6Server2PoolPdValTime_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolPdValTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 4294967295),
    )


_Hh3cDhcp6Server2PoolPdValTime_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolPdValTime_Object = MibTableColumn
hh3cDhcp6Server2PoolPdValTime = _Hh3cDhcp6Server2PoolPdValTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 26),
    _Hh3cDhcp6Server2PoolPdValTime_Type()
)
hh3cDhcp6Server2PoolPdValTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPdValTime.setStatus("current")
_Hh3cDhcp6Server2PoolPdExport_Type = TruthValue
_Hh3cDhcp6Server2PoolPdExport_Object = MibTableColumn
hh3cDhcp6Server2PoolPdExport = _Hh3cDhcp6Server2PoolPdExport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 27),
    _Hh3cDhcp6Server2PoolPdExport_Type()
)
hh3cDhcp6Server2PoolPdExport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPdExport.setStatus("current")


class _Hh3cDhcp6Server2PoolPdPreference_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolPdPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cDhcp6Server2PoolPdPreference_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolPdPreference_Object = MibTableColumn
hh3cDhcp6Server2PoolPdPreference = _Hh3cDhcp6Server2PoolPdPreference_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 28),
    _Hh3cDhcp6Server2PoolPdPreference_Type()
)
hh3cDhcp6Server2PoolPdPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPdPreference.setStatus("current")


class _Hh3cDhcp6Server2PoolPdTag_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolPdTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cDhcp6Server2PoolPdTag_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolPdTag_Object = MibTableColumn
hh3cDhcp6Server2PoolPdTag = _Hh3cDhcp6Server2PoolPdTag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 29),
    _Hh3cDhcp6Server2PoolPdTag_Type()
)
hh3cDhcp6Server2PoolPdTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPdTag.setStatus("current")


class _Hh3cDhcp6Server2PoolDomainName_Type(OctetString):
    """Custom type hh3cDhcp6Server2PoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_Hh3cDhcp6Server2PoolDomainName_Type.__name__ = "OctetString"
_Hh3cDhcp6Server2PoolDomainName_Object = MibTableColumn
hh3cDhcp6Server2PoolDomainName = _Hh3cDhcp6Server2PoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 30),
    _Hh3cDhcp6Server2PoolDomainName_Type()
)
hh3cDhcp6Server2PoolDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolDomainName.setStatus("current")


class _Hh3cDhcp6Server2PoolGatewayIp_Type(OctetString):
    """Custom type hh3cDhcp6Server2PoolGatewayIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 367),
    )


_Hh3cDhcp6Server2PoolGatewayIp_Type.__name__ = "OctetString"
_Hh3cDhcp6Server2PoolGatewayIp_Object = MibTableColumn
hh3cDhcp6Server2PoolGatewayIp = _Hh3cDhcp6Server2PoolGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 31),
    _Hh3cDhcp6Server2PoolGatewayIp_Type()
)
hh3cDhcp6Server2PoolGatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGatewayIp.setStatus("current")


class _Hh3cDhcp6Server2PoolDNSIp_Type(OctetString):
    """Custom type hh3cDhcp6Server2PoolDNSIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 367),
    )


_Hh3cDhcp6Server2PoolDNSIp_Type.__name__ = "OctetString"
_Hh3cDhcp6Server2PoolDNSIp_Object = MibTableColumn
hh3cDhcp6Server2PoolDNSIp = _Hh3cDhcp6Server2PoolDNSIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 32),
    _Hh3cDhcp6Server2PoolDNSIp_Type()
)
hh3cDhcp6Server2PoolDNSIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolDNSIp.setStatus("current")
_Hh3cDhcp6Server2PoolExpireIpEnbl_Type = TruthValue
_Hh3cDhcp6Server2PoolExpireIpEnbl_Object = MibTableColumn
hh3cDhcp6Server2PoolExpireIpEnbl = _Hh3cDhcp6Server2PoolExpireIpEnbl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 33),
    _Hh3cDhcp6Server2PoolExpireIpEnbl_Type()
)
hh3cDhcp6Server2PoolExpireIpEnbl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolExpireIpEnbl.setStatus("current")


class _Hh3cDhcp6Server2PoolExpireIpMode_Type(Integer32):
    """Custom type hh3cDhcp6Server2PoolExpireIpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cid", 0),
          ("mac", 1))
    )


_Hh3cDhcp6Server2PoolExpireIpMode_Type.__name__ = "Integer32"
_Hh3cDhcp6Server2PoolExpireIpMode_Object = MibTableColumn
hh3cDhcp6Server2PoolExpireIpMode = _Hh3cDhcp6Server2PoolExpireIpMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 34),
    _Hh3cDhcp6Server2PoolExpireIpMode_Type()
)
hh3cDhcp6Server2PoolExpireIpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolExpireIpMode.setStatus("current")


class _Hh3cDhcp6Server2PoolExpireIpLim_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolExpireIpLim based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256000),
    )


_Hh3cDhcp6Server2PoolExpireIpLim_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolExpireIpLim_Object = MibTableColumn
hh3cDhcp6Server2PoolExpireIpLim = _Hh3cDhcp6Server2PoolExpireIpLim_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 35),
    _Hh3cDhcp6Server2PoolExpireIpLim_Type()
)
hh3cDhcp6Server2PoolExpireIpLim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolExpireIpLim.setStatus("current")


class _Hh3cDhcp6Server2PoolExpireIpTime_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolExpireIpTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_Hh3cDhcp6Server2PoolExpireIpTime_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolExpireIpTime_Object = MibTableColumn
hh3cDhcp6Server2PoolExpireIpTime = _Hh3cDhcp6Server2PoolExpireIpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 36),
    _Hh3cDhcp6Server2PoolExpireIpTime_Type()
)
hh3cDhcp6Server2PoolExpireIpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolExpireIpTime.setStatus("current")
_Hh3cDhcp6Server2PoolExpirePdEnbl_Type = TruthValue
_Hh3cDhcp6Server2PoolExpirePdEnbl_Object = MibTableColumn
hh3cDhcp6Server2PoolExpirePdEnbl = _Hh3cDhcp6Server2PoolExpirePdEnbl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 37),
    _Hh3cDhcp6Server2PoolExpirePdEnbl_Type()
)
hh3cDhcp6Server2PoolExpirePdEnbl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolExpirePdEnbl.setStatus("current")


class _Hh3cDhcp6Server2PoolExpirePdMode_Type(Integer32):
    """Custom type hh3cDhcp6Server2PoolExpirePdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cid", 0),
          ("mac", 1))
    )


_Hh3cDhcp6Server2PoolExpirePdMode_Type.__name__ = "Integer32"
_Hh3cDhcp6Server2PoolExpirePdMode_Object = MibTableColumn
hh3cDhcp6Server2PoolExpirePdMode = _Hh3cDhcp6Server2PoolExpirePdMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 38),
    _Hh3cDhcp6Server2PoolExpirePdMode_Type()
)
hh3cDhcp6Server2PoolExpirePdMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolExpirePdMode.setStatus("current")


class _Hh3cDhcp6Server2PoolExpirePdLim_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolExpirePdLim based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256000),
    )


_Hh3cDhcp6Server2PoolExpirePdLim_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolExpirePdLim_Object = MibTableColumn
hh3cDhcp6Server2PoolExpirePdLim = _Hh3cDhcp6Server2PoolExpirePdLim_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 39),
    _Hh3cDhcp6Server2PoolExpirePdLim_Type()
)
hh3cDhcp6Server2PoolExpirePdLim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolExpirePdLim.setStatus("current")


class _Hh3cDhcp6Server2PoolExpirePdTime_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolExpirePdTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_Hh3cDhcp6Server2PoolExpirePdTime_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolExpirePdTime_Object = MibTableColumn
hh3cDhcp6Server2PoolExpirePdTime = _Hh3cDhcp6Server2PoolExpirePdTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 1, 1, 40),
    _Hh3cDhcp6Server2PoolExpirePdTime_Type()
)
hh3cDhcp6Server2PoolExpirePdTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolExpirePdTime.setStatus("current")
_Hh3cDhcp6Server2PoolStatTable_Object = MibTable
hh3cDhcp6Server2PoolStatTable = _Hh3cDhcp6Server2PoolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolStatTable.setStatus("current")
_Hh3cDhcp6Server2PoolStatEntry_Object = MibTableRow
hh3cDhcp6Server2PoolStatEntry = _Hh3cDhcp6Server2PoolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1)
)
hh3cDhcp6Server2PoolStatEntry.setIndexNames(
    (0, "HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolStatEntry.setStatus("current")
_Hh3cDhcp6Server2PoolIPIdleNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolIPIdleNum_Object = MibTableColumn
hh3cDhcp6Server2PoolIPIdleNum = _Hh3cDhcp6Server2PoolIPIdleNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 1),
    _Hh3cDhcp6Server2PoolIPIdleNum_Type()
)
hh3cDhcp6Server2PoolIPIdleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolIPIdleNum.setStatus("current")
_Hh3cDhcp6Server2PoolIPUsedNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolIPUsedNum_Object = MibTableColumn
hh3cDhcp6Server2PoolIPUsedNum = _Hh3cDhcp6Server2PoolIPUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 2),
    _Hh3cDhcp6Server2PoolIPUsedNum_Type()
)
hh3cDhcp6Server2PoolIPUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolIPUsedNum.setStatus("current")
_Hh3cDhcp6Server2PoolPrefixIdleNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolPrefixIdleNum_Object = MibTableColumn
hh3cDhcp6Server2PoolPrefixIdleNum = _Hh3cDhcp6Server2PoolPrefixIdleNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 3),
    _Hh3cDhcp6Server2PoolPrefixIdleNum_Type()
)
hh3cDhcp6Server2PoolPrefixIdleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPrefixIdleNum.setStatus("current")
_Hh3cDhcp6Server2PoolPrefixUsedNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolPrefixUsedNum_Object = MibTableColumn
hh3cDhcp6Server2PoolPrefixUsedNum = _Hh3cDhcp6Server2PoolPrefixUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 4),
    _Hh3cDhcp6Server2PoolPrefixUsedNum_Type()
)
hh3cDhcp6Server2PoolPrefixUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPrefixUsedNum.setStatus("current")


class _Hh3cDhcp6Server2PoolIPTotalNum_Type(OctetString):
    """Custom type hh3cDhcp6Server2PoolIPTotalNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_Hh3cDhcp6Server2PoolIPTotalNum_Type.__name__ = "OctetString"
_Hh3cDhcp6Server2PoolIPTotalNum_Object = MibTableColumn
hh3cDhcp6Server2PoolIPTotalNum = _Hh3cDhcp6Server2PoolIPTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 5),
    _Hh3cDhcp6Server2PoolIPTotalNum_Type()
)
hh3cDhcp6Server2PoolIPTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolIPTotalNum.setStatus("current")
_Hh3cDhcp6Server2PoolIPExpiredNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolIPExpiredNum_Object = MibTableColumn
hh3cDhcp6Server2PoolIPExpiredNum = _Hh3cDhcp6Server2PoolIPExpiredNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 6),
    _Hh3cDhcp6Server2PoolIPExpiredNum_Type()
)
hh3cDhcp6Server2PoolIPExpiredNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolIPExpiredNum.setStatus("current")
_Hh3cDhcp6Server2PoolIPDynamicUsedNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolIPDynamicUsedNum_Object = MibTableColumn
hh3cDhcp6Server2PoolIPDynamicUsedNum = _Hh3cDhcp6Server2PoolIPDynamicUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 7),
    _Hh3cDhcp6Server2PoolIPDynamicUsedNum_Type()
)
hh3cDhcp6Server2PoolIPDynamicUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolIPDynamicUsedNum.setStatus("current")
_Hh3cDhcp6Server2PoolIPStaticUsedNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolIPStaticUsedNum_Object = MibTableColumn
hh3cDhcp6Server2PoolIPStaticUsedNum = _Hh3cDhcp6Server2PoolIPStaticUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 8),
    _Hh3cDhcp6Server2PoolIPStaticUsedNum_Type()
)
hh3cDhcp6Server2PoolIPStaticUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolIPStaticUsedNum.setStatus("current")
_Hh3cDhcp6Server2PoolIPConflictNum_Type = Counter64
_Hh3cDhcp6Server2PoolIPConflictNum_Object = MibTableColumn
hh3cDhcp6Server2PoolIPConflictNum = _Hh3cDhcp6Server2PoolIPConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 9),
    _Hh3cDhcp6Server2PoolIPConflictNum_Type()
)
hh3cDhcp6Server2PoolIPConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolIPConflictNum.setStatus("current")
_Hh3cDhcp6Server2PoolIPExcludeNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolIPExcludeNum_Object = MibTableColumn
hh3cDhcp6Server2PoolIPExcludeNum = _Hh3cDhcp6Server2PoolIPExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 10),
    _Hh3cDhcp6Server2PoolIPExcludeNum_Type()
)
hh3cDhcp6Server2PoolIPExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolIPExcludeNum.setStatus("current")
_Hh3cDhcp6Server2PoolIPReserveNum_Type = Counter64
_Hh3cDhcp6Server2PoolIPReserveNum_Object = MibTableColumn
hh3cDhcp6Server2PoolIPReserveNum = _Hh3cDhcp6Server2PoolIPReserveNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 11),
    _Hh3cDhcp6Server2PoolIPReserveNum_Type()
)
hh3cDhcp6Server2PoolIPReserveNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolIPReserveNum.setStatus("current")
_Hh3cDhcp6Server2PoolIPUsage_Type = Unsigned32
_Hh3cDhcp6Server2PoolIPUsage_Object = MibTableColumn
hh3cDhcp6Server2PoolIPUsage = _Hh3cDhcp6Server2PoolIPUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 12),
    _Hh3cDhcp6Server2PoolIPUsage_Type()
)
hh3cDhcp6Server2PoolIPUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolIPUsage.setStatus("current")


class _Hh3cDhcp6Server2PoolPdTotalNum_Type(OctetString):
    """Custom type hh3cDhcp6Server2PoolPdTotalNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_Hh3cDhcp6Server2PoolPdTotalNum_Type.__name__ = "OctetString"
_Hh3cDhcp6Server2PoolPdTotalNum_Object = MibTableColumn
hh3cDhcp6Server2PoolPdTotalNum = _Hh3cDhcp6Server2PoolPdTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 13),
    _Hh3cDhcp6Server2PoolPdTotalNum_Type()
)
hh3cDhcp6Server2PoolPdTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPdTotalNum.setStatus("current")
_Hh3cDhcp6Server2PoolPdExpiredNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolPdExpiredNum_Object = MibTableColumn
hh3cDhcp6Server2PoolPdExpiredNum = _Hh3cDhcp6Server2PoolPdExpiredNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 14),
    _Hh3cDhcp6Server2PoolPdExpiredNum_Type()
)
hh3cDhcp6Server2PoolPdExpiredNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPdExpiredNum.setStatus("current")
_Hh3cDhcp6Server2PoolPdDynamicUsedNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolPdDynamicUsedNum_Object = MibTableColumn
hh3cDhcp6Server2PoolPdDynamicUsedNum = _Hh3cDhcp6Server2PoolPdDynamicUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 15),
    _Hh3cDhcp6Server2PoolPdDynamicUsedNum_Type()
)
hh3cDhcp6Server2PoolPdDynamicUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPdDynamicUsedNum.setStatus("current")
_Hh3cDhcp6Server2PoolPdStaticUsedNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolPdStaticUsedNum_Object = MibTableColumn
hh3cDhcp6Server2PoolPdStaticUsedNum = _Hh3cDhcp6Server2PoolPdStaticUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 16),
    _Hh3cDhcp6Server2PoolPdStaticUsedNum_Type()
)
hh3cDhcp6Server2PoolPdStaticUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPdStaticUsedNum.setStatus("current")
_Hh3cDhcp6Server2PoolPdConflictNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolPdConflictNum_Object = MibTableColumn
hh3cDhcp6Server2PoolPdConflictNum = _Hh3cDhcp6Server2PoolPdConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 17),
    _Hh3cDhcp6Server2PoolPdConflictNum_Type()
)
hh3cDhcp6Server2PoolPdConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPdConflictNum.setStatus("current")
_Hh3cDhcp6Server2PoolPdExcludeNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolPdExcludeNum_Object = MibTableColumn
hh3cDhcp6Server2PoolPdExcludeNum = _Hh3cDhcp6Server2PoolPdExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 18),
    _Hh3cDhcp6Server2PoolPdExcludeNum_Type()
)
hh3cDhcp6Server2PoolPdExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPdExcludeNum.setStatus("current")
_Hh3cDhcp6Server2PoolPdReserveNum_Type = Counter64
_Hh3cDhcp6Server2PoolPdReserveNum_Object = MibTableColumn
hh3cDhcp6Server2PoolPdReserveNum = _Hh3cDhcp6Server2PoolPdReserveNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 19),
    _Hh3cDhcp6Server2PoolPdReserveNum_Type()
)
hh3cDhcp6Server2PoolPdReserveNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPdReserveNum.setStatus("current")
_Hh3cDhcp6Server2PoolPdUsage_Type = Unsigned32
_Hh3cDhcp6Server2PoolPdUsage_Object = MibTableColumn
hh3cDhcp6Server2PoolPdUsage = _Hh3cDhcp6Server2PoolPdUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 2, 1, 20),
    _Hh3cDhcp6Server2PoolPdUsage_Type()
)
hh3cDhcp6Server2PoolPdUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolPdUsage.setStatus("current")
_Hh3cDhcp6Server2PoolGpTable_Object = MibTable
hh3cDhcp6Server2PoolGpTable = _Hh3cDhcp6Server2PoolGpTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpTable.setStatus("current")
_Hh3cDhcp6Server2PoolGpEntry_Object = MibTableRow
hh3cDhcp6Server2PoolGpEntry = _Hh3cDhcp6Server2PoolGpEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 3, 1)
)
hh3cDhcp6Server2PoolGpEntry.setIndexNames(
    (0, "HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolGpName"),
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpEntry.setStatus("current")


class _Hh3cDhcp6Server2PoolGpName_Type(OctetString):
    """Custom type hh3cDhcp6Server2PoolGpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDhcp6Server2PoolGpName_Type.__name__ = "OctetString"
_Hh3cDhcp6Server2PoolGpName_Object = MibTableColumn
hh3cDhcp6Server2PoolGpName = _Hh3cDhcp6Server2PoolGpName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 3, 1, 1),
    _Hh3cDhcp6Server2PoolGpName_Type()
)
hh3cDhcp6Server2PoolGpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpName.setStatus("current")


class _Hh3cDhcp6Server2PoolGpVpnName_Type(OctetString):
    """Custom type hh3cDhcp6Server2PoolGpVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cDhcp6Server2PoolGpVpnName_Type.__name__ = "OctetString"
_Hh3cDhcp6Server2PoolGpVpnName_Object = MibTableColumn
hh3cDhcp6Server2PoolGpVpnName = _Hh3cDhcp6Server2PoolGpVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 3, 1, 2),
    _Hh3cDhcp6Server2PoolGpVpnName_Type()
)
hh3cDhcp6Server2PoolGpVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpVpnName.setStatus("current")


class _Hh3cDhcp6Server2PoolGpIncUndo_Type(TruthValue):
    """Custom type hh3cDhcp6Server2PoolGpIncUndo based on TruthValue"""
    defaultValue = 2


_Hh3cDhcp6Server2PoolGpIncUndo_Type.__name__ = "TruthValue"
_Hh3cDhcp6Server2PoolGpIncUndo_Object = MibTableColumn
hh3cDhcp6Server2PoolGpIncUndo = _Hh3cDhcp6Server2PoolGpIncUndo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 3, 1, 3),
    _Hh3cDhcp6Server2PoolGpIncUndo_Type()
)
hh3cDhcp6Server2PoolGpIncUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpIncUndo.setStatus("current")
_Hh3cDhcp6Server2PoolGpRowSta_Type = RowStatus
_Hh3cDhcp6Server2PoolGpRowSta_Object = MibTableColumn
hh3cDhcp6Server2PoolGpRowSta = _Hh3cDhcp6Server2PoolGpRowSta_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 3, 1, 4),
    _Hh3cDhcp6Server2PoolGpRowSta_Type()
)
hh3cDhcp6Server2PoolGpRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpRowSta.setStatus("current")
_Hh3cDhcp6Server2PoolGpExtTable_Object = MibTable
hh3cDhcp6Server2PoolGpExtTable = _Hh3cDhcp6Server2PoolGpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpExtTable.setStatus("current")
_Hh3cDhcp6Server2PoolGpExtEntry_Object = MibTableRow
hh3cDhcp6Server2PoolGpExtEntry = _Hh3cDhcp6Server2PoolGpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 4, 1)
)
hh3cDhcp6Server2PoolGpExtEntry.setIndexNames(
    (0, "HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolGpName"),
    (0, "HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpExtEntry.setStatus("current")


class _Hh3cDhcp6Server2PoolGpIncPoolNm_Type(OctetString):
    """Custom type hh3cDhcp6Server2PoolGpIncPoolNm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDhcp6Server2PoolGpIncPoolNm_Type.__name__ = "OctetString"
_Hh3cDhcp6Server2PoolGpIncPoolNm_Object = MibTableColumn
hh3cDhcp6Server2PoolGpIncPoolNm = _Hh3cDhcp6Server2PoolGpIncPoolNm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 4, 1, 1),
    _Hh3cDhcp6Server2PoolGpIncPoolNm_Type()
)
hh3cDhcp6Server2PoolGpIncPoolNm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpIncPoolNm.setStatus("current")
_Hh3cDhcp6Server2PoolGpExtRowSta_Type = RowStatus
_Hh3cDhcp6Server2PoolGpExtRowSta_Object = MibTableColumn
hh3cDhcp6Server2PoolGpExtRowSta = _Hh3cDhcp6Server2PoolGpExtRowSta_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 4, 1, 2),
    _Hh3cDhcp6Server2PoolGpExtRowSta_Type()
)
hh3cDhcp6Server2PoolGpExtRowSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpExtRowSta.setStatus("current")
_Hh3cDhcp6Server2PoolGpStatTable_Object = MibTable
hh3cDhcp6Server2PoolGpStatTable = _Hh3cDhcp6Server2PoolGpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpStatTable.setStatus("current")
_Hh3cDhcp6Server2PoolGpStatEntry_Object = MibTableRow
hh3cDhcp6Server2PoolGpStatEntry = _Hh3cDhcp6Server2PoolGpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1)
)
hh3cDhcp6Server2PoolGpStatEntry.setIndexNames(
    (0, "HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolGpName"),
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpStatEntry.setStatus("current")


class _Hh3cDhcp6Server2PoolGpPoolNum_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolGpPoolNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Hh3cDhcp6Server2PoolGpPoolNum_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolGpPoolNum_Object = MibTableColumn
hh3cDhcp6Server2PoolGpPoolNum = _Hh3cDhcp6Server2PoolGpPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 1),
    _Hh3cDhcp6Server2PoolGpPoolNum_Type()
)
hh3cDhcp6Server2PoolGpPoolNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpPoolNum.setStatus("current")
_Hh3cDhcp6Server2PoolGpBndDomNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolGpBndDomNum_Object = MibTableColumn
hh3cDhcp6Server2PoolGpBndDomNum = _Hh3cDhcp6Server2PoolGpBndDomNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 2),
    _Hh3cDhcp6Server2PoolGpBndDomNum_Type()
)
hh3cDhcp6Server2PoolGpBndDomNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpBndDomNum.setStatus("current")


class _Hh3cDhcp6Server2PoolGpIPUsage_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolGpIPUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDhcp6Server2PoolGpIPUsage_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolGpIPUsage_Object = MibTableColumn
hh3cDhcp6Server2PoolGpIPUsage = _Hh3cDhcp6Server2PoolGpIPUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 3),
    _Hh3cDhcp6Server2PoolGpIPUsage_Type()
)
hh3cDhcp6Server2PoolGpIPUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpIPUsage.setStatus("current")
_Hh3cDhcp6Server2PoolGpIPTotaNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolGpIPTotaNum_Object = MibTableColumn
hh3cDhcp6Server2PoolGpIPTotaNum = _Hh3cDhcp6Server2PoolGpIPTotaNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 4),
    _Hh3cDhcp6Server2PoolGpIPTotaNum_Type()
)
hh3cDhcp6Server2PoolGpIPTotaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpIPTotaNum.setStatus("current")
_Hh3cDhcp6Server2PoolGpIPUsedNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolGpIPUsedNum_Object = MibTableColumn
hh3cDhcp6Server2PoolGpIPUsedNum = _Hh3cDhcp6Server2PoolGpIPUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 5),
    _Hh3cDhcp6Server2PoolGpIPUsedNum_Type()
)
hh3cDhcp6Server2PoolGpIPUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpIPUsedNum.setStatus("current")
_Hh3cDhcp6Server2PoolGpIPIdleNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolGpIPIdleNum_Object = MibTableColumn
hh3cDhcp6Server2PoolGpIPIdleNum = _Hh3cDhcp6Server2PoolGpIPIdleNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 6),
    _Hh3cDhcp6Server2PoolGpIPIdleNum_Type()
)
hh3cDhcp6Server2PoolGpIPIdleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpIPIdleNum.setStatus("current")
_Hh3cDhcp6Server2PoolGpIPExcNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolGpIPExcNum_Object = MibTableColumn
hh3cDhcp6Server2PoolGpIPExcNum = _Hh3cDhcp6Server2PoolGpIPExcNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 7),
    _Hh3cDhcp6Server2PoolGpIPExcNum_Type()
)
hh3cDhcp6Server2PoolGpIPExcNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpIPExcNum.setStatus("current")
_Hh3cDhcp6Server2PoolGpIPConfNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolGpIPConfNum_Object = MibTableColumn
hh3cDhcp6Server2PoolGpIPConfNum = _Hh3cDhcp6Server2PoolGpIPConfNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 8),
    _Hh3cDhcp6Server2PoolGpIPConfNum_Type()
)
hh3cDhcp6Server2PoolGpIPConfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpIPConfNum.setStatus("current")


class _Hh3cDhcp6Server2PoolGpPDUsage_Type(Unsigned32):
    """Custom type hh3cDhcp6Server2PoolGpPDUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDhcp6Server2PoolGpPDUsage_Type.__name__ = "Unsigned32"
_Hh3cDhcp6Server2PoolGpPDUsage_Object = MibTableColumn
hh3cDhcp6Server2PoolGpPDUsage = _Hh3cDhcp6Server2PoolGpPDUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 9),
    _Hh3cDhcp6Server2PoolGpPDUsage_Type()
)
hh3cDhcp6Server2PoolGpPDUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpPDUsage.setStatus("current")
_Hh3cDhcp6Server2PoolGpPDTotaNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolGpPDTotaNum_Object = MibTableColumn
hh3cDhcp6Server2PoolGpPDTotaNum = _Hh3cDhcp6Server2PoolGpPDTotaNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 10),
    _Hh3cDhcp6Server2PoolGpPDTotaNum_Type()
)
hh3cDhcp6Server2PoolGpPDTotaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpPDTotaNum.setStatus("current")
_Hh3cDhcp6Server2PoolGpPDUsedNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolGpPDUsedNum_Object = MibTableColumn
hh3cDhcp6Server2PoolGpPDUsedNum = _Hh3cDhcp6Server2PoolGpPDUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 11),
    _Hh3cDhcp6Server2PoolGpPDUsedNum_Type()
)
hh3cDhcp6Server2PoolGpPDUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpPDUsedNum.setStatus("current")
_Hh3cDhcp6Server2PoolGpPDIdleNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolGpPDIdleNum_Object = MibTableColumn
hh3cDhcp6Server2PoolGpPDIdleNum = _Hh3cDhcp6Server2PoolGpPDIdleNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 12),
    _Hh3cDhcp6Server2PoolGpPDIdleNum_Type()
)
hh3cDhcp6Server2PoolGpPDIdleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpPDIdleNum.setStatus("current")
_Hh3cDhcp6Server2PoolGpPDExcNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolGpPDExcNum_Object = MibTableColumn
hh3cDhcp6Server2PoolGpPDExcNum = _Hh3cDhcp6Server2PoolGpPDExcNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 13),
    _Hh3cDhcp6Server2PoolGpPDExcNum_Type()
)
hh3cDhcp6Server2PoolGpPDExcNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpPDExcNum.setStatus("current")
_Hh3cDhcp6Server2PoolGpPDConfNum_Type = Unsigned32
_Hh3cDhcp6Server2PoolGpPDConfNum_Object = MibTableColumn
hh3cDhcp6Server2PoolGpPDConfNum = _Hh3cDhcp6Server2PoolGpPDConfNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 14),
    _Hh3cDhcp6Server2PoolGpPDConfNum_Type()
)
hh3cDhcp6Server2PoolGpPDConfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpPDConfNum.setStatus("current")
_Hh3cDhcp6Server2PoolGpIPReserveNum_Type = Counter64
_Hh3cDhcp6Server2PoolGpIPReserveNum_Object = MibTableColumn
hh3cDhcp6Server2PoolGpIPReserveNum = _Hh3cDhcp6Server2PoolGpIPReserveNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 15),
    _Hh3cDhcp6Server2PoolGpIPReserveNum_Type()
)
hh3cDhcp6Server2PoolGpIPReserveNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpIPReserveNum.setStatus("current")
_Hh3cDhcp6Server2PoolGpPdReserveNum_Type = Counter64
_Hh3cDhcp6Server2PoolGpPdReserveNum_Object = MibTableColumn
hh3cDhcp6Server2PoolGpPdReserveNum = _Hh3cDhcp6Server2PoolGpPdReserveNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 5, 1, 16),
    _Hh3cDhcp6Server2PoolGpPdReserveNum_Type()
)
hh3cDhcp6Server2PoolGpPdReserveNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PoolGpPdReserveNum.setStatus("current")
_Hh3cDhcp6Server2PrefixPoolTable_Object = MibTable
hh3cDhcp6Server2PrefixPoolTable = _Hh3cDhcp6Server2PrefixPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PrefixPoolTable.setStatus("current")
_Hh3cDhcp6Server2PrefixPoolEntry_Object = MibTableRow
hh3cDhcp6Server2PrefixPoolEntry = _Hh3cDhcp6Server2PrefixPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 6, 1)
)
hh3cDhcp6Server2PrefixPoolEntry.setIndexNames(
    (0, "HH3C-DHCP6-MIB", "hh3cDhcp6Server2PdVPNInstance"),
    (0, "HH3C-DHCP6-MIB", "hh3cDhcp6Server2PdNumber"),
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PrefixPoolEntry.setStatus("current")


class _Hh3cDhcp6Server2PdVPNInstance_Type(OctetString):
    """Custom type hh3cDhcp6Server2PdVPNInstance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cDhcp6Server2PdVPNInstance_Type.__name__ = "OctetString"
_Hh3cDhcp6Server2PdVPNInstance_Object = MibTableColumn
hh3cDhcp6Server2PdVPNInstance = _Hh3cDhcp6Server2PdVPNInstance_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 6, 1, 1),
    _Hh3cDhcp6Server2PdVPNInstance_Type()
)
hh3cDhcp6Server2PdVPNInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdVPNInstance.setStatus("current")


class _Hh3cDhcp6Server2PdNumber_Type(Integer32):
    """Custom type hh3cDhcp6Server2PdNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Hh3cDhcp6Server2PdNumber_Type.__name__ = "Integer32"
_Hh3cDhcp6Server2PdNumber_Object = MibTableColumn
hh3cDhcp6Server2PdNumber = _Hh3cDhcp6Server2PdNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 6, 1, 2),
    _Hh3cDhcp6Server2PdNumber_Type()
)
hh3cDhcp6Server2PdNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdNumber.setStatus("current")


class _Hh3cDhcp6Server2PdPrefixAddr_Type(OctetString):
    """Custom type hh3cDhcp6Server2PdPrefixAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Hh3cDhcp6Server2PdPrefixAddr_Type.__name__ = "OctetString"
_Hh3cDhcp6Server2PdPrefixAddr_Object = MibTableColumn
hh3cDhcp6Server2PdPrefixAddr = _Hh3cDhcp6Server2PdPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 6, 1, 3),
    _Hh3cDhcp6Server2PdPrefixAddr_Type()
)
hh3cDhcp6Server2PdPrefixAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdPrefixAddr.setStatus("current")


class _Hh3cDhcp6Server2PdPrefixLen_Type(Integer32):
    """Custom type hh3cDhcp6Server2PdPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Hh3cDhcp6Server2PdPrefixLen_Type.__name__ = "Integer32"
_Hh3cDhcp6Server2PdPrefixLen_Object = MibTableColumn
hh3cDhcp6Server2PdPrefixLen = _Hh3cDhcp6Server2PdPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 6, 1, 4),
    _Hh3cDhcp6Server2PdPrefixLen_Type()
)
hh3cDhcp6Server2PdPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdPrefixLen.setStatus("current")


class _Hh3cDhcp6Server2PdPrefixNumber_Type(Integer32):
    """Custom type hh3cDhcp6Server2PdPrefixNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Hh3cDhcp6Server2PdPrefixNumber_Type.__name__ = "Integer32"
_Hh3cDhcp6Server2PdPrefixNumber_Object = MibTableColumn
hh3cDhcp6Server2PdPrefixNumber = _Hh3cDhcp6Server2PdPrefixNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 6, 1, 5),
    _Hh3cDhcp6Server2PdPrefixNumber_Type()
)
hh3cDhcp6Server2PdPrefixNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdPrefixNumber.setStatus("current")


class _Hh3cDhcp6Server2PdPrefixAssLen_Type(Integer32):
    """Custom type hh3cDhcp6Server2PdPrefixAssLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Hh3cDhcp6Server2PdPrefixAssLen_Type.__name__ = "Integer32"
_Hh3cDhcp6Server2PdPrefixAssLen_Object = MibTableColumn
hh3cDhcp6Server2PdPrefixAssLen = _Hh3cDhcp6Server2PdPrefixAssLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 6, 1, 6),
    _Hh3cDhcp6Server2PdPrefixAssLen_Type()
)
hh3cDhcp6Server2PdPrefixAssLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdPrefixAssLen.setStatus("current")
_Hh3cDhcp6Server2PdRowStatus_Type = RowStatus
_Hh3cDhcp6Server2PdRowStatus_Object = MibTableColumn
hh3cDhcp6Server2PdRowStatus = _Hh3cDhcp6Server2PdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 1, 6, 1, 7),
    _Hh3cDhcp6Server2PdRowStatus_Type()
)
hh3cDhcp6Server2PdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdRowStatus.setStatus("current")
_Hh3cDhcp6Server2Traps_ObjectIdentity = ObjectIdentity
hh3cDhcp6Server2Traps = _Hh3cDhcp6Server2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2)
)
_Hh3cDhcp6Server2TrapNotify_ObjectIdentity = ObjectIdentity
hh3cDhcp6Server2TrapNotify = _Hh3cDhcp6Server2TrapNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cDhcp6Server2AddrExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 1)
)
hh3cDhcp6Server2AddrExhaust.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2AddrExhaust.setStatus(
        "current"
    )

hh3cDhcp6Server2AddrExhaustRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 2)
)
hh3cDhcp6Server2AddrExhaustRecov.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2AddrExhaustRecov.setStatus(
        "current"
    )

hh3cDhcp6Server2IpUsageOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 3)
)
hh3cDhcp6Server2IpUsageOverflow.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2IpUsageOverflow.setStatus(
        "current"
    )

hh3cDhcp6Server2IpUsageOverflowRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 4)
)
hh3cDhcp6Server2IpUsageOverflowRecov.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2IpUsageOverflowRecov.setStatus(
        "current"
    )

hh3cDhcp6Server2PdExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 5)
)
hh3cDhcp6Server2PdExhaust.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdExhaust.setStatus(
        "current"
    )

hh3cDhcp6Server2PdExhaustRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 6)
)
hh3cDhcp6Server2PdExhaustRecov.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdExhaustRecov.setStatus(
        "current"
    )

hh3cDhcp6Server2PdUsageOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 7)
)
hh3cDhcp6Server2PdUsageOverflow.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdUsageOverflow.setStatus(
        "current"
    )

hh3cDhcp6Server2PdUsageOverflowRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 8)
)
hh3cDhcp6Server2PdUsageOverflowRecov.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdUsageOverflowRecov.setStatus(
        "current"
    )

hh3cDhcp6Server2IpNetUsageOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 9)
)
hh3cDhcp6Server2IpNetUsageOverflow.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2IpNetUsageOverflow.setStatus(
        "current"
    )

hh3cDhcp6Server2IpNetUsageOverflowRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 10)
)
hh3cDhcp6Server2IpNetUsageOverflowRecov.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2IpNetUsageOverflowRecov.setStatus(
        "current"
    )

hh3cDhcp6Server2IpNetExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 11)
)
hh3cDhcp6Server2IpNetExhaust.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2IpNetExhaust.setStatus(
        "current"
    )

hh3cDhcp6Server2IpNetExhaustRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 12)
)
hh3cDhcp6Server2IpNetExhaustRecov.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2IpNetExhaustRecov.setStatus(
        "current"
    )

hh3cDhcp6Server2PdNetUsageOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 13)
)
hh3cDhcp6Server2PdNetUsageOverflow.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdNetUsageOverflow.setStatus(
        "current"
    )

hh3cDhcp6Server2PdNetUsageOverflowRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 14)
)
hh3cDhcp6Server2PdNetUsageOverflowRecov.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdNetUsageOverflowRecov.setStatus(
        "current"
    )

hh3cDhcp6Server2PdNetExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 15)
)
hh3cDhcp6Server2PdNetExhaust.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdNetExhaust.setStatus(
        "current"
    )

hh3cDhcp6Server2PdNetExhaustRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 16)
)
hh3cDhcp6Server2PdNetExhaustRecov.setObjects(
      *(("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolIndex"),
        ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolName"))
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2PdNetExhaustRecov.setStatus(
        "current"
    )

hh3cDhcp6Server2GpIpNetExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 17)
)
hh3cDhcp6Server2GpIpNetExhaust.setObjects(
    ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolGpName")
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2GpIpNetExhaust.setStatus(
        "current"
    )

hh3cDhcp6Server2GpIpNetExhaustRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 18)
)
hh3cDhcp6Server2GpIpNetExhaustRecov.setObjects(
    ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolGpName")
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2GpIpNetExhaustRecov.setStatus(
        "current"
    )

hh3cDhcp6Server2GpPdNetExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 19)
)
hh3cDhcp6Server2GpPdNetExhaust.setObjects(
    ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolGpName")
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2GpPdNetExhaust.setStatus(
        "current"
    )

hh3cDhcp6Server2GpPdNetExhaustRecov = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 179, 2, 0, 20)
)
hh3cDhcp6Server2GpPdNetExhaustRecov.setObjects(
    ("HH3C-DHCP6-MIB", "hh3cDhcp6Server2PoolGpName")
)
if mibBuilder.loadTexts:
    hh3cDhcp6Server2GpPdNetExhaustRecov.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DHCP6-MIB",
    **{"hh3cDhcp6": hh3cDhcp6,
       "hh3cDhcp6Server2Tables": hh3cDhcp6Server2Tables,
       "hh3cDhcp6Server2PoolTable": hh3cDhcp6Server2PoolTable,
       "hh3cDhcp6Server2PoolEntry": hh3cDhcp6Server2PoolEntry,
       "hh3cDhcp6Server2PoolIndex": hh3cDhcp6Server2PoolIndex,
       "hh3cDhcp6Server2PoolName": hh3cDhcp6Server2PoolName,
       "hh3cDhcp6Server2PoolRowStatus": hh3cDhcp6Server2PoolRowStatus,
       "hh3cDhcp6Server2PoolVpnName": hh3cDhcp6Server2PoolVpnName,
       "hh3cDhcp6Server2PoolType": hh3cDhcp6Server2PoolType,
       "hh3cDhcp6Server2PoolNetwork": hh3cDhcp6Server2PoolNetwork,
       "hh3cDhcp6Server2PoolNetworkMask": hh3cDhcp6Server2PoolNetworkMask,
       "hh3cDhcp6Server2PoolNetworkPdNum": hh3cDhcp6Server2PoolNetworkPdNum,
       "hh3cDhcp6Server2PoolSubPdAddr": hh3cDhcp6Server2PoolSubPdAddr,
       "hh3cDhcp6Server2PoolSubPdLength": hh3cDhcp6Server2PoolSubPdLength,
       "hh3cDhcp6Server2PoolNetPreTime": hh3cDhcp6Server2PoolNetPreTime,
       "hh3cDhcp6Server2PoolNetValTime": hh3cDhcp6Server2PoolNetValTime,
       "hh3cDhcp6Server2PoolNetExport": hh3cDhcp6Server2PoolNetExport,
       "hh3cDhcp6Server2PoolNetPrefer": hh3cDhcp6Server2PoolNetPrefer,
       "hh3cDhcp6Server2PoolNetTag": hh3cDhcp6Server2PoolNetTag,
       "hh3cDhcp6Server2PoolNaStartAddr": hh3cDhcp6Server2PoolNaStartAddr,
       "hh3cDhcp6Server2PoolNaEndAddr": hh3cDhcp6Server2PoolNaEndAddr,
       "hh3cDhcp6Server2PoolNaPreTime": hh3cDhcp6Server2PoolNaPreTime,
       "hh3cDhcp6Server2PoolNaValTime": hh3cDhcp6Server2PoolNaValTime,
       "hh3cDhcp6Server2PoolTaStartAddr": hh3cDhcp6Server2PoolTaStartAddr,
       "hh3cDhcp6Server2PoolTaEndAddr": hh3cDhcp6Server2PoolTaEndAddr,
       "hh3cDhcp6Server2PoolTaPreTime": hh3cDhcp6Server2PoolTaPreTime,
       "hh3cDhcp6Server2PoolTaValTime": hh3cDhcp6Server2PoolTaValTime,
       "hh3cDhcp6Server2PoolPrefixPool": hh3cDhcp6Server2PoolPrefixPool,
       "hh3cDhcp6Server2PoolPdPreTime": hh3cDhcp6Server2PoolPdPreTime,
       "hh3cDhcp6Server2PoolPdValTime": hh3cDhcp6Server2PoolPdValTime,
       "hh3cDhcp6Server2PoolPdExport": hh3cDhcp6Server2PoolPdExport,
       "hh3cDhcp6Server2PoolPdPreference": hh3cDhcp6Server2PoolPdPreference,
       "hh3cDhcp6Server2PoolPdTag": hh3cDhcp6Server2PoolPdTag,
       "hh3cDhcp6Server2PoolDomainName": hh3cDhcp6Server2PoolDomainName,
       "hh3cDhcp6Server2PoolGatewayIp": hh3cDhcp6Server2PoolGatewayIp,
       "hh3cDhcp6Server2PoolDNSIp": hh3cDhcp6Server2PoolDNSIp,
       "hh3cDhcp6Server2PoolExpireIpEnbl": hh3cDhcp6Server2PoolExpireIpEnbl,
       "hh3cDhcp6Server2PoolExpireIpMode": hh3cDhcp6Server2PoolExpireIpMode,
       "hh3cDhcp6Server2PoolExpireIpLim": hh3cDhcp6Server2PoolExpireIpLim,
       "hh3cDhcp6Server2PoolExpireIpTime": hh3cDhcp6Server2PoolExpireIpTime,
       "hh3cDhcp6Server2PoolExpirePdEnbl": hh3cDhcp6Server2PoolExpirePdEnbl,
       "hh3cDhcp6Server2PoolExpirePdMode": hh3cDhcp6Server2PoolExpirePdMode,
       "hh3cDhcp6Server2PoolExpirePdLim": hh3cDhcp6Server2PoolExpirePdLim,
       "hh3cDhcp6Server2PoolExpirePdTime": hh3cDhcp6Server2PoolExpirePdTime,
       "hh3cDhcp6Server2PoolStatTable": hh3cDhcp6Server2PoolStatTable,
       "hh3cDhcp6Server2PoolStatEntry": hh3cDhcp6Server2PoolStatEntry,
       "hh3cDhcp6Server2PoolIPIdleNum": hh3cDhcp6Server2PoolIPIdleNum,
       "hh3cDhcp6Server2PoolIPUsedNum": hh3cDhcp6Server2PoolIPUsedNum,
       "hh3cDhcp6Server2PoolPrefixIdleNum": hh3cDhcp6Server2PoolPrefixIdleNum,
       "hh3cDhcp6Server2PoolPrefixUsedNum": hh3cDhcp6Server2PoolPrefixUsedNum,
       "hh3cDhcp6Server2PoolIPTotalNum": hh3cDhcp6Server2PoolIPTotalNum,
       "hh3cDhcp6Server2PoolIPExpiredNum": hh3cDhcp6Server2PoolIPExpiredNum,
       "hh3cDhcp6Server2PoolIPDynamicUsedNum": hh3cDhcp6Server2PoolIPDynamicUsedNum,
       "hh3cDhcp6Server2PoolIPStaticUsedNum": hh3cDhcp6Server2PoolIPStaticUsedNum,
       "hh3cDhcp6Server2PoolIPConflictNum": hh3cDhcp6Server2PoolIPConflictNum,
       "hh3cDhcp6Server2PoolIPExcludeNum": hh3cDhcp6Server2PoolIPExcludeNum,
       "hh3cDhcp6Server2PoolIPReserveNum": hh3cDhcp6Server2PoolIPReserveNum,
       "hh3cDhcp6Server2PoolIPUsage": hh3cDhcp6Server2PoolIPUsage,
       "hh3cDhcp6Server2PoolPdTotalNum": hh3cDhcp6Server2PoolPdTotalNum,
       "hh3cDhcp6Server2PoolPdExpiredNum": hh3cDhcp6Server2PoolPdExpiredNum,
       "hh3cDhcp6Server2PoolPdDynamicUsedNum": hh3cDhcp6Server2PoolPdDynamicUsedNum,
       "hh3cDhcp6Server2PoolPdStaticUsedNum": hh3cDhcp6Server2PoolPdStaticUsedNum,
       "hh3cDhcp6Server2PoolPdConflictNum": hh3cDhcp6Server2PoolPdConflictNum,
       "hh3cDhcp6Server2PoolPdExcludeNum": hh3cDhcp6Server2PoolPdExcludeNum,
       "hh3cDhcp6Server2PoolPdReserveNum": hh3cDhcp6Server2PoolPdReserveNum,
       "hh3cDhcp6Server2PoolPdUsage": hh3cDhcp6Server2PoolPdUsage,
       "hh3cDhcp6Server2PoolGpTable": hh3cDhcp6Server2PoolGpTable,
       "hh3cDhcp6Server2PoolGpEntry": hh3cDhcp6Server2PoolGpEntry,
       "hh3cDhcp6Server2PoolGpName": hh3cDhcp6Server2PoolGpName,
       "hh3cDhcp6Server2PoolGpVpnName": hh3cDhcp6Server2PoolGpVpnName,
       "hh3cDhcp6Server2PoolGpIncUndo": hh3cDhcp6Server2PoolGpIncUndo,
       "hh3cDhcp6Server2PoolGpRowSta": hh3cDhcp6Server2PoolGpRowSta,
       "hh3cDhcp6Server2PoolGpExtTable": hh3cDhcp6Server2PoolGpExtTable,
       "hh3cDhcp6Server2PoolGpExtEntry": hh3cDhcp6Server2PoolGpExtEntry,
       "hh3cDhcp6Server2PoolGpIncPoolNm": hh3cDhcp6Server2PoolGpIncPoolNm,
       "hh3cDhcp6Server2PoolGpExtRowSta": hh3cDhcp6Server2PoolGpExtRowSta,
       "hh3cDhcp6Server2PoolGpStatTable": hh3cDhcp6Server2PoolGpStatTable,
       "hh3cDhcp6Server2PoolGpStatEntry": hh3cDhcp6Server2PoolGpStatEntry,
       "hh3cDhcp6Server2PoolGpPoolNum": hh3cDhcp6Server2PoolGpPoolNum,
       "hh3cDhcp6Server2PoolGpBndDomNum": hh3cDhcp6Server2PoolGpBndDomNum,
       "hh3cDhcp6Server2PoolGpIPUsage": hh3cDhcp6Server2PoolGpIPUsage,
       "hh3cDhcp6Server2PoolGpIPTotaNum": hh3cDhcp6Server2PoolGpIPTotaNum,
       "hh3cDhcp6Server2PoolGpIPUsedNum": hh3cDhcp6Server2PoolGpIPUsedNum,
       "hh3cDhcp6Server2PoolGpIPIdleNum": hh3cDhcp6Server2PoolGpIPIdleNum,
       "hh3cDhcp6Server2PoolGpIPExcNum": hh3cDhcp6Server2PoolGpIPExcNum,
       "hh3cDhcp6Server2PoolGpIPConfNum": hh3cDhcp6Server2PoolGpIPConfNum,
       "hh3cDhcp6Server2PoolGpPDUsage": hh3cDhcp6Server2PoolGpPDUsage,
       "hh3cDhcp6Server2PoolGpPDTotaNum": hh3cDhcp6Server2PoolGpPDTotaNum,
       "hh3cDhcp6Server2PoolGpPDUsedNum": hh3cDhcp6Server2PoolGpPDUsedNum,
       "hh3cDhcp6Server2PoolGpPDIdleNum": hh3cDhcp6Server2PoolGpPDIdleNum,
       "hh3cDhcp6Server2PoolGpPDExcNum": hh3cDhcp6Server2PoolGpPDExcNum,
       "hh3cDhcp6Server2PoolGpPDConfNum": hh3cDhcp6Server2PoolGpPDConfNum,
       "hh3cDhcp6Server2PoolGpIPReserveNum": hh3cDhcp6Server2PoolGpIPReserveNum,
       "hh3cDhcp6Server2PoolGpPdReserveNum": hh3cDhcp6Server2PoolGpPdReserveNum,
       "hh3cDhcp6Server2PrefixPoolTable": hh3cDhcp6Server2PrefixPoolTable,
       "hh3cDhcp6Server2PrefixPoolEntry": hh3cDhcp6Server2PrefixPoolEntry,
       "hh3cDhcp6Server2PdVPNInstance": hh3cDhcp6Server2PdVPNInstance,
       "hh3cDhcp6Server2PdNumber": hh3cDhcp6Server2PdNumber,
       "hh3cDhcp6Server2PdPrefixAddr": hh3cDhcp6Server2PdPrefixAddr,
       "hh3cDhcp6Server2PdPrefixLen": hh3cDhcp6Server2PdPrefixLen,
       "hh3cDhcp6Server2PdPrefixNumber": hh3cDhcp6Server2PdPrefixNumber,
       "hh3cDhcp6Server2PdPrefixAssLen": hh3cDhcp6Server2PdPrefixAssLen,
       "hh3cDhcp6Server2PdRowStatus": hh3cDhcp6Server2PdRowStatus,
       "hh3cDhcp6Server2Traps": hh3cDhcp6Server2Traps,
       "hh3cDhcp6Server2TrapNotify": hh3cDhcp6Server2TrapNotify,
       "hh3cDhcp6Server2AddrExhaust": hh3cDhcp6Server2AddrExhaust,
       "hh3cDhcp6Server2AddrExhaustRecov": hh3cDhcp6Server2AddrExhaustRecov,
       "hh3cDhcp6Server2IpUsageOverflow": hh3cDhcp6Server2IpUsageOverflow,
       "hh3cDhcp6Server2IpUsageOverflowRecov": hh3cDhcp6Server2IpUsageOverflowRecov,
       "hh3cDhcp6Server2PdExhaust": hh3cDhcp6Server2PdExhaust,
       "hh3cDhcp6Server2PdExhaustRecov": hh3cDhcp6Server2PdExhaustRecov,
       "hh3cDhcp6Server2PdUsageOverflow": hh3cDhcp6Server2PdUsageOverflow,
       "hh3cDhcp6Server2PdUsageOverflowRecov": hh3cDhcp6Server2PdUsageOverflowRecov,
       "hh3cDhcp6Server2IpNetUsageOverflow": hh3cDhcp6Server2IpNetUsageOverflow,
       "hh3cDhcp6Server2IpNetUsageOverflowRecov": hh3cDhcp6Server2IpNetUsageOverflowRecov,
       "hh3cDhcp6Server2IpNetExhaust": hh3cDhcp6Server2IpNetExhaust,
       "hh3cDhcp6Server2IpNetExhaustRecov": hh3cDhcp6Server2IpNetExhaustRecov,
       "hh3cDhcp6Server2PdNetUsageOverflow": hh3cDhcp6Server2PdNetUsageOverflow,
       "hh3cDhcp6Server2PdNetUsageOverflowRecov": hh3cDhcp6Server2PdNetUsageOverflowRecov,
       "hh3cDhcp6Server2PdNetExhaust": hh3cDhcp6Server2PdNetExhaust,
       "hh3cDhcp6Server2PdNetExhaustRecov": hh3cDhcp6Server2PdNetExhaustRecov,
       "hh3cDhcp6Server2GpIpNetExhaust": hh3cDhcp6Server2GpIpNetExhaust,
       "hh3cDhcp6Server2GpIpNetExhaustRecov": hh3cDhcp6Server2GpIpNetExhaustRecov,
       "hh3cDhcp6Server2GpPdNetExhaust": hh3cDhcp6Server2GpPdNetExhaust,
       "hh3cDhcp6Server2GpPdNetExhaustRecov": hh3cDhcp6Server2GpPdNetExhaustRecov}
)
