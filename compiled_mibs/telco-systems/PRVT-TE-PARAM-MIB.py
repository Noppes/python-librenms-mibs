# SNMP MIB module (PRVT-TE-PARAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-TE-PARAM-MIB

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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(mpls,) = mibBuilder.importSymbols(
    "PRVT-CR-LDP-MIB",
    "mpls")

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

prvtTeParamMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9)
)
if mibBuilder.loadTexts:
    prvtTeParamMib.setRevisions(
        ("2007-12-11 00:00",
         "2007-10-25 00:00",
         "2007-08-10 00:00",
         "2007-06-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TeLinkBandwidth(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



# MIB Managed Objects in the order of their OIDs

_PrvtTeParamMibNotifications_ObjectIdentity = ObjectIdentity
prvtTeParamMibNotifications = _PrvtTeParamMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 0)
)
_PrvtTeParamMibObjects_ObjectIdentity = ObjectIdentity
prvtTeParamMibObjects = _PrvtTeParamMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1)
)


class _OspfOpaqueEngSupport_Type(Integer32):
    """Custom type ospfOpaqueEngSupport based on Integer32"""
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


_OspfOpaqueEngSupport_Type.__name__ = "Integer32"
_OspfOpaqueEngSupport_Object = MibScalar
ospfOpaqueEngSupport = _OspfOpaqueEngSupport_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 1),
    _OspfOpaqueEngSupport_Type()
)
ospfOpaqueEngSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfOpaqueEngSupport.setStatus("current")
_OspfTeRouterId_Type = IpAddress
_OspfTeRouterId_Object = MibScalar
ospfTeRouterId = _OspfTeRouterId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 2),
    _OspfTeRouterId_Type()
)
ospfTeRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfTeRouterId.setStatus("current")


class _OspfTrafficEngSupport_Type(Integer32):
    """Custom type ospfTrafficEngSupport based on Integer32"""
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


_OspfTrafficEngSupport_Type.__name__ = "Integer32"
_OspfTrafficEngSupport_Object = MibScalar
ospfTrafficEngSupport = _OspfTrafficEngSupport_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 3),
    _OspfTrafficEngSupport_Type()
)
ospfTrafficEngSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfTrafficEngSupport.setStatus("current")
_PrvtTeParamTable_Object = MibTable
prvtTeParamTable = _PrvtTeParamTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4)
)
if mibBuilder.loadTexts:
    prvtTeParamTable.setStatus("current")
_PrvtTeParamEntry_Object = MibTableRow
prvtTeParamEntry = _PrvtTeParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1)
)
prvtTeParamEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtTeParamEntry.setStatus("current")
_PrvtTeParamLinkAddressType_Type = InetAddressType
_PrvtTeParamLinkAddressType_Object = MibTableColumn
prvtTeParamLinkAddressType = _PrvtTeParamLinkAddressType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 1),
    _PrvtTeParamLinkAddressType_Type()
)
prvtTeParamLinkAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamLinkAddressType.setStatus("current")
_PrvtTeParamMetric_Type = Unsigned32
_PrvtTeParamMetric_Object = MibTableColumn
prvtTeParamMetric = _PrvtTeParamMetric_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 2),
    _PrvtTeParamMetric_Type()
)
prvtTeParamMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTeParamMetric.setStatus("current")


class _PrvtTeParamLinkType_Type(Integer32):
    """Custom type prvtTeParamLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiAccess", 1),
          ("pointToPoint", 2))
    )


_PrvtTeParamLinkType_Type.__name__ = "Integer32"
_PrvtTeParamLinkType_Object = MibTableColumn
prvtTeParamLinkType = _PrvtTeParamLinkType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 3),
    _PrvtTeParamLinkType_Type()
)
prvtTeParamLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamLinkType.setStatus("current")
_PrvtTeParamPhysicalBandwidth_Type = TeLinkBandwidth
_PrvtTeParamPhysicalBandwidth_Object = MibTableColumn
prvtTeParamPhysicalBandwidth = _PrvtTeParamPhysicalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 4),
    _PrvtTeParamPhysicalBandwidth_Type()
)
prvtTeParamPhysicalBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTeParamPhysicalBandwidth.setStatus("current")
_PrvtTeParamMaximumReservableBandwidth_Type = TeLinkBandwidth
_PrvtTeParamMaximumReservableBandwidth_Object = MibTableColumn
prvtTeParamMaximumReservableBandwidth = _PrvtTeParamMaximumReservableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 5),
    _PrvtTeParamMaximumReservableBandwidth_Type()
)
prvtTeParamMaximumReservableBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTeParamMaximumReservableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamMaximumReservableBandwidth.setUnits("bps")
_PrvtTeParamMaxReservableBandwidthPrio0_Type = TeLinkBandwidth
_PrvtTeParamMaxReservableBandwidthPrio0_Object = MibTableColumn
prvtTeParamMaxReservableBandwidthPrio0 = _PrvtTeParamMaxReservableBandwidthPrio0_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 6),
    _PrvtTeParamMaxReservableBandwidthPrio0_Type()
)
prvtTeParamMaxReservableBandwidthPrio0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio0.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio0.setUnits("bps")
_PrvtTeParamMaxReservableBandwidthPrio1_Type = TeLinkBandwidth
_PrvtTeParamMaxReservableBandwidthPrio1_Object = MibTableColumn
prvtTeParamMaxReservableBandwidthPrio1 = _PrvtTeParamMaxReservableBandwidthPrio1_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 7),
    _PrvtTeParamMaxReservableBandwidthPrio1_Type()
)
prvtTeParamMaxReservableBandwidthPrio1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio1.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio1.setUnits("bps")
_PrvtTeParamMaxReservableBandwidthPrio2_Type = TeLinkBandwidth
_PrvtTeParamMaxReservableBandwidthPrio2_Object = MibTableColumn
prvtTeParamMaxReservableBandwidthPrio2 = _PrvtTeParamMaxReservableBandwidthPrio2_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 8),
    _PrvtTeParamMaxReservableBandwidthPrio2_Type()
)
prvtTeParamMaxReservableBandwidthPrio2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio2.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio2.setUnits("bps")
_PrvtTeParamMaxReservableBandwidthPrio3_Type = TeLinkBandwidth
_PrvtTeParamMaxReservableBandwidthPrio3_Object = MibTableColumn
prvtTeParamMaxReservableBandwidthPrio3 = _PrvtTeParamMaxReservableBandwidthPrio3_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 9),
    _PrvtTeParamMaxReservableBandwidthPrio3_Type()
)
prvtTeParamMaxReservableBandwidthPrio3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio3.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio3.setUnits("bps")
_PrvtTeParamMaxReservableBandwidthPrio4_Type = TeLinkBandwidth
_PrvtTeParamMaxReservableBandwidthPrio4_Object = MibTableColumn
prvtTeParamMaxReservableBandwidthPrio4 = _PrvtTeParamMaxReservableBandwidthPrio4_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 10),
    _PrvtTeParamMaxReservableBandwidthPrio4_Type()
)
prvtTeParamMaxReservableBandwidthPrio4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio4.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio4.setUnits("bps")
_PrvtTeParamMaxReservableBandwidthPrio5_Type = TeLinkBandwidth
_PrvtTeParamMaxReservableBandwidthPrio5_Object = MibTableColumn
prvtTeParamMaxReservableBandwidthPrio5 = _PrvtTeParamMaxReservableBandwidthPrio5_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 11),
    _PrvtTeParamMaxReservableBandwidthPrio5_Type()
)
prvtTeParamMaxReservableBandwidthPrio5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio5.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio5.setUnits("bps")
_PrvtTeParamMaxReservableBandwidthPrio6_Type = TeLinkBandwidth
_PrvtTeParamMaxReservableBandwidthPrio6_Object = MibTableColumn
prvtTeParamMaxReservableBandwidthPrio6 = _PrvtTeParamMaxReservableBandwidthPrio6_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 12),
    _PrvtTeParamMaxReservableBandwidthPrio6_Type()
)
prvtTeParamMaxReservableBandwidthPrio6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio6.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio6.setUnits("bps")
_PrvtTeParamMaxReservableBandwidthPrio7_Type = TeLinkBandwidth
_PrvtTeParamMaxReservableBandwidthPrio7_Object = MibTableColumn
prvtTeParamMaxReservableBandwidthPrio7 = _PrvtTeParamMaxReservableBandwidthPrio7_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 13),
    _PrvtTeParamMaxReservableBandwidthPrio7_Type()
)
prvtTeParamMaxReservableBandwidthPrio7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio7.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamMaxReservableBandwidthPrio7.setUnits("bps")
_PrvtTeParamReservedBandwidthPrio0_Type = TeLinkBandwidth
_PrvtTeParamReservedBandwidthPrio0_Object = MibTableColumn
prvtTeParamReservedBandwidthPrio0 = _PrvtTeParamReservedBandwidthPrio0_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 14),
    _PrvtTeParamReservedBandwidthPrio0_Type()
)
prvtTeParamReservedBandwidthPrio0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio0.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio0.setUnits("bps")
_PrvtTeParamReservedBandwidthPrio1_Type = TeLinkBandwidth
_PrvtTeParamReservedBandwidthPrio1_Object = MibTableColumn
prvtTeParamReservedBandwidthPrio1 = _PrvtTeParamReservedBandwidthPrio1_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 15),
    _PrvtTeParamReservedBandwidthPrio1_Type()
)
prvtTeParamReservedBandwidthPrio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio1.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio1.setUnits("bps")
_PrvtTeParamReservedBandwidthPrio2_Type = TeLinkBandwidth
_PrvtTeParamReservedBandwidthPrio2_Object = MibTableColumn
prvtTeParamReservedBandwidthPrio2 = _PrvtTeParamReservedBandwidthPrio2_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 16),
    _PrvtTeParamReservedBandwidthPrio2_Type()
)
prvtTeParamReservedBandwidthPrio2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio2.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio2.setUnits("bps")
_PrvtTeParamReservedBandwidthPrio3_Type = TeLinkBandwidth
_PrvtTeParamReservedBandwidthPrio3_Object = MibTableColumn
prvtTeParamReservedBandwidthPrio3 = _PrvtTeParamReservedBandwidthPrio3_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 17),
    _PrvtTeParamReservedBandwidthPrio3_Type()
)
prvtTeParamReservedBandwidthPrio3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio3.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio3.setUnits("bps")
_PrvtTeParamReservedBandwidthPrio4_Type = TeLinkBandwidth
_PrvtTeParamReservedBandwidthPrio4_Object = MibTableColumn
prvtTeParamReservedBandwidthPrio4 = _PrvtTeParamReservedBandwidthPrio4_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 18),
    _PrvtTeParamReservedBandwidthPrio4_Type()
)
prvtTeParamReservedBandwidthPrio4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio4.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio4.setUnits("bps")
_PrvtTeParamReservedBandwidthPrio5_Type = TeLinkBandwidth
_PrvtTeParamReservedBandwidthPrio5_Object = MibTableColumn
prvtTeParamReservedBandwidthPrio5 = _PrvtTeParamReservedBandwidthPrio5_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 19),
    _PrvtTeParamReservedBandwidthPrio5_Type()
)
prvtTeParamReservedBandwidthPrio5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio5.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio5.setUnits("bps")
_PrvtTeParamReservedBandwidthPrio6_Type = TeLinkBandwidth
_PrvtTeParamReservedBandwidthPrio6_Object = MibTableColumn
prvtTeParamReservedBandwidthPrio6 = _PrvtTeParamReservedBandwidthPrio6_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 20),
    _PrvtTeParamReservedBandwidthPrio6_Type()
)
prvtTeParamReservedBandwidthPrio6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio6.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio6.setUnits("bps")
_PrvtTeParamReservedBandwidthPrio7_Type = TeLinkBandwidth
_PrvtTeParamReservedBandwidthPrio7_Object = MibTableColumn
prvtTeParamReservedBandwidthPrio7 = _PrvtTeParamReservedBandwidthPrio7_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 21),
    _PrvtTeParamReservedBandwidthPrio7_Type()
)
prvtTeParamReservedBandwidthPrio7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio7.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamReservedBandwidthPrio7.setUnits("bps")
_PrvtTeParamUnreservedBandwidthPrio0_Type = TeLinkBandwidth
_PrvtTeParamUnreservedBandwidthPrio0_Object = MibTableColumn
prvtTeParamUnreservedBandwidthPrio0 = _PrvtTeParamUnreservedBandwidthPrio0_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 22),
    _PrvtTeParamUnreservedBandwidthPrio0_Type()
)
prvtTeParamUnreservedBandwidthPrio0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio0.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio0.setUnits("bps")
_PrvtTeParamUnreservedBandwidthPrio1_Type = TeLinkBandwidth
_PrvtTeParamUnreservedBandwidthPrio1_Object = MibTableColumn
prvtTeParamUnreservedBandwidthPrio1 = _PrvtTeParamUnreservedBandwidthPrio1_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 23),
    _PrvtTeParamUnreservedBandwidthPrio1_Type()
)
prvtTeParamUnreservedBandwidthPrio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio1.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio1.setUnits("bps")
_PrvtTeParamUnreservedBandwidthPrio2_Type = TeLinkBandwidth
_PrvtTeParamUnreservedBandwidthPrio2_Object = MibTableColumn
prvtTeParamUnreservedBandwidthPrio2 = _PrvtTeParamUnreservedBandwidthPrio2_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 24),
    _PrvtTeParamUnreservedBandwidthPrio2_Type()
)
prvtTeParamUnreservedBandwidthPrio2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio2.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio2.setUnits("bps")
_PrvtTeParamUnreservedBandwidthPrio3_Type = TeLinkBandwidth
_PrvtTeParamUnreservedBandwidthPrio3_Object = MibTableColumn
prvtTeParamUnreservedBandwidthPrio3 = _PrvtTeParamUnreservedBandwidthPrio3_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 25),
    _PrvtTeParamUnreservedBandwidthPrio3_Type()
)
prvtTeParamUnreservedBandwidthPrio3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio3.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio3.setUnits("bps")
_PrvtTeParamUnreservedBandwidthPrio4_Type = TeLinkBandwidth
_PrvtTeParamUnreservedBandwidthPrio4_Object = MibTableColumn
prvtTeParamUnreservedBandwidthPrio4 = _PrvtTeParamUnreservedBandwidthPrio4_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 26),
    _PrvtTeParamUnreservedBandwidthPrio4_Type()
)
prvtTeParamUnreservedBandwidthPrio4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio4.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio4.setUnits("bps")
_PrvtTeParamUnreservedBandwidthPrio5_Type = TeLinkBandwidth
_PrvtTeParamUnreservedBandwidthPrio5_Object = MibTableColumn
prvtTeParamUnreservedBandwidthPrio5 = _PrvtTeParamUnreservedBandwidthPrio5_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 27),
    _PrvtTeParamUnreservedBandwidthPrio5_Type()
)
prvtTeParamUnreservedBandwidthPrio5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio5.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio5.setUnits("bps")
_PrvtTeParamUnreservedBandwidthPrio6_Type = TeLinkBandwidth
_PrvtTeParamUnreservedBandwidthPrio6_Object = MibTableColumn
prvtTeParamUnreservedBandwidthPrio6 = _PrvtTeParamUnreservedBandwidthPrio6_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 28),
    _PrvtTeParamUnreservedBandwidthPrio6_Type()
)
prvtTeParamUnreservedBandwidthPrio6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio6.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio6.setUnits("bps")
_PrvtTeParamUnreservedBandwidthPrio7_Type = TeLinkBandwidth
_PrvtTeParamUnreservedBandwidthPrio7_Object = MibTableColumn
prvtTeParamUnreservedBandwidthPrio7 = _PrvtTeParamUnreservedBandwidthPrio7_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 29),
    _PrvtTeParamUnreservedBandwidthPrio7_Type()
)
prvtTeParamUnreservedBandwidthPrio7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio7.setStatus("current")
if mibBuilder.loadTexts:
    prvtTeParamUnreservedBandwidthPrio7.setUnits("bps")
_PrvtTeParamResourceClass_Type = Unsigned32
_PrvtTeParamResourceClass_Object = MibTableColumn
prvtTeParamResourceClass = _PrvtTeParamResourceClass_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 4, 1, 30),
    _PrvtTeParamResourceClass_Type()
)
prvtTeParamResourceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTeParamResourceClass.setStatus("current")
_PrvtTeParamAdminGroupTable_Object = MibTable
prvtTeParamAdminGroupTable = _PrvtTeParamAdminGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 5)
)
if mibBuilder.loadTexts:
    prvtTeParamAdminGroupTable.setStatus("current")
_PrvtTeParamAdminGroupEntry_Object = MibTableRow
prvtTeParamAdminGroupEntry = _PrvtTeParamAdminGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 5, 1)
)
prvtTeParamAdminGroupEntry.setIndexNames(
    (0, "PRVT-TE-PARAM-MIB", "prvtTeParamAdminGroupId"),
)
if mibBuilder.loadTexts:
    prvtTeParamAdminGroupEntry.setStatus("current")


class _PrvtTeParamAdminGroupId_Type(Integer32):
    """Custom type prvtTeParamAdminGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrvtTeParamAdminGroupId_Type.__name__ = "Integer32"
_PrvtTeParamAdminGroupId_Object = MibTableColumn
prvtTeParamAdminGroupId = _PrvtTeParamAdminGroupId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 5, 1, 1),
    _PrvtTeParamAdminGroupId_Type()
)
prvtTeParamAdminGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTeParamAdminGroupId.setStatus("current")


class _PrvtTeParamAdminGroupName_Type(OctetString):
    """Custom type prvtTeParamAdminGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrvtTeParamAdminGroupName_Type.__name__ = "OctetString"
_PrvtTeParamAdminGroupName_Object = MibTableColumn
prvtTeParamAdminGroupName = _PrvtTeParamAdminGroupName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 5, 1, 2),
    _PrvtTeParamAdminGroupName_Type()
)
prvtTeParamAdminGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTeParamAdminGroupName.setStatus("current")
_PrvtCspfStatisticsTable_Object = MibTable
prvtCspfStatisticsTable = _PrvtCspfStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6)
)
if mibBuilder.loadTexts:
    prvtCspfStatisticsTable.setStatus("current")
_PrvtCspfStatisticsEntry_Object = MibTableRow
prvtCspfStatisticsEntry = _PrvtCspfStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1)
)
prvtCspfStatisticsEntry.setIndexNames(
    (0, "PRVT-TE-PARAM-MIB", "prvtCspfEntIndex"),
)
if mibBuilder.loadTexts:
    prvtCspfStatisticsEntry.setStatus("current")
_PrvtCspfEntIndex_Type = Unsigned32
_PrvtCspfEntIndex_Object = MibTableColumn
prvtCspfEntIndex = _PrvtCspfEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 1),
    _PrvtCspfEntIndex_Type()
)
prvtCspfEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtCspfEntIndex.setStatus("current")
_PrvtCspfStatNumRtQueries_Type = Counter32
_PrvtCspfStatNumRtQueries_Object = MibTableColumn
prvtCspfStatNumRtQueries = _PrvtCspfStatNumRtQueries_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 2),
    _PrvtCspfStatNumRtQueries_Type()
)
prvtCspfStatNumRtQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCspfStatNumRtQueries.setStatus("current")
_PrvtCspfStatNumRtsClcd_Type = Counter32
_PrvtCspfStatNumRtsClcd_Object = MibTableColumn
prvtCspfStatNumRtsClcd = _PrvtCspfStatNumRtsClcd_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 3),
    _PrvtCspfStatNumRtsClcd_Type()
)
prvtCspfStatNumRtsClcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCspfStatNumRtsClcd.setStatus("current")
_PrvtCspfStatNumRtsInCache_Type = Gauge32
_PrvtCspfStatNumRtsInCache_Object = MibTableColumn
prvtCspfStatNumRtsInCache = _PrvtCspfStatNumRtsInCache_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 4),
    _PrvtCspfStatNumRtsInCache_Type()
)
prvtCspfStatNumRtsInCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCspfStatNumRtsInCache.setStatus("current")
_PrvtCspfStatNumUpdatesRcvd_Type = Counter32
_PrvtCspfStatNumUpdatesRcvd_Object = MibTableColumn
prvtCspfStatNumUpdatesRcvd = _PrvtCspfStatNumUpdatesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 5),
    _PrvtCspfStatNumUpdatesRcvd_Type()
)
prvtCspfStatNumUpdatesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCspfStatNumUpdatesRcvd.setStatus("current")
_PrvtCspfStatNumEntriesDeleted_Type = Counter32
_PrvtCspfStatNumEntriesDeleted_Object = MibTableColumn
prvtCspfStatNumEntriesDeleted = _PrvtCspfStatNumEntriesDeleted_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 6),
    _PrvtCspfStatNumEntriesDeleted_Type()
)
prvtCspfStatNumEntriesDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCspfStatNumEntriesDeleted.setStatus("current")
_PrvtCspfStatNumLinkEntries_Type = Gauge32
_PrvtCspfStatNumLinkEntries_Object = MibTableColumn
prvtCspfStatNumLinkEntries = _PrvtCspfStatNumLinkEntries_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 7),
    _PrvtCspfStatNumLinkEntries_Type()
)
prvtCspfStatNumLinkEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCspfStatNumLinkEntries.setStatus("current")
_PrvtCspfStatNumNetworkEntries_Type = Gauge32
_PrvtCspfStatNumNetworkEntries_Object = MibTableColumn
prvtCspfStatNumNetworkEntries = _PrvtCspfStatNumNetworkEntries_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 8),
    _PrvtCspfStatNumNetworkEntries_Type()
)
prvtCspfStatNumNetworkEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCspfStatNumNetworkEntries.setStatus("current")
_PrvtCspfStatNumReturnedCaches_Type = Counter32
_PrvtCspfStatNumReturnedCaches_Object = MibTableColumn
prvtCspfStatNumReturnedCaches = _PrvtCspfStatNumReturnedCaches_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 9),
    _PrvtCspfStatNumReturnedCaches_Type()
)
prvtCspfStatNumReturnedCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCspfStatNumReturnedCaches.setStatus("current")
_PrvtCspfStatNumBkupQueries_Type = Counter32
_PrvtCspfStatNumBkupQueries_Object = MibTableColumn
prvtCspfStatNumBkupQueries = _PrvtCspfStatNumBkupQueries_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 10),
    _PrvtCspfStatNumBkupQueries_Type()
)
prvtCspfStatNumBkupQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCspfStatNumBkupQueries.setStatus("current")
_PrvtCspfStatNumBkupPathsFound_Type = Counter32
_PrvtCspfStatNumBkupPathsFound_Object = MibTableColumn
prvtCspfStatNumBkupPathsFound = _PrvtCspfStatNumBkupPathsFound_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 11),
    _PrvtCspfStatNumBkupPathsFound_Type()
)
prvtCspfStatNumBkupPathsFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCspfStatNumBkupPathsFound.setStatus("current")
_PrvtCspfStatNumRouteUpdates_Type = Counter32
_PrvtCspfStatNumRouteUpdates_Object = MibTableColumn
prvtCspfStatNumRouteUpdates = _PrvtCspfStatNumRouteUpdates_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 12),
    _PrvtCspfStatNumRouteUpdates_Type()
)
prvtCspfStatNumRouteUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCspfStatNumRouteUpdates.setStatus("current")
_PrvtCspfStatNumDiscardedRoutes_Type = Counter32
_PrvtCspfStatNumDiscardedRoutes_Object = MibTableColumn
prvtCspfStatNumDiscardedRoutes = _PrvtCspfStatNumDiscardedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 1, 6, 1, 13),
    _PrvtCspfStatNumDiscardedRoutes_Type()
)
prvtCspfStatNumDiscardedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCspfStatNumDiscardedRoutes.setStatus("current")
_PrvtTeParamMibConformance_ObjectIdentity = ObjectIdentity
prvtTeParamMibConformance = _PrvtTeParamMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 9, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-TE-PARAM-MIB",
    **{"TeLinkBandwidth": TeLinkBandwidth,
       "prvtTeParamMib": prvtTeParamMib,
       "prvtTeParamMibNotifications": prvtTeParamMibNotifications,
       "prvtTeParamMibObjects": prvtTeParamMibObjects,
       "ospfOpaqueEngSupport": ospfOpaqueEngSupport,
       "ospfTeRouterId": ospfTeRouterId,
       "ospfTrafficEngSupport": ospfTrafficEngSupport,
       "prvtTeParamTable": prvtTeParamTable,
       "prvtTeParamEntry": prvtTeParamEntry,
       "prvtTeParamLinkAddressType": prvtTeParamLinkAddressType,
       "prvtTeParamMetric": prvtTeParamMetric,
       "prvtTeParamLinkType": prvtTeParamLinkType,
       "prvtTeParamPhysicalBandwidth": prvtTeParamPhysicalBandwidth,
       "prvtTeParamMaximumReservableBandwidth": prvtTeParamMaximumReservableBandwidth,
       "prvtTeParamMaxReservableBandwidthPrio0": prvtTeParamMaxReservableBandwidthPrio0,
       "prvtTeParamMaxReservableBandwidthPrio1": prvtTeParamMaxReservableBandwidthPrio1,
       "prvtTeParamMaxReservableBandwidthPrio2": prvtTeParamMaxReservableBandwidthPrio2,
       "prvtTeParamMaxReservableBandwidthPrio3": prvtTeParamMaxReservableBandwidthPrio3,
       "prvtTeParamMaxReservableBandwidthPrio4": prvtTeParamMaxReservableBandwidthPrio4,
       "prvtTeParamMaxReservableBandwidthPrio5": prvtTeParamMaxReservableBandwidthPrio5,
       "prvtTeParamMaxReservableBandwidthPrio6": prvtTeParamMaxReservableBandwidthPrio6,
       "prvtTeParamMaxReservableBandwidthPrio7": prvtTeParamMaxReservableBandwidthPrio7,
       "prvtTeParamReservedBandwidthPrio0": prvtTeParamReservedBandwidthPrio0,
       "prvtTeParamReservedBandwidthPrio1": prvtTeParamReservedBandwidthPrio1,
       "prvtTeParamReservedBandwidthPrio2": prvtTeParamReservedBandwidthPrio2,
       "prvtTeParamReservedBandwidthPrio3": prvtTeParamReservedBandwidthPrio3,
       "prvtTeParamReservedBandwidthPrio4": prvtTeParamReservedBandwidthPrio4,
       "prvtTeParamReservedBandwidthPrio5": prvtTeParamReservedBandwidthPrio5,
       "prvtTeParamReservedBandwidthPrio6": prvtTeParamReservedBandwidthPrio6,
       "prvtTeParamReservedBandwidthPrio7": prvtTeParamReservedBandwidthPrio7,
       "prvtTeParamUnreservedBandwidthPrio0": prvtTeParamUnreservedBandwidthPrio0,
       "prvtTeParamUnreservedBandwidthPrio1": prvtTeParamUnreservedBandwidthPrio1,
       "prvtTeParamUnreservedBandwidthPrio2": prvtTeParamUnreservedBandwidthPrio2,
       "prvtTeParamUnreservedBandwidthPrio3": prvtTeParamUnreservedBandwidthPrio3,
       "prvtTeParamUnreservedBandwidthPrio4": prvtTeParamUnreservedBandwidthPrio4,
       "prvtTeParamUnreservedBandwidthPrio5": prvtTeParamUnreservedBandwidthPrio5,
       "prvtTeParamUnreservedBandwidthPrio6": prvtTeParamUnreservedBandwidthPrio6,
       "prvtTeParamUnreservedBandwidthPrio7": prvtTeParamUnreservedBandwidthPrio7,
       "prvtTeParamResourceClass": prvtTeParamResourceClass,
       "prvtTeParamAdminGroupTable": prvtTeParamAdminGroupTable,
       "prvtTeParamAdminGroupEntry": prvtTeParamAdminGroupEntry,
       "prvtTeParamAdminGroupId": prvtTeParamAdminGroupId,
       "prvtTeParamAdminGroupName": prvtTeParamAdminGroupName,
       "prvtCspfStatisticsTable": prvtCspfStatisticsTable,
       "prvtCspfStatisticsEntry": prvtCspfStatisticsEntry,
       "prvtCspfEntIndex": prvtCspfEntIndex,
       "prvtCspfStatNumRtQueries": prvtCspfStatNumRtQueries,
       "prvtCspfStatNumRtsClcd": prvtCspfStatNumRtsClcd,
       "prvtCspfStatNumRtsInCache": prvtCspfStatNumRtsInCache,
       "prvtCspfStatNumUpdatesRcvd": prvtCspfStatNumUpdatesRcvd,
       "prvtCspfStatNumEntriesDeleted": prvtCspfStatNumEntriesDeleted,
       "prvtCspfStatNumLinkEntries": prvtCspfStatNumLinkEntries,
       "prvtCspfStatNumNetworkEntries": prvtCspfStatNumNetworkEntries,
       "prvtCspfStatNumReturnedCaches": prvtCspfStatNumReturnedCaches,
       "prvtCspfStatNumBkupQueries": prvtCspfStatNumBkupQueries,
       "prvtCspfStatNumBkupPathsFound": prvtCspfStatNumBkupPathsFound,
       "prvtCspfStatNumRouteUpdates": prvtCspfStatNumRouteUpdates,
       "prvtCspfStatNumDiscardedRoutes": prvtCspfStatNumDiscardedRoutes,
       "prvtTeParamMibConformance": prvtTeParamMibConformance}
)
