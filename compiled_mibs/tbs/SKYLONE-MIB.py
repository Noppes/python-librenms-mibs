# SNMP MIB module (SKYLONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tbs\SKYLONE-MIB

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

skylone = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 51009)
)
if mibBuilder.loadTexts:
    skylone.setRevisions(
        ("2018-11-25 21:37",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BufferSize(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



# MIB Managed Objects in the order of their OIDs

_ProductInfo_ObjectIdentity = ObjectIdentity
productInfo = _ProductInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51009, 1)
)
_ProductName_Type = DisplayString
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 51009, 1, 1),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")
_ProductVersion_Type = DisplayString
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 51009, 1, 2),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("current")
_ProductBuild_Type = DisplayString
_ProductBuild_Object = MibScalar
productBuild = _ProductBuild_Object(
    (1, 3, 6, 1, 4, 1, 51009, 1, 3),
    _ProductBuild_Type()
)
productBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productBuild.setStatus("current")
_SysResource_ObjectIdentity = ObjectIdentity
sysResource = _SysResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51009, 2)
)
_SysResourceCPU_Type = Integer32
_SysResourceCPU_Object = MibScalar
sysResourceCPU = _SysResourceCPU_Object(
    (1, 3, 6, 1, 4, 1, 51009, 2, 1),
    _SysResourceCPU_Type()
)
sysResourceCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResourceCPU.setStatus("current")
_SysResourceMEM_Type = Integer32
_SysResourceMEM_Object = MibScalar
sysResourceMEM = _SysResourceMEM_Object(
    (1, 3, 6, 1, 4, 1, 51009, 2, 2),
    _SysResourceMEM_Type()
)
sysResourceMEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResourceMEM.setStatus("current")
_DbaseResource_ObjectIdentity = ObjectIdentity
dbaseResource = _DbaseResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51009, 3)
)
_DbaseCache_Type = Integer32
_DbaseCache_Object = MibScalar
dbaseCache = _DbaseCache_Object(
    (1, 3, 6, 1, 4, 1, 51009, 3, 1),
    _DbaseCache_Type()
)
dbaseCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbaseCache.setStatus("current")
_DbaseOpen_Type = Integer32
_DbaseOpen_Object = MibScalar
dbaseOpen = _DbaseOpen_Object(
    (1, 3, 6, 1, 4, 1, 51009, 3, 2),
    _DbaseOpen_Type()
)
dbaseOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbaseOpen.setStatus("current")
_DbasePool_Type = Integer32
_DbasePool_Object = MibScalar
dbasePool = _DbasePool_Object(
    (1, 3, 6, 1, 4, 1, 51009, 3, 3),
    _DbasePool_Type()
)
dbasePool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbasePool.setStatus("current")
_DbaseLive_Type = Integer32
_DbaseLive_Object = MibScalar
dbaseLive = _DbaseLive_Object(
    (1, 3, 6, 1, 4, 1, 51009, 3, 4),
    _DbaseLive_Type()
)
dbaseLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbaseLive.setStatus("current")
_DbasePeak_Type = Integer32
_DbasePeak_Object = MibScalar
dbasePeak = _DbasePeak_Object(
    (1, 3, 6, 1, 4, 1, 51009, 3, 5),
    _DbasePeak_Type()
)
dbasePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbasePeak.setStatus("current")
_SrvResource_ObjectIdentity = ObjectIdentity
srvResource = _SrvResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51009, 4)
)
_SrvResourceUser_Type = Integer32
_SrvResourceUser_Object = MibScalar
srvResourceUser = _SrvResourceUser_Object(
    (1, 3, 6, 1, 4, 1, 51009, 4, 1),
    _SrvResourceUser_Type()
)
srvResourceUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvResourceUser.setStatus("current")
_SrvResourceMaxUser_Type = Integer32
_SrvResourceMaxUser_Object = MibScalar
srvResourceMaxUser = _SrvResourceMaxUser_Object(
    (1, 3, 6, 1, 4, 1, 51009, 4, 2),
    _SrvResourceMaxUser_Type()
)
srvResourceMaxUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvResourceMaxUser.setStatus("current")
_SrvResourceActiveUser_Type = Integer32
_SrvResourceActiveUser_Object = MibScalar
srvResourceActiveUser = _SrvResourceActiveUser_Object(
    (1, 3, 6, 1, 4, 1, 51009, 4, 3),
    _SrvResourceActiveUser_Type()
)
srvResourceActiveUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvResourceActiveUser.setStatus("current")
_SrvResourceWaitingUser_Type = Integer32
_SrvResourceWaitingUser_Object = MibScalar
srvResourceWaitingUser = _SrvResourceWaitingUser_Object(
    (1, 3, 6, 1, 4, 1, 51009, 4, 4),
    _SrvResourceWaitingUser_Type()
)
srvResourceWaitingUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvResourceWaitingUser.setStatus("current")
_SrvStatus_ObjectIdentity = ObjectIdentity
srvStatus = _SrvStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51009, 5)
)
_TpStatus_ObjectIdentity = ObjectIdentity
tpStatus = _TpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51009, 6)
)
_TpNumber_Type = Integer32
_TpNumber_Object = MibScalar
tpNumber = _TpNumber_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 1),
    _TpNumber_Type()
)
tpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumber.setStatus("current")
_TpTable_Object = MibTable
tpTable = _TpTable_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2)
)
if mibBuilder.loadTexts:
    tpTable.setStatus("current")
_TpEntry_Object = MibTableRow
tpEntry = _TpEntry_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2, 1)
)
tpEntry.setIndexNames(
    (0, "SKYLONE-MIB", "tpIndex"),
)
if mibBuilder.loadTexts:
    tpEntry.setStatus("current")


class _TpIndex_Type(Integer32):
    """Custom type tpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TpIndex_Type.__name__ = "Integer32"
_TpIndex_Object = MibTableColumn
tpIndex = _TpIndex_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2, 1, 1),
    _TpIndex_Type()
)
tpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpIndex.setStatus("current")
_TpName_Type = DisplayString
_TpName_Object = MibTableColumn
tpName = _TpName_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2, 1, 2),
    _TpName_Type()
)
tpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpName.setStatus("current")
_TpSignal_Type = DisplayString
_TpSignal_Object = MibTableColumn
tpSignal = _TpSignal_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2, 1, 3),
    _TpSignal_Type()
)
tpSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSignal.setStatus("current")
_TpSync_Type = DisplayString
_TpSync_Object = MibTableColumn
tpSync = _TpSync_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2, 1, 4),
    _TpSync_Type()
)
tpSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSync.setStatus("current")
_TpLock_Type = DisplayString
_TpLock_Object = MibTableColumn
tpLock = _TpLock_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2, 1, 5),
    _TpLock_Type()
)
tpLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpLock.setStatus("current")
_TpStrength_Type = Integer32
_TpStrength_Object = MibTableColumn
tpStrength = _TpStrength_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2, 1, 6),
    _TpStrength_Type()
)
tpStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStrength.setStatus("current")
_TpSnr_Type = Integer32
_TpSnr_Object = MibTableColumn
tpSnr = _TpSnr_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2, 1, 7),
    _TpSnr_Type()
)
tpSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSnr.setStatus("current")
_TpBitrate_Type = Gauge32
_TpBitrate_Object = MibTableColumn
tpBitrate = _TpBitrate_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2, 1, 8),
    _TpBitrate_Type()
)
tpBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpBitrate.setStatus("current")
_TpInvalid_Type = Integer32
_TpInvalid_Object = MibTableColumn
tpInvalid = _TpInvalid_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2, 1, 9),
    _TpInvalid_Type()
)
tpInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpInvalid.setStatus("current")
_TpError_Type = Integer32
_TpError_Object = MibTableColumn
tpError = _TpError_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2, 1, 10),
    _TpError_Type()
)
tpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpError.setStatus("current")
_TpDiscont_Type = Integer32
_TpDiscont_Object = MibTableColumn
tpDiscont = _TpDiscont_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2, 1, 11),
    _TpDiscont_Type()
)
tpDiscont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDiscont.setStatus("current")
_TpNumConfig_Type = Integer32
_TpNumConfig_Object = MibTableColumn
tpNumConfig = _TpNumConfig_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2, 1, 12),
    _TpNumConfig_Type()
)
tpNumConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumConfig.setStatus("current")
_TpNumService_Type = Integer32
_TpNumService_Object = MibTableColumn
tpNumService = _TpNumService_Object(
    (1, 3, 6, 1, 4, 1, 51009, 6, 2, 1, 13),
    _TpNumService_Type()
)
tpNumService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNumService.setStatus("current")
_MptStatus_ObjectIdentity = ObjectIdentity
mptStatus = _MptStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51009, 7)
)
_MptNumber_Type = Integer32
_MptNumber_Object = MibScalar
mptNumber = _MptNumber_Object(
    (1, 3, 6, 1, 4, 1, 51009, 7, 1),
    _MptNumber_Type()
)
mptNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mptNumber.setStatus("current")
_MptTable_Object = MibTable
mptTable = _MptTable_Object(
    (1, 3, 6, 1, 4, 1, 51009, 7, 2)
)
if mibBuilder.loadTexts:
    mptTable.setStatus("current")
_MptEntry_Object = MibTableRow
mptEntry = _MptEntry_Object(
    (1, 3, 6, 1, 4, 1, 51009, 7, 2, 1)
)
mptEntry.setIndexNames(
    (0, "SKYLONE-MIB", "mptIndex"),
)
if mibBuilder.loadTexts:
    mptEntry.setStatus("current")


class _MptIndex_Type(Integer32):
    """Custom type mptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MptIndex_Type.__name__ = "Integer32"
_MptIndex_Object = MibTableColumn
mptIndex = _MptIndex_Object(
    (1, 3, 6, 1, 4, 1, 51009, 7, 2, 1, 1),
    _MptIndex_Type()
)
mptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mptIndex.setStatus("current")
_MptName_Type = DisplayString
_MptName_Object = MibTableColumn
mptName = _MptName_Object(
    (1, 3, 6, 1, 4, 1, 51009, 7, 2, 1, 2),
    _MptName_Type()
)
mptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mptName.setStatus("current")
_MptLock_Type = DisplayString
_MptLock_Object = MibTableColumn
mptLock = _MptLock_Object(
    (1, 3, 6, 1, 4, 1, 51009, 7, 2, 1, 3),
    _MptLock_Type()
)
mptLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mptLock.setStatus("current")
_MptBitrate_Type = Gauge32
_MptBitrate_Object = MibTableColumn
mptBitrate = _MptBitrate_Object(
    (1, 3, 6, 1, 4, 1, 51009, 7, 2, 1, 4),
    _MptBitrate_Type()
)
mptBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mptBitrate.setStatus("current")
_MptInvalid_Type = Integer32
_MptInvalid_Object = MibTableColumn
mptInvalid = _MptInvalid_Object(
    (1, 3, 6, 1, 4, 1, 51009, 7, 2, 1, 5),
    _MptInvalid_Type()
)
mptInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mptInvalid.setStatus("current")
_MptError_Type = Integer32
_MptError_Object = MibTableColumn
mptError = _MptError_Object(
    (1, 3, 6, 1, 4, 1, 51009, 7, 2, 1, 6),
    _MptError_Type()
)
mptError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mptError.setStatus("current")
_MptDiscont_Type = Integer32
_MptDiscont_Object = MibTableColumn
mptDiscont = _MptDiscont_Object(
    (1, 3, 6, 1, 4, 1, 51009, 7, 2, 1, 7),
    _MptDiscont_Type()
)
mptDiscont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mptDiscont.setStatus("current")
_MptNumConfig_Type = Integer32
_MptNumConfig_Object = MibTableColumn
mptNumConfig = _MptNumConfig_Object(
    (1, 3, 6, 1, 4, 1, 51009, 7, 2, 1, 8),
    _MptNumConfig_Type()
)
mptNumConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mptNumConfig.setStatus("current")
_MptNumService_Type = Integer32
_MptNumService_Object = MibTableColumn
mptNumService = _MptNumService_Object(
    (1, 3, 6, 1, 4, 1, 51009, 7, 2, 1, 9),
    _MptNumService_Type()
)
mptNumService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mptNumService.setStatus("current")
_MuxStatus_ObjectIdentity = ObjectIdentity
muxStatus = _MuxStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51009, 8)
)
_MuxNumber_Type = Integer32
_MuxNumber_Object = MibScalar
muxNumber = _MuxNumber_Object(
    (1, 3, 6, 1, 4, 1, 51009, 8, 1),
    _MuxNumber_Type()
)
muxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxNumber.setStatus("current")
_MuxTable_Object = MibTable
muxTable = _MuxTable_Object(
    (1, 3, 6, 1, 4, 1, 51009, 8, 2)
)
if mibBuilder.loadTexts:
    muxTable.setStatus("current")
_MuxEntry_Object = MibTableRow
muxEntry = _MuxEntry_Object(
    (1, 3, 6, 1, 4, 1, 51009, 8, 2, 1)
)
muxEntry.setIndexNames(
    (0, "SKYLONE-MIB", "muxIndex"),
)
if mibBuilder.loadTexts:
    muxEntry.setStatus("current")


class _MuxIndex_Type(Integer32):
    """Custom type muxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MuxIndex_Type.__name__ = "Integer32"
_MuxIndex_Object = MibTableColumn
muxIndex = _MuxIndex_Object(
    (1, 3, 6, 1, 4, 1, 51009, 8, 2, 1, 1),
    _MuxIndex_Type()
)
muxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    muxIndex.setStatus("current")
_MuxName_Type = DisplayString
_MuxName_Object = MibTableColumn
muxName = _MuxName_Object(
    (1, 3, 6, 1, 4, 1, 51009, 8, 2, 1, 2),
    _MuxName_Type()
)
muxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxName.setStatus("current")
_MuxLock_Type = DisplayString
_MuxLock_Object = MibTableColumn
muxLock = _MuxLock_Object(
    (1, 3, 6, 1, 4, 1, 51009, 8, 2, 1, 3),
    _MuxLock_Type()
)
muxLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxLock.setStatus("current")
_MuxBitrate_Type = Gauge32
_MuxBitrate_Object = MibTableColumn
muxBitrate = _MuxBitrate_Object(
    (1, 3, 6, 1, 4, 1, 51009, 8, 2, 1, 4),
    _MuxBitrate_Type()
)
muxBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxBitrate.setStatus("current")
_MuxInvalid_Type = Integer32
_MuxInvalid_Object = MibTableColumn
muxInvalid = _MuxInvalid_Object(
    (1, 3, 6, 1, 4, 1, 51009, 8, 2, 1, 5),
    _MuxInvalid_Type()
)
muxInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxInvalid.setStatus("current")
_MuxError_Type = Integer32
_MuxError_Object = MibTableColumn
muxError = _MuxError_Object(
    (1, 3, 6, 1, 4, 1, 51009, 8, 2, 1, 6),
    _MuxError_Type()
)
muxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxError.setStatus("current")
_MuxDiscont_Type = Integer32
_MuxDiscont_Object = MibTableColumn
muxDiscont = _MuxDiscont_Object(
    (1, 3, 6, 1, 4, 1, 51009, 8, 2, 1, 7),
    _MuxDiscont_Type()
)
muxDiscont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxDiscont.setStatus("current")
_MuxNumActive_Type = Integer32
_MuxNumActive_Object = MibTableColumn
muxNumActive = _MuxNumActive_Object(
    (1, 3, 6, 1, 4, 1, 51009, 8, 2, 1, 8),
    _MuxNumActive_Type()
)
muxNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxNumActive.setStatus("current")
_MuxNumConfig_Type = Integer32
_MuxNumConfig_Object = MibTableColumn
muxNumConfig = _MuxNumConfig_Object(
    (1, 3, 6, 1, 4, 1, 51009, 8, 2, 1, 9),
    _MuxNumConfig_Type()
)
muxNumConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxNumConfig.setStatus("current")
_DvmStatus_ObjectIdentity = ObjectIdentity
dvmStatus = _DvmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51009, 9)
)
_DvmNumber_Type = Integer32
_DvmNumber_Object = MibScalar
dvmNumber = _DvmNumber_Object(
    (1, 3, 6, 1, 4, 1, 51009, 9, 1),
    _DvmNumber_Type()
)
dvmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmNumber.setStatus("current")
_DvmTable_Object = MibTable
dvmTable = _DvmTable_Object(
    (1, 3, 6, 1, 4, 1, 51009, 9, 2)
)
if mibBuilder.loadTexts:
    dvmTable.setStatus("current")
_DvmEntry_Object = MibTableRow
dvmEntry = _DvmEntry_Object(
    (1, 3, 6, 1, 4, 1, 51009, 9, 2, 1)
)
dvmEntry.setIndexNames(
    (0, "SKYLONE-MIB", "dvmIndex"),
)
if mibBuilder.loadTexts:
    dvmEntry.setStatus("current")


class _DvmIndex_Type(Integer32):
    """Custom type dvmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DvmIndex_Type.__name__ = "Integer32"
_DvmIndex_Object = MibTableColumn
dvmIndex = _DvmIndex_Object(
    (1, 3, 6, 1, 4, 1, 51009, 9, 2, 1, 1),
    _DvmIndex_Type()
)
dvmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmIndex.setStatus("current")
_DvmName_Type = DisplayString
_DvmName_Object = MibTableColumn
dvmName = _DvmName_Object(
    (1, 3, 6, 1, 4, 1, 51009, 9, 2, 1, 2),
    _DvmName_Type()
)
dvmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmName.setStatus("current")
_DvmType_Type = DisplayString
_DvmType_Object = MibTableColumn
dvmType = _DvmType_Object(
    (1, 3, 6, 1, 4, 1, 51009, 9, 2, 1, 3),
    _DvmType_Type()
)
dvmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmType.setStatus("current")
_DvmLock_Type = DisplayString
_DvmLock_Object = MibTableColumn
dvmLock = _DvmLock_Object(
    (1, 3, 6, 1, 4, 1, 51009, 9, 2, 1, 4),
    _DvmLock_Type()
)
dvmLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmLock.setStatus("current")
_DvmStart_Type = DateAndTime
_DvmStart_Object = MibTableColumn
dvmStart = _DvmStart_Object(
    (1, 3, 6, 1, 4, 1, 51009, 9, 2, 1, 5),
    _DvmStart_Type()
)
dvmStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmStart.setStatus("current")
_DvmDuration_Type = TimeStamp
_DvmDuration_Object = MibTableColumn
dvmDuration = _DvmDuration_Object(
    (1, 3, 6, 1, 4, 1, 51009, 9, 2, 1, 6),
    _DvmDuration_Type()
)
dvmDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmDuration.setStatus("current")
_DvmBitrate_Type = Gauge32
_DvmBitrate_Object = MibTableColumn
dvmBitrate = _DvmBitrate_Object(
    (1, 3, 6, 1, 4, 1, 51009, 9, 2, 1, 7),
    _DvmBitrate_Type()
)
dvmBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmBitrate.setStatus("current")
_ExmStatus_ObjectIdentity = ObjectIdentity
exmStatus = _ExmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51009, 10)
)
_ExmNumber_Type = Integer32
_ExmNumber_Object = MibScalar
exmNumber = _ExmNumber_Object(
    (1, 3, 6, 1, 4, 1, 51009, 10, 1),
    _ExmNumber_Type()
)
exmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmNumber.setStatus("current")
_ExmTable_Object = MibTable
exmTable = _ExmTable_Object(
    (1, 3, 6, 1, 4, 1, 51009, 10, 2)
)
if mibBuilder.loadTexts:
    exmTable.setStatus("current")
_ExmEntry_Object = MibTableRow
exmEntry = _ExmEntry_Object(
    (1, 3, 6, 1, 4, 1, 51009, 10, 2, 1)
)
exmEntry.setIndexNames(
    (0, "SKYLONE-MIB", "exmIndex"),
)
if mibBuilder.loadTexts:
    exmEntry.setStatus("current")


class _ExmIndex_Type(Integer32):
    """Custom type exmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ExmIndex_Type.__name__ = "Integer32"
_ExmIndex_Object = MibTableColumn
exmIndex = _ExmIndex_Object(
    (1, 3, 6, 1, 4, 1, 51009, 10, 2, 1, 1),
    _ExmIndex_Type()
)
exmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    exmIndex.setStatus("current")
_ExmName_Type = DisplayString
_ExmName_Object = MibTableColumn
exmName = _ExmName_Object(
    (1, 3, 6, 1, 4, 1, 51009, 10, 2, 1, 2),
    _ExmName_Type()
)
exmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmName.setStatus("current")
_ExmType_Type = DisplayString
_ExmType_Object = MibTableColumn
exmType = _ExmType_Object(
    (1, 3, 6, 1, 4, 1, 51009, 10, 2, 1, 3),
    _ExmType_Type()
)
exmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmType.setStatus("current")
_ExmLock_Type = DisplayString
_ExmLock_Object = MibTableColumn
exmLock = _ExmLock_Object(
    (1, 3, 6, 1, 4, 1, 51009, 10, 2, 1, 4),
    _ExmLock_Type()
)
exmLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmLock.setStatus("current")
_ExmDrop_Type = Integer32
_ExmDrop_Object = MibTableColumn
exmDrop = _ExmDrop_Object(
    (1, 3, 6, 1, 4, 1, 51009, 10, 2, 1, 5),
    _ExmDrop_Type()
)
exmDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmDrop.setStatus("current")
_ExmDuration_Type = TimeStamp
_ExmDuration_Object = MibTableColumn
exmDuration = _ExmDuration_Object(
    (1, 3, 6, 1, 4, 1, 51009, 10, 2, 1, 6),
    _ExmDuration_Type()
)
exmDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmDuration.setStatus("current")
_ExmBitrate_Type = Gauge32
_ExmBitrate_Object = MibTableColumn
exmBitrate = _ExmBitrate_Object(
    (1, 3, 6, 1, 4, 1, 51009, 10, 2, 1, 7),
    _ExmBitrate_Type()
)
exmBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exmBitrate.setStatus("current")
_MulStatus_ObjectIdentity = ObjectIdentity
mulStatus = _MulStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51009, 11)
)
_MulNumber_Type = Integer32
_MulNumber_Object = MibScalar
mulNumber = _MulNumber_Object(
    (1, 3, 6, 1, 4, 1, 51009, 11, 1),
    _MulNumber_Type()
)
mulNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mulNumber.setStatus("current")
_MulTable_Object = MibTable
mulTable = _MulTable_Object(
    (1, 3, 6, 1, 4, 1, 51009, 11, 2)
)
if mibBuilder.loadTexts:
    mulTable.setStatus("current")
_MulEntry_Object = MibTableRow
mulEntry = _MulEntry_Object(
    (1, 3, 6, 1, 4, 1, 51009, 11, 2, 1)
)
mulEntry.setIndexNames(
    (0, "SKYLONE-MIB", "mulIndex"),
)
if mibBuilder.loadTexts:
    mulEntry.setStatus("current")


class _MulIndex_Type(Integer32):
    """Custom type mulIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MulIndex_Type.__name__ = "Integer32"
_MulIndex_Object = MibTableColumn
mulIndex = _MulIndex_Object(
    (1, 3, 6, 1, 4, 1, 51009, 11, 2, 1, 1),
    _MulIndex_Type()
)
mulIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mulIndex.setStatus("current")
_MulName_Type = DisplayString
_MulName_Object = MibTableColumn
mulName = _MulName_Object(
    (1, 3, 6, 1, 4, 1, 51009, 11, 2, 1, 2),
    _MulName_Type()
)
mulName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mulName.setStatus("current")
_MulLock_Type = DisplayString
_MulLock_Object = MibTableColumn
mulLock = _MulLock_Object(
    (1, 3, 6, 1, 4, 1, 51009, 11, 2, 1, 3),
    _MulLock_Type()
)
mulLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mulLock.setStatus("current")
_MulStart_Type = DateAndTime
_MulStart_Object = MibTableColumn
mulStart = _MulStart_Object(
    (1, 3, 6, 1, 4, 1, 51009, 11, 2, 1, 4),
    _MulStart_Type()
)
mulStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mulStart.setStatus("current")
_MulDuration_Type = TimeStamp
_MulDuration_Object = MibTableColumn
mulDuration = _MulDuration_Object(
    (1, 3, 6, 1, 4, 1, 51009, 11, 2, 1, 5),
    _MulDuration_Type()
)
mulDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mulDuration.setStatus("current")
_MulBitrate_Type = Gauge32
_MulBitrate_Object = MibTableColumn
mulBitrate = _MulBitrate_Object(
    (1, 3, 6, 1, 4, 1, 51009, 11, 2, 1, 6),
    _MulBitrate_Type()
)
mulBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mulBitrate.setStatus("current")
_MulBuffer_Type = BufferSize
_MulBuffer_Object = MibTableColumn
mulBuffer = _MulBuffer_Object(
    (1, 3, 6, 1, 4, 1, 51009, 11, 2, 1, 7),
    _MulBuffer_Type()
)
mulBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mulBuffer.setStatus("current")
_LfStatus_ObjectIdentity = ObjectIdentity
lfStatus = _LfStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51009, 12)
)
_LfNumber_Type = Integer32
_LfNumber_Object = MibScalar
lfNumber = _LfNumber_Object(
    (1, 3, 6, 1, 4, 1, 51009, 12, 1),
    _LfNumber_Type()
)
lfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lfNumber.setStatus("current")
_LfTable_Object = MibTable
lfTable = _LfTable_Object(
    (1, 3, 6, 1, 4, 1, 51009, 12, 2)
)
if mibBuilder.loadTexts:
    lfTable.setStatus("current")
_LfEntry_Object = MibTableRow
lfEntry = _LfEntry_Object(
    (1, 3, 6, 1, 4, 1, 51009, 12, 2, 1)
)
lfEntry.setIndexNames(
    (0, "SKYLONE-MIB", "lfIndex"),
)
if mibBuilder.loadTexts:
    lfEntry.setStatus("current")


class _LfIndex_Type(Integer32):
    """Custom type lfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LfIndex_Type.__name__ = "Integer32"
_LfIndex_Object = MibTableColumn
lfIndex = _LfIndex_Object(
    (1, 3, 6, 1, 4, 1, 51009, 12, 2, 1, 1),
    _LfIndex_Type()
)
lfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lfIndex.setStatus("current")
_LfName_Type = DisplayString
_LfName_Object = MibTableColumn
lfName = _LfName_Object(
    (1, 3, 6, 1, 4, 1, 51009, 12, 2, 1, 2),
    _LfName_Type()
)
lfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lfName.setStatus("current")
_LfLock_Type = DisplayString
_LfLock_Object = MibTableColumn
lfLock = _LfLock_Object(
    (1, 3, 6, 1, 4, 1, 51009, 12, 2, 1, 3),
    _LfLock_Type()
)
lfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lfLock.setStatus("current")
_LfLoop_Type = DisplayString
_LfLoop_Object = MibTableColumn
lfLoop = _LfLoop_Object(
    (1, 3, 6, 1, 4, 1, 51009, 12, 2, 1, 4),
    _LfLoop_Type()
)
lfLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lfLoop.setStatus("current")
_LfLoopCount_Type = Integer32
_LfLoopCount_Object = MibTableColumn
lfLoopCount = _LfLoopCount_Object(
    (1, 3, 6, 1, 4, 1, 51009, 12, 2, 1, 5),
    _LfLoopCount_Type()
)
lfLoopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lfLoopCount.setStatus("current")
_LfPosition_Type = TimeStamp
_LfPosition_Object = MibTableColumn
lfPosition = _LfPosition_Object(
    (1, 3, 6, 1, 4, 1, 51009, 12, 2, 1, 6),
    _LfPosition_Type()
)
lfPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lfPosition.setStatus("current")
_LfBitrate_Type = Gauge32
_LfBitrate_Object = MibTableColumn
lfBitrate = _LfBitrate_Object(
    (1, 3, 6, 1, 4, 1, 51009, 12, 2, 1, 7),
    _LfBitrate_Type()
)
lfBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lfBitrate.setStatus("current")
_InpStatus_ObjectIdentity = ObjectIdentity
inpStatus = _InpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51009, 13)
)
_InpNumber_Type = Integer32
_InpNumber_Object = MibScalar
inpNumber = _InpNumber_Object(
    (1, 3, 6, 1, 4, 1, 51009, 13, 1),
    _InpNumber_Type()
)
inpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpNumber.setStatus("current")
_InpTable_Object = MibTable
inpTable = _InpTable_Object(
    (1, 3, 6, 1, 4, 1, 51009, 13, 2)
)
if mibBuilder.loadTexts:
    inpTable.setStatus("current")
_InpEntry_Object = MibTableRow
inpEntry = _InpEntry_Object(
    (1, 3, 6, 1, 4, 1, 51009, 13, 2, 1)
)
inpEntry.setIndexNames(
    (0, "SKYLONE-MIB", "inpIndex"),
)
if mibBuilder.loadTexts:
    inpEntry.setStatus("current")


class _InpIndex_Type(Integer32):
    """Custom type inpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InpIndex_Type.__name__ = "Integer32"
_InpIndex_Object = MibTableColumn
inpIndex = _InpIndex_Object(
    (1, 3, 6, 1, 4, 1, 51009, 13, 2, 1, 1),
    _InpIndex_Type()
)
inpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inpIndex.setStatus("current")
_InpName_Type = DisplayString
_InpName_Object = MibTableColumn
inpName = _InpName_Object(
    (1, 3, 6, 1, 4, 1, 51009, 13, 2, 1, 2),
    _InpName_Type()
)
inpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpName.setStatus("current")
_InpType_Type = DisplayString
_InpType_Object = MibTableColumn
inpType = _InpType_Object(
    (1, 3, 6, 1, 4, 1, 51009, 13, 2, 1, 3),
    _InpType_Type()
)
inpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpType.setStatus("current")
_InpLock_Type = DisplayString
_InpLock_Object = MibTableColumn
inpLock = _InpLock_Object(
    (1, 3, 6, 1, 4, 1, 51009, 13, 2, 1, 4),
    _InpLock_Type()
)
inpLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpLock.setStatus("current")
_InpStart_Type = DateAndTime
_InpStart_Object = MibTableColumn
inpStart = _InpStart_Object(
    (1, 3, 6, 1, 4, 1, 51009, 13, 2, 1, 5),
    _InpStart_Type()
)
inpStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpStart.setStatus("current")
_InpDuration_Type = TimeStamp
_InpDuration_Object = MibTableColumn
inpDuration = _InpDuration_Object(
    (1, 3, 6, 1, 4, 1, 51009, 13, 2, 1, 6),
    _InpDuration_Type()
)
inpDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpDuration.setStatus("current")
_InpBitrate_Type = Gauge32
_InpBitrate_Object = MibTableColumn
inpBitrate = _InpBitrate_Object(
    (1, 3, 6, 1, 4, 1, 51009, 13, 2, 1, 7),
    _InpBitrate_Type()
)
inpBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpBitrate.setStatus("current")
_InpBuffer_Type = BufferSize
_InpBuffer_Object = MibTableColumn
inpBuffer = _InpBuffer_Object(
    (1, 3, 6, 1, 4, 1, 51009, 13, 2, 1, 8),
    _InpBuffer_Type()
)
inpBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inpBuffer.setStatus("current")
_PeerStatus_ObjectIdentity = ObjectIdentity
peerStatus = _PeerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 51009, 14)
)
_PeerNumber_Type = Integer32
_PeerNumber_Object = MibScalar
peerNumber = _PeerNumber_Object(
    (1, 3, 6, 1, 4, 1, 51009, 14, 1),
    _PeerNumber_Type()
)
peerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerNumber.setStatus("current")
_PeerTable_Object = MibTable
peerTable = _PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 51009, 14, 2)
)
if mibBuilder.loadTexts:
    peerTable.setStatus("current")
_PeerEntry_Object = MibTableRow
peerEntry = _PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 51009, 14, 2, 1)
)
peerEntry.setIndexNames(
    (0, "SKYLONE-MIB", "peerIndex"),
)
if mibBuilder.loadTexts:
    peerEntry.setStatus("current")


class _PeerIndex_Type(Integer32):
    """Custom type peerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PeerIndex_Type.__name__ = "Integer32"
_PeerIndex_Object = MibTableColumn
peerIndex = _PeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 51009, 14, 2, 1, 1),
    _PeerIndex_Type()
)
peerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    peerIndex.setStatus("current")
_PeerName_Type = DisplayString
_PeerName_Object = MibTableColumn
peerName = _PeerName_Object(
    (1, 3, 6, 1, 4, 1, 51009, 14, 2, 1, 2),
    _PeerName_Type()
)
peerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerName.setStatus("current")
_PeerMacAddr_Type = DisplayString
_PeerMacAddr_Object = MibTableColumn
peerMacAddr = _PeerMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 51009, 14, 2, 1, 3),
    _PeerMacAddr_Type()
)
peerMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerMacAddr.setStatus("current")
_PeerIPAddr_Type = DisplayString
_PeerIPAddr_Object = MibTableColumn
peerIPAddr = _PeerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 51009, 14, 2, 1, 4),
    _PeerIPAddr_Type()
)
peerIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerIPAddr.setStatus("current")
_PeerStart_Type = DateAndTime
_PeerStart_Object = MibTableColumn
peerStart = _PeerStart_Object(
    (1, 3, 6, 1, 4, 1, 51009, 14, 2, 1, 5),
    _PeerStart_Type()
)
peerStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerStart.setStatus("current")
_PeerDuration_Type = TimeStamp
_PeerDuration_Object = MibTableColumn
peerDuration = _PeerDuration_Object(
    (1, 3, 6, 1, 4, 1, 51009, 14, 2, 1, 6),
    _PeerDuration_Type()
)
peerDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerDuration.setStatus("current")
_PeerBitrate_Type = Gauge32
_PeerBitrate_Object = MibTableColumn
peerBitrate = _PeerBitrate_Object(
    (1, 3, 6, 1, 4, 1, 51009, 14, 2, 1, 7),
    _PeerBitrate_Type()
)
peerBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerBitrate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SKYLONE-MIB",
    **{"BufferSize": BufferSize,
       "skylone": skylone,
       "productInfo": productInfo,
       "productName": productName,
       "productVersion": productVersion,
       "productBuild": productBuild,
       "sysResource": sysResource,
       "sysResourceCPU": sysResourceCPU,
       "sysResourceMEM": sysResourceMEM,
       "dbaseResource": dbaseResource,
       "dbaseCache": dbaseCache,
       "dbaseOpen": dbaseOpen,
       "dbasePool": dbasePool,
       "dbaseLive": dbaseLive,
       "dbasePeak": dbasePeak,
       "srvResource": srvResource,
       "srvResourceUser": srvResourceUser,
       "srvResourceMaxUser": srvResourceMaxUser,
       "srvResourceActiveUser": srvResourceActiveUser,
       "srvResourceWaitingUser": srvResourceWaitingUser,
       "srvStatus": srvStatus,
       "tpStatus": tpStatus,
       "tpNumber": tpNumber,
       "tpTable": tpTable,
       "tpEntry": tpEntry,
       "tpIndex": tpIndex,
       "tpName": tpName,
       "tpSignal": tpSignal,
       "tpSync": tpSync,
       "tpLock": tpLock,
       "tpStrength": tpStrength,
       "tpSnr": tpSnr,
       "tpBitrate": tpBitrate,
       "tpInvalid": tpInvalid,
       "tpError": tpError,
       "tpDiscont": tpDiscont,
       "tpNumConfig": tpNumConfig,
       "tpNumService": tpNumService,
       "mptStatus": mptStatus,
       "mptNumber": mptNumber,
       "mptTable": mptTable,
       "mptEntry": mptEntry,
       "mptIndex": mptIndex,
       "mptName": mptName,
       "mptLock": mptLock,
       "mptBitrate": mptBitrate,
       "mptInvalid": mptInvalid,
       "mptError": mptError,
       "mptDiscont": mptDiscont,
       "mptNumConfig": mptNumConfig,
       "mptNumService": mptNumService,
       "muxStatus": muxStatus,
       "muxNumber": muxNumber,
       "muxTable": muxTable,
       "muxEntry": muxEntry,
       "muxIndex": muxIndex,
       "muxName": muxName,
       "muxLock": muxLock,
       "muxBitrate": muxBitrate,
       "muxInvalid": muxInvalid,
       "muxError": muxError,
       "muxDiscont": muxDiscont,
       "muxNumActive": muxNumActive,
       "muxNumConfig": muxNumConfig,
       "dvmStatus": dvmStatus,
       "dvmNumber": dvmNumber,
       "dvmTable": dvmTable,
       "dvmEntry": dvmEntry,
       "dvmIndex": dvmIndex,
       "dvmName": dvmName,
       "dvmType": dvmType,
       "dvmLock": dvmLock,
       "dvmStart": dvmStart,
       "dvmDuration": dvmDuration,
       "dvmBitrate": dvmBitrate,
       "exmStatus": exmStatus,
       "exmNumber": exmNumber,
       "exmTable": exmTable,
       "exmEntry": exmEntry,
       "exmIndex": exmIndex,
       "exmName": exmName,
       "exmType": exmType,
       "exmLock": exmLock,
       "exmDrop": exmDrop,
       "exmDuration": exmDuration,
       "exmBitrate": exmBitrate,
       "mulStatus": mulStatus,
       "mulNumber": mulNumber,
       "mulTable": mulTable,
       "mulEntry": mulEntry,
       "mulIndex": mulIndex,
       "mulName": mulName,
       "mulLock": mulLock,
       "mulStart": mulStart,
       "mulDuration": mulDuration,
       "mulBitrate": mulBitrate,
       "mulBuffer": mulBuffer,
       "lfStatus": lfStatus,
       "lfNumber": lfNumber,
       "lfTable": lfTable,
       "lfEntry": lfEntry,
       "lfIndex": lfIndex,
       "lfName": lfName,
       "lfLock": lfLock,
       "lfLoop": lfLoop,
       "lfLoopCount": lfLoopCount,
       "lfPosition": lfPosition,
       "lfBitrate": lfBitrate,
       "inpStatus": inpStatus,
       "inpNumber": inpNumber,
       "inpTable": inpTable,
       "inpEntry": inpEntry,
       "inpIndex": inpIndex,
       "inpName": inpName,
       "inpType": inpType,
       "inpLock": inpLock,
       "inpStart": inpStart,
       "inpDuration": inpDuration,
       "inpBitrate": inpBitrate,
       "inpBuffer": inpBuffer,
       "peerStatus": peerStatus,
       "peerNumber": peerNumber,
       "peerTable": peerTable,
       "peerEntry": peerEntry,
       "peerIndex": peerIndex,
       "peerName": peerName,
       "peerMacAddr": peerMacAddr,
       "peerIPAddr": peerIPAddr,
       "peerStart": peerStart,
       "peerDuration": peerDuration,
       "peerBitrate": peerBitrate}
)
