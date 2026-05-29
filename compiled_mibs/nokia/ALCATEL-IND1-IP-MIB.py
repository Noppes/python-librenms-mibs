# SNMP MIB module (ALCATEL-IND1-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\aos6\ALCATEL-IND1-IP-MIB

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

(softentIND1Ip,
 trafficEventTraps) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Ip",
    "trafficEventTraps")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ipCidrRouteEntry,) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "ipCidrRouteEntry")

(ipNetToMediaEntry,
 ipNetToMediaIfIndex,
 ipNetToMediaNetAddress) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipNetToMediaEntry",
    "ipNetToMediaIfIndex",
    "ipNetToMediaNetAddress")

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

alcatelIND1IPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1IPMIB.setRevisions(
        ("2009-09-12 00:00",
         "2007-06-11 00:00",
         "2019-10-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaIpManagedIntfAppIndex(TextualConvention, Integer32):
    status = "current"
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("tacacs", 1),
          ("sflow", 2),
          ("ntp", 3),
          ("syslog", 4),
          ("dns", 5),
          ("telnet", 6),
          ("ssh", 7),
          ("tftp", 8),
          ("ldap", 9),
          ("radius", 10),
          ("snmp", 11),
          ("ftp", 12),
          ("all", 13))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IPMIBObjects = _AlcatelIND1IPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1)
)
_AlaIpConfig_ObjectIdentity = ObjectIdentity
alaIpConfig = _AlaIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 1)
)


class _AlaIpClearArpCache_Type(Integer32):
    """Custom type alaIpClearArpCache based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AlaIpClearArpCache_Type.__name__ = "Integer32"
_AlaIpClearArpCache_Object = MibScalar
alaIpClearArpCache = _AlaIpClearArpCache_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 1, 1),
    _AlaIpClearArpCache_Type()
)
alaIpClearArpCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpClearArpCache.setStatus("current")


class _AlaIpArpTimeout_Type(Integer32):
    """Custom type alaIpArpTimeout based on Integer32"""
    defaultValue = 300


_AlaIpArpTimeout_Type.__name__ = "Integer32"
_AlaIpArpTimeout_Object = MibScalar
alaIpArpTimeout = _AlaIpArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 1, 2),
    _AlaIpArpTimeout_Type()
)
alaIpArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpArpTimeout.setStatus("current")


class _AlaIpDirectedBroadcast_Type(Integer32):
    """Custom type alaIpDirectedBroadcast based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("controlled", 2))
    )


_AlaIpDirectedBroadcast_Type.__name__ = "Integer32"
_AlaIpDirectedBroadcast_Object = MibScalar
alaIpDirectedBroadcast = _AlaIpDirectedBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 1, 3),
    _AlaIpDirectedBroadcast_Type()
)
alaIpDirectedBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpDirectedBroadcast.setStatus("current")


class _AlaIpClearArpFilter_Type(Integer32):
    """Custom type alaIpClearArpFilter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AlaIpClearArpFilter_Type.__name__ = "Integer32"
_AlaIpClearArpFilter_Object = MibScalar
alaIpClearArpFilter = _AlaIpClearArpFilter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 1, 4),
    _AlaIpClearArpFilter_Type()
)
alaIpClearArpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpClearArpFilter.setStatus("current")


class _AlaIpDualHashMode_Type(Integer32):
    """Custom type alaIpDualHashMode based on Integer32"""
    defaultValue = 2

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
        *(("enabled", 1),
          ("disabled", 2),
          ("enabledRebootRequired", 3),
          ("disabledRebootRequired", 4))
    )


_AlaIpDualHashMode_Type.__name__ = "Integer32"
_AlaIpDualHashMode_Object = MibScalar
alaIpDualHashMode = _AlaIpDualHashMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 1, 5),
    _AlaIpDualHashMode_Type()
)
alaIpDualHashMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpDualHashMode.setStatus("current")
_AlaIpNetToMediaTable_Object = MibTable
alaIpNetToMediaTable = _AlaIpNetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaIpNetToMediaTable.setStatus("current")
_AlaIpNetToMediaEntry_Object = MibTableRow
alaIpNetToMediaEntry = _AlaIpNetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 2, 1)
)
alaIpNetToMediaEntry.setIndexNames(
    (0, "IP-MIB", "ipNetToMediaIfIndex"),
    (0, "IP-MIB", "ipNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    alaIpNetToMediaEntry.setStatus("current")
_AlaIpNetToMediaPhysAddress_Type = PhysAddress
_AlaIpNetToMediaPhysAddress_Object = MibTableColumn
alaIpNetToMediaPhysAddress = _AlaIpNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 2, 1, 1),
    _AlaIpNetToMediaPhysAddress_Type()
)
alaIpNetToMediaPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpNetToMediaPhysAddress.setStatus("current")


class _AlaIpNetToMediaProxy_Type(Integer32):
    """Custom type alaIpNetToMediaProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AlaIpNetToMediaProxy_Type.__name__ = "Integer32"
_AlaIpNetToMediaProxy_Object = MibTableColumn
alaIpNetToMediaProxy = _AlaIpNetToMediaProxy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 2, 1, 2),
    _AlaIpNetToMediaProxy_Type()
)
alaIpNetToMediaProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpNetToMediaProxy.setStatus("current")


class _AlaIpNetToMediaVrrp_Type(Integer32):
    """Custom type alaIpNetToMediaVrrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AlaIpNetToMediaVrrp_Type.__name__ = "Integer32"
_AlaIpNetToMediaVrrp_Object = MibTableColumn
alaIpNetToMediaVrrp = _AlaIpNetToMediaVrrp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 2, 1, 3),
    _AlaIpNetToMediaVrrp_Type()
)
alaIpNetToMediaVrrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaVrrp.setStatus("current")


class _AlaIpNetToMediaAuth_Type(Integer32):
    """Custom type alaIpNetToMediaAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AlaIpNetToMediaAuth_Type.__name__ = "Integer32"
_AlaIpNetToMediaAuth_Object = MibTableColumn
alaIpNetToMediaAuth = _AlaIpNetToMediaAuth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 2, 1, 4),
    _AlaIpNetToMediaAuth_Type()
)
alaIpNetToMediaAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaAuth.setStatus("current")


class _AlaIpNetToMediaName_Type(DisplayString):
    """Custom type alaIpNetToMediaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaIpNetToMediaName_Type.__name__ = "DisplayString"
_AlaIpNetToMediaName_Object = MibTableColumn
alaIpNetToMediaName = _AlaIpNetToMediaName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 2, 1, 5),
    _AlaIpNetToMediaName_Type()
)
alaIpNetToMediaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpNetToMediaName.setStatus("current")
_AlaDoSConfig_ObjectIdentity = ObjectIdentity
alaDoSConfig = _AlaDoSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3)
)
_AlaDoSTable_Object = MibTable
alaDoSTable = _AlaDoSTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaDoSTable.setStatus("current")
_AlaDoSEntry_Object = MibTableRow
alaDoSEntry = _AlaDoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 1, 1)
)
alaDoSEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaDoSType"),
)
if mibBuilder.loadTexts:
    alaDoSEntry.setStatus("current")


class _AlaDoSType_Type(Integer32):
    """Custom type alaDoSType based on Integer32"""
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("portscan", 0),
          ("tcpsyn", 1),
          ("pingofdeath", 2),
          ("smurf", 3),
          ("pepsi", 4),
          ("land", 5),
          ("teardropBonkBoink", 6),
          ("loopbacksrcip", 7),
          ("invalidip", 8),
          ("mcastmismatch", 9),
          ("ucastipmcastmac", 10),
          ("pingattack", 11),
          ("arpattack", 12),
          ("arppoison", 13))
    )


_AlaDoSType_Type.__name__ = "Integer32"
_AlaDoSType_Object = MibTableColumn
alaDoSType = _AlaDoSType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 1, 1, 1),
    _AlaDoSType_Type()
)
alaDoSType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSType.setStatus("current")
_AlaDoSDetected_Type = Counter32
_AlaDoSDetected_Object = MibTableColumn
alaDoSDetected = _AlaDoSDetected_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 1, 1, 2),
    _AlaDoSDetected_Type()
)
alaDoSDetected.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSDetected.setStatus("current")
_AlaDoSIp_Type = IpAddress
_AlaDoSIp_Object = MibTableColumn
alaDoSIp = _AlaDoSIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 1, 1, 3),
    _AlaDoSIp_Type()
)
alaDoSIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSIp.setStatus("current")
_AlaDoSMac_Type = MacAddress
_AlaDoSMac_Object = MibTableColumn
alaDoSMac = _AlaDoSMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 1, 1, 4),
    _AlaDoSMac_Type()
)
alaDoSMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSMac.setStatus("current")
_AlaDoSSlot_Type = Integer32
_AlaDoSSlot_Object = MibTableColumn
alaDoSSlot = _AlaDoSSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 1, 1, 5),
    _AlaDoSSlot_Type()
)
alaDoSSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSSlot.setStatus("current")
_AlaDoSPort_Type = Integer32
_AlaDoSPort_Object = MibTableColumn
alaDoSPort = _AlaDoSPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 1, 1, 6),
    _AlaDoSPort_Type()
)
alaDoSPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSPort.setStatus("current")


class _AlaDoSStatus_Type(Integer32):
    """Custom type alaDoSStatus based on Integer32"""
    defaultValue = 1

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


_AlaDoSStatus_Type.__name__ = "Integer32"
_AlaDoSStatus_Object = MibTableColumn
alaDoSStatus = _AlaDoSStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 1, 1, 7),
    _AlaDoSStatus_Type()
)
alaDoSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSStatus.setStatus("current")
_AlaDoSDetectedCounter_Type = Counter32
_AlaDoSDetectedCounter_Object = MibTableColumn
alaDoSDetectedCounter = _AlaDoSDetectedCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 1, 1, 8),
    _AlaDoSDetectedCounter_Type()
)
alaDoSDetectedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDoSDetectedCounter.setStatus("current")


class _AlaDoSPortScanClosePortPenalty_Type(Integer32):
    """Custom type alaDoSPortScanClosePortPenalty based on Integer32"""
    defaultValue = 10


_AlaDoSPortScanClosePortPenalty_Type.__name__ = "Integer32"
_AlaDoSPortScanClosePortPenalty_Object = MibScalar
alaDoSPortScanClosePortPenalty = _AlaDoSPortScanClosePortPenalty_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 2),
    _AlaDoSPortScanClosePortPenalty_Type()
)
alaDoSPortScanClosePortPenalty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanClosePortPenalty.setStatus("current")


class _AlaDoSPortScanTcpOpenPortPenalty_Type(Integer32):
    """Custom type alaDoSPortScanTcpOpenPortPenalty based on Integer32"""
    defaultValue = 0


_AlaDoSPortScanTcpOpenPortPenalty_Type.__name__ = "Integer32"
_AlaDoSPortScanTcpOpenPortPenalty_Object = MibScalar
alaDoSPortScanTcpOpenPortPenalty = _AlaDoSPortScanTcpOpenPortPenalty_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 3),
    _AlaDoSPortScanTcpOpenPortPenalty_Type()
)
alaDoSPortScanTcpOpenPortPenalty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanTcpOpenPortPenalty.setStatus("current")


class _AlaDoSPortScanUdpOpenPortPenalty_Type(Integer32):
    """Custom type alaDoSPortScanUdpOpenPortPenalty based on Integer32"""
    defaultValue = 0


_AlaDoSPortScanUdpOpenPortPenalty_Type.__name__ = "Integer32"
_AlaDoSPortScanUdpOpenPortPenalty_Object = MibScalar
alaDoSPortScanUdpOpenPortPenalty = _AlaDoSPortScanUdpOpenPortPenalty_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 4),
    _AlaDoSPortScanUdpOpenPortPenalty_Type()
)
alaDoSPortScanUdpOpenPortPenalty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanUdpOpenPortPenalty.setStatus("current")
_AlaDoSPortScanTotalPenalty_Type = Integer32
_AlaDoSPortScanTotalPenalty_Object = MibScalar
alaDoSPortScanTotalPenalty = _AlaDoSPortScanTotalPenalty_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 5),
    _AlaDoSPortScanTotalPenalty_Type()
)
alaDoSPortScanTotalPenalty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDoSPortScanTotalPenalty.setStatus("current")


class _AlaDoSPortScanThreshold_Type(Integer32):
    """Custom type alaDoSPortScanThreshold based on Integer32"""
    defaultValue = 1000


_AlaDoSPortScanThreshold_Type.__name__ = "Integer32"
_AlaDoSPortScanThreshold_Object = MibScalar
alaDoSPortScanThreshold = _AlaDoSPortScanThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 6),
    _AlaDoSPortScanThreshold_Type()
)
alaDoSPortScanThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanThreshold.setStatus("current")


class _AlaDoSPortScanDecay_Type(Integer32):
    """Custom type alaDoSPortScanDecay based on Integer32"""
    defaultValue = 2


_AlaDoSPortScanDecay_Type.__name__ = "Integer32"
_AlaDoSPortScanDecay_Object = MibScalar
alaDoSPortScanDecay = _AlaDoSPortScanDecay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 7),
    _AlaDoSPortScanDecay_Type()
)
alaDoSPortScanDecay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanDecay.setStatus("current")


class _AlaDoSTrapCntl_Type(Integer32):
    """Custom type alaDoSTrapCntl based on Integer32"""
    defaultValue = 1

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


_AlaDoSTrapCntl_Type.__name__ = "Integer32"
_AlaDoSTrapCntl_Object = MibScalar
alaDoSTrapCntl = _AlaDoSTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 8),
    _AlaDoSTrapCntl_Type()
)
alaDoSTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSTrapCntl.setStatus("current")


class _AlaDoSARPRate_Type(Integer32):
    """Custom type alaDoSARPRate based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_AlaDoSARPRate_Type.__name__ = "Integer32"
_AlaDoSARPRate_Object = MibScalar
alaDoSARPRate = _AlaDoSARPRate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 9),
    _AlaDoSARPRate_Type()
)
alaDoSARPRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSARPRate.setStatus("current")


class _AlaDoSPingRate_Type(Integer32):
    """Custom type alaDoSPingRate based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AlaDoSPingRate_Type.__name__ = "Integer32"
_AlaDoSPingRate_Object = MibScalar
alaDoSPingRate = _AlaDoSPingRate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 10),
    _AlaDoSPingRate_Type()
)
alaDoSPingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPingRate.setStatus("current")
_AlaDoSArpPoisonTable_Object = MibTable
alaDoSArpPoisonTable = _AlaDoSArpPoisonTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 11)
)
if mibBuilder.loadTexts:
    alaDoSArpPoisonTable.setStatus("current")
_AlaDoSArpPoisonEntry_Object = MibTableRow
alaDoSArpPoisonEntry = _AlaDoSArpPoisonEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 11, 1)
)
alaDoSArpPoisonEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaDoSArpPoisonIpAddr"),
)
if mibBuilder.loadTexts:
    alaDoSArpPoisonEntry.setStatus("current")
_AlaDoSArpPoisonIpAddr_Type = IpAddress
_AlaDoSArpPoisonIpAddr_Object = MibTableColumn
alaDoSArpPoisonIpAddr = _AlaDoSArpPoisonIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 11, 1, 1),
    _AlaDoSArpPoisonIpAddr_Type()
)
alaDoSArpPoisonIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDoSArpPoisonIpAddr.setStatus("current")
_AlaDoSArpPoisonDetected_Type = Counter32
_AlaDoSArpPoisonDetected_Object = MibTableColumn
alaDoSArpPoisonDetected = _AlaDoSArpPoisonDetected_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 11, 1, 2),
    _AlaDoSArpPoisonDetected_Type()
)
alaDoSArpPoisonDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDoSArpPoisonDetected.setStatus("current")
_AlaDoSArpPoisonRowStatus_Type = RowStatus
_AlaDoSArpPoisonRowStatus_Object = MibTableColumn
alaDoSArpPoisonRowStatus = _AlaDoSArpPoisonRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 11, 1, 3),
    _AlaDoSArpPoisonRowStatus_Type()
)
alaDoSArpPoisonRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDoSArpPoisonRowStatus.setStatus("current")


class _AlaDoSIpAntiSpoof_Type(Integer32):
    """Custom type alaDoSIpAntiSpoof based on Integer32"""
    defaultValue = 1

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


_AlaDoSIpAntiSpoof_Type.__name__ = "Integer32"
_AlaDoSIpAntiSpoof_Object = MibScalar
alaDoSIpAntiSpoof = _AlaDoSIpAntiSpoof_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 12),
    _AlaDoSIpAntiSpoof_Type()
)
alaDoSIpAntiSpoof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSIpAntiSpoof.setStatus("current")


class _AlaDoSArpAntiSpoof_Type(Integer32):
    """Custom type alaDoSArpAntiSpoof based on Integer32"""
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


_AlaDoSArpAntiSpoof_Type.__name__ = "Integer32"
_AlaDoSArpAntiSpoof_Object = MibScalar
alaDoSArpAntiSpoof = _AlaDoSArpAntiSpoof_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 13),
    _AlaDoSArpAntiSpoof_Type()
)
alaDoSArpAntiSpoof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSArpAntiSpoof.setStatus("current")


class _AlaDosAntiGlobalSpoofCountReset_Type(Integer32):
    """Custom type alaDosAntiGlobalSpoofCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaDosAntiGlobalSpoofCountReset_Type.__name__ = "Integer32"
_AlaDosAntiGlobalSpoofCountReset_Object = MibScalar
alaDosAntiGlobalSpoofCountReset = _AlaDosAntiGlobalSpoofCountReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 14),
    _AlaDosAntiGlobalSpoofCountReset_Type()
)
alaDosAntiGlobalSpoofCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDosAntiGlobalSpoofCountReset.setStatus("current")
_AlaDoSAntiSpoofTable_Object = MibTable
alaDoSAntiSpoofTable = _AlaDoSAntiSpoofTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 15)
)
if mibBuilder.loadTexts:
    alaDoSAntiSpoofTable.setStatus("current")
_AlaDoSAntiSpoofEntry_Object = MibTableRow
alaDoSAntiSpoofEntry = _AlaDoSAntiSpoofEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 15, 1)
)
alaDoSAntiSpoofEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaDoSAntiSpoofIpAddrType"),
    (0, "ALCATEL-IND1-IP-MIB", "alaDoSAntiSpoofIpAddr"),
)
if mibBuilder.loadTexts:
    alaDoSAntiSpoofEntry.setStatus("current")
_AlaDoSAntiSpoofIpAddrType_Type = InetAddressType
_AlaDoSAntiSpoofIpAddrType_Object = MibTableColumn
alaDoSAntiSpoofIpAddrType = _AlaDoSAntiSpoofIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 15, 1, 1),
    _AlaDoSAntiSpoofIpAddrType_Type()
)
alaDoSAntiSpoofIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDoSAntiSpoofIpAddrType.setStatus("current")
_AlaDoSAntiSpoofIpAddr_Type = InetAddress
_AlaDoSAntiSpoofIpAddr_Object = MibTableColumn
alaDoSAntiSpoofIpAddr = _AlaDoSAntiSpoofIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 15, 1, 2),
    _AlaDoSAntiSpoofIpAddr_Type()
)
alaDoSAntiSpoofIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDoSAntiSpoofIpAddr.setStatus("current")


class _AlaDoSAntiSpoofVlan_Type(Integer32):
    """Custom type alaDoSAntiSpoofVlan based on Integer32"""
    defaultValue = 0


_AlaDoSAntiSpoofVlan_Type.__name__ = "Integer32"
_AlaDoSAntiSpoofVlan_Object = MibTableColumn
alaDoSAntiSpoofVlan = _AlaDoSAntiSpoofVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 15, 1, 3),
    _AlaDoSAntiSpoofVlan_Type()
)
alaDoSAntiSpoofVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDoSAntiSpoofVlan.setStatus("current")


class _AlaDoSAntiSpoofStatus_Type(Integer32):
    """Custom type alaDoSAntiSpoofStatus based on Integer32"""
    defaultValue = 1

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


_AlaDoSAntiSpoofStatus_Type.__name__ = "Integer32"
_AlaDoSAntiSpoofStatus_Object = MibTableColumn
alaDoSAntiSpoofStatus = _AlaDoSAntiSpoofStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 15, 1, 4),
    _AlaDoSAntiSpoofStatus_Type()
)
alaDoSAntiSpoofStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSAntiSpoofStatus.setStatus("current")


class _AlaDosAntiSpoofArpOnly_Type(Integer32):
    """Custom type alaDosAntiSpoofArpOnly based on Integer32"""
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


_AlaDosAntiSpoofArpOnly_Type.__name__ = "Integer32"
_AlaDosAntiSpoofArpOnly_Object = MibTableColumn
alaDosAntiSpoofArpOnly = _AlaDosAntiSpoofArpOnly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 15, 1, 5),
    _AlaDosAntiSpoofArpOnly_Type()
)
alaDosAntiSpoofArpOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDosAntiSpoofArpOnly.setStatus("current")


class _AlaDosAntiSpoofCountReset_Type(Integer32):
    """Custom type alaDosAntiSpoofCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaDosAntiSpoofCountReset_Type.__name__ = "Integer32"
_AlaDosAntiSpoofCountReset_Object = MibTableColumn
alaDosAntiSpoofCountReset = _AlaDosAntiSpoofCountReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 15, 1, 6),
    _AlaDosAntiSpoofCountReset_Type()
)
alaDosAntiSpoofCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDosAntiSpoofCountReset.setStatus("current")
_AlaDosAntiSpoofMac_Type = MacAddress
_AlaDosAntiSpoofMac_Object = MibTableColumn
alaDosAntiSpoofMac = _AlaDosAntiSpoofMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 15, 1, 7),
    _AlaDosAntiSpoofMac_Type()
)
alaDosAntiSpoofMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDosAntiSpoofMac.setStatus("current")
_AlaDosAntiSpoofSlot_Type = Integer32
_AlaDosAntiSpoofSlot_Object = MibTableColumn
alaDosAntiSpoofSlot = _AlaDosAntiSpoofSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 15, 1, 8),
    _AlaDosAntiSpoofSlot_Type()
)
alaDosAntiSpoofSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDosAntiSpoofSlot.setStatus("current")
_AlaDosAntiSpoofPort_Type = Integer32
_AlaDosAntiSpoofPort_Object = MibTableColumn
alaDosAntiSpoofPort = _AlaDosAntiSpoofPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 15, 1, 9),
    _AlaDosAntiSpoofPort_Type()
)
alaDosAntiSpoofPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDosAntiSpoofPort.setStatus("current")


class _AlaDoSArpProtect_Type(Integer32):
    """Custom type alaDoSArpProtect based on Integer32"""
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


_AlaDoSArpProtect_Type.__name__ = "Integer32"
_AlaDoSArpProtect_Object = MibScalar
alaDoSArpProtect = _AlaDoSArpProtect_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 16),
    _AlaDoSArpProtect_Type()
)
alaDoSArpProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSArpProtect.setStatus("current")


class _AlaDosStatsClear_Type(Integer32):
    """Custom type alaDosStatsClear based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaDosStatsClear_Type.__name__ = "Integer32"
_AlaDosStatsClear_Object = MibScalar
alaDosStatsClear = _AlaDosStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 3, 17),
    _AlaDosStatsClear_Type()
)
alaDosStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDosStatsClear.setStatus("current")
_IpNetToMediaAugTable_Object = MibTable
ipNetToMediaAugTable = _IpNetToMediaAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ipNetToMediaAugTable.setStatus("current")
_IpNetToMediaAugEntry_Object = MibTableRow
ipNetToMediaAugEntry = _IpNetToMediaAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipNetToMediaAugEntry.setStatus("current")
_IpNetToMediaSlot_Type = Integer32
_IpNetToMediaSlot_Object = MibTableColumn
ipNetToMediaSlot = _IpNetToMediaSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 4, 1, 1),
    _IpNetToMediaSlot_Type()
)
ipNetToMediaSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaSlot.setStatus("current")
_IpNetToMediaPort_Type = Integer32
_IpNetToMediaPort_Object = MibTableColumn
ipNetToMediaPort = _IpNetToMediaPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 4, 1, 2),
    _IpNetToMediaPort_Type()
)
ipNetToMediaPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaPort.setStatus("current")


class _IpNetToMediaName_Type(DisplayString):
    """Custom type ipNetToMediaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpNetToMediaName_Type.__name__ = "DisplayString"
_IpNetToMediaName_Object = MibTableColumn
ipNetToMediaName = _IpNetToMediaName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 4, 1, 3),
    _IpNetToMediaName_Type()
)
ipNetToMediaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaName.setStatus("current")
_AlaDoSTraps_ObjectIdentity = ObjectIdentity
alaDoSTraps = _AlaDoSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 5)
)
_IpCidrRouteAugTable_Object = MibTable
ipCidrRouteAugTable = _IpCidrRouteAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ipCidrRouteAugTable.setStatus("current")
_IpCidrRouteAugEntry_Object = MibTableRow
ipCidrRouteAugEntry = _IpCidrRouteAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ipCidrRouteAugEntry.setStatus("current")


class _IpCidrRouteScope_Type(Integer32):
    """Custom type ipCidrRouteScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("niroute", 1),
          ("emproute", 2))
    )


_IpCidrRouteScope_Type.__name__ = "Integer32"
_IpCidrRouteScope_Object = MibTableColumn
ipCidrRouteScope = _IpCidrRouteScope_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 6, 1, 1),
    _IpCidrRouteScope_Type()
)
ipCidrRouteScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteScope.setStatus("current")
_AlaIcmpCtrlTable_Object = MibTable
alaIcmpCtrlTable = _AlaIcmpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaIcmpCtrlTable.setStatus("current")
_AlaIcmpCtrlEntry_Object = MibTableRow
alaIcmpCtrlEntry = _AlaIcmpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 7, 1)
)
alaIcmpCtrlEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIcmpCtrlType"),
    (0, "ALCATEL-IND1-IP-MIB", "alaIcmpCtrlCode"),
)
if mibBuilder.loadTexts:
    alaIcmpCtrlEntry.setStatus("current")


class _AlaIcmpCtrlType_Type(Integer32):
    """Custom type alaIcmpCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_AlaIcmpCtrlType_Type.__name__ = "Integer32"
_AlaIcmpCtrlType_Object = MibTableColumn
alaIcmpCtrlType = _AlaIcmpCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 7, 1, 1),
    _AlaIcmpCtrlType_Type()
)
alaIcmpCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIcmpCtrlType.setStatus("current")


class _AlaIcmpCtrlCode_Type(Integer32):
    """Custom type alaIcmpCtrlCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaIcmpCtrlCode_Type.__name__ = "Integer32"
_AlaIcmpCtrlCode_Object = MibTableColumn
alaIcmpCtrlCode = _AlaIcmpCtrlCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 7, 1, 2),
    _AlaIcmpCtrlCode_Type()
)
alaIcmpCtrlCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIcmpCtrlCode.setStatus("current")


class _AlaIcmpCtrlStatus_Type(Integer32):
    """Custom type alaIcmpCtrlStatus based on Integer32"""
    defaultValue = 1

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


_AlaIcmpCtrlStatus_Type.__name__ = "Integer32"
_AlaIcmpCtrlStatus_Object = MibTableColumn
alaIcmpCtrlStatus = _AlaIcmpCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 7, 1, 3),
    _AlaIcmpCtrlStatus_Type()
)
alaIcmpCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIcmpCtrlStatus.setStatus("current")


class _AlaIcmpCtrlPktGap_Type(Integer32):
    """Custom type alaIcmpCtrlPktGap based on Integer32"""
    defaultValue = 0


_AlaIcmpCtrlPktGap_Type.__name__ = "Integer32"
_AlaIcmpCtrlPktGap_Object = MibTableColumn
alaIcmpCtrlPktGap = _AlaIcmpCtrlPktGap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 7, 1, 4),
    _AlaIcmpCtrlPktGap_Type()
)
alaIcmpCtrlPktGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIcmpCtrlPktGap.setStatus("current")
_AlaIpRouteSumTable_Object = MibTable
alaIpRouteSumTable = _AlaIpRouteSumTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaIpRouteSumTable.setStatus("current")
_AlaIpRouteSumEntry_Object = MibTableRow
alaIpRouteSumEntry = _AlaIpRouteSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 9, 1)
)
alaIpRouteSumEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIpRouteProtocol"),
)
if mibBuilder.loadTexts:
    alaIpRouteSumEntry.setStatus("current")


class _AlaIpRouteProtocol_Type(Integer32):
    """Custom type alaIpRouteProtocol based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("total", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("rip", 4),
          ("isis", 5),
          ("ospf", 6),
          ("bgp", 7),
          ("other", 8))
    )


_AlaIpRouteProtocol_Type.__name__ = "Integer32"
_AlaIpRouteProtocol_Object = MibTableColumn
alaIpRouteProtocol = _AlaIpRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 9, 1, 1),
    _AlaIpRouteProtocol_Type()
)
alaIpRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpRouteProtocol.setStatus("current")
_AlaIpRouteCount_Type = Integer32
_AlaIpRouteCount_Object = MibTableColumn
alaIpRouteCount = _AlaIpRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 9, 1, 2),
    _AlaIpRouteCount_Type()
)
alaIpRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpRouteCount.setStatus("current")
_AlaIcmpCtrl_ObjectIdentity = ObjectIdentity
alaIcmpCtrl = _AlaIcmpCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 10)
)


class _AlaIcmpAllMsgStatus_Type(Integer32):
    """Custom type alaIcmpAllMsgStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("other", 3))
    )


_AlaIcmpAllMsgStatus_Type.__name__ = "Integer32"
_AlaIcmpAllMsgStatus_Object = MibScalar
alaIcmpAllMsgStatus = _AlaIcmpAllMsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 10, 1),
    _AlaIcmpAllMsgStatus_Type()
)
alaIcmpAllMsgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIcmpAllMsgStatus.setStatus("current")
_AlaIpArpFilterTable_Object = MibTable
alaIpArpFilterTable = _AlaIpArpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaIpArpFilterTable.setStatus("current")
_AlaIpArpFilterEntry_Object = MibTableRow
alaIpArpFilterEntry = _AlaIpArpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 11, 1)
)
alaIpArpFilterEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIpArpFilterIpAddr"),
    (0, "ALCATEL-IND1-IP-MIB", "alaIpArpFilterIpMask"),
    (0, "ALCATEL-IND1-IP-MIB", "alaIpArpFilterVlan"),
    (0, "ALCATEL-IND1-IP-MIB", "alaIpArpFilterType"),
)
if mibBuilder.loadTexts:
    alaIpArpFilterEntry.setStatus("current")
_AlaIpArpFilterIpAddr_Type = IpAddress
_AlaIpArpFilterIpAddr_Object = MibTableColumn
alaIpArpFilterIpAddr = _AlaIpArpFilterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 11, 1, 1),
    _AlaIpArpFilterIpAddr_Type()
)
alaIpArpFilterIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpArpFilterIpAddr.setStatus("current")
_AlaIpArpFilterIpMask_Type = IpAddress
_AlaIpArpFilterIpMask_Object = MibTableColumn
alaIpArpFilterIpMask = _AlaIpArpFilterIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 11, 1, 2),
    _AlaIpArpFilterIpMask_Type()
)
alaIpArpFilterIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpArpFilterIpMask.setStatus("current")


class _AlaIpArpFilterVlan_Type(Integer32):
    """Custom type alaIpArpFilterVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpArpFilterVlan_Type.__name__ = "Integer32"
_AlaIpArpFilterVlan_Object = MibTableColumn
alaIpArpFilterVlan = _AlaIpArpFilterVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 11, 1, 3),
    _AlaIpArpFilterVlan_Type()
)
alaIpArpFilterVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpArpFilterVlan.setStatus("current")


class _AlaIpArpFilterType_Type(Integer32):
    """Custom type alaIpArpFilterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("target", 1),
          ("sender", 2))
    )


_AlaIpArpFilterType_Type.__name__ = "Integer32"
_AlaIpArpFilterType_Object = MibTableColumn
alaIpArpFilterType = _AlaIpArpFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 11, 1, 4),
    _AlaIpArpFilterType_Type()
)
alaIpArpFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpArpFilterType.setStatus("current")


class _AlaIpArpFilterMode_Type(Integer32):
    """Custom type alaIpArpFilterMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2))
    )


_AlaIpArpFilterMode_Type.__name__ = "Integer32"
_AlaIpArpFilterMode_Object = MibTableColumn
alaIpArpFilterMode = _AlaIpArpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 11, 1, 5),
    _AlaIpArpFilterMode_Type()
)
alaIpArpFilterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpArpFilterMode.setStatus("current")
_AlaIpArpFilterRowStatus_Type = RowStatus
_AlaIpArpFilterRowStatus_Object = MibTableColumn
alaIpArpFilterRowStatus = _AlaIpArpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 11, 1, 6),
    _AlaIpArpFilterRowStatus_Type()
)
alaIpArpFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpArpFilterRowStatus.setStatus("current")
_AlaIpServiceTable_Object = MibTable
alaIpServiceTable = _AlaIpServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaIpServiceTable.setStatus("current")
_AlaIpServiceEntry_Object = MibTableRow
alaIpServiceEntry = _AlaIpServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 12, 1)
)
alaIpServiceEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIpServiceType"),
)
if mibBuilder.loadTexts:
    alaIpServiceEntry.setStatus("current")


class _AlaIpServiceType_Type(Integer32):
    """Custom type alaIpServiceType based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("ftp", 1),
          ("ssh", 2),
          ("telnet", 3),
          ("udpRelay", 4),
          ("http", 5),
          ("networkTime", 6),
          ("snmp", 7),
          ("avlanTelnet", 8),
          ("avlanHttp", 9),
          ("avlanSecureHttp", 10),
          ("secureHttp", 11),
          ("avlanHttpProxy", 12))
    )


_AlaIpServiceType_Type.__name__ = "Integer32"
_AlaIpServiceType_Object = MibTableColumn
alaIpServiceType = _AlaIpServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 12, 1, 1),
    _AlaIpServiceType_Type()
)
alaIpServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpServiceType.setStatus("current")
_AlaIpServicePort_Type = Integer32
_AlaIpServicePort_Object = MibTableColumn
alaIpServicePort = _AlaIpServicePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 12, 1, 2),
    _AlaIpServicePort_Type()
)
alaIpServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpServicePort.setStatus("current")


class _AlaIpServiceStatus_Type(Integer32):
    """Custom type alaIpServiceStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("other", 3))
    )


_AlaIpServiceStatus_Type.__name__ = "Integer32"
_AlaIpServiceStatus_Object = MibTableColumn
alaIpServiceStatus = _AlaIpServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 12, 1, 3),
    _AlaIpServiceStatus_Type()
)
alaIpServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpServiceStatus.setStatus("current")
_AlaIpPortServiceTable_Object = MibTable
alaIpPortServiceTable = _AlaIpPortServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaIpPortServiceTable.setStatus("current")
_AlaIpPortServiceEntry_Object = MibTableRow
alaIpPortServiceEntry = _AlaIpPortServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 13, 1)
)
alaIpPortServiceEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIpPortServicePort"),
)
if mibBuilder.loadTexts:
    alaIpPortServiceEntry.setStatus("current")


class _AlaIpPortServicePort_Type(Integer32):
    """Custom type alaIpPortServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaIpPortServicePort_Type.__name__ = "Integer32"
_AlaIpPortServicePort_Object = MibTableColumn
alaIpPortServicePort = _AlaIpPortServicePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 13, 1, 1),
    _AlaIpPortServicePort_Type()
)
alaIpPortServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpPortServicePort.setStatus("current")


class _AlaIpPortServiceStatus_Type(Integer32):
    """Custom type alaIpPortServiceStatus based on Integer32"""
    defaultValue = 1

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


_AlaIpPortServiceStatus_Type.__name__ = "Integer32"
_AlaIpPortServiceStatus_Object = MibTableColumn
alaIpPortServiceStatus = _AlaIpPortServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 13, 1, 2),
    _AlaIpPortServiceStatus_Type()
)
alaIpPortServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpPortServiceStatus.setStatus("current")
_AlaIpInterfaceTable_Object = MibTable
alaIpInterfaceTable = _AlaIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alaIpInterfaceTable.setStatus("current")
_AlaIpInterfaceEntry_Object = MibTableRow
alaIpInterfaceEntry = _AlaIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1)
)
alaIpInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alaIpInterfaceEntry.setStatus("current")


class _AlaIpInterfaceName_Type(DisplayString):
    """Custom type alaIpInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaIpInterfaceName_Type.__name__ = "DisplayString"
_AlaIpInterfaceName_Object = MibTableColumn
alaIpInterfaceName = _AlaIpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 1),
    _AlaIpInterfaceName_Type()
)
alaIpInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceName.setStatus("current")


class _AlaIpInterfaceAddress_Type(IpAddress):
    """Custom type alaIpInterfaceAddress based on IpAddress"""
    defaultHexValue = "00000000"


_AlaIpInterfaceAddress_Type.__name__ = "IpAddress"
_AlaIpInterfaceAddress_Object = MibTableColumn
alaIpInterfaceAddress = _AlaIpInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 2),
    _AlaIpInterfaceAddress_Type()
)
alaIpInterfaceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceAddress.setStatus("current")


class _AlaIpInterfaceMask_Type(IpAddress):
    """Custom type alaIpInterfaceMask based on IpAddress"""
    defaultHexValue = "00000000"


_AlaIpInterfaceMask_Type.__name__ = "IpAddress"
_AlaIpInterfaceMask_Object = MibTableColumn
alaIpInterfaceMask = _AlaIpInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 3),
    _AlaIpInterfaceMask_Type()
)
alaIpInterfaceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceMask.setStatus("current")


class _AlaIpInterfaceAdminState_Type(Integer32):
    """Custom type alaIpInterfaceAdminState based on Integer32"""
    defaultValue = 1

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


_AlaIpInterfaceAdminState_Type.__name__ = "Integer32"
_AlaIpInterfaceAdminState_Object = MibTableColumn
alaIpInterfaceAdminState = _AlaIpInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 4),
    _AlaIpInterfaceAdminState_Type()
)
alaIpInterfaceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceAdminState.setStatus("current")


class _AlaIpInterfaceDeviceType_Type(Integer32):
    """Custom type alaIpInterfaceDeviceType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unbound", 0),
          ("vlan", 1),
          ("emp", 2),
          ("loopback", 3),
          ("greTunnel", 4),
          ("ipipTunnel", 5))
    )


_AlaIpInterfaceDeviceType_Type.__name__ = "Integer32"
_AlaIpInterfaceDeviceType_Object = MibTableColumn
alaIpInterfaceDeviceType = _AlaIpInterfaceDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 5),
    _AlaIpInterfaceDeviceType_Type()
)
alaIpInterfaceDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDeviceType.setStatus("current")


class _AlaIpInterfaceVlanID_Type(Integer32):
    """Custom type alaIpInterfaceVlanID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpInterfaceVlanID_Type.__name__ = "Integer32"
_AlaIpInterfaceVlanID_Object = MibTableColumn
alaIpInterfaceVlanID = _AlaIpInterfaceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 6),
    _AlaIpInterfaceVlanID_Type()
)
alaIpInterfaceVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceVlanID.setStatus("current")


class _AlaIpInterfaceIpForward_Type(Integer32):
    """Custom type alaIpInterfaceIpForward based on Integer32"""
    defaultValue = 1

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


_AlaIpInterfaceIpForward_Type.__name__ = "Integer32"
_AlaIpInterfaceIpForward_Object = MibTableColumn
alaIpInterfaceIpForward = _AlaIpInterfaceIpForward_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 7),
    _AlaIpInterfaceIpForward_Type()
)
alaIpInterfaceIpForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceIpForward.setStatus("current")


class _AlaIpInterfaceEncap_Type(Integer32):
    """Custom type alaIpInterfaceEncap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet2", 1),
          ("snap", 2))
    )


_AlaIpInterfaceEncap_Type.__name__ = "Integer32"
_AlaIpInterfaceEncap_Object = MibTableColumn
alaIpInterfaceEncap = _AlaIpInterfaceEncap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 8),
    _AlaIpInterfaceEncap_Type()
)
alaIpInterfaceEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceEncap.setStatus("current")


class _AlaIpInterfaceMtu_Type(Unsigned32):
    """Custom type alaIpInterfaceMtu based on Unsigned32"""
    defaultValue = 0


_AlaIpInterfaceMtu_Type.__name__ = "Unsigned32"
_AlaIpInterfaceMtu_Object = MibTableColumn
alaIpInterfaceMtu = _AlaIpInterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 9),
    _AlaIpInterfaceMtu_Type()
)
alaIpInterfaceMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceMtu.setStatus("current")


class _AlaIpInterfaceLocalProxyArp_Type(Integer32):
    """Custom type alaIpInterfaceLocalProxyArp based on Integer32"""
    defaultValue = 1

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


_AlaIpInterfaceLocalProxyArp_Type.__name__ = "Integer32"
_AlaIpInterfaceLocalProxyArp_Object = MibTableColumn
alaIpInterfaceLocalProxyArp = _AlaIpInterfaceLocalProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 10),
    _AlaIpInterfaceLocalProxyArp_Type()
)
alaIpInterfaceLocalProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceLocalProxyArp.setStatus("current")


class _AlaIpInterfacePrimCfg_Type(Integer32):
    """Custom type alaIpInterfacePrimCfg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AlaIpInterfacePrimCfg_Type.__name__ = "Integer32"
_AlaIpInterfacePrimCfg_Object = MibTableColumn
alaIpInterfacePrimCfg = _AlaIpInterfacePrimCfg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 11),
    _AlaIpInterfacePrimCfg_Type()
)
alaIpInterfacePrimCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfacePrimCfg.setStatus("current")


class _AlaIpInterfaceOperState_Type(Integer32):
    """Custom type alaIpInterfaceOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AlaIpInterfaceOperState_Type.__name__ = "Integer32"
_AlaIpInterfaceOperState_Object = MibTableColumn
alaIpInterfaceOperState = _AlaIpInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 12),
    _AlaIpInterfaceOperState_Type()
)
alaIpInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceOperState.setStatus("current")


class _AlaIpInterfaceOperReason_Type(Integer32):
    """Custom type alaIpInterfaceOperReason based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("interfaceUp", 0),
          ("adminDown", 1),
          ("unbound", 2),
          ("deviceDown", 3),
          ("noSuchDevice", 4),
          ("noRouterMac", 5),
          ("tunnelSrcInvalid", 6),
          ("tunnelDstUnreachable", 7))
    )


_AlaIpInterfaceOperReason_Type.__name__ = "Integer32"
_AlaIpInterfaceOperReason_Object = MibTableColumn
alaIpInterfaceOperReason = _AlaIpInterfaceOperReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 13),
    _AlaIpInterfaceOperReason_Type()
)
alaIpInterfaceOperReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceOperReason.setStatus("current")
_AlaIpInterfaceRouterMac_Type = MacAddress
_AlaIpInterfaceRouterMac_Object = MibTableColumn
alaIpInterfaceRouterMac = _AlaIpInterfaceRouterMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 14),
    _AlaIpInterfaceRouterMac_Type()
)
alaIpInterfaceRouterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceRouterMac.setStatus("current")
_AlaIpInterfaceBcastAddr_Type = IpAddress
_AlaIpInterfaceBcastAddr_Object = MibTableColumn
alaIpInterfaceBcastAddr = _AlaIpInterfaceBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 15),
    _AlaIpInterfaceBcastAddr_Type()
)
alaIpInterfaceBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceBcastAddr.setStatus("current")


class _AlaIpInterfacePrimAct_Type(Integer32):
    """Custom type alaIpInterfacePrimAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AlaIpInterfacePrimAct_Type.__name__ = "Integer32"
_AlaIpInterfacePrimAct_Object = MibTableColumn
alaIpInterfacePrimAct = _AlaIpInterfacePrimAct_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 16),
    _AlaIpInterfacePrimAct_Type()
)
alaIpInterfacePrimAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfacePrimAct.setStatus("current")
_AlaIpInterfaceRemoteAddr_Type = IpAddress
_AlaIpInterfaceRemoteAddr_Object = MibTableColumn
alaIpInterfaceRemoteAddr = _AlaIpInterfaceRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 17),
    _AlaIpInterfaceRemoteAddr_Type()
)
alaIpInterfaceRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceRemoteAddr.setStatus("current")
_AlaIpInterfaceTunnelSrcAddressType_Type = InetAddressType
_AlaIpInterfaceTunnelSrcAddressType_Object = MibTableColumn
alaIpInterfaceTunnelSrcAddressType = _AlaIpInterfaceTunnelSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 18),
    _AlaIpInterfaceTunnelSrcAddressType_Type()
)
alaIpInterfaceTunnelSrcAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceTunnelSrcAddressType.setStatus("current")
_AlaIpInterfaceTunnelSrc_Type = InetAddress
_AlaIpInterfaceTunnelSrc_Object = MibTableColumn
alaIpInterfaceTunnelSrc = _AlaIpInterfaceTunnelSrc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 19),
    _AlaIpInterfaceTunnelSrc_Type()
)
alaIpInterfaceTunnelSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceTunnelSrc.setStatus("current")
_AlaIpInterfaceTunnelDstAddressType_Type = InetAddressType
_AlaIpInterfaceTunnelDstAddressType_Object = MibTableColumn
alaIpInterfaceTunnelDstAddressType = _AlaIpInterfaceTunnelDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 20),
    _AlaIpInterfaceTunnelDstAddressType_Type()
)
alaIpInterfaceTunnelDstAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceTunnelDstAddressType.setStatus("current")
_AlaIpInterfaceTunnelDst_Type = InetAddress
_AlaIpInterfaceTunnelDst_Object = MibTableColumn
alaIpInterfaceTunnelDst = _AlaIpInterfaceTunnelDst_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 21),
    _AlaIpInterfaceTunnelDst_Type()
)
alaIpInterfaceTunnelDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceTunnelDst.setStatus("current")


class _AlaIpInterfaceDhcpStatus_Type(Integer32):
    """Custom type alaIpInterfaceDhcpStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discovery", 1),
          ("active", 2),
          ("timeout", 3))
    )


_AlaIpInterfaceDhcpStatus_Type.__name__ = "Integer32"
_AlaIpInterfaceDhcpStatus_Object = MibTableColumn
alaIpInterfaceDhcpStatus = _AlaIpInterfaceDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 22),
    _AlaIpInterfaceDhcpStatus_Type()
)
alaIpInterfaceDhcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpStatus.setStatus("current")


class _AlaIpInterfaceDhcpIpRelease_Type(Integer32):
    """Custom type alaIpInterfaceDhcpIpRelease based on Integer32"""
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


_AlaIpInterfaceDhcpIpRelease_Type.__name__ = "Integer32"
_AlaIpInterfaceDhcpIpRelease_Object = MibTableColumn
alaIpInterfaceDhcpIpRelease = _AlaIpInterfaceDhcpIpRelease_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 23),
    _AlaIpInterfaceDhcpIpRelease_Type()
)
alaIpInterfaceDhcpIpRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpIpRelease.setStatus("current")


class _AlaIpInterfaceDhcpIpRenew_Type(Integer32):
    """Custom type alaIpInterfaceDhcpIpRenew based on Integer32"""
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


_AlaIpInterfaceDhcpIpRenew_Type.__name__ = "Integer32"
_AlaIpInterfaceDhcpIpRenew_Object = MibTableColumn
alaIpInterfaceDhcpIpRenew = _AlaIpInterfaceDhcpIpRenew_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 24),
    _AlaIpInterfaceDhcpIpRenew_Type()
)
alaIpInterfaceDhcpIpRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpIpRenew.setStatus("current")


class _AlaIpInterfaceDhcpOption60String_Type(DisplayString):
    """Custom type alaIpInterfaceDhcpOption60String based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaIpInterfaceDhcpOption60String_Type.__name__ = "DisplayString"
_AlaIpInterfaceDhcpOption60String_Object = MibTableColumn
alaIpInterfaceDhcpOption60String = _AlaIpInterfaceDhcpOption60String_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 25),
    _AlaIpInterfaceDhcpOption60String_Type()
)
alaIpInterfaceDhcpOption60String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpOption60String.setStatus("current")


class _AlaIpInterfaceLocalHostDirectedBroadcast_Type(Integer32):
    """Custom type alaIpInterfaceLocalHostDirectedBroadcast based on Integer32"""
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


_AlaIpInterfaceLocalHostDirectedBroadcast_Type.__name__ = "Integer32"
_AlaIpInterfaceLocalHostDirectedBroadcast_Object = MibTableColumn
alaIpInterfaceLocalHostDirectedBroadcast = _AlaIpInterfaceLocalHostDirectedBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 26),
    _AlaIpInterfaceLocalHostDirectedBroadcast_Type()
)
alaIpInterfaceLocalHostDirectedBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceLocalHostDirectedBroadcast.setStatus("current")


class _AlaIpInterfaceRtrPortIfIndex_Type(Unsigned32):
    """Custom type alaIpInterfaceRtrPortIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 4294967295),
    )


_AlaIpInterfaceRtrPortIfIndex_Type.__name__ = "Unsigned32"
_AlaIpInterfaceRtrPortIfIndex_Object = MibTableColumn
alaIpInterfaceRtrPortIfIndex = _AlaIpInterfaceRtrPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 27),
    _AlaIpInterfaceRtrPortIfIndex_Type()
)
alaIpInterfaceRtrPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpInterfaceRtrPortIfIndex.setStatus("current")


class _AlaIpInterfaceRtrPortType_Type(Integer32):
    """Custom type alaIpInterfaceRtrPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untagged", 1),
          ("tagged", 2))
    )


_AlaIpInterfaceRtrPortType_Type.__name__ = "Integer32"
_AlaIpInterfaceRtrPortType_Object = MibTableColumn
alaIpInterfaceRtrPortType = _AlaIpInterfaceRtrPortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 28),
    _AlaIpInterfaceRtrPortType_Type()
)
alaIpInterfaceRtrPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpInterfaceRtrPortType.setStatus("current")


class _AlaIpInterfaceVipAddress_Type(IpAddress):
    """Custom type alaIpInterfaceVipAddress based on IpAddress"""
    defaultHexValue = "00000000"


_AlaIpInterfaceVipAddress_Type.__name__ = "IpAddress"
_AlaIpInterfaceVipAddress_Object = MibTableColumn
alaIpInterfaceVipAddress = _AlaIpInterfaceVipAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 29),
    _AlaIpInterfaceVipAddress_Type()
)
alaIpInterfaceVipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceVipAddress.setStatus("current")


class _AlaIpInterfaceDhcpVsiAcceptFilterString_Type(DisplayString):
    """Custom type alaIpInterfaceDhcpVsiAcceptFilterString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaIpInterfaceDhcpVsiAcceptFilterString_Type.__name__ = "DisplayString"
_AlaIpInterfaceDhcpVsiAcceptFilterString_Object = MibTableColumn
alaIpInterfaceDhcpVsiAcceptFilterString = _AlaIpInterfaceDhcpVsiAcceptFilterString_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 30),
    _AlaIpInterfaceDhcpVsiAcceptFilterString_Type()
)
alaIpInterfaceDhcpVsiAcceptFilterString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpVsiAcceptFilterString.setStatus("current")


class _AlaIpInterfaceCVlanID_Type(Integer32):
    """Custom type alaIpInterfaceCVlanID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpInterfaceCVlanID_Type.__name__ = "Integer32"
_AlaIpInterfaceCVlanID_Object = MibTableColumn
alaIpInterfaceCVlanID = _AlaIpInterfaceCVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 31),
    _AlaIpInterfaceCVlanID_Type()
)
alaIpInterfaceCVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceCVlanID.setStatus("current")


class _AlaIpInterfaceDhcpServerPreference_Type(Integer32):
    """Custom type alaIpInterfaceDhcpServerPreference based on Integer32"""
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


_AlaIpInterfaceDhcpServerPreference_Type.__name__ = "Integer32"
_AlaIpInterfaceDhcpServerPreference_Object = MibTableColumn
alaIpInterfaceDhcpServerPreference = _AlaIpInterfaceDhcpServerPreference_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 14, 1, 32),
    _AlaIpInterfaceDhcpServerPreference_Type()
)
alaIpInterfaceDhcpServerPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpServerPreference.setStatus("current")
_AlaIpItfConfigTable_Object = MibTable
alaIpItfConfigTable = _AlaIpItfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alaIpItfConfigTable.setStatus("current")
_AlaIpItfConfigEntry_Object = MibTableRow
alaIpItfConfigEntry = _AlaIpItfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 15, 1)
)
alaIpItfConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIpItfConfigName"),
)
if mibBuilder.loadTexts:
    alaIpItfConfigEntry.setStatus("current")


class _AlaIpItfConfigName_Type(DisplayString):
    """Custom type alaIpItfConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaIpItfConfigName_Type.__name__ = "DisplayString"
_AlaIpItfConfigName_Object = MibTableColumn
alaIpItfConfigName = _AlaIpItfConfigName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 15, 1, 1),
    _AlaIpItfConfigName_Type()
)
alaIpItfConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpItfConfigName.setStatus("current")
_AlaIpItfConfigIfIndex_Type = InterfaceIndexOrZero
_AlaIpItfConfigIfIndex_Object = MibTableColumn
alaIpItfConfigIfIndex = _AlaIpItfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 15, 1, 2),
    _AlaIpItfConfigIfIndex_Type()
)
alaIpItfConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpItfConfigIfIndex.setStatus("current")
_AlaIpItfConfigRowStatus_Type = RowStatus
_AlaIpItfConfigRowStatus_Object = MibTableColumn
alaIpItfConfigRowStatus = _AlaIpItfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 15, 1, 3),
    _AlaIpItfConfigRowStatus_Type()
)
alaIpItfConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpItfConfigRowStatus.setStatus("current")
_AlcatelIND1IPTraps_ObjectIdentity = ObjectIdentity
alcatelIND1IPTraps = _AlcatelIND1IPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 16)
)
_AlcatelIND1IPTrapsRoot_ObjectIdentity = ObjectIdentity
alcatelIND1IPTrapsRoot = _AlcatelIND1IPTrapsRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 16, 0)
)
_AlaIpNetToMediaDpaTable_Object = MibTable
alaIpNetToMediaDpaTable = _AlaIpNetToMediaDpaTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 17)
)
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaTable.setStatus("current")
_AlaIpNetToMediaDpaEntry_Object = MibTableRow
alaIpNetToMediaDpaEntry = _AlaIpNetToMediaDpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 17, 1)
)
alaIpNetToMediaDpaEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIpNetToMediaDpaVlan"),
)
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaEntry.setStatus("current")
_AlaIpNetToMediaDpaVlan_Type = Integer32
_AlaIpNetToMediaDpaVlan_Object = MibTableColumn
alaIpNetToMediaDpaVlan = _AlaIpNetToMediaDpaVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 17, 1, 1),
    _AlaIpNetToMediaDpaVlan_Type()
)
alaIpNetToMediaDpaVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaVlan.setStatus("current")
_AlaIpNetToMediaDpaPhysAddress_Type = PhysAddress
_AlaIpNetToMediaDpaPhysAddress_Object = MibTableColumn
alaIpNetToMediaDpaPhysAddress = _AlaIpNetToMediaDpaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 17, 1, 2),
    _AlaIpNetToMediaDpaPhysAddress_Type()
)
alaIpNetToMediaDpaPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaPhysAddress.setStatus("current")


class _AlaIpNetToMediaDpaIpType_Type(InetAddressType):
    """Custom type alaIpNetToMediaDpaIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIpNetToMediaDpaIpType_Type.__name__ = "InetAddressType"
_AlaIpNetToMediaDpaIpType_Object = MibTableColumn
alaIpNetToMediaDpaIpType = _AlaIpNetToMediaDpaIpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 17, 1, 3),
    _AlaIpNetToMediaDpaIpType_Type()
)
alaIpNetToMediaDpaIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaIpType.setStatus("current")
_AlaIpNetToMediaDpaIp_Type = InetAddress
_AlaIpNetToMediaDpaIp_Object = MibTableColumn
alaIpNetToMediaDpaIp = _AlaIpNetToMediaDpaIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 17, 1, 4),
    _AlaIpNetToMediaDpaIp_Type()
)
alaIpNetToMediaDpaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaIp.setStatus("current")
_AlaIpNetToMediaDpaSlot_Type = Integer32
_AlaIpNetToMediaDpaSlot_Object = MibTableColumn
alaIpNetToMediaDpaSlot = _AlaIpNetToMediaDpaSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 17, 1, 5),
    _AlaIpNetToMediaDpaSlot_Type()
)
alaIpNetToMediaDpaSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaSlot.setStatus("current")
_AlaIpNetToMediaDpaPort_Type = Integer32
_AlaIpNetToMediaDpaPort_Object = MibTableColumn
alaIpNetToMediaDpaPort = _AlaIpNetToMediaDpaPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 17, 1, 6),
    _AlaIpNetToMediaDpaPort_Type()
)
alaIpNetToMediaDpaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaPort.setStatus("current")
_AlaIpManagedIntfTable_Object = MibTable
alaIpManagedIntfTable = _AlaIpManagedIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 18)
)
if mibBuilder.loadTexts:
    alaIpManagedIntfTable.setStatus("current")
_AlaIpManagedIntfEntry_Object = MibTableRow
alaIpManagedIntfEntry = _AlaIpManagedIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 18, 1)
)
alaIpManagedIntfEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIpManagedIntfAppIndex"),
)
if mibBuilder.loadTexts:
    alaIpManagedIntfEntry.setStatus("current")
_AlaIpManagedIntfAppIndex_Type = AlaIpManagedIntfAppIndex
_AlaIpManagedIntfAppIndex_Object = MibTableColumn
alaIpManagedIntfAppIndex = _AlaIpManagedIntfAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 18, 1, 1),
    _AlaIpManagedIntfAppIndex_Type()
)
alaIpManagedIntfAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpManagedIntfAppIndex.setStatus("current")


class _AlaIpManagedIntfName_Type(DisplayString):
    """Custom type alaIpManagedIntfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaIpManagedIntfName_Type.__name__ = "DisplayString"
_AlaIpManagedIntfName_Object = MibTableColumn
alaIpManagedIntfName = _AlaIpManagedIntfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 18, 1, 2),
    _AlaIpManagedIntfName_Type()
)
alaIpManagedIntfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpManagedIntfName.setStatus("current")
_AlaIpManagedRowStatus_Type = RowStatus
_AlaIpManagedRowStatus_Object = MibTableColumn
alaIpManagedRowStatus = _AlaIpManagedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 18, 1, 3),
    _AlaIpManagedRowStatus_Type()
)
alaIpManagedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpManagedRowStatus.setStatus("current")
_AlaIpDhcpHostIdentifierTable_ObjectIdentity = ObjectIdentity
alaIpDhcpHostIdentifierTable = _AlaIpDhcpHostIdentifierTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 19)
)
_AlaIpDhcpServerIP_Type = IpAddress
_AlaIpDhcpServerIP_Object = MibScalar
alaIpDhcpServerIP = _AlaIpDhcpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 19, 1),
    _AlaIpDhcpServerIP_Type()
)
alaIpDhcpServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpServerIP.setStatus("current")
_AlaIpDhcpRouterIP_Type = IpAddress
_AlaIpDhcpRouterIP_Object = MibScalar
alaIpDhcpRouterIP = _AlaIpDhcpRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 19, 2),
    _AlaIpDhcpRouterIP_Type()
)
alaIpDhcpRouterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpRouterIP.setStatus("current")


class _AlaIpDhcpHostName_Type(DisplayString):
    """Custom type alaIpDhcpHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AlaIpDhcpHostName_Type.__name__ = "DisplayString"
_AlaIpDhcpHostName_Object = MibScalar
alaIpDhcpHostName = _AlaIpDhcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 19, 3),
    _AlaIpDhcpHostName_Type()
)
alaIpDhcpHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpHostName.setStatus("current")
_AlaIpDhcpClientLeaseObtained_Type = TimeStamp
_AlaIpDhcpClientLeaseObtained_Object = MibScalar
alaIpDhcpClientLeaseObtained = _AlaIpDhcpClientLeaseObtained_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 19, 4),
    _AlaIpDhcpClientLeaseObtained_Type()
)
alaIpDhcpClientLeaseObtained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpClientLeaseObtained.setStatus("current")
_AlaIpDhcpClientLeaseExpires_Type = TimeStamp
_AlaIpDhcpClientLeaseExpires_Object = MibScalar
alaIpDhcpClientLeaseExpires = _AlaIpDhcpClientLeaseExpires_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 19, 5),
    _AlaIpDhcpClientLeaseExpires_Type()
)
alaIpDhcpClientLeaseExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpClientLeaseExpires.setStatus("current")
_AlaIpDirectedBroadcastCtrlTable_Object = MibTable
alaIpDirectedBroadcastCtrlTable = _AlaIpDirectedBroadcastCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 20)
)
if mibBuilder.loadTexts:
    alaIpDirectedBroadcastCtrlTable.setStatus("current")
_AlaIpDirectedBroadcastCtrlEntry_Object = MibTableRow
alaIpDirectedBroadcastCtrlEntry = _AlaIpDirectedBroadcastCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 20, 1)
)
alaIpDirectedBroadcastCtrlEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIpDirectedBroadcastCtrlSrcAddr"),
    (0, "ALCATEL-IND1-IP-MIB", "alaIpDirectedBroadcastCtrlSrcMask"),
    (0, "ALCATEL-IND1-IP-MIB", "alaIpDirectedBroadcastCtrlDstAddr"),
    (0, "ALCATEL-IND1-IP-MIB", "alaIpDirectedBroadcastCtrlDstMask"),
    (0, "ALCATEL-IND1-IP-MIB", "alaIpDirectedBroadcastCtrlVlanID"),
)
if mibBuilder.loadTexts:
    alaIpDirectedBroadcastCtrlEntry.setStatus("current")


class _AlaIpDirectedBroadcastCtrlSrcAddr_Type(IpAddress):
    """Custom type alaIpDirectedBroadcastCtrlSrcAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaIpDirectedBroadcastCtrlSrcAddr_Type.__name__ = "IpAddress"
_AlaIpDirectedBroadcastCtrlSrcAddr_Object = MibTableColumn
alaIpDirectedBroadcastCtrlSrcAddr = _AlaIpDirectedBroadcastCtrlSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 20, 1, 1),
    _AlaIpDirectedBroadcastCtrlSrcAddr_Type()
)
alaIpDirectedBroadcastCtrlSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpDirectedBroadcastCtrlSrcAddr.setStatus("current")


class _AlaIpDirectedBroadcastCtrlSrcMask_Type(IpAddress):
    """Custom type alaIpDirectedBroadcastCtrlSrcMask based on IpAddress"""
    defaultHexValue = "00000000"


_AlaIpDirectedBroadcastCtrlSrcMask_Type.__name__ = "IpAddress"
_AlaIpDirectedBroadcastCtrlSrcMask_Object = MibTableColumn
alaIpDirectedBroadcastCtrlSrcMask = _AlaIpDirectedBroadcastCtrlSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 20, 1, 2),
    _AlaIpDirectedBroadcastCtrlSrcMask_Type()
)
alaIpDirectedBroadcastCtrlSrcMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpDirectedBroadcastCtrlSrcMask.setStatus("current")


class _AlaIpDirectedBroadcastCtrlDstAddr_Type(IpAddress):
    """Custom type alaIpDirectedBroadcastCtrlDstAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlaIpDirectedBroadcastCtrlDstAddr_Type.__name__ = "IpAddress"
_AlaIpDirectedBroadcastCtrlDstAddr_Object = MibTableColumn
alaIpDirectedBroadcastCtrlDstAddr = _AlaIpDirectedBroadcastCtrlDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 20, 1, 3),
    _AlaIpDirectedBroadcastCtrlDstAddr_Type()
)
alaIpDirectedBroadcastCtrlDstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpDirectedBroadcastCtrlDstAddr.setStatus("current")


class _AlaIpDirectedBroadcastCtrlDstMask_Type(IpAddress):
    """Custom type alaIpDirectedBroadcastCtrlDstMask based on IpAddress"""
    defaultHexValue = "00000000"


_AlaIpDirectedBroadcastCtrlDstMask_Type.__name__ = "IpAddress"
_AlaIpDirectedBroadcastCtrlDstMask_Object = MibTableColumn
alaIpDirectedBroadcastCtrlDstMask = _AlaIpDirectedBroadcastCtrlDstMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 20, 1, 4),
    _AlaIpDirectedBroadcastCtrlDstMask_Type()
)
alaIpDirectedBroadcastCtrlDstMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpDirectedBroadcastCtrlDstMask.setStatus("current")


class _AlaIpDirectedBroadcastCtrlVlanID_Type(Integer32):
    """Custom type alaIpDirectedBroadcastCtrlVlanID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpDirectedBroadcastCtrlVlanID_Type.__name__ = "Integer32"
_AlaIpDirectedBroadcastCtrlVlanID_Object = MibTableColumn
alaIpDirectedBroadcastCtrlVlanID = _AlaIpDirectedBroadcastCtrlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 20, 1, 5),
    _AlaIpDirectedBroadcastCtrlVlanID_Type()
)
alaIpDirectedBroadcastCtrlVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpDirectedBroadcastCtrlVlanID.setStatus("current")
_AlaIpDirectedBroadcastCtrlRowStatus_Type = RowStatus
_AlaIpDirectedBroadcastCtrlRowStatus_Object = MibTableColumn
alaIpDirectedBroadcastCtrlRowStatus = _AlaIpDirectedBroadcastCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 20, 1, 6),
    _AlaIpDirectedBroadcastCtrlRowStatus_Type()
)
alaIpDirectedBroadcastCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpDirectedBroadcastCtrlRowStatus.setStatus("current")
_AlaZeroConfConfig_ObjectIdentity = ObjectIdentity
alaZeroConfConfig = _AlaZeroConfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 21)
)
if mibBuilder.loadTexts:
    alaZeroConfConfig.setStatus("current")


class _AlaZeroConfMdnsAdminStatus_Type(Integer32):
    """Custom type alaZeroConfMdnsAdminStatus based on Integer32"""
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


_AlaZeroConfMdnsAdminStatus_Type.__name__ = "Integer32"
_AlaZeroConfMdnsAdminStatus_Object = MibScalar
alaZeroConfMdnsAdminStatus = _AlaZeroConfMdnsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 21, 1),
    _AlaZeroConfMdnsAdminStatus_Type()
)
alaZeroConfMdnsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaZeroConfMdnsAdminStatus.setStatus("current")


class _AlaZeroConfSsdpAdminStatus_Type(Integer32):
    """Custom type alaZeroConfSsdpAdminStatus based on Integer32"""
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


_AlaZeroConfSsdpAdminStatus_Type.__name__ = "Integer32"
_AlaZeroConfSsdpAdminStatus_Object = MibScalar
alaZeroConfSsdpAdminStatus = _AlaZeroConfSsdpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 21, 2),
    _AlaZeroConfSsdpAdminStatus_Type()
)
alaZeroConfSsdpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaZeroConfSsdpAdminStatus.setStatus("current")


class _AlaZeroConfMode_Type(Integer32):
    """Custom type alaZeroConfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 1),
          ("gateway", 2))
    )


_AlaZeroConfMode_Type.__name__ = "Integer32"
_AlaZeroConfMode_Object = MibScalar
alaZeroConfMode = _AlaZeroConfMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 21, 3),
    _AlaZeroConfMode_Type()
)
alaZeroConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaZeroConfMode.setStatus("current")


class _AlaZeroConfTunnelMode_Type(Integer32):
    """Custom type alaZeroConfTunnelMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("standard", 2))
    )


_AlaZeroConfTunnelMode_Type.__name__ = "Integer32"
_AlaZeroConfTunnelMode_Object = MibScalar
alaZeroConfTunnelMode = _AlaZeroConfTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 21, 4),
    _AlaZeroConfTunnelMode_Type()
)
alaZeroConfTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaZeroConfTunnelMode.setStatus("current")
_AlaZeroConfResponderIpAddr_Type = IpAddress
_AlaZeroConfResponderIpAddr_Object = MibScalar
alaZeroConfResponderIpAddr = _AlaZeroConfResponderIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 21, 5),
    _AlaZeroConfResponderIpAddr_Type()
)
alaZeroConfResponderIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaZeroConfResponderIpAddr.setStatus("current")
_AlaZeroConfGatewayVlanTable_Object = MibTable
alaZeroConfGatewayVlanTable = _AlaZeroConfGatewayVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 22)
)
if mibBuilder.loadTexts:
    alaZeroConfGatewayVlanTable.setStatus("current")
_AlaZeroConfGatewayVlanEntry_Object = MibTableRow
alaZeroConfGatewayVlanEntry = _AlaZeroConfGatewayVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 22, 1)
)
alaZeroConfGatewayVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaZeroConfGatewayVlan"),
)
if mibBuilder.loadTexts:
    alaZeroConfGatewayVlanEntry.setStatus("current")


class _AlaZeroConfGatewayVlan_Type(Unsigned32):
    """Custom type alaZeroConfGatewayVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaZeroConfGatewayVlan_Type.__name__ = "Unsigned32"
_AlaZeroConfGatewayVlan_Object = MibTableColumn
alaZeroConfGatewayVlan = _AlaZeroConfGatewayVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 22, 1, 1),
    _AlaZeroConfGatewayVlan_Type()
)
alaZeroConfGatewayVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaZeroConfGatewayVlan.setStatus("current")
_AlaZeroConfGatewayVlanRowStatus_Type = RowStatus
_AlaZeroConfGatewayVlanRowStatus_Object = MibTableColumn
alaZeroConfGatewayVlanRowStatus = _AlaZeroConfGatewayVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 22, 1, 2),
    _AlaZeroConfGatewayVlanRowStatus_Type()
)
alaZeroConfGatewayVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaZeroConfGatewayVlanRowStatus.setStatus("current")
_AlaZeroConfAccessVlanTable_Object = MibTable
alaZeroConfAccessVlanTable = _AlaZeroConfAccessVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 23)
)
if mibBuilder.loadTexts:
    alaZeroConfAccessVlanTable.setStatus("current")
_AlaZeroConfAccessVlanEntry_Object = MibTableRow
alaZeroConfAccessVlanEntry = _AlaZeroConfAccessVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 23, 1)
)
alaZeroConfAccessVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaZeroConfAccessVlan"),
)
if mibBuilder.loadTexts:
    alaZeroConfAccessVlanEntry.setStatus("current")


class _AlaZeroConfAccessVlan_Type(Unsigned32):
    """Custom type alaZeroConfAccessVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaZeroConfAccessVlan_Type.__name__ = "Unsigned32"
_AlaZeroConfAccessVlan_Object = MibTableColumn
alaZeroConfAccessVlan = _AlaZeroConfAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 23, 1, 1),
    _AlaZeroConfAccessVlan_Type()
)
alaZeroConfAccessVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaZeroConfAccessVlan.setStatus("current")
_AlaZeroConfAccessVlanRowStatus_Type = RowStatus
_AlaZeroConfAccessVlanRowStatus_Object = MibTableColumn
alaZeroConfAccessVlanRowStatus = _AlaZeroConfAccessVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 23, 1, 2),
    _AlaZeroConfAccessVlanRowStatus_Type()
)
alaZeroConfAccessVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaZeroConfAccessVlanRowStatus.setStatus("current")
_AlcatelIND1IPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IPMIBConformance = _AlcatelIND1IPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2)
)
_AlcatelIND1IPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IPMIBCompliances = _AlcatelIND1IPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 1)
)
_AlcatelIND1IPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IPMIBGroups = _AlcatelIND1IPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2)
)
_TrafficEvents_ObjectIdentity = ObjectIdentity
trafficEvents = _TrafficEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 15, 1)
)
_TrafficEventTrapObjs_ObjectIdentity = ObjectIdentity
trafficEventTrapObjs = _TrafficEventTrapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 15, 2)
)


class _PktDropType_Type(Integer32):
    """Custom type pktDropType based on Integer32"""
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("spoofedIp", 0),
          ("toBlockedPort", 1),
          ("rulematchTriggeredPortDisable", 2),
          ("spoofTriggeredUserPortDisable", 3),
          ("bpduTriggeredUserPortDisable", 4),
          ("bgpTriggeredUserPortDisable", 5),
          ("ospfTriggeredUserPortDisable", 6),
          ("ripTriggeredUserPortDisable", 7),
          ("vrrpTriggeredUserPortDisable", 8),
          ("dhcpserverTriggeredUserPortDisable", 9),
          ("pimTriggeredUserPortDisable", 10),
          ("dvmrpTriggeredUserPortDisable", 11),
          ("isisTriggeredUserPortDisable", 12),
          ("dns-replyTriggeredUserPortDisable", 13))
    )


_PktDropType_Type.__name__ = "Integer32"
_PktDropType_Object = MibScalar
pktDropType = _PktDropType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 15, 2, 1),
    _PktDropType_Type()
)
pktDropType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pktDropType.setStatus("current")
_PktDropIfIndex_Type = InterfaceIndexOrZero
_PktDropIfIndex_Object = MibScalar
pktDropIfIndex = _PktDropIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 15, 2, 2),
    _PktDropIfIndex_Type()
)
pktDropIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pktDropIfIndex.setStatus("current")
_PktDropCount_Type = Integer32
_PktDropCount_Object = MibScalar
pktDropCount = _PktDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 15, 2, 3),
    _PktDropCount_Type()
)
pktDropCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pktDropCount.setStatus("current")


class _PktDropFrag_Type(OctetString):
    """Custom type pktDropFrag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PktDropFrag_Type.__name__ = "OctetString"
_PktDropFrag_Object = MibScalar
pktDropFrag = _PktDropFrag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 15, 2, 4),
    _PktDropFrag_Type()
)
pktDropFrag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pktDropFrag.setStatus("current")
ipNetToMediaEntry.registerAugmentions(
    ("ALCATEL-IND1-IP-MIB",
     "ipNetToMediaAugEntry")
)
ipNetToMediaAugEntry.setIndexNames(*ipNetToMediaEntry.getIndexNames())
ipCidrRouteEntry.registerAugmentions(
    ("ALCATEL-IND1-IP-MIB",
     "ipCidrRouteAugEntry")
)
ipCidrRouteAugEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())

# Managed Objects groups

alaIpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 1)
)
alaIpConfigGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpClearArpCache"),
        ("ALCATEL-IND1-IP-MIB", "alaIpArpTimeout"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDirectedBroadcast"),
        ("ALCATEL-IND1-IP-MIB", "alaIpClearArpFilter"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDualHashMode"))
)
if mibBuilder.loadTexts:
    alaIpConfigGroup.setStatus("current")

alaIpDoSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 2)
)
alaIpDoSGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaDoSDetected"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSIp"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSMac"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSSlot"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPort"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSDetectedCounter"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSARPRate"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSArpPoisonDetected"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSArpPoisonRowStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPingRate"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPortScanClosePortPenalty"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPortScanDecay"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPortScanTcpOpenPortPenalty"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPortScanThreshold"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPortScanTotalPenalty"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPortScanUdpOpenPortPenalty"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSTrapCntl"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSType"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSIpAntiSpoof"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSArpAntiSpoof"),
        ("ALCATEL-IND1-IP-MIB", "alaDosAntiGlobalSpoofCountReset"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSAntiSpoofIpAddr"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSAntiSpoofVlan"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSAntiSpoofStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaDosAntiSpoofArpOnly"),
        ("ALCATEL-IND1-IP-MIB", "alaDosAntiSpoofCountReset"),
        ("ALCATEL-IND1-IP-MIB", "alaDosAntiSpoofMac"),
        ("ALCATEL-IND1-IP-MIB", "alaDosAntiSpoofSlot"),
        ("ALCATEL-IND1-IP-MIB", "alaDosAntiSpoofPort"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSArpProtect"),
        ("ALCATEL-IND1-IP-MIB", "alaDosStatsClear"))
)
if mibBuilder.loadTexts:
    alaIpDoSGroup.setStatus("current")

alaIpNetToMediaDpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 3)
)
alaIpNetToMediaDpGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaDpaPhysAddress"),
        ("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaDpaIpType"),
        ("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaDpaIp"),
        ("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaDpaSlot"),
        ("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaDpaPort"),
        ("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaAuth"),
        ("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaName"),
        ("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaPhysAddress"),
        ("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaProxy"),
        ("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaVrrp"))
)
if mibBuilder.loadTexts:
    alaIpNetToMediaDpGroup.setStatus("current")

alaIpDhcpHostIdentifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 4)
)
alaIpDhcpHostIdentifierGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpDhcpServerIP"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDhcpRouterIP"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDhcpHostName"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDhcpClientLeaseObtained"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDhcpClientLeaseExpires"))
)
if mibBuilder.loadTexts:
    alaIpDhcpHostIdentifierGroup.setStatus("current")

alaIcmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 5)
)
alaIcmpGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIcmpAllMsgStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaIcmpCtrlCode"),
        ("ALCATEL-IND1-IP-MIB", "alaIcmpCtrlType"),
        ("ALCATEL-IND1-IP-MIB", "alaIcmpCtrlStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaIcmpCtrlPktGap"))
)
if mibBuilder.loadTexts:
    alaIcmpGroup.setStatus("current")

alaIpArpFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 6)
)
alaIpArpFilterGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpArpFilterVlan"),
        ("ALCATEL-IND1-IP-MIB", "alaIpArpFilterMode"),
        ("ALCATEL-IND1-IP-MIB", "alaIpArpFilterType"),
        ("ALCATEL-IND1-IP-MIB", "alaIpArpFilterRowStatus"))
)
if mibBuilder.loadTexts:
    alaIpArpFilterGroup.setStatus("current")

alaIpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 7)
)
alaIpInterfaceGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpInterfaceName"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceAddress"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceMask"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceAdminState"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceDeviceType"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceVlanID"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceIpForward"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceEncap"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceMtu"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceLocalProxyArp"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfacePrimCfg"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceOperState"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceOperReason"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceRouterMac"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceBcastAddr"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfacePrimAct"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceRemoteAddr"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceTunnelSrcAddressType"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceTunnelSrc"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceTunnelDstAddressType"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceTunnelDst"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceDhcpStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceDhcpIpRelease"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceDhcpIpRenew"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceDhcpOption60String"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceLocalHostDirectedBroadcast"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceDhcpVsiAcceptFilterString"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceCVlanID"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceDhcpServerPreference"))
)
if mibBuilder.loadTexts:
    alaIpInterfaceGroup.setStatus("current")

alaIpItfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 9)
)
alaIpItfConfigGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpItfConfigRowStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaIpItfConfigIfIndex"),
        ("ALCATEL-IND1-IP-MIB", "alaIpItfConfigName"))
)
if mibBuilder.loadTexts:
    alaIpItfConfigGroup.setStatus("current")

alaIpManagedIntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 10)
)
alaIpManagedIntfGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpManagedIntfName"),
        ("ALCATEL-IND1-IP-MIB", "alaIpManagedRowStatus"))
)
if mibBuilder.loadTexts:
    alaIpManagedIntfGroup.setStatus("current")

alaIpPortServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 11)
)
alaIpPortServiceGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpPortServicePort"),
        ("ALCATEL-IND1-IP-MIB", "alaIpPortServiceStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaIpServicePort"),
        ("ALCATEL-IND1-IP-MIB", "alaIpServiceStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaIpServiceType"))
)
if mibBuilder.loadTexts:
    alaIpPortServiceGroup.setStatus("current")

alaIpRouteSumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 12)
)
alaIpRouteSumGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpRouteCount"),
        ("ALCATEL-IND1-IP-MIB", "alaIpRouteProtocol"))
)
if mibBuilder.loadTexts:
    alaIpRouteSumGroup.setStatus("current")

alaIpMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 13)
)
alaIpMiscGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "ipCidrRouteScope"),
        ("ALCATEL-IND1-IP-MIB", "ipNetToMediaName"),
        ("ALCATEL-IND1-IP-MIB", "ipNetToMediaPort"),
        ("ALCATEL-IND1-IP-MIB", "ipNetToMediaSlot"),
        ("ALCATEL-IND1-IP-MIB", "pktDropCount"),
        ("ALCATEL-IND1-IP-MIB", "pktDropFrag"),
        ("ALCATEL-IND1-IP-MIB", "pktDropIfIndex"),
        ("ALCATEL-IND1-IP-MIB", "pktDropType"))
)
if mibBuilder.loadTexts:
    alaIpMiscGroup.setStatus("current")

alaIpDirectedBroadcastCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 14)
)
alaIpDirectedBroadcastCtrlGroup.setObjects(
    ("ALCATEL-IND1-IP-MIB", "alaIpDirectedBroadcastCtrlRowStatus")
)
if mibBuilder.loadTexts:
    alaIpDirectedBroadcastCtrlGroup.setStatus("current")

alaZeroConfConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 15)
)
alaZeroConfConfGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaZeroConfMdnsAdminStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaZeroConfSsdpAdminStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaZeroConfMode"),
        ("ALCATEL-IND1-IP-MIB", "alaZeroConfTunnelMode"),
        ("ALCATEL-IND1-IP-MIB", "alaZeroConfResponderIpAddr"))
)
if mibBuilder.loadTexts:
    alaZeroConfConfGroup.setStatus("current")

alaZeroConfGatewayVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 16)
)
alaZeroConfGatewayVlanGroup.setObjects(
    ("ALCATEL-IND1-IP-MIB", "alaZeroConfGatewayVlanRowStatus")
)
if mibBuilder.loadTexts:
    alaZeroConfGatewayVlanGroup.setStatus("current")

alaZeroConfAccessVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 17)
)
alaZeroConfAccessVlanGroup.setObjects(
    ("ALCATEL-IND1-IP-MIB", "alaZeroConfAccessVlanRowStatus")
)
if mibBuilder.loadTexts:
    alaZeroConfAccessVlanGroup.setStatus("current")


# Notification objects

alaDoSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 5, 0, 1)
)
alaDoSTrap.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaDoSType"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSDetected"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSIp"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSMac"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSSlot"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPort"))
)
if mibBuilder.loadTexts:
    alaDoSTrap.setStatus(
        "current"
    )

arpMaxLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 1, 16, 0, 1)
)
if mibBuilder.loadTexts:
    arpMaxLimitReached.setStatus(
        "current"
    )

pktDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 15, 1, 0, 1)
)
pktDrop.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "pktDropType"),
        ("ALCATEL-IND1-IP-MIB", "pktDropIfIndex"),
        ("ALCATEL-IND1-IP-MIB", "pktDropCount"),
        ("ALCATEL-IND1-IP-MIB", "pktDropFrag"))
)
if mibBuilder.loadTexts:
    pktDrop.setStatus(
        "current"
    )


# Notifications groups

alaIpInterfaceTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 2, 8)
)
alaIpInterfaceTrapsGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaDoSTrap"),
        ("ALCATEL-IND1-IP-MIB", "pktDrop"),
        ("ALCATEL-IND1-IP-MIB", "arpMaxLimitReached"))
)
if mibBuilder.loadTexts:
    alaIpInterfaceTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaIpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 23, 1, 2, 1, 1)
)
alaIpCompliance.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpConfigGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDoSGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaDpGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDhcpHostIdentifierGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaIcmpGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaIpArpFilterGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaIpItfConfigGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaIpManagedIntfGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaIpPortServiceGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaIpRouteSumGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaIpMiscGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDirectedBroadcastCtrlGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaZeroConfConfGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaZeroConfGatewayVlanGroup"),
        ("ALCATEL-IND1-IP-MIB", "alaZeroConfAccessVlanGroup"))
)
if mibBuilder.loadTexts:
    alaIpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-IP-MIB",
    **{"AlaIpManagedIntfAppIndex": AlaIpManagedIntfAppIndex,
       "alcatelIND1IPMIB": alcatelIND1IPMIB,
       "alcatelIND1IPMIBObjects": alcatelIND1IPMIBObjects,
       "alaIpConfig": alaIpConfig,
       "alaIpClearArpCache": alaIpClearArpCache,
       "alaIpArpTimeout": alaIpArpTimeout,
       "alaIpDirectedBroadcast": alaIpDirectedBroadcast,
       "alaIpClearArpFilter": alaIpClearArpFilter,
       "alaIpDualHashMode": alaIpDualHashMode,
       "alaIpNetToMediaTable": alaIpNetToMediaTable,
       "alaIpNetToMediaEntry": alaIpNetToMediaEntry,
       "alaIpNetToMediaPhysAddress": alaIpNetToMediaPhysAddress,
       "alaIpNetToMediaProxy": alaIpNetToMediaProxy,
       "alaIpNetToMediaVrrp": alaIpNetToMediaVrrp,
       "alaIpNetToMediaAuth": alaIpNetToMediaAuth,
       "alaIpNetToMediaName": alaIpNetToMediaName,
       "alaDoSConfig": alaDoSConfig,
       "alaDoSTable": alaDoSTable,
       "alaDoSEntry": alaDoSEntry,
       "alaDoSType": alaDoSType,
       "alaDoSDetected": alaDoSDetected,
       "alaDoSIp": alaDoSIp,
       "alaDoSMac": alaDoSMac,
       "alaDoSSlot": alaDoSSlot,
       "alaDoSPort": alaDoSPort,
       "alaDoSStatus": alaDoSStatus,
       "alaDoSDetectedCounter": alaDoSDetectedCounter,
       "alaDoSPortScanClosePortPenalty": alaDoSPortScanClosePortPenalty,
       "alaDoSPortScanTcpOpenPortPenalty": alaDoSPortScanTcpOpenPortPenalty,
       "alaDoSPortScanUdpOpenPortPenalty": alaDoSPortScanUdpOpenPortPenalty,
       "alaDoSPortScanTotalPenalty": alaDoSPortScanTotalPenalty,
       "alaDoSPortScanThreshold": alaDoSPortScanThreshold,
       "alaDoSPortScanDecay": alaDoSPortScanDecay,
       "alaDoSTrapCntl": alaDoSTrapCntl,
       "alaDoSARPRate": alaDoSARPRate,
       "alaDoSPingRate": alaDoSPingRate,
       "alaDoSArpPoisonTable": alaDoSArpPoisonTable,
       "alaDoSArpPoisonEntry": alaDoSArpPoisonEntry,
       "alaDoSArpPoisonIpAddr": alaDoSArpPoisonIpAddr,
       "alaDoSArpPoisonDetected": alaDoSArpPoisonDetected,
       "alaDoSArpPoisonRowStatus": alaDoSArpPoisonRowStatus,
       "alaDoSIpAntiSpoof": alaDoSIpAntiSpoof,
       "alaDoSArpAntiSpoof": alaDoSArpAntiSpoof,
       "alaDosAntiGlobalSpoofCountReset": alaDosAntiGlobalSpoofCountReset,
       "alaDoSAntiSpoofTable": alaDoSAntiSpoofTable,
       "alaDoSAntiSpoofEntry": alaDoSAntiSpoofEntry,
       "alaDoSAntiSpoofIpAddrType": alaDoSAntiSpoofIpAddrType,
       "alaDoSAntiSpoofIpAddr": alaDoSAntiSpoofIpAddr,
       "alaDoSAntiSpoofVlan": alaDoSAntiSpoofVlan,
       "alaDoSAntiSpoofStatus": alaDoSAntiSpoofStatus,
       "alaDosAntiSpoofArpOnly": alaDosAntiSpoofArpOnly,
       "alaDosAntiSpoofCountReset": alaDosAntiSpoofCountReset,
       "alaDosAntiSpoofMac": alaDosAntiSpoofMac,
       "alaDosAntiSpoofSlot": alaDosAntiSpoofSlot,
       "alaDosAntiSpoofPort": alaDosAntiSpoofPort,
       "alaDoSArpProtect": alaDoSArpProtect,
       "alaDosStatsClear": alaDosStatsClear,
       "ipNetToMediaAugTable": ipNetToMediaAugTable,
       "ipNetToMediaAugEntry": ipNetToMediaAugEntry,
       "ipNetToMediaSlot": ipNetToMediaSlot,
       "ipNetToMediaPort": ipNetToMediaPort,
       "ipNetToMediaName": ipNetToMediaName,
       "alaDoSTraps": alaDoSTraps,
       "alaDoSTrap": alaDoSTrap,
       "ipCidrRouteAugTable": ipCidrRouteAugTable,
       "ipCidrRouteAugEntry": ipCidrRouteAugEntry,
       "ipCidrRouteScope": ipCidrRouteScope,
       "alaIcmpCtrlTable": alaIcmpCtrlTable,
       "alaIcmpCtrlEntry": alaIcmpCtrlEntry,
       "alaIcmpCtrlType": alaIcmpCtrlType,
       "alaIcmpCtrlCode": alaIcmpCtrlCode,
       "alaIcmpCtrlStatus": alaIcmpCtrlStatus,
       "alaIcmpCtrlPktGap": alaIcmpCtrlPktGap,
       "alaIpRouteSumTable": alaIpRouteSumTable,
       "alaIpRouteSumEntry": alaIpRouteSumEntry,
       "alaIpRouteProtocol": alaIpRouteProtocol,
       "alaIpRouteCount": alaIpRouteCount,
       "alaIcmpCtrl": alaIcmpCtrl,
       "alaIcmpAllMsgStatus": alaIcmpAllMsgStatus,
       "alaIpArpFilterTable": alaIpArpFilterTable,
       "alaIpArpFilterEntry": alaIpArpFilterEntry,
       "alaIpArpFilterIpAddr": alaIpArpFilterIpAddr,
       "alaIpArpFilterIpMask": alaIpArpFilterIpMask,
       "alaIpArpFilterVlan": alaIpArpFilterVlan,
       "alaIpArpFilterType": alaIpArpFilterType,
       "alaIpArpFilterMode": alaIpArpFilterMode,
       "alaIpArpFilterRowStatus": alaIpArpFilterRowStatus,
       "alaIpServiceTable": alaIpServiceTable,
       "alaIpServiceEntry": alaIpServiceEntry,
       "alaIpServiceType": alaIpServiceType,
       "alaIpServicePort": alaIpServicePort,
       "alaIpServiceStatus": alaIpServiceStatus,
       "alaIpPortServiceTable": alaIpPortServiceTable,
       "alaIpPortServiceEntry": alaIpPortServiceEntry,
       "alaIpPortServicePort": alaIpPortServicePort,
       "alaIpPortServiceStatus": alaIpPortServiceStatus,
       "alaIpInterfaceTable": alaIpInterfaceTable,
       "alaIpInterfaceEntry": alaIpInterfaceEntry,
       "alaIpInterfaceName": alaIpInterfaceName,
       "alaIpInterfaceAddress": alaIpInterfaceAddress,
       "alaIpInterfaceMask": alaIpInterfaceMask,
       "alaIpInterfaceAdminState": alaIpInterfaceAdminState,
       "alaIpInterfaceDeviceType": alaIpInterfaceDeviceType,
       "alaIpInterfaceVlanID": alaIpInterfaceVlanID,
       "alaIpInterfaceIpForward": alaIpInterfaceIpForward,
       "alaIpInterfaceEncap": alaIpInterfaceEncap,
       "alaIpInterfaceMtu": alaIpInterfaceMtu,
       "alaIpInterfaceLocalProxyArp": alaIpInterfaceLocalProxyArp,
       "alaIpInterfacePrimCfg": alaIpInterfacePrimCfg,
       "alaIpInterfaceOperState": alaIpInterfaceOperState,
       "alaIpInterfaceOperReason": alaIpInterfaceOperReason,
       "alaIpInterfaceRouterMac": alaIpInterfaceRouterMac,
       "alaIpInterfaceBcastAddr": alaIpInterfaceBcastAddr,
       "alaIpInterfacePrimAct": alaIpInterfacePrimAct,
       "alaIpInterfaceRemoteAddr": alaIpInterfaceRemoteAddr,
       "alaIpInterfaceTunnelSrcAddressType": alaIpInterfaceTunnelSrcAddressType,
       "alaIpInterfaceTunnelSrc": alaIpInterfaceTunnelSrc,
       "alaIpInterfaceTunnelDstAddressType": alaIpInterfaceTunnelDstAddressType,
       "alaIpInterfaceTunnelDst": alaIpInterfaceTunnelDst,
       "alaIpInterfaceDhcpStatus": alaIpInterfaceDhcpStatus,
       "alaIpInterfaceDhcpIpRelease": alaIpInterfaceDhcpIpRelease,
       "alaIpInterfaceDhcpIpRenew": alaIpInterfaceDhcpIpRenew,
       "alaIpInterfaceDhcpOption60String": alaIpInterfaceDhcpOption60String,
       "alaIpInterfaceLocalHostDirectedBroadcast": alaIpInterfaceLocalHostDirectedBroadcast,
       "alaIpInterfaceRtrPortIfIndex": alaIpInterfaceRtrPortIfIndex,
       "alaIpInterfaceRtrPortType": alaIpInterfaceRtrPortType,
       "alaIpInterfaceVipAddress": alaIpInterfaceVipAddress,
       "alaIpInterfaceDhcpVsiAcceptFilterString": alaIpInterfaceDhcpVsiAcceptFilterString,
       "alaIpInterfaceCVlanID": alaIpInterfaceCVlanID,
       "alaIpInterfaceDhcpServerPreference": alaIpInterfaceDhcpServerPreference,
       "alaIpItfConfigTable": alaIpItfConfigTable,
       "alaIpItfConfigEntry": alaIpItfConfigEntry,
       "alaIpItfConfigName": alaIpItfConfigName,
       "alaIpItfConfigIfIndex": alaIpItfConfigIfIndex,
       "alaIpItfConfigRowStatus": alaIpItfConfigRowStatus,
       "alcatelIND1IPTraps": alcatelIND1IPTraps,
       "alcatelIND1IPTrapsRoot": alcatelIND1IPTrapsRoot,
       "arpMaxLimitReached": arpMaxLimitReached,
       "alaIpNetToMediaDpaTable": alaIpNetToMediaDpaTable,
       "alaIpNetToMediaDpaEntry": alaIpNetToMediaDpaEntry,
       "alaIpNetToMediaDpaVlan": alaIpNetToMediaDpaVlan,
       "alaIpNetToMediaDpaPhysAddress": alaIpNetToMediaDpaPhysAddress,
       "alaIpNetToMediaDpaIpType": alaIpNetToMediaDpaIpType,
       "alaIpNetToMediaDpaIp": alaIpNetToMediaDpaIp,
       "alaIpNetToMediaDpaSlot": alaIpNetToMediaDpaSlot,
       "alaIpNetToMediaDpaPort": alaIpNetToMediaDpaPort,
       "alaIpManagedIntfTable": alaIpManagedIntfTable,
       "alaIpManagedIntfEntry": alaIpManagedIntfEntry,
       "alaIpManagedIntfAppIndex": alaIpManagedIntfAppIndex,
       "alaIpManagedIntfName": alaIpManagedIntfName,
       "alaIpManagedRowStatus": alaIpManagedRowStatus,
       "alaIpDhcpHostIdentifierTable": alaIpDhcpHostIdentifierTable,
       "alaIpDhcpServerIP": alaIpDhcpServerIP,
       "alaIpDhcpRouterIP": alaIpDhcpRouterIP,
       "alaIpDhcpHostName": alaIpDhcpHostName,
       "alaIpDhcpClientLeaseObtained": alaIpDhcpClientLeaseObtained,
       "alaIpDhcpClientLeaseExpires": alaIpDhcpClientLeaseExpires,
       "alaIpDirectedBroadcastCtrlTable": alaIpDirectedBroadcastCtrlTable,
       "alaIpDirectedBroadcastCtrlEntry": alaIpDirectedBroadcastCtrlEntry,
       "alaIpDirectedBroadcastCtrlSrcAddr": alaIpDirectedBroadcastCtrlSrcAddr,
       "alaIpDirectedBroadcastCtrlSrcMask": alaIpDirectedBroadcastCtrlSrcMask,
       "alaIpDirectedBroadcastCtrlDstAddr": alaIpDirectedBroadcastCtrlDstAddr,
       "alaIpDirectedBroadcastCtrlDstMask": alaIpDirectedBroadcastCtrlDstMask,
       "alaIpDirectedBroadcastCtrlVlanID": alaIpDirectedBroadcastCtrlVlanID,
       "alaIpDirectedBroadcastCtrlRowStatus": alaIpDirectedBroadcastCtrlRowStatus,
       "alaZeroConfConfig": alaZeroConfConfig,
       "alaZeroConfMdnsAdminStatus": alaZeroConfMdnsAdminStatus,
       "alaZeroConfSsdpAdminStatus": alaZeroConfSsdpAdminStatus,
       "alaZeroConfMode": alaZeroConfMode,
       "alaZeroConfTunnelMode": alaZeroConfTunnelMode,
       "alaZeroConfResponderIpAddr": alaZeroConfResponderIpAddr,
       "alaZeroConfGatewayVlanTable": alaZeroConfGatewayVlanTable,
       "alaZeroConfGatewayVlanEntry": alaZeroConfGatewayVlanEntry,
       "alaZeroConfGatewayVlan": alaZeroConfGatewayVlan,
       "alaZeroConfGatewayVlanRowStatus": alaZeroConfGatewayVlanRowStatus,
       "alaZeroConfAccessVlanTable": alaZeroConfAccessVlanTable,
       "alaZeroConfAccessVlanEntry": alaZeroConfAccessVlanEntry,
       "alaZeroConfAccessVlan": alaZeroConfAccessVlan,
       "alaZeroConfAccessVlanRowStatus": alaZeroConfAccessVlanRowStatus,
       "alcatelIND1IPMIBConformance": alcatelIND1IPMIBConformance,
       "alcatelIND1IPMIBCompliances": alcatelIND1IPMIBCompliances,
       "alaIpCompliance": alaIpCompliance,
       "alcatelIND1IPMIBGroups": alcatelIND1IPMIBGroups,
       "alaIpConfigGroup": alaIpConfigGroup,
       "alaIpDoSGroup": alaIpDoSGroup,
       "alaIpNetToMediaDpGroup": alaIpNetToMediaDpGroup,
       "alaIpDhcpHostIdentifierGroup": alaIpDhcpHostIdentifierGroup,
       "alaIcmpGroup": alaIcmpGroup,
       "alaIpArpFilterGroup": alaIpArpFilterGroup,
       "alaIpInterfaceGroup": alaIpInterfaceGroup,
       "alaIpInterfaceTrapsGroup": alaIpInterfaceTrapsGroup,
       "alaIpItfConfigGroup": alaIpItfConfigGroup,
       "alaIpManagedIntfGroup": alaIpManagedIntfGroup,
       "alaIpPortServiceGroup": alaIpPortServiceGroup,
       "alaIpRouteSumGroup": alaIpRouteSumGroup,
       "alaIpMiscGroup": alaIpMiscGroup,
       "alaIpDirectedBroadcastCtrlGroup": alaIpDirectedBroadcastCtrlGroup,
       "alaZeroConfConfGroup": alaZeroConfConfGroup,
       "alaZeroConfGatewayVlanGroup": alaZeroConfGatewayVlanGroup,
       "alaZeroConfAccessVlanGroup": alaZeroConfAccessVlanGroup,
       "trafficEvents": trafficEvents,
       "pktDrop": pktDrop,
       "trafficEventTrapObjs": trafficEventTrapObjs,
       "pktDropType": pktDropType,
       "pktDropIfIndex": pktDropIfIndex,
       "pktDropCount": pktDropCount,
       "pktDropFrag": pktDropFrag}
)
