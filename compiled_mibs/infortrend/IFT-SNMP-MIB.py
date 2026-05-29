# SNMP MIB module (IFT-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\infortrend\IFT-SNMP-MIB

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

infortrend = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1714)
)
if mibBuilder.loadTexts:
    infortrend.setRevisions(
        ("2017-09-19 00:00",
         "2017-05-16 00:00",
         "2017-04-28 00:00",
         "2015-09-25 00:00",
         "2015-01-22 00:00",
         "2015-01-21 00:00",
         "2015-01-07 00:00",
         "2014-10-16 00:00",
         "2014-08-22 00:00",
         "2014-01-08 00:00",
         "2011-11-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Raid_ObjectIdentity = ObjectIdentity
raid = _Raid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1714, 1)
)
if mibBuilder.loadTexts:
    raid.setStatus("current")
_ExtInterface_ObjectIdentity = ObjectIdentity
extInterface = _ExtInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1)
)
if mibBuilder.loadTexts:
    extInterface.setStatus("current")
_CtlrConfiguration_ObjectIdentity = ObjectIdentity
ctlrConfiguration = _CtlrConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1)
)
_SysInformation_ObjectIdentity = ObjectIdentity
sysInformation = _SysInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1)
)
_CpuType_Type = DisplayString
_CpuType_Object = MibScalar
cpuType = _CpuType_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 1),
    _CpuType_Type()
)
cpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuType.setStatus("current")
_CacheSize_Type = Integer32
_CacheSize_Object = MibScalar
cacheSize = _CacheSize_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 2),
    _CacheSize_Type()
)
cacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheSize.setStatus("current")
if mibBuilder.loadTexts:
    cacheSize.setUnits("MB")
_MemoryType_Type = Integer32
_MemoryType_Object = MibScalar
memoryType = _MemoryType_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 3),
    _MemoryType_Type()
)
memoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryType.setStatus("current")
_FwMajorVersion_Type = Integer32
_FwMajorVersion_Object = MibScalar
fwMajorVersion = _FwMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 4),
    _FwMajorVersion_Type()
)
fwMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMajorVersion.setStatus("current")
_FwMinorVersion_Type = Integer32
_FwMinorVersion_Object = MibScalar
fwMinorVersion = _FwMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 5),
    _FwMinorVersion_Type()
)
fwMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwMinorVersion.setStatus("current")
_FwEngineerVersion_Type = Integer32
_FwEngineerVersion_Object = MibScalar
fwEngineerVersion = _FwEngineerVersion_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 6),
    _FwEngineerVersion_Type()
)
fwEngineerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwEngineerVersion.setStatus("current")
_BrMajorVersion_Type = Integer32
_BrMajorVersion_Object = MibScalar
brMajorVersion = _BrMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 7),
    _BrMajorVersion_Type()
)
brMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMajorVersion.setStatus("current")
_BrMinorVersion_Type = Integer32
_BrMinorVersion_Object = MibScalar
brMinorVersion = _BrMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 8),
    _BrMinorVersion_Type()
)
brMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brMinorVersion.setStatus("current")
_BrEngineerVersion_Type = Integer32
_BrEngineerVersion_Object = MibScalar
brEngineerVersion = _BrEngineerVersion_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 9),
    _BrEngineerVersion_Type()
)
brEngineerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brEngineerVersion.setStatus("current")
_SerialNum_Type = Integer32
_SerialNum_Object = MibScalar
serialNum = _SerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 10),
    _SerialNum_Type()
)
serialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNum.setStatus("current")
_CtlrName_Type = DisplayString
_CtlrName_Object = MibScalar
ctlrName = _CtlrName_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 11),
    _CtlrName_Type()
)
ctlrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlrName.setStatus("current")
_CtlrCfgModeFlags_Type = Integer32
_CtlrCfgModeFlags_Object = MibScalar
ctlrCfgModeFlags = _CtlrCfgModeFlags_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 12),
    _CtlrCfgModeFlags_Type()
)
ctlrCfgModeFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlrCfgModeFlags.setStatus("current")
_PrivateLogoString_Type = DisplayString
_PrivateLogoString_Object = MibScalar
privateLogoString = _PrivateLogoString_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 13),
    _PrivateLogoString_Type()
)
privateLogoString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateLogoString.setStatus("current")
_PrivateLogoVendor_Type = DisplayString
_PrivateLogoVendor_Object = MibScalar
privateLogoVendor = _PrivateLogoVendor_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 14),
    _PrivateLogoVendor_Type()
)
privateLogoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateLogoVendor.setStatus("current")
_PrivateLogoModel_Type = DisplayString
_PrivateLogoModel_Object = MibScalar
privateLogoModel = _PrivateLogoModel_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 15),
    _PrivateLogoModel_Type()
)
privateLogoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateLogoModel.setStatus("current")
_CtlrUniqueID_Type = DisplayString
_CtlrUniqueID_Object = MibScalar
ctlrUniqueID = _CtlrUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 16),
    _CtlrUniqueID_Type()
)
ctlrUniqueID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlrUniqueID.setStatus("current")
_SerialNumSec_Type = Integer32
_SerialNumSec_Object = MibScalar
serialNumSec = _SerialNumSec_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 1, 17),
    _SerialNumSec_Type()
)
serialNumSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumSec.setStatus("current")
_CachingParams_ObjectIdentity = ObjectIdentity
cachingParams = _CachingParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 2)
)
_CacheModeFlags_Type = Integer32
_CacheModeFlags_Object = MibScalar
cacheModeFlags = _CacheModeFlags_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 2, 1),
    _CacheModeFlags_Type()
)
cacheModeFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheModeFlags.setStatus("current")
_CacheBlkSizeIdx_Type = Integer32
_CacheBlkSizeIdx_Object = MibScalar
cacheBlkSizeIdx = _CacheBlkSizeIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 2, 2),
    _CacheBlkSizeIdx_Type()
)
cacheBlkSizeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheBlkSizeIdx.setStatus("current")
_CacheTotal_Type = Integer32
_CacheTotal_Object = MibScalar
cacheTotal = _CacheTotal_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 2, 3),
    _CacheTotal_Type()
)
cacheTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheTotal.setStatus("current")
_CacheDirty_Type = Integer32
_CacheDirty_Object = MibScalar
cacheDirty = _CacheDirty_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 2, 4),
    _CacheDirty_Type()
)
cacheDirty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheDirty.setStatus("current")
_DiskArrayParams_ObjectIdentity = ObjectIdentity
diskArrayParams = _DiskArrayParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 3)
)
_MaxRebPriorityIdx_Type = Integer32
_MaxRebPriorityIdx_Object = MibScalar
maxRebPriorityIdx = _MaxRebPriorityIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 3, 1),
    _MaxRebPriorityIdx_Type()
)
maxRebPriorityIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxRebPriorityIdx.setStatus("current")
_MinRebPriorityIdx_Type = Integer32
_MinRebPriorityIdx_Object = MibScalar
minRebPriorityIdx = _MinRebPriorityIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 3, 2),
    _MinRebPriorityIdx_Type()
)
minRebPriorityIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minRebPriorityIdx.setStatus("current")
_DefRebPriorityIdx_Type = Integer32
_DefRebPriorityIdx_Object = MibScalar
defRebPriorityIdx = _DefRebPriorityIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 3, 3),
    _DefRebPriorityIdx_Type()
)
defRebPriorityIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defRebPriorityIdx.setStatus("current")
_CurRebPriorityIdx_Type = Integer32
_CurRebPriorityIdx_Object = MibScalar
curRebPriorityIdx = _CurRebPriorityIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 3, 4),
    _CurRebPriorityIdx_Type()
)
curRebPriorityIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curRebPriorityIdx.setStatus("current")
_WriteVerifyModeFlags_Type = Integer32
_WriteVerifyModeFlags_Object = MibScalar
writeVerifyModeFlags = _WriteVerifyModeFlags_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 3, 5),
    _WriteVerifyModeFlags_Type()
)
writeVerifyModeFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    writeVerifyModeFlags.setStatus("current")
_HostSideParams_ObjectIdentity = ObjectIdentity
hostSideParams = _HostSideParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 4)
)
_MaxQueuedIOCnt_Type = Integer32
_MaxQueuedIOCnt_Object = MibScalar
maxQueuedIOCnt = _MaxQueuedIOCnt_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 4, 1),
    _MaxQueuedIOCnt_Type()
)
maxQueuedIOCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxQueuedIOCnt.setStatus("current")
_MinQueuedIOCnt_Type = Integer32
_MinQueuedIOCnt_Object = MibScalar
minQueuedIOCnt = _MinQueuedIOCnt_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 4, 2),
    _MinQueuedIOCnt_Type()
)
minQueuedIOCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minQueuedIOCnt.setStatus("current")
_DefQueuedIOCnt_Type = Integer32
_DefQueuedIOCnt_Object = MibScalar
defQueuedIOCnt = _DefQueuedIOCnt_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 4, 3),
    _DefQueuedIOCnt_Type()
)
defQueuedIOCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defQueuedIOCnt.setStatus("current")
_CurQueuedIOCnt_Type = Integer32
_CurQueuedIOCnt_Object = MibScalar
curQueuedIOCnt = _CurQueuedIOCnt_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 4, 4),
    _CurQueuedIOCnt_Type()
)
curQueuedIOCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curQueuedIOCnt.setStatus("current")
_MaxLunNum_Type = Integer32
_MaxLunNum_Object = MibScalar
maxLunNum = _MaxLunNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 4, 5),
    _MaxLunNum_Type()
)
maxLunNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLunNum.setStatus("current")
_MinLunNum_Type = Integer32
_MinLunNum_Object = MibScalar
minLunNum = _MinLunNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 4, 6),
    _MinLunNum_Type()
)
minLunNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minLunNum.setStatus("current")
_DefLunNum_Type = Integer32
_DefLunNum_Object = MibScalar
defLunNum = _DefLunNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 4, 7),
    _DefLunNum_Type()
)
defLunNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defLunNum.setStatus("current")
_CurLunNum_Type = Integer32
_CurLunNum_Object = MibScalar
curLunNum = _CurLunNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 4, 8),
    _CurLunNum_Type()
)
curLunNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curLunNum.setStatus("current")
_CurReadStatistic_Type = DisplayString
_CurReadStatistic_Object = MibScalar
curReadStatistic = _CurReadStatistic_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 4, 9),
    _CurReadStatistic_Type()
)
curReadStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curReadStatistic.setStatus("current")
_CurWriteStatistic_Type = DisplayString
_CurWriteStatistic_Object = MibScalar
curWriteStatistic = _CurWriteStatistic_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 4, 10),
    _CurWriteStatistic_Type()
)
curWriteStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curWriteStatistic.setStatus("current")
_CurReadRequests_Type = DisplayString
_CurReadRequests_Object = MibScalar
curReadRequests = _CurReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 4, 11),
    _CurReadRequests_Type()
)
curReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curReadRequests.setStatus("current")
_CurWriteRequests_Type = DisplayString
_CurWriteRequests_Object = MibScalar
curWriteRequests = _CurWriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 4, 12),
    _CurWriteRequests_Type()
)
curWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curWriteRequests.setStatus("current")
_DriveSideParams_ObjectIdentity = ObjectIdentity
driveSideParams = _DriveSideParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5)
)
_ModeFlags_Type = Integer32
_ModeFlags_Object = MibScalar
modeFlags = _ModeFlags_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 1),
    _ModeFlags_Type()
)
modeFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeFlags.setStatus("current")
_MaxAccessDelayTime_Type = Integer32
_MaxAccessDelayTime_Object = MibScalar
maxAccessDelayTime = _MaxAccessDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 2),
    _MaxAccessDelayTime_Type()
)
maxAccessDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxAccessDelayTime.setStatus("current")
_MinAccessDelayTime_Type = Integer32
_MinAccessDelayTime_Object = MibScalar
minAccessDelayTime = _MinAccessDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 3),
    _MinAccessDelayTime_Type()
)
minAccessDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minAccessDelayTime.setStatus("current")
_DefAccessDelayTime_Type = Integer32
_DefAccessDelayTime_Object = MibScalar
defAccessDelayTime = _DefAccessDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 4),
    _DefAccessDelayTime_Type()
)
defAccessDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defAccessDelayTime.setStatus("current")
_CurAccessDelayTime_Type = Integer32
_CurAccessDelayTime_Object = MibScalar
curAccessDelayTime = _CurAccessDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 5),
    _CurAccessDelayTime_Type()
)
curAccessDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curAccessDelayTime.setStatus("current")
_MaxTagCnt_Type = Integer32
_MaxTagCnt_Object = MibScalar
maxTagCnt = _MaxTagCnt_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 6),
    _MaxTagCnt_Type()
)
maxTagCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxTagCnt.setStatus("current")
_MinTagCnt_Type = Integer32
_MinTagCnt_Object = MibScalar
minTagCnt = _MinTagCnt_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 7),
    _MinTagCnt_Type()
)
minTagCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minTagCnt.setStatus("current")
_DefTagCnt_Type = Integer32
_DefTagCnt_Object = MibScalar
defTagCnt = _DefTagCnt_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 8),
    _DefTagCnt_Type()
)
defTagCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defTagCnt.setStatus("current")
_CurTagCnt_Type = Integer32
_CurTagCnt_Object = MibScalar
curTagCnt = _CurTagCnt_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 9),
    _CurTagCnt_Type()
)
curTagCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curTagCnt.setStatus("current")
_DefIOTimeout_Type = Integer32
_DefIOTimeout_Object = MibScalar
defIOTimeout = _DefIOTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 10),
    _DefIOTimeout_Type()
)
defIOTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defIOTimeout.setStatus("current")
_CurIOTimeout_Type = Integer32
_CurIOTimeout_Object = MibScalar
curIOTimeout = _CurIOTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 11),
    _CurIOTimeout_Type()
)
curIOTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curIOTimeout.setStatus("current")
_DefDrvChkPeriod_Type = Integer32
_DefDrvChkPeriod_Object = MibScalar
defDrvChkPeriod = _DefDrvChkPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 12),
    _DefDrvChkPeriod_Type()
)
defDrvChkPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defDrvChkPeriod.setStatus("current")
_CurDrvChkPeriod_Type = Integer32
_CurDrvChkPeriod_Object = MibScalar
curDrvChkPeriod = _CurDrvChkPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 13),
    _CurDrvChkPeriod_Type()
)
curDrvChkPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curDrvChkPeriod.setStatus("current")
_DefSaftePollingPeriod_Type = Integer32
_DefSaftePollingPeriod_Object = MibScalar
defSaftePollingPeriod = _DefSaftePollingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 14),
    _DefSaftePollingPeriod_Type()
)
defSaftePollingPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defSaftePollingPeriod.setStatus("current")
_CurSaftePollingPeriod_Type = Integer32
_CurSaftePollingPeriod_Object = MibScalar
curSaftePollingPeriod = _CurSaftePollingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 15),
    _CurSaftePollingPeriod_Type()
)
curSaftePollingPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curSaftePollingPeriod.setStatus("current")
_DefAutoDetectPeriod_Type = Integer32
_DefAutoDetectPeriod_Object = MibScalar
defAutoDetectPeriod = _DefAutoDetectPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 16),
    _DefAutoDetectPeriod_Type()
)
defAutoDetectPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defAutoDetectPeriod.setStatus("current")
_CurAutoDetectPeriod_Type = Integer32
_CurAutoDetectPeriod_Object = MibScalar
curAutoDetectPeriod = _CurAutoDetectPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 5, 17),
    _CurAutoDetectPeriod_Type()
)
curAutoDetectPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curAutoDetectPeriod.setStatus("current")
_RedundantParams_ObjectIdentity = ObjectIdentity
redundantParams = _RedundantParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 6)
)
_RedCtlrCfg_Type = Integer32
_RedCtlrCfg_Object = MibScalar
redCtlrCfg = _RedCtlrCfg_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 6, 1),
    _RedCtlrCfg_Type()
)
redCtlrCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redCtlrCfg.setStatus("current")
_RedCtlrModeFlags_Type = Integer32
_RedCtlrModeFlags_Object = MibScalar
redCtlrModeFlags = _RedCtlrModeFlags_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 6, 2),
    _RedCtlrModeFlags_Type()
)
redCtlrModeFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redCtlrModeFlags.setStatus("current")
_RedCtlrCommType_Type = Integer32
_RedCtlrCommType_Object = MibScalar
redCtlrCommType = _RedCtlrCommType_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 6, 3),
    _RedCtlrCommType_Type()
)
redCtlrCommType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redCtlrCommType.setStatus("current")
_RedCtlrStatus_Type = Integer32
_RedCtlrStatus_Object = MibScalar
redCtlrStatus = _RedCtlrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 1, 6, 4),
    _RedCtlrStatus_Type()
)
redCtlrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redCtlrStatus.setStatus("current")
_LdTable_Object = MibTable
ldTable = _LdTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ldTable.setStatus("current")
_LdEntry_Object = MibTableRow
ldEntry = _LdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1)
)
ldEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "ldIndex"),
)
if mibBuilder.loadTexts:
    ldEntry.setStatus("current")


class _LdIndex_Type(Integer32):
    """Custom type ldIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LdIndex_Type.__name__ = "Integer32"
_LdIndex_Object = MibTableColumn
ldIndex = _LdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 1),
    _LdIndex_Type()
)
ldIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ldIndex.setStatus("current")
_LdID_Type = DisplayString
_LdID_Object = MibTableColumn
ldID = _LdID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 2),
    _LdID_Type()
)
ldID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldID.setStatus("current")
_LdSize_Type = DisplayString
_LdSize_Object = MibTableColumn
ldSize = _LdSize_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 3),
    _LdSize_Type()
)
ldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldSize.setStatus("current")
_LdBlkSizeIdx_Type = Integer32
_LdBlkSizeIdx_Object = MibTableColumn
ldBlkSizeIdx = _LdBlkSizeIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 4),
    _LdBlkSizeIdx_Type()
)
ldBlkSizeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldBlkSizeIdx.setStatus("current")
_LdOpModes_Type = Integer32
_LdOpModes_Object = MibTableColumn
ldOpModes = _LdOpModes_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 5),
    _LdOpModes_Type()
)
ldOpModes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldOpModes.setStatus("current")
_LdStatus_Type = Integer32
_LdStatus_Object = MibTableColumn
ldStatus = _LdStatus_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 6),
    _LdStatus_Type()
)
ldStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldStatus.setStatus("current")
_LdState_Type = Integer32
_LdState_Object = MibTableColumn
ldState = _LdState_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 7),
    _LdState_Type()
)
ldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldState.setStatus("current")
_LdTotalDrvCnt_Type = Integer32
_LdTotalDrvCnt_Object = MibTableColumn
ldTotalDrvCnt = _LdTotalDrvCnt_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 8),
    _LdTotalDrvCnt_Type()
)
ldTotalDrvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldTotalDrvCnt.setStatus("current")
_LdOnlineDrvCnt_Type = Integer32
_LdOnlineDrvCnt_Object = MibTableColumn
ldOnlineDrvCnt = _LdOnlineDrvCnt_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 9),
    _LdOnlineDrvCnt_Type()
)
ldOnlineDrvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldOnlineDrvCnt.setStatus("current")
_LdSpareDrvCnt_Type = Integer32
_LdSpareDrvCnt_Object = MibTableColumn
ldSpareDrvCnt = _LdSpareDrvCnt_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 10),
    _LdSpareDrvCnt_Type()
)
ldSpareDrvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldSpareDrvCnt.setStatus("current")
_LdFailedDrvCnt_Type = Integer32
_LdFailedDrvCnt_Object = MibTableColumn
ldFailedDrvCnt = _LdFailedDrvCnt_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 11),
    _LdFailedDrvCnt_Type()
)
ldFailedDrvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldFailedDrvCnt.setStatus("current")
_LdReadStatistic_Type = DisplayString
_LdReadStatistic_Object = MibTableColumn
ldReadStatistic = _LdReadStatistic_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 12),
    _LdReadStatistic_Type()
)
ldReadStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldReadStatistic.setStatus("current")
_LdWriteStatistic_Type = DisplayString
_LdWriteStatistic_Object = MibTableColumn
ldWriteStatistic = _LdWriteStatistic_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 13),
    _LdWriteStatistic_Type()
)
ldWriteStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldWriteStatistic.setStatus("current")
_LdReadLatency_Type = DisplayString
_LdReadLatency_Object = MibTableColumn
ldReadLatency = _LdReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 14),
    _LdReadLatency_Type()
)
ldReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldReadLatency.setStatus("current")
_LdWriteLatency_Type = DisplayString
_LdWriteLatency_Object = MibTableColumn
ldWriteLatency = _LdWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 2, 1, 15),
    _LdWriteLatency_Type()
)
ldWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldWriteLatency.setStatus("current")
_LvTable_Object = MibTable
lvTable = _LvTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lvTable.setStatus("current")
_LvEntry_Object = MibTableRow
lvEntry = _LvEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 3, 1)
)
lvEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "lvIndex"),
)
if mibBuilder.loadTexts:
    lvEntry.setStatus("current")


class _LvIndex_Type(Integer32):
    """Custom type lvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LvIndex_Type.__name__ = "Integer32"
_LvIndex_Object = MibTableColumn
lvIndex = _LvIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 3, 1, 1),
    _LvIndex_Type()
)
lvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lvIndex.setStatus("current")
_LvID_Type = DisplayString
_LvID_Object = MibTableColumn
lvID = _LvID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 3, 1, 2),
    _LvID_Type()
)
lvID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lvID.setStatus("current")
_LvSize_Type = DisplayString
_LvSize_Object = MibTableColumn
lvSize = _LvSize_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 3, 1, 3),
    _LvSize_Type()
)
lvSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lvSize.setStatus("current")
_LvBlkSizeIdx_Type = Integer32
_LvBlkSizeIdx_Object = MibTableColumn
lvBlkSizeIdx = _LvBlkSizeIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 3, 1, 4),
    _LvBlkSizeIdx_Type()
)
lvBlkSizeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lvBlkSizeIdx.setStatus("current")
_LvOpModes_Type = Integer32
_LvOpModes_Object = MibTableColumn
lvOpModes = _LvOpModes_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 3, 1, 5),
    _LvOpModes_Type()
)
lvOpModes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvOpModes.setStatus("current")
_LvLdCount_Type = Integer32
_LvLdCount_Object = MibTableColumn
lvLdCount = _LvLdCount_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 3, 1, 6),
    _LvLdCount_Type()
)
lvLdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lvLdCount.setStatus("current")
_LvLdList_Type = DisplayString
_LvLdList_Object = MibTableColumn
lvLdList = _LvLdList_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 3, 1, 7),
    _LvLdList_Type()
)
lvLdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lvLdList.setStatus("current")
_PartTable_Object = MibTable
partTable = _PartTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 4)
)
if mibBuilder.loadTexts:
    partTable.setStatus("current")
_PartEntry_Object = MibTableRow
partEntry = _PartEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 4, 1)
)
partEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "partIndex"),
)
if mibBuilder.loadTexts:
    partEntry.setStatus("current")


class _PartIndex_Type(Integer32):
    """Custom type partIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PartIndex_Type.__name__ = "Integer32"
_PartIndex_Object = MibTableColumn
partIndex = _PartIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 4, 1, 1),
    _PartIndex_Type()
)
partIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    partIndex.setStatus("current")
_PartLdLvID_Type = DisplayString
_PartLdLvID_Object = MibTableColumn
partLdLvID = _PartLdLvID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 4, 1, 2),
    _PartLdLvID_Type()
)
partLdLvID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partLdLvID.setStatus("current")
_PartOffset_Type = DisplayString
_PartOffset_Object = MibTableColumn
partOffset = _PartOffset_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 4, 1, 3),
    _PartOffset_Type()
)
partOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partOffset.setStatus("current")
_PartSize_Type = DisplayString
_PartSize_Object = MibTableColumn
partSize = _PartSize_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 4, 1, 4),
    _PartSize_Type()
)
partSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partSize.setStatus("current")
_LunTable_Object = MibTable
lunTable = _LunTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 5)
)
if mibBuilder.loadTexts:
    lunTable.setStatus("current")
_LunEntry_Object = MibTableRow
lunEntry = _LunEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 5, 1)
)
lunEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "lunIndex"),
)
if mibBuilder.loadTexts:
    lunEntry.setStatus("current")


class _LunIndex_Type(Integer32):
    """Custom type lunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LunIndex_Type.__name__ = "Integer32"
_LunIndex_Object = MibTableColumn
lunIndex = _LunIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 5, 1, 1),
    _LunIndex_Type()
)
lunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lunIndex.setStatus("current")
_LunChl_Type = Integer32
_LunChl_Object = MibTableColumn
lunChl = _LunChl_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 5, 1, 2),
    _LunChl_Type()
)
lunChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunChl.setStatus("current")
_LunID_Type = Integer32
_LunID_Object = MibTableColumn
lunID = _LunID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 5, 1, 3),
    _LunID_Type()
)
lunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunID.setStatus("current")
_LunNum_Type = Integer32
_LunNum_Object = MibTableColumn
lunNum = _LunNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 5, 1, 4),
    _LunNum_Type()
)
lunNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunNum.setStatus("current")
_LunLdLvID_Type = DisplayString
_LunLdLvID_Object = MibTableColumn
lunLdLvID = _LunLdLvID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 5, 1, 5),
    _LunLdLvID_Type()
)
lunLdLvID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunLdLvID.setStatus("current")
_LunPartIdx_Type = Integer32
_LunPartIdx_Object = MibTableColumn
lunPartIdx = _LunPartIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 5, 1, 6),
    _LunPartIdx_Type()
)
lunPartIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunPartIdx.setStatus("current")
_LunSsSiID_Type = DisplayString
_LunSsSiID_Object = MibTableColumn
lunSsSiID = _LunSsSiID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 5, 1, 7),
    _LunSsSiID_Type()
)
lunSsSiID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunSsSiID.setStatus("current")
_HddTable_Object = MibTable
hddTable = _HddTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hddTable.setStatus("current")
_HddEntry_Object = MibTableRow
hddEntry = _HddEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1)
)
hddEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "hddIndex"),
)
if mibBuilder.loadTexts:
    hddEntry.setStatus("current")


class _HddIndex_Type(Integer32):
    """Custom type hddIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_HddIndex_Type.__name__ = "Integer32"
_HddIndex_Object = MibTableColumn
hddIndex = _HddIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 1),
    _HddIndex_Type()
)
hddIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hddIndex.setStatus("current")
_HddLogChlNum_Type = Integer32
_HddLogChlNum_Object = MibTableColumn
hddLogChlNum = _HddLogChlNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 2),
    _HddLogChlNum_Type()
)
hddLogChlNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddLogChlNum.setStatus("current")
_HddPhyChlNum_Type = Integer32
_HddPhyChlNum_Object = MibTableColumn
hddPhyChlNum = _HddPhyChlNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 3),
    _HddPhyChlNum_Type()
)
hddPhyChlNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddPhyChlNum.setStatus("current")
_HddScsiId_Type = Integer32
_HddScsiId_Object = MibTableColumn
hddScsiId = _HddScsiId_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 4),
    _HddScsiId_Type()
)
hddScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddScsiId.setStatus("current")
_HddScsiLun_Type = Integer32
_HddScsiLun_Object = MibTableColumn
hddScsiLun = _HddScsiLun_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 5),
    _HddScsiLun_Type()
)
hddScsiLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddScsiLun.setStatus("current")
_HddLdId_Type = DisplayString
_HddLdId_Object = MibTableColumn
hddLdId = _HddLdId_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 6),
    _HddLdId_Type()
)
hddLdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddLdId.setStatus("current")
_HddSize_Type = DisplayString
_HddSize_Object = MibTableColumn
hddSize = _HddSize_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 7),
    _HddSize_Type()
)
hddSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSize.setStatus("current")
_HddBlkSizeIdx_Type = Integer32
_HddBlkSizeIdx_Object = MibTableColumn
hddBlkSizeIdx = _HddBlkSizeIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 8),
    _HddBlkSizeIdx_Type()
)
hddBlkSizeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddBlkSizeIdx.setStatus("current")
_HddSpeed_Type = Integer32
_HddSpeed_Object = MibTableColumn
hddSpeed = _HddSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 9),
    _HddSpeed_Type()
)
hddSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSpeed.setStatus("current")
_HddDataWidth_Type = Integer32
_HddDataWidth_Object = MibTableColumn
hddDataWidth = _HddDataWidth_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 10),
    _HddDataWidth_Type()
)
hddDataWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddDataWidth.setStatus("current")
_HddStatus_Type = Integer32
_HddStatus_Object = MibTableColumn
hddStatus = _HddStatus_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 11),
    _HddStatus_Type()
)
hddStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddStatus.setStatus("current")
_HddState_Type = Integer32
_HddState_Object = MibTableColumn
hddState = _HddState_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 12),
    _HddState_Type()
)
hddState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddState.setStatus("current")
_HddSlotNum_Type = Integer32
_HddSlotNum_Object = MibTableColumn
hddSlotNum = _HddSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 13),
    _HddSlotNum_Type()
)
hddSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSlotNum.setStatus("current")
_HddResvSpace_Type = Integer32
_HddResvSpace_Object = MibTableColumn
hddResvSpace = _HddResvSpace_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 14),
    _HddResvSpace_Type()
)
hddResvSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddResvSpace.setStatus("current")
_HddModelStr_Type = DisplayString
_HddModelStr_Object = MibTableColumn
hddModelStr = _HddModelStr_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 15),
    _HddModelStr_Type()
)
hddModelStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddModelStr.setStatus("current")
_HddFwRevStr_Type = DisplayString
_HddFwRevStr_Object = MibTableColumn
hddFwRevStr = _HddFwRevStr_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 16),
    _HddFwRevStr_Type()
)
hddFwRevStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddFwRevStr.setStatus("current")
_HddSerialNum_Type = DisplayString
_HddSerialNum_Object = MibTableColumn
hddSerialNum = _HddSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 17),
    _HddSerialNum_Type()
)
hddSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSerialNum.setStatus("current")
_HddReadStatistic_Type = DisplayString
_HddReadStatistic_Object = MibTableColumn
hddReadStatistic = _HddReadStatistic_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 18),
    _HddReadStatistic_Type()
)
hddReadStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddReadStatistic.setStatus("current")
_HddWriteStatistic_Type = DisplayString
_HddWriteStatistic_Object = MibTableColumn
hddWriteStatistic = _HddWriteStatistic_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 19),
    _HddWriteStatistic_Type()
)
hddWriteStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddWriteStatistic.setStatus("current")
_HddSmart1_Type = DisplayString
_HddSmart1_Object = MibTableColumn
hddSmart1 = _HddSmart1_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 20),
    _HddSmart1_Type()
)
hddSmart1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart1.setStatus("current")
_HddSmart2_Type = DisplayString
_HddSmart2_Object = MibTableColumn
hddSmart2 = _HddSmart2_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 21),
    _HddSmart2_Type()
)
hddSmart2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart2.setStatus("current")
_HddSmart3_Type = DisplayString
_HddSmart3_Object = MibTableColumn
hddSmart3 = _HddSmart3_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 22),
    _HddSmart3_Type()
)
hddSmart3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart3.setStatus("current")
_HddSmart4_Type = DisplayString
_HddSmart4_Object = MibTableColumn
hddSmart4 = _HddSmart4_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 23),
    _HddSmart4_Type()
)
hddSmart4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart4.setStatus("current")
_HddSmart5_Type = DisplayString
_HddSmart5_Object = MibTableColumn
hddSmart5 = _HddSmart5_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 24),
    _HddSmart5_Type()
)
hddSmart5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart5.setStatus("current")
_HddSmart6_Type = DisplayString
_HddSmart6_Object = MibTableColumn
hddSmart6 = _HddSmart6_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 25),
    _HddSmart6_Type()
)
hddSmart6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart6.setStatus("current")
_HddSmart7_Type = DisplayString
_HddSmart7_Object = MibTableColumn
hddSmart7 = _HddSmart7_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 26),
    _HddSmart7_Type()
)
hddSmart7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart7.setStatus("current")
_HddSmart8_Type = DisplayString
_HddSmart8_Object = MibTableColumn
hddSmart8 = _HddSmart8_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 27),
    _HddSmart8_Type()
)
hddSmart8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart8.setStatus("current")
_HddSmart9_Type = DisplayString
_HddSmart9_Object = MibTableColumn
hddSmart9 = _HddSmart9_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 28),
    _HddSmart9_Type()
)
hddSmart9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart9.setStatus("current")
_HddSmart10_Type = DisplayString
_HddSmart10_Object = MibTableColumn
hddSmart10 = _HddSmart10_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 29),
    _HddSmart10_Type()
)
hddSmart10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart10.setStatus("current")
_HddSmart11_Type = DisplayString
_HddSmart11_Object = MibTableColumn
hddSmart11 = _HddSmart11_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 30),
    _HddSmart11_Type()
)
hddSmart11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart11.setStatus("current")
_HddSmart12_Type = DisplayString
_HddSmart12_Object = MibTableColumn
hddSmart12 = _HddSmart12_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 31),
    _HddSmart12_Type()
)
hddSmart12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart12.setStatus("current")
_HddSmart13_Type = DisplayString
_HddSmart13_Object = MibTableColumn
hddSmart13 = _HddSmart13_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 32),
    _HddSmart13_Type()
)
hddSmart13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart13.setStatus("current")
_HddSmart14_Type = DisplayString
_HddSmart14_Object = MibTableColumn
hddSmart14 = _HddSmart14_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 33),
    _HddSmart14_Type()
)
hddSmart14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart14.setStatus("current")
_HddSmart15_Type = DisplayString
_HddSmart15_Object = MibTableColumn
hddSmart15 = _HddSmart15_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 34),
    _HddSmart15_Type()
)
hddSmart15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart15.setStatus("current")
_HddSmart16_Type = DisplayString
_HddSmart16_Object = MibTableColumn
hddSmart16 = _HddSmart16_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 35),
    _HddSmart16_Type()
)
hddSmart16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart16.setStatus("current")
_HddSmart17_Type = DisplayString
_HddSmart17_Object = MibTableColumn
hddSmart17 = _HddSmart17_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 36),
    _HddSmart17_Type()
)
hddSmart17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart17.setStatus("current")
_HddSmart18_Type = DisplayString
_HddSmart18_Object = MibTableColumn
hddSmart18 = _HddSmart18_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 37),
    _HddSmart18_Type()
)
hddSmart18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart18.setStatus("current")
_HddSmart19_Type = DisplayString
_HddSmart19_Object = MibTableColumn
hddSmart19 = _HddSmart19_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 38),
    _HddSmart19_Type()
)
hddSmart19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart19.setStatus("current")
_HddSmart20_Type = DisplayString
_HddSmart20_Object = MibTableColumn
hddSmart20 = _HddSmart20_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 39),
    _HddSmart20_Type()
)
hddSmart20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart20.setStatus("current")
_HddSmart21_Type = DisplayString
_HddSmart21_Object = MibTableColumn
hddSmart21 = _HddSmart21_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 40),
    _HddSmart21_Type()
)
hddSmart21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart21.setStatus("current")
_HddSmart22_Type = DisplayString
_HddSmart22_Object = MibTableColumn
hddSmart22 = _HddSmart22_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 41),
    _HddSmart22_Type()
)
hddSmart22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart22.setStatus("current")
_HddSmart23_Type = DisplayString
_HddSmart23_Object = MibTableColumn
hddSmart23 = _HddSmart23_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 42),
    _HddSmart23_Type()
)
hddSmart23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart23.setStatus("current")
_HddSmart24_Type = DisplayString
_HddSmart24_Object = MibTableColumn
hddSmart24 = _HddSmart24_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 43),
    _HddSmart24_Type()
)
hddSmart24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart24.setStatus("current")
_HddSmart25_Type = DisplayString
_HddSmart25_Object = MibTableColumn
hddSmart25 = _HddSmart25_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 44),
    _HddSmart25_Type()
)
hddSmart25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart25.setStatus("current")
_HddSmart26_Type = DisplayString
_HddSmart26_Object = MibTableColumn
hddSmart26 = _HddSmart26_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 45),
    _HddSmart26_Type()
)
hddSmart26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart26.setStatus("current")
_HddSmart27_Type = DisplayString
_HddSmart27_Object = MibTableColumn
hddSmart27 = _HddSmart27_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 46),
    _HddSmart27_Type()
)
hddSmart27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart27.setStatus("current")
_HddSmart28_Type = DisplayString
_HddSmart28_Object = MibTableColumn
hddSmart28 = _HddSmart28_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 47),
    _HddSmart28_Type()
)
hddSmart28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart28.setStatus("current")
_HddSmart29_Type = DisplayString
_HddSmart29_Object = MibTableColumn
hddSmart29 = _HddSmart29_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 48),
    _HddSmart29_Type()
)
hddSmart29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart29.setStatus("current")
_HddSmart30_Type = DisplayString
_HddSmart30_Object = MibTableColumn
hddSmart30 = _HddSmart30_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 49),
    _HddSmart30_Type()
)
hddSmart30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddSmart30.setStatus("current")
_HddWearLife_Type = Integer32
_HddWearLife_Object = MibTableColumn
hddWearLife = _HddWearLife_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 50),
    _HddWearLife_Type()
)
hddWearLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddWearLife.setStatus("current")
_HddReadLatency_Type = DisplayString
_HddReadLatency_Object = MibTableColumn
hddReadLatency = _HddReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 51),
    _HddReadLatency_Type()
)
hddReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddReadLatency.setStatus("current")
_HddWriteLatency_Type = DisplayString
_HddWriteLatency_Object = MibTableColumn
hddWriteLatency = _HddWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 6, 1, 52),
    _HddWriteLatency_Type()
)
hddWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddWriteLatency.setStatus("current")
_ChlTable_Object = MibTable
chlTable = _ChlTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7)
)
if mibBuilder.loadTexts:
    chlTable.setStatus("current")
_ChlEntry_Object = MibTableRow
chlEntry = _ChlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1)
)
chlEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "chlIndex"),
)
if mibBuilder.loadTexts:
    chlEntry.setStatus("current")


class _ChlIndex_Type(Integer32):
    """Custom type chlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_ChlIndex_Type.__name__ = "Integer32"
_ChlIndex_Object = MibTableColumn
chlIndex = _ChlIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 1),
    _ChlIndex_Type()
)
chlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chlIndex.setStatus("current")
_ChlLogChlNum_Type = Integer32
_ChlLogChlNum_Object = MibTableColumn
chlLogChlNum = _ChlLogChlNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 2),
    _ChlLogChlNum_Type()
)
chlLogChlNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlLogChlNum.setStatus("current")
_ChlPhyChlNum_Type = Integer32
_ChlPhyChlNum_Object = MibTableColumn
chlPhyChlNum = _ChlPhyChlNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 3),
    _ChlPhyChlNum_Type()
)
chlPhyChlNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlPhyChlNum.setStatus("current")
_ChlType_Type = Integer32
_ChlType_Object = MibTableColumn
chlType = _ChlType_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 4),
    _ChlType_Type()
)
chlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlType.setStatus("current")
_ChlChipType_Type = Integer32
_ChlChipType_Object = MibTableColumn
chlChipType = _ChlChipType_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 5),
    _ChlChipType_Type()
)
chlChipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlChipType.setStatus("current")
_ChlMaxSupId_Type = Integer32
_ChlMaxSupId_Object = MibTableColumn
chlMaxSupId = _ChlMaxSupId_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 6),
    _ChlMaxSupId_Type()
)
chlMaxSupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlMaxSupId.setStatus("current")
_ChlMaxSupLun_Type = Integer32
_ChlMaxSupLun_Object = MibTableColumn
chlMaxSupLun = _ChlMaxSupLun_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 7),
    _ChlMaxSupLun_Type()
)
chlMaxSupLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlMaxSupLun.setStatus("current")
_ChlMode_Type = Integer32
_ChlMode_Object = MibTableColumn
chlMode = _ChlMode_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 8),
    _ChlMode_Type()
)
chlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlMode.setStatus("current")
_ChlScsiIdBitmap_Type = Integer32
_ChlScsiIdBitmap_Object = MibTableColumn
chlScsiIdBitmap = _ChlScsiIdBitmap_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 9),
    _ChlScsiIdBitmap_Type()
)
chlScsiIdBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlScsiIdBitmap.setStatus("current")
_ChlFibreIdBase_Type = Integer32
_ChlFibreIdBase_Object = MibTableColumn
chlFibreIdBase = _ChlFibreIdBase_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 10),
    _ChlFibreIdBase_Type()
)
chlFibreIdBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlFibreIdBase.setStatus("current")
_ChlHostIdBitmap_Type = Integer32
_ChlHostIdBitmap_Object = MibTableColumn
chlHostIdBitmap = _ChlHostIdBitmap_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 11),
    _ChlHostIdBitmap_Type()
)
chlHostIdBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlHostIdBitmap.setStatus("current")
_ChlDrvPid_Type = Integer32
_ChlDrvPid_Object = MibTableColumn
chlDrvPid = _ChlDrvPid_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 12),
    _ChlDrvPid_Type()
)
chlDrvPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlDrvPid.setStatus("current")
_ChlDrvSid_Type = Integer32
_ChlDrvSid_Object = MibTableColumn
chlDrvSid = _ChlDrvSid_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 13),
    _ChlDrvSid_Type()
)
chlDrvSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlDrvSid.setStatus("current")
_ChlMaxTxPeriod_Type = Integer32
_ChlMaxTxPeriod_Object = MibTableColumn
chlMaxTxPeriod = _ChlMaxTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 14),
    _ChlMaxTxPeriod_Type()
)
chlMaxTxPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlMaxTxPeriod.setStatus("current")
_ChlMinTxPeriod_Type = Integer32
_ChlMinTxPeriod_Object = MibTableColumn
chlMinTxPeriod = _ChlMinTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 15),
    _ChlMinTxPeriod_Type()
)
chlMinTxPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlMinTxPeriod.setStatus("current")
_ChlDefTxPeriod_Type = Integer32
_ChlDefTxPeriod_Object = MibTableColumn
chlDefTxPeriod = _ChlDefTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 16),
    _ChlDefTxPeriod_Type()
)
chlDefTxPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlDefTxPeriod.setStatus("current")
_ChlCurTxPeriod_Type = Integer32
_ChlCurTxPeriod_Object = MibTableColumn
chlCurTxPeriod = _ChlCurTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 17),
    _ChlCurTxPeriod_Type()
)
chlCurTxPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlCurTxPeriod.setStatus("current")
_ChlMaxTxWidth_Type = Integer32
_ChlMaxTxWidth_Object = MibTableColumn
chlMaxTxWidth = _ChlMaxTxWidth_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 18),
    _ChlMaxTxWidth_Type()
)
chlMaxTxWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlMaxTxWidth.setStatus("current")
_ChlMinTxWidth_Type = Integer32
_ChlMinTxWidth_Object = MibTableColumn
chlMinTxWidth = _ChlMinTxWidth_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 19),
    _ChlMinTxWidth_Type()
)
chlMinTxWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlMinTxWidth.setStatus("current")
_ChlDefTxWidth_Type = Integer32
_ChlDefTxWidth_Object = MibTableColumn
chlDefTxWidth = _ChlDefTxWidth_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 20),
    _ChlDefTxWidth_Type()
)
chlDefTxWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlDefTxWidth.setStatus("current")
_ChlCurTxWidth_Type = Integer32
_ChlCurTxWidth_Object = MibTableColumn
chlCurTxWidth = _ChlCurTxWidth_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 21),
    _ChlCurTxWidth_Type()
)
chlCurTxWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlCurTxWidth.setStatus("current")
_ChlMaxTagCnt_Type = Integer32
_ChlMaxTagCnt_Object = MibTableColumn
chlMaxTagCnt = _ChlMaxTagCnt_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 22),
    _ChlMaxTagCnt_Type()
)
chlMaxTagCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlMaxTagCnt.setStatus("current")
_ChlDefTagCnt_Type = Integer32
_ChlDefTagCnt_Object = MibTableColumn
chlDefTagCnt = _ChlDefTagCnt_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 23),
    _ChlDefTagCnt_Type()
)
chlDefTagCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlDefTagCnt.setStatus("current")
_ChlReadStatistic_Type = DisplayString
_ChlReadStatistic_Object = MibTableColumn
chlReadStatistic = _ChlReadStatistic_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 24),
    _ChlReadStatistic_Type()
)
chlReadStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlReadStatistic.setStatus("current")
_ChlWriteStatistic_Type = DisplayString
_ChlWriteStatistic_Object = MibTableColumn
chlWriteStatistic = _ChlWriteStatistic_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 25),
    _ChlWriteStatistic_Type()
)
chlWriteStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlWriteStatistic.setStatus("current")
_ChlReadRequests_Type = DisplayString
_ChlReadRequests_Object = MibTableColumn
chlReadRequests = _ChlReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 26),
    _ChlReadRequests_Type()
)
chlReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlReadRequests.setStatus("current")
_ChlWriteRequests_Type = DisplayString
_ChlWriteRequests_Object = MibTableColumn
chlWriteRequests = _ChlWriteRequests_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 7, 1, 27),
    _ChlWriteRequests_Type()
)
chlWriteRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chlWriteRequests.setStatus("current")
_LuTable_Object = MibTable
luTable = _LuTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 8)
)
if mibBuilder.loadTexts:
    luTable.setStatus("current")
_LuEntry_Object = MibTableRow
luEntry = _LuEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 8, 1)
)
luEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "luIndex"),
)
if mibBuilder.loadTexts:
    luEntry.setStatus("current")


class _LuIndex_Type(Integer32):
    """Custom type luIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_LuIndex_Type.__name__ = "Integer32"
_LuIndex_Object = MibTableColumn
luIndex = _LuIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 8, 1, 1),
    _LuIndex_Type()
)
luIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    luIndex.setStatus("current")
_LuDescriptor_Type = Integer32
_LuDescriptor_Object = MibTableColumn
luDescriptor = _LuDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 8, 1, 2),
    _LuDescriptor_Type()
)
luDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDescriptor.setStatus("current")
_LuClassCode_Type = Integer32
_LuClassCode_Object = MibTableColumn
luClassCode = _LuClassCode_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 8, 1, 3),
    _LuClassCode_Type()
)
luClassCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luClassCode.setStatus("current")
_LuTypeCode_Type = Integer32
_LuTypeCode_Object = MibTableColumn
luTypeCode = _LuTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 8, 1, 4),
    _LuTypeCode_Type()
)
luTypeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luTypeCode.setStatus("current")
_LuVendorID_Type = DisplayString
_LuVendorID_Object = MibTableColumn
luVendorID = _LuVendorID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 8, 1, 5),
    _LuVendorID_Type()
)
luVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luVendorID.setStatus("current")
_LuIDString_Type = DisplayString
_LuIDString_Object = MibTableColumn
luIDString = _LuIDString_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 8, 1, 6),
    _LuIDString_Type()
)
luIDString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luIDString.setStatus("current")
_LuHWRev_Type = DisplayString
_LuHWRev_Object = MibTableColumn
luHWRev = _LuHWRev_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 8, 1, 7),
    _LuHWRev_Type()
)
luHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luHWRev.setStatus("current")
_LuSWRev_Type = DisplayString
_LuSWRev_Object = MibTableColumn
luSWRev = _LuSWRev_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 8, 1, 8),
    _LuSWRev_Type()
)
luSWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSWRev.setStatus("current")
_LuChlNum_Type = Integer32
_LuChlNum_Object = MibTableColumn
luChlNum = _LuChlNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 8, 1, 9),
    _LuChlNum_Type()
)
luChlNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luChlNum.setStatus("current")
_LuIDNum_Type = Integer32
_LuIDNum_Object = MibTableColumn
luIDNum = _LuIDNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 8, 1, 10),
    _LuIDNum_Type()
)
luIDNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luIDNum.setStatus("current")
_LuDevTable_Object = MibTable
luDevTable = _LuDevTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9)
)
if mibBuilder.loadTexts:
    luDevTable.setStatus("current")
_LuDevEntry_Object = MibTableRow
luDevEntry = _LuDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9, 1)
)
luDevEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "luDevTabIdx"),
)
if mibBuilder.loadTexts:
    luDevEntry.setStatus("current")


class _LuDevTabIdx_Type(Integer32):
    """Custom type luDevTabIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LuDevTabIdx_Type.__name__ = "Integer32"
_LuDevTabIdx_Object = MibTableColumn
luDevTabIdx = _LuDevTabIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9, 1, 1),
    _LuDevTabIdx_Type()
)
luDevTabIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    luDevTabIdx.setStatus("current")
_LuDeviceDescriptor_Type = Integer32
_LuDeviceDescriptor_Object = MibTableColumn
luDeviceDescriptor = _LuDeviceDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9, 1, 2),
    _LuDeviceDescriptor_Type()
)
luDeviceDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDeviceDescriptor.setStatus("current")
_LuDeviceClassCode_Type = Integer32
_LuDeviceClassCode_Object = MibTableColumn
luDeviceClassCode = _LuDeviceClassCode_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9, 1, 3),
    _LuDeviceClassCode_Type()
)
luDeviceClassCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDeviceClassCode.setStatus("current")
_LuDeviceTypeCode_Type = Integer32
_LuDeviceTypeCode_Object = MibTableColumn
luDeviceTypeCode = _LuDeviceTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9, 1, 4),
    _LuDeviceTypeCode_Type()
)
luDeviceTypeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDeviceTypeCode.setStatus("current")
_LuDevDescriptor_Type = Integer32
_LuDevDescriptor_Object = MibTableColumn
luDevDescriptor = _LuDevDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9, 1, 5),
    _LuDevDescriptor_Type()
)
luDevDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDevDescriptor.setStatus("current")
_LuDevTypeCode_Type = Integer32
_LuDevTypeCode_Object = MibTableColumn
luDevTypeCode = _LuDevTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9, 1, 6),
    _LuDevTypeCode_Type()
)
luDevTypeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDevTypeCode.setStatus("current")
_LuDevIndex_Type = Integer32
_LuDevIndex_Object = MibTableColumn
luDevIndex = _LuDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9, 1, 7),
    _LuDevIndex_Type()
)
luDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDevIndex.setStatus("current")
_LuDevDescription_Type = DisplayString
_LuDevDescription_Object = MibTableColumn
luDevDescription = _LuDevDescription_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9, 1, 8),
    _LuDevDescription_Type()
)
luDevDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDevDescription.setStatus("current")
_LuDevValue_Type = Integer32
_LuDevValue_Object = MibTableColumn
luDevValue = _LuDevValue_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9, 1, 9),
    _LuDevValue_Type()
)
luDevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDevValue.setStatus("current")
_LuDevValueUnit_Type = Integer32
_LuDevValueUnit_Object = MibTableColumn
luDevValueUnit = _LuDevValueUnit_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9, 1, 10),
    _LuDevValueUnit_Type()
)
luDevValueUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDevValueUnit.setStatus("current")
_LuDevChlNum_Type = Integer32
_LuDevChlNum_Object = MibTableColumn
luDevChlNum = _LuDevChlNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9, 1, 11),
    _LuDevChlNum_Type()
)
luDevChlNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDevChlNum.setStatus("current")
_LuDevIDNum_Type = Integer32
_LuDevIDNum_Object = MibTableColumn
luDevIDNum = _LuDevIDNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9, 1, 12),
    _LuDevIDNum_Type()
)
luDevIDNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDevIDNum.setStatus("current")
_LuDevStatus_Type = Integer32
_LuDevStatus_Object = MibTableColumn
luDevStatus = _LuDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 9, 1, 13),
    _LuDevStatus_Type()
)
luDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luDevStatus.setStatus("current")
_ExtLunTable_Object = MibTable
extLunTable = _ExtLunTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 10)
)
if mibBuilder.loadTexts:
    extLunTable.setStatus("current")
_ExtLunEntry_Object = MibTableRow
extLunEntry = _ExtLunEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 10, 1)
)
extLunEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "extLunIndex"),
)
if mibBuilder.loadTexts:
    extLunEntry.setStatus("current")


class _ExtLunIndex_Type(Integer32):
    """Custom type extLunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_ExtLunIndex_Type.__name__ = "Integer32"
_ExtLunIndex_Object = MibTableColumn
extLunIndex = _ExtLunIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 10, 1, 1),
    _ExtLunIndex_Type()
)
extLunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extLunIndex.setStatus("current")
_ExtLunGroupName_Type = DisplayString
_ExtLunGroupName_Object = MibTableColumn
extLunGroupName = _ExtLunGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 10, 1, 2),
    _ExtLunGroupName_Type()
)
extLunGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extLunGroupName.setStatus("current")
_ExtLunHostIDWWN_Type = DisplayString
_ExtLunHostIDWWN_Object = MibTableColumn
extLunHostIDWWN = _ExtLunHostIDWWN_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 10, 1, 3),
    _ExtLunHostIDWWN_Type()
)
extLunHostIDWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extLunHostIDWWN.setStatus("current")
_ExtLunChl_Type = Integer32
_ExtLunChl_Object = MibTableColumn
extLunChl = _ExtLunChl_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 10, 1, 4),
    _ExtLunChl_Type()
)
extLunChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extLunChl.setStatus("current")
_ExtLunID_Type = Integer32
_ExtLunID_Object = MibTableColumn
extLunID = _ExtLunID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 10, 1, 5),
    _ExtLunID_Type()
)
extLunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extLunID.setStatus("current")
_ExtLunNum_Type = Integer32
_ExtLunNum_Object = MibTableColumn
extLunNum = _ExtLunNum_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 10, 1, 6),
    _ExtLunNum_Type()
)
extLunNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extLunNum.setStatus("current")
_ExtLunLdLvID_Type = DisplayString
_ExtLunLdLvID_Object = MibTableColumn
extLunLdLvID = _ExtLunLdLvID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 10, 1, 7),
    _ExtLunLdLvID_Type()
)
extLunLdLvID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extLunLdLvID.setStatus("current")
_ExtLunPartIdx_Type = Integer32
_ExtLunPartIdx_Object = MibTableColumn
extLunPartIdx = _ExtLunPartIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 10, 1, 8),
    _ExtLunPartIdx_Type()
)
extLunPartIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extLunPartIdx.setStatus("current")
_ExtLunSsSiID_Type = DisplayString
_ExtLunSsSiID_Object = MibTableColumn
extLunSsSiID = _ExtLunSsSiID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 10, 1, 9),
    _ExtLunSsSiID_Type()
)
extLunSsSiID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extLunSsSiID.setStatus("current")
_ExtLunHostIDMask_Type = DisplayString
_ExtLunHostIDMask_Object = MibTableColumn
extLunHostIDMask = _ExtLunHostIDMask_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 10, 1, 10),
    _ExtLunHostIDMask_Type()
)
extLunHostIDMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extLunHostIDMask.setStatus("current")
_ExtLunFilterType_Type = DisplayString
_ExtLunFilterType_Object = MibTableColumn
extLunFilterType = _ExtLunFilterType_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 10, 1, 11),
    _ExtLunFilterType_Type()
)
extLunFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extLunFilterType.setStatus("current")
_ExtLunAccessMode_Type = DisplayString
_ExtLunAccessMode_Object = MibTableColumn
extLunAccessMode = _ExtLunAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 10, 1, 12),
    _ExtLunAccessMode_Type()
)
extLunAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extLunAccessMode.setStatus("current")
_EventLog_ObjectIdentity = ObjectIdentity
eventLog = _EventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11)
)
_AllEvtTable_Object = MibTable
allEvtTable = _AllEvtTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    allEvtTable.setStatus("current")
_AllEvtEntry_Object = MibTableRow
allEvtEntry = _AllEvtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 1, 1)
)
allEvtEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "evtTableIdx"),
)
if mibBuilder.loadTexts:
    allEvtEntry.setStatus("current")


class _EvtTableIdx_Type(Integer32):
    """Custom type evtTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_EvtTableIdx_Type.__name__ = "Integer32"
_EvtTableIdx_Object = MibTableColumn
evtTableIdx = _EvtTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 1, 1, 1),
    _EvtTableIdx_Type()
)
evtTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    evtTableIdx.setStatus("current")
_EvtSource_Type = DisplayString
_EvtSource_Object = MibTableColumn
evtSource = _EvtSource_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 1, 1, 2),
    _EvtSource_Type()
)
evtSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtSource.setStatus("current")
_EvtSeverity_Type = DisplayString
_EvtSeverity_Object = MibTableColumn
evtSeverity = _EvtSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 1, 1, 3),
    _EvtSeverity_Type()
)
evtSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtSeverity.setStatus("current")
_EvtIndex_Type = Integer32
_EvtIndex_Object = MibTableColumn
evtIndex = _EvtIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 1, 1, 4),
    _EvtIndex_Type()
)
evtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtIndex.setStatus("current")
_EvtType_Type = DisplayString
_EvtType_Object = MibTableColumn
evtType = _EvtType_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 1, 1, 5),
    _EvtType_Type()
)
evtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtType.setStatus("current")
_EvtCode_Type = DisplayString
_EvtCode_Object = MibTableColumn
evtCode = _EvtCode_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 1, 1, 6),
    _EvtCode_Type()
)
evtCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtCode.setStatus("current")
_EvtTime_Type = DisplayString
_EvtTime_Object = MibTableColumn
evtTime = _EvtTime_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 1, 1, 7),
    _EvtTime_Type()
)
evtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtTime.setStatus("current")
_CtlrEvtTable_Object = MibTable
ctlrEvtTable = _CtlrEvtTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    ctlrEvtTable.setStatus("current")
_CtlrEvtEntry_Object = MibTableRow
ctlrEvtEntry = _CtlrEvtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 2, 1)
)
ctlrEvtEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "cevtTableIdx"),
)
if mibBuilder.loadTexts:
    ctlrEvtEntry.setStatus("current")


class _CevtTableIdx_Type(Integer32):
    """Custom type cevtTableIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CevtTableIdx_Type.__name__ = "Integer32"
_CevtTableIdx_Object = MibTableColumn
cevtTableIdx = _CevtTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 2, 1, 1),
    _CevtTableIdx_Type()
)
cevtTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cevtTableIdx.setStatus("current")
_CevtSource_Type = DisplayString
_CevtSource_Object = MibTableColumn
cevtSource = _CevtSource_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 2, 1, 2),
    _CevtSource_Type()
)
cevtSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevtSource.setStatus("current")
_CevtSeverity_Type = DisplayString
_CevtSeverity_Object = MibTableColumn
cevtSeverity = _CevtSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 2, 1, 3),
    _CevtSeverity_Type()
)
cevtSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevtSeverity.setStatus("current")
_CevtIndex_Type = Integer32
_CevtIndex_Object = MibTableColumn
cevtIndex = _CevtIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 2, 1, 4),
    _CevtIndex_Type()
)
cevtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevtIndex.setStatus("current")
_CevtType_Type = DisplayString
_CevtType_Object = MibTableColumn
cevtType = _CevtType_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 2, 1, 5),
    _CevtType_Type()
)
cevtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevtType.setStatus("current")
_CevtCode_Type = DisplayString
_CevtCode_Object = MibTableColumn
cevtCode = _CevtCode_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 2, 1, 6),
    _CevtCode_Type()
)
cevtCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevtCode.setStatus("current")
_CevtTime_Type = DisplayString
_CevtTime_Object = MibTableColumn
cevtTime = _CevtTime_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 2, 1, 7),
    _CevtTime_Type()
)
cevtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cevtTime.setStatus("current")
_DrvEvtTable_Object = MibTable
drvEvtTable = _DrvEvtTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 3)
)
if mibBuilder.loadTexts:
    drvEvtTable.setStatus("current")
_DrvEvtEntry_Object = MibTableRow
drvEvtEntry = _DrvEvtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 3, 1)
)
drvEvtEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "evtTableIdx"),
)
if mibBuilder.loadTexts:
    drvEvtEntry.setStatus("current")
_DevtTableIdx_Type = Integer32
_DevtTableIdx_Object = MibTableColumn
devtTableIdx = _DevtTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 3, 1, 1),
    _DevtTableIdx_Type()
)
devtTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    devtTableIdx.setStatus("current")
_DevtSource_Type = DisplayString
_DevtSource_Object = MibTableColumn
devtSource = _DevtSource_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 3, 1, 2),
    _DevtSource_Type()
)
devtSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devtSource.setStatus("current")
_DevtSeverity_Type = DisplayString
_DevtSeverity_Object = MibTableColumn
devtSeverity = _DevtSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 3, 1, 3),
    _DevtSeverity_Type()
)
devtSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devtSeverity.setStatus("current")
_DevtIndex_Type = Integer32
_DevtIndex_Object = MibTableColumn
devtIndex = _DevtIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 3, 1, 4),
    _DevtIndex_Type()
)
devtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devtIndex.setStatus("current")
_DevtType_Type = DisplayString
_DevtType_Object = MibTableColumn
devtType = _DevtType_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 3, 1, 5),
    _DevtType_Type()
)
devtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devtType.setStatus("current")
_DevtCode_Type = DisplayString
_DevtCode_Object = MibTableColumn
devtCode = _DevtCode_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 3, 1, 6),
    _DevtCode_Type()
)
devtCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devtCode.setStatus("current")
_EvtLdID_Type = DisplayString
_EvtLdID_Object = MibTableColumn
evtLdID = _EvtLdID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 3, 1, 7),
    _EvtLdID_Type()
)
evtLdID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtLdID.setStatus("current")
_EvtLogChl_Type = Integer32
_EvtLogChl_Object = MibTableColumn
evtLogChl = _EvtLogChl_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 3, 1, 8),
    _EvtLogChl_Type()
)
evtLogChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtLogChl.setStatus("current")
_EvtID_Type = Integer32
_EvtID_Object = MibTableColumn
evtID = _EvtID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 3, 1, 9),
    _EvtID_Type()
)
evtID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtID.setStatus("current")
_EvtLun_Type = Integer32
_EvtLun_Object = MibTableColumn
evtLun = _EvtLun_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 3, 1, 10),
    _EvtLun_Type()
)
evtLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtLun.setStatus("current")
_DevtTime_Type = DisplayString
_DevtTime_Object = MibTableColumn
devtTime = _DevtTime_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 3, 1, 11),
    _DevtTime_Type()
)
devtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devtTime.setStatus("current")
_HostEvtTable_Object = MibTable
hostEvtTable = _HostEvtTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 4)
)
if mibBuilder.loadTexts:
    hostEvtTable.setStatus("current")
_HostEvtEntry_Object = MibTableRow
hostEvtEntry = _HostEvtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 4, 1)
)
hostEvtEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "evtTableIdx"),
)
if mibBuilder.loadTexts:
    hostEvtEntry.setStatus("current")
_HevtTableIdx_Type = Integer32
_HevtTableIdx_Object = MibTableColumn
hevtTableIdx = _HevtTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 4, 1, 1),
    _HevtTableIdx_Type()
)
hevtTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hevtTableIdx.setStatus("current")
_HevtSource_Type = DisplayString
_HevtSource_Object = MibTableColumn
hevtSource = _HevtSource_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 4, 1, 2),
    _HevtSource_Type()
)
hevtSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hevtSource.setStatus("current")
_HevtSeverity_Type = DisplayString
_HevtSeverity_Object = MibTableColumn
hevtSeverity = _HevtSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 4, 1, 3),
    _HevtSeverity_Type()
)
hevtSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hevtSeverity.setStatus("current")
_HevtIndex_Type = Integer32
_HevtIndex_Object = MibTableColumn
hevtIndex = _HevtIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 4, 1, 4),
    _HevtIndex_Type()
)
hevtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hevtIndex.setStatus("current")
_HevtType_Type = DisplayString
_HevtType_Object = MibTableColumn
hevtType = _HevtType_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 4, 1, 5),
    _HevtType_Type()
)
hevtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hevtType.setStatus("current")
_HevtCode_Type = DisplayString
_HevtCode_Object = MibTableColumn
hevtCode = _HevtCode_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 4, 1, 6),
    _HevtCode_Type()
)
hevtCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hevtCode.setStatus("current")
_EvtChl_Type = Integer32
_EvtChl_Object = MibTableColumn
evtChl = _EvtChl_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 4, 1, 7),
    _EvtChl_Type()
)
evtChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtChl.setStatus("current")
_HevtID_Type = Integer32
_HevtID_Object = MibTableColumn
hevtID = _HevtID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 4, 1, 8),
    _HevtID_Type()
)
hevtID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hevtID.setStatus("current")
_HevtLun_Type = Integer32
_HevtLun_Object = MibTableColumn
hevtLun = _HevtLun_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 4, 1, 9),
    _HevtLun_Type()
)
hevtLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hevtLun.setStatus("current")
_HevtTime_Type = DisplayString
_HevtTime_Object = MibTableColumn
hevtTime = _HevtTime_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 4, 1, 10),
    _HevtTime_Type()
)
hevtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hevtTime.setStatus("current")
_LdEvtTable_Object = MibTable
ldEvtTable = _LdEvtTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 5)
)
if mibBuilder.loadTexts:
    ldEvtTable.setStatus("current")
_LdEvtEntry_Object = MibTableRow
ldEvtEntry = _LdEvtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 5, 1)
)
ldEvtEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "evtTableIdx"),
)
if mibBuilder.loadTexts:
    ldEvtEntry.setStatus("current")
_LdevtTableIdx_Type = Integer32
_LdevtTableIdx_Object = MibTableColumn
ldevtTableIdx = _LdevtTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 5, 1, 1),
    _LdevtTableIdx_Type()
)
ldevtTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ldevtTableIdx.setStatus("current")
_LdevtSource_Type = DisplayString
_LdevtSource_Object = MibTableColumn
ldevtSource = _LdevtSource_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 5, 1, 2),
    _LdevtSource_Type()
)
ldevtSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevtSource.setStatus("current")
_LdevtSeverity_Type = DisplayString
_LdevtSeverity_Object = MibTableColumn
ldevtSeverity = _LdevtSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 5, 1, 3),
    _LdevtSeverity_Type()
)
ldevtSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevtSeverity.setStatus("current")
_LdevtIndex_Type = Integer32
_LdevtIndex_Object = MibTableColumn
ldevtIndex = _LdevtIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 5, 1, 4),
    _LdevtIndex_Type()
)
ldevtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevtIndex.setStatus("current")
_LdevtType_Type = DisplayString
_LdevtType_Object = MibTableColumn
ldevtType = _LdevtType_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 5, 1, 5),
    _LdevtType_Type()
)
ldevtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevtType.setStatus("current")
_LdevtCode_Type = DisplayString
_LdevtCode_Object = MibTableColumn
ldevtCode = _LdevtCode_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 5, 1, 6),
    _LdevtCode_Type()
)
ldevtCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevtCode.setStatus("current")
_LdevtLdID_Type = DisplayString
_LdevtLdID_Object = MibTableColumn
ldevtLdID = _LdevtLdID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 5, 1, 7),
    _LdevtLdID_Type()
)
ldevtLdID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevtLdID.setStatus("current")
_EvtFailedChl_Type = Integer32
_EvtFailedChl_Object = MibTableColumn
evtFailedChl = _EvtFailedChl_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 5, 1, 8),
    _EvtFailedChl_Type()
)
evtFailedChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtFailedChl.setStatus("current")
_EvtFailedID_Type = Integer32
_EvtFailedID_Object = MibTableColumn
evtFailedID = _EvtFailedID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 5, 1, 9),
    _EvtFailedID_Type()
)
evtFailedID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtFailedID.setStatus("current")
_EvtFailedLun_Type = Integer32
_EvtFailedLun_Object = MibTableColumn
evtFailedLun = _EvtFailedLun_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 5, 1, 10),
    _EvtFailedLun_Type()
)
evtFailedLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtFailedLun.setStatus("current")
_LdevtTime_Type = DisplayString
_LdevtTime_Object = MibTableColumn
ldevtTime = _LdevtTime_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 5, 1, 11),
    _LdevtTime_Type()
)
ldevtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldevtTime.setStatus("current")
_GtEvtTable_Object = MibTable
gtEvtTable = _GtEvtTable_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6)
)
if mibBuilder.loadTexts:
    gtEvtTable.setStatus("current")
_GtEvtEntry_Object = MibTableRow
gtEvtEntry = _GtEvtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1)
)
gtEvtEntry.setIndexNames(
    (0, "IFT-SNMP-MIB", "evtTableIdx"),
)
if mibBuilder.loadTexts:
    gtEvtEntry.setStatus("current")
_GtevtTableIdx_Type = Integer32
_GtevtTableIdx_Object = MibTableColumn
gtevtTableIdx = _GtevtTableIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 1),
    _GtevtTableIdx_Type()
)
gtevtTableIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gtevtTableIdx.setStatus("current")
_GtevtSource_Type = DisplayString
_GtevtSource_Object = MibTableColumn
gtevtSource = _GtevtSource_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 2),
    _GtevtSource_Type()
)
gtevtSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtevtSource.setStatus("current")
_GtevtSeverity_Type = DisplayString
_GtevtSeverity_Object = MibTableColumn
gtevtSeverity = _GtevtSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 3),
    _GtevtSeverity_Type()
)
gtevtSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtevtSeverity.setStatus("current")
_GtevtIndex_Type = Integer32
_GtevtIndex_Object = MibTableColumn
gtevtIndex = _GtevtIndex_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 4),
    _GtevtIndex_Type()
)
gtevtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtevtIndex.setStatus("current")
_GtevtType_Type = DisplayString
_GtevtType_Object = MibTableColumn
gtevtType = _GtevtType_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 5),
    _GtevtType_Type()
)
gtevtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtevtType.setStatus("current")
_EvtLuDesc_Type = Integer32
_EvtLuDesc_Object = MibTableColumn
evtLuDesc = _EvtLuDesc_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 6),
    _EvtLuDesc_Type()
)
evtLuDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtLuDesc.setStatus("current")
_EvtLuDevDesc_Type = Integer32
_EvtLuDevDesc_Object = MibTableColumn
evtLuDevDesc = _EvtLuDevDesc_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 7),
    _EvtLuDevDesc_Type()
)
evtLuDevDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtLuDevDesc.setStatus("current")
_EvtLuClass_Type = Integer32
_EvtLuClass_Object = MibTableColumn
evtLuClass = _EvtLuClass_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 8),
    _EvtLuClass_Type()
)
evtLuClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtLuClass.setStatus("current")
_EvtLuSubClass_Type = Integer32
_EvtLuSubClass_Object = MibTableColumn
evtLuSubClass = _EvtLuSubClass_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 9),
    _EvtLuSubClass_Type()
)
evtLuSubClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtLuSubClass.setStatus("current")
_GtevtCode_Type = DisplayString
_GtevtCode_Object = MibTableColumn
gtevtCode = _GtevtCode_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 10),
    _GtevtCode_Type()
)
gtevtCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtevtCode.setStatus("current")
_EvtLuDevType_Type = DisplayString
_EvtLuDevType_Object = MibTableColumn
evtLuDevType = _EvtLuDevType_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 11),
    _EvtLuDevType_Type()
)
evtLuDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtLuDevType.setStatus("current")
_EvtLuDevIdx_Type = Integer32
_EvtLuDevIdx_Object = MibTableColumn
evtLuDevIdx = _EvtLuDevIdx_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 12),
    _EvtLuDevIdx_Type()
)
evtLuDevIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtLuDevIdx.setStatus("current")
_EvtEncChl_Type = Integer32
_EvtEncChl_Object = MibTableColumn
evtEncChl = _EvtEncChl_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 13),
    _EvtEncChl_Type()
)
evtEncChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtEncChl.setStatus("current")
_EvtEncID_Type = Integer32
_EvtEncID_Object = MibTableColumn
evtEncID = _EvtEncID_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 14),
    _EvtEncID_Type()
)
evtEncID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtEncID.setStatus("current")
_EvtEncLun_Type = Integer32
_EvtEncLun_Object = MibTableColumn
evtEncLun = _EvtEncLun_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 15),
    _EvtEncLun_Type()
)
evtEncLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtEncLun.setStatus("current")
_GtevtTime_Type = DisplayString
_GtevtTime_Object = MibTableColumn
gtevtTime = _GtevtTime_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 1, 11, 6, 1, 16),
    _GtevtTime_Type()
)
gtevtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtevtTime.setStatus("current")
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000)
)
_EventString_Type = DisplayString
_EventString_Object = MibScalar
eventString = _EventString_Object(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8001),
    _EventString_Type()
)
eventString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventString.setStatus("mandatory")

# Managed Objects groups


# Notification objects

controller_memory_error_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 66564)
)
controller_memory_error_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_memory_error_detected.setStatus(
        ""
    )

memory_ECC_single_bit_error_has_been_corrected_in_DIMM_module = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 66567)
)
memory_ECC_single_bit_error_has_been_corrected_in_DIMM_module.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    memory_ECC_single_bit_error_has_been_corrected_in_DIMM_module.setStatus(
        ""
    )

inconsistent_board_ID_between_the_controllers_has_been_found = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67585)
)
inconsistent_board_ID_between_the_controllers_has_been_found.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_board_ID_between_the_controllers_has_been_found.setStatus(
        ""
    )

inconsistent_board_rev_number_between_the_controllers = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67586)
)
inconsistent_board_rev_number_between_the_controllers.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_board_rev_number_between_the_controllers.setStatus(
        ""
    )

invalid_hardware_settings_have_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67587)
)
invalid_hardware_settings_have_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    invalid_hardware_settings_have_been_detected.setStatus(
        ""
    )

inconsistent_HW_setting_ID_between_the_controllers = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67588)
)
inconsistent_HW_setting_ID_between_the_controllers.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_HW_setting_ID_between_the_controllers.setStatus(
        ""
    )

inconsistent_host_board_1_HW_setting_ID_between_the_controllers = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67589)
)
inconsistent_host_board_1_HW_setting_ID_between_the_controllers.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_host_board_1_HW_setting_ID_between_the_controllers.setStatus(
        ""
    )

inconsistent_host_board_2_HW_setting_ID_between_the_controllers = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67590)
)
inconsistent_host_board_2_HW_setting_ID_between_the_controllers.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_host_board_2_HW_setting_ID_between_the_controllers.setStatus(
        ""
    )

inconsistent_DRAM_size_between_the_controllers_has_been_found = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67591)
)
inconsistent_DRAM_size_between_the_controllers_has_been_found.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_DRAM_size_between_the_controllers_has_been_found.setStatus(
        ""
    )

inconsistent_NVRAM_size_between_the_controllers_has_been_found = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67592)
)
inconsistent_NVRAM_size_between_the_controllers_has_been_found.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_NVRAM_size_between_the_controllers_has_been_found.setStatus(
        ""
    )

inconsistent_hostboard_3_HW_setting_ID_between_the_controllers = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67594)
)
inconsistent_hostboard_3_HW_setting_ID_between_the_controllers.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_hostboard_3_HW_setting_ID_between_the_controllers.setStatus(
        ""
    )

inconsistent_hostboard_4_HW_setting_ID_between_the_controllers = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67595)
)
inconsistent_hostboard_4_HW_setting_ID_between_the_controllers.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_hostboard_4_HW_setting_ID_between_the_controllers.setStatus(
        ""
    )

inconsistent_hostboard_5_HW_setting_ID_between_the_controllers = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67596)
)
inconsistent_hostboard_5_HW_setting_ID_between_the_controllers.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_hostboard_5_HW_setting_ID_between_the_controllers.setStatus(
        ""
    )

inconsistent_hostboard_6_HW_setting_ID_between_the_controllers = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67597)
)
inconsistent_hostboard_6_HW_setting_ID_between_the_controllers.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_hostboard_6_HW_setting_ID_between_the_controllers.setStatus(
        ""
    )

inconsistent_hostboard_7_HW_setting_ID_between_the_controllers = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67598)
)
inconsistent_hostboard_7_HW_setting_ID_between_the_controllers.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_hostboard_7_HW_setting_ID_between_the_controllers.setStatus(
        ""
    )

inconsistent_hostboard_8_HW_setting_ID_between_the_controllers = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67599)
)
inconsistent_hostboard_8_HW_setting_ID_between_the_controllers.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_hostboard_8_HW_setting_ID_between_the_controllers.setStatus(
        ""
    )

inconsistent_hostboard_9_HW_setting_ID_between_the_controllers = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67600)
)
inconsistent_hostboard_9_HW_setting_ID_between_the_controllers.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_hostboard_9_HW_setting_ID_between_the_controllers.setStatus(
        ""
    )

inconsistent_hostboard_10_HW_setting_ID_between_the_controllers = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67601)
)
inconsistent_hostboard_10_HW_setting_ID_between_the_controllers.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    inconsistent_hostboard_10_HW_setting_ID_between_the_controllers.setStatus(
        ""
    )

a_non_supported_host_board_has_been_installed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 67841)
)
a_non_supported_host_board_has_been_installed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_non_supported_host_board_has_been_installed.setStatus(
        ""
    )

the_secondary_controller_is_incompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 69633)
)
the_secondary_controller_is_incompatible.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_secondary_controller_is_incompatible.setStatus(
        ""
    )

the_fatal_failed_LD_contains_unsaved_write_cache_data = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 69633)
)
the_fatal_failed_LD_contains_unsaved_write_cache_data.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_fatal_failed_LD_contains_unsaved_write_cache_data.setStatus(
        ""
    )

the_memory_size_of_the_secondary_controller_is_inconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 69634)
)
the_memory_size_of_the_secondary_controller_is_inconsistent.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_memory_size_of_the_secondary_controller_is_inconsistent.setStatus(
        ""
    )

the_secondary_controller_is_waiting_for_write_cache_recovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 69634)
)
the_secondary_controller_is_waiting_for_write_cache_recovery.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_secondary_controller_is_waiting_for_write_cache_recovery.setStatus(
        ""
    )

the_secondary_controller_with_cache_data_is_not_for_the_device = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 69635)
)
the_secondary_controller_with_cache_data_is_not_for_the_device.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_secondary_controller_with_cache_data_is_not_for_the_device.setStatus(
        ""
    )

the_firmware_of_the_secondary_controller_is_incompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 69636)
)
the_firmware_of_the_secondary_controller_is_incompatible.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_firmware_of_the_secondary_controller_is_incompatible.setStatus(
        ""
    )

cache_memory_range_of_the_secondary_controller_is_incompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 69637)
)
cache_memory_range_of_the_secondary_controller_is_incompatible.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    cache_memory_range_of_the_secondary_controller_is_incompatible.setStatus(
        ""
    )

redundant_controller_failure_or_shutdown_was_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 69889)
)
redundant_controller_failure_or_shutdown_was_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    redundant_controller_failure_or_shutdown_was_detected.setStatus(
        ""
    )

redundant_controller_has_shut_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 69890)
)
redundant_controller_has_shut_down.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    redundant_controller_has_shut_down.setStatus(
        ""
    )

controller_had_a_hardware_error_and_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 69891)
)
controller_had_a_hardware_error_and_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_had_a_hardware_error_and_failed.setStatus(
        ""
    )

redundant_controller_firmware_updated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 69892)
)
redundant_controller_firmware_updated.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    redundant_controller_firmware_updated.setStatus(
        ""
    )

the_controller_write_policy_was_forced_to_write_through_mode = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 70145)
)
the_controller_write_policy_was_forced_to_write_through_mode.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_controller_write_policy_was_forced_to_write_through_mode.setStatus(
        ""
    )

controller_initialization_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 98561)
)
controller_initialization_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_initialization_completed.setStatus(
        ""
    )

controller_slot_B_booted_as_primary_controller = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 98562)
)
controller_slot_B_booted_as_primary_controller.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_slot_B_booted_as_primary_controller.setStatus(
        ""
    )

firmware_synchronization_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 98817)
)
firmware_synchronization_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    firmware_synchronization_started.setStatus(
        ""
    )

firmware_synchronization_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 98818)
)
firmware_synchronization_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    firmware_synchronization_completed.setStatus(
        ""
    )

controller_NVRAM_factory_default_settings_restored = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 100609)
)
controller_NVRAM_factory_default_settings_restored.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_NVRAM_factory_default_settings_restored.setStatus(
        ""
    )

the_device_password_has_been_reset = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 100609)
)
the_device_password_has_been_reset.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_device_password_has_been_reset.setStatus(
        ""
    )

controller_NVRAM_restore_from_file_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 100610)
)
controller_NVRAM_restore_from_file_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_NVRAM_restore_from_file_completed.setStatus(
        ""
    )

controller_NVRAM_restore_from_drive_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 100611)
)
controller_NVRAM_restore_from_drive_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_NVRAM_restore_from_drive_completed.setStatus(
        ""
    )

cache_data_present_during_system_power_on = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 100865)
)
cache_data_present_during_system_power_on.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    cache_data_present_during_system_power_on.setStatus(
        ""
    )

the_controller_write_policy_default_setting_was_restored = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 102913)
)
the_controller_write_policy_default_setting_was_restored.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_controller_write_policy_default_setting_was_restored.setStatus(
        ""
    )

controller_shutdown_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 102914)
)
controller_shutdown_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_shutdown_started.setStatus(
        ""
    )

controller_shutdown_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 102915)
)
controller_shutdown_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_shutdown_completed.setStatus(
        ""
    )

enclosure_drawer_is_opened = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 131329)
)
enclosure_drawer_is_opened.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_drawer_is_opened.setStatus(
        ""
    )

expansion_enclosure_drawer_is_opened = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 131330)
)
expansion_enclosure_drawer_is_opened.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_drawer_is_opened.setStatus(
        ""
    )

enclosure_drawer_is_not_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 131331)
)
enclosure_drawer_is_not_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_drawer_is_not_detected.setStatus(
        ""
    )

expansion_enclosure_drawer_is_not_ready_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 131332)
)
expansion_enclosure_drawer_is_not_ready_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_drawer_is_not_ready_has_been_detected.setStatus(
        ""
    )

invalid_or_conflicting_enclosure_ID_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 135425)
)
invalid_or_conflicting_enclosure_ID_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    invalid_or_conflicting_enclosure_ID_detected.setStatus(
        ""
    )

enclosure_drive_configuration_error_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 135681)
)
enclosure_drive_configuration_error_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_drive_configuration_error_detected.setStatus(
        ""
    )

expansion_enclosure_drive_configuration_error_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 135682)
)
expansion_enclosure_drive_configuration_error_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_drive_configuration_error_detected.setStatus(
        ""
    )

expansion_enclosure_is_not_supported = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 135937)
)
expansion_enclosure_is_not_supported.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_is_not_supported.setStatus(
        ""
    )

enclosure_drawer_is_closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 164097)
)
enclosure_drawer_is_closed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_drawer_is_closed.setStatus(
        ""
    )

expansion_enclosure_drawer_is_closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 164098)
)
expansion_enclosure_drawer_is_closed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_drawer_is_closed.setStatus(
        ""
    )

enclosure_drawer_back_is_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 164099)
)
enclosure_drawer_back_is_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_drawer_back_is_to_normal.setStatus(
        ""
    )

expansion_enclosure_drawer_is_back_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 164100)
)
expansion_enclosure_drawer_is_back_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_drawer_is_back_to_normal.setStatus(
        ""
    )

power_supply_voltage_3_3V_is_lower_than_lower_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 205057)
)
power_supply_voltage_3_3V_is_lower_than_lower_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    power_supply_voltage_3_3V_is_lower_than_lower_threshold.setStatus(
        ""
    )

power_supply_voltage_5V_is_lower_than_lower_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 205058)
)
power_supply_voltage_5V_is_lower_than_lower_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    power_supply_voltage_5V_is_lower_than_lower_threshold.setStatus(
        ""
    )

power_supply_voltage_12V_is_lower_than_lower_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 205059)
)
power_supply_voltage_12V_is_lower_than_lower_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    power_supply_voltage_12V_is_lower_than_lower_threshold.setStatus(
        ""
    )

power_supply_voltage_3_3V_is_higher_than_upper_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 205060)
)
power_supply_voltage_3_3V_is_higher_than_upper_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    power_supply_voltage_3_3V_is_higher_than_upper_threshold.setStatus(
        ""
    )

power_supply_voltage_5V_is_higher_than_upper_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 205061)
)
power_supply_voltage_5V_is_higher_than_upper_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    power_supply_voltage_5V_is_higher_than_upper_threshold.setStatus(
        ""
    )

power_supply_voltage_12V_is_higher_than_upper_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 205062)
)
power_supply_voltage_12V_is_higher_than_upper_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    power_supply_voltage_12V_is_higher_than_upper_threshold.setStatus(
        ""
    )

enclosure_power_supply_sensor_detection_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 205063)
)
enclosure_power_supply_sensor_detection_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_power_supply_sensor_detection_failed.setStatus(
        ""
    )

power_supply_in_JBOD_failed_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 205064)
)
power_supply_in_JBOD_failed_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    power_supply_in_JBOD_failed_has_been_detected.setStatus(
        ""
    )

power_supply_in_storage_system_failed_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 205065)
)
power_supply_in_storage_system_failed_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    power_supply_in_storage_system_failed_has_been_detected.setStatus(
        ""
    )

expansion_enclosure_power_supply_is_absent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 205068)
)
expansion_enclosure_power_supply_is_absent.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_power_supply_is_absent.setStatus(
        ""
    )

power_supply_in_storage_system_is_missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 205069)
)
power_supply_in_storage_system_is_missing.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    power_supply_in_storage_system_is_missing.setStatus(
        ""
    )

expansion_enclosure_power_supply_absent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 205073)
)
expansion_enclosure_power_supply_absent.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_power_supply_absent.setStatus(
        ""
    )

expansion_enclosure_power_supply_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 205086)
)
expansion_enclosure_power_supply_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_power_supply_failed.setStatus(
        ""
    )

psu_voltage_3_3V_is_back_to_normal_and_below_upper_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 237826)
)
psu_voltage_3_3V_is_back_to_normal_and_below_upper_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    psu_voltage_3_3V_is_back_to_normal_and_below_upper_threshold.setStatus(
        ""
    )

psu_voltage_5V_is_back_to_normal_and_below_upper_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 237827)
)
psu_voltage_5V_is_back_to_normal_and_below_upper_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    psu_voltage_5V_is_back_to_normal_and_below_upper_threshold.setStatus(
        ""
    )

psu_voltage_12V_is_back_to_normal_and_below_upper_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 237828)
)
psu_voltage_12V_is_back_to_normal_and_below_upper_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    psu_voltage_12V_is_back_to_normal_and_below_upper_threshold.setStatus(
        ""
    )

psu_voltage_3_3V_is_back_to_normal_and_above_lower_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 237829)
)
psu_voltage_3_3V_is_back_to_normal_and_above_lower_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    psu_voltage_3_3V_is_back_to_normal_and_above_lower_threshold.setStatus(
        ""
    )

psu_voltage_5V_is_back_to_normal_and_above_lower_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 237830)
)
psu_voltage_5V_is_back_to_normal_and_above_lower_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    psu_voltage_5V_is_back_to_normal_and_above_lower_threshold.setStatus(
        ""
    )

psu_voltage_12V_is_back_to_normal_and_above_lower_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 237831)
)
psu_voltage_12V_is_back_to_normal_and_above_lower_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    psu_voltage_12V_is_back_to_normal_and_above_lower_threshold.setStatus(
        ""
    )

enclosure_power_supply_sensor_back_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 237832)
)
enclosure_power_supply_sensor_back_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_power_supply_sensor_back_to_normal.setStatus(
        ""
    )

expansion_enclosure_PSU_failed_status_recovered_to_on_line = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 237837)
)
expansion_enclosure_PSU_failed_status_recovered_to_on_line.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_PSU_failed_status_recovered_to_on_line.setStatus(
        ""
    )

enclosure_PSU_failed_status_recovered_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 237838)
)
enclosure_PSU_failed_status_recovered_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_PSU_failed_status_recovered_to_normal.setStatus(
        ""
    )

expansion_enclosure_PSU_absent_status_recovered_to_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 237839)
)
expansion_enclosure_PSU_absent_status_recovered_to_present.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_PSU_absent_status_recovered_to_present.setStatus(
        ""
    )

enclosure_PSU_absent_status_recovered_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 237840)
)
enclosure_PSU_absent_status_recovered_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_PSU_absent_status_recovered_to_normal.setStatus(
        ""
    )

expansion_enclosure_power_supply_back_to_on_line = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 237841)
)
expansion_enclosure_power_supply_back_to_on_line.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_power_supply_back_to_on_line.setStatus(
        ""
    )

controller_flash_backup_module_FBM_absent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 271618)
)
controller_flash_backup_module_FBM_absent.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_flash_backup_module_FBM_absent.setStatus(
        ""
    )

flash_Backup_Module_FBM_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 271619)
)
flash_Backup_Module_FBM_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    flash_Backup_Module_FBM_failed.setStatus(
        ""
    )

battery_Backup_Unit_BBU_is_missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 271620)
)
battery_Backup_Unit_BBU_is_missing.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    battery_Backup_Unit_BBU_is_missing.setStatus(
        ""
    )

battery_Backup_Unit_BBU_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 271621)
)
battery_Backup_Unit_BBU_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    battery_Backup_Unit_BBU_failed.setStatus(
        ""
    )

controller_battery_backup_unit_BBU_charging = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 271622)
)
controller_battery_backup_unit_BBU_charging.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_battery_backup_unit_BBU_charging.setStatus(
        ""
    )

battery_Backup_Unit_BBU_error_is_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 271623)
)
battery_Backup_Unit_BBU_error_is_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    battery_Backup_Unit_BBU_error_is_detected.setStatus(
        ""
    )

super_capacitor_is_missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 271624)
)
super_capacitor_is_missing.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    super_capacitor_is_missing.setStatus(
        ""
    )

super_capacitor_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 271625)
)
super_capacitor_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    super_capacitor_failed.setStatus(
        ""
    )

controller_Super_Capacitor_is_charging = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 271626)
)
controller_Super_Capacitor_is_charging.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_Super_Capacitor_is_charging.setStatus(
        ""
    )

controller_Super_Capacitor_error_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 271627)
)
controller_Super_Capacitor_error_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_Super_Capacitor_error_has_been_detected.setStatus(
        ""
    )

controller_battery_backup_unit_BBU_back_to_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 304385)
)
controller_battery_backup_unit_BBU_back_to_present.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_battery_backup_unit_BBU_back_to_present.setStatus(
        ""
    )

controller_battery_backup_unit_BBU_back_to_on_line = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 304386)
)
controller_battery_backup_unit_BBU_back_to_on_line.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_battery_backup_unit_BBU_back_to_on_line.setStatus(
        ""
    )

controller_battery_backup_unit_BBU_fully_charged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 304387)
)
controller_battery_backup_unit_BBU_fully_charged.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_battery_backup_unit_BBU_fully_charged.setStatus(
        ""
    )

controller_Super_Capacitor_is_back_to_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 304388)
)
controller_Super_Capacitor_is_back_to_present.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_Super_Capacitor_is_back_to_present.setStatus(
        ""
    )

controller_Super_Capacitor_is_back_to_on_line = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 304389)
)
controller_Super_Capacitor_is_back_to_on_line.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_Super_Capacitor_is_back_to_on_line.setStatus(
        ""
    )

controller_Super_Capacitor_has_been_fully_charged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 304390)
)
controller_Super_Capacitor_has_been_fully_charged.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_Super_Capacitor_has_been_fully_charged.setStatus(
        ""
    )

enclosure_fan_sensor_detection_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 336385)
)
enclosure_fan_sensor_detection_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_fan_sensor_detection_failed.setStatus(
        ""
    )

expansion_enclosure_fan_failed_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 336394)
)
expansion_enclosure_fan_failed_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_fan_failed_has_been_detected.setStatus(
        ""
    )

enclosure_fan_failed_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 336395)
)
enclosure_fan_failed_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_fan_failed_has_been_detected.setStatus(
        ""
    )

expansion_enclosure_fan_absent_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 336396)
)
expansion_enclosure_fan_absent_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_fan_absent_has_been_detected.setStatus(
        ""
    )

enclosure_fan_absent_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 336397)
)
enclosure_fan_absent_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_fan_absent_has_been_detected.setStatus(
        ""
    )

expansion_enclosure_fan_low_speed_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 336398)
)
expansion_enclosure_fan_low_speed_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_fan_low_speed_has_been_detected.setStatus(
        ""
    )

enclosure_fan_low_speed_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 336400)
)
enclosure_fan_low_speed_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_fan_low_speed_has_been_detected.setStatus(
        ""
    )

expansion_enclosure_fan_absent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 336403)
)
expansion_enclosure_fan_absent.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_fan_absent.setStatus(
        ""
    )

fan_in_JBOD_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 336406)
)
fan_in_JBOD_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    fan_in_JBOD_failed.setStatus(
        ""
    )

cpu_FAN_failure_has_been_detected_with_FAN_number = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 336411)
)
cpu_FAN_failure_has_been_detected_with_FAN_number.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    cpu_FAN_failure_has_been_detected_with_FAN_number.setStatus(
        ""
    )

enclosure_drawer_fan_failed_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 336459)
)
enclosure_drawer_fan_failed_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_drawer_fan_failed_has_been_detected.setStatus(
        ""
    )

enclosure_drawer_fan_absent_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 336461)
)
enclosure_drawer_fan_absent_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_drawer_fan_absent_has_been_detected.setStatus(
        ""
    )

enclosure_drawer_fan_low_speed_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 336464)
)
enclosure_drawer_fan_low_speed_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_drawer_fan_low_speed_has_been_detected.setStatus(
        ""
    )

enclosure_fan_back_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369156)
)
enclosure_fan_back_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_fan_back_to_normal.setStatus(
        ""
    )

expansion_enclosure_fan_backed_to_on_line = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369163)
)
expansion_enclosure_fan_backed_to_on_line.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_fan_backed_to_on_line.setStatus(
        ""
    )

enclosure_fan_is_back_to_on_line = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369164)
)
enclosure_fan_is_back_to_on_line.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_fan_is_back_to_on_line.setStatus(
        ""
    )

expansion_enclosure_fan_backed_to_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369165)
)
expansion_enclosure_fan_backed_to_present.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_fan_backed_to_present.setStatus(
        ""
    )

enclosure_fan_is_back_to_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369166)
)
enclosure_fan_is_back_to_present.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_fan_is_back_to_present.setStatus(
        ""
    )

expansion_enclosure_fan_backed_to_normal_speed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369167)
)
expansion_enclosure_fan_backed_to_normal_speed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_fan_backed_to_normal_speed.setStatus(
        ""
    )

enclosure_fan_is_back_to_normal_speed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369168)
)
enclosure_fan_is_back_to_normal_speed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_fan_is_back_to_normal_speed.setStatus(
        ""
    )

expansion_enclosure_fan_back_to_on_line = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369169)
)
expansion_enclosure_fan_back_to_on_line.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_fan_back_to_on_line.setStatus(
        ""
    )

cpu_FAN_is_back_online_with_FAN_number = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369170)
)
cpu_FAN_is_back_online_with_FAN_number.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    cpu_FAN_is_back_online_with_FAN_number.setStatus(
        ""
    )

expansion_enclosure_drawer_fan_is_back_to_on_line = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369227)
)
expansion_enclosure_drawer_fan_is_back_to_on_line.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_drawer_fan_is_back_to_on_line.setStatus(
        ""
    )

enclosure_drawer_fan_is_back_to_on_line = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369228)
)
enclosure_drawer_fan_is_back_to_on_line.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_drawer_fan_is_back_to_on_line.setStatus(
        ""
    )

expansion_enclosure_drawer_fan_is_back_to_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369229)
)
expansion_enclosure_drawer_fan_is_back_to_present.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_drawer_fan_is_back_to_present.setStatus(
        ""
    )

enclosure_drawer_fan_is_back_to_present = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369230)
)
enclosure_drawer_fan_is_back_to_present.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_drawer_fan_is_back_to_present.setStatus(
        ""
    )

expansion_enclosure_drawer_fan_is_back_to_normal_RPM = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369231)
)
expansion_enclosure_drawer_fan_is_back_to_normal_RPM.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_drawer_fan_is_back_to_normal_RPM.setStatus(
        ""
    )

enclosure_drawer_fan_speed_is_back_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 369232)
)
enclosure_drawer_fan_speed_is_back_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_drawer_fan_speed_is_back_to_normal.setStatus(
        ""
    )

ups_connection_failure_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 402464)
)
ups_connection_failure_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ups_connection_failure_has_been_detected.setStatus(
        ""
    )

ups_AC_power_failure_was_detected_The_device_entered_safe_mode = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 402465)
)
ups_AC_power_failure_was_detected_The_device_entered_safe_mode.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ups_AC_power_failure_was_detected_The_device_entered_safe_mode.setStatus(
        ""
    )

ups_Low_Battery_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 402466)
)
ups_Low_Battery_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ups_Low_Battery_has_been_detected.setStatus(
        ""
    )

ups_Low_Battery_has_been_detected_Please_shut_down_immediately = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 402467)
)
ups_Low_Battery_has_been_detected_Please_shut_down_immediately.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ups_Low_Battery_has_been_detected_Please_shut_down_immediately.setStatus(
        ""
    )

ups_connection_has_been_restored = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 435212)
)
ups_connection_has_been_restored.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ups_connection_has_been_restored.setStatus(
        ""
    )

ups_AC_power_was_restored_The_device_has_exited_safe_mode = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 435213)
)
ups_AC_power_was_restored_The_device_has_exited_safe_mode.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ups_AC_power_was_restored_The_device_has_exited_safe_mode.setStatus(
        ""
    )

ups_Battery_Level_Restored_to_Safety = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 435214)
)
ups_Battery_Level_Restored_to_Safety.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ups_Battery_Level_Restored_to_Safety.setStatus(
        ""
    )

cpu_low_temperature_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467713)
)
cpu_low_temperature_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    cpu_low_temperature_detected.setStatus(
        ""
    )

cpu_high_temperature_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467714)
)
cpu_high_temperature_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    cpu_high_temperature_detected.setStatus(
        ""
    )

controller_ASIC_low_temperature_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467715)
)
controller_ASIC_low_temperature_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_ASIC_low_temperature_detected.setStatus(
        ""
    )

controller_ASIC_high_temperature_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467716)
)
controller_ASIC_high_temperature_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_ASIC_high_temperature_detected.setStatus(
        ""
    )

controller_drive_channel_IO_chip_low_temperature_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467717)
)
controller_drive_channel_IO_chip_low_temperature_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_drive_channel_IO_chip_low_temperature_detected.setStatus(
        ""
    )

controller_drive_channel_IO_chip_high_temperature_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467718)
)
controller_drive_channel_IO_chip_high_temperature_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_drive_channel_IO_chip_high_temperature_detected.setStatus(
        ""
    )

controller_host_IO_chip_low_temperature_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467719)
)
controller_host_IO_chip_low_temperature_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_host_IO_chip_low_temperature_detected.setStatus(
        ""
    )

controller_host_IO_chip_high_temperature_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467720)
)
controller_host_IO_chip_high_temperature_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_host_IO_chip_high_temperature_detected.setStatus(
        ""
    )

enclosure_backplane_temperature_sensor_detection_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467721)
)
enclosure_backplane_temperature_sensor_detection_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_backplane_temperature_sensor_detection_failed.setStatus(
        ""
    )

expansion_enclosure_backplane_low_temperature_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467734)
)
expansion_enclosure_backplane_low_temperature_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_backplane_low_temperature_has_been_detected.setStatus(
        ""
    )

expansion_enclosure_backplane_high_temperature_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467735)
)
expansion_enclosure_backplane_high_temperature_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_backplane_high_temperature_has_been_detected.setStatus(
        ""
    )

enclosure_backplane_high_temperature_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467737)
)
enclosure_backplane_high_temperature_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_backplane_high_temperature_has_been_detected.setStatus(
        ""
    )

the_temperature_sensor_of_expansion_enclosure_is_not_supported = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467738)
)
the_temperature_sensor_of_expansion_enclosure_is_not_supported.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_temperature_sensor_of_expansion_enclosure_is_not_supported.setStatus(
        ""
    )

the_temperature_sensor_of_expansion_enclosure_is_not_installed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467739)
)
the_temperature_sensor_of_expansion_enclosure_is_not_installed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_temperature_sensor_of_expansion_enclosure_is_not_installed.setStatus(
        ""
    )

unknown_status_of_the_temperature_sensor_of_expansion_enclosure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467740)
)
unknown_status_of_the_temperature_sensor_of_expansion_enclosure.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unknown_status_of_the_temperature_sensor_of_expansion_enclosure.setStatus(
        ""
    )

the_temperature_sensor_of_expansion_enclosure_is_not_available = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467741)
)
the_temperature_sensor_of_expansion_enclosure_is_not_available.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_temperature_sensor_of_expansion_enclosure_is_not_available.setStatus(
        ""
    )

expansion_enclosure_sensor_detected_low_temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467742)
)
expansion_enclosure_sensor_detected_low_temperature.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_sensor_detected_low_temperature.setStatus(
        ""
    )

expansion_enclosure_sensor_detected_high_temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467743)
)
expansion_enclosure_sensor_detected_high_temperature.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_sensor_detected_high_temperature.setStatus(
        ""
    )

cpu_low_temperature_has_been_detected_with_CPU_number = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467745)
)
cpu_low_temperature_has_been_detected_with_CPU_number.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    cpu_low_temperature_has_been_detected_with_CPU_number.setStatus(
        ""
    )

cpu_high_temperature_has_been_detected_with_CPU_number = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467746)
)
cpu_high_temperature_has_been_detected_with_CPU_number.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    cpu_high_temperature_has_been_detected_with_CPU_number.setStatus(
        ""
    )

controller_host_IO_chip_high_temperature_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467749)
)
controller_host_IO_chip_high_temperature_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_host_IO_chip_high_temperature_has_been_detected.setStatus(
        ""
    )

io_module_low_temperature_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467750)
)
io_module_low_temperature_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    io_module_low_temperature_has_been_detected.setStatus(
        ""
    )

io_module_high_temperature_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 467751)
)
io_module_high_temperature_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    io_module_high_temperature_has_been_detected.setStatus(
        ""
    )

cpu_temperature_back_to_normal_from_low_temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500481)
)
cpu_temperature_back_to_normal_from_low_temperature.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    cpu_temperature_back_to_normal_from_low_temperature.setStatus(
        ""
    )

cpu_temperature_back_to_normal_from_high_temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500482)
)
cpu_temperature_back_to_normal_from_high_temperature.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    cpu_temperature_back_to_normal_from_high_temperature.setStatus(
        ""
    )

enclosure_backplane_temperature_sensor_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500483)
)
enclosure_backplane_temperature_sensor_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_backplane_temperature_sensor_detected.setStatus(
        ""
    )

controller_ASIC_temperature_back_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500484)
)
controller_ASIC_temperature_back_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_ASIC_temperature_back_to_normal.setStatus(
        ""
    )

controller_drive_channel_IO_chip_temperature_back_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500486)
)
controller_drive_channel_IO_chip_temperature_back_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_drive_channel_IO_chip_temperature_back_to_normal.setStatus(
        ""
    )

controller_host_board_IO_chip_temperature_back_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500488)
)
controller_host_board_IO_chip_temperature_back_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_host_board_IO_chip_temperature_back_to_normal.setStatus(
        ""
    )

expansion_enclosure_backplane_temperature_is_back_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500490)
)
expansion_enclosure_backplane_temperature_is_back_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_backplane_temperature_is_back_to_normal.setStatus(
        ""
    )

enclosure_backplane_temperature_is_back_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500491)
)
enclosure_backplane_temperature_is_back_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_backplane_temperature_is_back_to_normal.setStatus(
        ""
    )

expansion_enclosure_backplane_temperature_is_back_normal_state = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500494)
)
expansion_enclosure_backplane_temperature_is_back_normal_state.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_backplane_temperature_is_back_normal_state.setStatus(
        ""
    )

enclosure_backplane_temperature_is_back_to_normal_state = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500495)
)
enclosure_backplane_temperature_is_back_to_normal_state.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_backplane_temperature_is_back_to_normal_state.setStatus(
        ""
    )

expansion_enclosure_backplane_temperature_back_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500496)
)
expansion_enclosure_backplane_temperature_back_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_enclosure_backplane_temperature_back_to_normal.setStatus(
        ""
    )

enclosure_backplane_temperature_back_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500497)
)
enclosure_backplane_temperature_back_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_backplane_temperature_back_to_normal.setStatus(
        ""
    )

controller_host_board_IO_chip_temperature_is_back_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500499)
)
controller_host_board_IO_chip_temperature_is_back_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    controller_host_board_IO_chip_temperature_is_back_to_normal.setStatus(
        ""
    )

io_module_temperature_is_back_to_normal_from_low_temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500500)
)
io_module_temperature_is_back_to_normal_from_low_temperature.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    io_module_temperature_is_back_to_normal_from_low_temperature.setStatus(
        ""
    )

io_module_temperature_is_back_to_normal_from_high_temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500501)
)
io_module_temperature_is_back_to_normal_from_high_temperature.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    io_module_temperature_is_back_to_normal_from_high_temperature.setStatus(
        ""
    )

cpu_temperature_is_back_to_normal_from_low_temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500513)
)
cpu_temperature_is_back_to_normal_from_low_temperature.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    cpu_temperature_is_back_to_normal_from_low_temperature.setStatus(
        ""
    )

cpu_temperature_is_back_to_normal_from_high_temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 500514)
)
cpu_temperature_is_back_to_normal_from_high_temperature.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    cpu_temperature_is_back_to_normal_from_high_temperature.setStatus(
        ""
    )

unexpected_select_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 524545)
)
unexpected_select_timeout.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unexpected_select_timeout.setStatus(
        ""
    )

unexpected_select_timeout_detected_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 524609)
)
unexpected_select_timeout_detected_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unexpected_select_timeout_detected_on_expansion_drive.setStatus(
        ""
    )

unexpected_select_timeout_detected_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 524673)
)
unexpected_select_timeout_detected_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unexpected_select_timeout_detected_on_enclosure_drive.setStatus(
        ""
    )

gross_phase_or_signal_error_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 524802)
)
gross_phase_or_signal_error_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    gross_phase_or_signal_error_detected.setStatus(
        ""
    )

gross_phase_or_signal_error_detected_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 524866)
)
gross_phase_or_signal_error_detected_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    gross_phase_or_signal_error_detected_on_expansion_drive.setStatus(
        ""
    )

gross_phase_or_signal_error_detected_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 524930)
)
gross_phase_or_signal_error_detected_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    gross_phase_or_signal_error_detected_on_enclosure_drive.setStatus(
        ""
    )

drive_IO_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 525569)
)
drive_IO_timeout.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_IO_timeout.setStatus(
        ""
    )

drive_IO_timeout_detected_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 525633)
)
drive_IO_timeout_detected_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_IO_timeout_detected_on_expansion_drive.setStatus(
        ""
    )

drive_IO_timeout_detected_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 525697)
)
drive_IO_timeout_detected_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_IO_timeout_detected_on_enclosure_drive.setStatus(
        ""
    )

scsi_parity_or_CRC_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 525825)
)
scsi_parity_or_CRC_error.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    scsi_parity_or_CRC_error.setStatus(
        ""
    )

scsi_parity_or_CRC_error_detected_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 525889)
)
scsi_parity_or_CRC_error_detected_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    scsi_parity_or_CRC_error_detected_on_expansion_drive.setStatus(
        ""
    )

scsi_parity_or_CRC_error_detected_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 525953)
)
scsi_parity_or_CRC_error_detected_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    scsi_parity_or_CRC_error_detected_on_enclosure_drive.setStatus(
        ""
    )

data_overrun_or_underrun = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526081)
)
data_overrun_or_underrun.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    data_overrun_or_underrun.setStatus(
        ""
    )

media_scan_for_disk_drive_stopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526088)
)
media_scan_for_disk_drive_stopped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_disk_drive_stopped.setStatus(
        ""
    )

media_scan_for_disk_drvie_scan_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526097)
)
media_scan_for_disk_drvie_scan_aborted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_disk_drvie_scan_aborted.setStatus(
        ""
    )

data_overrun_or_underrun_detected_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526145)
)
data_overrun_or_underrun_detected_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    data_overrun_or_underrun_detected_on_expansion_drive.setStatus(
        ""
    )

media_scan_for_disk_drive_in_expansion_stopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526152)
)
media_scan_for_disk_drive_in_expansion_stopped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_disk_drive_in_expansion_stopped.setStatus(
        ""
    )

media_scan_for_disk_drvie_in_expansion_scan_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526161)
)
media_scan_for_disk_drvie_in_expansion_scan_aborted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_disk_drvie_in_expansion_scan_aborted.setStatus(
        ""
    )

data_overrun_or_underrun_detected_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526209)
)
data_overrun_or_underrun_detected_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    data_overrun_or_underrun_detected_on_enclosure_drive.setStatus(
        ""
    )

media_scan_for_disk_drive_in_enclosure_stopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526216)
)
media_scan_for_disk_drive_in_enclosure_stopped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_disk_drive_in_enclosure_stopped.setStatus(
        ""
    )

media_scan_for_disk_drvie_in_enclosure_scan_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526225)
)
media_scan_for_disk_drvie_in_enclosure_scan_aborted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_disk_drvie_in_enclosure_scan_aborted.setStatus(
        ""
    )

invalid_status_or_sense_data_received = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526337)
)
invalid_status_or_sense_data_received.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    invalid_status_or_sense_data_received.setStatus(
        ""
    )

invalid_status_or_sense_data_received_with_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526338)
)
invalid_status_or_sense_data_received_with_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    invalid_status_or_sense_data_received_with_info.setStatus(
        ""
    )

invalid_status_or_sense_data_received_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526401)
)
invalid_status_or_sense_data_received_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    invalid_status_or_sense_data_received_on_expansion_drive.setStatus(
        ""
    )

invalid_status_or_sense_data_received_w_info_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526402)
)
invalid_status_or_sense_data_received_w_info_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    invalid_status_or_sense_data_received_w_info_on_expansion_drive.setStatus(
        ""
    )

invalid_status_or_sense_data_received_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526465)
)
invalid_status_or_sense_data_received_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    invalid_status_or_sense_data_received_on_enclosure_drive.setStatus(
        ""
    )

invalid_status_or_sense_data_received_w_info_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 526466)
)
invalid_status_or_sense_data_received_w_info_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    invalid_status_or_sense_data_received_w_info_on_enclosure_drive.setStatus(
        ""
    )

drive_not_ready_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 528641)
)
drive_not_ready_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_not_ready_detected.setStatus(
        ""
    )

drive_not_ready_detected_with_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 528642)
)
drive_not_ready_detected_with_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_not_ready_detected_with_info.setStatus(
        ""
    )

drive_not_ready_detected_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 528705)
)
drive_not_ready_detected_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_not_ready_detected_on_expansion_drive.setStatus(
        ""
    )

drive_not_ready_detected_with_info_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 528706)
)
drive_not_ready_detected_with_info_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_not_ready_detected_with_info_on_expansion_drive.setStatus(
        ""
    )

drive_not_ready_detected_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 528769)
)
drive_not_ready_detected_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_not_ready_detected_on_enclosure_drive.setStatus(
        ""
    )

drive_not_ready_detected_with_info_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 528770)
)
drive_not_ready_detected_with_info_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_not_ready_detected_with_info_on_enclosure_drive.setStatus(
        ""
    )

drive_hardware_error_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 528897)
)
drive_hardware_error_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_hardware_error_detected.setStatus(
        ""
    )

drive_hardware_error_detected_with_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 528898)
)
drive_hardware_error_detected_with_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_hardware_error_detected_with_info.setStatus(
        ""
    )

drive_hardware_error_detected_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 528961)
)
drive_hardware_error_detected_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_hardware_error_detected_on_expansion_drive.setStatus(
        ""
    )

drive_hardware_error_detected_with_info_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 528962)
)
drive_hardware_error_detected_with_info_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_hardware_error_detected_with_info_on_expansion_drive.setStatus(
        ""
    )

drive_hardware_error_detected_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529025)
)
drive_hardware_error_detected_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_hardware_error_detected_on_enclosure_drive.setStatus(
        ""
    )

drive_hardware_error_detected_with_info_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529026)
)
drive_hardware_error_detected_with_info_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_hardware_error_detected_with_info_on_enclosure_drive.setStatus(
        ""
    )

drive_media_error_has_been_detected_with_LBA = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529153)
)
drive_media_error_has_been_detected_with_LBA.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_media_error_has_been_detected_with_LBA.setStatus(
        ""
    )

drive_media_error_has_been_detected_with_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529154)
)
drive_media_error_has_been_detected_with_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_media_error_has_been_detected_with_info.setStatus(
        ""
    )

drive_media_error_has_been_detected_with_LBA_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529217)
)
drive_media_error_has_been_detected_with_LBA_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_media_error_has_been_detected_with_LBA_on_expansion_drive.setStatus(
        ""
    )

drive_media_error_detected_with_info_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529218)
)
drive_media_error_detected_with_info_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_media_error_detected_with_info_on_expansion_drive.setStatus(
        ""
    )

drive_media_error_has_been_detected_with_LBA_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529281)
)
drive_media_error_has_been_detected_with_LBA_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_media_error_has_been_detected_with_LBA_on_enclosure_drive.setStatus(
        ""
    )

drive_media_error_detected_with_info_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529282)
)
drive_media_error_detected_with_info_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_media_error_detected_with_info_on_enclosure_drive.setStatus(
        ""
    )

unit_attention_received = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529409)
)
unit_attention_received.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unit_attention_received.setStatus(
        ""
    )

unit_attention_received_with_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529410)
)
unit_attention_received_with_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unit_attention_received_with_info.setStatus(
        ""
    )

unit_attention_received_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529473)
)
unit_attention_received_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unit_attention_received_on_expansion_drive.setStatus(
        ""
    )

unit_attention_received_with_info_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529474)
)
unit_attention_received_with_info_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unit_attention_received_with_info_on_expansion_drive.setStatus(
        ""
    )

unit_attention_received_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529537)
)
unit_attention_received_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unit_attention_received_on_enclosure_drive.setStatus(
        ""
    )

unit_attention_received_with_info_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529538)
)
unit_attention_received_with_info_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unit_attention_received_with_info_on_enclosure_drive.setStatus(
        ""
    )

unexpected_sense_data_received = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529665)
)
unexpected_sense_data_received.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unexpected_sense_data_received.setStatus(
        ""
    )

unexpected_sense_data_received_with_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529666)
)
unexpected_sense_data_received_with_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unexpected_sense_data_received_with_info.setStatus(
        ""
    )

unexpected_sense_data_received_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529729)
)
unexpected_sense_data_received_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unexpected_sense_data_received_on_expansion_drive.setStatus(
        ""
    )

unexpected_sense_data_received_with_info_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529730)
)
unexpected_sense_data_received_with_info_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unexpected_sense_data_received_with_info_on_expansion_drive.setStatus(
        ""
    )

unexpected_sense_data_received_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529793)
)
unexpected_sense_data_received_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unexpected_sense_data_received_on_enclosure_drive.setStatus(
        ""
    )

unexpected_sense_data_received_with_info_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529794)
)
unexpected_sense_data_received_with_info_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unexpected_sense_data_received_with_info_on_enclosure_drive.setStatus(
        ""
    )

failed_to_reassign_the_bad_block = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529921)
)
failed_to_reassign_the_bad_block.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_reassign_the_bad_block.setStatus(
        ""
    )

failed_to_reassign_the_bad_block_with_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529922)
)
failed_to_reassign_the_bad_block_with_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_reassign_the_bad_block_with_info.setStatus(
        ""
    )

failed_to_reassign_the_bad_block_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529985)
)
failed_to_reassign_the_bad_block_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_reassign_the_bad_block_on_expansion_drive.setStatus(
        ""
    )

failed_to_reassign_the_bad_block_with_info_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 529986)
)
failed_to_reassign_the_bad_block_with_info_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_reassign_the_bad_block_with_info_on_expansion_drive.setStatus(
        ""
    )

failed_to_reassign_the_bad_block_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530049)
)
failed_to_reassign_the_bad_block_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_reassign_the_bad_block_on_enclosure_drive.setStatus(
        ""
    )

failed_to_reassign_the_bad_block_with_info_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530050)
)
failed_to_reassign_the_bad_block_with_info_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_reassign_the_bad_block_with_info_on_enclosure_drive.setStatus(
        ""
    )

bad_block_reassigned_with_LBA = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530177)
)
bad_block_reassigned_with_LBA.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    bad_block_reassigned_with_LBA.setStatus(
        ""
    )

bad_block_reassigned_with_LBA_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530241)
)
bad_block_reassigned_with_LBA_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    bad_block_reassigned_with_LBA_on_expansion_drive.setStatus(
        ""
    )

bad_block_reassigned_with_LBA_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530305)
)
bad_block_reassigned_with_LBA_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    bad_block_reassigned_with_LBA_on_enclosure_drive.setStatus(
        ""
    )

drive_command_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530433)
)
drive_command_aborted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_command_aborted.setStatus(
        ""
    )

drive_command_aborted_with_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530434)
)
drive_command_aborted_with_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_command_aborted_with_info.setStatus(
        ""
    )

drive_command_aborted_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530497)
)
drive_command_aborted_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_command_aborted_on_expansion_drive.setStatus(
        ""
    )

drive_command_aborted_with_info_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530498)
)
drive_command_aborted_with_info_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_command_aborted_with_info_on_expansion_drive.setStatus(
        ""
    )

drive_command_aborted_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530561)
)
drive_command_aborted_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_command_aborted_on_enclosure_drive.setStatus(
        ""
    )

drive_command_aborted_with_info_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530562)
)
drive_command_aborted_with_info_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_command_aborted_with_info_on_enclosure_drive.setStatus(
        ""
    )

drive_error_has_been_recovered_with_LBA = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530689)
)
drive_error_has_been_recovered_with_LBA.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_error_has_been_recovered_with_LBA.setStatus(
        ""
    )

drive_error_has_been_recovered_with_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530690)
)
drive_error_has_been_recovered_with_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_error_has_been_recovered_with_info.setStatus(
        ""
    )

drive_error_has_been_recovered_with_LBA_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530753)
)
drive_error_has_been_recovered_with_LBA_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_error_has_been_recovered_with_LBA_on_expansion_drive.setStatus(
        ""
    )

drive_error_has_been_recovered_with_info_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530754)
)
drive_error_has_been_recovered_with_info_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_error_has_been_recovered_with_info_on_expansion_drive.setStatus(
        ""
    )

drive_error_has_been_recovered_with_LBA_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530817)
)
drive_error_has_been_recovered_with_LBA_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_error_has_been_recovered_with_LBA_on_enclosure_drive.setStatus(
        ""
    )

drive_error_has_been_recovered_with_info_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 530818)
)
drive_error_has_been_recovered_with_info_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_error_has_been_recovered_with_info_on_enclosure_drive.setStatus(
        ""
    )

unable_to_start_drive_error_recovery_procedure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541186)
)
unable_to_start_drive_error_recovery_procedure.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unable_to_start_drive_error_recovery_procedure.setStatus(
        ""
    )

drive_SMART_error_state_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541187)
)
drive_SMART_error_state_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_SMART_error_state_has_been_detected.setStatus(
        ""
    )

drive_error_recovery_procedure_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541188)
)
drive_error_recovery_procedure_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_error_recovery_procedure_started.setStatus(
        ""
    )

drive_error_recovery_procedure_stopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541189)
)
drive_error_recovery_procedure_stopped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_error_recovery_procedure_stopped.setStatus(
        ""
    )

drive_SMART_error_state_has_been_detected_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541251)
)
drive_SMART_error_state_has_been_detected_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_SMART_error_state_has_been_detected_on_expansion_drive.setStatus(
        ""
    )

drive_error_recovery_procedure_started_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541252)
)
drive_error_recovery_procedure_started_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_error_recovery_procedure_started_on_expansion_drive.setStatus(
        ""
    )

drive_error_recovery_procedure_stopped_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541253)
)
drive_error_recovery_procedure_stopped_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_error_recovery_procedure_stopped_on_expansion_drive.setStatus(
        ""
    )

drive_SMART_error_state_has_been_detected_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541315)
)
drive_SMART_error_state_has_been_detected_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_SMART_error_state_has_been_detected_on_enclosure_drive.setStatus(
        ""
    )

drive_error_recovery_procedure_started_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541316)
)
drive_error_recovery_procedure_started_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_error_recovery_procedure_started_on_enclosure_drive.setStatus(
        ""
    )

drive_error_recovery_procedure_stopped_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541317)
)
drive_error_recovery_procedure_stopped_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_error_recovery_procedure_stopped_on_enclosure_drive.setStatus(
        ""
    )

drive_media_error_has_been_recovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541441)
)
drive_media_error_has_been_recovered.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_media_error_has_been_recovered.setStatus(
        ""
    )

unrecovered_drive_media_error_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541442)
)
unrecovered_drive_media_error_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unrecovered_drive_media_error_detected.setStatus(
        ""
    )

drive_lifetime_estimate_warning_threshold_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541457)
)
drive_lifetime_estimate_warning_threshold_exceeded.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_lifetime_estimate_warning_threshold_exceeded.setStatus(
        ""
    )

the_SSDs_remaining_life_less_than_threshold_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541458)
)
the_SSDs_remaining_life_less_than_threshold_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_SSDs_remaining_life_less_than_threshold_detected.setStatus(
        ""
    )

drive_media_error_has_been_recovered_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541505)
)
drive_media_error_has_been_recovered_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_media_error_has_been_recovered_on_expansion_drive.setStatus(
        ""
    )

unrecovered_drive_media_error_detected_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541506)
)
unrecovered_drive_media_error_detected_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unrecovered_drive_media_error_detected_on_expansion_drive.setStatus(
        ""
    )

drive_media_error_has_been_recovered_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541569)
)
drive_media_error_has_been_recovered_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_media_error_has_been_recovered_on_enclosure_drive.setStatus(
        ""
    )

unrecovered_drive_media_error_detected_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 541570)
)
unrecovered_drive_media_error_detected_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unrecovered_drive_media_error_detected_on_enclosure_drive.setStatus(
        ""
    )

media_scan_for_disk_drive_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 560129)
)
media_scan_for_disk_drive_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_disk_drive_completed.setStatus(
        ""
    )

media_scan_for_disk_drive_in_expansion_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 560193)
)
media_scan_for_disk_drive_in_expansion_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_disk_drive_in_expansion_completed.setStatus(
        ""
    )

media_scan_for_disk_drive_enclosure_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 560257)
)
media_scan_for_disk_drive_enclosure_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_disk_drive_enclosure_completed.setStatus(
        ""
    )

drive_scanned = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573697)
)
drive_scanned.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_scanned.setStatus(
        ""
    )

exiled_drive_detected_with_ch_ID = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573698)
)
exiled_drive_detected_with_ch_ID.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    exiled_drive_detected_with_ch_ID.setStatus(
        ""
    )

unsupported_drive_detected_drive_type_or_license_is_invalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573699)
)
unsupported_drive_detected_drive_type_or_license_is_invalid.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unsupported_drive_detected_drive_type_or_license_is_invalid.setStatus(
        ""
    )

unsupported_drive_detected_incorrect_bundle_ID = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573700)
)
unsupported_drive_detected_incorrect_bundle_ID.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unsupported_drive_detected_incorrect_bundle_ID.setStatus(
        ""
    )

unsupported_drive_detected_unsupported_bundle_code = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573701)
)
unsupported_drive_detected_unsupported_bundle_code.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unsupported_drive_detected_unsupported_bundle_code.setStatus(
        ""
    )

drive_detection_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573703)
)
drive_detection_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_detection_failed.setStatus(
        ""
    )

drive_scanned_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573761)
)
drive_scanned_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_scanned_on_expansion_drive.setStatus(
        ""
    )

exiled_drive_detected_with_ch_ID_in_expansion = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573762)
)
exiled_drive_detected_with_ch_ID_in_expansion.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    exiled_drive_detected_with_ch_ID_in_expansion.setStatus(
        ""
    )

unsupported_drive_detected_in_expansion = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573763)
)
unsupported_drive_detected_in_expansion.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unsupported_drive_detected_in_expansion.setStatus(
        ""
    )

incorrect_bundle_ID_detected_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573764)
)
incorrect_bundle_ID_detected_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    incorrect_bundle_ID_detected_on_expansion_drive.setStatus(
        ""
    )

unsupported_bundle_code_detected_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573765)
)
unsupported_bundle_code_detected_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unsupported_bundle_code_detected_on_expansion_drive.setStatus(
        ""
    )

drive_detection_failed_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573767)
)
drive_detection_failed_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_detection_failed_on_expansion_drive.setStatus(
        ""
    )

drive_scanned_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573825)
)
drive_scanned_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_scanned_on_enclosure_drive.setStatus(
        ""
    )

exiled_drive_detected_with_ch_ID_in_enclosure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573826)
)
exiled_drive_detected_with_ch_ID_in_enclosure.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    exiled_drive_detected_with_ch_ID_in_enclosure.setStatus(
        ""
    )

unsupported_drive_detected_in_enclosure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573827)
)
unsupported_drive_detected_in_enclosure.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unsupported_drive_detected_in_enclosure.setStatus(
        ""
    )

incorrect_bundle_ID_detected_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573828)
)
incorrect_bundle_ID_detected_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    incorrect_bundle_ID_detected_on_enclosure_drive.setStatus(
        ""
    )

unsupported_bundle_code_detected_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573829)
)
unsupported_bundle_code_detected_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unsupported_bundle_code_detected_on_enclosure_drive.setStatus(
        ""
    )

drive_detection_failed_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 573831)
)
drive_detection_failed_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_detection_failed_on_enclosure_drive.setStatus(
        ""
    )

trunking_configuration_error_detected_in_Slot_B = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 595201)
)
trunking_configuration_error_detected_in_Slot_B.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    trunking_configuration_error_detected_in_Slot_B.setStatus(
        ""
    )

trunking_configuration_error_detected_in_Slot_A = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 595202)
)
trunking_configuration_error_detected_in_Slot_A.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    trunking_configuration_error_detected_in_Slot_A.setStatus(
        ""
    )

ipv4_address_conflict_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 595457)
)
ipv4_address_conflict_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ipv4_address_conflict_has_been_detected.setStatus(
        ""
    )

ipv6_address_conflict_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 595458)
)
ipv6_address_conflict_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ipv6_address_conflict_has_been_detected.setStatus(
        ""
    )

mismatched_SFP_installation_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 597505)
)
mismatched_SFP_installation_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    mismatched_SFP_installation_has_been_detected.setStatus(
        ""
    )

scsi_channel_failed_detected_with_channel_ID = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 605954)
)
scsi_channel_failed_detected_with_channel_ID.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    scsi_channel_failed_detected_with_channel_ID.setStatus(
        ""
    )

host_channel_failed_with_ID = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 605955)
)
host_channel_failed_with_ID.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    host_channel_failed_with_ID.setStatus(
        ""
    )

scsi_channel_failed_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 605956)
)
scsi_channel_failed_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    scsi_channel_failed_detected.setStatus(
        ""
    )

host_channel_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 605957)
)
host_channel_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    host_channel_failed.setStatus(
        ""
    )

redundant_path_error_detected_with_channel_ID = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 605959)
)
redundant_path_error_detected_with_channel_ID.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    redundant_path_error_detected_with_channel_ID.setStatus(
        ""
    )

redundant_path_error_detected_with_channel_and_target_ID = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 605961)
)
redundant_path_error_detected_with_channel_and_target_ID.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    redundant_path_error_detected_with_channel_and_target_ID.setStatus(
        ""
    )

fibre_Channel_loop_connection_restored = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 605962)
)
fibre_Channel_loop_connection_restored.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    fibre_Channel_loop_connection_restored.setStatus(
        ""
    )

ch_redundant_path_error_recovered_with_ch = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 605963)
)
ch_redundant_path_error_recovered_with_ch.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ch_redundant_path_error_recovered_with_ch.setStatus(
        ""
    )

ch_redundant_path_error_recovered_with_ch_ID = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 605964)
)
ch_redundant_path_error_recovered_with_ch_ID.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ch_redundant_path_error_recovered_with_ch_ID.setStatus(
        ""
    )

ch_iD_redundant_path_error_recovered_with_ch_ID = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 605965)
)
ch_iD_redundant_path_error_recovered_with_ch_ID.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ch_iD_redundant_path_error_recovered_with_ch_ID.setStatus(
        ""
    )

host_channel_disconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 622849)
)
host_channel_disconnected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    host_channel_disconnected.setStatus(
        ""
    )

host_channel_connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 622850)
)
host_channel_connected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    host_channel_connected.setStatus(
        ""
    )

host_channel_speed_has_backed_to_speed_in_Gb_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 622851)
)
host_channel_speed_has_backed_to_speed_in_Gb_warning.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    host_channel_speed_has_backed_to_speed_in_Gb_warning.setStatus(
        ""
    )

host_channel_speed_backed_to_speed_in_Gb_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 622851)
)
host_channel_speed_backed_to_speed_in_Gb_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    host_channel_speed_backed_to_speed_in_Gb_info.setStatus(
        ""
    )

host_channel_speed_has_backed_to_speed_in_Mb_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 622852)
)
host_channel_speed_has_backed_to_speed_in_Mb_warning.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    host_channel_speed_has_backed_to_speed_in_Mb_warning.setStatus(
        ""
    )

host_channel_speed_backed_to_speed_in_Mb_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 622852)
)
host_channel_speed_backed_to_speed_in_Mb_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    host_channel_speed_backed_to_speed_in_Mb_info.setStatus(
        ""
    )

host_channel_speed_has_changed_to_speed_in_Gb = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 622853)
)
host_channel_speed_has_changed_to_speed_in_Gb.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    host_channel_speed_has_changed_to_speed_in_Gb.setStatus(
        ""
    )

host_channel_speed_has_changed_to_speed_in_Mb = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 622854)
)
host_channel_speed_has_changed_to_speed_in_Mb.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    host_channel_speed_has_changed_to_speed_in_Mb.setStatus(
        ""
    )

drive_missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655617)
)
drive_missing.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_missing.setStatus(
        ""
    )

drive_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655618)
)
drive_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_failed.setStatus(
        ""
    )

drive_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655619)
)
drive_removed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_removed.setStatus(
        ""
    )

a_second_or_third_LD_member_drive_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655620)
)
a_second_or_third_LD_member_drive_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_second_or_third_LD_member_drive_failed.setStatus(
        ""
    )

the_first_LD_member_drive_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655621)
)
the_first_LD_member_drive_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_first_LD_member_drive_failed.setStatus(
        ""
    )

logical_drive_member_drive_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655622)
)
logical_drive_member_drive_removed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_member_drive_removed.setStatus(
        ""
    )

expansion_drive_missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655681)
)
expansion_drive_missing.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_drive_missing.setStatus(
        ""
    )

expansion_drive_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655682)
)
expansion_drive_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_drive_failed.setStatus(
        ""
    )

expansion_drive_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655683)
)
expansion_drive_removed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    expansion_drive_removed.setStatus(
        ""
    )

a_second_or_third_LD_member_drive_in_expansion_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655684)
)
a_second_or_third_LD_member_drive_in_expansion_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_second_or_third_LD_member_drive_in_expansion_failed.setStatus(
        ""
    )

the_first_LD_member_drive_in_expansion_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655685)
)
the_first_LD_member_drive_in_expansion_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_first_LD_member_drive_in_expansion_failed.setStatus(
        ""
    )

logical_drive_member_drive_in_expansion_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655686)
)
logical_drive_member_drive_in_expansion_removed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_member_drive_in_expansion_removed.setStatus(
        ""
    )

enclosure_drive_missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655745)
)
enclosure_drive_missing.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_drive_missing.setStatus(
        ""
    )

enclosure_drive_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655746)
)
enclosure_drive_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_drive_failed.setStatus(
        ""
    )

enclosure_drive_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655747)
)
enclosure_drive_removed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    enclosure_drive_removed.setStatus(
        ""
    )

a_second_or_third_LD_member_drive_in_enclosure_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655748)
)
a_second_or_third_LD_member_drive_in_enclosure_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_second_or_third_LD_member_drive_in_enclosure_failed.setStatus(
        ""
    )

the_first_LD_member_drive_in_enclosure_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655749)
)
the_first_LD_member_drive_in_enclosure_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_first_LD_member_drive_in_enclosure_failed.setStatus(
        ""
    )

logical_drive_member_drive_in_enclosure_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655750)
)
logical_drive_member_drive_in_enclosure_removed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_member_drive_in_enclosure_removed.setStatus(
        ""
    )

logical_drive_initialization_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655873)
)
logical_drive_initialization_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_initialization_failed.setStatus(
        ""
    )

logical_drive_creation_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655874)
)
logical_drive_creation_aborted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_creation_aborted.setStatus(
        ""
    )

logical_drive_creation_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 655875)
)
logical_drive_creation_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_creation_failed.setStatus(
        ""
    )

logical_drive_rebuild_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 656129)
)
logical_drive_rebuild_aborted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_rebuild_aborted.setStatus(
        ""
    )

logical_drive_rebuild_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 656130)
)
logical_drive_rebuild_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_rebuild_failed.setStatus(
        ""
    )

logical_drive_parity_regeneration_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 656385)
)
logical_drive_parity_regeneration_aborted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_parity_regeneration_aborted.setStatus(
        ""
    )

logical_drive_parity_regeneration_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 656386)
)
logical_drive_parity_regeneration_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_parity_regeneration_failed.setStatus(
        ""
    )

logical_drive_expansion_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 656641)
)
logical_drive_expansion_aborted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_expansion_aborted.setStatus(
        ""
    )

logical_drive_expansion_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 656642)
)
logical_drive_expansion_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_expansion_failed.setStatus(
        ""
    )

media_scan_for_logical_drive_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 657154)
)
media_scan_for_logical_drive_aborted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_logical_drive_aborted.setStatus(
        ""
    )

unable_to_start_media_scan_Status_is_invalid_for_media_scan = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 657156)
)
unable_to_start_media_scan_Status_is_invalid_for_media_scan.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unable_to_start_media_scan_Status_is_invalid_for_media_scan.setStatus(
        ""
    )

media_scan_for_logical_drive_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 657157)
)
media_scan_for_logical_drive_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_logical_drive_failed.setStatus(
        ""
    )

no_spare_drive_for_recovering_the_detected_unrecoverable_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 657158)
)
no_spare_drive_for_recovering_the_detected_unrecoverable_error.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    no_spare_drive_for_recovering_the_detected_unrecoverable_error.setStatus(
        ""
    )

unrecovered_media_error_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 657159)
)
unrecovered_media_error_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unrecovered_media_error_detected.setStatus(
        ""
    )

media_scan_for_logical_drive_member_drive_stopped_Scan_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 657161)
)
media_scan_for_logical_drive_member_drive_stopped_Scan_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_logical_drive_member_drive_stopped_Scan_failed.setStatus(
        ""
    )

unrecovered_media_error_detected_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 657223)
)
unrecovered_media_error_detected_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unrecovered_media_error_detected_on_expansion_drive.setStatus(
        ""
    )

media_scan_for_logical_drive_member_drive_in_expansion_stopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 657225)
)
media_scan_for_logical_drive_member_drive_in_expansion_stopped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_logical_drive_member_drive_in_expansion_stopped.setStatus(
        ""
    )

unrecovered_media_error_detected_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 657287)
)
unrecovered_media_error_detected_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unrecovered_media_error_detected_on_enclosure_drive.setStatus(
        ""
    )

media_scan_for_logical_drive_member_drive_in_enclosure_stopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 657289)
)
media_scan_for_logical_drive_member_drive_in_enclosure_stopped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_logical_drive_member_drive_in_enclosure_stopped.setStatus(
        ""
    )

logical_drive_cache_data_purged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 657410)
)
logical_drive_cache_data_purged.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_cache_data_purged.setStatus(
        ""
    )

drive_clone_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 659713)
)
drive_clone_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_failed.setStatus(
        ""
    )

drive_clone_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 659714)
)
drive_clone_aborted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_aborted.setStatus(
        ""
    )

drive_clone_failed_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 659777)
)
drive_clone_failed_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_failed_on_expansion_drive.setStatus(
        ""
    )

drive_clone_aborted_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 659778)
)
drive_clone_aborted_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_aborted_on_expansion_drive.setStatus(
        ""
    )

drive_clone_failed_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 659841)
)
drive_clone_failed_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_failed_on_enclosure_drive.setStatus(
        ""
    )

drive_clone_aborted_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 659842)
)
drive_clone_aborted_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_aborted_on_enclosure_drive.setStatus(
        ""
    )

logical_drive_error_detected_Bad_block_count_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 672001)
)
logical_drive_error_detected_Bad_block_count_exceeded.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_error_detected_Bad_block_count_exceeded.setStatus(
        ""
    )

logical_drive_error_detected_Bad_block_table_corrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 672002)
)
logical_drive_error_detected_Bad_block_table_corrupted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_error_detected_Bad_block_table_corrupted.setStatus(
        ""
    )

logical_drive_error_detected_Online_init_table_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 672003)
)
logical_drive_error_detected_Online_init_table_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_error_detected_Online_init_table_failed.setStatus(
        ""
    )

logical_drive_bad_data_block_detected_and_marked = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 672257)
)
logical_drive_bad_data_block_detected_and_marked.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_bad_data_block_detected_and_marked.setStatus(
        ""
    )

unprotected_block_on_the_logical_drive_detected_and_marked = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 672258)
)
unprotected_block_on_the_logical_drive_detected_and_marked.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unprotected_block_on_the_logical_drive_detected_and_marked.setStatus(
        ""
    )

logical_drive_bad_data_block_recovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 672259)
)
logical_drive_bad_data_block_recovered.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_bad_data_block_recovered.setStatus(
        ""
    )

logical_drive_bad_data_block_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 672260)
)
logical_drive_bad_data_block_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_bad_data_block_detected.setStatus(
        ""
    )

logical_drive_inconsistent_parity_block_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 672769)
)
logical_drive_inconsistent_parity_block_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_inconsistent_parity_block_detected.setStatus(
        ""
    )

logical_drive_inconsistent_parity_block_recovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 672770)
)
logical_drive_inconsistent_parity_block_recovered.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_inconsistent_parity_block_recovered.setStatus(
        ""
    )

logical_drive_media_error_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 672771)
)
logical_drive_media_error_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_media_error_detected.setStatus(
        ""
    )

logical_drive_media_error_recovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 672772)
)
logical_drive_media_error_recovered.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_media_error_recovered.setStatus(
        ""
    )

logical_drive_status_back_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 673031)
)
logical_drive_status_back_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_status_back_to_normal.setStatus(
        ""
    )

logical_drive_degraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 673032)
)
logical_drive_degraded.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_degraded.setStatus(
        ""
    )

logical_drive_had_fatal_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 673033)
)
logical_drive_had_fatal_failure.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_had_fatal_failure.setStatus(
        ""
    )

logical_drive_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 673034)
)
logical_drive_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_failed.setStatus(
        ""
    )

logical_drive_member_drive_missing_has_been_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 673035)
)
logical_drive_member_drive_missing_has_been_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_member_drive_missing_has_been_detected.setStatus(
        ""
    )

logical_drive_member_drive_missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 673036)
)
logical_drive_member_drive_missing.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_member_drive_missing.setStatus(
        ""
    )

logical_drive_status_changed_from_online_to_offline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 673286)
)
logical_drive_status_changed_from_online_to_offline.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_status_changed_from_online_to_offline.setStatus(
        ""
    )

logical_drive_status_changed_from_offline_to_online = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 673287)
)
logical_drive_status_changed_from_offline_to_online.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_status_changed_from_offline_to_online.setStatus(
        ""
    )

all_member_drives_of_logical_drive_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 673288)
)
all_member_drives_of_logical_drive_removed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    all_member_drives_of_logical_drive_removed.setStatus(
        ""
    )

all_member_drives_of_logical_drive_restored = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 673289)
)
all_member_drives_of_logical_drive_restored.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    all_member_drives_of_logical_drive_restored.setStatus(
        ""
    )

logical_drive_undeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 673290)
)
logical_drive_undeleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_undeleted.setStatus(
        ""
    )

logical_drive_online_initialization_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 688386)
)
logical_drive_online_initialization_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_online_initialization_started.setStatus(
        ""
    )

logical_drive_offline_initialization_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 688388)
)
logical_drive_offline_initialization_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_offline_initialization_started.setStatus(
        ""
    )

logical_drive_creation_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 688390)
)
logical_drive_creation_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_creation_started.setStatus(
        ""
    )

logical_drive_online_initialization_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 688642)
)
logical_drive_online_initialization_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_online_initialization_completed.setStatus(
        ""
    )

logical_drive_offline_initialization_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 688644)
)
logical_drive_offline_initialization_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_offline_initialization_completed.setStatus(
        ""
    )

logical_drive_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 688646)
)
logical_drive_created.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_created.setStatus(
        ""
    )

logical_drive_rebuild_resumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 688898)
)
logical_drive_rebuild_resumed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_rebuild_resumed.setStatus(
        ""
    )

logical_drive_rebuild_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 688900)
)
logical_drive_rebuild_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_rebuild_started.setStatus(
        ""
    )

logical_drive_rebuild_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 689154)
)
logical_drive_rebuild_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_rebuild_completed.setStatus(
        ""
    )

logical_drive_parity_regeneration_resumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 689410)
)
logical_drive_parity_regeneration_resumed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_parity_regeneration_resumed.setStatus(
        ""
    )

logical_drive_parity_regeneration_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 689412)
)
logical_drive_parity_regeneration_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_parity_regeneration_started.setStatus(
        ""
    )

logical_drive_parity_regeneration_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 689666)
)
logical_drive_parity_regeneration_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_parity_regeneration_completed.setStatus(
        ""
    )

logical_drive_online_expansion_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 689922)
)
logical_drive_online_expansion_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_online_expansion_started.setStatus(
        ""
    )

logical_drive_offline_expansion_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 689924)
)
logical_drive_offline_expansion_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_offline_expansion_started.setStatus(
        ""
    )

logical_drive_online_expansion_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 690178)
)
logical_drive_online_expansion_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_online_expansion_completed.setStatus(
        ""
    )

logical_drive_offline_expansion_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 690180)
)
logical_drive_offline_expansion_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_offline_expansion_completed.setStatus(
        ""
    )

logical_drive_RAID_migration_resumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 690434)
)
logical_drive_RAID_migration_resumed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_RAID_migration_resumed.setStatus(
        ""
    )

logical_drive_add_drive_action_resumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 690436)
)
logical_drive_add_drive_action_resumed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_add_drive_action_resumed.setStatus(
        ""
    )

logical_drive_RAID_migration_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 690438)
)
logical_drive_RAID_migration_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_RAID_migration_started.setStatus(
        ""
    )

logical_drive_add_drive_action_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 690440)
)
logical_drive_add_drive_action_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_add_drive_action_started.setStatus(
        ""
    )

logical_drive_RAID_migration_paused = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 690690)
)
logical_drive_RAID_migration_paused.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_RAID_migration_paused.setStatus(
        ""
    )

logical_drive_add_drive_action_paused = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 690692)
)
logical_drive_add_drive_action_paused.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_add_drive_action_paused.setStatus(
        ""
    )

logical_drive_RAID_migration_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 690694)
)
logical_drive_RAID_migration_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_RAID_migration_completed.setStatus(
        ""
    )

logical_drive_add_drive_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 690696)
)
logical_drive_add_drive_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_drive_add_drive_completed.setStatus(
        ""
    )

media_scan_for_disk_drive_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 690945)
)
media_scan_for_disk_drive_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_disk_drive_started.setStatus(
        ""
    )

media_scan_for_logical_drive_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 690946)
)
media_scan_for_logical_drive_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_logical_drive_started.setStatus(
        ""
    )

media_scan_for_logical_drive_member_drive_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 690947)
)
media_scan_for_logical_drive_member_drive_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_logical_drive_member_drive_started.setStatus(
        ""
    )

media_scan_for_disk_drive_in_expansion_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 691009)
)
media_scan_for_disk_drive_in_expansion_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_disk_drive_in_expansion_started.setStatus(
        ""
    )

media_scan_for_logical_drive_member_drive_in_expansion_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 691011)
)
media_scan_for_logical_drive_member_drive_in_expansion_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_logical_drive_member_drive_in_expansion_started.setStatus(
        ""
    )

media_scan_for_disk_drive_enclosure_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 691073)
)
media_scan_for_disk_drive_enclosure_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_disk_drive_enclosure_started.setStatus(
        ""
    )

media_scan_for_logical_drive_member_drive_in_enclosure_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 691075)
)
media_scan_for_logical_drive_member_drive_in_enclosure_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_logical_drive_member_drive_in_enclosure_started.setStatus(
        ""
    )

media_scan_for_logical_drive_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 691202)
)
media_scan_for_logical_drive_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_logical_drive_completed.setStatus(
        ""
    )

media_scan_for_logical_drvie_member_drive_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 691203)
)
media_scan_for_logical_drvie_member_drive_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_logical_drvie_member_drive_completed.setStatus(
        ""
    )

media_scan_for_logical_drive_stopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 691204)
)
media_scan_for_logical_drive_stopped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_logical_drive_stopped.setStatus(
        ""
    )

unable_to_start_media_scan_Previous_task_is_still_in_progress = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 691205)
)
unable_to_start_media_scan_Previous_task_is_still_in_progress.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    unable_to_start_media_scan_Previous_task_is_still_in_progress.setStatus(
        ""
    )

media_scan_for_logical_drvie_member_in_expansion_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 691267)
)
media_scan_for_logical_drvie_member_in_expansion_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_logical_drvie_member_in_expansion_completed.setStatus(
        ""
    )

media_scan_for_logical_drvie_member_in_enclosure_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 691331)
)
media_scan_for_logical_drvie_member_in_enclosure_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    media_scan_for_logical_drvie_member_in_enclosure_completed.setStatus(
        ""
    )

drive_clone_resumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 696577)
)
drive_clone_resumed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_resumed.setStatus(
        ""
    )

drive_clone_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 696578)
)
drive_clone_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_started.setStatus(
        ""
    )

drive_clone_resumed_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 696641)
)
drive_clone_resumed_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_resumed_on_expansion_drive.setStatus(
        ""
    )

drive_clone_started_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 696642)
)
drive_clone_started_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_started_on_expansion_drive.setStatus(
        ""
    )

drive_clone_resumed_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 696705)
)
drive_clone_resumed_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_resumed_on_enclosure_drive.setStatus(
        ""
    )

drive_clone_started_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 696706)
)
drive_clone_started_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_started_on_enclosure_drive.setStatus(
        ""
    )

drive_copy_and_replace_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 696833)
)
drive_copy_and_replace_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_copy_and_replace_completed.setStatus(
        ""
    )

drive_clone_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 696834)
)
drive_clone_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_completed.setStatus(
        ""
    )

drive_copy_and_replace_completed_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 696897)
)
drive_copy_and_replace_completed_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_copy_and_replace_completed_on_expansion_drive.setStatus(
        ""
    )

drive_clone_completed_on_expansion_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 696898)
)
drive_clone_completed_on_expansion_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_completed_on_expansion_drive.setStatus(
        ""
    )

drive_copy_and_replace_completed_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 696961)
)
drive_copy_and_replace_completed_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_copy_and_replace_completed_on_enclosure_drive.setStatus(
        ""
    )

drive_clone_completed_on_enclosure_drive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 696962)
)
drive_clone_completed_on_enclosure_drive.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    drive_clone_completed_on_enclosure_drive.setStatus(
        ""
    )

logical_volume_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 720936)
)
logical_volume_created.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_created.setStatus(
        ""
    )

logical_volume_creation_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 720937)
)
logical_volume_creation_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_creation_failed.setStatus(
        ""
    )

logical_volume_expansion_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 720938)
)
logical_volume_expansion_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_expansion_completed.setStatus(
        ""
    )

logical_volume_expansion_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 720939)
)
logical_volume_expansion_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_expansion_failed.setStatus(
        ""
    )

logical_volume_deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 720940)
)
logical_volume_deleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_deleted.setStatus(
        ""
    )

logical_volume_cache_data_purged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 722945)
)
logical_volume_cache_data_purged.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_cache_data_purged.setStatus(
        ""
    )

logical_volume_status_back_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 738561)
)
logical_volume_status_back_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_status_back_to_normal.setStatus(
        ""
    )

logical_volume_degraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 738562)
)
logical_volume_degraded.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_degraded.setStatus(
        ""
    )

logical_volume_failed_fatal_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 738563)
)
logical_volume_failed_fatal_fail.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_failed_fatal_fail.setStatus(
        ""
    )

logical_volume_failed_invalid_array = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 738564)
)
logical_volume_failed_invalid_array.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_failed_invalid_array.setStatus(
        ""
    )

logical_volume_member_drive_missing_incomplete_array = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 738565)
)
logical_volume_member_drive_missing_incomplete_array.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_member_drive_missing_incomplete_array.setStatus(
        ""
    )

logical_volume_member_drive_missing_missing_drives = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 738566)
)
logical_volume_member_drive_missing_missing_drives.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_member_drive_missing_missing_drives.setStatus(
        ""
    )

logical_volume_status_changed_from_online_to_offline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 738817)
)
logical_volume_status_changed_from_online_to_offline.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_status_changed_from_online_to_offline.setStatus(
        ""
    )

logical_volume_status_changed_from_offline_to_online = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 738818)
)
logical_volume_status_changed_from_offline_to_online.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_status_changed_from_offline_to_online.setStatus(
        ""
    )

all_member_drives_of_a_logical_volume_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 738819)
)
all_member_drives_of_a_logical_volume_removed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    all_member_drives_of_a_logical_volume_removed.setStatus(
        ""
    )

all_member_drives_of_a_logical_volume_restored = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 738820)
)
all_member_drives_of_a_logical_volume_restored.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    all_member_drives_of_a_logical_volume_restored.setStatus(
        ""
    )

logical_volume_undeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 738821)
)
logical_volume_undeleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_undeleted.setStatus(
        ""
    )

logical_volume_online_initialization_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 753921)
)
logical_volume_online_initialization_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_online_initialization_started.setStatus(
        ""
    )

logical_volume_offline_initialization_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 753923)
)
logical_volume_offline_initialization_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_offline_initialization_started.setStatus(
        ""
    )

logical_volume_creation_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 753925)
)
logical_volume_creation_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_creation_started.setStatus(
        ""
    )

logical_volume_online_initialization_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 754177)
)
logical_volume_online_initialization_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_online_initialization_completed.setStatus(
        ""
    )

logical_volume_offline_initialization_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 754179)
)
logical_volume_offline_initialization_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_offline_initialization_completed.setStatus(
        ""
    )

logical_volume_creation_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 754181)
)
logical_volume_creation_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_creation_completed.setStatus(
        ""
    )

logical_volume_rebuild_resumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 754433)
)
logical_volume_rebuild_resumed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_rebuild_resumed.setStatus(
        ""
    )

logical_volume_rebuild_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 754435)
)
logical_volume_rebuild_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_rebuild_started.setStatus(
        ""
    )

logical_volume_rebuild_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 754689)
)
logical_volume_rebuild_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_rebuild_completed.setStatus(
        ""
    )

logical_volume_parity_regeneration_resumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 754945)
)
logical_volume_parity_regeneration_resumed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_parity_regeneration_resumed.setStatus(
        ""
    )

logical_volume_parity_regeneration_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 754947)
)
logical_volume_parity_regeneration_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_parity_regeneration_started.setStatus(
        ""
    )

logical_volume_parity_regeneration_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 755201)
)
logical_volume_parity_regeneration_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_parity_regeneration_completed.setStatus(
        ""
    )

logical_volume_online_expansion_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 755457)
)
logical_volume_online_expansion_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_online_expansion_started.setStatus(
        ""
    )

logical_volume_offline_expansion_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 755459)
)
logical_volume_offline_expansion_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_offline_expansion_started.setStatus(
        ""
    )

logical_volume_online_expansion_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 755713)
)
logical_volume_online_expansion_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_online_expansion_completed.setStatus(
        ""
    )

logical_volume_offline_expansion_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 755715)
)
logical_volume_offline_expansion_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_offline_expansion_completed.setStatus(
        ""
    )

logical_volume_migration_resumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 755969)
)
logical_volume_migration_resumed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_migration_resumed.setStatus(
        ""
    )

logical_volume_add_drive_action_resumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 755971)
)
logical_volume_add_drive_action_resumed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_add_drive_action_resumed.setStatus(
        ""
    )

logical_volume_migration_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 755973)
)
logical_volume_migration_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_migration_started.setStatus(
        ""
    )

logical_volume_add_drive_action_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 755975)
)
logical_volume_add_drive_action_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_add_drive_action_started.setStatus(
        ""
    )

logical_volume_migration_paused = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 756225)
)
logical_volume_migration_paused.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_migration_paused.setStatus(
        ""
    )

logical_volume_add_drive_action_paused = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 756227)
)
logical_volume_add_drive_action_paused.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_add_drive_action_paused.setStatus(
        ""
    )

logical_volume_migration_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 756229)
)
logical_volume_migration_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_migration_completed.setStatus(
        ""
    )

logical_volume_add_drive_action_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 756231)
)
logical_volume_add_drive_action_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    logical_volume_add_drive_action_completed.setStatus(
        ""
    )

partition_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 786477)
)
partition_created.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    partition_created.setStatus(
        ""
    )

partition_creation_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 786478)
)
partition_creation_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    partition_creation_failed.setStatus(
        ""
    )

partition_deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 786479)
)
partition_deleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    partition_deleted.setStatus(
        ""
    )

partition_deletion_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 786480)
)
partition_deletion_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    partition_deletion_failed.setStatus(
        ""
    )

partition_has_been_activated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 786481)
)
partition_has_been_activated.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    partition_has_been_activated.setStatus(
        ""
    )

license_key_consistency_check_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 860417)
)
license_key_consistency_check_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    license_key_consistency_check_failed.setStatus(
        ""
    )

license_key_is_not_supported_by_the_installed_firmware = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 860418)
)
license_key_is_not_supported_by_the_installed_firmware.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    license_key_is_not_supported_by_the_installed_firmware.setStatus(
        ""
    )

pool_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917505)
)
pool_created.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_created.setStatus(
        ""
    )

pool_creation_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917506)
)
pool_creation_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_creation_failed.setStatus(
        ""
    )

pool_expansion_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917507)
)
pool_expansion_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_expansion_completed.setStatus(
        ""
    )

pool_expansion_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917508)
)
pool_expansion_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_expansion_failed.setStatus(
        ""
    )

pool_deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917509)
)
pool_deleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_deleted.setStatus(
        ""
    )

pool_migration_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917514)
)
pool_migration_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_migration_started.setStatus(
        ""
    )

pool_migration_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917515)
)
pool_migration_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_migration_completed.setStatus(
        ""
    )

pool_migration_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917516)
)
pool_migration_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_migration_failed.setStatus(
        ""
    )

bad_block_found_in_deleted_ME_migration_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917589)
)
bad_block_found_in_deleted_ME_migration_aborted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    bad_block_found_in_deleted_ME_migration_aborted.setStatus(
        ""
    )

the_pool_cannot_connect_to_cloud_because_the_network_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917632)
)
the_pool_cannot_connect_to_cloud_because_the_network_error.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_cannot_connect_to_cloud_because_the_network_error.setStatus(
        ""
    )

the_pool_cannot_connect_to_cloud_because_authentication_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917633)
)
the_pool_cannot_connect_to_cloud_because_authentication_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_cannot_connect_to_cloud_because_authentication_failed.setStatus(
        ""
    )

the_pool_cannot_connect_to_cloud_because_the_bucket_not_exist = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917634)
)
the_pool_cannot_connect_to_cloud_because_the_bucket_not_exist.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_cannot_connect_to_cloud_because_the_bucket_not_exist.setStatus(
        ""
    )

the_pool_cannot_connect_to_cloud_because_failed_create_bucket = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917635)
)
the_pool_cannot_connect_to_cloud_because_failed_create_bucket.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_cannot_connect_to_cloud_because_failed_create_bucket.setStatus(
        ""
    )

the_pool_cannot_connect_to_cloud_The_bucket_has_been_used = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917636)
)
the_pool_cannot_connect_to_cloud_The_bucket_has_been_used.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_cannot_connect_to_cloud_The_bucket_has_been_used.setStatus(
        ""
    )

the_pool_cannot_connect_to_cloud_Wrong_encryption_key = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917637)
)
the_pool_cannot_connect_to_cloud_Wrong_encryption_key.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_cannot_connect_to_cloud_Wrong_encryption_key.setStatus(
        ""
    )

the_pool_has_failed_to_upload_data_to_cloud = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917638)
)
the_pool_has_failed_to_upload_data_to_cloud.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_has_failed_to_upload_data_to_cloud.setStatus(
        ""
    )

the_pool_cannot_connect_to_cloud_No_channel_for_iSCSI_device = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917639)
)
the_pool_cannot_connect_to_cloud_No_channel_for_iSCSI_device.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_cannot_connect_to_cloud_No_channel_for_iSCSI_device.setStatus(
        ""
    )

the_pool_has_been_deleted_The_cloud_storage_is_not_deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917640)
)
the_pool_has_been_deleted_The_cloud_storage_is_not_deleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_has_been_deleted_The_cloud_storage_is_not_deleted.setStatus(
        ""
    )

the_data_of_the_pool_saved_in_the_bucket_is_corrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 917641)
)
the_data_of_the_pool_saved_in_the_bucket_is_corrupted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_data_of_the_pool_saved_in_the_bucket_is_corrupted.setStatus(
        ""
    )

volume_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 983053)
)
volume_created.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    volume_created.setStatus(
        ""
    )

volume_creation_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 983054)
)
volume_creation_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    volume_creation_failed.setStatus(
        ""
    )

volume_deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 983055)
)
volume_deleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    volume_deleted.setStatus(
        ""
    )

volume_deletion_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 983056)
)
volume_deletion_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    volume_deletion_failed.setStatus(
        ""
    )

volume_expansion_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 983058)
)
volume_expansion_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    volume_expansion_completed.setStatus(
        ""
    )

snapshot_image_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1048577)
)
snapshot_image_created.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_image_created.setStatus(
        ""
    )

snapshot_image_creation_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1048578)
)
snapshot_image_creation_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_image_creation_failed.setStatus(
        ""
    )

snapshot_image_deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1048579)
)
snapshot_image_deleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_image_deleted.setStatus(
        ""
    )

snapshot_image_deletion_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1048580)
)
snapshot_image_deletion_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_image_deletion_failed.setStatus(
        ""
    )

snapshot_image_purge_triggered = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1048596)
)
snapshot_image_purge_triggered.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_image_purge_triggered.setStatus(
        ""
    )

free_space_might_be_insufficient_for_future_snapshot_usage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1048627)
)
free_space_might_be_insufficient_for_future_snapshot_usage.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    free_space_might_be_insufficient_for_future_snapshot_usage.setStatus(
        ""
    )

free_space_recovered_for_future_snapshot_usage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1048630)
)
free_space_recovered_for_future_snapshot_usage.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    free_space_recovered_for_future_snapshot_usage.setStatus(
        ""
    )

the_snapshot_images_has_been_backed_up_to_cloud = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1048704)
)
the_snapshot_images_has_been_backed_up_to_cloud.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_snapshot_images_has_been_backed_up_to_cloud.setStatus(
        ""
    )

remote_drive_has_connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1114148)
)
remote_drive_has_connected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    remote_drive_has_connected.setStatus(
        ""
    )

remote_drive_has_disconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1114149)
)
remote_drive_has_disconnected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    remote_drive_has_disconnected.setStatus(
        ""
    )

pair_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179669)
)
pair_created.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pair_created.setStatus(
        ""
    )

pair_creation_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179670)
)
pair_creation_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pair_creation_failed.setStatus(
        ""
    )

pair_deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179671)
)
pair_deleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pair_deleted.setStatus(
        ""
    )

synchronous_replication_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179672)
)
synchronous_replication_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    synchronous_replication_started.setStatus(
        ""
    )

synchronous_replication_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179673)
)
synchronous_replication_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    synchronous_replication_completed.setStatus(
        ""
    )

synchronous_replication_paused = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179674)
)
synchronous_replication_paused.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    synchronous_replication_paused.setStatus(
        ""
    )

synchronous_replication_resumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179675)
)
synchronous_replication_resumed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    synchronous_replication_resumed.setStatus(
        ""
    )

synchronous_replication_pair_split = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179676)
)
synchronous_replication_pair_split.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    synchronous_replication_pair_split.setStatus(
        ""
    )

synchronous_pair_split_because_network_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179677)
)
synchronous_pair_split_because_network_timeout.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    synchronous_pair_split_because_network_timeout.setStatus(
        ""
    )

asynchronous_replication_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179678)
)
asynchronous_replication_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    asynchronous_replication_started.setStatus(
        ""
    )

asynchronous_replication_paused = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179679)
)
asynchronous_replication_paused.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    asynchronous_replication_paused.setStatus(
        ""
    )

asynchronous_replication_resumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179680)
)
asynchronous_replication_resumed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    asynchronous_replication_resumed.setStatus(
        ""
    )

asynchronous_replication_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179681)
)
asynchronous_replication_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    asynchronous_replication_completed.setStatus(
        ""
    )

asynchronous_replication_pair_split = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179682)
)
asynchronous_replication_pair_split.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    asynchronous_replication_pair_split.setStatus(
        ""
    )

replication_pair_role_switched = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179683)
)
replication_pair_role_switched.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    replication_pair_role_switched.setStatus(
        ""
    )

free_space_might_be_insufficient_for_future_replication_pair = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179700)
)
free_space_might_be_insufficient_for_future_replication_pair.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    free_space_might_be_insufficient_for_future_replication_pair.setStatus(
        ""
    )

free_space_recovered_for_future_replication_pair_usage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179703)
)
free_space_recovered_for_future_replication_pair_usage.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    free_space_recovered_for_future_replication_pair_usage.setStatus(
        ""
    )

pair_synchronization_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179706)
)
pair_synchronization_aborted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pair_synchronization_aborted.setStatus(
        ""
    )

pair_synchronization_failed_and_split = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179707)
)
pair_synchronization_failed_and_split.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pair_synchronization_failed_and_split.setStatus(
        ""
    )

initial_copy_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179709)
)
initial_copy_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    initial_copy_started.setStatus(
        ""
    )

failed_to_start_the_Initial_copy = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179710)
)
failed_to_start_the_Initial_copy.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_start_the_Initial_copy.setStatus(
        ""
    )

initial_copy_has_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179711)
)
initial_copy_has_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    initial_copy_has_completed.setStatus(
        ""
    )

initial_copy_has_continued = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179712)
)
initial_copy_has_continued.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    initial_copy_has_continued.setStatus(
        ""
    )

initial_copy_has_been_stopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179713)
)
initial_copy_has_been_stopped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    initial_copy_has_been_stopped.setStatus(
        ""
    )

initial_copy_has_been_resumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179714)
)
initial_copy_has_been_resumed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    initial_copy_has_been_resumed.setStatus(
        ""
    )

failed_to_resume_the_initial_copy = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179715)
)
failed_to_resume_the_initial_copy.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_resume_the_initial_copy.setStatus(
        ""
    )

pair_recovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179716)
)
pair_recovered.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pair_recovered.setStatus(
        ""
    )

pair_broken = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179717)
)
pair_broken.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pair_broken.setStatus(
        ""
    )

pair_synchronization_has_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179718)
)
pair_synchronization_has_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pair_synchronization_has_started.setStatus(
        ""
    )

failed_to_start_the_pair_synchronization = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179719)
)
failed_to_start_the_pair_synchronization.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_start_the_pair_synchronization.setStatus(
        ""
    )

pair_synchronization_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179720)
)
pair_synchronization_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pair_synchronization_completed.setStatus(
        ""
    )

pair_synchronization_has_continued = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179721)
)
pair_synchronization_has_continued.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pair_synchronization_has_continued.setStatus(
        ""
    )

pair_synchronization_has_been_stopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179722)
)
pair_synchronization_has_been_stopped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pair_synchronization_has_been_stopped.setStatus(
        ""
    )

pair_synchronization_has_been_resumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179723)
)
pair_synchronization_has_been_resumed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pair_synchronization_has_been_resumed.setStatus(
        ""
    )

failed_to_resume_the_pair_synchronization = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179724)
)
failed_to_resume_the_pair_synchronization.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_resume_the_pair_synchronization.setStatus(
        ""
    )

target_volume_full = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179725)
)
target_volume_full.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    target_volume_full.setStatus(
        ""
    )

pair_synchronization_is_in_progress = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179726)
)
pair_synchronization_is_in_progress.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pair_synchronization_is_in_progress.setStatus(
        ""
    )

bad_block_found_in_source_volume_pair_synchronization_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1179732)
)
bad_block_found_in_source_volume_pair_synchronization_aborted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    bad_block_found_in_source_volume_pair_synchronization_aborted.setStatus(
        ""
    )

pool_space_utilization_exceeded_the_threshold_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245190)
)
pool_space_utilization_exceeded_the_threshold_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_space_utilization_exceeded_the_threshold_info.setStatus(
        ""
    )

pool_space_utilization_exceeded_the_threshold_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245190)
)
pool_space_utilization_exceeded_the_threshold_warning.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_space_utilization_exceeded_the_threshold_warning.setStatus(
        ""
    )

pool_space_utilization_exceeded_the_threshold_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245190)
)
pool_space_utilization_exceeded_the_threshold_error.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_space_utilization_exceeded_the_threshold_error.setStatus(
        ""
    )

pool_space_utilization_exceeded_the_threshold_critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245190)
)
pool_space_utilization_exceeded_the_threshold_critical.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_space_utilization_exceeded_the_threshold_critical.setStatus(
        ""
    )

pool_space_utilization_has_dropped_below_threshold_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245191)
)
pool_space_utilization_has_dropped_below_threshold_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_space_utilization_has_dropped_below_threshold_info.setStatus(
        ""
    )

pool_space_utilization_has_dropped_below_threshold_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245191)
)
pool_space_utilization_has_dropped_below_threshold_warning.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_space_utilization_has_dropped_below_threshold_warning.setStatus(
        ""
    )

pool_space_utilization_has_dropped_below_threshold_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245191)
)
pool_space_utilization_has_dropped_below_threshold_error.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_space_utilization_has_dropped_below_threshold_error.setStatus(
        ""
    )

pool_space_utilization_has_dropped_below_threshold_critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245191)
)
pool_space_utilization_has_dropped_below_threshold_critical.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_space_utilization_has_dropped_below_threshold_critical.setStatus(
        ""
    )

pool_status_changed_to_online = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245192)
)
pool_status_changed_to_online.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_status_changed_to_online.setStatus(
        ""
    )

pool_status_changed_to_offline = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245193)
)
pool_status_changed_to_offline.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pool_status_changed_to_offline.setStatus(
        ""
    )

the_pool_allocated_space_has_exceeded_the_threshold_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245222)
)
the_pool_allocated_space_has_exceeded_the_threshold_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_allocated_space_has_exceeded_the_threshold_info.setStatus(
        ""
    )

the_pool_allocated_space_has_exceeded_the_threshold_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245222)
)
the_pool_allocated_space_has_exceeded_the_threshold_warning.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_allocated_space_has_exceeded_the_threshold_warning.setStatus(
        ""
    )

the_pool_allocated_space_has_exceeded_the_threshold_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245222)
)
the_pool_allocated_space_has_exceeded_the_threshold_error.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_allocated_space_has_exceeded_the_threshold_error.setStatus(
        ""
    )

the_pool_allocated_space_has_exceeded_the_threshold_critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245222)
)
the_pool_allocated_space_has_exceeded_the_threshold_critical.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_allocated_space_has_exceeded_the_threshold_critical.setStatus(
        ""
    )

the_pool_allocated_space_has_dropped_below_threshold_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245223)
)
the_pool_allocated_space_has_dropped_below_threshold_info.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_allocated_space_has_dropped_below_threshold_info.setStatus(
        ""
    )

the_pool_allocated_space_has_dropped_below_threshold_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245223)
)
the_pool_allocated_space_has_dropped_below_threshold_warning.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_allocated_space_has_dropped_below_threshold_warning.setStatus(
        ""
    )

the_pool_allocated_space_has_dropped_below_threshold_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245223)
)
the_pool_allocated_space_has_dropped_below_threshold_error.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_allocated_space_has_dropped_below_threshold_error.setStatus(
        ""
    )

the_pool_allocated_space_has_dropped_below_threshold_critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245223)
)
the_pool_allocated_space_has_dropped_below_threshold_critical.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_allocated_space_has_dropped_below_threshold_critical.setStatus(
        ""
    )

the_pool_has_been_foreced_offline_because_error_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1245244)
)
the_pool_has_been_foreced_offline_because_error_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_pool_has_been_foreced_offline_because_error_detected.setStatus(
        ""
    )

free_space_might_be_insufficient_for_future_volume_usage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1310770)
)
free_space_might_be_insufficient_for_future_volume_usage.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    free_space_might_be_insufficient_for_future_volume_usage.setStatus(
        ""
    )

free_space_recovered_for_future_volume_usage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1310773)
)
free_space_recovered_for_future_volume_usage.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    free_space_recovered_for_future_volume_usage.setStatus(
        ""
    )

tier_migration_has_been_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1310799)
)
tier_migration_has_been_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    tier_migration_has_been_started.setStatus(
        ""
    )

tier_migration_has_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1310800)
)
tier_migration_has_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    tier_migration_has_completed.setStatus(
        ""
    )

tier_migration_has_been_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1310801)
)
tier_migration_has_been_aborted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    tier_migration_has_been_aborted.setStatus(
        ""
    )

volume_expansion_has_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1310802)
)
volume_expansion_has_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    volume_expansion_has_completed.setStatus(
        ""
    )

volume_expansion_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1310803)
)
volume_expansion_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    volume_expansion_failed.setStatus(
        ""
    )

the_system_has_been_unable_to_satisfy_QoS_policy_for_15_min = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1310858)
)
the_system_has_been_unable_to_satisfy_QoS_policy_for_15_min.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_system_has_been_unable_to_satisfy_QoS_policy_for_15_min.setStatus(
        ""
    )

snapshot_image_has_been_activated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1376273)
)
snapshot_image_has_been_activated.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_image_has_been_activated.setStatus(
        ""
    )

insufficient_free_space_for_data_allocation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1441848)
)
insufficient_free_space_for_data_allocation.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    insufficient_free_space_for_data_allocation.setStatus(
        ""
    )

free_space_recovered_for_data_allocation = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1441849)
)
free_space_recovered_for_data_allocation.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    free_space_recovered_for_data_allocation.setStatus(
        ""
    )

non_optimal_configuration_may_impact_system_performance = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1507347)
)
non_optimal_configuration_may_impact_system_performance.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    non_optimal_configuration_may_impact_system_performance.setStatus(
        ""
    )

the_SMTP_server_has_not_been_configured_yet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1507501)
)
the_SMTP_server_has_not_been_configured_yet.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_SMTP_server_has_not_been_configured_yet.setStatus(
        ""
    )

snapshot_license_expired = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573003)
)
snapshot_license_expired.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_license_expired.setStatus(
        ""
    )

failed_to_take_snapshot_of_pair_target_volume = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573004)
)
failed_to_take_snapshot_of_pair_target_volume.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_take_snapshot_of_pair_target_volume.setStatus(
        ""
    )

the_exception_of_the_snapshot_schedule_prune_rule_occurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573005)
)
the_exception_of_the_snapshot_schedule_prune_rule_occurred.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_exception_of_the_snapshot_schedule_prune_rule_occurred.setStatus(
        ""
    )

maximum_snapshot_amount_of_the_volume_reached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573006)
)
maximum_snapshot_amount_of_the_volume_reached.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    maximum_snapshot_amount_of_the_volume_reached.setStatus(
        ""
    )

maximum_snapshot_amount_of_the_system_reached = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573007)
)
maximum_snapshot_amount_of_the_system_reached.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    maximum_snapshot_amount_of_the_system_reached.setStatus(
        ""
    )

snapshot_schedule_failed_Some_flush_agents_cannot_be_connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573008)
)
snapshot_schedule_failed_Some_flush_agents_cannot_be_connected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_schedule_failed_Some_flush_agents_cannot_be_connected.setStatus(
        ""
    )

snapshot_schedule_failed_Host_volume_disk_can_not_be_locked = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573009)
)
snapshot_schedule_failed_Host_volume_disk_can_not_be_locked.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_schedule_failed_Host_volume_disk_can_not_be_locked.setStatus(
        ""
    )

snapshot_schedule_failed_Host_cache_flush_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573010)
)
snapshot_schedule_failed_Host_cache_flush_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_schedule_failed_Host_cache_flush_failed.setStatus(
        ""
    )

snapshot_schedule_failed_Host_volume_disk_has_been_locked = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573011)
)
snapshot_schedule_failed_Host_volume_disk_has_been_locked.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_schedule_failed_Host_volume_disk_has_been_locked.setStatus(
        ""
    )

snapshot_schedule_failed_Host_cache_data_flush_has_timed_out = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573012)
)
snapshot_schedule_failed_Host_cache_data_flush_has_timed_out.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_schedule_failed_Host_cache_data_flush_has_timed_out.setStatus(
        ""
    )

snapshot_schedule_failed_Host_flush_the_database_cache_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573013)
)
snapshot_schedule_failed_Host_flush_the_database_cache_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_schedule_failed_Host_flush_the_database_cache_failed.setStatus(
        ""
    )

snapshot_schedule_failed_File_system_does_not_mount_the_volume = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573014)
)
snapshot_schedule_failed_File_system_does_not_mount_the_volume.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_schedule_failed_File_system_does_not_mount_the_volume.setStatus(
        ""
    )

snapshot_schedule_failed_Volume_has_not_been_mapped_to_host = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573015)
)
snapshot_schedule_failed_Volume_has_not_been_mapped_to_host.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_schedule_failed_Volume_has_not_been_mapped_to_host.setStatus(
        ""
    )

snapshot_schedule_failed_Exception_has_occurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573016)
)
snapshot_schedule_failed_Exception_has_occurred.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_schedule_failed_Exception_has_occurred.setStatus(
        ""
    )

snapshot_schedule_failed_The_volume_has_not_been_mapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573017)
)
snapshot_schedule_failed_The_volume_has_not_been_mapped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_schedule_failed_The_volume_has_not_been_mapped.setStatus(
        ""
    )

the_snapshot_schedule_has_failed_to_unlock_the_host_volume_disk = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573018)
)
the_snapshot_schedule_has_failed_to_unlock_the_host_volume_disk.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_snapshot_schedule_has_failed_to_unlock_the_host_volume_disk.setStatus(
        ""
    )

the_snapshot_schedule_has_failed_to_resume_the_host_database = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573019)
)
the_snapshot_schedule_has_failed_to_resume_the_host_database.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_snapshot_schedule_has_failed_to_resume_the_host_database.setStatus(
        ""
    )

snapshot_schedule_failed_Flush_settings_have_not_configured = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573020)
)
snapshot_schedule_failed_Flush_settings_have_not_configured.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_schedule_failed_Flush_settings_have_not_configured.setStatus(
        ""
    )

snapshot_schedule_and_backup_to_cloud_failed_Exception_occur = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573021)
)
snapshot_schedule_and_backup_to_cloud_failed_Exception_occur.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_schedule_and_backup_to_cloud_failed_Exception_occur.setStatus(
        ""
    )

failed_to_execute_the_snapshot_schedule = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573022)
)
failed_to_execute_the_snapshot_schedule.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_execute_the_snapshot_schedule.setStatus(
        ""
    )

snapshot_schedule_failed_The_device_can_not_be_connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573023)
)
snapshot_schedule_failed_The_device_can_not_be_connected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    snapshot_schedule_failed_The_device_can_not_be_connected.setStatus(
        ""
    )

the_storage_tiering_license_of_the_device_has_expired = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573024)
)
the_storage_tiering_license_of_the_device_has_expired.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_storage_tiering_license_of_the_device_has_expired.setStatus(
        ""
    )

tier_migration_schedule_failed_Previous_process_is_processing = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573025)
)
tier_migration_schedule_failed_Previous_process_is_processing.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    tier_migration_schedule_failed_Previous_process_is_processing.setStatus(
        ""
    )

tier_migration_schedule_failed_Specified_volumes_are_not_found = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573026)
)
tier_migration_schedule_failed_Specified_volumes_are_not_found.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    tier_migration_schedule_failed_Specified_volumes_are_not_found.setStatus(
        ""
    )

tier_migration_schedule_rejected_The_storage_has_one_tier = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573027)
)
tier_migration_schedule_rejected_The_storage_has_one_tier.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    tier_migration_schedule_rejected_The_storage_has_one_tier.setStatus(
        ""
    )

tier_migration_schedule_failed_Exception_has_occurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573028)
)
tier_migration_schedule_failed_Exception_has_occurred.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    tier_migration_schedule_failed_Exception_has_occurred.setStatus(
        ""
    )

volume_replication_schedule_failed_Target_volume_mapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573029)
)
volume_replication_schedule_failed_Target_volume_mapped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    volume_replication_schedule_failed_Target_volume_mapped.setStatus(
        ""
    )

the_volume_mirror_license_of_the_device_has_expired = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573030)
)
the_volume_mirror_license_of_the_device_has_expired.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_volume_mirror_license_of_the_device_has_expired.setStatus(
        ""
    )

volume_mirror_schedule_failed_Exceptions_have_occurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573031)
)
volume_mirror_schedule_failed_Exceptions_have_occurred.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    volume_mirror_schedule_failed_Exceptions_have_occurred.setStatus(
        ""
    )

volume_mirror_schedule_failed_Exception_has_occurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573032)
)
volume_mirror_schedule_failed_Exception_has_occurred.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    volume_mirror_schedule_failed_Exception_has_occurred.setStatus(
        ""
    )

volume_mirror_schedule_failed_The_source_volume_is_not_mapped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573033)
)
volume_mirror_schedule_failed_The_source_volume_is_not_mapped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    volume_mirror_schedule_failed_The_source_volume_is_not_mapped.setStatus(
        ""
    )

volume_mirror_schedule_failed_Flush_agents_not_connected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573034)
)
volume_mirror_schedule_failed_Flush_agents_not_connected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    volume_mirror_schedule_failed_Flush_agents_not_connected.setStatus(
        ""
    )

the_volume_copy_license_of_the_device_has_expired = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573035)
)
the_volume_copy_license_of_the_device_has_expired.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_volume_copy_license_of_the_device_has_expired.setStatus(
        ""
    )

volume_copy_schedule_failed_Exception_has_occurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1573036)
)
volume_copy_schedule_failed_Exception_has_occurred.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    volume_copy_schedule_failed_Exception_has_occurred.setStatus(
        ""
    )

user_s_password_has_been_changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520065)
)
user_s_password_has_been_changed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    user_s_password_has_been_changed.setStatus(
        ""
    )

user_s_password_has_expired = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520066)
)
user_s_password_has_expired.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    user_s_password_has_expired.setStatus(
        ""
    )

the_password_policy_has_been_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520067)
)
the_password_policy_has_been_enabled.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_password_policy_has_been_enabled.setStatus(
        ""
    )

the_settings_of_the_password_policy_have_been_changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520068)
)
the_settings_of_the_password_policy_have_been_changed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_settings_of_the_password_policy_have_been_changed.setStatus(
        ""
    )

the_password_policy_has_been_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520069)
)
the_password_policy_has_been_disabled.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_password_policy_has_been_disabled.setStatus(
        ""
    )

the_service_status_abnormal_has_beendetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520070)
)
the_service_status_abnormal_has_beendetected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_service_status_abnormal_has_beendetected.setStatus(
        ""
    )

the_service_status_has_returned_to_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520071)
)
the_service_status_has_returned_to_normal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_service_status_has_returned_to_normal.setStatus(
        ""
    )

abnormal_status_service_will_be_reactivated_in_a_few_minutes = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520072)
)
abnormal_status_service_will_be_reactivated_in_a_few_minutes.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    abnormal_status_service_will_be_reactivated_in_a_few_minutes.setStatus(
        ""
    )

the_service_has_been_reactivated_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520073)
)
the_service_has_been_reactivated_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_service_has_been_reactivated_successfully.setStatus(
        ""
    )

failed_to_reactivated_the_abnormal_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520074)
)
failed_to_reactivated_the_abnormal_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_reactivated_the_abnormal_service.setStatus(
        ""
    )

a_user_has_been_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520075)
)
a_user_has_been_created.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_user_has_been_created.setStatus(
        ""
    )

a_user_has_been_assigned_to_the_specific_groups = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520076)
)
a_user_has_been_assigned_to_the_specific_groups.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_user_has_been_assigned_to_the_specific_groups.setStatus(
        ""
    )

the_superuser_privilege_has_been_assigned_to_a_specific_user = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520077)
)
the_superuser_privilege_has_been_assigned_to_a_specific_user.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_superuser_privilege_has_been_assigned_to_a_specific_user.setStatus(
        ""
    )

the_superuser_privilege_for_a_specific_user_has_been_stopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520078)
)
the_superuser_privilege_for_a_specific_user_has_been_stopped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_superuser_privilege_for_a_specific_user_has_been_stopped.setStatus(
        ""
    )

a_user_account_has_been_deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520079)
)
a_user_account_has_been_deleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_user_account_has_been_deleted.setStatus(
        ""
    )

a_user_group_has_been_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520080)
)
a_user_group_has_been_created.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_user_group_has_been_created.setStatus(
        ""
    )

a_user_group_has_been_deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520081)
)
a_user_group_has_been_deleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_user_group_has_been_deleted.setStatus(
        ""
    )

a_user_group_added_users = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520082)
)
a_user_group_added_users.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_user_group_added_users.setStatus(
        ""
    )

a_user_group_removed_users = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520083)
)
a_user_group_removed_users.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_user_group_removed_users.setStatus(
        ""
    )

a_service_has_been_started_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520084)
)
a_service_has_been_started_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_service_has_been_started_successfully.setStatus(
        ""
    )

a_service_has_been_restarted_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520085)
)
a_service_has_been_restarted_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_service_has_been_restarted_successfully.setStatus(
        ""
    )

a_service_has_been_stopped_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520086)
)
a_service_has_been_stopped_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_service_has_been_stopped_successfully.setStatus(
        ""
    )

the_configuration_of_a_service_has_been_applied_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520087)
)
the_configuration_of_a_service_has_been_applied_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_configuration_of_a_service_has_been_applied_successfully.setStatus(
        ""
    )

failed_to_start_a_data_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520088)
)
failed_to_start_a_data_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_start_a_data_service.setStatus(
        ""
    )

failed_to_start_an_authentication_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520089)
)
failed_to_start_an_authentication_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_start_an_authentication_service.setStatus(
        ""
    )

failed_to_restart_a_data_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520090)
)
failed_to_restart_a_data_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_restart_a_data_service.setStatus(
        ""
    )

failed_to_restart_an_authentication_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520091)
)
failed_to_restart_an_authentication_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_restart_an_authentication_service.setStatus(
        ""
    )

failed_to_stop_a_data_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520092)
)
failed_to_stop_a_data_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_stop_a_data_service.setStatus(
        ""
    )

failed_to_stop_an_authentication_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520093)
)
failed_to_stop_an_authentication_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_stop_an_authentication_service.setStatus(
        ""
    )

failed_to_set_the_configuration_of_a_data_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520094)
)
failed_to_set_the_configuration_of_a_data_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_set_the_configuration_of_a_data_service.setStatus(
        ""
    )

failed_to_set_the_configuration_of_an_authentication_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520095)
)
failed_to_set_the_configuration_of_an_authentication_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_set_the_configuration_of_an_authentication_service.setStatus(
        ""
    )

a_folder_has_been_added_into_share_configuration = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520096)
)
a_folder_has_been_added_into_share_configuration.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_folder_has_been_added_into_share_configuration.setStatus(
        ""
    )

a_folder_has_been_removed_from_share_configuration = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520097)
)
a_folder_has_been_removed_from_share_configuration.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_folder_has_been_removed_from_share_configuration.setStatus(
        ""
    )

the_share_configuration_of_a_folder_has_been_applied = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520098)
)
the_share_configuration_of_a_folder_has_been_applied.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_share_configuration_of_a_folder_has_been_applied.setStatus(
        ""
    )

failed_to_add_a_folder_into_share_configuration = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520099)
)
failed_to_add_a_folder_into_share_configuration.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_add_a_folder_into_share_configuration.setStatus(
        ""
    )

failed_to_remove_a_folder_from_share_configuration = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520100)
)
failed_to_remove_a_folder_from_share_configuration.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_remove_a_folder_from_share_configuration.setStatus(
        ""
    )

failed_to_apply_the_share_configuration_of_a_folder = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520101)
)
failed_to_apply_the_share_configuration_of_a_folder.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_apply_the_share_configuration_of_a_folder.setStatus(
        ""
    )

remote_replication_test_failed_The_target_folder_is_invalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520102)
)
remote_replication_test_failed_The_target_folder_is_invalid.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    remote_replication_test_failed_The_target_folder_is_invalid.setStatus(
        ""
    )

remote_replication_test_failed_No_response_from_remote_host = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520103)
)
remote_replication_test_failed_No_response_from_remote_host.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    remote_replication_test_failed_No_response_from_remote_host.setStatus(
        ""
    )

remote_replication_test_failed_Username_or_password_is_invalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520104)
)
remote_replication_test_failed_Username_or_password_is_invalid.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    remote_replication_test_failed_Username_or_password_is_invalid.setStatus(
        ""
    )

a_remote_replication_task_has_been_deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520105)
)
a_remote_replication_task_has_been_deleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_remote_replication_task_has_been_deleted.setStatus(
        ""
    )

failed_to_delete_a_remote_replication_task = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520106)
)
failed_to_delete_a_remote_replication_task.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_delete_a_remote_replication_task.setStatus(
        ""
    )

the_backup_operation_of_a_remote_repllication_task_has_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520107)
)
the_backup_operation_of_a_remote_repllication_task_has_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_backup_operation_of_a_remote_repllication_task_has_started.setStatus(
        ""
    )

failed_to_activate_the_backup_of_a_remote_replication_task = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520108)
)
failed_to_activate_the_backup_of_a_remote_replication_task.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_activate_the_backup_of_a_remote_replication_task.setStatus(
        ""
    )

a_remote_replication_task_has_stopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520109)
)
a_remote_replication_task_has_stopped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_remote_replication_task_has_stopped.setStatus(
        ""
    )

failed_to_stop_a_remote_replication_task = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520110)
)
failed_to_stop_a_remote_replication_task.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_stop_a_remote_replication_task.setStatus(
        ""
    )

the_restoration_of_a_remote_replication_task_has_begun = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520111)
)
the_restoration_of_a_remote_replication_task_has_begun.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_restoration_of_a_remote_replication_task_has_begun.setStatus(
        ""
    )

failed_to_restore_from_source_to_target_of_a_replication_task = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520112)
)
failed_to_restore_from_source_to_target_of_a_replication_task.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_restore_from_source_to_target_of_a_replication_task.setStatus(
        ""
    )

the_restoration_of_a_remote_replication_task_has_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520113)
)
the_restoration_of_a_remote_replication_task_has_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_restoration_of_a_remote_replication_task_has_completed.setStatus(
        ""
    )

failed_to_restore_from_target_to_source_of_a_replication_task = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520114)
)
failed_to_restore_from_target_to_source_of_a_replication_task.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_restore_from_target_to_source_of_a_replication_task.setStatus(
        ""
    )

a_remote_replication_task_has_been_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520115)
)
a_remote_replication_task_has_been_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_remote_replication_task_has_been_completed.setStatus(
        ""
    )

failed_to_replicate_from_source_to_target_of_a_replication_task = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520116)
)
failed_to_replicate_from_source_to_target_of_a_replication_task.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_replicate_from_source_to_target_of_a_replication_task.setStatus(
        ""
    )

the_target_folder_of_a_replication_has_insufficient_capacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520117)
)
the_target_folder_of_a_replication_has_insufficient_capacity.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_target_folder_of_a_replication_has_insufficient_capacity.setStatus(
        ""
    )

remote_replication_task_failed_to_start_Netowrk_timeoout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520118)
)
remote_replication_task_failed_to_start_Netowrk_timeoout.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    remote_replication_task_failed_to_start_Netowrk_timeoout.setStatus(
        ""
    )

a_remote_replication_task_has_been_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520119)
)
a_remote_replication_task_has_been_created.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_remote_replication_task_has_been_created.setStatus(
        ""
    )

failed_to_create_remote_replication_task = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520120)
)
failed_to_create_remote_replication_task.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_create_remote_replication_task.setStatus(
        ""
    )

a_schedule_has_been_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520121)
)
a_schedule_has_been_created.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_schedule_has_been_created.setStatus(
        ""
    )

failed_to_create_a_schedule = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520122)
)
failed_to_create_a_schedule.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_create_a_schedule.setStatus(
        ""
    )

a_schedule_has_been_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520123)
)
a_schedule_has_been_enabled.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_schedule_has_been_enabled.setStatus(
        ""
    )

failed_to_enable_a_schedule = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520124)
)
failed_to_enable_a_schedule.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_enable_a_schedule.setStatus(
        ""
    )

a_schedule_has_been_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520125)
)
a_schedule_has_been_disabled.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_schedule_has_been_disabled.setStatus(
        ""
    )

failed_to_disabled_a_schedule = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520126)
)
failed_to_disabled_a_schedule.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_disabled_a_schedule.setStatus(
        ""
    )

a_schedule_has_been_deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520127)
)
a_schedule_has_been_deleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_schedule_has_been_deleted.setStatus(
        ""
    )

failed_to_delete_a_schedule = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520128)
)
failed_to_delete_a_schedule.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_delete_a_schedule.setStatus(
        ""
    )

a_instance_of_a_schedule_task_is_still_running = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520129)
)
a_instance_of_a_schedule_task_is_still_running.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_instance_of_a_schedule_task_is_still_running.setStatus(
        ""
    )

a_drive_has_been_inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520130)
)
a_drive_has_been_inserted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_drive_has_been_inserted.setStatus(
        ""
    )

a_drive_has_been_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520131)
)
a_drive_has_been_unplugged.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_drive_has_been_unplugged.setStatus(
        ""
    )

a_file_system_has_been_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520132)
)
a_file_system_has_been_created.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_file_system_has_been_created.setStatus(
        ""
    )

failed_to_created_a_file_system = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520133)
)
failed_to_created_a_file_system.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_created_a_file_system.setStatus(
        ""
    )

a_file_system_has_been_deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520134)
)
a_file_system_has_been_deleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_file_system_has_been_deleted.setStatus(
        ""
    )

failed_to_delete_a_file_system = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520135)
)
failed_to_delete_a_file_system.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_delete_a_file_system.setStatus(
        ""
    )

a_folder_has_been_created_in_the_file_system = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520136)
)
a_folder_has_been_created_in_the_file_system.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_folder_has_been_created_in_the_file_system.setStatus(
        ""
    )

failed_to_a_folder_in_the_file_system = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520137)
)
failed_to_a_folder_in_the_file_system.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_a_folder_in_the_file_system.setStatus(
        ""
    )

a_folder_has_been_deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520138)
)
a_folder_has_been_deleted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_folder_has_been_deleted.setStatus(
        ""
    )

failed_to_delete_a_folder = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520139)
)
failed_to_delete_a_folder.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_delete_a_folder.setStatus(
        ""
    )

the_system_enter_single_controller_mode = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520140)
)
the_system_enter_single_controller_mode.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_system_enter_single_controller_mode.setStatus(
        ""
    )

a_controller_has_been_booted_completely = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520141)
)
a_controller_has_been_booted_completely.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_controller_has_been_booted_completely.setStatus(
        ""
    )

a_controller_can_t_be_detected_System_will_reboot_to_recovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520142)
)
a_controller_can_t_be_detected_System_will_reboot_to_recovery.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_controller_can_t_be_detected_System_will_reboot_to_recovery.setStatus(
        ""
    )

the_configuration_broken_by_power_outage_has_been_recovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520143)
)
the_configuration_broken_by_power_outage_has_been_recovered.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_configuration_broken_by_power_outage_has_been_recovered.setStatus(
        ""
    )

detected_controller_failure_Ffailover_process_will_be_launched = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520144)
)
detected_controller_failure_Ffailover_process_will_be_launched.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    detected_controller_failure_Ffailover_process_will_be_launched.setStatus(
        ""
    )

the_controller_failover_process_has_been_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520145)
)
the_controller_failover_process_has_been_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_controller_failover_process_has_been_completed.setStatus(
        ""
    )

failed_controller_recovered_Failback_process_will_be_launched = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520146)
)
failed_controller_recovered_Failback_process_will_be_launched.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_controller_recovered_Failback_process_will_be_launched.setStatus(
        ""
    )

the_controller_failback_process_has_been_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520147)
)
the_controller_failback_process_has_been_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_controller_failback_process_has_been_completed.setStatus(
        ""
    )

a_controller_has_been_unplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520148)
)
a_controller_has_been_unplugged.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_controller_has_been_unplugged.setStatus(
        ""
    )

a_controller_has_been_inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520149)
)
a_controller_has_been_inserted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_controller_has_been_inserted.setStatus(
        ""
    )

network_connection_of_a_controller_has_been_restored = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520150)
)
network_connection_of_a_controller_has_been_restored.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    network_connection_of_a_controller_has_been_restored.setStatus(
        ""
    )

netwrok_connection_of_a_controller_is_disconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520151)
)
netwrok_connection_of_a_controller_is_disconnected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    netwrok_connection_of_a_controller_is_disconnected.setStatus(
        ""
    )

a_interface_of_a_controller_from_aggregation_group_restored = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520152)
)
a_interface_of_a_controller_from_aggregation_group_restored.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_interface_of_a_controller_from_aggregation_group_restored.setStatus(
        ""
    )

a_interface_of_a_controller_from_aggregation_group_is_abnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520153)
)
a_interface_of_a_controller_from_aggregation_group_is_abnormal.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_interface_of_a_controller_from_aggregation_group_is_abnormal.setStatus(
        ""
    )

the_address_mode_of_an_interface_has_been_changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520154)
)
the_address_mode_of_an_interface_has_been_changed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_address_mode_of_an_interface_has_been_changed.setStatus(
        ""
    )

the_MTU_size_of_a_interface_has_been_changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520155)
)
the_MTU_size_of_a_interface_has_been_changed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_MTU_size_of_a_interface_has_been_changed.setStatus(
        ""
    )

a_DNS_server_has_been_added_to_the_server_list = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520156)
)
a_DNS_server_has_been_added_to_the_server_list.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_DNS_server_has_been_added_to_the_server_list.setStatus(
        ""
    )

a_DNS_server_has_been_removed_from_the_server_list = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520157)
)
a_DNS_server_has_been_removed_from_the_server_list.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_DNS_server_has_been_removed_from_the_server_list.setStatus(
        ""
    )

a_DNS_suffix_has_been_added = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520158)
)
a_DNS_suffix_has_been_added.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_DNS_suffix_has_been_added.setStatus(
        ""
    )

a_DNS_suffix_has_been_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520159)
)
a_DNS_suffix_has_been_removed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_DNS_suffix_has_been_removed.setStatus(
        ""
    )

a_port_aggregation_group_has_been_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520160)
)
a_port_aggregation_group_has_been_created.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_port_aggregation_group_has_been_created.setStatus(
        ""
    )

a_port_aggregation_group_has_been_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520161)
)
a_port_aggregation_group_has_been_removed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_port_aggregation_group_has_been_removed.setStatus(
        ""
    )

route_rule_has_been_added_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520162)
)
route_rule_has_been_added_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    route_rule_has_been_added_successfully.setStatus(
        ""
    )

route_rule_has_been_removed_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520163)
)
route_rule_has_been_removed_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    route_rule_has_been_removed_successfully.setStatus(
        ""
    )

failed_to_set_IP_configuration_on_an_interface = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520164)
)
failed_to_set_IP_configuration_on_an_interface.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_set_IP_configuration_on_an_interface.setStatus(
        ""
    )

failed_to_set_MTU_size_on_an_interface = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520165)
)
failed_to_set_MTU_size_on_an_interface.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_set_MTU_size_on_an_interface.setStatus(
        ""
    )

failed_to_add_a_DNS_server = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520166)
)
failed_to_add_a_DNS_server.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_add_a_DNS_server.setStatus(
        ""
    )

failed_to_remove_a_DNS_server = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520167)
)
failed_to_remove_a_DNS_server.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_remove_a_DNS_server.setStatus(
        ""
    )

failed_to_add_a_DNS_suffix = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520168)
)
failed_to_add_a_DNS_suffix.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_add_a_DNS_suffix.setStatus(
        ""
    )

failed_to_remove_a_DNS_suffix = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520169)
)
failed_to_remove_a_DNS_suffix.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_remove_a_DNS_suffix.setStatus(
        ""
    )

failed_to_create_a_port_aggregation_group = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520170)
)
failed_to_create_a_port_aggregation_group.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_create_a_port_aggregation_group.setStatus(
        ""
    )

failed_to_remove_a_prot_aggregation_group = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520171)
)
failed_to_remove_a_prot_aggregation_group.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_remove_a_prot_aggregation_group.setStatus(
        ""
    )

failed_to_add_an_Route_rule = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520172)
)
failed_to_add_an_Route_rule.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_add_an_Route_rule.setStatus(
        ""
    )

failed_to_remove_an_Route_rule = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520173)
)
failed_to_remove_an_Route_rule.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_remove_an_Route_rule.setStatus(
        ""
    )

the_usage_of_the_coredump_folder_is_over_90_percent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520174)
)
the_usage_of_the_coredump_folder_is_over_90_percent.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_usage_of_the_coredump_folder_is_over_90_percent.setStatus(
        ""
    )

the_space_used_by_a_folder_has_exceeded_monitoring_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520175)
)
the_space_used_by_a_folder_has_exceeded_monitoring_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_space_used_by_a_folder_has_exceeded_monitoring_threshold.setStatus(
        ""
    )

the_ipblock_configuration_has_been_applied_on_a_controller = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520176)
)
the_ipblock_configuration_has_been_applied_on_a_controller.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_ipblock_configuration_has_been_applied_on_a_controller.setStatus(
        ""
    )

failed_to_apply_the_ipblock_configuration_on_a_controller = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520177)
)
failed_to_apply_the_ipblock_configuration_on_a_controller.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_apply_the_ipblock_configuration_on_a_controller.setStatus(
        ""
    )

a_IP_address_has_been_removed_on_a_controller = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520178)
)
a_IP_address_has_been_removed_on_a_controller.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_IP_address_has_been_removed_on_a_controller.setStatus(
        ""
    )

failed_to_remove_a_IP_address_from_ipblock_configuration = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520179)
)
failed_to_remove_a_IP_address_from_ipblock_configuration.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_remove_a_IP_address_from_ipblock_configuration.setStatus(
        ""
    )

a_IP_address_was_lbocked_The_maximum_login_attempts_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520180)
)
a_IP_address_was_lbocked_The_maximum_login_attempts_exceeded.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_IP_address_was_lbocked_The_maximum_login_attempts_exceeded.setStatus(
        ""
    )

failed_to_ban_a_IP_address_on_a_controller = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520181)
)
failed_to_ban_a_IP_address_on_a_controller.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_ban_a_IP_address_on_a_controller.setStatus(
        ""
    )

detect_a_IP_address_has_been_banned_by_system_on_a_controller = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520182)
)
detect_a_IP_address_has_been_banned_by_system_on_a_controller.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    detect_a_IP_address_has_been_banned_by_system_on_a_controller.setStatus(
        ""
    )

a_schedule_task_has_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520183)
)
a_schedule_task_has_started.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_schedule_task_has_started.setStatus(
        ""
    )

failed_to_start_a_schedule_task = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520184)
)
failed_to_start_a_schedule_task.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_start_a_schedule_task.setStatus(
        ""
    )

failed_to_restore_the_whitelist_or_blacklist = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520185)
)
failed_to_restore_the_whitelist_or_blacklist.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_restore_the_whitelist_or_blacklist.setStatus(
        ""
    )

a_user_failed_to_log_in_from_a_IP_address = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520186)
)
a_user_failed_to_log_in_from_a_IP_address.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_user_failed_to_log_in_from_a_IP_address.setStatus(
        ""
    )

the_LDAP_server_failed_to_add_a_user_from_the_CSV_file = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520187)
)
the_LDAP_server_failed_to_add_a_user_from_the_CSV_file.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_LDAP_server_failed_to_add_a_user_from_the_CSV_file.setStatus(
        ""
    )

a_user_has_nearly_reached_the_quota_limit_on_a_volume = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520188)
)
a_user_has_nearly_reached_the_quota_limit_on_a_volume.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_user_has_nearly_reached_the_quota_limit_on_a_volume.setStatus(
        ""
    )

the_LDAP_server_failed_to_add_users_in_batch_mode = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520189)
)
the_LDAP_server_failed_to_add_users_in_batch_mode.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_LDAP_server_failed_to_add_users_in_batch_mode.setStatus(
        ""
    )

the_AD_or_LDAP_server_has_been_disconnected_from_a_controller = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520190)
)
the_AD_or_LDAP_server_has_been_disconnected_from_a_controller.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_AD_or_LDAP_server_has_been_disconnected_from_a_controller.setStatus(
        ""
    )

the_AD_or_LDAP_server_connection_to_controller_has_been_restored = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520191)
)
the_AD_or_LDAP_server_connection_to_controller_has_been_restored.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_AD_or_LDAP_server_connection_to_controller_has_been_restored.setStatus(
        ""
    )

all_volumes_have_been_deactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520192)
)
all_volumes_have_been_deactivated.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    all_volumes_have_been_deactivated.setStatus(
        ""
    )

all_volumes_have_been_reactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520193)
)
all_volumes_have_been_reactivated.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    all_volumes_have_been_reactivated.setStatus(
        ""
    )

a_service_port_setting_has_conflict_with_another_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520194)
)
a_service_port_setting_has_conflict_with_another_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_service_port_setting_has_conflict_with_another_service.setStatus(
        ""
    )

an_application_server_has_been_started_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520195)
)
an_application_server_has_been_started_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    an_application_server_has_been_started_successfully.setStatus(
        ""
    )

an_application_server_has_been_restarted_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520196)
)
an_application_server_has_been_restarted_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    an_application_server_has_been_restarted_successfully.setStatus(
        ""
    )

an_application_server_has_been_stopped_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520197)
)
an_application_server_has_been_stopped_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    an_application_server_has_been_stopped_successfully.setStatus(
        ""
    )

an_application_server_has_been_configured_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520198)
)
an_application_server_has_been_configured_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    an_application_server_has_been_configured_successfully.setStatus(
        ""
    )

failed_to_start_an_application_server = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520199)
)
failed_to_start_an_application_server.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_start_an_application_server.setStatus(
        ""
    )

failed_to_restart_an_application_server = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520200)
)
failed_to_restart_an_application_server.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_restart_an_application_server.setStatus(
        ""
    )

failed_to_stop_an_application_server = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520201)
)
failed_to_stop_an_application_server.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_stop_an_application_server.setStatus(
        ""
    )

failed_to_configure_an_application_server = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520202)
)
failed_to_configure_an_application_server.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_configure_an_application_server.setStatus(
        ""
    )

app_server_stopped_Folder_for_saving_data_can_not_be_accessed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520203)
)
app_server_stopped_Folder_for_saving_data_can_not_be_accessed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    app_server_stopped_Folder_for_saving_data_can_not_be_accessed.setStatus(
        ""
    )

failed_to_backup_LDAP_DB_Folder_for_data_can_not_be_accessed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520204)
)
failed_to_backup_LDAP_DB_Folder_for_data_can_not_be_accessed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_backup_LDAP_DB_Folder_for_data_can_not_be_accessed.setStatus(
        ""
    )

failed_to_backup_LDAP_DB_Folder_may_assigned_to_sec_controller = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520205)
)
failed_to_backup_LDAP_DB_Folder_may_assigned_to_sec_controller.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_backup_LDAP_DB_Folder_may_assigned_to_sec_controller.setStatus(
        ""
    )

syncCloud_service_started_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520206)
)
syncCloud_service_started_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    syncCloud_service_started_successfully.setStatus(
        ""
    )

failed_to_start_SyncCloud_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520207)
)
failed_to_start_SyncCloud_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_start_SyncCloud_service.setStatus(
        ""
    )

syncCloud_service_stopped_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520208)
)
syncCloud_service_stopped_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    syncCloud_service_stopped_successfully.setStatus(
        ""
    )

failed_to_stop_SyncCloud_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520209)
)
failed_to_stop_SyncCloud_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_stop_SyncCloud_service.setStatus(
        ""
    )

failed_to_fetch_SyncCloud_database_Service_has_been_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520210)
)
failed_to_fetch_SyncCloud_database_Service_has_been_disabled.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_fetch_SyncCloud_database_Service_has_been_disabled.setStatus(
        ""
    )

a_volume_has_duplicated_name_for_file_service_cannot_be_mounted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520211)
)
a_volume_has_duplicated_name_for_file_service_cannot_be_mounted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    a_volume_has_duplicated_name_for_file_service_cannot_be_mounted.setStatus(
        ""
    )

the_size_of_a_folder_has_exceeded_the_quota_alert_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520212)
)
the_size_of_a_folder_has_exceeded_the_quota_alert_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_size_of_a_folder_has_exceeded_the_quota_alert_threshold.setStatus(
        ""
    )

ipv4_address_conflict_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520213)
)
ipv4_address_conflict_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ipv4_address_conflict_detected.setStatus(
        ""
    )

ipv6_address_conflict_detected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520214)
)
ipv6_address_conflict_detected.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ipv6_address_conflict_detected.setStatus(
        ""
    )

failed_to_initialize_the_SyncCloud_database = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520215)
)
failed_to_initialize_the_SyncCloud_database.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_initialize_the_SyncCloud_database.setStatus(
        ""
    )

the_SyncCloud_task_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520216)
)
the_SyncCloud_task_failed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_SyncCloud_task_failed.setStatus(
        ""
    )

file_system_usage_exceeds_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520217)
)
file_system_usage_exceeds_threshold.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    file_system_usage_exceeds_threshold.setStatus(
        ""
    )

file_system_usage_exceeds_90_percent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520218)
)
file_system_usage_exceeds_90_percent.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    file_system_usage_exceeds_90_percent.setStatus(
        ""
    )

the_file_system_of_the_volume_has_been_repaired = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520219)
)
the_file_system_of_the_volume_has_been_repaired.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_file_system_of_the_volume_has_been_repaired.setStatus(
        ""
    )

failed_to_repair_the_file_system_of_the_volume = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520220)
)
failed_to_repair_the_file_system_of_the_volume.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_repair_the_file_system_of_the_volume.setStatus(
        ""
    )

failed_to_upgrade_the_LDAP_server_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520221)
)
failed_to_upgrade_the_LDAP_server_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_upgrade_the_LDAP_server_service.setStatus(
        ""
    )

the_LDAP_server_service_has_been_upgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520222)
)
the_LDAP_server_service_has_been_upgraded.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_LDAP_server_service_has_been_upgraded.setStatus(
        ""
    )

ldap_server_has_been_disabled_Folder_for_data_is_not_found = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520223)
)
ldap_server_has_been_disabled_Folder_for_data_is_not_found.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ldap_server_has_been_disabled_Folder_for_data_is_not_found.setStatus(
        ""
    )

ldap_server_has_been_disabled_The_settings_are_incomplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520224)
)
ldap_server_has_been_disabled_The_settings_are_incomplete.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ldap_server_has_been_disabled_The_settings_are_incomplete.setStatus(
        ""
    )

ldap_server_has_been_disabled_The_database_was_corrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520225)
)
ldap_server_has_been_disabled_The_database_was_corrupted.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ldap_server_has_been_disabled_The_database_was_corrupted.setStatus(
        ""
    )

failed_to_connect_to_AD_server_Incorrect_username_or_password = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520226)
)
failed_to_connect_to_AD_server_Incorrect_username_or_password.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_connect_to_AD_server_Incorrect_username_or_password.setStatus(
        ""
    )

failed_to_connect_to_AD_server_KDC_server_is_not_found = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520227)
)
failed_to_connect_to_AD_server_KDC_server_is_not_found.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_connect_to_AD_server_KDC_server_is_not_found.setStatus(
        ""
    )

the_AD_server_is_unreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520228)
)
the_AD_server_is_unreachable.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_AD_server_is_unreachable.setStatus(
        ""
    )

not_enough_privilege_for_the_AD_user_to_join_the_domain = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520229)
)
not_enough_privilege_for_the_AD_user_to_join_the_domain.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    not_enough_privilege_for_the_AD_user_to_join_the_domain.setStatus(
        ""
    )

failed_to_connect_LDAP_server_Incorrect_username_or_password = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520230)
)
failed_to_connect_LDAP_server_Incorrect_username_or_password.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_connect_LDAP_server_Incorrect_username_or_password.setStatus(
        ""
    )

the_LDAP_server_is_unreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520232)
)
the_LDAP_server_is_unreachable.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_LDAP_server_is_unreachable.setStatus(
        ""
    )

failed_to_connect_to_the_LDAP_server_The_base_DN_is_incorrect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520233)
)
failed_to_connect_to_the_LDAP_server_The_base_DN_is_incorrect.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_connect_to_the_LDAP_server_The_base_DN_is_incorrect.setStatus(
        ""
    )

cloud_sync_service_started_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520234)
)
cloud_sync_service_started_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    cloud_sync_service_started_successfully.setStatus(
        ""
    )

failed_to_start_cloud_sync_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520235)
)
failed_to_start_cloud_sync_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_start_cloud_sync_service.setStatus(
        ""
    )

cloud_sync_service_stopped_successfully = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520236)
)
cloud_sync_service_stopped_successfully.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    cloud_sync_service_stopped_successfully.setStatus(
        ""
    )

failed_to_stop_cloud_sync_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520237)
)
failed_to_stop_cloud_sync_service.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_stop_cloud_sync_service.setStatus(
        ""
    )

failed_to_fetch_cloud_sync_database_service_has_been_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520238)
)
failed_to_fetch_cloud_sync_database_service_has_been_disabled.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_fetch_cloud_sync_database_service_has_been_disabled.setStatus(
        ""
    )

failed_to_initial_the_cloud_sync_database = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520239)
)
failed_to_initial_the_cloud_sync_database.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_initial_the_cloud_sync_database.setStatus(
        ""
    )

the_cloud_sync_task_failed_due_to_network_problems = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520240)
)
the_cloud_sync_task_failed_due_to_network_problems.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_cloud_sync_task_failed_due_to_network_problems.setStatus(
        ""
    )

the_antivirus_scan_job_has_been_stopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520241)
)
the_antivirus_scan_job_has_been_stopped.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_antivirus_scan_job_has_been_stopped.setStatus(
        ""
    )

the_antivirus_scheduled_scan_job_has_been_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520242)
)
the_antivirus_scheduled_scan_job_has_been_completed.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_antivirus_scheduled_scan_job_has_been_completed.setStatus(
        ""
    )

the_NVR_server_crash_detected_Recovery_process_will_be_start = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520243)
)
the_NVR_server_crash_detected_Recovery_process_will_be_start.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_NVR_server_crash_detected_Recovery_process_will_be_start.setStatus(
        ""
    )

the_NVR_server_has_been_recovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520244)
)
the_NVR_server_has_been_recovered.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    the_NVR_server_has_been_recovered.setStatus(
        ""
    )

failed_to_recover_the_NVR_server = NotificationType(
    (1, 3, 6, 1, 4, 1, 1714, 1, 8000, 0, 1090520245)
)
failed_to_recover_the_NVR_server.setObjects(
    ("IFT-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    failed_to_recover_the_NVR_server.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IFT-SNMP-MIB",
    **{"infortrend": infortrend,
       "raid": raid,
       "extInterface": extInterface,
       "ctlrConfiguration": ctlrConfiguration,
       "sysInformation": sysInformation,
       "cpuType": cpuType,
       "cacheSize": cacheSize,
       "memoryType": memoryType,
       "fwMajorVersion": fwMajorVersion,
       "fwMinorVersion": fwMinorVersion,
       "fwEngineerVersion": fwEngineerVersion,
       "brMajorVersion": brMajorVersion,
       "brMinorVersion": brMinorVersion,
       "brEngineerVersion": brEngineerVersion,
       "serialNum": serialNum,
       "ctlrName": ctlrName,
       "ctlrCfgModeFlags": ctlrCfgModeFlags,
       "privateLogoString": privateLogoString,
       "privateLogoVendor": privateLogoVendor,
       "privateLogoModel": privateLogoModel,
       "ctlrUniqueID": ctlrUniqueID,
       "serialNumSec": serialNumSec,
       "cachingParams": cachingParams,
       "cacheModeFlags": cacheModeFlags,
       "cacheBlkSizeIdx": cacheBlkSizeIdx,
       "cacheTotal": cacheTotal,
       "cacheDirty": cacheDirty,
       "diskArrayParams": diskArrayParams,
       "maxRebPriorityIdx": maxRebPriorityIdx,
       "minRebPriorityIdx": minRebPriorityIdx,
       "defRebPriorityIdx": defRebPriorityIdx,
       "curRebPriorityIdx": curRebPriorityIdx,
       "writeVerifyModeFlags": writeVerifyModeFlags,
       "hostSideParams": hostSideParams,
       "maxQueuedIOCnt": maxQueuedIOCnt,
       "minQueuedIOCnt": minQueuedIOCnt,
       "defQueuedIOCnt": defQueuedIOCnt,
       "curQueuedIOCnt": curQueuedIOCnt,
       "maxLunNum": maxLunNum,
       "minLunNum": minLunNum,
       "defLunNum": defLunNum,
       "curLunNum": curLunNum,
       "curReadStatistic": curReadStatistic,
       "curWriteStatistic": curWriteStatistic,
       "curReadRequests": curReadRequests,
       "curWriteRequests": curWriteRequests,
       "driveSideParams": driveSideParams,
       "modeFlags": modeFlags,
       "maxAccessDelayTime": maxAccessDelayTime,
       "minAccessDelayTime": minAccessDelayTime,
       "defAccessDelayTime": defAccessDelayTime,
       "curAccessDelayTime": curAccessDelayTime,
       "maxTagCnt": maxTagCnt,
       "minTagCnt": minTagCnt,
       "defTagCnt": defTagCnt,
       "curTagCnt": curTagCnt,
       "defIOTimeout": defIOTimeout,
       "curIOTimeout": curIOTimeout,
       "defDrvChkPeriod": defDrvChkPeriod,
       "curDrvChkPeriod": curDrvChkPeriod,
       "defSaftePollingPeriod": defSaftePollingPeriod,
       "curSaftePollingPeriod": curSaftePollingPeriod,
       "defAutoDetectPeriod": defAutoDetectPeriod,
       "curAutoDetectPeriod": curAutoDetectPeriod,
       "redundantParams": redundantParams,
       "redCtlrCfg": redCtlrCfg,
       "redCtlrModeFlags": redCtlrModeFlags,
       "redCtlrCommType": redCtlrCommType,
       "redCtlrStatus": redCtlrStatus,
       "ldTable": ldTable,
       "ldEntry": ldEntry,
       "ldIndex": ldIndex,
       "ldID": ldID,
       "ldSize": ldSize,
       "ldBlkSizeIdx": ldBlkSizeIdx,
       "ldOpModes": ldOpModes,
       "ldStatus": ldStatus,
       "ldState": ldState,
       "ldTotalDrvCnt": ldTotalDrvCnt,
       "ldOnlineDrvCnt": ldOnlineDrvCnt,
       "ldSpareDrvCnt": ldSpareDrvCnt,
       "ldFailedDrvCnt": ldFailedDrvCnt,
       "ldReadStatistic": ldReadStatistic,
       "ldWriteStatistic": ldWriteStatistic,
       "ldReadLatency": ldReadLatency,
       "ldWriteLatency": ldWriteLatency,
       "lvTable": lvTable,
       "lvEntry": lvEntry,
       "lvIndex": lvIndex,
       "lvID": lvID,
       "lvSize": lvSize,
       "lvBlkSizeIdx": lvBlkSizeIdx,
       "lvOpModes": lvOpModes,
       "lvLdCount": lvLdCount,
       "lvLdList": lvLdList,
       "partTable": partTable,
       "partEntry": partEntry,
       "partIndex": partIndex,
       "partLdLvID": partLdLvID,
       "partOffset": partOffset,
       "partSize": partSize,
       "lunTable": lunTable,
       "lunEntry": lunEntry,
       "lunIndex": lunIndex,
       "lunChl": lunChl,
       "lunID": lunID,
       "lunNum": lunNum,
       "lunLdLvID": lunLdLvID,
       "lunPartIdx": lunPartIdx,
       "lunSsSiID": lunSsSiID,
       "hddTable": hddTable,
       "hddEntry": hddEntry,
       "hddIndex": hddIndex,
       "hddLogChlNum": hddLogChlNum,
       "hddPhyChlNum": hddPhyChlNum,
       "hddScsiId": hddScsiId,
       "hddScsiLun": hddScsiLun,
       "hddLdId": hddLdId,
       "hddSize": hddSize,
       "hddBlkSizeIdx": hddBlkSizeIdx,
       "hddSpeed": hddSpeed,
       "hddDataWidth": hddDataWidth,
       "hddStatus": hddStatus,
       "hddState": hddState,
       "hddSlotNum": hddSlotNum,
       "hddResvSpace": hddResvSpace,
       "hddModelStr": hddModelStr,
       "hddFwRevStr": hddFwRevStr,
       "hddSerialNum": hddSerialNum,
       "hddReadStatistic": hddReadStatistic,
       "hddWriteStatistic": hddWriteStatistic,
       "hddSmart1": hddSmart1,
       "hddSmart2": hddSmart2,
       "hddSmart3": hddSmart3,
       "hddSmart4": hddSmart4,
       "hddSmart5": hddSmart5,
       "hddSmart6": hddSmart6,
       "hddSmart7": hddSmart7,
       "hddSmart8": hddSmart8,
       "hddSmart9": hddSmart9,
       "hddSmart10": hddSmart10,
       "hddSmart11": hddSmart11,
       "hddSmart12": hddSmart12,
       "hddSmart13": hddSmart13,
       "hddSmart14": hddSmart14,
       "hddSmart15": hddSmart15,
       "hddSmart16": hddSmart16,
       "hddSmart17": hddSmart17,
       "hddSmart18": hddSmart18,
       "hddSmart19": hddSmart19,
       "hddSmart20": hddSmart20,
       "hddSmart21": hddSmart21,
       "hddSmart22": hddSmart22,
       "hddSmart23": hddSmart23,
       "hddSmart24": hddSmart24,
       "hddSmart25": hddSmart25,
       "hddSmart26": hddSmart26,
       "hddSmart27": hddSmart27,
       "hddSmart28": hddSmart28,
       "hddSmart29": hddSmart29,
       "hddSmart30": hddSmart30,
       "hddWearLife": hddWearLife,
       "hddReadLatency": hddReadLatency,
       "hddWriteLatency": hddWriteLatency,
       "chlTable": chlTable,
       "chlEntry": chlEntry,
       "chlIndex": chlIndex,
       "chlLogChlNum": chlLogChlNum,
       "chlPhyChlNum": chlPhyChlNum,
       "chlType": chlType,
       "chlChipType": chlChipType,
       "chlMaxSupId": chlMaxSupId,
       "chlMaxSupLun": chlMaxSupLun,
       "chlMode": chlMode,
       "chlScsiIdBitmap": chlScsiIdBitmap,
       "chlFibreIdBase": chlFibreIdBase,
       "chlHostIdBitmap": chlHostIdBitmap,
       "chlDrvPid": chlDrvPid,
       "chlDrvSid": chlDrvSid,
       "chlMaxTxPeriod": chlMaxTxPeriod,
       "chlMinTxPeriod": chlMinTxPeriod,
       "chlDefTxPeriod": chlDefTxPeriod,
       "chlCurTxPeriod": chlCurTxPeriod,
       "chlMaxTxWidth": chlMaxTxWidth,
       "chlMinTxWidth": chlMinTxWidth,
       "chlDefTxWidth": chlDefTxWidth,
       "chlCurTxWidth": chlCurTxWidth,
       "chlMaxTagCnt": chlMaxTagCnt,
       "chlDefTagCnt": chlDefTagCnt,
       "chlReadStatistic": chlReadStatistic,
       "chlWriteStatistic": chlWriteStatistic,
       "chlReadRequests": chlReadRequests,
       "chlWriteRequests": chlWriteRequests,
       "luTable": luTable,
       "luEntry": luEntry,
       "luIndex": luIndex,
       "luDescriptor": luDescriptor,
       "luClassCode": luClassCode,
       "luTypeCode": luTypeCode,
       "luVendorID": luVendorID,
       "luIDString": luIDString,
       "luHWRev": luHWRev,
       "luSWRev": luSWRev,
       "luChlNum": luChlNum,
       "luIDNum": luIDNum,
       "luDevTable": luDevTable,
       "luDevEntry": luDevEntry,
       "luDevTabIdx": luDevTabIdx,
       "luDeviceDescriptor": luDeviceDescriptor,
       "luDeviceClassCode": luDeviceClassCode,
       "luDeviceTypeCode": luDeviceTypeCode,
       "luDevDescriptor": luDevDescriptor,
       "luDevTypeCode": luDevTypeCode,
       "luDevIndex": luDevIndex,
       "luDevDescription": luDevDescription,
       "luDevValue": luDevValue,
       "luDevValueUnit": luDevValueUnit,
       "luDevChlNum": luDevChlNum,
       "luDevIDNum": luDevIDNum,
       "luDevStatus": luDevStatus,
       "extLunTable": extLunTable,
       "extLunEntry": extLunEntry,
       "extLunIndex": extLunIndex,
       "extLunGroupName": extLunGroupName,
       "extLunHostIDWWN": extLunHostIDWWN,
       "extLunChl": extLunChl,
       "extLunID": extLunID,
       "extLunNum": extLunNum,
       "extLunLdLvID": extLunLdLvID,
       "extLunPartIdx": extLunPartIdx,
       "extLunSsSiID": extLunSsSiID,
       "extLunHostIDMask": extLunHostIDMask,
       "extLunFilterType": extLunFilterType,
       "extLunAccessMode": extLunAccessMode,
       "eventLog": eventLog,
       "allEvtTable": allEvtTable,
       "allEvtEntry": allEvtEntry,
       "evtTableIdx": evtTableIdx,
       "evtSource": evtSource,
       "evtSeverity": evtSeverity,
       "evtIndex": evtIndex,
       "evtType": evtType,
       "evtCode": evtCode,
       "evtTime": evtTime,
       "ctlrEvtTable": ctlrEvtTable,
       "ctlrEvtEntry": ctlrEvtEntry,
       "cevtTableIdx": cevtTableIdx,
       "cevtSource": cevtSource,
       "cevtSeverity": cevtSeverity,
       "cevtIndex": cevtIndex,
       "cevtType": cevtType,
       "cevtCode": cevtCode,
       "cevtTime": cevtTime,
       "drvEvtTable": drvEvtTable,
       "drvEvtEntry": drvEvtEntry,
       "devtTableIdx": devtTableIdx,
       "devtSource": devtSource,
       "devtSeverity": devtSeverity,
       "devtIndex": devtIndex,
       "devtType": devtType,
       "devtCode": devtCode,
       "evtLdID": evtLdID,
       "evtLogChl": evtLogChl,
       "evtID": evtID,
       "evtLun": evtLun,
       "devtTime": devtTime,
       "hostEvtTable": hostEvtTable,
       "hostEvtEntry": hostEvtEntry,
       "hevtTableIdx": hevtTableIdx,
       "hevtSource": hevtSource,
       "hevtSeverity": hevtSeverity,
       "hevtIndex": hevtIndex,
       "hevtType": hevtType,
       "hevtCode": hevtCode,
       "evtChl": evtChl,
       "hevtID": hevtID,
       "hevtLun": hevtLun,
       "hevtTime": hevtTime,
       "ldEvtTable": ldEvtTable,
       "ldEvtEntry": ldEvtEntry,
       "ldevtTableIdx": ldevtTableIdx,
       "ldevtSource": ldevtSource,
       "ldevtSeverity": ldevtSeverity,
       "ldevtIndex": ldevtIndex,
       "ldevtType": ldevtType,
       "ldevtCode": ldevtCode,
       "ldevtLdID": ldevtLdID,
       "evtFailedChl": evtFailedChl,
       "evtFailedID": evtFailedID,
       "evtFailedLun": evtFailedLun,
       "ldevtTime": ldevtTime,
       "gtEvtTable": gtEvtTable,
       "gtEvtEntry": gtEvtEntry,
       "gtevtTableIdx": gtevtTableIdx,
       "gtevtSource": gtevtSource,
       "gtevtSeverity": gtevtSeverity,
       "gtevtIndex": gtevtIndex,
       "gtevtType": gtevtType,
       "evtLuDesc": evtLuDesc,
       "evtLuDevDesc": evtLuDevDesc,
       "evtLuClass": evtLuClass,
       "evtLuSubClass": evtLuSubClass,
       "gtevtCode": gtevtCode,
       "evtLuDevType": evtLuDevType,
       "evtLuDevIdx": evtLuDevIdx,
       "evtEncChl": evtEncChl,
       "evtEncID": evtEncID,
       "evtEncLun": evtEncLun,
       "gtevtTime": gtevtTime,
       "event": event,
       "controller-memory-error-detected": controller_memory_error_detected,
       "memory-ECC-single-bit-error-has-been-corrected-in-DIMM-module": memory_ECC_single_bit_error_has_been_corrected_in_DIMM_module,
       "inconsistent-board-ID-between-the-controllers-has-been-found": inconsistent_board_ID_between_the_controllers_has_been_found,
       "inconsistent-board-rev-number-between-the-controllers": inconsistent_board_rev_number_between_the_controllers,
       "invalid-hardware-settings-have-been-detected": invalid_hardware_settings_have_been_detected,
       "inconsistent-HW-setting-ID-between-the-controllers": inconsistent_HW_setting_ID_between_the_controllers,
       "inconsistent-host-board-1-HW-setting-ID-between-the-controllers": inconsistent_host_board_1_HW_setting_ID_between_the_controllers,
       "inconsistent-host-board-2-HW-setting-ID-between-the-controllers": inconsistent_host_board_2_HW_setting_ID_between_the_controllers,
       "inconsistent-DRAM-size-between-the-controllers-has-been-found": inconsistent_DRAM_size_between_the_controllers_has_been_found,
       "inconsistent-NVRAM-size-between-the-controllers-has-been-found": inconsistent_NVRAM_size_between_the_controllers_has_been_found,
       "inconsistent-hostboard-3-HW-setting-ID-between-the-controllers": inconsistent_hostboard_3_HW_setting_ID_between_the_controllers,
       "inconsistent-hostboard-4-HW-setting-ID-between-the-controllers": inconsistent_hostboard_4_HW_setting_ID_between_the_controllers,
       "inconsistent-hostboard-5-HW-setting-ID-between-the-controllers": inconsistent_hostboard_5_HW_setting_ID_between_the_controllers,
       "inconsistent-hostboard-6-HW-setting-ID-between-the-controllers": inconsistent_hostboard_6_HW_setting_ID_between_the_controllers,
       "inconsistent-hostboard-7-HW-setting-ID-between-the-controllers": inconsistent_hostboard_7_HW_setting_ID_between_the_controllers,
       "inconsistent-hostboard-8-HW-setting-ID-between-the-controllers": inconsistent_hostboard_8_HW_setting_ID_between_the_controllers,
       "inconsistent-hostboard-9-HW-setting-ID-between-the-controllers": inconsistent_hostboard_9_HW_setting_ID_between_the_controllers,
       "inconsistent-hostboard-10-HW-setting-ID-between-the-controllers": inconsistent_hostboard_10_HW_setting_ID_between_the_controllers,
       "a-non-supported-host-board-has-been-installed": a_non_supported_host_board_has_been_installed,
       "the-secondary-controller-is-incompatible": the_secondary_controller_is_incompatible,
       "the-fatal-failed-LD-contains-unsaved-write-cache-data": the_fatal_failed_LD_contains_unsaved_write_cache_data,
       "the-memory-size-of-the-secondary-controller-is-inconsistent": the_memory_size_of_the_secondary_controller_is_inconsistent,
       "the-secondary-controller-is-waiting-for-write-cache-recovery": the_secondary_controller_is_waiting_for_write_cache_recovery,
       "the-secondary-controller-with-cache-data-is-not-for-the-device": the_secondary_controller_with_cache_data_is_not_for_the_device,
       "the-firmware-of-the-secondary-controller-is-incompatible": the_firmware_of_the_secondary_controller_is_incompatible,
       "cache-memory-range-of-the-secondary-controller-is-incompatible": cache_memory_range_of_the_secondary_controller_is_incompatible,
       "redundant-controller-failure-or-shutdown-was-detected": redundant_controller_failure_or_shutdown_was_detected,
       "redundant-controller-has-shut-down": redundant_controller_has_shut_down,
       "controller-had-a-hardware-error-and-failed": controller_had_a_hardware_error_and_failed,
       "redundant-controller-firmware-updated": redundant_controller_firmware_updated,
       "the-controller-write-policy-was-forced-to-write-through-mode": the_controller_write_policy_was_forced_to_write_through_mode,
       "controller-initialization-completed": controller_initialization_completed,
       "controller-slot-B-booted-as-primary-controller": controller_slot_B_booted_as_primary_controller,
       "firmware-synchronization-started": firmware_synchronization_started,
       "firmware-synchronization-completed": firmware_synchronization_completed,
       "controller-NVRAM-factory-default-settings-restored": controller_NVRAM_factory_default_settings_restored,
       "the-device-password-has-been-reset": the_device_password_has_been_reset,
       "controller-NVRAM-restore-from-file-completed": controller_NVRAM_restore_from_file_completed,
       "controller-NVRAM-restore-from-drive-completed": controller_NVRAM_restore_from_drive_completed,
       "cache-data-present-during-system-power-on": cache_data_present_during_system_power_on,
       "the-controller-write-policy-default-setting-was-restored": the_controller_write_policy_default_setting_was_restored,
       "controller-shutdown-started": controller_shutdown_started,
       "controller-shutdown-completed": controller_shutdown_completed,
       "enclosure-drawer-is-opened": enclosure_drawer_is_opened,
       "expansion-enclosure-drawer-is-opened": expansion_enclosure_drawer_is_opened,
       "enclosure-drawer-is-not-detected": enclosure_drawer_is_not_detected,
       "expansion-enclosure-drawer-is-not-ready-has-been-detected": expansion_enclosure_drawer_is_not_ready_has_been_detected,
       "invalid-or-conflicting-enclosure-ID-detected": invalid_or_conflicting_enclosure_ID_detected,
       "enclosure-drive-configuration-error-detected": enclosure_drive_configuration_error_detected,
       "expansion-enclosure-drive-configuration-error-detected": expansion_enclosure_drive_configuration_error_detected,
       "expansion-enclosure-is-not-supported": expansion_enclosure_is_not_supported,
       "enclosure-drawer-is-closed": enclosure_drawer_is_closed,
       "expansion-enclosure-drawer-is-closed": expansion_enclosure_drawer_is_closed,
       "enclosure-drawer-back-is-to-normal": enclosure_drawer_back_is_to_normal,
       "expansion-enclosure-drawer-is-back-to-normal": expansion_enclosure_drawer_is_back_to_normal,
       "power-supply-voltage-3-3V-is-lower-than-lower-threshold": power_supply_voltage_3_3V_is_lower_than_lower_threshold,
       "power-supply-voltage-5V-is-lower-than-lower-threshold": power_supply_voltage_5V_is_lower_than_lower_threshold,
       "power-supply-voltage-12V-is-lower-than-lower-threshold": power_supply_voltage_12V_is_lower_than_lower_threshold,
       "power-supply-voltage-3-3V-is-higher-than-upper-threshold": power_supply_voltage_3_3V_is_higher_than_upper_threshold,
       "power-supply-voltage-5V-is-higher-than-upper-threshold": power_supply_voltage_5V_is_higher_than_upper_threshold,
       "power-supply-voltage-12V-is-higher-than-upper-threshold": power_supply_voltage_12V_is_higher_than_upper_threshold,
       "enclosure-power-supply-sensor-detection-failed": enclosure_power_supply_sensor_detection_failed,
       "power-supply-in-JBOD-failed-has-been-detected": power_supply_in_JBOD_failed_has_been_detected,
       "power-supply-in-storage-system-failed-has-been-detected": power_supply_in_storage_system_failed_has_been_detected,
       "expansion-enclosure-power-supply-is-absent": expansion_enclosure_power_supply_is_absent,
       "power-supply-in-storage-system-is-missing": power_supply_in_storage_system_is_missing,
       "expansion-enclosure-power-supply-absent": expansion_enclosure_power_supply_absent,
       "expansion-enclosure-power-supply-failed": expansion_enclosure_power_supply_failed,
       "psu-voltage-3-3V-is-back-to-normal-and-below-upper-threshold": psu_voltage_3_3V_is_back_to_normal_and_below_upper_threshold,
       "psu-voltage-5V-is-back-to-normal-and-below-upper-threshold": psu_voltage_5V_is_back_to_normal_and_below_upper_threshold,
       "psu-voltage-12V-is-back-to-normal-and-below-upper-threshold": psu_voltage_12V_is_back_to_normal_and_below_upper_threshold,
       "psu-voltage-3-3V-is-back-to-normal-and-above-lower-threshold": psu_voltage_3_3V_is_back_to_normal_and_above_lower_threshold,
       "psu-voltage-5V-is-back-to-normal-and-above-lower-threshold": psu_voltage_5V_is_back_to_normal_and_above_lower_threshold,
       "psu-voltage-12V-is-back-to-normal-and-above-lower-threshold": psu_voltage_12V_is_back_to_normal_and_above_lower_threshold,
       "enclosure-power-supply-sensor-back-to-normal": enclosure_power_supply_sensor_back_to_normal,
       "expansion-enclosure-PSU-failed-status-recovered-to-on-line": expansion_enclosure_PSU_failed_status_recovered_to_on_line,
       "enclosure-PSU-failed-status-recovered-to-normal": enclosure_PSU_failed_status_recovered_to_normal,
       "expansion-enclosure-PSU-absent-status-recovered-to-present": expansion_enclosure_PSU_absent_status_recovered_to_present,
       "enclosure-PSU-absent-status-recovered-to-normal": enclosure_PSU_absent_status_recovered_to_normal,
       "expansion-enclosure-power-supply-back-to-on-line": expansion_enclosure_power_supply_back_to_on_line,
       "controller-flash-backup-module-FBM-absent": controller_flash_backup_module_FBM_absent,
       "flash-Backup-Module-FBM-failed": flash_Backup_Module_FBM_failed,
       "battery-Backup-Unit-BBU-is-missing": battery_Backup_Unit_BBU_is_missing,
       "battery-Backup-Unit-BBU-failed": battery_Backup_Unit_BBU_failed,
       "controller-battery-backup-unit-BBU-charging": controller_battery_backup_unit_BBU_charging,
       "battery-Backup-Unit-BBU-error-is-detected": battery_Backup_Unit_BBU_error_is_detected,
       "super-capacitor-is-missing": super_capacitor_is_missing,
       "super-capacitor-failed": super_capacitor_failed,
       "controller-Super-Capacitor-is-charging": controller_Super_Capacitor_is_charging,
       "controller-Super-Capacitor-error-has-been-detected": controller_Super_Capacitor_error_has_been_detected,
       "controller-battery-backup-unit-BBU-back-to-present": controller_battery_backup_unit_BBU_back_to_present,
       "controller-battery-backup-unit-BBU-back-to-on-line": controller_battery_backup_unit_BBU_back_to_on_line,
       "controller-battery-backup-unit-BBU-fully-charged": controller_battery_backup_unit_BBU_fully_charged,
       "controller-Super-Capacitor-is-back-to-present": controller_Super_Capacitor_is_back_to_present,
       "controller-Super-Capacitor-is-back-to-on-line": controller_Super_Capacitor_is_back_to_on_line,
       "controller-Super-Capacitor-has-been-fully-charged": controller_Super_Capacitor_has_been_fully_charged,
       "enclosure-fan-sensor-detection-failed": enclosure_fan_sensor_detection_failed,
       "expansion-enclosure-fan-failed-has-been-detected": expansion_enclosure_fan_failed_has_been_detected,
       "enclosure-fan-failed-has-been-detected": enclosure_fan_failed_has_been_detected,
       "expansion-enclosure-fan-absent-has-been-detected": expansion_enclosure_fan_absent_has_been_detected,
       "enclosure-fan-absent-has-been-detected": enclosure_fan_absent_has_been_detected,
       "expansion-enclosure-fan-low-speed-has-been-detected": expansion_enclosure_fan_low_speed_has_been_detected,
       "enclosure-fan-low-speed-has-been-detected": enclosure_fan_low_speed_has_been_detected,
       "expansion-enclosure-fan-absent": expansion_enclosure_fan_absent,
       "fan-in-JBOD-failed": fan_in_JBOD_failed,
       "cpu-FAN-failure-has-been-detected-with-FAN-number": cpu_FAN_failure_has_been_detected_with_FAN_number,
       "enclosure-drawer-fan-failed-has-been-detected": enclosure_drawer_fan_failed_has_been_detected,
       "enclosure-drawer-fan-absent-has-been-detected": enclosure_drawer_fan_absent_has_been_detected,
       "enclosure-drawer-fan-low-speed-has-been-detected": enclosure_drawer_fan_low_speed_has_been_detected,
       "enclosure-fan-back-to-normal": enclosure_fan_back_to_normal,
       "expansion-enclosure-fan-backed-to-on-line": expansion_enclosure_fan_backed_to_on_line,
       "enclosure-fan-is-back-to-on-line": enclosure_fan_is_back_to_on_line,
       "expansion-enclosure-fan-backed-to-present": expansion_enclosure_fan_backed_to_present,
       "enclosure-fan-is-back-to-present": enclosure_fan_is_back_to_present,
       "expansion-enclosure-fan-backed-to-normal-speed": expansion_enclosure_fan_backed_to_normal_speed,
       "enclosure-fan-is-back-to-normal-speed": enclosure_fan_is_back_to_normal_speed,
       "expansion-enclosure-fan-back-to-on-line": expansion_enclosure_fan_back_to_on_line,
       "cpu-FAN-is-back-online-with-FAN-number": cpu_FAN_is_back_online_with_FAN_number,
       "expansion-enclosure-drawer-fan-is-back-to-on-line": expansion_enclosure_drawer_fan_is_back_to_on_line,
       "enclosure-drawer-fan-is-back-to-on-line": enclosure_drawer_fan_is_back_to_on_line,
       "expansion-enclosure-drawer-fan-is-back-to-present": expansion_enclosure_drawer_fan_is_back_to_present,
       "enclosure-drawer-fan-is-back-to-present": enclosure_drawer_fan_is_back_to_present,
       "expansion-enclosure-drawer-fan-is-back-to-normal-RPM": expansion_enclosure_drawer_fan_is_back_to_normal_RPM,
       "enclosure-drawer-fan-speed-is-back-to-normal": enclosure_drawer_fan_speed_is_back_to_normal,
       "ups-connection-failure-has-been-detected": ups_connection_failure_has_been_detected,
       "ups-AC-power-failure-was-detected-The-device-entered-safe-mode": ups_AC_power_failure_was_detected_The_device_entered_safe_mode,
       "ups-Low-Battery-has-been-detected": ups_Low_Battery_has_been_detected,
       "ups-Low-Battery-has-been-detected-Please-shut-down-immediately": ups_Low_Battery_has_been_detected_Please_shut_down_immediately,
       "ups-connection-has-been-restored": ups_connection_has_been_restored,
       "ups-AC-power-was-restored-The-device-has-exited-safe-mode": ups_AC_power_was_restored_The_device_has_exited_safe_mode,
       "ups-Battery-Level-Restored-to-Safety": ups_Battery_Level_Restored_to_Safety,
       "cpu-low-temperature-detected": cpu_low_temperature_detected,
       "cpu-high-temperature-detected": cpu_high_temperature_detected,
       "controller-ASIC-low-temperature-detected": controller_ASIC_low_temperature_detected,
       "controller-ASIC-high-temperature-detected": controller_ASIC_high_temperature_detected,
       "controller-drive-channel-IO-chip-low-temperature-detected": controller_drive_channel_IO_chip_low_temperature_detected,
       "controller-drive-channel-IO-chip-high-temperature-detected": controller_drive_channel_IO_chip_high_temperature_detected,
       "controller-host-IO-chip-low-temperature-detected": controller_host_IO_chip_low_temperature_detected,
       "controller-host-IO-chip-high-temperature-detected": controller_host_IO_chip_high_temperature_detected,
       "enclosure-backplane-temperature-sensor-detection-failed": enclosure_backplane_temperature_sensor_detection_failed,
       "expansion-enclosure-backplane-low-temperature-has-been-detected": expansion_enclosure_backplane_low_temperature_has_been_detected,
       "expansion-enclosure-backplane-high-temperature-has-been-detected": expansion_enclosure_backplane_high_temperature_has_been_detected,
       "enclosure-backplane-high-temperature-has-been-detected": enclosure_backplane_high_temperature_has_been_detected,
       "the-temperature-sensor-of-expansion-enclosure-is-not-supported": the_temperature_sensor_of_expansion_enclosure_is_not_supported,
       "the-temperature-sensor-of-expansion-enclosure-is-not-installed": the_temperature_sensor_of_expansion_enclosure_is_not_installed,
       "unknown-status-of-the-temperature-sensor-of-expansion-enclosure": unknown_status_of_the_temperature_sensor_of_expansion_enclosure,
       "the-temperature-sensor-of-expansion-enclosure-is-not-available": the_temperature_sensor_of_expansion_enclosure_is_not_available,
       "expansion-enclosure-sensor-detected-low-temperature": expansion_enclosure_sensor_detected_low_temperature,
       "expansion-enclosure-sensor-detected-high-temperature": expansion_enclosure_sensor_detected_high_temperature,
       "cpu-low-temperature-has-been-detected-with-CPU-number": cpu_low_temperature_has_been_detected_with_CPU_number,
       "cpu-high-temperature-has-been-detected-with-CPU-number": cpu_high_temperature_has_been_detected_with_CPU_number,
       "controller-host-IO-chip-high-temperature-has-been-detected": controller_host_IO_chip_high_temperature_has_been_detected,
       "io-module-low-temperature-has-been-detected": io_module_low_temperature_has_been_detected,
       "io-module-high-temperature-has-been-detected": io_module_high_temperature_has_been_detected,
       "cpu-temperature-back-to-normal-from-low-temperature": cpu_temperature_back_to_normal_from_low_temperature,
       "cpu-temperature-back-to-normal-from-high-temperature": cpu_temperature_back_to_normal_from_high_temperature,
       "enclosure-backplane-temperature-sensor-detected": enclosure_backplane_temperature_sensor_detected,
       "controller-ASIC-temperature-back-to-normal": controller_ASIC_temperature_back_to_normal,
       "controller-drive-channel-IO-chip-temperature-back-to-normal": controller_drive_channel_IO_chip_temperature_back_to_normal,
       "controller-host-board-IO-chip-temperature-back-to-normal": controller_host_board_IO_chip_temperature_back_to_normal,
       "expansion-enclosure-backplane-temperature-is-back-to-normal": expansion_enclosure_backplane_temperature_is_back_to_normal,
       "enclosure-backplane-temperature-is-back-to-normal": enclosure_backplane_temperature_is_back_to_normal,
       "expansion-enclosure-backplane-temperature-is-back-normal-state": expansion_enclosure_backplane_temperature_is_back_normal_state,
       "enclosure-backplane-temperature-is-back-to-normal-state": enclosure_backplane_temperature_is_back_to_normal_state,
       "expansion-enclosure-backplane-temperature-back-to-normal": expansion_enclosure_backplane_temperature_back_to_normal,
       "enclosure-backplane-temperature-back-to-normal": enclosure_backplane_temperature_back_to_normal,
       "controller-host-board-IO-chip-temperature-is-back-to-normal": controller_host_board_IO_chip_temperature_is_back_to_normal,
       "io-module-temperature-is-back-to-normal-from-low-temperature": io_module_temperature_is_back_to_normal_from_low_temperature,
       "io-module-temperature-is-back-to-normal-from-high-temperature": io_module_temperature_is_back_to_normal_from_high_temperature,
       "cpu-temperature-is-back-to-normal-from-low-temperature": cpu_temperature_is_back_to_normal_from_low_temperature,
       "cpu-temperature-is-back-to-normal-from-high-temperature": cpu_temperature_is_back_to_normal_from_high_temperature,
       "unexpected-select-timeout": unexpected_select_timeout,
       "unexpected-select-timeout-detected-on-expansion-drive": unexpected_select_timeout_detected_on_expansion_drive,
       "unexpected-select-timeout-detected-on-enclosure-drive": unexpected_select_timeout_detected_on_enclosure_drive,
       "gross-phase-or-signal-error-detected": gross_phase_or_signal_error_detected,
       "gross-phase-or-signal-error-detected-on-expansion-drive": gross_phase_or_signal_error_detected_on_expansion_drive,
       "gross-phase-or-signal-error-detected-on-enclosure-drive": gross_phase_or_signal_error_detected_on_enclosure_drive,
       "drive-IO-timeout": drive_IO_timeout,
       "drive-IO-timeout-detected-on-expansion-drive": drive_IO_timeout_detected_on_expansion_drive,
       "drive-IO-timeout-detected-on-enclosure-drive": drive_IO_timeout_detected_on_enclosure_drive,
       "scsi-parity-or-CRC-error": scsi_parity_or_CRC_error,
       "scsi-parity-or-CRC-error-detected-on-expansion-drive": scsi_parity_or_CRC_error_detected_on_expansion_drive,
       "scsi-parity-or-CRC-error-detected-on-enclosure-drive": scsi_parity_or_CRC_error_detected_on_enclosure_drive,
       "data-overrun-or-underrun": data_overrun_or_underrun,
       "media-scan-for-disk-drive-stopped": media_scan_for_disk_drive_stopped,
       "media-scan-for-disk-drvie-scan-aborted": media_scan_for_disk_drvie_scan_aborted,
       "data-overrun-or-underrun-detected-on-expansion-drive": data_overrun_or_underrun_detected_on_expansion_drive,
       "media-scan-for-disk-drive-in-expansion-stopped": media_scan_for_disk_drive_in_expansion_stopped,
       "media-scan-for-disk-drvie-in-expansion-scan-aborted": media_scan_for_disk_drvie_in_expansion_scan_aborted,
       "data-overrun-or-underrun-detected-on-enclosure-drive": data_overrun_or_underrun_detected_on_enclosure_drive,
       "media-scan-for-disk-drive-in-enclosure-stopped": media_scan_for_disk_drive_in_enclosure_stopped,
       "media-scan-for-disk-drvie-in-enclosure-scan-aborted": media_scan_for_disk_drvie_in_enclosure_scan_aborted,
       "invalid-status-or-sense-data-received": invalid_status_or_sense_data_received,
       "invalid-status-or-sense-data-received-with-info": invalid_status_or_sense_data_received_with_info,
       "invalid-status-or-sense-data-received-on-expansion-drive": invalid_status_or_sense_data_received_on_expansion_drive,
       "invalid-status-or-sense-data-received-w-info-on-expansion-drive": invalid_status_or_sense_data_received_w_info_on_expansion_drive,
       "invalid-status-or-sense-data-received-on-enclosure-drive": invalid_status_or_sense_data_received_on_enclosure_drive,
       "invalid-status-or-sense-data-received-w-info-on-enclosure-drive": invalid_status_or_sense_data_received_w_info_on_enclosure_drive,
       "drive-not-ready-detected": drive_not_ready_detected,
       "drive-not-ready-detected-with-info": drive_not_ready_detected_with_info,
       "drive-not-ready-detected-on-expansion-drive": drive_not_ready_detected_on_expansion_drive,
       "drive-not-ready-detected-with-info-on-expansion-drive": drive_not_ready_detected_with_info_on_expansion_drive,
       "drive-not-ready-detected-on-enclosure-drive": drive_not_ready_detected_on_enclosure_drive,
       "drive-not-ready-detected-with-info-on-enclosure-drive": drive_not_ready_detected_with_info_on_enclosure_drive,
       "drive-hardware-error-detected": drive_hardware_error_detected,
       "drive-hardware-error-detected-with-info": drive_hardware_error_detected_with_info,
       "drive-hardware-error-detected-on-expansion-drive": drive_hardware_error_detected_on_expansion_drive,
       "drive-hardware-error-detected-with-info-on-expansion-drive": drive_hardware_error_detected_with_info_on_expansion_drive,
       "drive-hardware-error-detected-on-enclosure-drive": drive_hardware_error_detected_on_enclosure_drive,
       "drive-hardware-error-detected-with-info-on-enclosure-drive": drive_hardware_error_detected_with_info_on_enclosure_drive,
       "drive-media-error-has-been-detected-with-LBA": drive_media_error_has_been_detected_with_LBA,
       "drive-media-error-has-been-detected-with-info": drive_media_error_has_been_detected_with_info,
       "drive-media-error-has-been-detected-with-LBA-on-expansion-drive": drive_media_error_has_been_detected_with_LBA_on_expansion_drive,
       "drive-media-error-detected-with-info-on-expansion-drive": drive_media_error_detected_with_info_on_expansion_drive,
       "drive-media-error-has-been-detected-with-LBA-on-enclosure-drive": drive_media_error_has_been_detected_with_LBA_on_enclosure_drive,
       "drive-media-error-detected-with-info-on-enclosure-drive": drive_media_error_detected_with_info_on_enclosure_drive,
       "unit-attention-received": unit_attention_received,
       "unit-attention-received-with-info": unit_attention_received_with_info,
       "unit-attention-received-on-expansion-drive": unit_attention_received_on_expansion_drive,
       "unit-attention-received-with-info-on-expansion-drive": unit_attention_received_with_info_on_expansion_drive,
       "unit-attention-received-on-enclosure-drive": unit_attention_received_on_enclosure_drive,
       "unit-attention-received-with-info-on-enclosure-drive": unit_attention_received_with_info_on_enclosure_drive,
       "unexpected-sense-data-received": unexpected_sense_data_received,
       "unexpected-sense-data-received-with-info": unexpected_sense_data_received_with_info,
       "unexpected-sense-data-received-on-expansion-drive": unexpected_sense_data_received_on_expansion_drive,
       "unexpected-sense-data-received-with-info-on-expansion-drive": unexpected_sense_data_received_with_info_on_expansion_drive,
       "unexpected-sense-data-received-on-enclosure-drive": unexpected_sense_data_received_on_enclosure_drive,
       "unexpected-sense-data-received-with-info-on-enclosure-drive": unexpected_sense_data_received_with_info_on_enclosure_drive,
       "failed-to-reassign-the-bad-block": failed_to_reassign_the_bad_block,
       "failed-to-reassign-the-bad-block-with-info": failed_to_reassign_the_bad_block_with_info,
       "failed-to-reassign-the-bad-block-on-expansion-drive": failed_to_reassign_the_bad_block_on_expansion_drive,
       "failed-to-reassign-the-bad-block-with-info-on-expansion-drive": failed_to_reassign_the_bad_block_with_info_on_expansion_drive,
       "failed-to-reassign-the-bad-block-on-enclosure-drive": failed_to_reassign_the_bad_block_on_enclosure_drive,
       "failed-to-reassign-the-bad-block-with-info-on-enclosure-drive": failed_to_reassign_the_bad_block_with_info_on_enclosure_drive,
       "bad-block-reassigned-with-LBA": bad_block_reassigned_with_LBA,
       "bad-block-reassigned-with-LBA-on-expansion-drive": bad_block_reassigned_with_LBA_on_expansion_drive,
       "bad-block-reassigned-with-LBA-on-enclosure-drive": bad_block_reassigned_with_LBA_on_enclosure_drive,
       "drive-command-aborted": drive_command_aborted,
       "drive-command-aborted-with-info": drive_command_aborted_with_info,
       "drive-command-aborted-on-expansion-drive": drive_command_aborted_on_expansion_drive,
       "drive-command-aborted-with-info-on-expansion-drive": drive_command_aborted_with_info_on_expansion_drive,
       "drive-command-aborted-on-enclosure-drive": drive_command_aborted_on_enclosure_drive,
       "drive-command-aborted-with-info-on-enclosure-drive": drive_command_aborted_with_info_on_enclosure_drive,
       "drive-error-has-been-recovered-with-LBA": drive_error_has_been_recovered_with_LBA,
       "drive-error-has-been-recovered-with-info": drive_error_has_been_recovered_with_info,
       "drive-error-has-been-recovered-with-LBA-on-expansion-drive": drive_error_has_been_recovered_with_LBA_on_expansion_drive,
       "drive-error-has-been-recovered-with-info-on-expansion-drive": drive_error_has_been_recovered_with_info_on_expansion_drive,
       "drive-error-has-been-recovered-with-LBA-on-enclosure-drive": drive_error_has_been_recovered_with_LBA_on_enclosure_drive,
       "drive-error-has-been-recovered-with-info-on-enclosure-drive": drive_error_has_been_recovered_with_info_on_enclosure_drive,
       "unable-to-start-drive-error-recovery-procedure": unable_to_start_drive_error_recovery_procedure,
       "drive-SMART-error-state-has-been-detected": drive_SMART_error_state_has_been_detected,
       "drive-error-recovery-procedure-started": drive_error_recovery_procedure_started,
       "drive-error-recovery-procedure-stopped": drive_error_recovery_procedure_stopped,
       "drive-SMART-error-state-has-been-detected-on-expansion-drive": drive_SMART_error_state_has_been_detected_on_expansion_drive,
       "drive-error-recovery-procedure-started-on-expansion-drive": drive_error_recovery_procedure_started_on_expansion_drive,
       "drive-error-recovery-procedure-stopped-on-expansion-drive": drive_error_recovery_procedure_stopped_on_expansion_drive,
       "drive-SMART-error-state-has-been-detected-on-enclosure-drive": drive_SMART_error_state_has_been_detected_on_enclosure_drive,
       "drive-error-recovery-procedure-started-on-enclosure-drive": drive_error_recovery_procedure_started_on_enclosure_drive,
       "drive-error-recovery-procedure-stopped-on-enclosure-drive": drive_error_recovery_procedure_stopped_on_enclosure_drive,
       "drive-media-error-has-been-recovered": drive_media_error_has_been_recovered,
       "unrecovered-drive-media-error-detected": unrecovered_drive_media_error_detected,
       "drive-lifetime-estimate-warning-threshold-exceeded": drive_lifetime_estimate_warning_threshold_exceeded,
       "the-SSDs-remaining-life-less-than-threshold-detected": the_SSDs_remaining_life_less_than_threshold_detected,
       "drive-media-error-has-been-recovered-on-expansion-drive": drive_media_error_has_been_recovered_on_expansion_drive,
       "unrecovered-drive-media-error-detected-on-expansion-drive": unrecovered_drive_media_error_detected_on_expansion_drive,
       "drive-media-error-has-been-recovered-on-enclosure-drive": drive_media_error_has_been_recovered_on_enclosure_drive,
       "unrecovered-drive-media-error-detected-on-enclosure-drive": unrecovered_drive_media_error_detected_on_enclosure_drive,
       "media-scan-for-disk-drive-completed": media_scan_for_disk_drive_completed,
       "media-scan-for-disk-drive-in-expansion-completed": media_scan_for_disk_drive_in_expansion_completed,
       "media-scan-for-disk-drive-enclosure-completed": media_scan_for_disk_drive_enclosure_completed,
       "drive-scanned": drive_scanned,
       "exiled-drive-detected-with-ch-ID": exiled_drive_detected_with_ch_ID,
       "unsupported-drive-detected-drive-type-or-license-is-invalid": unsupported_drive_detected_drive_type_or_license_is_invalid,
       "unsupported-drive-detected-incorrect-bundle-ID": unsupported_drive_detected_incorrect_bundle_ID,
       "unsupported-drive-detected-unsupported-bundle-code": unsupported_drive_detected_unsupported_bundle_code,
       "drive-detection-failed": drive_detection_failed,
       "drive-scanned-on-expansion-drive": drive_scanned_on_expansion_drive,
       "exiled-drive-detected-with-ch-ID-in-expansion": exiled_drive_detected_with_ch_ID_in_expansion,
       "unsupported-drive-detected-in-expansion": unsupported_drive_detected_in_expansion,
       "incorrect-bundle-ID-detected-on-expansion-drive": incorrect_bundle_ID_detected_on_expansion_drive,
       "unsupported-bundle-code-detected-on-expansion-drive": unsupported_bundle_code_detected_on_expansion_drive,
       "drive-detection-failed-on-expansion-drive": drive_detection_failed_on_expansion_drive,
       "drive-scanned-on-enclosure-drive": drive_scanned_on_enclosure_drive,
       "exiled-drive-detected-with-ch-ID-in-enclosure": exiled_drive_detected_with_ch_ID_in_enclosure,
       "unsupported-drive-detected-in-enclosure": unsupported_drive_detected_in_enclosure,
       "incorrect-bundle-ID-detected-on-enclosure-drive": incorrect_bundle_ID_detected_on_enclosure_drive,
       "unsupported-bundle-code-detected-on-enclosure-drive": unsupported_bundle_code_detected_on_enclosure_drive,
       "drive-detection-failed-on-enclosure-drive": drive_detection_failed_on_enclosure_drive,
       "trunking-configuration-error-detected-in-Slot-B": trunking_configuration_error_detected_in_Slot_B,
       "trunking-configuration-error-detected-in-Slot-A": trunking_configuration_error_detected_in_Slot_A,
       "ipv4-address-conflict-has-been-detected": ipv4_address_conflict_has_been_detected,
       "ipv6-address-conflict-has-been-detected": ipv6_address_conflict_has_been_detected,
       "mismatched-SFP-installation-has-been-detected": mismatched_SFP_installation_has_been_detected,
       "scsi-channel-failed-detected-with-channel-ID": scsi_channel_failed_detected_with_channel_ID,
       "host-channel-failed-with-ID": host_channel_failed_with_ID,
       "scsi-channel-failed-detected": scsi_channel_failed_detected,
       "host-channel-failed": host_channel_failed,
       "redundant-path-error-detected-with-channel-ID": redundant_path_error_detected_with_channel_ID,
       "redundant-path-error-detected-with-channel-and-target-ID": redundant_path_error_detected_with_channel_and_target_ID,
       "fibre-Channel-loop-connection-restored": fibre_Channel_loop_connection_restored,
       "ch-redundant-path-error-recovered-with-ch": ch_redundant_path_error_recovered_with_ch,
       "ch-redundant-path-error-recovered-with-ch-ID": ch_redundant_path_error_recovered_with_ch_ID,
       "ch-iD-redundant-path-error-recovered-with-ch-ID": ch_iD_redundant_path_error_recovered_with_ch_ID,
       "host-channel-disconnected": host_channel_disconnected,
       "host-channel-connected": host_channel_connected,
       "host-channel-speed-has-backed-to-speed-in-Gb-warning": host_channel_speed_has_backed_to_speed_in_Gb_warning,
       "host-channel-speed-backed-to-speed-in-Gb-info": host_channel_speed_backed_to_speed_in_Gb_info,
       "host-channel-speed-has-backed-to-speed-in-Mb-warning": host_channel_speed_has_backed_to_speed_in_Mb_warning,
       "host-channel-speed-backed-to-speed-in-Mb-info": host_channel_speed_backed_to_speed_in_Mb_info,
       "host-channel-speed-has-changed-to-speed-in-Gb": host_channel_speed_has_changed_to_speed_in_Gb,
       "host-channel-speed-has-changed-to-speed-in-Mb": host_channel_speed_has_changed_to_speed_in_Mb,
       "drive-missing": drive_missing,
       "drive-failed": drive_failed,
       "drive-removed": drive_removed,
       "a-second-or-third-LD-member-drive-failed": a_second_or_third_LD_member_drive_failed,
       "the-first-LD-member-drive-failed": the_first_LD_member_drive_failed,
       "logical-drive-member-drive-removed": logical_drive_member_drive_removed,
       "expansion-drive-missing": expansion_drive_missing,
       "expansion-drive-failed": expansion_drive_failed,
       "expansion-drive-removed": expansion_drive_removed,
       "a-second-or-third-LD-member-drive-in-expansion-failed": a_second_or_third_LD_member_drive_in_expansion_failed,
       "the-first-LD-member-drive-in-expansion-failed": the_first_LD_member_drive_in_expansion_failed,
       "logical-drive-member-drive-in-expansion-removed": logical_drive_member_drive_in_expansion_removed,
       "enclosure-drive-missing": enclosure_drive_missing,
       "enclosure-drive-failed": enclosure_drive_failed,
       "enclosure-drive-removed": enclosure_drive_removed,
       "a-second-or-third-LD-member-drive-in-enclosure-failed": a_second_or_third_LD_member_drive_in_enclosure_failed,
       "the-first-LD-member-drive-in-enclosure-failed": the_first_LD_member_drive_in_enclosure_failed,
       "logical-drive-member-drive-in-enclosure-removed": logical_drive_member_drive_in_enclosure_removed,
       "logical-drive-initialization-failed": logical_drive_initialization_failed,
       "logical-drive-creation-aborted": logical_drive_creation_aborted,
       "logical-drive-creation-failed": logical_drive_creation_failed,
       "logical-drive-rebuild-aborted": logical_drive_rebuild_aborted,
       "logical-drive-rebuild-failed": logical_drive_rebuild_failed,
       "logical-drive-parity-regeneration-aborted": logical_drive_parity_regeneration_aborted,
       "logical-drive-parity-regeneration-failed": logical_drive_parity_regeneration_failed,
       "logical-drive-expansion-aborted": logical_drive_expansion_aborted,
       "logical-drive-expansion-failed": logical_drive_expansion_failed,
       "media-scan-for-logical-drive-aborted": media_scan_for_logical_drive_aborted,
       "unable-to-start-media-scan-Status-is-invalid-for-media-scan": unable_to_start_media_scan_Status_is_invalid_for_media_scan,
       "media-scan-for-logical-drive-failed": media_scan_for_logical_drive_failed,
       "no-spare-drive-for-recovering-the-detected-unrecoverable-error": no_spare_drive_for_recovering_the_detected_unrecoverable_error,
       "unrecovered-media-error-detected": unrecovered_media_error_detected,
       "media-scan-for-logical-drive-member-drive-stopped-Scan-failed": media_scan_for_logical_drive_member_drive_stopped_Scan_failed,
       "unrecovered-media-error-detected-on-expansion-drive": unrecovered_media_error_detected_on_expansion_drive,
       "media-scan-for-logical-drive-member-drive-in-expansion-stopped": media_scan_for_logical_drive_member_drive_in_expansion_stopped,
       "unrecovered-media-error-detected-on-enclosure-drive": unrecovered_media_error_detected_on_enclosure_drive,
       "media-scan-for-logical-drive-member-drive-in-enclosure-stopped": media_scan_for_logical_drive_member_drive_in_enclosure_stopped,
       "logical-drive-cache-data-purged": logical_drive_cache_data_purged,
       "drive-clone-failed": drive_clone_failed,
       "drive-clone-aborted": drive_clone_aborted,
       "drive-clone-failed-on-expansion-drive": drive_clone_failed_on_expansion_drive,
       "drive-clone-aborted-on-expansion-drive": drive_clone_aborted_on_expansion_drive,
       "drive-clone-failed-on-enclosure-drive": drive_clone_failed_on_enclosure_drive,
       "drive-clone-aborted-on-enclosure-drive": drive_clone_aborted_on_enclosure_drive,
       "logical-drive-error-detected-Bad-block-count-exceeded": logical_drive_error_detected_Bad_block_count_exceeded,
       "logical-drive-error-detected-Bad-block-table-corrupted": logical_drive_error_detected_Bad_block_table_corrupted,
       "logical-drive-error-detected-Online-init-table-failed": logical_drive_error_detected_Online_init_table_failed,
       "logical-drive-bad-data-block-detected-and-marked": logical_drive_bad_data_block_detected_and_marked,
       "unprotected-block-on-the-logical-drive-detected-and-marked": unprotected_block_on_the_logical_drive_detected_and_marked,
       "logical-drive-bad-data-block-recovered": logical_drive_bad_data_block_recovered,
       "logical-drive-bad-data-block-detected": logical_drive_bad_data_block_detected,
       "logical-drive-inconsistent-parity-block-detected": logical_drive_inconsistent_parity_block_detected,
       "logical-drive-inconsistent-parity-block-recovered": logical_drive_inconsistent_parity_block_recovered,
       "logical-drive-media-error-detected": logical_drive_media_error_detected,
       "logical-drive-media-error-recovered": logical_drive_media_error_recovered,
       "logical-drive-status-back-to-normal": logical_drive_status_back_to_normal,
       "logical-drive-degraded": logical_drive_degraded,
       "logical-drive-had-fatal-failure": logical_drive_had_fatal_failure,
       "logical-drive-failed": logical_drive_failed,
       "logical-drive-member-drive-missing-has-been-detected": logical_drive_member_drive_missing_has_been_detected,
       "logical-drive-member-drive-missing": logical_drive_member_drive_missing,
       "logical-drive-status-changed-from-online-to-offline": logical_drive_status_changed_from_online_to_offline,
       "logical-drive-status-changed-from-offline-to-online": logical_drive_status_changed_from_offline_to_online,
       "all-member-drives-of-logical-drive-removed": all_member_drives_of_logical_drive_removed,
       "all-member-drives-of-logical-drive-restored": all_member_drives_of_logical_drive_restored,
       "logical-drive-undeleted": logical_drive_undeleted,
       "logical-drive-online-initialization-started": logical_drive_online_initialization_started,
       "logical-drive-offline-initialization-started": logical_drive_offline_initialization_started,
       "logical-drive-creation-started": logical_drive_creation_started,
       "logical-drive-online-initialization-completed": logical_drive_online_initialization_completed,
       "logical-drive-offline-initialization-completed": logical_drive_offline_initialization_completed,
       "logical-drive-created": logical_drive_created,
       "logical-drive-rebuild-resumed": logical_drive_rebuild_resumed,
       "logical-drive-rebuild-started": logical_drive_rebuild_started,
       "logical-drive-rebuild-completed": logical_drive_rebuild_completed,
       "logical-drive-parity-regeneration-resumed": logical_drive_parity_regeneration_resumed,
       "logical-drive-parity-regeneration-started": logical_drive_parity_regeneration_started,
       "logical-drive-parity-regeneration-completed": logical_drive_parity_regeneration_completed,
       "logical-drive-online-expansion-started": logical_drive_online_expansion_started,
       "logical-drive-offline-expansion-started": logical_drive_offline_expansion_started,
       "logical-drive-online-expansion-completed": logical_drive_online_expansion_completed,
       "logical-drive-offline-expansion-completed": logical_drive_offline_expansion_completed,
       "logical-drive-RAID-migration-resumed": logical_drive_RAID_migration_resumed,
       "logical-drive-add-drive-action-resumed": logical_drive_add_drive_action_resumed,
       "logical-drive-RAID-migration-started": logical_drive_RAID_migration_started,
       "logical-drive-add-drive-action-started": logical_drive_add_drive_action_started,
       "logical-drive-RAID-migration-paused": logical_drive_RAID_migration_paused,
       "logical-drive-add-drive-action-paused": logical_drive_add_drive_action_paused,
       "logical-drive-RAID-migration-completed": logical_drive_RAID_migration_completed,
       "logical-drive-add-drive-completed": logical_drive_add_drive_completed,
       "media-scan-for-disk-drive-started": media_scan_for_disk_drive_started,
       "media-scan-for-logical-drive-started": media_scan_for_logical_drive_started,
       "media-scan-for-logical-drive-member-drive-started": media_scan_for_logical_drive_member_drive_started,
       "media-scan-for-disk-drive-in-expansion-started": media_scan_for_disk_drive_in_expansion_started,
       "media-scan-for-logical-drive-member-drive-in-expansion-started": media_scan_for_logical_drive_member_drive_in_expansion_started,
       "media-scan-for-disk-drive-enclosure-started": media_scan_for_disk_drive_enclosure_started,
       "media-scan-for-logical-drive-member-drive-in-enclosure-started": media_scan_for_logical_drive_member_drive_in_enclosure_started,
       "media-scan-for-logical-drive-completed": media_scan_for_logical_drive_completed,
       "media-scan-for-logical-drvie-member-drive-completed": media_scan_for_logical_drvie_member_drive_completed,
       "media-scan-for-logical-drive-stopped": media_scan_for_logical_drive_stopped,
       "unable-to-start-media-scan-Previous-task-is-still-in-progress": unable_to_start_media_scan_Previous_task_is_still_in_progress,
       "media-scan-for-logical-drvie-member-in-expansion-completed": media_scan_for_logical_drvie_member_in_expansion_completed,
       "media-scan-for-logical-drvie-member-in-enclosure-completed": media_scan_for_logical_drvie_member_in_enclosure_completed,
       "drive-clone-resumed": drive_clone_resumed,
       "drive-clone-started": drive_clone_started,
       "drive-clone-resumed-on-expansion-drive": drive_clone_resumed_on_expansion_drive,
       "drive-clone-started-on-expansion-drive": drive_clone_started_on_expansion_drive,
       "drive-clone-resumed-on-enclosure-drive": drive_clone_resumed_on_enclosure_drive,
       "drive-clone-started-on-enclosure-drive": drive_clone_started_on_enclosure_drive,
       "drive-copy-and-replace-completed": drive_copy_and_replace_completed,
       "drive-clone-completed": drive_clone_completed,
       "drive-copy-and-replace-completed-on-expansion-drive": drive_copy_and_replace_completed_on_expansion_drive,
       "drive-clone-completed-on-expansion-drive": drive_clone_completed_on_expansion_drive,
       "drive-copy-and-replace-completed-on-enclosure-drive": drive_copy_and_replace_completed_on_enclosure_drive,
       "drive-clone-completed-on-enclosure-drive": drive_clone_completed_on_enclosure_drive,
       "logical-volume-created": logical_volume_created,
       "logical-volume-creation-failed": logical_volume_creation_failed,
       "logical-volume-expansion-completed": logical_volume_expansion_completed,
       "logical-volume-expansion-failed": logical_volume_expansion_failed,
       "logical-volume-deleted": logical_volume_deleted,
       "logical-volume-cache-data-purged": logical_volume_cache_data_purged,
       "logical-volume-status-back-to-normal": logical_volume_status_back_to_normal,
       "logical-volume-degraded": logical_volume_degraded,
       "logical-volume-failed-fatal-fail": logical_volume_failed_fatal_fail,
       "logical-volume-failed-invalid-array": logical_volume_failed_invalid_array,
       "logical-volume-member-drive-missing-incomplete-array": logical_volume_member_drive_missing_incomplete_array,
       "logical-volume-member-drive-missing-missing-drives": logical_volume_member_drive_missing_missing_drives,
       "logical-volume-status-changed-from-online-to-offline": logical_volume_status_changed_from_online_to_offline,
       "logical-volume-status-changed-from-offline-to-online": logical_volume_status_changed_from_offline_to_online,
       "all-member-drives-of-a-logical-volume-removed": all_member_drives_of_a_logical_volume_removed,
       "all-member-drives-of-a-logical-volume-restored": all_member_drives_of_a_logical_volume_restored,
       "logical-volume-undeleted": logical_volume_undeleted,
       "logical-volume-online-initialization-started": logical_volume_online_initialization_started,
       "logical-volume-offline-initialization-started": logical_volume_offline_initialization_started,
       "logical-volume-creation-started": logical_volume_creation_started,
       "logical-volume-online-initialization-completed": logical_volume_online_initialization_completed,
       "logical-volume-offline-initialization-completed": logical_volume_offline_initialization_completed,
       "logical-volume-creation-completed": logical_volume_creation_completed,
       "logical-volume-rebuild-resumed": logical_volume_rebuild_resumed,
       "logical-volume-rebuild-started": logical_volume_rebuild_started,
       "logical-volume-rebuild-completed": logical_volume_rebuild_completed,
       "logical-volume-parity-regeneration-resumed": logical_volume_parity_regeneration_resumed,
       "logical-volume-parity-regeneration-started": logical_volume_parity_regeneration_started,
       "logical-volume-parity-regeneration-completed": logical_volume_parity_regeneration_completed,
       "logical-volume-online-expansion-started": logical_volume_online_expansion_started,
       "logical-volume-offline-expansion-started": logical_volume_offline_expansion_started,
       "logical-volume-online-expansion-completed": logical_volume_online_expansion_completed,
       "logical-volume-offline-expansion-completed": logical_volume_offline_expansion_completed,
       "logical-volume-migration-resumed": logical_volume_migration_resumed,
       "logical-volume-add-drive-action-resumed": logical_volume_add_drive_action_resumed,
       "logical-volume-migration-started": logical_volume_migration_started,
       "logical-volume-add-drive-action-started": logical_volume_add_drive_action_started,
       "logical-volume-migration-paused": logical_volume_migration_paused,
       "logical-volume-add-drive-action-paused": logical_volume_add_drive_action_paused,
       "logical-volume-migration-completed": logical_volume_migration_completed,
       "logical-volume-add-drive-action-completed": logical_volume_add_drive_action_completed,
       "partition-created": partition_created,
       "partition-creation-failed": partition_creation_failed,
       "partition-deleted": partition_deleted,
       "partition-deletion-failed": partition_deletion_failed,
       "partition-has-been-activated": partition_has_been_activated,
       "license-key-consistency-check-failed": license_key_consistency_check_failed,
       "license-key-is-not-supported-by-the-installed-firmware": license_key_is_not_supported_by_the_installed_firmware,
       "pool-created": pool_created,
       "pool-creation-failed": pool_creation_failed,
       "pool-expansion-completed": pool_expansion_completed,
       "pool-expansion-failed": pool_expansion_failed,
       "pool-deleted": pool_deleted,
       "pool-migration-started": pool_migration_started,
       "pool-migration-completed": pool_migration_completed,
       "pool-migration-failed": pool_migration_failed,
       "bad-block-found-in-deleted-ME-migration-aborted": bad_block_found_in_deleted_ME_migration_aborted,
       "the-pool-cannot-connect-to-cloud-because-the-network-error": the_pool_cannot_connect_to_cloud_because_the_network_error,
       "the-pool-cannot-connect-to-cloud-because-authentication-failed": the_pool_cannot_connect_to_cloud_because_authentication_failed,
       "the-pool-cannot-connect-to-cloud-because-the-bucket-not-exist": the_pool_cannot_connect_to_cloud_because_the_bucket_not_exist,
       "the-pool-cannot-connect-to-cloud-because-failed-create-bucket": the_pool_cannot_connect_to_cloud_because_failed_create_bucket,
       "the-pool-cannot-connect-to-cloud-The-bucket-has-been-used": the_pool_cannot_connect_to_cloud_The_bucket_has_been_used,
       "the-pool-cannot-connect-to-cloud-Wrong-encryption-key": the_pool_cannot_connect_to_cloud_Wrong_encryption_key,
       "the-pool-has-failed-to-upload-data-to-cloud": the_pool_has_failed_to_upload_data_to_cloud,
       "the-pool-cannot-connect-to-cloud-No-channel-for-iSCSI-device": the_pool_cannot_connect_to_cloud_No_channel_for_iSCSI_device,
       "the-pool-has-been-deleted-The-cloud-storage-is-not-deleted": the_pool_has_been_deleted_The_cloud_storage_is_not_deleted,
       "the-data-of-the-pool-saved-in-the-bucket-is-corrupted": the_data_of_the_pool_saved_in_the_bucket_is_corrupted,
       "volume-created": volume_created,
       "volume-creation-failed": volume_creation_failed,
       "volume-deleted": volume_deleted,
       "volume-deletion-failed": volume_deletion_failed,
       "volume-expansion-completed": volume_expansion_completed,
       "snapshot-image-created": snapshot_image_created,
       "snapshot-image-creation-failed": snapshot_image_creation_failed,
       "snapshot-image-deleted": snapshot_image_deleted,
       "snapshot-image-deletion-failed": snapshot_image_deletion_failed,
       "snapshot-image-purge-triggered": snapshot_image_purge_triggered,
       "free-space-might-be-insufficient-for-future-snapshot-usage": free_space_might_be_insufficient_for_future_snapshot_usage,
       "free-space-recovered-for-future-snapshot-usage": free_space_recovered_for_future_snapshot_usage,
       "the-snapshot-images-has-been-backed-up-to-cloud": the_snapshot_images_has_been_backed_up_to_cloud,
       "remote-drive-has-connected": remote_drive_has_connected,
       "remote-drive-has-disconnected": remote_drive_has_disconnected,
       "pair-created": pair_created,
       "pair-creation-failed": pair_creation_failed,
       "pair-deleted": pair_deleted,
       "synchronous-replication-started": synchronous_replication_started,
       "synchronous-replication-completed": synchronous_replication_completed,
       "synchronous-replication-paused": synchronous_replication_paused,
       "synchronous-replication-resumed": synchronous_replication_resumed,
       "synchronous-replication-pair-split": synchronous_replication_pair_split,
       "synchronous-pair-split-because-network-timeout": synchronous_pair_split_because_network_timeout,
       "asynchronous-replication-started": asynchronous_replication_started,
       "asynchronous-replication-paused": asynchronous_replication_paused,
       "asynchronous-replication-resumed": asynchronous_replication_resumed,
       "asynchronous-replication-completed": asynchronous_replication_completed,
       "asynchronous-replication-pair-split": asynchronous_replication_pair_split,
       "replication-pair-role-switched": replication_pair_role_switched,
       "free-space-might-be-insufficient-for-future-replication-pair": free_space_might_be_insufficient_for_future_replication_pair,
       "free-space-recovered-for-future-replication-pair-usage": free_space_recovered_for_future_replication_pair_usage,
       "pair-synchronization-aborted": pair_synchronization_aborted,
       "pair-synchronization-failed-and-split": pair_synchronization_failed_and_split,
       "initial-copy-started": initial_copy_started,
       "failed-to-start-the-Initial-copy": failed_to_start_the_Initial_copy,
       "initial-copy-has-completed": initial_copy_has_completed,
       "initial-copy-has-continued": initial_copy_has_continued,
       "initial-copy-has-been-stopped": initial_copy_has_been_stopped,
       "initial-copy-has-been-resumed": initial_copy_has_been_resumed,
       "failed-to-resume-the-initial-copy": failed_to_resume_the_initial_copy,
       "pair-recovered": pair_recovered,
       "pair-broken": pair_broken,
       "pair-synchronization-has-started": pair_synchronization_has_started,
       "failed-to-start-the-pair-synchronization": failed_to_start_the_pair_synchronization,
       "pair-synchronization-completed": pair_synchronization_completed,
       "pair-synchronization-has-continued": pair_synchronization_has_continued,
       "pair-synchronization-has-been-stopped": pair_synchronization_has_been_stopped,
       "pair-synchronization-has-been-resumed": pair_synchronization_has_been_resumed,
       "failed-to-resume-the-pair-synchronization": failed_to_resume_the_pair_synchronization,
       "target-volume-full": target_volume_full,
       "pair-synchronization-is-in-progress": pair_synchronization_is_in_progress,
       "bad-block-found-in-source-volume-pair-synchronization-aborted": bad_block_found_in_source_volume_pair_synchronization_aborted,
       "pool-space-utilization-exceeded-the-threshold-info": pool_space_utilization_exceeded_the_threshold_info,
       "pool-space-utilization-exceeded-the-threshold-warning": pool_space_utilization_exceeded_the_threshold_warning,
       "pool-space-utilization-exceeded-the-threshold-error": pool_space_utilization_exceeded_the_threshold_error,
       "pool-space-utilization-exceeded-the-threshold-critical": pool_space_utilization_exceeded_the_threshold_critical,
       "pool-space-utilization-has-dropped-below-threshold-info": pool_space_utilization_has_dropped_below_threshold_info,
       "pool-space-utilization-has-dropped-below-threshold-warning": pool_space_utilization_has_dropped_below_threshold_warning,
       "pool-space-utilization-has-dropped-below-threshold-error": pool_space_utilization_has_dropped_below_threshold_error,
       "pool-space-utilization-has-dropped-below-threshold-critical": pool_space_utilization_has_dropped_below_threshold_critical,
       "pool-status-changed-to-online": pool_status_changed_to_online,
       "pool-status-changed-to-offline": pool_status_changed_to_offline,
       "the-pool-allocated-space-has-exceeded-the-threshold-info": the_pool_allocated_space_has_exceeded_the_threshold_info,
       "the-pool-allocated-space-has-exceeded-the-threshold-warning": the_pool_allocated_space_has_exceeded_the_threshold_warning,
       "the-pool-allocated-space-has-exceeded-the-threshold-error": the_pool_allocated_space_has_exceeded_the_threshold_error,
       "the-pool-allocated-space-has-exceeded-the-threshold-critical": the_pool_allocated_space_has_exceeded_the_threshold_critical,
       "the-pool-allocated-space-has-dropped-below-threshold-info": the_pool_allocated_space_has_dropped_below_threshold_info,
       "the-pool-allocated-space-has-dropped-below-threshold-warning": the_pool_allocated_space_has_dropped_below_threshold_warning,
       "the-pool-allocated-space-has-dropped-below-threshold-error": the_pool_allocated_space_has_dropped_below_threshold_error,
       "the-pool-allocated-space-has-dropped-below-threshold-critical": the_pool_allocated_space_has_dropped_below_threshold_critical,
       "the-pool-has-been-foreced-offline-because-error-detected": the_pool_has_been_foreced_offline_because_error_detected,
       "free-space-might-be-insufficient-for-future-volume-usage": free_space_might_be_insufficient_for_future_volume_usage,
       "free-space-recovered-for-future-volume-usage": free_space_recovered_for_future_volume_usage,
       "tier-migration-has-been-started": tier_migration_has_been_started,
       "tier-migration-has-completed": tier_migration_has_completed,
       "tier-migration-has-been-aborted": tier_migration_has_been_aborted,
       "volume-expansion-has-completed": volume_expansion_has_completed,
       "volume-expansion-failed": volume_expansion_failed,
       "the-system-has-been-unable-to-satisfy-QoS-policy-for-15-min": the_system_has_been_unable_to_satisfy_QoS_policy_for_15_min,
       "snapshot-image-has-been-activated": snapshot_image_has_been_activated,
       "insufficient-free-space-for-data-allocation": insufficient_free_space_for_data_allocation,
       "free-space-recovered-for-data-allocation": free_space_recovered_for_data_allocation,
       "non-optimal-configuration-may-impact-system-performance": non_optimal_configuration_may_impact_system_performance,
       "the-SMTP-server-has-not-been-configured-yet": the_SMTP_server_has_not_been_configured_yet,
       "snapshot-license-expired": snapshot_license_expired,
       "failed-to-take-snapshot-of-pair-target-volume": failed_to_take_snapshot_of_pair_target_volume,
       "the-exception-of-the-snapshot-schedule-prune-rule-occurred": the_exception_of_the_snapshot_schedule_prune_rule_occurred,
       "maximum-snapshot-amount-of-the-volume-reached": maximum_snapshot_amount_of_the_volume_reached,
       "maximum-snapshot-amount-of-the-system-reached": maximum_snapshot_amount_of_the_system_reached,
       "snapshot-schedule-failed-Some-flush-agents-cannot-be-connected": snapshot_schedule_failed_Some_flush_agents_cannot_be_connected,
       "snapshot-schedule-failed-Host-volume-disk-can-not-be-locked": snapshot_schedule_failed_Host_volume_disk_can_not_be_locked,
       "snapshot-schedule-failed-Host-cache-flush-failed": snapshot_schedule_failed_Host_cache_flush_failed,
       "snapshot-schedule-failed-Host-volume-disk-has-been-locked": snapshot_schedule_failed_Host_volume_disk_has_been_locked,
       "snapshot-schedule-failed-Host-cache-data-flush-has-timed-out": snapshot_schedule_failed_Host_cache_data_flush_has_timed_out,
       "snapshot-schedule-failed-Host-flush-the-database-cache-failed": snapshot_schedule_failed_Host_flush_the_database_cache_failed,
       "snapshot-schedule-failed-File-system-does-not-mount-the-volume": snapshot_schedule_failed_File_system_does_not_mount_the_volume,
       "snapshot-schedule-failed-Volume-has-not-been-mapped-to-host": snapshot_schedule_failed_Volume_has_not_been_mapped_to_host,
       "snapshot-schedule-failed-Exception-has-occurred": snapshot_schedule_failed_Exception_has_occurred,
       "snapshot-schedule-failed-The-volume-has-not-been-mapped": snapshot_schedule_failed_The_volume_has_not_been_mapped,
       "the-snapshot-schedule-has-failed-to-unlock-the-host-volume-disk": the_snapshot_schedule_has_failed_to_unlock_the_host_volume_disk,
       "the-snapshot-schedule-has-failed-to-resume-the-host-database": the_snapshot_schedule_has_failed_to_resume_the_host_database,
       "snapshot-schedule-failed-Flush-settings-have-not-configured": snapshot_schedule_failed_Flush_settings_have_not_configured,
       "snapshot-schedule-and-backup-to-cloud-failed-Exception-occur": snapshot_schedule_and_backup_to_cloud_failed_Exception_occur,
       "failed-to-execute-the-snapshot-schedule": failed_to_execute_the_snapshot_schedule,
       "snapshot-schedule-failed-The-device-can-not-be-connected": snapshot_schedule_failed_The_device_can_not_be_connected,
       "the-storage-tiering-license-of-the-device-has-expired": the_storage_tiering_license_of_the_device_has_expired,
       "tier-migration-schedule-failed-Previous-process-is-processing": tier_migration_schedule_failed_Previous_process_is_processing,
       "tier-migration-schedule-failed-Specified-volumes-are-not-found": tier_migration_schedule_failed_Specified_volumes_are_not_found,
       "tier-migration-schedule-rejected-The-storage-has-one-tier": tier_migration_schedule_rejected_The_storage_has_one_tier,
       "tier-migration-schedule-failed-Exception-has-occurred": tier_migration_schedule_failed_Exception_has_occurred,
       "volume-replication-schedule-failed-Target-volume-mapped": volume_replication_schedule_failed_Target_volume_mapped,
       "the-volume-mirror-license-of-the-device-has-expired": the_volume_mirror_license_of_the_device_has_expired,
       "volume-mirror-schedule-failed-Exceptions-have-occurred": volume_mirror_schedule_failed_Exceptions_have_occurred,
       "volume-mirror-schedule-failed-Exception-has-occurred": volume_mirror_schedule_failed_Exception_has_occurred,
       "volume-mirror-schedule-failed-The-source-volume-is-not-mapped": volume_mirror_schedule_failed_The_source_volume_is_not_mapped,
       "volume-mirror-schedule-failed-Flush-agents-not-connected": volume_mirror_schedule_failed_Flush_agents_not_connected,
       "the-volume-copy-license-of-the-device-has-expired": the_volume_copy_license_of_the_device_has_expired,
       "volume-copy-schedule-failed-Exception-has-occurred": volume_copy_schedule_failed_Exception_has_occurred,
       "user-s-password-has-been-changed": user_s_password_has_been_changed,
       "user-s-password-has-expired": user_s_password_has_expired,
       "the-password-policy-has-been-enabled": the_password_policy_has_been_enabled,
       "the-settings-of-the-password-policy-have-been-changed": the_settings_of_the_password_policy_have_been_changed,
       "the-password-policy-has-been-disabled": the_password_policy_has_been_disabled,
       "the-service-status-abnormal-has-beendetected": the_service_status_abnormal_has_beendetected,
       "the-service-status-has-returned-to-normal": the_service_status_has_returned_to_normal,
       "abnormal-status-service-will-be-reactivated-in-a-few-minutes": abnormal_status_service_will_be_reactivated_in_a_few_minutes,
       "the-service-has-been-reactivated-successfully": the_service_has_been_reactivated_successfully,
       "failed-to-reactivated-the-abnormal-service": failed_to_reactivated_the_abnormal_service,
       "a-user-has-been-created": a_user_has_been_created,
       "a-user-has-been-assigned-to-the-specific-groups": a_user_has_been_assigned_to_the_specific_groups,
       "the-superuser-privilege-has-been-assigned-to-a-specific-user": the_superuser_privilege_has_been_assigned_to_a_specific_user,
       "the-superuser-privilege-for-a-specific-user-has-been-stopped": the_superuser_privilege_for_a_specific_user_has_been_stopped,
       "a-user-account-has-been-deleted": a_user_account_has_been_deleted,
       "a-user-group-has-been-created": a_user_group_has_been_created,
       "a-user-group-has-been-deleted": a_user_group_has_been_deleted,
       "a-user-group-added-users": a_user_group_added_users,
       "a-user-group-removed-users": a_user_group_removed_users,
       "a-service-has-been-started-successfully": a_service_has_been_started_successfully,
       "a-service-has-been-restarted-successfully": a_service_has_been_restarted_successfully,
       "a-service-has-been-stopped-successfully": a_service_has_been_stopped_successfully,
       "the-configuration-of-a-service-has-been-applied-successfully": the_configuration_of_a_service_has_been_applied_successfully,
       "failed-to-start-a-data-service": failed_to_start_a_data_service,
       "failed-to-start-an-authentication-service": failed_to_start_an_authentication_service,
       "failed-to-restart-a-data-service": failed_to_restart_a_data_service,
       "failed-to-restart-an-authentication-service": failed_to_restart_an_authentication_service,
       "failed-to-stop-a-data-service": failed_to_stop_a_data_service,
       "failed-to-stop-an-authentication-service": failed_to_stop_an_authentication_service,
       "failed-to-set-the-configuration-of-a-data-service": failed_to_set_the_configuration_of_a_data_service,
       "failed-to-set-the-configuration-of-an-authentication-service": failed_to_set_the_configuration_of_an_authentication_service,
       "a-folder-has-been-added-into-share-configuration": a_folder_has_been_added_into_share_configuration,
       "a-folder-has-been-removed-from-share-configuration": a_folder_has_been_removed_from_share_configuration,
       "the-share-configuration-of-a-folder-has-been-applied": the_share_configuration_of_a_folder_has_been_applied,
       "failed-to-add-a-folder-into-share-configuration": failed_to_add_a_folder_into_share_configuration,
       "failed-to-remove-a-folder-from-share-configuration": failed_to_remove_a_folder_from_share_configuration,
       "failed-to-apply-the-share-configuration-of-a-folder": failed_to_apply_the_share_configuration_of_a_folder,
       "remote-replication-test-failed-The-target-folder-is-invalid": remote_replication_test_failed_The_target_folder_is_invalid,
       "remote-replication-test-failed-No-response-from-remote-host": remote_replication_test_failed_No_response_from_remote_host,
       "remote-replication-test-failed-Username-or-password-is-invalid": remote_replication_test_failed_Username_or_password_is_invalid,
       "a-remote-replication-task-has-been-deleted": a_remote_replication_task_has_been_deleted,
       "failed-to-delete-a-remote-replication-task": failed_to_delete_a_remote_replication_task,
       "the-backup-operation-of-a-remote-repllication-task-has-started": the_backup_operation_of_a_remote_repllication_task_has_started,
       "failed-to-activate-the-backup-of-a-remote-replication-task": failed_to_activate_the_backup_of_a_remote_replication_task,
       "a-remote-replication-task-has-stopped": a_remote_replication_task_has_stopped,
       "failed-to-stop-a-remote-replication-task": failed_to_stop_a_remote_replication_task,
       "the-restoration-of-a-remote-replication-task-has-begun": the_restoration_of_a_remote_replication_task_has_begun,
       "failed-to-restore-from-source-to-target-of-a-replication-task": failed_to_restore_from_source_to_target_of_a_replication_task,
       "the-restoration-of-a-remote-replication-task-has-completed": the_restoration_of_a_remote_replication_task_has_completed,
       "failed-to-restore-from-target-to-source-of-a-replication-task": failed_to_restore_from_target_to_source_of_a_replication_task,
       "a-remote-replication-task-has-been-completed": a_remote_replication_task_has_been_completed,
       "failed-to-replicate-from-source-to-target-of-a-replication-task": failed_to_replicate_from_source_to_target_of_a_replication_task,
       "the-target-folder-of-a-replication-has-insufficient-capacity": the_target_folder_of_a_replication_has_insufficient_capacity,
       "remote-replication-task-failed-to-start-Netowrk-timeoout": remote_replication_task_failed_to_start_Netowrk_timeoout,
       "a-remote-replication-task-has-been-created": a_remote_replication_task_has_been_created,
       "failed-to-create-remote-replication-task": failed_to_create_remote_replication_task,
       "a-schedule-has-been-created": a_schedule_has_been_created,
       "failed-to-create-a-schedule": failed_to_create_a_schedule,
       "a-schedule-has-been-enabled": a_schedule_has_been_enabled,
       "failed-to-enable-a-schedule": failed_to_enable_a_schedule,
       "a-schedule-has-been-disabled": a_schedule_has_been_disabled,
       "failed-to-disabled-a-schedule": failed_to_disabled_a_schedule,
       "a-schedule-has-been-deleted": a_schedule_has_been_deleted,
       "failed-to-delete-a-schedule": failed_to_delete_a_schedule,
       "a-instance-of-a-schedule-task-is-still-running": a_instance_of_a_schedule_task_is_still_running,
       "a-drive-has-been-inserted": a_drive_has_been_inserted,
       "a-drive-has-been-unplugged": a_drive_has_been_unplugged,
       "a-file-system-has-been-created": a_file_system_has_been_created,
       "failed-to-created-a-file-system": failed_to_created_a_file_system,
       "a-file-system-has-been-deleted": a_file_system_has_been_deleted,
       "failed-to-delete-a-file-system": failed_to_delete_a_file_system,
       "a-folder-has-been-created-in-the-file-system": a_folder_has_been_created_in_the_file_system,
       "failed-to-a-folder-in-the-file-system": failed_to_a_folder_in_the_file_system,
       "a-folder-has-been-deleted": a_folder_has_been_deleted,
       "failed-to-delete-a-folder": failed_to_delete_a_folder,
       "the-system-enter-single-controller-mode": the_system_enter_single_controller_mode,
       "a-controller-has-been-booted-completely": a_controller_has_been_booted_completely,
       "a-controller-can-t-be-detected-System-will-reboot-to-recovery": a_controller_can_t_be_detected_System_will_reboot_to_recovery,
       "the-configuration-broken-by-power-outage-has-been-recovered": the_configuration_broken_by_power_outage_has_been_recovered,
       "detected-controller-failure-Ffailover-process-will-be-launched": detected_controller_failure_Ffailover_process_will_be_launched,
       "the-controller-failover-process-has-been-completed": the_controller_failover_process_has_been_completed,
       "failed-controller-recovered-Failback-process-will-be-launched": failed_controller_recovered_Failback_process_will_be_launched,
       "the-controller-failback-process-has-been-completed": the_controller_failback_process_has_been_completed,
       "a-controller-has-been-unplugged": a_controller_has_been_unplugged,
       "a-controller-has-been-inserted": a_controller_has_been_inserted,
       "network-connection-of-a-controller-has-been-restored": network_connection_of_a_controller_has_been_restored,
       "netwrok-connection-of-a-controller-is-disconnected": netwrok_connection_of_a_controller_is_disconnected,
       "a-interface-of-a-controller-from-aggregation-group-restored": a_interface_of_a_controller_from_aggregation_group_restored,
       "a-interface-of-a-controller-from-aggregation-group-is-abnormal": a_interface_of_a_controller_from_aggregation_group_is_abnormal,
       "the-address-mode-of-an-interface-has-been-changed": the_address_mode_of_an_interface_has_been_changed,
       "the-MTU-size-of-a-interface-has-been-changed": the_MTU_size_of_a_interface_has_been_changed,
       "a-DNS-server-has-been-added-to-the-server-list": a_DNS_server_has_been_added_to_the_server_list,
       "a-DNS-server-has-been-removed-from-the-server-list": a_DNS_server_has_been_removed_from_the_server_list,
       "a-DNS-suffix-has-been-added": a_DNS_suffix_has_been_added,
       "a-DNS-suffix-has-been-removed": a_DNS_suffix_has_been_removed,
       "a-port-aggregation-group-has-been-created": a_port_aggregation_group_has_been_created,
       "a-port-aggregation-group-has-been-removed": a_port_aggregation_group_has_been_removed,
       "route-rule-has-been-added-successfully": route_rule_has_been_added_successfully,
       "route-rule-has-been-removed-successfully": route_rule_has_been_removed_successfully,
       "failed-to-set-IP-configuration-on-an-interface": failed_to_set_IP_configuration_on_an_interface,
       "failed-to-set-MTU-size-on-an-interface": failed_to_set_MTU_size_on_an_interface,
       "failed-to-add-a-DNS-server": failed_to_add_a_DNS_server,
       "failed-to-remove-a-DNS-server": failed_to_remove_a_DNS_server,
       "failed-to-add-a-DNS-suffix": failed_to_add_a_DNS_suffix,
       "failed-to-remove-a-DNS-suffix": failed_to_remove_a_DNS_suffix,
       "failed-to-create-a-port-aggregation-group": failed_to_create_a_port_aggregation_group,
       "failed-to-remove-a-prot-aggregation-group": failed_to_remove_a_prot_aggregation_group,
       "failed-to-add-an-Route-rule": failed_to_add_an_Route_rule,
       "failed-to-remove-an-Route-rule": failed_to_remove_an_Route_rule,
       "the-usage-of-the-coredump-folder-is-over-90-percent": the_usage_of_the_coredump_folder_is_over_90_percent,
       "the-space-used-by-a-folder-has-exceeded-monitoring-threshold": the_space_used_by_a_folder_has_exceeded_monitoring_threshold,
       "the-ipblock-configuration-has-been-applied-on-a-controller": the_ipblock_configuration_has_been_applied_on_a_controller,
       "failed-to-apply-the-ipblock-configuration-on-a-controller": failed_to_apply_the_ipblock_configuration_on_a_controller,
       "a-IP-address-has-been-removed-on-a-controller": a_IP_address_has_been_removed_on_a_controller,
       "failed-to-remove-a-IP-address-from-ipblock-configuration": failed_to_remove_a_IP_address_from_ipblock_configuration,
       "a-IP-address-was-lbocked-The-maximum-login-attempts-exceeded": a_IP_address_was_lbocked_The_maximum_login_attempts_exceeded,
       "failed-to-ban-a-IP-address-on-a-controller": failed_to_ban_a_IP_address_on_a_controller,
       "detect-a-IP-address-has-been-banned-by-system-on-a-controller": detect_a_IP_address_has_been_banned_by_system_on_a_controller,
       "a-schedule-task-has-started": a_schedule_task_has_started,
       "failed-to-start-a-schedule-task": failed_to_start_a_schedule_task,
       "failed-to-restore-the-whitelist-or-blacklist": failed_to_restore_the_whitelist_or_blacklist,
       "a-user-failed-to-log-in-from-a-IP-address": a_user_failed_to_log_in_from_a_IP_address,
       "the-LDAP-server-failed-to-add-a-user-from-the-CSV-file": the_LDAP_server_failed_to_add_a_user_from_the_CSV_file,
       "a-user-has-nearly-reached-the-quota-limit-on-a-volume": a_user_has_nearly_reached_the_quota_limit_on_a_volume,
       "the-LDAP-server-failed-to-add-users-in-batch-mode": the_LDAP_server_failed_to_add_users_in_batch_mode,
       "the-AD-or-LDAP-server-has-been-disconnected-from-a-controller": the_AD_or_LDAP_server_has_been_disconnected_from_a_controller,
       "the-AD-or-LDAP-server-connection-to-controller-has-been-restored": the_AD_or_LDAP_server_connection_to_controller_has_been_restored,
       "all-volumes-have-been-deactivated": all_volumes_have_been_deactivated,
       "all-volumes-have-been-reactivated": all_volumes_have_been_reactivated,
       "a-service-port-setting-has-conflict-with-another-service": a_service_port_setting_has_conflict_with_another_service,
       "an-application-server-has-been-started-successfully": an_application_server_has_been_started_successfully,
       "an-application-server-has-been-restarted-successfully": an_application_server_has_been_restarted_successfully,
       "an-application-server-has-been-stopped-successfully": an_application_server_has_been_stopped_successfully,
       "an-application-server-has-been-configured-successfully": an_application_server_has_been_configured_successfully,
       "failed-to-start-an-application-server": failed_to_start_an_application_server,
       "failed-to-restart-an-application-server": failed_to_restart_an_application_server,
       "failed-to-stop-an-application-server": failed_to_stop_an_application_server,
       "failed-to-configure-an-application-server": failed_to_configure_an_application_server,
       "app-server-stopped-Folder-for-saving-data-can-not-be-accessed": app_server_stopped_Folder_for_saving_data_can_not_be_accessed,
       "failed-to-backup-LDAP-DB-Folder-for-data-can-not-be-accessed": failed_to_backup_LDAP_DB_Folder_for_data_can_not_be_accessed,
       "failed-to-backup-LDAP-DB-Folder-may-assigned-to-sec-controller": failed_to_backup_LDAP_DB_Folder_may_assigned_to_sec_controller,
       "syncCloud-service-started-successfully": syncCloud_service_started_successfully,
       "failed-to-start-SyncCloud-service": failed_to_start_SyncCloud_service,
       "syncCloud-service-stopped-successfully": syncCloud_service_stopped_successfully,
       "failed-to-stop-SyncCloud-service": failed_to_stop_SyncCloud_service,
       "failed-to-fetch-SyncCloud-database-Service-has-been-disabled": failed_to_fetch_SyncCloud_database_Service_has_been_disabled,
       "a-volume-has-duplicated-name-for-file-service-cannot-be-mounted": a_volume_has_duplicated_name_for_file_service_cannot_be_mounted,
       "the-size-of-a-folder-has-exceeded-the-quota-alert-threshold": the_size_of_a_folder_has_exceeded_the_quota_alert_threshold,
       "ipv4-address-conflict-detected": ipv4_address_conflict_detected,
       "ipv6-address-conflict-detected": ipv6_address_conflict_detected,
       "failed-to-initialize-the-SyncCloud-database": failed_to_initialize_the_SyncCloud_database,
       "the-SyncCloud-task-failed": the_SyncCloud_task_failed,
       "file-system-usage-exceeds-threshold": file_system_usage_exceeds_threshold,
       "file-system-usage-exceeds-90-percent": file_system_usage_exceeds_90_percent,
       "the-file-system-of-the-volume-has-been-repaired": the_file_system_of_the_volume_has_been_repaired,
       "failed-to-repair-the-file-system-of-the-volume": failed_to_repair_the_file_system_of_the_volume,
       "failed-to-upgrade-the-LDAP-server-service": failed_to_upgrade_the_LDAP_server_service,
       "the-LDAP-server-service-has-been-upgraded": the_LDAP_server_service_has_been_upgraded,
       "ldap-server-has-been-disabled-Folder-for-data-is-not-found": ldap_server_has_been_disabled_Folder_for_data_is_not_found,
       "ldap-server-has-been-disabled-The-settings-are-incomplete": ldap_server_has_been_disabled_The_settings_are_incomplete,
       "ldap-server-has-been-disabled-The-database-was-corrupted": ldap_server_has_been_disabled_The_database_was_corrupted,
       "failed-to-connect-to-AD-server-Incorrect-username-or-password": failed_to_connect_to_AD_server_Incorrect_username_or_password,
       "failed-to-connect-to-AD-server-KDC-server-is-not-found": failed_to_connect_to_AD_server_KDC_server_is_not_found,
       "the-AD-server-is-unreachable": the_AD_server_is_unreachable,
       "not-enough-privilege-for-the-AD-user-to-join-the-domain": not_enough_privilege_for_the_AD_user_to_join_the_domain,
       "failed-to-connect-LDAP-server-Incorrect-username-or-password": failed_to_connect_LDAP_server_Incorrect_username_or_password,
       "the-LDAP-server-is-unreachable": the_LDAP_server_is_unreachable,
       "failed-to-connect-to-the-LDAP-server-The-base-DN-is-incorrect": failed_to_connect_to_the_LDAP_server_The_base_DN_is_incorrect,
       "cloud-sync-service-started-successfully": cloud_sync_service_started_successfully,
       "failed-to-start-cloud-sync-service": failed_to_start_cloud_sync_service,
       "cloud-sync-service-stopped-successfully": cloud_sync_service_stopped_successfully,
       "failed-to-stop-cloud-sync-service": failed_to_stop_cloud_sync_service,
       "failed-to-fetch-cloud-sync-database-service-has-been-disabled": failed_to_fetch_cloud_sync_database_service_has_been_disabled,
       "failed-to-initial-the-cloud-sync-database": failed_to_initial_the_cloud_sync_database,
       "the-cloud-sync-task-failed-due-to-network-problems": the_cloud_sync_task_failed_due_to_network_problems,
       "the-antivirus-scan-job-has-been-stopped": the_antivirus_scan_job_has_been_stopped,
       "the-antivirus-scheduled-scan-job-has-been-completed": the_antivirus_scheduled_scan_job_has_been_completed,
       "the-NVR-server-crash-detected-Recovery-process-will-be-start": the_NVR_server_crash_detected_Recovery_process_will_be_start,
       "the-NVR-server-has-been-recovered": the_NVR_server_has_been_recovered,
       "failed-to-recover-the-NVR-server": failed_to_recover_the_NVR_server,
       "eventString": eventString}
)
