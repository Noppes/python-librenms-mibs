# SNMP MIB module (HH3C-EPON-UNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-EPON-UNI-MIB

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

(hh3cEpon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cEpon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cEponUni = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5)
)
if mibBuilder.loadTexts:
    hh3cEponUni.setRevisions(
        ("2018-11-28 10:49",
         "2017-06-06 11:45",
         "2017-03-06 11:45")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cEponUniSysMan_ObjectIdentity = ObjectIdentity
hh3cEponUniSysMan = _Hh3cEponUniSysMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1)
)
_Hh3cEponUniSysManTable_Object = MibTable
hh3cEponUniSysManTable = _Hh3cEponUniSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cEponUniSysManTable.setStatus("current")
_Hh3cEponUniSysManEntry_Object = MibTableRow
hh3cEponUniSysManEntry = _Hh3cEponUniSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1)
)
hh3cEponUniSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniSysManEntry.setStatus("current")
_Hh3cEponUniIndex_Type = Integer32
_Hh3cEponUniIndex_Object = MibTableColumn
hh3cEponUniIndex = _Hh3cEponUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 1),
    _Hh3cEponUniIndex_Type()
)
hh3cEponUniIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEponUniIndex.setStatus("current")
_Hh3cEponUniDescr_Type = OctetString
_Hh3cEponUniDescr_Object = MibTableColumn
hh3cEponUniDescr = _Hh3cEponUniDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 2),
    _Hh3cEponUniDescr_Type()
)
hh3cEponUniDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniDescr.setStatus("current")


class _Hh3cEponUniAdminStatus_Type(Integer32):
    """Custom type hh3cEponUniAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_Hh3cEponUniAdminStatus_Type.__name__ = "Integer32"
_Hh3cEponUniAdminStatus_Object = MibTableColumn
hh3cEponUniAdminStatus = _Hh3cEponUniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 3),
    _Hh3cEponUniAdminStatus_Type()
)
hh3cEponUniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniAdminStatus.setStatus("current")


class _Hh3cEponUniMdi_Type(Integer32):
    """Custom type hh3cEponUniMdi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mdi-ii", 1),
          ("mdi-x", 2),
          ("mdi-auto", 3))
    )


_Hh3cEponUniMdi_Type.__name__ = "Integer32"
_Hh3cEponUniMdi_Object = MibTableColumn
hh3cEponUniMdi = _Hh3cEponUniMdi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 4),
    _Hh3cEponUniMdi_Type()
)
hh3cEponUniMdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniMdi.setStatus("current")


class _Hh3cEponUniPriority_Type(Integer32):
    """Custom type hh3cEponUniPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cEponUniPriority_Type.__name__ = "Integer32"
_Hh3cEponUniPriority_Object = MibTableColumn
hh3cEponUniPriority = _Hh3cEponUniPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 5),
    _Hh3cEponUniPriority_Type()
)
hh3cEponUniPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPriority.setStatus("current")


class _Hh3cEponUniVlanType_Type(Integer32):
    """Custom type hh3cEponUniVlanType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("vlantrunk", 1),
          ("access", 2),
          ("hybrid", 3),
          ("untagged", 4),
          ("transparent", 5),
          ("doubletagged", 6),
          ("tag", 7),
          ("translation", 8),
          ("aggregation", 9))
    )


_Hh3cEponUniVlanType_Type.__name__ = "Integer32"
_Hh3cEponUniVlanType_Object = MibTableColumn
hh3cEponUniVlanType = _Hh3cEponUniVlanType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 6),
    _Hh3cEponUniVlanType_Type()
)
hh3cEponUniVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniVlanType.setStatus("current")


class _Hh3cEponUniAccessVlan_Type(Integer32):
    """Custom type hh3cEponUniAccessVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cEponUniAccessVlan_Type.__name__ = "Integer32"
_Hh3cEponUniAccessVlan_Object = MibTableColumn
hh3cEponUniAccessVlan = _Hh3cEponUniAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 7),
    _Hh3cEponUniAccessVlan_Type()
)
hh3cEponUniAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniAccessVlan.setStatus("current")


class _Hh3cEponUniTrunkPvid_Type(Integer32):
    """Custom type hh3cEponUniTrunkPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cEponUniTrunkPvid_Type.__name__ = "Integer32"
_Hh3cEponUniTrunkPvid_Object = MibTableColumn
hh3cEponUniTrunkPvid = _Hh3cEponUniTrunkPvid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 8),
    _Hh3cEponUniTrunkPvid_Type()
)
hh3cEponUniTrunkPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniTrunkPvid.setStatus("current")
_Hh3cEponUniVLANTrunkAllowListLow_Type = OctetString
_Hh3cEponUniVLANTrunkAllowListLow_Object = MibTableColumn
hh3cEponUniVLANTrunkAllowListLow = _Hh3cEponUniVLANTrunkAllowListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 9),
    _Hh3cEponUniVLANTrunkAllowListLow_Type()
)
hh3cEponUniVLANTrunkAllowListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniVLANTrunkAllowListLow.setStatus("current")
_Hh3cEponUniVLANTrunkAllowListHigh_Type = OctetString
_Hh3cEponUniVLANTrunkAllowListHigh_Object = MibTableColumn
hh3cEponUniVLANTrunkAllowListHigh = _Hh3cEponUniVLANTrunkAllowListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 10),
    _Hh3cEponUniVLANTrunkAllowListHigh_Type()
)
hh3cEponUniVLANTrunkAllowListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniVLANTrunkAllowListHigh.setStatus("current")
_Hh3cEponUniInboundLineRate_Type = Integer32
_Hh3cEponUniInboundLineRate_Object = MibTableColumn
hh3cEponUniInboundLineRate = _Hh3cEponUniInboundLineRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 11),
    _Hh3cEponUniInboundLineRate_Type()
)
hh3cEponUniInboundLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniInboundLineRate.setStatus("current")
_Hh3cEponUniOutboundLineRate_Type = Integer32
_Hh3cEponUniOutboundLineRate_Object = MibTableColumn
hh3cEponUniOutboundLineRate = _Hh3cEponUniOutboundLineRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 12),
    _Hh3cEponUniOutboundLineRate_Type()
)
hh3cEponUniOutboundLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniOutboundLineRate.setStatus("current")
_Hh3cEponUniFlowControl_Type = TruthValue
_Hh3cEponUniFlowControl_Object = MibTableColumn
hh3cEponUniFlowControl = _Hh3cEponUniFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 13),
    _Hh3cEponUniFlowControl_Type()
)
hh3cEponUniFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniFlowControl.setStatus("current")


class _Hh3cEponUniSpeed_Type(Integer32):
    """Custom type hh3cEponUniSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              100,
              1000,
              10000,
              24000)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("s10M", 10),
          ("s100M", 100),
          ("s1000M", 1000),
          ("s10000M", 10000),
          ("s24000M", 24000))
    )


_Hh3cEponUniSpeed_Type.__name__ = "Integer32"
_Hh3cEponUniSpeed_Object = MibTableColumn
hh3cEponUniSpeed = _Hh3cEponUniSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 14),
    _Hh3cEponUniSpeed_Type()
)
hh3cEponUniSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniSpeed.setStatus("current")


class _Hh3cEponUniDuplex_Type(Integer32):
    """Custom type hh3cEponUniDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("auto", 3))
    )


_Hh3cEponUniDuplex_Type.__name__ = "Integer32"
_Hh3cEponUniDuplex_Object = MibTableColumn
hh3cEponUniDuplex = _Hh3cEponUniDuplex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 15),
    _Hh3cEponUniDuplex_Type()
)
hh3cEponUniDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniDuplex.setStatus("current")
_Hh3cEponUniVlanVPNStatus_Type = TruthValue
_Hh3cEponUniVlanVPNStatus_Object = MibTableColumn
hh3cEponUniVlanVPNStatus = _Hh3cEponUniVlanVPNStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 16),
    _Hh3cEponUniVlanVPNStatus_Type()
)
hh3cEponUniVlanVPNStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniVlanVPNStatus.setStatus("current")


class _Hh3cEponUniCountReset_Type(Integer32):
    """Custom type hh3cEponUniCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cEponUniCountReset_Type.__name__ = "Integer32"
_Hh3cEponUniCountReset_Object = MibTableColumn
hh3cEponUniCountReset = _Hh3cEponUniCountReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 17),
    _Hh3cEponUniCountReset_Type()
)
hh3cEponUniCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniCountReset.setStatus("current")


class _Hh3cEponUniPortIsolate_Type(Integer32):
    """Custom type hh3cEponUniPortIsolate based on Integer32"""
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


_Hh3cEponUniPortIsolate_Type.__name__ = "Integer32"
_Hh3cEponUniPortIsolate_Object = MibTableColumn
hh3cEponUniPortIsolate = _Hh3cEponUniPortIsolate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 18),
    _Hh3cEponUniPortIsolate_Type()
)
hh3cEponUniPortIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortIsolate.setStatus("current")


class _Hh3cEponUniVlanConfiguration_Type(OctetString):
    """Custom type hh3cEponUniVlanConfiguration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponUniVlanConfiguration_Type.__name__ = "OctetString"
_Hh3cEponUniVlanConfiguration_Object = MibTableColumn
hh3cEponUniVlanConfiguration = _Hh3cEponUniVlanConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 23),
    _Hh3cEponUniVlanConfiguration_Type()
)
hh3cEponUniVlanConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniVlanConfiguration.setStatus("current")


class _Hh3cEponUniAutoNegotiation_Type(Integer32):
    """Custom type hh3cEponUniAutoNegotiation based on Integer32"""
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


_Hh3cEponUniAutoNegotiation_Type.__name__ = "Integer32"
_Hh3cEponUniAutoNegotiation_Object = MibTableColumn
hh3cEponUniAutoNegotiation = _Hh3cEponUniAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 25),
    _Hh3cEponUniAutoNegotiation_Type()
)
hh3cEponUniAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniAutoNegotiation.setStatus("current")


class _Hh3cEponUniRestartAutoNeg_Type(Integer32):
    """Custom type hh3cEponUniRestartAutoNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("autoNegotiation", 1)
    )


_Hh3cEponUniRestartAutoNeg_Type.__name__ = "Integer32"
_Hh3cEponUniRestartAutoNeg_Object = MibTableColumn
hh3cEponUniRestartAutoNeg = _Hh3cEponUniRestartAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 26),
    _Hh3cEponUniRestartAutoNeg_Type()
)
hh3cEponUniRestartAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniRestartAutoNeg.setStatus("current")


class _Hh3cEponUniLinkStatus_Type(Integer32):
    """Custom type hh3cEponUniLinkStatus based on Integer32"""
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


_Hh3cEponUniLinkStatus_Type.__name__ = "Integer32"
_Hh3cEponUniLinkStatus_Object = MibTableColumn
hh3cEponUniLinkStatus = _Hh3cEponUniLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 29),
    _Hh3cEponUniLinkStatus_Type()
)
hh3cEponUniLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniLinkStatus.setStatus("current")


class _Hh3cEponUniInterfaceType_Type(Integer32):
    """Custom type hh3cEponUniInterfaceType based on Integer32"""
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
        *(("gigabitethernetport", 1),
          ("fastethernetport", 2),
          ("voipport", 3),
          ("e1port", 4))
    )


_Hh3cEponUniInterfaceType_Type.__name__ = "Integer32"
_Hh3cEponUniInterfaceType_Object = MibTableColumn
hh3cEponUniInterfaceType = _Hh3cEponUniInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 30),
    _Hh3cEponUniInterfaceType_Type()
)
hh3cEponUniInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInterfaceType.setStatus("current")


class _Hh3cEponUniVitualCableTest_Type(Integer32):
    """Custom type hh3cEponUniVitualCableTest based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_Hh3cEponUniVitualCableTest_Type.__name__ = "Integer32"
_Hh3cEponUniVitualCableTest_Object = MibTableColumn
hh3cEponUniVitualCableTest = _Hh3cEponUniVitualCableTest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 31),
    _Hh3cEponUniVitualCableTest_Type()
)
hh3cEponUniVitualCableTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniVitualCableTest.setStatus("current")


class _Hh3cEponUniVCTCableStatus_Type(Integer32):
    """Custom type hh3cEponUniVCTCableStatus based on Integer32"""
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
        *(("normal", 1),
          ("abnormal", 2),
          ("abnormalOpen", 3),
          ("abnormalShort", 4),
          ("failure", 5))
    )


_Hh3cEponUniVCTCableStatus_Type.__name__ = "Integer32"
_Hh3cEponUniVCTCableStatus_Object = MibTableColumn
hh3cEponUniVCTCableStatus = _Hh3cEponUniVCTCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 32),
    _Hh3cEponUniVCTCableStatus_Type()
)
hh3cEponUniVCTCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTCableStatus.setStatus("current")
_Hh3cEponUniVCTCableLength_Type = Integer32
_Hh3cEponUniVCTCableLength_Object = MibTableColumn
hh3cEponUniVCTCableLength = _Hh3cEponUniVCTCableLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 33),
    _Hh3cEponUniVCTCableLength_Type()
)
hh3cEponUniVCTCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTCableLength.setStatus("current")


class _Hh3cEponUniVCTImpedanceMismatch_Type(Integer32):
    """Custom type hh3cEponUniVCTImpedanceMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-support", 1),
          ("true", 2),
          ("false", 3))
    )


_Hh3cEponUniVCTImpedanceMismatch_Type.__name__ = "Integer32"
_Hh3cEponUniVCTImpedanceMismatch_Object = MibTableColumn
hh3cEponUniVCTImpedanceMismatch = _Hh3cEponUniVCTImpedanceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 34),
    _Hh3cEponUniVCTImpedanceMismatch_Type()
)
hh3cEponUniVCTImpedanceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTImpedanceMismatch.setStatus("current")
_Hh3cEponUniVCTPairSkew_Type = Integer32
_Hh3cEponUniVCTPairSkew_Object = MibTableColumn
hh3cEponUniVCTPairSkew = _Hh3cEponUniVCTPairSkew_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 35),
    _Hh3cEponUniVCTPairSkew_Type()
)
hh3cEponUniVCTPairSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTPairSkew.setStatus("current")


class _Hh3cEponUniVCTPairSwap_Type(Integer32):
    """Custom type hh3cEponUniVCTPairSwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupport", 1),
          ("true", 2),
          ("false", 3))
    )


_Hh3cEponUniVCTPairSwap_Type.__name__ = "Integer32"
_Hh3cEponUniVCTPairSwap_Object = MibTableColumn
hh3cEponUniVCTPairSwap = _Hh3cEponUniVCTPairSwap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 36),
    _Hh3cEponUniVCTPairSwap_Type()
)
hh3cEponUniVCTPairSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTPairSwap.setStatus("current")


class _Hh3cEponUniVCTPolaritySwap_Type(Integer32):
    """Custom type hh3cEponUniVCTPolaritySwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupport", 1),
          ("true", 2),
          ("false", 3))
    )


_Hh3cEponUniVCTPolaritySwap_Type.__name__ = "Integer32"
_Hh3cEponUniVCTPolaritySwap_Object = MibTableColumn
hh3cEponUniVCTPolaritySwap = _Hh3cEponUniVCTPolaritySwap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 37),
    _Hh3cEponUniVCTPolaritySwap_Type()
)
hh3cEponUniVCTPolaritySwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTPolaritySwap.setStatus("current")
_Hh3cEponUniVCTInsertionLoss_Type = Integer32
_Hh3cEponUniVCTInsertionLoss_Object = MibTableColumn
hh3cEponUniVCTInsertionLoss = _Hh3cEponUniVCTInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 38),
    _Hh3cEponUniVCTInsertionLoss_Type()
)
hh3cEponUniVCTInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTInsertionLoss.setStatus("current")
_Hh3cEponUniVCTReturnLoss_Type = Integer32
_Hh3cEponUniVCTReturnLoss_Object = MibTableColumn
hh3cEponUniVCTReturnLoss = _Hh3cEponUniVCTReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 39),
    _Hh3cEponUniVCTReturnLoss_Type()
)
hh3cEponUniVCTReturnLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTReturnLoss.setStatus("current")
_Hh3cEponUniVCTNearendCrosstalk_Type = Integer32
_Hh3cEponUniVCTNearendCrosstalk_Object = MibTableColumn
hh3cEponUniVCTNearendCrosstalk = _Hh3cEponUniVCTNearendCrosstalk_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 40),
    _Hh3cEponUniVCTNearendCrosstalk_Type()
)
hh3cEponUniVCTNearendCrosstalk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTNearendCrosstalk.setStatus("current")
_Hh3cEponUniVlan_Type = Integer32
_Hh3cEponUniVlan_Object = MibTableColumn
hh3cEponUniVlan = _Hh3cEponUniVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 41),
    _Hh3cEponUniVlan_Type()
)
hh3cEponUniVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEponUniVlan.setStatus("current")


class _Hh3cEponUniMacMax_Type(Integer32):
    """Custom type hh3cEponUniMacMax based on Integer32"""
    defaultValue = 65535


_Hh3cEponUniMacMax_Type.__name__ = "Integer32"
_Hh3cEponUniMacMax_Object = MibTableColumn
hh3cEponUniMacMax = _Hh3cEponUniMacMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 42),
    _Hh3cEponUniMacMax_Type()
)
hh3cEponUniMacMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniMacMax.setStatus("current")
_Hh3cEponUniCountTable_Object = MibTable
hh3cEponUniCountTable = _Hh3cEponUniCountTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cEponUniCountTable.setStatus("current")
_Hh3cEponUniCountEntry_Object = MibTableRow
hh3cEponUniCountEntry = _Hh3cEponUniCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1)
)
hh3cEponUniCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniCountEntry.setStatus("current")
_Hh3cEponUniInStatsPkts_Type = Unsigned32
_Hh3cEponUniInStatsPkts_Object = MibTableColumn
hh3cEponUniInStatsPkts = _Hh3cEponUniInStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 1),
    _Hh3cEponUniInStatsPkts_Type()
)
hh3cEponUniInStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInStatsPkts.setStatus("current")
_Hh3cEponUniInStatsUnicastPkts_Type = Unsigned32
_Hh3cEponUniInStatsUnicastPkts_Object = MibTableColumn
hh3cEponUniInStatsUnicastPkts = _Hh3cEponUniInStatsUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 2),
    _Hh3cEponUniInStatsUnicastPkts_Type()
)
hh3cEponUniInStatsUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInStatsUnicastPkts.setStatus("current")
_Hh3cEponUniInStatsBroadcastPkts_Type = Unsigned32
_Hh3cEponUniInStatsBroadcastPkts_Object = MibTableColumn
hh3cEponUniInStatsBroadcastPkts = _Hh3cEponUniInStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 3),
    _Hh3cEponUniInStatsBroadcastPkts_Type()
)
hh3cEponUniInStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInStatsBroadcastPkts.setStatus("current")
_Hh3cEponUniInStatsMulticastPkts_Type = Unsigned32
_Hh3cEponUniInStatsMulticastPkts_Object = MibTableColumn
hh3cEponUniInStatsMulticastPkts = _Hh3cEponUniInStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 4),
    _Hh3cEponUniInStatsMulticastPkts_Type()
)
hh3cEponUniInStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInStatsMulticastPkts.setStatus("current")
_Hh3cEponUniInPausePkts_Type = Unsigned32
_Hh3cEponUniInPausePkts_Object = MibTableColumn
hh3cEponUniInPausePkts = _Hh3cEponUniInPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 5),
    _Hh3cEponUniInPausePkts_Type()
)
hh3cEponUniInPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInPausePkts.setStatus("current")
_Hh3cEponUniInTotalErrors_Type = Unsigned32
_Hh3cEponUniInTotalErrors_Object = MibTableColumn
hh3cEponUniInTotalErrors = _Hh3cEponUniInTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 6),
    _Hh3cEponUniInTotalErrors_Type()
)
hh3cEponUniInTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInTotalErrors.setStatus("current")
_Hh3cEponUniInStatsCRCAlignErrors_Type = Unsigned32
_Hh3cEponUniInStatsCRCAlignErrors_Object = MibTableColumn
hh3cEponUniInStatsCRCAlignErrors = _Hh3cEponUniInStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 7),
    _Hh3cEponUniInStatsCRCAlignErrors_Type()
)
hh3cEponUniInStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInStatsCRCAlignErrors.setStatus("current")
_Hh3cEponUniInStatsUndersizePkts_Type = Unsigned32
_Hh3cEponUniInStatsUndersizePkts_Object = MibTableColumn
hh3cEponUniInStatsUndersizePkts = _Hh3cEponUniInStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 8),
    _Hh3cEponUniInStatsUndersizePkts_Type()
)
hh3cEponUniInStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInStatsUndersizePkts.setStatus("current")
_Hh3cEponUniInStatsOversizePkts_Type = Unsigned32
_Hh3cEponUniInStatsOversizePkts_Object = MibTableColumn
hh3cEponUniInStatsOversizePkts = _Hh3cEponUniInStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 9),
    _Hh3cEponUniInStatsOversizePkts_Type()
)
hh3cEponUniInStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInStatsOversizePkts.setStatus("current")
_Hh3cEponUniInErrorbyOther_Type = Unsigned32
_Hh3cEponUniInErrorbyOther_Object = MibTableColumn
hh3cEponUniInErrorbyOther = _Hh3cEponUniInErrorbyOther_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 10),
    _Hh3cEponUniInErrorbyOther_Type()
)
hh3cEponUniInErrorbyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInErrorbyOther.setStatus("current")
_Hh3cEponUniOutStatsPkts_Type = Unsigned32
_Hh3cEponUniOutStatsPkts_Object = MibTableColumn
hh3cEponUniOutStatsPkts = _Hh3cEponUniOutStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 11),
    _Hh3cEponUniOutStatsPkts_Type()
)
hh3cEponUniOutStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutStatsPkts.setStatus("current")
_Hh3cEponUniOutStatsUnicastPkts_Type = Unsigned32
_Hh3cEponUniOutStatsUnicastPkts_Object = MibTableColumn
hh3cEponUniOutStatsUnicastPkts = _Hh3cEponUniOutStatsUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 12),
    _Hh3cEponUniOutStatsUnicastPkts_Type()
)
hh3cEponUniOutStatsUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutStatsUnicastPkts.setStatus("current")
_Hh3cEponUniOutStatsBroadcastPkts_Type = Unsigned32
_Hh3cEponUniOutStatsBroadcastPkts_Object = MibTableColumn
hh3cEponUniOutStatsBroadcastPkts = _Hh3cEponUniOutStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 13),
    _Hh3cEponUniOutStatsBroadcastPkts_Type()
)
hh3cEponUniOutStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutStatsBroadcastPkts.setStatus("current")
_Hh3cEponUniOutStatsMulticastPkts_Type = Unsigned32
_Hh3cEponUniOutStatsMulticastPkts_Object = MibTableColumn
hh3cEponUniOutStatsMulticastPkts = _Hh3cEponUniOutStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 14),
    _Hh3cEponUniOutStatsMulticastPkts_Type()
)
hh3cEponUniOutStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutStatsMulticastPkts.setStatus("current")
_Hh3cEponUniOutStatsPausePkts_Type = Unsigned32
_Hh3cEponUniOutStatsPausePkts_Object = MibTableColumn
hh3cEponUniOutStatsPausePkts = _Hh3cEponUniOutStatsPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 15),
    _Hh3cEponUniOutStatsPausePkts_Type()
)
hh3cEponUniOutStatsPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutStatsPausePkts.setStatus("current")
_Hh3cEponUniOutTotalErrors_Type = Unsigned32
_Hh3cEponUniOutTotalErrors_Object = MibTableColumn
hh3cEponUniOutTotalErrors = _Hh3cEponUniOutTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 16),
    _Hh3cEponUniOutTotalErrors_Type()
)
hh3cEponUniOutTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutTotalErrors.setStatus("current")
_Hh3cEponUniOutStatsCollisions_Type = Unsigned32
_Hh3cEponUniOutStatsCollisions_Object = MibTableColumn
hh3cEponUniOutStatsCollisions = _Hh3cEponUniOutStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 17),
    _Hh3cEponUniOutStatsCollisions_Type()
)
hh3cEponUniOutStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutStatsCollisions.setStatus("current")
_Hh3cEponUniOutDelayExceededDiscards_Type = Unsigned32
_Hh3cEponUniOutDelayExceededDiscards_Object = MibTableColumn
hh3cEponUniOutDelayExceededDiscards = _Hh3cEponUniOutDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 18),
    _Hh3cEponUniOutDelayExceededDiscards_Type()
)
hh3cEponUniOutDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutDelayExceededDiscards.setStatus("current")
_Hh3cEponUniOutErrorbyOther_Type = Unsigned32
_Hh3cEponUniOutErrorbyOther_Object = MibTableColumn
hh3cEponUniOutErrorbyOther = _Hh3cEponUniOutErrorbyOther_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 19),
    _Hh3cEponUniOutErrorbyOther_Type()
)
hh3cEponUniOutErrorbyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutErrorbyOther.setStatus("current")
_Hh3cEponUniOutDroppedFrames_Type = Unsigned32
_Hh3cEponUniOutDroppedFrames_Object = MibTableColumn
hh3cEponUniOutDroppedFrames = _Hh3cEponUniOutDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 20),
    _Hh3cEponUniOutDroppedFrames_Type()
)
hh3cEponUniOutDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutDroppedFrames.setStatus("current")
_Hh3cEponUniIgmpInfoTable_Object = MibTable
hh3cEponUniIgmpInfoTable = _Hh3cEponUniIgmpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cEponUniIgmpInfoTable.setStatus("current")
_Hh3cEponUniIgmpInfoEntry_Object = MibTableRow
hh3cEponUniIgmpInfoEntry = _Hh3cEponUniIgmpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 3, 1)
)
hh3cEponUniIgmpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniMacIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniIgmpInfoEntry.setStatus("current")
_Hh3cEponUniMacIndex_Type = Integer32
_Hh3cEponUniMacIndex_Object = MibTableColumn
hh3cEponUniMacIndex = _Hh3cEponUniMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 3, 1, 1),
    _Hh3cEponUniMacIndex_Type()
)
hh3cEponUniMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponUniMacIndex.setStatus("current")
_Hh3cEponUniIgmpMacAddress_Type = MacAddress
_Hh3cEponUniIgmpMacAddress_Object = MibTableColumn
hh3cEponUniIgmpMacAddress = _Hh3cEponUniIgmpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 3, 1, 2),
    _Hh3cEponUniIgmpMacAddress_Type()
)
hh3cEponUniIgmpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniIgmpMacAddress.setStatus("current")


class _Hh3cEponUniIgmpVlanId_Type(Integer32):
    """Custom type hh3cEponUniIgmpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cEponUniIgmpVlanId_Type.__name__ = "Integer32"
_Hh3cEponUniIgmpVlanId_Object = MibTableColumn
hh3cEponUniIgmpVlanId = _Hh3cEponUniIgmpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 3, 1, 3),
    _Hh3cEponUniIgmpVlanId_Type()
)
hh3cEponUniIgmpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniIgmpVlanId.setStatus("current")
_Hh3cEponUniParaMan_ObjectIdentity = ObjectIdentity
hh3cEponUniParaMan = _Hh3cEponUniParaMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 4)
)
_Hh3cEponUniLineRateMax_Type = Integer32
_Hh3cEponUniLineRateMax_Object = MibScalar
hh3cEponUniLineRateMax = _Hh3cEponUniLineRateMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 4, 1),
    _Hh3cEponUniLineRateMax_Type()
)
hh3cEponUniLineRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniLineRateMax.setStatus("current")
_Hh3cEponUniLineRateStep_Type = Integer32
_Hh3cEponUniLineRateStep_Object = MibScalar
hh3cEponUniLineRateStep = _Hh3cEponUniLineRateStep_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 4, 2),
    _Hh3cEponUniLineRateStep_Type()
)
hh3cEponUniLineRateStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniLineRateStep.setStatus("current")
_Hh3cEponUniNumberOnOnu_Type = Integer32
_Hh3cEponUniNumberOnOnu_Object = MibScalar
hh3cEponUniNumberOnOnu = _Hh3cEponUniNumberOnOnu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 4, 3),
    _Hh3cEponUniNumberOnOnu_Type()
)
hh3cEponUniNumberOnOnu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniNumberOnOnu.setStatus("current")
_Hh3cEponUniScalarGroup_ObjectIdentity = ObjectIdentity
hh3cEponUniScalarGroup = _Hh3cEponUniScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 5)
)
_Hh3cEponUniPortPolicyTable_Object = MibTable
hh3cEponUniPortPolicyTable = _Hh3cEponUniPortPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyTable.setStatus("current")
_Hh3cEponUniPortPolicyEntry_Object = MibTableRow
hh3cEponUniPortPolicyEntry = _Hh3cEponUniPortPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1)
)
hh3cEponUniPortPolicyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyEntry.setStatus("current")


class _Hh3cEponUniPortPolicyStatus_Type(Integer32):
    """Custom type hh3cEponUniPortPolicyStatus based on Integer32"""
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


_Hh3cEponUniPortPolicyStatus_Type.__name__ = "Integer32"
_Hh3cEponUniPortPolicyStatus_Object = MibTableColumn
hh3cEponUniPortPolicyStatus = _Hh3cEponUniPortPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 1),
    _Hh3cEponUniPortPolicyStatus_Type()
)
hh3cEponUniPortPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyStatus.setStatus("current")


class _Hh3cEponUniPortPolicyCir_Type(Integer32):
    """Custom type hh3cEponUniPortPolicyCir based on Integer32"""
    defaultValue = 102400


_Hh3cEponUniPortPolicyCir_Type.__name__ = "Integer32"
_Hh3cEponUniPortPolicyCir_Object = MibTableColumn
hh3cEponUniPortPolicyCir = _Hh3cEponUniPortPolicyCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 2),
    _Hh3cEponUniPortPolicyCir_Type()
)
hh3cEponUniPortPolicyCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyCir.setStatus("current")


class _Hh3cEponUniPortPolicyBucketDepth_Type(Integer32):
    """Custom type hh3cEponUniPortPolicyBucketDepth based on Integer32"""
    defaultValue = 0


_Hh3cEponUniPortPolicyBucketDepth_Type.__name__ = "Integer32"
_Hh3cEponUniPortPolicyBucketDepth_Object = MibTableColumn
hh3cEponUniPortPolicyBucketDepth = _Hh3cEponUniPortPolicyBucketDepth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 3),
    _Hh3cEponUniPortPolicyBucketDepth_Type()
)
hh3cEponUniPortPolicyBucketDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyBucketDepth.setStatus("current")


class _Hh3cEponUniPortPolicyExtraBurst_Type(Integer32):
    """Custom type hh3cEponUniPortPolicyExtraBurst based on Integer32"""
    defaultValue = 0


_Hh3cEponUniPortPolicyExtraBurst_Type.__name__ = "Integer32"
_Hh3cEponUniPortPolicyExtraBurst_Object = MibTableColumn
hh3cEponUniPortPolicyExtraBurst = _Hh3cEponUniPortPolicyExtraBurst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 4),
    _Hh3cEponUniPortPolicyExtraBurst_Type()
)
hh3cEponUniPortPolicyExtraBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyExtraBurst.setStatus("current")
_Hh3cEponUniPortPolicyInboundCir_Type = Integer32
_Hh3cEponUniPortPolicyInboundCir_Object = MibTableColumn
hh3cEponUniPortPolicyInboundCir = _Hh3cEponUniPortPolicyInboundCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 5),
    _Hh3cEponUniPortPolicyInboundCir_Type()
)
hh3cEponUniPortPolicyInboundCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyInboundCir.setStatus("current")


class _Hh3cEponUniPortPolicyInboundBucketDepth_Type(Integer32):
    """Custom type hh3cEponUniPortPolicyInboundBucketDepth based on Integer32"""
    defaultValue = 0


_Hh3cEponUniPortPolicyInboundBucketDepth_Type.__name__ = "Integer32"
_Hh3cEponUniPortPolicyInboundBucketDepth_Object = MibTableColumn
hh3cEponUniPortPolicyInboundBucketDepth = _Hh3cEponUniPortPolicyInboundBucketDepth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 6),
    _Hh3cEponUniPortPolicyInboundBucketDepth_Type()
)
hh3cEponUniPortPolicyInboundBucketDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyInboundBucketDepth.setStatus("current")


class _Hh3cEponUniPortPolicyInboundExtraBurst_Type(Integer32):
    """Custom type hh3cEponUniPortPolicyInboundExtraBurst based on Integer32"""
    defaultValue = 0


_Hh3cEponUniPortPolicyInboundExtraBurst_Type.__name__ = "Integer32"
_Hh3cEponUniPortPolicyInboundExtraBurst_Object = MibTableColumn
hh3cEponUniPortPolicyInboundExtraBurst = _Hh3cEponUniPortPolicyInboundExtraBurst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 7),
    _Hh3cEponUniPortPolicyInboundExtraBurst_Type()
)
hh3cEponUniPortPolicyInboundExtraBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyInboundExtraBurst.setStatus("current")
_Hh3cEponUniPortPolicyOutboundCir_Type = Integer32
_Hh3cEponUniPortPolicyOutboundCir_Object = MibTableColumn
hh3cEponUniPortPolicyOutboundCir = _Hh3cEponUniPortPolicyOutboundCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 8),
    _Hh3cEponUniPortPolicyOutboundCir_Type()
)
hh3cEponUniPortPolicyOutboundCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyOutboundCir.setStatus("current")
_Hh3cEponUniPortPolicyOutboundPir_Type = Integer32
_Hh3cEponUniPortPolicyOutboundPir_Object = MibTableColumn
hh3cEponUniPortPolicyOutboundPir = _Hh3cEponUniPortPolicyOutboundPir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 9),
    _Hh3cEponUniPortPolicyOutboundPir_Type()
)
hh3cEponUniPortPolicyOutboundPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyOutboundPir.setStatus("current")
_Hh3cEponUniMulticastTable_Object = MibTable
hh3cEponUniMulticastTable = _Hh3cEponUniMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastTable.setStatus("current")
_Hh3cEponUniMulticastEntry_Object = MibTableRow
hh3cEponUniMulticastEntry = _Hh3cEponUniMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 7, 1)
)
hh3cEponUniMulticastEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastEntry.setStatus("current")


class _Hh3cEponUniMulticastGroupNumber_Type(Integer32):
    """Custom type hh3cEponUniMulticastGroupNumber based on Integer32"""
    defaultValue = 64


_Hh3cEponUniMulticastGroupNumber_Type.__name__ = "Integer32"
_Hh3cEponUniMulticastGroupNumber_Object = MibTableColumn
hh3cEponUniMulticastGroupNumber = _Hh3cEponUniMulticastGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 7, 1, 1),
    _Hh3cEponUniMulticastGroupNumber_Type()
)
hh3cEponUniMulticastGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastGroupNumber.setStatus("current")


class _Hh3cEponUniMulticastVlanList_Type(OctetString):
    """Custom type hh3cEponUniMulticastVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponUniMulticastVlanList_Type.__name__ = "OctetString"
_Hh3cEponUniMulticastVlanList_Object = MibTableColumn
hh3cEponUniMulticastVlanList = _Hh3cEponUniMulticastVlanList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 7, 1, 2),
    _Hh3cEponUniMulticastVlanList_Type()
)
hh3cEponUniMulticastVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastVlanList.setStatus("current")


class _Hh3cEponUniMulticastStripStatus_Type(Integer32):
    """Custom type hh3cEponUniMulticastStripStatus based on Integer32"""
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


_Hh3cEponUniMulticastStripStatus_Type.__name__ = "Integer32"
_Hh3cEponUniMulticastStripStatus_Object = MibTableColumn
hh3cEponUniMulticastStripStatus = _Hh3cEponUniMulticastStripStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 7, 1, 3),
    _Hh3cEponUniMulticastStripStatus_Type()
)
hh3cEponUniMulticastStripStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastStripStatus.setStatus("current")


class _Hh3cEponUniMulticastFastleave_Type(TruthValue):
    """Custom type hh3cEponUniMulticastFastleave based on TruthValue"""
    defaultValue = 2


_Hh3cEponUniMulticastFastleave_Type.__name__ = "TruthValue"
_Hh3cEponUniMulticastFastleave_Object = MibTableColumn
hh3cEponUniMulticastFastleave = _Hh3cEponUniMulticastFastleave_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 7, 1, 4),
    _Hh3cEponUniMulticastFastleave_Type()
)
hh3cEponUniMulticastFastleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastFastleave.setStatus("current")
_Hh3cEponUniTechAbilityTable_Object = MibTable
hh3cEponUniTechAbilityTable = _Hh3cEponUniTechAbilityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cEponUniTechAbilityTable.setStatus("current")
_Hh3cEponUniTechAbilityEntry_Object = MibTableRow
hh3cEponUniTechAbilityEntry = _Hh3cEponUniTechAbilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 8, 1)
)
hh3cEponUniTechAbilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniTechAbilityEntry.setStatus("current")


class _Hh3cEponUniLocalTechAbility_Type(OctetString):
    """Custom type hh3cEponUniLocalTechAbility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponUniLocalTechAbility_Type.__name__ = "OctetString"
_Hh3cEponUniLocalTechAbility_Object = MibTableColumn
hh3cEponUniLocalTechAbility = _Hh3cEponUniLocalTechAbility_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 8, 1, 1),
    _Hh3cEponUniLocalTechAbility_Type()
)
hh3cEponUniLocalTechAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniLocalTechAbility.setStatus("current")


class _Hh3cEponUniAdvertisedTechAbility_Type(OctetString):
    """Custom type hh3cEponUniAdvertisedTechAbility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponUniAdvertisedTechAbility_Type.__name__ = "OctetString"
_Hh3cEponUniAdvertisedTechAbility_Object = MibTableColumn
hh3cEponUniAdvertisedTechAbility = _Hh3cEponUniAdvertisedTechAbility_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 8, 1, 2),
    _Hh3cEponUniAdvertisedTechAbility_Type()
)
hh3cEponUniAdvertisedTechAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniAdvertisedTechAbility.setStatus("current")
_Hh3cEponUniMulticastControlTable_Object = MibTable
hh3cEponUniMulticastControlTable = _Hh3cEponUniMulticastControlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9)
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastControlTable.setStatus("current")
_Hh3cEponUniMulticastControlEntry_Object = MibTableRow
hh3cEponUniMulticastControlEntry = _Hh3cEponUniMulticastControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1)
)
hh3cEponUniMulticastControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniMulticastIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastControlEntry.setStatus("current")
_Hh3cEponUniMulticastVlanIndex_Type = Integer32
_Hh3cEponUniMulticastVlanIndex_Object = MibTableColumn
hh3cEponUniMulticastVlanIndex = _Hh3cEponUniMulticastVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 1),
    _Hh3cEponUniMulticastVlanIndex_Type()
)
hh3cEponUniMulticastVlanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastVlanIndex.setStatus("current")


class _Hh3cEponUniMulticastAddressList_Type(OctetString):
    """Custom type hh3cEponUniMulticastAddressList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponUniMulticastAddressList_Type.__name__ = "OctetString"
_Hh3cEponUniMulticastAddressList_Object = MibTableColumn
hh3cEponUniMulticastAddressList = _Hh3cEponUniMulticastAddressList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 2),
    _Hh3cEponUniMulticastAddressList_Type()
)
hh3cEponUniMulticastAddressList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastAddressList.setStatus("current")


class _Hh3cEponUniMulticastAccessRule_Type(Integer32):
    """Custom type hh3cEponUniMulticastAccessRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2),
          ("preview", 3))
    )


_Hh3cEponUniMulticastAccessRule_Type.__name__ = "Integer32"
_Hh3cEponUniMulticastAccessRule_Object = MibTableColumn
hh3cEponUniMulticastAccessRule = _Hh3cEponUniMulticastAccessRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 3),
    _Hh3cEponUniMulticastAccessRule_Type()
)
hh3cEponUniMulticastAccessRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastAccessRule.setStatus("current")
_Hh3cEponUniMulticastChannelLimit_Type = Integer32
_Hh3cEponUniMulticastChannelLimit_Object = MibTableColumn
hh3cEponUniMulticastChannelLimit = _Hh3cEponUniMulticastChannelLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 4),
    _Hh3cEponUniMulticastChannelLimit_Type()
)
hh3cEponUniMulticastChannelLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastChannelLimit.setStatus("current")
_Hh3cEponUniMulticastPreTimeSlice_Type = Integer32
_Hh3cEponUniMulticastPreTimeSlice_Object = MibTableColumn
hh3cEponUniMulticastPreTimeSlice = _Hh3cEponUniMulticastPreTimeSlice_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 5),
    _Hh3cEponUniMulticastPreTimeSlice_Type()
)
hh3cEponUniMulticastPreTimeSlice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastPreTimeSlice.setStatus("current")
_Hh3cEponUniMulticastPreTimes_Type = Integer32
_Hh3cEponUniMulticastPreTimes_Object = MibTableColumn
hh3cEponUniMulticastPreTimes = _Hh3cEponUniMulticastPreTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 6),
    _Hh3cEponUniMulticastPreTimes_Type()
)
hh3cEponUniMulticastPreTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastPreTimes.setStatus("current")
_Hh3cEponUniMulticastPreInterval_Type = Integer32
_Hh3cEponUniMulticastPreInterval_Object = MibTableColumn
hh3cEponUniMulticastPreInterval = _Hh3cEponUniMulticastPreInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 7),
    _Hh3cEponUniMulticastPreInterval_Type()
)
hh3cEponUniMulticastPreInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastPreInterval.setStatus("current")
_Hh3cEponUniMulticastRowStatus_Type = RowStatus
_Hh3cEponUniMulticastRowStatus_Object = MibTableColumn
hh3cEponUniMulticastRowStatus = _Hh3cEponUniMulticastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 8),
    _Hh3cEponUniMulticastRowStatus_Type()
)
hh3cEponUniMulticastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastRowStatus.setStatus("current")
_Hh3cEponUniMulticastIndex_Type = Integer32
_Hh3cEponUniMulticastIndex_Object = MibTableColumn
hh3cEponUniMulticastIndex = _Hh3cEponUniMulticastIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 9),
    _Hh3cEponUniMulticastIndex_Type()
)
hh3cEponUniMulticastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastIndex.setStatus("current")


class _Hh3cEponUniMulticastSourceIpList_Type(OctetString):
    """Custom type hh3cEponUniMulticastSourceIpList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponUniMulticastSourceIpList_Type.__name__ = "OctetString"
_Hh3cEponUniMulticastSourceIpList_Object = MibTableColumn
hh3cEponUniMulticastSourceIpList = _Hh3cEponUniMulticastSourceIpList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 10),
    _Hh3cEponUniMulticastSourceIpList_Type()
)
hh3cEponUniMulticastSourceIpList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastSourceIpList.setStatus("current")
_Hh3cEponUniMulticastResetInterval_Type = Integer32
_Hh3cEponUniMulticastResetInterval_Object = MibTableColumn
hh3cEponUniMulticastResetInterval = _Hh3cEponUniMulticastResetInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 11),
    _Hh3cEponUniMulticastResetInterval_Type()
)
hh3cEponUniMulticastResetInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastResetInterval.setStatus("current")
_Hh3cEponUniQosIndexNextTable_Object = MibTable
hh3cEponUniQosIndexNextTable = _Hh3cEponUniQosIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 10)
)
if mibBuilder.loadTexts:
    hh3cEponUniQosIndexNextTable.setStatus("current")
_Hh3cEponUniQosIndexNextEntry_Object = MibTableRow
hh3cEponUniQosIndexNextEntry = _Hh3cEponUniQosIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 10, 1)
)
hh3cEponUniQosIndexNextEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniQosIndexNextEntry.setStatus("current")
_Hh3cEponUniQosConfIndexNext_Type = Integer32
_Hh3cEponUniQosConfIndexNext_Object = MibTableColumn
hh3cEponUniQosConfIndexNext = _Hh3cEponUniQosConfIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 10, 1, 1),
    _Hh3cEponUniQosConfIndexNext_Type()
)
hh3cEponUniQosConfIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniQosConfIndexNext.setStatus("current")
_Hh3cEponUniQosConfTable_Object = MibTable
hh3cEponUniQosConfTable = _Hh3cEponUniQosConfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 11)
)
if mibBuilder.loadTexts:
    hh3cEponUniQosConfTable.setStatus("current")
_Hh3cEponUniQosConfEntry_Object = MibTableRow
hh3cEponUniQosConfEntry = _Hh3cEponUniQosConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 11, 1)
)
hh3cEponUniQosConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniQosConfIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniQosConfEntry.setStatus("current")
_Hh3cEponUniQosConfIndex_Type = Integer32
_Hh3cEponUniQosConfIndex_Object = MibTableColumn
hh3cEponUniQosConfIndex = _Hh3cEponUniQosConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 11, 1, 1),
    _Hh3cEponUniQosConfIndex_Type()
)
hh3cEponUniQosConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponUniQosConfIndex.setStatus("current")
_Hh3cEponUniQosConfRuleIndexNext_Type = Integer32
_Hh3cEponUniQosConfRuleIndexNext_Object = MibTableColumn
hh3cEponUniQosConfRuleIndexNext = _Hh3cEponUniQosConfRuleIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 11, 1, 2),
    _Hh3cEponUniQosConfRuleIndexNext_Type()
)
hh3cEponUniQosConfRuleIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniQosConfRuleIndexNext.setStatus("current")
_Hh3cEponUniQosConfMappedQueue_Type = Integer32
_Hh3cEponUniQosConfMappedQueue_Object = MibTableColumn
hh3cEponUniQosConfMappedQueue = _Hh3cEponUniQosConfMappedQueue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 11, 1, 3),
    _Hh3cEponUniQosConfMappedQueue_Type()
)
hh3cEponUniQosConfMappedQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosConfMappedQueue.setStatus("current")
_Hh3cEponUniQosConfMarkedPriority_Type = Integer32
_Hh3cEponUniQosConfMarkedPriority_Object = MibTableColumn
hh3cEponUniQosConfMarkedPriority = _Hh3cEponUniQosConfMarkedPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 11, 1, 4),
    _Hh3cEponUniQosConfMarkedPriority_Type()
)
hh3cEponUniQosConfMarkedPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosConfMarkedPriority.setStatus("current")
_Hh3cEponUniQosConfRowStatus_Type = RowStatus
_Hh3cEponUniQosConfRowStatus_Object = MibTableColumn
hh3cEponUniQosConfRowStatus = _Hh3cEponUniQosConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 11, 1, 5),
    _Hh3cEponUniQosConfRowStatus_Type()
)
hh3cEponUniQosConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosConfRowStatus.setStatus("current")
_Hh3cEponUniQosRuleTable_Object = MibTable
hh3cEponUniQosRuleTable = _Hh3cEponUniQosRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12)
)
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleTable.setStatus("current")
_Hh3cEponUniQosRuleEntry_Object = MibTableRow
hh3cEponUniQosRuleEntry = _Hh3cEponUniQosRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12, 1)
)
hh3cEponUniQosRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniQosConfIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniQosRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleEntry.setStatus("current")


class _Hh3cEponUniQosRuleIndex_Type(Integer32):
    """Custom type hh3cEponUniQosRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cEponUniQosRuleIndex_Type.__name__ = "Integer32"
_Hh3cEponUniQosRuleIndex_Object = MibTableColumn
hh3cEponUniQosRuleIndex = _Hh3cEponUniQosRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12, 1, 1),
    _Hh3cEponUniQosRuleIndex_Type()
)
hh3cEponUniQosRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleIndex.setStatus("current")


class _Hh3cEponUniQosRuleSelector_Type(Integer32):
    """Custom type hh3cEponUniQosRuleSelector based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dstmac", 1),
          ("srcmac", 2),
          ("ethernetpriority", 3),
          ("vlanid", 4),
          ("ethernettype", 5),
          ("dstip", 6),
          ("srcip", 7),
          ("ipprototype", 8),
          ("ipv4tosdscp", 9),
          ("ipv6precedence", 10),
          ("srcport", 11),
          ("dstport", 12))
    )


_Hh3cEponUniQosRuleSelector_Type.__name__ = "Integer32"
_Hh3cEponUniQosRuleSelector_Object = MibTableColumn
hh3cEponUniQosRuleSelector = _Hh3cEponUniQosRuleSelector_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12, 1, 2),
    _Hh3cEponUniQosRuleSelector_Type()
)
hh3cEponUniQosRuleSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleSelector.setStatus("current")
_Hh3cEponUniQosRuleValue_Type = Integer32
_Hh3cEponUniQosRuleValue_Object = MibTableColumn
hh3cEponUniQosRuleValue = _Hh3cEponUniQosRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12, 1, 3),
    _Hh3cEponUniQosRuleValue_Type()
)
hh3cEponUniQosRuleValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleValue.setStatus("current")
_Hh3cEponUniQosRuleMacAddress_Type = MacAddress
_Hh3cEponUniQosRuleMacAddress_Object = MibTableColumn
hh3cEponUniQosRuleMacAddress = _Hh3cEponUniQosRuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12, 1, 4),
    _Hh3cEponUniQosRuleMacAddress_Type()
)
hh3cEponUniQosRuleMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleMacAddress.setStatus("current")


class _Hh3cEponUniQosRuleOperator_Type(Integer32):
    """Custom type hh3cEponUniQosRuleOperator based on Integer32"""
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
        *(("nevermatch", 1),
          ("equal", 2),
          ("notequal", 3),
          ("lessthanequal", 4),
          ("greaterthanequal", 5),
          ("fieldexist", 6),
          ("fieldnotexist", 7),
          ("alwaysmatch", 8))
    )


_Hh3cEponUniQosRuleOperator_Type.__name__ = "Integer32"
_Hh3cEponUniQosRuleOperator_Object = MibTableColumn
hh3cEponUniQosRuleOperator = _Hh3cEponUniQosRuleOperator_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12, 1, 5),
    _Hh3cEponUniQosRuleOperator_Type()
)
hh3cEponUniQosRuleOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleOperator.setStatus("current")
_Hh3cEponUniQosRuleRowStatus_Type = RowStatus
_Hh3cEponUniQosRuleRowStatus_Object = MibTableColumn
hh3cEponUniQosRuleRowStatus = _Hh3cEponUniQosRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12, 1, 6),
    _Hh3cEponUniQosRuleRowStatus_Type()
)
hh3cEponUniQosRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleRowStatus.setStatus("current")
_Hh3cEponUniMirrorGroupTable_Object = MibTable
hh3cEponUniMirrorGroupTable = _Hh3cEponUniMirrorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 13)
)
if mibBuilder.loadTexts:
    hh3cEponUniMirrorGroupTable.setStatus("current")
_Hh3cEponUniMirrorGroupEntry_Object = MibTableRow
hh3cEponUniMirrorGroupEntry = _Hh3cEponUniMirrorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 13, 1)
)
hh3cEponUniMirrorGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniMirrorGroupID"),
)
if mibBuilder.loadTexts:
    hh3cEponUniMirrorGroupEntry.setStatus("current")
_Hh3cEponUniMirrorGroupID_Type = Integer32
_Hh3cEponUniMirrorGroupID_Object = MibTableColumn
hh3cEponUniMirrorGroupID = _Hh3cEponUniMirrorGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 13, 1, 1),
    _Hh3cEponUniMirrorGroupID_Type()
)
hh3cEponUniMirrorGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponUniMirrorGroupID.setStatus("current")
_Hh3cEponUniMirrorInboundPortList_Type = OctetString
_Hh3cEponUniMirrorInboundPortList_Object = MibTableColumn
hh3cEponUniMirrorInboundPortList = _Hh3cEponUniMirrorInboundPortList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 13, 1, 2),
    _Hh3cEponUniMirrorInboundPortList_Type()
)
hh3cEponUniMirrorInboundPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniMirrorInboundPortList.setStatus("current")
_Hh3cEponUniMirrorOutboundPortList_Type = OctetString
_Hh3cEponUniMirrorOutboundPortList_Object = MibTableColumn
hh3cEponUniMirrorOutboundPortList = _Hh3cEponUniMirrorOutboundPortList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 13, 1, 3),
    _Hh3cEponUniMirrorOutboundPortList_Type()
)
hh3cEponUniMirrorOutboundPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMirrorOutboundPortList.setStatus("current")
_Hh3cEponUniMonitorPort_Type = Integer32
_Hh3cEponUniMonitorPort_Object = MibTableColumn
hh3cEponUniMonitorPort = _Hh3cEponUniMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 13, 1, 4),
    _Hh3cEponUniMonitorPort_Type()
)
hh3cEponUniMonitorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMonitorPort.setStatus("current")
_Hh3cEponUniMirrorRowStatus_Type = RowStatus
_Hh3cEponUniMirrorRowStatus_Object = MibTableColumn
hh3cEponUniMirrorRowStatus = _Hh3cEponUniMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 13, 1, 5),
    _Hh3cEponUniMirrorRowStatus_Type()
)
hh3cEponUniMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMirrorRowStatus.setStatus("current")
_Hh3cEponUniMirrorGroupIdNextTable_Object = MibTable
hh3cEponUniMirrorGroupIdNextTable = _Hh3cEponUniMirrorGroupIdNextTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 14)
)
if mibBuilder.loadTexts:
    hh3cEponUniMirrorGroupIdNextTable.setStatus("current")
_Hh3cEponUniMirrorGroupIdNextEntry_Object = MibTableRow
hh3cEponUniMirrorGroupIdNextEntry = _Hh3cEponUniMirrorGroupIdNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 14, 1)
)
hh3cEponUniMirrorGroupIdNextEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniMirrorGroupIdNextEntry.setStatus("current")
_Hh3cEponUniMirrorGroupIDNext_Type = Integer32
_Hh3cEponUniMirrorGroupIDNext_Object = MibTableColumn
hh3cEponUniMirrorGroupIDNext = _Hh3cEponUniMirrorGroupIDNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 14, 1, 1),
    _Hh3cEponUniMirrorGroupIDNext_Type()
)
hh3cEponUniMirrorGroupIDNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniMirrorGroupIDNext.setStatus("current")
_Hh3cEponUniMulticastCtrlInfoTable_Object = MibTable
hh3cEponUniMulticastCtrlInfoTable = _Hh3cEponUniMulticastCtrlInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 15)
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastCtrlInfoTable.setStatus("current")
_Hh3cEponUniMulticastCtrlInfoEntry_Object = MibTableRow
hh3cEponUniMulticastCtrlInfoEntry = _Hh3cEponUniMulticastCtrlInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 15, 1)
)
hh3cEponUniMulticastCtrlInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniMultActVlan"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniMultActAddress"),
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastCtrlInfoEntry.setStatus("current")
_Hh3cEponUniMultActVlan_Type = Integer32
_Hh3cEponUniMultActVlan_Object = MibTableColumn
hh3cEponUniMultActVlan = _Hh3cEponUniMultActVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 15, 1, 1),
    _Hh3cEponUniMultActVlan_Type()
)
hh3cEponUniMultActVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponUniMultActVlan.setStatus("current")
_Hh3cEponUniMultActAddress_Type = IpAddress
_Hh3cEponUniMultActAddress_Object = MibTableColumn
hh3cEponUniMultActAddress = _Hh3cEponUniMultActAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 15, 1, 2),
    _Hh3cEponUniMultActAddress_Type()
)
hh3cEponUniMultActAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponUniMultActAddress.setStatus("current")


class _Hh3cEponUniMultActAccessRule_Type(Integer32):
    """Custom type hh3cEponUniMultActAccessRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2),
          ("preview", 3))
    )


_Hh3cEponUniMultActAccessRule_Type.__name__ = "Integer32"
_Hh3cEponUniMultActAccessRule_Object = MibTableColumn
hh3cEponUniMultActAccessRule = _Hh3cEponUniMultActAccessRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 15, 1, 3),
    _Hh3cEponUniMultActAccessRule_Type()
)
hh3cEponUniMultActAccessRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniMultActAccessRule.setStatus("current")
_Hh3cEponUniMultActPreTimes_Type = Integer32
_Hh3cEponUniMultActPreTimes_Object = MibTableColumn
hh3cEponUniMultActPreTimes = _Hh3cEponUniMultActPreTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 15, 1, 4),
    _Hh3cEponUniMultActPreTimes_Type()
)
hh3cEponUniMultActPreTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniMultActPreTimes.setStatus("current")
_Hh3cEponUniMultActPreRemain_Type = Integer32
_Hh3cEponUniMultActPreRemain_Object = MibTableColumn
hh3cEponUniMultActPreRemain = _Hh3cEponUniMultActPreRemain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 15, 1, 5),
    _Hh3cEponUniMultActPreRemain_Type()
)
hh3cEponUniMultActPreRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniMultActPreRemain.setStatus("current")
_Hh3cEponUniMulticastIndexNextTable_Object = MibTable
hh3cEponUniMulticastIndexNextTable = _Hh3cEponUniMulticastIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 16)
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastIndexNextTable.setStatus("current")
_Hh3cEponUniMulticastIndexNextEntry_Object = MibTableRow
hh3cEponUniMulticastIndexNextEntry = _Hh3cEponUniMulticastIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 16, 1)
)
hh3cEponUniMulticastIndexNextEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastIndexNextEntry.setStatus("current")
_Hh3cEponUniMulticastConfIndexNext_Type = Integer32
_Hh3cEponUniMulticastConfIndexNext_Object = MibTableColumn
hh3cEponUniMulticastConfIndexNext = _Hh3cEponUniMulticastConfIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 16, 1, 1),
    _Hh3cEponUniMulticastConfIndexNext_Type()
)
hh3cEponUniMulticastConfIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastConfIndexNext.setStatus("current")
_Hh3cEponCTCAlarmTable_Object = MibTable
hh3cEponCTCAlarmTable = _Hh3cEponCTCAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 17)
)
if mibBuilder.loadTexts:
    hh3cEponCTCAlarmTable.setStatus("current")
_Hh3cEponCTCAlarmEntry_Object = MibTableRow
hh3cEponCTCAlarmEntry = _Hh3cEponCTCAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 17, 1)
)
hh3cEponCTCAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponCTCAlarmID"),
)
if mibBuilder.loadTexts:
    hh3cEponCTCAlarmEntry.setStatus("current")


class _Hh3cEponCTCAlarmID_Type(Integer32):
    """Custom type hh3cEponCTCAlarmID based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              769,
              770,
              771,
              772,
              773,
              774,
              775,
              776,
              777,
              778,
              779,
              780,
              781,
              782,
              783,
              784,
              785,
              786,
              787,
              788,
              789,
              790,
              791,
              792,
              793,
              794,
              795,
              796,
              797,
              798,
              799,
              800,
              801,
              802,
              803,
              804,
              805,
              806,
              807,
              1025,
              1281,
              1282,
              1283)
        )
    )
    namedValues = NamedValues(
        *(("onuEquipmentAlarm", 1),
          ("onuPowerAlarm", 2),
          ("onuBatteryMissing", 3),
          ("onuBatteryFailure", 4),
          ("onuBatteryVoltLow", 5),
          ("onuPhysicalIntrusionAlarm", 6),
          ("onuONUSelfTestFailure", 7),
          ("onuONUTempHighAlarm", 9),
          ("onuONUTempLowAlarm", 10),
          ("onuIADConnectionFailure", 11),
          ("onuPonIFSwitch", 12),
          ("onuSleepStatusUpdate", 13),
          ("ponRXPowerHighAlarm", 257),
          ("ponRXPowerLowAlarm", 258),
          ("ponTXPowerHighAlarm", 259),
          ("ponTXPowerLowAlarm", 260),
          ("ponTXBiasHighAlarm", 261),
          ("ponTXBiasLowAlarm", 262),
          ("ponVccHighAlarm", 263),
          ("ponVccLowAlarm", 264),
          ("ponTempHighAlarm", 265),
          ("ponTempLowAlarm", 266),
          ("ponRXPowerHighWarning", 267),
          ("ponRXPowerLowWarning", 268),
          ("ponTXPowerHighWarning", 269),
          ("ponTXPowerLowWarning", 270),
          ("ponTXBiasHighWarning", 271),
          ("ponTXBiasLowWarning", 272),
          ("ponVccHighWarning", 273),
          ("ponVccLowWarning", 274),
          ("ponTempHighWarning", 275),
          ("ponTempLowWarning", 276),
          ("ponDownstreamDropEventsAlarm", 277),
          ("ponUpstreamDropEventsAlarm", 278),
          ("ponDownstreamCRCErrorFramesAlarm", 279),
          ("ponUpstreamCRCErrorFramesAlarm", 280),
          ("ponDownstreamUndersizeFramesAlarm", 281),
          ("ponUpstreamUndersizeFramesAlarm", 282),
          ("ponDownstreamOversizeFramesAlarm", 283),
          ("ponUpstreamOversizeFramesAlarm", 284),
          ("ponDownstreamFragmentsAlarm", 285),
          ("ponUpstreamFragmentsAlarm", 286),
          ("ponDownstreamJabbersAlarm", 287),
          ("ponUpstreamJabbersAlarm", 288),
          ("ponDownstreamDiscardsAlarm", 289),
          ("ponUpstreamDiscardsAlarm", 290),
          ("ponDownstreamErrorsAlarm", 291),
          ("ponUpstreamErrorsAlarm", 292),
          ("ponDownstreamDropEventsWarning", 293),
          ("ponUpstreamDropEventsWarning", 294),
          ("ponDownstreamCRCErrorFramesWarning", 295),
          ("ponUpstreamCRCErrorFramesWarning", 296),
          ("ponDownstreamUndersizeFramesWarning", 297),
          ("ponUpstreamUndersizeFramesWarning", 298),
          ("ponDownstreamOversizeFramesWarning", 299),
          ("ponUpstreamOversizeFramesWarning", 300),
          ("ponDownstreamFragmentsWarning", 301),
          ("ponUpstreamFragmentsWarning", 302),
          ("ponDownstreamJabbersWarning", 303),
          ("ponUpstreamJabbersWarning", 304),
          ("ponDownstreamDiscardsWarning", 305),
          ("ponUpstreamDiscardsWarning", 306),
          ("ponDownstreamErrorsWarning", 307),
          ("ponUpstreamErrorsWarning", 308),
          ("uniEthPortAutoNegFailure", 769),
          ("uniEthPortLOS", 770),
          ("uniEthPortFailure", 771),
          ("uniEthPortLoopback", 772),
          ("uniEthPortCongestion", 773),
          ("uniDownstreamDropEventsAlarm", 774),
          ("uniUpstreamDropEventsAlarm", 775),
          ("uniDownstreamCRCErrorFramesAlarm", 776),
          ("uniUpstreamCRCErrorFramesAlarm", 777),
          ("uniDownstreamUndersizeFramesAlarm", 778),
          ("uniUpstreamUndersizeFramesAlarm", 779),
          ("uniDownstreamOversizeFramesAlarm", 780),
          ("uniUpstreamOversizeFramesAlarm", 781),
          ("uniDownstreamFragmentsAlarm", 782),
          ("uniUpstreamFragmentsAlarm", 783),
          ("uniDownstreamJabbersAlarm", 784),
          ("uniUpstreamJabbersAlarm", 785),
          ("uniDownstreamDiscardsAlarm", 786),
          ("uniUpstreamDiscardsAlarm", 787),
          ("uniDownstreamErrorsAlarm", 788),
          ("uniUpstreamErrorsAlarm", 789),
          ("uniStatusChangeTimesAlarm", 790),
          ("uniDownstreamDropEventsWarning", 791),
          ("uniUpstreamDropEventsWarning", 792),
          ("uniDownstreamCRCErrorFramesWarning", 793),
          ("uniUpstreamCRCErrorFramesWarning", 794),
          ("uniDownstreamUndersizeFramesWarning", 795),
          ("uniUpstreamUndersizeFramesWarning", 796),
          ("uniDownstreamOversizeFramesWarning", 797),
          ("uniUpstreamOversizeFramesWarning", 798),
          ("uniDownstreamFragmentsWarning", 799),
          ("uniUpstreamFragmentsWarning", 800),
          ("uniDownstreamJabbersWarning", 801),
          ("uniUpstreamJabbersWarning", 802),
          ("uniDownstreamDiscardsWarning", 803),
          ("uniUpstreamDiscardsWarning", 804),
          ("uniDownstreamErrorsWarning", 805),
          ("uniUpstreamErrorsWarning", 806),
          ("uniStatusChangeTimesWarning", 807),
          ("uniPOTSPortFailure", 1025),
          ("uniE1PortFailure", 1281),
          ("uniE1TimingUnlock", 1282),
          ("uniE1LOS", 1283))
    )


_Hh3cEponCTCAlarmID_Type.__name__ = "Integer32"
_Hh3cEponCTCAlarmID_Object = MibTableColumn
hh3cEponCTCAlarmID = _Hh3cEponCTCAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 17, 1, 1),
    _Hh3cEponCTCAlarmID_Type()
)
hh3cEponCTCAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponCTCAlarmID.setStatus("current")


class _Hh3cEponCTCAlarmProtocol_Type(Integer32):
    """Custom type hh3cEponCTCAlarmProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              33,
              48)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("ctc21", 33),
          ("ctc30", 48))
    )


_Hh3cEponCTCAlarmProtocol_Type.__name__ = "Integer32"
_Hh3cEponCTCAlarmProtocol_Object = MibTableColumn
hh3cEponCTCAlarmProtocol = _Hh3cEponCTCAlarmProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 17, 1, 2),
    _Hh3cEponCTCAlarmProtocol_Type()
)
hh3cEponCTCAlarmProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponCTCAlarmProtocol.setStatus("current")
_Hh3cEponCTCAlarmEnable_Type = TruthValue
_Hh3cEponCTCAlarmEnable_Object = MibTableColumn
hh3cEponCTCAlarmEnable = _Hh3cEponCTCAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 17, 1, 3),
    _Hh3cEponCTCAlarmEnable_Type()
)
hh3cEponCTCAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponCTCAlarmEnable.setStatus("current")
_Hh3cEponCTCAlarmTriggerThresVal_Type = OctetString
_Hh3cEponCTCAlarmTriggerThresVal_Object = MibTableColumn
hh3cEponCTCAlarmTriggerThresVal = _Hh3cEponCTCAlarmTriggerThresVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 17, 1, 4),
    _Hh3cEponCTCAlarmTriggerThresVal_Type()
)
hh3cEponCTCAlarmTriggerThresVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponCTCAlarmTriggerThresVal.setStatus("current")
_Hh3cEponCTCAlarmClearThresVal_Type = OctetString
_Hh3cEponCTCAlarmClearThresVal_Object = MibTableColumn
hh3cEponCTCAlarmClearThresVal = _Hh3cEponCTCAlarmClearThresVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 17, 1, 5),
    _Hh3cEponCTCAlarmClearThresVal_Type()
)
hh3cEponCTCAlarmClearThresVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponCTCAlarmClearThresVal.setStatus("current")
_Hh3cEponUniErrorInfo_ObjectIdentity = ObjectIdentity
hh3cEponUniErrorInfo = _Hh3cEponUniErrorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 18)
)
_Hh3cEponCTCAlarmInfo_Type = OctetString
_Hh3cEponCTCAlarmInfo_Object = MibScalar
hh3cEponCTCAlarmInfo = _Hh3cEponCTCAlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 18, 1),
    _Hh3cEponCTCAlarmInfo_Type()
)
hh3cEponCTCAlarmInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEponCTCAlarmInfo.setStatus("current")
_Hh3cUniStatisticsTable_Object = MibTable
hh3cUniStatisticsTable = _Hh3cUniStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 19)
)
if mibBuilder.loadTexts:
    hh3cUniStatisticsTable.setStatus("current")
_Hh3cUniStatisticsEntry_Object = MibTableRow
hh3cUniStatisticsEntry = _Hh3cUniStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 19, 1)
)
hh3cUniStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cUniStatisticsEntry.setStatus("current")
_Hh3cUniStatisticsPeriodVal_Type = Unsigned32
_Hh3cUniStatisticsPeriodVal_Object = MibTableColumn
hh3cUniStatisticsPeriodVal = _Hh3cUniStatisticsPeriodVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 19, 1, 1),
    _Hh3cUniStatisticsPeriodVal_Type()
)
hh3cUniStatisticsPeriodVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUniStatisticsPeriodVal.setStatus("current")
_Hh3cUniStatisticsEnable_Type = TruthValue
_Hh3cUniStatisticsEnable_Object = MibTableColumn
hh3cUniStatisticsEnable = _Hh3cUniStatisticsEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 19, 1, 2),
    _Hh3cUniStatisticsEnable_Type()
)
hh3cUniStatisticsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUniStatisticsEnable.setStatus("current")
_Hh3cUniPoeTable_Object = MibTable
hh3cUniPoeTable = _Hh3cUniPoeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 20)
)
if mibBuilder.loadTexts:
    hh3cUniPoeTable.setStatus("current")
_Hh3cUniPoeEntry_Object = MibTableRow
hh3cUniPoeEntry = _Hh3cUniPoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 20, 1)
)
hh3cUniPoeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cUniPoeEntry.setStatus("current")


class _Hh3cUniPoeEnable_Type(TruthValue):
    """Custom type hh3cUniPoeEnable based on TruthValue"""
    defaultValue = 2


_Hh3cUniPoeEnable_Type.__name__ = "TruthValue"
_Hh3cUniPoeEnable_Object = MibTableColumn
hh3cUniPoeEnable = _Hh3cUniPoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 20, 1, 1),
    _Hh3cUniPoeEnable_Type()
)
hh3cUniPoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUniPoeEnable.setStatus("current")


class _Hh3cUniPoeMode_Type(Integer32):
    """Custom type hh3cUniPoeMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("signal", 0),
          ("spare", 1))
    )


_Hh3cUniPoeMode_Type.__name__ = "Integer32"
_Hh3cUniPoeMode_Object = MibTableColumn
hh3cUniPoeMode = _Hh3cUniPoeMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 20, 1, 2),
    _Hh3cUniPoeMode_Type()
)
hh3cUniPoeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUniPoeMode.setStatus("current")


class _Hh3cUniPoePriority_Type(Integer32):
    """Custom type hh3cUniPoePriority based on Integer32"""
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
        *(("high", 0),
          ("critical", 1),
          ("low", 2))
    )


_Hh3cUniPoePriority_Type.__name__ = "Integer32"
_Hh3cUniPoePriority_Object = MibTableColumn
hh3cUniPoePriority = _Hh3cUniPoePriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 20, 1, 3),
    _Hh3cUniPoePriority_Type()
)
hh3cUniPoePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUniPoePriority.setStatus("current")


class _Hh3cUniPoeMaxPowerClass_Type(Integer32):
    """Custom type hh3cUniPoeMaxPowerClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("undefined", 255))
    )


_Hh3cUniPoeMaxPowerClass_Type.__name__ = "Integer32"
_Hh3cUniPoeMaxPowerClass_Object = MibTableColumn
hh3cUniPoeMaxPowerClass = _Hh3cUniPoeMaxPowerClass_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 20, 1, 4),
    _Hh3cUniPoeMaxPowerClass_Type()
)
hh3cUniPoeMaxPowerClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUniPoeMaxPowerClass.setStatus("current")


class _Hh3cUniPoeMaxPowerValue_Type(Integer32):
    """Custom type hh3cUniPoeMaxPowerValue based on Integer32"""
    defaultValue = 0


_Hh3cUniPoeMaxPowerValue_Type.__name__ = "Integer32"
_Hh3cUniPoeMaxPowerValue_Object = MibTableColumn
hh3cUniPoeMaxPowerValue = _Hh3cUniPoeMaxPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 20, 1, 5),
    _Hh3cUniPoeMaxPowerValue_Type()
)
hh3cUniPoeMaxPowerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUniPoeMaxPowerValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cUniPoeMaxPowerValue.setUnits("mW")
_Hh3cUniPoeLegacyEnable_Type = TruthValue
_Hh3cUniPoeLegacyEnable_Object = MibTableColumn
hh3cUniPoeLegacyEnable = _Hh3cUniPoeLegacyEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 20, 1, 6),
    _Hh3cUniPoeLegacyEnable_Type()
)
hh3cUniPoeLegacyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUniPoeLegacyEnable.setStatus("current")
_Hh3cUniPoeInfoTable_Object = MibTable
hh3cUniPoeInfoTable = _Hh3cUniPoeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21)
)
if mibBuilder.loadTexts:
    hh3cUniPoeInfoTable.setStatus("current")
_Hh3cUniPoeInfoEntry_Object = MibTableRow
hh3cUniPoeInfoEntry = _Hh3cUniPoeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1)
)
hh3cUniPoeInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cUniPoeInfoEntry.setStatus("current")


class _Hh3cUniPoeInfoCapability_Type(Integer32):
    """Custom type hh3cUniPoeInfoCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("incapable", 0),
          ("capable", 1))
    )


_Hh3cUniPoeInfoCapability_Type.__name__ = "Integer32"
_Hh3cUniPoeInfoCapability_Object = MibTableColumn
hh3cUniPoeInfoCapability = _Hh3cUniPoeInfoCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 1),
    _Hh3cUniPoeInfoCapability_Type()
)
hh3cUniPoeInfoCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoCapability.setStatus("current")
_Hh3cUniPoeInfoEnable_Type = TruthValue
_Hh3cUniPoeInfoEnable_Object = MibTableColumn
hh3cUniPoeInfoEnable = _Hh3cUniPoeInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 2),
    _Hh3cUniPoeInfoEnable_Type()
)
hh3cUniPoeInfoEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoEnable.setStatus("current")
_Hh3cUniPoeInfoLegacyEnable_Type = TruthValue
_Hh3cUniPoeInfoLegacyEnable_Object = MibTableColumn
hh3cUniPoeInfoLegacyEnable = _Hh3cUniPoeInfoLegacyEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 3),
    _Hh3cUniPoeInfoLegacyEnable_Type()
)
hh3cUniPoeInfoLegacyEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoLegacyEnable.setStatus("current")


class _Hh3cUniPoeInfoMode_Type(Integer32):
    """Custom type hh3cUniPoeInfoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("signal", 0),
          ("spare", 1))
    )


_Hh3cUniPoeInfoMode_Type.__name__ = "Integer32"
_Hh3cUniPoeInfoMode_Object = MibTableColumn
hh3cUniPoeInfoMode = _Hh3cUniPoeInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 4),
    _Hh3cUniPoeInfoMode_Type()
)
hh3cUniPoeInfoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoMode.setStatus("current")


class _Hh3cUniPoeInfoPriority_Type(Integer32):
    """Custom type hh3cUniPoeInfoPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("critical", 1),
          ("low", 2))
    )


_Hh3cUniPoeInfoPriority_Type.__name__ = "Integer32"
_Hh3cUniPoeInfoPriority_Object = MibTableColumn
hh3cUniPoeInfoPriority = _Hh3cUniPoeInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 5),
    _Hh3cUniPoeInfoPriority_Type()
)
hh3cUniPoeInfoPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoPriority.setStatus("current")


class _Hh3cUniPoeInfoMaxPwrClass_Type(Integer32):
    """Custom type hh3cUniPoeInfoMaxPwrClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("undefined", 255))
    )


_Hh3cUniPoeInfoMaxPwrClass_Type.__name__ = "Integer32"
_Hh3cUniPoeInfoMaxPwrClass_Object = MibTableColumn
hh3cUniPoeInfoMaxPwrClass = _Hh3cUniPoeInfoMaxPwrClass_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 6),
    _Hh3cUniPoeInfoMaxPwrClass_Type()
)
hh3cUniPoeInfoMaxPwrClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoMaxPwrClass.setStatus("current")
_Hh3cUniPoeInfoMaxPwrValue_Type = Integer32
_Hh3cUniPoeInfoMaxPwrValue_Object = MibTableColumn
hh3cUniPoeInfoMaxPwrValue = _Hh3cUniPoeInfoMaxPwrValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 7),
    _Hh3cUniPoeInfoMaxPwrValue_Type()
)
hh3cUniPoeInfoMaxPwrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoMaxPwrValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoMaxPwrValue.setUnits("mW")


class _Hh3cUniPoeInfoPdClass_Type(Integer32):
    """Custom type hh3cUniPoeInfoPdClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("undefined", 255))
    )


_Hh3cUniPoeInfoPdClass_Type.__name__ = "Integer32"
_Hh3cUniPoeInfoPdClass_Object = MibTableColumn
hh3cUniPoeInfoPdClass = _Hh3cUniPoeInfoPdClass_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 8),
    _Hh3cUniPoeInfoPdClass_Type()
)
hh3cUniPoeInfoPdClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoPdClass.setStatus("current")


class _Hh3cUniPoeInfoPwrSuppStat_Type(Integer32):
    """Custom type hh3cUniPoeInfoPwrSuppStat based on Integer32"""
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
        *(("noNeed", 0),
          ("searching", 1),
          ("power", 2),
          ("force", 3),
          ("forceFailed", 4),
          ("powerFailed", 5))
    )


_Hh3cUniPoeInfoPwrSuppStat_Type.__name__ = "Integer32"
_Hh3cUniPoeInfoPwrSuppStat_Object = MibTableColumn
hh3cUniPoeInfoPwrSuppStat = _Hh3cUniPoeInfoPwrSuppStat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 9),
    _Hh3cUniPoeInfoPwrSuppStat_Type()
)
hh3cUniPoeInfoPwrSuppStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoPwrSuppStat.setStatus("current")
_Hh3cUniPoeInfoSignalErrCnt_Type = Integer32
_Hh3cUniPoeInfoSignalErrCnt_Object = MibTableColumn
hh3cUniPoeInfoSignalErrCnt = _Hh3cUniPoeInfoSignalErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 10),
    _Hh3cUniPoeInfoSignalErrCnt_Type()
)
hh3cUniPoeInfoSignalErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoSignalErrCnt.setStatus("current")
_Hh3cUniPoeInfoPwrDeniedCnt_Type = Integer32
_Hh3cUniPoeInfoPwrDeniedCnt_Object = MibTableColumn
hh3cUniPoeInfoPwrDeniedCnt = _Hh3cUniPoeInfoPwrDeniedCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 11),
    _Hh3cUniPoeInfoPwrDeniedCnt_Type()
)
hh3cUniPoeInfoPwrDeniedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoPwrDeniedCnt.setStatus("current")
_Hh3cUniPoeInfoPwrOverCnt_Type = Integer32
_Hh3cUniPoeInfoPwrOverCnt_Object = MibTableColumn
hh3cUniPoeInfoPwrOverCnt = _Hh3cUniPoeInfoPwrOverCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 12),
    _Hh3cUniPoeInfoPwrOverCnt_Type()
)
hh3cUniPoeInfoPwrOverCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoPwrOverCnt.setStatus("current")
_Hh3cUniPoeInfoCurOverCnt_Type = Integer32
_Hh3cUniPoeInfoCurOverCnt_Object = MibTableColumn
hh3cUniPoeInfoCurOverCnt = _Hh3cUniPoeInfoCurOverCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 13),
    _Hh3cUniPoeInfoCurOverCnt_Type()
)
hh3cUniPoeInfoCurOverCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoCurOverCnt.setStatus("current")
_Hh3cUniPoeInfoPdUndetectCnt_Type = Integer32
_Hh3cUniPoeInfoPdUndetectCnt_Object = MibTableColumn
hh3cUniPoeInfoPdUndetectCnt = _Hh3cUniPoeInfoPdUndetectCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 14),
    _Hh3cUniPoeInfoPdUndetectCnt_Type()
)
hh3cUniPoeInfoPdUndetectCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoPdUndetectCnt.setStatus("current")
_Hh3cUniPoeInfoMaxPower_Type = Integer32
_Hh3cUniPoeInfoMaxPower_Object = MibTableColumn
hh3cUniPoeInfoMaxPower = _Hh3cUniPoeInfoMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 15),
    _Hh3cUniPoeInfoMaxPower_Type()
)
hh3cUniPoeInfoMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoMaxPower.setUnits("mW")
_Hh3cUniPoeInfoCurOutputPwr_Type = Integer32
_Hh3cUniPoeInfoCurOutputPwr_Object = MibTableColumn
hh3cUniPoeInfoCurOutputPwr = _Hh3cUniPoeInfoCurOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 16),
    _Hh3cUniPoeInfoCurOutputPwr_Type()
)
hh3cUniPoeInfoCurOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoCurOutputPwr.setStatus("current")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoCurOutputPwr.setUnits("mW")
_Hh3cUniPoeInfoAvgOutputPwr_Type = Integer32
_Hh3cUniPoeInfoAvgOutputPwr_Object = MibTableColumn
hh3cUniPoeInfoAvgOutputPwr = _Hh3cUniPoeInfoAvgOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 17),
    _Hh3cUniPoeInfoAvgOutputPwr_Type()
)
hh3cUniPoeInfoAvgOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoAvgOutputPwr.setStatus("current")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoAvgOutputPwr.setUnits("mW")
_Hh3cUniPoeInfoPeakOutputPwr_Type = Integer32
_Hh3cUniPoeInfoPeakOutputPwr_Object = MibTableColumn
hh3cUniPoeInfoPeakOutputPwr = _Hh3cUniPoeInfoPeakOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 21, 1, 18),
    _Hh3cUniPoeInfoPeakOutputPwr_Type()
)
hh3cUniPoeInfoPeakOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoPeakOutputPwr.setStatus("current")
if mibBuilder.loadTexts:
    hh3cUniPoeInfoPeakOutputPwr.setUnits("mW")
_Hh3cEponUniTrap_ObjectIdentity = ObjectIdentity
hh3cEponUniTrap = _Hh3cEponUniTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 2)
)
_Hh3cEponUniTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cEponUniTrapPrefix = _Hh3cEponUniTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cEponUniLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 2, 0, 1)
)
hh3cEponUniLinkUpTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniAdminStatus"))
)
if mibBuilder.loadTexts:
    hh3cEponUniLinkUpTrap.setStatus(
        "current"
    )

hh3cEponUniLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 2, 0, 2)
)
hh3cEponUniLinkDownTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniAdminStatus"))
)
if mibBuilder.loadTexts:
    hh3cEponUniLinkDownTrap.setStatus(
        "current"
    )

hh3cEponUniLoopBackDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 2, 0, 3)
)
hh3cEponUniLoopBackDetectedTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniVlan"))
)
if mibBuilder.loadTexts:
    hh3cEponUniLoopBackDetectedTrap.setStatus(
        "current"
    )

hh3cEponUniLoopBackRecoveredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 2, 0, 4)
)
hh3cEponUniLoopBackRecoveredTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniVlan"))
)
if mibBuilder.loadTexts:
    hh3cEponUniLoopBackRecoveredTrap.setStatus(
        "current"
    )

hh3cEponCTCAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 2, 0, 5)
)
hh3cEponCTCAlarmTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponCTCAlarmID"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponCTCAlarmInfo"))
)
if mibBuilder.loadTexts:
    hh3cEponCTCAlarmTrap.setStatus(
        "current"
    )

hh3cEponCTCAlarmRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 2, 0, 6)
)
hh3cEponCTCAlarmRecoverTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponCTCAlarmID"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponCTCAlarmInfo"))
)
if mibBuilder.loadTexts:
    hh3cEponCTCAlarmRecoverTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-EPON-UNI-MIB",
    **{"hh3cEponUni": hh3cEponUni,
       "hh3cEponUniSysMan": hh3cEponUniSysMan,
       "hh3cEponUniSysManTable": hh3cEponUniSysManTable,
       "hh3cEponUniSysManEntry": hh3cEponUniSysManEntry,
       "hh3cEponUniIndex": hh3cEponUniIndex,
       "hh3cEponUniDescr": hh3cEponUniDescr,
       "hh3cEponUniAdminStatus": hh3cEponUniAdminStatus,
       "hh3cEponUniMdi": hh3cEponUniMdi,
       "hh3cEponUniPriority": hh3cEponUniPriority,
       "hh3cEponUniVlanType": hh3cEponUniVlanType,
       "hh3cEponUniAccessVlan": hh3cEponUniAccessVlan,
       "hh3cEponUniTrunkPvid": hh3cEponUniTrunkPvid,
       "hh3cEponUniVLANTrunkAllowListLow": hh3cEponUniVLANTrunkAllowListLow,
       "hh3cEponUniVLANTrunkAllowListHigh": hh3cEponUniVLANTrunkAllowListHigh,
       "hh3cEponUniInboundLineRate": hh3cEponUniInboundLineRate,
       "hh3cEponUniOutboundLineRate": hh3cEponUniOutboundLineRate,
       "hh3cEponUniFlowControl": hh3cEponUniFlowControl,
       "hh3cEponUniSpeed": hh3cEponUniSpeed,
       "hh3cEponUniDuplex": hh3cEponUniDuplex,
       "hh3cEponUniVlanVPNStatus": hh3cEponUniVlanVPNStatus,
       "hh3cEponUniCountReset": hh3cEponUniCountReset,
       "hh3cEponUniPortIsolate": hh3cEponUniPortIsolate,
       "hh3cEponUniVlanConfiguration": hh3cEponUniVlanConfiguration,
       "hh3cEponUniAutoNegotiation": hh3cEponUniAutoNegotiation,
       "hh3cEponUniRestartAutoNeg": hh3cEponUniRestartAutoNeg,
       "hh3cEponUniLinkStatus": hh3cEponUniLinkStatus,
       "hh3cEponUniInterfaceType": hh3cEponUniInterfaceType,
       "hh3cEponUniVitualCableTest": hh3cEponUniVitualCableTest,
       "hh3cEponUniVCTCableStatus": hh3cEponUniVCTCableStatus,
       "hh3cEponUniVCTCableLength": hh3cEponUniVCTCableLength,
       "hh3cEponUniVCTImpedanceMismatch": hh3cEponUniVCTImpedanceMismatch,
       "hh3cEponUniVCTPairSkew": hh3cEponUniVCTPairSkew,
       "hh3cEponUniVCTPairSwap": hh3cEponUniVCTPairSwap,
       "hh3cEponUniVCTPolaritySwap": hh3cEponUniVCTPolaritySwap,
       "hh3cEponUniVCTInsertionLoss": hh3cEponUniVCTInsertionLoss,
       "hh3cEponUniVCTReturnLoss": hh3cEponUniVCTReturnLoss,
       "hh3cEponUniVCTNearendCrosstalk": hh3cEponUniVCTNearendCrosstalk,
       "hh3cEponUniVlan": hh3cEponUniVlan,
       "hh3cEponUniMacMax": hh3cEponUniMacMax,
       "hh3cEponUniCountTable": hh3cEponUniCountTable,
       "hh3cEponUniCountEntry": hh3cEponUniCountEntry,
       "hh3cEponUniInStatsPkts": hh3cEponUniInStatsPkts,
       "hh3cEponUniInStatsUnicastPkts": hh3cEponUniInStatsUnicastPkts,
       "hh3cEponUniInStatsBroadcastPkts": hh3cEponUniInStatsBroadcastPkts,
       "hh3cEponUniInStatsMulticastPkts": hh3cEponUniInStatsMulticastPkts,
       "hh3cEponUniInPausePkts": hh3cEponUniInPausePkts,
       "hh3cEponUniInTotalErrors": hh3cEponUniInTotalErrors,
       "hh3cEponUniInStatsCRCAlignErrors": hh3cEponUniInStatsCRCAlignErrors,
       "hh3cEponUniInStatsUndersizePkts": hh3cEponUniInStatsUndersizePkts,
       "hh3cEponUniInStatsOversizePkts": hh3cEponUniInStatsOversizePkts,
       "hh3cEponUniInErrorbyOther": hh3cEponUniInErrorbyOther,
       "hh3cEponUniOutStatsPkts": hh3cEponUniOutStatsPkts,
       "hh3cEponUniOutStatsUnicastPkts": hh3cEponUniOutStatsUnicastPkts,
       "hh3cEponUniOutStatsBroadcastPkts": hh3cEponUniOutStatsBroadcastPkts,
       "hh3cEponUniOutStatsMulticastPkts": hh3cEponUniOutStatsMulticastPkts,
       "hh3cEponUniOutStatsPausePkts": hh3cEponUniOutStatsPausePkts,
       "hh3cEponUniOutTotalErrors": hh3cEponUniOutTotalErrors,
       "hh3cEponUniOutStatsCollisions": hh3cEponUniOutStatsCollisions,
       "hh3cEponUniOutDelayExceededDiscards": hh3cEponUniOutDelayExceededDiscards,
       "hh3cEponUniOutErrorbyOther": hh3cEponUniOutErrorbyOther,
       "hh3cEponUniOutDroppedFrames": hh3cEponUniOutDroppedFrames,
       "hh3cEponUniIgmpInfoTable": hh3cEponUniIgmpInfoTable,
       "hh3cEponUniIgmpInfoEntry": hh3cEponUniIgmpInfoEntry,
       "hh3cEponUniMacIndex": hh3cEponUniMacIndex,
       "hh3cEponUniIgmpMacAddress": hh3cEponUniIgmpMacAddress,
       "hh3cEponUniIgmpVlanId": hh3cEponUniIgmpVlanId,
       "hh3cEponUniParaMan": hh3cEponUniParaMan,
       "hh3cEponUniLineRateMax": hh3cEponUniLineRateMax,
       "hh3cEponUniLineRateStep": hh3cEponUniLineRateStep,
       "hh3cEponUniNumberOnOnu": hh3cEponUniNumberOnOnu,
       "hh3cEponUniScalarGroup": hh3cEponUniScalarGroup,
       "hh3cEponUniPortPolicyTable": hh3cEponUniPortPolicyTable,
       "hh3cEponUniPortPolicyEntry": hh3cEponUniPortPolicyEntry,
       "hh3cEponUniPortPolicyStatus": hh3cEponUniPortPolicyStatus,
       "hh3cEponUniPortPolicyCir": hh3cEponUniPortPolicyCir,
       "hh3cEponUniPortPolicyBucketDepth": hh3cEponUniPortPolicyBucketDepth,
       "hh3cEponUniPortPolicyExtraBurst": hh3cEponUniPortPolicyExtraBurst,
       "hh3cEponUniPortPolicyInboundCir": hh3cEponUniPortPolicyInboundCir,
       "hh3cEponUniPortPolicyInboundBucketDepth": hh3cEponUniPortPolicyInboundBucketDepth,
       "hh3cEponUniPortPolicyInboundExtraBurst": hh3cEponUniPortPolicyInboundExtraBurst,
       "hh3cEponUniPortPolicyOutboundCir": hh3cEponUniPortPolicyOutboundCir,
       "hh3cEponUniPortPolicyOutboundPir": hh3cEponUniPortPolicyOutboundPir,
       "hh3cEponUniMulticastTable": hh3cEponUniMulticastTable,
       "hh3cEponUniMulticastEntry": hh3cEponUniMulticastEntry,
       "hh3cEponUniMulticastGroupNumber": hh3cEponUniMulticastGroupNumber,
       "hh3cEponUniMulticastVlanList": hh3cEponUniMulticastVlanList,
       "hh3cEponUniMulticastStripStatus": hh3cEponUniMulticastStripStatus,
       "hh3cEponUniMulticastFastleave": hh3cEponUniMulticastFastleave,
       "hh3cEponUniTechAbilityTable": hh3cEponUniTechAbilityTable,
       "hh3cEponUniTechAbilityEntry": hh3cEponUniTechAbilityEntry,
       "hh3cEponUniLocalTechAbility": hh3cEponUniLocalTechAbility,
       "hh3cEponUniAdvertisedTechAbility": hh3cEponUniAdvertisedTechAbility,
       "hh3cEponUniMulticastControlTable": hh3cEponUniMulticastControlTable,
       "hh3cEponUniMulticastControlEntry": hh3cEponUniMulticastControlEntry,
       "hh3cEponUniMulticastVlanIndex": hh3cEponUniMulticastVlanIndex,
       "hh3cEponUniMulticastAddressList": hh3cEponUniMulticastAddressList,
       "hh3cEponUniMulticastAccessRule": hh3cEponUniMulticastAccessRule,
       "hh3cEponUniMulticastChannelLimit": hh3cEponUniMulticastChannelLimit,
       "hh3cEponUniMulticastPreTimeSlice": hh3cEponUniMulticastPreTimeSlice,
       "hh3cEponUniMulticastPreTimes": hh3cEponUniMulticastPreTimes,
       "hh3cEponUniMulticastPreInterval": hh3cEponUniMulticastPreInterval,
       "hh3cEponUniMulticastRowStatus": hh3cEponUniMulticastRowStatus,
       "hh3cEponUniMulticastIndex": hh3cEponUniMulticastIndex,
       "hh3cEponUniMulticastSourceIpList": hh3cEponUniMulticastSourceIpList,
       "hh3cEponUniMulticastResetInterval": hh3cEponUniMulticastResetInterval,
       "hh3cEponUniQosIndexNextTable": hh3cEponUniQosIndexNextTable,
       "hh3cEponUniQosIndexNextEntry": hh3cEponUniQosIndexNextEntry,
       "hh3cEponUniQosConfIndexNext": hh3cEponUniQosConfIndexNext,
       "hh3cEponUniQosConfTable": hh3cEponUniQosConfTable,
       "hh3cEponUniQosConfEntry": hh3cEponUniQosConfEntry,
       "hh3cEponUniQosConfIndex": hh3cEponUniQosConfIndex,
       "hh3cEponUniQosConfRuleIndexNext": hh3cEponUniQosConfRuleIndexNext,
       "hh3cEponUniQosConfMappedQueue": hh3cEponUniQosConfMappedQueue,
       "hh3cEponUniQosConfMarkedPriority": hh3cEponUniQosConfMarkedPriority,
       "hh3cEponUniQosConfRowStatus": hh3cEponUniQosConfRowStatus,
       "hh3cEponUniQosRuleTable": hh3cEponUniQosRuleTable,
       "hh3cEponUniQosRuleEntry": hh3cEponUniQosRuleEntry,
       "hh3cEponUniQosRuleIndex": hh3cEponUniQosRuleIndex,
       "hh3cEponUniQosRuleSelector": hh3cEponUniQosRuleSelector,
       "hh3cEponUniQosRuleValue": hh3cEponUniQosRuleValue,
       "hh3cEponUniQosRuleMacAddress": hh3cEponUniQosRuleMacAddress,
       "hh3cEponUniQosRuleOperator": hh3cEponUniQosRuleOperator,
       "hh3cEponUniQosRuleRowStatus": hh3cEponUniQosRuleRowStatus,
       "hh3cEponUniMirrorGroupTable": hh3cEponUniMirrorGroupTable,
       "hh3cEponUniMirrorGroupEntry": hh3cEponUniMirrorGroupEntry,
       "hh3cEponUniMirrorGroupID": hh3cEponUniMirrorGroupID,
       "hh3cEponUniMirrorInboundPortList": hh3cEponUniMirrorInboundPortList,
       "hh3cEponUniMirrorOutboundPortList": hh3cEponUniMirrorOutboundPortList,
       "hh3cEponUniMonitorPort": hh3cEponUniMonitorPort,
       "hh3cEponUniMirrorRowStatus": hh3cEponUniMirrorRowStatus,
       "hh3cEponUniMirrorGroupIdNextTable": hh3cEponUniMirrorGroupIdNextTable,
       "hh3cEponUniMirrorGroupIdNextEntry": hh3cEponUniMirrorGroupIdNextEntry,
       "hh3cEponUniMirrorGroupIDNext": hh3cEponUniMirrorGroupIDNext,
       "hh3cEponUniMulticastCtrlInfoTable": hh3cEponUniMulticastCtrlInfoTable,
       "hh3cEponUniMulticastCtrlInfoEntry": hh3cEponUniMulticastCtrlInfoEntry,
       "hh3cEponUniMultActVlan": hh3cEponUniMultActVlan,
       "hh3cEponUniMultActAddress": hh3cEponUniMultActAddress,
       "hh3cEponUniMultActAccessRule": hh3cEponUniMultActAccessRule,
       "hh3cEponUniMultActPreTimes": hh3cEponUniMultActPreTimes,
       "hh3cEponUniMultActPreRemain": hh3cEponUniMultActPreRemain,
       "hh3cEponUniMulticastIndexNextTable": hh3cEponUniMulticastIndexNextTable,
       "hh3cEponUniMulticastIndexNextEntry": hh3cEponUniMulticastIndexNextEntry,
       "hh3cEponUniMulticastConfIndexNext": hh3cEponUniMulticastConfIndexNext,
       "hh3cEponCTCAlarmTable": hh3cEponCTCAlarmTable,
       "hh3cEponCTCAlarmEntry": hh3cEponCTCAlarmEntry,
       "hh3cEponCTCAlarmID": hh3cEponCTCAlarmID,
       "hh3cEponCTCAlarmProtocol": hh3cEponCTCAlarmProtocol,
       "hh3cEponCTCAlarmEnable": hh3cEponCTCAlarmEnable,
       "hh3cEponCTCAlarmTriggerThresVal": hh3cEponCTCAlarmTriggerThresVal,
       "hh3cEponCTCAlarmClearThresVal": hh3cEponCTCAlarmClearThresVal,
       "hh3cEponUniErrorInfo": hh3cEponUniErrorInfo,
       "hh3cEponCTCAlarmInfo": hh3cEponCTCAlarmInfo,
       "hh3cUniStatisticsTable": hh3cUniStatisticsTable,
       "hh3cUniStatisticsEntry": hh3cUniStatisticsEntry,
       "hh3cUniStatisticsPeriodVal": hh3cUniStatisticsPeriodVal,
       "hh3cUniStatisticsEnable": hh3cUniStatisticsEnable,
       "hh3cUniPoeTable": hh3cUniPoeTable,
       "hh3cUniPoeEntry": hh3cUniPoeEntry,
       "hh3cUniPoeEnable": hh3cUniPoeEnable,
       "hh3cUniPoeMode": hh3cUniPoeMode,
       "hh3cUniPoePriority": hh3cUniPoePriority,
       "hh3cUniPoeMaxPowerClass": hh3cUniPoeMaxPowerClass,
       "hh3cUniPoeMaxPowerValue": hh3cUniPoeMaxPowerValue,
       "hh3cUniPoeLegacyEnable": hh3cUniPoeLegacyEnable,
       "hh3cUniPoeInfoTable": hh3cUniPoeInfoTable,
       "hh3cUniPoeInfoEntry": hh3cUniPoeInfoEntry,
       "hh3cUniPoeInfoCapability": hh3cUniPoeInfoCapability,
       "hh3cUniPoeInfoEnable": hh3cUniPoeInfoEnable,
       "hh3cUniPoeInfoLegacyEnable": hh3cUniPoeInfoLegacyEnable,
       "hh3cUniPoeInfoMode": hh3cUniPoeInfoMode,
       "hh3cUniPoeInfoPriority": hh3cUniPoeInfoPriority,
       "hh3cUniPoeInfoMaxPwrClass": hh3cUniPoeInfoMaxPwrClass,
       "hh3cUniPoeInfoMaxPwrValue": hh3cUniPoeInfoMaxPwrValue,
       "hh3cUniPoeInfoPdClass": hh3cUniPoeInfoPdClass,
       "hh3cUniPoeInfoPwrSuppStat": hh3cUniPoeInfoPwrSuppStat,
       "hh3cUniPoeInfoSignalErrCnt": hh3cUniPoeInfoSignalErrCnt,
       "hh3cUniPoeInfoPwrDeniedCnt": hh3cUniPoeInfoPwrDeniedCnt,
       "hh3cUniPoeInfoPwrOverCnt": hh3cUniPoeInfoPwrOverCnt,
       "hh3cUniPoeInfoCurOverCnt": hh3cUniPoeInfoCurOverCnt,
       "hh3cUniPoeInfoPdUndetectCnt": hh3cUniPoeInfoPdUndetectCnt,
       "hh3cUniPoeInfoMaxPower": hh3cUniPoeInfoMaxPower,
       "hh3cUniPoeInfoCurOutputPwr": hh3cUniPoeInfoCurOutputPwr,
       "hh3cUniPoeInfoAvgOutputPwr": hh3cUniPoeInfoAvgOutputPwr,
       "hh3cUniPoeInfoPeakOutputPwr": hh3cUniPoeInfoPeakOutputPwr,
       "hh3cEponUniTrap": hh3cEponUniTrap,
       "hh3cEponUniTrapPrefix": hh3cEponUniTrapPrefix,
       "hh3cEponUniLinkUpTrap": hh3cEponUniLinkUpTrap,
       "hh3cEponUniLinkDownTrap": hh3cEponUniLinkDownTrap,
       "hh3cEponUniLoopBackDetectedTrap": hh3cEponUniLoopBackDetectedTrap,
       "hh3cEponUniLoopBackRecoveredTrap": hh3cEponUniLoopBackRecoveredTrap,
       "hh3cEponCTCAlarmTrap": hh3cEponCTCAlarmTrap,
       "hh3cEponCTCAlarmRecoverTrap": hh3cEponCTCAlarmRecoverTrap}
)
