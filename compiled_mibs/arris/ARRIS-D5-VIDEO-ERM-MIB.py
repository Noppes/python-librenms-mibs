# SNMP MIB module (ARRIS-D5-VIDEO-ERM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\d5\ARRIS-D5-VIDEO-ERM-MIB

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

(arrisD5UEQam,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisD5UEQam")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arrisD5UEQamErmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_D5ErmComponentName_Type = DisplayString
_D5ErmComponentName_Object = MibScalar
d5ErmComponentName = _D5ErmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 1, 1),
    _D5ErmComponentName_Type()
)
d5ErmComponentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmComponentName.setStatus("current")
_D5ErmStreamingZone_Type = DisplayString
_D5ErmStreamingZone_Object = MibScalar
d5ErmStreamingZone = _D5ErmStreamingZone_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 1, 2),
    _D5ErmStreamingZone_Type()
)
d5ErmStreamingZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmStreamingZone.setStatus("current")
_D5ErmTable_Object = MibTable
d5ErmTable = _D5ErmTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2)
)
if mibBuilder.loadTexts:
    d5ErmTable.setStatus("current")
_D5ErmEntry_Object = MibTableRow
d5ErmEntry = _D5ErmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1)
)
d5ErmEntry.setIndexNames(
    (0, "ARRIS-D5-VIDEO-ERM-MIB", "d5ErmName"),
)
if mibBuilder.loadTexts:
    d5ErmEntry.setStatus("current")
_D5ErmName_Type = DisplayString
_D5ErmName_Object = MibTableColumn
d5ErmName = _D5ErmName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 1),
    _D5ErmName_Type()
)
d5ErmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmName.setStatus("current")
_D5ErmDescription_Type = DisplayString
_D5ErmDescription_Object = MibTableColumn
d5ErmDescription = _D5ErmDescription_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 2),
    _D5ErmDescription_Type()
)
d5ErmDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmDescription.setStatus("current")
_D5ErmLocalIpAddress_Type = InetAddress
_D5ErmLocalIpAddress_Object = MibTableColumn
d5ErmLocalIpAddress = _D5ErmLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 3),
    _D5ErmLocalIpAddress_Type()
)
d5ErmLocalIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmLocalIpAddress.setStatus("current")
_D5ErmRemoteIpName_Type = DisplayString
_D5ErmRemoteIpName_Object = MibTableColumn
d5ErmRemoteIpName = _D5ErmRemoteIpName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 4),
    _D5ErmRemoteIpName_Type()
)
d5ErmRemoteIpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmRemoteIpName.setStatus("current")


class _D5ErmVrepPort_Type(Integer32):
    """Custom type d5ErmVrepPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5ErmVrepPort_Type.__name__ = "Integer32"
_D5ErmVrepPort_Object = MibTableColumn
d5ErmVrepPort = _D5ErmVrepPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 5),
    _D5ErmVrepPort_Type()
)
d5ErmVrepPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmVrepPort.setStatus("current")


class _D5ErmHoldTime_Type(Unsigned32):
    """Custom type d5ErmHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5ErmHoldTime_Type.__name__ = "Unsigned32"
_D5ErmHoldTime_Object = MibTableColumn
d5ErmHoldTime = _D5ErmHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 6),
    _D5ErmHoldTime_Type()
)
d5ErmHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmHoldTime.setStatus("current")


class _D5ErmBwInterval_Type(Unsigned32):
    """Custom type d5ErmBwInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5ErmBwInterval_Type.__name__ = "Unsigned32"
_D5ErmBwInterval_Object = MibTableColumn
d5ErmBwInterval = _D5ErmBwInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 7),
    _D5ErmBwInterval_Type()
)
d5ErmBwInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmBwInterval.setStatus("current")


class _D5ErmBwThreshold_Type(Unsigned32):
    """Custom type d5ErmBwThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5ErmBwThreshold_Type.__name__ = "Unsigned32"
_D5ErmBwThreshold_Object = MibTableColumn
d5ErmBwThreshold = _D5ErmBwThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 8),
    _D5ErmBwThreshold_Type()
)
d5ErmBwThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmBwThreshold.setStatus("current")


class _D5ErmCost_Type(Unsigned32):
    """Custom type d5ErmCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5ErmCost_Type.__name__ = "Unsigned32"
_D5ErmCost_Object = MibTableColumn
d5ErmCost = _D5ErmCost_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 9),
    _D5ErmCost_Type()
)
d5ErmCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmCost.setStatus("current")


class _D5ErmRtspPort_Type(Integer32):
    """Custom type d5ErmRtspPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5ErmRtspPort_Type.__name__ = "Integer32"
_D5ErmRtspPort_Object = MibTableColumn
d5ErmRtspPort = _D5ErmRtspPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 10),
    _D5ErmRtspPort_Type()
)
d5ErmRtspPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmRtspPort.setStatus("current")


class _D5ErmRtspConnectionTimeout_Type(Integer32):
    """Custom type d5ErmRtspConnectionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5ErmRtspConnectionTimeout_Type.__name__ = "Integer32"
_D5ErmRtspConnectionTimeout_Object = MibTableColumn
d5ErmRtspConnectionTimeout = _D5ErmRtspConnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 11),
    _D5ErmRtspConnectionTimeout_Type()
)
d5ErmRtspConnectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmRtspConnectionTimeout.setStatus("current")


class _D5ErmRtspMessageTimeout_Type(Integer32):
    """Custom type d5ErmRtspMessageTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5ErmRtspMessageTimeout_Type.__name__ = "Integer32"
_D5ErmRtspMessageTimeout_Object = MibTableColumn
d5ErmRtspMessageTimeout = _D5ErmRtspMessageTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 12),
    _D5ErmRtspMessageTimeout_Type()
)
d5ErmRtspMessageTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmRtspMessageTimeout.setStatus("current")


class _D5ErmRtspSessionTimeout_Type(Integer32):
    """Custom type d5ErmRtspSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5ErmRtspSessionTimeout_Type.__name__ = "Integer32"
_D5ErmRtspSessionTimeout_Object = MibTableColumn
d5ErmRtspSessionTimeout = _D5ErmRtspSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 13),
    _D5ErmRtspSessionTimeout_Type()
)
d5ErmRtspSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmRtspSessionTimeout.setStatus("current")


class _D5ErmAdminStatus_Type(Integer32):
    """Custom type d5ErmAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("shuttingdown", 3))
    )


_D5ErmAdminStatus_Type.__name__ = "Integer32"
_D5ErmAdminStatus_Object = MibTableColumn
d5ErmAdminStatus = _D5ErmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 14),
    _D5ErmAdminStatus_Type()
)
d5ErmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmAdminStatus.setStatus("current")


class _D5ErmVrepStatus_Type(Integer32):
    """Custom type d5ErmVrepStatus based on Integer32"""
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
        *(("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )


_D5ErmVrepStatus_Type.__name__ = "Integer32"
_D5ErmVrepStatus_Object = MibTableColumn
d5ErmVrepStatus = _D5ErmVrepStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 15),
    _D5ErmVrepStatus_Type()
)
d5ErmVrepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5ErmVrepStatus.setStatus("current")


class _D5ErmVrepConnRetryTimeout_Type(Unsigned32):
    """Custom type d5ErmVrepConnRetryTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5ErmVrepConnRetryTimeout_Type.__name__ = "Unsigned32"
_D5ErmVrepConnRetryTimeout_Object = MibTableColumn
d5ErmVrepConnRetryTimeout = _D5ErmVrepConnRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 16),
    _D5ErmVrepConnRetryTimeout_Type()
)
d5ErmVrepConnRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5ErmVrepConnRetryTimeout.setStatus("current")


class _D5ErmRtspStatus_Type(Integer32):
    """Custom type d5ErmRtspStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notrunning", 1),
          ("notconnected", 2),
          ("connected", 3))
    )


_D5ErmRtspStatus_Type.__name__ = "Integer32"
_D5ErmRtspStatus_Object = MibTableColumn
d5ErmRtspStatus = _D5ErmRtspStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 17),
    _D5ErmRtspStatus_Type()
)
d5ErmRtspStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5ErmRtspStatus.setStatus("current")
_D5ErmRowStatus_Type = RowStatus
_D5ErmRowStatus_Object = MibTableColumn
d5ErmRowStatus = _D5ErmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 2, 1, 18),
    _D5ErmRowStatus_Type()
)
d5ErmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    d5ErmRowStatus.setStatus("current")
_D5ErmSubIfTable_Object = MibTable
d5ErmSubIfTable = _D5ErmSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 3)
)
if mibBuilder.loadTexts:
    d5ErmSubIfTable.setStatus("current")
_D5ErmSubIfEntry_Object = MibTableRow
d5ErmSubIfEntry = _D5ErmSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 3, 1)
)
d5ErmSubIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    d5ErmSubIfEntry.setStatus("current")


class _D5ErmSubIfErmName_Type(OctetString):
    """Custom type d5ErmSubIfErmName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_D5ErmSubIfErmName_Type.__name__ = "OctetString"
_D5ErmSubIfErmName_Object = MibTableColumn
d5ErmSubIfErmName = _D5ErmSubIfErmName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 3, 1, 1),
    _D5ErmSubIfErmName_Type()
)
d5ErmSubIfErmName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    d5ErmSubIfErmName.setStatus("current")


class _D5ErmSubIfEigName_Type(OctetString):
    """Custom type d5ErmSubIfEigName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_D5ErmSubIfEigName_Type.__name__ = "OctetString"
_D5ErmSubIfEigName_Object = MibTableColumn
d5ErmSubIfEigName = _D5ErmSubIfEigName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 3, 1, 2),
    _D5ErmSubIfEigName_Type()
)
d5ErmSubIfEigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    d5ErmSubIfEigName.setStatus("current")
_D5ErmSubIfRowStatus_Type = RowStatus
_D5ErmSubIfRowStatus_Object = MibTableColumn
d5ErmSubIfRowStatus = _D5ErmSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 3, 1, 3),
    _D5ErmSubIfRowStatus_Type()
)
d5ErmSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    d5ErmSubIfRowStatus.setStatus("current")

# Managed Objects groups

arrisD5UEQamErmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 11, 1)
)
arrisD5UEQamErmGroup.setObjects(
      *(("ARRIS-D5-VIDEO-ERM-MIB", "d5ErmComponentName"),
        ("ARRIS-D5-VIDEO-ERM-MIB", "d5ErmStreamingZone"))
)
if mibBuilder.loadTexts:
    arrisD5UEQamErmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-D5-VIDEO-ERM-MIB",
    **{"arrisD5UEQamErmMib": arrisD5UEQamErmMib,
       "arrisD5UEQamErmGroup": arrisD5UEQamErmGroup,
       "d5ErmComponentName": d5ErmComponentName,
       "d5ErmStreamingZone": d5ErmStreamingZone,
       "d5ErmTable": d5ErmTable,
       "d5ErmEntry": d5ErmEntry,
       "d5ErmName": d5ErmName,
       "d5ErmDescription": d5ErmDescription,
       "d5ErmLocalIpAddress": d5ErmLocalIpAddress,
       "d5ErmRemoteIpName": d5ErmRemoteIpName,
       "d5ErmVrepPort": d5ErmVrepPort,
       "d5ErmHoldTime": d5ErmHoldTime,
       "d5ErmBwInterval": d5ErmBwInterval,
       "d5ErmBwThreshold": d5ErmBwThreshold,
       "d5ErmCost": d5ErmCost,
       "d5ErmRtspPort": d5ErmRtspPort,
       "d5ErmRtspConnectionTimeout": d5ErmRtspConnectionTimeout,
       "d5ErmRtspMessageTimeout": d5ErmRtspMessageTimeout,
       "d5ErmRtspSessionTimeout": d5ErmRtspSessionTimeout,
       "d5ErmAdminStatus": d5ErmAdminStatus,
       "d5ErmVrepStatus": d5ErmVrepStatus,
       "d5ErmVrepConnRetryTimeout": d5ErmVrepConnRetryTimeout,
       "d5ErmRtspStatus": d5ErmRtspStatus,
       "d5ErmRowStatus": d5ErmRowStatus,
       "d5ErmSubIfTable": d5ErmSubIfTable,
       "d5ErmSubIfEntry": d5ErmSubIfEntry,
       "d5ErmSubIfErmName": d5ErmSubIfErmName,
       "d5ErmSubIfEigName": d5ErmSubIfEigName,
       "d5ErmSubIfRowStatus": d5ErmSubIfRowStatus}
)
