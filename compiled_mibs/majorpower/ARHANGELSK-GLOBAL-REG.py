# SNMP MIB module (ARHANGELSK-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\majorpower\ARHANGELSK-GLOBAL-REG

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mts_com_ObjectIdentity = ObjectIdentity
mts_com = _Mts_com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40865)
)
_Mts_ObjectIdentity = ObjectIdentity
mts = _Mts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40865, 1)
)
_Manufacturer_Type = OctetString
_Manufacturer_Object = MibScalar
manufacturer = _Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 1),
    _Manufacturer_Type()
)
manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturer.setStatus("mandatory")
_Modelname_Type = OctetString
_Modelname_Object = MibScalar
modelname = _Modelname_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 2),
    _Modelname_Type()
)
modelname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelname.setStatus("mandatory")
_Controllerswversion_Type = OctetString
_Controllerswversion_Object = MibScalar
controllerswversion = _Controllerswversion_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 3),
    _Controllerswversion_Type()
)
controllerswversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerswversion.setStatus("mandatory")


class _Sitename_Type(OctetString):
    """Custom type sitename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Sitename_Type.__name__ = "OctetString"
_Sitename_Object = MibScalar
sitename = _Sitename_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 4),
    _Sitename_Type()
)
sitename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sitename.setStatus("mandatory")


class _Systemstatus_Type(Integer32):
    """Custom type systemstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("minoralarm", 2),
          ("majoralarm", 3))
    )


_Systemstatus_Type.__name__ = "Integer32"
_Systemstatus_Object = MibScalar
systemstatus = _Systemstatus_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 5),
    _Systemstatus_Type()
)
systemstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemstatus.setStatus("mandatory")
_Systemvoltage_Type = Integer32
_Systemvoltage_Object = MibScalar
systemvoltage = _Systemvoltage_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 6),
    _Systemvoltage_Type()
)
systemvoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemvoltage.setStatus("mandatory")
_Systemcurrent_Type = Integer32
_Systemcurrent_Object = MibScalar
systemcurrent = _Systemcurrent_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 7),
    _Systemcurrent_Type()
)
systemcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemcurrent.setStatus("mandatory")
_Acvoltage_Type = Integer32
_Acvoltage_Object = MibScalar
acvoltage = _Acvoltage_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 8),
    _Acvoltage_Type()
)
acvoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acvoltage.setStatus("mandatory")
_Batterynumber_Type = Integer32
_Batterynumber_Object = MibScalar
batterynumber = _Batterynumber_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 9),
    _Batterynumber_Type()
)
batterynumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterynumber.setStatus("mandatory")
_Systemcapacityavailable_Type = Integer32
_Systemcapacityavailable_Object = MibScalar
systemcapacityavailable = _Systemcapacityavailable_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 10),
    _Systemcapacityavailable_Type()
)
systemcapacityavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemcapacityavailable.setStatus("mandatory")
_Batterycurrent_Type = Integer32
_Batterycurrent_Object = MibScalar
batterycurrent = _Batterycurrent_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 11),
    _Batterycurrent_Type()
)
batterycurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterycurrent.setStatus("mandatory")
_Temperature1_Type = Integer32
_Temperature1_Object = MibScalar
temperature1 = _Temperature1_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 12),
    _Temperature1_Type()
)
temperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature1.setStatus("mandatory")


class _Batterymode_Type(Integer32):
    """Custom type batterymode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("floatcharge", 1),
          ("equalizecharge", 2))
    )


_Batterymode_Type.__name__ = "Integer32"
_Batterymode_Object = MibScalar
batterymode = _Batterymode_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 13),
    _Batterymode_Type()
)
batterymode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterymode.setStatus("mandatory")
_Rectnumsum_Type = Integer32
_Rectnumsum_Object = MibScalar
rectnumsum = _Rectnumsum_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 14),
    _Rectnumsum_Type()
)
rectnumsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectnumsum.setStatus("mandatory")


class _Reccommunicationstatus_Type(Integer32):
    """Custom type reccommunicationstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("interrupt", 2))
    )


_Reccommunicationstatus_Type.__name__ = "Integer32"
_Reccommunicationstatus_Object = MibScalar
reccommunicationstatus = _Reccommunicationstatus_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 15),
    _Reccommunicationstatus_Type()
)
reccommunicationstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reccommunicationstatus.setStatus("mandatory")
_Rectoutputvoltage_Type = Integer32
_Rectoutputvoltage_Object = MibScalar
rectoutputvoltage = _Rectoutputvoltage_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 16),
    _Rectoutputvoltage_Type()
)
rectoutputvoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectoutputvoltage.setStatus("mandatory")
_Rectoutputcurrent_Type = Integer32
_Rectoutputcurrent_Object = MibScalar
rectoutputcurrent = _Rectoutputcurrent_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 17),
    _Rectoutputcurrent_Type()
)
rectoutputcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectoutputcurrent.setStatus("mandatory")
_Rectcurrentref_Type = Integer32
_Rectcurrentref_Object = MibScalar
rectcurrentref = _Rectcurrentref_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 18),
    _Rectcurrentref_Type()
)
rectcurrentref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectcurrentref.setStatus("mandatory")
_Rectinputvoltage_Type = Integer32
_Rectinputvoltage_Object = MibScalar
rectinputvoltage = _Rectinputvoltage_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 19),
    _Rectinputvoltage_Type()
)
rectinputvoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectinputvoltage.setStatus("mandatory")
_Rectopenstate_Type = Integer32
_Rectopenstate_Object = MibScalar
rectopenstate = _Rectopenstate_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 20),
    _Rectopenstate_Type()
)
rectopenstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectopenstate.setStatus("mandatory")
_Rectpluginnotok_Type = Integer32
_Rectpluginnotok_Object = MibScalar
rectpluginnotok = _Rectpluginnotok_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 21),
    _Rectpluginnotok_Type()
)
rectpluginnotok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectpluginnotok.setStatus("mandatory")
_Hvsdflag_Type = Integer32
_Hvsdflag_Object = MibScalar
hvsdflag = _Hvsdflag_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 22),
    _Hvsdflag_Type()
)
hvsdflag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hvsdflag.setStatus("mandatory")
_Outputundervol_Type = Integer32
_Outputundervol_Object = MibScalar
outputundervol = _Outputundervol_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 23),
    _Outputundervol_Type()
)
outputundervol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputundervol.setStatus("mandatory")
_Inputovervol_Type = Integer32
_Inputovervol_Object = MibScalar
inputovervol = _Inputovervol_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 24),
    _Inputovervol_Type()
)
inputovervol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputovervol.setStatus("mandatory")
_Inputundervol_Type = Integer32
_Inputundervol_Object = MibScalar
inputundervol = _Inputundervol_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 25),
    _Inputundervol_Type()
)
inputundervol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputundervol.setStatus("mandatory")
_Fanisnotrotate_Type = Integer32
_Fanisnotrotate_Object = MibScalar
fanisnotrotate = _Fanisnotrotate_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 26),
    _Fanisnotrotate_Type()
)
fanisnotrotate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanisnotrotate.setStatus("mandatory")
_Ambientovertemp_Type = Integer32
_Ambientovertemp_Object = MibScalar
ambientovertemp = _Ambientovertemp_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 27),
    _Ambientovertemp_Type()
)
ambientovertemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ambientovertemp.setStatus("mandatory")
_Ambientundertemp_Type = Integer32
_Ambientundertemp_Object = MibScalar
ambientundertemp = _Ambientundertemp_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 28),
    _Ambientundertemp_Type()
)
ambientundertemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ambientundertemp.setStatus("mandatory")
_Pfcovertemp_Type = Integer32
_Pfcovertemp_Object = MibScalar
pfcovertemp = _Pfcovertemp_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 29),
    _Pfcovertemp_Type()
)
pfcovertemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfcovertemp.setStatus("mandatory")
_Dcdcovertemp_Type = Integer32
_Dcdcovertemp_Object = MibScalar
dcdcovertemp = _Dcdcovertemp_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 30),
    _Dcdcovertemp_Type()
)
dcdcovertemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcovertemp.setStatus("mandatory")
_Communicationnotok_Type = Integer32
_Communicationnotok_Object = MibScalar
communicationnotok = _Communicationnotok_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 31),
    _Communicationnotok_Type()
)
communicationnotok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    communicationnotok.setStatus("mandatory")
_Dcdceepromfault_Type = Integer32
_Dcdceepromfault_Object = MibScalar
dcdceepromfault = _Dcdceepromfault_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 32),
    _Dcdceepromfault_Type()
)
dcdceepromfault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdceepromfault.setStatus("mandatory")
_Powderatedbyacvol_Type = Integer32
_Powderatedbyacvol_Object = MibScalar
powderatedbyacvol = _Powderatedbyacvol_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 33),
    _Powderatedbyacvol_Type()
)
powderatedbyacvol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powderatedbyacvol.setStatus("mandatory")
_Powderatedbytemp_Type = Integer32
_Powderatedbytemp_Object = MibScalar
powderatedbytemp = _Powderatedbytemp_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 34),
    _Powderatedbytemp_Type()
)
powderatedbytemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powderatedbytemp.setStatus("mandatory")
_Currentsharenotok_Type = Integer32
_Currentsharenotok_Object = MibScalar
currentsharenotok = _Currentsharenotok_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 35),
    _Currentsharenotok_Type()
)
currentsharenotok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentsharenotok.setStatus("mandatory")
_Pfceepromfault_Type = Integer32
_Pfceepromfault_Object = MibScalar
pfceepromfault = _Pfceepromfault_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 36),
    _Pfceepromfault_Type()
)
pfceepromfault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pfceepromfault.setStatus("mandatory")
_Commwithmonitorlost_Type = Integer32
_Commwithmonitorlost_Object = MibScalar
commwithmonitorlost = _Commwithmonitorlost_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 37),
    _Commwithmonitorlost_Type()
)
commwithmonitorlost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commwithmonitorlost.setStatus("mandatory")
_Acstopflag_Type = Integer32
_Acstopflag_Object = MibScalar
acstopflag = _Acstopflag_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 38),
    _Acstopflag_Type()
)
acstopflag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acstopflag.setStatus("mandatory")
_Dcvoltagealarm_Type = Integer32
_Dcvoltagealarm_Object = MibScalar
dcvoltagealarm = _Dcvoltagealarm_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 39),
    _Dcvoltagealarm_Type()
)
dcvoltagealarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcvoltagealarm.setStatus("mandatory")
_Battcurralarm_Type = Integer32
_Battcurralarm_Object = MibScalar
battcurralarm = _Battcurralarm_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 40),
    _Battcurralarm_Type()
)
battcurralarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battcurralarm.setStatus("mandatory")
_Batttempalarm_Type = Integer32
_Batttempalarm_Object = MibScalar
batttempalarm = _Batttempalarm_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 41),
    _Batttempalarm_Type()
)
batttempalarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batttempalarm.setStatus("mandatory")
_Battfusebreak_Type = Integer32
_Battfusebreak_Object = MibScalar
battfusebreak = _Battfusebreak_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 42),
    _Battfusebreak_Type()
)
battfusebreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battfusebreak.setStatus("mandatory")
_Loadfusenum_Type = Integer32
_Loadfusenum_Object = MibScalar
loadfusenum = _Loadfusenum_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 43),
    _Loadfusenum_Type()
)
loadfusenum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadfusenum.setStatus("mandatory")
_Loadfusebreak_Type = Integer32
_Loadfusebreak_Object = MibScalar
loadfusebreak = _Loadfusebreak_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 44),
    _Loadfusebreak_Type()
)
loadfusebreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadfusebreak.setStatus("mandatory")
_Batteryprotectflag_Type = Integer32
_Batteryprotectflag_Object = MibScalar
batteryprotectflag = _Batteryprotectflag_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 45),
    _Batteryprotectflag_Type()
)
batteryprotectflag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryprotectflag.setStatus("mandatory")
_Digitalinput_Type = Integer32
_Digitalinput_Object = MibScalar
digitalinput = _Digitalinput_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 46),
    _Digitalinput_Type()
)
digitalinput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalinput.setStatus("mandatory")
_Activealarmsum_Type = Integer32
_Activealarmsum_Object = MibScalar
activealarmsum = _Activealarmsum_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 47),
    _Activealarmsum_Type()
)
activealarmsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activealarmsum.setStatus("mandatory")
_Dateyear_Type = Integer32
_Dateyear_Object = MibScalar
dateyear = _Dateyear_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 48),
    _Dateyear_Type()
)
dateyear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateyear.setStatus("mandatory")
_Datemonth_Type = Integer32
_Datemonth_Object = MibScalar
datemonth = _Datemonth_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 49),
    _Datemonth_Type()
)
datemonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datemonth.setStatus("mandatory")
_Dateday_Type = Integer32
_Dateday_Object = MibScalar
dateday = _Dateday_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 50),
    _Dateday_Type()
)
dateday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateday.setStatus("mandatory")
_Timehour_Type = Integer32
_Timehour_Object = MibScalar
timehour = _Timehour_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 51),
    _Timehour_Type()
)
timehour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timehour.setStatus("mandatory")
_Timeminute_Type = Integer32
_Timeminute_Object = MibScalar
timeminute = _Timeminute_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 52),
    _Timeminute_Type()
)
timeminute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeminute.setStatus("mandatory")
_Timesecond_Type = Integer32
_Timesecond_Object = MibScalar
timesecond = _Timesecond_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 53),
    _Timesecond_Type()
)
timesecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timesecond.setStatus("mandatory")
_Floatchargevol_Type = Integer32
_Floatchargevol_Object = MibScalar
floatchargevol = _Floatchargevol_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 54),
    _Floatchargevol_Type()
)
floatchargevol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    floatchargevol.setStatus("mandatory")
_Eqchargevol_Type = Integer32
_Eqchargevol_Object = MibScalar
eqchargevol = _Eqchargevol_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 55),
    _Eqchargevol_Type()
)
eqchargevol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqchargevol.setStatus("mandatory")
_Battovercurr_Type = Integer32
_Battovercurr_Object = MibScalar
battovercurr = _Battovercurr_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 56),
    _Battovercurr_Type()
)
battovercurr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    battovercurr.setStatus("mandatory")
_Llvdvolt_Type = Integer32
_Llvdvolt_Object = MibScalar
llvdvolt = _Llvdvolt_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 57),
    _Llvdvolt_Type()
)
llvdvolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llvdvolt.setStatus("mandatory")
_Lblvdvolt_Type = Integer32
_Lblvdvolt_Object = MibScalar
lblvdvolt = _Lblvdvolt_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 58),
    _Lblvdvolt_Type()
)
lblvdvolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lblvdvolt.setStatus("mandatory")
_Chargecurrlimit_Type = Integer32
_Chargecurrlimit_Object = MibScalar
chargecurrlimit = _Chargecurrlimit_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 59),
    _Chargecurrlimit_Type()
)
chargecurrlimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chargecurrlimit.setStatus("mandatory")
_Eqchargeperiod_Type = Integer32
_Eqchargeperiod_Object = MibScalar
eqchargeperiod = _Eqchargeperiod_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 60),
    _Eqchargeperiod_Type()
)
eqchargeperiod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqchargeperiod.setStatus("mandatory")
_Battovertemp_Type = Integer32
_Battovertemp_Object = MibScalar
battovertemp = _Battovertemp_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 61),
    _Battovertemp_Type()
)
battovertemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    battovertemp.setStatus("mandatory")
_Battstdcapacity_Type = Integer32
_Battstdcapacity_Object = MibScalar
battstdcapacity = _Battstdcapacity_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 62),
    _Battstdcapacity_Type()
)
battstdcapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    battstdcapacity.setStatus("mandatory")
_Eqprotecttime_Type = Integer32
_Eqprotecttime_Object = MibScalar
eqprotecttime = _Eqprotecttime_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 63),
    _Eqprotecttime_Type()
)
eqprotecttime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqprotecttime.setStatus("mandatory")
_Stableeqtime_Type = Integer32
_Stableeqtime_Object = MibScalar
stableeqtime = _Stableeqtime_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 64),
    _Stableeqtime_Type()
)
stableeqtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stableeqtime.setStatus("mandatory")
_Turneqcurrent_Type = Integer32
_Turneqcurrent_Object = MibScalar
turneqcurrent = _Turneqcurrent_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 65),
    _Turneqcurrent_Type()
)
turneqcurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turneqcurrent.setStatus("mandatory")
_Turneqcaprate_Type = Integer32
_Turneqcaprate_Object = MibScalar
turneqcaprate = _Turneqcaprate_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 66),
    _Turneqcaprate_Type()
)
turneqcaprate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turneqcaprate.setStatus("mandatory")
_Chargeefficient_Type = Integer32
_Chargeefficient_Object = MibScalar
chargeefficient = _Chargeefficient_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 67),
    _Chargeefficient_Type()
)
chargeefficient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chargeefficient.setStatus("mandatory")
_Autoecenable_Type = Integer32
_Autoecenable_Object = MibScalar
autoecenable = _Autoecenable_Object(
    (1, 3, 6, 1, 4, 1, 40865, 1, 68),
    _Autoecenable_Type()
)
autoecenable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoecenable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARHANGELSK-GLOBAL-REG",
    **{"mts-com": mts_com,
       "mts": mts,
       "manufacturer": manufacturer,
       "modelname": modelname,
       "controllerswversion": controllerswversion,
       "sitename": sitename,
       "systemstatus": systemstatus,
       "systemvoltage": systemvoltage,
       "systemcurrent": systemcurrent,
       "acvoltage": acvoltage,
       "batterynumber": batterynumber,
       "systemcapacityavailable": systemcapacityavailable,
       "batterycurrent": batterycurrent,
       "temperature1": temperature1,
       "batterymode": batterymode,
       "rectnumsum": rectnumsum,
       "reccommunicationstatus": reccommunicationstatus,
       "rectoutputvoltage": rectoutputvoltage,
       "rectoutputcurrent": rectoutputcurrent,
       "rectcurrentref": rectcurrentref,
       "rectinputvoltage": rectinputvoltage,
       "rectopenstate": rectopenstate,
       "rectpluginnotok": rectpluginnotok,
       "hvsdflag": hvsdflag,
       "outputundervol": outputundervol,
       "inputovervol": inputovervol,
       "inputundervol": inputundervol,
       "fanisnotrotate": fanisnotrotate,
       "ambientovertemp": ambientovertemp,
       "ambientundertemp": ambientundertemp,
       "pfcovertemp": pfcovertemp,
       "dcdcovertemp": dcdcovertemp,
       "communicationnotok": communicationnotok,
       "dcdceepromfault": dcdceepromfault,
       "powderatedbyacvol": powderatedbyacvol,
       "powderatedbytemp": powderatedbytemp,
       "currentsharenotok": currentsharenotok,
       "pfceepromfault": pfceepromfault,
       "commwithmonitorlost": commwithmonitorlost,
       "acstopflag": acstopflag,
       "dcvoltagealarm": dcvoltagealarm,
       "battcurralarm": battcurralarm,
       "batttempalarm": batttempalarm,
       "battfusebreak": battfusebreak,
       "loadfusenum": loadfusenum,
       "loadfusebreak": loadfusebreak,
       "batteryprotectflag": batteryprotectflag,
       "digitalinput": digitalinput,
       "activealarmsum": activealarmsum,
       "dateyear": dateyear,
       "datemonth": datemonth,
       "dateday": dateday,
       "timehour": timehour,
       "timeminute": timeminute,
       "timesecond": timesecond,
       "floatchargevol": floatchargevol,
       "eqchargevol": eqchargevol,
       "battovercurr": battovercurr,
       "llvdvolt": llvdvolt,
       "lblvdvolt": lblvdvolt,
       "chargecurrlimit": chargecurrlimit,
       "eqchargeperiod": eqchargeperiod,
       "battovertemp": battovertemp,
       "battstdcapacity": battstdcapacity,
       "eqprotecttime": eqprotecttime,
       "stableeqtime": stableeqtime,
       "turneqcurrent": turneqcurrent,
       "turneqcaprate": turneqcaprate,
       "chargeefficient": chargeefficient,
       "autoecenable": autoecenable}
)
