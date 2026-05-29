# SNMP MIB module (PRVT-LOAD-BALANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-LOAD-BALANCE-MIB

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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(ipSwitch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "ipSwitch")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

prvtLoadBalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7)
)
if mibBuilder.loadTexts:
    prvtLoadBalMIB.setRevisions(
        ("2010-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrvtLoadBalMtxIndexTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



# MIB Managed Objects in the order of their OIDs

_PrvtLoadBalObjects_ObjectIdentity = ObjectIdentity
prvtLoadBalObjects = _PrvtLoadBalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1)
)


class _PrvtLoadBalDistributionMode_Type(Integer32):
    """Custom type prvtLoadBalDistributionMode based on Integer32"""
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
        *(("disabled", 1),
          ("general", 2),
          ("perPortUserNetwork", 3),
          ("globalNetwork", 4),
          ("globalUser", 5))
    )


_PrvtLoadBalDistributionMode_Type.__name__ = "Integer32"
_PrvtLoadBalDistributionMode_Object = MibScalar
prvtLoadBalDistributionMode = _PrvtLoadBalDistributionMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 1),
    _PrvtLoadBalDistributionMode_Type()
)
prvtLoadBalDistributionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalDistributionMode.setStatus("current")


class _PrvtLoadBalIpV6DistributionMode_Type(Integer32):
    """Custom type prvtLoadBalIpV6DistributionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PrvtLoadBalIpV6DistributionMode_Type.__name__ = "Integer32"
_PrvtLoadBalIpV6DistributionMode_Object = MibScalar
prvtLoadBalIpV6DistributionMode = _PrvtLoadBalIpV6DistributionMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 2),
    _PrvtLoadBalIpV6DistributionMode_Type()
)
prvtLoadBalIpV6DistributionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalIpV6DistributionMode.setStatus("current")


class _PrvtLoadBalSpiDistributionMode_Type(Integer32):
    """Custom type prvtLoadBalSpiDistributionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PrvtLoadBalSpiDistributionMode_Type.__name__ = "Integer32"
_PrvtLoadBalSpiDistributionMode_Object = MibScalar
prvtLoadBalSpiDistributionMode = _PrvtLoadBalSpiDistributionMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 3),
    _PrvtLoadBalSpiDistributionMode_Type()
)
prvtLoadBalSpiDistributionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalSpiDistributionMode.setStatus("current")
_PrvtLoadBalMaxAvailSize_Type = Unsigned32
_PrvtLoadBalMaxAvailSize_Object = MibScalar
prvtLoadBalMaxAvailSize = _PrvtLoadBalMaxAvailSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 5),
    _PrvtLoadBalMaxAvailSize_Type()
)
prvtLoadBalMaxAvailSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLoadBalMaxAvailSize.setStatus("current")
_PrvtLoadBalMtxTable_Object = MibTable
prvtLoadBalMtxTable = _PrvtLoadBalMtxTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 6)
)
if mibBuilder.loadTexts:
    prvtLoadBalMtxTable.setStatus("current")
_PrvtLoadBalMtxEntry_Object = MibTableRow
prvtLoadBalMtxEntry = _PrvtLoadBalMtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 6, 1)
)
prvtLoadBalMtxEntry.setIndexNames(
    (0, "PRVT-LOAD-BALANCE-MIB", "prvtLoadBalMtxIndex"),
)
if mibBuilder.loadTexts:
    prvtLoadBalMtxEntry.setStatus("current")
_PrvtLoadBalMtxIndex_Type = PrvtLoadBalMtxIndexTC
_PrvtLoadBalMtxIndex_Object = MibTableColumn
prvtLoadBalMtxIndex = _PrvtLoadBalMtxIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 6, 1, 1),
    _PrvtLoadBalMtxIndex_Type()
)
prvtLoadBalMtxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtLoadBalMtxIndex.setStatus("current")


class _PrvtLoadBalMtxBuckets_Type(OctetString):
    """Custom type prvtLoadBalMtxBuckets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_PrvtLoadBalMtxBuckets_Type.__name__ = "OctetString"
_PrvtLoadBalMtxBuckets_Object = MibTableColumn
prvtLoadBalMtxBuckets = _PrvtLoadBalMtxBuckets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 6, 1, 2),
    _PrvtLoadBalMtxBuckets_Type()
)
prvtLoadBalMtxBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLoadBalMtxBuckets.setStatus("current")
_PrvtLoadBalMtxSignature_Type = OctetString
_PrvtLoadBalMtxSignature_Object = MibTableColumn
prvtLoadBalMtxSignature = _PrvtLoadBalMtxSignature_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 6, 1, 3),
    _PrvtLoadBalMtxSignature_Type()
)
prvtLoadBalMtxSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLoadBalMtxSignature.setStatus("current")
_PrvtLoadBalIfTable_Object = MibTable
prvtLoadBalIfTable = _PrvtLoadBalIfTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 7)
)
if mibBuilder.loadTexts:
    prvtLoadBalIfTable.setStatus("current")
_PrvtLoadBalIfEntry_Object = MibTableRow
prvtLoadBalIfEntry = _PrvtLoadBalIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 7, 1)
)
prvtLoadBalIfEntry.setIndexNames(
    (0, "PRVT-LOAD-BALANCE-MIB", "prvtLoadBalIfId"),
)
if mibBuilder.loadTexts:
    prvtLoadBalIfEntry.setStatus("current")


class _PrvtLoadBalIfId_Type(Unsigned32):
    """Custom type prvtLoadBalIfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PrvtLoadBalIfId_Type.__name__ = "Unsigned32"
_PrvtLoadBalIfId_Object = MibTableColumn
prvtLoadBalIfId = _PrvtLoadBalIfId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 7, 1, 1),
    _PrvtLoadBalIfId_Type()
)
prvtLoadBalIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtLoadBalIfId.setStatus("current")
_PrvtLoadBalIfRowStatus_Type = RowStatus
_PrvtLoadBalIfRowStatus_Object = MibTableColumn
prvtLoadBalIfRowStatus = _PrvtLoadBalIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 7, 1, 2),
    _PrvtLoadBalIfRowStatus_Type()
)
prvtLoadBalIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLoadBalIfRowStatus.setStatus("current")


class _PrvtLoadBalIfMode_Type(Integer32):
    """Custom type prvtLoadBalIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("user", 2),
          ("sync", 3))
    )


_PrvtLoadBalIfMode_Type.__name__ = "Integer32"
_PrvtLoadBalIfMode_Object = MibTableColumn
prvtLoadBalIfMode = _PrvtLoadBalIfMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 7, 1, 3),
    _PrvtLoadBalIfMode_Type()
)
prvtLoadBalIfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLoadBalIfMode.setStatus("current")
_PrvtLoadBalIfMatrixIndex_Type = PrvtLoadBalMtxIndexTC
_PrvtLoadBalIfMatrixIndex_Object = MibTableColumn
prvtLoadBalIfMatrixIndex = _PrvtLoadBalIfMatrixIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 7, 1, 4),
    _PrvtLoadBalIfMatrixIndex_Type()
)
prvtLoadBalIfMatrixIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLoadBalIfMatrixIndex.setStatus("current")
_PrvtLoadBalUserNtwkSrcIpv4Mask_Type = IpAddress
_PrvtLoadBalUserNtwkSrcIpv4Mask_Object = MibScalar
prvtLoadBalUserNtwkSrcIpv4Mask = _PrvtLoadBalUserNtwkSrcIpv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 8),
    _PrvtLoadBalUserNtwkSrcIpv4Mask_Type()
)
prvtLoadBalUserNtwkSrcIpv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalUserNtwkSrcIpv4Mask.setStatus("current")
_PrvtLoadBalUserNtwkDstIpv4Mask_Type = IpAddress
_PrvtLoadBalUserNtwkDstIpv4Mask_Object = MibScalar
prvtLoadBalUserNtwkDstIpv4Mask = _PrvtLoadBalUserNtwkDstIpv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 9),
    _PrvtLoadBalUserNtwkDstIpv4Mask_Type()
)
prvtLoadBalUserNtwkDstIpv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalUserNtwkDstIpv4Mask.setStatus("current")
_PrvtLoadBalUserNtwkSrcIpv6Mask_Type = Ipv6Address
_PrvtLoadBalUserNtwkSrcIpv6Mask_Object = MibScalar
prvtLoadBalUserNtwkSrcIpv6Mask = _PrvtLoadBalUserNtwkSrcIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 10),
    _PrvtLoadBalUserNtwkSrcIpv6Mask_Type()
)
prvtLoadBalUserNtwkSrcIpv6Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalUserNtwkSrcIpv6Mask.setStatus("current")
_PrvtLoadBalUserNtwkDstIpv6Mask_Type = Ipv6Address
_PrvtLoadBalUserNtwkDstIpv6Mask_Object = MibScalar
prvtLoadBalUserNtwkDstIpv6Mask = _PrvtLoadBalUserNtwkDstIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 11),
    _PrvtLoadBalUserNtwkDstIpv6Mask_Type()
)
prvtLoadBalUserNtwkDstIpv6Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalUserNtwkDstIpv6Mask.setStatus("current")
_PrvtLoadBalSpiMask_Type = Unsigned32
_PrvtLoadBalSpiMask_Object = MibScalar
prvtLoadBalSpiMask = _PrvtLoadBalSpiMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 12),
    _PrvtLoadBalSpiMask_Type()
)
prvtLoadBalSpiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalSpiMask.setStatus("current")
_PrvtLoadBalGeneralSrcIpv4Mask_Type = IpAddress
_PrvtLoadBalGeneralSrcIpv4Mask_Object = MibScalar
prvtLoadBalGeneralSrcIpv4Mask = _PrvtLoadBalGeneralSrcIpv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 13),
    _PrvtLoadBalGeneralSrcIpv4Mask_Type()
)
prvtLoadBalGeneralSrcIpv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalGeneralSrcIpv4Mask.setStatus("current")
_PrvtLoadBalGeneralDstIpv4Mask_Type = IpAddress
_PrvtLoadBalGeneralDstIpv4Mask_Object = MibScalar
prvtLoadBalGeneralDstIpv4Mask = _PrvtLoadBalGeneralDstIpv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 14),
    _PrvtLoadBalGeneralDstIpv4Mask_Type()
)
prvtLoadBalGeneralDstIpv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalGeneralDstIpv4Mask.setStatus("current")
_PrvtLoadBalGeneralSrcIpv6Mask_Type = Ipv6Address
_PrvtLoadBalGeneralSrcIpv6Mask_Object = MibScalar
prvtLoadBalGeneralSrcIpv6Mask = _PrvtLoadBalGeneralSrcIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 15),
    _PrvtLoadBalGeneralSrcIpv6Mask_Type()
)
prvtLoadBalGeneralSrcIpv6Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalGeneralSrcIpv6Mask.setStatus("current")
_PrvtLoadBalGeneralDstIpv6Mask_Type = Ipv6Address
_PrvtLoadBalGeneralDstIpv6Mask_Object = MibScalar
prvtLoadBalGeneralDstIpv6Mask = _PrvtLoadBalGeneralDstIpv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 16),
    _PrvtLoadBalGeneralDstIpv6Mask_Type()
)
prvtLoadBalGeneralDstIpv6Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalGeneralDstIpv6Mask.setStatus("current")
_PrvtLoadBalLastUpdateTime_Type = TimeStamp
_PrvtLoadBalLastUpdateTime_Object = MibScalar
prvtLoadBalLastUpdateTime = _PrvtLoadBalLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 17),
    _PrvtLoadBalLastUpdateTime_Type()
)
prvtLoadBalLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLoadBalLastUpdateTime.setStatus("current")


class _PrvtLoadBalApplyConfiguration_Type(Integer32):
    """Custom type prvtLoadBalApplyConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("apply", 1))
    )


_PrvtLoadBalApplyConfiguration_Type.__name__ = "Integer32"
_PrvtLoadBalApplyConfiguration_Object = MibScalar
prvtLoadBalApplyConfiguration = _PrvtLoadBalApplyConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 18),
    _PrvtLoadBalApplyConfiguration_Type()
)
prvtLoadBalApplyConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalApplyConfiguration.setStatus("current")
_PrvtLoadBalBladeTable_Object = MibTable
prvtLoadBalBladeTable = _PrvtLoadBalBladeTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 19)
)
if mibBuilder.loadTexts:
    prvtLoadBalBladeTable.setStatus("current")
_PrvtLoadBalBladeEntry_Object = MibTableRow
prvtLoadBalBladeEntry = _PrvtLoadBalBladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 19, 1)
)
prvtLoadBalBladeEntry.setIndexNames(
    (0, "PRVT-LOAD-BALANCE-MIB", "prvtLoadBalBladeIndex"),
)
if mibBuilder.loadTexts:
    prvtLoadBalBladeEntry.setStatus("current")


class _PrvtLoadBalBladeIndex_Type(Unsigned32):
    """Custom type prvtLoadBalBladeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_PrvtLoadBalBladeIndex_Type.__name__ = "Unsigned32"
_PrvtLoadBalBladeIndex_Object = MibTableColumn
prvtLoadBalBladeIndex = _PrvtLoadBalBladeIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 19, 1, 1),
    _PrvtLoadBalBladeIndex_Type()
)
prvtLoadBalBladeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtLoadBalBladeIndex.setStatus("current")
_PrvtLoadBalBladeMacAddr_Type = MacAddress
_PrvtLoadBalBladeMacAddr_Object = MibTableColumn
prvtLoadBalBladeMacAddr = _PrvtLoadBalBladeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 19, 1, 3),
    _PrvtLoadBalBladeMacAddr_Type()
)
prvtLoadBalBladeMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLoadBalBladeMacAddr.setStatus("current")
_PrvtLoadBalBaseIpAddr_Type = IpAddress
_PrvtLoadBalBaseIpAddr_Object = MibScalar
prvtLoadBalBaseIpAddr = _PrvtLoadBalBaseIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 20),
    _PrvtLoadBalBaseIpAddr_Type()
)
prvtLoadBalBaseIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalBaseIpAddr.setStatus("current")
_PrvtLoadBalBaseIpAddrMask_Type = IpAddress
_PrvtLoadBalBaseIpAddrMask_Object = MibScalar
prvtLoadBalBaseIpAddrMask = _PrvtLoadBalBaseIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 21),
    _PrvtLoadBalBaseIpAddrMask_Type()
)
prvtLoadBalBaseIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalBaseIpAddrMask.setStatus("current")
_PrvtLoadBalAdminPass_Type = OctetString
_PrvtLoadBalAdminPass_Object = MibScalar
prvtLoadBalAdminPass = _PrvtLoadBalAdminPass_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 22),
    _PrvtLoadBalAdminPass_Type()
)
prvtLoadBalAdminPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalAdminPass.setStatus("current")


class _PrvtLoadBalQsfpPortsMode_Type(Integer32):
    """Custom type prvtLoadBalQsfpPortsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode4x10g", 1),
          ("mode40g", 2))
    )


_PrvtLoadBalQsfpPortsMode_Type.__name__ = "Integer32"
_PrvtLoadBalQsfpPortsMode_Object = MibScalar
prvtLoadBalQsfpPortsMode = _PrvtLoadBalQsfpPortsMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 23),
    _PrvtLoadBalQsfpPortsMode_Type()
)
prvtLoadBalQsfpPortsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalQsfpPortsMode.setStatus("current")
_PrvtLoadBalIfVlanTable_Object = MibTable
prvtLoadBalIfVlanTable = _PrvtLoadBalIfVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 24)
)
if mibBuilder.loadTexts:
    prvtLoadBalIfVlanTable.setStatus("current")
_PrvtLoadBalIfVlanEntry_Object = MibTableRow
prvtLoadBalIfVlanEntry = _PrvtLoadBalIfVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 24, 1)
)
prvtLoadBalIfVlanEntry.setIndexNames(
    (0, "PRVT-LOAD-BALANCE-MIB", "prvtLoadBalIfId"),
    (0, "PRVT-LOAD-BALANCE-MIB", "prvtLoadBalVlanId"),
)
if mibBuilder.loadTexts:
    prvtLoadBalIfVlanEntry.setStatus("current")


class _PrvtLoadBalVlanId_Type(Unsigned32):
    """Custom type prvtLoadBalVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_PrvtLoadBalVlanId_Type.__name__ = "Unsigned32"
_PrvtLoadBalVlanId_Object = MibTableColumn
prvtLoadBalVlanId = _PrvtLoadBalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 24, 1, 1),
    _PrvtLoadBalVlanId_Type()
)
prvtLoadBalVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtLoadBalVlanId.setStatus("current")
_PrvtLoadBalIfVlanRowStatus_Type = RowStatus
_PrvtLoadBalIfVlanRowStatus_Object = MibTableColumn
prvtLoadBalIfVlanRowStatus = _PrvtLoadBalIfVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 24, 1, 2),
    _PrvtLoadBalIfVlanRowStatus_Type()
)
prvtLoadBalIfVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLoadBalIfVlanRowStatus.setStatus("current")


class _PrvtLoadBalIfVlanMode_Type(Integer32):
    """Custom type prvtLoadBalIfVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("user", 2))
    )


_PrvtLoadBalIfVlanMode_Type.__name__ = "Integer32"
_PrvtLoadBalIfVlanMode_Object = MibTableColumn
prvtLoadBalIfVlanMode = _PrvtLoadBalIfVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 24, 1, 3),
    _PrvtLoadBalIfVlanMode_Type()
)
prvtLoadBalIfVlanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLoadBalIfVlanMode.setStatus("current")
_PrvtLoadBalIfVlanMatrixIndex_Type = PrvtLoadBalMtxIndexTC
_PrvtLoadBalIfVlanMatrixIndex_Object = MibTableColumn
prvtLoadBalIfVlanMatrixIndex = _PrvtLoadBalIfVlanMatrixIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 24, 1, 4),
    _PrvtLoadBalIfVlanMatrixIndex_Type()
)
prvtLoadBalIfVlanMatrixIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLoadBalIfVlanMatrixIndex.setStatus("current")


class _PrvtLoadBalLoseLessMode_Type(Integer32):
    """Custom type prvtLoadBalLoseLessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("mode1to64", 0),
          ("mode1to32", 1),
          ("mode1to16", 2),
          ("mode1to8", 3),
          ("mode1to4", 4),
          ("mode1to2", 5),
          ("mode1", 6),
          ("mode2", 7),
          ("mode4", 8),
          ("mode8", 9))
    )


_PrvtLoadBalLoseLessMode_Type.__name__ = "Integer32"
_PrvtLoadBalLoseLessMode_Object = MibScalar
prvtLoadBalLoseLessMode = _PrvtLoadBalLoseLessMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 25),
    _PrvtLoadBalLoseLessMode_Type()
)
prvtLoadBalLoseLessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLoadBalLoseLessMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-LOAD-BALANCE-MIB",
    **{"PrvtLoadBalMtxIndexTC": PrvtLoadBalMtxIndexTC,
       "prvtLoadBalMIB": prvtLoadBalMIB,
       "prvtLoadBalObjects": prvtLoadBalObjects,
       "prvtLoadBalDistributionMode": prvtLoadBalDistributionMode,
       "prvtLoadBalIpV6DistributionMode": prvtLoadBalIpV6DistributionMode,
       "prvtLoadBalSpiDistributionMode": prvtLoadBalSpiDistributionMode,
       "prvtLoadBalMaxAvailSize": prvtLoadBalMaxAvailSize,
       "prvtLoadBalMtxTable": prvtLoadBalMtxTable,
       "prvtLoadBalMtxEntry": prvtLoadBalMtxEntry,
       "prvtLoadBalMtxIndex": prvtLoadBalMtxIndex,
       "prvtLoadBalMtxBuckets": prvtLoadBalMtxBuckets,
       "prvtLoadBalMtxSignature": prvtLoadBalMtxSignature,
       "prvtLoadBalIfTable": prvtLoadBalIfTable,
       "prvtLoadBalIfEntry": prvtLoadBalIfEntry,
       "prvtLoadBalIfId": prvtLoadBalIfId,
       "prvtLoadBalIfRowStatus": prvtLoadBalIfRowStatus,
       "prvtLoadBalIfMode": prvtLoadBalIfMode,
       "prvtLoadBalIfMatrixIndex": prvtLoadBalIfMatrixIndex,
       "prvtLoadBalUserNtwkSrcIpv4Mask": prvtLoadBalUserNtwkSrcIpv4Mask,
       "prvtLoadBalUserNtwkDstIpv4Mask": prvtLoadBalUserNtwkDstIpv4Mask,
       "prvtLoadBalUserNtwkSrcIpv6Mask": prvtLoadBalUserNtwkSrcIpv6Mask,
       "prvtLoadBalUserNtwkDstIpv6Mask": prvtLoadBalUserNtwkDstIpv6Mask,
       "prvtLoadBalSpiMask": prvtLoadBalSpiMask,
       "prvtLoadBalGeneralSrcIpv4Mask": prvtLoadBalGeneralSrcIpv4Mask,
       "prvtLoadBalGeneralDstIpv4Mask": prvtLoadBalGeneralDstIpv4Mask,
       "prvtLoadBalGeneralSrcIpv6Mask": prvtLoadBalGeneralSrcIpv6Mask,
       "prvtLoadBalGeneralDstIpv6Mask": prvtLoadBalGeneralDstIpv6Mask,
       "prvtLoadBalLastUpdateTime": prvtLoadBalLastUpdateTime,
       "prvtLoadBalApplyConfiguration": prvtLoadBalApplyConfiguration,
       "prvtLoadBalBladeTable": prvtLoadBalBladeTable,
       "prvtLoadBalBladeEntry": prvtLoadBalBladeEntry,
       "prvtLoadBalBladeIndex": prvtLoadBalBladeIndex,
       "prvtLoadBalBladeMacAddr": prvtLoadBalBladeMacAddr,
       "prvtLoadBalBaseIpAddr": prvtLoadBalBaseIpAddr,
       "prvtLoadBalBaseIpAddrMask": prvtLoadBalBaseIpAddrMask,
       "prvtLoadBalAdminPass": prvtLoadBalAdminPass,
       "prvtLoadBalQsfpPortsMode": prvtLoadBalQsfpPortsMode,
       "prvtLoadBalIfVlanTable": prvtLoadBalIfVlanTable,
       "prvtLoadBalIfVlanEntry": prvtLoadBalIfVlanEntry,
       "prvtLoadBalVlanId": prvtLoadBalVlanId,
       "prvtLoadBalIfVlanRowStatus": prvtLoadBalIfVlanRowStatus,
       "prvtLoadBalIfVlanMode": prvtLoadBalIfVlanMode,
       "prvtLoadBalIfVlanMatrixIndex": prvtLoadBalIfVlanMatrixIndex,
       "prvtLoadBalLoseLessMode": prvtLoadBalLoseLessMode}
)
