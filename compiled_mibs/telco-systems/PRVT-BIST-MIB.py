# SNMP MIB module (PRVT-BIST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-BIST-MIB

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

(reportsL2IfacePort,
 reportsL2IfaceSlot,
 reportsL2IfaceUnit,
 switch) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "reportsL2IfacePort",
    "reportsL2IfaceSlot",
    "reportsL2IfaceUnit",
    "switch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

prvtBISTMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108)
)
if mibBuilder.loadTexts:
    prvtBISTMib.setRevisions(
        ("2005-02-16 00:00",
         "2004-10-14 00:00",
         "2003-11-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TestResult(TextualConvention, Integer32):
    status = "current"
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
        *(("passed", 1),
          ("failed", 2),
          ("unknown", 3),
          ("notAvailable", 4))
    )



# MIB Managed Objects in the order of their OIDs

_PrvtBISTNotifications_ObjectIdentity = ObjectIdentity
prvtBISTNotifications = _PrvtBISTNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 0)
)
_PrvtBISTObjects_ObjectIdentity = ObjectIdentity
prvtBISTObjects = _PrvtBISTObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1)
)
_BistConfig_ObjectIdentity = ObjectIdentity
bistConfig = _BistConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 1)
)


class _BistSelfTestExecute_Type(Integer32):
    """Custom type bistSelfTestExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("execute", 2))
    )


_BistSelfTestExecute_Type.__name__ = "Integer32"
_BistSelfTestExecute_Object = MibScalar
bistSelfTestExecute = _BistSelfTestExecute_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 1, 1),
    _BistSelfTestExecute_Type()
)
bistSelfTestExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bistSelfTestExecute.setStatus("current")
_BistStatus_ObjectIdentity = ObjectIdentity
bistStatus = _BistStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 2)
)


class _BistSelfTestExecuteStatus_Type(Integer32):
    """Custom type bistSelfTestExecuteStatus based on Integer32"""
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
        *(("not-started", 1),
          ("in-progress", 2),
          ("success", 3),
          ("error", 4))
    )


_BistSelfTestExecuteStatus_Type.__name__ = "Integer32"
_BistSelfTestExecuteStatus_Object = MibScalar
bistSelfTestExecuteStatus = _BistSelfTestExecuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 2, 1),
    _BistSelfTestExecuteStatus_Type()
)
bistSelfTestExecuteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistSelfTestExecuteStatus.setStatus("current")
_BistResult_ObjectIdentity = ObjectIdentity
bistResult = _BistResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3)
)
_BistCPU_ObjectIdentity = ObjectIdentity
bistCPU = _BistCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 1)
)
_CPUTestTable_Object = MibTable
cPUTestTable = _CPUTestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cPUTestTable.setStatus("current")
_CPUTestEntry_Object = MibTableRow
cPUTestEntry = _CPUTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 1, 1, 1)
)
cPUTestEntry.setIndexNames(
    (0, "PRVT-BIST-MIB", "cpuTestType"),
)
if mibBuilder.loadTexts:
    cPUTestEntry.setStatus("current")


class _CpuTestType_Type(Integer32):
    """Custom type cpuTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bistCPUValidation", 1),
          ("bistCPUUsage", 2))
    )


_CpuTestType_Type.__name__ = "Integer32"
_CpuTestType_Object = MibTableColumn
cpuTestType = _CpuTestType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 1, 1, 1, 1),
    _CpuTestType_Type()
)
cpuTestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpuTestType.setStatus("current")
_CpuTestResult_Type = TestResult
_CpuTestResult_Object = MibTableColumn
cpuTestResult = _CpuTestResult_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 1, 1, 1, 2),
    _CpuTestResult_Type()
)
cpuTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTestResult.setStatus("current")
_BistRAM_ObjectIdentity = ObjectIdentity
bistRAM = _BistRAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 2)
)
_RamTestTable_Object = MibTable
ramTestTable = _RamTestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ramTestTable.setStatus("current")
_RamTestEntry_Object = MibTableRow
ramTestEntry = _RamTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 2, 1, 1)
)
ramTestEntry.setIndexNames(
    (0, "PRVT-BIST-MIB", "ramTestType"),
)
if mibBuilder.loadTexts:
    ramTestEntry.setStatus("current")


class _RamTestType_Type(Integer32):
    """Custom type ramTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bistRAMValidation", 1),
          ("bistRAMUsage", 2))
    )


_RamTestType_Type.__name__ = "Integer32"
_RamTestType_Object = MibTableColumn
ramTestType = _RamTestType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 2, 1, 1, 1),
    _RamTestType_Type()
)
ramTestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ramTestType.setStatus("current")
_RamTestResult_Type = TestResult
_RamTestResult_Object = MibTableColumn
ramTestResult = _RamTestResult_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 2, 1, 1, 2),
    _RamTestResult_Type()
)
ramTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ramTestResult.setStatus("current")
_BistUART_ObjectIdentity = ObjectIdentity
bistUART = _BistUART_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 3)
)
_UartExistTestTable_Object = MibTable
uartExistTestTable = _UartExistTestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    uartExistTestTable.setStatus("current")
_UartExistTestEntry_Object = MibTableRow
uartExistTestEntry = _UartExistTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 3, 1, 1)
)
uartExistTestEntry.setIndexNames(
    (0, "PRVT-BIST-MIB", "uartIndex"),
)
if mibBuilder.loadTexts:
    uartExistTestEntry.setStatus("current")


class _UartIndex_Type(Integer32):
    """Custom type uartIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UartIndex_Type.__name__ = "Integer32"
_UartIndex_Object = MibTableColumn
uartIndex = _UartIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 3, 1, 1, 1),
    _UartIndex_Type()
)
uartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uartIndex.setStatus("current")
_UartExistTestResult_Type = TestResult
_UartExistTestResult_Object = MibTableColumn
uartExistTestResult = _UartExistTestResult_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 3, 1, 1, 2),
    _UartExistTestResult_Type()
)
uartExistTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uartExistTestResult.setStatus("current")
_BistSwitchCore_ObjectIdentity = ObjectIdentity
bistSwitchCore = _BistSwitchCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 4)
)
_BistCrossbarExistence_Type = TestResult
_BistCrossbarExistence_Object = MibScalar
bistCrossbarExistence = _BistCrossbarExistence_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 4, 1),
    _BistCrossbarExistence_Type()
)
bistCrossbarExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistCrossbarExistence.setStatus("current")
_BistNVRAM_ObjectIdentity = ObjectIdentity
bistNVRAM = _BistNVRAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 5)
)
_NvramTestTable_Object = MibTable
nvramTestTable = _NvramTestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    nvramTestTable.setStatus("current")
_NvramTestEntry_Object = MibTableRow
nvramTestEntry = _NvramTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 5, 1, 1)
)
nvramTestEntry.setIndexNames(
    (0, "PRVT-BIST-MIB", "nvramTestType"),
)
if mibBuilder.loadTexts:
    nvramTestEntry.setStatus("current")


class _NvramTestType_Type(Integer32):
    """Custom type nvramTestType based on Integer32"""
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
        *(("bistBootLoaderValidation", 1),
          ("bistApplicationValidation", 2),
          ("bistStartupConfigValidation", 3),
          ("bistScriptFileSystemValidation", 4),
          ("bistJavaImageValidation", 5),
          ("bistPROMValidation", 6))
    )


_NvramTestType_Type.__name__ = "Integer32"
_NvramTestType_Object = MibTableColumn
nvramTestType = _NvramTestType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 5, 1, 1, 1),
    _NvramTestType_Type()
)
nvramTestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nvramTestType.setStatus("current")
_NvramTestResult_Type = TestResult
_NvramTestResult_Object = MibTableColumn
nvramTestResult = _NvramTestResult_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 5, 1, 1, 2),
    _NvramTestResult_Type()
)
nvramTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramTestResult.setStatus("current")
_BistPowerSupply_ObjectIdentity = ObjectIdentity
bistPowerSupply = _BistPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 6)
)
_PowerSupplyTestTable_Object = MibTable
powerSupplyTestTable = _PowerSupplyTestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    powerSupplyTestTable.setStatus("current")
_PowerSupplyTestEntry_Object = MibTableRow
powerSupplyTestEntry = _PowerSupplyTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 6, 1, 1)
)
powerSupplyTestEntry.setIndexNames(
    (0, "PRVT-BIST-MIB", "powerSupplyIndex"),
)
if mibBuilder.loadTexts:
    powerSupplyTestEntry.setStatus("current")


class _PowerSupplyIndex_Type(Integer32):
    """Custom type powerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PowerSupplyIndex_Type.__name__ = "Integer32"
_PowerSupplyIndex_Object = MibTableColumn
powerSupplyIndex = _PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 6, 1, 1, 1),
    _PowerSupplyIndex_Type()
)
powerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerSupplyIndex.setStatus("current")
_PowerSupplyTestResult_Type = TestResult
_PowerSupplyTestResult_Object = MibTableColumn
powerSupplyTestResult = _PowerSupplyTestResult_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 6, 1, 1, 2),
    _PowerSupplyTestResult_Type()
)
powerSupplyTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyTestResult.setStatus("current")
_BistOnboardPower_ObjectIdentity = ObjectIdentity
bistOnboardPower = _BistOnboardPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 7)
)
_OnboardPowerTestTable_Object = MibTable
onboardPowerTestTable = _OnboardPowerTestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 7, 1)
)
if mibBuilder.loadTexts:
    onboardPowerTestTable.setStatus("current")
_OnboardPowerTestEntry_Object = MibTableRow
onboardPowerTestEntry = _OnboardPowerTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 7, 1, 1)
)
onboardPowerTestEntry.setIndexNames(
    (0, "PRVT-BIST-MIB", "onboardPowerTestType"),
)
if mibBuilder.loadTexts:
    onboardPowerTestEntry.setStatus("current")


class _OnboardPowerTestType_Type(Integer32):
    """Custom type onboardPowerTestType based on Integer32"""
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
        *(("bistOnboardPowerPHY", 1),
          ("bistOnboardPowerCPU", 2),
          ("bistOnboardPowerOC", 3),
          ("bistOnboardPower3-2V", 4),
          ("bistOnboardPower2-5V", 5),
          ("bistOnboardPower1-8V", 6),
          ("bistOnboardPower1-5V", 7),
          ("bistOnboardPower1-25V", 8))
    )


_OnboardPowerTestType_Type.__name__ = "Integer32"
_OnboardPowerTestType_Object = MibTableColumn
onboardPowerTestType = _OnboardPowerTestType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 7, 1, 1, 1),
    _OnboardPowerTestType_Type()
)
onboardPowerTestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onboardPowerTestType.setStatus("current")
_OnboardPowerTestResult_Type = TestResult
_OnboardPowerTestResult_Object = MibTableColumn
onboardPowerTestResult = _OnboardPowerTestResult_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 7, 1, 1, 2),
    _OnboardPowerTestResult_Type()
)
onboardPowerTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onboardPowerTestResult.setStatus("current")
_BistFan_ObjectIdentity = ObjectIdentity
bistFan = _BistFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 8)
)
_FanTestTable_Object = MibTable
fanTestTable = _FanTestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 8, 1)
)
if mibBuilder.loadTexts:
    fanTestTable.setStatus("current")
_FanTestEntry_Object = MibTableRow
fanTestEntry = _FanTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 8, 1, 1)
)
fanTestEntry.setIndexNames(
    (0, "PRVT-BIST-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanTestEntry.setStatus("current")


class _FanIndex_Type(Integer32):
    """Custom type fanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FanIndex_Type.__name__ = "Integer32"
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 8, 1, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanIndex.setStatus("current")
_FanTestResult_Type = TestResult
_FanTestResult_Object = MibTableColumn
fanTestResult = _FanTestResult_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 8, 1, 1, 2),
    _FanTestResult_Type()
)
fanTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanTestResult.setStatus("current")
_BistTemperature_ObjectIdentity = ObjectIdentity
bistTemperature = _BistTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 9)
)
_BistTemperatureTest_Type = TestResult
_BistTemperatureTest_Object = MibScalar
bistTemperatureTest = _BistTemperatureTest_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 9, 1),
    _BistTemperatureTest_Type()
)
bistTemperatureTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistTemperatureTest.setStatus("current")
_BistUPS_ObjectIdentity = ObjectIdentity
bistUPS = _BistUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 10)
)
_BistUPSTest_Type = TestResult
_BistUPSTest_Object = MibScalar
bistUPSTest = _BistUPSTest_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 10, 1),
    _BistUPSTest_Type()
)
bistUPSTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bistUPSTest.setStatus("current")
_BistPorts_ObjectIdentity = ObjectIdentity
bistPorts = _BistPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 11)
)
_PortsTestTable_Object = MibTable
portsTestTable = _PortsTestTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 11, 1)
)
if mibBuilder.loadTexts:
    portsTestTable.setStatus("current")
_PortsTestEntry_Object = MibTableRow
portsTestEntry = _PortsTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 11, 1, 1)
)
portsTestEntry.setIndexNames(
    (0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"),
    (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"),
    (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"),
)
if mibBuilder.loadTexts:
    portsTestEntry.setStatus("current")
_PortTest_Type = TestResult
_PortTest_Object = MibTableColumn
portTest = _PortTest_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 1, 3, 11, 1, 1, 1),
    _PortTest_Type()
)
portTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTest.setStatus("current")
_PrvtBISTConformance_ObjectIdentity = ObjectIdentity
prvtBISTConformance = _PrvtBISTConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 108, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-BIST-MIB",
    **{"TestResult": TestResult,
       "prvtBISTMib": prvtBISTMib,
       "prvtBISTNotifications": prvtBISTNotifications,
       "prvtBISTObjects": prvtBISTObjects,
       "bistConfig": bistConfig,
       "bistSelfTestExecute": bistSelfTestExecute,
       "bistStatus": bistStatus,
       "bistSelfTestExecuteStatus": bistSelfTestExecuteStatus,
       "bistResult": bistResult,
       "bistCPU": bistCPU,
       "cPUTestTable": cPUTestTable,
       "cPUTestEntry": cPUTestEntry,
       "cpuTestType": cpuTestType,
       "cpuTestResult": cpuTestResult,
       "bistRAM": bistRAM,
       "ramTestTable": ramTestTable,
       "ramTestEntry": ramTestEntry,
       "ramTestType": ramTestType,
       "ramTestResult": ramTestResult,
       "bistUART": bistUART,
       "uartExistTestTable": uartExistTestTable,
       "uartExistTestEntry": uartExistTestEntry,
       "uartIndex": uartIndex,
       "uartExistTestResult": uartExistTestResult,
       "bistSwitchCore": bistSwitchCore,
       "bistCrossbarExistence": bistCrossbarExistence,
       "bistNVRAM": bistNVRAM,
       "nvramTestTable": nvramTestTable,
       "nvramTestEntry": nvramTestEntry,
       "nvramTestType": nvramTestType,
       "nvramTestResult": nvramTestResult,
       "bistPowerSupply": bistPowerSupply,
       "powerSupplyTestTable": powerSupplyTestTable,
       "powerSupplyTestEntry": powerSupplyTestEntry,
       "powerSupplyIndex": powerSupplyIndex,
       "powerSupplyTestResult": powerSupplyTestResult,
       "bistOnboardPower": bistOnboardPower,
       "onboardPowerTestTable": onboardPowerTestTable,
       "onboardPowerTestEntry": onboardPowerTestEntry,
       "onboardPowerTestType": onboardPowerTestType,
       "onboardPowerTestResult": onboardPowerTestResult,
       "bistFan": bistFan,
       "fanTestTable": fanTestTable,
       "fanTestEntry": fanTestEntry,
       "fanIndex": fanIndex,
       "fanTestResult": fanTestResult,
       "bistTemperature": bistTemperature,
       "bistTemperatureTest": bistTemperatureTest,
       "bistUPS": bistUPS,
       "bistUPSTest": bistUPSTest,
       "bistPorts": bistPorts,
       "portsTestTable": portsTestTable,
       "portsTestEntry": portsTestEntry,
       "portTest": portTest,
       "prvtBISTConformance": prvtBISTConformance}
)
