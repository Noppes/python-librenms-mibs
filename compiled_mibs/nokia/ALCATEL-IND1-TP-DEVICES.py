# SNMP MIB module (ALCATEL-IND1-TP-DEVICES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\aos6\ALCATEL-IND1-TP-DEVICES

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

(hardwareIND1Devices,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "hardwareIND1Devices")

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

alcatelIND1TpDevicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1TpDevicesMIB.setRevisions(
        ("2019-10-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FamilyOmniAccess4000_ObjectIdentity = ObjectIdentity
familyOmniAccess4000 = _FamilyOmniAccess4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    familyOmniAccess4000.setStatus("current")
_ChassisOmniAccess4000_ObjectIdentity = ObjectIdentity
chassisOmniAccess4000 = _ChassisOmniAccess4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    chassisOmniAccess4000.setStatus("current")
_DeviceOmniAccess4012_ObjectIdentity = ObjectIdentity
deviceOmniAccess4012 = _DeviceOmniAccess4012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4012.setStatus("current")
_DeviceOmniAccess4024_ObjectIdentity = ObjectIdentity
deviceOmniAccess4024 = _DeviceOmniAccess4024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4024.setStatus("current")
_DeviceOmniAccess4102_ObjectIdentity = ObjectIdentity
deviceOmniAccess4102 = _DeviceOmniAccess4102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4102.setStatus("current")
_FansOmniAccess4000_ObjectIdentity = ObjectIdentity
fansOmniAccess4000 = _FansOmniAccess4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fansOmniAccess4000.setStatus("current")
_PowersOmniAccess4000_ObjectIdentity = ObjectIdentity
powersOmniAccess4000 = _PowersOmniAccess4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    powersOmniAccess4000.setStatus("current")
_ModulesOmniAccess4000_ObjectIdentity = ObjectIdentity
modulesOmniAccess4000 = _ModulesOmniAccess4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    modulesOmniAccess4000.setStatus("current")
_FamilyOmniAccessWireless_ObjectIdentity = ObjectIdentity
familyOmniAccessWireless = _FamilyOmniAccessWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    familyOmniAccessWireless.setStatus("current")
_ChassisOmniAccessWireless_ObjectIdentity = ObjectIdentity
chassisOmniAccessWireless = _ChassisOmniAccessWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    chassisOmniAccessWireless.setStatus("current")
_ChassisOmniAccessWirelessSwitch_ObjectIdentity = ObjectIdentity
chassisOmniAccessWirelessSwitch = _ChassisOmniAccessWirelessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    chassisOmniAccessWirelessSwitch.setStatus("current")
_DeviceOmniAccess5000_ObjectIdentity = ObjectIdentity
deviceOmniAccess5000 = _DeviceOmniAccess5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniAccess5000.setStatus("current")
_DeviceOmniAccess4324_ObjectIdentity = ObjectIdentity
deviceOmniAccess4324 = _DeviceOmniAccess4324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4324.setStatus("current")
_DeviceOmniAccess4308_ObjectIdentity = ObjectIdentity
deviceOmniAccess4308 = _DeviceOmniAccess4308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4308.setStatus("current")
_DeviceOmniAccess6000_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000 = _DeviceOmniAccess6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000.setStatus("current")
_ChassisOmniAccess6000Wireless_ObjectIdentity = ObjectIdentity
chassisOmniAccess6000Wireless = _ChassisOmniAccess6000Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    chassisOmniAccess6000Wireless.setStatus("current")
_DeviceOmniAccess6000PS2_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000PS2 = _DeviceOmniAccess6000PS2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000PS2.setStatus("current")
_FansOmniAccess6000Wireless_ObjectIdentity = ObjectIdentity
fansOmniAccess6000Wireless = _FansOmniAccess6000Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    fansOmniAccess6000Wireless.setStatus("current")
_PowersOmniAccess6000Wireless_ObjectIdentity = ObjectIdentity
powersOmniAccess6000Wireless = _PowersOmniAccess6000Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    powersOmniAccess6000Wireless.setStatus("current")
_ModulesOmniAccess6000Wireless_ObjectIdentity = ObjectIdentity
modulesOmniAccess6000Wireless = _ModulesOmniAccess6000Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    modulesOmniAccess6000Wireless.setStatus("current")
_DeviceOmniAccess6000SCI48_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000SCI48 = _DeviceOmniAccess6000SCI48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000SCI48.setStatus("current")
_DeviceOmniAccess6000SCII256_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000SCII256 = _DeviceOmniAccess6000SCII256_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 4, 4, 3)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000SCII256.setStatus("current")
_DeviceOmniAccess6000LC2G_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000LC2G = _DeviceOmniAccess6000LC2G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 4, 4, 4)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000LC2G.setStatus("current")
_DeviceOmniAccess6000LC2G24F_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000LC2G24F = _DeviceOmniAccess6000LC2G24F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 4, 4, 5)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000LC2G24F.setStatus("current")
_DeviceOmniAccess6000LC2G24FP_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000LC2G24FP = _DeviceOmniAccess6000LC2G24FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 4, 4, 6)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000LC2G24FP.setStatus("current")
_DeviceOmniAccess6000S3C20G_ObjectIdentity = ObjectIdentity
deviceOmniAccess6000S3C20G = _DeviceOmniAccess6000S3C20G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 4, 4, 7)
)
if mibBuilder.loadTexts:
    deviceOmniAccess6000S3C20G.setStatus("current")
_DeviceOmniAccess4302_ObjectIdentity = ObjectIdentity
deviceOmniAccess4302 = _DeviceOmniAccess4302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4302.setStatus("current")
_DeviceOmniAccess4504_ObjectIdentity = ObjectIdentity
deviceOmniAccess4504 = _DeviceOmniAccess4504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4504.setStatus("current")
_DeviceOmniAccess4604_ObjectIdentity = ObjectIdentity
deviceOmniAccess4604 = _DeviceOmniAccess4604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4604.setStatus("current")
_DeviceOmniAccess4704_ObjectIdentity = ObjectIdentity
deviceOmniAccess4704 = _DeviceOmniAccess4704_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4704.setStatus("current")
_DeviceOmniAccess4304_ObjectIdentity = ObjectIdentity
deviceOmniAccess4304 = _DeviceOmniAccess4304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 9)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4304.setStatus("current")
_DeviceOmniAccess4306_ObjectIdentity = ObjectIdentity
deviceOmniAccess4306 = _DeviceOmniAccess4306_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 10)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4306.setStatus("current")
_DeviceOmniAccess4306G_ObjectIdentity = ObjectIdentity
deviceOmniAccess4306G = _DeviceOmniAccess4306G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 11)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4306G.setStatus("current")
_DeviceOmniAccess4306GW_ObjectIdentity = ObjectIdentity
deviceOmniAccess4306GW = _DeviceOmniAccess4306GW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4306GW.setStatus("current")
_DeviceOmniAccess4550_ObjectIdentity = ObjectIdentity
deviceOmniAccess4550 = _DeviceOmniAccess4550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 13)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4550.setStatus("current")
_DeviceOmniAccess4650_ObjectIdentity = ObjectIdentity
deviceOmniAccess4650 = _DeviceOmniAccess4650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 14)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4650.setStatus("current")
_DeviceOmniAccess4750_ObjectIdentity = ObjectIdentity
deviceOmniAccess4750 = _DeviceOmniAccess4750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 15)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4750.setStatus("current")
_DeviceOmniAccess4005_ObjectIdentity = ObjectIdentity
deviceOmniAccess4005 = _DeviceOmniAccess4005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 16)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4005.setStatus("current")
_DeviceOmniAccess4010_ObjectIdentity = ObjectIdentity
deviceOmniAccess4010 = _DeviceOmniAccess4010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 17)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4010.setStatus("current")
_DeviceOmniAccess4030_ObjectIdentity = ObjectIdentity
deviceOmniAccess4030 = _DeviceOmniAccess4030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 18)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4030.setStatus("current")
_DeviceOmniAccessWireless4024_ObjectIdentity = ObjectIdentity
deviceOmniAccessWireless4024 = _DeviceOmniAccessWireless4024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 19)
)
if mibBuilder.loadTexts:
    deviceOmniAccessWireless4024.setStatus("current")
_DeviceOmniAccessWireless4450_ObjectIdentity = ObjectIdentity
deviceOmniAccessWireless4450 = _DeviceOmniAccessWireless4450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 20)
)
if mibBuilder.loadTexts:
    deviceOmniAccessWireless4450.setStatus("current")
_DeviceOmniAccess4750XM_ObjectIdentity = ObjectIdentity
deviceOmniAccess4750XM = _DeviceOmniAccess4750XM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 21)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4750XM.setStatus("current")
_DeviceOmniAccess4008_ObjectIdentity = ObjectIdentity
deviceOmniAccess4008 = _DeviceOmniAccess4008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 22)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4008.setStatus("current")
_DeviceOmniAccess4850IS_ObjectIdentity = ObjectIdentity
deviceOmniAccess4850IS = _DeviceOmniAccess4850IS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 23)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4850IS.setStatus("current")
_DeviceOmniAccessMMHW1K_ObjectIdentity = ObjectIdentity
deviceOmniAccessMMHW1K = _DeviceOmniAccessMMHW1K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 24)
)
if mibBuilder.loadTexts:
    deviceOmniAccessMMHW1K.setStatus("current")
_DeviceOmniAccessMMHW5K_ObjectIdentity = ObjectIdentity
deviceOmniAccessMMHW5K = _DeviceOmniAccessMMHW5K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 25)
)
if mibBuilder.loadTexts:
    deviceOmniAccessMMHW5K.setStatus("current")
_DeviceOmniAccessMMHW10K_ObjectIdentity = ObjectIdentity
deviceOmniAccessMMHW10K = _DeviceOmniAccessMMHW10K_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 26)
)
if mibBuilder.loadTexts:
    deviceOmniAccessMMHW10K.setStatus("current")
_DeviceOmniAccessMMVA_ObjectIdentity = ObjectIdentity
deviceOmniAccessMMVA = _DeviceOmniAccessMMVA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 27)
)
if mibBuilder.loadTexts:
    deviceOmniAccessMMVA.setStatus("current")
_DeviceOmniAccessMCVARW_ObjectIdentity = ObjectIdentity
deviceOmniAccessMCVARW = _DeviceOmniAccessMCVARW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 28)
)
if mibBuilder.loadTexts:
    deviceOmniAccessMCVARW.setStatus("current")
_DeviceOmniAccess4104_ObjectIdentity = ObjectIdentity
deviceOmniAccess4104 = _DeviceOmniAccess4104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 1, 29)
)
if mibBuilder.loadTexts:
    deviceOmniAccess4104.setStatus("current")
_ChassisOmniAccessWirelessAP_ObjectIdentity = ObjectIdentity
chassisOmniAccessWirelessAP = _ChassisOmniAccessWirelessAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    chassisOmniAccessWirelessAP.setStatus("current")
_DeviceOmniAccessAP60_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP60 = _DeviceOmniAccessAP60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP60.setStatus("current")
_DeviceOmniAccessAP61_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP61 = _DeviceOmniAccessAP61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP61.setStatus("current")
_DeviceOmniAccessAP70_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP70 = _DeviceOmniAccessAP70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP70.setStatus("current")
_DeviceOmniAccessAP80S_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP80S = _DeviceOmniAccessAP80S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP80S.setStatus("current")
_DeviceOmniAccessAP80M_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP80M = _DeviceOmniAccessAP80M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP80M.setStatus("current")
_DeviceOmniAccessAP65_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP65 = _DeviceOmniAccessAP65_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP65.setStatus("current")
_DeviceOmniAccessAP40_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP40 = _DeviceOmniAccessAP40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP40.setStatus("current")
_DeviceOmniAccessAP85_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP85 = _DeviceOmniAccessAP85_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP85.setStatus("current")
_DeviceOmniAccessAP41_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP41 = _DeviceOmniAccessAP41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 9)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP41.setStatus("current")
_DeviceOmniAccessAP120_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP120 = _DeviceOmniAccessAP120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 10)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP120.setStatus("current")
_DeviceOmniAccessAP121_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP121 = _DeviceOmniAccessAP121_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 11)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP121.setStatus("current")
_DeviceOmniAccessAP124_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP124 = _DeviceOmniAccessAP124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 12)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP124.setStatus("current")
_DeviceOmniAccessAP125_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP125 = _DeviceOmniAccessAP125_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 13)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP125.setStatus("current")
_DeviceOmniAccessAP120ABG_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP120ABG = _DeviceOmniAccessAP120ABG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 14)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP120ABG.setStatus("current")
_DeviceOmniAccessAP121ABG_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP121ABG = _DeviceOmniAccessAP121ABG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 15)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP121ABG.setStatus("current")
_DeviceOmniAccessAP124ABG_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP124ABG = _DeviceOmniAccessAP124ABG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 16)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP124ABG.setStatus("current")
_DeviceOmniAccessAP125ABG_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP125ABG = _DeviceOmniAccessAP125ABG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 17)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP125ABG.setStatus("current")
_DeviceOmniAccessAP60P_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP60P = _DeviceOmniAccessAP60P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 18)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP60P.setStatus("current")
_DeviceOmniAccessAP105_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP105 = _DeviceOmniAccessAP105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 19)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP105.setStatus("current")
_DeviceOmniAccessAP4306INT_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP4306INT = _DeviceOmniAccessAP4306INT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 20)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP4306INT.setStatus("current")
_DeviceOmniAccessRAP2WG_ObjectIdentity = ObjectIdentity
deviceOmniAccessRAP2WG = _DeviceOmniAccessRAP2WG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 21)
)
if mibBuilder.loadTexts:
    deviceOmniAccessRAP2WG.setStatus("current")
_DeviceOmniAccessRAP5WN_ObjectIdentity = ObjectIdentity
deviceOmniAccessRAP5WN = _DeviceOmniAccessRAP5WN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 22)
)
if mibBuilder.loadTexts:
    deviceOmniAccessRAP5WN.setStatus("current")
_DeviceOmniAccessRAP5_ObjectIdentity = ObjectIdentity
deviceOmniAccessRAP5 = _DeviceOmniAccessRAP5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 23)
)
if mibBuilder.loadTexts:
    deviceOmniAccessRAP5.setStatus("current")
_DeviceOmniAccessAP92_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP92 = _DeviceOmniAccessAP92_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 24)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP92.setStatus("current")
_DeviceOmniAccessAP93_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP93 = _DeviceOmniAccessAP93_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 25)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP93.setStatus("current")
_DeviceOmniAccessAP185_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP185 = _DeviceOmniAccessAP185_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 26)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP185.setStatus("current")
_DeviceOmniAccessAP175POE_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP175POE = _DeviceOmniAccessAP175POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 27)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP175POE.setStatus("current")
_DeviceOmniAccessAP175AC_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP175AC = _DeviceOmniAccessAP175AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 28)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP175AC.setStatus("current")
_DeviceOmniAccessAP175DC_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP175DC = _DeviceOmniAccessAP175DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 29)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP175DC.setStatus("current")
_DeviceOmniAccessAP68_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP68 = _DeviceOmniAccessAP68_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 30)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP68.setStatus("current")
_DeviceOmniAccessAP68P_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP68P = _DeviceOmniAccessAP68P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 31)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP68P.setStatus("current")
_DeviceOmniAccessAP93H_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP93H = _DeviceOmniAccessAP93H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 32)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP93H.setStatus("current")
_DeviceOmniAccessAP134_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP134 = _DeviceOmniAccessAP134_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 33)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP134.setStatus("current")
_DeviceOmniAccessAP135_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP135 = _DeviceOmniAccessAP135_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 34)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP135.setStatus("current")
_DeviceOmniAccessIAP23_ObjectIdentity = ObjectIdentity
deviceOmniAccessIAP23 = _DeviceOmniAccessIAP23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 35)
)
if mibBuilder.loadTexts:
    deviceOmniAccessIAP23.setStatus("current")
_DeviceOmniAccessIAP23P_ObjectIdentity = ObjectIdentity
deviceOmniAccessIAP23P = _DeviceOmniAccessIAP23P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 36)
)
if mibBuilder.loadTexts:
    deviceOmniAccessIAP23P.setStatus("current")
_DeviceOmniAccessAP104_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP104 = _DeviceOmniAccessAP104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 37)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP104.setStatus("current")
_DeviceOmniAccessRAP108_ObjectIdentity = ObjectIdentity
deviceOmniAccessRAP108 = _DeviceOmniAccessRAP108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 38)
)
if mibBuilder.loadTexts:
    deviceOmniAccessRAP108.setStatus("current")
_DeviceOmniAccessRAP109_ObjectIdentity = ObjectIdentity
deviceOmniAccessRAP109 = _DeviceOmniAccessRAP109_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 39)
)
if mibBuilder.loadTexts:
    deviceOmniAccessRAP109.setStatus("current")
_DeviceOmniAccessRAP155_ObjectIdentity = ObjectIdentity
deviceOmniAccessRAP155 = _DeviceOmniAccessRAP155_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 40)
)
if mibBuilder.loadTexts:
    deviceOmniAccessRAP155.setStatus("current")
_DeviceOmniAccessRAP155P_ObjectIdentity = ObjectIdentity
deviceOmniAccessRAP155P = _DeviceOmniAccessRAP155P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 41)
)
if mibBuilder.loadTexts:
    deviceOmniAccessRAP155P.setStatus("current")
_DeviceOmniAccessAP224_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP224 = _DeviceOmniAccessAP224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 42)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP224.setStatus("current")
_DeviceOmniAccessAP114_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP114 = _DeviceOmniAccessAP114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 43)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP114.setStatus("current")
_DeviceOmniAccessAP225_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP225 = _DeviceOmniAccessAP225_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 44)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP225.setStatus("current")
_DeviceOmniAccessAP115_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP115 = _DeviceOmniAccessAP115_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 45)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP115.setStatus("current")
_DeviceOmniAccessAP274_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP274 = _DeviceOmniAccessAP274_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 46)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP274.setStatus("current")
_DeviceOmniAccessAP275_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP275 = _DeviceOmniAccessAP275_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 47)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP275.setStatus("current")
_DeviceOmniAccessAP214_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP214 = _DeviceOmniAccessAP214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 48)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP214.setStatus("current")
_DeviceOmniAccessAP215_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP215 = _DeviceOmniAccessAP215_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 49)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP215.setStatus("current")
_DeviceOmniAccessAP204_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP204 = _DeviceOmniAccessAP204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 50)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP204.setStatus("current")
_DeviceOmniAccessAP205_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP205 = _DeviceOmniAccessAP205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 51)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP205.setStatus("current")
_DeviceOmniAccessAP103_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP103 = _DeviceOmniAccessAP103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 52)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP103.setStatus("current")
_DeviceOmniAccessAP103H_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP103H = _DeviceOmniAccessAP103H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 53)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP103H.setStatus("current")
_DeviceOmniAccessAP277_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP277 = _DeviceOmniAccessAP277_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 54)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP277.setStatus("current")
_DeviceOmniAccessAP228_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP228 = _DeviceOmniAccessAP228_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 55)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP228.setStatus("current")
_DeviceOmniAccessAP205H_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP205H = _DeviceOmniAccessAP205H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 56)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP205H.setStatus("current")
_DeviceOmniAccessAP324_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP324 = _DeviceOmniAccessAP324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 58)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP324.setStatus("current")
_DeviceOmniAccessAP325_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP325 = _DeviceOmniAccessAP325_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 59)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP325.setStatus("current")
_DeviceOmniAccessAP314_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP314 = _DeviceOmniAccessAP314_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 60)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP314.setStatus("current")
_DeviceOmniAccessAP315_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP315 = _DeviceOmniAccessAP315_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 61)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP315.setStatus("current")
_DeviceOmniAccessAP334_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP334 = _DeviceOmniAccessAP334_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 62)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP334.setStatus("current")
_DeviceOmniAccessAP335_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP335 = _DeviceOmniAccessAP335_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 63)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP335.setStatus("current")
_DeviceOmniAccessAP304_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP304 = _DeviceOmniAccessAP304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 64)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP304.setStatus("current")
_DeviceOmniAccessAP305_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP305 = _DeviceOmniAccessAP305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 65)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP305.setStatus("current")
_DeviceOmniAccessAP207_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP207 = _DeviceOmniAccessAP207_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 66)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP207.setStatus("current")
_DeviceOmniAccessAP262_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP262 = _DeviceOmniAccessAP262_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 67)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP262.setStatus("current")
_DeviceOmniAccessAP365_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP365 = _DeviceOmniAccessAP365_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 68)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP365.setStatus("current")
_DeviceOmniAccessAP367_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP367 = _DeviceOmniAccessAP367_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 69)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP367.setStatus("current")
_DeviceOmniAccessAP203H_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP203H = _DeviceOmniAccessAP203H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 70)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP203H.setStatus("current")
_DeviceOmniAccessAP303H_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP303H = _DeviceOmniAccessAP303H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 71)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP303H.setStatus("current")
_DeviceOmniAccessAP203R_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP203R = _DeviceOmniAccessAP203R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 72)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP203R.setStatus("current")
_DeviceOmniAccessAP203RP_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP203RP = _DeviceOmniAccessAP203RP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 73)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP203RP.setStatus("current")
_DeviceOmniAccessOAWAP318_ObjectIdentity = ObjectIdentity
deviceOmniAccessOAWAP318 = _DeviceOmniAccessOAWAP318_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 74)
)
if mibBuilder.loadTexts:
    deviceOmniAccessOAWAP318.setStatus("current")
_DeviceOmniAccessOAWAP344_ObjectIdentity = ObjectIdentity
deviceOmniAccessOAWAP344 = _DeviceOmniAccessOAWAP344_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 75)
)
if mibBuilder.loadTexts:
    deviceOmniAccessOAWAP344.setStatus("current")
_DeviceOmniAccessOAWAP345_ObjectIdentity = ObjectIdentity
deviceOmniAccessOAWAP345 = _DeviceOmniAccessOAWAP345_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 76)
)
if mibBuilder.loadTexts:
    deviceOmniAccessOAWAP345.setStatus("current")
_DeviceOmniAccessOAWAP374_ObjectIdentity = ObjectIdentity
deviceOmniAccessOAWAP374 = _DeviceOmniAccessOAWAP374_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 77)
)
if mibBuilder.loadTexts:
    deviceOmniAccessOAWAP374.setStatus("current")
_DeviceOmniAccessOAWAP375_ObjectIdentity = ObjectIdentity
deviceOmniAccessOAWAP375 = _DeviceOmniAccessOAWAP375_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 78)
)
if mibBuilder.loadTexts:
    deviceOmniAccessOAWAP375.setStatus("current")
_DeviceOmniAccessOAWAP377_ObjectIdentity = ObjectIdentity
deviceOmniAccessOAWAP377 = _DeviceOmniAccessOAWAP377_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 79)
)
if mibBuilder.loadTexts:
    deviceOmniAccessOAWAP377.setStatus("current")
_DeviceOmniAccessAP303_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP303 = _DeviceOmniAccessAP303_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 80)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP303.setStatus("current")
_DeviceOmniAccessAP303P_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP303P = _DeviceOmniAccessAP303P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 81)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP303P.setStatus("current")
_DeviceOmniAccessAP514_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP514 = _DeviceOmniAccessAP514_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 82)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP514.setStatus("current")
_DeviceOmniAccessAP515_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP515 = _DeviceOmniAccessAP515_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 83)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP515.setStatus("current")
_DeviceOmniAccessAP534_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP534 = _DeviceOmniAccessAP534_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 84)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP534.setStatus("current")
_DeviceOmniAccessAP535_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP535 = _DeviceOmniAccessAP535_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 85)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP535.setStatus("current")
_DeviceOmniAccessAP554_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP554 = _DeviceOmniAccessAP554_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 86)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP554.setStatus("current")
_DeviceOmniAccessAP555_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP555 = _DeviceOmniAccessAP555_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 87)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP555.setStatus("current")
_DeviceOmniAccessAP504_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP504 = _DeviceOmniAccessAP504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 88)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP504.setStatus("current")
_DeviceOmniAccessAP505_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP505 = _DeviceOmniAccessAP505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 89)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP505.setStatus("current")
_DeviceOmniAccessAP503H_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP503H = _DeviceOmniAccessAP503H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 90)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP503H.setStatus("current")
_DeviceOmniAccessAP505H_ObjectIdentity = ObjectIdentity
deviceOmniAccessAP505H = _DeviceOmniAccessAP505H_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 1, 2, 91)
)
if mibBuilder.loadTexts:
    deviceOmniAccessAP505H.setStatus("current")
_FansOmniAccessWireless_ObjectIdentity = ObjectIdentity
fansOmniAccessWireless = _FansOmniAccessWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fansOmniAccessWireless.setStatus("current")
_PowersOmniAccessWireless_ObjectIdentity = ObjectIdentity
powersOmniAccessWireless = _PowersOmniAccessWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    powersOmniAccessWireless.setStatus("current")
_ModulesOmniAccessWireless_ObjectIdentity = ObjectIdentity
modulesOmniAccessWireless = _ModulesOmniAccessWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    modulesOmniAccessWireless.setStatus("current")
_FamilyOmniAccessWAN_ObjectIdentity = ObjectIdentity
familyOmniAccessWAN = _FamilyOmniAccessWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    familyOmniAccessWAN.setStatus("current")
_ChassisOmniAccessWAN_ObjectIdentity = ObjectIdentity
chassisOmniAccessWAN = _ChassisOmniAccessWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    chassisOmniAccessWAN.setStatus("current")
_DeviceOmniAccess604T1_ObjectIdentity = ObjectIdentity
deviceOmniAccess604T1 = _DeviceOmniAccess604T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3, 1, 20)
)
if mibBuilder.loadTexts:
    deviceOmniAccess604T1.setStatus("current")
_DeviceOmniAccess604E1_ObjectIdentity = ObjectIdentity
deviceOmniAccess604E1 = _DeviceOmniAccess604E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3, 1, 21)
)
if mibBuilder.loadTexts:
    deviceOmniAccess604E1.setStatus("current")
_DeviceOmniAccess602T1_ObjectIdentity = ObjectIdentity
deviceOmniAccess602T1 = _DeviceOmniAccess602T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3, 1, 22)
)
if mibBuilder.loadTexts:
    deviceOmniAccess602T1.setStatus("current")
_DeviceOmniAccess602E1_ObjectIdentity = ObjectIdentity
deviceOmniAccess602E1 = _DeviceOmniAccess602E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3, 1, 23)
)
if mibBuilder.loadTexts:
    deviceOmniAccess602E1.setStatus("current")
_DeviceOmniAccess601_ObjectIdentity = ObjectIdentity
deviceOmniAccess601 = _DeviceOmniAccess601_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3, 1, 30)
)
if mibBuilder.loadTexts:
    deviceOmniAccess601.setStatus("current")
_DeviceOmniAccess601SBU_ObjectIdentity = ObjectIdentity
deviceOmniAccess601SBU = _DeviceOmniAccess601SBU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3, 1, 31)
)
if mibBuilder.loadTexts:
    deviceOmniAccess601SBU.setStatus("current")
_DeviceOmniAccess625_ObjectIdentity = ObjectIdentity
deviceOmniAccess625 = _DeviceOmniAccess625_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3, 1, 32)
)
if mibBuilder.loadTexts:
    deviceOmniAccess625.setStatus("current")
_DeviceOmniAccess601SBST_ObjectIdentity = ObjectIdentity
deviceOmniAccess601SBST = _DeviceOmniAccess601SBST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3, 1, 33)
)
if mibBuilder.loadTexts:
    deviceOmniAccess601SBST.setStatus("current")
_DeviceOmniAccess601BU_ObjectIdentity = ObjectIdentity
deviceOmniAccess601BU = _DeviceOmniAccess601BU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3, 1, 34)
)
if mibBuilder.loadTexts:
    deviceOmniAccess601BU.setStatus("current")
_DeviceOmniAccess601BST_ObjectIdentity = ObjectIdentity
deviceOmniAccess601BST = _DeviceOmniAccess601BST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3, 1, 35)
)
if mibBuilder.loadTexts:
    deviceOmniAccess601BST.setStatus("current")
_FansOmniAccessWAN_ObjectIdentity = ObjectIdentity
fansOmniAccessWAN = _FansOmniAccessWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    fansOmniAccessWAN.setStatus("current")
_PowersOmniAccessWAN_ObjectIdentity = ObjectIdentity
powersOmniAccessWAN = _PowersOmniAccessWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    powersOmniAccessWAN.setStatus("current")
_ModulesOmniAccessWAN_ObjectIdentity = ObjectIdentity
modulesOmniAccessWAN = _ModulesOmniAccessWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    modulesOmniAccessWAN.setStatus("current")
_Family6200_ObjectIdentity = ObjectIdentity
family6200 = _Family6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    family6200.setStatus("current")
_Chassis6200_ObjectIdentity = ObjectIdentity
chassis6200 = _Chassis6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    chassis6200.setStatus("current")
_Device6224_ObjectIdentity = ObjectIdentity
device6224 = _Device6224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    device6224.setStatus("current")
_Device6224P_ObjectIdentity = ObjectIdentity
device6224P = _Device6224P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    device6224P.setStatus("current")
_Device6248_ObjectIdentity = ObjectIdentity
device6248 = _Device6248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    device6248.setStatus("current")
_Device6248P_ObjectIdentity = ObjectIdentity
device6248P = _Device6248P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    device6248P.setStatus("current")
_Device6224U_ObjectIdentity = ObjectIdentity
device6224U = _Device6224U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    device6224U.setStatus("current")
_Device6212_ObjectIdentity = ObjectIdentity
device6212 = _Device6212_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 4, 1, 6)
)
if mibBuilder.loadTexts:
    device6212.setStatus("current")
_Device6212P_ObjectIdentity = ObjectIdentity
device6212P = _Device6212P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 4, 1, 7)
)
if mibBuilder.loadTexts:
    device6212P.setStatus("current")
_Fans6200_ObjectIdentity = ObjectIdentity
fans6200 = _Fans6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    fans6200.setStatus("current")
_Powers6200_ObjectIdentity = ObjectIdentity
powers6200 = _Powers6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    powers6200.setStatus("current")
_Modules6200_ObjectIdentity = ObjectIdentity
modules6200 = _Modules6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 4, 4)
)
if mibBuilder.loadTexts:
    modules6200.setStatus("current")
_FamilyOAG_ObjectIdentity = ObjectIdentity
familyOAG = _FamilyOAG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    familyOAG.setStatus("current")
_ChassisOAG_ObjectIdentity = ObjectIdentity
chassisOAG = _ChassisOAG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    chassisOAG.setStatus("current")
_DeviceOAG1000_ObjectIdentity = ObjectIdentity
deviceOAG1000 = _DeviceOAG1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOAG1000.setStatus("current")
_DeviceOAG2400_ObjectIdentity = ObjectIdentity
deviceOAG2400 = _DeviceOAG2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOAG2400.setStatus("current")
_FansOAG_ObjectIdentity = ObjectIdentity
fansOAG = _FansOAG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    fansOAG.setStatus("current")
_PowersOAG_ObjectIdentity = ObjectIdentity
powersOAG = _PowersOAG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    powersOAG.setStatus("current")
_ModulesOAG_ObjectIdentity = ObjectIdentity
modulesOAG = _ModulesOAG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 5, 4)
)
if mibBuilder.loadTexts:
    modulesOAG.setStatus("current")
_FamilyOA7XX_ObjectIdentity = ObjectIdentity
familyOA7XX = _FamilyOA7XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    familyOA7XX.setStatus("current")
_ChassisOA7XX_ObjectIdentity = ObjectIdentity
chassisOA7XX = _ChassisOA7XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    chassisOA7XX.setStatus("current")
_DeviceOA740_ObjectIdentity = ObjectIdentity
deviceOA740 = _DeviceOA740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOA740.setStatus("current")
_DeviceOA780_ObjectIdentity = ObjectIdentity
deviceOA780 = _DeviceOA780_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 6, 1, 2)
)
if mibBuilder.loadTexts:
    deviceOA780.setStatus("current")
_FansOA7XX_ObjectIdentity = ObjectIdentity
fansOA7XX = _FansOA7XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 6, 2)
)
if mibBuilder.loadTexts:
    fansOA7XX.setStatus("current")
_PowersOA7XX_ObjectIdentity = ObjectIdentity
powersOA7XX = _PowersOA7XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 6, 3)
)
if mibBuilder.loadTexts:
    powersOA7XX.setStatus("current")
_ModulesOA7XX_ObjectIdentity = ObjectIdentity
modulesOA7XX = _ModulesOA7XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 6, 4)
)
if mibBuilder.loadTexts:
    modulesOA7XX.setStatus("current")
_FamilyOA855X_ObjectIdentity = ObjectIdentity
familyOA855X = _FamilyOA855X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    familyOA855X.setStatus("current")
_ChassisOA855X_ObjectIdentity = ObjectIdentity
chassisOA855X = _ChassisOA855X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    chassisOA855X.setStatus("current")
_DeviceOA8550WSG_ObjectIdentity = ObjectIdentity
deviceOA8550WSG = _DeviceOA8550WSG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    deviceOA8550WSG.setStatus("current")
_ModuleOA855X_ObjectIdentity = ObjectIdentity
moduleOA855X = _ModuleOA855X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 7, 2)
)
if mibBuilder.loadTexts:
    moduleOA855X.setStatus("current")
_FamilyWiNGOAW_ObjectIdentity = ObjectIdentity
familyWiNGOAW = _FamilyWiNGOAW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    familyWiNGOAW.setStatus("current")
_FamilyPhoenixOA_ObjectIdentity = ObjectIdentity
familyPhoenixOA = _FamilyPhoenixOA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 9)
)
if mibBuilder.loadTexts:
    familyPhoenixOA.setStatus("current")
_ChassisPhoenixOA_ObjectIdentity = ObjectIdentity
chassisPhoenixOA = _ChassisPhoenixOA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 9, 1)
)
if mibBuilder.loadTexts:
    chassisPhoenixOA.setStatus("current")
_DevicePhoenixOA5710V_ObjectIdentity = ObjectIdentity
devicePhoenixOA5710V = _DevicePhoenixOA5710V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    devicePhoenixOA5710V.setStatus("current")
_DevicePhoenixOA5720_ObjectIdentity = ObjectIdentity
devicePhoenixOA5720 = _DevicePhoenixOA5720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 9, 1, 2)
)
if mibBuilder.loadTexts:
    devicePhoenixOA5720.setStatus("current")
_DevicePhoenixOA5840_ObjectIdentity = ObjectIdentity
devicePhoenixOA5840 = _DevicePhoenixOA5840_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 9, 1, 3)
)
if mibBuilder.loadTexts:
    devicePhoenixOA5840.setStatus("current")
_DevicePhoenixOA5850_ObjectIdentity = ObjectIdentity
devicePhoenixOA5850 = _DevicePhoenixOA5850_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 9, 1, 4)
)
if mibBuilder.loadTexts:
    devicePhoenixOA5850.setStatus("current")
_DevicePhoenixOA5725R61ER_ObjectIdentity = ObjectIdentity
devicePhoenixOA5725R61ER = _DevicePhoenixOA5725R61ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 9, 1, 5)
)
if mibBuilder.loadTexts:
    devicePhoenixOA5725R61ER.setStatus("current")
_DevicePhoenixOA5725R62ER_ObjectIdentity = ObjectIdentity
devicePhoenixOA5725R62ER = _DevicePhoenixOA5725R62ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 9, 1, 6)
)
if mibBuilder.loadTexts:
    devicePhoenixOA5725R62ER.setStatus("current")
_DevicePhoenixOA5725A3G_ObjectIdentity = ObjectIdentity
devicePhoenixOA5725A3G = _DevicePhoenixOA5725A3G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 9, 1, 7)
)
if mibBuilder.loadTexts:
    devicePhoenixOA5725A3G.setStatus("current")
_DevicePhoenixOA5725ALTE_ObjectIdentity = ObjectIdentity
devicePhoenixOA5725ALTE = _DevicePhoenixOA5725ALTE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 9, 1, 8)
)
if mibBuilder.loadTexts:
    devicePhoenixOA5725ALTE.setStatus("current")
_DevicePhoenixESRWWANENABLER_ObjectIdentity = ObjectIdentity
devicePhoenixESRWWANENABLER = _DevicePhoenixESRWWANENABLER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 9, 1, 9)
)
if mibBuilder.loadTexts:
    devicePhoenixESRWWANENABLER.setStatus("current")
_FansPhoenixOA_ObjectIdentity = ObjectIdentity
fansPhoenixOA = _FansPhoenixOA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 9, 2)
)
if mibBuilder.loadTexts:
    fansPhoenixOA.setStatus("current")
_PowersPhoenixOA_ObjectIdentity = ObjectIdentity
powersPhoenixOA = _PowersPhoenixOA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 9, 3)
)
if mibBuilder.loadTexts:
    powersPhoenixOA.setStatus("current")
_ModulesPhoenixOA_ObjectIdentity = ObjectIdentity
modulesPhoenixOA = _ModulesPhoenixOA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 9, 4)
)
if mibBuilder.loadTexts:
    modulesPhoenixOA.setStatus("current")
_FamilyWebSmart_ObjectIdentity = ObjectIdentity
familyWebSmart = _FamilyWebSmart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 10)
)
if mibBuilder.loadTexts:
    familyWebSmart.setStatus("current")
_ChassisWebSmart_ObjectIdentity = ObjectIdentity
chassisWebSmart = _ChassisWebSmart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 10, 1)
)
if mibBuilder.loadTexts:
    chassisWebSmart.setStatus("current")
_DeviceWebSmartOS22208_ObjectIdentity = ObjectIdentity
deviceWebSmartOS22208 = _DeviceWebSmartOS22208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    deviceWebSmartOS22208.setStatus("current")
_DeviceWebSmartOS2220P8_ObjectIdentity = ObjectIdentity
deviceWebSmartOS2220P8 = _DeviceWebSmartOS2220P8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 10, 1, 2)
)
if mibBuilder.loadTexts:
    deviceWebSmartOS2220P8.setStatus("current")
_DeviceWebSmartOS222024_ObjectIdentity = ObjectIdentity
deviceWebSmartOS222024 = _DeviceWebSmartOS222024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 10, 1, 3)
)
if mibBuilder.loadTexts:
    deviceWebSmartOS222024.setStatus("current")
_DeviceWebSmartOS2220P24_ObjectIdentity = ObjectIdentity
deviceWebSmartOS2220P24 = _DeviceWebSmartOS2220P24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 10, 1, 4)
)
if mibBuilder.loadTexts:
    deviceWebSmartOS2220P24.setStatus("current")
_DeviceWebSmartOS222048_ObjectIdentity = ObjectIdentity
deviceWebSmartOS222048 = _DeviceWebSmartOS222048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 10, 1, 5)
)
if mibBuilder.loadTexts:
    deviceWebSmartOS222048.setStatus("current")
_DeviceWebSmartOS2220P48_ObjectIdentity = ObjectIdentity
deviceWebSmartOS2220P48 = _DeviceWebSmartOS2220P48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 10, 1, 6)
)
if mibBuilder.loadTexts:
    deviceWebSmartOS2220P48.setStatus("current")
_FansWebSmart_ObjectIdentity = ObjectIdentity
fansWebSmart = _FansWebSmart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 10, 2)
)
if mibBuilder.loadTexts:
    fansWebSmart.setStatus("current")
_PowersWebSmart_ObjectIdentity = ObjectIdentity
powersWebSmart = _PowersWebSmart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 10, 3)
)
if mibBuilder.loadTexts:
    powersWebSmart.setStatus("current")
_ModuleWebSmart_ObjectIdentity = ObjectIdentity
moduleWebSmart = _ModuleWebSmart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 2, 2, 10, 4)
)
if mibBuilder.loadTexts:
    moduleWebSmart.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TP-DEVICES",
    **{"alcatelIND1TpDevicesMIB": alcatelIND1TpDevicesMIB,
       "familyOmniAccess4000": familyOmniAccess4000,
       "chassisOmniAccess4000": chassisOmniAccess4000,
       "deviceOmniAccess4012": deviceOmniAccess4012,
       "deviceOmniAccess4024": deviceOmniAccess4024,
       "deviceOmniAccess4102": deviceOmniAccess4102,
       "fansOmniAccess4000": fansOmniAccess4000,
       "powersOmniAccess4000": powersOmniAccess4000,
       "modulesOmniAccess4000": modulesOmniAccess4000,
       "familyOmniAccessWireless": familyOmniAccessWireless,
       "chassisOmniAccessWireless": chassisOmniAccessWireless,
       "chassisOmniAccessWirelessSwitch": chassisOmniAccessWirelessSwitch,
       "deviceOmniAccess5000": deviceOmniAccess5000,
       "deviceOmniAccess4324": deviceOmniAccess4324,
       "deviceOmniAccess4308": deviceOmniAccess4308,
       "deviceOmniAccess6000": deviceOmniAccess6000,
       "chassisOmniAccess6000Wireless": chassisOmniAccess6000Wireless,
       "deviceOmniAccess6000PS2": deviceOmniAccess6000PS2,
       "fansOmniAccess6000Wireless": fansOmniAccess6000Wireless,
       "powersOmniAccess6000Wireless": powersOmniAccess6000Wireless,
       "modulesOmniAccess6000Wireless": modulesOmniAccess6000Wireless,
       "deviceOmniAccess6000SCI48": deviceOmniAccess6000SCI48,
       "deviceOmniAccess6000SCII256": deviceOmniAccess6000SCII256,
       "deviceOmniAccess6000LC2G": deviceOmniAccess6000LC2G,
       "deviceOmniAccess6000LC2G24F": deviceOmniAccess6000LC2G24F,
       "deviceOmniAccess6000LC2G24FP": deviceOmniAccess6000LC2G24FP,
       "deviceOmniAccess6000S3C20G": deviceOmniAccess6000S3C20G,
       "deviceOmniAccess4302": deviceOmniAccess4302,
       "deviceOmniAccess4504": deviceOmniAccess4504,
       "deviceOmniAccess4604": deviceOmniAccess4604,
       "deviceOmniAccess4704": deviceOmniAccess4704,
       "deviceOmniAccess4304": deviceOmniAccess4304,
       "deviceOmniAccess4306": deviceOmniAccess4306,
       "deviceOmniAccess4306G": deviceOmniAccess4306G,
       "deviceOmniAccess4306GW": deviceOmniAccess4306GW,
       "deviceOmniAccess4550": deviceOmniAccess4550,
       "deviceOmniAccess4650": deviceOmniAccess4650,
       "deviceOmniAccess4750": deviceOmniAccess4750,
       "deviceOmniAccess4005": deviceOmniAccess4005,
       "deviceOmniAccess4010": deviceOmniAccess4010,
       "deviceOmniAccess4030": deviceOmniAccess4030,
       "deviceOmniAccessWireless4024": deviceOmniAccessWireless4024,
       "deviceOmniAccessWireless4450": deviceOmniAccessWireless4450,
       "deviceOmniAccess4750XM": deviceOmniAccess4750XM,
       "deviceOmniAccess4008": deviceOmniAccess4008,
       "deviceOmniAccess4850IS": deviceOmniAccess4850IS,
       "deviceOmniAccessMMHW1K": deviceOmniAccessMMHW1K,
       "deviceOmniAccessMMHW5K": deviceOmniAccessMMHW5K,
       "deviceOmniAccessMMHW10K": deviceOmniAccessMMHW10K,
       "deviceOmniAccessMMVA": deviceOmniAccessMMVA,
       "deviceOmniAccessMCVARW": deviceOmniAccessMCVARW,
       "deviceOmniAccess4104": deviceOmniAccess4104,
       "chassisOmniAccessWirelessAP": chassisOmniAccessWirelessAP,
       "deviceOmniAccessAP60": deviceOmniAccessAP60,
       "deviceOmniAccessAP61": deviceOmniAccessAP61,
       "deviceOmniAccessAP70": deviceOmniAccessAP70,
       "deviceOmniAccessAP80S": deviceOmniAccessAP80S,
       "deviceOmniAccessAP80M": deviceOmniAccessAP80M,
       "deviceOmniAccessAP65": deviceOmniAccessAP65,
       "deviceOmniAccessAP40": deviceOmniAccessAP40,
       "deviceOmniAccessAP85": deviceOmniAccessAP85,
       "deviceOmniAccessAP41": deviceOmniAccessAP41,
       "deviceOmniAccessAP120": deviceOmniAccessAP120,
       "deviceOmniAccessAP121": deviceOmniAccessAP121,
       "deviceOmniAccessAP124": deviceOmniAccessAP124,
       "deviceOmniAccessAP125": deviceOmniAccessAP125,
       "deviceOmniAccessAP120ABG": deviceOmniAccessAP120ABG,
       "deviceOmniAccessAP121ABG": deviceOmniAccessAP121ABG,
       "deviceOmniAccessAP124ABG": deviceOmniAccessAP124ABG,
       "deviceOmniAccessAP125ABG": deviceOmniAccessAP125ABG,
       "deviceOmniAccessAP60P": deviceOmniAccessAP60P,
       "deviceOmniAccessAP105": deviceOmniAccessAP105,
       "deviceOmniAccessAP4306INT": deviceOmniAccessAP4306INT,
       "deviceOmniAccessRAP2WG": deviceOmniAccessRAP2WG,
       "deviceOmniAccessRAP5WN": deviceOmniAccessRAP5WN,
       "deviceOmniAccessRAP5": deviceOmniAccessRAP5,
       "deviceOmniAccessAP92": deviceOmniAccessAP92,
       "deviceOmniAccessAP93": deviceOmniAccessAP93,
       "deviceOmniAccessAP185": deviceOmniAccessAP185,
       "deviceOmniAccessAP175POE": deviceOmniAccessAP175POE,
       "deviceOmniAccessAP175AC": deviceOmniAccessAP175AC,
       "deviceOmniAccessAP175DC": deviceOmniAccessAP175DC,
       "deviceOmniAccessAP68": deviceOmniAccessAP68,
       "deviceOmniAccessAP68P": deviceOmniAccessAP68P,
       "deviceOmniAccessAP93H": deviceOmniAccessAP93H,
       "deviceOmniAccessAP134": deviceOmniAccessAP134,
       "deviceOmniAccessAP135": deviceOmniAccessAP135,
       "deviceOmniAccessIAP23": deviceOmniAccessIAP23,
       "deviceOmniAccessIAP23P": deviceOmniAccessIAP23P,
       "deviceOmniAccessAP104": deviceOmniAccessAP104,
       "deviceOmniAccessRAP108": deviceOmniAccessRAP108,
       "deviceOmniAccessRAP109": deviceOmniAccessRAP109,
       "deviceOmniAccessRAP155": deviceOmniAccessRAP155,
       "deviceOmniAccessRAP155P": deviceOmniAccessRAP155P,
       "deviceOmniAccessAP224": deviceOmniAccessAP224,
       "deviceOmniAccessAP114": deviceOmniAccessAP114,
       "deviceOmniAccessAP225": deviceOmniAccessAP225,
       "deviceOmniAccessAP115": deviceOmniAccessAP115,
       "deviceOmniAccessAP274": deviceOmniAccessAP274,
       "deviceOmniAccessAP275": deviceOmniAccessAP275,
       "deviceOmniAccessAP214": deviceOmniAccessAP214,
       "deviceOmniAccessAP215": deviceOmniAccessAP215,
       "deviceOmniAccessAP204": deviceOmniAccessAP204,
       "deviceOmniAccessAP205": deviceOmniAccessAP205,
       "deviceOmniAccessAP103": deviceOmniAccessAP103,
       "deviceOmniAccessAP103H": deviceOmniAccessAP103H,
       "deviceOmniAccessAP277": deviceOmniAccessAP277,
       "deviceOmniAccessAP228": deviceOmniAccessAP228,
       "deviceOmniAccessAP205H": deviceOmniAccessAP205H,
       "deviceOmniAccessAP324": deviceOmniAccessAP324,
       "deviceOmniAccessAP325": deviceOmniAccessAP325,
       "deviceOmniAccessAP314": deviceOmniAccessAP314,
       "deviceOmniAccessAP315": deviceOmniAccessAP315,
       "deviceOmniAccessAP334": deviceOmniAccessAP334,
       "deviceOmniAccessAP335": deviceOmniAccessAP335,
       "deviceOmniAccessAP304": deviceOmniAccessAP304,
       "deviceOmniAccessAP305": deviceOmniAccessAP305,
       "deviceOmniAccessAP207": deviceOmniAccessAP207,
       "deviceOmniAccessAP262": deviceOmniAccessAP262,
       "deviceOmniAccessAP365": deviceOmniAccessAP365,
       "deviceOmniAccessAP367": deviceOmniAccessAP367,
       "deviceOmniAccessAP203H": deviceOmniAccessAP203H,
       "deviceOmniAccessAP303H": deviceOmniAccessAP303H,
       "deviceOmniAccessAP203R": deviceOmniAccessAP203R,
       "deviceOmniAccessAP203RP": deviceOmniAccessAP203RP,
       "deviceOmniAccessOAWAP318": deviceOmniAccessOAWAP318,
       "deviceOmniAccessOAWAP344": deviceOmniAccessOAWAP344,
       "deviceOmniAccessOAWAP345": deviceOmniAccessOAWAP345,
       "deviceOmniAccessOAWAP374": deviceOmniAccessOAWAP374,
       "deviceOmniAccessOAWAP375": deviceOmniAccessOAWAP375,
       "deviceOmniAccessOAWAP377": deviceOmniAccessOAWAP377,
       "deviceOmniAccessAP303": deviceOmniAccessAP303,
       "deviceOmniAccessAP303P": deviceOmniAccessAP303P,
       "deviceOmniAccessAP514": deviceOmniAccessAP514,
       "deviceOmniAccessAP515": deviceOmniAccessAP515,
       "deviceOmniAccessAP534": deviceOmniAccessAP534,
       "deviceOmniAccessAP535": deviceOmniAccessAP535,
       "deviceOmniAccessAP554": deviceOmniAccessAP554,
       "deviceOmniAccessAP555": deviceOmniAccessAP555,
       "deviceOmniAccessAP504": deviceOmniAccessAP504,
       "deviceOmniAccessAP505": deviceOmniAccessAP505,
       "deviceOmniAccessAP503H": deviceOmniAccessAP503H,
       "deviceOmniAccessAP505H": deviceOmniAccessAP505H,
       "fansOmniAccessWireless": fansOmniAccessWireless,
       "powersOmniAccessWireless": powersOmniAccessWireless,
       "modulesOmniAccessWireless": modulesOmniAccessWireless,
       "familyOmniAccessWAN": familyOmniAccessWAN,
       "chassisOmniAccessWAN": chassisOmniAccessWAN,
       "deviceOmniAccess604T1": deviceOmniAccess604T1,
       "deviceOmniAccess604E1": deviceOmniAccess604E1,
       "deviceOmniAccess602T1": deviceOmniAccess602T1,
       "deviceOmniAccess602E1": deviceOmniAccess602E1,
       "deviceOmniAccess601": deviceOmniAccess601,
       "deviceOmniAccess601SBU": deviceOmniAccess601SBU,
       "deviceOmniAccess625": deviceOmniAccess625,
       "deviceOmniAccess601SBST": deviceOmniAccess601SBST,
       "deviceOmniAccess601BU": deviceOmniAccess601BU,
       "deviceOmniAccess601BST": deviceOmniAccess601BST,
       "fansOmniAccessWAN": fansOmniAccessWAN,
       "powersOmniAccessWAN": powersOmniAccessWAN,
       "modulesOmniAccessWAN": modulesOmniAccessWAN,
       "family6200": family6200,
       "chassis6200": chassis6200,
       "device6224": device6224,
       "device6224P": device6224P,
       "device6248": device6248,
       "device6248P": device6248P,
       "device6224U": device6224U,
       "device6212": device6212,
       "device6212P": device6212P,
       "fans6200": fans6200,
       "powers6200": powers6200,
       "modules6200": modules6200,
       "familyOAG": familyOAG,
       "chassisOAG": chassisOAG,
       "deviceOAG1000": deviceOAG1000,
       "deviceOAG2400": deviceOAG2400,
       "fansOAG": fansOAG,
       "powersOAG": powersOAG,
       "modulesOAG": modulesOAG,
       "familyOA7XX": familyOA7XX,
       "chassisOA7XX": chassisOA7XX,
       "deviceOA740": deviceOA740,
       "deviceOA780": deviceOA780,
       "fansOA7XX": fansOA7XX,
       "powersOA7XX": powersOA7XX,
       "modulesOA7XX": modulesOA7XX,
       "familyOA855X": familyOA855X,
       "chassisOA855X": chassisOA855X,
       "deviceOA8550WSG": deviceOA8550WSG,
       "moduleOA855X": moduleOA855X,
       "familyWiNGOAW": familyWiNGOAW,
       "familyPhoenixOA": familyPhoenixOA,
       "chassisPhoenixOA": chassisPhoenixOA,
       "devicePhoenixOA5710V": devicePhoenixOA5710V,
       "devicePhoenixOA5720": devicePhoenixOA5720,
       "devicePhoenixOA5840": devicePhoenixOA5840,
       "devicePhoenixOA5850": devicePhoenixOA5850,
       "devicePhoenixOA5725R61ER": devicePhoenixOA5725R61ER,
       "devicePhoenixOA5725R62ER": devicePhoenixOA5725R62ER,
       "devicePhoenixOA5725A3G": devicePhoenixOA5725A3G,
       "devicePhoenixOA5725ALTE": devicePhoenixOA5725ALTE,
       "devicePhoenixESRWWANENABLER": devicePhoenixESRWWANENABLER,
       "fansPhoenixOA": fansPhoenixOA,
       "powersPhoenixOA": powersPhoenixOA,
       "modulesPhoenixOA": modulesPhoenixOA,
       "familyWebSmart": familyWebSmart,
       "chassisWebSmart": chassisWebSmart,
       "deviceWebSmartOS22208": deviceWebSmartOS22208,
       "deviceWebSmartOS2220P8": deviceWebSmartOS2220P8,
       "deviceWebSmartOS222024": deviceWebSmartOS222024,
       "deviceWebSmartOS2220P24": deviceWebSmartOS2220P24,
       "deviceWebSmartOS222048": deviceWebSmartOS222048,
       "deviceWebSmartOS2220P48": deviceWebSmartOS2220P48,
       "fansWebSmart": fansWebSmart,
       "powersWebSmart": powersWebSmart,
       "moduleWebSmart": moduleWebSmart}
)
