# SNMP MIB module (AX-VRF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-VRF-MIB

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

(axMib,) = mibBuilder.importSymbols(
    "AX-SMI-MIB",
    "axMib")

(Ipv6Address,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressPrefix")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

axVrf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11)
)
if mibBuilder.loadTexts:
    axVrf.setRevisions(
        ("2014-05-07 00:00",
         "2013-10-03 00:00",
         "2013-06-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxVrfIp_ObjectIdentity = ObjectIdentity
axVrfIp = _AxVrfIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1)
)
_AxVrfIpAddrTable_Object = MibTable
axVrfIpAddrTable = _AxVrfIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    axVrfIpAddrTable.setStatus("current")
_AxVrfIpAddrEntry_Object = MibTableRow
axVrfIpAddrEntry = _AxVrfIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 1, 1)
)
axVrfIpAddrEntry.setIndexNames(
    (0, "AX-VRF-MIB", "axVrfIpAddrVrfIndex"),
    (0, "AX-VRF-MIB", "axVrfIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    axVrfIpAddrEntry.setStatus("current")
_AxVrfIpAddrVrfIndex_Type = Integer32
_AxVrfIpAddrVrfIndex_Object = MibTableColumn
axVrfIpAddrVrfIndex = _AxVrfIpAddrVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 1, 1, 1),
    _AxVrfIpAddrVrfIndex_Type()
)
axVrfIpAddrVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpAddrVrfIndex.setStatus("current")
_AxVrfIpAdEntAddr_Type = IpAddress
_AxVrfIpAdEntAddr_Object = MibTableColumn
axVrfIpAdEntAddr = _AxVrfIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 1, 1, 2),
    _AxVrfIpAdEntAddr_Type()
)
axVrfIpAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpAdEntAddr.setStatus("current")
_AxVrfIpAdEntIfIndex_Type = Integer32
_AxVrfIpAdEntIfIndex_Object = MibTableColumn
axVrfIpAdEntIfIndex = _AxVrfIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 1, 1, 3),
    _AxVrfIpAdEntIfIndex_Type()
)
axVrfIpAdEntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpAdEntIfIndex.setStatus("current")
_AxVrfIpAdEntNetMask_Type = IpAddress
_AxVrfIpAdEntNetMask_Object = MibTableColumn
axVrfIpAdEntNetMask = _AxVrfIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 1, 1, 4),
    _AxVrfIpAdEntNetMask_Type()
)
axVrfIpAdEntNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpAdEntNetMask.setStatus("current")
_AxVrfIpAdEntBcastAddr_Type = Integer32
_AxVrfIpAdEntBcastAddr_Object = MibTableColumn
axVrfIpAdEntBcastAddr = _AxVrfIpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 1, 1, 5),
    _AxVrfIpAdEntBcastAddr_Type()
)
axVrfIpAdEntBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpAdEntBcastAddr.setStatus("current")
_AxVrfIpAdEntReasmMaxSize_Type = Integer32
_AxVrfIpAdEntReasmMaxSize_Object = MibTableColumn
axVrfIpAdEntReasmMaxSize = _AxVrfIpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 1, 1, 6),
    _AxVrfIpAdEntReasmMaxSize_Type()
)
axVrfIpAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpAdEntReasmMaxSize.setStatus("current")
_AxVrfIpAdEntDescr_Type = DisplayString
_AxVrfIpAdEntDescr_Object = MibTableColumn
axVrfIpAdEntDescr = _AxVrfIpAdEntDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 1, 1, 7),
    _AxVrfIpAdEntDescr_Type()
)
axVrfIpAdEntDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpAdEntDescr.setStatus("current")
_AxVrfIpNetToMediaTable_Object = MibTable
axVrfIpNetToMediaTable = _AxVrfIpNetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    axVrfIpNetToMediaTable.setStatus("current")
_AxVrfIpNetToMediaEntry_Object = MibTableRow
axVrfIpNetToMediaEntry = _AxVrfIpNetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 2, 1)
)
axVrfIpNetToMediaEntry.setIndexNames(
    (0, "AX-VRF-MIB", "axVrfIpNetMediaVrfIndex"),
    (0, "AX-VRF-MIB", "axVrfIpNetToMediaIfIndex"),
    (0, "AX-VRF-MIB", "axVrfIpNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    axVrfIpNetToMediaEntry.setStatus("current")
_AxVrfIpNetMediaVrfIndex_Type = Integer32
_AxVrfIpNetMediaVrfIndex_Object = MibTableColumn
axVrfIpNetMediaVrfIndex = _AxVrfIpNetMediaVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 2, 1, 1),
    _AxVrfIpNetMediaVrfIndex_Type()
)
axVrfIpNetMediaVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpNetMediaVrfIndex.setStatus("current")
_AxVrfIpNetToMediaIfIndex_Type = Integer32
_AxVrfIpNetToMediaIfIndex_Object = MibTableColumn
axVrfIpNetToMediaIfIndex = _AxVrfIpNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 2, 1, 2),
    _AxVrfIpNetToMediaIfIndex_Type()
)
axVrfIpNetToMediaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpNetToMediaIfIndex.setStatus("current")
_AxVrfIpNetToMediaPhysAddress_Type = PhysAddress
_AxVrfIpNetToMediaPhysAddress_Object = MibTableColumn
axVrfIpNetToMediaPhysAddress = _AxVrfIpNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 2, 1, 3),
    _AxVrfIpNetToMediaPhysAddress_Type()
)
axVrfIpNetToMediaPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpNetToMediaPhysAddress.setStatus("current")
_AxVrfIpNetToMediaNetAddress_Type = IpAddress
_AxVrfIpNetToMediaNetAddress_Object = MibTableColumn
axVrfIpNetToMediaNetAddress = _AxVrfIpNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 2, 1, 4),
    _AxVrfIpNetToMediaNetAddress_Type()
)
axVrfIpNetToMediaNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpNetToMediaNetAddress.setStatus("current")


class _AxVrfIpNetToMediaType_Type(Integer32):
    """Custom type axVrfIpNetToMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("invalid", 2),
          ("dynamic", 3),
          ("static", 4))
    )


_AxVrfIpNetToMediaType_Type.__name__ = "Integer32"
_AxVrfIpNetToMediaType_Object = MibTableColumn
axVrfIpNetToMediaType = _AxVrfIpNetToMediaType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 2, 1, 5),
    _AxVrfIpNetToMediaType_Type()
)
axVrfIpNetToMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpNetToMediaType.setStatus("current")
_AxVrfIpNetToMediaDescr_Type = DisplayString
_AxVrfIpNetToMediaDescr_Object = MibTableColumn
axVrfIpNetToMediaDescr = _AxVrfIpNetToMediaDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1, 2, 1, 6),
    _AxVrfIpNetToMediaDescr_Type()
)
axVrfIpNetToMediaDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpNetToMediaDescr.setStatus("current")
_AxVrfIpForward_ObjectIdentity = ObjectIdentity
axVrfIpForward = _AxVrfIpForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2)
)
_AxVrfIpFwNoTable_Object = MibTable
axVrfIpFwNoTable = _AxVrfIpFwNoTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    axVrfIpFwNoTable.setStatus("current")
_AxVrfIpFwNoEntry_Object = MibTableRow
axVrfIpFwNoEntry = _AxVrfIpFwNoEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 1, 1)
)
axVrfIpFwNoEntry.setIndexNames(
    (0, "AX-VRF-MIB", "axVrfIpFwNoVRFIndex"),
)
if mibBuilder.loadTexts:
    axVrfIpFwNoEntry.setStatus("current")


class _AxVrfIpFwNoVRFIndex_Type(Integer32):
    """Custom type axVrfIpFwNoVRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AxVrfIpFwNoVRFIndex_Type.__name__ = "Integer32"
_AxVrfIpFwNoVRFIndex_Object = MibTableColumn
axVrfIpFwNoVRFIndex = _AxVrfIpFwNoVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 1, 1, 1),
    _AxVrfIpFwNoVRFIndex_Type()
)
axVrfIpFwNoVRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwNoVRFIndex.setStatus("current")
_AxVrfIpFwNo_Type = Integer32
_AxVrfIpFwNo_Object = MibTableColumn
axVrfIpFwNo = _AxVrfIpFwNo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 1, 1, 2),
    _AxVrfIpFwNo_Type()
)
axVrfIpFwNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwNo.setStatus("current")
_AxVrfIpFwNoDescr_Type = DisplayString
_AxVrfIpFwNoDescr_Object = MibTableColumn
axVrfIpFwNoDescr = _AxVrfIpFwNoDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 1, 1, 3),
    _AxVrfIpFwNoDescr_Type()
)
axVrfIpFwNoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwNoDescr.setStatus("current")
_AxVrfIpFwTable_Object = MibTable
axVrfIpFwTable = _AxVrfIpFwTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2)
)
if mibBuilder.loadTexts:
    axVrfIpFwTable.setStatus("current")
_AxVrfIpFwEntry_Object = MibTableRow
axVrfIpFwEntry = _AxVrfIpFwEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1)
)
axVrfIpFwEntry.setIndexNames(
    (0, "AX-VRF-MIB", "axVrfIpFwVRFIndex"),
    (0, "AX-VRF-MIB", "axVrfIpFwDest"),
    (0, "AX-VRF-MIB", "axVrfIpFwProto"),
    (0, "AX-VRF-MIB", "axVrfIpFwPolicy"),
    (0, "AX-VRF-MIB", "axVrfIpFwNextHop"),
)
if mibBuilder.loadTexts:
    axVrfIpFwEntry.setStatus("current")


class _AxVrfIpFwVRFIndex_Type(Integer32):
    """Custom type axVrfIpFwVRFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AxVrfIpFwVRFIndex_Type.__name__ = "Integer32"
_AxVrfIpFwVRFIndex_Object = MibTableColumn
axVrfIpFwVRFIndex = _AxVrfIpFwVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 1),
    _AxVrfIpFwVRFIndex_Type()
)
axVrfIpFwVRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwVRFIndex.setStatus("current")
_AxVrfIpFwDest_Type = IpAddress
_AxVrfIpFwDest_Object = MibTableColumn
axVrfIpFwDest = _AxVrfIpFwDest_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 2),
    _AxVrfIpFwDest_Type()
)
axVrfIpFwDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwDest.setStatus("current")
_AxVrfIpFwMask_Type = IpAddress
_AxVrfIpFwMask_Object = MibTableColumn
axVrfIpFwMask = _AxVrfIpFwMask_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 3),
    _AxVrfIpFwMask_Type()
)
axVrfIpFwMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwMask.setStatus("current")


class _AxVrfIpFwPolicy_Type(Integer32):
    """Custom type axVrfIpFwPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AxVrfIpFwPolicy_Type.__name__ = "Integer32"
_AxVrfIpFwPolicy_Object = MibTableColumn
axVrfIpFwPolicy = _AxVrfIpFwPolicy_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 4),
    _AxVrfIpFwPolicy_Type()
)
axVrfIpFwPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwPolicy.setStatus("current")
_AxVrfIpFwNextHop_Type = IpAddress
_AxVrfIpFwNextHop_Object = MibTableColumn
axVrfIpFwNextHop = _AxVrfIpFwNextHop_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 5),
    _AxVrfIpFwNextHop_Type()
)
axVrfIpFwNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwNextHop.setStatus("current")
_AxVrfIpFwIfIndex_Type = Integer32
_AxVrfIpFwIfIndex_Object = MibTableColumn
axVrfIpFwIfIndex = _AxVrfIpFwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 6),
    _AxVrfIpFwIfIndex_Type()
)
axVrfIpFwIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwIfIndex.setStatus("current")


class _AxVrfIpFwType_Type(Integer32):
    """Custom type axVrfIpFwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("invalid", 2),
          ("local", 3),
          ("remote", 4))
    )


_AxVrfIpFwType_Type.__name__ = "Integer32"
_AxVrfIpFwType_Object = MibTableColumn
axVrfIpFwType = _AxVrfIpFwType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 7),
    _AxVrfIpFwType_Type()
)
axVrfIpFwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwType.setStatus("current")


class _AxVrfIpFwProto_Type(Integer32):
    """Custom type axVrfIpFwProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("rip", 8),
          ("ospf", 13),
          ("bgp", 14))
    )


_AxVrfIpFwProto_Type.__name__ = "Integer32"
_AxVrfIpFwProto_Object = MibTableColumn
axVrfIpFwProto = _AxVrfIpFwProto_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 8),
    _AxVrfIpFwProto_Type()
)
axVrfIpFwProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwProto.setStatus("current")
_AxVrfIpFwAge_Type = Integer32
_AxVrfIpFwAge_Object = MibTableColumn
axVrfIpFwAge = _AxVrfIpFwAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 9),
    _AxVrfIpFwAge_Type()
)
axVrfIpFwAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwAge.setStatus("current")
_AxVrfIpFwInfo_Type = ObjectIdentifier
_AxVrfIpFwInfo_Object = MibTableColumn
axVrfIpFwInfo = _AxVrfIpFwInfo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 10),
    _AxVrfIpFwInfo_Type()
)
axVrfIpFwInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwInfo.setStatus("current")
_AxVrfIpFwNextHopAS_Type = Integer32
_AxVrfIpFwNextHopAS_Object = MibTableColumn
axVrfIpFwNextHopAS = _AxVrfIpFwNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 11),
    _AxVrfIpFwNextHopAS_Type()
)
axVrfIpFwNextHopAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwNextHopAS.setStatus("current")
_AxVrfIpFwMetric1_Type = Integer32
_AxVrfIpFwMetric1_Object = MibTableColumn
axVrfIpFwMetric1 = _AxVrfIpFwMetric1_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 12),
    _AxVrfIpFwMetric1_Type()
)
axVrfIpFwMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwMetric1.setStatus("current")
_AxVrfIpFwMetric2_Type = Integer32
_AxVrfIpFwMetric2_Object = MibTableColumn
axVrfIpFwMetric2 = _AxVrfIpFwMetric2_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 13),
    _AxVrfIpFwMetric2_Type()
)
axVrfIpFwMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwMetric2.setStatus("current")
_AxVrfIpFwMetric3_Type = Integer32
_AxVrfIpFwMetric3_Object = MibTableColumn
axVrfIpFwMetric3 = _AxVrfIpFwMetric3_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 14),
    _AxVrfIpFwMetric3_Type()
)
axVrfIpFwMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwMetric3.setStatus("current")
_AxVrfIpFwMetric4_Type = Integer32
_AxVrfIpFwMetric4_Object = MibTableColumn
axVrfIpFwMetric4 = _AxVrfIpFwMetric4_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 15),
    _AxVrfIpFwMetric4_Type()
)
axVrfIpFwMetric4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwMetric4.setStatus("current")
_AxVrfIpFwMetric5_Type = Integer32
_AxVrfIpFwMetric5_Object = MibTableColumn
axVrfIpFwMetric5 = _AxVrfIpFwMetric5_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 16),
    _AxVrfIpFwMetric5_Type()
)
axVrfIpFwMetric5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwMetric5.setStatus("current")
_AxVrfIpFwDescr_Type = DisplayString
_AxVrfIpFwDescr_Object = MibTableColumn
axVrfIpFwDescr = _AxVrfIpFwDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 2, 2, 1, 17),
    _AxVrfIpFwDescr_Type()
)
axVrfIpFwDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpFwDescr.setStatus("current")
_AxVrfIpv6_ObjectIdentity = ObjectIdentity
axVrfIpv6 = _AxVrfIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3)
)
_AxVrfIpv6AddrTable_Object = MibTable
axVrfIpv6AddrTable = _AxVrfIpv6AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 1)
)
if mibBuilder.loadTexts:
    axVrfIpv6AddrTable.setStatus("current")
_AxVrfIpv6AddrEntry_Object = MibTableRow
axVrfIpv6AddrEntry = _AxVrfIpv6AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 1, 1)
)
axVrfIpv6AddrEntry.setIndexNames(
    (0, "AX-VRF-MIB", "axVrfIpv6AddrVrfIndex"),
    (0, "AX-VRF-MIB", "axVrfIpv6AddrIfIndex"),
    (0, "AX-VRF-MIB", "axVrfIpv6AddrAddress"),
)
if mibBuilder.loadTexts:
    axVrfIpv6AddrEntry.setStatus("current")
_AxVrfIpv6AddrVrfIndex_Type = Integer32
_AxVrfIpv6AddrVrfIndex_Object = MibTableColumn
axVrfIpv6AddrVrfIndex = _AxVrfIpv6AddrVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 1, 1, 1),
    _AxVrfIpv6AddrVrfIndex_Type()
)
axVrfIpv6AddrVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6AddrVrfIndex.setStatus("current")
_AxVrfIpv6AddrIfIndex_Type = Integer32
_AxVrfIpv6AddrIfIndex_Object = MibTableColumn
axVrfIpv6AddrIfIndex = _AxVrfIpv6AddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 1, 1, 2),
    _AxVrfIpv6AddrIfIndex_Type()
)
axVrfIpv6AddrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6AddrIfIndex.setStatus("current")
_AxVrfIpv6AddrAddress_Type = Ipv6Address
_AxVrfIpv6AddrAddress_Object = MibTableColumn
axVrfIpv6AddrAddress = _AxVrfIpv6AddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 1, 1, 3),
    _AxVrfIpv6AddrAddress_Type()
)
axVrfIpv6AddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6AddrAddress.setStatus("current")
_AxVrfIpv6AddrPfxLength_Type = Integer32
_AxVrfIpv6AddrPfxLength_Object = MibTableColumn
axVrfIpv6AddrPfxLength = _AxVrfIpv6AddrPfxLength_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 1, 1, 4),
    _AxVrfIpv6AddrPfxLength_Type()
)
axVrfIpv6AddrPfxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6AddrPfxLength.setStatus("current")


class _AxVrfIpv6AddrType_Type(Integer32):
    """Custom type axVrfIpv6AddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stateless", 1),
          ("stateful", 2),
          ("unknown", 3))
    )


_AxVrfIpv6AddrType_Type.__name__ = "Integer32"
_AxVrfIpv6AddrType_Object = MibTableColumn
axVrfIpv6AddrType = _AxVrfIpv6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 1, 1, 5),
    _AxVrfIpv6AddrType_Type()
)
axVrfIpv6AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6AddrType.setStatus("current")
_AxVrfIpv6AddrAnycastFlag_Type = TruthValue
_AxVrfIpv6AddrAnycastFlag_Object = MibTableColumn
axVrfIpv6AddrAnycastFlag = _AxVrfIpv6AddrAnycastFlag_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 1, 1, 6),
    _AxVrfIpv6AddrAnycastFlag_Type()
)
axVrfIpv6AddrAnycastFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6AddrAnycastFlag.setStatus("current")


class _AxVrfIpv6AddrStatus_Type(Integer32):
    """Custom type axVrfIpv6AddrStatus based on Integer32"""
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
        *(("preferred", 1),
          ("deprecated", 2),
          ("invalid", 3),
          ("inaccessible", 4),
          ("unknown", 5))
    )


_AxVrfIpv6AddrStatus_Type.__name__ = "Integer32"
_AxVrfIpv6AddrStatus_Object = MibTableColumn
axVrfIpv6AddrStatus = _AxVrfIpv6AddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 1, 1, 7),
    _AxVrfIpv6AddrStatus_Type()
)
axVrfIpv6AddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6AddrStatus.setStatus("current")
_AxVrfIpv6AddrDescr_Type = DisplayString
_AxVrfIpv6AddrDescr_Object = MibTableColumn
axVrfIpv6AddrDescr = _AxVrfIpv6AddrDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 1, 1, 8),
    _AxVrfIpv6AddrDescr_Type()
)
axVrfIpv6AddrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6AddrDescr.setStatus("current")
_AxVrfIpv6AddrPrefixTable_Object = MibTable
axVrfIpv6AddrPrefixTable = _AxVrfIpv6AddrPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 2)
)
if mibBuilder.loadTexts:
    axVrfIpv6AddrPrefixTable.setStatus("current")
_AxVrfIpv6AddrPrefixEntry_Object = MibTableRow
axVrfIpv6AddrPrefixEntry = _AxVrfIpv6AddrPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 2, 1)
)
axVrfIpv6AddrPrefixEntry.setIndexNames(
    (0, "AX-VRF-MIB", "axVrfIpv6AddrPrefixVrfIndex"),
    (0, "AX-VRF-MIB", "axVrfIpv6AddrPrefixIfIndex"),
    (0, "AX-VRF-MIB", "axVrfIpv6AddrPrefix"),
    (0, "AX-VRF-MIB", "axVrfIpv6AddrPrefixLength"),
)
if mibBuilder.loadTexts:
    axVrfIpv6AddrPrefixEntry.setStatus("current")
_AxVrfIpv6AddrPrefixVrfIndex_Type = Integer32
_AxVrfIpv6AddrPrefixVrfIndex_Object = MibTableColumn
axVrfIpv6AddrPrefixVrfIndex = _AxVrfIpv6AddrPrefixVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 2, 1, 1),
    _AxVrfIpv6AddrPrefixVrfIndex_Type()
)
axVrfIpv6AddrPrefixVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axVrfIpv6AddrPrefixVrfIndex.setStatus("current")
_AxVrfIpv6AddrPrefixIfIndex_Type = Integer32
_AxVrfIpv6AddrPrefixIfIndex_Object = MibTableColumn
axVrfIpv6AddrPrefixIfIndex = _AxVrfIpv6AddrPrefixIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 2, 1, 2),
    _AxVrfIpv6AddrPrefixIfIndex_Type()
)
axVrfIpv6AddrPrefixIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axVrfIpv6AddrPrefixIfIndex.setStatus("current")
_AxVrfIpv6AddrPrefix_Type = Ipv6AddressPrefix
_AxVrfIpv6AddrPrefix_Object = MibTableColumn
axVrfIpv6AddrPrefix = _AxVrfIpv6AddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 2, 1, 3),
    _AxVrfIpv6AddrPrefix_Type()
)
axVrfIpv6AddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axVrfIpv6AddrPrefix.setStatus("current")


class _AxVrfIpv6AddrPrefixLength_Type(Integer32):
    """Custom type axVrfIpv6AddrPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AxVrfIpv6AddrPrefixLength_Type.__name__ = "Integer32"
_AxVrfIpv6AddrPrefixLength_Object = MibTableColumn
axVrfIpv6AddrPrefixLength = _AxVrfIpv6AddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 2, 1, 4),
    _AxVrfIpv6AddrPrefixLength_Type()
)
axVrfIpv6AddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axVrfIpv6AddrPrefixLength.setStatus("current")
_AxVrfIpv6AddrPrefixOnLinkFlag_Type = TruthValue
_AxVrfIpv6AddrPrefixOnLinkFlag_Object = MibTableColumn
axVrfIpv6AddrPrefixOnLinkFlag = _AxVrfIpv6AddrPrefixOnLinkFlag_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 2, 1, 5),
    _AxVrfIpv6AddrPrefixOnLinkFlag_Type()
)
axVrfIpv6AddrPrefixOnLinkFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6AddrPrefixOnLinkFlag.setStatus("current")
_AxVrfIpv6AddrPrefixAutonomousFlag_Type = TruthValue
_AxVrfIpv6AddrPrefixAutonomousFlag_Object = MibTableColumn
axVrfIpv6AddrPrefixAutonomousFlag = _AxVrfIpv6AddrPrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 2, 1, 6),
    _AxVrfIpv6AddrPrefixAutonomousFlag_Type()
)
axVrfIpv6AddrPrefixAutonomousFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6AddrPrefixAutonomousFlag.setStatus("current")
_AxVrfIpv6AddrPrefixAdvPreferredLifetime_Type = Unsigned32
_AxVrfIpv6AddrPrefixAdvPreferredLifetime_Object = MibTableColumn
axVrfIpv6AddrPrefixAdvPreferredLifetime = _AxVrfIpv6AddrPrefixAdvPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 2, 1, 7),
    _AxVrfIpv6AddrPrefixAdvPreferredLifetime_Type()
)
axVrfIpv6AddrPrefixAdvPreferredLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6AddrPrefixAdvPreferredLifetime.setStatus("current")
_AxVrfIpv6AddrPrefixAdvValidLifetime_Type = Unsigned32
_AxVrfIpv6AddrPrefixAdvValidLifetime_Object = MibTableColumn
axVrfIpv6AddrPrefixAdvValidLifetime = _AxVrfIpv6AddrPrefixAdvValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 2, 1, 8),
    _AxVrfIpv6AddrPrefixAdvValidLifetime_Type()
)
axVrfIpv6AddrPrefixAdvValidLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6AddrPrefixAdvValidLifetime.setStatus("current")
_AxVrfIpv6NetToMediaTable_Object = MibTable
axVrfIpv6NetToMediaTable = _AxVrfIpv6NetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 3)
)
if mibBuilder.loadTexts:
    axVrfIpv6NetToMediaTable.setStatus("current")
_AxVrfIpv6NetToMediaEntry_Object = MibTableRow
axVrfIpv6NetToMediaEntry = _AxVrfIpv6NetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 3, 1)
)
axVrfIpv6NetToMediaEntry.setIndexNames(
    (0, "AX-VRF-MIB", "axVrfIpv6NetToMediaVrfIndex"),
    (0, "AX-VRF-MIB", "axVrfIpv6NetToMediaIfIndex"),
    (0, "AX-VRF-MIB", "axVrfIpv6NetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    axVrfIpv6NetToMediaEntry.setStatus("current")
_AxVrfIpv6NetToMediaVrfIndex_Type = Integer32
_AxVrfIpv6NetToMediaVrfIndex_Object = MibTableColumn
axVrfIpv6NetToMediaVrfIndex = _AxVrfIpv6NetToMediaVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 3, 1, 1),
    _AxVrfIpv6NetToMediaVrfIndex_Type()
)
axVrfIpv6NetToMediaVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6NetToMediaVrfIndex.setStatus("current")
_AxVrfIpv6NetToMediaIfIndex_Type = Integer32
_AxVrfIpv6NetToMediaIfIndex_Object = MibTableColumn
axVrfIpv6NetToMediaIfIndex = _AxVrfIpv6NetToMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 3, 1, 2),
    _AxVrfIpv6NetToMediaIfIndex_Type()
)
axVrfIpv6NetToMediaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6NetToMediaIfIndex.setStatus("current")
_AxVrfIpv6NetToMediaNetAddress_Type = Ipv6Address
_AxVrfIpv6NetToMediaNetAddress_Object = MibTableColumn
axVrfIpv6NetToMediaNetAddress = _AxVrfIpv6NetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 3, 1, 3),
    _AxVrfIpv6NetToMediaNetAddress_Type()
)
axVrfIpv6NetToMediaNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6NetToMediaNetAddress.setStatus("current")
_AxVrfIpv6NetToMediaPhysAddress_Type = PhysAddress
_AxVrfIpv6NetToMediaPhysAddress_Object = MibTableColumn
axVrfIpv6NetToMediaPhysAddress = _AxVrfIpv6NetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 3, 1, 4),
    _AxVrfIpv6NetToMediaPhysAddress_Type()
)
axVrfIpv6NetToMediaPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6NetToMediaPhysAddress.setStatus("current")


class _AxVrfIpv6NetToMediaType_Type(Integer32):
    """Custom type axVrfIpv6NetToMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dynamic", 2),
          ("static", 3),
          ("local", 4))
    )


_AxVrfIpv6NetToMediaType_Type.__name__ = "Integer32"
_AxVrfIpv6NetToMediaType_Object = MibTableColumn
axVrfIpv6NetToMediaType = _AxVrfIpv6NetToMediaType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 3, 1, 5),
    _AxVrfIpv6NetToMediaType_Type()
)
axVrfIpv6NetToMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6NetToMediaType.setStatus("current")


class _AxVrfIpv6IfNetToMediaState_Type(Integer32):
    """Custom type axVrfIpv6IfNetToMediaState based on Integer32"""
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
        *(("reachable", 1),
          ("stale", 2),
          ("delay", 3),
          ("probe", 4),
          ("invalid", 5),
          ("unknown", 6))
    )


_AxVrfIpv6IfNetToMediaState_Type.__name__ = "Integer32"
_AxVrfIpv6IfNetToMediaState_Object = MibTableColumn
axVrfIpv6IfNetToMediaState = _AxVrfIpv6IfNetToMediaState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 3, 1, 6),
    _AxVrfIpv6IfNetToMediaState_Type()
)
axVrfIpv6IfNetToMediaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6IfNetToMediaState.setStatus("current")
_AxVrfIpv6IfNetToMediaLastUpdated_Type = TimeStamp
_AxVrfIpv6IfNetToMediaLastUpdated_Object = MibTableColumn
axVrfIpv6IfNetToMediaLastUpdated = _AxVrfIpv6IfNetToMediaLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 3, 1, 7),
    _AxVrfIpv6IfNetToMediaLastUpdated_Type()
)
axVrfIpv6IfNetToMediaLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6IfNetToMediaLastUpdated.setStatus("current")
_AxVrfIpv6NetToMediaValid_Type = TruthValue
_AxVrfIpv6NetToMediaValid_Object = MibTableColumn
axVrfIpv6NetToMediaValid = _AxVrfIpv6NetToMediaValid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 3, 1, 8),
    _AxVrfIpv6NetToMediaValid_Type()
)
axVrfIpv6NetToMediaValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6NetToMediaValid.setStatus("current")
_AxVrfIpv6NetToMediaDescr_Type = DisplayString
_AxVrfIpv6NetToMediaDescr_Object = MibTableColumn
axVrfIpv6NetToMediaDescr = _AxVrfIpv6NetToMediaDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 3, 3, 1, 9),
    _AxVrfIpv6NetToMediaDescr_Type()
)
axVrfIpv6NetToMediaDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6NetToMediaDescr.setStatus("current")
_AxVrfIpv6Forward_ObjectIdentity = ObjectIdentity
axVrfIpv6Forward = _AxVrfIpv6Forward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4)
)
_AxVrfIpv6FwNoTable_Object = MibTable
axVrfIpv6FwNoTable = _AxVrfIpv6FwNoTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 1)
)
if mibBuilder.loadTexts:
    axVrfIpv6FwNoTable.setStatus("current")
_AxVrfIpv6FwNoEntry_Object = MibTableRow
axVrfIpv6FwNoEntry = _AxVrfIpv6FwNoEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 1, 1)
)
axVrfIpv6FwNoEntry.setIndexNames(
    (0, "AX-VRF-MIB", "axVrfIpv6FwNoVRFIndex"),
)
if mibBuilder.loadTexts:
    axVrfIpv6FwNoEntry.setStatus("current")
_AxVrfIpv6FwNoVRFIndex_Type = Integer32
_AxVrfIpv6FwNoVRFIndex_Object = MibTableColumn
axVrfIpv6FwNoVRFIndex = _AxVrfIpv6FwNoVRFIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 1, 1, 1),
    _AxVrfIpv6FwNoVRFIndex_Type()
)
axVrfIpv6FwNoVRFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwNoVRFIndex.setStatus("current")
_AxVrfIpv6FwNo_Type = Integer32
_AxVrfIpv6FwNo_Object = MibTableColumn
axVrfIpv6FwNo = _AxVrfIpv6FwNo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 1, 1, 2),
    _AxVrfIpv6FwNo_Type()
)
axVrfIpv6FwNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwNo.setStatus("current")
_AxVrfIpv6FwNoDescr_Type = DisplayString
_AxVrfIpv6FwNoDescr_Object = MibTableColumn
axVrfIpv6FwNoDescr = _AxVrfIpv6FwNoDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 1, 1, 3),
    _AxVrfIpv6FwNoDescr_Type()
)
axVrfIpv6FwNoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwNoDescr.setStatus("current")
_AxVrfIpv6FwTable_Object = MibTable
axVrfIpv6FwTable = _AxVrfIpv6FwTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2)
)
if mibBuilder.loadTexts:
    axVrfIpv6FwTable.setStatus("current")
_AxVrfIpv6FwEntry_Object = MibTableRow
axVrfIpv6FwEntry = _AxVrfIpv6FwEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1)
)
axVrfIpv6FwEntry.setIndexNames(
    (0, "AX-VRF-MIB", "axVrfIpv6FwVrfIndex"),
    (0, "AX-VRF-MIB", "axVrfIpv6FwDest"),
    (0, "AX-VRF-MIB", "axVrfIpv6FwProto"),
    (0, "AX-VRF-MIB", "axVrfIpv6FwPolicy"),
    (0, "AX-VRF-MIB", "axVrfIpv6FwNextHop"),
)
if mibBuilder.loadTexts:
    axVrfIpv6FwEntry.setStatus("current")
_AxVrfIpv6FwVrfIndex_Type = Integer32
_AxVrfIpv6FwVrfIndex_Object = MibTableColumn
axVrfIpv6FwVrfIndex = _AxVrfIpv6FwVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 1),
    _AxVrfIpv6FwVrfIndex_Type()
)
axVrfIpv6FwVrfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwVrfIndex.setStatus("current")
_AxVrfIpv6FwDest_Type = Ipv6Address
_AxVrfIpv6FwDest_Object = MibTableColumn
axVrfIpv6FwDest = _AxVrfIpv6FwDest_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 2),
    _AxVrfIpv6FwDest_Type()
)
axVrfIpv6FwDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwDest.setStatus("current")
_AxVrfIpv6FwPfxLength_Type = Integer32
_AxVrfIpv6FwPfxLength_Object = MibTableColumn
axVrfIpv6FwPfxLength = _AxVrfIpv6FwPfxLength_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 3),
    _AxVrfIpv6FwPfxLength_Type()
)
axVrfIpv6FwPfxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwPfxLength.setStatus("current")
_AxVrfIpv6FwPolicy_Type = Integer32
_AxVrfIpv6FwPolicy_Object = MibTableColumn
axVrfIpv6FwPolicy = _AxVrfIpv6FwPolicy_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 4),
    _AxVrfIpv6FwPolicy_Type()
)
axVrfIpv6FwPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwPolicy.setStatus("current")
_AxVrfIpv6FwNextHop_Type = Ipv6Address
_AxVrfIpv6FwNextHop_Object = MibTableColumn
axVrfIpv6FwNextHop = _AxVrfIpv6FwNextHop_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 5),
    _AxVrfIpv6FwNextHop_Type()
)
axVrfIpv6FwNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwNextHop.setStatus("current")
_AxVrfIpv6FwIfIndex_Type = Integer32
_AxVrfIpv6FwIfIndex_Object = MibTableColumn
axVrfIpv6FwIfIndex = _AxVrfIpv6FwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 6),
    _AxVrfIpv6FwIfIndex_Type()
)
axVrfIpv6FwIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwIfIndex.setStatus("current")


class _AxVrfIpv6FwType_Type(Integer32):
    """Custom type axVrfIpv6FwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("invalid", 2),
          ("local", 3),
          ("remote", 4))
    )


_AxVrfIpv6FwType_Type.__name__ = "Integer32"
_AxVrfIpv6FwType_Object = MibTableColumn
axVrfIpv6FwType = _AxVrfIpv6FwType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 7),
    _AxVrfIpv6FwType_Type()
)
axVrfIpv6FwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwType.setStatus("current")


class _AxVrfIpv6FwProto_Type(Integer32):
    """Custom type axVrfIpv6FwProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("rip", 8),
          ("ospf", 13),
          ("bgp", 14))
    )


_AxVrfIpv6FwProto_Type.__name__ = "Integer32"
_AxVrfIpv6FwProto_Object = MibTableColumn
axVrfIpv6FwProto = _AxVrfIpv6FwProto_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 8),
    _AxVrfIpv6FwProto_Type()
)
axVrfIpv6FwProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwProto.setStatus("current")
_AxVrfIpv6FwAge_Type = Integer32
_AxVrfIpv6FwAge_Object = MibTableColumn
axVrfIpv6FwAge = _AxVrfIpv6FwAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 9),
    _AxVrfIpv6FwAge_Type()
)
axVrfIpv6FwAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwAge.setStatus("current")
_AxVrfIpv6FwInfo_Type = ObjectIdentifier
_AxVrfIpv6FwInfo_Object = MibTableColumn
axVrfIpv6FwInfo = _AxVrfIpv6FwInfo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 10),
    _AxVrfIpv6FwInfo_Type()
)
axVrfIpv6FwInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwInfo.setStatus("current")
_AxVrfIpv6FwNextHopAS_Type = Integer32
_AxVrfIpv6FwNextHopAS_Object = MibTableColumn
axVrfIpv6FwNextHopAS = _AxVrfIpv6FwNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 11),
    _AxVrfIpv6FwNextHopAS_Type()
)
axVrfIpv6FwNextHopAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwNextHopAS.setStatus("current")
_AxVrfIpv6FwMetric1_Type = Integer32
_AxVrfIpv6FwMetric1_Object = MibTableColumn
axVrfIpv6FwMetric1 = _AxVrfIpv6FwMetric1_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 12),
    _AxVrfIpv6FwMetric1_Type()
)
axVrfIpv6FwMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwMetric1.setStatus("current")
_AxVrfIpv6FwMetric2_Type = Integer32
_AxVrfIpv6FwMetric2_Object = MibTableColumn
axVrfIpv6FwMetric2 = _AxVrfIpv6FwMetric2_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 13),
    _AxVrfIpv6FwMetric2_Type()
)
axVrfIpv6FwMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwMetric2.setStatus("current")
_AxVrfIpv6FwMetric3_Type = Integer32
_AxVrfIpv6FwMetric3_Object = MibTableColumn
axVrfIpv6FwMetric3 = _AxVrfIpv6FwMetric3_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 14),
    _AxVrfIpv6FwMetric3_Type()
)
axVrfIpv6FwMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwMetric3.setStatus("current")
_AxVrfIpv6FwMetric4_Type = Integer32
_AxVrfIpv6FwMetric4_Object = MibTableColumn
axVrfIpv6FwMetric4 = _AxVrfIpv6FwMetric4_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 15),
    _AxVrfIpv6FwMetric4_Type()
)
axVrfIpv6FwMetric4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwMetric4.setStatus("current")
_AxVrfIpv6FwMetric5_Type = Integer32
_AxVrfIpv6FwMetric5_Object = MibTableColumn
axVrfIpv6FwMetric5 = _AxVrfIpv6FwMetric5_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 16),
    _AxVrfIpv6FwMetric5_Type()
)
axVrfIpv6FwMetric5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwMetric5.setStatus("current")
_AxVrfIpv6FwDescr_Type = DisplayString
_AxVrfIpv6FwDescr_Object = MibTableColumn
axVrfIpv6FwDescr = _AxVrfIpv6FwDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 4, 2, 1, 17),
    _AxVrfIpv6FwDescr_Type()
)
axVrfIpv6FwDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVrfIpv6FwDescr.setStatus("current")
_AxVrfConformance_ObjectIdentity = ObjectIdentity
axVrfConformance = _AxVrfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1000)
)
_AxVrfCompliances_ObjectIdentity = ObjectIdentity
axVrfCompliances = _AxVrfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1000, 1)
)
_AxVrfGroups_ObjectIdentity = ObjectIdentity
axVrfGroups = _AxVrfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1000, 2)
)

# Managed Objects groups

axVrfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1000, 2, 1)
)
axVrfGroup.setObjects(
      *(("AX-VRF-MIB", "axVrfIpAddrVrfIndex"),
        ("AX-VRF-MIB", "axVrfIpAdEntAddr"),
        ("AX-VRF-MIB", "axVrfIpAdEntIfIndex"),
        ("AX-VRF-MIB", "axVrfIpAdEntNetMask"),
        ("AX-VRF-MIB", "axVrfIpAdEntBcastAddr"),
        ("AX-VRF-MIB", "axVrfIpAdEntReasmMaxSize"),
        ("AX-VRF-MIB", "axVrfIpAdEntDescr"),
        ("AX-VRF-MIB", "axVrfIpNetMediaVrfIndex"),
        ("AX-VRF-MIB", "axVrfIpNetToMediaIfIndex"),
        ("AX-VRF-MIB", "axVrfIpNetToMediaPhysAddress"),
        ("AX-VRF-MIB", "axVrfIpNetToMediaNetAddress"),
        ("AX-VRF-MIB", "axVrfIpNetToMediaType"),
        ("AX-VRF-MIB", "axVrfIpNetToMediaDescr"),
        ("AX-VRF-MIB", "axVrfIpFwNoVRFIndex"),
        ("AX-VRF-MIB", "axVrfIpFwNo"),
        ("AX-VRF-MIB", "axVrfIpFwNoDescr"),
        ("AX-VRF-MIB", "axVrfIpFwVRFIndex"),
        ("AX-VRF-MIB", "axVrfIpFwDest"),
        ("AX-VRF-MIB", "axVrfIpFwMask"),
        ("AX-VRF-MIB", "axVrfIpFwPolicy"),
        ("AX-VRF-MIB", "axVrfIpFwNextHop"),
        ("AX-VRF-MIB", "axVrfIpFwIfIndex"),
        ("AX-VRF-MIB", "axVrfIpFwType"),
        ("AX-VRF-MIB", "axVrfIpFwProto"),
        ("AX-VRF-MIB", "axVrfIpFwAge"),
        ("AX-VRF-MIB", "axVrfIpFwInfo"),
        ("AX-VRF-MIB", "axVrfIpFwNextHopAS"),
        ("AX-VRF-MIB", "axVrfIpFwMetric1"),
        ("AX-VRF-MIB", "axVrfIpFwMetric2"),
        ("AX-VRF-MIB", "axVrfIpFwMetric3"),
        ("AX-VRF-MIB", "axVrfIpFwMetric4"),
        ("AX-VRF-MIB", "axVrfIpFwMetric5"),
        ("AX-VRF-MIB", "axVrfIpFwDescr"),
        ("AX-VRF-MIB", "axVrfIpv6AddrVrfIndex"),
        ("AX-VRF-MIB", "axVrfIpv6AddrIfIndex"),
        ("AX-VRF-MIB", "axVrfIpv6AddrAddress"),
        ("AX-VRF-MIB", "axVrfIpv6AddrPfxLength"),
        ("AX-VRF-MIB", "axVrfIpv6AddrType"),
        ("AX-VRF-MIB", "axVrfIpv6AddrAnycastFlag"),
        ("AX-VRF-MIB", "axVrfIpv6AddrStatus"),
        ("AX-VRF-MIB", "axVrfIpv6AddrDescr"),
        ("AX-VRF-MIB", "axVrfIpv6AddrPrefixOnLinkFlag"),
        ("AX-VRF-MIB", "axVrfIpv6AddrPrefixAutonomousFlag"),
        ("AX-VRF-MIB", "axVrfIpv6AddrPrefixAdvPreferredLifetime"),
        ("AX-VRF-MIB", "axVrfIpv6AddrPrefixAdvValidLifetime"),
        ("AX-VRF-MIB", "axVrfIpv6AddrPrefixOnLinkFlag"),
        ("AX-VRF-MIB", "axVrfIpv6AddrPrefixAutonomousFlag"),
        ("AX-VRF-MIB", "axVrfIpv6AddrPrefixAdvPreferredLifetime"),
        ("AX-VRF-MIB", "axVrfIpv6AddrPrefixAdvValidLifetime"),
        ("AX-VRF-MIB", "axVrfIpv6NetToMediaVrfIndex"),
        ("AX-VRF-MIB", "axVrfIpv6NetToMediaIfIndex"),
        ("AX-VRF-MIB", "axVrfIpv6NetToMediaNetAddress"),
        ("AX-VRF-MIB", "axVrfIpv6NetToMediaPhysAddress"),
        ("AX-VRF-MIB", "axVrfIpv6NetToMediaType"),
        ("AX-VRF-MIB", "axVrfIpv6IfNetToMediaState"),
        ("AX-VRF-MIB", "axVrfIpv6IfNetToMediaLastUpdated"),
        ("AX-VRF-MIB", "axVrfIpv6NetToMediaValid"),
        ("AX-VRF-MIB", "axVrfIpv6NetToMediaDescr"),
        ("AX-VRF-MIB", "axVrfIpv6FwNoVRFIndex"),
        ("AX-VRF-MIB", "axVrfIpv6FwNo"),
        ("AX-VRF-MIB", "axVrfIpv6FwNoDescr"),
        ("AX-VRF-MIB", "axVrfIpv6FwVrfIndex"),
        ("AX-VRF-MIB", "axVrfIpv6FwDest"),
        ("AX-VRF-MIB", "axVrfIpv6FwPfxLength"),
        ("AX-VRF-MIB", "axVrfIpv6FwPolicy"),
        ("AX-VRF-MIB", "axVrfIpv6FwNextHop"),
        ("AX-VRF-MIB", "axVrfIpv6FwIfIndex"),
        ("AX-VRF-MIB", "axVrfIpv6FwType"),
        ("AX-VRF-MIB", "axVrfIpv6FwProto"),
        ("AX-VRF-MIB", "axVrfIpv6FwAge"),
        ("AX-VRF-MIB", "axVrfIpv6FwInfo"),
        ("AX-VRF-MIB", "axVrfIpv6FwNextHopAS"),
        ("AX-VRF-MIB", "axVrfIpv6FwMetric1"),
        ("AX-VRF-MIB", "axVrfIpv6FwMetric2"),
        ("AX-VRF-MIB", "axVrfIpv6FwMetric3"),
        ("AX-VRF-MIB", "axVrfIpv6FwMetric4"),
        ("AX-VRF-MIB", "axVrfIpv6FwMetric5"),
        ("AX-VRF-MIB", "axVrfIpv6FwDescr"))
)
if mibBuilder.loadTexts:
    axVrfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

axVrfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 11, 1000, 1, 1)
)
axVrfCompliance.setObjects(
    ("AX-VRF-MIB", "axVrfGroup")
)
if mibBuilder.loadTexts:
    axVrfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-VRF-MIB",
    **{"axVrf": axVrf,
       "axVrfIp": axVrfIp,
       "axVrfIpAddrTable": axVrfIpAddrTable,
       "axVrfIpAddrEntry": axVrfIpAddrEntry,
       "axVrfIpAddrVrfIndex": axVrfIpAddrVrfIndex,
       "axVrfIpAdEntAddr": axVrfIpAdEntAddr,
       "axVrfIpAdEntIfIndex": axVrfIpAdEntIfIndex,
       "axVrfIpAdEntNetMask": axVrfIpAdEntNetMask,
       "axVrfIpAdEntBcastAddr": axVrfIpAdEntBcastAddr,
       "axVrfIpAdEntReasmMaxSize": axVrfIpAdEntReasmMaxSize,
       "axVrfIpAdEntDescr": axVrfIpAdEntDescr,
       "axVrfIpNetToMediaTable": axVrfIpNetToMediaTable,
       "axVrfIpNetToMediaEntry": axVrfIpNetToMediaEntry,
       "axVrfIpNetMediaVrfIndex": axVrfIpNetMediaVrfIndex,
       "axVrfIpNetToMediaIfIndex": axVrfIpNetToMediaIfIndex,
       "axVrfIpNetToMediaPhysAddress": axVrfIpNetToMediaPhysAddress,
       "axVrfIpNetToMediaNetAddress": axVrfIpNetToMediaNetAddress,
       "axVrfIpNetToMediaType": axVrfIpNetToMediaType,
       "axVrfIpNetToMediaDescr": axVrfIpNetToMediaDescr,
       "axVrfIpForward": axVrfIpForward,
       "axVrfIpFwNoTable": axVrfIpFwNoTable,
       "axVrfIpFwNoEntry": axVrfIpFwNoEntry,
       "axVrfIpFwNoVRFIndex": axVrfIpFwNoVRFIndex,
       "axVrfIpFwNo": axVrfIpFwNo,
       "axVrfIpFwNoDescr": axVrfIpFwNoDescr,
       "axVrfIpFwTable": axVrfIpFwTable,
       "axVrfIpFwEntry": axVrfIpFwEntry,
       "axVrfIpFwVRFIndex": axVrfIpFwVRFIndex,
       "axVrfIpFwDest": axVrfIpFwDest,
       "axVrfIpFwMask": axVrfIpFwMask,
       "axVrfIpFwPolicy": axVrfIpFwPolicy,
       "axVrfIpFwNextHop": axVrfIpFwNextHop,
       "axVrfIpFwIfIndex": axVrfIpFwIfIndex,
       "axVrfIpFwType": axVrfIpFwType,
       "axVrfIpFwProto": axVrfIpFwProto,
       "axVrfIpFwAge": axVrfIpFwAge,
       "axVrfIpFwInfo": axVrfIpFwInfo,
       "axVrfIpFwNextHopAS": axVrfIpFwNextHopAS,
       "axVrfIpFwMetric1": axVrfIpFwMetric1,
       "axVrfIpFwMetric2": axVrfIpFwMetric2,
       "axVrfIpFwMetric3": axVrfIpFwMetric3,
       "axVrfIpFwMetric4": axVrfIpFwMetric4,
       "axVrfIpFwMetric5": axVrfIpFwMetric5,
       "axVrfIpFwDescr": axVrfIpFwDescr,
       "axVrfIpv6": axVrfIpv6,
       "axVrfIpv6AddrTable": axVrfIpv6AddrTable,
       "axVrfIpv6AddrEntry": axVrfIpv6AddrEntry,
       "axVrfIpv6AddrVrfIndex": axVrfIpv6AddrVrfIndex,
       "axVrfIpv6AddrIfIndex": axVrfIpv6AddrIfIndex,
       "axVrfIpv6AddrAddress": axVrfIpv6AddrAddress,
       "axVrfIpv6AddrPfxLength": axVrfIpv6AddrPfxLength,
       "axVrfIpv6AddrType": axVrfIpv6AddrType,
       "axVrfIpv6AddrAnycastFlag": axVrfIpv6AddrAnycastFlag,
       "axVrfIpv6AddrStatus": axVrfIpv6AddrStatus,
       "axVrfIpv6AddrDescr": axVrfIpv6AddrDescr,
       "axVrfIpv6AddrPrefixTable": axVrfIpv6AddrPrefixTable,
       "axVrfIpv6AddrPrefixEntry": axVrfIpv6AddrPrefixEntry,
       "axVrfIpv6AddrPrefixVrfIndex": axVrfIpv6AddrPrefixVrfIndex,
       "axVrfIpv6AddrPrefixIfIndex": axVrfIpv6AddrPrefixIfIndex,
       "axVrfIpv6AddrPrefix": axVrfIpv6AddrPrefix,
       "axVrfIpv6AddrPrefixLength": axVrfIpv6AddrPrefixLength,
       "axVrfIpv6AddrPrefixOnLinkFlag": axVrfIpv6AddrPrefixOnLinkFlag,
       "axVrfIpv6AddrPrefixAutonomousFlag": axVrfIpv6AddrPrefixAutonomousFlag,
       "axVrfIpv6AddrPrefixAdvPreferredLifetime": axVrfIpv6AddrPrefixAdvPreferredLifetime,
       "axVrfIpv6AddrPrefixAdvValidLifetime": axVrfIpv6AddrPrefixAdvValidLifetime,
       "axVrfIpv6NetToMediaTable": axVrfIpv6NetToMediaTable,
       "axVrfIpv6NetToMediaEntry": axVrfIpv6NetToMediaEntry,
       "axVrfIpv6NetToMediaVrfIndex": axVrfIpv6NetToMediaVrfIndex,
       "axVrfIpv6NetToMediaIfIndex": axVrfIpv6NetToMediaIfIndex,
       "axVrfIpv6NetToMediaNetAddress": axVrfIpv6NetToMediaNetAddress,
       "axVrfIpv6NetToMediaPhysAddress": axVrfIpv6NetToMediaPhysAddress,
       "axVrfIpv6NetToMediaType": axVrfIpv6NetToMediaType,
       "axVrfIpv6IfNetToMediaState": axVrfIpv6IfNetToMediaState,
       "axVrfIpv6IfNetToMediaLastUpdated": axVrfIpv6IfNetToMediaLastUpdated,
       "axVrfIpv6NetToMediaValid": axVrfIpv6NetToMediaValid,
       "axVrfIpv6NetToMediaDescr": axVrfIpv6NetToMediaDescr,
       "axVrfIpv6Forward": axVrfIpv6Forward,
       "axVrfIpv6FwNoTable": axVrfIpv6FwNoTable,
       "axVrfIpv6FwNoEntry": axVrfIpv6FwNoEntry,
       "axVrfIpv6FwNoVRFIndex": axVrfIpv6FwNoVRFIndex,
       "axVrfIpv6FwNo": axVrfIpv6FwNo,
       "axVrfIpv6FwNoDescr": axVrfIpv6FwNoDescr,
       "axVrfIpv6FwTable": axVrfIpv6FwTable,
       "axVrfIpv6FwEntry": axVrfIpv6FwEntry,
       "axVrfIpv6FwVrfIndex": axVrfIpv6FwVrfIndex,
       "axVrfIpv6FwDest": axVrfIpv6FwDest,
       "axVrfIpv6FwPfxLength": axVrfIpv6FwPfxLength,
       "axVrfIpv6FwPolicy": axVrfIpv6FwPolicy,
       "axVrfIpv6FwNextHop": axVrfIpv6FwNextHop,
       "axVrfIpv6FwIfIndex": axVrfIpv6FwIfIndex,
       "axVrfIpv6FwType": axVrfIpv6FwType,
       "axVrfIpv6FwProto": axVrfIpv6FwProto,
       "axVrfIpv6FwAge": axVrfIpv6FwAge,
       "axVrfIpv6FwInfo": axVrfIpv6FwInfo,
       "axVrfIpv6FwNextHopAS": axVrfIpv6FwNextHopAS,
       "axVrfIpv6FwMetric1": axVrfIpv6FwMetric1,
       "axVrfIpv6FwMetric2": axVrfIpv6FwMetric2,
       "axVrfIpv6FwMetric3": axVrfIpv6FwMetric3,
       "axVrfIpv6FwMetric4": axVrfIpv6FwMetric4,
       "axVrfIpv6FwMetric5": axVrfIpv6FwMetric5,
       "axVrfIpv6FwDescr": axVrfIpv6FwDescr,
       "axVrfConformance": axVrfConformance,
       "axVrfCompliances": axVrfCompliances,
       "axVrfCompliance": axVrfCompliance,
       "axVrfGroups": axVrfGroups,
       "axVrfGroup": axVrfGroup}
)
