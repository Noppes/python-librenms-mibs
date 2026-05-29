# SNMP MIB module (RpsSc300Mib) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\eaton\RpsSc300Mib

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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rpsSc300MibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 1)
)
if mibBuilder.loadTexts:
    rpsSc300MibModule.setRevisions(
        ("2013-03-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Signed8(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )



class Signed16(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )



class Signed32(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class Unsigned8(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class Unsigned16(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class Unsigned31(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483646),
    )



class UnsignedNan8(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("notavailable", 255)
    )



class UnsignedNan16(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65535
        )
    )
    namedValues = NamedValues(
        ("notavailable", 65535)
    )



class UnsignedNan32(TextualConvention, Integer32):
    status = "current"


class Boolean(TextualConvention, Integer32):
    status = "current"
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



class Float(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



class NoData(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
    )
    fixed_length = 0



class TimeIntervalInSeconds(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TimeIntervalInMinutes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483646),
    )



class TimeIntervalInDays(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483646),
    )



class JulianTimeUtc(TextualConvention, OctetString):
    status = "current"
    displayHint = "25t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )



class JulianDateUtc(TextualConvention, OctetString):
    status = "current"
    displayHint = "25t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )



class JulianDateUtc25(TextualConvention, OctetString):
    status = "current"
    displayHint = "25t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )
    fixed_length = 25



class EnableState(TextualConvention, Integer32):
    status = "current"
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



class BaudRate(TextualConvention, Integer32):
    status = "current"
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
        *(("baudRate1200", 0),
          ("baudRate2400", 1),
          ("baudRate4800", 2),
          ("baudRate9600", 3),
          ("baudRate19200", 4),
          ("baudRate38400", 5),
          ("baudRate57600", 6),
          ("baudRate115200", 7),
          ("baudRate250000", 8),
          ("baudRate1843200", 9))
    )



class Parity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("odd", 1),
          ("even", 2))
    )



class StopBits(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )



class SnmpTrapVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpV2Trap", 1),
          ("snmpV3Trap", 3))
    )



class SeverityLevel(TextualConvention, Integer32):
    status = "current"
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
        *(("warningsAndAbove", 1),
          ("minorAndAbove", 2),
          ("majorAndAbove", 3),
          ("none", 4),
          ("criticalOnly", 5))
    )



class YesNo(TextualConvention, Integer32):
    status = "current"
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



class Sysoid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("sc200", 13),
          ("sc300", 14))
    )



class UserSnmp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSnmp", 0),
          ("get", 1),
          ("getSet", 2))
    )



class WebAccess(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("httpsDefaultUser", 1),
          ("http", 2),
          ("https", 3))
    )



class ThreadPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("user", 1),
          ("system", 2),
          ("realtime", 3))
    )



class RectifierShutdownMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("manual", 1),
          ("automatic", 2))
    )



class DcdcHardwareType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("outputUnknown", 0),
          ("output12v", 1),
          ("output24v", 2),
          ("output48v", 3))
    )



class InputType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 0),
          ("dc", 1),
          ("mppt", 2))
    )



class DcPower(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            65535
        )
    )
    namedValues = NamedValues(
        ("notAvailable", 65535)
    )



class Percentile8Nan(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("notAvailable", 255)
    )



class ProductType(TextualConvention, Integer32):
    status = "current"
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
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("sm20", 1),
          ("sm50", 2),
          ("sm30", 3),
          ("sm30Slave", 4),
          ("iom", 5),
          ("cbc", 6),
          ("weir", 7),
          ("sm35", 8),
          ("nesBatteryTray", 9),
          ("sm30SlaveFrontPort", 10),
          ("sm60", 11),
          ("sm40", 12),
          ("sm70Iob", 13),
          ("sm70", 14),
          ("sm45Iob", 15),
          ("sm45", 16),
          ("sm65", 17),
          ("sc200", 18),
          ("sc300", 19))
    )



class AccessLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(80,
              81)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 80),
          ("readWrite", 81))
    )



class SnmpAccessState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("all", 1),
          ("readOnly", 2),
          ("v3Only", 3))
    )



class GenericTrapsEnable(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("coldStartTrapOnly", 1),
          ("none", 2))
    )



class SendTrap(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("both", 1),
          ("activation", 2),
          ("deactivation", 4))
    )



class AlarmReport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("warningsAndAbove", 1),
          ("minorAndAbove", 2),
          ("majorAndAbove", 3),
          ("criticalOnly", 4))
    )



class SnmpTrapFormat(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eaton", 0),
          ("x733", 1))
    )



class AccessProtection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unprotected", 0),
          ("readOnly", 1),
          ("pinProtected", 2))
    )



class CanStart(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224)
        )
    )
    namedValues = NamedValues(
        *(("started", 190),
          ("canStart", 191),
          ("busy", 192),
          ("disabled", 193),
          ("alarmsActive", 194),
          ("sensorFailed", 195),
          ("batteryNotCharged", 196),
          ("noRectifiersNorSolarAvailable", 197),
          ("rectifierOvsd", 198),
          ("noBatteryConfigured", 199),
          ("loadCurrentTooLow", 200),
          ("acFailed", 201),
          ("manualStop", 202),
          ("batteryNotDischarged", 203),
          ("acStateUnavailable", 204),
          ("systemOverloaded", 205),
          ("noPeakLoadReduction", 206),
          ("inLockout", 207),
          ("rectifiersFailed", 208),
          ("rectifiersCommsLost", 209),
          ("systemInOverload", 210),
          ("batteryFuseFail", 211),
          ("batteryTestFail", 212),
          ("bAcFailed", 213),
          ("bAcStateUnavailable", 214),
          ("bNoBatteryConfigured", 215),
          ("bSensorFailed", 216),
          ("bNoRectifiersNorSolarAvailable", 217),
          ("bRectifiersFailed", 218),
          ("bRectifiersCommsLost", 219),
          ("bSystemInOverload", 220),
          ("bBatteryFuseFail", 221),
          ("bBusy", 222),
          ("bBatteryTestFail", 223),
          ("bSystemOverloaded", 224))
    )



class AvcState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(115,
              116,
              117,
              118,
              119)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 115),
          ("inoperative", 116),
          ("active", 117),
          ("lostControl", 118),
          ("inDeadband", 119))
    )



class TcState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(80,
              81,
              82)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 80),
          ("inoperative", 81),
          ("active", 82))
    )



class BatteryTestState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(95,
              96,
              97,
              98,
              99,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 95),
          ("inactive", 96),
          ("active", 97),
          ("failed", 98),
          ("lockedOut", 99),
          ("bActiveAFailed", 100),
          ("aActiveBFailed", 101))
    )



class BatteryChargeState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101,
              102,
              103)
        )
    )
    namedValues = NamedValues(
        *(("float", 100),
          ("discharge", 101),
          ("charge", 102),
          ("unavailable", 103))
    )



class BclState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(110,
              111,
              112,
              113,
              114,
              115,
              116)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 110),
          ("inoperative", 111),
          ("active", 112),
          ("inactive", 113),
          ("lostControl", 114),
          ("inDeadband", 115),
          ("pending", 116))
    )



class EngineRunState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(85,
              86,
              87,
              88)
        )
    )
    namedValues = NamedValues(
        *(("notRunning", 85),
          ("running", 86),
          ("unavailable", 87),
          ("missing", 88))
    )



class RcpSlaveState(TextualConvention, Integer32):
    status = "current"
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
        *(("notDetected", 0),
          ("detected", 1),
          ("registered", 2),
          ("commsLost", 3),
          ("missing", 4),
          ("rebooting", 5))
    )



class TrapAlarmKeepSeverity(TextualConvention, Integer32):
    status = "current"
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("cleared", 5))
    )



class AlarmSeverity(TextualConvention, Integer32):
    status = "current"
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
        *(("disabled", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("control", 5))
    )



class TrapReceiverMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTraps", 1),
          ("acknowledgedSummaryTrap", 2))
    )



class ControlState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("equalize", 1),
          ("fastCharge", 2),
          ("batteryTest", 3),
          ("peakLoadReduction", 4))
    )



class ControlProcessState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("active", 1),
          ("inactive", 2),
          ("pending", 3))
    )



class PeakLoadReductionState(TextualConvention, Integer32):
    status = "current"
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
        *(("disabled", 0),
          ("inactiveNotRunning", 1),
          ("inactiveNoBusVoltage", 2),
          ("inactiveNotEnoughRectifiers", 3),
          ("inactiveExceededMaxDuration", 4),
          ("heldAtMinimumBusVoltage", 5),
          ("activeCharge", 6),
          ("activeDischarge", 7))
    )



class ExternalRelayState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1),
          ("missing", 2),
          ("disabled", 3),
          ("conflict", 4))
    )



class RelayControlState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("automatic", 1),
          ("inactive", 2))
    )



class RectFailState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notFailed", 0),
          ("badStatus", 1),
          ("badOutput", 2))
    )



class AcPhase(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("acPhase1", 0),
          ("acPhase2", 1),
          ("acPhase3", 2),
          ("n", 3),
          ("unknown", 4))
    )



class AlarmType(TextualConvention, Integer32):
    status = "current"
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
        *(("systemAlarm", 0),
          ("aiHigh", 1),
          ("aiLow", 2),
          ("di", 3),
          ("smartAlarm", 4),
          ("do", 5))
    )



class SystemState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("failed", 1),
          ("unavailable", 2),
          ("missing", 3))
    )



class BtrState(TextualConvention, Integer32):
    status = "current"
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
        *(("inoperative", 0),
          ("inactive", 1),
          ("active", 2),
          ("characterizing", 3),
          ("waiting", 4),
          ("notCharacterized", 5))
    )



class EndOfChargeAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setAhDischargedToZeroAfterEqualizeAndFastCharge", 0),
          ("setAhDischargedToZeroAfterFastChargeOnly", 1),
          ("setAhDischargedToZeroAfterEqualizeOnly", 2))
    )



class AlarmActiveState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("activeWarning", 1),
          ("activeMajor", 2),
          ("activeMinor", 3),
          ("reserved", 4),
          ("activeCritical", 5),
          ("activeControl", 6))
    )



class AlarmOperator(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("and", 0),
          ("or", 1),
          ("xor", 2))
    )



class SourceTrigger(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("triggered", 0),
          ("active", 1))
    )



class SourceState(TextualConvention, Integer32):
    status = "current"
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
        *(("inactiveClear", 0),
          ("inactiveArmed", 1),
          ("activeClear", 2),
          ("activeArmed", 3),
          ("cycle", 4),
          ("invalid", 5))
    )



class InDischargeAlarmCondition(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("always", 0),
          ("onlyWhileAcPresent", 1))
    )



class ThresholdType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("low", 1))
    )



class SystemValueSourceValue(TextualConvention, Integer32):
    status = "current"
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("busVoltage", 0),
          ("rectifierCurrent", 1),
          ("loadCurrent", 2),
          ("batteryCurrent", 3),
          ("batteryTemperature", 4),
          ("loadPower", 5),
          ("systemPower", 6),
          ("ahDischarged", 7),
          ("numberOfRectifiersFailed", 8),
          ("numberOfRectifiersCommsLost", 9),
          ("acVoltage", 10),
          ("batteryTimeRemaining", 11),
          ("alternativeSourceCurrent", 12),
          ("highestRectifierHeatsinkTemperature", 13),
          ("fuelLevel", 14),
          ("generatorBackupTime", 15),
          ("fuelRemainingTime", 16),
          ("smartAnalog", 17),
          ("energyMeter", 18),
          ("powerMeter", 19),
          ("currentMeter", 20),
          ("voltageMeter", 21),
          ("solarPower", 22),
          ("rectifierInputVoltage", 23),
          ("solarCurrent", 24),
          ("dcInputVoltage", 25),
          ("generatorCurrent", 26),
          ("batteryHealth", 27),
          ("acInputCurrent", 28),
          ("dcInputCurrent", 29),
          ("operatingVoltage", 30),
          ("fanTemperature", 31),
          ("fanPower", 32),
          ("dcdcVoltage", 33),
          ("dcdcCurrent", 34),
          ("dcdcPower", 35),
          ("dcdcHeatsinkTemperature", 36),
          ("dcInputVoltageMax", 37),
          ("dcInputVoltageMin", 38),
          ("numberOfSolarCommsLost", 39),
          ("solarInputVoltage", 40),
          ("numberOfSolarFailed", 41))
    )



class SystemAlarm(TextualConvention, Integer32):
    status = "current"
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72)
        )
    )
    namedValues = NamedValues(
        *(("lowFloat", 0),
          ("lowLoad", 1),
          ("highFloat", 2),
          ("highLoad", 3),
          ("rectifierFail", 4),
          ("multipleRectifierFail", 5),
          ("rectifierCommsLost", 6),
          ("multipleRectifierCommsLost", 7),
          ("partialAcFail", 8),
          ("acFail", 9),
          ("systemOverload", 10),
          ("loadFuseFail", 11),
          ("batteryFuseFail", 12),
          ("batteryTestFail", 13),
          ("movFail", 14),
          ("acdFanFail", 15),
          ("lvd1Disconnected", 16),
          ("lvd1Fail", 17),
          ("lvd1Manual", 18),
          ("lvd2Disconnected", 19),
          ("lvd2Fail", 20),
          ("lvd2Manual", 21),
          ("batteryTemperatureLow", 22),
          ("batteryTemperatureHigh", 23),
          ("sensorFail", 24),
          ("equalize", 25),
          ("fastCharge", 26),
          ("batteryTest", 27),
          ("auxiliarySensorFail", 28),
          ("inDischarge", 29),
          ("batteryCurrentLimit", 30),
          ("rectifierNoLoad", 31),
          ("rectifierCurrentLimit", 32),
          ("rectifierOverTemperature", 33),
          ("acPhase1Fail", 34),
          ("acPhase1Voltage", 35),
          ("acPhase2Fail", 36),
          ("acPhase2Voltage", 37),
          ("acPhase3Fail", 38),
          ("acPhase3Voltage", 39),
          ("acFrequency", 40),
          ("reserved", 41),
          ("cabinetFanFail", 42),
          ("unmappedIobFound", 43),
          ("unknownHardware", 44),
          ("iobCommsLost", 45),
          ("standbyMode", 46),
          ("lvd1CharacterizationError", 47),
          ("lvd2CharacterizationError", 48),
          ("stringFail", 49),
          ("generatorFail", 50),
          ("lvdDisconnected", 51),
          ("lvdFail", 52),
          ("lvdManual", 53),
          ("lvdCharacterizationError", 54),
          ("configurationError", 55),
          ("wrongBatteryPolarity", 56),
          ("characterizingBattery", 57),
          ("doManual", 58),
          ("normalCharge", 59),
          ("peakLoadReduction", 60),
          ("siteBackupTimeRemaining", 61),
          ("dcdcFail", 62),
          ("solarFail", 63),
          ("systemOverloadB", 64),
          ("batteryEndOfLife", 65),
          ("rtcLowBattery", 66),
          ("batteryTestCancelled", 67),
          ("lowRectifierCapacity", 68),
          ("solarCommsLost", 69),
          ("multipleSolarCommsLost", 70),
          ("unstableRectifierAc", 71),
          ("ripCommsLost", 72))
    )



class EnergizeState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deenergized", 0),
          ("energized", 1))
    )



class RelayMapping(TextualConvention, Integer32):
    status = "current"
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("digitalOutput1", 1),
          ("digitalOutput2", 2),
          ("digitalOutput3", 3),
          ("digitalOutput4", 4),
          ("digitalOutput5", 5),
          ("digitalOutput6", 6),
          ("digitalOutput7", 7),
          ("digitalOutput8", 8),
          ("digitalOutput9", 9),
          ("digitalOutput10", 10),
          ("digitalOutput11", 11),
          ("digitalOutput12", 12),
          ("digitalOutput13", 13),
          ("digitalOutput14", 14),
          ("digitalOutput15", 15),
          ("digitalOutput16", 16),
          ("digitalOutput17", 17),
          ("digitalOutput18", 18),
          ("digitalOutput19", 19),
          ("digitalOutput20", 20),
          ("digitalOutput21", 21),
          ("digitalOutput22", 22),
          ("digitalOutput23", 23),
          ("digitalOutput24", 24),
          ("digitalOutput25", 25),
          ("digitalOutput26", 26),
          ("digitalOutput27", 27),
          ("digitalOutput28", 28),
          ("digitalOutput29", 29),
          ("digitalOutput30", 30),
          ("digitalOutput31", 31),
          ("digitalOutput32", 32),
          ("digitalOutput33", 33),
          ("digitalOutput34", 34),
          ("digitalOutput35", 35),
          ("digitalOutput36", 36),
          ("digitalOutput37", 37),
          ("digitalOutput38", 38),
          ("digitalOutput39", 39),
          ("digitalOutput40", 40),
          ("digitalOutput41", 41),
          ("digitalOutput42", 42),
          ("digitalOutput43", 43),
          ("digitalOutput44", 44),
          ("digitalOutput45", 45),
          ("digitalOutput46", 46),
          ("digitalOutput47", 47),
          ("digitalOutput48", 48),
          ("digitalOutput49", 49),
          ("digitalOutput50", 50),
          ("digitalOutput51", 51),
          ("digitalOutput52", 52),
          ("digitalOutput53", 53),
          ("digitalOutput54", 54),
          ("digitalOutput55", 55),
          ("digitalOutput56", 56),
          ("digitalOutput57", 57),
          ("digitalOutput58", 58),
          ("digitalOutput59", 59),
          ("digitalOutput60", 60),
          ("digitalOutput61", 61),
          ("digitalOutput62", 62),
          ("digitalOutput63", 63),
          ("digitalOutput64", 64),
          ("digitalOutput65", 65),
          ("digitalOutput66", 66),
          ("digitalOutput67", 67),
          ("digitalOutput68", 68),
          ("digitalOutput69", 69),
          ("digitalOutput70", 70),
          ("digitalOutput71", 71),
          ("digitalOutput72", 72),
          ("digitalOutput73", 73),
          ("digitalOutput74", 74),
          ("digitalOutput75", 75),
          ("digitalOutput76", 76),
          ("digitalOutput77", 77),
          ("digitalOutput78", 78),
          ("digitalOutput79", 79),
          ("digitalOutput80", 80),
          ("digitalOutput81", 81),
          ("digitalOutput82", 82),
          ("digitalOutput83", 83),
          ("digitalOutput84", 84),
          ("digitalOutput85", 85),
          ("digitalOutput86", 86),
          ("digitalOutput87", 87),
          ("digitalOutput88", 88),
          ("digitalOutput89", 89),
          ("digitalOutput90", 90),
          ("digitalOutput91", 91),
          ("digitalOutput92", 92),
          ("digitalOutput93", 93),
          ("digitalOutput94", 94),
          ("digitalOutput95", 95),
          ("digitalOutput96", 96),
          ("digitalOutput97", 97),
          ("digitalOutput98", 98),
          ("digitalOutput99", 99),
          ("digitalOutput100", 100),
          ("digitalOutput101", 101),
          ("digitalOutput102", 102),
          ("digitalOutput103", 103),
          ("digitalOutput104", 104),
          ("digitalOutput105", 105),
          ("digitalOutput106", 106),
          ("digitalOutput107", 107),
          ("digitalOutput108", 108))
    )



class AiFunction(TextualConvention, Integer32):
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("userDefined", 1),
          ("busVoltage", 2),
          ("batteryTemperature", 3),
          ("batteryCurrent", 4),
          ("loadCurrent", 5),
          ("rectifierCurrent", 6),
          ("batteryMidpoint", 7),
          ("reverseBatteryDetect", 8),
          ("alternativeEnergySourceCurrent", 9),
          ("fuelLevel", 10),
          ("smartAnalog", 11),
          ("fanTemperature", 12),
          ("batteryFirstQuarterPoint", 13),
          ("batteryThirdQuarterPoint", 14),
          ("generatorCurrent", 15),
          ("solarCurrent", 16))
    )



class SmartAnalogType(TextualConvention, Integer32):
    status = "current"
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
        *(("average", 0),
          ("addition", 1),
          ("multiplication", 2),
          ("max", 3),
          ("min", 4),
          ("kmultiplication", 5))
    )



class SmartAnalogGate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("positiveOnly", 1),
          ("negativeOnly", 2),
          ("absolute", 3),
          ("change", 4))
    )



class ActiveState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 3))
    )



class DigitalInputState(TextualConvention, Integer32):
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
        *(("missing", 1),
          ("closed", 2),
          ("open", 3),
          ("disabled", 4))
    )



class MeasurementUnits(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58)
        )
    )
    namedValues = NamedValues(
        *(("none", 30),
          ("volts", 31),
          ("milliAmps", 32),
          ("amps", 33),
          ("kiloAmps", 34),
          ("degreeCelsius", 35),
          ("kiloWatts", 36),
          ("percent", 37),
          ("voltsAc", 38),
          ("voltsDc", 39),
          ("ampsAc", 40),
          ("ampsDc", 41),
          ("litre", 42),
          ("litrePerSec", 43),
          ("cubicMeterPerHour", 44),
          ("pascal", 45),
          ("kiloPascal", 46),
          ("mmh2o", 47),
          ("percentRelativeHumidity", 48),
          ("rpm", 49),
          ("hertz", 50),
          ("kiloVoltAmps", 51),
          ("kiloWattHour", 52),
          ("watts", 53),
          ("bar", 54),
          ("psi", 55),
          ("ah", 56),
          ("hours", 57),
          ("minutes", 58))
    )



class OverloadAlarmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("totalCapacity", 0),
          ("redundancyNPlus1", 1),
          ("redundancyNPlus2", 2))
    )



class RxpSlaveType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("iob", 1),
          ("rectifier", 2),
          ("solar", 3),
          ("fanController", 4),
          ("dcdc", 5),
          ("dataLogger", 6))
    )



class BsmState(TextualConvention, Integer32):
    status = "current"
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
        *(("unableToStart", 0),
          ("lockedOut", 1),
          ("converging", 2),
          ("stable", 3),
          ("disabled", 4),
          ("zeroCellsPerString", 5),
          ("busSensorFailed", 6),
          ("acFailed", 7),
          ("inDischarge", 8),
          ("chargeStateUnavailable", 9),
          ("inFastCharge", 10),
          ("inEqualize", 11),
          ("inBatteryTest", 12),
          ("batteryFuseFailed", 13))
    )



class BsmBatteryState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("pendingFail", 1),
          ("failed", 2),
          ("unavailable", 3),
          ("notConfigured", 4))
    )



class LvdState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("connected", 1),
          ("disconnected", 2),
          ("manual", 3),
          ("noContactors", 4),
          ("remoteConnected", 5),
          ("remoteDisconnected", 6))
    )



class LvdcType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normallyOpen", 0),
          ("normallyClosed", 1))
    )



class LvdcState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("connected", 0),
          ("disconnected", 1),
          ("failed", 2),
          ("missing", 3),
          ("disabled", 4),
          ("conflict", 5),
          ("notCharacterized", 6))
    )



class BtrCharacterizationResult(TextualConvention, Integer32):
    status = "current"
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
        *(("notYetRun", 0),
          ("sensorFailed", 1),
          ("notFullyCharged", 2),
          ("unstableBatteryCurrent", 3),
          ("voltageStepDetected", 4),
          ("complete", 5),
          ("updated", 6),
          ("userCanceled", 7))
    )



class GeneratorStartupWiring(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("indirectStart", 0),
          ("directStart", 1))
    )



class EnergyMeterAiFunction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("current", 0),
          ("voltage", 1),
          ("powerW", 2),
          ("powerKw", 3))
    )



class EnergyMeterSystemValue(TextualConvention, Integer32):
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("busVoltage", 1),
          ("rectifierCurrent", 2),
          ("loadCurrent", 3),
          ("batteryCurrent", 4),
          ("smartAnalogCurrent", 5),
          ("alternativeSourceCurrent", 6),
          ("solarCurrent", 7),
          ("acInputCurrent", 8),
          ("dcInputCurrent", 9),
          ("smartAnalogVoltage", 10),
          ("acVoltage", 11),
          ("dcInputVoltage", 12),
          ("powerMeter", 13),
          ("loadPower", 14),
          ("smartAnalogPowerKw", 15),
          ("smartAnalogPowerW", 16),
          ("solarPower", 17),
          ("generatorCurrent", 18),
          ("pulseMeter", 19),
          ("dcdcVoltage", 20),
          ("dcdcCurrent", 21),
          ("dcdcPower", 22))
    )



class LogItems(TextualConvention, Integer32):
    status = "current"
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
        *(("smartAnalogs", 0),
          ("generatorControl", 1),
          ("energyMeters", 2),
          ("powerMeters", 3),
          ("otherMeters", 4),
          ("fanController", 5),
          ("data", 6),
          ("batterySymmetryMonitoring", 7))
    )



class Redundancy(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("n", 1),
          ("nPlus1", 2),
          ("nPlus2", 3))
    )



class PreventBatteryTest(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("batteryFuseFail", 1),
          ("allow", 2))
    )



class FanControllerMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dualController", 1),
          ("singleController", 2),
          ("independentControllers", 3))
    )



class FanControllerProfile(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1),
          ("fanPowerIsSet", 2))
    )



class SystemInputType(TextualConvention, Integer32):
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("rectifierCurrent", 1),
          ("loadCurrent", 2),
          ("batteryCurrent", 3),
          ("smartAnalog", 4),
          ("alternativeSourceCurrent", 5),
          ("solarCurrent", 6),
          ("acInputCurrent", 7),
          ("dcInputCurrent", 8),
          ("acVoltage", 9),
          ("dcInputVoltage", 10),
          ("powerMeter", 11),
          ("loadPower", 12),
          ("solarPower", 13),
          ("generatorCurrent", 14),
          ("ampHourDischarged", 15),
          ("btrTimeRemaining", 16),
          ("operatingVoltage", 17),
          ("firstQuarterPointVoltage", 18),
          ("thirdQuarterPointVoltage", 19),
          ("midPointVoltage", 20),
          ("imbalancePercent", 21),
          ("fanTemperature", 22),
          ("fanPower", 23),
          ("dcdcVoltage", 24),
          ("dcdcCurrent", 25),
          ("dcdcPower", 26),
          ("dcdcHeatsinkTemperature", 27),
          ("dcInputVoltageMax", 28),
          ("dcInputVoltageMin", 29),
          ("busVoltage", 30))
    )



class GenericSystemType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("factory", 2),
          ("masterConfig", 3),
          ("aps48v", 4),
          ("aps24v", 5),
          ("eps48vLvd", 8),
          ("eps48v", 9))
    )



class S3pAccess(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("allow", 1),
          ("usbOnly", 2))
    )



class String7(TextualConvention, OctetString):
    status = "current"
    displayHint = "7t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )



class String10(TextualConvention, OctetString):
    status = "current"
    displayHint = "10t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )



class String16(TextualConvention, OctetString):
    status = "current"
    displayHint = "16t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class String17(TextualConvention, OctetString):
    status = "current"
    displayHint = "17t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )



class String20(TextualConvention, OctetString):
    status = "current"
    displayHint = "20t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class String30(TextualConvention, OctetString):
    status = "current"
    displayHint = "30t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )



class String32(TextualConvention, OctetString):
    status = "current"
    displayHint = "32t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class String40(TextualConvention, OctetString):
    status = "current"
    displayHint = "40t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )



class String60(TextualConvention, OctetString):
    status = "current"
    displayHint = "60t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )



class String64(TextualConvention, OctetString):
    status = "current"
    displayHint = "64t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class String100(TextualConvention, OctetString):
    status = "current"
    displayHint = "100t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )



class String150(TextualConvention, OctetString):
    status = "current"
    displayHint = "150t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 150),
    )



class String253(TextualConvention, OctetString):
    status = "current"
    displayHint = "253t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )



# MIB Managed Objects in the order of their OIDs

_EatonChNz_ObjectIdentity = ObjectIdentity
eatonChNz = _EatonChNz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918)
)
_DcPowerSystem_ObjectIdentity = ObjectIdentity
dcPowerSystem = _DcPowerSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2)
)
_RpsSc300_ObjectIdentity = ObjectIdentity
rpsSc300 = _RpsSc300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14)
)
_IpAddressType_Type = InetAddressType
_IpAddressType_Object = MibScalar
ipAddressType = _IpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 2),
    _IpAddressType_Type()
)
ipAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddressType.setStatus("current")
_RpsObjects_ObjectIdentity = ObjectIdentity
rpsObjects = _RpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10)
)
if mibBuilder.loadTexts:
    rpsObjects.setStatus("current")
_SystemIdentity_ObjectIdentity = ObjectIdentity
systemIdentity = _SystemIdentity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10)
)
if mibBuilder.loadTexts:
    systemIdentity.setStatus("current")


class _SystemManufacturer_Type(DisplayString):
    """Custom type systemManufacturer based on DisplayString"""
    defaultValue = OctetString("System Manufacturer")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SystemManufacturer_Type.__name__ = "DisplayString"
_SystemManufacturer_Object = MibScalar
systemManufacturer = _SystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 10),
    _SystemManufacturer_Type()
)
systemManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemManufacturer.setStatus("current")


class _SystemSerialNumber_Type(DisplayString):
    """Custom type systemSerialNumber based on DisplayString"""
    defaultValue = OctetString("0000000000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SystemSerialNumber_Type.__name__ = "DisplayString"
_SystemSerialNumber_Object = MibScalar
systemSerialNumber = _SystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 20),
    _SystemSerialNumber_Type()
)
systemSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSerialNumber.setStatus("current")


class _SystemType_Type(DisplayString):
    """Custom type systemType based on DisplayString"""
    defaultValue = OctetString("System Type")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SystemType_Type.__name__ = "DisplayString"
_SystemType_Object = MibScalar
systemType = _SystemType_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 30),
    _SystemType_Type()
)
systemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemType.setStatus("current")


class _SystemLocation_Type(DisplayString):
    """Custom type systemLocation based on DisplayString"""
    defaultValue = OctetString("System Location")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SystemLocation_Type.__name__ = "DisplayString"
_SystemLocation_Object = MibScalar
systemLocation = _SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 40),
    _SystemLocation_Type()
)
systemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLocation.setStatus("current")


class _SiteName_Type(DisplayString):
    """Custom type siteName based on DisplayString"""
    defaultValue = OctetString("Site Name")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SiteName_Type.__name__ = "DisplayString"
_SiteName_Object = MibScalar
siteName = _SiteName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 50),
    _SiteName_Type()
)
siteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteName.setStatus("current")


class _SiteAddress_Type(DisplayString):
    """Custom type siteAddress based on DisplayString"""
    defaultValue = OctetString("Site Address")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SiteAddress_Type.__name__ = "DisplayString"
_SiteAddress_Object = MibScalar
siteAddress = _SiteAddress_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 60),
    _SiteAddress_Type()
)
siteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteAddress.setStatus("current")


class _SiteNotes_Type(DisplayString):
    """Custom type siteNotes based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_SiteNotes_Type.__name__ = "DisplayString"
_SiteNotes_Object = MibScalar
siteNotes = _SiteNotes_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 70),
    _SiteNotes_Type()
)
siteNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteNotes.setStatus("current")


class _SystemObjectId2_Type(Sysoid):
    """Custom type systemObjectId2 based on Sysoid"""
    defaultValue = 14


_SystemObjectId2_Type.__name__ = "Sysoid"
_SystemObjectId2_Object = MibScalar
systemObjectId2 = _SystemObjectId2_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 85),
    _SystemObjectId2_Type()
)
systemObjectId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemObjectId2.setStatus("current")


class _TrapFormat_Type(SnmpTrapFormat):
    """Custom type trapFormat based on SnmpTrapFormat"""
    defaultValue = 1


_TrapFormat_Type.__name__ = "SnmpTrapFormat"
_TrapFormat_Object = MibScalar
trapFormat = _TrapFormat_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 90),
    _TrapFormat_Type()
)
trapFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapFormat.setStatus("current")


class _GenericTrapsEnable_Type(GenericTrapsEnable):
    """Custom type genericTrapsEnable based on GenericTrapsEnable"""
    defaultValue = 2


_GenericTrapsEnable_Type.__name__ = "GenericTrapsEnable"
_GenericTrapsEnable_Object = MibScalar
genericTrapsEnable = _GenericTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 95),
    _GenericTrapsEnable_Type()
)
genericTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericTrapsEnable.setStatus("current")


class _ConfigurationName_Type(DisplayString):
    """Custom type configurationName based on DisplayString"""
    defaultValue = OctetString("Factory")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ConfigurationName_Type.__name__ = "DisplayString"
_ConfigurationName_Object = MibScalar
configurationName = _ConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 100),
    _ConfigurationName_Type()
)
configurationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationName.setStatus("current")


class _ConfigurationVersion_Type(Integer32):
    """Custom type configurationVersion based on Integer32"""
    defaultValue = 0


_ConfigurationVersion_Type.__name__ = "Integer32"
_ConfigurationVersion_Object = MibScalar
configurationVersion = _ConfigurationVersion_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 101),
    _ConfigurationVersion_Type()
)
configurationVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationVersion.setStatus("current")
_ConfigurationModified_Type = Boolean
_ConfigurationModified_Object = MibScalar
configurationModified = _ConfigurationModified_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 102),
    _ConfigurationModified_Type()
)
configurationModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationModified.setStatus("current")


class _SiteBuilding_Type(DisplayString):
    """Custom type siteBuilding based on DisplayString"""
    defaultValue = OctetString("Site Building")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SiteBuilding_Type.__name__ = "DisplayString"
_SiteBuilding_Object = MibScalar
siteBuilding = _SiteBuilding_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 106),
    _SiteBuilding_Type()
)
siteBuilding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteBuilding.setStatus("current")


class _SiteRoom_Type(DisplayString):
    """Custom type siteRoom based on DisplayString"""
    defaultValue = OctetString("Site Room")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SiteRoom_Type.__name__ = "DisplayString"
_SiteRoom_Object = MibScalar
siteRoom = _SiteRoom_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 108),
    _SiteRoom_Type()
)
siteRoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteRoom.setStatus("current")


class _SiteContact_Type(DisplayString):
    """Custom type siteContact based on DisplayString"""
    defaultValue = OctetString("Site Contact")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SiteContact_Type.__name__ = "DisplayString"
_SiteContact_Object = MibScalar
siteContact = _SiteContact_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 110),
    _SiteContact_Type()
)
siteContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteContact.setStatus("current")


class _SiteSupportContact_Type(DisplayString):
    """Custom type siteSupportContact based on DisplayString"""
    defaultValue = OctetString("Support Contact")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SiteSupportContact_Type.__name__ = "DisplayString"
_SiteSupportContact_Object = MibScalar
siteSupportContact = _SiteSupportContact_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 112),
    _SiteSupportContact_Type()
)
siteSupportContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteSupportContact.setStatus("current")
_IsThreePhaseSystem_Type = Boolean
_IsThreePhaseSystem_Object = MibScalar
isThreePhaseSystem = _IsThreePhaseSystem_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 120),
    _IsThreePhaseSystem_Type()
)
isThreePhaseSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isThreePhaseSystem.setStatus("current")
_Controller_ObjectIdentity = ObjectIdentity
controller = _Controller_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 20)
)
if mibBuilder.loadTexts:
    controller.setStatus("current")


class _ManufacturerName_Type(DisplayString):
    """Custom type manufacturerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ManufacturerName_Type.__name__ = "DisplayString"
_ManufacturerName_Object = MibScalar
manufacturerName = _ManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 20, 10),
    _ManufacturerName_Type()
)
manufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturerName.setStatus("current")
_ProductType_Type = ProductType
_ProductType_Object = MibScalar
productType = _ProductType_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 20, 20),
    _ProductType_Type()
)
productType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productType.setStatus("current")


class _SoftwareVersion_Type(DisplayString):
    """Custom type softwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SoftwareVersion_Type.__name__ = "DisplayString"
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 20, 30),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")


class _BootVersion_Type(DisplayString):
    """Custom type bootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_BootVersion_Type.__name__ = "DisplayString"
_BootVersion_Object = MibScalar
bootVersion = _BootVersion_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 20, 50),
    _BootVersion_Type()
)
bootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootVersion.setStatus("current")
_InterfaceVersion_Type = Unsigned16
_InterfaceVersion_Object = MibScalar
interfaceVersion = _InterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 20, 70),
    _InterfaceVersion_Type()
)
interfaceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceVersion.setStatus("current")


class _HardwareVersion_Type(DisplayString):
    """Custom type hardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HardwareVersion_Type.__name__ = "DisplayString"
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 20, 80),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("current")


class _LcdVersion_Type(DisplayString):
    """Custom type lcdVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LcdVersion_Type.__name__ = "DisplayString"
_LcdVersion_Object = MibScalar
lcdVersion = _LcdVersion_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 20, 82),
    _LcdVersion_Type()
)
lcdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcdVersion.setStatus("current")
_BatteryMonitor_Type = Percentile8Nan
_BatteryMonitor_Object = MibScalar
batteryMonitor = _BatteryMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 20, 83),
    _BatteryMonitor_Type()
)
batteryMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitor.setStatus("current")
if mibBuilder.loadTexts:
    batteryMonitor.setUnits("%")


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 20, 90),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _EthernetMacAddress_Type(DisplayString):
    """Custom type ethernetMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_EthernetMacAddress_Type.__name__ = "DisplayString"
_EthernetMacAddress_Object = MibScalar
ethernetMacAddress = _EthernetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 20, 100),
    _EthernetMacAddress_Type()
)
ethernetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetMacAddress.setStatus("current")


class _SubversionRevision_Type(DisplayString):
    """Custom type subversionRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SubversionRevision_Type.__name__ = "DisplayString"
_SubversionRevision_Object = MibScalar
subversionRevision = _SubversionRevision_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 20, 110),
    _SubversionRevision_Type()
)
subversionRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subversionRevision.setStatus("current")
_EvaluationSoftwareFound_Type = Boolean
_EvaluationSoftwareFound_Object = MibScalar
evaluationSoftwareFound = _EvaluationSoftwareFound_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 20, 120),
    _EvaluationSoftwareFound_Type()
)
evaluationSoftwareFound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evaluationSoftwareFound.setStatus("current")
_GenericSystemType_Type = GenericSystemType
_GenericSystemType_Object = MibScalar
genericSystemType = _GenericSystemType_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 20, 150),
    _GenericSystemType_Type()
)
genericSystemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericSystemType.setStatus("current")
_Communications_ObjectIdentity = ObjectIdentity
communications = _Communications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30)
)
if mibBuilder.loadTexts:
    communications.setStatus("current")


class _S3pAccess_Type(S3pAccess):
    """Custom type s3pAccess based on S3pAccess"""
    defaultValue = 2


_S3pAccess_Type.__name__ = "S3pAccess"
_S3pAccess_Object = MibScalar
s3pAccess = _S3pAccess_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 3),
    _S3pAccess_Type()
)
s3pAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3pAccess.setStatus("current")


class _SnmpAccess_Type(SnmpAccessState):
    """Custom type snmpAccess based on SnmpAccessState"""
    defaultValue = 3


_SnmpAccess_Type.__name__ = "SnmpAccessState"
_SnmpAccess_Object = MibScalar
snmpAccess = _SnmpAccess_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 8),
    _SnmpAccess_Type()
)
snmpAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccess.setStatus("current")


class _SerialServerAccess_Type(EnableState):
    """Custom type serialServerAccess based on EnableState"""
    defaultValue = 0


_SerialServerAccess_Type.__name__ = "EnableState"
_SerialServerAccess_Object = MibScalar
serialServerAccess = _SerialServerAccess_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 9),
    _SerialServerAccess_Type()
)
serialServerAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialServerAccess.setStatus("current")


class _SerialServerPort_Type(Integer32):
    """Custom type serialServerPort based on Integer32"""
    defaultValue = 15000


_SerialServerPort_Type.__name__ = "Integer32"
_SerialServerPort_Object = MibScalar
serialServerPort = _SerialServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 10),
    _SerialServerPort_Type()
)
serialServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialServerPort.setStatus("current")


class _S3pAddress_Type(Unsigned16):
    """Custom type s3pAddress based on Unsigned16"""
    defaultValue = 1


_S3pAddress_Type.__name__ = "Unsigned16"
_S3pAddress_Object = MibScalar
s3pAddress = _S3pAddress_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 15),
    _S3pAddress_Type()
)
s3pAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3pAddress.setStatus("current")


class _IpAddress_Type(InetAddress):
    """Custom type ipAddress based on InetAddress"""
    defaultValue = OctetString("0.0.0.0")

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_IpAddress_Type.__name__ = "InetAddress"
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 20),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")


class _SubnetMask_Type(InetAddress):
    """Custom type subnetMask based on InetAddress"""
    defaultValue = OctetString("0.0.0.0")

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SubnetMask_Type.__name__ = "InetAddress"
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 30),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")


class _GatewayAddress_Type(InetAddress):
    """Custom type gatewayAddress based on InetAddress"""
    defaultValue = OctetString("0.0.0.0")

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_GatewayAddress_Type.__name__ = "InetAddress"
_GatewayAddress_Object = MibScalar
gatewayAddress = _GatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 50),
    _GatewayAddress_Type()
)
gatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayAddress.setStatus("current")


class _VlanId_Type(Unsigned16):
    """Custom type vlanId based on Unsigned16"""
    defaultValue = 0


_VlanId_Type.__name__ = "Unsigned16"
_VlanId_Object = MibScalar
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 51),
    _VlanId_Type()
)
vlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")
_Serial_ObjectIdentity = ObjectIdentity
serial = _Serial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53)
)
if mibBuilder.loadTexts:
    serial.setStatus("current")
_PortSettings_ObjectIdentity = ObjectIdentity
portSettings = _PortSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 5)
)
if mibBuilder.loadTexts:
    portSettings.setStatus("current")
_BaudRate_Type = BaudRate
_BaudRate_Object = MibScalar
baudRate = _BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 5, 10),
    _BaudRate_Type()
)
baudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baudRate.setStatus("current")


class _Parity_Type(Parity):
    """Custom type parity based on Parity"""
    defaultValue = 0


_Parity_Type.__name__ = "Parity"
_Parity_Object = MibScalar
parity = _Parity_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 5, 20),
    _Parity_Type()
)
parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parity.setStatus("current")


class _StopBits_Type(StopBits):
    """Custom type stopBits based on StopBits"""
    defaultValue = 1


_StopBits_Type.__name__ = "StopBits"
_StopBits_Object = MibScalar
stopBits = _StopBits_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 5, 30),
    _StopBits_Type()
)
stopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stopBits.setStatus("current")


class _EnableModem_Type(EnableState):
    """Custom type enableModem based on EnableState"""
    defaultValue = 0


_EnableModem_Type.__name__ = "EnableState"
_EnableModem_Object = MibScalar
enableModem = _EnableModem_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 10),
    _EnableModem_Type()
)
enableModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableModem.setStatus("current")


class _AlarmReport_Type(AlarmReport):
    """Custom type alarmReport based on AlarmReport"""
    defaultValue = 0


_AlarmReport_Type.__name__ = "AlarmReport"
_AlarmReport_Object = MibScalar
alarmReport = _AlarmReport_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 20),
    _AlarmReport_Type()
)
alarmReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmReport.setStatus("current")


class _ModemSetUpString_Type(DisplayString):
    """Custom type modemSetUpString based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ModemSetUpString_Type.__name__ = "DisplayString"
_ModemSetUpString_Object = MibScalar
modemSetUpString = _ModemSetUpString_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 30),
    _ModemSetUpString_Type()
)
modemSetUpString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemSetUpString.setStatus("current")


class _ModemAutoAnswerRings_Type(Unsigned8):
    """Custom type modemAutoAnswerRings based on Unsigned8"""
    defaultValue = 2


_ModemAutoAnswerRings_Type.__name__ = "Unsigned8"
_ModemAutoAnswerRings_Object = MibScalar
modemAutoAnswerRings = _ModemAutoAnswerRings_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 40),
    _ModemAutoAnswerRings_Type()
)
modemAutoAnswerRings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemAutoAnswerRings.setStatus("current")


class _ModemMaximumRetries_Type(Unsigned8):
    """Custom type modemMaximumRetries based on Unsigned8"""
    defaultValue = 0


_ModemMaximumRetries_Type.__name__ = "Unsigned8"
_ModemMaximumRetries_Object = MibScalar
modemMaximumRetries = _ModemMaximumRetries_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 50),
    _ModemMaximumRetries_Type()
)
modemMaximumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemMaximumRetries.setStatus("current")


class _ModemRetryInterval_Type(TimeIntervalInSeconds):
    """Custom type modemRetryInterval based on TimeIntervalInSeconds"""
    defaultValue = 0


_ModemRetryInterval_Type.__name__ = "TimeIntervalInSeconds"
_ModemRetryInterval_Object = MibScalar
modemRetryInterval = _ModemRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 60),
    _ModemRetryInterval_Type()
)
modemRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    modemRetryInterval.setUnits("s")


class _ModemPowerReset_Type(EnableState):
    """Custom type modemPowerReset based on EnableState"""
    defaultValue = 0


_ModemPowerReset_Type.__name__ = "EnableState"
_ModemPowerReset_Object = MibScalar
modemPowerReset = _ModemPowerReset_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 70),
    _ModemPowerReset_Type()
)
modemPowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemPowerReset.setStatus("current")
_DialOutNumberTable_Object = MibTable
dialOutNumberTable = _DialOutNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 80)
)
if mibBuilder.loadTexts:
    dialOutNumberTable.setStatus("current")
_DialOutNumberEntry_Object = MibTableRow
dialOutNumberEntry = _DialOutNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 80, 1)
)
dialOutNumberEntry.setIndexNames(
    (0, "RpsSc300Mib", "dialOutNumberIndex"),
)
if mibBuilder.loadTexts:
    dialOutNumberEntry.setStatus("current")


class _DialOutNumberIndex_Type(Unsigned8):
    """Custom type dialOutNumberIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DialOutNumberIndex_Type.__name__ = "Unsigned8"
_DialOutNumberIndex_Object = MibTableColumn
dialOutNumberIndex = _DialOutNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 80, 1, 1),
    _DialOutNumberIndex_Type()
)
dialOutNumberIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dialOutNumberIndex.setStatus("current")


class _DialOutNumber_Type(DisplayString):
    """Custom type dialOutNumber based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DialOutNumber_Type.__name__ = "DisplayString"
_DialOutNumber_Object = MibTableColumn
dialOutNumber = _DialOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 80, 1, 10),
    _DialOutNumber_Type()
)
dialOutNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialOutNumber.setStatus("current")
_SmsNotificationTable_Object = MibTable
smsNotificationTable = _SmsNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 90)
)
if mibBuilder.loadTexts:
    smsNotificationTable.setStatus("current")
_SmsNotificationEntry_Object = MibTableRow
smsNotificationEntry = _SmsNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 90, 1)
)
smsNotificationEntry.setIndexNames(
    (0, "RpsSc300Mib", "smsNotificationIndex"),
)
if mibBuilder.loadTexts:
    smsNotificationEntry.setStatus("current")


class _SmsNotificationIndex_Type(Unsigned8):
    """Custom type smsNotificationIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SmsNotificationIndex_Type.__name__ = "Unsigned8"
_SmsNotificationIndex_Object = MibTableColumn
smsNotificationIndex = _SmsNotificationIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 90, 1, 1),
    _SmsNotificationIndex_Type()
)
smsNotificationIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smsNotificationIndex.setStatus("current")


class _SmsPhoneName_Type(DisplayString):
    """Custom type smsPhoneName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SmsPhoneName_Type.__name__ = "DisplayString"
_SmsPhoneName_Object = MibTableColumn
smsPhoneName = _SmsPhoneName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 90, 1, 10),
    _SmsPhoneName_Type()
)
smsPhoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsPhoneName.setStatus("current")


class _SmsLevel_Type(SeverityLevel):
    """Custom type smsLevel based on SeverityLevel"""
    defaultValue = 4


_SmsLevel_Type.__name__ = "SeverityLevel"
_SmsLevel_Object = MibTableColumn
smsLevel = _SmsLevel_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 90, 1, 20),
    _SmsLevel_Type()
)
smsLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsLevel.setStatus("current")


class _SmsPhoneNumber_Type(DisplayString):
    """Custom type smsPhoneNumber based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SmsPhoneNumber_Type.__name__ = "DisplayString"
_SmsPhoneNumber_Object = MibTableColumn
smsPhoneNumber = _SmsPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 90, 1, 30),
    _SmsPhoneNumber_Type()
)
smsPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsPhoneNumber.setStatus("current")


class _SmsPrefix_Type(DisplayString):
    """Custom type smsPrefix based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_SmsPrefix_Type.__name__ = "DisplayString"
_SmsPrefix_Object = MibTableColumn
smsPrefix = _SmsPrefix_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 90, 1, 40),
    _SmsPrefix_Type()
)
smsPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsPrefix.setStatus("current")


class _SmsEmailGateway_Type(DisplayString):
    """Custom type smsEmailGateway based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SmsEmailGateway_Type.__name__ = "DisplayString"
_SmsEmailGateway_Object = MibTableColumn
smsEmailGateway = _SmsEmailGateway_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 53, 90, 1, 50),
    _SmsEmailGateway_Type()
)
smsEmailGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smsEmailGateway.setStatus("current")
_Modbus_ObjectIdentity = ObjectIdentity
modbus = _Modbus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 57)
)
if mibBuilder.loadTexts:
    modbus.setStatus("current")


class _ModbusAccess_Type(EnableState):
    """Custom type modbusAccess based on EnableState"""
    defaultValue = 0


_ModbusAccess_Type.__name__ = "EnableState"
_ModbusAccess_Object = MibScalar
modbusAccess = _ModbusAccess_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 57, 10),
    _ModbusAccess_Type()
)
modbusAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modbusAccess.setStatus("current")


class _ModbusAddress_Type(Unsigned8):
    """Custom type modbusAddress based on Unsigned8"""
    defaultValue = 1


_ModbusAddress_Type.__name__ = "Unsigned8"
_ModbusAddress_Object = MibScalar
modbusAddress = _ModbusAddress_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 57, 20),
    _ModbusAddress_Type()
)
modbusAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modbusAddress.setStatus("current")
_ModbusInterfaceVersion_Type = Unsigned16
_ModbusInterfaceVersion_Object = MibScalar
modbusInterfaceVersion = _ModbusInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 57, 30),
    _ModbusInterfaceVersion_Type()
)
modbusInterfaceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusInterfaceVersion.setStatus("current")
_SnmpSettings_ObjectIdentity = ObjectIdentity
snmpSettings = _SnmpSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60)
)
if mibBuilder.loadTexts:
    snmpSettings.setStatus("current")


class _SnmpReadCommunity_Type(DisplayString):
    """Custom type snmpReadCommunity based on DisplayString"""
    defaultValue = OctetString("EatonPublic")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpReadCommunity_Type.__name__ = "DisplayString"
_SnmpReadCommunity_Object = MibScalar
snmpReadCommunity = _SnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 10),
    _SnmpReadCommunity_Type()
)
snmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadCommunity.setStatus("current")


class _SnmpWriteCommunity_Type(DisplayString):
    """Custom type snmpWriteCommunity based on DisplayString"""
    defaultValue = OctetString("EatonPrivate")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpWriteCommunity_Type.__name__ = "DisplayString"
_SnmpWriteCommunity_Object = MibScalar
snmpWriteCommunity = _SnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 20),
    _SnmpWriteCommunity_Type()
)
snmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpWriteCommunity.setStatus("current")


class _EnableTrapRepeat_Type(EnableState):
    """Custom type enableTrapRepeat based on EnableState"""
    defaultValue = 1


_EnableTrapRepeat_Type.__name__ = "EnableState"
_EnableTrapRepeat_Object = MibScalar
enableTrapRepeat = _EnableTrapRepeat_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 30),
    _EnableTrapRepeat_Type()
)
enableTrapRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTrapRepeat.setStatus("current")


class _TrapRepeatRate_Type(TimeIntervalInMinutes):
    """Custom type trapRepeatRate based on TimeIntervalInMinutes"""
    defaultValue = 1


_TrapRepeatRate_Type.__name__ = "TimeIntervalInMinutes"
_TrapRepeatRate_Object = MibScalar
trapRepeatRate = _TrapRepeatRate_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 40),
    _TrapRepeatRate_Type()
)
trapRepeatRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapRepeatRate.setStatus("current")
if mibBuilder.loadTexts:
    trapRepeatRate.setUnits("min")


class _TrapVersion_Type(SnmpTrapVersion):
    """Custom type trapVersion based on SnmpTrapVersion"""
    defaultValue = 3


_TrapVersion_Type.__name__ = "SnmpTrapVersion"
_TrapVersion_Object = MibScalar
trapVersion = _TrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 45),
    _TrapVersion_Type()
)
trapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapVersion.setStatus("current")
_SnmpTrapReceiverTable_Object = MibTable
snmpTrapReceiverTable = _SnmpTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 50)
)
if mibBuilder.loadTexts:
    snmpTrapReceiverTable.setStatus("current")
_SnmpTrapReceiverEntry_Object = MibTableRow
snmpTrapReceiverEntry = _SnmpTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 50, 1)
)
snmpTrapReceiverEntry.setIndexNames(
    (0, "RpsSc300Mib", "snmpTrapReceiverIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapReceiverEntry.setStatus("current")


class _SnmpTrapReceiverIndex_Type(Unsigned8):
    """Custom type snmpTrapReceiverIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnmpTrapReceiverIndex_Type.__name__ = "Unsigned8"
_SnmpTrapReceiverIndex_Object = MibTableColumn
snmpTrapReceiverIndex = _SnmpTrapReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 50, 1, 1),
    _SnmpTrapReceiverIndex_Type()
)
snmpTrapReceiverIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    snmpTrapReceiverIndex.setStatus("current")


class _TrapReceiverIpAddress_Type(InetAddress):
    """Custom type trapReceiverIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TrapReceiverIpAddress_Type.__name__ = "InetAddress"
_TrapReceiverIpAddress_Object = MibTableColumn
trapReceiverIpAddress = _TrapReceiverIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 50, 1, 20),
    _TrapReceiverIpAddress_Type()
)
trapReceiverIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverIpAddress.setStatus("current")


class _TrapReceiverPort_Type(Unsigned16):
    """Custom type trapReceiverPort based on Unsigned16"""
    defaultValue = 162


_TrapReceiverPort_Type.__name__ = "Unsigned16"
_TrapReceiverPort_Object = MibTableColumn
trapReceiverPort = _TrapReceiverPort_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 50, 1, 30),
    _TrapReceiverPort_Type()
)
trapReceiverPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverPort.setStatus("current")


class _TrapReceiverName_Type(DisplayString):
    """Custom type trapReceiverName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TrapReceiverName_Type.__name__ = "DisplayString"
_TrapReceiverName_Object = MibTableColumn
trapReceiverName = _TrapReceiverName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 50, 1, 40),
    _TrapReceiverName_Type()
)
trapReceiverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverName.setStatus("current")


class _TrapReceiverLevel_Type(SeverityLevel):
    """Custom type trapReceiverLevel based on SeverityLevel"""
    defaultValue = 4


_TrapReceiverLevel_Type.__name__ = "SeverityLevel"
_TrapReceiverLevel_Object = MibTableColumn
trapReceiverLevel = _TrapReceiverLevel_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 50, 1, 50),
    _TrapReceiverLevel_Type()
)
trapReceiverLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverLevel.setStatus("current")


class _TrapReceiverCommunity_Type(DisplayString):
    """Custom type trapReceiverCommunity based on DisplayString"""
    defaultValue = OctetString("EatonPublic")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrapReceiverCommunity_Type.__name__ = "DisplayString"
_TrapReceiverCommunity_Object = MibTableColumn
trapReceiverCommunity = _TrapReceiverCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 50, 1, 60),
    _TrapReceiverCommunity_Type()
)
trapReceiverCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverCommunity.setStatus("current")


class _TrapReceiverMode_Type(TrapReceiverMode):
    """Custom type trapReceiverMode based on TrapReceiverMode"""
    defaultValue = 1


_TrapReceiverMode_Type.__name__ = "TrapReceiverMode"
_TrapReceiverMode_Object = MibTableColumn
trapReceiverMode = _TrapReceiverMode_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 50, 1, 70),
    _TrapReceiverMode_Type()
)
trapReceiverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverMode.setStatus("current")
_AcknowledgeAlarmSummaryTrap_Type = NoData
_AcknowledgeAlarmSummaryTrap_Object = MibTableColumn
acknowledgeAlarmSummaryTrap = _AcknowledgeAlarmSummaryTrap_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 50, 1, 80),
    _AcknowledgeAlarmSummaryTrap_Type()
)
acknowledgeAlarmSummaryTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acknowledgeAlarmSummaryTrap.setStatus("current")


class _SnmpV3PrivacyPassword_Type(DisplayString):
    """Custom type snmpV3PrivacyPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpV3PrivacyPassword_Type.__name__ = "DisplayString"
_SnmpV3PrivacyPassword_Object = MibScalar
snmpV3PrivacyPassword = _SnmpV3PrivacyPassword_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 70),
    _SnmpV3PrivacyPassword_Type()
)
snmpV3PrivacyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpV3PrivacyPassword.setStatus("current")


class _EnableHeartbeatTrap_Type(EnableState):
    """Custom type enableHeartbeatTrap based on EnableState"""
    defaultValue = 0


_EnableHeartbeatTrap_Type.__name__ = "EnableState"
_EnableHeartbeatTrap_Object = MibScalar
enableHeartbeatTrap = _EnableHeartbeatTrap_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 80),
    _EnableHeartbeatTrap_Type()
)
enableHeartbeatTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableHeartbeatTrap.setStatus("current")


class _HeartbeatTrapPeriod_Type(TimeIntervalInMinutes):
    """Custom type heartbeatTrapPeriod based on TimeIntervalInMinutes"""
    defaultValue = 60


_HeartbeatTrapPeriod_Type.__name__ = "TimeIntervalInMinutes"
_HeartbeatTrapPeriod_Object = MibScalar
heartbeatTrapPeriod = _HeartbeatTrapPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 60, 90),
    _HeartbeatTrapPeriod_Type()
)
heartbeatTrapPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heartbeatTrapPeriod.setStatus("current")
if mibBuilder.loadTexts:
    heartbeatTrapPeriod.setUnits("min")
_Email_ObjectIdentity = ObjectIdentity
email = _Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65)
)
if mibBuilder.loadTexts:
    email.setStatus("current")


class _EmailNotifications_Type(EnableState):
    """Custom type emailNotifications based on EnableState"""
    defaultValue = 0


_EmailNotifications_Type.__name__ = "EnableState"
_EmailNotifications_Object = MibScalar
emailNotifications = _EmailNotifications_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 10),
    _EmailNotifications_Type()
)
emailNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailNotifications.setStatus("current")


class _SmtpServerIpAddress_Type(InetAddress):
    """Custom type smtpServerIpAddress based on InetAddress"""
    defaultValue = OctetString("1.1.1.1")

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SmtpServerIpAddress_Type.__name__ = "InetAddress"
_SmtpServerIpAddress_Object = MibScalar
smtpServerIpAddress = _SmtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 20),
    _SmtpServerIpAddress_Type()
)
smtpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerIpAddress.setStatus("current")


class _SmtpServerPort_Type(Unsigned16):
    """Custom type smtpServerPort based on Unsigned16"""
    defaultValue = 25


_SmtpServerPort_Type.__name__ = "Unsigned16"
_SmtpServerPort_Object = MibScalar
smtpServerPort = _SmtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 30),
    _SmtpServerPort_Type()
)
smtpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerPort.setStatus("current")


class _EmailReturnAddress_Type(DisplayString):
    """Custom type emailReturnAddress based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_EmailReturnAddress_Type.__name__ = "DisplayString"
_EmailReturnAddress_Object = MibScalar
emailReturnAddress = _EmailReturnAddress_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 40),
    _EmailReturnAddress_Type()
)
emailReturnAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailReturnAddress.setStatus("current")


class _EmailFromAddress_Type(DisplayString):
    """Custom type emailFromAddress based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_EmailFromAddress_Type.__name__ = "DisplayString"
_EmailFromAddress_Object = MibScalar
emailFromAddress = _EmailFromAddress_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 42),
    _EmailFromAddress_Type()
)
emailFromAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailFromAddress.setStatus("current")


class _EmailValidAddress_Type(DisplayString):
    """Custom type emailValidAddress based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_EmailValidAddress_Type.__name__ = "DisplayString"
_EmailValidAddress_Object = MibScalar
emailValidAddress = _EmailValidAddress_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 43),
    _EmailValidAddress_Type()
)
emailValidAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailValidAddress.setStatus("current")


class _EmailSubjectPrefix_Type(DisplayString):
    """Custom type emailSubjectPrefix based on DisplayString"""
    defaultValue = OctetString("[DC-POWER] ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EmailSubjectPrefix_Type.__name__ = "DisplayString"
_EmailSubjectPrefix_Object = MibScalar
emailSubjectPrefix = _EmailSubjectPrefix_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 50),
    _EmailSubjectPrefix_Type()
)
emailSubjectPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSubjectPrefix.setStatus("current")
_EmailReceiverTable_Object = MibTable
emailReceiverTable = _EmailReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 60)
)
if mibBuilder.loadTexts:
    emailReceiverTable.setStatus("current")
_EmailReceiverEntry_Object = MibTableRow
emailReceiverEntry = _EmailReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 60, 1)
)
emailReceiverEntry.setIndexNames(
    (0, "RpsSc300Mib", "emailReceiverIndex"),
)
if mibBuilder.loadTexts:
    emailReceiverEntry.setStatus("current")


class _EmailReceiverIndex_Type(Unsigned8):
    """Custom type emailReceiverIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EmailReceiverIndex_Type.__name__ = "Unsigned8"
_EmailReceiverIndex_Object = MibTableColumn
emailReceiverIndex = _EmailReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 60, 1, 1),
    _EmailReceiverIndex_Type()
)
emailReceiverIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    emailReceiverIndex.setStatus("current")


class _EmailReceiverAddress_Type(DisplayString):
    """Custom type emailReceiverAddress based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_EmailReceiverAddress_Type.__name__ = "DisplayString"
_EmailReceiverAddress_Object = MibTableColumn
emailReceiverAddress = _EmailReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 60, 1, 10),
    _EmailReceiverAddress_Type()
)
emailReceiverAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailReceiverAddress.setStatus("current")


class _EmailReceiverLevel_Type(SeverityLevel):
    """Custom type emailReceiverLevel based on SeverityLevel"""
    defaultValue = 4


_EmailReceiverLevel_Type.__name__ = "SeverityLevel"
_EmailReceiverLevel_Object = MibTableColumn
emailReceiverLevel = _EmailReceiverLevel_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 60, 1, 20),
    _EmailReceiverLevel_Type()
)
emailReceiverLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailReceiverLevel.setStatus("current")


class _EmailReceiverDelay_Type(TimeIntervalInSeconds):
    """Custom type emailReceiverDelay based on TimeIntervalInSeconds"""
    defaultValue = 30


_EmailReceiverDelay_Type.__name__ = "TimeIntervalInSeconds"
_EmailReceiverDelay_Object = MibTableColumn
emailReceiverDelay = _EmailReceiverDelay_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 60, 1, 30),
    _EmailReceiverDelay_Type()
)
emailReceiverDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailReceiverDelay.setStatus("current")
if mibBuilder.loadTexts:
    emailReceiverDelay.setUnits("s")
_SendTestEmail_Type = NoData
_SendTestEmail_Object = MibTableColumn
sendTestEmail = _SendTestEmail_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 60, 1, 40),
    _SendTestEmail_Type()
)
sendTestEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendTestEmail.setStatus("current")
_SmtpResult_Type = Unsigned16
_SmtpResult_Object = MibTableColumn
smtpResult = _SmtpResult_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 65, 60, 1, 50),
    _SmtpResult_Type()
)
smtpResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpResult.setStatus("current")
_Sntp_ObjectIdentity = ObjectIdentity
sntp = _Sntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 70)
)
if mibBuilder.loadTexts:
    sntp.setStatus("current")


class _SntpPollInterval_Type(TimeIntervalInSeconds):
    """Custom type sntpPollInterval based on TimeIntervalInSeconds"""
    defaultValue = 3600


_SntpPollInterval_Type.__name__ = "TimeIntervalInSeconds"
_SntpPollInterval_Object = MibScalar
sntpPollInterval = _SntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 70, 10),
    _SntpPollInterval_Type()
)
sntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    sntpPollInterval.setUnits("s")


class _UdpPort_Type(Unsigned16):
    """Custom type udpPort based on Unsigned16"""
    defaultValue = 123


_UdpPort_Type.__name__ = "Unsigned16"
_UdpPort_Object = MibScalar
udpPort = _UdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 70, 20),
    _UdpPort_Type()
)
udpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpPort.setStatus("current")


class _PrimaryAddress_Type(DisplayString):
    """Custom type primaryAddress based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PrimaryAddress_Type.__name__ = "DisplayString"
_PrimaryAddress_Object = MibScalar
primaryAddress = _PrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 70, 30),
    _PrimaryAddress_Type()
)
primaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryAddress.setStatus("current")


class _BackupAddress_Type(DisplayString):
    """Custom type backupAddress based on DisplayString"""
    defaultValue = OctetString("time.nist.gov")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BackupAddress_Type.__name__ = "DisplayString"
_BackupAddress_Object = MibScalar
backupAddress = _BackupAddress_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 70, 40),
    _BackupAddress_Type()
)
backupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupAddress.setStatus("current")
_SntpLastUpdate_Type = JulianDateUtc25
_SntpLastUpdate_Object = MibScalar
sntpLastUpdate = _SntpLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 70, 50),
    _SntpLastUpdate_Type()
)
sntpLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpLastUpdate.setStatus("current")
_WebUserTable_Object = MibTable
webUserTable = _WebUserTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 80)
)
if mibBuilder.loadTexts:
    webUserTable.setStatus("current")
_WebUserEntry_Object = MibTableRow
webUserEntry = _WebUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 80, 1)
)
webUserEntry.setIndexNames(
    (0, "RpsSc300Mib", "webUserIndex"),
)
if mibBuilder.loadTexts:
    webUserEntry.setStatus("current")


class _WebUserIndex_Type(Unsigned8):
    """Custom type webUserIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WebUserIndex_Type.__name__ = "Unsigned8"
_WebUserIndex_Object = MibTableColumn
webUserIndex = _WebUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 80, 1, 1),
    _WebUserIndex_Type()
)
webUserIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    webUserIndex.setStatus("current")


class _UserName_Type(DisplayString):
    """Custom type userName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_UserName_Type.__name__ = "DisplayString"
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 80, 1, 10),
    _UserName_Type()
)
userName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _UserLogonId_Type(DisplayString):
    """Custom type userLogonId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserLogonId_Type.__name__ = "DisplayString"
_UserLogonId_Object = MibTableColumn
userLogonId = _UserLogonId_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 80, 1, 21),
    _UserLogonId_Type()
)
userLogonId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userLogonId.setStatus("current")


class _UserLogonPassword_Type(DisplayString):
    """Custom type userLogonPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UserLogonPassword_Type.__name__ = "DisplayString"
_UserLogonPassword_Object = MibTableColumn
userLogonPassword = _UserLogonPassword_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 80, 1, 31),
    _UserLogonPassword_Type()
)
userLogonPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userLogonPassword.setStatus("current")


class _UserActive_Type(Boolean):
    """Custom type userActive based on Boolean"""
    defaultValue = 0


_UserActive_Type.__name__ = "Boolean"
_UserActive_Object = MibTableColumn
userActive = _UserActive_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 80, 1, 40),
    _UserActive_Type()
)
userActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userActive.setStatus("current")


class _UserWrite_Type(Boolean):
    """Custom type userWrite based on Boolean"""
    defaultValue = 0


_UserWrite_Type.__name__ = "Boolean"
_UserWrite_Object = MibTableColumn
userWrite = _UserWrite_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 80, 1, 60),
    _UserWrite_Type()
)
userWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userWrite.setStatus("current")


class _UserRestore_Type(Boolean):
    """Custom type userRestore based on Boolean"""
    defaultValue = 0


_UserRestore_Type.__name__ = "Boolean"
_UserRestore_Object = MibTableColumn
userRestore = _UserRestore_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 80, 1, 70),
    _UserRestore_Type()
)
userRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userRestore.setStatus("current")


class _UserBackup_Type(Boolean):
    """Custom type userBackup based on Boolean"""
    defaultValue = 0


_UserBackup_Type.__name__ = "Boolean"
_UserBackup_Object = MibTableColumn
userBackup = _UserBackup_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 80, 1, 80),
    _UserBackup_Type()
)
userBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userBackup.setStatus("current")


class _UserExecute_Type(Boolean):
    """Custom type userExecute based on Boolean"""
    defaultValue = 0


_UserExecute_Type.__name__ = "Boolean"
_UserExecute_Object = MibTableColumn
userExecute = _UserExecute_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 80, 1, 90),
    _UserExecute_Type()
)
userExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userExecute.setStatus("current")


class _UserUpgradeFirmware_Type(Boolean):
    """Custom type userUpgradeFirmware based on Boolean"""
    defaultValue = 0


_UserUpgradeFirmware_Type.__name__ = "Boolean"
_UserUpgradeFirmware_Object = MibTableColumn
userUpgradeFirmware = _UserUpgradeFirmware_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 80, 1, 100),
    _UserUpgradeFirmware_Type()
)
userUpgradeFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userUpgradeFirmware.setStatus("current")


class _UserAdministrator_Type(Boolean):
    """Custom type userAdministrator based on Boolean"""
    defaultValue = 0


_UserAdministrator_Type.__name__ = "Boolean"
_UserAdministrator_Object = MibTableColumn
userAdministrator = _UserAdministrator_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 80, 1, 110),
    _UserAdministrator_Type()
)
userAdministrator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAdministrator.setStatus("current")


class _UserSnmp_Type(UserSnmp):
    """Custom type userSnmp based on UserSnmp"""
    defaultValue = 0


_UserSnmp_Type.__name__ = "UserSnmp"
_UserSnmp_Object = MibTableColumn
userSnmp = _UserSnmp_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 80, 1, 120),
    _UserSnmp_Type()
)
userSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSnmp.setStatus("current")
_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 90)
)
if mibBuilder.loadTexts:
    radius.setStatus("current")


class _AuthServer_Type(InetAddress):
    """Custom type authServer based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AuthServer_Type.__name__ = "InetAddress"
_AuthServer_Object = MibScalar
authServer = _AuthServer_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 90, 10),
    _AuthServer_Type()
)
authServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authServer.setStatus("current")


class _RadiusAuthSvrSecret_Type(DisplayString):
    """Custom type radiusAuthSvrSecret based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RadiusAuthSvrSecret_Type.__name__ = "DisplayString"
_RadiusAuthSvrSecret_Object = MibScalar
radiusAuthSvrSecret = _RadiusAuthSvrSecret_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 90, 20),
    _RadiusAuthSvrSecret_Type()
)
radiusAuthSvrSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthSvrSecret.setStatus("current")


class _AcctServer_Type(InetAddress):
    """Custom type acctServer based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AcctServer_Type.__name__ = "InetAddress"
_AcctServer_Object = MibScalar
acctServer = _AcctServer_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 90, 30),
    _AcctServer_Type()
)
acctServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acctServer.setStatus("current")


class _RadiusAcctSvrSecret_Type(DisplayString):
    """Custom type radiusAcctSvrSecret based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RadiusAcctSvrSecret_Type.__name__ = "DisplayString"
_RadiusAcctSvrSecret_Object = MibScalar
radiusAcctSvrSecret = _RadiusAcctSvrSecret_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 90, 40),
    _RadiusAcctSvrSecret_Type()
)
radiusAcctSvrSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAcctSvrSecret.setStatus("current")


class _IpAddressAuto_Type(DisplayString):
    """Custom type ipAddressAuto based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_IpAddressAuto_Type.__name__ = "DisplayString"
_IpAddressAuto_Object = MibScalar
ipAddressAuto = _IpAddressAuto_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 100),
    _IpAddressAuto_Type()
)
ipAddressAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressAuto.setStatus("current")


class _SubnetMaskAuto_Type(DisplayString):
    """Custom type subnetMaskAuto based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SubnetMaskAuto_Type.__name__ = "DisplayString"
_SubnetMaskAuto_Object = MibScalar
subnetMaskAuto = _SubnetMaskAuto_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 110),
    _SubnetMaskAuto_Type()
)
subnetMaskAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetMaskAuto.setStatus("current")


class _GatewayAddressAuto_Type(DisplayString):
    """Custom type gatewayAddressAuto based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_GatewayAddressAuto_Type.__name__ = "DisplayString"
_GatewayAddressAuto_Object = MibScalar
gatewayAddressAuto = _GatewayAddressAuto_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 120),
    _GatewayAddressAuto_Type()
)
gatewayAddressAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayAddressAuto.setStatus("current")


class _AutoIp_Type(EnableState):
    """Custom type autoIp based on EnableState"""
    defaultValue = 1


_AutoIp_Type.__name__ = "EnableState"
_AutoIp_Object = MibScalar
autoIp = _AutoIp_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 130),
    _AutoIp_Type()
)
autoIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoIp.setStatus("current")


class _WebSessionTimeout_Type(TimeIntervalInMinutes):
    """Custom type webSessionTimeout based on TimeIntervalInMinutes"""
    defaultValue = 10


_WebSessionTimeout_Type.__name__ = "TimeIntervalInMinutes"
_WebSessionTimeout_Object = MibScalar
webSessionTimeout = _WebSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 140),
    _WebSessionTimeout_Type()
)
webSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    webSessionTimeout.setUnits("min")


class _WebAccess_Type(WebAccess):
    """Custom type webAccess based on WebAccess"""
    defaultValue = 1


_WebAccess_Type.__name__ = "WebAccess"
_WebAccess_Object = MibScalar
webAccess = _WebAccess_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 150),
    _WebAccess_Type()
)
webAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAccess.setStatus("current")


class _Blacklist_Type(EnableState):
    """Custom type blacklist based on EnableState"""
    defaultValue = 1


_Blacklist_Type.__name__ = "EnableState"
_Blacklist_Object = MibScalar
blacklist = _Blacklist_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 160),
    _Blacklist_Type()
)
blacklist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blacklist.setStatus("current")


class _Blacklisted_Type(DisplayString):
    """Custom type blacklisted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 150),
    )


_Blacklisted_Type.__name__ = "DisplayString"
_Blacklisted_Object = MibScalar
blacklisted = _Blacklisted_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 30, 170),
    _Blacklisted_Type()
)
blacklisted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blacklisted.setStatus("current")
_AccessControl_ObjectIdentity = ObjectIdentity
accessControl = _AccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 33)
)
if mibBuilder.loadTexts:
    accessControl.setStatus("current")


class _UiAccess_Type(AccessProtection):
    """Custom type uiAccess based on AccessProtection"""
    defaultValue = 0


_UiAccess_Type.__name__ = "AccessProtection"
_UiAccess_Object = MibScalar
uiAccess = _UiAccess_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 33, 10),
    _UiAccess_Type()
)
uiAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uiAccess.setStatus("current")


class _S3pWriteAccessPassword_Type(DisplayString):
    """Custom type s3pWriteAccessPassword based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_S3pWriteAccessPassword_Type.__name__ = "DisplayString"
_S3pWriteAccessPassword_Object = MibScalar
s3pWriteAccessPassword = _S3pWriteAccessPassword_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 33, 20),
    _S3pWriteAccessPassword_Type()
)
s3pWriteAccessPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3pWriteAccessPassword.setStatus("current")
_RemoteAccessLevel_Type = AccessLevel
_RemoteAccessLevel_Object = MibScalar
remoteAccessLevel = _RemoteAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 33, 30),
    _RemoteAccessLevel_Type()
)
remoteAccessLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessLevel.setStatus("current")
_UploadingFirmware_Type = Unsigned8
_UploadingFirmware_Object = MibScalar
uploadingFirmware = _UploadingFirmware_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 33, 40),
    _UploadingFirmware_Type()
)
uploadingFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uploadingFirmware.setStatus("current")
if mibBuilder.loadTexts:
    uploadingFirmware.setUnits("%")
_AcInput_ObjectIdentity = ObjectIdentity
acInput = _AcInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 40)
)
if mibBuilder.loadTexts:
    acInput.setStatus("current")
_AcVoltage_Type = Float
_AcVoltage_Object = MibScalar
acVoltage = _AcVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 40, 10),
    _AcVoltage_Type()
)
acVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acVoltage.setStatus("current")
if mibBuilder.loadTexts:
    acVoltage.setUnits("V")
_Phase1_Type = Float
_Phase1_Object = MibScalar
phase1 = _Phase1_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 40, 20),
    _Phase1_Type()
)
phase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phase1.setStatus("current")
if mibBuilder.loadTexts:
    phase1.setUnits("V")
_Phase2_Type = Float
_Phase2_Object = MibScalar
phase2 = _Phase2_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 40, 30),
    _Phase2_Type()
)
phase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phase2.setStatus("current")
if mibBuilder.loadTexts:
    phase2.setUnits("V")
_Phase3_Type = Float
_Phase3_Object = MibScalar
phase3 = _Phase3_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 40, 40),
    _Phase3_Type()
)
phase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phase3.setStatus("current")
if mibBuilder.loadTexts:
    phase3.setUnits("V")
_DcOutput_ObjectIdentity = ObjectIdentity
dcOutput = _DcOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 50)
)
if mibBuilder.loadTexts:
    dcOutput.setStatus("current")
_LoadCurrent_Type = Float
_LoadCurrent_Object = MibScalar
loadCurrent = _LoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 50, 10),
    _LoadCurrent_Type()
)
loadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadCurrent.setStatus("current")
if mibBuilder.loadTexts:
    loadCurrent.setUnits("A")
_SystemPower_Type = Percentile8Nan
_SystemPower_Object = MibScalar
systemPower = _SystemPower_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 50, 20),
    _SystemPower_Type()
)
systemPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPower.setStatus("current")
if mibBuilder.loadTexts:
    systemPower.setUnits("%")
_LoadPower_Type = Float
_LoadPower_Object = MibScalar
loadPower = _LoadPower_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 50, 30),
    _LoadPower_Type()
)
loadPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadPower.setStatus("current")
if mibBuilder.loadTexts:
    loadPower.setUnits("0.01 kW")
_Rxp_ObjectIdentity = ObjectIdentity
rxp = _Rxp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55)
)
if mibBuilder.loadTexts:
    rxp.setStatus("current")
_RxpTable_Object = MibTable
rxpTable = _RxpTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 10)
)
if mibBuilder.loadTexts:
    rxpTable.setStatus("current")
_RxpEntry_Object = MibTableRow
rxpEntry = _RxpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 10, 1)
)
rxpEntry.setIndexNames(
    (0, "RpsSc300Mib", "rxpIndex"),
)
if mibBuilder.loadTexts:
    rxpEntry.setStatus("current")


class _RxpIndex_Type(Unsigned8):
    """Custom type rxpIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RxpIndex_Type.__name__ = "Unsigned8"
_RxpIndex_Object = MibTableColumn
rxpIndex = _RxpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 10, 1, 1),
    _RxpIndex_Type()
)
rxpIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rxpIndex.setStatus("current")
_RxpSlaveRegistrationState_Type = RcpSlaveState
_RxpSlaveRegistrationState_Object = MibTableColumn
rxpSlaveRegistrationState = _RxpSlaveRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 10, 1, 10),
    _RxpSlaveRegistrationState_Type()
)
rxpSlaveRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxpSlaveRegistrationState.setStatus("current")


class _RxpSlaveName_Type(DisplayString):
    """Custom type rxpSlaveName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RxpSlaveName_Type.__name__ = "DisplayString"
_RxpSlaveName_Object = MibTableColumn
rxpSlaveName = _RxpSlaveName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 10, 1, 20),
    _RxpSlaveName_Type()
)
rxpSlaveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxpSlaveName.setStatus("current")
_RxpSlaveSerialNumber_Type = Integer32
_RxpSlaveSerialNumber_Object = MibTableColumn
rxpSlaveSerialNumber = _RxpSlaveSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 10, 1, 30),
    _RxpSlaveSerialNumber_Type()
)
rxpSlaveSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxpSlaveSerialNumber.setStatus("current")
_RxpSlaveType_Type = RxpSlaveType
_RxpSlaveType_Object = MibTableColumn
rxpSlaveType = _RxpSlaveType_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 10, 1, 40),
    _RxpSlaveType_Type()
)
rxpSlaveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxpSlaveType.setStatus("current")
_RxpSlaveCommandSet_Type = Integer32
_RxpSlaveCommandSet_Object = MibTableColumn
rxpSlaveCommandSet = _RxpSlaveCommandSet_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 10, 1, 50),
    _RxpSlaveCommandSet_Type()
)
rxpSlaveCommandSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxpSlaveCommandSet.setStatus("current")


class _RxpBomRevision_Type(DisplayString):
    """Custom type rxpBomRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RxpBomRevision_Type.__name__ = "DisplayString"
_RxpBomRevision_Object = MibTableColumn
rxpBomRevision = _RxpBomRevision_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 10, 1, 60),
    _RxpBomRevision_Type()
)
rxpBomRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxpBomRevision.setStatus("current")


class _RxpSoftwareVersion_Type(DisplayString):
    """Custom type rxpSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RxpSoftwareVersion_Type.__name__ = "DisplayString"
_RxpSoftwareVersion_Object = MibTableColumn
rxpSoftwareVersion = _RxpSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 10, 1, 70),
    _RxpSoftwareVersion_Type()
)
rxpSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxpSoftwareVersion.setStatus("current")
_IdentifyRxpSlave_Type = Boolean
_IdentifyRxpSlave_Object = MibTableColumn
identifyRxpSlave = _IdentifyRxpSlave_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 10, 1, 80),
    _IdentifyRxpSlave_Type()
)
identifyRxpSlave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identifyRxpSlave.setStatus("current")
_IobTable_Object = MibTable
iobTable = _IobTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 20)
)
if mibBuilder.loadTexts:
    iobTable.setStatus("current")
_IobEntry_Object = MibTableRow
iobEntry = _IobEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 20, 1)
)
iobEntry.setIndexNames(
    (0, "RpsSc300Mib", "iobIndex"),
)
if mibBuilder.loadTexts:
    iobEntry.setStatus("current")


class _IobIndex_Type(Unsigned8):
    """Custom type iobIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IobIndex_Type.__name__ = "Unsigned8"
_IobIndex_Object = MibTableColumn
iobIndex = _IobIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 20, 1, 1),
    _IobIndex_Type()
)
iobIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    iobIndex.setStatus("current")
_IobRegistrationState_Type = RcpSlaveState
_IobRegistrationState_Object = MibTableColumn
iobRegistrationState = _IobRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 20, 1, 10),
    _IobRegistrationState_Type()
)
iobRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iobRegistrationState.setStatus("current")


class _IobSerialNumber_Type(Integer32):
    """Custom type iobSerialNumber based on Integer32"""
    defaultValue = 0


_IobSerialNumber_Type.__name__ = "Integer32"
_IobSerialNumber_Object = MibTableColumn
iobSerialNumber = _IobSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 20, 1, 20),
    _IobSerialNumber_Type()
)
iobSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iobSerialNumber.setStatus("current")


class _IobMapping_Type(Unsigned8):
    """Custom type iobMapping based on Unsigned8"""
    defaultValue = 0


_IobMapping_Type.__name__ = "Unsigned8"
_IobMapping_Object = MibTableColumn
iobMapping = _IobMapping_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 20, 1, 30),
    _IobMapping_Type()
)
iobMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iobMapping.setStatus("current")
_IobNumberOfVoltages_Type = Unsigned8
_IobNumberOfVoltages_Object = MibTableColumn
iobNumberOfVoltages = _IobNumberOfVoltages_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 20, 1, 40),
    _IobNumberOfVoltages_Type()
)
iobNumberOfVoltages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iobNumberOfVoltages.setStatus("current")
_IobNumberOfCurrents_Type = Unsigned8
_IobNumberOfCurrents_Object = MibTableColumn
iobNumberOfCurrents = _IobNumberOfCurrents_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 20, 1, 50),
    _IobNumberOfCurrents_Type()
)
iobNumberOfCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iobNumberOfCurrents.setStatus("current")
_IobNumberOfTemperatures_Type = Unsigned8
_IobNumberOfTemperatures_Object = MibTableColumn
iobNumberOfTemperatures = _IobNumberOfTemperatures_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 20, 1, 60),
    _IobNumberOfTemperatures_Type()
)
iobNumberOfTemperatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iobNumberOfTemperatures.setStatus("current")
_IobNumberOfDigitalInputs_Type = Unsigned8
_IobNumberOfDigitalInputs_Object = MibTableColumn
iobNumberOfDigitalInputs = _IobNumberOfDigitalInputs_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 20, 1, 70),
    _IobNumberOfDigitalInputs_Type()
)
iobNumberOfDigitalInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iobNumberOfDigitalInputs.setStatus("current")
_IobNumberOfRelays_Type = Unsigned8
_IobNumberOfRelays_Object = MibTableColumn
iobNumberOfRelays = _IobNumberOfRelays_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 20, 1, 80),
    _IobNumberOfRelays_Type()
)
iobNumberOfRelays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iobNumberOfRelays.setStatus("current")
_IobNumberOfLvds_Type = Unsigned8
_IobNumberOfLvds_Object = MibTableColumn
iobNumberOfLvds = _IobNumberOfLvds_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 55, 20, 1, 90),
    _IobNumberOfLvds_Type()
)
iobNumberOfLvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iobNumberOfLvds.setStatus("current")
_Rectifiers_ObjectIdentity = ObjectIdentity
rectifiers = _Rectifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60)
)
if mibBuilder.loadTexts:
    rectifiers.setStatus("current")
_NumberOfRegisteredRectifiers_Type = Unsigned8
_NumberOfRegisteredRectifiers_Object = MibScalar
numberOfRegisteredRectifiers = _NumberOfRegisteredRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 10),
    _NumberOfRegisteredRectifiers_Type()
)
numberOfRegisteredRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfRegisteredRectifiers.setStatus("current")
_NumberOfRegisteredSolarChargers_Type = Unsigned8
_NumberOfRegisteredSolarChargers_Object = MibScalar
numberOfRegisteredSolarChargers = _NumberOfRegisteredSolarChargers_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 11),
    _NumberOfRegisteredSolarChargers_Type()
)
numberOfRegisteredSolarChargers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfRegisteredSolarChargers.setStatus("current")
_NumberOfRectifiersFailed_Type = Unsigned8
_NumberOfRectifiersFailed_Object = MibScalar
numberOfRectifiersFailed = _NumberOfRectifiersFailed_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 13),
    _NumberOfRectifiersFailed_Type()
)
numberOfRectifiersFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfRectifiersFailed.setStatus("current")
_NumberOfSolarFailed_Type = Unsigned8
_NumberOfSolarFailed_Object = MibScalar
numberOfSolarFailed = _NumberOfSolarFailed_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 14),
    _NumberOfSolarFailed_Type()
)
numberOfSolarFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfSolarFailed.setStatus("current")
_NumberOfRectifiersCommsLost_Type = Unsigned8
_NumberOfRectifiersCommsLost_Object = MibScalar
numberOfRectifiersCommsLost = _NumberOfRectifiersCommsLost_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 17),
    _NumberOfRectifiersCommsLost_Type()
)
numberOfRectifiersCommsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfRectifiersCommsLost.setStatus("current")
_NumberOfSolarCommsLost_Type = Unsigned8
_NumberOfSolarCommsLost_Object = MibScalar
numberOfSolarCommsLost = _NumberOfSolarCommsLost_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 18),
    _NumberOfSolarCommsLost_Type()
)
numberOfSolarCommsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfSolarCommsLost.setStatus("current")
_RectifierCurrent_Type = Float
_RectifierCurrent_Object = MibScalar
rectifierCurrent = _RectifierCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 20),
    _RectifierCurrent_Type()
)
rectifierCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierCurrent.setStatus("current")
if mibBuilder.loadTexts:
    rectifierCurrent.setUnits("A")


class _RectifierCurrentLimit_Type(Unsigned8):
    """Custom type rectifierCurrentLimit based on Unsigned8"""
    defaultValue = 0


_RectifierCurrentLimit_Type.__name__ = "Unsigned8"
_RectifierCurrentLimit_Object = MibScalar
rectifierCurrentLimit = _RectifierCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 23),
    _RectifierCurrentLimit_Type()
)
rectifierCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    rectifierCurrentLimit.setUnits("A")


class _SolarCurrentLimit_Type(Unsigned8):
    """Custom type solarCurrentLimit based on Unsigned8"""
    defaultValue = 0


_SolarCurrentLimit_Type.__name__ = "Unsigned8"
_SolarCurrentLimit_Object = MibScalar
solarCurrentLimit = _SolarCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 24),
    _SolarCurrentLimit_Type()
)
solarCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    solarCurrentLimit.setUnits("A")


class _EnableCurrentShare_Type(EnableState):
    """Custom type enableCurrentShare based on EnableState"""
    defaultValue = 1


_EnableCurrentShare_Type.__name__ = "EnableState"
_EnableCurrentShare_Object = MibScalar
enableCurrentShare = _EnableCurrentShare_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 26),
    _EnableCurrentShare_Type()
)
enableCurrentShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableCurrentShare.setStatus("current")
_HighestRectifierHeatsinkTemperature_Type = Float
_HighestRectifierHeatsinkTemperature_Object = MibScalar
highestRectifierHeatsinkTemperature = _HighestRectifierHeatsinkTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 29),
    _HighestRectifierHeatsinkTemperature_Type()
)
highestRectifierHeatsinkTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highestRectifierHeatsinkTemperature.setStatus("current")
if mibBuilder.loadTexts:
    highestRectifierHeatsinkTemperature.setUnits("°C")
_RectifierValuesTable_Object = MibTable
rectifierValuesTable = _RectifierValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30)
)
if mibBuilder.loadTexts:
    rectifierValuesTable.setStatus("current")
_RectifierValuesEntry_Object = MibTableRow
rectifierValuesEntry = _RectifierValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1)
)
rectifierValuesEntry.setIndexNames(
    (0, "RpsSc300Mib", "rectifierValuesIndex"),
)
if mibBuilder.loadTexts:
    rectifierValuesEntry.setStatus("current")


class _RectifierValuesIndex_Type(Unsigned8):
    """Custom type rectifierValuesIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RectifierValuesIndex_Type.__name__ = "Unsigned8"
_RectifierValuesIndex_Object = MibTableColumn
rectifierValuesIndex = _RectifierValuesIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 1),
    _RectifierValuesIndex_Type()
)
rectifierValuesIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rectifierValuesIndex.setStatus("current")
_RectifierSerialNumber_Type = Integer32
_RectifierSerialNumber_Object = MibTableColumn
rectifierSerialNumber = _RectifierSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 30),
    _RectifierSerialNumber_Type()
)
rectifierSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierSerialNumber.setStatus("current")


class _RectifierType_Type(DisplayString):
    """Custom type rectifierType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifierType_Type.__name__ = "DisplayString"
_RectifierType_Object = MibTableColumn
rectifierType = _RectifierType_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 40),
    _RectifierType_Type()
)
rectifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierType.setStatus("current")
_RectifierInputType_Type = InputType
_RectifierInputType_Object = MibTableColumn
rectifierInputType = _RectifierInputType_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 50),
    _RectifierInputType_Type()
)
rectifierInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierInputType.setStatus("current")
_RectifierStatus_Type = Unsigned8
_RectifierStatus_Object = MibTableColumn
rectifierStatus = _RectifierStatus_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 60),
    _RectifierStatus_Type()
)
rectifierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatus.setStatus("current")
_RectifierMaximumCurrentLimit_Type = Unsigned8
_RectifierMaximumCurrentLimit_Object = MibTableColumn
rectifierMaximumCurrentLimit = _RectifierMaximumCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 70),
    _RectifierMaximumCurrentLimit_Type()
)
rectifierMaximumCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierMaximumCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    rectifierMaximumCurrentLimit.setUnits("A")
_RectifierMaximumPowerLimit_Type = DcPower
_RectifierMaximumPowerLimit_Object = MibTableColumn
rectifierMaximumPowerLimit = _RectifierMaximumPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 80),
    _RectifierMaximumPowerLimit_Type()
)
rectifierMaximumPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierMaximumPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    rectifierMaximumPowerLimit.setUnits("W")
_RectifierMinimumOvsdSetPoint_Type = Float
_RectifierMinimumOvsdSetPoint_Object = MibTableColumn
rectifierMinimumOvsdSetPoint = _RectifierMinimumOvsdSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 83),
    _RectifierMinimumOvsdSetPoint_Type()
)
rectifierMinimumOvsdSetPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierMinimumOvsdSetPoint.setStatus("current")
if mibBuilder.loadTexts:
    rectifierMinimumOvsdSetPoint.setUnits("0.01 V")
_RectifierMaximumOvsdSetPoint_Type = Float
_RectifierMaximumOvsdSetPoint_Object = MibTableColumn
rectifierMaximumOvsdSetPoint = _RectifierMaximumOvsdSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 86),
    _RectifierMaximumOvsdSetPoint_Type()
)
rectifierMaximumOvsdSetPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierMaximumOvsdSetPoint.setStatus("current")
if mibBuilder.loadTexts:
    rectifierMaximumOvsdSetPoint.setUnits("0.01 V")
_RectifierInputVoltage_Type = Float
_RectifierInputVoltage_Object = MibTableColumn
rectifierInputVoltage = _RectifierInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 90),
    _RectifierInputVoltage_Type()
)
rectifierInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    rectifierInputVoltage.setUnits("V")
_RectifierReportedVoltage_Type = Float
_RectifierReportedVoltage_Object = MibTableColumn
rectifierReportedVoltage = _RectifierReportedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 95),
    _RectifierReportedVoltage_Type()
)
rectifierReportedVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierReportedVoltage.setStatus("current")
if mibBuilder.loadTexts:
    rectifierReportedVoltage.setUnits("0.01 V")
_RectifierReportedCurrent_Type = Float
_RectifierReportedCurrent_Object = MibTableColumn
rectifierReportedCurrent = _RectifierReportedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 100),
    _RectifierReportedCurrent_Type()
)
rectifierReportedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierReportedCurrent.setStatus("current")
if mibBuilder.loadTexts:
    rectifierReportedCurrent.setUnits("A")
_RectifierOutputPowerw_Type = DcPower
_RectifierOutputPowerw_Object = MibTableColumn
rectifierOutputPowerw = _RectifierOutputPowerw_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 103),
    _RectifierOutputPowerw_Type()
)
rectifierOutputPowerw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierOutputPowerw.setStatus("current")
if mibBuilder.loadTexts:
    rectifierOutputPowerw.setUnits("W")
_RectifierOutputPower_Type = Float
_RectifierOutputPower_Object = MibTableColumn
rectifierOutputPower = _RectifierOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 105),
    _RectifierOutputPower_Type()
)
rectifierOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    rectifierOutputPower.setUnits("0.1 %")
_RectifierHeatsinkTemperature_Type = Float
_RectifierHeatsinkTemperature_Object = MibTableColumn
rectifierHeatsinkTemperature = _RectifierHeatsinkTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 110),
    _RectifierHeatsinkTemperature_Type()
)
rectifierHeatsinkTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierHeatsinkTemperature.setStatus("current")
if mibBuilder.loadTexts:
    rectifierHeatsinkTemperature.setUnits("°C")
_RectifierRegistrationState_Type = RcpSlaveState
_RectifierRegistrationState_Object = MibTableColumn
rectifierRegistrationState = _RectifierRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 120),
    _RectifierRegistrationState_Type()
)
rectifierRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierRegistrationState.setStatus("current")
_RectifierFailedState_Type = RectFailState
_RectifierFailedState_Object = MibTableColumn
rectifierFailedState = _RectifierFailedState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 130),
    _RectifierFailedState_Type()
)
rectifierFailedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierFailedState.setStatus("current")
_LoadBasedRunTime_Type = TimeIntervalInSeconds
_LoadBasedRunTime_Object = MibTableColumn
loadBasedRunTime = _LoadBasedRunTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 140),
    _LoadBasedRunTime_Type()
)
loadBasedRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadBasedRunTime.setStatus("current")
if mibBuilder.loadTexts:
    loadBasedRunTime.setUnits("s")
_ShutdownRectifier_Type = Boolean
_ShutdownRectifier_Object = MibTableColumn
shutdownRectifier = _ShutdownRectifier_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 150),
    _ShutdownRectifier_Type()
)
shutdownRectifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shutdownRectifier.setStatus("current")
_RectifierHasBeenShutdown_Type = Boolean
_RectifierHasBeenShutdown_Object = MibTableColumn
rectifierHasBeenShutdown = _RectifierHasBeenShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 160),
    _RectifierHasBeenShutdown_Type()
)
rectifierHasBeenShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierHasBeenShutdown.setStatus("current")
_RectifierPhase1_Type = Float
_RectifierPhase1_Object = MibTableColumn
rectifierPhase1 = _RectifierPhase1_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 170),
    _RectifierPhase1_Type()
)
rectifierPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierPhase1.setStatus("current")
if mibBuilder.loadTexts:
    rectifierPhase1.setUnits("V")
_RectifierPhase2_Type = Float
_RectifierPhase2_Object = MibTableColumn
rectifierPhase2 = _RectifierPhase2_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 180),
    _RectifierPhase2_Type()
)
rectifierPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierPhase2.setStatus("current")
if mibBuilder.loadTexts:
    rectifierPhase2.setUnits("V")
_RectifierPhase3_Type = Float
_RectifierPhase3_Object = MibTableColumn
rectifierPhase3 = _RectifierPhase3_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 190),
    _RectifierPhase3_Type()
)
rectifierPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierPhase3.setStatus("current")
if mibBuilder.loadTexts:
    rectifierPhase3.setUnits("V")


class _RectifierNotes_Type(DisplayString):
    """Custom type rectifierNotes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_RectifierNotes_Type.__name__ = "DisplayString"
_RectifierNotes_Object = MibTableColumn
rectifierNotes = _RectifierNotes_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 200),
    _RectifierNotes_Type()
)
rectifierNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierNotes.setStatus("current")
_RectifierInputCurrent_Type = Float
_RectifierInputCurrent_Object = MibTableColumn
rectifierInputCurrent = _RectifierInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 210),
    _RectifierInputCurrent_Type()
)
rectifierInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierInputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    rectifierInputCurrent.setUnits("A")
_RectifierPhase_Type = AcPhase
_RectifierPhase_Object = MibTableColumn
rectifierPhase = _RectifierPhase_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 30, 1, 220),
    _RectifierPhase_Type()
)
rectifierPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierPhase.setStatus("current")


class _Phase1SerialNumber_Type(Integer32):
    """Custom type phase1SerialNumber based on Integer32"""
    defaultValue = 0


_Phase1SerialNumber_Type.__name__ = "Integer32"
_Phase1SerialNumber_Object = MibScalar
phase1SerialNumber = _Phase1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 42),
    _Phase1SerialNumber_Type()
)
phase1SerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phase1SerialNumber.setStatus("current")
_AcInputCurrent_Type = Float
_AcInputCurrent_Object = MibScalar
acInputCurrent = _AcInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 43),
    _AcInputCurrent_Type()
)
acInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acInputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    acInputCurrent.setUnits("A")
_DcInputCurrent_Type = Float
_DcInputCurrent_Object = MibScalar
dcInputCurrent = _DcInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 44),
    _DcInputCurrent_Type()
)
dcInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dcInputCurrent.setUnits("A")


class _RectifierShutdownMode_Type(RectifierShutdownMode):
    """Custom type rectifierShutdownMode based on RectifierShutdownMode"""
    defaultValue = 0


_RectifierShutdownMode_Type.__name__ = "RectifierShutdownMode"
_RectifierShutdownMode_Object = MibScalar
rectifierShutdownMode = _RectifierShutdownMode_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 55),
    _RectifierShutdownMode_Type()
)
rectifierShutdownMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierShutdownMode.setStatus("current")
_RestartAllRectifiers_Type = NoData
_RestartAllRectifiers_Object = MibScalar
restartAllRectifiers = _RestartAllRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 60),
    _RestartAllRectifiers_Type()
)
restartAllRectifiers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartAllRectifiers.setStatus("current")


class _RectifierShutdownSmartAlarm_Type(Unsigned8):
    """Custom type rectifierShutdownSmartAlarm based on Unsigned8"""
    defaultValue = 0


_RectifierShutdownSmartAlarm_Type.__name__ = "Unsigned8"
_RectifierShutdownSmartAlarm_Object = MibScalar
rectifierShutdownSmartAlarm = _RectifierShutdownSmartAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 65),
    _RectifierShutdownSmartAlarm_Type()
)
rectifierShutdownSmartAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierShutdownSmartAlarm.setStatus("current")
_LoadBasedRectifierShutdownConfig_ObjectIdentity = ObjectIdentity
loadBasedRectifierShutdownConfig = _LoadBasedRectifierShutdownConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 70)
)
if mibBuilder.loadTexts:
    loadBasedRectifierShutdownConfig.setStatus("current")


class _RectCycleLowThreshold_Type(Unsigned8):
    """Custom type rectCycleLowThreshold based on Unsigned8"""
    defaultValue = 40


_RectCycleLowThreshold_Type.__name__ = "Unsigned8"
_RectCycleLowThreshold_Object = MibScalar
rectCycleLowThreshold = _RectCycleLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 70, 20),
    _RectCycleLowThreshold_Type()
)
rectCycleLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectCycleLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rectCycleLowThreshold.setUnits("%")


class _RectCycleHighThreshold_Type(Unsigned8):
    """Custom type rectCycleHighThreshold based on Unsigned8"""
    defaultValue = 60


_RectCycleHighThreshold_Type.__name__ = "Unsigned8"
_RectCycleHighThreshold_Object = MibScalar
rectCycleHighThreshold = _RectCycleHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 70, 30),
    _RectCycleHighThreshold_Type()
)
rectCycleHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectCycleHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rectCycleHighThreshold.setUnits("%")


class _RectCycleInterval_Type(TimeIntervalInMinutes):
    """Custom type rectCycleInterval based on TimeIntervalInMinutes"""
    defaultValue = 10080


_RectCycleInterval_Type.__name__ = "TimeIntervalInMinutes"
_RectCycleInterval_Object = MibScalar
rectCycleInterval = _RectCycleInterval_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 70, 40),
    _RectCycleInterval_Type()
)
rectCycleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectCycleInterval.setStatus("current")
if mibBuilder.loadTexts:
    rectCycleInterval.setUnits("min")


class _Redundancy_Type(Redundancy):
    """Custom type redundancy based on Redundancy"""
    defaultValue = 2


_Redundancy_Type.__name__ = "Redundancy"
_Redundancy_Object = MibScalar
redundancy = _Redundancy_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 70, 50),
    _Redundancy_Type()
)
redundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancy.setStatus("current")
_ResetRunTimes_Type = NoData
_ResetRunTimes_Object = MibScalar
resetRunTimes = _ResetRunTimes_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 70, 100),
    _ResetRunTimes_Type()
)
resetRunTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetRunTimes.setStatus("current")


class _RampUpSlope_Type(Unsigned8):
    """Custom type rampUpSlope based on Unsigned8"""
    defaultValue = 20


_RampUpSlope_Type.__name__ = "Unsigned8"
_RampUpSlope_Object = MibScalar
rampUpSlope = _RampUpSlope_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 80),
    _RampUpSlope_Type()
)
rampUpSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rampUpSlope.setStatus("current")
if mibBuilder.loadTexts:
    rampUpSlope.setUnits("%/s")


class _OvsdSetPoint_Type(Float):
    """Custom type ovsdSetPoint based on Float"""
    defaultValue = 5920


_OvsdSetPoint_Type.__name__ = "Float"
_OvsdSetPoint_Object = MibScalar
ovsdSetPoint = _OvsdSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 90),
    _OvsdSetPoint_Type()
)
ovsdSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ovsdSetPoint.setStatus("current")
if mibBuilder.loadTexts:
    ovsdSetPoint.setUnits("0.01 V")


class _RectifierStartUpDelay_Type(TimeIntervalInSeconds):
    """Custom type rectifierStartUpDelay based on TimeIntervalInSeconds"""
    defaultValue = 2


_RectifierStartUpDelay_Type.__name__ = "TimeIntervalInSeconds"
_RectifierStartUpDelay_Object = MibScalar
rectifierStartUpDelay = _RectifierStartUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 110),
    _RectifierStartUpDelay_Type()
)
rectifierStartUpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierStartUpDelay.setStatus("current")
if mibBuilder.loadTexts:
    rectifierStartUpDelay.setUnits("s")


class _EnableRipPowerShare_Type(EnableState):
    """Custom type enableRipPowerShare based on EnableState"""
    defaultValue = 0


_EnableRipPowerShare_Type.__name__ = "EnableState"
_EnableRipPowerShare_Object = MibScalar
enableRipPowerShare = _EnableRipPowerShare_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 60, 120),
    _EnableRipPowerShare_Type()
)
enableRipPowerShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableRipPowerShare.setStatus("current")
_ControlFunctions_ObjectIdentity = ObjectIdentity
controlFunctions = _ControlFunctions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70)
)
if mibBuilder.loadTexts:
    controlFunctions.setStatus("current")
_ControlState_Type = ControlState
_ControlState_Object = MibScalar
controlState = _ControlState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 5),
    _ControlState_Type()
)
controlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlState.setStatus("current")
_VoltageControl_ObjectIdentity = ObjectIdentity
voltageControl = _VoltageControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 10)
)
if mibBuilder.loadTexts:
    voltageControl.setStatus("current")


class _FloatVoltage_Type(Float):
    """Custom type floatVoltage based on Float"""
    defaultValue = 5450


_FloatVoltage_Type.__name__ = "Float"
_FloatVoltage_Object = MibScalar
floatVoltage = _FloatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 10, 10),
    _FloatVoltage_Type()
)
floatVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    floatVoltage.setStatus("current")
if mibBuilder.loadTexts:
    floatVoltage.setUnits("0.01 V")


class _AlternativeFloatVoltage_Type(Float):
    """Custom type alternativeFloatVoltage based on Float"""
    defaultValue = 5520


_AlternativeFloatVoltage_Type.__name__ = "Float"
_AlternativeFloatVoltage_Object = MibScalar
alternativeFloatVoltage = _AlternativeFloatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 10, 11),
    _AlternativeFloatVoltage_Type()
)
alternativeFloatVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alternativeFloatVoltage.setStatus("current")
if mibBuilder.loadTexts:
    alternativeFloatVoltage.setUnits("0.01 V")


class _AlternativeFloatSmartAlarm_Type(Unsigned8):
    """Custom type alternativeFloatSmartAlarm based on Unsigned8"""
    defaultValue = 0


_AlternativeFloatSmartAlarm_Type.__name__ = "Unsigned8"
_AlternativeFloatSmartAlarm_Object = MibScalar
alternativeFloatSmartAlarm = _AlternativeFloatSmartAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 10, 12),
    _AlternativeFloatSmartAlarm_Type()
)
alternativeFloatSmartAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alternativeFloatSmartAlarm.setStatus("current")
_AlternativeFloatStatus_Type = ControlProcessState
_AlternativeFloatStatus_Object = MibScalar
alternativeFloatStatus = _AlternativeFloatStatus_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 10, 13),
    _AlternativeFloatStatus_Type()
)
alternativeFloatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alternativeFloatStatus.setStatus("current")


class _MaximumSystemVoltage_Type(Float):
    """Custom type maximumSystemVoltage based on Float"""
    defaultValue = 5760


_MaximumSystemVoltage_Type.__name__ = "Float"
_MaximumSystemVoltage_Object = MibScalar
maximumSystemVoltage = _MaximumSystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 10, 15),
    _MaximumSystemVoltage_Type()
)
maximumSystemVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maximumSystemVoltage.setStatus("current")
if mibBuilder.loadTexts:
    maximumSystemVoltage.setUnits("0.01 V")


class _MinimumSystemVoltage_Type(Float):
    """Custom type minimumSystemVoltage based on Float"""
    defaultValue = 4260


_MinimumSystemVoltage_Type.__name__ = "Float"
_MinimumSystemVoltage_Object = MibScalar
minimumSystemVoltage = _MinimumSystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 10, 17),
    _MinimumSystemVoltage_Type()
)
minimumSystemVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minimumSystemVoltage.setStatus("current")
if mibBuilder.loadTexts:
    minimumSystemVoltage.setUnits("0.01 V")
_BusVoltage_Type = Float
_BusVoltage_Object = MibScalar
busVoltage = _BusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 10, 20),
    _BusVoltage_Type()
)
busVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busVoltage.setStatus("current")
if mibBuilder.loadTexts:
    busVoltage.setUnits("0.01 V")
_TargetVoltage_Type = Float
_TargetVoltage_Object = MibScalar
targetVoltage = _TargetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 10, 30),
    _TargetVoltage_Type()
)
targetVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetVoltage.setStatus("current")
if mibBuilder.loadTexts:
    targetVoltage.setUnits("0.01 V")


class _EnableActiveVoltageControl_Type(EnableState):
    """Custom type enableActiveVoltageControl based on EnableState"""
    defaultValue = 1


_EnableActiveVoltageControl_Type.__name__ = "EnableState"
_EnableActiveVoltageControl_Object = MibScalar
enableActiveVoltageControl = _EnableActiveVoltageControl_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 10, 35),
    _EnableActiveVoltageControl_Type()
)
enableActiveVoltageControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableActiveVoltageControl.setStatus("current")
_AvcState_Type = AvcState
_AvcState_Object = MibScalar
avcState = _AvcState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 10, 40),
    _AvcState_Type()
)
avcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avcState.setStatus("current")
_AvcOffset_Type = Float
_AvcOffset_Object = MibScalar
avcOffset = _AvcOffset_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 10, 50),
    _AvcOffset_Type()
)
avcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avcOffset.setStatus("current")
if mibBuilder.loadTexts:
    avcOffset.setUnits("0.01 V")
_BaseVoltage_Type = Float
_BaseVoltage_Object = MibScalar
baseVoltage = _BaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 10, 60),
    _BaseVoltage_Type()
)
baseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    baseVoltage.setUnits("0.01 V")
_TemperatureCompensation_ObjectIdentity = ObjectIdentity
temperatureCompensation = _TemperatureCompensation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 20)
)
if mibBuilder.loadTexts:
    temperatureCompensation.setStatus("current")


class _EnableTemperatureCompensation_Type(EnableState):
    """Custom type enableTemperatureCompensation based on EnableState"""
    defaultValue = 1


_EnableTemperatureCompensation_Type.__name__ = "EnableState"
_EnableTemperatureCompensation_Object = MibScalar
enableTemperatureCompensation = _EnableTemperatureCompensation_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 20, 5),
    _EnableTemperatureCompensation_Type()
)
enableTemperatureCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTemperatureCompensation.setStatus("current")
_TemperatureCompensationAllowed_Type = CanStart
_TemperatureCompensationAllowed_Object = MibScalar
temperatureCompensationAllowed = _TemperatureCompensationAllowed_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 20, 7),
    _TemperatureCompensationAllowed_Type()
)
temperatureCompensationAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCompensationAllowed.setStatus("current")
_TemperatureCompensationState_Type = TcState
_TemperatureCompensationState_Object = MibScalar
temperatureCompensationState = _TemperatureCompensationState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 20, 10),
    _TemperatureCompensationState_Type()
)
temperatureCompensationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCompensationState.setStatus("current")


class _TemperatureCompensationSlope_Type(Float):
    """Custom type temperatureCompensationSlope based on Float"""
    defaultValue = -400


_TemperatureCompensationSlope_Type.__name__ = "Float"
_TemperatureCompensationSlope_Object = MibScalar
temperatureCompensationSlope = _TemperatureCompensationSlope_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 20, 20),
    _TemperatureCompensationSlope_Type()
)
temperatureCompensationSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureCompensationSlope.setStatus("current")
if mibBuilder.loadTexts:
    temperatureCompensationSlope.setUnits("0.01 mV/°C/Cell")


class _TemperatureCompensationReferenceTemperature_Type(Float):
    """Custom type temperatureCompensationReferenceTemperature based on Float"""
    defaultValue = 200


_TemperatureCompensationReferenceTemperature_Type.__name__ = "Float"
_TemperatureCompensationReferenceTemperature_Object = MibScalar
temperatureCompensationReferenceTemperature = _TemperatureCompensationReferenceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 20, 30),
    _TemperatureCompensationReferenceTemperature_Type()
)
temperatureCompensationReferenceTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureCompensationReferenceTemperature.setStatus("current")
if mibBuilder.loadTexts:
    temperatureCompensationReferenceTemperature.setUnits("0.1 °C")


class _TemperatureCompensationUpperLimit_Type(Float):
    """Custom type temperatureCompensationUpperLimit based on Float"""
    defaultValue = 500


_TemperatureCompensationUpperLimit_Type.__name__ = "Float"
_TemperatureCompensationUpperLimit_Object = MibScalar
temperatureCompensationUpperLimit = _TemperatureCompensationUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 20, 40),
    _TemperatureCompensationUpperLimit_Type()
)
temperatureCompensationUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureCompensationUpperLimit.setStatus("current")
if mibBuilder.loadTexts:
    temperatureCompensationUpperLimit.setUnits("0.1 °C")


class _TemperatureCompensationLowerLimit_Type(Float):
    """Custom type temperatureCompensationLowerLimit based on Float"""
    defaultValue = 0


_TemperatureCompensationLowerLimit_Type.__name__ = "Float"
_TemperatureCompensationLowerLimit_Object = MibScalar
temperatureCompensationLowerLimit = _TemperatureCompensationLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 20, 50),
    _TemperatureCompensationLowerLimit_Type()
)
temperatureCompensationLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureCompensationLowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    temperatureCompensationLowerLimit.setUnits("0.1 °C")
_TemperatureCompensationOffsetVoltage_Type = Float
_TemperatureCompensationOffsetVoltage_Object = MibScalar
temperatureCompensationOffsetVoltage = _TemperatureCompensationOffsetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 20, 60),
    _TemperatureCompensationOffsetVoltage_Type()
)
temperatureCompensationOffsetVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureCompensationOffsetVoltage.setStatus("current")
if mibBuilder.loadTexts:
    temperatureCompensationOffsetVoltage.setUnits("0.01 V")
_ResetAhDischarged_Type = NoData
_ResetAhDischarged_Object = MibScalar
resetAhDischarged = _ResetAhDischarged_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 25),
    _ResetAhDischarged_Type()
)
resetAhDischarged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetAhDischarged.setStatus("current")


class _AhDischargedFloatResetRate_Type(Float):
    """Custom type ahDischargedFloatResetRate based on Float"""
    defaultValue = 5


_AhDischargedFloatResetRate_Type.__name__ = "Float"
_AhDischargedFloatResetRate_Object = MibScalar
ahDischargedFloatResetRate = _AhDischargedFloatResetRate_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 27),
    _AhDischargedFloatResetRate_Type()
)
ahDischargedFloatResetRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahDischargedFloatResetRate.setStatus("current")
if mibBuilder.loadTexts:
    ahDischargedFloatResetRate.setUnits("0.1")
_Equalize_ObjectIdentity = ObjectIdentity
equalize = _Equalize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 30)
)
if mibBuilder.loadTexts:
    equalize.setStatus("current")


class _EnableEqualize_Type(EnableState):
    """Custom type enableEqualize based on EnableState"""
    defaultValue = 0


_EnableEqualize_Type.__name__ = "EnableState"
_EnableEqualize_Object = MibScalar
enableEqualize = _EnableEqualize_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 30, 5),
    _EnableEqualize_Type()
)
enableEqualize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableEqualize.setStatus("current")
_EqualizeStartAllowed_Type = CanStart
_EqualizeStartAllowed_Object = MibScalar
equalizeStartAllowed = _EqualizeStartAllowed_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 30, 9),
    _EqualizeStartAllowed_Type()
)
equalizeStartAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equalizeStartAllowed.setStatus("current")
_EqualizeState_Type = ControlProcessState
_EqualizeState_Object = MibScalar
equalizeState = _EqualizeState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 30, 10),
    _EqualizeState_Type()
)
equalizeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equalizeState.setStatus("current")


class _EqualizeVoltage_Type(Float):
    """Custom type equalizeVoltage based on Float"""
    defaultValue = 5600


_EqualizeVoltage_Type.__name__ = "Float"
_EqualizeVoltage_Object = MibScalar
equalizeVoltage = _EqualizeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 30, 12),
    _EqualizeVoltage_Type()
)
equalizeVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equalizeVoltage.setStatus("current")
if mibBuilder.loadTexts:
    equalizeVoltage.setUnits("0.01 V")
_EqualizeOffsetVoltage_Type = Float
_EqualizeOffsetVoltage_Object = MibScalar
equalizeOffsetVoltage = _EqualizeOffsetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 30, 13),
    _EqualizeOffsetVoltage_Type()
)
equalizeOffsetVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equalizeOffsetVoltage.setStatus("current")
if mibBuilder.loadTexts:
    equalizeOffsetVoltage.setUnits("0.01 V")
_PeriodicEqualizeFirstDateTime_Type = JulianDateUtc25
_PeriodicEqualizeFirstDateTime_Object = MibScalar
periodicEqualizeFirstDateTime = _PeriodicEqualizeFirstDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 30, 15),
    _PeriodicEqualizeFirstDateTime_Type()
)
periodicEqualizeFirstDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    periodicEqualizeFirstDateTime.setStatus("current")


class _EqualizeInterval_Type(TimeIntervalInDays):
    """Custom type equalizeInterval based on TimeIntervalInDays"""
    defaultValue = 182


_EqualizeInterval_Type.__name__ = "TimeIntervalInDays"
_EqualizeInterval_Object = MibScalar
equalizeInterval = _EqualizeInterval_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 30, 17),
    _EqualizeInterval_Type()
)
equalizeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equalizeInterval.setStatus("current")
if mibBuilder.loadTexts:
    equalizeInterval.setUnits("d")
_NextEqualizeStartTime_Type = JulianDateUtc25
_NextEqualizeStartTime_Object = MibScalar
nextEqualizeStartTime = _NextEqualizeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 30, 20),
    _NextEqualizeStartTime_Type()
)
nextEqualizeStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextEqualizeStartTime.setStatus("current")


class _EqualizeDuration_Type(TimeIntervalInMinutes):
    """Custom type equalizeDuration based on TimeIntervalInMinutes"""
    defaultValue = 600


_EqualizeDuration_Type.__name__ = "TimeIntervalInMinutes"
_EqualizeDuration_Object = MibScalar
equalizeDuration = _EqualizeDuration_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 30, 30),
    _EqualizeDuration_Type()
)
equalizeDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equalizeDuration.setStatus("current")
if mibBuilder.loadTexts:
    equalizeDuration.setUnits("min")
_EqualizeRemainingTime_Type = TimeIntervalInSeconds
_EqualizeRemainingTime_Object = MibScalar
equalizeRemainingTime = _EqualizeRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 30, 40),
    _EqualizeRemainingTime_Type()
)
equalizeRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equalizeRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    equalizeRemainingTime.setUnits("s")
_StartEqualize_Type = NoData
_StartEqualize_Object = MibScalar
startEqualize = _StartEqualize_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 30, 100),
    _StartEqualize_Type()
)
startEqualize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startEqualize.setStatus("current")
_StopEqualize_Type = NoData
_StopEqualize_Object = MibScalar
stopEqualize = _StopEqualize_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 30, 110),
    _StopEqualize_Type()
)
stopEqualize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stopEqualize.setStatus("current")


class _EqualizeSmartAlarm_Type(Unsigned8):
    """Custom type equalizeSmartAlarm based on Unsigned8"""
    defaultValue = 0


_EqualizeSmartAlarm_Type.__name__ = "Unsigned8"
_EqualizeSmartAlarm_Object = MibScalar
equalizeSmartAlarm = _EqualizeSmartAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 30, 120),
    _EqualizeSmartAlarm_Type()
)
equalizeSmartAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    equalizeSmartAlarm.setStatus("current")
_FastCharge_ObjectIdentity = ObjectIdentity
fastCharge = _FastCharge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 40)
)
if mibBuilder.loadTexts:
    fastCharge.setStatus("current")


class _EnableFastCharge_Type(EnableState):
    """Custom type enableFastCharge based on EnableState"""
    defaultValue = 0


_EnableFastCharge_Type.__name__ = "EnableState"
_EnableFastCharge_Object = MibScalar
enableFastCharge = _EnableFastCharge_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 40, 5),
    _EnableFastCharge_Type()
)
enableFastCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableFastCharge.setStatus("current")
_FastChargeState_Type = ControlProcessState
_FastChargeState_Object = MibScalar
fastChargeState = _FastChargeState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 40, 10),
    _FastChargeState_Type()
)
fastChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fastChargeState.setStatus("current")
_FastChargeStartAllowed_Type = CanStart
_FastChargeStartAllowed_Object = MibScalar
fastChargeStartAllowed = _FastChargeStartAllowed_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 40, 12),
    _FastChargeStartAllowed_Type()
)
fastChargeStartAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fastChargeStartAllowed.setStatus("current")


class _FastChargeVoltage_Type(Float):
    """Custom type fastChargeVoltage based on Float"""
    defaultValue = 5600


_FastChargeVoltage_Type.__name__ = "Float"
_FastChargeVoltage_Object = MibScalar
fastChargeVoltage = _FastChargeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 40, 15),
    _FastChargeVoltage_Type()
)
fastChargeVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastChargeVoltage.setStatus("current")
if mibBuilder.loadTexts:
    fastChargeVoltage.setUnits("0.01 V")
_FastChargeOffsetVoltage_Type = Float
_FastChargeOffsetVoltage_Object = MibScalar
fastChargeOffsetVoltage = _FastChargeOffsetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 40, 17),
    _FastChargeOffsetVoltage_Type()
)
fastChargeOffsetVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fastChargeOffsetVoltage.setStatus("current")
if mibBuilder.loadTexts:
    fastChargeOffsetVoltage.setUnits("0.01 V")
_FastChargeAhDischarged_Type = Float
_FastChargeAhDischarged_Object = MibScalar
fastChargeAhDischarged = _FastChargeAhDischarged_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 40, 20),
    _FastChargeAhDischarged_Type()
)
fastChargeAhDischarged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fastChargeAhDischarged.setStatus("current")
if mibBuilder.loadTexts:
    fastChargeAhDischarged.setUnits("Ah")


class _FastChargeMaximumDuration_Type(TimeIntervalInMinutes):
    """Custom type fastChargeMaximumDuration based on TimeIntervalInMinutes"""
    defaultValue = 1440


_FastChargeMaximumDuration_Type.__name__ = "TimeIntervalInMinutes"
_FastChargeMaximumDuration_Object = MibScalar
fastChargeMaximumDuration = _FastChargeMaximumDuration_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 40, 30),
    _FastChargeMaximumDuration_Type()
)
fastChargeMaximumDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastChargeMaximumDuration.setStatus("current")
if mibBuilder.loadTexts:
    fastChargeMaximumDuration.setUnits("min")


class _FastChargeAmpereHourThreshold_Type(Unsigned8):
    """Custom type fastChargeAmpereHourThreshold based on Unsigned8"""
    defaultValue = 25


_FastChargeAmpereHourThreshold_Type.__name__ = "Unsigned8"
_FastChargeAmpereHourThreshold_Object = MibScalar
fastChargeAmpereHourThreshold = _FastChargeAmpereHourThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 40, 35),
    _FastChargeAmpereHourThreshold_Type()
)
fastChargeAmpereHourThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastChargeAmpereHourThreshold.setStatus("current")
if mibBuilder.loadTexts:
    fastChargeAmpereHourThreshold.setUnits("%")


class _FastChargeVoltageThreshold_Type(Float):
    """Custom type fastChargeVoltageThreshold based on Float"""
    defaultValue = 4800


_FastChargeVoltageThreshold_Type.__name__ = "Float"
_FastChargeVoltageThreshold_Object = MibScalar
fastChargeVoltageThreshold = _FastChargeVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 40, 40),
    _FastChargeVoltageThreshold_Type()
)
fastChargeVoltageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastChargeVoltageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    fastChargeVoltageThreshold.setUnits("0.01 V")


class _FastChargeRechargePercentage_Type(Unsigned8):
    """Custom type fastChargeRechargePercentage based on Unsigned8"""
    defaultValue = 110


_FastChargeRechargePercentage_Type.__name__ = "Unsigned8"
_FastChargeRechargePercentage_Object = MibScalar
fastChargeRechargePercentage = _FastChargeRechargePercentage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 40, 45),
    _FastChargeRechargePercentage_Type()
)
fastChargeRechargePercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastChargeRechargePercentage.setStatus("current")
if mibBuilder.loadTexts:
    fastChargeRechargePercentage.setUnits("%")


class _FastChargeAmpereHourStopThreshold_Type(Unsigned8):
    """Custom type fastChargeAmpereHourStopThreshold based on Unsigned8"""
    defaultValue = 0


_FastChargeAmpereHourStopThreshold_Type.__name__ = "Unsigned8"
_FastChargeAmpereHourStopThreshold_Object = MibScalar
fastChargeAmpereHourStopThreshold = _FastChargeAmpereHourStopThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 40, 47),
    _FastChargeAmpereHourStopThreshold_Type()
)
fastChargeAmpereHourStopThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastChargeAmpereHourStopThreshold.setStatus("current")
if mibBuilder.loadTexts:
    fastChargeAmpereHourStopThreshold.setUnits("%")
_FastChargeMaximumTimeRemaining_Type = TimeIntervalInSeconds
_FastChargeMaximumTimeRemaining_Object = MibScalar
fastChargeMaximumTimeRemaining = _FastChargeMaximumTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 40, 50),
    _FastChargeMaximumTimeRemaining_Type()
)
fastChargeMaximumTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fastChargeMaximumTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    fastChargeMaximumTimeRemaining.setUnits("s")
_StopFastCharge_Type = NoData
_StopFastCharge_Object = MibScalar
stopFastCharge = _StopFastCharge_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 40, 100),
    _StopFastCharge_Type()
)
stopFastCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stopFastCharge.setStatus("current")
_BatteryCurrentLimit_ObjectIdentity = ObjectIdentity
batteryCurrentLimit = _BatteryCurrentLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 50)
)
if mibBuilder.loadTexts:
    batteryCurrentLimit.setStatus("current")


class _EnableBatteryCurrentLimit_Type(EnableState):
    """Custom type enableBatteryCurrentLimit based on EnableState"""
    defaultValue = 1


_EnableBatteryCurrentLimit_Type.__name__ = "EnableState"
_EnableBatteryCurrentLimit_Object = MibScalar
enableBatteryCurrentLimit = _EnableBatteryCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 50, 5),
    _EnableBatteryCurrentLimit_Type()
)
enableBatteryCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableBatteryCurrentLimit.setStatus("current")
_BclState_Type = BclState
_BclState_Object = MibScalar
bclState = _BclState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 50, 10),
    _BclState_Type()
)
bclState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bclState.setStatus("current")


class _BclLimit_Type(Unsigned8):
    """Custom type bclLimit based on Unsigned8"""
    defaultValue = 10


_BclLimit_Type.__name__ = "Unsigned8"
_BclLimit_Object = MibScalar
bclLimit = _BclLimit_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 50, 30),
    _BclLimit_Type()
)
bclLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bclLimit.setStatus("current")
if mibBuilder.loadTexts:
    bclLimit.setUnits("%")
_BclOffsetVoltage_Type = Float
_BclOffsetVoltage_Object = MibScalar
bclOffsetVoltage = _BclOffsetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 50, 40),
    _BclOffsetVoltage_Type()
)
bclOffsetVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bclOffsetVoltage.setStatus("current")
if mibBuilder.loadTexts:
    bclOffsetVoltage.setUnits("0.01 V")


class _BclEngineRunLimit_Type(Unsigned8):
    """Custom type bclEngineRunLimit based on Unsigned8"""
    defaultValue = 2


_BclEngineRunLimit_Type.__name__ = "Unsigned8"
_BclEngineRunLimit_Object = MibScalar
bclEngineRunLimit = _BclEngineRunLimit_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 50, 50),
    _BclEngineRunLimit_Type()
)
bclEngineRunLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bclEngineRunLimit.setStatus("current")
if mibBuilder.loadTexts:
    bclEngineRunLimit.setUnits("%")
_BatteryTest_ObjectIdentity = ObjectIdentity
batteryTest = _BatteryTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70)
)
if mibBuilder.loadTexts:
    batteryTest.setStatus("current")


class _EnableBatteryTest_Type(EnableState):
    """Custom type enableBatteryTest based on EnableState"""
    defaultValue = 0


_EnableBatteryTest_Type.__name__ = "EnableState"
_EnableBatteryTest_Object = MibScalar
enableBatteryTest = _EnableBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 3),
    _EnableBatteryTest_Type()
)
enableBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableBatteryTest.setStatus("current")


class _PreventBatteryTest_Type(PreventBatteryTest):
    """Custom type preventBatteryTest based on PreventBatteryTest"""
    defaultValue = 1


_PreventBatteryTest_Type.__name__ = "PreventBatteryTest"
_PreventBatteryTest_Object = MibScalar
preventBatteryTest = _PreventBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 4),
    _PreventBatteryTest_Type()
)
preventBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preventBatteryTest.setStatus("current")
_BatteryTestStartAllowed_Type = CanStart
_BatteryTestStartAllowed_Object = MibScalar
batteryTestStartAllowed = _BatteryTestStartAllowed_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 7),
    _BatteryTestStartAllowed_Type()
)
batteryTestStartAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestStartAllowed.setStatus("current")
_BatteryTestLockoutRemaining_Type = TimeIntervalInSeconds
_BatteryTestLockoutRemaining_Object = MibScalar
batteryTestLockoutRemaining = _BatteryTestLockoutRemaining_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 8),
    _BatteryTestLockoutRemaining_Type()
)
batteryTestLockoutRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestLockoutRemaining.setStatus("current")
if mibBuilder.loadTexts:
    batteryTestLockoutRemaining.setUnits("s")
_BatteryTestState_Type = BatteryTestState
_BatteryTestState_Object = MibScalar
batteryTestState = _BatteryTestState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 10),
    _BatteryTestState_Type()
)
batteryTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestState.setStatus("current")
_BatteryTestFirstDateTime_Type = JulianDateUtc25
_BatteryTestFirstDateTime_Object = MibScalar
batteryTestFirstDateTime = _BatteryTestFirstDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 15),
    _BatteryTestFirstDateTime_Type()
)
batteryTestFirstDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTestFirstDateTime.setStatus("current")


class _BatteryTestInterval_Type(TimeIntervalInDays):
    """Custom type batteryTestInterval based on TimeIntervalInDays"""
    defaultValue = 183


_BatteryTestInterval_Type.__name__ = "TimeIntervalInDays"
_BatteryTestInterval_Object = MibScalar
batteryTestInterval = _BatteryTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 17),
    _BatteryTestInterval_Type()
)
batteryTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTestInterval.setStatus("current")
if mibBuilder.loadTexts:
    batteryTestInterval.setUnits("d")
_NextBatteryTestStartTime_Type = JulianDateUtc25
_NextBatteryTestStartTime_Object = MibScalar
nextBatteryTestStartTime = _NextBatteryTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 20),
    _NextBatteryTestStartTime_Type()
)
nextBatteryTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextBatteryTestStartTime.setStatus("current")


class _BatteryTestDuration_Type(TimeIntervalInMinutes):
    """Custom type batteryTestDuration based on TimeIntervalInMinutes"""
    defaultValue = 30


_BatteryTestDuration_Type.__name__ = "TimeIntervalInMinutes"
_BatteryTestDuration_Object = MibScalar
batteryTestDuration = _BatteryTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 30),
    _BatteryTestDuration_Type()
)
batteryTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    batteryTestDuration.setUnits("min")
_BatteryTestRemainingTime_Type = TimeIntervalInSeconds
_BatteryTestRemainingTime_Object = MibScalar
batteryTestRemainingTime = _BatteryTestRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 40),
    _BatteryTestRemainingTime_Type()
)
batteryTestRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    batteryTestRemainingTime.setUnits("s")


class _BatteryTestTerminationVoltage_Type(Float):
    """Custom type batteryTestTerminationVoltage based on Float"""
    defaultValue = 4750


_BatteryTestTerminationVoltage_Type.__name__ = "Float"
_BatteryTestTerminationVoltage_Object = MibScalar
batteryTestTerminationVoltage = _BatteryTestTerminationVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 50),
    _BatteryTestTerminationVoltage_Type()
)
batteryTestTerminationVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTestTerminationVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryTestTerminationVoltage.setUnits("0.01 V")
_BatteryTestOffsetVoltage_Type = Float
_BatteryTestOffsetVoltage_Object = MibScalar
batteryTestOffsetVoltage = _BatteryTestOffsetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 60),
    _BatteryTestOffsetVoltage_Type()
)
batteryTestOffsetVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestOffsetVoltage.setStatus("current")
if mibBuilder.loadTexts:
    batteryTestOffsetVoltage.setUnits("0.01 V")
_StartBatteryTest_Type = NoData
_StartBatteryTest_Object = MibScalar
startBatteryTest = _StartBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 100),
    _StartBatteryTest_Type()
)
startBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startBatteryTest.setStatus("current")
_StopBatteryTest_Type = NoData
_StopBatteryTest_Object = MibScalar
stopBatteryTest = _StopBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 110),
    _StopBatteryTest_Type()
)
stopBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stopBatteryTest.setStatus("current")
_AllowBatteryTestDuringLockout_Type = NoData
_AllowBatteryTestDuringLockout_Object = MibScalar
allowBatteryTestDuringLockout = _AllowBatteryTestDuringLockout_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 130),
    _AllowBatteryTestDuringLockout_Type()
)
allowBatteryTestDuringLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowBatteryTestDuringLockout.setStatus("current")
_BBatteryTestOffsetVoltage_Type = Float
_BBatteryTestOffsetVoltage_Object = MibScalar
bBatteryTestOffsetVoltage = _BBatteryTestOffsetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 70, 140),
    _BBatteryTestOffsetVoltage_Type()
)
bBatteryTestOffsetVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bBatteryTestOffsetVoltage.setStatus("current")
if mibBuilder.loadTexts:
    bBatteryTestOffsetVoltage.setUnits("0.01 V")
_Lvd_ObjectIdentity = ObjectIdentity
lvd = _Lvd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75)
)
if mibBuilder.loadTexts:
    lvd.setStatus("current")


class _LvdInhibitPeriod_Type(TimeIntervalInSeconds):
    """Custom type lvdInhibitPeriod based on TimeIntervalInSeconds"""
    defaultValue = 10


_LvdInhibitPeriod_Type.__name__ = "TimeIntervalInSeconds"
_LvdInhibitPeriod_Object = MibScalar
lvdInhibitPeriod = _LvdInhibitPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 10),
    _LvdInhibitPeriod_Type()
)
lvdInhibitPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvdInhibitPeriod.setStatus("current")
if mibBuilder.loadTexts:
    lvdInhibitPeriod.setUnits("s")


class _AllowFrontPanelLvdControl_Type(Boolean):
    """Custom type allowFrontPanelLvdControl based on Boolean"""
    defaultValue = 1


_AllowFrontPanelLvdControl_Type.__name__ = "Boolean"
_AllowFrontPanelLvdControl_Object = MibScalar
allowFrontPanelLvdControl = _AllowFrontPanelLvdControl_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 20),
    _AllowFrontPanelLvdControl_Type()
)
allowFrontPanelLvdControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowFrontPanelLvdControl.setStatus("current")
_LvdTable_Object = MibTable
lvdTable = _LvdTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50)
)
if mibBuilder.loadTexts:
    lvdTable.setStatus("current")
_LvdEntry_Object = MibTableRow
lvdEntry = _LvdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1)
)
lvdEntry.setIndexNames(
    (0, "RpsSc300Mib", "lvdIndex"),
)
if mibBuilder.loadTexts:
    lvdEntry.setStatus("current")


class _LvdIndex_Type(Unsigned8):
    """Custom type lvdIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LvdIndex_Type.__name__ = "Unsigned8"
_LvdIndex_Object = MibTableColumn
lvdIndex = _LvdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1, 1),
    _LvdIndex_Type()
)
lvdIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lvdIndex.setStatus("current")


class _LvdName_Type(DisplayString):
    """Custom type lvdName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LvdName_Type.__name__ = "DisplayString"
_LvdName_Object = MibTableColumn
lvdName = _LvdName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1, 5),
    _LvdName_Type()
)
lvdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvdName.setStatus("current")
_LvdState_Type = LvdState
_LvdState_Object = MibTableColumn
lvdState = _LvdState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1, 10),
    _LvdState_Type()
)
lvdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lvdState.setStatus("current")
_LvdInhibited_Type = Boolean
_LvdInhibited_Object = MibTableColumn
lvdInhibited = _LvdInhibited_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1, 15),
    _LvdInhibited_Type()
)
lvdInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lvdInhibited.setStatus("current")


class _EnableLvdVoltageDisconnect_Type(EnableState):
    """Custom type enableLvdVoltageDisconnect based on EnableState"""
    defaultValue = 1


_EnableLvdVoltageDisconnect_Type.__name__ = "EnableState"
_EnableLvdVoltageDisconnect_Object = MibTableColumn
enableLvdVoltageDisconnect = _EnableLvdVoltageDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1, 20),
    _EnableLvdVoltageDisconnect_Type()
)
enableLvdVoltageDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableLvdVoltageDisconnect.setStatus("current")


class _LvdDisconnectVoltage_Type(Float):
    """Custom type lvdDisconnectVoltage based on Float"""
    defaultValue = 4320


_LvdDisconnectVoltage_Type.__name__ = "Float"
_LvdDisconnectVoltage_Object = MibTableColumn
lvdDisconnectVoltage = _LvdDisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1, 30),
    _LvdDisconnectVoltage_Type()
)
lvdDisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvdDisconnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    lvdDisconnectVoltage.setUnits("0.01 V")


class _LvdReconnectVoltage_Type(Float):
    """Custom type lvdReconnectVoltage based on Float"""
    defaultValue = 4800


_LvdReconnectVoltage_Type.__name__ = "Float"
_LvdReconnectVoltage_Object = MibTableColumn
lvdReconnectVoltage = _LvdReconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1, 40),
    _LvdReconnectVoltage_Type()
)
lvdReconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvdReconnectVoltage.setStatus("current")
if mibBuilder.loadTexts:
    lvdReconnectVoltage.setUnits("0.01 V")


class _LvdRecognitionPeriod_Type(TimeIntervalInSeconds):
    """Custom type lvdRecognitionPeriod based on TimeIntervalInSeconds"""
    defaultValue = 10


_LvdRecognitionPeriod_Type.__name__ = "TimeIntervalInSeconds"
_LvdRecognitionPeriod_Object = MibTableColumn
lvdRecognitionPeriod = _LvdRecognitionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1, 50),
    _LvdRecognitionPeriod_Type()
)
lvdRecognitionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvdRecognitionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    lvdRecognitionPeriod.setUnits("s")


class _EnableLvdAcTimer_Type(EnableState):
    """Custom type enableLvdAcTimer based on EnableState"""
    defaultValue = 0


_EnableLvdAcTimer_Type.__name__ = "EnableState"
_EnableLvdAcTimer_Object = MibTableColumn
enableLvdAcTimer = _EnableLvdAcTimer_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1, 60),
    _EnableLvdAcTimer_Type()
)
enableLvdAcTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableLvdAcTimer.setStatus("current")


class _LvdAcTimerDisconnectDelay_Type(TimeIntervalInMinutes):
    """Custom type lvdAcTimerDisconnectDelay based on TimeIntervalInMinutes"""
    defaultValue = 240


_LvdAcTimerDisconnectDelay_Type.__name__ = "TimeIntervalInMinutes"
_LvdAcTimerDisconnectDelay_Object = MibTableColumn
lvdAcTimerDisconnectDelay = _LvdAcTimerDisconnectDelay_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1, 70),
    _LvdAcTimerDisconnectDelay_Type()
)
lvdAcTimerDisconnectDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvdAcTimerDisconnectDelay.setStatus("current")
if mibBuilder.loadTexts:
    lvdAcTimerDisconnectDelay.setUnits("min")


class _EnableLvdSaDisconnect_Type(EnableState):
    """Custom type enableLvdSaDisconnect based on EnableState"""
    defaultValue = 0


_EnableLvdSaDisconnect_Type.__name__ = "EnableState"
_EnableLvdSaDisconnect_Object = MibTableColumn
enableLvdSaDisconnect = _EnableLvdSaDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1, 80),
    _EnableLvdSaDisconnect_Type()
)
enableLvdSaDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableLvdSaDisconnect.setStatus("current")


class _LvdSaDisconnectIndex_Type(Unsigned8):
    """Custom type lvdSaDisconnectIndex based on Unsigned8"""
    defaultValue = 1


_LvdSaDisconnectIndex_Type.__name__ = "Unsigned8"
_LvdSaDisconnectIndex_Object = MibTableColumn
lvdSaDisconnectIndex = _LvdSaDisconnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1, 90),
    _LvdSaDisconnectIndex_Type()
)
lvdSaDisconnectIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvdSaDisconnectIndex.setStatus("current")


class _EnableLvdChainedToPrevious_Type(EnableState):
    """Custom type enableLvdChainedToPrevious based on EnableState"""
    defaultValue = 0


_EnableLvdChainedToPrevious_Type.__name__ = "EnableState"
_EnableLvdChainedToPrevious_Object = MibTableColumn
enableLvdChainedToPrevious = _EnableLvdChainedToPrevious_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1, 100),
    _EnableLvdChainedToPrevious_Type()
)
enableLvdChainedToPrevious.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableLvdChainedToPrevious.setStatus("current")
_LvdRemoteManualControl_Type = Boolean
_LvdRemoteManualControl_Object = MibTableColumn
lvdRemoteManualControl = _LvdRemoteManualControl_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 50, 1, 120),
    _LvdRemoteManualControl_Type()
)
lvdRemoteManualControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvdRemoteManualControl.setStatus("current")
_LvdcTable_Object = MibTable
lvdcTable = _LvdcTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 60)
)
if mibBuilder.loadTexts:
    lvdcTable.setStatus("current")
_LvdcEntry_Object = MibTableRow
lvdcEntry = _LvdcEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 60, 1)
)
lvdcEntry.setIndexNames(
    (0, "RpsSc300Mib", "lvdcIndex"),
)
if mibBuilder.loadTexts:
    lvdcEntry.setStatus("current")


class _LvdcIndex_Type(Unsigned8):
    """Custom type lvdcIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LvdcIndex_Type.__name__ = "Unsigned8"
_LvdcIndex_Object = MibTableColumn
lvdcIndex = _LvdcIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 60, 1, 1),
    _LvdcIndex_Type()
)
lvdcIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lvdcIndex.setStatus("current")


class _LvdcLvdMapping_Type(Unsigned8):
    """Custom type lvdcLvdMapping based on Unsigned8"""
    defaultValue = 16


_LvdcLvdMapping_Type.__name__ = "Unsigned8"
_LvdcLvdMapping_Object = MibTableColumn
lvdcLvdMapping = _LvdcLvdMapping_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 60, 1, 10),
    _LvdcLvdMapping_Type()
)
lvdcLvdMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvdcLvdMapping.setStatus("current")
_LvdcState_Type = LvdcState
_LvdcState_Object = MibTableColumn
lvdcState = _LvdcState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 60, 1, 20),
    _LvdcState_Type()
)
lvdcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lvdcState.setStatus("current")


class _EnableLvdc_Type(EnableState):
    """Custom type enableLvdc based on EnableState"""
    defaultValue = 0


_EnableLvdc_Type.__name__ = "EnableState"
_EnableLvdc_Object = MibTableColumn
enableLvdc = _EnableLvdc_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 60, 1, 30),
    _EnableLvdc_Type()
)
enableLvdc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableLvdc.setStatus("current")


class _LvdcIobNumber_Type(Unsigned8):
    """Custom type lvdcIobNumber based on Unsigned8"""
    defaultValue = 1


_LvdcIobNumber_Type.__name__ = "Unsigned8"
_LvdcIobNumber_Object = MibTableColumn
lvdcIobNumber = _LvdcIobNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 60, 1, 40),
    _LvdcIobNumber_Type()
)
lvdcIobNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvdcIobNumber.setStatus("current")


class _LvdcIobLvdNumber_Type(Unsigned8):
    """Custom type lvdcIobLvdNumber based on Unsigned8"""
    defaultValue = 1


_LvdcIobLvdNumber_Type.__name__ = "Unsigned8"
_LvdcIobLvdNumber_Object = MibTableColumn
lvdcIobLvdNumber = _LvdcIobLvdNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 60, 1, 50),
    _LvdcIobLvdNumber_Type()
)
lvdcIobLvdNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvdcIobLvdNumber.setStatus("current")


class _LvdcType_Type(LvdcType):
    """Custom type lvdcType based on LvdcType"""
    defaultValue = 0


_LvdcType_Type.__name__ = "LvdcType"
_LvdcType_Object = MibTableColumn
lvdcType = _LvdcType_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 60, 1, 60),
    _LvdcType_Type()
)
lvdcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvdcType.setStatus("current")


class _LvdRemoteManualReconnectTimeoutPeriod_Type(TimeIntervalInMinutes):
    """Custom type lvdRemoteManualReconnectTimeoutPeriod based on TimeIntervalInMinutes"""
    defaultValue = 60


_LvdRemoteManualReconnectTimeoutPeriod_Type.__name__ = "TimeIntervalInMinutes"
_LvdRemoteManualReconnectTimeoutPeriod_Object = MibScalar
lvdRemoteManualReconnectTimeoutPeriod = _LvdRemoteManualReconnectTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 70),
    _LvdRemoteManualReconnectTimeoutPeriod_Type()
)
lvdRemoteManualReconnectTimeoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvdRemoteManualReconnectTimeoutPeriod.setStatus("current")
if mibBuilder.loadTexts:
    lvdRemoteManualReconnectTimeoutPeriod.setUnits("min")
_LvdRemoteManualReconnectTimer_Type = TimeIntervalInMinutes
_LvdRemoteManualReconnectTimer_Object = MibScalar
lvdRemoteManualReconnectTimer = _LvdRemoteManualReconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 75, 80),
    _LvdRemoteManualReconnectTimer_Type()
)
lvdRemoteManualReconnectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lvdRemoteManualReconnectTimer.setStatus("current")
if mibBuilder.loadTexts:
    lvdRemoteManualReconnectTimer.setUnits("min")
_GeneratorControl_ObjectIdentity = ObjectIdentity
generatorControl = _GeneratorControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80)
)
if mibBuilder.loadTexts:
    generatorControl.setStatus("current")
_GeneratorCurrent_Type = Float
_GeneratorCurrent_Object = MibScalar
generatorCurrent = _GeneratorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 91),
    _GeneratorCurrent_Type()
)
generatorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorCurrent.setStatus("current")
if mibBuilder.loadTexts:
    generatorCurrent.setUnits("0.01 kW")


class _GeneratorFailAlarmRecognitionPeriod_Type(TimeIntervalInSeconds):
    """Custom type generatorFailAlarmRecognitionPeriod based on TimeIntervalInSeconds"""
    defaultValue = 300


_GeneratorFailAlarmRecognitionPeriod_Type.__name__ = "TimeIntervalInSeconds"
_GeneratorFailAlarmRecognitionPeriod_Object = MibScalar
generatorFailAlarmRecognitionPeriod = _GeneratorFailAlarmRecognitionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 100),
    _GeneratorFailAlarmRecognitionPeriod_Type()
)
generatorFailAlarmRecognitionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorFailAlarmRecognitionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    generatorFailAlarmRecognitionPeriod.setUnits("s")


class _GeneratorOnFastCharge_Type(YesNo):
    """Custom type generatorOnFastCharge based on YesNo"""
    defaultValue = 1


_GeneratorOnFastCharge_Type.__name__ = "YesNo"
_GeneratorOnFastCharge_Object = MibScalar
generatorOnFastCharge = _GeneratorOnFastCharge_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 111),
    _GeneratorOnFastCharge_Type()
)
generatorOnFastCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorOnFastCharge.setStatus("current")


class _GeneratorOnEqualize_Type(YesNo):
    """Custom type generatorOnEqualize based on YesNo"""
    defaultValue = 0


_GeneratorOnEqualize_Type.__name__ = "YesNo"
_GeneratorOnEqualize_Object = MibScalar
generatorOnEqualize = _GeneratorOnEqualize_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 112),
    _GeneratorOnEqualize_Type()
)
generatorOnEqualize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorOnEqualize.setStatus("current")


class _GeneratorOnAcPeakLoadReduction_Type(YesNo):
    """Custom type generatorOnAcPeakLoadReduction based on YesNo"""
    defaultValue = 0


_GeneratorOnAcPeakLoadReduction_Type.__name__ = "YesNo"
_GeneratorOnAcPeakLoadReduction_Object = MibScalar
generatorOnAcPeakLoadReduction = _GeneratorOnAcPeakLoadReduction_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 114),
    _GeneratorOnAcPeakLoadReduction_Type()
)
generatorOnAcPeakLoadReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorOnAcPeakLoadReduction.setStatus("current")


class _GeneratorOnMainsFailure_Type(YesNo):
    """Custom type generatorOnMainsFailure based on YesNo"""
    defaultValue = 0


_GeneratorOnMainsFailure_Type.__name__ = "YesNo"
_GeneratorOnMainsFailure_Object = MibScalar
generatorOnMainsFailure = _GeneratorOnMainsFailure_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 116),
    _GeneratorOnMainsFailure_Type()
)
generatorOnMainsFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorOnMainsFailure.setStatus("current")
_AcSupplyState_Type = SystemState
_AcSupplyState_Object = MibScalar
acSupplyState = _AcSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 120),
    _AcSupplyState_Type()
)
acSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSupplyState.setStatus("current")
_GeneratorRunTimeRemaining_Type = TimeIntervalInSeconds
_GeneratorRunTimeRemaining_Object = MibScalar
generatorRunTimeRemaining = _GeneratorRunTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 130),
    _GeneratorRunTimeRemaining_Type()
)
generatorRunTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    generatorRunTimeRemaining.setUnits("s")
_GeneratorState_Type = EngineRunState
_GeneratorState_Object = MibScalar
generatorState = _GeneratorState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 140),
    _GeneratorState_Type()
)
generatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorState.setStatus("current")
_GeneratorRefuelDate_Type = JulianDateUtc25
_GeneratorRefuelDate_Object = MibScalar
generatorRefuelDate = _GeneratorRefuelDate_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 150),
    _GeneratorRefuelDate_Type()
)
generatorRefuelDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRefuelDate.setStatus("current")
_GeneratorRefuelVolume_Type = Float
_GeneratorRefuelVolume_Object = MibScalar
generatorRefuelVolume = _GeneratorRefuelVolume_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 160),
    _GeneratorRefuelVolume_Type()
)
generatorRefuelVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRefuelVolume.setStatus("current")
if mibBuilder.loadTexts:
    generatorRefuelVolume.setUnits("L")
_GeneratorBackupTime_Type = TimeIntervalInSeconds
_GeneratorBackupTime_Object = MibScalar
generatorBackupTime = _GeneratorBackupTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 170),
    _GeneratorBackupTime_Type()
)
generatorBackupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorBackupTime.setStatus("current")
if mibBuilder.loadTexts:
    generatorBackupTime.setUnits("s")
_TankEmptyDateTime_Type = JulianDateUtc25
_TankEmptyDateTime_Object = MibScalar
tankEmptyDateTime = _TankEmptyDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 180),
    _TankEmptyDateTime_Type()
)
tankEmptyDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tankEmptyDateTime.setStatus("current")
_FuelLevel_Type = Float
_FuelLevel_Object = MibScalar
fuelLevel = _FuelLevel_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 190),
    _FuelLevel_Type()
)
fuelLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelLevel.setStatus("current")
if mibBuilder.loadTexts:
    fuelLevel.setUnits("L")


class _GeneratorControlRelay_Type(RelayMapping):
    """Custom type generatorControlRelay based on RelayMapping"""
    defaultValue = 0


_GeneratorControlRelay_Type.__name__ = "RelayMapping"
_GeneratorControlRelay_Object = MibScalar
generatorControlRelay = _GeneratorControlRelay_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 200),
    _GeneratorControlRelay_Type()
)
generatorControlRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorControlRelay.setStatus("current")


class _GeneratorStartupWiring_Type(GeneratorStartupWiring):
    """Custom type generatorStartupWiring based on GeneratorStartupWiring"""
    defaultValue = 0


_GeneratorStartupWiring_Type.__name__ = "GeneratorStartupWiring"
_GeneratorStartupWiring_Object = MibScalar
generatorStartupWiring = _GeneratorStartupWiring_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 210),
    _GeneratorStartupWiring_Type()
)
generatorStartupWiring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorStartupWiring.setStatus("current")


class _ManualGeneratorRunTime_Type(TimeIntervalInMinutes):
    """Custom type manualGeneratorRunTime based on TimeIntervalInMinutes"""
    defaultValue = 0


_ManualGeneratorRunTime_Type.__name__ = "TimeIntervalInMinutes"
_ManualGeneratorRunTime_Object = MibScalar
manualGeneratorRunTime = _ManualGeneratorRunTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 230),
    _ManualGeneratorRunTime_Type()
)
manualGeneratorRunTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manualGeneratorRunTime.setStatus("current")
if mibBuilder.loadTexts:
    manualGeneratorRunTime.setUnits("min")


class _FuelTankVolume_Type(Float):
    """Custom type fuelTankVolume based on Float"""
    defaultValue = 0


_FuelTankVolume_Type.__name__ = "Float"
_FuelTankVolume_Object = MibScalar
fuelTankVolume = _FuelTankVolume_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 240),
    _FuelTankVolume_Type()
)
fuelTankVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fuelTankVolume.setStatus("current")
if mibBuilder.loadTexts:
    fuelTankVolume.setUnits("L")
_ManualGeneratorStart_Type = NoData
_ManualGeneratorStart_Object = MibScalar
manualGeneratorStart = _ManualGeneratorStart_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 260),
    _ManualGeneratorStart_Type()
)
manualGeneratorStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manualGeneratorStart.setStatus("current")
_ManualGeneratorStop_Type = NoData
_ManualGeneratorStop_Object = MibScalar
manualGeneratorStop = _ManualGeneratorStop_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 270),
    _ManualGeneratorStop_Type()
)
manualGeneratorStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manualGeneratorStop.setStatus("current")
_ClearFuelConsumptionHistory_Type = NoData
_ClearFuelConsumptionHistory_Object = MibScalar
clearFuelConsumptionHistory = _ClearFuelConsumptionHistory_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 80, 280),
    _ClearFuelConsumptionHistory_Type()
)
clearFuelConsumptionHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearFuelConsumptionHistory.setStatus("current")
_PeakLoadReduction_ObjectIdentity = ObjectIdentity
peakLoadReduction = _PeakLoadReduction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 85)
)
if mibBuilder.loadTexts:
    peakLoadReduction.setStatus("current")
_PeakLoadReductionState_Type = PeakLoadReductionState
_PeakLoadReductionState_Object = MibScalar
peakLoadReductionState = _PeakLoadReductionState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 85, 10),
    _PeakLoadReductionState_Type()
)
peakLoadReductionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakLoadReductionState.setStatus("current")


class _EnablePeakLoadReduction_Type(EnableState):
    """Custom type enablePeakLoadReduction based on EnableState"""
    defaultValue = 0


_EnablePeakLoadReduction_Type.__name__ = "EnableState"
_EnablePeakLoadReduction_Object = MibScalar
enablePeakLoadReduction = _EnablePeakLoadReduction_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 85, 20),
    _EnablePeakLoadReduction_Type()
)
enablePeakLoadReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablePeakLoadReduction.setStatus("current")
_PeakLoadReductionRunningTime_Type = TimeIntervalInSeconds
_PeakLoadReductionRunningTime_Object = MibScalar
peakLoadReductionRunningTime = _PeakLoadReductionRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 85, 30),
    _PeakLoadReductionRunningTime_Type()
)
peakLoadReductionRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakLoadReductionRunningTime.setStatus("current")
if mibBuilder.loadTexts:
    peakLoadReductionRunningTime.setUnits("s")
_PeakLoadReductionOffsetVoltage_Type = Float
_PeakLoadReductionOffsetVoltage_Object = MibScalar
peakLoadReductionOffsetVoltage = _PeakLoadReductionOffsetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 85, 40),
    _PeakLoadReductionOffsetVoltage_Type()
)
peakLoadReductionOffsetVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakLoadReductionOffsetVoltage.setStatus("current")
if mibBuilder.loadTexts:
    peakLoadReductionOffsetVoltage.setUnits("0.01 V")


class _PeakLoadReductionSmartAlarm_Type(Unsigned8):
    """Custom type peakLoadReductionSmartAlarm based on Unsigned8"""
    defaultValue = 0


_PeakLoadReductionSmartAlarm_Type.__name__ = "Unsigned8"
_PeakLoadReductionSmartAlarm_Object = MibScalar
peakLoadReductionSmartAlarm = _PeakLoadReductionSmartAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 85, 50),
    _PeakLoadReductionSmartAlarm_Type()
)
peakLoadReductionSmartAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peakLoadReductionSmartAlarm.setStatus("current")


class _PeakLoadReductionMaxDuration_Type(TimeIntervalInMinutes):
    """Custom type peakLoadReductionMaxDuration based on TimeIntervalInMinutes"""
    defaultValue = 120


_PeakLoadReductionMaxDuration_Type.__name__ = "TimeIntervalInMinutes"
_PeakLoadReductionMaxDuration_Object = MibScalar
peakLoadReductionMaxDuration = _PeakLoadReductionMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 85, 60),
    _PeakLoadReductionMaxDuration_Type()
)
peakLoadReductionMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peakLoadReductionMaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    peakLoadReductionMaxDuration.setUnits("min")


class _PeakLoadReductionLowVoltageLimit_Type(Float):
    """Custom type peakLoadReductionLowVoltageLimit based on Float"""
    defaultValue = 4800


_PeakLoadReductionLowVoltageLimit_Type.__name__ = "Float"
_PeakLoadReductionLowVoltageLimit_Object = MibScalar
peakLoadReductionLowVoltageLimit = _PeakLoadReductionLowVoltageLimit_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 85, 70),
    _PeakLoadReductionLowVoltageLimit_Type()
)
peakLoadReductionLowVoltageLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peakLoadReductionLowVoltageLimit.setStatus("current")
if mibBuilder.loadTexts:
    peakLoadReductionLowVoltageLimit.setUnits("0.01 V")
_PeakLoadReductionScheduledStartTime_Type = JulianDateUtc25
_PeakLoadReductionScheduledStartTime_Object = MibScalar
peakLoadReductionScheduledStartTime = _PeakLoadReductionScheduledStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 85, 80),
    _PeakLoadReductionScheduledStartTime_Type()
)
peakLoadReductionScheduledStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peakLoadReductionScheduledStartTime.setStatus("current")
_PeakLoadReductionScheduledDuration_Type = TimeIntervalInMinutes
_PeakLoadReductionScheduledDuration_Object = MibScalar
peakLoadReductionScheduledDuration = _PeakLoadReductionScheduledDuration_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 85, 90),
    _PeakLoadReductionScheduledDuration_Type()
)
peakLoadReductionScheduledDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peakLoadReductionScheduledDuration.setStatus("current")
if mibBuilder.loadTexts:
    peakLoadReductionScheduledDuration.setUnits("min")
_EnergyMeters_ObjectIdentity = ObjectIdentity
energyMeters = _EnergyMeters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87)
)
if mibBuilder.loadTexts:
    energyMeters.setStatus("current")
_EnergyMeterTable_Object = MibTable
energyMeterTable = _EnergyMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10)
)
if mibBuilder.loadTexts:
    energyMeterTable.setStatus("current")
_EnergyMeterEntry_Object = MibTableRow
energyMeterEntry = _EnergyMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1)
)
energyMeterEntry.setIndexNames(
    (0, "RpsSc300Mib", "energyMeterIndex"),
)
if mibBuilder.loadTexts:
    energyMeterEntry.setStatus("current")


class _EnergyMeterIndex_Type(Unsigned8):
    """Custom type energyMeterIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnergyMeterIndex_Type.__name__ = "Unsigned8"
_EnergyMeterIndex_Object = MibTableColumn
energyMeterIndex = _EnergyMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1, 1),
    _EnergyMeterIndex_Type()
)
energyMeterIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    energyMeterIndex.setStatus("current")


class _EnergyMeterName_Type(DisplayString):
    """Custom type energyMeterName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EnergyMeterName_Type.__name__ = "DisplayString"
_EnergyMeterName_Object = MibTableColumn
energyMeterName = _EnergyMeterName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1, 10),
    _EnergyMeterName_Type()
)
energyMeterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    energyMeterName.setStatus("current")


class _EnergyMeterGroup_Type(Unsigned8):
    """Custom type energyMeterGroup based on Unsigned8"""
    defaultValue = 0


_EnergyMeterGroup_Type.__name__ = "Unsigned8"
_EnergyMeterGroup_Object = MibTableColumn
energyMeterGroup = _EnergyMeterGroup_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1, 12),
    _EnergyMeterGroup_Type()
)
energyMeterGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    energyMeterGroup.setStatus("current")
_EnergyMeter_Type = Float
_EnergyMeter_Object = MibTableColumn
energyMeter = _EnergyMeter_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1, 15),
    _EnergyMeter_Type()
)
energyMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    energyMeter.setStatus("current")
if mibBuilder.loadTexts:
    energyMeter.setUnits("0.001 kWh")
_ResetEnergyMeter_Type = NoData
_ResetEnergyMeter_Object = MibTableColumn
resetEnergyMeter = _ResetEnergyMeter_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1, 20),
    _ResetEnergyMeter_Type()
)
resetEnergyMeter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetEnergyMeter.setStatus("current")
_EnergyResetDate_Type = JulianDateUtc25
_EnergyResetDate_Object = MibTableColumn
energyResetDate = _EnergyResetDate_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1, 25),
    _EnergyResetDate_Type()
)
energyResetDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    energyResetDate.setStatus("current")
_CurrentMeter_Type = Float
_CurrentMeter_Object = MibTableColumn
currentMeter = _CurrentMeter_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1, 30),
    _CurrentMeter_Type()
)
currentMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMeter.setStatus("current")
if mibBuilder.loadTexts:
    currentMeter.setUnits("0.1 A")
_VoltageMeter_Type = Float
_VoltageMeter_Object = MibTableColumn
voltageMeter = _VoltageMeter_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1, 35),
    _VoltageMeter_Type()
)
voltageMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMeter.setStatus("current")
if mibBuilder.loadTexts:
    voltageMeter.setUnits("0.01 V")
_PowerMeter_Type = Float
_PowerMeter_Object = MibTableColumn
powerMeter = _PowerMeter_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1, 40),
    _PowerMeter_Type()
)
powerMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerMeter.setStatus("current")
if mibBuilder.loadTexts:
    powerMeter.setUnits("0.01 kW")
_PowerMeterMin_Type = Float
_PowerMeterMin_Object = MibTableColumn
powerMeterMin = _PowerMeterMin_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1, 45),
    _PowerMeterMin_Type()
)
powerMeterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerMeterMin.setStatus("current")
if mibBuilder.loadTexts:
    powerMeterMin.setUnits("0.01 kW")
_PowerMeterMax_Type = Float
_PowerMeterMax_Object = MibTableColumn
powerMeterMax = _PowerMeterMax_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1, 50),
    _PowerMeterMax_Type()
)
powerMeterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerMeterMax.setStatus("current")
if mibBuilder.loadTexts:
    powerMeterMax.setUnits("0.01 kW")
_ResetPowerMeterRange_Type = NoData
_ResetPowerMeterRange_Object = MibTableColumn
resetPowerMeterRange = _ResetPowerMeterRange_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1, 55),
    _ResetPowerMeterRange_Type()
)
resetPowerMeterRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetPowerMeterRange.setStatus("current")


class _PowerMeterGain_Type(Float):
    """Custom type powerMeterGain based on Float"""
    defaultValue = 100


_PowerMeterGain_Type.__name__ = "Float"
_PowerMeterGain_Object = MibTableColumn
powerMeterGain = _PowerMeterGain_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1, 60),
    _PowerMeterGain_Type()
)
powerMeterGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMeterGain.setStatus("current")
if mibBuilder.loadTexts:
    powerMeterGain.setUnits("0.01")


class _PowerMeterOffset_Type(Float):
    """Custom type powerMeterOffset based on Float"""
    defaultValue = 0


_PowerMeterOffset_Type.__name__ = "Float"
_PowerMeterOffset_Object = MibTableColumn
powerMeterOffset = _PowerMeterOffset_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 10, 1, 65),
    _PowerMeterOffset_Type()
)
powerMeterOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMeterOffset.setStatus("current")
if mibBuilder.loadTexts:
    powerMeterOffset.setUnits("0.01")
_EnergyMeterAiMappingTable_Object = MibTable
energyMeterAiMappingTable = _EnergyMeterAiMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 20)
)
if mibBuilder.loadTexts:
    energyMeterAiMappingTable.setStatus("current")
_EnergyMeterAiMappingEntry_Object = MibTableRow
energyMeterAiMappingEntry = _EnergyMeterAiMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 20, 1)
)
energyMeterAiMappingEntry.setIndexNames(
    (0, "RpsSc300Mib", "energyMeterAiMappingIndex"),
)
if mibBuilder.loadTexts:
    energyMeterAiMappingEntry.setStatus("current")


class _EnergyMeterAiMappingIndex_Type(Unsigned8):
    """Custom type energyMeterAiMappingIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnergyMeterAiMappingIndex_Type.__name__ = "Unsigned8"
_EnergyMeterAiMappingIndex_Object = MibTableColumn
energyMeterAiMappingIndex = _EnergyMeterAiMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 20, 1, 1),
    _EnergyMeterAiMappingIndex_Type()
)
energyMeterAiMappingIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    energyMeterAiMappingIndex.setStatus("current")


class _EnergyMeterMeter_Type(Unsigned8):
    """Custom type energyMeterMeter based on Unsigned8"""
    defaultValue = 0


_EnergyMeterMeter_Type.__name__ = "Unsigned8"
_EnergyMeterMeter_Object = MibTableColumn
energyMeterMeter = _EnergyMeterMeter_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 20, 1, 10),
    _EnergyMeterMeter_Type()
)
energyMeterMeter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    energyMeterMeter.setStatus("current")


class _EnergyMeterAi_Type(Unsigned8):
    """Custom type energyMeterAi based on Unsigned8"""
    defaultValue = 0


_EnergyMeterAi_Type.__name__ = "Unsigned8"
_EnergyMeterAi_Object = MibTableColumn
energyMeterAi = _EnergyMeterAi_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 20, 1, 15),
    _EnergyMeterAi_Type()
)
energyMeterAi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    energyMeterAi.setStatus("current")


class _EnergyMeterAiFunction_Type(EnergyMeterAiFunction):
    """Custom type energyMeterAiFunction based on EnergyMeterAiFunction"""
    defaultValue = 0


_EnergyMeterAiFunction_Type.__name__ = "EnergyMeterAiFunction"
_EnergyMeterAiFunction_Object = MibTableColumn
energyMeterAiFunction = _EnergyMeterAiFunction_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 20, 1, 20),
    _EnergyMeterAiFunction_Type()
)
energyMeterAiFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    energyMeterAiFunction.setStatus("current")
_EnergyMeterValueMappingTable_Object = MibTable
energyMeterValueMappingTable = _EnergyMeterValueMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 30)
)
if mibBuilder.loadTexts:
    energyMeterValueMappingTable.setStatus("current")
_EnergyMeterValueMappingEntry_Object = MibTableRow
energyMeterValueMappingEntry = _EnergyMeterValueMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 30, 1)
)
energyMeterValueMappingEntry.setIndexNames(
    (0, "RpsSc300Mib", "energyMeterValueMappingIndex"),
)
if mibBuilder.loadTexts:
    energyMeterValueMappingEntry.setStatus("current")


class _EnergyMeterValueMappingIndex_Type(Unsigned8):
    """Custom type energyMeterValueMappingIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnergyMeterValueMappingIndex_Type.__name__ = "Unsigned8"
_EnergyMeterValueMappingIndex_Object = MibTableColumn
energyMeterValueMappingIndex = _EnergyMeterValueMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 30, 1, 1),
    _EnergyMeterValueMappingIndex_Type()
)
energyMeterValueMappingIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    energyMeterValueMappingIndex.setStatus("current")


class _EnergyMeterMeterNumber_Type(Unsigned8):
    """Custom type energyMeterMeterNumber based on Unsigned8"""
    defaultValue = 0


_EnergyMeterMeterNumber_Type.__name__ = "Unsigned8"
_EnergyMeterMeterNumber_Object = MibTableColumn
energyMeterMeterNumber = _EnergyMeterMeterNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 30, 1, 10),
    _EnergyMeterMeterNumber_Type()
)
energyMeterMeterNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    energyMeterMeterNumber.setStatus("current")


class _EnergyMeterSystemValue_Type(EnergyMeterSystemValue):
    """Custom type energyMeterSystemValue based on EnergyMeterSystemValue"""
    defaultValue = 3


_EnergyMeterSystemValue_Type.__name__ = "EnergyMeterSystemValue"
_EnergyMeterSystemValue_Object = MibTableColumn
energyMeterSystemValue = _EnergyMeterSystemValue_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 30, 1, 15),
    _EnergyMeterSystemValue_Type()
)
energyMeterSystemValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    energyMeterSystemValue.setStatus("current")


class _EnergyMeterSystemValueIndex_Type(Unsigned8):
    """Custom type energyMeterSystemValueIndex based on Unsigned8"""
    defaultValue = 0


_EnergyMeterSystemValueIndex_Type.__name__ = "Unsigned8"
_EnergyMeterSystemValueIndex_Object = MibTableColumn
energyMeterSystemValueIndex = _EnergyMeterSystemValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 30, 1, 20),
    _EnergyMeterSystemValueIndex_Type()
)
energyMeterSystemValueIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    energyMeterSystemValueIndex.setStatus("current")
_ResetAllEnergyMeters_Type = NoData
_ResetAllEnergyMeters_Object = MibScalar
resetAllEnergyMeters = _ResetAllEnergyMeters_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 40),
    _ResetAllEnergyMeters_Type()
)
resetAllEnergyMeters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetAllEnergyMeters.setStatus("current")
_ResetAllPowerMeterRanges_Type = NoData
_ResetAllPowerMeterRanges_Object = MibScalar
resetAllPowerMeterRanges = _ResetAllPowerMeterRanges_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 87, 50),
    _ResetAllPowerMeterRanges_Type()
)
resetAllPowerMeterRanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetAllPowerMeterRanges.setStatus("current")
_FanController_ObjectIdentity = ObjectIdentity
fanController = _FanController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88)
)
if mibBuilder.loadTexts:
    fanController.setStatus("current")
_SetFanPowerRunningTime_Type = TimeIntervalInMinutes
_SetFanPowerRunningTime_Object = MibScalar
setFanPowerRunningTime = _SetFanPowerRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 10),
    _SetFanPowerRunningTime_Type()
)
setFanPowerRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setFanPowerRunningTime.setStatus("current")
if mibBuilder.loadTexts:
    setFanPowerRunningTime.setUnits("min")
_FanControllerProfile_Type = FanControllerProfile
_FanControllerProfile_Object = MibScalar
fanControllerProfile = _FanControllerProfile_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 20),
    _FanControllerProfile_Type()
)
fanControllerProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanControllerProfile.setStatus("current")
_RxpFcFaults_Type = Unsigned16
_RxpFcFaults_Object = MibScalar
rxpFcFaults = _RxpFcFaults_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 25),
    _RxpFcFaults_Type()
)
rxpFcFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxpFcFaults.setStatus("current")
_FanControllerStateTable_Object = MibTable
fanControllerStateTable = _FanControllerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 30)
)
if mibBuilder.loadTexts:
    fanControllerStateTable.setStatus("current")
_FanControllerStateEntry_Object = MibTableRow
fanControllerStateEntry = _FanControllerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 30, 1)
)
fanControllerStateEntry.setIndexNames(
    (0, "RpsSc300Mib", "fanControllerStateIndex"),
)
if mibBuilder.loadTexts:
    fanControllerStateEntry.setStatus("current")


class _FanControllerStateIndex_Type(Unsigned8):
    """Custom type fanControllerStateIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FanControllerStateIndex_Type.__name__ = "Unsigned8"
_FanControllerStateIndex_Object = MibTableColumn
fanControllerStateIndex = _FanControllerStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 30, 1, 1),
    _FanControllerStateIndex_Type()
)
fanControllerStateIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fanControllerStateIndex.setStatus("current")
_FanTemperature_Type = Float
_FanTemperature_Object = MibTableColumn
fanTemperature = _FanTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 30, 1, 10),
    _FanTemperature_Type()
)
fanTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanTemperature.setStatus("current")
if mibBuilder.loadTexts:
    fanTemperature.setUnits("0.1 °C")
_FanPower_Type = Percentile8Nan
_FanPower_Object = MibTableColumn
fanPower = _FanPower_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 30, 1, 20),
    _FanPower_Type()
)
fanPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanPower.setStatus("current")
if mibBuilder.loadTexts:
    fanPower.setUnits("%")
_SetFanPower_Type = Unsigned8
_SetFanPower_Object = MibTableColumn
setFanPower = _SetFanPower_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 30, 1, 30),
    _SetFanPower_Type()
)
setFanPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setFanPower.setStatus("current")
if mibBuilder.loadTexts:
    setFanPower.setUnits("%")


class _FanPoles_Type(Unsigned8):
    """Custom type fanPoles based on Unsigned8"""
    defaultValue = 4


_FanPoles_Type.__name__ = "Unsigned8"
_FanPoles_Object = MibTableColumn
fanPoles = _FanPoles_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 30, 1, 40),
    _FanPoles_Type()
)
fanPoles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanPoles.setStatus("current")
_FanSpeedA_Type = Unsigned16
_FanSpeedA_Object = MibTableColumn
fanSpeedA = _FanSpeedA_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 30, 1, 50),
    _FanSpeedA_Type()
)
fanSpeedA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedA.setStatus("current")
_FanSpeedB_Type = Unsigned16
_FanSpeedB_Object = MibTableColumn
fanSpeedB = _FanSpeedB_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 30, 1, 60),
    _FanSpeedB_Type()
)
fanSpeedB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedB.setStatus("current")


class _FanControllerMode_Type(FanControllerMode):
    """Custom type fanControllerMode based on FanControllerMode"""
    defaultValue = 2


_FanControllerMode_Type.__name__ = "FanControllerMode"
_FanControllerMode_Object = MibScalar
fanControllerMode = _FanControllerMode_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 40),
    _FanControllerMode_Type()
)
fanControllerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanControllerMode.setStatus("current")


class _SetFanPowerPeriod_Type(Unsigned16):
    """Custom type setFanPowerPeriod based on Unsigned16"""
    defaultValue = 10


_SetFanPowerPeriod_Type.__name__ = "Unsigned16"
_SetFanPowerPeriod_Object = MibScalar
setFanPowerPeriod = _SetFanPowerPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 50),
    _SetFanPowerPeriod_Type()
)
setFanPowerPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setFanPowerPeriod.setStatus("current")
_ApplySetPower_Type = NoData
_ApplySetPower_Object = MibScalar
applySetPower = _ApplySetPower_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 60),
    _ApplySetPower_Type()
)
applySetPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applySetPower.setStatus("current")
_FanController1PrimaryTable_Object = MibTable
fanController1PrimaryTable = _FanController1PrimaryTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 70)
)
if mibBuilder.loadTexts:
    fanController1PrimaryTable.setStatus("current")
_FanController1PrimaryEntry_Object = MibTableRow
fanController1PrimaryEntry = _FanController1PrimaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 70, 1)
)
fanController1PrimaryEntry.setIndexNames(
    (0, "RpsSc300Mib", "fanController1PrimaryIndex"),
)
if mibBuilder.loadTexts:
    fanController1PrimaryEntry.setStatus("current")


class _FanController1PrimaryIndex_Type(Unsigned16):
    """Custom type fanController1PrimaryIndex based on Unsigned16"""
    subtypeSpec = Unsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FanController1PrimaryIndex_Type.__name__ = "Unsigned16"
_FanController1PrimaryIndex_Object = MibTableColumn
fanController1PrimaryIndex = _FanController1PrimaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 70, 1, 1),
    _FanController1PrimaryIndex_Type()
)
fanController1PrimaryIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fanController1PrimaryIndex.setStatus("current")


class _Fc1pTemperature_Type(Float):
    """Custom type fc1pTemperature based on Float"""
    defaultValue = 340


_Fc1pTemperature_Type.__name__ = "Float"
_Fc1pTemperature_Object = MibTableColumn
fc1pTemperature = _Fc1pTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 70, 1, 10),
    _Fc1pTemperature_Type()
)
fc1pTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fc1pTemperature.setStatus("current")
if mibBuilder.loadTexts:
    fc1pTemperature.setUnits("0.1 °C")


class _Fc1pPower_Type(Unsigned8):
    """Custom type fc1pPower based on Unsigned8"""
    defaultValue = 20


_Fc1pPower_Type.__name__ = "Unsigned8"
_Fc1pPower_Object = MibTableColumn
fc1pPower = _Fc1pPower_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 70, 1, 20),
    _Fc1pPower_Type()
)
fc1pPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fc1pPower.setStatus("current")
if mibBuilder.loadTexts:
    fc1pPower.setUnits("%")
_FanController1SecondaryTable_Object = MibTable
fanController1SecondaryTable = _FanController1SecondaryTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 90)
)
if mibBuilder.loadTexts:
    fanController1SecondaryTable.setStatus("current")
_FanController1SecondaryEntry_Object = MibTableRow
fanController1SecondaryEntry = _FanController1SecondaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 90, 1)
)
fanController1SecondaryEntry.setIndexNames(
    (0, "RpsSc300Mib", "fanController1SecondaryIndex"),
)
if mibBuilder.loadTexts:
    fanController1SecondaryEntry.setStatus("current")


class _FanController1SecondaryIndex_Type(Unsigned16):
    """Custom type fanController1SecondaryIndex based on Unsigned16"""
    subtypeSpec = Unsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FanController1SecondaryIndex_Type.__name__ = "Unsigned16"
_FanController1SecondaryIndex_Object = MibTableColumn
fanController1SecondaryIndex = _FanController1SecondaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 90, 1, 1),
    _FanController1SecondaryIndex_Type()
)
fanController1SecondaryIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fanController1SecondaryIndex.setStatus("current")


class _Fc1sTemperature_Type(Float):
    """Custom type fc1sTemperature based on Float"""
    defaultValue = 340


_Fc1sTemperature_Type.__name__ = "Float"
_Fc1sTemperature_Object = MibTableColumn
fc1sTemperature = _Fc1sTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 90, 1, 10),
    _Fc1sTemperature_Type()
)
fc1sTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fc1sTemperature.setStatus("current")
if mibBuilder.loadTexts:
    fc1sTemperature.setUnits("0.1 °C")


class _Fc1sPower_Type(Unsigned8):
    """Custom type fc1sPower based on Unsigned8"""
    defaultValue = 20


_Fc1sPower_Type.__name__ = "Unsigned8"
_Fc1sPower_Object = MibTableColumn
fc1sPower = _Fc1sPower_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 90, 1, 20),
    _Fc1sPower_Type()
)
fc1sPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fc1sPower.setStatus("current")
if mibBuilder.loadTexts:
    fc1sPower.setUnits("%")
_FanController2PrimaryTable_Object = MibTable
fanController2PrimaryTable = _FanController2PrimaryTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 110)
)
if mibBuilder.loadTexts:
    fanController2PrimaryTable.setStatus("current")
_FanController2PrimaryEntry_Object = MibTableRow
fanController2PrimaryEntry = _FanController2PrimaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 110, 1)
)
fanController2PrimaryEntry.setIndexNames(
    (0, "RpsSc300Mib", "fanController2PrimaryIndex"),
)
if mibBuilder.loadTexts:
    fanController2PrimaryEntry.setStatus("current")


class _FanController2PrimaryIndex_Type(Unsigned16):
    """Custom type fanController2PrimaryIndex based on Unsigned16"""
    subtypeSpec = Unsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FanController2PrimaryIndex_Type.__name__ = "Unsigned16"
_FanController2PrimaryIndex_Object = MibTableColumn
fanController2PrimaryIndex = _FanController2PrimaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 110, 1, 1),
    _FanController2PrimaryIndex_Type()
)
fanController2PrimaryIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fanController2PrimaryIndex.setStatus("current")


class _Fc2pTemperature_Type(Float):
    """Custom type fc2pTemperature based on Float"""
    defaultValue = 340


_Fc2pTemperature_Type.__name__ = "Float"
_Fc2pTemperature_Object = MibTableColumn
fc2pTemperature = _Fc2pTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 110, 1, 10),
    _Fc2pTemperature_Type()
)
fc2pTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fc2pTemperature.setStatus("current")
if mibBuilder.loadTexts:
    fc2pTemperature.setUnits("0.1 °C")


class _Fc2pPower_Type(Unsigned8):
    """Custom type fc2pPower based on Unsigned8"""
    defaultValue = 20


_Fc2pPower_Type.__name__ = "Unsigned8"
_Fc2pPower_Object = MibTableColumn
fc2pPower = _Fc2pPower_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 110, 1, 20),
    _Fc2pPower_Type()
)
fc2pPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fc2pPower.setStatus("current")
if mibBuilder.loadTexts:
    fc2pPower.setUnits("%")
_FanController2SecondaryTable_Object = MibTable
fanController2SecondaryTable = _FanController2SecondaryTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 130)
)
if mibBuilder.loadTexts:
    fanController2SecondaryTable.setStatus("current")
_FanController2SecondaryEntry_Object = MibTableRow
fanController2SecondaryEntry = _FanController2SecondaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 130, 1)
)
fanController2SecondaryEntry.setIndexNames(
    (0, "RpsSc300Mib", "fanController2SecondaryIndex"),
)
if mibBuilder.loadTexts:
    fanController2SecondaryEntry.setStatus("current")


class _FanController2SecondaryIndex_Type(Unsigned16):
    """Custom type fanController2SecondaryIndex based on Unsigned16"""
    subtypeSpec = Unsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FanController2SecondaryIndex_Type.__name__ = "Unsigned16"
_FanController2SecondaryIndex_Object = MibTableColumn
fanController2SecondaryIndex = _FanController2SecondaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 130, 1, 1),
    _FanController2SecondaryIndex_Type()
)
fanController2SecondaryIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fanController2SecondaryIndex.setStatus("current")


class _Fc2sTemperature_Type(Float):
    """Custom type fc2sTemperature based on Float"""
    defaultValue = 340


_Fc2sTemperature_Type.__name__ = "Float"
_Fc2sTemperature_Object = MibTableColumn
fc2sTemperature = _Fc2sTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 130, 1, 10),
    _Fc2sTemperature_Type()
)
fc2sTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fc2sTemperature.setStatus("current")
if mibBuilder.loadTexts:
    fc2sTemperature.setUnits("0.1 °C")


class _Fc2sPower_Type(Unsigned8):
    """Custom type fc2sPower based on Unsigned8"""
    defaultValue = 20


_Fc2sPower_Type.__name__ = "Unsigned8"
_Fc2sPower_Object = MibTableColumn
fc2sPower = _Fc2sPower_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 130, 1, 20),
    _Fc2sPower_Type()
)
fc2sPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fc2sPower.setStatus("current")
if mibBuilder.loadTexts:
    fc2sPower.setUnits("%")


class _FanControllerSmartAlarm_Type(Unsigned8):
    """Custom type fanControllerSmartAlarm based on Unsigned8"""
    defaultValue = 0


_FanControllerSmartAlarm_Type.__name__ = "Unsigned8"
_FanControllerSmartAlarm_Object = MibScalar
fanControllerSmartAlarm = _FanControllerSmartAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 70, 88, 150),
    _FanControllerSmartAlarm_Type()
)
fanControllerSmartAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanControllerSmartAlarm.setStatus("current")
_RealTimeClock_ObjectIdentity = ObjectIdentity
realTimeClock = _RealTimeClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 80)
)
if mibBuilder.loadTexts:
    realTimeClock.setStatus("current")
_ControllerTime_Type = JulianDateUtc25
_ControllerTime_Object = MibScalar
controllerTime = _ControllerTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 80, 10),
    _ControllerTime_Type()
)
controllerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerTime.setStatus("current")
_InputOutput_ObjectIdentity = ObjectIdentity
inputOutput = _InputOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90)
)
if mibBuilder.loadTexts:
    inputOutput.setStatus("current")
_SystemAnalogInput_ObjectIdentity = ObjectIdentity
systemAnalogInput = _SystemAnalogInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10)
)
if mibBuilder.loadTexts:
    systemAnalogInput.setStatus("current")
_AnalogInputTable_Object = MibTable
analogInputTable = _AnalogInputTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30)
)
if mibBuilder.loadTexts:
    analogInputTable.setStatus("current")
_AnalogInputEntry_Object = MibTableRow
analogInputEntry = _AnalogInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1)
)
analogInputEntry.setIndexNames(
    (0, "RpsSc300Mib", "analogInputIndex"),
)
if mibBuilder.loadTexts:
    analogInputEntry.setStatus("current")


class _AnalogInputIndex_Type(Unsigned8):
    """Custom type analogInputIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnalogInputIndex_Type.__name__ = "Unsigned8"
_AnalogInputIndex_Object = MibTableColumn
analogInputIndex = _AnalogInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 1),
    _AnalogInputIndex_Type()
)
analogInputIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    analogInputIndex.setStatus("current")
_AiHighState_Type = AlarmActiveState
_AiHighState_Object = MibTableColumn
aiHighState = _AiHighState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 20),
    _AiHighState_Type()
)
aiHighState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiHighState.setStatus("current")
_AiLowState_Type = AlarmActiveState
_AiLowState_Object = MibTableColumn
aiLowState = _AiLowState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 30),
    _AiLowState_Type()
)
aiLowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiLowState.setStatus("current")
_AiValue_Type = Float
_AiValue_Object = MibTableColumn
aiValue = _AiValue_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 40),
    _AiValue_Type()
)
aiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiValue.setStatus("current")
if mibBuilder.loadTexts:
    aiValue.setUnits("0.01")


class _AiStatus_Type(EnableState):
    """Custom type aiStatus based on EnableState"""
    defaultValue = 0


_AiStatus_Type.__name__ = "EnableState"
_AiStatus_Object = MibTableColumn
aiStatus = _AiStatus_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 50),
    _AiStatus_Type()
)
aiStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiStatus.setStatus("current")


class _AiName_Type(DisplayString):
    """Custom type aiName based on DisplayString"""
    defaultValue = OctetString("Bus Voltage")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AiName_Type.__name__ = "DisplayString"
_AiName_Object = MibTableColumn
aiName = _AiName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 60),
    _AiName_Type()
)
aiName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiName.setStatus("current")


class _AiFunction_Type(AiFunction):
    """Custom type aiFunction based on AiFunction"""
    defaultValue = 1


_AiFunction_Type.__name__ = "AiFunction"
_AiFunction_Object = MibTableColumn
aiFunction = _AiFunction_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 64),
    _AiFunction_Type()
)
aiFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiFunction.setStatus("current")


class _AiFunctionIndex_Type(Unsigned8):
    """Custom type aiFunctionIndex based on Unsigned8"""
    defaultValue = 1


_AiFunctionIndex_Type.__name__ = "Unsigned8"
_AiFunctionIndex_Object = MibTableColumn
aiFunctionIndex = _AiFunctionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 66),
    _AiFunctionIndex_Type()
)
aiFunctionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiFunctionIndex.setStatus("current")


class _AiUnits_Type(MeasurementUnits):
    """Custom type aiUnits based on MeasurementUnits"""
    defaultValue = 30


_AiUnits_Type.__name__ = "MeasurementUnits"
_AiUnits_Object = MibTableColumn
aiUnits = _AiUnits_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 70),
    _AiUnits_Type()
)
aiUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiUnits.setStatus("current")


class _AiIobNumber_Type(Unsigned8):
    """Custom type aiIobNumber based on Unsigned8"""
    defaultValue = 1


_AiIobNumber_Type.__name__ = "Unsigned8"
_AiIobNumber_Object = MibTableColumn
aiIobNumber = _AiIobNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 80),
    _AiIobNumber_Type()
)
aiIobNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiIobNumber.setStatus("current")


class _InputNumber_Type(Unsigned8):
    """Custom type inputNumber based on Unsigned8"""
    defaultValue = 2


_InputNumber_Type.__name__ = "Unsigned8"
_InputNumber_Object = MibTableColumn
inputNumber = _InputNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 90),
    _InputNumber_Type()
)
inputNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputNumber.setStatus("current")


class _Gain_Type(Float):
    """Custom type gain based on Float"""
    defaultValue = 100


_Gain_Type.__name__ = "Float"
_Gain_Object = MibTableColumn
gain = _Gain_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 100),
    _Gain_Type()
)
gain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gain.setStatus("current")
if mibBuilder.loadTexts:
    gain.setUnits("0.01")


class _Offset_Type(Float):
    """Custom type offset based on Float"""
    defaultValue = 0


_Offset_Type.__name__ = "Float"
_Offset_Object = MibTableColumn
offset = _Offset_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 110),
    _Offset_Type()
)
offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offset.setStatus("current")
if mibBuilder.loadTexts:
    offset.setUnits("0.01")


class _Hysteresis_Type(Float):
    """Custom type hysteresis based on Float"""
    defaultValue = 0


_Hysteresis_Type.__name__ = "Float"
_Hysteresis_Object = MibTableColumn
hysteresis = _Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 130),
    _Hysteresis_Type()
)
hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hysteresis.setStatus("current")
if mibBuilder.loadTexts:
    hysteresis.setUnits("0.01")


class _HighSeverity_Type(AlarmSeverity):
    """Custom type highSeverity based on AlarmSeverity"""
    defaultValue = 0


_HighSeverity_Type.__name__ = "AlarmSeverity"
_HighSeverity_Object = MibTableColumn
highSeverity = _HighSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 141),
    _HighSeverity_Type()
)
highSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highSeverity.setStatus("current")


class _HighThreshold_Type(Float):
    """Custom type highThreshold based on Float"""
    defaultValue = 1000


_HighThreshold_Type.__name__ = "Float"
_HighThreshold_Object = MibTableColumn
highThreshold = _HighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 150),
    _HighThreshold_Type()
)
highThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highThreshold.setStatus("current")
if mibBuilder.loadTexts:
    highThreshold.setUnits("0.01")


class _HighDoMappingA_Type(RelayMapping):
    """Custom type highDoMappingA based on RelayMapping"""
    defaultValue = 0


_HighDoMappingA_Type.__name__ = "RelayMapping"
_HighDoMappingA_Object = MibTableColumn
highDoMappingA = _HighDoMappingA_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 160),
    _HighDoMappingA_Type()
)
highDoMappingA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highDoMappingA.setStatus("current")


class _HighDoMappingB_Type(RelayMapping):
    """Custom type highDoMappingB based on RelayMapping"""
    defaultValue = 0


_HighDoMappingB_Type.__name__ = "RelayMapping"
_HighDoMappingB_Object = MibTableColumn
highDoMappingB = _HighDoMappingB_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 170),
    _HighDoMappingB_Type()
)
highDoMappingB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highDoMappingB.setStatus("current")


class _HighTrapSend_Type(SendTrap):
    """Custom type highTrapSend based on SendTrap"""
    defaultValue = 1


_HighTrapSend_Type.__name__ = "SendTrap"
_HighTrapSend_Object = MibTableColumn
highTrapSend = _HighTrapSend_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 175),
    _HighTrapSend_Type()
)
highTrapSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highTrapSend.setStatus("current")


class _LowSeverity_Type(AlarmSeverity):
    """Custom type lowSeverity based on AlarmSeverity"""
    defaultValue = 0


_LowSeverity_Type.__name__ = "AlarmSeverity"
_LowSeverity_Object = MibTableColumn
lowSeverity = _LowSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 181),
    _LowSeverity_Type()
)
lowSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowSeverity.setStatus("current")


class _LowThreshold_Type(Float):
    """Custom type lowThreshold based on Float"""
    defaultValue = 0


_LowThreshold_Type.__name__ = "Float"
_LowThreshold_Object = MibTableColumn
lowThreshold = _LowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 190),
    _LowThreshold_Type()
)
lowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    lowThreshold.setUnits("0.01")


class _LowDoMappingA_Type(RelayMapping):
    """Custom type lowDoMappingA based on RelayMapping"""
    defaultValue = 0


_LowDoMappingA_Type.__name__ = "RelayMapping"
_LowDoMappingA_Object = MibTableColumn
lowDoMappingA = _LowDoMappingA_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 200),
    _LowDoMappingA_Type()
)
lowDoMappingA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowDoMappingA.setStatus("current")


class _LowDoMappingB_Type(RelayMapping):
    """Custom type lowDoMappingB based on RelayMapping"""
    defaultValue = 0


_LowDoMappingB_Type.__name__ = "RelayMapping"
_LowDoMappingB_Object = MibTableColumn
lowDoMappingB = _LowDoMappingB_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 210),
    _LowDoMappingB_Type()
)
lowDoMappingB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowDoMappingB.setStatus("current")


class _LowTrapSend_Type(SendTrap):
    """Custom type lowTrapSend based on SendTrap"""
    defaultValue = 1


_LowTrapSend_Type.__name__ = "SendTrap"
_LowTrapSend_Object = MibTableColumn
lowTrapSend = _LowTrapSend_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 215),
    _LowTrapSend_Type()
)
lowTrapSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowTrapSend.setStatus("current")


class _AiGroup_Type(Unsigned8):
    """Custom type aiGroup based on Unsigned8"""
    defaultValue = 0


_AiGroup_Type.__name__ = "Unsigned8"
_AiGroup_Object = MibTableColumn
aiGroup = _AiGroup_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 220),
    _AiGroup_Type()
)
aiGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiGroup.setStatus("current")


class _AiHighNotes_Type(DisplayString):
    """Custom type aiHighNotes based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AiHighNotes_Type.__name__ = "DisplayString"
_AiHighNotes_Object = MibTableColumn
aiHighNotes = _AiHighNotes_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 230),
    _AiHighNotes_Type()
)
aiHighNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiHighNotes.setStatus("current")


class _AiLowNotes_Type(DisplayString):
    """Custom type aiLowNotes based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AiLowNotes_Type.__name__ = "DisplayString"
_AiLowNotes_Object = MibTableColumn
aiLowNotes = _AiLowNotes_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 30, 1, 240),
    _AiLowNotes_Type()
)
aiLowNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiLowNotes.setStatus("current")
_SmartAnalogTable_Object = MibTable
smartAnalogTable = _SmartAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 40)
)
if mibBuilder.loadTexts:
    smartAnalogTable.setStatus("current")
_SmartAnalogEntry_Object = MibTableRow
smartAnalogEntry = _SmartAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 40, 1)
)
smartAnalogEntry.setIndexNames(
    (0, "RpsSc300Mib", "smartAnalogIndex"),
)
if mibBuilder.loadTexts:
    smartAnalogEntry.setStatus("current")


class _SmartAnalogIndex_Type(Unsigned8):
    """Custom type smartAnalogIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SmartAnalogIndex_Type.__name__ = "Unsigned8"
_SmartAnalogIndex_Object = MibTableColumn
smartAnalogIndex = _SmartAnalogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 40, 1, 1),
    _SmartAnalogIndex_Type()
)
smartAnalogIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartAnalogIndex.setStatus("current")


class _Name_Type(DisplayString):
    """Custom type name based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Name_Type.__name__ = "DisplayString"
_Name_Object = MibTableColumn
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 40, 1, 10),
    _Name_Type()
)
name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    name.setStatus("current")


class _Group_Type(Unsigned8):
    """Custom type group based on Unsigned8"""
    defaultValue = 0


_Group_Type.__name__ = "Unsigned8"
_Group_Object = MibTableColumn
group = _Group_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 40, 1, 20),
    _Group_Type()
)
group.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group.setStatus("current")
_Value_Type = Float
_Value_Object = MibTableColumn
value = _Value_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 40, 1, 30),
    _Value_Type()
)
value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    value.setStatus("current")
if mibBuilder.loadTexts:
    value.setUnits("0.01")


class _Type_Type(SmartAnalogType):
    """Custom type type based on SmartAnalogType"""
    defaultValue = 1


_Type_Type.__name__ = "SmartAnalogType"
_Type_Object = MibTableColumn
type = _Type_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 40, 1, 40),
    _Type_Type()
)
type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    type.setStatus("current")


class _Units_Type(DisplayString):
    """Custom type units based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Units_Type.__name__ = "DisplayString"
_Units_Object = MibTableColumn
units = _Units_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 40, 1, 50),
    _Units_Type()
)
units.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    units.setStatus("current")


class _SmartAnalogGate_Type(SmartAnalogGate):
    """Custom type smartAnalogGate based on SmartAnalogGate"""
    defaultValue = 0


_SmartAnalogGate_Type.__name__ = "SmartAnalogGate"
_SmartAnalogGate_Object = MibTableColumn
smartAnalogGate = _SmartAnalogGate_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 40, 1, 60),
    _SmartAnalogGate_Type()
)
smartAnalogGate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAnalogGate.setStatus("current")


class _SaiFunction_Type(AiFunction):
    """Custom type saiFunction based on AiFunction"""
    defaultValue = 1


_SaiFunction_Type.__name__ = "AiFunction"
_SaiFunction_Object = MibTableColumn
saiFunction = _SaiFunction_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 40, 1, 70),
    _SaiFunction_Type()
)
saiFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saiFunction.setStatus("current")


class _SaiFunctionIndex_Type(Unsigned8):
    """Custom type saiFunctionIndex based on Unsigned8"""
    defaultValue = 1


_SaiFunctionIndex_Type.__name__ = "Unsigned8"
_SaiFunctionIndex_Object = MibTableColumn
saiFunctionIndex = _SaiFunctionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 40, 1, 80),
    _SaiFunctionIndex_Type()
)
saiFunctionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saiFunctionIndex.setStatus("current")
_SmartAnalogMappingTable_Object = MibTable
smartAnalogMappingTable = _SmartAnalogMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 45)
)
if mibBuilder.loadTexts:
    smartAnalogMappingTable.setStatus("current")
_SmartAnalogMappingEntry_Object = MibTableRow
smartAnalogMappingEntry = _SmartAnalogMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 45, 1)
)
smartAnalogMappingEntry.setIndexNames(
    (0, "RpsSc300Mib", "smartAnalogMappingIndex"),
)
if mibBuilder.loadTexts:
    smartAnalogMappingEntry.setStatus("current")


class _SmartAnalogMappingIndex_Type(Unsigned8):
    """Custom type smartAnalogMappingIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SmartAnalogMappingIndex_Type.__name__ = "Unsigned8"
_SmartAnalogMappingIndex_Object = MibTableColumn
smartAnalogMappingIndex = _SmartAnalogMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 45, 1, 1),
    _SmartAnalogMappingIndex_Type()
)
smartAnalogMappingIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartAnalogMappingIndex.setStatus("current")


class _SmartAnalogSystemInputMapping_Type(Unsigned8):
    """Custom type smartAnalogSystemInputMapping based on Unsigned8"""
    defaultValue = 0


_SmartAnalogSystemInputMapping_Type.__name__ = "Unsigned8"
_SmartAnalogSystemInputMapping_Object = MibTableColumn
smartAnalogSystemInputMapping = _SmartAnalogSystemInputMapping_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 45, 1, 10),
    _SmartAnalogSystemInputMapping_Type()
)
smartAnalogSystemInputMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAnalogSystemInputMapping.setStatus("current")
_SmartAnalogSystemInputValue_Type = Float
_SmartAnalogSystemInputValue_Object = MibTableColumn
smartAnalogSystemInputValue = _SmartAnalogSystemInputValue_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 45, 1, 20),
    _SmartAnalogSystemInputValue_Type()
)
smartAnalogSystemInputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAnalogSystemInputValue.setStatus("current")
if mibBuilder.loadTexts:
    smartAnalogSystemInputValue.setUnits("0.01")


class _SmartAnalogSystemInput_Type(SystemInputType):
    """Custom type smartAnalogSystemInput based on SystemInputType"""
    defaultValue = 1


_SmartAnalogSystemInput_Type.__name__ = "SystemInputType"
_SmartAnalogSystemInput_Object = MibTableColumn
smartAnalogSystemInput = _SmartAnalogSystemInput_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 45, 1, 30),
    _SmartAnalogSystemInput_Type()
)
smartAnalogSystemInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAnalogSystemInput.setStatus("current")


class _SmartAnalogSystemInputIndex_Type(Unsigned8):
    """Custom type smartAnalogSystemInputIndex based on Unsigned8"""
    defaultValue = 0


_SmartAnalogSystemInputIndex_Type.__name__ = "Unsigned8"
_SmartAnalogSystemInputIndex_Object = MibTableColumn
smartAnalogSystemInputIndex = _SmartAnalogSystemInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 45, 1, 40),
    _SmartAnalogSystemInputIndex_Type()
)
smartAnalogSystemInputIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAnalogSystemInputIndex.setStatus("current")


class _SmartAnalogSystemInputInvert_Type(Boolean):
    """Custom type smartAnalogSystemInputInvert based on Boolean"""
    defaultValue = 0


_SmartAnalogSystemInputInvert_Type.__name__ = "Boolean"
_SmartAnalogSystemInputInvert_Object = MibTableColumn
smartAnalogSystemInputInvert = _SmartAnalogSystemInputInvert_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 45, 1, 50),
    _SmartAnalogSystemInputInvert_Type()
)
smartAnalogSystemInputInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAnalogSystemInputInvert.setStatus("current")
_AlternativeEnergySource_ObjectIdentity = ObjectIdentity
alternativeEnergySource = _AlternativeEnergySource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 50)
)
if mibBuilder.loadTexts:
    alternativeEnergySource.setStatus("current")
_AlternativeSourceCurrent_Type = Float
_AlternativeSourceCurrent_Object = MibScalar
alternativeSourceCurrent = _AlternativeSourceCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 10, 50, 10),
    _AlternativeSourceCurrent_Type()
)
alternativeSourceCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alternativeSourceCurrent.setStatus("current")
if mibBuilder.loadTexts:
    alternativeSourceCurrent.setUnits("A")
_SystemStates_ObjectIdentity = ObjectIdentity
systemStates = _SystemStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 15)
)
if mibBuilder.loadTexts:
    systemStates.setStatus("current")
_MainsFail_Type = SystemState
_MainsFail_Object = MibScalar
mainsFail = _MainsFail_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 15, 10),
    _MainsFail_Type()
)
mainsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsFail.setStatus("current")
_FanFail_Type = SystemState
_FanFail_Object = MibScalar
fanFail = _FanFail_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 15, 20),
    _FanFail_Type()
)
fanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFail.setStatus("current")
_MovFail_Type = SystemState
_MovFail_Object = MibScalar
movFail = _MovFail_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 15, 30),
    _MovFail_Type()
)
movFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    movFail.setStatus("current")
_LoadFuseFail_Type = SystemState
_LoadFuseFail_Object = MibScalar
loadFuseFail = _LoadFuseFail_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 15, 40),
    _LoadFuseFail_Type()
)
loadFuseFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFuseFail.setStatus("current")
_BatteryFuseFail_Type = SystemState
_BatteryFuseFail_Object = MibScalar
batteryFuseFail = _BatteryFuseFail_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 15, 50),
    _BatteryFuseFail_Type()
)
batteryFuseFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryFuseFail.setStatus("current")
_PhaseFail_Type = SystemState
_PhaseFail_Object = MibScalar
phaseFail = _PhaseFail_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 15, 60),
    _PhaseFail_Type()
)
phaseFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseFail.setStatus("current")
_DigitalInputTable_Object = MibTable
digitalInputTable = _DigitalInputTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40)
)
if mibBuilder.loadTexts:
    digitalInputTable.setStatus("current")
_DigitalInputEntry_Object = MibTableRow
digitalInputEntry = _DigitalInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1)
)
digitalInputEntry.setIndexNames(
    (0, "RpsSc300Mib", "digitalInputIndex"),
)
if mibBuilder.loadTexts:
    digitalInputEntry.setStatus("current")


class _DigitalInputIndex_Type(Unsigned8):
    """Custom type digitalInputIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DigitalInputIndex_Type.__name__ = "Unsigned8"
_DigitalInputIndex_Object = MibTableColumn
digitalInputIndex = _DigitalInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 1),
    _DigitalInputIndex_Type()
)
digitalInputIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    digitalInputIndex.setStatus("current")
_DiState_Type = AlarmActiveState
_DiState_Object = MibTableColumn
diState = _DiState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 20),
    _DiState_Type()
)
diState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diState.setStatus("current")
_DiValue_Type = DigitalInputState
_DiValue_Object = MibTableColumn
diValue = _DiValue_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 30),
    _DiValue_Type()
)
diValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diValue.setStatus("current")


class _DiStatus_Type(EnableState):
    """Custom type diStatus based on EnableState"""
    defaultValue = 0


_DiStatus_Type.__name__ = "EnableState"
_DiStatus_Object = MibTableColumn
diStatus = _DiStatus_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 40),
    _DiStatus_Type()
)
diStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diStatus.setStatus("current")


class _DiName_Type(DisplayString):
    """Custom type diName based on DisplayString"""
    defaultValue = OctetString("Digital Input 1")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DiName_Type.__name__ = "DisplayString"
_DiName_Object = MibTableColumn
diName = _DiName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 50),
    _DiName_Type()
)
diName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diName.setStatus("current")


class _DiIobNumber_Type(Unsigned8):
    """Custom type diIobNumber based on Unsigned8"""
    defaultValue = 1


_DiIobNumber_Type.__name__ = "Unsigned8"
_DiIobNumber_Object = MibTableColumn
diIobNumber = _DiIobNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 60),
    _DiIobNumber_Type()
)
diIobNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diIobNumber.setStatus("current")


class _DigitalInputNumber_Type(Unsigned8):
    """Custom type digitalInputNumber based on Unsigned8"""
    defaultValue = 1


_DigitalInputNumber_Type.__name__ = "Unsigned8"
_DigitalInputNumber_Object = MibTableColumn
digitalInputNumber = _DigitalInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 70),
    _DigitalInputNumber_Type()
)
digitalInputNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInputNumber.setStatus("current")


class _DiSeverity_Type(AlarmSeverity):
    """Custom type diSeverity based on AlarmSeverity"""
    defaultValue = 0


_DiSeverity_Type.__name__ = "AlarmSeverity"
_DiSeverity_Object = MibTableColumn
diSeverity = _DiSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 81),
    _DiSeverity_Type()
)
diSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diSeverity.setStatus("current")


class _DiRecognitionPeriod_Type(TimeIntervalInSeconds):
    """Custom type diRecognitionPeriod based on TimeIntervalInSeconds"""
    defaultValue = 10


_DiRecognitionPeriod_Type.__name__ = "TimeIntervalInSeconds"
_DiRecognitionPeriod_Object = MibTableColumn
diRecognitionPeriod = _DiRecognitionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 85),
    _DiRecognitionPeriod_Type()
)
diRecognitionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diRecognitionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    diRecognitionPeriod.setUnits("s")


class _DiDeactivationRecognitionPeriod_Type(TimeIntervalInSeconds):
    """Custom type diDeactivationRecognitionPeriod based on TimeIntervalInSeconds"""
    defaultValue = 0


_DiDeactivationRecognitionPeriod_Type.__name__ = "TimeIntervalInSeconds"
_DiDeactivationRecognitionPeriod_Object = MibTableColumn
diDeactivationRecognitionPeriod = _DiDeactivationRecognitionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 86),
    _DiDeactivationRecognitionPeriod_Type()
)
diDeactivationRecognitionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diDeactivationRecognitionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    diDeactivationRecognitionPeriod.setUnits("s")


class _DiDoMappingA_Type(RelayMapping):
    """Custom type diDoMappingA based on RelayMapping"""
    defaultValue = 0


_DiDoMappingA_Type.__name__ = "RelayMapping"
_DiDoMappingA_Object = MibTableColumn
diDoMappingA = _DiDoMappingA_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 90),
    _DiDoMappingA_Type()
)
diDoMappingA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diDoMappingA.setStatus("current")


class _DiDoMappingB_Type(RelayMapping):
    """Custom type diDoMappingB based on RelayMapping"""
    defaultValue = 0


_DiDoMappingB_Type.__name__ = "RelayMapping"
_DiDoMappingB_Object = MibTableColumn
diDoMappingB = _DiDoMappingB_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 100),
    _DiDoMappingB_Type()
)
diDoMappingB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diDoMappingB.setStatus("current")


class _DiTrapSend_Type(SendTrap):
    """Custom type diTrapSend based on SendTrap"""
    defaultValue = 1


_DiTrapSend_Type.__name__ = "SendTrap"
_DiTrapSend_Object = MibTableColumn
diTrapSend = _DiTrapSend_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 105),
    _DiTrapSend_Type()
)
diTrapSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diTrapSend.setStatus("current")


class _DiActiveState_Type(ActiveState):
    """Custom type diActiveState based on ActiveState"""
    defaultValue = 2


_DiActiveState_Type.__name__ = "ActiveState"
_DiActiveState_Object = MibTableColumn
diActiveState = _DiActiveState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 110),
    _DiActiveState_Type()
)
diActiveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diActiveState.setStatus("current")


class _DiGroup_Type(Unsigned8):
    """Custom type diGroup based on Unsigned8"""
    defaultValue = 0


_DiGroup_Type.__name__ = "Unsigned8"
_DiGroup_Object = MibTableColumn
diGroup = _DiGroup_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 120),
    _DiGroup_Type()
)
diGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diGroup.setStatus("current")


class _DiNotes_Type(DisplayString):
    """Custom type diNotes based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_DiNotes_Type.__name__ = "DisplayString"
_DiNotes_Object = MibTableColumn
diNotes = _DiNotes_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 40, 1, 130),
    _DiNotes_Type()
)
diNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diNotes.setStatus("current")
_DigitalOutputTable_Object = MibTable
digitalOutputTable = _DigitalOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 50)
)
if mibBuilder.loadTexts:
    digitalOutputTable.setStatus("current")
_DigitalOutputEntry_Object = MibTableRow
digitalOutputEntry = _DigitalOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 50, 1)
)
digitalOutputEntry.setIndexNames(
    (0, "RpsSc300Mib", "digitalOutputIndex"),
)
if mibBuilder.loadTexts:
    digitalOutputEntry.setStatus("current")


class _DigitalOutputIndex_Type(Unsigned8):
    """Custom type digitalOutputIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DigitalOutputIndex_Type.__name__ = "Unsigned8"
_DigitalOutputIndex_Object = MibTableColumn
digitalOutputIndex = _DigitalOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 50, 1, 1),
    _DigitalOutputIndex_Type()
)
digitalOutputIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    digitalOutputIndex.setStatus("current")
_DoState_Type = ExternalRelayState
_DoState_Object = MibTableColumn
doState = _DoState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 50, 1, 20),
    _DoState_Type()
)
doState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doState.setStatus("current")
_RemoteControlState_Type = RelayControlState
_RemoteControlState_Object = MibTableColumn
remoteControlState = _RemoteControlState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 50, 1, 40),
    _RemoteControlState_Type()
)
remoteControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteControlState.setStatus("current")


class _DoStatus_Type(EnableState):
    """Custom type doStatus based on EnableState"""
    defaultValue = 0


_DoStatus_Type.__name__ = "EnableState"
_DoStatus_Object = MibTableColumn
doStatus = _DoStatus_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 50, 1, 50),
    _DoStatus_Type()
)
doStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doStatus.setStatus("current")


class _DoName_Type(DisplayString):
    """Custom type doName based on DisplayString"""
    defaultValue = OctetString("Summary Minor")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DoName_Type.__name__ = "DisplayString"
_DoName_Object = MibTableColumn
doName = _DoName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 50, 1, 60),
    _DoName_Type()
)
doName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doName.setStatus("current")


class _DoIobNumber_Type(Unsigned8):
    """Custom type doIobNumber based on Unsigned8"""
    defaultValue = 1


_DoIobNumber_Type.__name__ = "Unsigned8"
_DoIobNumber_Object = MibTableColumn
doIobNumber = _DoIobNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 50, 1, 70),
    _DoIobNumber_Type()
)
doIobNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doIobNumber.setStatus("current")


class _DoIobDoNumber_Type(Unsigned8):
    """Custom type doIobDoNumber based on Unsigned8"""
    defaultValue = 1


_DoIobDoNumber_Type.__name__ = "Unsigned8"
_DoIobDoNumber_Object = MibTableColumn
doIobDoNumber = _DoIobDoNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 50, 1, 80),
    _DoIobDoNumber_Type()
)
doIobDoNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doIobDoNumber.setStatus("current")


class _DoActiveState_Type(EnergizeState):
    """Custom type doActiveState based on EnergizeState"""
    defaultValue = 1


_DoActiveState_Type.__name__ = "EnergizeState"
_DoActiveState_Object = MibTableColumn
doActiveState = _DoActiveState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 50, 1, 90),
    _DoActiveState_Type()
)
doActiveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doActiveState.setStatus("current")


class _DoGroup_Type(Unsigned8):
    """Custom type doGroup based on Unsigned8"""
    defaultValue = 0


_DoGroup_Type.__name__ = "Unsigned8"
_DoGroup_Object = MibTableColumn
doGroup = _DoGroup_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 50, 1, 100),
    _DoGroup_Type()
)
doGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doGroup.setStatus("current")


class _DoControlTimeoutPeriod_Type(TimeIntervalInMinutes):
    """Custom type doControlTimeoutPeriod based on TimeIntervalInMinutes"""
    defaultValue = 60


_DoControlTimeoutPeriod_Type.__name__ = "TimeIntervalInMinutes"
_DoControlTimeoutPeriod_Object = MibScalar
doControlTimeoutPeriod = _DoControlTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 60),
    _DoControlTimeoutPeriod_Type()
)
doControlTimeoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doControlTimeoutPeriod.setStatus("current")
if mibBuilder.loadTexts:
    doControlTimeoutPeriod.setUnits("min")
_DoControlTimer_Type = TimeIntervalInMinutes
_DoControlTimer_Object = MibScalar
doControlTimer = _DoControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 90, 70),
    _DoControlTimer_Type()
)
doControlTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doControlTimer.setStatus("current")
if mibBuilder.loadTexts:
    doControlTimer.setUnits("min")
_Battery_ObjectIdentity = ObjectIdentity
battery = _Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100)
)
if mibBuilder.loadTexts:
    battery.setStatus("current")


class _BatteryCapacity_Type(Integer32):
    """Custom type batteryCapacity based on Integer32"""
    defaultValue = 100


_BatteryCapacity_Type.__name__ = "Integer32"
_BatteryCapacity_Object = MibScalar
batteryCapacity = _BatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 10),
    _BatteryCapacity_Type()
)
batteryCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    batteryCapacity.setUnits("Ah")


class _CellsPerString_Type(Unsigned8):
    """Custom type cellsPerString based on Unsigned8"""
    defaultValue = 24


_CellsPerString_Type.__name__ = "Unsigned8"
_CellsPerString_Object = MibScalar
cellsPerString = _CellsPerString_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 20),
    _CellsPerString_Type()
)
cellsPerString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cellsPerString.setStatus("current")
_BatteryTemperature_Type = Float
_BatteryTemperature_Object = MibScalar
batteryTemperature = _BatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 30),
    _BatteryTemperature_Type()
)
batteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperature.setStatus("current")
if mibBuilder.loadTexts:
    batteryTemperature.setUnits("°C")
_BatteryCurrent_Type = Float
_BatteryCurrent_Object = MibScalar
batteryCurrent = _BatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 40),
    _BatteryCurrent_Type()
)
batteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    batteryCurrent.setUnits("A")


class _BatteryType_Type(DisplayString):
    """Custom type batteryType based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_BatteryType_Type.__name__ = "DisplayString"
_BatteryType_Object = MibScalar
batteryType = _BatteryType_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 42),
    _BatteryType_Type()
)
batteryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryType.setStatus("current")
_BtrTimeRemaining_Type = TimeIntervalInMinutes
_BtrTimeRemaining_Object = MibScalar
btrTimeRemaining = _BtrTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 43),
    _BtrTimeRemaining_Type()
)
btrTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btrTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    btrTimeRemaining.setUnits("min")


class _BtrStateOfHealth_Type(Percentile8Nan):
    """Custom type btrStateOfHealth based on Percentile8Nan"""
    defaultValue = 255


_BtrStateOfHealth_Type.__name__ = "Percentile8Nan"
_BtrStateOfHealth_Object = MibScalar
btrStateOfHealth = _BtrStateOfHealth_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 44),
    _BtrStateOfHealth_Type()
)
btrStateOfHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btrStateOfHealth.setStatus("current")
if mibBuilder.loadTexts:
    btrStateOfHealth.setUnits("%")
_BatteryChargeState_Type = BatteryChargeState
_BatteryChargeState_Object = MibScalar
batteryChargeState = _BatteryChargeState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 45),
    _BatteryChargeState_Type()
)
batteryChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryChargeState.setStatus("current")


class _BatteryStateThreshold_Type(Float):
    """Custom type batteryStateThreshold based on Float"""
    defaultValue = 20


_BatteryStateThreshold_Type.__name__ = "Float"
_BatteryStateThreshold_Object = MibScalar
batteryStateThreshold = _BatteryStateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 47),
    _BatteryStateThreshold_Type()
)
batteryStateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryStateThreshold.setStatus("current")
if mibBuilder.loadTexts:
    batteryStateThreshold.setUnits("0.1 A")


class _EndOfChargeAction_Type(EndOfChargeAction):
    """Custom type endOfChargeAction based on EndOfChargeAction"""
    defaultValue = 0


_EndOfChargeAction_Type.__name__ = "EndOfChargeAction"
_EndOfChargeAction_Object = MibScalar
endOfChargeAction = _EndOfChargeAction_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 48),
    _EndOfChargeAction_Type()
)
endOfChargeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endOfChargeAction.setStatus("current")
_BatteryDesign_ObjectIdentity = ObjectIdentity
batteryDesign = _BatteryDesign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 49)
)
if mibBuilder.loadTexts:
    batteryDesign.setStatus("current")
_BatteryInstalledDate_Type = JulianDateUtc25
_BatteryInstalledDate_Object = MibScalar
batteryInstalledDate = _BatteryInstalledDate_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 49, 10),
    _BatteryInstalledDate_Type()
)
batteryInstalledDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryInstalledDate.setStatus("current")
_BatteryDesignEndOfLifeDate_Type = JulianDateUtc25
_BatteryDesignEndOfLifeDate_Object = MibScalar
batteryDesignEndOfLifeDate = _BatteryDesignEndOfLifeDate_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 49, 20),
    _BatteryDesignEndOfLifeDate_Type()
)
batteryDesignEndOfLifeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryDesignEndOfLifeDate.setStatus("current")
_MidPointMonitoring_ObjectIdentity = ObjectIdentity
midPointMonitoring = _MidPointMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50)
)
if mibBuilder.loadTexts:
    midPointMonitoring.setStatus("current")


class _BsmLockoutPeriod_Type(TimeIntervalInMinutes):
    """Custom type bsmLockoutPeriod based on TimeIntervalInMinutes"""
    defaultValue = 720


_BsmLockoutPeriod_Type.__name__ = "TimeIntervalInMinutes"
_BsmLockoutPeriod_Object = MibScalar
bsmLockoutPeriod = _BsmLockoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 20),
    _BsmLockoutPeriod_Type()
)
bsmLockoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsmLockoutPeriod.setStatus("current")
if mibBuilder.loadTexts:
    bsmLockoutPeriod.setUnits("min")


class _BsmConvergencePeriod_Type(TimeIntervalInMinutes):
    """Custom type bsmConvergencePeriod based on TimeIntervalInMinutes"""
    defaultValue = 1440


_BsmConvergencePeriod_Type.__name__ = "TimeIntervalInMinutes"
_BsmConvergencePeriod_Object = MibScalar
bsmConvergencePeriod = _BsmConvergencePeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 30),
    _BsmConvergencePeriod_Type()
)
bsmConvergencePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsmConvergencePeriod.setStatus("current")
if mibBuilder.loadTexts:
    bsmConvergencePeriod.setUnits("min")


class _StringFailRecognitionPeriod_Type(TimeIntervalInMinutes):
    """Custom type stringFailRecognitionPeriod based on TimeIntervalInMinutes"""
    defaultValue = 60


_StringFailRecognitionPeriod_Type.__name__ = "TimeIntervalInMinutes"
_StringFailRecognitionPeriod_Object = MibScalar
stringFailRecognitionPeriod = _StringFailRecognitionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 40),
    _StringFailRecognitionPeriod_Type()
)
stringFailRecognitionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stringFailRecognitionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    stringFailRecognitionPeriod.setUnits("min")


class _BsmStartThreshold_Type(Float):
    """Custom type bsmStartThreshold based on Float"""
    defaultValue = 80


_BsmStartThreshold_Type.__name__ = "Float"
_BsmStartThreshold_Object = MibScalar
bsmStartThreshold = _BsmStartThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 50),
    _BsmStartThreshold_Type()
)
bsmStartThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsmStartThreshold.setStatus("current")
if mibBuilder.loadTexts:
    bsmStartThreshold.setUnits("0.1 %")


class _BsmStableThreshold_Type(Float):
    """Custom type bsmStableThreshold based on Float"""
    defaultValue = 40


_BsmStableThreshold_Type.__name__ = "Float"
_BsmStableThreshold_Object = MibScalar
bsmStableThreshold = _BsmStableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 60),
    _BsmStableThreshold_Type()
)
bsmStableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsmStableThreshold.setStatus("current")
if mibBuilder.loadTexts:
    bsmStableThreshold.setUnits("0.1 %")
_MidpointMonitoringStringTable_Object = MibTable
midpointMonitoringStringTable = _MidpointMonitoringStringTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 70)
)
if mibBuilder.loadTexts:
    midpointMonitoringStringTable.setStatus("current")
_MidpointMonitoringStringEntry_Object = MibTableRow
midpointMonitoringStringEntry = _MidpointMonitoringStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 70, 1)
)
midpointMonitoringStringEntry.setIndexNames(
    (0, "RpsSc300Mib", "midpointMonitoringStringIndex"),
)
if mibBuilder.loadTexts:
    midpointMonitoringStringEntry.setStatus("current")


class _MidpointMonitoringStringIndex_Type(Unsigned8):
    """Custom type midpointMonitoringStringIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MidpointMonitoringStringIndex_Type.__name__ = "Unsigned8"
_MidpointMonitoringStringIndex_Object = MibTableColumn
midpointMonitoringStringIndex = _MidpointMonitoringStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 70, 1, 1),
    _MidpointMonitoringStringIndex_Type()
)
midpointMonitoringStringIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    midpointMonitoringStringIndex.setStatus("current")


class _StringName_Type(DisplayString):
    """Custom type stringName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_StringName_Type.__name__ = "DisplayString"
_StringName_Object = MibTableColumn
stringName = _StringName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 70, 1, 10),
    _StringName_Type()
)
stringName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stringName.setStatus("current")
_StringState_Type = BsmBatteryState
_StringState_Object = MibTableColumn
stringState = _StringState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 70, 1, 20),
    _StringState_Type()
)
stringState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stringState.setStatus("current")
_FirstQuarterPointVoltage_Type = Float
_FirstQuarterPointVoltage_Object = MibTableColumn
firstQuarterPointVoltage = _FirstQuarterPointVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 70, 1, 25),
    _FirstQuarterPointVoltage_Type()
)
firstQuarterPointVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firstQuarterPointVoltage.setStatus("current")
if mibBuilder.loadTexts:
    firstQuarterPointVoltage.setUnits("0.01 V")
_MidPointVoltage_Type = Float
_MidPointVoltage_Object = MibTableColumn
midPointVoltage = _MidPointVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 70, 1, 30),
    _MidPointVoltage_Type()
)
midPointVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    midPointVoltage.setStatus("current")
if mibBuilder.loadTexts:
    midPointVoltage.setUnits("0.01 V")
_ThirdQuarterPointVoltage_Type = Float
_ThirdQuarterPointVoltage_Object = MibTableColumn
thirdQuarterPointVoltage = _ThirdQuarterPointVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 70, 1, 35),
    _ThirdQuarterPointVoltage_Type()
)
thirdQuarterPointVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thirdQuarterPointVoltage.setStatus("current")
if mibBuilder.loadTexts:
    thirdQuarterPointVoltage.setUnits("0.01 V")
_ImbalancePercent_Type = Float
_ImbalancePercent_Object = MibTableColumn
imbalancePercent = _ImbalancePercent_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 70, 1, 40),
    _ImbalancePercent_Type()
)
imbalancePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imbalancePercent.setStatus("current")
if mibBuilder.loadTexts:
    imbalancePercent.setUnits("0.1 %")
_BsmState_Type = BsmState
_BsmState_Object = MibScalar
bsmState = _BsmState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 80),
    _BsmState_Type()
)
bsmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsmState.setStatus("current")
_TimeInThisState_Type = TimeIntervalInMinutes
_TimeInThisState_Object = MibScalar
timeInThisState = _TimeInThisState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 90),
    _TimeInThisState_Type()
)
timeInThisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeInThisState.setStatus("current")
if mibBuilder.loadTexts:
    timeInThisState.setUnits("min")
_CurrentBsmThreshold_Type = Float
_CurrentBsmThreshold_Object = MibScalar
currentBsmThreshold = _CurrentBsmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 100),
    _CurrentBsmThreshold_Type()
)
currentBsmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentBsmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    currentBsmThreshold.setUnits("0.1 %")
_ReferenceVoltage_Type = Float
_ReferenceVoltage_Object = MibScalar
referenceVoltage = _ReferenceVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 105),
    _ReferenceVoltage_Type()
)
referenceVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    referenceVoltage.setStatus("current")
if mibBuilder.loadTexts:
    referenceVoltage.setUnits("0.01 V")
_ClearStringFail_Type = NoData
_ClearStringFail_Object = MibScalar
clearStringFail = _ClearStringFail_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 50, 110),
    _ClearStringFail_Type()
)
clearStringFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearStringFail.setStatus("current")
_BatteryTimeRemaining_ObjectIdentity = ObjectIdentity
batteryTimeRemaining = _BatteryTimeRemaining_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 60)
)
if mibBuilder.loadTexts:
    batteryTimeRemaining.setStatus("current")
_BtrState_Type = BtrState
_BtrState_Object = MibScalar
btrState = _BtrState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 60, 10),
    _BtrState_Type()
)
btrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btrState.setStatus("current")


class _BtrEndVoltage_Type(Float):
    """Custom type btrEndVoltage based on Float"""
    defaultValue = 180


_BtrEndVoltage_Type.__name__ = "Float"
_BtrEndVoltage_Object = MibScalar
btrEndVoltage = _BtrEndVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 60, 20),
    _BtrEndVoltage_Type()
)
btrEndVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btrEndVoltage.setStatus("current")
if mibBuilder.loadTexts:
    btrEndVoltage.setUnits("0.01 V/Cell")
_BtrCharacterizationEndVoltage_Type = Float
_BtrCharacterizationEndVoltage_Object = MibScalar
btrCharacterizationEndVoltage = _BtrCharacterizationEndVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 60, 30),
    _BtrCharacterizationEndVoltage_Type()
)
btrCharacterizationEndVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btrCharacterizationEndVoltage.setStatus("current")
if mibBuilder.loadTexts:
    btrCharacterizationEndVoltage.setUnits("0.01 V/Cell")
_BtrCharacterizationResult_Type = BtrCharacterizationResult
_BtrCharacterizationResult_Object = MibScalar
btrCharacterizationResult = _BtrCharacterizationResult_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 60, 40),
    _BtrCharacterizationResult_Type()
)
btrCharacterizationResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btrCharacterizationResult.setStatus("current")
_BtrCharacterizationTime_Type = JulianDateUtc25
_BtrCharacterizationTime_Object = MibScalar
btrCharacterizationTime = _BtrCharacterizationTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 60, 50),
    _BtrCharacterizationTime_Type()
)
btrCharacterizationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btrCharacterizationTime.setStatus("current")


class _BtrAutomaticCharacterization_Type(EnableState):
    """Custom type btrAutomaticCharacterization based on EnableState"""
    defaultValue = 0


_BtrAutomaticCharacterization_Type.__name__ = "EnableState"
_BtrAutomaticCharacterization_Object = MibScalar
btrAutomaticCharacterization = _BtrAutomaticCharacterization_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 60, 60),
    _BtrAutomaticCharacterization_Type()
)
btrAutomaticCharacterization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btrAutomaticCharacterization.setStatus("current")


class _BtrCharacterizationDelay_Type(TimeIntervalInMinutes):
    """Custom type btrCharacterizationDelay based on TimeIntervalInMinutes"""
    defaultValue = 2880


_BtrCharacterizationDelay_Type.__name__ = "TimeIntervalInMinutes"
_BtrCharacterizationDelay_Object = MibScalar
btrCharacterizationDelay = _BtrCharacterizationDelay_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 60, 70),
    _BtrCharacterizationDelay_Type()
)
btrCharacterizationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btrCharacterizationDelay.setStatus("current")
if mibBuilder.loadTexts:
    btrCharacterizationDelay.setUnits("min")
_BtrCharacterizationStart_Type = TimeIntervalInSeconds
_BtrCharacterizationStart_Object = MibScalar
btrCharacterizationStart = _BtrCharacterizationStart_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 60, 80),
    _BtrCharacterizationStart_Type()
)
btrCharacterizationStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btrCharacterizationStart.setStatus("current")
if mibBuilder.loadTexts:
    btrCharacterizationStart.setUnits("s")
_BtrCharacterizeBattery_Type = NoData
_BtrCharacterizeBattery_Object = MibScalar
btrCharacterizeBattery = _BtrCharacterizeBattery_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 60, 90),
    _BtrCharacterizeBattery_Type()
)
btrCharacterizeBattery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btrCharacterizeBattery.setStatus("current")
_BtrStopBatteryCharacterization_Type = NoData
_BtrStopBatteryCharacterization_Object = MibScalar
btrStopBatteryCharacterization = _BtrStopBatteryCharacterization_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 60, 100),
    _BtrStopBatteryCharacterization_Type()
)
btrStopBatteryCharacterization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btrStopBatteryCharacterization.setStatus("current")
_BtrCancelWaiting_Type = NoData
_BtrCancelWaiting_Object = MibScalar
btrCancelWaiting = _BtrCancelWaiting_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 60, 105),
    _BtrCancelWaiting_Type()
)
btrCancelWaiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btrCancelWaiting.setStatus("current")
_BtrClearBatteryCharacterization_Type = NoData
_BtrClearBatteryCharacterization_Object = MibScalar
btrClearBatteryCharacterization = _BtrClearBatteryCharacterization_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 60, 110),
    _BtrClearBatteryCharacterization_Type()
)
btrClearBatteryCharacterization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    btrClearBatteryCharacterization.setStatus("current")
_BatteryCharacterizationInstantaneousQuality_Type = Percentile8Nan
_BatteryCharacterizationInstantaneousQuality_Object = MibScalar
batteryCharacterizationInstantaneousQuality = _BatteryCharacterizationInstantaneousQuality_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 60, 120),
    _BatteryCharacterizationInstantaneousQuality_Type()
)
batteryCharacterizationInstantaneousQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCharacterizationInstantaneousQuality.setStatus("current")
if mibBuilder.loadTexts:
    batteryCharacterizationInstantaneousQuality.setUnits("%")
_BatteryCharacterizationDataTable_Object = MibTable
batteryCharacterizationDataTable = _BatteryCharacterizationDataTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 62)
)
if mibBuilder.loadTexts:
    batteryCharacterizationDataTable.setStatus("current")
_BatteryCharacterizationDataEntry_Object = MibTableRow
batteryCharacterizationDataEntry = _BatteryCharacterizationDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 62, 1)
)
batteryCharacterizationDataEntry.setIndexNames(
    (0, "RpsSc300Mib", "batteryCharacterizationDataIndex"),
)
if mibBuilder.loadTexts:
    batteryCharacterizationDataEntry.setStatus("current")


class _BatteryCharacterizationDataIndex_Type(Unsigned8):
    """Custom type batteryCharacterizationDataIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BatteryCharacterizationDataIndex_Type.__name__ = "Unsigned8"
_BatteryCharacterizationDataIndex_Object = MibTableColumn
batteryCharacterizationDataIndex = _BatteryCharacterizationDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 62, 1, 1),
    _BatteryCharacterizationDataIndex_Type()
)
batteryCharacterizationDataIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryCharacterizationDataIndex.setStatus("current")


class _BatteryCharacterizationSample_Type(Float):
    """Custom type batteryCharacterizationSample based on Float"""
    defaultValue = 0


_BatteryCharacterizationSample_Type.__name__ = "Float"
_BatteryCharacterizationSample_Object = MibTableColumn
batteryCharacterizationSample = _BatteryCharacterizationSample_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 62, 1, 10),
    _BatteryCharacterizationSample_Type()
)
batteryCharacterizationSample.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCharacterizationSample.setStatus("current")
if mibBuilder.loadTexts:
    batteryCharacterizationSample.setUnits("0.01")


class _BatteryCharacterizationTime_Type(TimeIntervalInMinutes):
    """Custom type batteryCharacterizationTime based on TimeIntervalInMinutes"""
    defaultValue = 0


_BatteryCharacterizationTime_Type.__name__ = "TimeIntervalInMinutes"
_BatteryCharacterizationTime_Object = MibTableColumn
batteryCharacterizationTime = _BatteryCharacterizationTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 62, 1, 20),
    _BatteryCharacterizationTime_Type()
)
batteryCharacterizationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCharacterizationTime.setStatus("current")
if mibBuilder.loadTexts:
    batteryCharacterizationTime.setUnits("min")
_SiteBackupTimeSettings_ObjectIdentity = ObjectIdentity
siteBackupTimeSettings = _SiteBackupTimeSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 65)
)
if mibBuilder.loadTexts:
    siteBackupTimeSettings.setStatus("current")
_SiteBackupTimeRemaining_Type = TimeIntervalInMinutes
_SiteBackupTimeRemaining_Object = MibScalar
siteBackupTimeRemaining = _SiteBackupTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 65, 10),
    _SiteBackupTimeRemaining_Type()
)
siteBackupTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteBackupTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    siteBackupTimeRemaining.setUnits("min")


class _SiteBackupTime_Type(TimeIntervalInMinutes):
    """Custom type siteBackupTime based on TimeIntervalInMinutes"""
    defaultValue = 0


_SiteBackupTime_Type.__name__ = "TimeIntervalInMinutes"
_SiteBackupTime_Object = MibScalar
siteBackupTime = _SiteBackupTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 100, 65, 20),
    _SiteBackupTime_Type()
)
siteBackupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteBackupTime.setStatus("current")
if mibBuilder.loadTexts:
    siteBackupTime.setUnits("min")
_Solar_ObjectIdentity = ObjectIdentity
solar = _Solar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 105)
)
if mibBuilder.loadTexts:
    solar.setStatus("current")
_DcInputVoltage_Type = Float
_DcInputVoltage_Object = MibScalar
dcInputVoltage = _DcInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 105, 10),
    _DcInputVoltage_Type()
)
dcInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcInputVoltage.setUnits("0.01 V")


class _SolarPowerShareOffset_Type(Float):
    """Custom type solarPowerShareOffset based on Float"""
    defaultValue = 25


_SolarPowerShareOffset_Type.__name__ = "Float"
_SolarPowerShareOffset_Object = MibScalar
solarPowerShareOffset = _SolarPowerShareOffset_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 105, 20),
    _SolarPowerShareOffset_Type()
)
solarPowerShareOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarPowerShareOffset.setStatus("current")
if mibBuilder.loadTexts:
    solarPowerShareOffset.setUnits("0.01 V")
_SolarPower_Type = Float
_SolarPower_Object = MibScalar
solarPower = _SolarPower_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 105, 30),
    _SolarPower_Type()
)
solarPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarPower.setStatus("current")
if mibBuilder.loadTexts:
    solarPower.setUnits("0.01 kW")
_SolarCurrent_Type = Float
_SolarCurrent_Object = MibScalar
solarCurrent = _SolarCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 105, 40),
    _SolarCurrent_Type()
)
solarCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarCurrent.setStatus("current")
if mibBuilder.loadTexts:
    solarCurrent.setUnits("A")
_SolarBaseVoltage_Type = Float
_SolarBaseVoltage_Object = MibScalar
solarBaseVoltage = _SolarBaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 105, 50),
    _SolarBaseVoltage_Type()
)
solarBaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarBaseVoltage.setStatus("current")
if mibBuilder.loadTexts:
    solarBaseVoltage.setUnits("0.01 V")


class _SolarShutdownSmartAlarm_Type(Unsigned8):
    """Custom type solarShutdownSmartAlarm based on Unsigned8"""
    defaultValue = 0


_SolarShutdownSmartAlarm_Type.__name__ = "Unsigned8"
_SolarShutdownSmartAlarm_Object = MibScalar
solarShutdownSmartAlarm = _SolarShutdownSmartAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 105, 60),
    _SolarShutdownSmartAlarm_Type()
)
solarShutdownSmartAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarShutdownSmartAlarm.setStatus("current")
_Dcdc_ObjectIdentity = ObjectIdentity
dcdc = _Dcdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106)
)
if mibBuilder.loadTexts:
    dcdc.setStatus("current")
_DcdcType_Type = DcdcHardwareType
_DcdcType_Object = MibScalar
dcdcType = _DcdcType_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 10),
    _DcdcType_Type()
)
dcdcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcType.setStatus("current")
_DcdcVoltage_Type = Float
_DcdcVoltage_Object = MibScalar
dcdcVoltage = _DcdcVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 20),
    _DcdcVoltage_Type()
)
dcdcVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcdcVoltage.setUnits("0.01 V")
_DcdcCurrent_Type = Float
_DcdcCurrent_Object = MibScalar
dcdcCurrent = _DcdcCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 30),
    _DcdcCurrent_Type()
)
dcdcCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dcdcCurrent.setUnits("A")
_DcdcPower_Type = DcPower
_DcdcPower_Object = MibScalar
dcdcPower = _DcdcPower_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 40),
    _DcdcPower_Type()
)
dcdcPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcPower.setStatus("current")
if mibBuilder.loadTexts:
    dcdcPower.setUnits("W")
_DcdcHeatsinkTemperature_Type = Float
_DcdcHeatsinkTemperature_Object = MibScalar
dcdcHeatsinkTemperature = _DcdcHeatsinkTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 50),
    _DcdcHeatsinkTemperature_Type()
)
dcdcHeatsinkTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcHeatsinkTemperature.setStatus("current")
if mibBuilder.loadTexts:
    dcdcHeatsinkTemperature.setUnits("°C")
_NumberOfRegisteredDcdcConverters_Type = Unsigned8
_NumberOfRegisteredDcdcConverters_Object = MibScalar
numberOfRegisteredDcdcConverters = _NumberOfRegisteredDcdcConverters_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 60),
    _NumberOfRegisteredDcdcConverters_Type()
)
numberOfRegisteredDcdcConverters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfRegisteredDcdcConverters.setStatus("current")
_DcdcOutputVoltageSetpoint_Type = Float
_DcdcOutputVoltageSetpoint_Object = MibScalar
dcdcOutputVoltageSetpoint = _DcdcOutputVoltageSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 70),
    _DcdcOutputVoltageSetpoint_Type()
)
dcdcOutputVoltageSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcOutputVoltageSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    dcdcOutputVoltageSetpoint.setUnits("0.01 V")


class _Dcdc12vOutputVoltageSetpoint_Type(Float):
    """Custom type dcdc12vOutputVoltageSetpoint based on Float"""
    defaultValue = 1375


_Dcdc12vOutputVoltageSetpoint_Type.__name__ = "Float"
_Dcdc12vOutputVoltageSetpoint_Object = MibScalar
dcdc12vOutputVoltageSetpoint = _Dcdc12vOutputVoltageSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 80),
    _Dcdc12vOutputVoltageSetpoint_Type()
)
dcdc12vOutputVoltageSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdc12vOutputVoltageSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    dcdc12vOutputVoltageSetpoint.setUnits("0.01 V")


class _Dcdc24vOutputVoltageSetpoint_Type(Float):
    """Custom type dcdc24vOutputVoltageSetpoint based on Float"""
    defaultValue = 2733


_Dcdc24vOutputVoltageSetpoint_Type.__name__ = "Float"
_Dcdc24vOutputVoltageSetpoint_Object = MibScalar
dcdc24vOutputVoltageSetpoint = _Dcdc24vOutputVoltageSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 90),
    _Dcdc24vOutputVoltageSetpoint_Type()
)
dcdc24vOutputVoltageSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdc24vOutputVoltageSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    dcdc24vOutputVoltageSetpoint.setUnits("0.01 V")


class _Dcdc48vOutputVoltageSetpoint_Type(Float):
    """Custom type dcdc48vOutputVoltageSetpoint based on Float"""
    defaultValue = 5440


_Dcdc48vOutputVoltageSetpoint_Type.__name__ = "Float"
_Dcdc48vOutputVoltageSetpoint_Object = MibScalar
dcdc48vOutputVoltageSetpoint = _Dcdc48vOutputVoltageSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 100),
    _Dcdc48vOutputVoltageSetpoint_Type()
)
dcdc48vOutputVoltageSetpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdc48vOutputVoltageSetpoint.setStatus("current")
if mibBuilder.loadTexts:
    dcdc48vOutputVoltageSetpoint.setUnits("0.01 V")
_DcdcCurrentLimit_Type = Float
_DcdcCurrentLimit_Object = MibScalar
dcdcCurrentLimit = _DcdcCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 110),
    _DcdcCurrentLimit_Type()
)
dcdcCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcdcCurrentLimit.setUnits("0.01 A")


class _Dcdc12vCurrentLimit_Type(Float):
    """Custom type dcdc12vCurrentLimit based on Float"""
    defaultValue = 2200


_Dcdc12vCurrentLimit_Type.__name__ = "Float"
_Dcdc12vCurrentLimit_Object = MibScalar
dcdc12vCurrentLimit = _Dcdc12vCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 120),
    _Dcdc12vCurrentLimit_Type()
)
dcdc12vCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdc12vCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcdc12vCurrentLimit.setUnits("0.01 A")


class _Dcdc24vCurrentLimit_Type(Float):
    """Custom type dcdc24vCurrentLimit based on Float"""
    defaultValue = 1100


_Dcdc24vCurrentLimit_Type.__name__ = "Float"
_Dcdc24vCurrentLimit_Object = MibScalar
dcdc24vCurrentLimit = _Dcdc24vCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 130),
    _Dcdc24vCurrentLimit_Type()
)
dcdc24vCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdc24vCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcdc24vCurrentLimit.setUnits("0.01 A")


class _Dcdc48vCurrentLimit_Type(Float):
    """Custom type dcdc48vCurrentLimit based on Float"""
    defaultValue = 550


_Dcdc48vCurrentLimit_Type.__name__ = "Float"
_Dcdc48vCurrentLimit_Object = MibScalar
dcdc48vCurrentLimit = _Dcdc48vCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 140),
    _Dcdc48vCurrentLimit_Type()
)
dcdc48vCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdc48vCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcdc48vCurrentLimit.setUnits("0.01 A")


class _DcdcInputVoltageItem_Type(DisplayString):
    """Custom type dcdcInputVoltageItem based on DisplayString"""
    defaultValue = OctetString("Bus-Voltage")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DcdcInputVoltageItem_Type.__name__ = "DisplayString"
_DcdcInputVoltageItem_Object = MibScalar
dcdcInputVoltageItem = _DcdcInputVoltageItem_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 150),
    _DcdcInputVoltageItem_Type()
)
dcdcInputVoltageItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcInputVoltageItem.setStatus("current")
_DcdcInputVoltage_Type = Float
_DcdcInputVoltage_Object = MibScalar
dcdcInputVoltage = _DcdcInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 106, 160),
    _DcdcInputVoltage_Type()
)
dcdcInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcdcInputVoltage.setUnits("0.01 V")
_Log_ObjectIdentity = ObjectIdentity
log = _Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 107)
)
if mibBuilder.loadTexts:
    log.setStatus("current")
_LogFillMonths_Type = Unsigned16
_LogFillMonths_Object = MibScalar
logFillMonths = _LogFillMonths_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 107, 10),
    _LogFillMonths_Type()
)
logFillMonths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFillMonths.setStatus("current")
_LogUsed_Type = Integer32
_LogUsed_Object = MibScalar
logUsed = _LogUsed_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 107, 20),
    _LogUsed_Type()
)
logUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logUsed.setStatus("current")
_LogItemsTable_Object = MibTable
logItemsTable = _LogItemsTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 107, 40)
)
if mibBuilder.loadTexts:
    logItemsTable.setStatus("current")
_LogItemsEntry_Object = MibTableRow
logItemsEntry = _LogItemsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 107, 40, 1)
)
logItemsEntry.setIndexNames(
    (0, "RpsSc300Mib", "logItemsIndex"),
)
if mibBuilder.loadTexts:
    logItemsEntry.setStatus("current")
_LogItemsIndex_Type = LogItems
_LogItemsIndex_Object = MibTableColumn
logItemsIndex = _LogItemsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 107, 40, 1, 1),
    _LogItemsIndex_Type()
)
logItemsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    logItemsIndex.setStatus("current")


class _LogInterval_Type(TimeIntervalInSeconds):
    """Custom type logInterval based on TimeIntervalInSeconds"""
    defaultValue = 1800


_LogInterval_Type.__name__ = "TimeIntervalInSeconds"
_LogInterval_Object = MibTableColumn
logInterval = _LogInterval_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 107, 40, 1, 10),
    _LogInterval_Type()
)
logInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logInterval.setStatus("current")
if mibBuilder.loadTexts:
    logInterval.setUnits("s")


class _UseOffNormal_Type(Boolean):
    """Custom type useOffNormal based on Boolean"""
    defaultValue = 0


_UseOffNormal_Type.__name__ = "Boolean"
_UseOffNormal_Object = MibTableColumn
useOffNormal = _UseOffNormal_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 107, 40, 1, 20),
    _UseOffNormal_Type()
)
useOffNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useOffNormal.setStatus("current")
_LogNumberOfEntries_Type = Unsigned16
_LogNumberOfEntries_Object = MibTableColumn
logNumberOfEntries = _LogNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 107, 40, 1, 30),
    _LogNumberOfEntries_Type()
)
logNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logNumberOfEntries.setStatus("current")


class _OffNormalInterval_Type(TimeIntervalInSeconds):
    """Custom type offNormalInterval based on TimeIntervalInSeconds"""
    defaultValue = 60


_OffNormalInterval_Type.__name__ = "TimeIntervalInSeconds"
_OffNormalInterval_Object = MibScalar
offNormalInterval = _OffNormalInterval_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 107, 50),
    _OffNormalInterval_Type()
)
offNormalInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offNormalInterval.setStatus("current")
if mibBuilder.loadTexts:
    offNormalInterval.setUnits("s")


class _OffNormalOffsetVoltage_Type(Float):
    """Custom type offNormalOffsetVoltage based on Float"""
    defaultValue = 400


_OffNormalOffsetVoltage_Type.__name__ = "Float"
_OffNormalOffsetVoltage_Object = MibScalar
offNormalOffsetVoltage = _OffNormalOffsetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 107, 60),
    _OffNormalOffsetVoltage_Type()
)
offNormalOffsetVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offNormalOffsetVoltage.setStatus("current")
if mibBuilder.loadTexts:
    offNormalOffsetVoltage.setUnits("0.01 V")


class _OffNormalSmartAlarm_Type(Unsigned8):
    """Custom type offNormalSmartAlarm based on Unsigned8"""
    defaultValue = 0


_OffNormalSmartAlarm_Type.__name__ = "Unsigned8"
_OffNormalSmartAlarm_Object = MibScalar
offNormalSmartAlarm = _OffNormalSmartAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 107, 70),
    _OffNormalSmartAlarm_Type()
)
offNormalSmartAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offNormalSmartAlarm.setStatus("current")
_IsOffNormal_Type = Boolean
_IsOffNormal_Object = MibScalar
isOffNormal = _IsOffNormal_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 107, 80),
    _IsOffNormal_Type()
)
isOffNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isOffNormal.setStatus("current")
_Internal_ObjectIdentity = ObjectIdentity
internal = _Internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 108)
)
if mibBuilder.loadTexts:
    internal.setStatus("current")
_ThreadLoadingTable_Object = MibTable
threadLoadingTable = _ThreadLoadingTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 108, 10)
)
if mibBuilder.loadTexts:
    threadLoadingTable.setStatus("current")
_ThreadLoadingEntry_Object = MibTableRow
threadLoadingEntry = _ThreadLoadingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 108, 10, 1)
)
threadLoadingEntry.setIndexNames(
    (0, "RpsSc300Mib", "threadLoadingIndex"),
)
if mibBuilder.loadTexts:
    threadLoadingEntry.setStatus("current")


class _ThreadLoadingIndex_Type(Unsigned16):
    """Custom type threadLoadingIndex based on Unsigned16"""
    subtypeSpec = Unsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ThreadLoadingIndex_Type.__name__ = "Unsigned16"
_ThreadLoadingIndex_Object = MibTableColumn
threadLoadingIndex = _ThreadLoadingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 108, 10, 1, 1),
    _ThreadLoadingIndex_Type()
)
threadLoadingIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    threadLoadingIndex.setStatus("current")


class _ThreadName_Type(DisplayString):
    """Custom type threadName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ThreadName_Type.__name__ = "DisplayString"
_ThreadName_Object = MibTableColumn
threadName = _ThreadName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 108, 10, 1, 20),
    _ThreadName_Type()
)
threadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threadName.setStatus("current")
_ThreadLoading_Type = Float
_ThreadLoading_Object = MibTableColumn
threadLoading = _ThreadLoading_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 108, 10, 1, 30),
    _ThreadLoading_Type()
)
threadLoading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threadLoading.setStatus("current")
if mibBuilder.loadTexts:
    threadLoading.setUnits("0.1 %")
_ThreadPriority_Type = ThreadPriority
_ThreadPriority_Object = MibTableColumn
threadPriority = _ThreadPriority_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 108, 10, 1, 40),
    _ThreadPriority_Type()
)
threadPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threadPriority.setStatus("current")
_ThreadStack_Type = Integer32
_ThreadStack_Object = MibTableColumn
threadStack = _ThreadStack_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 108, 10, 1, 50),
    _ThreadStack_Type()
)
threadStack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threadStack.setStatus("current")
if mibBuilder.loadTexts:
    threadStack.setUnits("B")
_ThreadHeap_Type = Integer32
_ThreadHeap_Object = MibTableColumn
threadHeap = _ThreadHeap_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 108, 10, 1, 60),
    _ThreadHeap_Type()
)
threadHeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threadHeap.setStatus("current")
if mibBuilder.loadTexts:
    threadHeap.setUnits("B")
_ThreadHighWaterMark_Type = Integer32
_ThreadHighWaterMark_Object = MibTableColumn
threadHighWaterMark = _ThreadHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 108, 10, 1, 70),
    _ThreadHighWaterMark_Type()
)
threadHighWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threadHighWaterMark.setStatus("current")
if mibBuilder.loadTexts:
    threadHighWaterMark.setUnits("B")
_Preemptive_Type = Unsigned8
_Preemptive_Object = MibScalar
preemptive = _Preemptive_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 108, 20),
    _Preemptive_Type()
)
preemptive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preemptive.setStatus("current")
if mibBuilder.loadTexts:
    preemptive.setUnits("%")
_RamFree_Type = Float
_RamFree_Object = MibScalar
ramFree = _RamFree_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 108, 30),
    _RamFree_Type()
)
ramFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ramFree.setStatus("current")
if mibBuilder.loadTexts:
    ramFree.setUnits("0.01 kB")
_RamHeap_Type = Float
_RamHeap_Object = MibScalar
ramHeap = _RamHeap_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 108, 40),
    _RamHeap_Type()
)
ramHeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ramHeap.setStatus("current")
if mibBuilder.loadTexts:
    ramHeap.setUnits("0.01 kB")
_RamStack_Type = Float
_RamStack_Object = MibScalar
ramStack = _RamStack_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 108, 50),
    _RamStack_Type()
)
ramStack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ramStack.setStatus("current")
if mibBuilder.loadTexts:
    ramStack.setUnits("0.01 kB")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110)
)
if mibBuilder.loadTexts:
    alarms.setStatus("current")
_AlarmStates_ObjectIdentity = ObjectIdentity
alarmStates = _AlarmStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 5)
)
if mibBuilder.loadTexts:
    alarmStates.setStatus("current")
_SummaryAlarmCritical_Type = Boolean
_SummaryAlarmCritical_Object = MibScalar
summaryAlarmCritical = _SummaryAlarmCritical_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 5, 10),
    _SummaryAlarmCritical_Type()
)
summaryAlarmCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryAlarmCritical.setStatus("current")
_SummaryAlarmMajor_Type = Boolean
_SummaryAlarmMajor_Object = MibScalar
summaryAlarmMajor = _SummaryAlarmMajor_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 5, 20),
    _SummaryAlarmMajor_Type()
)
summaryAlarmMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryAlarmMajor.setStatus("current")
_SummaryAlarmMinor_Type = Boolean
_SummaryAlarmMinor_Object = MibScalar
summaryAlarmMinor = _SummaryAlarmMinor_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 5, 30),
    _SummaryAlarmMinor_Type()
)
summaryAlarmMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryAlarmMinor.setStatus("current")
_ResetBatteryTestFailedAlarm_Type = NoData
_ResetBatteryTestFailedAlarm_Object = MibScalar
resetBatteryTestFailedAlarm = _ResetBatteryTestFailedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 5, 100),
    _ResetBatteryTestFailedAlarm_Type()
)
resetBatteryTestFailedAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetBatteryTestFailedAlarm.setStatus("current")
_ResetCommsLostAlarm_Type = NoData
_ResetCommsLostAlarm_Object = MibScalar
resetCommsLostAlarm = _ResetCommsLostAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 5, 110),
    _ResetCommsLostAlarm_Type()
)
resetCommsLostAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetCommsLostAlarm.setStatus("current")
_ResetBatteryTestCancelledAlarm_Type = NoData
_ResetBatteryTestCancelledAlarm_Object = MibScalar
resetBatteryTestCancelledAlarm = _ResetBatteryTestCancelledAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 5, 115),
    _ResetBatteryTestCancelledAlarm_Type()
)
resetBatteryTestCancelledAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetBatteryTestCancelledAlarm.setStatus("current")
_ResetLowRectifierCapacityAlarm_Type = NoData
_ResetLowRectifierCapacityAlarm_Object = MibScalar
resetLowRectifierCapacityAlarm = _ResetLowRectifierCapacityAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 5, 117),
    _ResetLowRectifierCapacityAlarm_Type()
)
resetLowRectifierCapacityAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetLowRectifierCapacityAlarm.setStatus("current")


class _AlarmInfo_Type(DisplayString):
    """Custom type alarmInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AlarmInfo_Type.__name__ = "DisplayString"
_AlarmInfo_Object = MibScalar
alarmInfo = _AlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 5, 130),
    _AlarmInfo_Type()
)
alarmInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmInfo.setStatus("current")
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 10)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 10, 1)
)
alarmEntry.setIndexNames(
    (0, "RpsSc300Mib", "alarmIndex"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")
_AlarmIndex_Type = SystemAlarm
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 10, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")


class _AlarmName_Type(DisplayString):
    """Custom type alarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AlarmName_Type.__name__ = "DisplayString"
_AlarmName_Object = MibTableColumn
alarmName = _AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 10, 1, 20),
    _AlarmName_Type()
)
alarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmName.setStatus("current")


class _AlarmSeverity_Type(AlarmSeverity):
    """Custom type alarmSeverity based on AlarmSeverity"""
    defaultValue = 2


_AlarmSeverity_Type.__name__ = "AlarmSeverity"
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 10, 1, 31),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmState_Type = AlarmActiveState
_AlarmState_Object = MibTableColumn
alarmState = _AlarmState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 10, 1, 40),
    _AlarmState_Type()
)
alarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmState.setStatus("current")


class _AlarmNotes_Type(DisplayString):
    """Custom type alarmNotes based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AlarmNotes_Type.__name__ = "DisplayString"
_AlarmNotes_Object = MibTableColumn
alarmNotes = _AlarmNotes_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 10, 1, 50),
    _AlarmNotes_Type()
)
alarmNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmNotes.setStatus("current")


class _AlarmDoMappingA_Type(RelayMapping):
    """Custom type alarmDoMappingA based on RelayMapping"""
    defaultValue = 0


_AlarmDoMappingA_Type.__name__ = "RelayMapping"
_AlarmDoMappingA_Object = MibTableColumn
alarmDoMappingA = _AlarmDoMappingA_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 10, 1, 60),
    _AlarmDoMappingA_Type()
)
alarmDoMappingA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmDoMappingA.setStatus("current")


class _AlarmDoMappingB_Type(RelayMapping):
    """Custom type alarmDoMappingB based on RelayMapping"""
    defaultValue = 0


_AlarmDoMappingB_Type.__name__ = "RelayMapping"
_AlarmDoMappingB_Object = MibTableColumn
alarmDoMappingB = _AlarmDoMappingB_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 10, 1, 70),
    _AlarmDoMappingB_Type()
)
alarmDoMappingB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmDoMappingB.setStatus("current")


class _AlarmTrapSend_Type(SendTrap):
    """Custom type alarmTrapSend based on SendTrap"""
    defaultValue = 1


_AlarmTrapSend_Type.__name__ = "SendTrap"
_AlarmTrapSend_Object = MibTableColumn
alarmTrapSend = _AlarmTrapSend_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 10, 1, 80),
    _AlarmTrapSend_Type()
)
alarmTrapSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTrapSend.setStatus("current")
_AlarmStateChangeTime_Type = JulianDateUtc25
_AlarmStateChangeTime_Object = MibTableColumn
alarmStateChangeTime = _AlarmStateChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 10, 1, 90),
    _AlarmStateChangeTime_Type()
)
alarmStateChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStateChangeTime.setStatus("current")
_AlarmConfiguration_ObjectIdentity = ObjectIdentity
alarmConfiguration = _AlarmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15)
)
if mibBuilder.loadTexts:
    alarmConfiguration.setStatus("current")


class _EnableAudibleAlarmIndication_Type(EnableState):
    """Custom type enableAudibleAlarmIndication based on EnableState"""
    defaultValue = 1


_EnableAudibleAlarmIndication_Type.__name__ = "EnableState"
_EnableAudibleAlarmIndication_Object = MibScalar
enableAudibleAlarmIndication = _EnableAudibleAlarmIndication_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 10),
    _EnableAudibleAlarmIndication_Type()
)
enableAudibleAlarmIndication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableAudibleAlarmIndication.setStatus("current")


class _AlarmRecognitionPeriod_Type(TimeIntervalInSeconds):
    """Custom type alarmRecognitionPeriod based on TimeIntervalInSeconds"""
    defaultValue = 10


_AlarmRecognitionPeriod_Type.__name__ = "TimeIntervalInSeconds"
_AlarmRecognitionPeriod_Object = MibScalar
alarmRecognitionPeriod = _AlarmRecognitionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 20),
    _AlarmRecognitionPeriod_Type()
)
alarmRecognitionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRecognitionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    alarmRecognitionPeriod.setUnits("s")


class _AcFailRecognitionPeriod_Type(TimeIntervalInSeconds):
    """Custom type acFailRecognitionPeriod based on TimeIntervalInSeconds"""
    defaultValue = 10


_AcFailRecognitionPeriod_Type.__name__ = "TimeIntervalInSeconds"
_AcFailRecognitionPeriod_Object = MibScalar
acFailRecognitionPeriod = _AcFailRecognitionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 30),
    _AcFailRecognitionPeriod_Type()
)
acFailRecognitionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFailRecognitionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    acFailRecognitionPeriod.setUnits("s")


class _EnableHighFloatTracking_Type(EnableState):
    """Custom type enableHighFloatTracking based on EnableState"""
    defaultValue = 1


_EnableHighFloatTracking_Type.__name__ = "EnableState"
_EnableHighFloatTracking_Object = MibScalar
enableHighFloatTracking = _EnableHighFloatTracking_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 40),
    _EnableHighFloatTracking_Type()
)
enableHighFloatTracking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableHighFloatTracking.setStatus("current")


class _HighFloatThreshold_Type(Float):
    """Custom type highFloatThreshold based on Float"""
    defaultValue = 5560


_HighFloatThreshold_Type.__name__ = "Float"
_HighFloatThreshold_Object = MibScalar
highFloatThreshold = _HighFloatThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 50),
    _HighFloatThreshold_Type()
)
highFloatThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highFloatThreshold.setStatus("current")
if mibBuilder.loadTexts:
    highFloatThreshold.setUnits("0.01 V")


class _EnableLowFloatTracking_Type(EnableState):
    """Custom type enableLowFloatTracking based on EnableState"""
    defaultValue = 1


_EnableLowFloatTracking_Type.__name__ = "EnableState"
_EnableLowFloatTracking_Object = MibScalar
enableLowFloatTracking = _EnableLowFloatTracking_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 60),
    _EnableLowFloatTracking_Type()
)
enableLowFloatTracking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableLowFloatTracking.setStatus("current")


class _LowFloatThreshold_Type(Float):
    """Custom type lowFloatThreshold based on Float"""
    defaultValue = 5280


_LowFloatThreshold_Type.__name__ = "Float"
_LowFloatThreshold_Object = MibScalar
lowFloatThreshold = _LowFloatThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 70),
    _LowFloatThreshold_Type()
)
lowFloatThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowFloatThreshold.setStatus("current")
if mibBuilder.loadTexts:
    lowFloatThreshold.setUnits("0.01 V")


class _HighLoadThreshold_Type(Float):
    """Custom type highLoadThreshold based on Float"""
    defaultValue = 5760


_HighLoadThreshold_Type.__name__ = "Float"
_HighLoadThreshold_Object = MibScalar
highLoadThreshold = _HighLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 80),
    _HighLoadThreshold_Type()
)
highLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highLoadThreshold.setStatus("current")
if mibBuilder.loadTexts:
    highLoadThreshold.setUnits("0.01 V")


class _LowLoadThreshold_Type(Float):
    """Custom type lowLoadThreshold based on Float"""
    defaultValue = 4700


_LowLoadThreshold_Type.__name__ = "Float"
_LowLoadThreshold_Object = MibScalar
lowLoadThreshold = _LowLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 90),
    _LowLoadThreshold_Type()
)
lowLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowLoadThreshold.setStatus("current")
if mibBuilder.loadTexts:
    lowLoadThreshold.setUnits("0.01 V")


class _BatteryTemperatureHighThreshold_Type(Signed8):
    """Custom type batteryTemperatureHighThreshold based on Signed8"""
    defaultValue = 50


_BatteryTemperatureHighThreshold_Type.__name__ = "Signed8"
_BatteryTemperatureHighThreshold_Object = MibScalar
batteryTemperatureHighThreshold = _BatteryTemperatureHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 130),
    _BatteryTemperatureHighThreshold_Type()
)
batteryTemperatureHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperatureHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    batteryTemperatureHighThreshold.setUnits("°C")


class _BatteryTemperatureLowThreshold_Type(Signed8):
    """Custom type batteryTemperatureLowThreshold based on Signed8"""
    defaultValue = 0


_BatteryTemperatureLowThreshold_Type.__name__ = "Signed8"
_BatteryTemperatureLowThreshold_Object = MibScalar
batteryTemperatureLowThreshold = _BatteryTemperatureLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 140),
    _BatteryTemperatureLowThreshold_Type()
)
batteryTemperatureLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperatureLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    batteryTemperatureLowThreshold.setUnits("°C")


class _SystemOverloadType_Type(OverloadAlarmType):
    """Custom type systemOverloadType based on OverloadAlarmType"""
    defaultValue = 0


_SystemOverloadType_Type.__name__ = "OverloadAlarmType"
_SystemOverloadType_Object = MibScalar
systemOverloadType = _SystemOverloadType_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 170),
    _SystemOverloadType_Type()
)
systemOverloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemOverloadType.setStatus("current")


class _SystemOverloadTypeB_Type(OverloadAlarmType):
    """Custom type systemOverloadTypeB based on OverloadAlarmType"""
    defaultValue = 2


_SystemOverloadTypeB_Type.__name__ = "OverloadAlarmType"
_SystemOverloadTypeB_Object = MibScalar
systemOverloadTypeB = _SystemOverloadTypeB_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 171),
    _SystemOverloadTypeB_Type()
)
systemOverloadTypeB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemOverloadTypeB.setStatus("current")


class _SystemOverloadRecognitionPeriod_Type(TimeIntervalInMinutes):
    """Custom type systemOverloadRecognitionPeriod based on TimeIntervalInMinutes"""
    defaultValue = 240


_SystemOverloadRecognitionPeriod_Type.__name__ = "TimeIntervalInMinutes"
_SystemOverloadRecognitionPeriod_Object = MibScalar
systemOverloadRecognitionPeriod = _SystemOverloadRecognitionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 180),
    _SystemOverloadRecognitionPeriod_Type()
)
systemOverloadRecognitionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemOverloadRecognitionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    systemOverloadRecognitionPeriod.setUnits("min")


class _SystemOverloadThreshold_Type(Unsigned8):
    """Custom type systemOverloadThreshold based on Unsigned8"""
    defaultValue = 85


_SystemOverloadThreshold_Type.__name__ = "Unsigned8"
_SystemOverloadThreshold_Object = MibScalar
systemOverloadThreshold = _SystemOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 190),
    _SystemOverloadThreshold_Type()
)
systemOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemOverloadThreshold.setStatus("current")
if mibBuilder.loadTexts:
    systemOverloadThreshold.setUnits("%")


class _SystemOverloadThresholdB_Type(Unsigned8):
    """Custom type systemOverloadThresholdB based on Unsigned8"""
    defaultValue = 85


_SystemOverloadThresholdB_Type.__name__ = "Unsigned8"
_SystemOverloadThresholdB_Object = MibScalar
systemOverloadThresholdB = _SystemOverloadThresholdB_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 191),
    _SystemOverloadThresholdB_Type()
)
systemOverloadThresholdB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemOverloadThresholdB.setStatus("current")
if mibBuilder.loadTexts:
    systemOverloadThresholdB.setUnits("%")


class _InDischargeAlarmCondition_Type(InDischargeAlarmCondition):
    """Custom type inDischargeAlarmCondition based on InDischargeAlarmCondition"""
    defaultValue = 0


_InDischargeAlarmCondition_Type.__name__ = "InDischargeAlarmCondition"
_InDischargeAlarmCondition_Object = MibScalar
inDischargeAlarmCondition = _InDischargeAlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 200),
    _InDischargeAlarmCondition_Type()
)
inDischargeAlarmCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inDischargeAlarmCondition.setStatus("current")


class _BatteryCurrentSensorFailRecognitionPeriod_Type(TimeIntervalInSeconds):
    """Custom type batteryCurrentSensorFailRecognitionPeriod based on TimeIntervalInSeconds"""
    defaultValue = 60


_BatteryCurrentSensorFailRecognitionPeriod_Type.__name__ = "TimeIntervalInSeconds"
_BatteryCurrentSensorFailRecognitionPeriod_Object = MibScalar
batteryCurrentSensorFailRecognitionPeriod = _BatteryCurrentSensorFailRecognitionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 220),
    _BatteryCurrentSensorFailRecognitionPeriod_Type()
)
batteryCurrentSensorFailRecognitionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentSensorFailRecognitionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    batteryCurrentSensorFailRecognitionPeriod.setUnits("s")


class _LowRectifierCapacityRedundancy_Type(Unsigned8):
    """Custom type lowRectifierCapacityRedundancy based on Unsigned8"""
    defaultValue = 20


_LowRectifierCapacityRedundancy_Type.__name__ = "Unsigned8"
_LowRectifierCapacityRedundancy_Object = MibScalar
lowRectifierCapacityRedundancy = _LowRectifierCapacityRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 240),
    _LowRectifierCapacityRedundancy_Type()
)
lowRectifierCapacityRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowRectifierCapacityRedundancy.setStatus("current")
if mibBuilder.loadTexts:
    lowRectifierCapacityRedundancy.setUnits("%")


class _LowRectifierCapacityAlarmThreshold_Type(Unsigned8):
    """Custom type lowRectifierCapacityAlarmThreshold based on Unsigned8"""
    defaultValue = 75


_LowRectifierCapacityAlarmThreshold_Type.__name__ = "Unsigned8"
_LowRectifierCapacityAlarmThreshold_Object = MibScalar
lowRectifierCapacityAlarmThreshold = _LowRectifierCapacityAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 250),
    _LowRectifierCapacityAlarmThreshold_Type()
)
lowRectifierCapacityAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowRectifierCapacityAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    lowRectifierCapacityAlarmThreshold.setUnits("%")


class _LowRectifierCapacityRecognitionPeriod_Type(TimeIntervalInMinutes):
    """Custom type lowRectifierCapacityRecognitionPeriod based on TimeIntervalInMinutes"""
    defaultValue = 0


_LowRectifierCapacityRecognitionPeriod_Type.__name__ = "TimeIntervalInMinutes"
_LowRectifierCapacityRecognitionPeriod_Object = MibScalar
lowRectifierCapacityRecognitionPeriod = _LowRectifierCapacityRecognitionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 252),
    _LowRectifierCapacityRecognitionPeriod_Type()
)
lowRectifierCapacityRecognitionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowRectifierCapacityRecognitionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    lowRectifierCapacityRecognitionPeriod.setUnits("min")
_RectifierCapacityBalance_Type = Percentile8Nan
_RectifierCapacityBalance_Object = MibScalar
rectifierCapacityBalance = _RectifierCapacityBalance_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 15, 260),
    _RectifierCapacityBalance_Type()
)
rectifierCapacityBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierCapacityBalance.setStatus("current")
if mibBuilder.loadTexts:
    rectifierCapacityBalance.setUnits("%")
_SmartAlarmTable_Object = MibTable
smartAlarmTable = _SmartAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20)
)
if mibBuilder.loadTexts:
    smartAlarmTable.setStatus("current")
_SmartAlarmEntry_Object = MibTableRow
smartAlarmEntry = _SmartAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1)
)
smartAlarmEntry.setIndexNames(
    (0, "RpsSc300Mib", "smartAlarmIndex"),
)
if mibBuilder.loadTexts:
    smartAlarmEntry.setStatus("current")


class _SmartAlarmIndex_Type(Unsigned8):
    """Custom type smartAlarmIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SmartAlarmIndex_Type.__name__ = "Unsigned8"
_SmartAlarmIndex_Object = MibTableColumn
smartAlarmIndex = _SmartAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1, 1),
    _SmartAlarmIndex_Type()
)
smartAlarmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartAlarmIndex.setStatus("current")


class _SmartAlarmTrapSend_Type(SendTrap):
    """Custom type smartAlarmTrapSend based on SendTrap"""
    defaultValue = 1


_SmartAlarmTrapSend_Type.__name__ = "SendTrap"
_SmartAlarmTrapSend_Object = MibTableColumn
smartAlarmTrapSend = _SmartAlarmTrapSend_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1, 10),
    _SmartAlarmTrapSend_Type()
)
smartAlarmTrapSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmTrapSend.setStatus("current")


class _SmartAlarmName_Type(DisplayString):
    """Custom type smartAlarmName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SmartAlarmName_Type.__name__ = "DisplayString"
_SmartAlarmName_Object = MibTableColumn
smartAlarmName = _SmartAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1, 20),
    _SmartAlarmName_Type()
)
smartAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmName.setStatus("current")


class _SmartAlarmSeverity_Type(AlarmSeverity):
    """Custom type smartAlarmSeverity based on AlarmSeverity"""
    defaultValue = 0


_SmartAlarmSeverity_Type.__name__ = "AlarmSeverity"
_SmartAlarmSeverity_Object = MibTableColumn
smartAlarmSeverity = _SmartAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1, 30),
    _SmartAlarmSeverity_Type()
)
smartAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSeverity.setStatus("current")


class _SmartAlarmGroup_Type(Unsigned8):
    """Custom type smartAlarmGroup based on Unsigned8"""
    defaultValue = 0


_SmartAlarmGroup_Type.__name__ = "Unsigned8"
_SmartAlarmGroup_Object = MibTableColumn
smartAlarmGroup = _SmartAlarmGroup_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1, 35),
    _SmartAlarmGroup_Type()
)
smartAlarmGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmGroup.setStatus("current")


class _SmartAlarmNotes_Type(DisplayString):
    """Custom type smartAlarmNotes based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_SmartAlarmNotes_Type.__name__ = "DisplayString"
_SmartAlarmNotes_Object = MibTableColumn
smartAlarmNotes = _SmartAlarmNotes_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1, 40),
    _SmartAlarmNotes_Type()
)
smartAlarmNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmNotes.setStatus("current")


class _SmartAlarmOperator_Type(AlarmOperator):
    """Custom type smartAlarmOperator based on AlarmOperator"""
    defaultValue = 1


_SmartAlarmOperator_Type.__name__ = "AlarmOperator"
_SmartAlarmOperator_Object = MibTableColumn
smartAlarmOperator = _SmartAlarmOperator_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1, 50),
    _SmartAlarmOperator_Type()
)
smartAlarmOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmOperator.setStatus("current")


class _SmartAlarmRecognitionPeriod_Type(TimeIntervalInSeconds):
    """Custom type smartAlarmRecognitionPeriod based on TimeIntervalInSeconds"""
    defaultValue = 10


_SmartAlarmRecognitionPeriod_Type.__name__ = "TimeIntervalInSeconds"
_SmartAlarmRecognitionPeriod_Object = MibTableColumn
smartAlarmRecognitionPeriod = _SmartAlarmRecognitionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1, 60),
    _SmartAlarmRecognitionPeriod_Type()
)
smartAlarmRecognitionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmRecognitionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    smartAlarmRecognitionPeriod.setUnits("s")


class _SmartAlarmDeactivationRecognitionPeriod_Type(TimeIntervalInSeconds):
    """Custom type smartAlarmDeactivationRecognitionPeriod based on TimeIntervalInSeconds"""
    defaultValue = 0


_SmartAlarmDeactivationRecognitionPeriod_Type.__name__ = "TimeIntervalInSeconds"
_SmartAlarmDeactivationRecognitionPeriod_Object = MibTableColumn
smartAlarmDeactivationRecognitionPeriod = _SmartAlarmDeactivationRecognitionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1, 61),
    _SmartAlarmDeactivationRecognitionPeriod_Type()
)
smartAlarmDeactivationRecognitionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmDeactivationRecognitionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    smartAlarmDeactivationRecognitionPeriod.setUnits("s")


class _SmartAlarmDoMappingA_Type(RelayMapping):
    """Custom type smartAlarmDoMappingA based on RelayMapping"""
    defaultValue = 0


_SmartAlarmDoMappingA_Type.__name__ = "RelayMapping"
_SmartAlarmDoMappingA_Object = MibTableColumn
smartAlarmDoMappingA = _SmartAlarmDoMappingA_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1, 70),
    _SmartAlarmDoMappingA_Type()
)
smartAlarmDoMappingA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmDoMappingA.setStatus("current")


class _SmartAlarmDoMappingB_Type(RelayMapping):
    """Custom type smartAlarmDoMappingB based on RelayMapping"""
    defaultValue = 0


_SmartAlarmDoMappingB_Type.__name__ = "RelayMapping"
_SmartAlarmDoMappingB_Object = MibTableColumn
smartAlarmDoMappingB = _SmartAlarmDoMappingB_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1, 80),
    _SmartAlarmDoMappingB_Type()
)
smartAlarmDoMappingB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmDoMappingB.setStatus("current")
_SmartAlarmState_Type = AlarmActiveState
_SmartAlarmState_Object = MibTableColumn
smartAlarmState = _SmartAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1, 100),
    _SmartAlarmState_Type()
)
smartAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmState.setStatus("current")
_ClearSmartAlarm_Type = NoData
_ClearSmartAlarm_Object = MibTableColumn
clearSmartAlarm = _ClearSmartAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1, 110),
    _ClearSmartAlarm_Type()
)
clearSmartAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearSmartAlarm.setStatus("current")


class _SmartAlarmSendEmail_Type(EnableState):
    """Custom type smartAlarmSendEmail based on EnableState"""
    defaultValue = 0


_SmartAlarmSendEmail_Type.__name__ = "EnableState"
_SmartAlarmSendEmail_Object = MibTableColumn
smartAlarmSendEmail = _SmartAlarmSendEmail_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 20, 1, 120),
    _SmartAlarmSendEmail_Type()
)
smartAlarmSendEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSendEmail.setStatus("current")
_SmartAlarmCountReset_Type = NoData
_SmartAlarmCountReset_Object = MibScalar
smartAlarmCountReset = _SmartAlarmCountReset_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 25),
    _SmartAlarmCountReset_Type()
)
smartAlarmCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmCountReset.setStatus("current")
_SourceAlarmTable_Object = MibTable
sourceAlarmTable = _SourceAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 30)
)
if mibBuilder.loadTexts:
    sourceAlarmTable.setStatus("current")
_SourceAlarmEntry_Object = MibTableRow
sourceAlarmEntry = _SourceAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 30, 1)
)
sourceAlarmEntry.setIndexNames(
    (0, "RpsSc300Mib", "sourceAlarmIndex"),
)
if mibBuilder.loadTexts:
    sourceAlarmEntry.setStatus("current")


class _SourceAlarmIndex_Type(Unsigned8):
    """Custom type sourceAlarmIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SourceAlarmIndex_Type.__name__ = "Unsigned8"
_SourceAlarmIndex_Object = MibTableColumn
sourceAlarmIndex = _SourceAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 30, 1, 1),
    _SourceAlarmIndex_Type()
)
sourceAlarmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sourceAlarmIndex.setStatus("current")
_SmartAlarmAlarmSourceTriggerState_Type = SourceState
_SmartAlarmAlarmSourceTriggerState_Object = MibTableColumn
smartAlarmAlarmSourceTriggerState = _SmartAlarmAlarmSourceTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 30, 1, 10),
    _SmartAlarmAlarmSourceTriggerState_Type()
)
smartAlarmAlarmSourceTriggerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmAlarmSourceTriggerState.setStatus("current")


class _SmartAlarmAlarmSourceStatus_Type(EnableState):
    """Custom type smartAlarmAlarmSourceStatus based on EnableState"""
    defaultValue = 0


_SmartAlarmAlarmSourceStatus_Type.__name__ = "EnableState"
_SmartAlarmAlarmSourceStatus_Object = MibTableColumn
smartAlarmAlarmSourceStatus = _SmartAlarmAlarmSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 30, 1, 20),
    _SmartAlarmAlarmSourceStatus_Type()
)
smartAlarmAlarmSourceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmAlarmSourceStatus.setStatus("current")


class _SmartAlarmAlarmSourceMapping_Type(Unsigned8):
    """Custom type smartAlarmAlarmSourceMapping based on Unsigned8"""
    defaultValue = 0


_SmartAlarmAlarmSourceMapping_Type.__name__ = "Unsigned8"
_SmartAlarmAlarmSourceMapping_Object = MibTableColumn
smartAlarmAlarmSourceMapping = _SmartAlarmAlarmSourceMapping_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 30, 1, 30),
    _SmartAlarmAlarmSourceMapping_Type()
)
smartAlarmAlarmSourceMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmAlarmSourceMapping.setStatus("current")


class _SmartAlarmAlarmSourceTrigger_Type(SourceTrigger):
    """Custom type smartAlarmAlarmSourceTrigger based on SourceTrigger"""
    defaultValue = 0


_SmartAlarmAlarmSourceTrigger_Type.__name__ = "SourceTrigger"
_SmartAlarmAlarmSourceTrigger_Object = MibTableColumn
smartAlarmAlarmSourceTrigger = _SmartAlarmAlarmSourceTrigger_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 30, 1, 41),
    _SmartAlarmAlarmSourceTrigger_Type()
)
smartAlarmAlarmSourceTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmAlarmSourceTrigger.setStatus("current")


class _SmartAlarmAlarmSourceType_Type(AlarmType):
    """Custom type smartAlarmAlarmSourceType based on AlarmType"""
    defaultValue = 0


_SmartAlarmAlarmSourceType_Type.__name__ = "AlarmType"
_SmartAlarmAlarmSourceType_Object = MibTableColumn
smartAlarmAlarmSourceType = _SmartAlarmAlarmSourceType_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 30, 1, 50),
    _SmartAlarmAlarmSourceType_Type()
)
smartAlarmAlarmSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmAlarmSourceType.setStatus("current")


class _SmartAlarmAlarmSourceIndex_Type(Unsigned8):
    """Custom type smartAlarmAlarmSourceIndex based on Unsigned8"""
    defaultValue = 1


_SmartAlarmAlarmSourceIndex_Type.__name__ = "Unsigned8"
_SmartAlarmAlarmSourceIndex_Object = MibTableColumn
smartAlarmAlarmSourceIndex = _SmartAlarmAlarmSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 30, 1, 60),
    _SmartAlarmAlarmSourceIndex_Type()
)
smartAlarmAlarmSourceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmAlarmSourceIndex.setStatus("current")


class _SmartAlarmAlarmSourceActiveCount_Type(Unsigned16):
    """Custom type smartAlarmAlarmSourceActiveCount based on Unsigned16"""
    defaultValue = 1


_SmartAlarmAlarmSourceActiveCount_Type.__name__ = "Unsigned16"
_SmartAlarmAlarmSourceActiveCount_Object = MibTableColumn
smartAlarmAlarmSourceActiveCount = _SmartAlarmAlarmSourceActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 30, 1, 70),
    _SmartAlarmAlarmSourceActiveCount_Type()
)
smartAlarmAlarmSourceActiveCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmAlarmSourceActiveCount.setStatus("current")


class _SmartAlarmAlarmSourceInactiveCount_Type(Unsigned16):
    """Custom type smartAlarmAlarmSourceInactiveCount based on Unsigned16"""
    defaultValue = 1


_SmartAlarmAlarmSourceInactiveCount_Type.__name__ = "Unsigned16"
_SmartAlarmAlarmSourceInactiveCount_Object = MibTableColumn
smartAlarmAlarmSourceInactiveCount = _SmartAlarmAlarmSourceInactiveCount_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 30, 1, 80),
    _SmartAlarmAlarmSourceInactiveCount_Type()
)
smartAlarmAlarmSourceInactiveCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmAlarmSourceInactiveCount.setStatus("current")
_SmartAlarmAlarmSourceCount_Type = Signed16
_SmartAlarmAlarmSourceCount_Object = MibTableColumn
smartAlarmAlarmSourceCount = _SmartAlarmAlarmSourceCount_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 30, 1, 90),
    _SmartAlarmAlarmSourceCount_Type()
)
smartAlarmAlarmSourceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmAlarmSourceCount.setStatus("current")
_SourceScheduleTable_Object = MibTable
sourceScheduleTable = _SourceScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 40)
)
if mibBuilder.loadTexts:
    sourceScheduleTable.setStatus("current")
_SourceScheduleEntry_Object = MibTableRow
sourceScheduleEntry = _SourceScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 40, 1)
)
sourceScheduleEntry.setIndexNames(
    (0, "RpsSc300Mib", "sourceScheduleIndex"),
)
if mibBuilder.loadTexts:
    sourceScheduleEntry.setStatus("current")


class _SourceScheduleIndex_Type(Unsigned8):
    """Custom type sourceScheduleIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SourceScheduleIndex_Type.__name__ = "Unsigned8"
_SourceScheduleIndex_Object = MibTableColumn
sourceScheduleIndex = _SourceScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 40, 1, 1),
    _SourceScheduleIndex_Type()
)
sourceScheduleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sourceScheduleIndex.setStatus("current")
_SmartAlarmScheduleSourceIsTriggered_Type = SourceState
_SmartAlarmScheduleSourceIsTriggered_Object = MibTableColumn
smartAlarmScheduleSourceIsTriggered = _SmartAlarmScheduleSourceIsTriggered_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 40, 1, 10),
    _SmartAlarmScheduleSourceIsTriggered_Type()
)
smartAlarmScheduleSourceIsTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmScheduleSourceIsTriggered.setStatus("current")


class _SmartAlarmScheduleSourceStatus_Type(EnableState):
    """Custom type smartAlarmScheduleSourceStatus based on EnableState"""
    defaultValue = 0


_SmartAlarmScheduleSourceStatus_Type.__name__ = "EnableState"
_SmartAlarmScheduleSourceStatus_Object = MibTableColumn
smartAlarmScheduleSourceStatus = _SmartAlarmScheduleSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 40, 1, 20),
    _SmartAlarmScheduleSourceStatus_Type()
)
smartAlarmScheduleSourceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmScheduleSourceStatus.setStatus("current")


class _SmartAlarmScheduleSourceMapping_Type(Unsigned8):
    """Custom type smartAlarmScheduleSourceMapping based on Unsigned8"""
    defaultValue = 0


_SmartAlarmScheduleSourceMapping_Type.__name__ = "Unsigned8"
_SmartAlarmScheduleSourceMapping_Object = MibTableColumn
smartAlarmScheduleSourceMapping = _SmartAlarmScheduleSourceMapping_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 40, 1, 30),
    _SmartAlarmScheduleSourceMapping_Type()
)
smartAlarmScheduleSourceMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmScheduleSourceMapping.setStatus("current")
_SmartAlarmScheduleSourceFirstActivation_Type = JulianDateUtc25
_SmartAlarmScheduleSourceFirstActivation_Object = MibTableColumn
smartAlarmScheduleSourceFirstActivation = _SmartAlarmScheduleSourceFirstActivation_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 40, 1, 50),
    _SmartAlarmScheduleSourceFirstActivation_Type()
)
smartAlarmScheduleSourceFirstActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmScheduleSourceFirstActivation.setStatus("current")


class _SmartAlarmScheduleSourceDuration_Type(TimeIntervalInMinutes):
    """Custom type smartAlarmScheduleSourceDuration based on TimeIntervalInMinutes"""
    defaultValue = 60


_SmartAlarmScheduleSourceDuration_Type.__name__ = "TimeIntervalInMinutes"
_SmartAlarmScheduleSourceDuration_Object = MibTableColumn
smartAlarmScheduleSourceDuration = _SmartAlarmScheduleSourceDuration_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 40, 1, 60),
    _SmartAlarmScheduleSourceDuration_Type()
)
smartAlarmScheduleSourceDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmScheduleSourceDuration.setStatus("current")
if mibBuilder.loadTexts:
    smartAlarmScheduleSourceDuration.setUnits("min")


class _SmartAlarmScheduleSourceInterval_Type(TimeIntervalInMinutes):
    """Custom type smartAlarmScheduleSourceInterval based on TimeIntervalInMinutes"""
    defaultValue = 1440


_SmartAlarmScheduleSourceInterval_Type.__name__ = "TimeIntervalInMinutes"
_SmartAlarmScheduleSourceInterval_Object = MibTableColumn
smartAlarmScheduleSourceInterval = _SmartAlarmScheduleSourceInterval_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 40, 1, 70),
    _SmartAlarmScheduleSourceInterval_Type()
)
smartAlarmScheduleSourceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmScheduleSourceInterval.setStatus("current")
if mibBuilder.loadTexts:
    smartAlarmScheduleSourceInterval.setUnits("min")


class _SmartAlarmScheduleSourceRepetitions_Type(Integer32):
    """Custom type smartAlarmScheduleSourceRepetitions based on Integer32"""
    defaultValue = 0


_SmartAlarmScheduleSourceRepetitions_Type.__name__ = "Integer32"
_SmartAlarmScheduleSourceRepetitions_Object = MibTableColumn
smartAlarmScheduleSourceRepetitions = _SmartAlarmScheduleSourceRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 40, 1, 80),
    _SmartAlarmScheduleSourceRepetitions_Type()
)
smartAlarmScheduleSourceRepetitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmScheduleSourceRepetitions.setStatus("current")
_SmartAlarmScheduleSourceNext_Type = JulianDateUtc25
_SmartAlarmScheduleSourceNext_Object = MibTableColumn
smartAlarmScheduleSourceNext = _SmartAlarmScheduleSourceNext_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 40, 1, 90),
    _SmartAlarmScheduleSourceNext_Type()
)
smartAlarmScheduleSourceNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmScheduleSourceNext.setStatus("current")
_SmartAlarmScheduleSourceEnd_Type = JulianDateUtc25
_SmartAlarmScheduleSourceEnd_Object = MibTableColumn
smartAlarmScheduleSourceEnd = _SmartAlarmScheduleSourceEnd_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 40, 1, 100),
    _SmartAlarmScheduleSourceEnd_Type()
)
smartAlarmScheduleSourceEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmScheduleSourceEnd.setStatus("current")
_SystemValueSourceTable_Object = MibTable
systemValueSourceTable = _SystemValueSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50)
)
if mibBuilder.loadTexts:
    systemValueSourceTable.setStatus("current")
_SystemValueSourceEntry_Object = MibTableRow
systemValueSourceEntry = _SystemValueSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50, 1)
)
systemValueSourceEntry.setIndexNames(
    (0, "RpsSc300Mib", "systemValueSourceIndex"),
)
if mibBuilder.loadTexts:
    systemValueSourceEntry.setStatus("current")


class _SystemValueSourceIndex_Type(Unsigned8):
    """Custom type systemValueSourceIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemValueSourceIndex_Type.__name__ = "Unsigned8"
_SystemValueSourceIndex_Object = MibTableColumn
systemValueSourceIndex = _SystemValueSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50, 1, 1),
    _SystemValueSourceIndex_Type()
)
systemValueSourceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemValueSourceIndex.setStatus("current")
_SmartAlarmSystemValueSourceIsTriggered_Type = SourceState
_SmartAlarmSystemValueSourceIsTriggered_Object = MibTableColumn
smartAlarmSystemValueSourceIsTriggered = _SmartAlarmSystemValueSourceIsTriggered_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50, 1, 10),
    _SmartAlarmSystemValueSourceIsTriggered_Type()
)
smartAlarmSystemValueSourceIsTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmSystemValueSourceIsTriggered.setStatus("current")


class _SmartAlarmSystemValueSourceStatus_Type(EnableState):
    """Custom type smartAlarmSystemValueSourceStatus based on EnableState"""
    defaultValue = 0


_SmartAlarmSystemValueSourceStatus_Type.__name__ = "EnableState"
_SmartAlarmSystemValueSourceStatus_Object = MibTableColumn
smartAlarmSystemValueSourceStatus = _SmartAlarmSystemValueSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50, 1, 20),
    _SmartAlarmSystemValueSourceStatus_Type()
)
smartAlarmSystemValueSourceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSystemValueSourceStatus.setStatus("current")


class _SmartAlarmSystemValueAlarmMapping_Type(Unsigned8):
    """Custom type smartAlarmSystemValueAlarmMapping based on Unsigned8"""
    defaultValue = 0


_SmartAlarmSystemValueAlarmMapping_Type.__name__ = "Unsigned8"
_SmartAlarmSystemValueAlarmMapping_Object = MibTableColumn
smartAlarmSystemValueAlarmMapping = _SmartAlarmSystemValueAlarmMapping_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50, 1, 30),
    _SmartAlarmSystemValueAlarmMapping_Type()
)
smartAlarmSystemValueAlarmMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSystemValueAlarmMapping.setStatus("current")


class _SmartAlarmSystemValueSourceValue_Type(SystemValueSourceValue):
    """Custom type smartAlarmSystemValueSourceValue based on SystemValueSourceValue"""
    defaultValue = 0


_SmartAlarmSystemValueSourceValue_Type.__name__ = "SystemValueSourceValue"
_SmartAlarmSystemValueSourceValue_Object = MibTableColumn
smartAlarmSystemValueSourceValue = _SmartAlarmSystemValueSourceValue_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50, 1, 40),
    _SmartAlarmSystemValueSourceValue_Type()
)
smartAlarmSystemValueSourceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSystemValueSourceValue.setStatus("current")


class _SmartAlarmSystemValueSourceValueIndex_Type(Unsigned8):
    """Custom type smartAlarmSystemValueSourceValueIndex based on Unsigned8"""
    defaultValue = 1


_SmartAlarmSystemValueSourceValueIndex_Type.__name__ = "Unsigned8"
_SmartAlarmSystemValueSourceValueIndex_Object = MibTableColumn
smartAlarmSystemValueSourceValueIndex = _SmartAlarmSystemValueSourceValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50, 1, 42),
    _SmartAlarmSystemValueSourceValueIndex_Type()
)
smartAlarmSystemValueSourceValueIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSystemValueSourceValueIndex.setStatus("current")
_SmartAlarmSystemValueSourceInput_Type = Float
_SmartAlarmSystemValueSourceInput_Object = MibTableColumn
smartAlarmSystemValueSourceInput = _SmartAlarmSystemValueSourceInput_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50, 1, 45),
    _SmartAlarmSystemValueSourceInput_Type()
)
smartAlarmSystemValueSourceInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmSystemValueSourceInput.setStatus("current")
if mibBuilder.loadTexts:
    smartAlarmSystemValueSourceInput.setUnits("0.01")


class _SmartAlarmSystemValueSourceThresholdType_Type(ThresholdType):
    """Custom type smartAlarmSystemValueSourceThresholdType based on ThresholdType"""
    defaultValue = 0


_SmartAlarmSystemValueSourceThresholdType_Type.__name__ = "ThresholdType"
_SmartAlarmSystemValueSourceThresholdType_Object = MibTableColumn
smartAlarmSystemValueSourceThresholdType = _SmartAlarmSystemValueSourceThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50, 1, 50),
    _SmartAlarmSystemValueSourceThresholdType_Type()
)
smartAlarmSystemValueSourceThresholdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSystemValueSourceThresholdType.setStatus("current")


class _SmartAlarmSystemValueSourceThreshold_Type(Float):
    """Custom type smartAlarmSystemValueSourceThreshold based on Float"""
    defaultValue = 0


_SmartAlarmSystemValueSourceThreshold_Type.__name__ = "Float"
_SmartAlarmSystemValueSourceThreshold_Object = MibTableColumn
smartAlarmSystemValueSourceThreshold = _SmartAlarmSystemValueSourceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50, 1, 60),
    _SmartAlarmSystemValueSourceThreshold_Type()
)
smartAlarmSystemValueSourceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSystemValueSourceThreshold.setStatus("current")
if mibBuilder.loadTexts:
    smartAlarmSystemValueSourceThreshold.setUnits("0.01")


class _SmartAlarmSystemValueSourceHysteresis_Type(Float):
    """Custom type smartAlarmSystemValueSourceHysteresis based on Float"""
    defaultValue = 0


_SmartAlarmSystemValueSourceHysteresis_Type.__name__ = "Float"
_SmartAlarmSystemValueSourceHysteresis_Object = MibTableColumn
smartAlarmSystemValueSourceHysteresis = _SmartAlarmSystemValueSourceHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50, 1, 65),
    _SmartAlarmSystemValueSourceHysteresis_Type()
)
smartAlarmSystemValueSourceHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSystemValueSourceHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    smartAlarmSystemValueSourceHysteresis.setUnits("0.01")


class _SmartAlarmSystemValueSourceActiveCount_Type(Unsigned16):
    """Custom type smartAlarmSystemValueSourceActiveCount based on Unsigned16"""
    defaultValue = 1


_SmartAlarmSystemValueSourceActiveCount_Type.__name__ = "Unsigned16"
_SmartAlarmSystemValueSourceActiveCount_Object = MibTableColumn
smartAlarmSystemValueSourceActiveCount = _SmartAlarmSystemValueSourceActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50, 1, 70),
    _SmartAlarmSystemValueSourceActiveCount_Type()
)
smartAlarmSystemValueSourceActiveCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSystemValueSourceActiveCount.setStatus("current")


class _SmartAlarmSystemValueSourceInactiveCount_Type(Unsigned16):
    """Custom type smartAlarmSystemValueSourceInactiveCount based on Unsigned16"""
    defaultValue = 1


_SmartAlarmSystemValueSourceInactiveCount_Type.__name__ = "Unsigned16"
_SmartAlarmSystemValueSourceInactiveCount_Object = MibTableColumn
smartAlarmSystemValueSourceInactiveCount = _SmartAlarmSystemValueSourceInactiveCount_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50, 1, 80),
    _SmartAlarmSystemValueSourceInactiveCount_Type()
)
smartAlarmSystemValueSourceInactiveCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSystemValueSourceInactiveCount.setStatus("current")
_SmartAlarmSystemValueSourceCount_Type = Signed16
_SmartAlarmSystemValueSourceCount_Object = MibTableColumn
smartAlarmSystemValueSourceCount = _SmartAlarmSystemValueSourceCount_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 50, 1, 90),
    _SmartAlarmSystemValueSourceCount_Type()
)
smartAlarmSystemValueSourceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmSystemValueSourceCount.setStatus("current")
_SourceManualTable_Object = MibTable
sourceManualTable = _SourceManualTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 60)
)
if mibBuilder.loadTexts:
    sourceManualTable.setStatus("current")
_SourceManualEntry_Object = MibTableRow
sourceManualEntry = _SourceManualEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 60, 1)
)
sourceManualEntry.setIndexNames(
    (0, "RpsSc300Mib", "sourceManualIndex"),
)
if mibBuilder.loadTexts:
    sourceManualEntry.setStatus("current")


class _SourceManualIndex_Type(Unsigned8):
    """Custom type sourceManualIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SourceManualIndex_Type.__name__ = "Unsigned8"
_SourceManualIndex_Object = MibTableColumn
sourceManualIndex = _SourceManualIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 60, 1, 1),
    _SourceManualIndex_Type()
)
sourceManualIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sourceManualIndex.setStatus("current")
_SmartAlarmIsManualSourceTriggered_Type = SourceState
_SmartAlarmIsManualSourceTriggered_Object = MibTableColumn
smartAlarmIsManualSourceTriggered = _SmartAlarmIsManualSourceTriggered_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 60, 1, 10),
    _SmartAlarmIsManualSourceTriggered_Type()
)
smartAlarmIsManualSourceTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmIsManualSourceTriggered.setStatus("current")


class _SmartAlarmSourceManualStatus_Type(EnableState):
    """Custom type smartAlarmSourceManualStatus based on EnableState"""
    defaultValue = 0


_SmartAlarmSourceManualStatus_Type.__name__ = "EnableState"
_SmartAlarmSourceManualStatus_Object = MibTableColumn
smartAlarmSourceManualStatus = _SmartAlarmSourceManualStatus_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 60, 1, 20),
    _SmartAlarmSourceManualStatus_Type()
)
smartAlarmSourceManualStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSourceManualStatus.setStatus("current")
_SmartAlarmSourceManualTrigger_Type = Boolean
_SmartAlarmSourceManualTrigger_Object = MibTableColumn
smartAlarmSourceManualTrigger = _SmartAlarmSourceManualTrigger_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 60, 1, 30),
    _SmartAlarmSourceManualTrigger_Type()
)
smartAlarmSourceManualTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSourceManualTrigger.setStatus("current")


class _SmartAlarmSourceManualMapping_Type(Unsigned8):
    """Custom type smartAlarmSourceManualMapping based on Unsigned8"""
    defaultValue = 0


_SmartAlarmSourceManualMapping_Type.__name__ = "Unsigned8"
_SmartAlarmSourceManualMapping_Object = MibTableColumn
smartAlarmSourceManualMapping = _SmartAlarmSourceManualMapping_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 60, 1, 40),
    _SmartAlarmSourceManualMapping_Type()
)
smartAlarmSourceManualMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSourceManualMapping.setStatus("current")


class _SmartAlarmSourceManualPeriod_Type(TimeIntervalInSeconds):
    """Custom type smartAlarmSourceManualPeriod based on TimeIntervalInSeconds"""
    defaultValue = 0


_SmartAlarmSourceManualPeriod_Type.__name__ = "TimeIntervalInSeconds"
_SmartAlarmSourceManualPeriod_Object = MibTableColumn
smartAlarmSourceManualPeriod = _SmartAlarmSourceManualPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 60, 1, 50),
    _SmartAlarmSourceManualPeriod_Type()
)
smartAlarmSourceManualPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmSourceManualPeriod.setStatus("current")
if mibBuilder.loadTexts:
    smartAlarmSourceManualPeriod.setUnits("s")
_SmartAlarmNamedItemsTable_Object = MibTable
smartAlarmNamedItemsTable = _SmartAlarmNamedItemsTable_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 70)
)
if mibBuilder.loadTexts:
    smartAlarmNamedItemsTable.setStatus("current")
_SmartAlarmNamedItemsEntry_Object = MibTableRow
smartAlarmNamedItemsEntry = _SmartAlarmNamedItemsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 70, 1)
)
smartAlarmNamedItemsEntry.setIndexNames(
    (0, "RpsSc300Mib", "smartAlarmNamedItemsIndex"),
)
if mibBuilder.loadTexts:
    smartAlarmNamedItemsEntry.setStatus("current")


class _SmartAlarmNamedItemsIndex_Type(Unsigned8):
    """Custom type smartAlarmNamedItemsIndex based on Unsigned8"""
    subtypeSpec = Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SmartAlarmNamedItemsIndex_Type.__name__ = "Unsigned8"
_SmartAlarmNamedItemsIndex_Object = MibTableColumn
smartAlarmNamedItemsIndex = _SmartAlarmNamedItemsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 70, 1, 1),
    _SmartAlarmNamedItemsIndex_Type()
)
smartAlarmNamedItemsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartAlarmNamedItemsIndex.setStatus("current")


class _SmartAlarmItemMapping_Type(Unsigned8):
    """Custom type smartAlarmItemMapping based on Unsigned8"""
    defaultValue = 0


_SmartAlarmItemMapping_Type.__name__ = "Unsigned8"
_SmartAlarmItemMapping_Object = MibTableColumn
smartAlarmItemMapping = _SmartAlarmItemMapping_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 70, 1, 10),
    _SmartAlarmItemMapping_Type()
)
smartAlarmItemMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmItemMapping.setStatus("current")
_SmartAlarmItemValue_Type = Float
_SmartAlarmItemValue_Object = MibTableColumn
smartAlarmItemValue = _SmartAlarmItemValue_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 70, 1, 20),
    _SmartAlarmItemValue_Type()
)
smartAlarmItemValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmItemValue.setStatus("current")
if mibBuilder.loadTexts:
    smartAlarmItemValue.setUnits("0.01")


class _SmartAlarmItemName_Type(DisplayString):
    """Custom type smartAlarmItemName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SmartAlarmItemName_Type.__name__ = "DisplayString"
_SmartAlarmItemName_Object = MibTableColumn
smartAlarmItemName = _SmartAlarmItemName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 70, 1, 30),
    _SmartAlarmItemName_Type()
)
smartAlarmItemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmItemName.setStatus("current")
_SmartAlarmItemTriggerState_Type = SourceState
_SmartAlarmItemTriggerState_Object = MibTableColumn
smartAlarmItemTriggerState = _SmartAlarmItemTriggerState_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 70, 1, 50),
    _SmartAlarmItemTriggerState_Type()
)
smartAlarmItemTriggerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAlarmItemTriggerState.setStatus("current")


class _SmartAlarmItemThresholdType_Type(ThresholdType):
    """Custom type smartAlarmItemThresholdType based on ThresholdType"""
    defaultValue = 0


_SmartAlarmItemThresholdType_Type.__name__ = "ThresholdType"
_SmartAlarmItemThresholdType_Object = MibTableColumn
smartAlarmItemThresholdType = _SmartAlarmItemThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 70, 1, 60),
    _SmartAlarmItemThresholdType_Type()
)
smartAlarmItemThresholdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmItemThresholdType.setStatus("current")


class _SmartAlarmItemThreshold_Type(Float):
    """Custom type smartAlarmItemThreshold based on Float"""
    defaultValue = 0


_SmartAlarmItemThreshold_Type.__name__ = "Float"
_SmartAlarmItemThreshold_Object = MibTableColumn
smartAlarmItemThreshold = _SmartAlarmItemThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 70, 1, 70),
    _SmartAlarmItemThreshold_Type()
)
smartAlarmItemThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmItemThreshold.setStatus("current")
if mibBuilder.loadTexts:
    smartAlarmItemThreshold.setUnits("0.01")


class _SmartAlarmItemHysteresis_Type(Float):
    """Custom type smartAlarmItemHysteresis based on Float"""
    defaultValue = 0


_SmartAlarmItemHysteresis_Type.__name__ = "Float"
_SmartAlarmItemHysteresis_Object = MibTableColumn
smartAlarmItemHysteresis = _SmartAlarmItemHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 110, 70, 1, 80),
    _SmartAlarmItemHysteresis_Type()
)
smartAlarmItemHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAlarmItemHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    smartAlarmItemHysteresis.setUnits("0.01")
_Trap700Bindings_ObjectIdentity = ObjectIdentity
trap700Bindings = _Trap700Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 111)
)
if mibBuilder.loadTexts:
    trap700Bindings.setStatus("current")
_TrapAlarmOrigin_Type = AlarmType
_TrapAlarmOrigin_Object = MibScalar
trapAlarmOrigin = _TrapAlarmOrigin_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 111, 10),
    _TrapAlarmOrigin_Type()
)
trapAlarmOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmOrigin.setStatus("current")


class _TrapAlarmName_Type(DisplayString):
    """Custom type trapAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TrapAlarmName_Type.__name__ = "DisplayString"
_TrapAlarmName_Object = MibScalar
trapAlarmName = _TrapAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 111, 11),
    _TrapAlarmName_Type()
)
trapAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmName.setStatus("current")
_TrapAlarmNumber_Type = Unsigned16
_TrapAlarmNumber_Object = MibScalar
trapAlarmNumber = _TrapAlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 111, 12),
    _TrapAlarmNumber_Type()
)
trapAlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmNumber.setStatus("current")


class _TrapAdditionalText_Type(DisplayString):
    """Custom type trapAdditionalText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_TrapAdditionalText_Type.__name__ = "DisplayString"
_TrapAdditionalText_Object = MibScalar
trapAdditionalText = _TrapAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 111, 13),
    _TrapAdditionalText_Type()
)
trapAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAdditionalText.setStatus("current")
_TrapAlarmKeepSeverity_Type = TrapAlarmKeepSeverity
_TrapAlarmKeepSeverity_Object = MibScalar
trapAlarmKeepSeverity = _TrapAlarmKeepSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 111, 14),
    _TrapAlarmKeepSeverity_Type()
)
trapAlarmKeepSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmKeepSeverity.setStatus("current")
_RpsTraps_ObjectIdentity = ObjectIdentity
rpsTraps = _RpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20)
)
if mibBuilder.loadTexts:
    rpsTraps.setStatus("current")

# Managed Objects groups

systemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 10, 10, 1)
)
systemObjectGroup.setObjects(
      *(("RpsSc300Mib", "batteryCharacterizationDataIndex"),
        ("RpsSc300Mib", "logItemsIndex"),
        ("RpsSc300Mib", "systemManufacturer"),
        ("RpsSc300Mib", "systemSerialNumber"),
        ("RpsSc300Mib", "systemType"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteNotes"),
        ("RpsSc300Mib", "systemObjectId2"),
        ("RpsSc300Mib", "trapFormat"),
        ("RpsSc300Mib", "genericTrapsEnable"),
        ("RpsSc300Mib", "configurationName"),
        ("RpsSc300Mib", "configurationVersion"),
        ("RpsSc300Mib", "configurationModified"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "isThreePhaseSystem"),
        ("RpsSc300Mib", "manufacturerName"),
        ("RpsSc300Mib", "productType"),
        ("RpsSc300Mib", "softwareVersion"),
        ("RpsSc300Mib", "bootVersion"),
        ("RpsSc300Mib", "interfaceVersion"),
        ("RpsSc300Mib", "hardwareVersion"),
        ("RpsSc300Mib", "lcdVersion"),
        ("RpsSc300Mib", "batteryMonitor"),
        ("RpsSc300Mib", "serialNumber"),
        ("RpsSc300Mib", "ethernetMacAddress"),
        ("RpsSc300Mib", "subversionRevision"),
        ("RpsSc300Mib", "evaluationSoftwareFound"),
        ("RpsSc300Mib", "genericSystemType"),
        ("RpsSc300Mib", "s3pAccess"),
        ("RpsSc300Mib", "snmpAccess"),
        ("RpsSc300Mib", "serialServerAccess"),
        ("RpsSc300Mib", "serialServerPort"),
        ("RpsSc300Mib", "s3pAddress"),
        ("RpsSc300Mib", "ipAddress"),
        ("RpsSc300Mib", "subnetMask"),
        ("RpsSc300Mib", "gatewayAddress"),
        ("RpsSc300Mib", "vlanId"),
        ("RpsSc300Mib", "ipAddressAuto"),
        ("RpsSc300Mib", "subnetMaskAuto"),
        ("RpsSc300Mib", "gatewayAddressAuto"),
        ("RpsSc300Mib", "autoIp"),
        ("RpsSc300Mib", "webSessionTimeout"),
        ("RpsSc300Mib", "webAccess"),
        ("RpsSc300Mib", "blacklist"),
        ("RpsSc300Mib", "blacklisted"),
        ("RpsSc300Mib", "baudRate"),
        ("RpsSc300Mib", "parity"),
        ("RpsSc300Mib", "stopBits"),
        ("RpsSc300Mib", "enableModem"),
        ("RpsSc300Mib", "alarmReport"),
        ("RpsSc300Mib", "modemSetUpString"),
        ("RpsSc300Mib", "modemAutoAnswerRings"),
        ("RpsSc300Mib", "modemMaximumRetries"),
        ("RpsSc300Mib", "modemRetryInterval"),
        ("RpsSc300Mib", "modemPowerReset"),
        ("RpsSc300Mib", "dialOutNumber"),
        ("RpsSc300Mib", "smsPhoneName"),
        ("RpsSc300Mib", "smsLevel"),
        ("RpsSc300Mib", "smsPhoneNumber"),
        ("RpsSc300Mib", "smsPrefix"),
        ("RpsSc300Mib", "smsEmailGateway"),
        ("RpsSc300Mib", "modbusAccess"),
        ("RpsSc300Mib", "modbusAddress"),
        ("RpsSc300Mib", "modbusInterfaceVersion"),
        ("RpsSc300Mib", "snmpReadCommunity"),
        ("RpsSc300Mib", "snmpWriteCommunity"),
        ("RpsSc300Mib", "enableTrapRepeat"),
        ("RpsSc300Mib", "trapRepeatRate"),
        ("RpsSc300Mib", "trapVersion"),
        ("RpsSc300Mib", "trapReceiverIpAddress"),
        ("RpsSc300Mib", "trapReceiverPort"),
        ("RpsSc300Mib", "trapReceiverName"),
        ("RpsSc300Mib", "trapReceiverLevel"),
        ("RpsSc300Mib", "trapReceiverCommunity"),
        ("RpsSc300Mib", "trapReceiverMode"),
        ("RpsSc300Mib", "acknowledgeAlarmSummaryTrap"),
        ("RpsSc300Mib", "snmpV3PrivacyPassword"),
        ("RpsSc300Mib", "enableHeartbeatTrap"),
        ("RpsSc300Mib", "heartbeatTrapPeriod"),
        ("RpsSc300Mib", "emailNotifications"),
        ("RpsSc300Mib", "smtpServerIpAddress"),
        ("RpsSc300Mib", "smtpServerPort"),
        ("RpsSc300Mib", "emailReturnAddress"),
        ("RpsSc300Mib", "emailFromAddress"),
        ("RpsSc300Mib", "emailValidAddress"),
        ("RpsSc300Mib", "emailSubjectPrefix"),
        ("RpsSc300Mib", "emailReceiverAddress"),
        ("RpsSc300Mib", "emailReceiverLevel"),
        ("RpsSc300Mib", "emailReceiverDelay"),
        ("RpsSc300Mib", "sendTestEmail"),
        ("RpsSc300Mib", "smtpResult"),
        ("RpsSc300Mib", "sntpPollInterval"),
        ("RpsSc300Mib", "udpPort"),
        ("RpsSc300Mib", "primaryAddress"),
        ("RpsSc300Mib", "backupAddress"),
        ("RpsSc300Mib", "sntpLastUpdate"),
        ("RpsSc300Mib", "userName"),
        ("RpsSc300Mib", "userLogonId"),
        ("RpsSc300Mib", "userLogonPassword"),
        ("RpsSc300Mib", "userActive"),
        ("RpsSc300Mib", "userWrite"),
        ("RpsSc300Mib", "userRestore"),
        ("RpsSc300Mib", "userBackup"),
        ("RpsSc300Mib", "userExecute"),
        ("RpsSc300Mib", "userUpgradeFirmware"),
        ("RpsSc300Mib", "userAdministrator"),
        ("RpsSc300Mib", "userSnmp"),
        ("RpsSc300Mib", "authServer"),
        ("RpsSc300Mib", "radiusAuthSvrSecret"),
        ("RpsSc300Mib", "acctServer"),
        ("RpsSc300Mib", "radiusAcctSvrSecret"),
        ("RpsSc300Mib", "uiAccess"),
        ("RpsSc300Mib", "s3pWriteAccessPassword"),
        ("RpsSc300Mib", "remoteAccessLevel"),
        ("RpsSc300Mib", "uploadingFirmware"),
        ("RpsSc300Mib", "acVoltage"),
        ("RpsSc300Mib", "phase1"),
        ("RpsSc300Mib", "phase2"),
        ("RpsSc300Mib", "phase3"),
        ("RpsSc300Mib", "loadCurrent"),
        ("RpsSc300Mib", "systemPower"),
        ("RpsSc300Mib", "loadPower"),
        ("RpsSc300Mib", "rxpSlaveRegistrationState"),
        ("RpsSc300Mib", "rxpSlaveName"),
        ("RpsSc300Mib", "rxpSlaveSerialNumber"),
        ("RpsSc300Mib", "rxpSlaveType"),
        ("RpsSc300Mib", "rxpSlaveCommandSet"),
        ("RpsSc300Mib", "rxpBomRevision"),
        ("RpsSc300Mib", "rxpSoftwareVersion"),
        ("RpsSc300Mib", "identifyRxpSlave"),
        ("RpsSc300Mib", "iobRegistrationState"),
        ("RpsSc300Mib", "iobSerialNumber"),
        ("RpsSc300Mib", "iobMapping"),
        ("RpsSc300Mib", "iobNumberOfVoltages"),
        ("RpsSc300Mib", "iobNumberOfCurrents"),
        ("RpsSc300Mib", "iobNumberOfTemperatures"),
        ("RpsSc300Mib", "iobNumberOfDigitalInputs"),
        ("RpsSc300Mib", "iobNumberOfRelays"),
        ("RpsSc300Mib", "iobNumberOfLvds"),
        ("RpsSc300Mib", "numberOfRegisteredRectifiers"),
        ("RpsSc300Mib", "numberOfRegisteredSolarChargers"),
        ("RpsSc300Mib", "numberOfRectifiersFailed"),
        ("RpsSc300Mib", "numberOfSolarFailed"),
        ("RpsSc300Mib", "numberOfRectifiersCommsLost"),
        ("RpsSc300Mib", "numberOfSolarCommsLost"),
        ("RpsSc300Mib", "rectifierCurrent"),
        ("RpsSc300Mib", "rectifierCurrentLimit"),
        ("RpsSc300Mib", "solarCurrentLimit"),
        ("RpsSc300Mib", "enableCurrentShare"),
        ("RpsSc300Mib", "highestRectifierHeatsinkTemperature"),
        ("RpsSc300Mib", "rectifierSerialNumber"),
        ("RpsSc300Mib", "rectifierType"),
        ("RpsSc300Mib", "rectifierInputType"),
        ("RpsSc300Mib", "rectifierStatus"),
        ("RpsSc300Mib", "rectifierMaximumCurrentLimit"),
        ("RpsSc300Mib", "rectifierMaximumPowerLimit"),
        ("RpsSc300Mib", "rectifierMinimumOvsdSetPoint"),
        ("RpsSc300Mib", "rectifierMaximumOvsdSetPoint"),
        ("RpsSc300Mib", "rectifierInputVoltage"),
        ("RpsSc300Mib", "rectifierReportedVoltage"),
        ("RpsSc300Mib", "rectifierReportedCurrent"),
        ("RpsSc300Mib", "rectifierOutputPowerw"),
        ("RpsSc300Mib", "rectifierOutputPower"),
        ("RpsSc300Mib", "rectifierHeatsinkTemperature"),
        ("RpsSc300Mib", "rectifierRegistrationState"),
        ("RpsSc300Mib", "rectifierFailedState"),
        ("RpsSc300Mib", "loadBasedRunTime"),
        ("RpsSc300Mib", "shutdownRectifier"),
        ("RpsSc300Mib", "rectifierHasBeenShutdown"),
        ("RpsSc300Mib", "rectifierPhase1"),
        ("RpsSc300Mib", "rectifierPhase2"),
        ("RpsSc300Mib", "rectifierPhase3"),
        ("RpsSc300Mib", "rectifierNotes"),
        ("RpsSc300Mib", "rectifierInputCurrent"),
        ("RpsSc300Mib", "rectifierPhase"),
        ("RpsSc300Mib", "phase1SerialNumber"),
        ("RpsSc300Mib", "acInputCurrent"),
        ("RpsSc300Mib", "dcInputCurrent"),
        ("RpsSc300Mib", "rectifierShutdownMode"),
        ("RpsSc300Mib", "restartAllRectifiers"),
        ("RpsSc300Mib", "rectifierShutdownSmartAlarm"),
        ("RpsSc300Mib", "rectCycleLowThreshold"),
        ("RpsSc300Mib", "rectCycleHighThreshold"),
        ("RpsSc300Mib", "rectCycleInterval"),
        ("RpsSc300Mib", "redundancy"),
        ("RpsSc300Mib", "resetRunTimes"),
        ("RpsSc300Mib", "rampUpSlope"),
        ("RpsSc300Mib", "ovsdSetPoint"),
        ("RpsSc300Mib", "rectifierStartUpDelay"),
        ("RpsSc300Mib", "enableRipPowerShare"),
        ("RpsSc300Mib", "controlState"),
        ("RpsSc300Mib", "floatVoltage"),
        ("RpsSc300Mib", "alternativeFloatVoltage"),
        ("RpsSc300Mib", "alternativeFloatSmartAlarm"),
        ("RpsSc300Mib", "alternativeFloatStatus"),
        ("RpsSc300Mib", "maximumSystemVoltage"),
        ("RpsSc300Mib", "minimumSystemVoltage"),
        ("RpsSc300Mib", "busVoltage"),
        ("RpsSc300Mib", "targetVoltage"),
        ("RpsSc300Mib", "enableActiveVoltageControl"),
        ("RpsSc300Mib", "avcState"),
        ("RpsSc300Mib", "avcOffset"),
        ("RpsSc300Mib", "baseVoltage"),
        ("RpsSc300Mib", "enableTemperatureCompensation"),
        ("RpsSc300Mib", "temperatureCompensationAllowed"),
        ("RpsSc300Mib", "temperatureCompensationState"),
        ("RpsSc300Mib", "temperatureCompensationSlope"),
        ("RpsSc300Mib", "temperatureCompensationReferenceTemperature"),
        ("RpsSc300Mib", "temperatureCompensationUpperLimit"),
        ("RpsSc300Mib", "temperatureCompensationLowerLimit"),
        ("RpsSc300Mib", "temperatureCompensationOffsetVoltage"),
        ("RpsSc300Mib", "resetAhDischarged"),
        ("RpsSc300Mib", "ahDischargedFloatResetRate"),
        ("RpsSc300Mib", "enableEqualize"),
        ("RpsSc300Mib", "equalizeStartAllowed"),
        ("RpsSc300Mib", "equalizeState"),
        ("RpsSc300Mib", "equalizeVoltage"),
        ("RpsSc300Mib", "equalizeOffsetVoltage"),
        ("RpsSc300Mib", "periodicEqualizeFirstDateTime"),
        ("RpsSc300Mib", "equalizeInterval"),
        ("RpsSc300Mib", "nextEqualizeStartTime"),
        ("RpsSc300Mib", "equalizeDuration"),
        ("RpsSc300Mib", "equalizeRemainingTime"),
        ("RpsSc300Mib", "startEqualize"),
        ("RpsSc300Mib", "stopEqualize"),
        ("RpsSc300Mib", "equalizeSmartAlarm"),
        ("RpsSc300Mib", "enableFastCharge"),
        ("RpsSc300Mib", "fastChargeState"),
        ("RpsSc300Mib", "fastChargeStartAllowed"),
        ("RpsSc300Mib", "fastChargeVoltage"),
        ("RpsSc300Mib", "fastChargeOffsetVoltage"),
        ("RpsSc300Mib", "fastChargeAhDischarged"),
        ("RpsSc300Mib", "fastChargeMaximumDuration"),
        ("RpsSc300Mib", "fastChargeAmpereHourThreshold"),
        ("RpsSc300Mib", "fastChargeVoltageThreshold"),
        ("RpsSc300Mib", "fastChargeRechargePercentage"),
        ("RpsSc300Mib", "fastChargeAmpereHourStopThreshold"),
        ("RpsSc300Mib", "fastChargeMaximumTimeRemaining"),
        ("RpsSc300Mib", "stopFastCharge"),
        ("RpsSc300Mib", "enableBatteryCurrentLimit"),
        ("RpsSc300Mib", "bclState"),
        ("RpsSc300Mib", "bclLimit"),
        ("RpsSc300Mib", "bclOffsetVoltage"),
        ("RpsSc300Mib", "bclEngineRunLimit"),
        ("RpsSc300Mib", "enableBatteryTest"),
        ("RpsSc300Mib", "preventBatteryTest"),
        ("RpsSc300Mib", "batteryTestStartAllowed"),
        ("RpsSc300Mib", "batteryTestLockoutRemaining"),
        ("RpsSc300Mib", "batteryTestState"),
        ("RpsSc300Mib", "batteryTestFirstDateTime"),
        ("RpsSc300Mib", "batteryTestInterval"),
        ("RpsSc300Mib", "nextBatteryTestStartTime"),
        ("RpsSc300Mib", "batteryTestDuration"),
        ("RpsSc300Mib", "batteryTestRemainingTime"),
        ("RpsSc300Mib", "batteryTestTerminationVoltage"),
        ("RpsSc300Mib", "batteryTestOffsetVoltage"),
        ("RpsSc300Mib", "startBatteryTest"),
        ("RpsSc300Mib", "stopBatteryTest"),
        ("RpsSc300Mib", "allowBatteryTestDuringLockout"),
        ("RpsSc300Mib", "bBatteryTestOffsetVoltage"),
        ("RpsSc300Mib", "lvdInhibitPeriod"),
        ("RpsSc300Mib", "allowFrontPanelLvdControl"),
        ("RpsSc300Mib", "lvdName"),
        ("RpsSc300Mib", "lvdState"),
        ("RpsSc300Mib", "lvdInhibited"),
        ("RpsSc300Mib", "enableLvdVoltageDisconnect"),
        ("RpsSc300Mib", "lvdDisconnectVoltage"),
        ("RpsSc300Mib", "lvdReconnectVoltage"),
        ("RpsSc300Mib", "lvdRecognitionPeriod"),
        ("RpsSc300Mib", "enableLvdAcTimer"),
        ("RpsSc300Mib", "lvdAcTimerDisconnectDelay"),
        ("RpsSc300Mib", "enableLvdSaDisconnect"),
        ("RpsSc300Mib", "lvdSaDisconnectIndex"),
        ("RpsSc300Mib", "enableLvdChainedToPrevious"),
        ("RpsSc300Mib", "lvdRemoteManualControl"),
        ("RpsSc300Mib", "lvdcLvdMapping"),
        ("RpsSc300Mib", "lvdcState"),
        ("RpsSc300Mib", "enableLvdc"),
        ("RpsSc300Mib", "lvdcIobNumber"),
        ("RpsSc300Mib", "lvdcIobLvdNumber"),
        ("RpsSc300Mib", "lvdcType"),
        ("RpsSc300Mib", "lvdRemoteManualReconnectTimeoutPeriod"),
        ("RpsSc300Mib", "lvdRemoteManualReconnectTimer"),
        ("RpsSc300Mib", "generatorCurrent"),
        ("RpsSc300Mib", "generatorFailAlarmRecognitionPeriod"),
        ("RpsSc300Mib", "generatorOnFastCharge"),
        ("RpsSc300Mib", "generatorOnEqualize"),
        ("RpsSc300Mib", "generatorOnAcPeakLoadReduction"),
        ("RpsSc300Mib", "generatorOnMainsFailure"),
        ("RpsSc300Mib", "acSupplyState"),
        ("RpsSc300Mib", "generatorRunTimeRemaining"),
        ("RpsSc300Mib", "generatorState"),
        ("RpsSc300Mib", "generatorRefuelDate"),
        ("RpsSc300Mib", "generatorRefuelVolume"),
        ("RpsSc300Mib", "generatorBackupTime"),
        ("RpsSc300Mib", "tankEmptyDateTime"),
        ("RpsSc300Mib", "fuelLevel"),
        ("RpsSc300Mib", "generatorControlRelay"),
        ("RpsSc300Mib", "generatorStartupWiring"),
        ("RpsSc300Mib", "manualGeneratorRunTime"),
        ("RpsSc300Mib", "fuelTankVolume"),
        ("RpsSc300Mib", "manualGeneratorStart"),
        ("RpsSc300Mib", "manualGeneratorStop"),
        ("RpsSc300Mib", "clearFuelConsumptionHistory"),
        ("RpsSc300Mib", "peakLoadReductionState"),
        ("RpsSc300Mib", "enablePeakLoadReduction"),
        ("RpsSc300Mib", "peakLoadReductionRunningTime"),
        ("RpsSc300Mib", "peakLoadReductionOffsetVoltage"),
        ("RpsSc300Mib", "peakLoadReductionSmartAlarm"),
        ("RpsSc300Mib", "peakLoadReductionMaxDuration"),
        ("RpsSc300Mib", "peakLoadReductionLowVoltageLimit"),
        ("RpsSc300Mib", "peakLoadReductionScheduledStartTime"),
        ("RpsSc300Mib", "peakLoadReductionScheduledDuration"),
        ("RpsSc300Mib", "energyMeterName"),
        ("RpsSc300Mib", "energyMeterGroup"),
        ("RpsSc300Mib", "energyMeter"),
        ("RpsSc300Mib", "resetEnergyMeter"),
        ("RpsSc300Mib", "energyResetDate"),
        ("RpsSc300Mib", "currentMeter"),
        ("RpsSc300Mib", "voltageMeter"),
        ("RpsSc300Mib", "powerMeter"),
        ("RpsSc300Mib", "powerMeterMin"),
        ("RpsSc300Mib", "powerMeterMax"),
        ("RpsSc300Mib", "resetPowerMeterRange"),
        ("RpsSc300Mib", "powerMeterGain"),
        ("RpsSc300Mib", "powerMeterOffset"),
        ("RpsSc300Mib", "energyMeterMeter"),
        ("RpsSc300Mib", "energyMeterAi"),
        ("RpsSc300Mib", "energyMeterAiFunction"),
        ("RpsSc300Mib", "energyMeterMeterNumber"),
        ("RpsSc300Mib", "energyMeterSystemValue"),
        ("RpsSc300Mib", "energyMeterSystemValueIndex"),
        ("RpsSc300Mib", "resetAllEnergyMeters"),
        ("RpsSc300Mib", "resetAllPowerMeterRanges"),
        ("RpsSc300Mib", "setFanPowerRunningTime"),
        ("RpsSc300Mib", "fanControllerProfile"),
        ("RpsSc300Mib", "rxpFcFaults"),
        ("RpsSc300Mib", "fanTemperature"),
        ("RpsSc300Mib", "fanPower"),
        ("RpsSc300Mib", "setFanPower"),
        ("RpsSc300Mib", "fanPoles"),
        ("RpsSc300Mib", "fanSpeedA"),
        ("RpsSc300Mib", "fanSpeedB"),
        ("RpsSc300Mib", "fanControllerMode"),
        ("RpsSc300Mib", "setFanPowerPeriod"),
        ("RpsSc300Mib", "applySetPower"),
        ("RpsSc300Mib", "fc1pTemperature"),
        ("RpsSc300Mib", "fc1pPower"),
        ("RpsSc300Mib", "fc1sTemperature"),
        ("RpsSc300Mib", "fc1sPower"),
        ("RpsSc300Mib", "fc2pTemperature"),
        ("RpsSc300Mib", "fc2pPower"),
        ("RpsSc300Mib", "fc2sTemperature"),
        ("RpsSc300Mib", "fc2sPower"),
        ("RpsSc300Mib", "fanControllerSmartAlarm"),
        ("RpsSc300Mib", "controllerTime"),
        ("RpsSc300Mib", "aiHighState"),
        ("RpsSc300Mib", "aiLowState"),
        ("RpsSc300Mib", "aiValue"),
        ("RpsSc300Mib", "aiStatus"),
        ("RpsSc300Mib", "aiName"),
        ("RpsSc300Mib", "aiFunction"),
        ("RpsSc300Mib", "aiFunctionIndex"),
        ("RpsSc300Mib", "aiUnits"),
        ("RpsSc300Mib", "aiIobNumber"),
        ("RpsSc300Mib", "inputNumber"),
        ("RpsSc300Mib", "gain"),
        ("RpsSc300Mib", "offset"),
        ("RpsSc300Mib", "hysteresis"),
        ("RpsSc300Mib", "highSeverity"),
        ("RpsSc300Mib", "highThreshold"),
        ("RpsSc300Mib", "highDoMappingA"),
        ("RpsSc300Mib", "highDoMappingB"),
        ("RpsSc300Mib", "highTrapSend"),
        ("RpsSc300Mib", "lowSeverity"),
        ("RpsSc300Mib", "lowThreshold"),
        ("RpsSc300Mib", "lowDoMappingA"),
        ("RpsSc300Mib", "lowDoMappingB"),
        ("RpsSc300Mib", "lowTrapSend"),
        ("RpsSc300Mib", "aiGroup"),
        ("RpsSc300Mib", "aiHighNotes"),
        ("RpsSc300Mib", "aiLowNotes"),
        ("RpsSc300Mib", "name"),
        ("RpsSc300Mib", "group"),
        ("RpsSc300Mib", "value"),
        ("RpsSc300Mib", "type"),
        ("RpsSc300Mib", "units"),
        ("RpsSc300Mib", "smartAnalogGate"),
        ("RpsSc300Mib", "saiFunction"),
        ("RpsSc300Mib", "saiFunctionIndex"),
        ("RpsSc300Mib", "smartAnalogSystemInputMapping"),
        ("RpsSc300Mib", "smartAnalogSystemInputValue"),
        ("RpsSc300Mib", "smartAnalogSystemInput"),
        ("RpsSc300Mib", "smartAnalogSystemInputIndex"),
        ("RpsSc300Mib", "smartAnalogSystemInputInvert"),
        ("RpsSc300Mib", "alternativeSourceCurrent"),
        ("RpsSc300Mib", "mainsFail"),
        ("RpsSc300Mib", "fanFail"),
        ("RpsSc300Mib", "movFail"),
        ("RpsSc300Mib", "loadFuseFail"),
        ("RpsSc300Mib", "batteryFuseFail"),
        ("RpsSc300Mib", "phaseFail"),
        ("RpsSc300Mib", "diState"),
        ("RpsSc300Mib", "diValue"),
        ("RpsSc300Mib", "diStatus"),
        ("RpsSc300Mib", "diName"),
        ("RpsSc300Mib", "diIobNumber"),
        ("RpsSc300Mib", "digitalInputNumber"),
        ("RpsSc300Mib", "diSeverity"),
        ("RpsSc300Mib", "diRecognitionPeriod"),
        ("RpsSc300Mib", "diDeactivationRecognitionPeriod"),
        ("RpsSc300Mib", "diDoMappingA"),
        ("RpsSc300Mib", "diDoMappingB"),
        ("RpsSc300Mib", "diTrapSend"),
        ("RpsSc300Mib", "diActiveState"),
        ("RpsSc300Mib", "diGroup"),
        ("RpsSc300Mib", "diNotes"),
        ("RpsSc300Mib", "doState"),
        ("RpsSc300Mib", "remoteControlState"),
        ("RpsSc300Mib", "doStatus"),
        ("RpsSc300Mib", "doName"),
        ("RpsSc300Mib", "doIobNumber"),
        ("RpsSc300Mib", "doIobDoNumber"),
        ("RpsSc300Mib", "doActiveState"),
        ("RpsSc300Mib", "doGroup"),
        ("RpsSc300Mib", "doControlTimeoutPeriod"),
        ("RpsSc300Mib", "doControlTimer"),
        ("RpsSc300Mib", "batteryCapacity"),
        ("RpsSc300Mib", "cellsPerString"),
        ("RpsSc300Mib", "batteryTemperature"),
        ("RpsSc300Mib", "batteryCurrent"),
        ("RpsSc300Mib", "batteryType"),
        ("RpsSc300Mib", "btrTimeRemaining"),
        ("RpsSc300Mib", "btrStateOfHealth"),
        ("RpsSc300Mib", "batteryChargeState"),
        ("RpsSc300Mib", "batteryStateThreshold"),
        ("RpsSc300Mib", "endOfChargeAction"),
        ("RpsSc300Mib", "batteryInstalledDate"),
        ("RpsSc300Mib", "batteryDesignEndOfLifeDate"),
        ("RpsSc300Mib", "bsmLockoutPeriod"),
        ("RpsSc300Mib", "bsmConvergencePeriod"),
        ("RpsSc300Mib", "stringFailRecognitionPeriod"),
        ("RpsSc300Mib", "bsmStartThreshold"),
        ("RpsSc300Mib", "bsmStableThreshold"),
        ("RpsSc300Mib", "stringName"),
        ("RpsSc300Mib", "stringState"),
        ("RpsSc300Mib", "firstQuarterPointVoltage"),
        ("RpsSc300Mib", "midPointVoltage"),
        ("RpsSc300Mib", "thirdQuarterPointVoltage"),
        ("RpsSc300Mib", "imbalancePercent"),
        ("RpsSc300Mib", "bsmState"),
        ("RpsSc300Mib", "timeInThisState"),
        ("RpsSc300Mib", "currentBsmThreshold"),
        ("RpsSc300Mib", "referenceVoltage"),
        ("RpsSc300Mib", "clearStringFail"),
        ("RpsSc300Mib", "btrState"),
        ("RpsSc300Mib", "btrEndVoltage"),
        ("RpsSc300Mib", "btrCharacterizationEndVoltage"),
        ("RpsSc300Mib", "btrCharacterizationResult"),
        ("RpsSc300Mib", "btrCharacterizationTime"),
        ("RpsSc300Mib", "btrAutomaticCharacterization"),
        ("RpsSc300Mib", "btrCharacterizationDelay"),
        ("RpsSc300Mib", "btrCharacterizationStart"),
        ("RpsSc300Mib", "btrCharacterizeBattery"),
        ("RpsSc300Mib", "btrStopBatteryCharacterization"),
        ("RpsSc300Mib", "btrCancelWaiting"),
        ("RpsSc300Mib", "btrClearBatteryCharacterization"),
        ("RpsSc300Mib", "batteryCharacterizationInstantaneousQuality"),
        ("RpsSc300Mib", "batteryCharacterizationSample"),
        ("RpsSc300Mib", "batteryCharacterizationTime"),
        ("RpsSc300Mib", "siteBackupTimeRemaining"),
        ("RpsSc300Mib", "siteBackupTime"),
        ("RpsSc300Mib", "dcInputVoltage"),
        ("RpsSc300Mib", "solarPowerShareOffset"),
        ("RpsSc300Mib", "solarPower"),
        ("RpsSc300Mib", "solarCurrent"),
        ("RpsSc300Mib", "solarBaseVoltage"),
        ("RpsSc300Mib", "solarShutdownSmartAlarm"),
        ("RpsSc300Mib", "dcdcType"),
        ("RpsSc300Mib", "dcdcVoltage"),
        ("RpsSc300Mib", "dcdcCurrent"),
        ("RpsSc300Mib", "dcdcPower"),
        ("RpsSc300Mib", "dcdcHeatsinkTemperature"),
        ("RpsSc300Mib", "numberOfRegisteredDcdcConverters"),
        ("RpsSc300Mib", "dcdcOutputVoltageSetpoint"),
        ("RpsSc300Mib", "dcdc12vOutputVoltageSetpoint"),
        ("RpsSc300Mib", "dcdc24vOutputVoltageSetpoint"),
        ("RpsSc300Mib", "dcdc48vOutputVoltageSetpoint"),
        ("RpsSc300Mib", "dcdcCurrentLimit"),
        ("RpsSc300Mib", "dcdc12vCurrentLimit"),
        ("RpsSc300Mib", "dcdc24vCurrentLimit"),
        ("RpsSc300Mib", "dcdc48vCurrentLimit"),
        ("RpsSc300Mib", "dcdcInputVoltageItem"),
        ("RpsSc300Mib", "dcdcInputVoltage"),
        ("RpsSc300Mib", "logFillMonths"),
        ("RpsSc300Mib", "logUsed"),
        ("RpsSc300Mib", "logInterval"),
        ("RpsSc300Mib", "useOffNormal"),
        ("RpsSc300Mib", "logNumberOfEntries"),
        ("RpsSc300Mib", "offNormalInterval"),
        ("RpsSc300Mib", "offNormalOffsetVoltage"),
        ("RpsSc300Mib", "offNormalSmartAlarm"),
        ("RpsSc300Mib", "isOffNormal"),
        ("RpsSc300Mib", "threadName"),
        ("RpsSc300Mib", "threadLoading"),
        ("RpsSc300Mib", "threadPriority"),
        ("RpsSc300Mib", "threadStack"),
        ("RpsSc300Mib", "threadHeap"),
        ("RpsSc300Mib", "threadHighWaterMark"),
        ("RpsSc300Mib", "preemptive"),
        ("RpsSc300Mib", "ramFree"),
        ("RpsSc300Mib", "ramHeap"),
        ("RpsSc300Mib", "ramStack"),
        ("RpsSc300Mib", "summaryAlarmCritical"),
        ("RpsSc300Mib", "summaryAlarmMajor"),
        ("RpsSc300Mib", "summaryAlarmMinor"),
        ("RpsSc300Mib", "resetBatteryTestFailedAlarm"),
        ("RpsSc300Mib", "resetCommsLostAlarm"),
        ("RpsSc300Mib", "resetBatteryTestCancelledAlarm"),
        ("RpsSc300Mib", "resetLowRectifierCapacityAlarm"),
        ("RpsSc300Mib", "alarmInfo"),
        ("RpsSc300Mib", "alarmName"),
        ("RpsSc300Mib", "alarmSeverity"),
        ("RpsSc300Mib", "alarmState"),
        ("RpsSc300Mib", "alarmNotes"),
        ("RpsSc300Mib", "alarmDoMappingA"),
        ("RpsSc300Mib", "alarmDoMappingB"),
        ("RpsSc300Mib", "alarmTrapSend"),
        ("RpsSc300Mib", "alarmStateChangeTime"),
        ("RpsSc300Mib", "enableAudibleAlarmIndication"),
        ("RpsSc300Mib", "alarmRecognitionPeriod"),
        ("RpsSc300Mib", "acFailRecognitionPeriod"),
        ("RpsSc300Mib", "enableHighFloatTracking"),
        ("RpsSc300Mib", "highFloatThreshold"),
        ("RpsSc300Mib", "enableLowFloatTracking"),
        ("RpsSc300Mib", "lowFloatThreshold"),
        ("RpsSc300Mib", "highLoadThreshold"),
        ("RpsSc300Mib", "lowLoadThreshold"),
        ("RpsSc300Mib", "batteryTemperatureHighThreshold"),
        ("RpsSc300Mib", "batteryTemperatureLowThreshold"),
        ("RpsSc300Mib", "systemOverloadType"),
        ("RpsSc300Mib", "systemOverloadTypeB"),
        ("RpsSc300Mib", "systemOverloadRecognitionPeriod"),
        ("RpsSc300Mib", "systemOverloadThreshold"),
        ("RpsSc300Mib", "systemOverloadThresholdB"),
        ("RpsSc300Mib", "inDischargeAlarmCondition"),
        ("RpsSc300Mib", "batteryCurrentSensorFailRecognitionPeriod"),
        ("RpsSc300Mib", "lowRectifierCapacityRedundancy"),
        ("RpsSc300Mib", "lowRectifierCapacityAlarmThreshold"),
        ("RpsSc300Mib", "lowRectifierCapacityRecognitionPeriod"),
        ("RpsSc300Mib", "rectifierCapacityBalance"),
        ("RpsSc300Mib", "smartAlarmTrapSend"),
        ("RpsSc300Mib", "smartAlarmName"),
        ("RpsSc300Mib", "smartAlarmSeverity"),
        ("RpsSc300Mib", "smartAlarmGroup"),
        ("RpsSc300Mib", "smartAlarmNotes"),
        ("RpsSc300Mib", "smartAlarmOperator"),
        ("RpsSc300Mib", "smartAlarmRecognitionPeriod"),
        ("RpsSc300Mib", "smartAlarmDeactivationRecognitionPeriod"),
        ("RpsSc300Mib", "smartAlarmDoMappingA"),
        ("RpsSc300Mib", "smartAlarmDoMappingB"),
        ("RpsSc300Mib", "smartAlarmState"),
        ("RpsSc300Mib", "clearSmartAlarm"),
        ("RpsSc300Mib", "smartAlarmSendEmail"),
        ("RpsSc300Mib", "smartAlarmCountReset"),
        ("RpsSc300Mib", "smartAlarmAlarmSourceTriggerState"),
        ("RpsSc300Mib", "smartAlarmAlarmSourceStatus"),
        ("RpsSc300Mib", "smartAlarmAlarmSourceMapping"),
        ("RpsSc300Mib", "smartAlarmAlarmSourceTrigger"),
        ("RpsSc300Mib", "smartAlarmAlarmSourceType"),
        ("RpsSc300Mib", "smartAlarmAlarmSourceIndex"),
        ("RpsSc300Mib", "smartAlarmAlarmSourceActiveCount"),
        ("RpsSc300Mib", "smartAlarmAlarmSourceInactiveCount"),
        ("RpsSc300Mib", "smartAlarmAlarmSourceCount"),
        ("RpsSc300Mib", "smartAlarmScheduleSourceIsTriggered"),
        ("RpsSc300Mib", "smartAlarmScheduleSourceStatus"),
        ("RpsSc300Mib", "smartAlarmScheduleSourceMapping"),
        ("RpsSc300Mib", "smartAlarmScheduleSourceFirstActivation"),
        ("RpsSc300Mib", "smartAlarmScheduleSourceDuration"),
        ("RpsSc300Mib", "smartAlarmScheduleSourceInterval"),
        ("RpsSc300Mib", "smartAlarmScheduleSourceRepetitions"),
        ("RpsSc300Mib", "smartAlarmScheduleSourceNext"),
        ("RpsSc300Mib", "smartAlarmScheduleSourceEnd"),
        ("RpsSc300Mib", "smartAlarmSystemValueSourceIsTriggered"),
        ("RpsSc300Mib", "smartAlarmSystemValueSourceStatus"),
        ("RpsSc300Mib", "smartAlarmSystemValueAlarmMapping"),
        ("RpsSc300Mib", "smartAlarmSystemValueSourceValue"),
        ("RpsSc300Mib", "smartAlarmSystemValueSourceValueIndex"),
        ("RpsSc300Mib", "smartAlarmSystemValueSourceInput"),
        ("RpsSc300Mib", "smartAlarmSystemValueSourceThresholdType"),
        ("RpsSc300Mib", "smartAlarmSystemValueSourceThreshold"),
        ("RpsSc300Mib", "smartAlarmSystemValueSourceHysteresis"),
        ("RpsSc300Mib", "smartAlarmSystemValueSourceActiveCount"),
        ("RpsSc300Mib", "smartAlarmSystemValueSourceInactiveCount"),
        ("RpsSc300Mib", "smartAlarmSystemValueSourceCount"),
        ("RpsSc300Mib", "smartAlarmIsManualSourceTriggered"),
        ("RpsSc300Mib", "smartAlarmSourceManualStatus"),
        ("RpsSc300Mib", "smartAlarmSourceManualTrigger"),
        ("RpsSc300Mib", "smartAlarmSourceManualMapping"),
        ("RpsSc300Mib", "smartAlarmSourceManualPeriod"),
        ("RpsSc300Mib", "smartAlarmItemMapping"),
        ("RpsSc300Mib", "smartAlarmItemValue"),
        ("RpsSc300Mib", "smartAlarmItemName"),
        ("RpsSc300Mib", "smartAlarmItemTriggerState"),
        ("RpsSc300Mib", "smartAlarmItemThresholdType"),
        ("RpsSc300Mib", "smartAlarmItemThreshold"),
        ("RpsSc300Mib", "smartAlarmItemHysteresis"),
        ("RpsSc300Mib", "trapAlarmOrigin"),
        ("RpsSc300Mib", "trapAlarmName"),
        ("RpsSc300Mib", "trapAlarmNumber"),
        ("RpsSc300Mib", "trapAdditionalText"),
        ("RpsSc300Mib", "trapAlarmKeepSeverity"),
        ("RpsSc300Mib", "dialOutNumberIndex"),
        ("RpsSc300Mib", "smsNotificationIndex"),
        ("RpsSc300Mib", "snmpTrapReceiverIndex"),
        ("RpsSc300Mib", "emailReceiverIndex"),
        ("RpsSc300Mib", "webUserIndex"),
        ("RpsSc300Mib", "rxpIndex"),
        ("RpsSc300Mib", "iobIndex"),
        ("RpsSc300Mib", "rectifierValuesIndex"),
        ("RpsSc300Mib", "lvdIndex"),
        ("RpsSc300Mib", "lvdcIndex"),
        ("RpsSc300Mib", "energyMeterIndex"),
        ("RpsSc300Mib", "energyMeterAiMappingIndex"),
        ("RpsSc300Mib", "energyMeterValueMappingIndex"),
        ("RpsSc300Mib", "fanControllerStateIndex"),
        ("RpsSc300Mib", "fanController1PrimaryIndex"),
        ("RpsSc300Mib", "fanController1SecondaryIndex"),
        ("RpsSc300Mib", "fanController2PrimaryIndex"),
        ("RpsSc300Mib", "fanController2SecondaryIndex"),
        ("RpsSc300Mib", "analogInputIndex"),
        ("RpsSc300Mib", "smartAnalogIndex"),
        ("RpsSc300Mib", "smartAnalogMappingIndex"),
        ("RpsSc300Mib", "digitalInputIndex"),
        ("RpsSc300Mib", "digitalOutputIndex"),
        ("RpsSc300Mib", "midpointMonitoringStringIndex"),
        ("RpsSc300Mib", "threadLoadingIndex"),
        ("RpsSc300Mib", "alarmIndex"),
        ("RpsSc300Mib", "smartAlarmIndex"),
        ("RpsSc300Mib", "sourceAlarmIndex"),
        ("RpsSc300Mib", "sourceScheduleIndex"),
        ("RpsSc300Mib", "systemValueSourceIndex"),
        ("RpsSc300Mib", "sourceManualIndex"),
        ("RpsSc300Mib", "smartAlarmNamedItemsIndex"),
        ("RpsSc300Mib", "ipAddressType"))
)
if mibBuilder.loadTexts:
    systemObjectGroup.setStatus("current")


# Notification objects

majorAlarmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 100)
)
majorAlarmActive.setObjects(
      *(("RpsSc300Mib", "alarmIndex"),
        ("RpsSc300Mib", "alarmName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "alarmNotes"))
)
if mibBuilder.loadTexts:
    majorAlarmActive.setStatus(
        "current"
    )

majorAiHighActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 101)
)
majorAiHighActive.setObjects(
      *(("RpsSc300Mib", "analogInputIndex"),
        ("RpsSc300Mib", "aiName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "aiHighNotes"))
)
if mibBuilder.loadTexts:
    majorAiHighActive.setStatus(
        "current"
    )

majorAiLowActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 102)
)
majorAiLowActive.setObjects(
      *(("RpsSc300Mib", "analogInputIndex"),
        ("RpsSc300Mib", "aiName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "aiLowNotes"))
)
if mibBuilder.loadTexts:
    majorAiLowActive.setStatus(
        "current"
    )

majorDiActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 103)
)
majorDiActive.setObjects(
      *(("RpsSc300Mib", "digitalInputIndex"),
        ("RpsSc300Mib", "diName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "diNotes"))
)
if mibBuilder.loadTexts:
    majorDiActive.setStatus(
        "current"
    )

majorSmartActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 104)
)
majorSmartActive.setObjects(
      *(("RpsSc300Mib", "smartAlarmIndex"),
        ("RpsSc300Mib", "smartAlarmName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "smartAlarmNotes"))
)
if mibBuilder.loadTexts:
    majorSmartActive.setStatus(
        "current"
    )

minorAlarmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 200)
)
minorAlarmActive.setObjects(
      *(("RpsSc300Mib", "alarmIndex"),
        ("RpsSc300Mib", "alarmName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "alarmNotes"))
)
if mibBuilder.loadTexts:
    minorAlarmActive.setStatus(
        "current"
    )

minorAiHighActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 201)
)
minorAiHighActive.setObjects(
      *(("RpsSc300Mib", "analogInputIndex"),
        ("RpsSc300Mib", "aiName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "aiHighNotes"))
)
if mibBuilder.loadTexts:
    minorAiHighActive.setStatus(
        "current"
    )

minorAiLowActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 202)
)
minorAiLowActive.setObjects(
      *(("RpsSc300Mib", "analogInputIndex"),
        ("RpsSc300Mib", "aiName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "aiLowNotes"))
)
if mibBuilder.loadTexts:
    minorAiLowActive.setStatus(
        "current"
    )

minorDiActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 203)
)
minorDiActive.setObjects(
      *(("RpsSc300Mib", "digitalInputIndex"),
        ("RpsSc300Mib", "diName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "diNotes"))
)
if mibBuilder.loadTexts:
    minorDiActive.setStatus(
        "current"
    )

minorSmartActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 204)
)
minorSmartActive.setObjects(
      *(("RpsSc300Mib", "smartAlarmIndex"),
        ("RpsSc300Mib", "smartAlarmName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "smartAlarmNotes"))
)
if mibBuilder.loadTexts:
    minorSmartActive.setStatus(
        "current"
    )

warningAlarmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 300)
)
warningAlarmActive.setObjects(
      *(("RpsSc300Mib", "alarmIndex"),
        ("RpsSc300Mib", "alarmName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "alarmNotes"))
)
if mibBuilder.loadTexts:
    warningAlarmActive.setStatus(
        "current"
    )

warningAiHighActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 301)
)
warningAiHighActive.setObjects(
      *(("RpsSc300Mib", "analogInputIndex"),
        ("RpsSc300Mib", "aiName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "aiHighNotes"))
)
if mibBuilder.loadTexts:
    warningAiHighActive.setStatus(
        "current"
    )

warningAiLowActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 302)
)
warningAiLowActive.setObjects(
      *(("RpsSc300Mib", "analogInputIndex"),
        ("RpsSc300Mib", "aiName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "aiLowNotes"))
)
if mibBuilder.loadTexts:
    warningAiLowActive.setStatus(
        "current"
    )

warningDiActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 303)
)
warningDiActive.setObjects(
      *(("RpsSc300Mib", "digitalInputIndex"),
        ("RpsSc300Mib", "diName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "diNotes"))
)
if mibBuilder.loadTexts:
    warningDiActive.setStatus(
        "current"
    )

warningSmartActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 304)
)
warningSmartActive.setObjects(
      *(("RpsSc300Mib", "smartAlarmIndex"),
        ("RpsSc300Mib", "smartAlarmName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "smartAlarmNotes"))
)
if mibBuilder.loadTexts:
    warningSmartActive.setStatus(
        "current"
    )

alarmInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 400)
)
alarmInactive.setObjects(
      *(("RpsSc300Mib", "alarmIndex"),
        ("RpsSc300Mib", "alarmName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "alarmNotes"))
)
if mibBuilder.loadTexts:
    alarmInactive.setStatus(
        "current"
    )

aiHighInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 401)
)
aiHighInactive.setObjects(
      *(("RpsSc300Mib", "analogInputIndex"),
        ("RpsSc300Mib", "aiName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "aiHighNotes"))
)
if mibBuilder.loadTexts:
    aiHighInactive.setStatus(
        "current"
    )

aiLowInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 402)
)
aiLowInactive.setObjects(
      *(("RpsSc300Mib", "analogInputIndex"),
        ("RpsSc300Mib", "aiName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "aiLowNotes"))
)
if mibBuilder.loadTexts:
    aiLowInactive.setStatus(
        "current"
    )

diInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 403)
)
diInactive.setObjects(
      *(("RpsSc300Mib", "digitalInputIndex"),
        ("RpsSc300Mib", "diName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "diNotes"))
)
if mibBuilder.loadTexts:
    diInactive.setStatus(
        "current"
    )

smartInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 404)
)
smartInactive.setObjects(
      *(("RpsSc300Mib", "smartAlarmIndex"),
        ("RpsSc300Mib", "smartAlarmName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "smartAlarmNotes"))
)
if mibBuilder.loadTexts:
    smartInactive.setStatus(
        "current"
    )

alarmStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 500)
)
alarmStatusChange.setObjects(
      *(("RpsSc300Mib", "serialNumber"),
        ("RpsSc300Mib", "snmpTrapReceiverIndex"))
)
if mibBuilder.loadTexts:
    alarmStatusChange.setStatus(
        "current"
    )

criticalAlarmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 600)
)
criticalAlarmActive.setObjects(
      *(("RpsSc300Mib", "alarmIndex"),
        ("RpsSc300Mib", "alarmName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "alarmNotes"))
)
if mibBuilder.loadTexts:
    criticalAlarmActive.setStatus(
        "current"
    )

criticalAiHighActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 601)
)
criticalAiHighActive.setObjects(
      *(("RpsSc300Mib", "analogInputIndex"),
        ("RpsSc300Mib", "aiName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "aiHighNotes"))
)
if mibBuilder.loadTexts:
    criticalAiHighActive.setStatus(
        "current"
    )

criticalAiLowActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 602)
)
criticalAiLowActive.setObjects(
      *(("RpsSc300Mib", "analogInputIndex"),
        ("RpsSc300Mib", "aiName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "aiLowNotes"))
)
if mibBuilder.loadTexts:
    criticalAiLowActive.setStatus(
        "current"
    )

criticalDiActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 603)
)
criticalDiActive.setObjects(
      *(("RpsSc300Mib", "digitalInputIndex"),
        ("RpsSc300Mib", "diName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "diNotes"))
)
if mibBuilder.loadTexts:
    criticalDiActive.setStatus(
        "current"
    )

criticalSmartActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 604)
)
criticalSmartActive.setObjects(
      *(("RpsSc300Mib", "smartAlarmIndex"),
        ("RpsSc300Mib", "smartAlarmName"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "smartAlarmNotes"))
)
if mibBuilder.loadTexts:
    criticalSmartActive.setStatus(
        "current"
    )

_pysmi_global = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 700)
)
_pysmi_global.setObjects(
      *(("RpsSc300Mib", "trapAlarmNumber"),
        ("RpsSc300Mib", "trapAlarmOrigin"),
        ("RpsSc300Mib", "trapAlarmName"),
        ("RpsSc300Mib", "trapAlarmKeepSeverity"),
        ("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"),
        ("RpsSc300Mib", "trapAdditionalText"))
)
if mibBuilder.loadTexts:
    _pysmi_global.setStatus(
        "current"
    )

heartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 800)
)
heartbeat.setObjects(
      *(("RpsSc300Mib", "systemLocation"),
        ("RpsSc300Mib", "siteName"),
        ("RpsSc300Mib", "siteAddress"),
        ("RpsSc300Mib", "siteBuilding"),
        ("RpsSc300Mib", "siteRoom"),
        ("RpsSc300Mib", "siteContact"),
        ("RpsSc300Mib", "siteSupportContact"))
)
if mibBuilder.loadTexts:
    heartbeat.setStatus(
        "current"
    )


# Notifications groups

systemNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1918, 2, 14, 20, 1)
)
systemNotificationGroup.setObjects(
      *(("RpsSc300Mib", "majorAlarmActive"),
        ("RpsSc300Mib", "majorAiHighActive"),
        ("RpsSc300Mib", "majorAiLowActive"),
        ("RpsSc300Mib", "majorDiActive"),
        ("RpsSc300Mib", "majorSmartActive"),
        ("RpsSc300Mib", "minorAlarmActive"),
        ("RpsSc300Mib", "minorAiHighActive"),
        ("RpsSc300Mib", "minorAiLowActive"),
        ("RpsSc300Mib", "minorDiActive"),
        ("RpsSc300Mib", "minorSmartActive"),
        ("RpsSc300Mib", "warningAlarmActive"),
        ("RpsSc300Mib", "warningAiHighActive"),
        ("RpsSc300Mib", "warningAiLowActive"),
        ("RpsSc300Mib", "warningDiActive"),
        ("RpsSc300Mib", "warningSmartActive"),
        ("RpsSc300Mib", "alarmInactive"),
        ("RpsSc300Mib", "aiHighInactive"),
        ("RpsSc300Mib", "aiLowInactive"),
        ("RpsSc300Mib", "diInactive"),
        ("RpsSc300Mib", "smartInactive"),
        ("RpsSc300Mib", "alarmStatusChange"),
        ("RpsSc300Mib", "criticalAlarmActive"),
        ("RpsSc300Mib", "criticalAiHighActive"),
        ("RpsSc300Mib", "criticalAiLowActive"),
        ("RpsSc300Mib", "criticalDiActive"),
        ("RpsSc300Mib", "criticalSmartActive"),
        ("RpsSc300Mib", "global"),
        ("RpsSc300Mib", "heartbeat"))
)
if mibBuilder.loadTexts:
    systemNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RpsSc300Mib",
    **{"Signed8": Signed8,
       "Signed16": Signed16,
       "Signed32": Signed32,
       "Unsigned8": Unsigned8,
       "Unsigned16": Unsigned16,
       "Unsigned31": Unsigned31,
       "UnsignedNan8": UnsignedNan8,
       "UnsignedNan16": UnsignedNan16,
       "UnsignedNan32": UnsignedNan32,
       "Boolean": Boolean,
       "Float": Float,
       "NoData": NoData,
       "TimeIntervalInSeconds": TimeIntervalInSeconds,
       "TimeIntervalInMinutes": TimeIntervalInMinutes,
       "TimeIntervalInDays": TimeIntervalInDays,
       "JulianTimeUtc": JulianTimeUtc,
       "JulianDateUtc": JulianDateUtc,
       "JulianDateUtc25": JulianDateUtc25,
       "EnableState": EnableState,
       "BaudRate": BaudRate,
       "Parity": Parity,
       "StopBits": StopBits,
       "SnmpTrapVersion": SnmpTrapVersion,
       "SeverityLevel": SeverityLevel,
       "YesNo": YesNo,
       "Sysoid": Sysoid,
       "UserSnmp": UserSnmp,
       "WebAccess": WebAccess,
       "ThreadPriority": ThreadPriority,
       "RectifierShutdownMode": RectifierShutdownMode,
       "DcdcHardwareType": DcdcHardwareType,
       "InputType": InputType,
       "DcPower": DcPower,
       "Percentile8Nan": Percentile8Nan,
       "ProductType": ProductType,
       "AccessLevel": AccessLevel,
       "SnmpAccessState": SnmpAccessState,
       "GenericTrapsEnable": GenericTrapsEnable,
       "SendTrap": SendTrap,
       "AlarmReport": AlarmReport,
       "SnmpTrapFormat": SnmpTrapFormat,
       "AccessProtection": AccessProtection,
       "CanStart": CanStart,
       "AvcState": AvcState,
       "TcState": TcState,
       "BatteryTestState": BatteryTestState,
       "BatteryChargeState": BatteryChargeState,
       "BclState": BclState,
       "EngineRunState": EngineRunState,
       "RcpSlaveState": RcpSlaveState,
       "TrapAlarmKeepSeverity": TrapAlarmKeepSeverity,
       "AlarmSeverity": AlarmSeverity,
       "TrapReceiverMode": TrapReceiverMode,
       "ControlState": ControlState,
       "ControlProcessState": ControlProcessState,
       "PeakLoadReductionState": PeakLoadReductionState,
       "ExternalRelayState": ExternalRelayState,
       "RelayControlState": RelayControlState,
       "RectFailState": RectFailState,
       "AcPhase": AcPhase,
       "AlarmType": AlarmType,
       "SystemState": SystemState,
       "BtrState": BtrState,
       "EndOfChargeAction": EndOfChargeAction,
       "AlarmActiveState": AlarmActiveState,
       "AlarmOperator": AlarmOperator,
       "SourceTrigger": SourceTrigger,
       "SourceState": SourceState,
       "InDischargeAlarmCondition": InDischargeAlarmCondition,
       "ThresholdType": ThresholdType,
       "SystemValueSourceValue": SystemValueSourceValue,
       "SystemAlarm": SystemAlarm,
       "EnergizeState": EnergizeState,
       "RelayMapping": RelayMapping,
       "AiFunction": AiFunction,
       "SmartAnalogType": SmartAnalogType,
       "SmartAnalogGate": SmartAnalogGate,
       "ActiveState": ActiveState,
       "DigitalInputState": DigitalInputState,
       "MeasurementUnits": MeasurementUnits,
       "OverloadAlarmType": OverloadAlarmType,
       "RxpSlaveType": RxpSlaveType,
       "BsmState": BsmState,
       "BsmBatteryState": BsmBatteryState,
       "LvdState": LvdState,
       "LvdcType": LvdcType,
       "LvdcState": LvdcState,
       "BtrCharacterizationResult": BtrCharacterizationResult,
       "GeneratorStartupWiring": GeneratorStartupWiring,
       "EnergyMeterAiFunction": EnergyMeterAiFunction,
       "EnergyMeterSystemValue": EnergyMeterSystemValue,
       "LogItems": LogItems,
       "Redundancy": Redundancy,
       "PreventBatteryTest": PreventBatteryTest,
       "FanControllerMode": FanControllerMode,
       "FanControllerProfile": FanControllerProfile,
       "SystemInputType": SystemInputType,
       "GenericSystemType": GenericSystemType,
       "S3pAccess": S3pAccess,
       "String7": String7,
       "String10": String10,
       "String16": String16,
       "String17": String17,
       "String20": String20,
       "String30": String30,
       "String32": String32,
       "String40": String40,
       "String60": String60,
       "String64": String64,
       "String100": String100,
       "String150": String150,
       "String253": String253,
       "eatonChNz": eatonChNz,
       "dcPowerSystem": dcPowerSystem,
       "rpsSc300": rpsSc300,
       "rpsSc300MibModule": rpsSc300MibModule,
       "ipAddressType": ipAddressType,
       "rpsObjects": rpsObjects,
       "systemIdentity": systemIdentity,
       "systemObjectGroup": systemObjectGroup,
       "systemManufacturer": systemManufacturer,
       "systemSerialNumber": systemSerialNumber,
       "systemType": systemType,
       "systemLocation": systemLocation,
       "siteName": siteName,
       "siteAddress": siteAddress,
       "siteNotes": siteNotes,
       "systemObjectId2": systemObjectId2,
       "trapFormat": trapFormat,
       "genericTrapsEnable": genericTrapsEnable,
       "configurationName": configurationName,
       "configurationVersion": configurationVersion,
       "configurationModified": configurationModified,
       "siteBuilding": siteBuilding,
       "siteRoom": siteRoom,
       "siteContact": siteContact,
       "siteSupportContact": siteSupportContact,
       "isThreePhaseSystem": isThreePhaseSystem,
       "controller": controller,
       "manufacturerName": manufacturerName,
       "productType": productType,
       "softwareVersion": softwareVersion,
       "bootVersion": bootVersion,
       "interfaceVersion": interfaceVersion,
       "hardwareVersion": hardwareVersion,
       "lcdVersion": lcdVersion,
       "batteryMonitor": batteryMonitor,
       "serialNumber": serialNumber,
       "ethernetMacAddress": ethernetMacAddress,
       "subversionRevision": subversionRevision,
       "evaluationSoftwareFound": evaluationSoftwareFound,
       "genericSystemType": genericSystemType,
       "communications": communications,
       "s3pAccess": s3pAccess,
       "snmpAccess": snmpAccess,
       "serialServerAccess": serialServerAccess,
       "serialServerPort": serialServerPort,
       "s3pAddress": s3pAddress,
       "ipAddress": ipAddress,
       "subnetMask": subnetMask,
       "gatewayAddress": gatewayAddress,
       "vlanId": vlanId,
       "serial": serial,
       "portSettings": portSettings,
       "baudRate": baudRate,
       "parity": parity,
       "stopBits": stopBits,
       "enableModem": enableModem,
       "alarmReport": alarmReport,
       "modemSetUpString": modemSetUpString,
       "modemAutoAnswerRings": modemAutoAnswerRings,
       "modemMaximumRetries": modemMaximumRetries,
       "modemRetryInterval": modemRetryInterval,
       "modemPowerReset": modemPowerReset,
       "dialOutNumberTable": dialOutNumberTable,
       "dialOutNumberEntry": dialOutNumberEntry,
       "dialOutNumberIndex": dialOutNumberIndex,
       "dialOutNumber": dialOutNumber,
       "smsNotificationTable": smsNotificationTable,
       "smsNotificationEntry": smsNotificationEntry,
       "smsNotificationIndex": smsNotificationIndex,
       "smsPhoneName": smsPhoneName,
       "smsLevel": smsLevel,
       "smsPhoneNumber": smsPhoneNumber,
       "smsPrefix": smsPrefix,
       "smsEmailGateway": smsEmailGateway,
       "modbus": modbus,
       "modbusAccess": modbusAccess,
       "modbusAddress": modbusAddress,
       "modbusInterfaceVersion": modbusInterfaceVersion,
       "snmpSettings": snmpSettings,
       "snmpReadCommunity": snmpReadCommunity,
       "snmpWriteCommunity": snmpWriteCommunity,
       "enableTrapRepeat": enableTrapRepeat,
       "trapRepeatRate": trapRepeatRate,
       "trapVersion": trapVersion,
       "snmpTrapReceiverTable": snmpTrapReceiverTable,
       "snmpTrapReceiverEntry": snmpTrapReceiverEntry,
       "snmpTrapReceiverIndex": snmpTrapReceiverIndex,
       "trapReceiverIpAddress": trapReceiverIpAddress,
       "trapReceiverPort": trapReceiverPort,
       "trapReceiverName": trapReceiverName,
       "trapReceiverLevel": trapReceiverLevel,
       "trapReceiverCommunity": trapReceiverCommunity,
       "trapReceiverMode": trapReceiverMode,
       "acknowledgeAlarmSummaryTrap": acknowledgeAlarmSummaryTrap,
       "snmpV3PrivacyPassword": snmpV3PrivacyPassword,
       "enableHeartbeatTrap": enableHeartbeatTrap,
       "heartbeatTrapPeriod": heartbeatTrapPeriod,
       "email": email,
       "emailNotifications": emailNotifications,
       "smtpServerIpAddress": smtpServerIpAddress,
       "smtpServerPort": smtpServerPort,
       "emailReturnAddress": emailReturnAddress,
       "emailFromAddress": emailFromAddress,
       "emailValidAddress": emailValidAddress,
       "emailSubjectPrefix": emailSubjectPrefix,
       "emailReceiverTable": emailReceiverTable,
       "emailReceiverEntry": emailReceiverEntry,
       "emailReceiverIndex": emailReceiverIndex,
       "emailReceiverAddress": emailReceiverAddress,
       "emailReceiverLevel": emailReceiverLevel,
       "emailReceiverDelay": emailReceiverDelay,
       "sendTestEmail": sendTestEmail,
       "smtpResult": smtpResult,
       "sntp": sntp,
       "sntpPollInterval": sntpPollInterval,
       "udpPort": udpPort,
       "primaryAddress": primaryAddress,
       "backupAddress": backupAddress,
       "sntpLastUpdate": sntpLastUpdate,
       "webUserTable": webUserTable,
       "webUserEntry": webUserEntry,
       "webUserIndex": webUserIndex,
       "userName": userName,
       "userLogonId": userLogonId,
       "userLogonPassword": userLogonPassword,
       "userActive": userActive,
       "userWrite": userWrite,
       "userRestore": userRestore,
       "userBackup": userBackup,
       "userExecute": userExecute,
       "userUpgradeFirmware": userUpgradeFirmware,
       "userAdministrator": userAdministrator,
       "userSnmp": userSnmp,
       "radius": radius,
       "authServer": authServer,
       "radiusAuthSvrSecret": radiusAuthSvrSecret,
       "acctServer": acctServer,
       "radiusAcctSvrSecret": radiusAcctSvrSecret,
       "ipAddressAuto": ipAddressAuto,
       "subnetMaskAuto": subnetMaskAuto,
       "gatewayAddressAuto": gatewayAddressAuto,
       "autoIp": autoIp,
       "webSessionTimeout": webSessionTimeout,
       "webAccess": webAccess,
       "blacklist": blacklist,
       "blacklisted": blacklisted,
       "accessControl": accessControl,
       "uiAccess": uiAccess,
       "s3pWriteAccessPassword": s3pWriteAccessPassword,
       "remoteAccessLevel": remoteAccessLevel,
       "uploadingFirmware": uploadingFirmware,
       "acInput": acInput,
       "acVoltage": acVoltage,
       "phase1": phase1,
       "phase2": phase2,
       "phase3": phase3,
       "dcOutput": dcOutput,
       "loadCurrent": loadCurrent,
       "systemPower": systemPower,
       "loadPower": loadPower,
       "rxp": rxp,
       "rxpTable": rxpTable,
       "rxpEntry": rxpEntry,
       "rxpIndex": rxpIndex,
       "rxpSlaveRegistrationState": rxpSlaveRegistrationState,
       "rxpSlaveName": rxpSlaveName,
       "rxpSlaveSerialNumber": rxpSlaveSerialNumber,
       "rxpSlaveType": rxpSlaveType,
       "rxpSlaveCommandSet": rxpSlaveCommandSet,
       "rxpBomRevision": rxpBomRevision,
       "rxpSoftwareVersion": rxpSoftwareVersion,
       "identifyRxpSlave": identifyRxpSlave,
       "iobTable": iobTable,
       "iobEntry": iobEntry,
       "iobIndex": iobIndex,
       "iobRegistrationState": iobRegistrationState,
       "iobSerialNumber": iobSerialNumber,
       "iobMapping": iobMapping,
       "iobNumberOfVoltages": iobNumberOfVoltages,
       "iobNumberOfCurrents": iobNumberOfCurrents,
       "iobNumberOfTemperatures": iobNumberOfTemperatures,
       "iobNumberOfDigitalInputs": iobNumberOfDigitalInputs,
       "iobNumberOfRelays": iobNumberOfRelays,
       "iobNumberOfLvds": iobNumberOfLvds,
       "rectifiers": rectifiers,
       "numberOfRegisteredRectifiers": numberOfRegisteredRectifiers,
       "numberOfRegisteredSolarChargers": numberOfRegisteredSolarChargers,
       "numberOfRectifiersFailed": numberOfRectifiersFailed,
       "numberOfSolarFailed": numberOfSolarFailed,
       "numberOfRectifiersCommsLost": numberOfRectifiersCommsLost,
       "numberOfSolarCommsLost": numberOfSolarCommsLost,
       "rectifierCurrent": rectifierCurrent,
       "rectifierCurrentLimit": rectifierCurrentLimit,
       "solarCurrentLimit": solarCurrentLimit,
       "enableCurrentShare": enableCurrentShare,
       "highestRectifierHeatsinkTemperature": highestRectifierHeatsinkTemperature,
       "rectifierValuesTable": rectifierValuesTable,
       "rectifierValuesEntry": rectifierValuesEntry,
       "rectifierValuesIndex": rectifierValuesIndex,
       "rectifierSerialNumber": rectifierSerialNumber,
       "rectifierType": rectifierType,
       "rectifierInputType": rectifierInputType,
       "rectifierStatus": rectifierStatus,
       "rectifierMaximumCurrentLimit": rectifierMaximumCurrentLimit,
       "rectifierMaximumPowerLimit": rectifierMaximumPowerLimit,
       "rectifierMinimumOvsdSetPoint": rectifierMinimumOvsdSetPoint,
       "rectifierMaximumOvsdSetPoint": rectifierMaximumOvsdSetPoint,
       "rectifierInputVoltage": rectifierInputVoltage,
       "rectifierReportedVoltage": rectifierReportedVoltage,
       "rectifierReportedCurrent": rectifierReportedCurrent,
       "rectifierOutputPowerw": rectifierOutputPowerw,
       "rectifierOutputPower": rectifierOutputPower,
       "rectifierHeatsinkTemperature": rectifierHeatsinkTemperature,
       "rectifierRegistrationState": rectifierRegistrationState,
       "rectifierFailedState": rectifierFailedState,
       "loadBasedRunTime": loadBasedRunTime,
       "shutdownRectifier": shutdownRectifier,
       "rectifierHasBeenShutdown": rectifierHasBeenShutdown,
       "rectifierPhase1": rectifierPhase1,
       "rectifierPhase2": rectifierPhase2,
       "rectifierPhase3": rectifierPhase3,
       "rectifierNotes": rectifierNotes,
       "rectifierInputCurrent": rectifierInputCurrent,
       "rectifierPhase": rectifierPhase,
       "phase1SerialNumber": phase1SerialNumber,
       "acInputCurrent": acInputCurrent,
       "dcInputCurrent": dcInputCurrent,
       "rectifierShutdownMode": rectifierShutdownMode,
       "restartAllRectifiers": restartAllRectifiers,
       "rectifierShutdownSmartAlarm": rectifierShutdownSmartAlarm,
       "loadBasedRectifierShutdownConfig": loadBasedRectifierShutdownConfig,
       "rectCycleLowThreshold": rectCycleLowThreshold,
       "rectCycleHighThreshold": rectCycleHighThreshold,
       "rectCycleInterval": rectCycleInterval,
       "redundancy": redundancy,
       "resetRunTimes": resetRunTimes,
       "rampUpSlope": rampUpSlope,
       "ovsdSetPoint": ovsdSetPoint,
       "rectifierStartUpDelay": rectifierStartUpDelay,
       "enableRipPowerShare": enableRipPowerShare,
       "controlFunctions": controlFunctions,
       "controlState": controlState,
       "voltageControl": voltageControl,
       "floatVoltage": floatVoltage,
       "alternativeFloatVoltage": alternativeFloatVoltage,
       "alternativeFloatSmartAlarm": alternativeFloatSmartAlarm,
       "alternativeFloatStatus": alternativeFloatStatus,
       "maximumSystemVoltage": maximumSystemVoltage,
       "minimumSystemVoltage": minimumSystemVoltage,
       "busVoltage": busVoltage,
       "targetVoltage": targetVoltage,
       "enableActiveVoltageControl": enableActiveVoltageControl,
       "avcState": avcState,
       "avcOffset": avcOffset,
       "baseVoltage": baseVoltage,
       "temperatureCompensation": temperatureCompensation,
       "enableTemperatureCompensation": enableTemperatureCompensation,
       "temperatureCompensationAllowed": temperatureCompensationAllowed,
       "temperatureCompensationState": temperatureCompensationState,
       "temperatureCompensationSlope": temperatureCompensationSlope,
       "temperatureCompensationReferenceTemperature": temperatureCompensationReferenceTemperature,
       "temperatureCompensationUpperLimit": temperatureCompensationUpperLimit,
       "temperatureCompensationLowerLimit": temperatureCompensationLowerLimit,
       "temperatureCompensationOffsetVoltage": temperatureCompensationOffsetVoltage,
       "resetAhDischarged": resetAhDischarged,
       "ahDischargedFloatResetRate": ahDischargedFloatResetRate,
       "equalize": equalize,
       "enableEqualize": enableEqualize,
       "equalizeStartAllowed": equalizeStartAllowed,
       "equalizeState": equalizeState,
       "equalizeVoltage": equalizeVoltage,
       "equalizeOffsetVoltage": equalizeOffsetVoltage,
       "periodicEqualizeFirstDateTime": periodicEqualizeFirstDateTime,
       "equalizeInterval": equalizeInterval,
       "nextEqualizeStartTime": nextEqualizeStartTime,
       "equalizeDuration": equalizeDuration,
       "equalizeRemainingTime": equalizeRemainingTime,
       "startEqualize": startEqualize,
       "stopEqualize": stopEqualize,
       "equalizeSmartAlarm": equalizeSmartAlarm,
       "fastCharge": fastCharge,
       "enableFastCharge": enableFastCharge,
       "fastChargeState": fastChargeState,
       "fastChargeStartAllowed": fastChargeStartAllowed,
       "fastChargeVoltage": fastChargeVoltage,
       "fastChargeOffsetVoltage": fastChargeOffsetVoltage,
       "fastChargeAhDischarged": fastChargeAhDischarged,
       "fastChargeMaximumDuration": fastChargeMaximumDuration,
       "fastChargeAmpereHourThreshold": fastChargeAmpereHourThreshold,
       "fastChargeVoltageThreshold": fastChargeVoltageThreshold,
       "fastChargeRechargePercentage": fastChargeRechargePercentage,
       "fastChargeAmpereHourStopThreshold": fastChargeAmpereHourStopThreshold,
       "fastChargeMaximumTimeRemaining": fastChargeMaximumTimeRemaining,
       "stopFastCharge": stopFastCharge,
       "batteryCurrentLimit": batteryCurrentLimit,
       "enableBatteryCurrentLimit": enableBatteryCurrentLimit,
       "bclState": bclState,
       "bclLimit": bclLimit,
       "bclOffsetVoltage": bclOffsetVoltage,
       "bclEngineRunLimit": bclEngineRunLimit,
       "batteryTest": batteryTest,
       "enableBatteryTest": enableBatteryTest,
       "preventBatteryTest": preventBatteryTest,
       "batteryTestStartAllowed": batteryTestStartAllowed,
       "batteryTestLockoutRemaining": batteryTestLockoutRemaining,
       "batteryTestState": batteryTestState,
       "batteryTestFirstDateTime": batteryTestFirstDateTime,
       "batteryTestInterval": batteryTestInterval,
       "nextBatteryTestStartTime": nextBatteryTestStartTime,
       "batteryTestDuration": batteryTestDuration,
       "batteryTestRemainingTime": batteryTestRemainingTime,
       "batteryTestTerminationVoltage": batteryTestTerminationVoltage,
       "batteryTestOffsetVoltage": batteryTestOffsetVoltage,
       "startBatteryTest": startBatteryTest,
       "stopBatteryTest": stopBatteryTest,
       "allowBatteryTestDuringLockout": allowBatteryTestDuringLockout,
       "bBatteryTestOffsetVoltage": bBatteryTestOffsetVoltage,
       "lvd": lvd,
       "lvdInhibitPeriod": lvdInhibitPeriod,
       "allowFrontPanelLvdControl": allowFrontPanelLvdControl,
       "lvdTable": lvdTable,
       "lvdEntry": lvdEntry,
       "lvdIndex": lvdIndex,
       "lvdName": lvdName,
       "lvdState": lvdState,
       "lvdInhibited": lvdInhibited,
       "enableLvdVoltageDisconnect": enableLvdVoltageDisconnect,
       "lvdDisconnectVoltage": lvdDisconnectVoltage,
       "lvdReconnectVoltage": lvdReconnectVoltage,
       "lvdRecognitionPeriod": lvdRecognitionPeriod,
       "enableLvdAcTimer": enableLvdAcTimer,
       "lvdAcTimerDisconnectDelay": lvdAcTimerDisconnectDelay,
       "enableLvdSaDisconnect": enableLvdSaDisconnect,
       "lvdSaDisconnectIndex": lvdSaDisconnectIndex,
       "enableLvdChainedToPrevious": enableLvdChainedToPrevious,
       "lvdRemoteManualControl": lvdRemoteManualControl,
       "lvdcTable": lvdcTable,
       "lvdcEntry": lvdcEntry,
       "lvdcIndex": lvdcIndex,
       "lvdcLvdMapping": lvdcLvdMapping,
       "lvdcState": lvdcState,
       "enableLvdc": enableLvdc,
       "lvdcIobNumber": lvdcIobNumber,
       "lvdcIobLvdNumber": lvdcIobLvdNumber,
       "lvdcType": lvdcType,
       "lvdRemoteManualReconnectTimeoutPeriod": lvdRemoteManualReconnectTimeoutPeriod,
       "lvdRemoteManualReconnectTimer": lvdRemoteManualReconnectTimer,
       "generatorControl": generatorControl,
       "generatorCurrent": generatorCurrent,
       "generatorFailAlarmRecognitionPeriod": generatorFailAlarmRecognitionPeriod,
       "generatorOnFastCharge": generatorOnFastCharge,
       "generatorOnEqualize": generatorOnEqualize,
       "generatorOnAcPeakLoadReduction": generatorOnAcPeakLoadReduction,
       "generatorOnMainsFailure": generatorOnMainsFailure,
       "acSupplyState": acSupplyState,
       "generatorRunTimeRemaining": generatorRunTimeRemaining,
       "generatorState": generatorState,
       "generatorRefuelDate": generatorRefuelDate,
       "generatorRefuelVolume": generatorRefuelVolume,
       "generatorBackupTime": generatorBackupTime,
       "tankEmptyDateTime": tankEmptyDateTime,
       "fuelLevel": fuelLevel,
       "generatorControlRelay": generatorControlRelay,
       "generatorStartupWiring": generatorStartupWiring,
       "manualGeneratorRunTime": manualGeneratorRunTime,
       "fuelTankVolume": fuelTankVolume,
       "manualGeneratorStart": manualGeneratorStart,
       "manualGeneratorStop": manualGeneratorStop,
       "clearFuelConsumptionHistory": clearFuelConsumptionHistory,
       "peakLoadReduction": peakLoadReduction,
       "peakLoadReductionState": peakLoadReductionState,
       "enablePeakLoadReduction": enablePeakLoadReduction,
       "peakLoadReductionRunningTime": peakLoadReductionRunningTime,
       "peakLoadReductionOffsetVoltage": peakLoadReductionOffsetVoltage,
       "peakLoadReductionSmartAlarm": peakLoadReductionSmartAlarm,
       "peakLoadReductionMaxDuration": peakLoadReductionMaxDuration,
       "peakLoadReductionLowVoltageLimit": peakLoadReductionLowVoltageLimit,
       "peakLoadReductionScheduledStartTime": peakLoadReductionScheduledStartTime,
       "peakLoadReductionScheduledDuration": peakLoadReductionScheduledDuration,
       "energyMeters": energyMeters,
       "energyMeterTable": energyMeterTable,
       "energyMeterEntry": energyMeterEntry,
       "energyMeterIndex": energyMeterIndex,
       "energyMeterName": energyMeterName,
       "energyMeterGroup": energyMeterGroup,
       "energyMeter": energyMeter,
       "resetEnergyMeter": resetEnergyMeter,
       "energyResetDate": energyResetDate,
       "currentMeter": currentMeter,
       "voltageMeter": voltageMeter,
       "powerMeter": powerMeter,
       "powerMeterMin": powerMeterMin,
       "powerMeterMax": powerMeterMax,
       "resetPowerMeterRange": resetPowerMeterRange,
       "powerMeterGain": powerMeterGain,
       "powerMeterOffset": powerMeterOffset,
       "energyMeterAiMappingTable": energyMeterAiMappingTable,
       "energyMeterAiMappingEntry": energyMeterAiMappingEntry,
       "energyMeterAiMappingIndex": energyMeterAiMappingIndex,
       "energyMeterMeter": energyMeterMeter,
       "energyMeterAi": energyMeterAi,
       "energyMeterAiFunction": energyMeterAiFunction,
       "energyMeterValueMappingTable": energyMeterValueMappingTable,
       "energyMeterValueMappingEntry": energyMeterValueMappingEntry,
       "energyMeterValueMappingIndex": energyMeterValueMappingIndex,
       "energyMeterMeterNumber": energyMeterMeterNumber,
       "energyMeterSystemValue": energyMeterSystemValue,
       "energyMeterSystemValueIndex": energyMeterSystemValueIndex,
       "resetAllEnergyMeters": resetAllEnergyMeters,
       "resetAllPowerMeterRanges": resetAllPowerMeterRanges,
       "fanController": fanController,
       "setFanPowerRunningTime": setFanPowerRunningTime,
       "fanControllerProfile": fanControllerProfile,
       "rxpFcFaults": rxpFcFaults,
       "fanControllerStateTable": fanControllerStateTable,
       "fanControllerStateEntry": fanControllerStateEntry,
       "fanControllerStateIndex": fanControllerStateIndex,
       "fanTemperature": fanTemperature,
       "fanPower": fanPower,
       "setFanPower": setFanPower,
       "fanPoles": fanPoles,
       "fanSpeedA": fanSpeedA,
       "fanSpeedB": fanSpeedB,
       "fanControllerMode": fanControllerMode,
       "setFanPowerPeriod": setFanPowerPeriod,
       "applySetPower": applySetPower,
       "fanController1PrimaryTable": fanController1PrimaryTable,
       "fanController1PrimaryEntry": fanController1PrimaryEntry,
       "fanController1PrimaryIndex": fanController1PrimaryIndex,
       "fc1pTemperature": fc1pTemperature,
       "fc1pPower": fc1pPower,
       "fanController1SecondaryTable": fanController1SecondaryTable,
       "fanController1SecondaryEntry": fanController1SecondaryEntry,
       "fanController1SecondaryIndex": fanController1SecondaryIndex,
       "fc1sTemperature": fc1sTemperature,
       "fc1sPower": fc1sPower,
       "fanController2PrimaryTable": fanController2PrimaryTable,
       "fanController2PrimaryEntry": fanController2PrimaryEntry,
       "fanController2PrimaryIndex": fanController2PrimaryIndex,
       "fc2pTemperature": fc2pTemperature,
       "fc2pPower": fc2pPower,
       "fanController2SecondaryTable": fanController2SecondaryTable,
       "fanController2SecondaryEntry": fanController2SecondaryEntry,
       "fanController2SecondaryIndex": fanController2SecondaryIndex,
       "fc2sTemperature": fc2sTemperature,
       "fc2sPower": fc2sPower,
       "fanControllerSmartAlarm": fanControllerSmartAlarm,
       "realTimeClock": realTimeClock,
       "controllerTime": controllerTime,
       "inputOutput": inputOutput,
       "systemAnalogInput": systemAnalogInput,
       "analogInputTable": analogInputTable,
       "analogInputEntry": analogInputEntry,
       "analogInputIndex": analogInputIndex,
       "aiHighState": aiHighState,
       "aiLowState": aiLowState,
       "aiValue": aiValue,
       "aiStatus": aiStatus,
       "aiName": aiName,
       "aiFunction": aiFunction,
       "aiFunctionIndex": aiFunctionIndex,
       "aiUnits": aiUnits,
       "aiIobNumber": aiIobNumber,
       "inputNumber": inputNumber,
       "gain": gain,
       "offset": offset,
       "hysteresis": hysteresis,
       "highSeverity": highSeverity,
       "highThreshold": highThreshold,
       "highDoMappingA": highDoMappingA,
       "highDoMappingB": highDoMappingB,
       "highTrapSend": highTrapSend,
       "lowSeverity": lowSeverity,
       "lowThreshold": lowThreshold,
       "lowDoMappingA": lowDoMappingA,
       "lowDoMappingB": lowDoMappingB,
       "lowTrapSend": lowTrapSend,
       "aiGroup": aiGroup,
       "aiHighNotes": aiHighNotes,
       "aiLowNotes": aiLowNotes,
       "smartAnalogTable": smartAnalogTable,
       "smartAnalogEntry": smartAnalogEntry,
       "smartAnalogIndex": smartAnalogIndex,
       "name": name,
       "group": group,
       "value": value,
       "type": type,
       "units": units,
       "smartAnalogGate": smartAnalogGate,
       "saiFunction": saiFunction,
       "saiFunctionIndex": saiFunctionIndex,
       "smartAnalogMappingTable": smartAnalogMappingTable,
       "smartAnalogMappingEntry": smartAnalogMappingEntry,
       "smartAnalogMappingIndex": smartAnalogMappingIndex,
       "smartAnalogSystemInputMapping": smartAnalogSystemInputMapping,
       "smartAnalogSystemInputValue": smartAnalogSystemInputValue,
       "smartAnalogSystemInput": smartAnalogSystemInput,
       "smartAnalogSystemInputIndex": smartAnalogSystemInputIndex,
       "smartAnalogSystemInputInvert": smartAnalogSystemInputInvert,
       "alternativeEnergySource": alternativeEnergySource,
       "alternativeSourceCurrent": alternativeSourceCurrent,
       "systemStates": systemStates,
       "mainsFail": mainsFail,
       "fanFail": fanFail,
       "movFail": movFail,
       "loadFuseFail": loadFuseFail,
       "batteryFuseFail": batteryFuseFail,
       "phaseFail": phaseFail,
       "digitalInputTable": digitalInputTable,
       "digitalInputEntry": digitalInputEntry,
       "digitalInputIndex": digitalInputIndex,
       "diState": diState,
       "diValue": diValue,
       "diStatus": diStatus,
       "diName": diName,
       "diIobNumber": diIobNumber,
       "digitalInputNumber": digitalInputNumber,
       "diSeverity": diSeverity,
       "diRecognitionPeriod": diRecognitionPeriod,
       "diDeactivationRecognitionPeriod": diDeactivationRecognitionPeriod,
       "diDoMappingA": diDoMappingA,
       "diDoMappingB": diDoMappingB,
       "diTrapSend": diTrapSend,
       "diActiveState": diActiveState,
       "diGroup": diGroup,
       "diNotes": diNotes,
       "digitalOutputTable": digitalOutputTable,
       "digitalOutputEntry": digitalOutputEntry,
       "digitalOutputIndex": digitalOutputIndex,
       "doState": doState,
       "remoteControlState": remoteControlState,
       "doStatus": doStatus,
       "doName": doName,
       "doIobNumber": doIobNumber,
       "doIobDoNumber": doIobDoNumber,
       "doActiveState": doActiveState,
       "doGroup": doGroup,
       "doControlTimeoutPeriod": doControlTimeoutPeriod,
       "doControlTimer": doControlTimer,
       "battery": battery,
       "batteryCapacity": batteryCapacity,
       "cellsPerString": cellsPerString,
       "batteryTemperature": batteryTemperature,
       "batteryCurrent": batteryCurrent,
       "batteryType": batteryType,
       "btrTimeRemaining": btrTimeRemaining,
       "btrStateOfHealth": btrStateOfHealth,
       "batteryChargeState": batteryChargeState,
       "batteryStateThreshold": batteryStateThreshold,
       "endOfChargeAction": endOfChargeAction,
       "batteryDesign": batteryDesign,
       "batteryInstalledDate": batteryInstalledDate,
       "batteryDesignEndOfLifeDate": batteryDesignEndOfLifeDate,
       "midPointMonitoring": midPointMonitoring,
       "bsmLockoutPeriod": bsmLockoutPeriod,
       "bsmConvergencePeriod": bsmConvergencePeriod,
       "stringFailRecognitionPeriod": stringFailRecognitionPeriod,
       "bsmStartThreshold": bsmStartThreshold,
       "bsmStableThreshold": bsmStableThreshold,
       "midpointMonitoringStringTable": midpointMonitoringStringTable,
       "midpointMonitoringStringEntry": midpointMonitoringStringEntry,
       "midpointMonitoringStringIndex": midpointMonitoringStringIndex,
       "stringName": stringName,
       "stringState": stringState,
       "firstQuarterPointVoltage": firstQuarterPointVoltage,
       "midPointVoltage": midPointVoltage,
       "thirdQuarterPointVoltage": thirdQuarterPointVoltage,
       "imbalancePercent": imbalancePercent,
       "bsmState": bsmState,
       "timeInThisState": timeInThisState,
       "currentBsmThreshold": currentBsmThreshold,
       "referenceVoltage": referenceVoltage,
       "clearStringFail": clearStringFail,
       "batteryTimeRemaining": batteryTimeRemaining,
       "btrState": btrState,
       "btrEndVoltage": btrEndVoltage,
       "btrCharacterizationEndVoltage": btrCharacterizationEndVoltage,
       "btrCharacterizationResult": btrCharacterizationResult,
       "btrCharacterizationTime": btrCharacterizationTime,
       "btrAutomaticCharacterization": btrAutomaticCharacterization,
       "btrCharacterizationDelay": btrCharacterizationDelay,
       "btrCharacterizationStart": btrCharacterizationStart,
       "btrCharacterizeBattery": btrCharacterizeBattery,
       "btrStopBatteryCharacterization": btrStopBatteryCharacterization,
       "btrCancelWaiting": btrCancelWaiting,
       "btrClearBatteryCharacterization": btrClearBatteryCharacterization,
       "batteryCharacterizationInstantaneousQuality": batteryCharacterizationInstantaneousQuality,
       "batteryCharacterizationDataTable": batteryCharacterizationDataTable,
       "batteryCharacterizationDataEntry": batteryCharacterizationDataEntry,
       "batteryCharacterizationDataIndex": batteryCharacterizationDataIndex,
       "batteryCharacterizationSample": batteryCharacterizationSample,
       "batteryCharacterizationTime": batteryCharacterizationTime,
       "siteBackupTimeSettings": siteBackupTimeSettings,
       "siteBackupTimeRemaining": siteBackupTimeRemaining,
       "siteBackupTime": siteBackupTime,
       "solar": solar,
       "dcInputVoltage": dcInputVoltage,
       "solarPowerShareOffset": solarPowerShareOffset,
       "solarPower": solarPower,
       "solarCurrent": solarCurrent,
       "solarBaseVoltage": solarBaseVoltage,
       "solarShutdownSmartAlarm": solarShutdownSmartAlarm,
       "dcdc": dcdc,
       "dcdcType": dcdcType,
       "dcdcVoltage": dcdcVoltage,
       "dcdcCurrent": dcdcCurrent,
       "dcdcPower": dcdcPower,
       "dcdcHeatsinkTemperature": dcdcHeatsinkTemperature,
       "numberOfRegisteredDcdcConverters": numberOfRegisteredDcdcConverters,
       "dcdcOutputVoltageSetpoint": dcdcOutputVoltageSetpoint,
       "dcdc12vOutputVoltageSetpoint": dcdc12vOutputVoltageSetpoint,
       "dcdc24vOutputVoltageSetpoint": dcdc24vOutputVoltageSetpoint,
       "dcdc48vOutputVoltageSetpoint": dcdc48vOutputVoltageSetpoint,
       "dcdcCurrentLimit": dcdcCurrentLimit,
       "dcdc12vCurrentLimit": dcdc12vCurrentLimit,
       "dcdc24vCurrentLimit": dcdc24vCurrentLimit,
       "dcdc48vCurrentLimit": dcdc48vCurrentLimit,
       "dcdcInputVoltageItem": dcdcInputVoltageItem,
       "dcdcInputVoltage": dcdcInputVoltage,
       "log": log,
       "logFillMonths": logFillMonths,
       "logUsed": logUsed,
       "logItemsTable": logItemsTable,
       "logItemsEntry": logItemsEntry,
       "logItemsIndex": logItemsIndex,
       "logInterval": logInterval,
       "useOffNormal": useOffNormal,
       "logNumberOfEntries": logNumberOfEntries,
       "offNormalInterval": offNormalInterval,
       "offNormalOffsetVoltage": offNormalOffsetVoltage,
       "offNormalSmartAlarm": offNormalSmartAlarm,
       "isOffNormal": isOffNormal,
       "internal": internal,
       "threadLoadingTable": threadLoadingTable,
       "threadLoadingEntry": threadLoadingEntry,
       "threadLoadingIndex": threadLoadingIndex,
       "threadName": threadName,
       "threadLoading": threadLoading,
       "threadPriority": threadPriority,
       "threadStack": threadStack,
       "threadHeap": threadHeap,
       "threadHighWaterMark": threadHighWaterMark,
       "preemptive": preemptive,
       "ramFree": ramFree,
       "ramHeap": ramHeap,
       "ramStack": ramStack,
       "alarms": alarms,
       "alarmStates": alarmStates,
       "summaryAlarmCritical": summaryAlarmCritical,
       "summaryAlarmMajor": summaryAlarmMajor,
       "summaryAlarmMinor": summaryAlarmMinor,
       "resetBatteryTestFailedAlarm": resetBatteryTestFailedAlarm,
       "resetCommsLostAlarm": resetCommsLostAlarm,
       "resetBatteryTestCancelledAlarm": resetBatteryTestCancelledAlarm,
       "resetLowRectifierCapacityAlarm": resetLowRectifierCapacityAlarm,
       "alarmInfo": alarmInfo,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmIndex": alarmIndex,
       "alarmName": alarmName,
       "alarmSeverity": alarmSeverity,
       "alarmState": alarmState,
       "alarmNotes": alarmNotes,
       "alarmDoMappingA": alarmDoMappingA,
       "alarmDoMappingB": alarmDoMappingB,
       "alarmTrapSend": alarmTrapSend,
       "alarmStateChangeTime": alarmStateChangeTime,
       "alarmConfiguration": alarmConfiguration,
       "enableAudibleAlarmIndication": enableAudibleAlarmIndication,
       "alarmRecognitionPeriod": alarmRecognitionPeriod,
       "acFailRecognitionPeriod": acFailRecognitionPeriod,
       "enableHighFloatTracking": enableHighFloatTracking,
       "highFloatThreshold": highFloatThreshold,
       "enableLowFloatTracking": enableLowFloatTracking,
       "lowFloatThreshold": lowFloatThreshold,
       "highLoadThreshold": highLoadThreshold,
       "lowLoadThreshold": lowLoadThreshold,
       "batteryTemperatureHighThreshold": batteryTemperatureHighThreshold,
       "batteryTemperatureLowThreshold": batteryTemperatureLowThreshold,
       "systemOverloadType": systemOverloadType,
       "systemOverloadTypeB": systemOverloadTypeB,
       "systemOverloadRecognitionPeriod": systemOverloadRecognitionPeriod,
       "systemOverloadThreshold": systemOverloadThreshold,
       "systemOverloadThresholdB": systemOverloadThresholdB,
       "inDischargeAlarmCondition": inDischargeAlarmCondition,
       "batteryCurrentSensorFailRecognitionPeriod": batteryCurrentSensorFailRecognitionPeriod,
       "lowRectifierCapacityRedundancy": lowRectifierCapacityRedundancy,
       "lowRectifierCapacityAlarmThreshold": lowRectifierCapacityAlarmThreshold,
       "lowRectifierCapacityRecognitionPeriod": lowRectifierCapacityRecognitionPeriod,
       "rectifierCapacityBalance": rectifierCapacityBalance,
       "smartAlarmTable": smartAlarmTable,
       "smartAlarmEntry": smartAlarmEntry,
       "smartAlarmIndex": smartAlarmIndex,
       "smartAlarmTrapSend": smartAlarmTrapSend,
       "smartAlarmName": smartAlarmName,
       "smartAlarmSeverity": smartAlarmSeverity,
       "smartAlarmGroup": smartAlarmGroup,
       "smartAlarmNotes": smartAlarmNotes,
       "smartAlarmOperator": smartAlarmOperator,
       "smartAlarmRecognitionPeriod": smartAlarmRecognitionPeriod,
       "smartAlarmDeactivationRecognitionPeriod": smartAlarmDeactivationRecognitionPeriod,
       "smartAlarmDoMappingA": smartAlarmDoMappingA,
       "smartAlarmDoMappingB": smartAlarmDoMappingB,
       "smartAlarmState": smartAlarmState,
       "clearSmartAlarm": clearSmartAlarm,
       "smartAlarmSendEmail": smartAlarmSendEmail,
       "smartAlarmCountReset": smartAlarmCountReset,
       "sourceAlarmTable": sourceAlarmTable,
       "sourceAlarmEntry": sourceAlarmEntry,
       "sourceAlarmIndex": sourceAlarmIndex,
       "smartAlarmAlarmSourceTriggerState": smartAlarmAlarmSourceTriggerState,
       "smartAlarmAlarmSourceStatus": smartAlarmAlarmSourceStatus,
       "smartAlarmAlarmSourceMapping": smartAlarmAlarmSourceMapping,
       "smartAlarmAlarmSourceTrigger": smartAlarmAlarmSourceTrigger,
       "smartAlarmAlarmSourceType": smartAlarmAlarmSourceType,
       "smartAlarmAlarmSourceIndex": smartAlarmAlarmSourceIndex,
       "smartAlarmAlarmSourceActiveCount": smartAlarmAlarmSourceActiveCount,
       "smartAlarmAlarmSourceInactiveCount": smartAlarmAlarmSourceInactiveCount,
       "smartAlarmAlarmSourceCount": smartAlarmAlarmSourceCount,
       "sourceScheduleTable": sourceScheduleTable,
       "sourceScheduleEntry": sourceScheduleEntry,
       "sourceScheduleIndex": sourceScheduleIndex,
       "smartAlarmScheduleSourceIsTriggered": smartAlarmScheduleSourceIsTriggered,
       "smartAlarmScheduleSourceStatus": smartAlarmScheduleSourceStatus,
       "smartAlarmScheduleSourceMapping": smartAlarmScheduleSourceMapping,
       "smartAlarmScheduleSourceFirstActivation": smartAlarmScheduleSourceFirstActivation,
       "smartAlarmScheduleSourceDuration": smartAlarmScheduleSourceDuration,
       "smartAlarmScheduleSourceInterval": smartAlarmScheduleSourceInterval,
       "smartAlarmScheduleSourceRepetitions": smartAlarmScheduleSourceRepetitions,
       "smartAlarmScheduleSourceNext": smartAlarmScheduleSourceNext,
       "smartAlarmScheduleSourceEnd": smartAlarmScheduleSourceEnd,
       "systemValueSourceTable": systemValueSourceTable,
       "systemValueSourceEntry": systemValueSourceEntry,
       "systemValueSourceIndex": systemValueSourceIndex,
       "smartAlarmSystemValueSourceIsTriggered": smartAlarmSystemValueSourceIsTriggered,
       "smartAlarmSystemValueSourceStatus": smartAlarmSystemValueSourceStatus,
       "smartAlarmSystemValueAlarmMapping": smartAlarmSystemValueAlarmMapping,
       "smartAlarmSystemValueSourceValue": smartAlarmSystemValueSourceValue,
       "smartAlarmSystemValueSourceValueIndex": smartAlarmSystemValueSourceValueIndex,
       "smartAlarmSystemValueSourceInput": smartAlarmSystemValueSourceInput,
       "smartAlarmSystemValueSourceThresholdType": smartAlarmSystemValueSourceThresholdType,
       "smartAlarmSystemValueSourceThreshold": smartAlarmSystemValueSourceThreshold,
       "smartAlarmSystemValueSourceHysteresis": smartAlarmSystemValueSourceHysteresis,
       "smartAlarmSystemValueSourceActiveCount": smartAlarmSystemValueSourceActiveCount,
       "smartAlarmSystemValueSourceInactiveCount": smartAlarmSystemValueSourceInactiveCount,
       "smartAlarmSystemValueSourceCount": smartAlarmSystemValueSourceCount,
       "sourceManualTable": sourceManualTable,
       "sourceManualEntry": sourceManualEntry,
       "sourceManualIndex": sourceManualIndex,
       "smartAlarmIsManualSourceTriggered": smartAlarmIsManualSourceTriggered,
       "smartAlarmSourceManualStatus": smartAlarmSourceManualStatus,
       "smartAlarmSourceManualTrigger": smartAlarmSourceManualTrigger,
       "smartAlarmSourceManualMapping": smartAlarmSourceManualMapping,
       "smartAlarmSourceManualPeriod": smartAlarmSourceManualPeriod,
       "smartAlarmNamedItemsTable": smartAlarmNamedItemsTable,
       "smartAlarmNamedItemsEntry": smartAlarmNamedItemsEntry,
       "smartAlarmNamedItemsIndex": smartAlarmNamedItemsIndex,
       "smartAlarmItemMapping": smartAlarmItemMapping,
       "smartAlarmItemValue": smartAlarmItemValue,
       "smartAlarmItemName": smartAlarmItemName,
       "smartAlarmItemTriggerState": smartAlarmItemTriggerState,
       "smartAlarmItemThresholdType": smartAlarmItemThresholdType,
       "smartAlarmItemThreshold": smartAlarmItemThreshold,
       "smartAlarmItemHysteresis": smartAlarmItemHysteresis,
       "trap700Bindings": trap700Bindings,
       "trapAlarmOrigin": trapAlarmOrigin,
       "trapAlarmName": trapAlarmName,
       "trapAlarmNumber": trapAlarmNumber,
       "trapAdditionalText": trapAdditionalText,
       "trapAlarmKeepSeverity": trapAlarmKeepSeverity,
       "rpsTraps": rpsTraps,
       "systemNotificationGroup": systemNotificationGroup,
       "majorAlarmActive": majorAlarmActive,
       "majorAiHighActive": majorAiHighActive,
       "majorAiLowActive": majorAiLowActive,
       "majorDiActive": majorDiActive,
       "majorSmartActive": majorSmartActive,
       "minorAlarmActive": minorAlarmActive,
       "minorAiHighActive": minorAiHighActive,
       "minorAiLowActive": minorAiLowActive,
       "minorDiActive": minorDiActive,
       "minorSmartActive": minorSmartActive,
       "warningAlarmActive": warningAlarmActive,
       "warningAiHighActive": warningAiHighActive,
       "warningAiLowActive": warningAiLowActive,
       "warningDiActive": warningDiActive,
       "warningSmartActive": warningSmartActive,
       "alarmInactive": alarmInactive,
       "aiHighInactive": aiHighInactive,
       "aiLowInactive": aiLowInactive,
       "diInactive": diInactive,
       "smartInactive": smartInactive,
       "alarmStatusChange": alarmStatusChange,
       "criticalAlarmActive": criticalAlarmActive,
       "criticalAiHighActive": criticalAiHighActive,
       "criticalAiLowActive": criticalAiLowActive,
       "criticalDiActive": criticalDiActive,
       "criticalSmartActive": criticalSmartActive,
       "global": _pysmi_global,
       "heartbeat": heartbeat}
)
