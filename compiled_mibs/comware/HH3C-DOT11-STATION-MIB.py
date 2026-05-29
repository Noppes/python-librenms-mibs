# SNMP MIB module (HH3C-DOT11-STATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-DOT11-STATION-MIB

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

(Hh3cDot11AKMType,
 Hh3cDot11AssocFailType,
 Hh3cDot11AuthenType,
 Hh3cDot11AuthorFailType,
 Hh3cDot11ChannelScopeType,
 Hh3cDot11CipherType,
 Hh3cDot11ObjectIDType,
 Hh3cDot11RadioScopeType,
 Hh3cDot11RadioType,
 Hh3cDot11RadioType2,
 Hh3cDot11SSIDEncryptModeType,
 Hh3cDot11SSIDStringType,
 Hh3cDot11SecIEStatusType,
 hh3cDot11) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "Hh3cDot11AKMType",
    "Hh3cDot11AssocFailType",
    "Hh3cDot11AuthenType",
    "Hh3cDot11AuthorFailType",
    "Hh3cDot11ChannelScopeType",
    "Hh3cDot11CipherType",
    "Hh3cDot11ObjectIDType",
    "Hh3cDot11RadioScopeType",
    "Hh3cDot11RadioType",
    "Hh3cDot11RadioType2",
    "Hh3cDot11SSIDEncryptModeType",
    "Hh3cDot11SSIDStringType",
    "Hh3cDot11SecIEStatusType",
    "hh3cDot11")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cDot11STATION = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11STATION.setRevisions(
        ("2017-10-09 18:00",
         "2017-02-24 18:00",
         "2016-03-11 18:00",
         "2015-04-13 18:00",
         "2010-09-02 18:00",
         "2010-02-23 18:00",
         "2009-12-01 18:00",
         "2009-08-07 18:00",
         "2009-07-29 18:00",
         "2009-05-07 20:00",
         "2008-11-07 17:30",
         "2008-02-25 18:00",
         "2007-12-21 18:00",
         "2007-06-21 20:00",
         "2007-04-27 20:00",
         "2006-05-10 16:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11StationMtGroup_ObjectIdentity = ObjectIdentity
hh3cDot11StationMtGroup = _Hh3cDot11StationMtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1)
)
_Hh3cDot11StationAssociateTable_Object = MibTable
hh3cDot11StationAssociateTable = _Hh3cDot11StationAssociateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11StationAssociateTable.setStatus("current")
_Hh3cDot11StationAssociateEntry_Object = MibTableRow
hh3cDot11StationAssociateEntry = _Hh3cDot11StationAssociateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1)
)
hh3cDot11StationAssociateEntry.setIndexNames(
    (0, "HH3C-DOT11-STATION-MIB", "hh3cDot11StationMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11StationAssociateEntry.setStatus("current")
_Hh3cDot11StationMAC_Type = MacAddress
_Hh3cDot11StationMAC_Object = MibTableColumn
hh3cDot11StationMAC = _Hh3cDot11StationMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 1),
    _Hh3cDot11StationMAC_Type()
)
hh3cDot11StationMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11StationMAC.setStatus("current")
_Hh3cDot11StationIPAddress_Type = IpAddress
_Hh3cDot11StationIPAddress_Object = MibTableColumn
hh3cDot11StationIPAddress = _Hh3cDot11StationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 2),
    _Hh3cDot11StationIPAddress_Type()
)
hh3cDot11StationIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationIPAddress.setStatus("current")
_Hh3cDot11StationUserName_Type = OctetString
_Hh3cDot11StationUserName_Object = MibTableColumn
hh3cDot11StationUserName = _Hh3cDot11StationUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 3),
    _Hh3cDot11StationUserName_Type()
)
hh3cDot11StationUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationUserName.setStatus("current")
_Hh3cDot11StationTxRateSet_Type = OctetString
_Hh3cDot11StationTxRateSet_Object = MibTableColumn
hh3cDot11StationTxRateSet = _Hh3cDot11StationTxRateSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 4),
    _Hh3cDot11StationTxRateSet_Type()
)
hh3cDot11StationTxRateSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxRateSet.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationTxRateSet.setUnits("Mbps")
_Hh3cDot11StationUpTime_Type = Unsigned32
_Hh3cDot11StationUpTime_Object = MibTableColumn
hh3cDot11StationUpTime = _Hh3cDot11StationUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 5),
    _Hh3cDot11StationUpTime_Type()
)
hh3cDot11StationUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationUpTime.setUnits("second")
_Hh3cDot11StationSignalStrength_Type = Integer32
_Hh3cDot11StationSignalStrength_Object = MibTableColumn
hh3cDot11StationSignalStrength = _Hh3cDot11StationSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 6),
    _Hh3cDot11StationSignalStrength_Type()
)
hh3cDot11StationSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationSignalStrength.setUnits("dBm")
_Hh3cDot11StationRSSI_Type = Integer32
_Hh3cDot11StationRSSI_Object = MibTableColumn
hh3cDot11StationRSSI = _Hh3cDot11StationRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 7),
    _Hh3cDot11StationRSSI_Type()
)
hh3cDot11StationRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRSSI.setStatus("current")
_Hh3cDot11StationChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11StationChannel_Object = MibTableColumn
hh3cDot11StationChannel = _Hh3cDot11StationChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 8),
    _Hh3cDot11StationChannel_Type()
)
hh3cDot11StationChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationChannel.setStatus("current")


class _Hh3cDot11StationPowerSaveMode_Type(Integer32):
    """Custom type hh3cDot11StationPowerSaveMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("powersave", 2))
    )


_Hh3cDot11StationPowerSaveMode_Type.__name__ = "Integer32"
_Hh3cDot11StationPowerSaveMode_Object = MibTableColumn
hh3cDot11StationPowerSaveMode = _Hh3cDot11StationPowerSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 9),
    _Hh3cDot11StationPowerSaveMode_Type()
)
hh3cDot11StationPowerSaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationPowerSaveMode.setStatus("current")
_Hh3cDot11StationAid_Type = Integer32
_Hh3cDot11StationAid_Object = MibTableColumn
hh3cDot11StationAid = _Hh3cDot11StationAid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 10),
    _Hh3cDot11StationAid_Type()
)
hh3cDot11StationAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAid.setStatus("current")
_Hh3cDot11StationVlanId_Type = Integer32
_Hh3cDot11StationVlanId_Object = MibTableColumn
hh3cDot11StationVlanId = _Hh3cDot11StationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 11),
    _Hh3cDot11StationVlanId_Type()
)
hh3cDot11StationVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationVlanId.setStatus("current")
_Hh3cDot11StationSSIDName_Type = Hh3cDot11SSIDStringType
_Hh3cDot11StationSSIDName_Object = MibTableColumn
hh3cDot11StationSSIDName = _Hh3cDot11StationSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 12),
    _Hh3cDot11StationSSIDName_Type()
)
hh3cDot11StationSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSSIDName.setStatus("current")
_Hh3cDot11StationAuthenMode_Type = Hh3cDot11AuthenType
_Hh3cDot11StationAuthenMode_Object = MibTableColumn
hh3cDot11StationAuthenMode = _Hh3cDot11StationAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 13),
    _Hh3cDot11StationAuthenMode_Type()
)
hh3cDot11StationAuthenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAuthenMode.setStatus("current")
_Hh3cDot11StationAKMMode_Type = Hh3cDot11AKMType
_Hh3cDot11StationAKMMode_Object = MibTableColumn
hh3cDot11StationAKMMode = _Hh3cDot11StationAKMMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 14),
    _Hh3cDot11StationAKMMode_Type()
)
hh3cDot11StationAKMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAKMMode.setStatus("current")
_Hh3cDot11StationSecurityCiphers_Type = Hh3cDot11CipherType
_Hh3cDot11StationSecurityCiphers_Object = MibTableColumn
hh3cDot11StationSecurityCiphers = _Hh3cDot11StationSecurityCiphers_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 15),
    _Hh3cDot11StationSecurityCiphers_Type()
)
hh3cDot11StationSecurityCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSecurityCiphers.setStatus("current")


class _Hh3cDot11StationSSIDEncryptMode_Type(Hh3cDot11SSIDEncryptModeType):
    """Custom type hh3cDot11StationSSIDEncryptMode based on Hh3cDot11SSIDEncryptModeType"""
    defaultValue = 2


_Hh3cDot11StationSSIDEncryptMode_Type.__name__ = "Hh3cDot11SSIDEncryptModeType"
_Hh3cDot11StationSSIDEncryptMode_Object = MibTableColumn
hh3cDot11StationSSIDEncryptMode = _Hh3cDot11StationSSIDEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 16),
    _Hh3cDot11StationSSIDEncryptMode_Type()
)
hh3cDot11StationSSIDEncryptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSSIDEncryptMode.setStatus("current")
_Hh3cDot11StationRxSNR_Type = Integer32
_Hh3cDot11StationRxSNR_Object = MibTableColumn
hh3cDot11StationRxSNR = _Hh3cDot11StationRxSNR_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 17),
    _Hh3cDot11StationRxSNR_Type()
)
hh3cDot11StationRxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxSNR.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationRxSNR.setUnits("One Percent")
_Hh3cDot11StationTxRate_Type = Integer32
_Hh3cDot11StationTxRate_Object = MibTableColumn
hh3cDot11StationTxRate = _Hh3cDot11StationTxRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 18),
    _Hh3cDot11StationTxRate_Type()
)
hh3cDot11StationTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationTxRate.setUnits("Mbps")
_Hh3cDot11StationRxRate_Type = Integer32
_Hh3cDot11StationRxRate_Object = MibTableColumn
hh3cDot11StationRxRate = _Hh3cDot11StationRxRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 19),
    _Hh3cDot11StationRxRate_Type()
)
hh3cDot11StationRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationRxRate.setUnits("Mbps")


class _Hh3cDot11StationVendorName_Type(OctetString):
    """Custom type hh3cDot11StationVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11StationVendorName_Type.__name__ = "OctetString"
_Hh3cDot11StationVendorName_Object = MibTableColumn
hh3cDot11StationVendorName = _Hh3cDot11StationVendorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 20),
    _Hh3cDot11StationVendorName_Type()
)
hh3cDot11StationVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationVendorName.setStatus("current")
_Hh3cDot11StationRadioMode_Type = Hh3cDot11RadioType
_Hh3cDot11StationRadioMode_Object = MibTableColumn
hh3cDot11StationRadioMode = _Hh3cDot11StationRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 21),
    _Hh3cDot11StationRadioMode_Type()
)
hh3cDot11StationRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRadioMode.setStatus("current")
_Hh3cDot11StationRxNoise_Type = Integer32
_Hh3cDot11StationRxNoise_Object = MibTableColumn
hh3cDot11StationRxNoise = _Hh3cDot11StationRxNoise_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 22),
    _Hh3cDot11StationRxNoise_Type()
)
hh3cDot11StationRxNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxNoise.setStatus("current")
_Hh3cDot11StationMACAddress_Type = MacAddress
_Hh3cDot11StationMACAddress_Object = MibTableColumn
hh3cDot11StationMACAddress = _Hh3cDot11StationMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 23),
    _Hh3cDot11StationMACAddress_Type()
)
hh3cDot11StationMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationMACAddress.setStatus("current")
_Hh3cDot11StationTxSpeed_Type = Integer32
_Hh3cDot11StationTxSpeed_Object = MibTableColumn
hh3cDot11StationTxSpeed = _Hh3cDot11StationTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 24),
    _Hh3cDot11StationTxSpeed_Type()
)
hh3cDot11StationTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationTxSpeed.setUnits("byte/s")
_Hh3cDot11StationRxSpeed_Type = Integer32
_Hh3cDot11StationRxSpeed_Object = MibTableColumn
hh3cDot11StationRxSpeed = _Hh3cDot11StationRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 25),
    _Hh3cDot11StationRxSpeed_Type()
)
hh3cDot11StationRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationRxSpeed.setUnits("byte/s")


class _Hh3cDot11StationWmmMode_Type(Integer32):
    """Custom type hh3cDot11StationWmmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wmm", 1),
          ("nonwmm", 2))
    )


_Hh3cDot11StationWmmMode_Type.__name__ = "Integer32"
_Hh3cDot11StationWmmMode_Object = MibTableColumn
hh3cDot11StationWmmMode = _Hh3cDot11StationWmmMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 26),
    _Hh3cDot11StationWmmMode_Type()
)
hh3cDot11StationWmmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationWmmMode.setStatus("current")
_Hh3cDot11StationSecIEStatus_Type = Hh3cDot11SecIEStatusType
_Hh3cDot11StationSecIEStatus_Object = MibTableColumn
hh3cDot11StationSecIEStatus = _Hh3cDot11StationSecIEStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 27),
    _Hh3cDot11StationSecIEStatus_Type()
)
hh3cDot11StationSecIEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSecIEStatus.setStatus("current")
_Hh3cDot11StationUpTimeTicks_Type = TimeTicks
_Hh3cDot11StationUpTimeTicks_Object = MibTableColumn
hh3cDot11StationUpTimeTicks = _Hh3cDot11StationUpTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 28),
    _Hh3cDot11StationUpTimeTicks_Type()
)
hh3cDot11StationUpTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationUpTimeTicks.setStatus("current")
_Hh3cDot11StationRadioMode2_Type = Hh3cDot11RadioType2
_Hh3cDot11StationRadioMode2_Object = MibTableColumn
hh3cDot11StationRadioMode2 = _Hh3cDot11StationRadioMode2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 29),
    _Hh3cDot11StationRadioMode2_Type()
)
hh3cDot11StationRadioMode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRadioMode2.setStatus("current")
_Hh3cDot11StationAssTime_Type = DateAndTime
_Hh3cDot11StationAssTime_Object = MibTableColumn
hh3cDot11StationAssTime = _Hh3cDot11StationAssTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 30),
    _Hh3cDot11StationAssTime_Type()
)
hh3cDot11StationAssTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAssTime.setStatus("current")


class _Hh3cDot11StationUserAuthType_Type(Integer32):
    """Custom type hh3cDot11StationUserAuthType based on Integer32"""
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
        *(("portalAuth", 1),
          ("authFree", 2),
          ("associateAuth", 3),
          ("macAuth", 4))
    )


_Hh3cDot11StationUserAuthType_Type.__name__ = "Integer32"
_Hh3cDot11StationUserAuthType_Object = MibTableColumn
hh3cDot11StationUserAuthType = _Hh3cDot11StationUserAuthType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 31),
    _Hh3cDot11StationUserAuthType_Type()
)
hh3cDot11StationUserAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationUserAuthType.setStatus("current")
_Hh3cDot11StationRfPingTest_Type = TruthValue
_Hh3cDot11StationRfPingTest_Object = MibTableColumn
hh3cDot11StationRfPingTest = _Hh3cDot11StationRfPingTest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 32),
    _Hh3cDot11StationRfPingTest_Type()
)
hh3cDot11StationRfPingTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11StationRfPingTest.setStatus("current")
_Hh3cDot11StationMaxRate_Type = Integer32
_Hh3cDot11StationMaxRate_Object = MibTableColumn
hh3cDot11StationMaxRate = _Hh3cDot11StationMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 33),
    _Hh3cDot11StationMaxRate_Type()
)
hh3cDot11StationMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationMaxRate.setUnits("Mbps")


class _Hh3cDot11StationPowerSaveModeCM_Type(Integer32):
    """Custom type hh3cDot11StationPowerSaveModeCM based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("powersave", 1))
    )


_Hh3cDot11StationPowerSaveModeCM_Type.__name__ = "Integer32"
_Hh3cDot11StationPowerSaveModeCM_Object = MibTableColumn
hh3cDot11StationPowerSaveModeCM = _Hh3cDot11StationPowerSaveModeCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 34),
    _Hh3cDot11StationPowerSaveModeCM_Type()
)
hh3cDot11StationPowerSaveModeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationPowerSaveModeCM.setStatus("current")


class _Hh3cDot11StationAuthenModeCM_Type(Integer32):
    """Custom type hh3cDot11StationAuthenModeCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 0),
          ("sharedkey", 1))
    )


_Hh3cDot11StationAuthenModeCM_Type.__name__ = "Integer32"
_Hh3cDot11StationAuthenModeCM_Object = MibTableColumn
hh3cDot11StationAuthenModeCM = _Hh3cDot11StationAuthenModeCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 35),
    _Hh3cDot11StationAuthenModeCM_Type()
)
hh3cDot11StationAuthenModeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAuthenModeCM.setStatus("current")


class _Hh3cDot11StationAKMModeCM_Type(Integer32):
    """Custom type hh3cDot11StationAKMModeCM based on Integer32"""
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
          ("psk", 1),
          ("radius", 2),
          ("wlanex", 3))
    )


_Hh3cDot11StationAKMModeCM_Type.__name__ = "Integer32"
_Hh3cDot11StationAKMModeCM_Object = MibTableColumn
hh3cDot11StationAKMModeCM = _Hh3cDot11StationAKMModeCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 36),
    _Hh3cDot11StationAKMModeCM_Type()
)
hh3cDot11StationAKMModeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAKMModeCM.setStatus("current")


class _Hh3cDot11StationSecurityCiphersCM_Type(Integer32):
    """Custom type hh3cDot11StationSecurityCiphersCM based on Integer32"""
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
        *(("none", 0),
          ("wep40", 1),
          ("wep104", 2),
          ("tkip", 3),
          ("aesccmp", 4),
          ("wpisms4", 5))
    )


_Hh3cDot11StationSecurityCiphersCM_Type.__name__ = "Integer32"
_Hh3cDot11StationSecurityCiphersCM_Object = MibTableColumn
hh3cDot11StationSecurityCiphersCM = _Hh3cDot11StationSecurityCiphersCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 37),
    _Hh3cDot11StationSecurityCiphersCM_Type()
)
hh3cDot11StationSecurityCiphersCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSecurityCiphersCM.setStatus("current")


class _Hh3cDot11StationSecIEStatusCM_Type(Integer32):
    """Custom type hh3cDot11StationSecIEStatusCM based on Integer32"""
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
          ("wpa", 1),
          ("wpa2", 2),
          ("wlanex", 3))
    )


_Hh3cDot11StationSecIEStatusCM_Type.__name__ = "Integer32"
_Hh3cDot11StationSecIEStatusCM_Object = MibTableColumn
hh3cDot11StationSecIEStatusCM = _Hh3cDot11StationSecIEStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 38),
    _Hh3cDot11StationSecIEStatusCM_Type()
)
hh3cDot11StationSecIEStatusCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSecIEStatusCM.setStatus("current")
_Hh3cDot11StationIPv6Address_Type = OctetString
_Hh3cDot11StationIPv6Address_Object = MibTableColumn
hh3cDot11StationIPv6Address = _Hh3cDot11StationIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 39),
    _Hh3cDot11StationIPv6Address_Type()
)
hh3cDot11StationIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationIPv6Address.setStatus("current")
_Hh3cDot11StationAssociateAPMACAddressCM_Type = MacAddress
_Hh3cDot11StationAssociateAPMACAddressCM_Object = MibTableColumn
hh3cDot11StationAssociateAPMACAddressCM = _Hh3cDot11StationAssociateAPMACAddressCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 40),
    _Hh3cDot11StationAssociateAPMACAddressCM_Type()
)
hh3cDot11StationAssociateAPMACAddressCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAssociateAPMACAddressCM.setStatus("current")
_Hh3cDot11StationDeviceType_Type = OctetString
_Hh3cDot11StationDeviceType_Object = MibTableColumn
hh3cDot11StationDeviceType = _Hh3cDot11StationDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 41),
    _Hh3cDot11StationDeviceType_Type()
)
hh3cDot11StationDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationDeviceType.setStatus("current")
_Hh3cDot11StationTxRateCM_Type = OctetString
_Hh3cDot11StationTxRateCM_Object = MibTableColumn
hh3cDot11StationTxRateCM = _Hh3cDot11StationTxRateCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 42),
    _Hh3cDot11StationTxRateCM_Type()
)
hh3cDot11StationTxRateCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxRateCM.setStatus("current")
_Hh3cDot11StationRxRateCM_Type = OctetString
_Hh3cDot11StationRxRateCM_Object = MibTableColumn
hh3cDot11StationRxRateCM = _Hh3cDot11StationRxRateCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 43),
    _Hh3cDot11StationRxRateCM_Type()
)
hh3cDot11StationRxRateCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxRateCM.setStatus("current")
_Hh3cDot11StationAPRelationTable_Object = MibTable
hh3cDot11StationAPRelationTable = _Hh3cDot11StationAPRelationTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11StationAPRelationTable.setStatus("current")
_Hh3cDot11StationAPRelationEntry_Object = MibTableRow
hh3cDot11StationAPRelationEntry = _Hh3cDot11StationAPRelationEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2, 1)
)
hh3cDot11StationAPRelationEntry.setIndexNames(
    (0, "HH3C-DOT11-STATION-MIB", "hh3cDot11StationMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11StationAPRelationEntry.setStatus("current")
_Hh3cDot11CurrAPID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11CurrAPID_Object = MibTableColumn
hh3cDot11CurrAPID = _Hh3cDot11CurrAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2, 1, 1),
    _Hh3cDot11CurrAPID_Type()
)
hh3cDot11CurrAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPID.setStatus("current")
_Hh3cDot11CurrRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11CurrRadioID_Object = MibTableColumn
hh3cDot11CurrRadioID = _Hh3cDot11CurrRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2, 1, 2),
    _Hh3cDot11CurrRadioID_Type()
)
hh3cDot11CurrRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrRadioID.setStatus("current")
_Hh3cDot11CurrWlanID_Type = Integer32
_Hh3cDot11CurrWlanID_Object = MibTableColumn
hh3cDot11CurrWlanID = _Hh3cDot11CurrWlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2, 1, 3),
    _Hh3cDot11CurrWlanID_Type()
)
hh3cDot11CurrWlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrWlanID.setStatus("current")
_Hh3cDot11CurrAntennaID_Type = Integer32
_Hh3cDot11CurrAntennaID_Object = MibTableColumn
hh3cDot11CurrAntennaID = _Hh3cDot11CurrAntennaID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2, 1, 4),
    _Hh3cDot11CurrAntennaID_Type()
)
hh3cDot11CurrAntennaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAntennaID.setStatus("current")
_Hh3cDot11StationStatisTable_Object = MibTable
hh3cDot11StationStatisTable = _Hh3cDot11StationStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11StationStatisTable.setStatus("current")
_Hh3cDot11StationStatisEntry_Object = MibTableRow
hh3cDot11StationStatisEntry = _Hh3cDot11StationStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1)
)
hh3cDot11StationStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-STATION-MIB", "hh3cDot11StationMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11StationStatisEntry.setStatus("current")
_Hh3cDot11StationRxFrameCnt_Type = Counter32
_Hh3cDot11StationRxFrameCnt_Object = MibTableColumn
hh3cDot11StationRxFrameCnt = _Hh3cDot11StationRxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 1),
    _Hh3cDot11StationRxFrameCnt_Type()
)
hh3cDot11StationRxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxFrameCnt.setStatus("current")
_Hh3cDot11StationTxFrameCnt_Type = Counter32
_Hh3cDot11StationTxFrameCnt_Object = MibTableColumn
hh3cDot11StationTxFrameCnt = _Hh3cDot11StationTxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 2),
    _Hh3cDot11StationTxFrameCnt_Type()
)
hh3cDot11StationTxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxFrameCnt.setStatus("current")
_Hh3cDot11StationDropFrameCnt_Type = Counter32
_Hh3cDot11StationDropFrameCnt_Object = MibTableColumn
hh3cDot11StationDropFrameCnt = _Hh3cDot11StationDropFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 3),
    _Hh3cDot11StationDropFrameCnt_Type()
)
hh3cDot11StationDropFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationDropFrameCnt.setStatus("current")
_Hh3cDot11StationRxFrameBytes_Type = Counter64
_Hh3cDot11StationRxFrameBytes_Object = MibTableColumn
hh3cDot11StationRxFrameBytes = _Hh3cDot11StationRxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 4),
    _Hh3cDot11StationRxFrameBytes_Type()
)
hh3cDot11StationRxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxFrameBytes.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationRxFrameBytes.setUnits("bytes")
_Hh3cDot11StationTxFrameBytes_Type = Counter64
_Hh3cDot11StationTxFrameBytes_Object = MibTableColumn
hh3cDot11StationTxFrameBytes = _Hh3cDot11StationTxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 5),
    _Hh3cDot11StationTxFrameBytes_Type()
)
hh3cDot11StationTxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxFrameBytes.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationTxFrameBytes.setUnits("bytes")
_Hh3cDot11StationDropFrameBytes_Type = Counter64
_Hh3cDot11StationDropFrameBytes_Object = MibTableColumn
hh3cDot11StationDropFrameBytes = _Hh3cDot11StationDropFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 6),
    _Hh3cDot11StationDropFrameBytes_Type()
)
hh3cDot11StationDropFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationDropFrameBytes.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationDropFrameBytes.setUnits("bytes")
_Hh3cDot11StationRxRetryPkts_Type = Counter32
_Hh3cDot11StationRxRetryPkts_Object = MibTableColumn
hh3cDot11StationRxRetryPkts = _Hh3cDot11StationRxRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 7),
    _Hh3cDot11StationRxRetryPkts_Type()
)
hh3cDot11StationRxRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxRetryPkts.setStatus("current")
_Hh3cDot11StationTxRetryPkts_Type = Counter32
_Hh3cDot11StationTxRetryPkts_Object = MibTableColumn
hh3cDot11StationTxRetryPkts = _Hh3cDot11StationTxRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 8),
    _Hh3cDot11StationTxRetryPkts_Type()
)
hh3cDot11StationTxRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxRetryPkts.setStatus("current")
_Hh3cDot11StationRxRetryBytes_Type = Counter64
_Hh3cDot11StationRxRetryBytes_Object = MibTableColumn
hh3cDot11StationRxRetryBytes = _Hh3cDot11StationRxRetryBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 9),
    _Hh3cDot11StationRxRetryBytes_Type()
)
hh3cDot11StationRxRetryBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxRetryBytes.setStatus("current")
_Hh3cDot11StationTxRetryBytes_Type = Counter64
_Hh3cDot11StationTxRetryBytes_Object = MibTableColumn
hh3cDot11StationTxRetryBytes = _Hh3cDot11StationTxRetryBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 10),
    _Hh3cDot11StationTxRetryBytes_Type()
)
hh3cDot11StationTxRetryBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxRetryBytes.setStatus("current")
_Hh3cDot11StationThroughput_Type = Counter64
_Hh3cDot11StationThroughput_Object = MibTableColumn
hh3cDot11StationThroughput = _Hh3cDot11StationThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 11),
    _Hh3cDot11StationThroughput_Type()
)
hh3cDot11StationThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationThroughput.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationThroughput.setUnits("bytes")
_Hh3cDot11StationSuccessTxCnt_Type = Counter32
_Hh3cDot11StationSuccessTxCnt_Object = MibTableColumn
hh3cDot11StationSuccessTxCnt = _Hh3cDot11StationSuccessTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 12),
    _Hh3cDot11StationSuccessTxCnt_Type()
)
hh3cDot11StationSuccessTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSuccessTxCnt.setStatus("current")
_Hh3cDot11StationSuccessTxDataCnt_Type = Counter32
_Hh3cDot11StationSuccessTxDataCnt_Object = MibTableColumn
hh3cDot11StationSuccessTxDataCnt = _Hh3cDot11StationSuccessTxDataCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 13),
    _Hh3cDot11StationSuccessTxDataCnt_Type()
)
hh3cDot11StationSuccessTxDataCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSuccessTxDataCnt.setStatus("current")
_Hh3cDot11StationRxDataFrameCnt_Type = Counter32
_Hh3cDot11StationRxDataFrameCnt_Object = MibTableColumn
hh3cDot11StationRxDataFrameCnt = _Hh3cDot11StationRxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 14),
    _Hh3cDot11StationRxDataFrameCnt_Type()
)
hh3cDot11StationRxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxDataFrameCnt.setStatus("current")
_Hh3cDot11StationTxDataFrameCnt_Type = Counter32
_Hh3cDot11StationTxDataFrameCnt_Object = MibTableColumn
hh3cDot11StationTxDataFrameCnt = _Hh3cDot11StationTxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 15),
    _Hh3cDot11StationTxDataFrameCnt_Type()
)
hh3cDot11StationTxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxDataFrameCnt.setStatus("current")
_Hh3cDot11StationRxDataFrameBytes_Type = Counter64
_Hh3cDot11StationRxDataFrameBytes_Object = MibTableColumn
hh3cDot11StationRxDataFrameBytes = _Hh3cDot11StationRxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 16),
    _Hh3cDot11StationRxDataFrameBytes_Type()
)
hh3cDot11StationRxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxDataFrameBytes.setStatus("current")
_Hh3cDot11StationTxDataFrameBytes_Type = Counter64
_Hh3cDot11StationTxDataFrameBytes_Object = MibTableColumn
hh3cDot11StationTxDataFrameBytes = _Hh3cDot11StationTxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 17),
    _Hh3cDot11StationTxDataFrameBytes_Type()
)
hh3cDot11StationTxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxDataFrameBytes.setStatus("current")
_Hh3cDot11StationRxFragCnt_Type = Counter32
_Hh3cDot11StationRxFragCnt_Object = MibTableColumn
hh3cDot11StationRxFragCnt = _Hh3cDot11StationRxFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 18),
    _Hh3cDot11StationRxFragCnt_Type()
)
hh3cDot11StationRxFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxFragCnt.setStatus("current")
_Hh3cDot11StaRxErrDataFrameCnt_Type = Counter64
_Hh3cDot11StaRxErrDataFrameCnt_Object = MibTableColumn
hh3cDot11StaRxErrDataFrameCnt = _Hh3cDot11StaRxErrDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 19),
    _Hh3cDot11StaRxErrDataFrameCnt_Type()
)
hh3cDot11StaRxErrDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StaRxErrDataFrameCnt.setStatus("current")
_Hh3cDot11StaTxRetryDataFrameCnt_Type = Counter64
_Hh3cDot11StaTxRetryDataFrameCnt_Object = MibTableColumn
hh3cDot11StaTxRetryDataFrameCnt = _Hh3cDot11StaTxRetryDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 20),
    _Hh3cDot11StaTxRetryDataFrameCnt_Type()
)
hh3cDot11StaTxRetryDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StaTxRetryDataFrameCnt.setStatus("current")
_Hh3cDot11StaTxDataRatePkts_Type = OctetString
_Hh3cDot11StaTxDataRatePkts_Object = MibTableColumn
hh3cDot11StaTxDataRatePkts = _Hh3cDot11StaTxDataRatePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 21),
    _Hh3cDot11StaTxDataRatePkts_Type()
)
hh3cDot11StaTxDataRatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StaTxDataRatePkts.setStatus("current")
_Hh3cDot11StaRxDataRatePkts_Type = OctetString
_Hh3cDot11StaRxDataRatePkts_Object = MibTableColumn
hh3cDot11StaRxDataRatePkts = _Hh3cDot11StaRxDataRatePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 22),
    _Hh3cDot11StaRxDataRatePkts_Type()
)
hh3cDot11StaRxDataRatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StaRxDataRatePkts.setStatus("current")
_Hh3cDot11StaTxSignalStrengthPkts_Type = OctetString
_Hh3cDot11StaTxSignalStrengthPkts_Object = MibTableColumn
hh3cDot11StaTxSignalStrengthPkts = _Hh3cDot11StaTxSignalStrengthPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 23),
    _Hh3cDot11StaTxSignalStrengthPkts_Type()
)
hh3cDot11StaTxSignalStrengthPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StaTxSignalStrengthPkts.setStatus("current")
_Hh3cDot11StaInternetRxFrameBytes_Type = Counter64
_Hh3cDot11StaInternetRxFrameBytes_Object = MibTableColumn
hh3cDot11StaInternetRxFrameBytes = _Hh3cDot11StaInternetRxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 24),
    _Hh3cDot11StaInternetRxFrameBytes_Type()
)
hh3cDot11StaInternetRxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StaInternetRxFrameBytes.setStatus("current")
_Hh3cDot11StaInternetTxFrameBytes_Type = Counter64
_Hh3cDot11StaInternetTxFrameBytes_Object = MibTableColumn
hh3cDot11StaInternetTxFrameBytes = _Hh3cDot11StaInternetTxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 25),
    _Hh3cDot11StaInternetTxFrameBytes_Type()
)
hh3cDot11StaInternetTxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StaInternetTxFrameBytes.setStatus("current")
_Hh3cDot11StaLocalRxFrameBytes_Type = Counter64
_Hh3cDot11StaLocalRxFrameBytes_Object = MibTableColumn
hh3cDot11StaLocalRxFrameBytes = _Hh3cDot11StaLocalRxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 26),
    _Hh3cDot11StaLocalRxFrameBytes_Type()
)
hh3cDot11StaLocalRxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StaLocalRxFrameBytes.setStatus("current")
_Hh3cDot11StaLocalTxFrameBytes_Type = Counter64
_Hh3cDot11StaLocalTxFrameBytes_Object = MibTableColumn
hh3cDot11StaLocalTxFrameBytes = _Hh3cDot11StaLocalTxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 27),
    _Hh3cDot11StaLocalTxFrameBytes_Type()
)
hh3cDot11StaLocalTxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StaLocalTxFrameBytes.setStatus("current")
_Hh3cDot11StationRfPingTable_Object = MibTable
hh3cDot11StationRfPingTable = _Hh3cDot11StationRfPingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11StationRfPingTable.setStatus("current")
_Hh3cDot11StationRfPingEntry_Object = MibTableRow
hh3cDot11StationRfPingEntry = _Hh3cDot11StationRfPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 4, 1)
)
hh3cDot11StationRfPingEntry.setIndexNames(
    (0, "HH3C-DOT11-STATION-MIB", "hh3cDot11StationMAC"),
    (0, "HH3C-DOT11-STATION-MIB", "hh3cDot11StationRfPingIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11StationRfPingEntry.setStatus("current")


class _Hh3cDot11StationRfPingIndex_Type(Integer32):
    """Custom type hh3cDot11StationRfPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214783647),
    )


_Hh3cDot11StationRfPingIndex_Type.__name__ = "Integer32"
_Hh3cDot11StationRfPingIndex_Object = MibTableColumn
hh3cDot11StationRfPingIndex = _Hh3cDot11StationRfPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 4, 1, 1),
    _Hh3cDot11StationRfPingIndex_Type()
)
hh3cDot11StationRfPingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11StationRfPingIndex.setStatus("current")
_Hh3cDot11StationRfPingRate_Type = OctetString
_Hh3cDot11StationRfPingRate_Object = MibTableColumn
hh3cDot11StationRfPingRate = _Hh3cDot11StationRfPingRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 4, 1, 2),
    _Hh3cDot11StationRfPingRate_Type()
)
hh3cDot11StationRfPingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRfPingRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationRfPingRate.setUnits("Mbps")
_Hh3cDot11StationRfPingTxCnt_Type = Integer32
_Hh3cDot11StationRfPingTxCnt_Object = MibTableColumn
hh3cDot11StationRfPingTxCnt = _Hh3cDot11StationRfPingTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 4, 1, 3),
    _Hh3cDot11StationRfPingTxCnt_Type()
)
hh3cDot11StationRfPingTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRfPingTxCnt.setStatus("current")
_Hh3cDot11StationRfPingRxCnt_Type = Integer32
_Hh3cDot11StationRfPingRxCnt_Object = MibTableColumn
hh3cDot11StationRfPingRxCnt = _Hh3cDot11StationRfPingRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 4, 1, 4),
    _Hh3cDot11StationRfPingRxCnt_Type()
)
hh3cDot11StationRfPingRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRfPingRxCnt.setStatus("current")
_Hh3cDot11StationRfPingRssi_Type = Integer32
_Hh3cDot11StationRfPingRssi_Object = MibTableColumn
hh3cDot11StationRfPingRssi = _Hh3cDot11StationRfPingRssi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 4, 1, 5),
    _Hh3cDot11StationRfPingRssi_Type()
)
hh3cDot11StationRfPingRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRfPingRssi.setStatus("current")
_Hh3cDot11StationRfPingRetries_Type = Integer32
_Hh3cDot11StationRfPingRetries_Object = MibTableColumn
hh3cDot11StationRfPingRetries = _Hh3cDot11StationRfPingRetries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 4, 1, 6),
    _Hh3cDot11StationRfPingRetries_Type()
)
hh3cDot11StationRfPingRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRfPingRetries.setStatus("current")
_Hh3cDot11StationRfPingRtt_Type = Integer32
_Hh3cDot11StationRfPingRtt_Object = MibTableColumn
hh3cDot11StationRfPingRtt = _Hh3cDot11StationRfPingRtt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 4, 1, 7),
    _Hh3cDot11StationRfPingRtt_Type()
)
hh3cDot11StationRfPingRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRfPingRtt.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationRfPingRtt.setUnits("ms")
_Hh3cDot11StationNotifyGroup_ObjectIdentity = ObjectIdentity
hh3cDot11StationNotifyGroup = _Hh3cDot11StationNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2)
)
_Hh3cDot11StationTraps_ObjectIdentity = ObjectIdentity
hh3cDot11StationTraps = _Hh3cDot11StationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0)
)
_Hh3cDot11StationTrapVarObjects_ObjectIdentity = ObjectIdentity
hh3cDot11StationTrapVarObjects = _Hh3cDot11StationTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1)
)
_Hh3cDot11StationTrapBSSID_Type = MacAddress
_Hh3cDot11StationTrapBSSID_Object = MibScalar
hh3cDot11StationTrapBSSID = _Hh3cDot11StationTrapBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 1),
    _Hh3cDot11StationTrapBSSID_Type()
)
hh3cDot11StationTrapBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapBSSID.setStatus("current")
_Hh3cDot11StationTrapStaMAC_Type = MacAddress
_Hh3cDot11StationTrapStaMAC_Object = MibScalar
hh3cDot11StationTrapStaMAC = _Hh3cDot11StationTrapStaMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 2),
    _Hh3cDot11StationTrapStaMAC_Type()
)
hh3cDot11StationTrapStaMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapStaMAC.setStatus("current")
_Hh3cDot11StationSessionStartTime_Type = DateAndTime
_Hh3cDot11StationSessionStartTime_Object = MibScalar
hh3cDot11StationSessionStartTime = _Hh3cDot11StationSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 3),
    _Hh3cDot11StationSessionStartTime_Type()
)
hh3cDot11StationSessionStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationSessionStartTime.setStatus("current")
_Hh3cDot11StationAssocFailCause_Type = Hh3cDot11AssocFailType
_Hh3cDot11StationAssocFailCause_Object = MibScalar
hh3cDot11StationAssocFailCause = _Hh3cDot11StationAssocFailCause_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 4),
    _Hh3cDot11StationAssocFailCause_Type()
)
hh3cDot11StationAssocFailCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationAssocFailCause.setStatus("current")
_Hh3cDot11StationAuthorFailCause_Type = Hh3cDot11AuthorFailType
_Hh3cDot11StationAuthorFailCause_Object = MibScalar
hh3cDot11StationAuthorFailCause = _Hh3cDot11StationAuthorFailCause_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 5),
    _Hh3cDot11StationAuthorFailCause_Type()
)
hh3cDot11StationAuthorFailCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationAuthorFailCause.setStatus("current")


class _Hh3cDot11StationFailCauseDesc_Type(OctetString):
    """Custom type hh3cDot11StationFailCauseDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11StationFailCauseDesc_Type.__name__ = "OctetString"
_Hh3cDot11StationFailCauseDesc_Object = MibScalar
hh3cDot11StationFailCauseDesc = _Hh3cDot11StationFailCauseDesc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 6),
    _Hh3cDot11StationFailCauseDesc_Type()
)
hh3cDot11StationFailCauseDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationFailCauseDesc.setStatus("current")
_Hh3cDot11StationSessionDuration_Type = Unsigned32
_Hh3cDot11StationSessionDuration_Object = MibScalar
hh3cDot11StationSessionDuration = _Hh3cDot11StationSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 7),
    _Hh3cDot11StationSessionDuration_Type()
)
hh3cDot11StationSessionDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationSessionDuration.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationSessionDuration.setUnits("second")
_Hh3cDot11StationRoamingTime_Type = Unsigned32
_Hh3cDot11StationRoamingTime_Object = MibScalar
hh3cDot11StationRoamingTime = _Hh3cDot11StationRoamingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 8),
    _Hh3cDot11StationRoamingTime_Type()
)
hh3cDot11StationRoamingTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationRoamingTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationRoamingTime.setUnits("second")
_Hh3cDot11StationACIPAddress_Type = IpAddress
_Hh3cDot11StationACIPAddress_Object = MibScalar
hh3cDot11StationACIPAddress = _Hh3cDot11StationACIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 9),
    _Hh3cDot11StationACIPAddress_Type()
)
hh3cDot11StationACIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationACIPAddress.setStatus("current")
_Hh3cDot11StationAPName_Type = OctetString
_Hh3cDot11StationAPName_Object = MibScalar
hh3cDot11StationAPName = _Hh3cDot11StationAPName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 10),
    _Hh3cDot11StationAPName_Type()
)
hh3cDot11StationAPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationAPName.setStatus("current")
_Hh3cDot11StationBSSID_Type = MacAddress
_Hh3cDot11StationBSSID_Object = MibScalar
hh3cDot11StationBSSID = _Hh3cDot11StationBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 11),
    _Hh3cDot11StationBSSID_Type()
)
hh3cDot11StationBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationBSSID.setStatus("current")
_Hh3cDot11StaDisconnectReason_Type = OctetString
_Hh3cDot11StaDisconnectReason_Object = MibScalar
hh3cDot11StaDisconnectReason = _Hh3cDot11StaDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 12),
    _Hh3cDot11StaDisconnectReason_Type()
)
hh3cDot11StaDisconnectReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StaDisconnectReason.setStatus("current")


class _Hh3cDot11StationAuthMode_Type(Integer32):
    """Custom type hh3cDot11StationAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 1),
          ("sharedkey", 2))
    )


_Hh3cDot11StationAuthMode_Type.__name__ = "Integer32"
_Hh3cDot11StationAuthMode_Object = MibScalar
hh3cDot11StationAuthMode = _Hh3cDot11StationAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 13),
    _Hh3cDot11StationAuthMode_Type()
)
hh3cDot11StationAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationAuthMode.setStatus("current")
_Hh3cDot11StationACIPv6Add_Type = OctetString
_Hh3cDot11StationACIPv6Add_Object = MibScalar
hh3cDot11StationACIPv6Add = _Hh3cDot11StationACIPv6Add_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 14),
    _Hh3cDot11StationACIPv6Add_Type()
)
hh3cDot11StationACIPv6Add.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationACIPv6Add.setStatus("current")
_Hh3cDot11UserName_Type = OctetString
_Hh3cDot11UserName_Object = MibScalar
hh3cDot11UserName = _Hh3cDot11UserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 15),
    _Hh3cDot11UserName_Type()
)
hh3cDot11UserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11UserName.setStatus("current")
_Hh3cDot11StationTrapAPMacAddress_Type = MacAddress
_Hh3cDot11StationTrapAPMacAddress_Object = MibScalar
hh3cDot11StationTrapAPMacAddress = _Hh3cDot11StationTrapAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 16),
    _Hh3cDot11StationTrapAPMacAddress_Type()
)
hh3cDot11StationTrapAPMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapAPMacAddress.setStatus("current")
_Hh3cDot11StationTrapOldAntennaID_Type = Integer32
_Hh3cDot11StationTrapOldAntennaID_Object = MibScalar
hh3cDot11StationTrapOldAntennaID = _Hh3cDot11StationTrapOldAntennaID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 17),
    _Hh3cDot11StationTrapOldAntennaID_Type()
)
hh3cDot11StationTrapOldAntennaID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapOldAntennaID.setStatus("current")
_Hh3cDot11StationTrapNewAntennaID_Type = Integer32
_Hh3cDot11StationTrapNewAntennaID_Object = MibScalar
hh3cDot11StationTrapNewAntennaID = _Hh3cDot11StationTrapNewAntennaID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 18),
    _Hh3cDot11StationTrapNewAntennaID_Type()
)
hh3cDot11StationTrapNewAntennaID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapNewAntennaID.setStatus("current")
_Hh3cDot11StationTrapAPIPAddress_Type = IpAddress
_Hh3cDot11StationTrapAPIPAddress_Object = MibScalar
hh3cDot11StationTrapAPIPAddress = _Hh3cDot11StationTrapAPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 19),
    _Hh3cDot11StationTrapAPIPAddress_Type()
)
hh3cDot11StationTrapAPIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapAPIPAddress.setStatus("current")
_Hh3cDot11StationTrapStartTime_Type = Unsigned32
_Hh3cDot11StationTrapStartTime_Object = MibScalar
hh3cDot11StationTrapStartTime = _Hh3cDot11StationTrapStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 20),
    _Hh3cDot11StationTrapStartTime_Type()
)
hh3cDot11StationTrapStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapStartTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapStartTime.setUnits("second")
_Hh3cDot11StationAuditTrapOpType_Type = Unsigned32
_Hh3cDot11StationAuditTrapOpType_Object = MibScalar
hh3cDot11StationAuditTrapOpType = _Hh3cDot11StationAuditTrapOpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 21),
    _Hh3cDot11StationAuditTrapOpType_Type()
)
hh3cDot11StationAuditTrapOpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationAuditTrapOpType.setStatus("current")
_Hh3cDot11StationTrapStaIPAddress_Type = IpAddress
_Hh3cDot11StationTrapStaIPAddress_Object = MibScalar
hh3cDot11StationTrapStaIPAddress = _Hh3cDot11StationTrapStaIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 22),
    _Hh3cDot11StationTrapStaIPAddress_Type()
)
hh3cDot11StationTrapStaIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapStaIPAddress.setStatus("current")
_Hh3cDot11StationTrapRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11StationTrapRadioID_Object = MibScalar
hh3cDot11StationTrapRadioID = _Hh3cDot11StationTrapRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 23),
    _Hh3cDot11StationTrapRadioID_Type()
)
hh3cDot11StationTrapRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapRadioID.setStatus("current")
_Hh3cDot11StationTrapRadioMode_Type = Hh3cDot11RadioType2
_Hh3cDot11StationTrapRadioMode_Object = MibScalar
hh3cDot11StationTrapRadioMode = _Hh3cDot11StationTrapRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 24),
    _Hh3cDot11StationTrapRadioMode_Type()
)
hh3cDot11StationTrapRadioMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapRadioMode.setStatus("current")
_Hh3cDot11StationTrapWlanID_Type = Integer32
_Hh3cDot11StationTrapWlanID_Object = MibScalar
hh3cDot11StationTrapWlanID = _Hh3cDot11StationTrapWlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 25),
    _Hh3cDot11StationTrapWlanID_Type()
)
hh3cDot11StationTrapWlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapWlanID.setStatus("current")
_Hh3cDot11StationTrapSSIDName_Type = Hh3cDot11SSIDStringType
_Hh3cDot11StationTrapSSIDName_Object = MibScalar
hh3cDot11StationTrapSSIDName = _Hh3cDot11StationTrapSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 26),
    _Hh3cDot11StationTrapSSIDName_Type()
)
hh3cDot11StationTrapSSIDName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapSSIDName.setStatus("current")
_Hh3cDot11StationTrapVlan_Type = Integer32
_Hh3cDot11StationTrapVlan_Object = MibScalar
hh3cDot11StationTrapVlan = _Hh3cDot11StationTrapVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 27),
    _Hh3cDot11StationTrapVlan_Type()
)
hh3cDot11StationTrapVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapVlan.setStatus("current")
_Hh3cDot11StationTrapChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11StationTrapChannel_Object = MibScalar
hh3cDot11StationTrapChannel = _Hh3cDot11StationTrapChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 28),
    _Hh3cDot11StationTrapChannel_Type()
)
hh3cDot11StationTrapChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapChannel.setStatus("current")
_Hh3cDot11StationTrapRSSI_Type = Integer32
_Hh3cDot11StationTrapRSSI_Object = MibScalar
hh3cDot11StationTrapRSSI = _Hh3cDot11StationTrapRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 29),
    _Hh3cDot11StationTrapRSSI_Type()
)
hh3cDot11StationTrapRSSI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapRSSI.setStatus("current")
_Hh3cDot11StationTrapRxFrameKbit_Type = Counter64
_Hh3cDot11StationTrapRxFrameKbit_Object = MibScalar
hh3cDot11StationTrapRxFrameKbit = _Hh3cDot11StationTrapRxFrameKbit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 30),
    _Hh3cDot11StationTrapRxFrameKbit_Type()
)
hh3cDot11StationTrapRxFrameKbit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapRxFrameKbit.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapRxFrameKbit.setUnits("kbit")
_Hh3cDot11StationTrapTxFrameKbit_Type = Counter64
_Hh3cDot11StationTrapTxFrameKbit_Object = MibScalar
hh3cDot11StationTrapTxFrameKbit = _Hh3cDot11StationTrapTxFrameKbit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 31),
    _Hh3cDot11StationTrapTxFrameKbit_Type()
)
hh3cDot11StationTrapTxFrameKbit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapTxFrameKbit.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapTxFrameKbit.setUnits("kbit")

# Managed Objects groups


# Notification objects

hh3cDot11StationMICErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 1)
)
hh3cDot11StationMICErrorTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapBSSID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationMICErrorTrap.setStatus(
        "current"
    )

hh3cDot11StationAuthenErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 2)
)
hh3cDot11StationAuthenErrorTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapBSSID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAuthenMode"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAKMMode"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationAuthenErrorTrap.setStatus(
        "current"
    )

hh3cDot11StationAuthorFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 3)
)
hh3cDot11StationAuthorFailTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationUserName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAuthorFailCause"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationFailCauseDesc"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationBSSID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAuthMode"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationAuthorFailTrap.setStatus(
        "current"
    )

hh3cDot11StationAssocFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 4)
)
hh3cDot11StationAssocFailTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAssocFailCause"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationFailCauseDesc"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapAPMacAddress"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationBSSID"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationAssocFailTrap.setStatus(
        "current"
    )

hh3cDot11StationDeAssocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 5)
)
hh3cDot11StationDeAssocTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationUserName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationVlanId"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSessionDuration"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAPName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationBSSID"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationDeAssocTrap.setStatus(
        "current"
    )

hh3cDot11StationAuthorSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 6)
)
hh3cDot11StationAuthorSuccTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationUserName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationVlanId"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSessionStartTime"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAPName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationBSSID"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationAuthorSuccTrap.setStatus(
        "current"
    )

hh3cDot11StationRoamingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 7)
)
hh3cDot11StationRoamingTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationUserName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationVlanId"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationRoamingTime"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationACIPAddress"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationACIPv6Add"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationRoamingTrap.setStatus(
        "current"
    )

hh3cDot11StationDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 8)
)
hh3cDot11StationDisconnectTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAPName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationBSSID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSessionDuration"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationVlanId"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StaDisconnectReason"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationDisconnectTrap.setStatus(
        "current"
    )

hh3cDot11UserDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 9)
)
hh3cDot11UserDisconnectTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAPName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11UserName"))
)
if mibBuilder.loadTexts:
    hh3cDot11UserDisconnectTrap.setStatus(
        "current"
    )

hh3cDot11StaAntennaChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 10)
)
hh3cDot11StaAntennaChgTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapBSSID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapOldAntennaID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapNewAntennaID"))
)
if mibBuilder.loadTexts:
    hh3cDot11StaAntennaChgTrap.setStatus(
        "current"
    )

hh3cDot11StationAuditTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 11)
)
hh3cDot11StationAuditTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAuditTrapOpType"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaIPAddress"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapAPMacAddress"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapAPIPAddress"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapRadioMode"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapWlanID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapVlan"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapChannel"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapRSSI"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStartTime"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSessionDuration"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapRxFrameKbit"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapTxFrameKbit"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationAuditTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-STATION-MIB",
    **{"hh3cDot11STATION": hh3cDot11STATION,
       "hh3cDot11StationMtGroup": hh3cDot11StationMtGroup,
       "hh3cDot11StationAssociateTable": hh3cDot11StationAssociateTable,
       "hh3cDot11StationAssociateEntry": hh3cDot11StationAssociateEntry,
       "hh3cDot11StationMAC": hh3cDot11StationMAC,
       "hh3cDot11StationIPAddress": hh3cDot11StationIPAddress,
       "hh3cDot11StationUserName": hh3cDot11StationUserName,
       "hh3cDot11StationTxRateSet": hh3cDot11StationTxRateSet,
       "hh3cDot11StationUpTime": hh3cDot11StationUpTime,
       "hh3cDot11StationSignalStrength": hh3cDot11StationSignalStrength,
       "hh3cDot11StationRSSI": hh3cDot11StationRSSI,
       "hh3cDot11StationChannel": hh3cDot11StationChannel,
       "hh3cDot11StationPowerSaveMode": hh3cDot11StationPowerSaveMode,
       "hh3cDot11StationAid": hh3cDot11StationAid,
       "hh3cDot11StationVlanId": hh3cDot11StationVlanId,
       "hh3cDot11StationSSIDName": hh3cDot11StationSSIDName,
       "hh3cDot11StationAuthenMode": hh3cDot11StationAuthenMode,
       "hh3cDot11StationAKMMode": hh3cDot11StationAKMMode,
       "hh3cDot11StationSecurityCiphers": hh3cDot11StationSecurityCiphers,
       "hh3cDot11StationSSIDEncryptMode": hh3cDot11StationSSIDEncryptMode,
       "hh3cDot11StationRxSNR": hh3cDot11StationRxSNR,
       "hh3cDot11StationTxRate": hh3cDot11StationTxRate,
       "hh3cDot11StationRxRate": hh3cDot11StationRxRate,
       "hh3cDot11StationVendorName": hh3cDot11StationVendorName,
       "hh3cDot11StationRadioMode": hh3cDot11StationRadioMode,
       "hh3cDot11StationRxNoise": hh3cDot11StationRxNoise,
       "hh3cDot11StationMACAddress": hh3cDot11StationMACAddress,
       "hh3cDot11StationTxSpeed": hh3cDot11StationTxSpeed,
       "hh3cDot11StationRxSpeed": hh3cDot11StationRxSpeed,
       "hh3cDot11StationWmmMode": hh3cDot11StationWmmMode,
       "hh3cDot11StationSecIEStatus": hh3cDot11StationSecIEStatus,
       "hh3cDot11StationUpTimeTicks": hh3cDot11StationUpTimeTicks,
       "hh3cDot11StationRadioMode2": hh3cDot11StationRadioMode2,
       "hh3cDot11StationAssTime": hh3cDot11StationAssTime,
       "hh3cDot11StationUserAuthType": hh3cDot11StationUserAuthType,
       "hh3cDot11StationRfPingTest": hh3cDot11StationRfPingTest,
       "hh3cDot11StationMaxRate": hh3cDot11StationMaxRate,
       "hh3cDot11StationPowerSaveModeCM": hh3cDot11StationPowerSaveModeCM,
       "hh3cDot11StationAuthenModeCM": hh3cDot11StationAuthenModeCM,
       "hh3cDot11StationAKMModeCM": hh3cDot11StationAKMModeCM,
       "hh3cDot11StationSecurityCiphersCM": hh3cDot11StationSecurityCiphersCM,
       "hh3cDot11StationSecIEStatusCM": hh3cDot11StationSecIEStatusCM,
       "hh3cDot11StationIPv6Address": hh3cDot11StationIPv6Address,
       "hh3cDot11StationAssociateAPMACAddressCM": hh3cDot11StationAssociateAPMACAddressCM,
       "hh3cDot11StationDeviceType": hh3cDot11StationDeviceType,
       "hh3cDot11StationTxRateCM": hh3cDot11StationTxRateCM,
       "hh3cDot11StationRxRateCM": hh3cDot11StationRxRateCM,
       "hh3cDot11StationAPRelationTable": hh3cDot11StationAPRelationTable,
       "hh3cDot11StationAPRelationEntry": hh3cDot11StationAPRelationEntry,
       "hh3cDot11CurrAPID": hh3cDot11CurrAPID,
       "hh3cDot11CurrRadioID": hh3cDot11CurrRadioID,
       "hh3cDot11CurrWlanID": hh3cDot11CurrWlanID,
       "hh3cDot11CurrAntennaID": hh3cDot11CurrAntennaID,
       "hh3cDot11StationStatisTable": hh3cDot11StationStatisTable,
       "hh3cDot11StationStatisEntry": hh3cDot11StationStatisEntry,
       "hh3cDot11StationRxFrameCnt": hh3cDot11StationRxFrameCnt,
       "hh3cDot11StationTxFrameCnt": hh3cDot11StationTxFrameCnt,
       "hh3cDot11StationDropFrameCnt": hh3cDot11StationDropFrameCnt,
       "hh3cDot11StationRxFrameBytes": hh3cDot11StationRxFrameBytes,
       "hh3cDot11StationTxFrameBytes": hh3cDot11StationTxFrameBytes,
       "hh3cDot11StationDropFrameBytes": hh3cDot11StationDropFrameBytes,
       "hh3cDot11StationRxRetryPkts": hh3cDot11StationRxRetryPkts,
       "hh3cDot11StationTxRetryPkts": hh3cDot11StationTxRetryPkts,
       "hh3cDot11StationRxRetryBytes": hh3cDot11StationRxRetryBytes,
       "hh3cDot11StationTxRetryBytes": hh3cDot11StationTxRetryBytes,
       "hh3cDot11StationThroughput": hh3cDot11StationThroughput,
       "hh3cDot11StationSuccessTxCnt": hh3cDot11StationSuccessTxCnt,
       "hh3cDot11StationSuccessTxDataCnt": hh3cDot11StationSuccessTxDataCnt,
       "hh3cDot11StationRxDataFrameCnt": hh3cDot11StationRxDataFrameCnt,
       "hh3cDot11StationTxDataFrameCnt": hh3cDot11StationTxDataFrameCnt,
       "hh3cDot11StationRxDataFrameBytes": hh3cDot11StationRxDataFrameBytes,
       "hh3cDot11StationTxDataFrameBytes": hh3cDot11StationTxDataFrameBytes,
       "hh3cDot11StationRxFragCnt": hh3cDot11StationRxFragCnt,
       "hh3cDot11StaRxErrDataFrameCnt": hh3cDot11StaRxErrDataFrameCnt,
       "hh3cDot11StaTxRetryDataFrameCnt": hh3cDot11StaTxRetryDataFrameCnt,
       "hh3cDot11StaTxDataRatePkts": hh3cDot11StaTxDataRatePkts,
       "hh3cDot11StaRxDataRatePkts": hh3cDot11StaRxDataRatePkts,
       "hh3cDot11StaTxSignalStrengthPkts": hh3cDot11StaTxSignalStrengthPkts,
       "hh3cDot11StaInternetRxFrameBytes": hh3cDot11StaInternetRxFrameBytes,
       "hh3cDot11StaInternetTxFrameBytes": hh3cDot11StaInternetTxFrameBytes,
       "hh3cDot11StaLocalRxFrameBytes": hh3cDot11StaLocalRxFrameBytes,
       "hh3cDot11StaLocalTxFrameBytes": hh3cDot11StaLocalTxFrameBytes,
       "hh3cDot11StationRfPingTable": hh3cDot11StationRfPingTable,
       "hh3cDot11StationRfPingEntry": hh3cDot11StationRfPingEntry,
       "hh3cDot11StationRfPingIndex": hh3cDot11StationRfPingIndex,
       "hh3cDot11StationRfPingRate": hh3cDot11StationRfPingRate,
       "hh3cDot11StationRfPingTxCnt": hh3cDot11StationRfPingTxCnt,
       "hh3cDot11StationRfPingRxCnt": hh3cDot11StationRfPingRxCnt,
       "hh3cDot11StationRfPingRssi": hh3cDot11StationRfPingRssi,
       "hh3cDot11StationRfPingRetries": hh3cDot11StationRfPingRetries,
       "hh3cDot11StationRfPingRtt": hh3cDot11StationRfPingRtt,
       "hh3cDot11StationNotifyGroup": hh3cDot11StationNotifyGroup,
       "hh3cDot11StationTraps": hh3cDot11StationTraps,
       "hh3cDot11StationMICErrorTrap": hh3cDot11StationMICErrorTrap,
       "hh3cDot11StationAuthenErrorTrap": hh3cDot11StationAuthenErrorTrap,
       "hh3cDot11StationAuthorFailTrap": hh3cDot11StationAuthorFailTrap,
       "hh3cDot11StationAssocFailTrap": hh3cDot11StationAssocFailTrap,
       "hh3cDot11StationDeAssocTrap": hh3cDot11StationDeAssocTrap,
       "hh3cDot11StationAuthorSuccTrap": hh3cDot11StationAuthorSuccTrap,
       "hh3cDot11StationRoamingTrap": hh3cDot11StationRoamingTrap,
       "hh3cDot11StationDisconnectTrap": hh3cDot11StationDisconnectTrap,
       "hh3cDot11UserDisconnectTrap": hh3cDot11UserDisconnectTrap,
       "hh3cDot11StaAntennaChgTrap": hh3cDot11StaAntennaChgTrap,
       "hh3cDot11StationAuditTrap": hh3cDot11StationAuditTrap,
       "hh3cDot11StationTrapVarObjects": hh3cDot11StationTrapVarObjects,
       "hh3cDot11StationTrapBSSID": hh3cDot11StationTrapBSSID,
       "hh3cDot11StationTrapStaMAC": hh3cDot11StationTrapStaMAC,
       "hh3cDot11StationSessionStartTime": hh3cDot11StationSessionStartTime,
       "hh3cDot11StationAssocFailCause": hh3cDot11StationAssocFailCause,
       "hh3cDot11StationAuthorFailCause": hh3cDot11StationAuthorFailCause,
       "hh3cDot11StationFailCauseDesc": hh3cDot11StationFailCauseDesc,
       "hh3cDot11StationSessionDuration": hh3cDot11StationSessionDuration,
       "hh3cDot11StationRoamingTime": hh3cDot11StationRoamingTime,
       "hh3cDot11StationACIPAddress": hh3cDot11StationACIPAddress,
       "hh3cDot11StationAPName": hh3cDot11StationAPName,
       "hh3cDot11StationBSSID": hh3cDot11StationBSSID,
       "hh3cDot11StaDisconnectReason": hh3cDot11StaDisconnectReason,
       "hh3cDot11StationAuthMode": hh3cDot11StationAuthMode,
       "hh3cDot11StationACIPv6Add": hh3cDot11StationACIPv6Add,
       "hh3cDot11UserName": hh3cDot11UserName,
       "hh3cDot11StationTrapAPMacAddress": hh3cDot11StationTrapAPMacAddress,
       "hh3cDot11StationTrapOldAntennaID": hh3cDot11StationTrapOldAntennaID,
       "hh3cDot11StationTrapNewAntennaID": hh3cDot11StationTrapNewAntennaID,
       "hh3cDot11StationTrapAPIPAddress": hh3cDot11StationTrapAPIPAddress,
       "hh3cDot11StationTrapStartTime": hh3cDot11StationTrapStartTime,
       "hh3cDot11StationAuditTrapOpType": hh3cDot11StationAuditTrapOpType,
       "hh3cDot11StationTrapStaIPAddress": hh3cDot11StationTrapStaIPAddress,
       "hh3cDot11StationTrapRadioID": hh3cDot11StationTrapRadioID,
       "hh3cDot11StationTrapRadioMode": hh3cDot11StationTrapRadioMode,
       "hh3cDot11StationTrapWlanID": hh3cDot11StationTrapWlanID,
       "hh3cDot11StationTrapSSIDName": hh3cDot11StationTrapSSIDName,
       "hh3cDot11StationTrapVlan": hh3cDot11StationTrapVlan,
       "hh3cDot11StationTrapChannel": hh3cDot11StationTrapChannel,
       "hh3cDot11StationTrapRSSI": hh3cDot11StationTrapRSSI,
       "hh3cDot11StationTrapRxFrameKbit": hh3cDot11StationTrapRxFrameKbit,
       "hh3cDot11StationTrapTxFrameKbit": hh3cDot11StationTrapTxFrameKbit}
)
