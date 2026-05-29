# SNMP MIB module (HH3C-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-NAT-MIB

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

hh3cNat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18)
)
if mibBuilder.loadTexts:
    hh3cNat.setRevisions(
        ("2020-12-29 14:40",
         "2019-12-01 14:46",
         "2019-10-10 17:52",
         "2017-04-07 15:03",
         "2016-12-25 11:05",
         "2014-07-11 11:15",
         "2005-01-20 15:18")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cNATGlobalVars_ObjectIdentity = ObjectIdentity
hh3cNATGlobalVars = _Hh3cNATGlobalVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1)
)
_Hh3cNATClearSession_ObjectIdentity = ObjectIdentity
hh3cNATClearSession = _Hh3cNATClearSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 1)
)


class _Hh3cNATClearSessionSlotNo_Type(Integer32):
    """Custom type hh3cNATClearSessionSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_Hh3cNATClearSessionSlotNo_Type.__name__ = "Integer32"
_Hh3cNATClearSessionSlotNo_Object = MibScalar
hh3cNATClearSessionSlotNo = _Hh3cNATClearSessionSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 1, 1),
    _Hh3cNATClearSessionSlotNo_Type()
)
hh3cNATClearSessionSlotNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATClearSessionSlotNo.setStatus("current")
_Hh3cNATBLConnectLimitPara_ObjectIdentity = ObjectIdentity
hh3cNATBLConnectLimitPara = _Hh3cNATBLConnectLimitPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2)
)


class _Hh3cNATBLConnectHighValue_Type(Integer32):
    """Custom type hh3cNATBLConnectHighValue based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_Hh3cNATBLConnectHighValue_Type.__name__ = "Integer32"
_Hh3cNATBLConnectHighValue_Object = MibScalar
hh3cNATBLConnectHighValue = _Hh3cNATBLConnectHighValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 1),
    _Hh3cNATBLConnectHighValue_Type()
)
hh3cNATBLConnectHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLConnectHighValue.setStatus("current")


class _Hh3cNATBLConnectLowValue_Type(Integer32):
    """Custom type hh3cNATBLConnectLowValue based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_Hh3cNATBLConnectLowValue_Type.__name__ = "Integer32"
_Hh3cNATBLConnectLowValue_Object = MibScalar
hh3cNATBLConnectLowValue = _Hh3cNATBLConnectLowValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 2),
    _Hh3cNATBLConnectLowValue_Type()
)
hh3cNATBLConnectLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLConnectLowValue.setStatus("current")


class _Hh3cNATBLConnectHighRate_Type(Integer32):
    """Custom type hh3cNATBLConnectHighRate based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_Hh3cNATBLConnectHighRate_Type.__name__ = "Integer32"
_Hh3cNATBLConnectHighRate_Object = MibScalar
hh3cNATBLConnectHighRate = _Hh3cNATBLConnectHighRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 3),
    _Hh3cNATBLConnectHighRate_Type()
)
hh3cNATBLConnectHighRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLConnectHighRate.setStatus("current")


class _Hh3cNATBLConnectLowRate_Type(Integer32):
    """Custom type hh3cNATBLConnectLowRate based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_Hh3cNATBLConnectLowRate_Type.__name__ = "Integer32"
_Hh3cNATBLConnectLowRate_Object = MibScalar
hh3cNATBLConnectLowRate = _Hh3cNATBLConnectLowRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 4),
    _Hh3cNATBLConnectLowRate_Type()
)
hh3cNATBLConnectLowRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLConnectLowRate.setStatus("current")


class _Hh3cNATBLSpecialConnectHighRate_Type(Integer32):
    """Custom type hh3cNATBLSpecialConnectHighRate based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_Hh3cNATBLSpecialConnectHighRate_Type.__name__ = "Integer32"
_Hh3cNATBLSpecialConnectHighRate_Object = MibScalar
hh3cNATBLSpecialConnectHighRate = _Hh3cNATBLSpecialConnectHighRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 5),
    _Hh3cNATBLSpecialConnectHighRate_Type()
)
hh3cNATBLSpecialConnectHighRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLSpecialConnectHighRate.setStatus("current")


class _Hh3cNATBLSpecialConnectLowRate_Type(Integer32):
    """Custom type hh3cNATBLSpecialConnectLowRate based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 21474836),
    )


_Hh3cNATBLSpecialConnectLowRate_Type.__name__ = "Integer32"
_Hh3cNATBLSpecialConnectLowRate_Object = MibScalar
hh3cNATBLSpecialConnectLowRate = _Hh3cNATBLSpecialConnectLowRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 2, 6),
    _Hh3cNATBLSpecialConnectLowRate_Type()
)
hh3cNATBLSpecialConnectLowRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLSpecialConnectLowRate.setStatus("current")
_Hh3cNATBLCtrlEnable_ObjectIdentity = ObjectIdentity
hh3cNATBLCtrlEnable = _Hh3cNATBLCtrlEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 3)
)


class _Hh3cNATBLConnectSumEnable_Type(Integer32):
    """Custom type hh3cNATBLConnectSumEnable based on Integer32"""
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


_Hh3cNATBLConnectSumEnable_Type.__name__ = "Integer32"
_Hh3cNATBLConnectSumEnable_Object = MibScalar
hh3cNATBLConnectSumEnable = _Hh3cNATBLConnectSumEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 3, 1),
    _Hh3cNATBLConnectSumEnable_Type()
)
hh3cNATBLConnectSumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLConnectSumEnable.setStatus("current")


class _Hh3cNATBLConnectRateEnable_Type(Integer32):
    """Custom type hh3cNATBLConnectRateEnable based on Integer32"""
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


_Hh3cNATBLConnectRateEnable_Type.__name__ = "Integer32"
_Hh3cNATBLConnectRateEnable_Object = MibScalar
hh3cNATBLConnectRateEnable = _Hh3cNATBLConnectRateEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 3, 2),
    _Hh3cNATBLConnectRateEnable_Type()
)
hh3cNATBLConnectRateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLConnectRateEnable.setStatus("current")
_Hh3cNATNPTimer_ObjectIdentity = ObjectIdentity
hh3cNATNPTimer = _Hh3cNATNPTimer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 4)
)


class _Hh3cNATNPAgingTime_Type(Integer32):
    """Custom type hh3cNATNPAgingTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("slow", 2))
    )


_Hh3cNATNPAgingTime_Type.__name__ = "Integer32"
_Hh3cNATNPAgingTime_Object = MibScalar
hh3cNATNPAgingTime = _Hh3cNATNPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 1, 4, 1),
    _Hh3cNATNPAgingTime_Type()
)
hh3cNATNPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATNPAgingTime.setStatus("current")
_Hh3cNATMibObjects_ObjectIdentity = ObjectIdentity
hh3cNATMibObjects = _Hh3cNATMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2)
)
_Hh3cNATPoolInfoTable_Object = MibTable
hh3cNATPoolInfoTable = _Hh3cNATPoolInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cNATPoolInfoTable.setStatus("current")
_Hh3cNATPoolInfoEntry_Object = MibTableRow
hh3cNATPoolInfoEntry = _Hh3cNATPoolInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1)
)
hh3cNATPoolInfoEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATPoolIdx"),
)
if mibBuilder.loadTexts:
    hh3cNATPoolInfoEntry.setStatus("current")


class _Hh3cNATPoolIdx_Type(Integer32):
    """Custom type hh3cNATPoolIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 320),
    )


_Hh3cNATPoolIdx_Type.__name__ = "Integer32"
_Hh3cNATPoolIdx_Object = MibTableColumn
hh3cNATPoolIdx = _Hh3cNATPoolIdx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 1),
    _Hh3cNATPoolIdx_Type()
)
hh3cNATPoolIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATPoolIdx.setStatus("current")
_Hh3cNATPoolStartIpAddr_Type = IpAddress
_Hh3cNATPoolStartIpAddr_Object = MibTableColumn
hh3cNATPoolStartIpAddr = _Hh3cNATPoolStartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 2),
    _Hh3cNATPoolStartIpAddr_Type()
)
hh3cNATPoolStartIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATPoolStartIpAddr.setStatus("current")
_Hh3cNATPoolEndIpAddr_Type = IpAddress
_Hh3cNATPoolEndIpAddr_Object = MibTableColumn
hh3cNATPoolEndIpAddr = _Hh3cNATPoolEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 3),
    _Hh3cNATPoolEndIpAddr_Type()
)
hh3cNATPoolEndIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATPoolEndIpAddr.setStatus("current")


class _Hh3cNATPoolSlotNo_Type(Integer32):
    """Custom type hh3cNATPoolSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_Hh3cNATPoolSlotNo_Type.__name__ = "Integer32"
_Hh3cNATPoolSlotNo_Object = MibTableColumn
hh3cNATPoolSlotNo = _Hh3cNATPoolSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 4),
    _Hh3cNATPoolSlotNo_Type()
)
hh3cNATPoolSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATPoolSlotNo.setStatus("current")
_Hh3cNATPoolRefCounter_Type = Integer32
_Hh3cNATPoolRefCounter_Object = MibTableColumn
hh3cNATPoolRefCounter = _Hh3cNATPoolRefCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 5),
    _Hh3cNATPoolRefCounter_Type()
)
hh3cNATPoolRefCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATPoolRefCounter.setStatus("current")
_Hh3cNATPoolRowStatus_Type = RowStatus
_Hh3cNATPoolRowStatus_Object = MibTableColumn
hh3cNATPoolRowStatus = _Hh3cNATPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 1, 1, 6),
    _Hh3cNATPoolRowStatus_Type()
)
hh3cNATPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATPoolRowStatus.setStatus("current")
_Hh3cNATOutboundTable_Object = MibTable
hh3cNATOutboundTable = _Hh3cNATOutboundTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cNATOutboundTable.setStatus("current")
_Hh3cNATOutboundEntry_Object = MibTableRow
hh3cNATOutboundEntry = _Hh3cNATOutboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1)
)
hh3cNATOutboundEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-NAT-MIB", "hh3cNATOutboundAclNo"),
)
if mibBuilder.loadTexts:
    hh3cNATOutboundEntry.setStatus("current")


class _Hh3cNATOutboundAclNo_Type(Integer32):
    """Custom type hh3cNATOutboundAclNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3999),
    )


_Hh3cNATOutboundAclNo_Type.__name__ = "Integer32"
_Hh3cNATOutboundAclNo_Object = MibTableColumn
hh3cNATOutboundAclNo = _Hh3cNATOutboundAclNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 1),
    _Hh3cNATOutboundAclNo_Type()
)
hh3cNATOutboundAclNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATOutboundAclNo.setStatus("current")


class _Hh3cNATOutboundPoolIdx_Type(Integer32):
    """Custom type hh3cNATOutboundPoolIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Hh3cNATOutboundPoolIdx_Type.__name__ = "Integer32"
_Hh3cNATOutboundPoolIdx_Object = MibTableColumn
hh3cNATOutboundPoolIdx = _Hh3cNATOutboundPoolIdx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 2),
    _Hh3cNATOutboundPoolIdx_Type()
)
hh3cNATOutboundPoolIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATOutboundPoolIdx.setStatus("current")


class _Hh3cNATOutboundIsNoPat_Type(Integer32):
    """Custom type hh3cNATOutboundIsNoPat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Hh3cNATOutboundIsNoPat_Type.__name__ = "Integer32"
_Hh3cNATOutboundIsNoPat_Object = MibTableColumn
hh3cNATOutboundIsNoPat = _Hh3cNATOutboundIsNoPat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 3),
    _Hh3cNATOutboundIsNoPat_Type()
)
hh3cNATOutboundIsNoPat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATOutboundIsNoPat.setStatus("current")


class _Hh3cNATOutboundSlotNo_Type(Integer32):
    """Custom type hh3cNATOutboundSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_Hh3cNATOutboundSlotNo_Type.__name__ = "Integer32"
_Hh3cNATOutboundSlotNo_Object = MibTableColumn
hh3cNATOutboundSlotNo = _Hh3cNATOutboundSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 4),
    _Hh3cNATOutboundSlotNo_Type()
)
hh3cNATOutboundSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATOutboundSlotNo.setStatus("current")
_Hh3cNATOutboundRowStatus_Type = RowStatus
_Hh3cNATOutboundRowStatus_Object = MibTableColumn
hh3cNATOutboundRowStatus = _Hh3cNATOutboundRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 2, 1, 5),
    _Hh3cNATOutboundRowStatus_Type()
)
hh3cNATOutboundRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATOutboundRowStatus.setStatus("current")
_Hh3cNATServerTable_Object = MibTable
hh3cNATServerTable = _Hh3cNATServerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cNATServerTable.setStatus("current")
_Hh3cNATServerEntry_Object = MibTableRow
hh3cNATServerEntry = _Hh3cNATServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1)
)
hh3cNATServerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-NAT-MIB", "hh3cNATServerProType"),
    (0, "HH3C-NAT-MIB", "hh3cNATServerGlobalIP"),
    (0, "HH3C-NAT-MIB", "hh3cNATServerStartGlobalPort"),
    (0, "HH3C-NAT-MIB", "hh3cNATServerVpnIndex"),
)
if mibBuilder.loadTexts:
    hh3cNATServerEntry.setStatus("current")


class _Hh3cNATServerProType_Type(Integer32):
    """Custom type hh3cNATServerProType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cNATServerProType_Type.__name__ = "Integer32"
_Hh3cNATServerProType_Object = MibTableColumn
hh3cNATServerProType = _Hh3cNATServerProType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 1),
    _Hh3cNATServerProType_Type()
)
hh3cNATServerProType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATServerProType.setStatus("current")
_Hh3cNATServerGlobalIP_Type = IpAddress
_Hh3cNATServerGlobalIP_Object = MibTableColumn
hh3cNATServerGlobalIP = _Hh3cNATServerGlobalIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 2),
    _Hh3cNATServerGlobalIP_Type()
)
hh3cNATServerGlobalIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATServerGlobalIP.setStatus("current")


class _Hh3cNATServerStartGlobalPort_Type(Integer32):
    """Custom type hh3cNATServerStartGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATServerStartGlobalPort_Type.__name__ = "Integer32"
_Hh3cNATServerStartGlobalPort_Object = MibTableColumn
hh3cNATServerStartGlobalPort = _Hh3cNATServerStartGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 3),
    _Hh3cNATServerStartGlobalPort_Type()
)
hh3cNATServerStartGlobalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATServerStartGlobalPort.setStatus("current")


class _Hh3cNATServerEndGlobalPort_Type(Integer32):
    """Custom type hh3cNATServerEndGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATServerEndGlobalPort_Type.__name__ = "Integer32"
_Hh3cNATServerEndGlobalPort_Object = MibTableColumn
hh3cNATServerEndGlobalPort = _Hh3cNATServerEndGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 4),
    _Hh3cNATServerEndGlobalPort_Type()
)
hh3cNATServerEndGlobalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATServerEndGlobalPort.setStatus("current")
_Hh3cNATServerStartInsideIP_Type = IpAddress
_Hh3cNATServerStartInsideIP_Object = MibTableColumn
hh3cNATServerStartInsideIP = _Hh3cNATServerStartInsideIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 5),
    _Hh3cNATServerStartInsideIP_Type()
)
hh3cNATServerStartInsideIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATServerStartInsideIP.setStatus("current")
_Hh3cNATServerEndInsideIP_Type = IpAddress
_Hh3cNATServerEndInsideIP_Object = MibTableColumn
hh3cNATServerEndInsideIP = _Hh3cNATServerEndInsideIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 6),
    _Hh3cNATServerEndInsideIP_Type()
)
hh3cNATServerEndInsideIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATServerEndInsideIP.setStatus("current")


class _Hh3cNATServerInsidePort_Type(Integer32):
    """Custom type hh3cNATServerInsidePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATServerInsidePort_Type.__name__ = "Integer32"
_Hh3cNATServerInsidePort_Object = MibTableColumn
hh3cNATServerInsidePort = _Hh3cNATServerInsidePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 7),
    _Hh3cNATServerInsidePort_Type()
)
hh3cNATServerInsidePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATServerInsidePort.setStatus("current")


class _Hh3cNATServerSlotNo_Type(Integer32):
    """Custom type hh3cNATServerSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_Hh3cNATServerSlotNo_Type.__name__ = "Integer32"
_Hh3cNATServerSlotNo_Object = MibTableColumn
hh3cNATServerSlotNo = _Hh3cNATServerSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 8),
    _Hh3cNATServerSlotNo_Type()
)
hh3cNATServerSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATServerSlotNo.setStatus("current")


class _Hh3cNATServerVpnIndex_Type(Integer32):
    """Custom type hh3cNATServerVpnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATServerVpnIndex_Type.__name__ = "Integer32"
_Hh3cNATServerVpnIndex_Object = MibTableColumn
hh3cNATServerVpnIndex = _Hh3cNATServerVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 10),
    _Hh3cNATServerVpnIndex_Type()
)
hh3cNATServerVpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATServerVpnIndex.setStatus("current")


class _Hh3cNATServerAclNumber_Type(Integer32):
    """Custom type hh3cNATServerAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Hh3cNATServerAclNumber_Type.__name__ = "Integer32"
_Hh3cNATServerAclNumber_Object = MibTableColumn
hh3cNATServerAclNumber = _Hh3cNATServerAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 11),
    _Hh3cNATServerAclNumber_Type()
)
hh3cNATServerAclNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATServerAclNumber.setStatus("current")
_Hh3cNATServerRowStatus_Type = RowStatus
_Hh3cNATServerRowStatus_Object = MibTableColumn
hh3cNATServerRowStatus = _Hh3cNATServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 3, 1, 12),
    _Hh3cNATServerRowStatus_Type()
)
hh3cNATServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATServerRowStatus.setStatus("current")
_Hh3cNATTimeOutTable_Object = MibTable
hh3cNATTimeOutTable = _Hh3cNATTimeOutTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cNATTimeOutTable.setStatus("current")
_Hh3cNATTimeOutEntry_Object = MibTableRow
hh3cNATTimeOutEntry = _Hh3cNATTimeOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 4, 1)
)
hh3cNATTimeOutEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATTimeOutProtocol"),
)
if mibBuilder.loadTexts:
    hh3cNATTimeOutEntry.setStatus("current")


class _Hh3cNATTimeOutProtocol_Type(Integer32):
    """Custom type hh3cNATTimeOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("pptp", 4),
          ("dns", 5),
          ("tcpFin", 6),
          ("tcpSyn", 7),
          ("ftpCtrl", 8),
          ("ftpData", 9))
    )


_Hh3cNATTimeOutProtocol_Type.__name__ = "Integer32"
_Hh3cNATTimeOutProtocol_Object = MibTableColumn
hh3cNATTimeOutProtocol = _Hh3cNATTimeOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 4, 1, 1),
    _Hh3cNATTimeOutProtocol_Type()
)
hh3cNATTimeOutProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATTimeOutProtocol.setStatus("current")


class _Hh3cNATTimeOutTimeValue_Type(Integer32):
    """Custom type hh3cNATTimeOutTimeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_Hh3cNATTimeOutTimeValue_Type.__name__ = "Integer32"
_Hh3cNATTimeOutTimeValue_Object = MibTableColumn
hh3cNATTimeOutTimeValue = _Hh3cNATTimeOutTimeValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 4, 1, 2),
    _Hh3cNATTimeOutTimeValue_Type()
)
hh3cNATTimeOutTimeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATTimeOutTimeValue.setStatus("current")
_Hh3cNATBLEnableTable_Object = MibTable
hh3cNATBLEnableTable = _Hh3cNATBLEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cNATBLEnableTable.setStatus("current")
_Hh3cNATBLEnableEntry_Object = MibTableRow
hh3cNATBLEnableEntry = _Hh3cNATBLEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 5, 1)
)
hh3cNATBLEnableEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATBLEnableSlotNo"),
)
if mibBuilder.loadTexts:
    hh3cNATBLEnableEntry.setStatus("current")


class _Hh3cNATBLEnableSlotNo_Type(Integer32):
    """Custom type hh3cNATBLEnableSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_Hh3cNATBLEnableSlotNo_Type.__name__ = "Integer32"
_Hh3cNATBLEnableSlotNo_Object = MibTableColumn
hh3cNATBLEnableSlotNo = _Hh3cNATBLEnableSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 5, 1, 1),
    _Hh3cNATBLEnableSlotNo_Type()
)
hh3cNATBLEnableSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATBLEnableSlotNo.setStatus("current")


class _Hh3cNATBLEnable_Type(Integer32):
    """Custom type hh3cNATBLEnable based on Integer32"""
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


_Hh3cNATBLEnable_Type.__name__ = "Integer32"
_Hh3cNATBLEnable_Object = MibTableColumn
hh3cNATBLEnable = _Hh3cNATBLEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 5, 1, 2),
    _Hh3cNATBLEnable_Type()
)
hh3cNATBLEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATBLEnable.setStatus("current")
_Hh3cNATBLIPConnectLimitParaTable_Object = MibTable
hh3cNATBLIPConnectLimitParaTable = _Hh3cNATBLIPConnectLimitParaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cNATBLIPConnectLimitParaTable.setStatus("current")
_Hh3cNATBLIPConnectLimitParaEntry_Object = MibTableRow
hh3cNATBLIPConnectLimitParaEntry = _Hh3cNATBLIPConnectLimitParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1)
)
hh3cNATBLIPConnectLimitParaEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATBLIPConnectLimitParaIP"),
)
if mibBuilder.loadTexts:
    hh3cNATBLIPConnectLimitParaEntry.setStatus("current")
_Hh3cNATBLIPConnectLimitParaIP_Type = IpAddress
_Hh3cNATBLIPConnectLimitParaIP_Object = MibTableColumn
hh3cNATBLIPConnectLimitParaIP = _Hh3cNATBLIPConnectLimitParaIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 1),
    _Hh3cNATBLIPConnectLimitParaIP_Type()
)
hh3cNATBLIPConnectLimitParaIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATBLIPConnectLimitParaIP.setStatus("current")


class _Hh3cNATBLIPConnectHighValue_Type(Integer32):
    """Custom type hh3cNATBLIPConnectHighValue based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_Hh3cNATBLIPConnectHighValue_Type.__name__ = "Integer32"
_Hh3cNATBLIPConnectHighValue_Object = MibTableColumn
hh3cNATBLIPConnectHighValue = _Hh3cNATBLIPConnectHighValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 2),
    _Hh3cNATBLIPConnectHighValue_Type()
)
hh3cNATBLIPConnectHighValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATBLIPConnectHighValue.setStatus("current")


class _Hh3cNATBLIPConnectLowValue_Type(Integer32):
    """Custom type hh3cNATBLIPConnectLowValue based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20000),
    )


_Hh3cNATBLIPConnectLowValue_Type.__name__ = "Integer32"
_Hh3cNATBLIPConnectLowValue_Object = MibTableColumn
hh3cNATBLIPConnectLowValue = _Hh3cNATBLIPConnectLowValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 3),
    _Hh3cNATBLIPConnectLowValue_Type()
)
hh3cNATBLIPConnectLowValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATBLIPConnectLowValue.setStatus("current")


class _Hh3cNATBLIPUseSpecialConnectRate_Type(Integer32):
    """Custom type hh3cNATBLIPUseSpecialConnectRate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Hh3cNATBLIPUseSpecialConnectRate_Type.__name__ = "Integer32"
_Hh3cNATBLIPUseSpecialConnectRate_Object = MibTableColumn
hh3cNATBLIPUseSpecialConnectRate = _Hh3cNATBLIPUseSpecialConnectRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 4),
    _Hh3cNATBLIPUseSpecialConnectRate_Type()
)
hh3cNATBLIPUseSpecialConnectRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATBLIPUseSpecialConnectRate.setStatus("current")
_Hh3cNATBLIPConnectLimitRowStatus_Type = RowStatus
_Hh3cNATBLIPConnectLimitRowStatus_Object = MibTableColumn
hh3cNATBLIPConnectLimitRowStatus = _Hh3cNATBLIPConnectLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 6, 1, 5),
    _Hh3cNATBLIPConnectLimitRowStatus_Type()
)
hh3cNATBLIPConnectLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATBLIPConnectLimitRowStatus.setStatus("current")
_Hh3cNATBLManagerTable_Object = MibTable
hh3cNATBLManagerTable = _Hh3cNATBLManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cNATBLManagerTable.setStatus("current")
_Hh3cNATBLManagerEntry_Object = MibTableRow
hh3cNATBLManagerEntry = _Hh3cNATBLManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1)
)
hh3cNATBLManagerEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATBLIpAdress"),
    (0, "HH3C-NAT-MIB", "hh3cNATBLSlotNo"),
)
if mibBuilder.loadTexts:
    hh3cNATBLManagerEntry.setStatus("current")
_Hh3cNATBLIpAdress_Type = IpAddress
_Hh3cNATBLIpAdress_Object = MibTableColumn
hh3cNATBLIpAdress = _Hh3cNATBLIpAdress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1, 1),
    _Hh3cNATBLIpAdress_Type()
)
hh3cNATBLIpAdress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATBLIpAdress.setStatus("current")


class _Hh3cNATBLSlotNo_Type(Integer32):
    """Custom type hh3cNATBLSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Hh3cNATBLSlotNo_Type.__name__ = "Integer32"
_Hh3cNATBLSlotNo_Object = MibTableColumn
hh3cNATBLSlotNo = _Hh3cNATBLSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1, 2),
    _Hh3cNATBLSlotNo_Type()
)
hh3cNATBLSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATBLSlotNo.setStatus("current")
_Hh3cNATBLConSum_Type = Integer32
_Hh3cNATBLConSum_Object = MibTableColumn
hh3cNATBLConSum = _Hh3cNATBLConSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1, 3),
    _Hh3cNATBLConSum_Type()
)
hh3cNATBLConSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATBLConSum.setStatus("current")


class _Hh3cNATBLConSpd_Type(Integer32):
    """Custom type hh3cNATBLConSpd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("red", 1),
          ("yellow", 2),
          ("green", 3))
    )


_Hh3cNATBLConSpd_Type.__name__ = "Integer32"
_Hh3cNATBLConSpd_Object = MibTableColumn
hh3cNATBLConSpd = _Hh3cNATBLConSpd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 7, 1, 4),
    _Hh3cNATBLConSpd_Type()
)
hh3cNATBLConSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATBLConSpd.setStatus("current")
_Hh3cNATStatTable_Object = MibTable
hh3cNATStatTable = _Hh3cNATStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cNATStatTable.setStatus("current")
_Hh3cNATStatEntry_Object = MibTableRow
hh3cNATStatEntry = _Hh3cNATStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1)
)
hh3cNATStatEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATStatNATBoardNo"),
)
if mibBuilder.loadTexts:
    hh3cNATStatEntry.setStatus("current")


class _Hh3cNATStatNATBoardNo_Type(Integer32):
    """Custom type hh3cNATStatNATBoardNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(255, 255),
    )


_Hh3cNATStatNATBoardNo_Type.__name__ = "Integer32"
_Hh3cNATStatNATBoardNo_Object = MibTableColumn
hh3cNATStatNATBoardNo = _Hh3cNATStatNATBoardNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 1),
    _Hh3cNATStatNATBoardNo_Type()
)
hh3cNATStatNATBoardNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATStatNATBoardNo.setStatus("current")
_Hh3cNATStatActiveTblCount_Type = Counter32
_Hh3cNATStatActiveTblCount_Object = MibTableColumn
hh3cNATStatActiveTblCount = _Hh3cNATStatActiveTblCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 2),
    _Hh3cNATStatActiveTblCount_Type()
)
hh3cNATStatActiveTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatActiveTblCount.setStatus("current")
_Hh3cNATStatActiveTblCountInNP_Type = Counter32
_Hh3cNATStatActiveTblCountInNP_Object = MibTableColumn
hh3cNATStatActiveTblCountInNP = _Hh3cNATStatActiveTblCountInNP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 3),
    _Hh3cNATStatActiveTblCountInNP_Type()
)
hh3cNATStatActiveTblCountInNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatActiveTblCountInNP.setStatus("current")
_Hh3cNATStatActiveNatTblCount_Type = Counter32
_Hh3cNATStatActiveNatTblCount_Object = MibTableColumn
hh3cNATStatActiveNatTblCount = _Hh3cNATStatActiveNatTblCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 4),
    _Hh3cNATStatActiveNatTblCount_Type()
)
hh3cNATStatActiveNatTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatActiveNatTblCount.setStatus("current")
_Hh3cNATStatActiveSvrTblCount_Type = Counter32
_Hh3cNATStatActiveSvrTblCount_Object = MibTableColumn
hh3cNATStatActiveSvrTblCount = _Hh3cNATStatActiveSvrTblCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 5),
    _Hh3cNATStatActiveSvrTblCount_Type()
)
hh3cNATStatActiveSvrTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatActiveSvrTblCount.setStatus("current")
_Hh3cNATStatActivePoolTblCount_Type = Counter32
_Hh3cNATStatActivePoolTblCount_Object = MibTableColumn
hh3cNATStatActivePoolTblCount = _Hh3cNATStatActivePoolTblCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 6),
    _Hh3cNATStatActivePoolTblCount_Type()
)
hh3cNATStatActivePoolTblCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatActivePoolTblCount.setStatus("current")
_Hh3cNATStatNumOfUsedPort_Type = Counter32
_Hh3cNATStatNumOfUsedPort_Object = MibTableColumn
hh3cNATStatNumOfUsedPort = _Hh3cNATStatNumOfUsedPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 7),
    _Hh3cNATStatNumOfUsedPort_Type()
)
hh3cNATStatNumOfUsedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatNumOfUsedPort.setStatus("current")
_Hh3cNATStatNumOfGoodPkt_Type = Counter32
_Hh3cNATStatNumOfGoodPkt_Object = MibTableColumn
hh3cNATStatNumOfGoodPkt = _Hh3cNATStatNumOfGoodPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 8),
    _Hh3cNATStatNumOfGoodPkt_Type()
)
hh3cNATStatNumOfGoodPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatNumOfGoodPkt.setStatus("current")
_Hh3cNATStatNumOfBadPkt_Type = Counter32
_Hh3cNATStatNumOfBadPkt_Object = MibTableColumn
hh3cNATStatNumOfBadPkt = _Hh3cNATStatNumOfBadPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 9),
    _Hh3cNATStatNumOfBadPkt_Type()
)
hh3cNATStatNumOfBadPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStatNumOfBadPkt.setStatus("current")
_Hh3cNATStaticSessionCount_Type = Integer32
_Hh3cNATStaticSessionCount_Object = MibTableColumn
hh3cNATStaticSessionCount = _Hh3cNATStaticSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 10),
    _Hh3cNATStaticSessionCount_Type()
)
hh3cNATStaticSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATStaticSessionCount.setStatus("current")
_Hh3cNATFragmentSessionCount_Type = Integer32
_Hh3cNATFragmentSessionCount_Object = MibTableColumn
hh3cNATFragmentSessionCount = _Hh3cNATFragmentSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 11),
    _Hh3cNATFragmentSessionCount_Type()
)
hh3cNATFragmentSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATFragmentSessionCount.setStatus("current")
_Hh3cNATSequenceSessionCount_Type = Integer32
_Hh3cNATSequenceSessionCount_Object = MibTableColumn
hh3cNATSequenceSessionCount = _Hh3cNATSequenceSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 12),
    _Hh3cNATSequenceSessionCount_Type()
)
hh3cNATSequenceSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATSequenceSessionCount.setStatus("current")
_Hh3cNATLogCount_Type = Integer32
_Hh3cNATLogCount_Object = MibTableColumn
hh3cNATLogCount = _Hh3cNATLogCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 8, 1, 13),
    _Hh3cNATLogCount_Type()
)
hh3cNATLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATLogCount.setStatus("current")
_Hh3cNATSessionTable_Object = MibTable
hh3cNATSessionTable = _Hh3cNATSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9)
)
if mibBuilder.loadTexts:
    hh3cNATSessionTable.setStatus("current")
_Hh3cNATSessionEntry_Object = MibTableRow
hh3cNATSessionEntry = _Hh3cNATSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1)
)
hh3cNATSessionEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATSessionHashNumber"),
    (0, "HH3C-NAT-MIB", "hh3cNATSessionProtocol"),
    (0, "HH3C-NAT-MIB", "hh3cNATSessionInsideIP"),
    (0, "HH3C-NAT-MIB", "hh3cNATSessionInsidePort"),
    (0, "HH3C-NAT-MIB", "hh3cNATSessionPeerIP"),
    (0, "HH3C-NAT-MIB", "hh3cNATSessionPeerPort"),
    (0, "HH3C-NAT-MIB", "hh3cNATSessionVpnIndex"),
)
if mibBuilder.loadTexts:
    hh3cNATSessionEntry.setStatus("current")


class _Hh3cNATSessionHashNumber_Type(Integer32):
    """Custom type hh3cNATSessionHashNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300000),
    )


_Hh3cNATSessionHashNumber_Type.__name__ = "Integer32"
_Hh3cNATSessionHashNumber_Object = MibTableColumn
hh3cNATSessionHashNumber = _Hh3cNATSessionHashNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 1),
    _Hh3cNATSessionHashNumber_Type()
)
hh3cNATSessionHashNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATSessionHashNumber.setStatus("current")


class _Hh3cNATSessionProtocol_Type(Integer32):
    """Custom type hh3cNATSessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cNATSessionProtocol_Type.__name__ = "Integer32"
_Hh3cNATSessionProtocol_Object = MibTableColumn
hh3cNATSessionProtocol = _Hh3cNATSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 2),
    _Hh3cNATSessionProtocol_Type()
)
hh3cNATSessionProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATSessionProtocol.setStatus("current")
_Hh3cNATSessionGlobalIP_Type = IpAddress
_Hh3cNATSessionGlobalIP_Object = MibTableColumn
hh3cNATSessionGlobalIP = _Hh3cNATSessionGlobalIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 3),
    _Hh3cNATSessionGlobalIP_Type()
)
hh3cNATSessionGlobalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATSessionGlobalIP.setStatus("current")


class _Hh3cNATSessionGlobalPort_Type(Integer32):
    """Custom type hh3cNATSessionGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATSessionGlobalPort_Type.__name__ = "Integer32"
_Hh3cNATSessionGlobalPort_Object = MibTableColumn
hh3cNATSessionGlobalPort = _Hh3cNATSessionGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 4),
    _Hh3cNATSessionGlobalPort_Type()
)
hh3cNATSessionGlobalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATSessionGlobalPort.setStatus("current")
_Hh3cNATSessionInsideIP_Type = IpAddress
_Hh3cNATSessionInsideIP_Object = MibTableColumn
hh3cNATSessionInsideIP = _Hh3cNATSessionInsideIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 5),
    _Hh3cNATSessionInsideIP_Type()
)
hh3cNATSessionInsideIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATSessionInsideIP.setStatus("current")


class _Hh3cNATSessionInsidePort_Type(Integer32):
    """Custom type hh3cNATSessionInsidePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATSessionInsidePort_Type.__name__ = "Integer32"
_Hh3cNATSessionInsidePort_Object = MibTableColumn
hh3cNATSessionInsidePort = _Hh3cNATSessionInsidePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 6),
    _Hh3cNATSessionInsidePort_Type()
)
hh3cNATSessionInsidePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATSessionInsidePort.setStatus("current")
_Hh3cNATSessionPeerIP_Type = IpAddress
_Hh3cNATSessionPeerIP_Object = MibTableColumn
hh3cNATSessionPeerIP = _Hh3cNATSessionPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 7),
    _Hh3cNATSessionPeerIP_Type()
)
hh3cNATSessionPeerIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATSessionPeerIP.setStatus("current")


class _Hh3cNATSessionPeerPort_Type(Integer32):
    """Custom type hh3cNATSessionPeerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATSessionPeerPort_Type.__name__ = "Integer32"
_Hh3cNATSessionPeerPort_Object = MibTableColumn
hh3cNATSessionPeerPort = _Hh3cNATSessionPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 8),
    _Hh3cNATSessionPeerPort_Type()
)
hh3cNATSessionPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATSessionPeerPort.setStatus("current")


class _Hh3cNATSessionVpnIndex_Type(Integer32):
    """Custom type hh3cNATSessionVpnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cNATSessionVpnIndex_Type.__name__ = "Integer32"
_Hh3cNATSessionVpnIndex_Object = MibTableColumn
hh3cNATSessionVpnIndex = _Hh3cNATSessionVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 9),
    _Hh3cNATSessionVpnIndex_Type()
)
hh3cNATSessionVpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATSessionVpnIndex.setStatus("current")
_Hh3cNATSessionTTL_Type = Integer32
_Hh3cNATSessionTTL_Object = MibTableColumn
hh3cNATSessionTTL = _Hh3cNATSessionTTL_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 10),
    _Hh3cNATSessionTTL_Type()
)
hh3cNATSessionTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATSessionTTL.setStatus("current")
_Hh3cNATSessionStatus_Type = Integer32
_Hh3cNATSessionStatus_Object = MibTableColumn
hh3cNATSessionStatus = _Hh3cNATSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 11),
    _Hh3cNATSessionStatus_Type()
)
hh3cNATSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATSessionStatus.setStatus("current")
_Hh3cNATSessionLeftTime_Type = TimeTicks
_Hh3cNATSessionLeftTime_Object = MibTableColumn
hh3cNATSessionLeftTime = _Hh3cNATSessionLeftTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 9, 1, 12),
    _Hh3cNATSessionLeftTime_Type()
)
hh3cNATSessionLeftTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATSessionLeftTime.setStatus("current")
_Hh3cNATStaticConfTable_Object = MibTable
hh3cNATStaticConfTable = _Hh3cNATStaticConfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10)
)
if mibBuilder.loadTexts:
    hh3cNATStaticConfTable.setStatus("current")
_Hh3cNATStaticConfEntry_Object = MibTableRow
hh3cNATStaticConfEntry = _Hh3cNATStaticConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10, 1)
)
hh3cNATStaticConfEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATStaticInsideIp"),
)
if mibBuilder.loadTexts:
    hh3cNATStaticConfEntry.setStatus("current")
_Hh3cNATStaticInsideIp_Type = IpAddress
_Hh3cNATStaticInsideIp_Object = MibTableColumn
hh3cNATStaticInsideIp = _Hh3cNATStaticInsideIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10, 1, 1),
    _Hh3cNATStaticInsideIp_Type()
)
hh3cNATStaticInsideIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATStaticInsideIp.setStatus("current")
_Hh3cNATStaticGlobalIp_Type = IpAddress
_Hh3cNATStaticGlobalIp_Object = MibTableColumn
hh3cNATStaticGlobalIp = _Hh3cNATStaticGlobalIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10, 1, 2),
    _Hh3cNATStaticGlobalIp_Type()
)
hh3cNATStaticGlobalIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATStaticGlobalIp.setStatus("current")
_Hh3cNATStaticRowStatus_Type = RowStatus
_Hh3cNATStaticRowStatus_Object = MibTableColumn
hh3cNATStaticRowStatus = _Hh3cNATStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 10, 1, 3),
    _Hh3cNATStaticRowStatus_Type()
)
hh3cNATStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATStaticRowStatus.setStatus("current")
_Hh3cNATStaticEnableTable_Object = MibTable
hh3cNATStaticEnableTable = _Hh3cNATStaticEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 11)
)
if mibBuilder.loadTexts:
    hh3cNATStaticEnableTable.setStatus("current")
_Hh3cNATStaticEnableEntry_Object = MibTableRow
hh3cNATStaticEnableEntry = _Hh3cNATStaticEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 11, 1)
)
hh3cNATStaticEnableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cNATStaticEnableEntry.setStatus("current")


class _Hh3cNATStaticEnable_Type(Integer32):
    """Custom type hh3cNATStaticEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Hh3cNATStaticEnable_Type.__name__ = "Integer32"
_Hh3cNATStaticEnable_Object = MibTableColumn
hh3cNATStaticEnable = _Hh3cNATStaticEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 11, 1, 2),
    _Hh3cNATStaticEnable_Type()
)
hh3cNATStaticEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNATStaticEnable.setStatus("current")
_Hh3cNATDnsMapTable_Object = MibTable
hh3cNATDnsMapTable = _Hh3cNATDnsMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12)
)
if mibBuilder.loadTexts:
    hh3cNATDnsMapTable.setStatus("current")
_Hh3cNATDnsMapEntry_Object = MibTableRow
hh3cNATDnsMapEntry = _Hh3cNATDnsMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1)
)
hh3cNATDnsMapEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATDnsMapDomainName"),
)
if mibBuilder.loadTexts:
    hh3cNATDnsMapEntry.setStatus("current")
_Hh3cNATDnsMapDomainName_Type = DisplayString
_Hh3cNATDnsMapDomainName_Object = MibTableColumn
hh3cNATDnsMapDomainName = _Hh3cNATDnsMapDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 1),
    _Hh3cNATDnsMapDomainName_Type()
)
hh3cNATDnsMapDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATDnsMapDomainName.setStatus("current")
_Hh3cNATDnsMapGlobalIp_Type = IpAddress
_Hh3cNATDnsMapGlobalIp_Object = MibTableColumn
hh3cNATDnsMapGlobalIp = _Hh3cNATDnsMapGlobalIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 2),
    _Hh3cNATDnsMapGlobalIp_Type()
)
hh3cNATDnsMapGlobalIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATDnsMapGlobalIp.setStatus("current")


class _Hh3cNATDnsMapGlobalPort_Type(Integer32):
    """Custom type hh3cNATDnsMapGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cNATDnsMapGlobalPort_Type.__name__ = "Integer32"
_Hh3cNATDnsMapGlobalPort_Object = MibTableColumn
hh3cNATDnsMapGlobalPort = _Hh3cNATDnsMapGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 3),
    _Hh3cNATDnsMapGlobalPort_Type()
)
hh3cNATDnsMapGlobalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATDnsMapGlobalPort.setStatus("current")


class _Hh3cNATDnsMapProtocolType_Type(Integer32):
    """Custom type hh3cNATDnsMapProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("typeTCP", 1),
          ("typeUDP", 2))
    )


_Hh3cNATDnsMapProtocolType_Type.__name__ = "Integer32"
_Hh3cNATDnsMapProtocolType_Object = MibTableColumn
hh3cNATDnsMapProtocolType = _Hh3cNATDnsMapProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 4),
    _Hh3cNATDnsMapProtocolType_Type()
)
hh3cNATDnsMapProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATDnsMapProtocolType.setStatus("current")
_Hh3cNATDnsMapLastUseTime_Type = TimeTicks
_Hh3cNATDnsMapLastUseTime_Object = MibTableColumn
hh3cNATDnsMapLastUseTime = _Hh3cNATDnsMapLastUseTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 5),
    _Hh3cNATDnsMapLastUseTime_Type()
)
hh3cNATDnsMapLastUseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATDnsMapLastUseTime.setStatus("current")
_Hh3cNATDnsMapRowStatus_Type = RowStatus
_Hh3cNATDnsMapRowStatus_Object = MibTableColumn
hh3cNATDnsMapRowStatus = _Hh3cNATDnsMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 12, 1, 6),
    _Hh3cNATDnsMapRowStatus_Type()
)
hh3cNATDnsMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNATDnsMapRowStatus.setStatus("current")
_Hh3cNATStatVer2Table_Object = MibTable
hh3cNATStatVer2Table = _Hh3cNATStatVer2Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13)
)
if mibBuilder.loadTexts:
    hh3cNATStatVer2Table.setStatus("current")
_Hh3cNATStatVer2TableEntry_Object = MibTableRow
hh3cNATStatVer2TableEntry = _Hh3cNATStatVer2TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13, 1)
)
hh3cNATStatVer2TableEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATStatChassis"),
    (0, "HH3C-NAT-MIB", "hh3cNATStatSlot"),
    (0, "HH3C-NAT-MIB", "hh3cNATStatCPUID"),
)
if mibBuilder.loadTexts:
    hh3cNATStatVer2TableEntry.setStatus("current")


class _Hh3cNATStatChassis_Type(Unsigned32):
    """Custom type hh3cNATStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cNATStatChassis_Type.__name__ = "Unsigned32"
_Hh3cNATStatChassis_Object = MibTableColumn
hh3cNATStatChassis = _Hh3cNATStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13, 1, 1),
    _Hh3cNATStatChassis_Type()
)
hh3cNATStatChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATStatChassis.setStatus("current")


class _Hh3cNATStatSlot_Type(Unsigned32):
    """Custom type hh3cNATStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cNATStatSlot_Type.__name__ = "Unsigned32"
_Hh3cNATStatSlot_Object = MibTableColumn
hh3cNATStatSlot = _Hh3cNATStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13, 1, 2),
    _Hh3cNATStatSlot_Type()
)
hh3cNATStatSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATStatSlot.setStatus("current")


class _Hh3cNATStatCPUID_Type(Unsigned32):
    """Custom type hh3cNATStatCPUID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cNATStatCPUID_Type.__name__ = "Unsigned32"
_Hh3cNATStatCPUID_Object = MibTableColumn
hh3cNATStatCPUID = _Hh3cNATStatCPUID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13, 1, 3),
    _Hh3cNATStatCPUID_Type()
)
hh3cNATStatCPUID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATStatCPUID.setStatus("current")
_Hh3cNATTotalNATSessionCount_Type = Unsigned32
_Hh3cNATTotalNATSessionCount_Object = MibTableColumn
hh3cNATTotalNATSessionCount = _Hh3cNATTotalNATSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13, 1, 4),
    _Hh3cNATTotalNATSessionCount_Type()
)
hh3cNATTotalNATSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATTotalNATSessionCount.setStatus("current")
_Hh3cNATEimTableCount_Type = Unsigned32
_Hh3cNATEimTableCount_Object = MibTableColumn
hh3cNATEimTableCount = _Hh3cNATEimTableCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13, 1, 5),
    _Hh3cNATEimTableCount_Type()
)
hh3cNATEimTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATEimTableCount.setStatus("current")
_Hh3cNATInboundNoPATTableCount_Type = Unsigned32
_Hh3cNATInboundNoPATTableCount_Object = MibTableColumn
hh3cNATInboundNoPATTableCount = _Hh3cNATInboundNoPATTableCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13, 1, 6),
    _Hh3cNATInboundNoPATTableCount_Type()
)
hh3cNATInboundNoPATTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATInboundNoPATTableCount.setStatus("current")
_Hh3cNATOutboundNoPATTableCount_Type = Unsigned32
_Hh3cNATOutboundNoPATTableCount_Object = MibTableColumn
hh3cNATOutboundNoPATTableCount = _Hh3cNATOutboundNoPATTableCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13, 1, 7),
    _Hh3cNATOutboundNoPATTableCount_Type()
)
hh3cNATOutboundNoPATTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATOutboundNoPATTableCount.setStatus("current")
_Hh3cNATMaxDynamicPortblock_Type = Unsigned32
_Hh3cNATMaxDynamicPortblock_Object = MibTableColumn
hh3cNATMaxDynamicPortblock = _Hh3cNATMaxDynamicPortblock_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13, 1, 8),
    _Hh3cNATMaxDynamicPortblock_Type()
)
hh3cNATMaxDynamicPortblock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATMaxDynamicPortblock.setStatus("current")
_Hh3cNATMaxStaticPortblock_Type = Unsigned32
_Hh3cNATMaxStaticPortblock_Object = MibTableColumn
hh3cNATMaxStaticPortblock = _Hh3cNATMaxStaticPortblock_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13, 1, 9),
    _Hh3cNATMaxStaticPortblock_Type()
)
hh3cNATMaxStaticPortblock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATMaxStaticPortblock.setStatus("current")
_Hh3cNATActiveDynamicPortblock_Type = Unsigned32
_Hh3cNATActiveDynamicPortblock_Object = MibTableColumn
hh3cNATActiveDynamicPortblock = _Hh3cNATActiveDynamicPortblock_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13, 1, 10),
    _Hh3cNATActiveDynamicPortblock_Type()
)
hh3cNATActiveDynamicPortblock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATActiveDynamicPortblock.setStatus("current")
_Hh3cNATActiveStaticPortblock_Type = Unsigned32
_Hh3cNATActiveStaticPortblock_Object = MibTableColumn
hh3cNATActiveStaticPortblock = _Hh3cNATActiveStaticPortblock_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13, 1, 11),
    _Hh3cNATActiveStaticPortblock_Type()
)
hh3cNATActiveStaticPortblock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATActiveStaticPortblock.setStatus("current")
_Hh3cNATSessionCreateRate_Type = Unsigned32
_Hh3cNATSessionCreateRate_Object = MibTableColumn
hh3cNATSessionCreateRate = _Hh3cNATSessionCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13, 1, 12),
    _Hh3cNATSessionCreateRate_Type()
)
hh3cNATSessionCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATSessionCreateRate.setStatus("current")


class _Hh3cNATCurBandwidthRatio_Type(Unsigned32):
    """Custom type hh3cNATCurBandwidthRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cNATCurBandwidthRatio_Type.__name__ = "Unsigned32"
_Hh3cNATCurBandwidthRatio_Object = MibTableColumn
hh3cNATCurBandwidthRatio = _Hh3cNATCurBandwidthRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 13, 1, 13),
    _Hh3cNATCurBandwidthRatio_Type()
)
hh3cNATCurBandwidthRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATCurBandwidthRatio.setStatus("current")
_Hh3cNATAddrGrpStatTable_Object = MibTable
hh3cNATAddrGrpStatTable = _Hh3cNATAddrGrpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 14)
)
if mibBuilder.loadTexts:
    hh3cNATAddrGrpStatTable.setStatus("current")
_Hh3cNATAddrGrpStatTableEntry_Object = MibTableRow
hh3cNATAddrGrpStatTableEntry = _Hh3cNATAddrGrpStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 14, 1)
)
hh3cNATAddrGrpStatTableEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNATAddrGrpStatChassis"),
    (0, "HH3C-NAT-MIB", "hh3cNATAddrGrpStatSlot"),
    (0, "HH3C-NAT-MIB", "hh3cNATAddrGrpStatCPUID"),
    (0, "HH3C-NAT-MIB", "hh3cNATAddrGrpStatAddrGrpNum"),
)
if mibBuilder.loadTexts:
    hh3cNATAddrGrpStatTableEntry.setStatus("current")


class _Hh3cNATAddrGrpStatChassis_Type(Unsigned32):
    """Custom type hh3cNATAddrGrpStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cNATAddrGrpStatChassis_Type.__name__ = "Unsigned32"
_Hh3cNATAddrGrpStatChassis_Object = MibTableColumn
hh3cNATAddrGrpStatChassis = _Hh3cNATAddrGrpStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 14, 1, 1),
    _Hh3cNATAddrGrpStatChassis_Type()
)
hh3cNATAddrGrpStatChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATAddrGrpStatChassis.setStatus("current")


class _Hh3cNATAddrGrpStatSlot_Type(Unsigned32):
    """Custom type hh3cNATAddrGrpStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cNATAddrGrpStatSlot_Type.__name__ = "Unsigned32"
_Hh3cNATAddrGrpStatSlot_Object = MibTableColumn
hh3cNATAddrGrpStatSlot = _Hh3cNATAddrGrpStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 14, 1, 2),
    _Hh3cNATAddrGrpStatSlot_Type()
)
hh3cNATAddrGrpStatSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATAddrGrpStatSlot.setStatus("current")


class _Hh3cNATAddrGrpStatCPUID_Type(Unsigned32):
    """Custom type hh3cNATAddrGrpStatCPUID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cNATAddrGrpStatCPUID_Type.__name__ = "Unsigned32"
_Hh3cNATAddrGrpStatCPUID_Object = MibTableColumn
hh3cNATAddrGrpStatCPUID = _Hh3cNATAddrGrpStatCPUID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 14, 1, 3),
    _Hh3cNATAddrGrpStatCPUID_Type()
)
hh3cNATAddrGrpStatCPUID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATAddrGrpStatCPUID.setStatus("current")


class _Hh3cNATAddrGrpStatAddrGrpNum_Type(Unsigned32):
    """Custom type hh3cNATAddrGrpStatAddrGrpNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cNATAddrGrpStatAddrGrpNum_Type.__name__ = "Unsigned32"
_Hh3cNATAddrGrpStatAddrGrpNum_Object = MibTableColumn
hh3cNATAddrGrpStatAddrGrpNum = _Hh3cNATAddrGrpStatAddrGrpNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 14, 1, 4),
    _Hh3cNATAddrGrpStatAddrGrpNum_Type()
)
hh3cNATAddrGrpStatAddrGrpNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNATAddrGrpStatAddrGrpNum.setStatus("current")
_Hh3cNATAddrGrpStatFailAllocPort_Type = Unsigned32
_Hh3cNATAddrGrpStatFailAllocPort_Object = MibTableColumn
hh3cNATAddrGrpStatFailAllocPort = _Hh3cNATAddrGrpStatFailAllocPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 14, 1, 5),
    _Hh3cNATAddrGrpStatFailAllocPort_Type()
)
hh3cNATAddrGrpStatFailAllocPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATAddrGrpStatFailAllocPort.setStatus("current")
_Hh3cNATAddrGrpStatAddrGrpSessCnt_Type = Counter64
_Hh3cNATAddrGrpStatAddrGrpSessCnt_Object = MibTableColumn
hh3cNATAddrGrpStatAddrGrpSessCnt = _Hh3cNATAddrGrpStatAddrGrpSessCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 14, 1, 6),
    _Hh3cNATAddrGrpStatAddrGrpSessCnt_Type()
)
hh3cNATAddrGrpStatAddrGrpSessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNATAddrGrpStatAddrGrpSessCnt.setStatus("current")
_Hh3cNATBandwidthTraps_ObjectIdentity = ObjectIdentity
hh3cNATBandwidthTraps = _Hh3cNATBandwidthTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 15)
)
_Hh3cNATBandwidthPrefix_ObjectIdentity = ObjectIdentity
hh3cNATBandwidthPrefix = _Hh3cNATBandwidthPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 15, 0)
)
_Hh3cNATBandwidthTrapObjects_ObjectIdentity = ObjectIdentity
hh3cNATBandwidthTrapObjects = _Hh3cNATBandwidthTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 15, 1)
)
_Hh3cNATBandwidthRatio_Type = Unsigned32
_Hh3cNATBandwidthRatio_Object = MibScalar
hh3cNATBandwidthRatio = _Hh3cNATBandwidthRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 15, 1, 1),
    _Hh3cNATBandwidthRatio_Type()
)
hh3cNATBandwidthRatio.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cNATBandwidthRatio.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNATBandwidthRatio.setUnits("percent")


class _Hh3cNATChassis_Type(Unsigned32):
    """Custom type hh3cNATChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cNATChassis_Type.__name__ = "Unsigned32"
_Hh3cNATChassis_Object = MibScalar
hh3cNATChassis = _Hh3cNATChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 15, 1, 2),
    _Hh3cNATChassis_Type()
)
hh3cNATChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cNATChassis.setStatus("current")


class _Hh3cNATSlot_Type(Unsigned32):
    """Custom type hh3cNATSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cNATSlot_Type.__name__ = "Unsigned32"
_Hh3cNATSlot_Object = MibScalar
hh3cNATSlot = _Hh3cNATSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 15, 1, 3),
    _Hh3cNATSlot_Type()
)
hh3cNATSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cNATSlot.setStatus("current")


class _Hh3cNATCpu_Type(Unsigned32):
    """Custom type hh3cNATCpu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cNATCpu_Type.__name__ = "Unsigned32"
_Hh3cNATCpu_Object = MibScalar
hh3cNATCpu = _Hh3cNATCpu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 15, 1, 4),
    _Hh3cNATCpu_Type()
)
hh3cNATCpu.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cNATCpu.setStatus("current")
_Hh3cInstAddrGrpUsgTable_Object = MibTable
hh3cInstAddrGrpUsgTable = _Hh3cInstAddrGrpUsgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 16)
)
if mibBuilder.loadTexts:
    hh3cInstAddrGrpUsgTable.setStatus("current")
_Hh3cInstAddrGrpUsgEntry_Object = MibTableRow
hh3cInstAddrGrpUsgEntry = _Hh3cInstAddrGrpUsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 16, 1)
)
hh3cInstAddrGrpUsgEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cInstAddrUsgInstName"),
    (0, "HH3C-NAT-MIB", "hh3cInstAddrUsgGrpIndex"),
)
if mibBuilder.loadTexts:
    hh3cInstAddrGrpUsgEntry.setStatus("current")


class _Hh3cInstAddrUsgInstName_Type(OctetString):
    """Custom type hh3cInstAddrUsgInstName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cInstAddrUsgInstName_Type.__name__ = "OctetString"
_Hh3cInstAddrUsgInstName_Object = MibTableColumn
hh3cInstAddrUsgInstName = _Hh3cInstAddrUsgInstName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 16, 1, 1),
    _Hh3cInstAddrUsgInstName_Type()
)
hh3cInstAddrUsgInstName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cInstAddrUsgInstName.setStatus("current")


class _Hh3cInstAddrUsgGrpIndex_Type(Unsigned32):
    """Custom type hh3cInstAddrUsgGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_Hh3cInstAddrUsgGrpIndex_Type.__name__ = "Unsigned32"
_Hh3cInstAddrUsgGrpIndex_Object = MibTableColumn
hh3cInstAddrUsgGrpIndex = _Hh3cInstAddrUsgGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 16, 1, 2),
    _Hh3cInstAddrUsgGrpIndex_Type()
)
hh3cInstAddrUsgGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cInstAddrUsgGrpIndex.setStatus("current")


class _Hh3cInstAddrUsgInstIndex_Type(Unsigned32):
    """Custom type hh3cInstAddrUsgInstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Hh3cInstAddrUsgInstIndex_Type.__name__ = "Unsigned32"
_Hh3cInstAddrUsgInstIndex_Object = MibTableColumn
hh3cInstAddrUsgInstIndex = _Hh3cInstAddrUsgInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 16, 1, 3),
    _Hh3cInstAddrUsgInstIndex_Type()
)
hh3cInstAddrUsgInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cInstAddrUsgInstIndex.setStatus("current")


class _Hh3cInstAddrUsgGrpUsage_Type(Unsigned32):
    """Custom type hh3cInstAddrUsgGrpUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cInstAddrUsgGrpUsage_Type.__name__ = "Unsigned32"
_Hh3cInstAddrUsgGrpUsage_Object = MibTableColumn
hh3cInstAddrUsgGrpUsage = _Hh3cInstAddrUsgGrpUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 16, 1, 4),
    _Hh3cInstAddrUsgGrpUsage_Type()
)
hh3cInstAddrUsgGrpUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cInstAddrUsgGrpUsage.setStatus("current")
if mibBuilder.loadTexts:
    hh3cInstAddrUsgGrpUsage.setUnits("percent")


class _Hh3cInstAddrUsgTotalIPCount_Type(Unsigned32):
    """Custom type hh3cInstAddrUsgTotalIPCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Hh3cInstAddrUsgTotalIPCount_Type.__name__ = "Unsigned32"
_Hh3cInstAddrUsgTotalIPCount_Object = MibTableColumn
hh3cInstAddrUsgTotalIPCount = _Hh3cInstAddrUsgTotalIPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 16, 1, 5),
    _Hh3cInstAddrUsgTotalIPCount_Type()
)
hh3cInstAddrUsgTotalIPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cInstAddrUsgTotalIPCount.setStatus("current")


class _Hh3cInstAddrUsgUsedIPCount_Type(Unsigned32):
    """Custom type hh3cInstAddrUsgUsedIPCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Hh3cInstAddrUsgUsedIPCount_Type.__name__ = "Unsigned32"
_Hh3cInstAddrUsgUsedIPCount_Object = MibTableColumn
hh3cInstAddrUsgUsedIPCount = _Hh3cInstAddrUsgUsedIPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 16, 1, 6),
    _Hh3cInstAddrUsgUsedIPCount_Type()
)
hh3cInstAddrUsgUsedIPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cInstAddrUsgUsedIPCount.setStatus("current")


class _Hh3cInstAddrUsgUnusedIPCount_Type(Unsigned32):
    """Custom type hh3cInstAddrUsgUnusedIPCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Hh3cInstAddrUsgUnusedIPCount_Type.__name__ = "Unsigned32"
_Hh3cInstAddrUsgUnusedIPCount_Object = MibTableColumn
hh3cInstAddrUsgUnusedIPCount = _Hh3cInstAddrUsgUnusedIPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 16, 1, 7),
    _Hh3cInstAddrUsgUnusedIPCount_Type()
)
hh3cInstAddrUsgUnusedIPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cInstAddrUsgUnusedIPCount.setStatus("current")
if mibBuilder.loadTexts:
    hh3cInstAddrUsgUnusedIPCount.setUnits("percent")
_Hh3cInstAddrGrpMemberUsgTable_Object = MibTable
hh3cInstAddrGrpMemberUsgTable = _Hh3cInstAddrGrpMemberUsgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 17)
)
if mibBuilder.loadTexts:
    hh3cInstAddrGrpMemberUsgTable.setStatus("current")
_Hh3cInstAddrGrpMemberUsgEntry_Object = MibTableRow
hh3cInstAddrGrpMemberUsgEntry = _Hh3cInstAddrGrpMemberUsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 17, 1)
)
hh3cInstAddrGrpMemberUsgEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cInstAddrMemUsgInstName"),
    (0, "HH3C-NAT-MIB", "hh3cInstAddrMemUsgGrpIndex"),
    (0, "HH3C-NAT-MIB", "hh3cInstAddrMemUsgGrpStartIP"),
)
if mibBuilder.loadTexts:
    hh3cInstAddrGrpMemberUsgEntry.setStatus("current")


class _Hh3cInstAddrMemUsgInstName_Type(OctetString):
    """Custom type hh3cInstAddrMemUsgInstName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cInstAddrMemUsgInstName_Type.__name__ = "OctetString"
_Hh3cInstAddrMemUsgInstName_Object = MibTableColumn
hh3cInstAddrMemUsgInstName = _Hh3cInstAddrMemUsgInstName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 17, 1, 1),
    _Hh3cInstAddrMemUsgInstName_Type()
)
hh3cInstAddrMemUsgInstName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cInstAddrMemUsgInstName.setStatus("current")


class _Hh3cInstAddrMemUsgGrpIndex_Type(Unsigned32):
    """Custom type hh3cInstAddrMemUsgGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_Hh3cInstAddrMemUsgGrpIndex_Type.__name__ = "Unsigned32"
_Hh3cInstAddrMemUsgGrpIndex_Object = MibTableColumn
hh3cInstAddrMemUsgGrpIndex = _Hh3cInstAddrMemUsgGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 17, 1, 2),
    _Hh3cInstAddrMemUsgGrpIndex_Type()
)
hh3cInstAddrMemUsgGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cInstAddrMemUsgGrpIndex.setStatus("current")
_Hh3cInstAddrMemUsgGrpStartIP_Type = IpAddress
_Hh3cInstAddrMemUsgGrpStartIP_Object = MibTableColumn
hh3cInstAddrMemUsgGrpStartIP = _Hh3cInstAddrMemUsgGrpStartIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 17, 1, 3),
    _Hh3cInstAddrMemUsgGrpStartIP_Type()
)
hh3cInstAddrMemUsgGrpStartIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cInstAddrMemUsgGrpStartIP.setStatus("current")
_Hh3cInstAddrMemUsgGrpEndIP_Type = IpAddress
_Hh3cInstAddrMemUsgGrpEndIP_Object = MibTableColumn
hh3cInstAddrMemUsgGrpEndIP = _Hh3cInstAddrMemUsgGrpEndIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 17, 1, 4),
    _Hh3cInstAddrMemUsgGrpEndIP_Type()
)
hh3cInstAddrMemUsgGrpEndIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cInstAddrMemUsgGrpEndIP.setStatus("current")


class _Hh3cInstAddrMemUsgInstIndex_Type(Unsigned32):
    """Custom type hh3cInstAddrMemUsgInstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Hh3cInstAddrMemUsgInstIndex_Type.__name__ = "Unsigned32"
_Hh3cInstAddrMemUsgInstIndex_Object = MibTableColumn
hh3cInstAddrMemUsgInstIndex = _Hh3cInstAddrMemUsgInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 17, 1, 5),
    _Hh3cInstAddrMemUsgInstIndex_Type()
)
hh3cInstAddrMemUsgInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cInstAddrMemUsgInstIndex.setStatus("current")


class _Hh3cInstAddrMemUsgGrpUsage_Type(Unsigned32):
    """Custom type hh3cInstAddrMemUsgGrpUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cInstAddrMemUsgGrpUsage_Type.__name__ = "Unsigned32"
_Hh3cInstAddrMemUsgGrpUsage_Object = MibTableColumn
hh3cInstAddrMemUsgGrpUsage = _Hh3cInstAddrMemUsgGrpUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 17, 1, 6),
    _Hh3cInstAddrMemUsgGrpUsage_Type()
)
hh3cInstAddrMemUsgGrpUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cInstAddrMemUsgGrpUsage.setStatus("current")
if mibBuilder.loadTexts:
    hh3cInstAddrMemUsgGrpUsage.setUnits("percent")


class _Hh3cInstAddrMemUsgGrpIPMask_Type(OctetString):
    """Custom type hh3cInstAddrMemUsgGrpIPMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cInstAddrMemUsgGrpIPMask_Type.__name__ = "OctetString"
_Hh3cInstAddrMemUsgGrpIPMask_Object = MibTableColumn
hh3cInstAddrMemUsgGrpIPMask = _Hh3cInstAddrMemUsgGrpIPMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 17, 1, 7),
    _Hh3cInstAddrMemUsgGrpIPMask_Type()
)
hh3cInstAddrMemUsgGrpIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cInstAddrMemUsgGrpIPMask.setStatus("current")
_Hh3cInstAddrGrpUsageTraps_ObjectIdentity = ObjectIdentity
hh3cInstAddrGrpUsageTraps = _Hh3cInstAddrGrpUsageTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 18)
)
_Hh3cInstAddrGrpUsagePrefix_ObjectIdentity = ObjectIdentity
hh3cInstAddrGrpUsagePrefix = _Hh3cInstAddrGrpUsagePrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 18, 0)
)
_Hh3cInstAddrGrpUsageTrapInfo_ObjectIdentity = ObjectIdentity
hh3cInstAddrGrpUsageTrapInfo = _Hh3cInstAddrGrpUsageTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 18, 1)
)


class _Hh3cInstAddrTrapInstName_Type(DisplayString):
    """Custom type hh3cInstAddrTrapInstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cInstAddrTrapInstName_Type.__name__ = "DisplayString"
_Hh3cInstAddrTrapInstName_Object = MibScalar
hh3cInstAddrTrapInstName = _Hh3cInstAddrTrapInstName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 18, 1, 1),
    _Hh3cInstAddrTrapInstName_Type()
)
hh3cInstAddrTrapInstName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cInstAddrTrapInstName.setStatus("current")


class _Hh3cInstAddrTrapGrpIndex_Type(Unsigned32):
    """Custom type hh3cInstAddrTrapGrpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_Hh3cInstAddrTrapGrpIndex_Type.__name__ = "Unsigned32"
_Hh3cInstAddrTrapGrpIndex_Object = MibScalar
hh3cInstAddrTrapGrpIndex = _Hh3cInstAddrTrapGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 18, 1, 2),
    _Hh3cInstAddrTrapGrpIndex_Type()
)
hh3cInstAddrTrapGrpIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cInstAddrTrapGrpIndex.setStatus("current")


class _Hh3cInstAddrTrapInstIndex_Type(Unsigned32):
    """Custom type hh3cInstAddrTrapInstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Hh3cInstAddrTrapInstIndex_Type.__name__ = "Unsigned32"
_Hh3cInstAddrTrapInstIndex_Object = MibScalar
hh3cInstAddrTrapInstIndex = _Hh3cInstAddrTrapInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 18, 1, 3),
    _Hh3cInstAddrTrapInstIndex_Type()
)
hh3cInstAddrTrapInstIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cInstAddrTrapInstIndex.setStatus("current")


class _Hh3cInstAddrTrapUsgThreshold_Type(Unsigned32):
    """Custom type hh3cInstAddrTrapUsgThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cInstAddrTrapUsgThreshold_Type.__name__ = "Unsigned32"
_Hh3cInstAddrTrapUsgThreshold_Object = MibScalar
hh3cInstAddrTrapUsgThreshold = _Hh3cInstAddrTrapUsgThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 18, 1, 4),
    _Hh3cInstAddrTrapUsgThreshold_Type()
)
hh3cInstAddrTrapUsgThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cInstAddrTrapUsgThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cInstAddrTrapUsgThreshold.setUnits("percent")
_Hh3cNatIPPoolGroupTable_Object = MibTable
hh3cNatIPPoolGroupTable = _Hh3cNatIPPoolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 19)
)
if mibBuilder.loadTexts:
    hh3cNatIPPoolGroupTable.setStatus("current")
_Hh3cNatIPPoolGroupEntry_Object = MibTableRow
hh3cNatIPPoolGroupEntry = _Hh3cNatIPPoolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 19, 1)
)
hh3cNatIPPoolGroupEntry.setIndexNames(
    (0, "HH3C-NAT-MIB", "hh3cNatIPPoolName"),
)
if mibBuilder.loadTexts:
    hh3cNatIPPoolGroupEntry.setStatus("current")


class _Hh3cNatIPPoolName_Type(OctetString):
    """Custom type hh3cNatIPPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cNatIPPoolName_Type.__name__ = "OctetString"
_Hh3cNatIPPoolName_Object = MibTableColumn
hh3cNatIPPoolName = _Hh3cNatIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 19, 1, 1),
    _Hh3cNatIPPoolName_Type()
)
hh3cNatIPPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNatIPPoolName.setStatus("current")


class _Hh3cNatIPPoolAddrUsage_Type(Unsigned32):
    """Custom type hh3cNatIPPoolAddrUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cNatIPPoolAddrUsage_Type.__name__ = "Unsigned32"
_Hh3cNatIPPoolAddrUsage_Object = MibTableColumn
hh3cNatIPPoolAddrUsage = _Hh3cNatIPPoolAddrUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 19, 1, 2),
    _Hh3cNatIPPoolAddrUsage_Type()
)
hh3cNatIPPoolAddrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNatIPPoolAddrUsage.setStatus("current")


class _Hh3cNatIPPoolTotalCount_Type(Unsigned32):
    """Custom type hh3cNatIPPoolTotalCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Hh3cNatIPPoolTotalCount_Type.__name__ = "Unsigned32"
_Hh3cNatIPPoolTotalCount_Object = MibTableColumn
hh3cNatIPPoolTotalCount = _Hh3cNatIPPoolTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 19, 1, 3),
    _Hh3cNatIPPoolTotalCount_Type()
)
hh3cNatIPPoolTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNatIPPoolTotalCount.setStatus("current")


class _Hh3cNatIPPoolUsedCount_Type(Unsigned32):
    """Custom type hh3cNatIPPoolUsedCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Hh3cNatIPPoolUsedCount_Type.__name__ = "Unsigned32"
_Hh3cNatIPPoolUsedCount_Object = MibTableColumn
hh3cNatIPPoolUsedCount = _Hh3cNatIPPoolUsedCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 19, 1, 4),
    _Hh3cNatIPPoolUsedCount_Type()
)
hh3cNatIPPoolUsedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNatIPPoolUsedCount.setStatus("current")


class _Hh3cNatIPPoolUnusedCount_Type(Unsigned32):
    """Custom type hh3cNatIPPoolUnusedCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Hh3cNatIPPoolUnusedCount_Type.__name__ = "Unsigned32"
_Hh3cNatIPPoolUnusedCount_Object = MibTableColumn
hh3cNatIPPoolUnusedCount = _Hh3cNatIPPoolUnusedCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 19, 1, 5),
    _Hh3cNatIPPoolUnusedCount_Type()
)
hh3cNatIPPoolUnusedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNatIPPoolUnusedCount.setStatus("current")
_Hh3cNatIPPoolAddrUsageExceedTraps_ObjectIdentity = ObjectIdentity
hh3cNatIPPoolAddrUsageExceedTraps = _Hh3cNatIPPoolAddrUsageExceedTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 20)
)
_Hh3cNatIPPoolAddrUsageExceedPrefix_ObjectIdentity = ObjectIdentity
hh3cNatIPPoolAddrUsageExceedPrefix = _Hh3cNatIPPoolAddrUsageExceedPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 20, 0)
)
_Hh3cNatIPPoolAddrUsageTrapExceed_ObjectIdentity = ObjectIdentity
hh3cNatIPPoolAddrUsageTrapExceed = _Hh3cNatIPPoolAddrUsageTrapExceed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 20, 1)
)


class _Hh3cNatTrapIPPoolName_Type(OctetString):
    """Custom type hh3cNatTrapIPPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cNatTrapIPPoolName_Type.__name__ = "OctetString"
_Hh3cNatTrapIPPoolName_Object = MibScalar
hh3cNatTrapIPPoolName = _Hh3cNatTrapIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 20, 1, 1),
    _Hh3cNatTrapIPPoolName_Type()
)
hh3cNatTrapIPPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cNatTrapIPPoolName.setStatus("current")


class _Hh3cNatTrapIPPoolAddrUsage_Type(Unsigned32):
    """Custom type hh3cNatTrapIPPoolAddrUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cNatTrapIPPoolAddrUsage_Type.__name__ = "Unsigned32"
_Hh3cNatTrapIPPoolAddrUsage_Object = MibScalar
hh3cNatTrapIPPoolAddrUsage = _Hh3cNatTrapIPPoolAddrUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 20, 1, 2),
    _Hh3cNatTrapIPPoolAddrUsage_Type()
)
hh3cNatTrapIPPoolAddrUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cNatTrapIPPoolAddrUsage.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cNATBandwidthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 15, 0, 1)
)
hh3cNATBandwidthTrap.setObjects(
      *(("HH3C-NAT-MIB", "hh3cNATBandwidthRatio"),
        ("HH3C-NAT-MIB", "hh3cNATChassis"),
        ("HH3C-NAT-MIB", "hh3cNATSlot"),
        ("HH3C-NAT-MIB", "hh3cNATCpu"))
)
if mibBuilder.loadTexts:
    hh3cNATBandwidthTrap.setStatus(
        "current"
    )

hh3cNATBandwidthRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 15, 0, 2)
)
hh3cNATBandwidthRecoveryTrap.setObjects(
      *(("HH3C-NAT-MIB", "hh3cNATChassis"),
        ("HH3C-NAT-MIB", "hh3cNATSlot"),
        ("HH3C-NAT-MIB", "hh3cNATCpu"))
)
if mibBuilder.loadTexts:
    hh3cNATBandwidthRecoveryTrap.setStatus(
        "current"
    )

hh3cInstAddrGrpUsageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 18, 0, 1)
)
hh3cInstAddrGrpUsageTrap.setObjects(
      *(("HH3C-NAT-MIB", "hh3cInstAddrTrapInstName"),
        ("HH3C-NAT-MIB", "hh3cInstAddrTrapGrpIndex"),
        ("HH3C-NAT-MIB", "hh3cInstAddrTrapInstIndex"),
        ("HH3C-NAT-MIB", "hh3cInstAddrTrapUsgThreshold"))
)
if mibBuilder.loadTexts:
    hh3cInstAddrGrpUsageTrap.setStatus(
        "current"
    )

hh3cInstAddrGrpUsageRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 18, 0, 2)
)
hh3cInstAddrGrpUsageRecovTrap.setObjects(
      *(("HH3C-NAT-MIB", "hh3cInstAddrTrapInstName"),
        ("HH3C-NAT-MIB", "hh3cInstAddrTrapGrpIndex"),
        ("HH3C-NAT-MIB", "hh3cInstAddrTrapInstIndex"))
)
if mibBuilder.loadTexts:
    hh3cInstAddrGrpUsageRecovTrap.setStatus(
        "current"
    )

hh3cNatIPPoolAddrUsageExceedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 20, 0, 1)
)
hh3cNatIPPoolAddrUsageExceedTrap.setObjects(
      *(("HH3C-NAT-MIB", "hh3cNatTrapIPPoolName"),
        ("HH3C-NAT-MIB", "hh3cNatTrapIPPoolAddrUsage"))
)
if mibBuilder.loadTexts:
    hh3cNatIPPoolAddrUsageExceedTrap.setStatus(
        "current"
    )

hh3cNatIPPoolAddrUsageRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 18, 2, 20, 0, 2)
)
hh3cNatIPPoolAddrUsageRecoveryTrap.setObjects(
      *(("HH3C-NAT-MIB", "hh3cNatTrapIPPoolName"),
        ("HH3C-NAT-MIB", "hh3cNatTrapIPPoolAddrUsage"))
)
if mibBuilder.loadTexts:
    hh3cNatIPPoolAddrUsageRecoveryTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-NAT-MIB",
    **{"hh3cNat": hh3cNat,
       "hh3cNATGlobalVars": hh3cNATGlobalVars,
       "hh3cNATClearSession": hh3cNATClearSession,
       "hh3cNATClearSessionSlotNo": hh3cNATClearSessionSlotNo,
       "hh3cNATBLConnectLimitPara": hh3cNATBLConnectLimitPara,
       "hh3cNATBLConnectHighValue": hh3cNATBLConnectHighValue,
       "hh3cNATBLConnectLowValue": hh3cNATBLConnectLowValue,
       "hh3cNATBLConnectHighRate": hh3cNATBLConnectHighRate,
       "hh3cNATBLConnectLowRate": hh3cNATBLConnectLowRate,
       "hh3cNATBLSpecialConnectHighRate": hh3cNATBLSpecialConnectHighRate,
       "hh3cNATBLSpecialConnectLowRate": hh3cNATBLSpecialConnectLowRate,
       "hh3cNATBLCtrlEnable": hh3cNATBLCtrlEnable,
       "hh3cNATBLConnectSumEnable": hh3cNATBLConnectSumEnable,
       "hh3cNATBLConnectRateEnable": hh3cNATBLConnectRateEnable,
       "hh3cNATNPTimer": hh3cNATNPTimer,
       "hh3cNATNPAgingTime": hh3cNATNPAgingTime,
       "hh3cNATMibObjects": hh3cNATMibObjects,
       "hh3cNATPoolInfoTable": hh3cNATPoolInfoTable,
       "hh3cNATPoolInfoEntry": hh3cNATPoolInfoEntry,
       "hh3cNATPoolIdx": hh3cNATPoolIdx,
       "hh3cNATPoolStartIpAddr": hh3cNATPoolStartIpAddr,
       "hh3cNATPoolEndIpAddr": hh3cNATPoolEndIpAddr,
       "hh3cNATPoolSlotNo": hh3cNATPoolSlotNo,
       "hh3cNATPoolRefCounter": hh3cNATPoolRefCounter,
       "hh3cNATPoolRowStatus": hh3cNATPoolRowStatus,
       "hh3cNATOutboundTable": hh3cNATOutboundTable,
       "hh3cNATOutboundEntry": hh3cNATOutboundEntry,
       "hh3cNATOutboundAclNo": hh3cNATOutboundAclNo,
       "hh3cNATOutboundPoolIdx": hh3cNATOutboundPoolIdx,
       "hh3cNATOutboundIsNoPat": hh3cNATOutboundIsNoPat,
       "hh3cNATOutboundSlotNo": hh3cNATOutboundSlotNo,
       "hh3cNATOutboundRowStatus": hh3cNATOutboundRowStatus,
       "hh3cNATServerTable": hh3cNATServerTable,
       "hh3cNATServerEntry": hh3cNATServerEntry,
       "hh3cNATServerProType": hh3cNATServerProType,
       "hh3cNATServerGlobalIP": hh3cNATServerGlobalIP,
       "hh3cNATServerStartGlobalPort": hh3cNATServerStartGlobalPort,
       "hh3cNATServerEndGlobalPort": hh3cNATServerEndGlobalPort,
       "hh3cNATServerStartInsideIP": hh3cNATServerStartInsideIP,
       "hh3cNATServerEndInsideIP": hh3cNATServerEndInsideIP,
       "hh3cNATServerInsidePort": hh3cNATServerInsidePort,
       "hh3cNATServerSlotNo": hh3cNATServerSlotNo,
       "hh3cNATServerVpnIndex": hh3cNATServerVpnIndex,
       "hh3cNATServerAclNumber": hh3cNATServerAclNumber,
       "hh3cNATServerRowStatus": hh3cNATServerRowStatus,
       "hh3cNATTimeOutTable": hh3cNATTimeOutTable,
       "hh3cNATTimeOutEntry": hh3cNATTimeOutEntry,
       "hh3cNATTimeOutProtocol": hh3cNATTimeOutProtocol,
       "hh3cNATTimeOutTimeValue": hh3cNATTimeOutTimeValue,
       "hh3cNATBLEnableTable": hh3cNATBLEnableTable,
       "hh3cNATBLEnableEntry": hh3cNATBLEnableEntry,
       "hh3cNATBLEnableSlotNo": hh3cNATBLEnableSlotNo,
       "hh3cNATBLEnable": hh3cNATBLEnable,
       "hh3cNATBLIPConnectLimitParaTable": hh3cNATBLIPConnectLimitParaTable,
       "hh3cNATBLIPConnectLimitParaEntry": hh3cNATBLIPConnectLimitParaEntry,
       "hh3cNATBLIPConnectLimitParaIP": hh3cNATBLIPConnectLimitParaIP,
       "hh3cNATBLIPConnectHighValue": hh3cNATBLIPConnectHighValue,
       "hh3cNATBLIPConnectLowValue": hh3cNATBLIPConnectLowValue,
       "hh3cNATBLIPUseSpecialConnectRate": hh3cNATBLIPUseSpecialConnectRate,
       "hh3cNATBLIPConnectLimitRowStatus": hh3cNATBLIPConnectLimitRowStatus,
       "hh3cNATBLManagerTable": hh3cNATBLManagerTable,
       "hh3cNATBLManagerEntry": hh3cNATBLManagerEntry,
       "hh3cNATBLIpAdress": hh3cNATBLIpAdress,
       "hh3cNATBLSlotNo": hh3cNATBLSlotNo,
       "hh3cNATBLConSum": hh3cNATBLConSum,
       "hh3cNATBLConSpd": hh3cNATBLConSpd,
       "hh3cNATStatTable": hh3cNATStatTable,
       "hh3cNATStatEntry": hh3cNATStatEntry,
       "hh3cNATStatNATBoardNo": hh3cNATStatNATBoardNo,
       "hh3cNATStatActiveTblCount": hh3cNATStatActiveTblCount,
       "hh3cNATStatActiveTblCountInNP": hh3cNATStatActiveTblCountInNP,
       "hh3cNATStatActiveNatTblCount": hh3cNATStatActiveNatTblCount,
       "hh3cNATStatActiveSvrTblCount": hh3cNATStatActiveSvrTblCount,
       "hh3cNATStatActivePoolTblCount": hh3cNATStatActivePoolTblCount,
       "hh3cNATStatNumOfUsedPort": hh3cNATStatNumOfUsedPort,
       "hh3cNATStatNumOfGoodPkt": hh3cNATStatNumOfGoodPkt,
       "hh3cNATStatNumOfBadPkt": hh3cNATStatNumOfBadPkt,
       "hh3cNATStaticSessionCount": hh3cNATStaticSessionCount,
       "hh3cNATFragmentSessionCount": hh3cNATFragmentSessionCount,
       "hh3cNATSequenceSessionCount": hh3cNATSequenceSessionCount,
       "hh3cNATLogCount": hh3cNATLogCount,
       "hh3cNATSessionTable": hh3cNATSessionTable,
       "hh3cNATSessionEntry": hh3cNATSessionEntry,
       "hh3cNATSessionHashNumber": hh3cNATSessionHashNumber,
       "hh3cNATSessionProtocol": hh3cNATSessionProtocol,
       "hh3cNATSessionGlobalIP": hh3cNATSessionGlobalIP,
       "hh3cNATSessionGlobalPort": hh3cNATSessionGlobalPort,
       "hh3cNATSessionInsideIP": hh3cNATSessionInsideIP,
       "hh3cNATSessionInsidePort": hh3cNATSessionInsidePort,
       "hh3cNATSessionPeerIP": hh3cNATSessionPeerIP,
       "hh3cNATSessionPeerPort": hh3cNATSessionPeerPort,
       "hh3cNATSessionVpnIndex": hh3cNATSessionVpnIndex,
       "hh3cNATSessionTTL": hh3cNATSessionTTL,
       "hh3cNATSessionStatus": hh3cNATSessionStatus,
       "hh3cNATSessionLeftTime": hh3cNATSessionLeftTime,
       "hh3cNATStaticConfTable": hh3cNATStaticConfTable,
       "hh3cNATStaticConfEntry": hh3cNATStaticConfEntry,
       "hh3cNATStaticInsideIp": hh3cNATStaticInsideIp,
       "hh3cNATStaticGlobalIp": hh3cNATStaticGlobalIp,
       "hh3cNATStaticRowStatus": hh3cNATStaticRowStatus,
       "hh3cNATStaticEnableTable": hh3cNATStaticEnableTable,
       "hh3cNATStaticEnableEntry": hh3cNATStaticEnableEntry,
       "hh3cNATStaticEnable": hh3cNATStaticEnable,
       "hh3cNATDnsMapTable": hh3cNATDnsMapTable,
       "hh3cNATDnsMapEntry": hh3cNATDnsMapEntry,
       "hh3cNATDnsMapDomainName": hh3cNATDnsMapDomainName,
       "hh3cNATDnsMapGlobalIp": hh3cNATDnsMapGlobalIp,
       "hh3cNATDnsMapGlobalPort": hh3cNATDnsMapGlobalPort,
       "hh3cNATDnsMapProtocolType": hh3cNATDnsMapProtocolType,
       "hh3cNATDnsMapLastUseTime": hh3cNATDnsMapLastUseTime,
       "hh3cNATDnsMapRowStatus": hh3cNATDnsMapRowStatus,
       "hh3cNATStatVer2Table": hh3cNATStatVer2Table,
       "hh3cNATStatVer2TableEntry": hh3cNATStatVer2TableEntry,
       "hh3cNATStatChassis": hh3cNATStatChassis,
       "hh3cNATStatSlot": hh3cNATStatSlot,
       "hh3cNATStatCPUID": hh3cNATStatCPUID,
       "hh3cNATTotalNATSessionCount": hh3cNATTotalNATSessionCount,
       "hh3cNATEimTableCount": hh3cNATEimTableCount,
       "hh3cNATInboundNoPATTableCount": hh3cNATInboundNoPATTableCount,
       "hh3cNATOutboundNoPATTableCount": hh3cNATOutboundNoPATTableCount,
       "hh3cNATMaxDynamicPortblock": hh3cNATMaxDynamicPortblock,
       "hh3cNATMaxStaticPortblock": hh3cNATMaxStaticPortblock,
       "hh3cNATActiveDynamicPortblock": hh3cNATActiveDynamicPortblock,
       "hh3cNATActiveStaticPortblock": hh3cNATActiveStaticPortblock,
       "hh3cNATSessionCreateRate": hh3cNATSessionCreateRate,
       "hh3cNATCurBandwidthRatio": hh3cNATCurBandwidthRatio,
       "hh3cNATAddrGrpStatTable": hh3cNATAddrGrpStatTable,
       "hh3cNATAddrGrpStatTableEntry": hh3cNATAddrGrpStatTableEntry,
       "hh3cNATAddrGrpStatChassis": hh3cNATAddrGrpStatChassis,
       "hh3cNATAddrGrpStatSlot": hh3cNATAddrGrpStatSlot,
       "hh3cNATAddrGrpStatCPUID": hh3cNATAddrGrpStatCPUID,
       "hh3cNATAddrGrpStatAddrGrpNum": hh3cNATAddrGrpStatAddrGrpNum,
       "hh3cNATAddrGrpStatFailAllocPort": hh3cNATAddrGrpStatFailAllocPort,
       "hh3cNATAddrGrpStatAddrGrpSessCnt": hh3cNATAddrGrpStatAddrGrpSessCnt,
       "hh3cNATBandwidthTraps": hh3cNATBandwidthTraps,
       "hh3cNATBandwidthPrefix": hh3cNATBandwidthPrefix,
       "hh3cNATBandwidthTrap": hh3cNATBandwidthTrap,
       "hh3cNATBandwidthRecoveryTrap": hh3cNATBandwidthRecoveryTrap,
       "hh3cNATBandwidthTrapObjects": hh3cNATBandwidthTrapObjects,
       "hh3cNATBandwidthRatio": hh3cNATBandwidthRatio,
       "hh3cNATChassis": hh3cNATChassis,
       "hh3cNATSlot": hh3cNATSlot,
       "hh3cNATCpu": hh3cNATCpu,
       "hh3cInstAddrGrpUsgTable": hh3cInstAddrGrpUsgTable,
       "hh3cInstAddrGrpUsgEntry": hh3cInstAddrGrpUsgEntry,
       "hh3cInstAddrUsgInstName": hh3cInstAddrUsgInstName,
       "hh3cInstAddrUsgGrpIndex": hh3cInstAddrUsgGrpIndex,
       "hh3cInstAddrUsgInstIndex": hh3cInstAddrUsgInstIndex,
       "hh3cInstAddrUsgGrpUsage": hh3cInstAddrUsgGrpUsage,
       "hh3cInstAddrUsgTotalIPCount": hh3cInstAddrUsgTotalIPCount,
       "hh3cInstAddrUsgUsedIPCount": hh3cInstAddrUsgUsedIPCount,
       "hh3cInstAddrUsgUnusedIPCount": hh3cInstAddrUsgUnusedIPCount,
       "hh3cInstAddrGrpMemberUsgTable": hh3cInstAddrGrpMemberUsgTable,
       "hh3cInstAddrGrpMemberUsgEntry": hh3cInstAddrGrpMemberUsgEntry,
       "hh3cInstAddrMemUsgInstName": hh3cInstAddrMemUsgInstName,
       "hh3cInstAddrMemUsgGrpIndex": hh3cInstAddrMemUsgGrpIndex,
       "hh3cInstAddrMemUsgGrpStartIP": hh3cInstAddrMemUsgGrpStartIP,
       "hh3cInstAddrMemUsgGrpEndIP": hh3cInstAddrMemUsgGrpEndIP,
       "hh3cInstAddrMemUsgInstIndex": hh3cInstAddrMemUsgInstIndex,
       "hh3cInstAddrMemUsgGrpUsage": hh3cInstAddrMemUsgGrpUsage,
       "hh3cInstAddrMemUsgGrpIPMask": hh3cInstAddrMemUsgGrpIPMask,
       "hh3cInstAddrGrpUsageTraps": hh3cInstAddrGrpUsageTraps,
       "hh3cInstAddrGrpUsagePrefix": hh3cInstAddrGrpUsagePrefix,
       "hh3cInstAddrGrpUsageTrap": hh3cInstAddrGrpUsageTrap,
       "hh3cInstAddrGrpUsageRecovTrap": hh3cInstAddrGrpUsageRecovTrap,
       "hh3cInstAddrGrpUsageTrapInfo": hh3cInstAddrGrpUsageTrapInfo,
       "hh3cInstAddrTrapInstName": hh3cInstAddrTrapInstName,
       "hh3cInstAddrTrapGrpIndex": hh3cInstAddrTrapGrpIndex,
       "hh3cInstAddrTrapInstIndex": hh3cInstAddrTrapInstIndex,
       "hh3cInstAddrTrapUsgThreshold": hh3cInstAddrTrapUsgThreshold,
       "hh3cNatIPPoolGroupTable": hh3cNatIPPoolGroupTable,
       "hh3cNatIPPoolGroupEntry": hh3cNatIPPoolGroupEntry,
       "hh3cNatIPPoolName": hh3cNatIPPoolName,
       "hh3cNatIPPoolAddrUsage": hh3cNatIPPoolAddrUsage,
       "hh3cNatIPPoolTotalCount": hh3cNatIPPoolTotalCount,
       "hh3cNatIPPoolUsedCount": hh3cNatIPPoolUsedCount,
       "hh3cNatIPPoolUnusedCount": hh3cNatIPPoolUnusedCount,
       "hh3cNatIPPoolAddrUsageExceedTraps": hh3cNatIPPoolAddrUsageExceedTraps,
       "hh3cNatIPPoolAddrUsageExceedPrefix": hh3cNatIPPoolAddrUsageExceedPrefix,
       "hh3cNatIPPoolAddrUsageExceedTrap": hh3cNatIPPoolAddrUsageExceedTrap,
       "hh3cNatIPPoolAddrUsageRecoveryTrap": hh3cNatIPPoolAddrUsageRecoveryTrap,
       "hh3cNatIPPoolAddrUsageTrapExceed": hh3cNatIPPoolAddrUsageTrapExceed,
       "hh3cNatTrapIPPoolName": hh3cNatTrapIPPoolName,
       "hh3cNatTrapIPPoolAddrUsage": hh3cNatTrapIPPoolAddrUsage}
)
