# SNMP MIB module (PRVT-MPLS-TE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-MPLS-TE-MIB

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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv4,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressPrefixLength",
    "InetAddressType")

(MplsBitRate,
 MplsBurstSize,
 MplsExtendedTunnelId,
 MplsLSPID,
 MplsOwner,
 MplsPathIndex,
 MplsPathIndexOrZero,
 MplsTunnelAffinity,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex,
 TeHopAddress,
 TeHopAddressAS,
 TeHopAddressType,
 TeHopAddressUnnum) = mibBuilder.importSymbols(
    "MPLS-TC-PRIV-STDEXT-MIB",
    "MplsBitRate",
    "MplsBurstSize",
    "MplsExtendedTunnelId",
    "MplsLSPID",
    "MplsOwner",
    "MplsPathIndex",
    "MplsPathIndexOrZero",
    "MplsTunnelAffinity",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex",
    "TeHopAddress",
    "TeHopAddressAS",
    "TeHopAddressType",
    "TeHopAddressUnnum")

(mpls,) = mibBuilder.importSymbols(
    "PRVT-CR-LDP-MIB",
    "mpls")

(prvtMplsTeMibEntityIndex,) = mibBuilder.importSymbols(
    "PRVT-TEMIB-ENTITY-MIB",
    "prvtMplsTeMibEntityIndex")

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
 iso,
 transmission,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "transmission",
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mplsTeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    mplsTeMIB.setRevisions(
        ("2009-02-17 00:00",
         "2008-11-20 00:00",
         "2008-08-28 00:00",
         "2008-03-03 00:00",
         "2007-12-06 00:00",
         "2007-12-02 09:59")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MplsTunnelIndexSyntax(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class MplsLsrId(TextualConvention, Unsigned32):
    status = "current"


class MplsGeneralizedLabelType(TextualConvention, Integer32):
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
        *(("mplsLabel", 1),
          ("generalizedLabel", 2),
          ("wavebandLabel", 3))
    )



class MplsTunnelPrivateDataSyntax(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class MplsTunnelTNAAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class MplsGeneralizedLabel(TextualConvention, OctetString):
    status = "current"
    displayHint = "255x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_MplsTeObjects_ObjectIdentity = ObjectIdentity
mplsTeObjects = _MplsTeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1)
)
_MplsTunnelIndexNextTable_Object = MibTable
mplsTunnelIndexNextTable = _MplsTunnelIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mplsTunnelIndexNextTable.setStatus("current")
_MplsTunnelIndexNextEntry_Object = MibTableRow
mplsTunnelIndexNextEntry = _MplsTunnelIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 1, 1)
)
mplsTunnelIndexNextEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelIndexNextEntry.setStatus("current")
_MplsTunnelIndexNextIndex_Type = Integer32
_MplsTunnelIndexNextIndex_Object = MibTableColumn
mplsTunnelIndexNextIndex = _MplsTunnelIndexNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 1, 1, 1),
    _MplsTunnelIndexNextIndex_Type()
)
mplsTunnelIndexNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelIndexNextIndex.setStatus("current")
_MplsTunnelTable_Object = MibTable
mplsTunnelTable = _MplsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mplsTunnelTable.setStatus("current")
_MplsTunnelEntry_Object = MibTableRow
mplsTunnelEntry = _MplsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1)
)
mplsTunnelEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
    (0, "PRVT-MPLS-TE-MIB", "mplsTunnelIndex"),
    (0, "PRVT-MPLS-TE-MIB", "mplsTunnelInstance"),
    (0, "PRVT-MPLS-TE-MIB", "mplsTunnelIngressLSRId"),
    (0, "PRVT-MPLS-TE-MIB", "mplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    mplsTunnelEntry.setStatus("current")
_MplsTunnelIndex_Type = MplsTunnelIndexSyntax
_MplsTunnelIndex_Object = MibTableColumn
mplsTunnelIndex = _MplsTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 1),
    _MplsTunnelIndex_Type()
)
mplsTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelIndex.setStatus("current")
_MplsTunnelInstance_Type = MplsTunnelInstanceIndex
_MplsTunnelInstance_Object = MibTableColumn
mplsTunnelInstance = _MplsTunnelInstance_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 2),
    _MplsTunnelInstance_Type()
)
mplsTunnelInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelInstance.setStatus("current")
_MplsTunnelIngressLSRId_Type = MplsExtendedTunnelId
_MplsTunnelIngressLSRId_Object = MibTableColumn
mplsTunnelIngressLSRId = _MplsTunnelIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 3),
    _MplsTunnelIngressLSRId_Type()
)
mplsTunnelIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelIngressLSRId.setStatus("current")
_MplsTunnelEgressLSRId_Type = MplsExtendedTunnelId
_MplsTunnelEgressLSRId_Object = MibTableColumn
mplsTunnelEgressLSRId = _MplsTunnelEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 4),
    _MplsTunnelEgressLSRId_Type()
)
mplsTunnelEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelEgressLSRId.setStatus("current")
_MplsTunnelName_Type = DisplayString
_MplsTunnelName_Object = MibTableColumn
mplsTunnelName = _MplsTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 5),
    _MplsTunnelName_Type()
)
mplsTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelName.setStatus("current")
_MplsTunnelDescr_Type = DisplayString
_MplsTunnelDescr_Object = MibTableColumn
mplsTunnelDescr = _MplsTunnelDescr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 6),
    _MplsTunnelDescr_Type()
)
mplsTunnelDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelDescr.setStatus("current")


class _MplsTunnelIsIf_Type(TruthValue):
    """Custom type mplsTunnelIsIf based on TruthValue"""
    defaultValue = 2


_MplsTunnelIsIf_Type.__name__ = "TruthValue"
_MplsTunnelIsIf_Object = MibTableColumn
mplsTunnelIsIf = _MplsTunnelIsIf_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 7),
    _MplsTunnelIsIf_Type()
)
mplsTunnelIsIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIsIf.setStatus("current")


class _MplsTunnelIfIndex_Type(InterfaceIndexOrZero):
    """Custom type mplsTunnelIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_MplsTunnelIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_MplsTunnelIfIndex_Object = MibTableColumn
mplsTunnelIfIndex = _MplsTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 8),
    _MplsTunnelIfIndex_Type()
)
mplsTunnelIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIfIndex.setStatus("current")
_MplsTunnelOwner_Type = MplsOwner
_MplsTunnelOwner_Object = MibTableColumn
mplsTunnelOwner = _MplsTunnelOwner_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 9),
    _MplsTunnelOwner_Type()
)
mplsTunnelOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelOwner.setStatus("current")


class _MplsTunnelRole_Type(Integer32):
    """Custom type mplsTunnelRole based on Integer32"""
    defaultValue = 1

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
        *(("head", 1),
          ("transit", 2),
          ("tail", 3),
          ("headTail", 4))
    )


_MplsTunnelRole_Type.__name__ = "Integer32"
_MplsTunnelRole_Object = MibTableColumn
mplsTunnelRole = _MplsTunnelRole_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 10),
    _MplsTunnelRole_Type()
)
mplsTunnelRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelRole.setStatus("current")


class _MplsTunnelXCPointer_Type(RowPointer):
    """Custom type mplsTunnelXCPointer based on RowPointer"""
    defaultValue = (0, 0)


_MplsTunnelXCPointer_Type.__name__ = "RowPointer"
_MplsTunnelXCPointer_Object = MibTableColumn
mplsTunnelXCPointer = _MplsTunnelXCPointer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 11),
    _MplsTunnelXCPointer_Type()
)
mplsTunnelXCPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelXCPointer.setStatus("current")


class _MplsTunnelSignallingProto_Type(Integer32):
    """Custom type mplsTunnelSignallingProto based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("rsvp", 2),
          ("crldp", 3),
          ("other", 4))
    )


_MplsTunnelSignallingProto_Type.__name__ = "Integer32"
_MplsTunnelSignallingProto_Object = MibTableColumn
mplsTunnelSignallingProto = _MplsTunnelSignallingProto_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 12),
    _MplsTunnelSignallingProto_Type()
)
mplsTunnelSignallingProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSignallingProto.setStatus("current")


class _MplsTunnelSetupPrio_Type(Integer32):
    """Custom type mplsTunnelSetupPrio based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsTunnelSetupPrio_Type.__name__ = "Integer32"
_MplsTunnelSetupPrio_Object = MibTableColumn
mplsTunnelSetupPrio = _MplsTunnelSetupPrio_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 13),
    _MplsTunnelSetupPrio_Type()
)
mplsTunnelSetupPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSetupPrio.setStatus("current")


class _MplsTunnelHoldingPrio_Type(Integer32):
    """Custom type mplsTunnelHoldingPrio based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsTunnelHoldingPrio_Type.__name__ = "Integer32"
_MplsTunnelHoldingPrio_Object = MibTableColumn
mplsTunnelHoldingPrio = _MplsTunnelHoldingPrio_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 14),
    _MplsTunnelHoldingPrio_Type()
)
mplsTunnelHoldingPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHoldingPrio.setStatus("current")


class _MplsTunnelSessionAttributes_Type(Bits):
    """Custom type mplsTunnelSessionAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("fastReroute", 0),
          ("mergingPermitted", 1),
          ("isPersistent", 2),
          ("isPinned", 3),
          ("recordRoute", 4),
          ("reserved5", 5),
          ("bandwidthProtect", 6),
          ("nodeProtect", 7))
    )

_MplsTunnelSessionAttributes_Type.__name__ = "Bits"
_MplsTunnelSessionAttributes_Object = MibTableColumn
mplsTunnelSessionAttributes = _MplsTunnelSessionAttributes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 15),
    _MplsTunnelSessionAttributes_Type()
)
mplsTunnelSessionAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSessionAttributes.setStatus("current")


class _MplsTunnelLocalProtectInUse_Type(TruthValue):
    """Custom type mplsTunnelLocalProtectInUse based on TruthValue"""
    defaultValue = 2


_MplsTunnelLocalProtectInUse_Type.__name__ = "TruthValue"
_MplsTunnelLocalProtectInUse_Object = MibTableColumn
mplsTunnelLocalProtectInUse = _MplsTunnelLocalProtectInUse_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 16),
    _MplsTunnelLocalProtectInUse_Type()
)
mplsTunnelLocalProtectInUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelLocalProtectInUse.setStatus("current")
_MplsTunnelResourcePointer_Type = RowPointer
_MplsTunnelResourcePointer_Object = MibTableColumn
mplsTunnelResourcePointer = _MplsTunnelResourcePointer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 17),
    _MplsTunnelResourcePointer_Type()
)
mplsTunnelResourcePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourcePointer.setStatus("current")


class _MplsTunnelPrimaryInstance_Type(MplsTunnelInstanceIndex):
    """Custom type mplsTunnelPrimaryInstance based on MplsTunnelInstanceIndex"""
    defaultValue = 0


_MplsTunnelPrimaryInstance_Type.__name__ = "MplsTunnelInstanceIndex"
_MplsTunnelPrimaryInstance_Object = MibTableColumn
mplsTunnelPrimaryInstance = _MplsTunnelPrimaryInstance_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 18),
    _MplsTunnelPrimaryInstance_Type()
)
mplsTunnelPrimaryInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPrimaryInstance.setStatus("current")


class _MplsTunnelInstancePriority_Type(Unsigned32):
    """Custom type mplsTunnelInstancePriority based on Unsigned32"""
    defaultValue = 0


_MplsTunnelInstancePriority_Type.__name__ = "Unsigned32"
_MplsTunnelInstancePriority_Object = MibTableColumn
mplsTunnelInstancePriority = _MplsTunnelInstancePriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 19),
    _MplsTunnelInstancePriority_Type()
)
mplsTunnelInstancePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelInstancePriority.setStatus("current")


class _MplsTunnelHopTableIndex_Type(MplsPathIndexOrZero):
    """Custom type mplsTunnelHopTableIndex based on MplsPathIndexOrZero"""
    defaultValue = 0


_MplsTunnelHopTableIndex_Type.__name__ = "MplsPathIndexOrZero"
_MplsTunnelHopTableIndex_Object = MibTableColumn
mplsTunnelHopTableIndex = _MplsTunnelHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 20),
    _MplsTunnelHopTableIndex_Type()
)
mplsTunnelHopTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopTableIndex.setStatus("current")


class _MplsTunnelPathInUse_Type(MplsPathIndexOrZero):
    """Custom type mplsTunnelPathInUse based on MplsPathIndexOrZero"""
    defaultValue = 0


_MplsTunnelPathInUse_Type.__name__ = "MplsPathIndexOrZero"
_MplsTunnelPathInUse_Object = MibTableColumn
mplsTunnelPathInUse = _MplsTunnelPathInUse_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 21),
    _MplsTunnelPathInUse_Type()
)
mplsTunnelPathInUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelPathInUse.setStatus("current")


class _MplsTunnelARHopTableIndex_Type(MplsPathIndexOrZero):
    """Custom type mplsTunnelARHopTableIndex based on MplsPathIndexOrZero"""
    defaultValue = 0


_MplsTunnelARHopTableIndex_Type.__name__ = "MplsPathIndexOrZero"
_MplsTunnelARHopTableIndex_Object = MibTableColumn
mplsTunnelARHopTableIndex = _MplsTunnelARHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 22),
    _MplsTunnelARHopTableIndex_Type()
)
mplsTunnelARHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopTableIndex.setStatus("current")


class _MplsTunnelCHopTableIndex_Type(MplsPathIndexOrZero):
    """Custom type mplsTunnelCHopTableIndex based on MplsPathIndexOrZero"""
    defaultValue = 0


_MplsTunnelCHopTableIndex_Type.__name__ = "MplsPathIndexOrZero"
_MplsTunnelCHopTableIndex_Object = MibTableColumn
mplsTunnelCHopTableIndex = _MplsTunnelCHopTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 23),
    _MplsTunnelCHopTableIndex_Type()
)
mplsTunnelCHopTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopTableIndex.setStatus("current")


class _MplsTunnelIncludeAnyAffinity_Type(MplsTunnelAffinity):
    """Custom type mplsTunnelIncludeAnyAffinity based on MplsTunnelAffinity"""
    defaultValue = 0


_MplsTunnelIncludeAnyAffinity_Type.__name__ = "MplsTunnelAffinity"
_MplsTunnelIncludeAnyAffinity_Object = MibTableColumn
mplsTunnelIncludeAnyAffinity = _MplsTunnelIncludeAnyAffinity_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 24),
    _MplsTunnelIncludeAnyAffinity_Type()
)
mplsTunnelIncludeAnyAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIncludeAnyAffinity.setStatus("current")


class _MplsTunnelIncludeAllAffinity_Type(MplsTunnelAffinity):
    """Custom type mplsTunnelIncludeAllAffinity based on MplsTunnelAffinity"""
    defaultValue = 0


_MplsTunnelIncludeAllAffinity_Type.__name__ = "MplsTunnelAffinity"
_MplsTunnelIncludeAllAffinity_Object = MibTableColumn
mplsTunnelIncludeAllAffinity = _MplsTunnelIncludeAllAffinity_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 25),
    _MplsTunnelIncludeAllAffinity_Type()
)
mplsTunnelIncludeAllAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIncludeAllAffinity.setStatus("current")


class _MplsTunnelExcludeAnyAffinity_Type(MplsTunnelAffinity):
    """Custom type mplsTunnelExcludeAnyAffinity based on MplsTunnelAffinity"""
    defaultValue = 0


_MplsTunnelExcludeAnyAffinity_Type.__name__ = "MplsTunnelAffinity"
_MplsTunnelExcludeAnyAffinity_Object = MibTableColumn
mplsTunnelExcludeAnyAffinity = _MplsTunnelExcludeAnyAffinity_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 26),
    _MplsTunnelExcludeAnyAffinity_Type()
)
mplsTunnelExcludeAnyAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExcludeAnyAffinity.setStatus("current")


class _MplsTunnelTotalUpTime_Type(TimeTicks):
    """Custom type mplsTunnelTotalUpTime based on TimeTicks"""
    defaultValue = 0


_MplsTunnelTotalUpTime_Type.__name__ = "TimeTicks"
_MplsTunnelTotalUpTime_Object = MibTableColumn
mplsTunnelTotalUpTime = _MplsTunnelTotalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 27),
    _MplsTunnelTotalUpTime_Type()
)
mplsTunnelTotalUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelTotalUpTime.setStatus("current")


class _MplsTunnelInstanceUpTime_Type(TimeTicks):
    """Custom type mplsTunnelInstanceUpTime based on TimeTicks"""
    defaultValue = 0


_MplsTunnelInstanceUpTime_Type.__name__ = "TimeTicks"
_MplsTunnelInstanceUpTime_Object = MibTableColumn
mplsTunnelInstanceUpTime = _MplsTunnelInstanceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 28),
    _MplsTunnelInstanceUpTime_Type()
)
mplsTunnelInstanceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelInstanceUpTime.setStatus("current")
_MplsTunnelPrimaryUpTime_Type = TimeTicks
_MplsTunnelPrimaryUpTime_Object = MibTableColumn
mplsTunnelPrimaryUpTime = _MplsTunnelPrimaryUpTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 29),
    _MplsTunnelPrimaryUpTime_Type()
)
mplsTunnelPrimaryUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPrimaryUpTime.setStatus("current")
_MplsTunnelPathChanges_Type = Counter32
_MplsTunnelPathChanges_Object = MibTableColumn
mplsTunnelPathChanges = _MplsTunnelPathChanges_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 30),
    _MplsTunnelPathChanges_Type()
)
mplsTunnelPathChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPathChanges.setStatus("current")
_MplsTunnelLastPathChange_Type = TimeTicks
_MplsTunnelLastPathChange_Object = MibTableColumn
mplsTunnelLastPathChange = _MplsTunnelLastPathChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 31),
    _MplsTunnelLastPathChange_Type()
)
mplsTunnelLastPathChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelLastPathChange.setStatus("current")
_MplsTunnelCreationTime_Type = TimeStamp
_MplsTunnelCreationTime_Object = MibTableColumn
mplsTunnelCreationTime = _MplsTunnelCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 32),
    _MplsTunnelCreationTime_Type()
)
mplsTunnelCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCreationTime.setStatus("current")
_MplsTunnelStateTransitions_Type = Counter32
_MplsTunnelStateTransitions_Object = MibTableColumn
mplsTunnelStateTransitions = _MplsTunnelStateTransitions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 33),
    _MplsTunnelStateTransitions_Type()
)
mplsTunnelStateTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelStateTransitions.setStatus("current")


class _MplsTunnelAdminStatus_Type(Integer32):
    """Custom type mplsTunnelAdminStatus based on Integer32"""
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


_MplsTunnelAdminStatus_Type.__name__ = "Integer32"
_MplsTunnelAdminStatus_Object = MibTableColumn
mplsTunnelAdminStatus = _MplsTunnelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 34),
    _MplsTunnelAdminStatus_Type()
)
mplsTunnelAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelAdminStatus.setStatus("current")


class _MplsTunnelOperStatus_Type(Integer32):
    """Custom type mplsTunnelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_MplsTunnelOperStatus_Type.__name__ = "Integer32"
_MplsTunnelOperStatus_Object = MibTableColumn
mplsTunnelOperStatus = _MplsTunnelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 35),
    _MplsTunnelOperStatus_Type()
)
mplsTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelOperStatus.setStatus("current")
_MplsTunnelRowStatus_Type = RowStatus
_MplsTunnelRowStatus_Object = MibTableColumn
mplsTunnelRowStatus = _MplsTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 36),
    _MplsTunnelRowStatus_Type()
)
mplsTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelRowStatus.setStatus("current")


class _MplsTunnelStorageType_Type(StorageType):
    """Custom type mplsTunnelStorageType based on StorageType"""
    defaultValue = 2


_MplsTunnelStorageType_Type.__name__ = "StorageType"
_MplsTunnelStorageType_Object = MibTableColumn
mplsTunnelStorageType = _MplsTunnelStorageType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 37),
    _MplsTunnelStorageType_Type()
)
mplsTunnelStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelStorageType.setStatus("current")


class _MplsTunnelUnnumIf_Type(TruthValue):
    """Custom type mplsTunnelUnnumIf based on TruthValue"""
    defaultValue = 2


_MplsTunnelUnnumIf_Type.__name__ = "TruthValue"
_MplsTunnelUnnumIf_Object = MibTableColumn
mplsTunnelUnnumIf = _MplsTunnelUnnumIf_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 38),
    _MplsTunnelUnnumIf_Type()
)
mplsTunnelUnnumIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUnnumIf.setStatus("current")


class _MplsTunnelAttributes_Type(Bits):
    """Custom type mplsTunnelAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("reserved0", 0),
          ("reserved1", 1),
          ("reserved2", 2),
          ("reserved3", 3),
          ("reserved4", 4),
          ("labelRecordingDesired", 5))
    )

_MplsTunnelAttributes_Type.__name__ = "Bits"
_MplsTunnelAttributes_Object = MibTableColumn
mplsTunnelAttributes = _MplsTunnelAttributes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 39),
    _MplsTunnelAttributes_Type()
)
mplsTunnelAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelAttributes.setStatus("current")


class _MplsTunnelLSPEncoding_Type(Integer32):
    """Custom type mplsTunnelLSPEncoding based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              7,
              8,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("notInUse", 0),
          ("tunnelLspPacket", 1),
          ("tunnelLspEthernet", 2),
          ("tunnelLspAnsiEtsiPdh", 3),
          ("tunnelLspSdhSonet", 5),
          ("tunnelLspDigitalWrapper", 7),
          ("tunnelLspLambda", 8),
          ("tunnelLspFiber", 9),
          ("tunnelLspFiberChannel", 11))
    )


_MplsTunnelLSPEncoding_Type.__name__ = "Integer32"
_MplsTunnelLSPEncoding_Object = MibTableColumn
mplsTunnelLSPEncoding = _MplsTunnelLSPEncoding_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 40),
    _MplsTunnelLSPEncoding_Type()
)
mplsTunnelLSPEncoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelLSPEncoding.setStatus("current")


class _MplsTunnelSwitchingType_Type(Unsigned32):
    """Custom type mplsTunnelSwitchingType based on Unsigned32"""
    defaultValue = 0


_MplsTunnelSwitchingType_Type.__name__ = "Unsigned32"
_MplsTunnelSwitchingType_Object = MibTableColumn
mplsTunnelSwitchingType = _MplsTunnelSwitchingType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 41),
    _MplsTunnelSwitchingType_Type()
)
mplsTunnelSwitchingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSwitchingType.setStatus("current")


class _MplsTunnelLinkProtection_Type(Bits):
    """Custom type mplsTunnelLinkProtection based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("extraTraffic", 0),
          ("unprotected", 1),
          ("shared", 2),
          ("dedicatedOneToOne", 3),
          ("dedicatedOnePlusOne", 4),
          ("enhanced", 5))
    )

_MplsTunnelLinkProtection_Type.__name__ = "Bits"
_MplsTunnelLinkProtection_Object = MibTableColumn
mplsTunnelLinkProtection = _MplsTunnelLinkProtection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 42),
    _MplsTunnelLinkProtection_Type()
)
mplsTunnelLinkProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelLinkProtection.setStatus("current")


class _MplsTunnelGPid_Type(Integer32):
    """Custom type mplsTunnelGPid based on Integer32"""
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
              56)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ds1SF", 1),
          ("ds1ESF", 2),
          ("ds3M23", 3),
          ("ds3Cbit", 4),
          ("asyncE4", 5),
          ("asyncDS3", 6),
          ("asyncE3", 7),
          ("bitSyncE3", 8),
          ("byteSyncE3", 9),
          ("asyncDS2", 10),
          ("bitSyncDS2", 11),
          ("byteSyncDS2", 12),
          ("asyncE1", 13),
          ("byteSyncE1", 14),
          ("byteSync31DS0", 15),
          ("asyncDS1", 16),
          ("bitSyncDS1", 17),
          ("byteSyncDS1", 18),
          ("vcByteSyncDS2", 19),
          ("vcAsyncE1", 20),
          ("vcByteSyncE1", 21),
          ("ds1SFAsync", 22),
          ("ds1ESFAsync", 23),
          ("ds3M23Async", 24),
          ("ds3CbitAsync", 25),
          ("vt", 26),
          ("sts", 27),
          ("pos16CRC", 28),
          ("pos32CRC", 29),
          ("posScrambling16CRC", 30),
          ("posScrambling32CRC", 31),
          ("atmMapping", 32),
          ("ethernet", 33),
          ("sdh", 34),
          ("sonet", 35),
          ("digitalWrapper", 36),
          ("lambda", 37),
          ("etsiPdh", 38),
          ("ansiPdh", 39),
          ("laps", 40),
          ("fddi", 41),
          ("dqdb", 42),
          ("fiberch3", 43),
          ("hdlc", 44),
          ("etherV2di", 45),
          ("ether8023", 46),
          ("etherGfpSonet", 56))
    )


_MplsTunnelGPid_Type.__name__ = "Integer32"
_MplsTunnelGPid_Object = MibTableColumn
mplsTunnelGPid = _MplsTunnelGPid_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 43),
    _MplsTunnelGPid_Type()
)
mplsTunnelGPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelGPid.setStatus("current")


class _MplsTunnelSecondary_Type(TruthValue):
    """Custom type mplsTunnelSecondary based on TruthValue"""
    defaultValue = 2


_MplsTunnelSecondary_Type.__name__ = "TruthValue"
_MplsTunnelSecondary_Object = MibTableColumn
mplsTunnelSecondary = _MplsTunnelSecondary_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 44),
    _MplsTunnelSecondary_Type()
)
mplsTunnelSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSecondary.setStatus("current")


class _MplsTunnelDirection_Type(Integer32):
    """Custom type mplsTunnelDirection based on Integer32"""
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
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("out", 0),
          ("outbidir", 1),
          ("in", 2),
          ("hwbidir", 3),
          ("inbidir", 4),
          ("transuni", 5),
          ("transbi", 6),
          ("transbih", 7))
    )


_MplsTunnelDirection_Type.__name__ = "Integer32"
_MplsTunnelDirection_Object = MibTableColumn
mplsTunnelDirection = _MplsTunnelDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 45),
    _MplsTunnelDirection_Type()
)
mplsTunnelDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelDirection.setStatus("current")


class _MplsTunnelPathComp_Type(Integer32):
    """Custom type mplsTunnelPathComp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamicFull", 1),
          ("explicit", 2),
          ("dynamicPartial", 3))
    )


_MplsTunnelPathComp_Type.__name__ = "Integer32"
_MplsTunnelPathComp_Object = MibTableColumn
mplsTunnelPathComp = _MplsTunnelPathComp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 46),
    _MplsTunnelPathComp_Type()
)
mplsTunnelPathComp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelPathComp.setStatus("current")
_MplsTunnelUpNotRecip_Type = InetAddress
_MplsTunnelUpNotRecip_Object = MibTableColumn
mplsTunnelUpNotRecip = _MplsTunnelUpNotRecip_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 47),
    _MplsTunnelUpNotRecip_Type()
)
mplsTunnelUpNotRecip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUpNotRecip.setStatus("current")
_MplsTunnelDownNotRecip_Type = InetAddress
_MplsTunnelDownNotRecip_Object = MibTableColumn
mplsTunnelDownNotRecip = _MplsTunnelDownNotRecip_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 48),
    _MplsTunnelDownNotRecip_Type()
)
mplsTunnelDownNotRecip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelDownNotRecip.setStatus("current")


class _MplsTunnelAdminStatusFlags_Type(Bits):
    """Custom type mplsTunnelAdminStatusFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("delInProgress", 0),
          ("adminDown", 1),
          ("testing", 2),
          ("reserved3", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved6", 6),
          ("reserved7", 7),
          ("reserved8", 8),
          ("reserved9", 9),
          ("reserved10", 10),
          ("reserved11", 11),
          ("reserved12", 12),
          ("reserved13", 13),
          ("reserved14", 14),
          ("reserved15", 15),
          ("reserved16", 16),
          ("reserved17", 17),
          ("reserved18", 18),
          ("reserved19", 19),
          ("reserved20", 20),
          ("reserved21", 21),
          ("reserved22", 22),
          ("reserved23", 23),
          ("reserved24", 24),
          ("reserved25", 25),
          ("reserved26", 26),
          ("reserved27", 27),
          ("reserved28", 28),
          ("reserved29", 29),
          ("reserved30", 30),
          ("reflect", 31))
    )

_MplsTunnelAdminStatusFlags_Type.__name__ = "Bits"
_MplsTunnelAdminStatusFlags_Object = MibTableColumn
mplsTunnelAdminStatusFlags = _MplsTunnelAdminStatusFlags_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 49),
    _MplsTunnelAdminStatusFlags_Type()
)
mplsTunnelAdminStatusFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelAdminStatusFlags.setStatus("current")
_MplsTunnelExtraParamsPtr_Type = RowPointer
_MplsTunnelExtraParamsPtr_Object = MibTableColumn
mplsTunnelExtraParamsPtr = _MplsTunnelExtraParamsPtr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 50),
    _MplsTunnelExtraParamsPtr_Type()
)
mplsTunnelExtraParamsPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtraParamsPtr.setStatus("current")


class _MplsTunnelUseEgressLabel_Type(TruthValue):
    """Custom type mplsTunnelUseEgressLabel based on TruthValue"""
    defaultValue = 2


_MplsTunnelUseEgressLabel_Type.__name__ = "TruthValue"
_MplsTunnelUseEgressLabel_Object = MibTableColumn
mplsTunnelUseEgressLabel = _MplsTunnelUseEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 51),
    _MplsTunnelUseEgressLabel_Type()
)
mplsTunnelUseEgressLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUseEgressLabel.setStatus("current")
_MplsTunnelEgressLabel_Type = MplsGeneralizedLabel
_MplsTunnelEgressLabel_Object = MibTableColumn
mplsTunnelEgressLabel = _MplsTunnelEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 52),
    _MplsTunnelEgressLabel_Type()
)
mplsTunnelEgressLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelEgressLabel.setStatus("current")
_MplsTunnelEgressLabelType_Type = MplsGeneralizedLabelType
_MplsTunnelEgressLabelType_Object = MibTableColumn
mplsTunnelEgressLabelType = _MplsTunnelEgressLabelType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 53),
    _MplsTunnelEgressLabelType_Type()
)
mplsTunnelEgressLabelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelEgressLabelType.setStatus("current")


class _MplsTunnelOmitEROIfOneHop_Type(TruthValue):
    """Custom type mplsTunnelOmitEROIfOneHop based on TruthValue"""
    defaultValue = 2


_MplsTunnelOmitEROIfOneHop_Type.__name__ = "TruthValue"
_MplsTunnelOmitEROIfOneHop_Object = MibTableColumn
mplsTunnelOmitEROIfOneHop = _MplsTunnelOmitEROIfOneHop_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 54),
    _MplsTunnelOmitEROIfOneHop_Type()
)
mplsTunnelOmitEROIfOneHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelOmitEROIfOneHop.setStatus("current")
_MplsTunnelPrivateData_Type = MplsTunnelPrivateDataSyntax
_MplsTunnelPrivateData_Object = MibTableColumn
mplsTunnelPrivateData = _MplsTunnelPrivateData_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 55),
    _MplsTunnelPrivateData_Type()
)
mplsTunnelPrivateData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelPrivateData.setStatus("current")


class _MplsTunnelSrcTNAAddressType_Type(Integer32):
    """Custom type mplsTunnelSrcTNAAddressType based on Integer32"""
    defaultValue = 0

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
          ("ipv4", 1),
          ("ipv6", 2),
          ("nsap", 3))
    )


_MplsTunnelSrcTNAAddressType_Type.__name__ = "Integer32"
_MplsTunnelSrcTNAAddressType_Object = MibTableColumn
mplsTunnelSrcTNAAddressType = _MplsTunnelSrcTNAAddressType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 56),
    _MplsTunnelSrcTNAAddressType_Type()
)
mplsTunnelSrcTNAAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSrcTNAAddressType.setStatus("current")
_MplsTunnelSrcTNAAddress_Type = MplsTunnelTNAAddress
_MplsTunnelSrcTNAAddress_Object = MibTableColumn
mplsTunnelSrcTNAAddress = _MplsTunnelSrcTNAAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 57),
    _MplsTunnelSrcTNAAddress_Type()
)
mplsTunnelSrcTNAAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSrcTNAAddress.setStatus("current")


class _MplsTunnelDestTNAAddressType_Type(Integer32):
    """Custom type mplsTunnelDestTNAAddressType based on Integer32"""
    defaultValue = 0

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
          ("ipv4", 1),
          ("ipv6", 2),
          ("nsap", 3))
    )


_MplsTunnelDestTNAAddressType_Type.__name__ = "Integer32"
_MplsTunnelDestTNAAddressType_Object = MibTableColumn
mplsTunnelDestTNAAddressType = _MplsTunnelDestTNAAddressType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 58),
    _MplsTunnelDestTNAAddressType_Type()
)
mplsTunnelDestTNAAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelDestTNAAddressType.setStatus("current")
_MplsTunnelDestTNAAddress_Type = MplsTunnelTNAAddress
_MplsTunnelDestTNAAddress_Object = MibTableColumn
mplsTunnelDestTNAAddress = _MplsTunnelDestTNAAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 59),
    _MplsTunnelDestTNAAddress_Type()
)
mplsTunnelDestTNAAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelDestTNAAddress.setStatus("current")


class _MplsTunnelEndToEndRerouting_Type(TruthValue):
    """Custom type mplsTunnelEndToEndRerouting based on TruthValue"""
    defaultValue = 2


_MplsTunnelEndToEndRerouting_Type.__name__ = "TruthValue"
_MplsTunnelEndToEndRerouting_Object = MibTableColumn
mplsTunnelEndToEndRerouting = _MplsTunnelEndToEndRerouting_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 60),
    _MplsTunnelEndToEndRerouting_Type()
)
mplsTunnelEndToEndRerouting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelEndToEndRerouting.setStatus("current")


class _MplsTunnelIsUni_Type(TruthValue):
    """Custom type mplsTunnelIsUni based on TruthValue"""
    defaultValue = 2


_MplsTunnelIsUni_Type.__name__ = "TruthValue"
_MplsTunnelIsUni_Object = MibTableColumn
mplsTunnelIsUni = _MplsTunnelIsUni_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 62),
    _MplsTunnelIsUni_Type()
)
mplsTunnelIsUni.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIsUni.setStatus("current")
_MplsTunnelUniServiceLevel_Type = Integer32
_MplsTunnelUniServiceLevel_Object = MibTableColumn
mplsTunnelUniServiceLevel = _MplsTunnelUniServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 63),
    _MplsTunnelUniServiceLevel_Type()
)
mplsTunnelUniServiceLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUniServiceLevel.setStatus("current")
_MplsTunnelUniEgressLabel_Type = MplsGeneralizedLabel
_MplsTunnelUniEgressLabel_Object = MibTableColumn
mplsTunnelUniEgressLabel = _MplsTunnelUniEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 64),
    _MplsTunnelUniEgressLabel_Type()
)
mplsTunnelUniEgressLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUniEgressLabel.setStatus("current")
_MplsTunnelUniEgressLabelType_Type = MplsGeneralizedLabelType
_MplsTunnelUniEgressLabelType_Object = MibTableColumn
mplsTunnelUniEgressLabelType = _MplsTunnelUniEgressLabelType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 65),
    _MplsTunnelUniEgressLabelType_Type()
)
mplsTunnelUniEgressLabelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUniEgressLabelType.setStatus("current")
_MplsTunnelUniEgressLabelPort_Type = Unsigned32
_MplsTunnelUniEgressLabelPort_Object = MibTableColumn
mplsTunnelUniEgressLabelPort = _MplsTunnelUniEgressLabelPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 66),
    _MplsTunnelUniEgressLabelPort_Type()
)
mplsTunnelUniEgressLabelPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUniEgressLabelPort.setStatus("current")
_MplsTunnelUniRvsEgressLabel_Type = MplsGeneralizedLabel
_MplsTunnelUniRvsEgressLabel_Object = MibTableColumn
mplsTunnelUniRvsEgressLabel = _MplsTunnelUniRvsEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 67),
    _MplsTunnelUniRvsEgressLabel_Type()
)
mplsTunnelUniRvsEgressLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUniRvsEgressLabel.setStatus("current")
_MplsTunnelUniRvsEgressLabelType_Type = MplsGeneralizedLabelType
_MplsTunnelUniRvsEgressLabelType_Object = MibTableColumn
mplsTunnelUniRvsEgressLabelType = _MplsTunnelUniRvsEgressLabelType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 68),
    _MplsTunnelUniRvsEgressLabelType_Type()
)
mplsTunnelUniRvsEgressLabelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUniRvsEgressLabelType.setStatus("current")
_MplsTunnelUniRvsEgressLabelPort_Type = Unsigned32
_MplsTunnelUniRvsEgressLabelPort_Object = MibTableColumn
mplsTunnelUniRvsEgressLabelPort = _MplsTunnelUniRvsEgressLabelPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 69),
    _MplsTunnelUniRvsEgressLabelPort_Type()
)
mplsTunnelUniRvsEgressLabelPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUniRvsEgressLabelPort.setStatus("current")


class _MplsTunnelDeletionMode_Type(Integer32):
    """Custom type mplsTunnelDeletionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forced", 1),
          ("graceful", 2))
    )


_MplsTunnelDeletionMode_Type.__name__ = "Integer32"
_MplsTunnelDeletionMode_Object = MibTableColumn
mplsTunnelDeletionMode = _MplsTunnelDeletionMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 70),
    _MplsTunnelDeletionMode_Type()
)
mplsTunnelDeletionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelDeletionMode.setStatus("current")


class _MplsTunnelUniDiversityListIndex_Type(Integer32):
    """Custom type mplsTunnelUniDiversityListIndex based on Integer32"""
    defaultValue = 0


_MplsTunnelUniDiversityListIndex_Type.__name__ = "Integer32"
_MplsTunnelUniDiversityListIndex_Object = MibTableColumn
mplsTunnelUniDiversityListIndex = _MplsTunnelUniDiversityListIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 71),
    _MplsTunnelUniDiversityListIndex_Type()
)
mplsTunnelUniDiversityListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUniDiversityListIndex.setStatus("current")
_MplsTunnelDiffServIndex_Type = Integer32
_MplsTunnelDiffServIndex_Object = MibTableColumn
mplsTunnelDiffServIndex = _MplsTunnelDiffServIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 72),
    _MplsTunnelDiffServIndex_Type()
)
mplsTunnelDiffServIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelDiffServIndex.setStatus("current")
_MplsTunnelReversePrivateData_Type = MplsTunnelPrivateDataSyntax
_MplsTunnelReversePrivateData_Object = MibTableColumn
mplsTunnelReversePrivateData = _MplsTunnelReversePrivateData_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 73),
    _MplsTunnelReversePrivateData_Type()
)
mplsTunnelReversePrivateData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelReversePrivateData.setStatus("current")


class _MplsTunnelFastRerouteMode_Type(Integer32):
    """Custom type mplsTunnelFastRerouteMode based on Integer32"""
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
        *(("noFastReroute", 0),
          ("detourFastReroute", 1),
          ("facilityFastReroute", 2))
    )


_MplsTunnelFastRerouteMode_Type.__name__ = "Integer32"
_MplsTunnelFastRerouteMode_Object = MibTableColumn
mplsTunnelFastRerouteMode = _MplsTunnelFastRerouteMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 74),
    _MplsTunnelFastRerouteMode_Type()
)
mplsTunnelFastRerouteMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelFastRerouteMode.setStatus("current")


class _MplsTunnelBackupSetupPrio_Type(Integer32):
    """Custom type mplsTunnelBackupSetupPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsTunnelBackupSetupPrio_Type.__name__ = "Integer32"
_MplsTunnelBackupSetupPrio_Object = MibTableColumn
mplsTunnelBackupSetupPrio = _MplsTunnelBackupSetupPrio_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 75),
    _MplsTunnelBackupSetupPrio_Type()
)
mplsTunnelBackupSetupPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelBackupSetupPrio.setStatus("current")


class _MplsTunnelBackupHoldingPriority_Type(Integer32):
    """Custom type mplsTunnelBackupHoldingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsTunnelBackupHoldingPriority_Type.__name__ = "Integer32"
_MplsTunnelBackupHoldingPriority_Object = MibTableColumn
mplsTunnelBackupHoldingPriority = _MplsTunnelBackupHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 76),
    _MplsTunnelBackupHoldingPriority_Type()
)
mplsTunnelBackupHoldingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelBackupHoldingPriority.setStatus("current")


class _MplsTunnelBackupIncAny_Type(MplsTunnelAffinity):
    """Custom type mplsTunnelBackupIncAny based on MplsTunnelAffinity"""
    defaultValue = 0


_MplsTunnelBackupIncAny_Type.__name__ = "MplsTunnelAffinity"
_MplsTunnelBackupIncAny_Object = MibTableColumn
mplsTunnelBackupIncAny = _MplsTunnelBackupIncAny_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 77),
    _MplsTunnelBackupIncAny_Type()
)
mplsTunnelBackupIncAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelBackupIncAny.setStatus("current")


class _MplsTunnelBackupIncAll_Type(MplsTunnelAffinity):
    """Custom type mplsTunnelBackupIncAll based on MplsTunnelAffinity"""
    defaultValue = 0


_MplsTunnelBackupIncAll_Type.__name__ = "MplsTunnelAffinity"
_MplsTunnelBackupIncAll_Object = MibTableColumn
mplsTunnelBackupIncAll = _MplsTunnelBackupIncAll_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 78),
    _MplsTunnelBackupIncAll_Type()
)
mplsTunnelBackupIncAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelBackupIncAll.setStatus("current")


class _MplsTunnelBackupExcAny_Type(MplsTunnelAffinity):
    """Custom type mplsTunnelBackupExcAny based on MplsTunnelAffinity"""
    defaultValue = 0


_MplsTunnelBackupExcAny_Type.__name__ = "MplsTunnelAffinity"
_MplsTunnelBackupExcAny_Object = MibTableColumn
mplsTunnelBackupExcAny = _MplsTunnelBackupExcAny_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 79),
    _MplsTunnelBackupExcAny_Type()
)
mplsTunnelBackupExcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelBackupExcAny.setStatus("current")


class _MplsTunnelBackupBandwidth_Type(MplsBitRate):
    """Custom type mplsTunnelBackupBandwidth based on MplsBitRate"""
    defaultValue = 0


_MplsTunnelBackupBandwidth_Type.__name__ = "MplsBitRate"
_MplsTunnelBackupBandwidth_Object = MibTableColumn
mplsTunnelBackupBandwidth = _MplsTunnelBackupBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 80),
    _MplsTunnelBackupBandwidth_Type()
)
mplsTunnelBackupBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelBackupBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelBackupBandwidth.setUnits("1000s of bits per second")


class _MplsTunnelBackupMaxHops_Type(Unsigned32):
    """Custom type mplsTunnelBackupMaxHops based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsTunnelBackupMaxHops_Type.__name__ = "Unsigned32"
_MplsTunnelBackupMaxHops_Object = MibTableColumn
mplsTunnelBackupMaxHops = _MplsTunnelBackupMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 81),
    _MplsTunnelBackupMaxHops_Type()
)
mplsTunnelBackupMaxHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelBackupMaxHops.setStatus("current")


class _MplsTunnelIsSpc_Type(TruthValue):
    """Custom type mplsTunnelIsSpc based on TruthValue"""
    defaultValue = 2


_MplsTunnelIsSpc_Type.__name__ = "TruthValue"
_MplsTunnelIsSpc_Object = MibTableColumn
mplsTunnelIsSpc = _MplsTunnelIsSpc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 84),
    _MplsTunnelIsSpc_Type()
)
mplsTunnelIsSpc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIsSpc.setStatus("current")
_MplsTunnelUniIngressLabel_Type = MplsGeneralizedLabel
_MplsTunnelUniIngressLabel_Object = MibTableColumn
mplsTunnelUniIngressLabel = _MplsTunnelUniIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 85),
    _MplsTunnelUniIngressLabel_Type()
)
mplsTunnelUniIngressLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUniIngressLabel.setStatus("current")
_MplsTunnelUniIngressLabelType_Type = MplsGeneralizedLabelType
_MplsTunnelUniIngressLabelType_Object = MibTableColumn
mplsTunnelUniIngressLabelType = _MplsTunnelUniIngressLabelType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 86),
    _MplsTunnelUniIngressLabelType_Type()
)
mplsTunnelUniIngressLabelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUniIngressLabelType.setStatus("current")
_MplsTunnelUniIngressLabelPort_Type = Unsigned32
_MplsTunnelUniIngressLabelPort_Object = MibTableColumn
mplsTunnelUniIngressLabelPort = _MplsTunnelUniIngressLabelPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 87),
    _MplsTunnelUniIngressLabelPort_Type()
)
mplsTunnelUniIngressLabelPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUniIngressLabelPort.setStatus("current")
_MplsTunnelUniRvsIngrLabel_Type = MplsGeneralizedLabel
_MplsTunnelUniRvsIngrLabel_Object = MibTableColumn
mplsTunnelUniRvsIngrLabel = _MplsTunnelUniRvsIngrLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 88),
    _MplsTunnelUniRvsIngrLabel_Type()
)
mplsTunnelUniRvsIngrLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUniRvsIngrLabel.setStatus("current")
_MplsTunnelUniRvsIngrLabelType_Type = MplsGeneralizedLabelType
_MplsTunnelUniRvsIngrLabelType_Object = MibTableColumn
mplsTunnelUniRvsIngrLabelType = _MplsTunnelUniRvsIngrLabelType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 89),
    _MplsTunnelUniRvsIngrLabelType_Type()
)
mplsTunnelUniRvsIngrLabelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUniRvsIngrLabelType.setStatus("current")
_MplsTunnelUniRvsIngrLabelPort_Type = Unsigned32
_MplsTunnelUniRvsIngrLabelPort_Object = MibTableColumn
mplsTunnelUniRvsIngrLabelPort = _MplsTunnelUniRvsIngrLabelPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 90),
    _MplsTunnelUniRvsIngrLabelPort_Type()
)
mplsTunnelUniRvsIngrLabelPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUniRvsIngrLabelPort.setStatus("current")


class _MplsTunnelDiffServClassType_Type(Integer32):
    """Custom type mplsTunnelDiffServClassType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsTunnelDiffServClassType_Type.__name__ = "Integer32"
_MplsTunnelDiffServClassType_Object = MibTableColumn
mplsTunnelDiffServClassType = _MplsTunnelDiffServClassType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 91),
    _MplsTunnelDiffServClassType_Type()
)
mplsTunnelDiffServClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelDiffServClassType.setStatus("current")


class _MplsTunnelExtendedProtection_Type(TruthValue):
    """Custom type mplsTunnelExtendedProtection based on TruthValue"""
    defaultValue = 2


_MplsTunnelExtendedProtection_Type.__name__ = "TruthValue"
_MplsTunnelExtendedProtection_Object = MibTableColumn
mplsTunnelExtendedProtection = _MplsTunnelExtendedProtection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 92),
    _MplsTunnelExtendedProtection_Type()
)
mplsTunnelExtendedProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelExtendedProtection.setStatus("current")


class _MplsTunnelProtecting_Type(TruthValue):
    """Custom type mplsTunnelProtecting based on TruthValue"""
    defaultValue = 2


_MplsTunnelProtecting_Type.__name__ = "TruthValue"
_MplsTunnelProtecting_Object = MibTableColumn
mplsTunnelProtecting = _MplsTunnelProtecting_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 93),
    _MplsTunnelProtecting_Type()
)
mplsTunnelProtecting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelProtecting.setStatus("current")


class _MplsTunnelNotification_Type(TruthValue):
    """Custom type mplsTunnelNotification based on TruthValue"""
    defaultValue = 2


_MplsTunnelNotification_Type.__name__ = "TruthValue"
_MplsTunnelNotification_Object = MibTableColumn
mplsTunnelNotification = _MplsTunnelNotification_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 94),
    _MplsTunnelNotification_Type()
)
mplsTunnelNotification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelNotification.setStatus("current")


class _MplsTunnelLspProtection_Type(Unsigned32):
    """Custom type mplsTunnelLspProtection based on Unsigned32"""
    defaultValue = 0


_MplsTunnelLspProtection_Type.__name__ = "Unsigned32"
_MplsTunnelLspProtection_Object = MibTableColumn
mplsTunnelLspProtection = _MplsTunnelLspProtection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 95),
    _MplsTunnelLspProtection_Type()
)
mplsTunnelLspProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelLspProtection.setStatus("current")


class _MplsTunnelAssociatedLspId_Type(MplsTunnelInstanceIndex):
    """Custom type mplsTunnelAssociatedLspId based on MplsTunnelInstanceIndex"""
    defaultValue = 0


_MplsTunnelAssociatedLspId_Type.__name__ = "MplsTunnelInstanceIndex"
_MplsTunnelAssociatedLspId_Object = MibTableColumn
mplsTunnelAssociatedLspId = _MplsTunnelAssociatedLspId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 96),
    _MplsTunnelAssociatedLspId_Type()
)
mplsTunnelAssociatedLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelAssociatedLspId.setStatus("current")


class _MplsTunnelCallIdType_Type(Integer32):
    """Custom type mplsTunnelCallIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operatorSpecific", 1),
          ("globallyUnique", 2))
    )


_MplsTunnelCallIdType_Type.__name__ = "Integer32"
_MplsTunnelCallIdType_Object = MibTableColumn
mplsTunnelCallIdType = _MplsTunnelCallIdType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 97),
    _MplsTunnelCallIdType_Type()
)
mplsTunnelCallIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCallIdType.setStatus("current")


class _MplsTunnelCallId_Type(OctetString):
    """Custom type mplsTunnelCallId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MplsTunnelCallId_Type.__name__ = "OctetString"
_MplsTunnelCallId_Object = MibTableColumn
mplsTunnelCallId = _MplsTunnelCallId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 98),
    _MplsTunnelCallId_Type()
)
mplsTunnelCallId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCallId.setStatus("current")


class _MplsTunnelIsIpv6_Type(TruthValue):
    """Custom type mplsTunnelIsIpv6 based on TruthValue"""
    defaultValue = 2


_MplsTunnelIsIpv6_Type.__name__ = "TruthValue"
_MplsTunnelIsIpv6_Object = MibTableColumn
mplsTunnelIsIpv6 = _MplsTunnelIsIpv6_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 100),
    _MplsTunnelIsIpv6_Type()
)
mplsTunnelIsIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelIsIpv6.setStatus("current")


class _MplsTunnelUpNotRecipType_Type(InetAddressType):
    """Custom type mplsTunnelUpNotRecipType based on InetAddressType"""
    defaultValue = 0


_MplsTunnelUpNotRecipType_Type.__name__ = "InetAddressType"
_MplsTunnelUpNotRecipType_Object = MibTableColumn
mplsTunnelUpNotRecipType = _MplsTunnelUpNotRecipType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 101),
    _MplsTunnelUpNotRecipType_Type()
)
mplsTunnelUpNotRecipType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelUpNotRecipType.setStatus("current")


class _MplsTunnelDownNotRecipType_Type(InetAddressType):
    """Custom type mplsTunnelDownNotRecipType based on InetAddressType"""
    defaultValue = 0


_MplsTunnelDownNotRecipType_Type.__name__ = "InetAddressType"
_MplsTunnelDownNotRecipType_Object = MibTableColumn
mplsTunnelDownNotRecipType = _MplsTunnelDownNotRecipType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 102),
    _MplsTunnelDownNotRecipType_Type()
)
mplsTunnelDownNotRecipType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelDownNotRecipType.setStatus("current")
_MplsTunnelMtu_Type = Integer32
_MplsTunnelMtu_Object = MibTableColumn
mplsTunnelMtu = _MplsTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 103),
    _MplsTunnelMtu_Type()
)
mplsTunnelMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelMtu.setStatus("current")


class _MplsTunnelRebuildTimer_Type(TimeTicks):
    """Custom type mplsTunnelRebuildTimer based on TimeTicks"""
    defaultValue = 60


_MplsTunnelRebuildTimer_Type.__name__ = "TimeTicks"
_MplsTunnelRebuildTimer_Object = MibTableColumn
mplsTunnelRebuildTimer = _MplsTunnelRebuildTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 104),
    _MplsTunnelRebuildTimer_Type()
)
mplsTunnelRebuildTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelRebuildTimer.setStatus("current")


class _MplsTunnelOperStatusFlags_Type(Bits):
    """Custom type mplsTunnelOperStatusFlags based on Bits"""
    namedValues = NamedValues(
        *(("empty", 0),
          ("tunnelResignalling", 1),
          ("tunnelSuppressed", 2))
    )

_MplsTunnelOperStatusFlags_Type.__name__ = "Bits"
_MplsTunnelOperStatusFlags_Object = MibTableColumn
mplsTunnelOperStatusFlags = _MplsTunnelOperStatusFlags_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 105),
    _MplsTunnelOperStatusFlags_Type()
)
mplsTunnelOperStatusFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelOperStatusFlags.setStatus("current")
_MplsTunnelGuardedDest_Type = InetAddressIPv4
_MplsTunnelGuardedDest_Object = MibTableColumn
mplsTunnelGuardedDest = _MplsTunnelGuardedDest_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 106),
    _MplsTunnelGuardedDest_Type()
)
mplsTunnelGuardedDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelGuardedDest.setStatus("current")
_MplsTunnelMBBTimeOut_Type = Integer32
_MplsTunnelMBBTimeOut_Object = MibTableColumn
mplsTunnelMBBTimeOut = _MplsTunnelMBBTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 2, 1, 107),
    _MplsTunnelMBBTimeOut_Type()
)
mplsTunnelMBBTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelMBBTimeOut.setStatus("current")
_MplsTunnelHopIndexNextTable_Object = MibTable
mplsTunnelHopIndexNextTable = _MplsTunnelHopIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    mplsTunnelHopIndexNextTable.setStatus("current")
_MplsTunnelHopIndexNextEntry_Object = MibTableRow
mplsTunnelHopIndexNextEntry = _MplsTunnelHopIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 3, 1)
)
mplsTunnelHopIndexNextEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelHopIndexNextEntry.setStatus("current")


class _MplsTunnelHopIndexNextIndex_Type(Unsigned32):
    """Custom type mplsTunnelHopIndexNextIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsTunnelHopIndexNextIndex_Type.__name__ = "Unsigned32"
_MplsTunnelHopIndexNextIndex_Object = MibTableColumn
mplsTunnelHopIndexNextIndex = _MplsTunnelHopIndexNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 3, 1, 1),
    _MplsTunnelHopIndexNextIndex_Type()
)
mplsTunnelHopIndexNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelHopIndexNextIndex.setStatus("current")
_MplsTunnelHopTable_Object = MibTable
mplsTunnelHopTable = _MplsTunnelHopTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    mplsTunnelHopTable.setStatus("current")
_MplsTunnelHopEntry_Object = MibTableRow
mplsTunnelHopEntry = _MplsTunnelHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1)
)
mplsTunnelHopEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
    (0, "PRVT-MPLS-TE-MIB", "mplsTunnelHopListIndex"),
    (0, "PRVT-MPLS-TE-MIB", "mplsTunnelHopPathOptionIndex"),
    (0, "PRVT-MPLS-TE-MIB", "mplsTunnelHopIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelHopEntry.setStatus("current")
_MplsTunnelHopListIndex_Type = MplsPathIndex
_MplsTunnelHopListIndex_Object = MibTableColumn
mplsTunnelHopListIndex = _MplsTunnelHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 1),
    _MplsTunnelHopListIndex_Type()
)
mplsTunnelHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelHopListIndex.setStatus("current")
_MplsTunnelHopPathOptionIndex_Type = MplsPathIndex
_MplsTunnelHopPathOptionIndex_Object = MibTableColumn
mplsTunnelHopPathOptionIndex = _MplsTunnelHopPathOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 2),
    _MplsTunnelHopPathOptionIndex_Type()
)
mplsTunnelHopPathOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelHopPathOptionIndex.setStatus("current")
_MplsTunnelHopIndex_Type = MplsPathIndex
_MplsTunnelHopIndex_Object = MibTableColumn
mplsTunnelHopIndex = _MplsTunnelHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 3),
    _MplsTunnelHopIndex_Type()
)
mplsTunnelHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelHopIndex.setStatus("current")


class _MplsTunnelHopAddrType_Type(TeHopAddressType):
    """Custom type mplsTunnelHopAddrType based on TeHopAddressType"""
    defaultValue = 1


_MplsTunnelHopAddrType_Type.__name__ = "TeHopAddressType"
_MplsTunnelHopAddrType_Object = MibTableColumn
mplsTunnelHopAddrType = _MplsTunnelHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 4),
    _MplsTunnelHopAddrType_Type()
)
mplsTunnelHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopAddrType.setStatus("current")
_MplsTunnelHopIpAddr_Type = TeHopAddress
_MplsTunnelHopIpAddr_Object = MibTableColumn
mplsTunnelHopIpAddr = _MplsTunnelHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 5),
    _MplsTunnelHopIpAddr_Type()
)
mplsTunnelHopIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopIpAddr.setStatus("current")


class _MplsTunnelHopIpPrefixLen_Type(Unsigned32):
    """Custom type mplsTunnelHopIpPrefixLen based on Unsigned32"""
    defaultValue = 32


_MplsTunnelHopIpPrefixLen_Type.__name__ = "Unsigned32"
_MplsTunnelHopIpPrefixLen_Object = MibTableColumn
mplsTunnelHopIpPrefixLen = _MplsTunnelHopIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 6),
    _MplsTunnelHopIpPrefixLen_Type()
)
mplsTunnelHopIpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopIpPrefixLen.setStatus("current")
_MplsTunnelHopAsNumber_Type = TeHopAddressAS
_MplsTunnelHopAsNumber_Object = MibTableColumn
mplsTunnelHopAsNumber = _MplsTunnelHopAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 7),
    _MplsTunnelHopAsNumber_Type()
)
mplsTunnelHopAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopAsNumber.setStatus("current")
_MplsTunnelHopAddrUnnum_Type = TeHopAddressUnnum
_MplsTunnelHopAddrUnnum_Object = MibTableColumn
mplsTunnelHopAddrUnnum = _MplsTunnelHopAddrUnnum_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 8),
    _MplsTunnelHopAddrUnnum_Type()
)
mplsTunnelHopAddrUnnum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopAddrUnnum.setStatus("current")
_MplsTunnelHopLspId_Type = MplsLSPID
_MplsTunnelHopLspId_Object = MibTableColumn
mplsTunnelHopLspId = _MplsTunnelHopLspId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 9),
    _MplsTunnelHopLspId_Type()
)
mplsTunnelHopLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopLspId.setStatus("current")


class _MplsTunnelHopType_Type(Integer32):
    """Custom type mplsTunnelHopType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("loose", 2))
    )


_MplsTunnelHopType_Type.__name__ = "Integer32"
_MplsTunnelHopType_Object = MibTableColumn
mplsTunnelHopType = _MplsTunnelHopType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 10),
    _MplsTunnelHopType_Type()
)
mplsTunnelHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopType.setStatus("current")


class _MplsTunnelHopInclude_Type(TruthValue):
    """Custom type mplsTunnelHopInclude based on TruthValue"""
    defaultValue = 1


_MplsTunnelHopInclude_Type.__name__ = "TruthValue"
_MplsTunnelHopInclude_Object = MibTableColumn
mplsTunnelHopInclude = _MplsTunnelHopInclude_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 11),
    _MplsTunnelHopInclude_Type()
)
mplsTunnelHopInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopInclude.setStatus("current")
_MplsTunnelHopPathOptionName_Type = DisplayString
_MplsTunnelHopPathOptionName_Object = MibTableColumn
mplsTunnelHopPathOptionName = _MplsTunnelHopPathOptionName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 12),
    _MplsTunnelHopPathOptionName_Type()
)
mplsTunnelHopPathOptionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopPathOptionName.setStatus("current")


class _MplsTunnelHopEntryPathComp_Type(Integer32):
    """Custom type mplsTunnelHopEntryPathComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("explicit", 2))
    )


_MplsTunnelHopEntryPathComp_Type.__name__ = "Integer32"
_MplsTunnelHopEntryPathComp_Object = MibTableColumn
mplsTunnelHopEntryPathComp = _MplsTunnelHopEntryPathComp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 13),
    _MplsTunnelHopEntryPathComp_Type()
)
mplsTunnelHopEntryPathComp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopEntryPathComp.setStatus("current")
_MplsTunnelHopRowStatus_Type = RowStatus
_MplsTunnelHopRowStatus_Object = MibTableColumn
mplsTunnelHopRowStatus = _MplsTunnelHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 14),
    _MplsTunnelHopRowStatus_Type()
)
mplsTunnelHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopRowStatus.setStatus("current")


class _MplsTunnelHopStorageType_Type(StorageType):
    """Custom type mplsTunnelHopStorageType based on StorageType"""
    defaultValue = 2


_MplsTunnelHopStorageType_Type.__name__ = "StorageType"
_MplsTunnelHopStorageType_Object = MibTableColumn
mplsTunnelHopStorageType = _MplsTunnelHopStorageType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 15),
    _MplsTunnelHopStorageType_Type()
)
mplsTunnelHopStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopStorageType.setStatus("current")


class _MplsTunnelHopLabelStatuses_Type(Bits):
    """Custom type mplsTunnelHopLabelStatuses based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("forwardPresent", 0),
          ("reversePresent", 1))
    )

_MplsTunnelHopLabelStatuses_Type.__name__ = "Bits"
_MplsTunnelHopLabelStatuses_Object = MibTableColumn
mplsTunnelHopLabelStatuses = _MplsTunnelHopLabelStatuses_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 16),
    _MplsTunnelHopLabelStatuses_Type()
)
mplsTunnelHopLabelStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelHopLabelStatuses.setStatus("current")
_MplsTunnelHopExpLabelType_Type = MplsGeneralizedLabelType
_MplsTunnelHopExpLabelType_Object = MibTableColumn
mplsTunnelHopExpLabelType = _MplsTunnelHopExpLabelType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 17),
    _MplsTunnelHopExpLabelType_Type()
)
mplsTunnelHopExpLabelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopExpLabelType.setStatus("current")
_MplsTunnelHopExpLabel_Type = MplsGeneralizedLabel
_MplsTunnelHopExpLabel_Object = MibTableColumn
mplsTunnelHopExpLabel = _MplsTunnelHopExpLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 18),
    _MplsTunnelHopExpLabel_Type()
)
mplsTunnelHopExpLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopExpLabel.setStatus("current")
_MplsTunnelHopExpRvrsLabelType_Type = MplsGeneralizedLabelType
_MplsTunnelHopExpRvrsLabelType_Object = MibTableColumn
mplsTunnelHopExpRvrsLabelType = _MplsTunnelHopExpRvrsLabelType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 19),
    _MplsTunnelHopExpRvrsLabelType_Type()
)
mplsTunnelHopExpRvrsLabelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopExpRvrsLabelType.setStatus("current")
_MplsTunnelHopExpRvrsLabel_Type = MplsGeneralizedLabel
_MplsTunnelHopExpRvrsLabel_Object = MibTableColumn
mplsTunnelHopExpRvrsLabel = _MplsTunnelHopExpRvrsLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 4, 1, 20),
    _MplsTunnelHopExpRvrsLabel_Type()
)
mplsTunnelHopExpRvrsLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelHopExpRvrsLabel.setStatus("current")
_MplsTunnelResourceIndexNextTable_Object = MibTable
mplsTunnelResourceIndexNextTable = _MplsTunnelResourceIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 5)
)
if mibBuilder.loadTexts:
    mplsTunnelResourceIndexNextTable.setStatus("current")
_MplsTunnelResourceIndexNextEntry_Object = MibTableRow
mplsTunnelResourceIndexNextEntry = _MplsTunnelResourceIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 5, 1)
)
mplsTunnelResourceIndexNextEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelResourceIndexNextEntry.setStatus("current")


class _MplsTunnelResourceIndexNextIndex_Type(Unsigned32):
    """Custom type mplsTunnelResourceIndexNextIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsTunnelResourceIndexNextIndex_Type.__name__ = "Unsigned32"
_MplsTunnelResourceIndexNextIndex_Object = MibTableColumn
mplsTunnelResourceIndexNextIndex = _MplsTunnelResourceIndexNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 5, 1, 1),
    _MplsTunnelResourceIndexNextIndex_Type()
)
mplsTunnelResourceIndexNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelResourceIndexNextIndex.setStatus("current")
_MplsTunnelResourceTable_Object = MibTable
mplsTunnelResourceTable = _MplsTunnelResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 6)
)
if mibBuilder.loadTexts:
    mplsTunnelResourceTable.setStatus("current")
_MplsTunnelResourceEntry_Object = MibTableRow
mplsTunnelResourceEntry = _MplsTunnelResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 6, 1)
)
mplsTunnelResourceEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
    (0, "PRVT-MPLS-TE-MIB", "mplsTunnelResourceIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelResourceEntry.setStatus("current")


class _MplsTunnelResourceIndex_Type(Unsigned32):
    """Custom type mplsTunnelResourceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsTunnelResourceIndex_Type.__name__ = "Unsigned32"
_MplsTunnelResourceIndex_Object = MibTableColumn
mplsTunnelResourceIndex = _MplsTunnelResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 6, 1, 1),
    _MplsTunnelResourceIndex_Type()
)
mplsTunnelResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelResourceIndex.setStatus("current")


class _MplsTunnelResourceMaxRate_Type(MplsBitRate):
    """Custom type mplsTunnelResourceMaxRate based on MplsBitRate"""
    defaultValue = 0


_MplsTunnelResourceMaxRate_Type.__name__ = "MplsBitRate"
_MplsTunnelResourceMaxRate_Object = MibTableColumn
mplsTunnelResourceMaxRate = _MplsTunnelResourceMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 6, 1, 2),
    _MplsTunnelResourceMaxRate_Type()
)
mplsTunnelResourceMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceMaxRate.setUnits("1000s of bits per second")


class _MplsTunnelResourceMeanRate_Type(MplsBitRate):
    """Custom type mplsTunnelResourceMeanRate based on MplsBitRate"""
    defaultValue = 0


_MplsTunnelResourceMeanRate_Type.__name__ = "MplsBitRate"
_MplsTunnelResourceMeanRate_Object = MibTableColumn
mplsTunnelResourceMeanRate = _MplsTunnelResourceMeanRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 6, 1, 3),
    _MplsTunnelResourceMeanRate_Type()
)
mplsTunnelResourceMeanRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceMeanRate.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceMeanRate.setUnits("1000s of bits per second")


class _MplsTunnelResourceMaxBurstSize_Type(MplsBurstSize):
    """Custom type mplsTunnelResourceMaxBurstSize based on MplsBurstSize"""
    defaultValue = 0


_MplsTunnelResourceMaxBurstSize_Type.__name__ = "MplsBurstSize"
_MplsTunnelResourceMaxBurstSize_Object = MibTableColumn
mplsTunnelResourceMaxBurstSize = _MplsTunnelResourceMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 6, 1, 4),
    _MplsTunnelResourceMaxBurstSize_Type()
)
mplsTunnelResourceMaxBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceMaxBurstSize.setUnits("bytes")


class _MplsTunnelResourceMeanBurstSize_Type(MplsBurstSize):
    """Custom type mplsTunnelResourceMeanBurstSize based on MplsBurstSize"""
    defaultValue = 0


_MplsTunnelResourceMeanBurstSize_Type.__name__ = "MplsBurstSize"
_MplsTunnelResourceMeanBurstSize_Object = MibTableColumn
mplsTunnelResourceMeanBurstSize = _MplsTunnelResourceMeanBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 6, 1, 5),
    _MplsTunnelResourceMeanBurstSize_Type()
)
mplsTunnelResourceMeanBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceMeanBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceMeanBurstSize.setUnits("bytes")


class _MplsTunnelResourceExBurstSize_Type(MplsBurstSize):
    """Custom type mplsTunnelResourceExBurstSize based on MplsBurstSize"""
    defaultValue = 0


_MplsTunnelResourceExBurstSize_Type.__name__ = "MplsBurstSize"
_MplsTunnelResourceExBurstSize_Object = MibTableColumn
mplsTunnelResourceExBurstSize = _MplsTunnelResourceExBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 6, 1, 6),
    _MplsTunnelResourceExBurstSize_Type()
)
mplsTunnelResourceExBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceExBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelResourceExBurstSize.setUnits("bytes")


class _MplsTunnelResourceFrequency_Type(Integer32):
    """Custom type mplsTunnelResourceFrequency based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("frequent", 2),
          ("veryFrequent", 3))
    )


_MplsTunnelResourceFrequency_Type.__name__ = "Integer32"
_MplsTunnelResourceFrequency_Object = MibTableColumn
mplsTunnelResourceFrequency = _MplsTunnelResourceFrequency_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 6, 1, 7),
    _MplsTunnelResourceFrequency_Type()
)
mplsTunnelResourceFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceFrequency.setStatus("current")


class _MplsTunnelResourceWeight_Type(Unsigned32):
    """Custom type mplsTunnelResourceWeight based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsTunnelResourceWeight_Type.__name__ = "Unsigned32"
_MplsTunnelResourceWeight_Object = MibTableColumn
mplsTunnelResourceWeight = _MplsTunnelResourceWeight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 6, 1, 8),
    _MplsTunnelResourceWeight_Type()
)
mplsTunnelResourceWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceWeight.setStatus("current")
_MplsTunnelResourceRowStatus_Type = RowStatus
_MplsTunnelResourceRowStatus_Object = MibTableColumn
mplsTunnelResourceRowStatus = _MplsTunnelResourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 6, 1, 9),
    _MplsTunnelResourceRowStatus_Type()
)
mplsTunnelResourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceRowStatus.setStatus("current")


class _MplsTunnelResourceStorageType_Type(StorageType):
    """Custom type mplsTunnelResourceStorageType based on StorageType"""
    defaultValue = 2


_MplsTunnelResourceStorageType_Type.__name__ = "StorageType"
_MplsTunnelResourceStorageType_Object = MibTableColumn
mplsTunnelResourceStorageType = _MplsTunnelResourceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 6, 1, 10),
    _MplsTunnelResourceStorageType_Type()
)
mplsTunnelResourceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelResourceStorageType.setStatus("current")
_MplsTunnelARHopTable_Object = MibTable
mplsTunnelARHopTable = _MplsTunnelARHopTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 7)
)
if mibBuilder.loadTexts:
    mplsTunnelARHopTable.setStatus("current")
_MplsTunnelARHopEntry_Object = MibTableRow
mplsTunnelARHopEntry = _MplsTunnelARHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 7, 1)
)
mplsTunnelARHopEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
    (0, "PRVT-MPLS-TE-MIB", "mplsTunnelARHopListIndex"),
    (0, "PRVT-MPLS-TE-MIB", "mplsTunnelARHopIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelARHopEntry.setStatus("current")
_MplsTunnelARHopListIndex_Type = MplsPathIndex
_MplsTunnelARHopListIndex_Object = MibTableColumn
mplsTunnelARHopListIndex = _MplsTunnelARHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 7, 1, 1),
    _MplsTunnelARHopListIndex_Type()
)
mplsTunnelARHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelARHopListIndex.setStatus("current")
_MplsTunnelARHopIndex_Type = MplsPathIndex
_MplsTunnelARHopIndex_Object = MibTableColumn
mplsTunnelARHopIndex = _MplsTunnelARHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 7, 1, 2),
    _MplsTunnelARHopIndex_Type()
)
mplsTunnelARHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelARHopIndex.setStatus("current")


class _MplsTunnelARHopAddrType_Type(TeHopAddressType):
    """Custom type mplsTunnelARHopAddrType based on TeHopAddressType"""
    defaultValue = 1


_MplsTunnelARHopAddrType_Type.__name__ = "TeHopAddressType"
_MplsTunnelARHopAddrType_Object = MibTableColumn
mplsTunnelARHopAddrType = _MplsTunnelARHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 7, 1, 3),
    _MplsTunnelARHopAddrType_Type()
)
mplsTunnelARHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopAddrType.setStatus("current")
_MplsTunnelARHopIpAddr_Type = TeHopAddress
_MplsTunnelARHopIpAddr_Object = MibTableColumn
mplsTunnelARHopIpAddr = _MplsTunnelARHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 7, 1, 4),
    _MplsTunnelARHopIpAddr_Type()
)
mplsTunnelARHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopIpAddr.setStatus("current")
_MplsTunnelARHopAddrUnnum_Type = TeHopAddressUnnum
_MplsTunnelARHopAddrUnnum_Object = MibTableColumn
mplsTunnelARHopAddrUnnum = _MplsTunnelARHopAddrUnnum_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 7, 1, 5),
    _MplsTunnelARHopAddrUnnum_Type()
)
mplsTunnelARHopAddrUnnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopAddrUnnum.setStatus("current")
_MplsTunnelARHopLspId_Type = MplsLSPID
_MplsTunnelARHopLspId_Object = MibTableColumn
mplsTunnelARHopLspId = _MplsTunnelARHopLspId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 7, 1, 6),
    _MplsTunnelARHopLspId_Type()
)
mplsTunnelARHopLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopLspId.setStatus("current")


class _MplsTunnelARHopLabelStatuses_Type(Bits):
    """Custom type mplsTunnelARHopLabelStatuses based on Bits"""
    namedValues = NamedValues(
        *(("forwardPresent", 0),
          ("reversePresent", 1),
          ("forwardGlobal", 2),
          ("reverseGlobal", 3))
    )

_MplsTunnelARHopLabelStatuses_Type.__name__ = "Bits"
_MplsTunnelARHopLabelStatuses_Object = MibTableColumn
mplsTunnelARHopLabelStatuses = _MplsTunnelARHopLabelStatuses_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 7, 1, 7),
    _MplsTunnelARHopLabelStatuses_Type()
)
mplsTunnelARHopLabelStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopLabelStatuses.setStatus("current")
_MplsTunnelARHopExpLabelType_Type = MplsGeneralizedLabelType
_MplsTunnelARHopExpLabelType_Object = MibTableColumn
mplsTunnelARHopExpLabelType = _MplsTunnelARHopExpLabelType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 7, 1, 8),
    _MplsTunnelARHopExpLabelType_Type()
)
mplsTunnelARHopExpLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopExpLabelType.setStatus("current")
_MplsTunnelARHopExpLabel_Type = MplsGeneralizedLabel
_MplsTunnelARHopExpLabel_Object = MibTableColumn
mplsTunnelARHopExpLabel = _MplsTunnelARHopExpLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 7, 1, 9),
    _MplsTunnelARHopExpLabel_Type()
)
mplsTunnelARHopExpLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopExpLabel.setStatus("current")
_MplsTunnelARHopExpRvrsLabelType_Type = MplsGeneralizedLabelType
_MplsTunnelARHopExpRvrsLabelType_Object = MibTableColumn
mplsTunnelARHopExpRvrsLabelType = _MplsTunnelARHopExpRvrsLabelType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 7, 1, 10),
    _MplsTunnelARHopExpRvrsLabelType_Type()
)
mplsTunnelARHopExpRvrsLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopExpRvrsLabelType.setStatus("current")
_MplsTunnelARHopExpRvrsLabel_Type = MplsGeneralizedLabel
_MplsTunnelARHopExpRvrsLabel_Object = MibTableColumn
mplsTunnelARHopExpRvrsLabel = _MplsTunnelARHopExpRvrsLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 7, 1, 11),
    _MplsTunnelARHopExpRvrsLabel_Type()
)
mplsTunnelARHopExpRvrsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopExpRvrsLabel.setStatus("current")


class _MplsTunnelARHopProtection_Type(Bits):
    """Custom type mplsTunnelARHopProtection based on Bits"""
    namedValues = NamedValues(
        *(("localAvailable", 0),
          ("localInUse", 1))
    )

_MplsTunnelARHopProtection_Type.__name__ = "Bits"
_MplsTunnelARHopProtection_Object = MibTableColumn
mplsTunnelARHopProtection = _MplsTunnelARHopProtection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 7, 1, 12),
    _MplsTunnelARHopProtection_Type()
)
mplsTunnelARHopProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelARHopProtection.setStatus("current")
_MplsTunnelCHopTable_Object = MibTable
mplsTunnelCHopTable = _MplsTunnelCHopTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8)
)
if mibBuilder.loadTexts:
    mplsTunnelCHopTable.setStatus("current")
_MplsTunnelCHopEntry_Object = MibTableRow
mplsTunnelCHopEntry = _MplsTunnelCHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1)
)
mplsTunnelCHopEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
    (0, "PRVT-MPLS-TE-MIB", "mplsTunnelCHopListIndex"),
    (0, "PRVT-MPLS-TE-MIB", "mplsTunnelCHopIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelCHopEntry.setStatus("current")
_MplsTunnelCHopListIndex_Type = MplsPathIndex
_MplsTunnelCHopListIndex_Object = MibTableColumn
mplsTunnelCHopListIndex = _MplsTunnelCHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1, 1),
    _MplsTunnelCHopListIndex_Type()
)
mplsTunnelCHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelCHopListIndex.setStatus("current")
_MplsTunnelCHopIndex_Type = MplsPathIndex
_MplsTunnelCHopIndex_Object = MibTableColumn
mplsTunnelCHopIndex = _MplsTunnelCHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1, 2),
    _MplsTunnelCHopIndex_Type()
)
mplsTunnelCHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsTunnelCHopIndex.setStatus("current")


class _MplsTunnelCHopAddrType_Type(TeHopAddressType):
    """Custom type mplsTunnelCHopAddrType based on TeHopAddressType"""
    defaultValue = 1


_MplsTunnelCHopAddrType_Type.__name__ = "TeHopAddressType"
_MplsTunnelCHopAddrType_Object = MibTableColumn
mplsTunnelCHopAddrType = _MplsTunnelCHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1, 3),
    _MplsTunnelCHopAddrType_Type()
)
mplsTunnelCHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopAddrType.setStatus("current")
_MplsTunnelCHopIpAddr_Type = TeHopAddress
_MplsTunnelCHopIpAddr_Object = MibTableColumn
mplsTunnelCHopIpAddr = _MplsTunnelCHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1, 4),
    _MplsTunnelCHopIpAddr_Type()
)
mplsTunnelCHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopIpAddr.setStatus("current")


class _MplsTunnelCHopIpPrefixLen_Type(Unsigned32):
    """Custom type mplsTunnelCHopIpPrefixLen based on Unsigned32"""
    defaultValue = 32


_MplsTunnelCHopIpPrefixLen_Type.__name__ = "Unsigned32"
_MplsTunnelCHopIpPrefixLen_Object = MibTableColumn
mplsTunnelCHopIpPrefixLen = _MplsTunnelCHopIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1, 5),
    _MplsTunnelCHopIpPrefixLen_Type()
)
mplsTunnelCHopIpPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopIpPrefixLen.setStatus("current")
_MplsTunnelCHopAsNumber_Type = TeHopAddressAS
_MplsTunnelCHopAsNumber_Object = MibTableColumn
mplsTunnelCHopAsNumber = _MplsTunnelCHopAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1, 6),
    _MplsTunnelCHopAsNumber_Type()
)
mplsTunnelCHopAsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopAsNumber.setStatus("current")
_MplsTunnelCHopAddrUnnum_Type = TeHopAddressUnnum
_MplsTunnelCHopAddrUnnum_Object = MibTableColumn
mplsTunnelCHopAddrUnnum = _MplsTunnelCHopAddrUnnum_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1, 7),
    _MplsTunnelCHopAddrUnnum_Type()
)
mplsTunnelCHopAddrUnnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopAddrUnnum.setStatus("current")
_MplsTunnelCHopLspId_Type = MplsLSPID
_MplsTunnelCHopLspId_Object = MibTableColumn
mplsTunnelCHopLspId = _MplsTunnelCHopLspId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1, 8),
    _MplsTunnelCHopLspId_Type()
)
mplsTunnelCHopLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopLspId.setStatus("current")


class _MplsTunnelCHopType_Type(Integer32):
    """Custom type mplsTunnelCHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("loose", 2))
    )


_MplsTunnelCHopType_Type.__name__ = "Integer32"
_MplsTunnelCHopType_Object = MibTableColumn
mplsTunnelCHopType = _MplsTunnelCHopType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1, 9),
    _MplsTunnelCHopType_Type()
)
mplsTunnelCHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopType.setStatus("current")


class _MplsTunnelCHopLabelStatuses_Type(Bits):
    """Custom type mplsTunnelCHopLabelStatuses based on Bits"""
    namedValues = NamedValues(
        *(("forwardPresent", 0),
          ("reversePresent", 1))
    )

_MplsTunnelCHopLabelStatuses_Type.__name__ = "Bits"
_MplsTunnelCHopLabelStatuses_Object = MibTableColumn
mplsTunnelCHopLabelStatuses = _MplsTunnelCHopLabelStatuses_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1, 11),
    _MplsTunnelCHopLabelStatuses_Type()
)
mplsTunnelCHopLabelStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopLabelStatuses.setStatus("current")
_MplsTunnelCHopExpLabelType_Type = MplsGeneralizedLabelType
_MplsTunnelCHopExpLabelType_Object = MibTableColumn
mplsTunnelCHopExpLabelType = _MplsTunnelCHopExpLabelType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1, 12),
    _MplsTunnelCHopExpLabelType_Type()
)
mplsTunnelCHopExpLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopExpLabelType.setStatus("current")
_MplsTunnelCHopExpLabel_Type = MplsGeneralizedLabel
_MplsTunnelCHopExpLabel_Object = MibTableColumn
mplsTunnelCHopExpLabel = _MplsTunnelCHopExpLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1, 13),
    _MplsTunnelCHopExpLabel_Type()
)
mplsTunnelCHopExpLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopExpLabel.setStatus("current")
_MplsTunnelCHopExpRvrsLabelType_Type = MplsGeneralizedLabelType
_MplsTunnelCHopExpRvrsLabelType_Object = MibTableColumn
mplsTunnelCHopExpRvrsLabelType = _MplsTunnelCHopExpRvrsLabelType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1, 14),
    _MplsTunnelCHopExpRvrsLabelType_Type()
)
mplsTunnelCHopExpRvrsLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelCHopExpRvrsLabelType.setStatus("current")
_MplsTunnelCHopExpRvrsLabel_Type = MplsGeneralizedLabel
_MplsTunnelCHopExpRvrsLabel_Object = MibTableColumn
mplsTunnelCHopExpRvrsLabel = _MplsTunnelCHopExpRvrsLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 8, 1, 15),
    _MplsTunnelCHopExpRvrsLabel_Type()
)
mplsTunnelCHopExpRvrsLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCHopExpRvrsLabel.setStatus("current")
_MplsTunnelPerfTable_Object = MibTable
mplsTunnelPerfTable = _MplsTunnelPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 9)
)
if mibBuilder.loadTexts:
    mplsTunnelPerfTable.setStatus("current")
_MplsTunnelPerfEntry_Object = MibTableRow
mplsTunnelPerfEntry = _MplsTunnelPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    mplsTunnelPerfEntry.setStatus("current")
_MplsTunnelPerfPackets_Type = Counter32
_MplsTunnelPerfPackets_Object = MibTableColumn
mplsTunnelPerfPackets = _MplsTunnelPerfPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 9, 1, 1),
    _MplsTunnelPerfPackets_Type()
)
mplsTunnelPerfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfPackets.setStatus("current")
_MplsTunnelPerfHCPackets_Type = Counter64
_MplsTunnelPerfHCPackets_Object = MibTableColumn
mplsTunnelPerfHCPackets = _MplsTunnelPerfHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 9, 1, 2),
    _MplsTunnelPerfHCPackets_Type()
)
mplsTunnelPerfHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfHCPackets.setStatus("current")
_MplsTunnelPerfErrors_Type = Counter32
_MplsTunnelPerfErrors_Object = MibTableColumn
mplsTunnelPerfErrors = _MplsTunnelPerfErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 9, 1, 3),
    _MplsTunnelPerfErrors_Type()
)
mplsTunnelPerfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfErrors.setStatus("current")
_MplsTunnelPerfBytes_Type = Counter32
_MplsTunnelPerfBytes_Object = MibTableColumn
mplsTunnelPerfBytes = _MplsTunnelPerfBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 9, 1, 4),
    _MplsTunnelPerfBytes_Type()
)
mplsTunnelPerfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfBytes.setStatus("current")
_MplsTunnelPerfHCBytes_Type = Counter64
_MplsTunnelPerfHCBytes_Object = MibTableColumn
mplsTunnelPerfHCBytes = _MplsTunnelPerfHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 9, 1, 5),
    _MplsTunnelPerfHCBytes_Type()
)
mplsTunnelPerfHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelPerfHCBytes.setStatus("current")
_MplsTunnelCRLDPResTable_Object = MibTable
mplsTunnelCRLDPResTable = _MplsTunnelCRLDPResTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 10)
)
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResTable.setStatus("current")
_MplsTunnelCRLDPResEntry_Object = MibTableRow
mplsTunnelCRLDPResEntry = _MplsTunnelCRLDPResEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 10, 1)
)
mplsTunnelCRLDPResEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
    (0, "PRVT-MPLS-TE-MIB", "mplsTunnelResourceIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResEntry.setStatus("current")


class _MplsTunnelCRLDPResMeanBurstSize_Type(MplsBurstSize):
    """Custom type mplsTunnelCRLDPResMeanBurstSize based on MplsBurstSize"""
    defaultValue = 0


_MplsTunnelCRLDPResMeanBurstSize_Type.__name__ = "MplsBurstSize"
_MplsTunnelCRLDPResMeanBurstSize_Object = MibTableColumn
mplsTunnelCRLDPResMeanBurstSize = _MplsTunnelCRLDPResMeanBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 10, 1, 2),
    _MplsTunnelCRLDPResMeanBurstSize_Type()
)
mplsTunnelCRLDPResMeanBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResMeanBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResMeanBurstSize.setUnits("bytes")
_MplsTunnelCRLDPResExBurstSize_Type = MplsBurstSize
_MplsTunnelCRLDPResExBurstSize_Object = MibTableColumn
mplsTunnelCRLDPResExBurstSize = _MplsTunnelCRLDPResExBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 10, 1, 3),
    _MplsTunnelCRLDPResExBurstSize_Type()
)
mplsTunnelCRLDPResExBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResExBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResExBurstSize.setUnits("bytes")


class _MplsTunnelCRLDPResFrequency_Type(Integer32):
    """Custom type mplsTunnelCRLDPResFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("frequent", 2),
          ("veryFrequent", 3))
    )


_MplsTunnelCRLDPResFrequency_Type.__name__ = "Integer32"
_MplsTunnelCRLDPResFrequency_Object = MibTableColumn
mplsTunnelCRLDPResFrequency = _MplsTunnelCRLDPResFrequency_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 10, 1, 4),
    _MplsTunnelCRLDPResFrequency_Type()
)
mplsTunnelCRLDPResFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResFrequency.setStatus("current")


class _MplsTunnelCRLDPResWeight_Type(Unsigned32):
    """Custom type mplsTunnelCRLDPResWeight based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsTunnelCRLDPResWeight_Type.__name__ = "Unsigned32"
_MplsTunnelCRLDPResWeight_Object = MibTableColumn
mplsTunnelCRLDPResWeight = _MplsTunnelCRLDPResWeight_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 10, 1, 5),
    _MplsTunnelCRLDPResWeight_Type()
)
mplsTunnelCRLDPResWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResWeight.setStatus("current")


class _MplsTunnelCRLDPResFlags_Type(Unsigned32):
    """Custom type mplsTunnelCRLDPResFlags based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MplsTunnelCRLDPResFlags_Type.__name__ = "Unsigned32"
_MplsTunnelCRLDPResFlags_Object = MibTableColumn
mplsTunnelCRLDPResFlags = _MplsTunnelCRLDPResFlags_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 10, 1, 6),
    _MplsTunnelCRLDPResFlags_Type()
)
mplsTunnelCRLDPResFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResFlags.setStatus("current")
_MplsTunnelCRLDPResRowStatus_Type = RowStatus
_MplsTunnelCRLDPResRowStatus_Object = MibTableColumn
mplsTunnelCRLDPResRowStatus = _MplsTunnelCRLDPResRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 10, 1, 7),
    _MplsTunnelCRLDPResRowStatus_Type()
)
mplsTunnelCRLDPResRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResRowStatus.setStatus("current")


class _MplsTunnelCRLDPResStorageType_Type(StorageType):
    """Custom type mplsTunnelCRLDPResStorageType based on StorageType"""
    defaultValue = 2


_MplsTunnelCRLDPResStorageType_Type.__name__ = "StorageType"
_MplsTunnelCRLDPResStorageType_Object = MibTableColumn
mplsTunnelCRLDPResStorageType = _MplsTunnelCRLDPResStorageType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 10, 1, 8),
    _MplsTunnelCRLDPResStorageType_Type()
)
mplsTunnelCRLDPResStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResStorageType.setStatus("current")
_MplsDiffServIndexNextTable_Object = MibTable
mplsDiffServIndexNextTable = _MplsDiffServIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 11)
)
if mibBuilder.loadTexts:
    mplsDiffServIndexNextTable.setStatus("current")
_MplsDiffServIndexNextEntry_Object = MibTableRow
mplsDiffServIndexNextEntry = _MplsDiffServIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 11, 1)
)
mplsDiffServIndexNextEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsDiffServIndexNextEntry.setStatus("current")
_MplsDiffServIndexNextIndex_Type = Integer32
_MplsDiffServIndexNextIndex_Object = MibTableColumn
mplsDiffServIndexNextIndex = _MplsDiffServIndexNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 11, 1, 1),
    _MplsDiffServIndexNextIndex_Type()
)
mplsDiffServIndexNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsDiffServIndexNextIndex.setStatus("current")
_MplsDiffServTable_Object = MibTable
mplsDiffServTable = _MplsDiffServTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12)
)
if mibBuilder.loadTexts:
    mplsDiffServTable.setStatus("current")
_MplsDiffServEntry_Object = MibTableRow
mplsDiffServEntry = _MplsDiffServEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12, 1)
)
mplsDiffServEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
    (0, "PRVT-MPLS-TE-MIB", "mplsDiffServIndex"),
)
if mibBuilder.loadTexts:
    mplsDiffServEntry.setStatus("current")


class _MplsDiffServIndex_Type(Integer32):
    """Custom type mplsDiffServIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsDiffServIndex_Type.__name__ = "Integer32"
_MplsDiffServIndex_Object = MibTableColumn
mplsDiffServIndex = _MplsDiffServIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12, 1, 1),
    _MplsDiffServIndex_Type()
)
mplsDiffServIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsDiffServIndex.setStatus("current")


class _MplsDiffServType_Type(Integer32):
    """Custom type mplsDiffServType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("elsp", 0),
          ("llsp", 1))
    )


_MplsDiffServType_Type.__name__ = "Integer32"
_MplsDiffServType_Object = MibTableColumn
mplsDiffServType = _MplsDiffServType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12, 1, 2),
    _MplsDiffServType_Type()
)
mplsDiffServType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsDiffServType.setStatus("current")
_MplsDiffServLLSPPSC_Type = Integer32
_MplsDiffServLLSPPSC_Object = MibTableColumn
mplsDiffServLLSPPSC = _MplsDiffServLLSPPSC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12, 1, 3),
    _MplsDiffServLLSPPSC_Type()
)
mplsDiffServLLSPPSC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsDiffServLLSPPSC.setStatus("current")


class _MplsDiffServELSPNumPHBs_Type(Integer32):
    """Custom type mplsDiffServELSPNumPHBs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MplsDiffServELSPNumPHBs_Type.__name__ = "Integer32"
_MplsDiffServELSPNumPHBs_Object = MibTableColumn
mplsDiffServELSPNumPHBs = _MplsDiffServELSPNumPHBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12, 1, 4),
    _MplsDiffServELSPNumPHBs_Type()
)
mplsDiffServELSPNumPHBs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsDiffServELSPNumPHBs.setStatus("current")
_MplsDiffServELSPPHB0_Type = Integer32
_MplsDiffServELSPPHB0_Object = MibTableColumn
mplsDiffServELSPPHB0 = _MplsDiffServELSPPHB0_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12, 1, 5),
    _MplsDiffServELSPPHB0_Type()
)
mplsDiffServELSPPHB0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsDiffServELSPPHB0.setStatus("current")
_MplsDiffServELSPPHB1_Type = Integer32
_MplsDiffServELSPPHB1_Object = MibTableColumn
mplsDiffServELSPPHB1 = _MplsDiffServELSPPHB1_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12, 1, 6),
    _MplsDiffServELSPPHB1_Type()
)
mplsDiffServELSPPHB1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsDiffServELSPPHB1.setStatus("current")
_MplsDiffServELSPPHB2_Type = Integer32
_MplsDiffServELSPPHB2_Object = MibTableColumn
mplsDiffServELSPPHB2 = _MplsDiffServELSPPHB2_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12, 1, 7),
    _MplsDiffServELSPPHB2_Type()
)
mplsDiffServELSPPHB2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsDiffServELSPPHB2.setStatus("current")
_MplsDiffServELSPPHB3_Type = Integer32
_MplsDiffServELSPPHB3_Object = MibTableColumn
mplsDiffServELSPPHB3 = _MplsDiffServELSPPHB3_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12, 1, 8),
    _MplsDiffServELSPPHB3_Type()
)
mplsDiffServELSPPHB3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsDiffServELSPPHB3.setStatus("current")
_MplsDiffServELSPPHB4_Type = Integer32
_MplsDiffServELSPPHB4_Object = MibTableColumn
mplsDiffServELSPPHB4 = _MplsDiffServELSPPHB4_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12, 1, 9),
    _MplsDiffServELSPPHB4_Type()
)
mplsDiffServELSPPHB4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsDiffServELSPPHB4.setStatus("current")
_MplsDiffServELSPPHB5_Type = Integer32
_MplsDiffServELSPPHB5_Object = MibTableColumn
mplsDiffServELSPPHB5 = _MplsDiffServELSPPHB5_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12, 1, 10),
    _MplsDiffServELSPPHB5_Type()
)
mplsDiffServELSPPHB5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsDiffServELSPPHB5.setStatus("current")
_MplsDiffServELSPPHB6_Type = Integer32
_MplsDiffServELSPPHB6_Object = MibTableColumn
mplsDiffServELSPPHB6 = _MplsDiffServELSPPHB6_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12, 1, 11),
    _MplsDiffServELSPPHB6_Type()
)
mplsDiffServELSPPHB6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsDiffServELSPPHB6.setStatus("current")
_MplsDiffServELSPPHB7_Type = Integer32
_MplsDiffServELSPPHB7_Object = MibTableColumn
mplsDiffServELSPPHB7 = _MplsDiffServELSPPHB7_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12, 1, 12),
    _MplsDiffServELSPPHB7_Type()
)
mplsDiffServELSPPHB7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsDiffServELSPPHB7.setStatus("current")
_MplsDiffServRowStatus_Type = RowStatus
_MplsDiffServRowStatus_Object = MibTableColumn
mplsDiffServRowStatus = _MplsDiffServRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 12, 1, 13),
    _MplsDiffServRowStatus_Type()
)
mplsDiffServRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsDiffServRowStatus.setStatus("current")
_PrvtMplsTunnelUNIDvLstIdxNxtTable_Object = MibTable
prvtMplsTunnelUNIDvLstIdxNxtTable = _PrvtMplsTunnelUNIDvLstIdxNxtTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 13)
)
if mibBuilder.loadTexts:
    prvtMplsTunnelUNIDvLstIdxNxtTable.setStatus("current")
_PrvtMplsTunnelUNIDvLstIdxNxtEntry_Object = MibTableRow
prvtMplsTunnelUNIDvLstIdxNxtEntry = _PrvtMplsTunnelUNIDvLstIdxNxtEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 13, 1)
)
prvtMplsTunnelUNIDvLstIdxNxtEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
)
if mibBuilder.loadTexts:
    prvtMplsTunnelUNIDvLstIdxNxtEntry.setStatus("current")
_PrvtMplsTunnelUNIDivListIdxNext_Type = Integer32
_PrvtMplsTunnelUNIDivListIdxNext_Object = MibTableColumn
prvtMplsTunnelUNIDivListIdxNext = _PrvtMplsTunnelUNIDivListIdxNext_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 13, 1, 1),
    _PrvtMplsTunnelUNIDivListIdxNext_Type()
)
prvtMplsTunnelUNIDivListIdxNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMplsTunnelUNIDivListIdxNext.setStatus("current")
_PrvtMplsTunnelUNIDiversityTable_Object = MibTable
prvtMplsTunnelUNIDiversityTable = _PrvtMplsTunnelUNIDiversityTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 14)
)
if mibBuilder.loadTexts:
    prvtMplsTunnelUNIDiversityTable.setStatus("current")
_PrvtMplsTunnelUNIDiversityEntry_Object = MibTableRow
prvtMplsTunnelUNIDiversityEntry = _PrvtMplsTunnelUNIDiversityEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 14, 1)
)
prvtMplsTunnelUNIDiversityEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
    (0, "PRVT-MPLS-TE-MIB", "prvtMplsTunnelUNIDivListIdx"),
    (0, "PRVT-MPLS-TE-MIB", "prvtMplsTunnelUNIDivIdx"),
)
if mibBuilder.loadTexts:
    prvtMplsTunnelUNIDiversityEntry.setStatus("current")


class _PrvtMplsTunnelUNIDivListIdx_Type(Integer32):
    """Custom type prvtMplsTunnelUNIDivListIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrvtMplsTunnelUNIDivListIdx_Type.__name__ = "Integer32"
_PrvtMplsTunnelUNIDivListIdx_Object = MibTableColumn
prvtMplsTunnelUNIDivListIdx = _PrvtMplsTunnelUNIDivListIdx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 14, 1, 2),
    _PrvtMplsTunnelUNIDivListIdx_Type()
)
prvtMplsTunnelUNIDivListIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtMplsTunnelUNIDivListIdx.setStatus("current")


class _PrvtMplsTunnelUNIDivIdx_Type(Integer32):
    """Custom type prvtMplsTunnelUNIDivIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrvtMplsTunnelUNIDivIdx_Type.__name__ = "Integer32"
_PrvtMplsTunnelUNIDivIdx_Object = MibTableColumn
prvtMplsTunnelUNIDivIdx = _PrvtMplsTunnelUNIDivIdx_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 14, 1, 3),
    _PrvtMplsTunnelUNIDivIdx_Type()
)
prvtMplsTunnelUNIDivIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtMplsTunnelUNIDivIdx.setStatus("current")
_PrvtMplsTunnelUNIDivRowPointer_Type = RowPointer
_PrvtMplsTunnelUNIDivRowPointer_Object = MibTableColumn
prvtMplsTunnelUNIDivRowPointer = _PrvtMplsTunnelUNIDivRowPointer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 14, 1, 4),
    _PrvtMplsTunnelUNIDivRowPointer_Type()
)
prvtMplsTunnelUNIDivRowPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTunnelUNIDivRowPointer.setStatus("current")
_PrvtMplsTunnelOperStatus_Type = Integer32
_PrvtMplsTunnelOperStatus_Object = MibTableColumn
prvtMplsTunnelOperStatus = _PrvtMplsTunnelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 14, 1, 5),
    _PrvtMplsTunnelOperStatus_Type()
)
prvtMplsTunnelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMplsTunnelOperStatus.setStatus("current")
_PrvtMplsTunnelUNIDivRowStatus_Type = RowStatus
_PrvtMplsTunnelUNIDivRowStatus_Object = MibTableColumn
prvtMplsTunnelUNIDivRowStatus = _PrvtMplsTunnelUNIDivRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 14, 1, 6),
    _PrvtMplsTunnelUNIDivRowStatus_Type()
)
prvtMplsTunnelUNIDivRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTunnelUNIDivRowStatus.setStatus("current")


class _PrvtMplsTunnelUNIDivRequirement_Type(Integer32):
    """Custom type prvtMplsTunnelUNIDivRequirement based on Integer32"""
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
        *(("nodeDiverse", 1),
          ("linkDiverse", 2),
          ("srlg", 3),
          ("sharedPath", 4))
    )


_PrvtMplsTunnelUNIDivRequirement_Type.__name__ = "Integer32"
_PrvtMplsTunnelUNIDivRequirement_Object = MibTableColumn
prvtMplsTunnelUNIDivRequirement = _PrvtMplsTunnelUNIDivRequirement_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 14, 1, 7),
    _PrvtMplsTunnelUNIDivRequirement_Type()
)
prvtMplsTunnelUNIDivRequirement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTunnelUNIDivRequirement.setStatus("current")
_PrvtMplsTunnelUNIDivAccess_Type = Integer32
_PrvtMplsTunnelUNIDivAccess_Object = MibTableColumn
prvtMplsTunnelUNIDivAccess = _PrvtMplsTunnelUNIDivAccess_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 14, 1, 8),
    _PrvtMplsTunnelUNIDivAccess_Type()
)
prvtMplsTunnelUNIDivAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMplsTunnelUNIDivAccess.setStatus("current")
_PrvtMplsTunnelTrapEnableTable_Object = MibTable
prvtMplsTunnelTrapEnableTable = _PrvtMplsTunnelTrapEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 15)
)
if mibBuilder.loadTexts:
    prvtMplsTunnelTrapEnableTable.setStatus("current")
_PrvtMplsTunnelTrapEnableEntry_Object = MibTableRow
prvtMplsTunnelTrapEnableEntry = _PrvtMplsTunnelTrapEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 15, 1)
)
prvtMplsTunnelTrapEnableEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
)
if mibBuilder.loadTexts:
    prvtMplsTunnelTrapEnableEntry.setStatus("current")


class _MplsTunnelTrapEnable_Type(TruthValue):
    """Custom type mplsTunnelTrapEnable based on TruthValue"""
    defaultValue = 2


_MplsTunnelTrapEnable_Type.__name__ = "TruthValue"
_MplsTunnelTrapEnable_Object = MibTableColumn
mplsTunnelTrapEnable = _MplsTunnelTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 15, 1, 2),
    _MplsTunnelTrapEnable_Type()
)
mplsTunnelTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelTrapEnable.setStatus("current")
_MplsTeMibEntityScalarTable_Object = MibTable
mplsTeMibEntityScalarTable = _MplsTeMibEntityScalarTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 16)
)
if mibBuilder.loadTexts:
    mplsTeMibEntityScalarTable.setStatus("current")
_MplsTeMibEntityScalarEntry_Object = MibTableRow
mplsTeMibEntityScalarEntry = _MplsTeMibEntityScalarEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 16, 1)
)
mplsTeMibEntityScalarEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
)
if mibBuilder.loadTexts:
    mplsTeMibEntityScalarEntry.setStatus("current")
_MplsTunnelConfigured_Type = Unsigned32
_MplsTunnelConfigured_Object = MibTableColumn
mplsTunnelConfigured = _MplsTunnelConfigured_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 16, 1, 2),
    _MplsTunnelConfigured_Type()
)
mplsTunnelConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelConfigured.setStatus("current")
_MplsTunnelActive_Type = Unsigned32
_MplsTunnelActive_Object = MibTableColumn
mplsTunnelActive = _MplsTunnelActive_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 16, 1, 3),
    _MplsTunnelActive_Type()
)
mplsTunnelActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelActive.setStatus("current")


class _MplsTunnelTEDistProto_Type(Bits):
    """Custom type mplsTunnelTEDistProto based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("ospf", 1),
          ("isis", 2))
    )

_MplsTunnelTEDistProto_Type.__name__ = "Bits"
_MplsTunnelTEDistProto_Object = MibTableColumn
mplsTunnelTEDistProto = _MplsTunnelTEDistProto_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 16, 1, 4),
    _MplsTunnelTEDistProto_Type()
)
mplsTunnelTEDistProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelTEDistProto.setStatus("current")
_MplsTunnelMaxHops_Type = Unsigned32
_MplsTunnelMaxHops_Object = MibTableColumn
mplsTunnelMaxHops = _MplsTunnelMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 16, 1, 5),
    _MplsTunnelMaxHops_Type()
)
mplsTunnelMaxHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelMaxHops.setStatus("current")


class _MplsTunnelNotificationMaxRate_Type(Unsigned32):
    """Custom type mplsTunnelNotificationMaxRate based on Unsigned32"""
    defaultValue = 0


_MplsTunnelNotificationMaxRate_Type.__name__ = "Unsigned32"
_MplsTunnelNotificationMaxRate_Object = MibTableColumn
mplsTunnelNotificationMaxRate = _MplsTunnelNotificationMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 16, 1, 6),
    _MplsTunnelNotificationMaxRate_Type()
)
mplsTunnelNotificationMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelNotificationMaxRate.setStatus("current")
_MplsTunnelSonetResTable_Object = MibTable
mplsTunnelSonetResTable = _MplsTunnelSonetResTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 17)
)
if mibBuilder.loadTexts:
    mplsTunnelSonetResTable.setStatus("current")
_MplsTunnelSonetResEntry_Object = MibTableRow
mplsTunnelSonetResEntry = _MplsTunnelSonetResEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 17, 1)
)
mplsTunnelSonetResEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
    (0, "PRVT-MPLS-TE-MIB", "mplsTunnelResourceIndex"),
)
if mibBuilder.loadTexts:
    mplsTunnelSonetResEntry.setStatus("current")


class _MplsTunnelSonetResRCC_Type(Integer32):
    """Custom type mplsTunnelSonetResRCC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsTunnelSonetResRCC_Type.__name__ = "Integer32"
_MplsTunnelSonetResRCC_Object = MibTableColumn
mplsTunnelSonetResRCC = _MplsTunnelSonetResRCC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 17, 1, 2),
    _MplsTunnelSonetResRCC_Type()
)
mplsTunnelSonetResRCC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSonetResRCC.setStatus("current")


class _MplsTunnelSonetResNCC_Type(Unsigned32):
    """Custom type mplsTunnelSonetResNCC based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsTunnelSonetResNCC_Type.__name__ = "Unsigned32"
_MplsTunnelSonetResNCC_Object = MibTableColumn
mplsTunnelSonetResNCC = _MplsTunnelSonetResNCC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 17, 1, 3),
    _MplsTunnelSonetResNCC_Type()
)
mplsTunnelSonetResNCC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSonetResNCC.setStatus("current")


class _MplsTunnelSonetResNVC_Type(Unsigned32):
    """Custom type mplsTunnelSonetResNVC based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MplsTunnelSonetResNVC_Type.__name__ = "Unsigned32"
_MplsTunnelSonetResNVC_Object = MibTableColumn
mplsTunnelSonetResNVC = _MplsTunnelSonetResNVC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 17, 1, 4),
    _MplsTunnelSonetResNVC_Type()
)
mplsTunnelSonetResNVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSonetResNVC.setStatus("current")


class _MplsTunnelSonetResMultiplier_Type(Unsigned32):
    """Custom type mplsTunnelSonetResMultiplier based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MplsTunnelSonetResMultiplier_Type.__name__ = "Unsigned32"
_MplsTunnelSonetResMultiplier_Object = MibTableColumn
mplsTunnelSonetResMultiplier = _MplsTunnelSonetResMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 17, 1, 5),
    _MplsTunnelSonetResMultiplier_Type()
)
mplsTunnelSonetResMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSonetResMultiplier.setStatus("current")


class _MplsTunnelSonetResTransparency_Type(Unsigned32):
    """Custom type mplsTunnelSonetResTransparency based on Unsigned32"""
    defaultValue = 0


_MplsTunnelSonetResTransparency_Type.__name__ = "Unsigned32"
_MplsTunnelSonetResTransparency_Object = MibTableColumn
mplsTunnelSonetResTransparency = _MplsTunnelSonetResTransparency_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 17, 1, 6),
    _MplsTunnelSonetResTransparency_Type()
)
mplsTunnelSonetResTransparency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSonetResTransparency.setStatus("current")
_MplsTunnelSonetResRowStatus_Type = RowStatus
_MplsTunnelSonetResRowStatus_Object = MibTableColumn
mplsTunnelSonetResRowStatus = _MplsTunnelSonetResRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 17, 1, 7),
    _MplsTunnelSonetResRowStatus_Type()
)
mplsTunnelSonetResRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSonetResRowStatus.setStatus("current")


class _MplsTunnelSonetResSignalType_Type(Integer32):
    """Custom type mplsTunnelSonetResSignalType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsTunnelSonetResSignalType_Type.__name__ = "Integer32"
_MplsTunnelSonetResSignalType_Object = MibTableColumn
mplsTunnelSonetResSignalType = _MplsTunnelSonetResSignalType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 17, 1, 9),
    _MplsTunnelSonetResSignalType_Type()
)
mplsTunnelSonetResSignalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsTunnelSonetResSignalType.setStatus("current")
_MplsTunnelErrorTable_Object = MibTable
mplsTunnelErrorTable = _MplsTunnelErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 18)
)
if mibBuilder.loadTexts:
    mplsTunnelErrorTable.setStatus("current")
_MplsTunnelErrorEntry_Object = MibTableRow
mplsTunnelErrorEntry = _MplsTunnelErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 18, 1)
)
if mibBuilder.loadTexts:
    mplsTunnelErrorEntry.setStatus("current")


class _MplsTunnelErrorLastErrorType_Type(Integer32):
    """Custom type mplsTunnelErrorLastErrorType based on Integer32"""
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
        *(("noError", 0),
          ("unknown", 1),
          ("protocol", 2),
          ("pathComputation", 3),
          ("localConfiguration", 4),
          ("localResources", 5),
          ("localOther", 6))
    )


_MplsTunnelErrorLastErrorType_Type.__name__ = "Integer32"
_MplsTunnelErrorLastErrorType_Object = MibTableColumn
mplsTunnelErrorLastErrorType = _MplsTunnelErrorLastErrorType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 18, 1, 1),
    _MplsTunnelErrorLastErrorType_Type()
)
mplsTunnelErrorLastErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelErrorLastErrorType.setStatus("current")
_MplsTunnelErrorLastTime_Type = TimeStamp
_MplsTunnelErrorLastTime_Object = MibTableColumn
mplsTunnelErrorLastTime = _MplsTunnelErrorLastTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 18, 1, 2),
    _MplsTunnelErrorLastTime_Type()
)
mplsTunnelErrorLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelErrorLastTime.setStatus("current")
_MplsTunnelErrorReporterType_Type = InetAddressType
_MplsTunnelErrorReporterType_Object = MibTableColumn
mplsTunnelErrorReporterType = _MplsTunnelErrorReporterType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 18, 1, 3),
    _MplsTunnelErrorReporterType_Type()
)
mplsTunnelErrorReporterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelErrorReporterType.setStatus("current")
_MplsTunnelErrorReporter_Type = InetAddress
_MplsTunnelErrorReporter_Object = MibTableColumn
mplsTunnelErrorReporter = _MplsTunnelErrorReporter_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 18, 1, 4),
    _MplsTunnelErrorReporter_Type()
)
mplsTunnelErrorReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelErrorReporter.setStatus("current")
_MplsTunnelErrorCode_Type = Unsigned32
_MplsTunnelErrorCode_Object = MibTableColumn
mplsTunnelErrorCode = _MplsTunnelErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 18, 1, 5),
    _MplsTunnelErrorCode_Type()
)
mplsTunnelErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelErrorCode.setStatus("current")
_MplsTunnelErrorSubcode_Type = Unsigned32
_MplsTunnelErrorSubcode_Object = MibTableColumn
mplsTunnelErrorSubcode = _MplsTunnelErrorSubcode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 18, 1, 6),
    _MplsTunnelErrorSubcode_Type()
)
mplsTunnelErrorSubcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelErrorSubcode.setStatus("current")


class _MplsTunnelErrorTLVs_Type(OctetString):
    """Custom type mplsTunnelErrorTLVs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MplsTunnelErrorTLVs_Type.__name__ = "OctetString"
_MplsTunnelErrorTLVs_Object = MibTableColumn
mplsTunnelErrorTLVs = _MplsTunnelErrorTLVs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 18, 1, 7),
    _MplsTunnelErrorTLVs_Type()
)
mplsTunnelErrorTLVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelErrorTLVs.setStatus("current")
_MplsTunnelErrorHelpString_Type = DisplayString
_MplsTunnelErrorHelpString_Object = MibTableColumn
mplsTunnelErrorHelpString = _MplsTunnelErrorHelpString_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 18, 1, 8),
    _MplsTunnelErrorHelpString_Type()
)
mplsTunnelErrorHelpString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelErrorHelpString.setStatus("current")
_MplsTunnelHoldTimer_Type = Unsigned32
_MplsTunnelHoldTimer_Object = MibScalar
mplsTunnelHoldTimer = _MplsTunnelHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 1, 19),
    _MplsTunnelHoldTimer_Type()
)
mplsTunnelHoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelHoldTimer.setStatus("current")
_MplsTeNotifications_ObjectIdentity = ObjectIdentity
mplsTeNotifications = _MplsTeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 2)
)
_MplsTeNotifyPrefix_ObjectIdentity = ObjectIdentity
mplsTeNotifyPrefix = _MplsTeNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 2, 0)
)
_MplsTeConformance_ObjectIdentity = ObjectIdentity
mplsTeConformance = _MplsTeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3)
)
_MplsTeGroups_ObjectIdentity = ObjectIdentity
mplsTeGroups = _MplsTeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1)
)
_MplsTeCompliances_ObjectIdentity = ObjectIdentity
mplsTeCompliances = _MplsTeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 2)
)
mplsTunnelEntry.registerAugmentions(
    ("PRVT-MPLS-TE-MIB",
     "mplsTunnelPerfEntry")
)
mplsTunnelPerfEntry.setIndexNames(*mplsTunnelEntry.getIndexNames())
mplsTunnelEntry.registerAugmentions(
    ("PRVT-MPLS-TE-MIB",
     "mplsTunnelErrorEntry")
)
mplsTunnelErrorEntry.setIndexNames(*mplsTunnelEntry.getIndexNames())

# Managed Objects groups

mplsTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1, 1)
)
mplsTunnelGroup.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelIndexNextIndex"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelName"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelDescr"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelOwner"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelXCPointer"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelIfIndex"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopTableIndex"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopTableIndex"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopTableIndex"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelOperStatus"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelRowStatus"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelStorageType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelDirection"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelLSPEncoding"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelLinkProtection"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelGPid"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUseEgressLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelEgressLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelEgressLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelOmitEROIfOneHop"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelPrivateData"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSrcTNAAddressType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSrcTNAAddress"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelDestTNAAddressType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelDestTNAAddress"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSecondary"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUnnumIf"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelAttributes"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelEndToEndRerouting"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelIsUni"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniServiceLevel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniEgressLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniEgressLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniEgressLabelPort"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniRvsEgressLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniRvsEgressLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniRvsEgressLabelPort"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSwitchingType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelDeletionMode"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniDiversityListIndex"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelDiffServIndex"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelReversePrivateData"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelAdminStatusFlags"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelFastRerouteMode"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelBackupSetupPrio"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelBackupHoldingPriority"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelBackupIncAny"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelBackupIncAll"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelBackupExcAny"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelBackupBandwidth"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelBackupMaxHops"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelDownNotRecipType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelDownNotRecip"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelPathComp"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUpNotRecipType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUpNotRecip"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelExtraParamsPtr"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelIsSpc"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniIngressLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniIngressLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniIngressLabelPort"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniRvsIngrLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniRvsIngrLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniRvsIngrLabelPort"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelDiffServClassType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelExtendedProtection"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelProtecting"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelNotification"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelLspProtection"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelAssociatedLspId"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCallIdType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCallId"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelIsIpv6"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelConfigured"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelActive"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelPrimaryInstance"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelPrimaryUpTime"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelPathChanges"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelLastPathChange"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCreationTime"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelStateTransitions"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelIncludeAnyAffinity"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelIncludeAllAffinity"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelExcludeAnyAffinity"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelResourcePointer"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelInstancePriority"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelPathInUse"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelRole"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelTotalUpTime"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelInstanceUpTime"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelResourceMaxRate"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelResourceMeanRate"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelResourceMaxBurstSize"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelResourceMeanBurstSize"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelResourceExBurstSize"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelResourceFrequency"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelResourceWeight"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelResourceRowStatus"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelResourceStorageType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelResourceIndexNextIndex"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSonetResRCC"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSonetResNCC"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSonetResNVC"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSonetResMultiplier"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSonetResTransparency"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSonetResRowStatus"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopAddrType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopIpAddr"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopAddrUnnum"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopLspId"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopAddrType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopIpAddr"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopIpPrefixLen"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopAsNumber"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopAddrUnnum"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopLspId"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelTrapEnable"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelErrorLastErrorType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelErrorLastTime"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelErrorReporterType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelErrorReporter"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelErrorCode"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelErrorSubcode"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelErrorTLVs"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelErrorHelpString"))
)
if mibBuilder.loadTexts:
    mplsTunnelGroup.setStatus("current")

mplsTunnelManualGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1, 2)
)
mplsTunnelManualGroup.setObjects(
    ("PRVT-MPLS-TE-MIB", "mplsTunnelSignallingProto")
)
if mibBuilder.loadTexts:
    mplsTunnelManualGroup.setStatus("current")

mplsTunnelSignaledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1, 3)
)
mplsTunnelSignaledGroup.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelSetupPrio"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHoldingPrio"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSignallingProto"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelLocalProtectInUse"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSessionAttributes"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopAddrType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopIpAddr"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopIpPrefixLen"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopAddrUnnum"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopAsNumber"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopLspId"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopInclude"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopPathOptionName"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopEntryPathComp"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopRowStatus"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopStorageType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopLabelStatuses"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopExpLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopExpLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopExpRvrsLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopExpRvrsLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelHopIndexNextIndex"))
)
if mibBuilder.loadTexts:
    mplsTunnelSignaledGroup.setStatus("current")

mplsTunnelScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1, 4)
)
mplsTunnelScalarGroup.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelConfigured"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelActive"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelTEDistProto"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelMaxHops"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelNotificationMaxRate"))
)
if mibBuilder.loadTexts:
    mplsTunnelScalarGroup.setStatus("current")

mplsTunnelIsIntfcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1, 5)
)
mplsTunnelIsIntfcGroup.setObjects(
    ("PRVT-MPLS-TE-MIB", "mplsTunnelIsIf")
)
if mibBuilder.loadTexts:
    mplsTunnelIsIntfcGroup.setStatus("current")

mplsTunnelIsNotIntfcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1, 6)
)
mplsTunnelIsNotIntfcGroup.setObjects(
    ("PRVT-MPLS-TE-MIB", "mplsTunnelIsIf")
)
if mibBuilder.loadTexts:
    mplsTunnelIsNotIntfcGroup.setStatus("current")

mplsTunnelCRLDPResOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1, 7)
)
mplsTunnelCRLDPResOptionalGroup.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelCRLDPResMeanBurstSize"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCRLDPResExBurstSize"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCRLDPResFrequency"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCRLDPResWeight"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCRLDPResFlags"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCRLDPResRowStatus"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCRLDPResStorageType"))
)
if mibBuilder.loadTexts:
    mplsTunnelCRLDPResOptionalGroup.setStatus("current")

mplsTunnelSonetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1, 8)
)
mplsTunnelSonetGroup.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelSonetResSignalType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSonetResRCC"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSonetResNCC"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSonetResNVC"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSonetResMultiplier"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSonetResTransparency"))
)
if mibBuilder.loadTexts:
    mplsTunnelSonetGroup.setStatus("current")

mplsTunnelUniGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1, 9)
)
mplsTunnelUniGroup.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelIsUni"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniServiceLevel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniEgressLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniEgressLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniEgressLabelPort"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniRvsEgressLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniRvsEgressLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniRvsEgressLabelPort"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniDiversityListIndex"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniIngressLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniIngressLabelPort"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniIngressLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniRvsIngrLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniRvsIngrLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniRvsIngrLabelPort"))
)
if mibBuilder.loadTexts:
    mplsTunnelUniGroup.setStatus("current")

mplsTunnelBackupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1, 11)
)
mplsTunnelBackupGroup.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelBackupSetupPrio"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelBackupHoldingPriority"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelBackupIncAny"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelBackupIncAll"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelBackupExcAny"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelBackupBandwidth"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelBackupMaxHops"))
)
if mibBuilder.loadTexts:
    mplsTunnelBackupGroup.setStatus("current")

mplsTunnelARHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1, 12)
)
mplsTunnelARHopGroup.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelARHopAddrType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopIpAddr"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopAddrUnnum"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopLspId"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopLabelStatuses"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopExpLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopExpLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopExpRvrsLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopExpRvrsLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopProtection"))
)
if mibBuilder.loadTexts:
    mplsTunnelARHopGroup.setStatus("current")

mplsTunnelCHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1, 13)
)
mplsTunnelCHopGroup.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelCHopAddrType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopIpAddr"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopIpPrefixLen"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopAsNumber"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopAddrUnnum"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopLspId"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopLabelStatuses"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopExpLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopExpLabel"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopExpRvrsLabelType"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopExpRvrsLabel"))
)
if mibBuilder.loadTexts:
    mplsTunnelCHopGroup.setStatus("current")

mplsDiffServGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1, 14)
)
mplsDiffServGroup.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsDiffServIndexNextIndex"),
        ("PRVT-MPLS-TE-MIB", "mplsDiffServType"),
        ("PRVT-MPLS-TE-MIB", "mplsDiffServLLSPPSC"),
        ("PRVT-MPLS-TE-MIB", "mplsDiffServELSPNumPHBs"),
        ("PRVT-MPLS-TE-MIB", "mplsDiffServELSPPHB0"),
        ("PRVT-MPLS-TE-MIB", "mplsDiffServELSPPHB1"),
        ("PRVT-MPLS-TE-MIB", "mplsDiffServELSPPHB2"),
        ("PRVT-MPLS-TE-MIB", "mplsDiffServELSPPHB3"),
        ("PRVT-MPLS-TE-MIB", "mplsDiffServELSPPHB4"),
        ("PRVT-MPLS-TE-MIB", "mplsDiffServELSPPHB5"),
        ("PRVT-MPLS-TE-MIB", "mplsDiffServELSPPHB6"),
        ("PRVT-MPLS-TE-MIB", "mplsDiffServELSPPHB7"),
        ("PRVT-MPLS-TE-MIB", "mplsDiffServRowStatus"))
)
if mibBuilder.loadTexts:
    mplsDiffServGroup.setStatus("current")


# Notification objects

mplsTunnelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 2, 0, 1)
)
mplsTunnelUp.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelUp.setStatus(
        "current"
    )

mplsTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 2, 0, 2)
)
mplsTunnelDown.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelOperStatus"))
)
if mibBuilder.loadTexts:
    mplsTunnelDown.setStatus(
        "current"
    )

mplsTunnelRerouted = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 2, 0, 3)
)
mplsTunnelRerouted.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelOperStatus"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopTableIndex"))
)
if mibBuilder.loadTexts:
    mplsTunnelRerouted.setStatus(
        "current"
    )

mplsTunnelReoptimized = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 2, 0, 4)
)
mplsTunnelReoptimized.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelAdminStatus"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelOperStatus"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopTableIndex"))
)
if mibBuilder.loadTexts:
    mplsTunnelReoptimized.setStatus(
        "current"
    )


# Notifications groups

mplsTeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 1, 15)
)
mplsTeNotificationGroup.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelUp"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelDown"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelRerouted"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelReoptimized"))
)
if mibBuilder.loadTexts:
    mplsTeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mplsTeModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 2, 1)
)
mplsTeModuleFullCompliance.setObjects(
      *(("IF-MIB", "ifGeneralInformationGroup"),
        ("IF-MIB", "ifCounterDiscontinuityGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelScalarGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelManualGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSignaledGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelIsNotIntfcGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelIsIntfcGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCRLDPResOptionalGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSonetGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelUniGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelBackupGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelARHopGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCHopGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsDiffServGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTeNotificationGroup"))
)
if mibBuilder.loadTexts:
    mplsTeModuleFullCompliance.setStatus(
        "current"
    )

mplsTeModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 2, 3, 2, 2)
)
mplsTeModuleReadOnlyCompliance.setObjects(
      *(("PRVT-MPLS-TE-MIB", "mplsTunnelGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelScalarGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelManualGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelSignaledGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelIsNotIntfcGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelIsIntfcGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTunnelCRLDPResOptionalGroup"),
        ("PRVT-MPLS-TE-MIB", "mplsTeNotificationGroup"))
)
if mibBuilder.loadTexts:
    mplsTeModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-MPLS-TE-MIB",
    **{"MplsTunnelIndexSyntax": MplsTunnelIndexSyntax,
       "MplsLsrId": MplsLsrId,
       "MplsGeneralizedLabelType": MplsGeneralizedLabelType,
       "MplsTunnelPrivateDataSyntax": MplsTunnelPrivateDataSyntax,
       "MplsTunnelTNAAddress": MplsTunnelTNAAddress,
       "MplsGeneralizedLabel": MplsGeneralizedLabel,
       "mplsTeMIB": mplsTeMIB,
       "mplsTeObjects": mplsTeObjects,
       "mplsTunnelIndexNextTable": mplsTunnelIndexNextTable,
       "mplsTunnelIndexNextEntry": mplsTunnelIndexNextEntry,
       "mplsTunnelIndexNextIndex": mplsTunnelIndexNextIndex,
       "mplsTunnelTable": mplsTunnelTable,
       "mplsTunnelEntry": mplsTunnelEntry,
       "mplsTunnelIndex": mplsTunnelIndex,
       "mplsTunnelInstance": mplsTunnelInstance,
       "mplsTunnelIngressLSRId": mplsTunnelIngressLSRId,
       "mplsTunnelEgressLSRId": mplsTunnelEgressLSRId,
       "mplsTunnelName": mplsTunnelName,
       "mplsTunnelDescr": mplsTunnelDescr,
       "mplsTunnelIsIf": mplsTunnelIsIf,
       "mplsTunnelIfIndex": mplsTunnelIfIndex,
       "mplsTunnelOwner": mplsTunnelOwner,
       "mplsTunnelRole": mplsTunnelRole,
       "mplsTunnelXCPointer": mplsTunnelXCPointer,
       "mplsTunnelSignallingProto": mplsTunnelSignallingProto,
       "mplsTunnelSetupPrio": mplsTunnelSetupPrio,
       "mplsTunnelHoldingPrio": mplsTunnelHoldingPrio,
       "mplsTunnelSessionAttributes": mplsTunnelSessionAttributes,
       "mplsTunnelLocalProtectInUse": mplsTunnelLocalProtectInUse,
       "mplsTunnelResourcePointer": mplsTunnelResourcePointer,
       "mplsTunnelPrimaryInstance": mplsTunnelPrimaryInstance,
       "mplsTunnelInstancePriority": mplsTunnelInstancePriority,
       "mplsTunnelHopTableIndex": mplsTunnelHopTableIndex,
       "mplsTunnelPathInUse": mplsTunnelPathInUse,
       "mplsTunnelARHopTableIndex": mplsTunnelARHopTableIndex,
       "mplsTunnelCHopTableIndex": mplsTunnelCHopTableIndex,
       "mplsTunnelIncludeAnyAffinity": mplsTunnelIncludeAnyAffinity,
       "mplsTunnelIncludeAllAffinity": mplsTunnelIncludeAllAffinity,
       "mplsTunnelExcludeAnyAffinity": mplsTunnelExcludeAnyAffinity,
       "mplsTunnelTotalUpTime": mplsTunnelTotalUpTime,
       "mplsTunnelInstanceUpTime": mplsTunnelInstanceUpTime,
       "mplsTunnelPrimaryUpTime": mplsTunnelPrimaryUpTime,
       "mplsTunnelPathChanges": mplsTunnelPathChanges,
       "mplsTunnelLastPathChange": mplsTunnelLastPathChange,
       "mplsTunnelCreationTime": mplsTunnelCreationTime,
       "mplsTunnelStateTransitions": mplsTunnelStateTransitions,
       "mplsTunnelAdminStatus": mplsTunnelAdminStatus,
       "mplsTunnelOperStatus": mplsTunnelOperStatus,
       "mplsTunnelRowStatus": mplsTunnelRowStatus,
       "mplsTunnelStorageType": mplsTunnelStorageType,
       "mplsTunnelUnnumIf": mplsTunnelUnnumIf,
       "mplsTunnelAttributes": mplsTunnelAttributes,
       "mplsTunnelLSPEncoding": mplsTunnelLSPEncoding,
       "mplsTunnelSwitchingType": mplsTunnelSwitchingType,
       "mplsTunnelLinkProtection": mplsTunnelLinkProtection,
       "mplsTunnelGPid": mplsTunnelGPid,
       "mplsTunnelSecondary": mplsTunnelSecondary,
       "mplsTunnelDirection": mplsTunnelDirection,
       "mplsTunnelPathComp": mplsTunnelPathComp,
       "mplsTunnelUpNotRecip": mplsTunnelUpNotRecip,
       "mplsTunnelDownNotRecip": mplsTunnelDownNotRecip,
       "mplsTunnelAdminStatusFlags": mplsTunnelAdminStatusFlags,
       "mplsTunnelExtraParamsPtr": mplsTunnelExtraParamsPtr,
       "mplsTunnelUseEgressLabel": mplsTunnelUseEgressLabel,
       "mplsTunnelEgressLabel": mplsTunnelEgressLabel,
       "mplsTunnelEgressLabelType": mplsTunnelEgressLabelType,
       "mplsTunnelOmitEROIfOneHop": mplsTunnelOmitEROIfOneHop,
       "mplsTunnelPrivateData": mplsTunnelPrivateData,
       "mplsTunnelSrcTNAAddressType": mplsTunnelSrcTNAAddressType,
       "mplsTunnelSrcTNAAddress": mplsTunnelSrcTNAAddress,
       "mplsTunnelDestTNAAddressType": mplsTunnelDestTNAAddressType,
       "mplsTunnelDestTNAAddress": mplsTunnelDestTNAAddress,
       "mplsTunnelEndToEndRerouting": mplsTunnelEndToEndRerouting,
       "mplsTunnelIsUni": mplsTunnelIsUni,
       "mplsTunnelUniServiceLevel": mplsTunnelUniServiceLevel,
       "mplsTunnelUniEgressLabel": mplsTunnelUniEgressLabel,
       "mplsTunnelUniEgressLabelType": mplsTunnelUniEgressLabelType,
       "mplsTunnelUniEgressLabelPort": mplsTunnelUniEgressLabelPort,
       "mplsTunnelUniRvsEgressLabel": mplsTunnelUniRvsEgressLabel,
       "mplsTunnelUniRvsEgressLabelType": mplsTunnelUniRvsEgressLabelType,
       "mplsTunnelUniRvsEgressLabelPort": mplsTunnelUniRvsEgressLabelPort,
       "mplsTunnelDeletionMode": mplsTunnelDeletionMode,
       "mplsTunnelUniDiversityListIndex": mplsTunnelUniDiversityListIndex,
       "mplsTunnelDiffServIndex": mplsTunnelDiffServIndex,
       "mplsTunnelReversePrivateData": mplsTunnelReversePrivateData,
       "mplsTunnelFastRerouteMode": mplsTunnelFastRerouteMode,
       "mplsTunnelBackupSetupPrio": mplsTunnelBackupSetupPrio,
       "mplsTunnelBackupHoldingPriority": mplsTunnelBackupHoldingPriority,
       "mplsTunnelBackupIncAny": mplsTunnelBackupIncAny,
       "mplsTunnelBackupIncAll": mplsTunnelBackupIncAll,
       "mplsTunnelBackupExcAny": mplsTunnelBackupExcAny,
       "mplsTunnelBackupBandwidth": mplsTunnelBackupBandwidth,
       "mplsTunnelBackupMaxHops": mplsTunnelBackupMaxHops,
       "mplsTunnelIsSpc": mplsTunnelIsSpc,
       "mplsTunnelUniIngressLabel": mplsTunnelUniIngressLabel,
       "mplsTunnelUniIngressLabelType": mplsTunnelUniIngressLabelType,
       "mplsTunnelUniIngressLabelPort": mplsTunnelUniIngressLabelPort,
       "mplsTunnelUniRvsIngrLabel": mplsTunnelUniRvsIngrLabel,
       "mplsTunnelUniRvsIngrLabelType": mplsTunnelUniRvsIngrLabelType,
       "mplsTunnelUniRvsIngrLabelPort": mplsTunnelUniRvsIngrLabelPort,
       "mplsTunnelDiffServClassType": mplsTunnelDiffServClassType,
       "mplsTunnelExtendedProtection": mplsTunnelExtendedProtection,
       "mplsTunnelProtecting": mplsTunnelProtecting,
       "mplsTunnelNotification": mplsTunnelNotification,
       "mplsTunnelLspProtection": mplsTunnelLspProtection,
       "mplsTunnelAssociatedLspId": mplsTunnelAssociatedLspId,
       "mplsTunnelCallIdType": mplsTunnelCallIdType,
       "mplsTunnelCallId": mplsTunnelCallId,
       "mplsTunnelIsIpv6": mplsTunnelIsIpv6,
       "mplsTunnelUpNotRecipType": mplsTunnelUpNotRecipType,
       "mplsTunnelDownNotRecipType": mplsTunnelDownNotRecipType,
       "mplsTunnelMtu": mplsTunnelMtu,
       "mplsTunnelRebuildTimer": mplsTunnelRebuildTimer,
       "mplsTunnelOperStatusFlags": mplsTunnelOperStatusFlags,
       "mplsTunnelGuardedDest": mplsTunnelGuardedDest,
       "mplsTunnelMBBTimeOut": mplsTunnelMBBTimeOut,
       "mplsTunnelHopIndexNextTable": mplsTunnelHopIndexNextTable,
       "mplsTunnelHopIndexNextEntry": mplsTunnelHopIndexNextEntry,
       "mplsTunnelHopIndexNextIndex": mplsTunnelHopIndexNextIndex,
       "mplsTunnelHopTable": mplsTunnelHopTable,
       "mplsTunnelHopEntry": mplsTunnelHopEntry,
       "mplsTunnelHopListIndex": mplsTunnelHopListIndex,
       "mplsTunnelHopPathOptionIndex": mplsTunnelHopPathOptionIndex,
       "mplsTunnelHopIndex": mplsTunnelHopIndex,
       "mplsTunnelHopAddrType": mplsTunnelHopAddrType,
       "mplsTunnelHopIpAddr": mplsTunnelHopIpAddr,
       "mplsTunnelHopIpPrefixLen": mplsTunnelHopIpPrefixLen,
       "mplsTunnelHopAsNumber": mplsTunnelHopAsNumber,
       "mplsTunnelHopAddrUnnum": mplsTunnelHopAddrUnnum,
       "mplsTunnelHopLspId": mplsTunnelHopLspId,
       "mplsTunnelHopType": mplsTunnelHopType,
       "mplsTunnelHopInclude": mplsTunnelHopInclude,
       "mplsTunnelHopPathOptionName": mplsTunnelHopPathOptionName,
       "mplsTunnelHopEntryPathComp": mplsTunnelHopEntryPathComp,
       "mplsTunnelHopRowStatus": mplsTunnelHopRowStatus,
       "mplsTunnelHopStorageType": mplsTunnelHopStorageType,
       "mplsTunnelHopLabelStatuses": mplsTunnelHopLabelStatuses,
       "mplsTunnelHopExpLabelType": mplsTunnelHopExpLabelType,
       "mplsTunnelHopExpLabel": mplsTunnelHopExpLabel,
       "mplsTunnelHopExpRvrsLabelType": mplsTunnelHopExpRvrsLabelType,
       "mplsTunnelHopExpRvrsLabel": mplsTunnelHopExpRvrsLabel,
       "mplsTunnelResourceIndexNextTable": mplsTunnelResourceIndexNextTable,
       "mplsTunnelResourceIndexNextEntry": mplsTunnelResourceIndexNextEntry,
       "mplsTunnelResourceIndexNextIndex": mplsTunnelResourceIndexNextIndex,
       "mplsTunnelResourceTable": mplsTunnelResourceTable,
       "mplsTunnelResourceEntry": mplsTunnelResourceEntry,
       "mplsTunnelResourceIndex": mplsTunnelResourceIndex,
       "mplsTunnelResourceMaxRate": mplsTunnelResourceMaxRate,
       "mplsTunnelResourceMeanRate": mplsTunnelResourceMeanRate,
       "mplsTunnelResourceMaxBurstSize": mplsTunnelResourceMaxBurstSize,
       "mplsTunnelResourceMeanBurstSize": mplsTunnelResourceMeanBurstSize,
       "mplsTunnelResourceExBurstSize": mplsTunnelResourceExBurstSize,
       "mplsTunnelResourceFrequency": mplsTunnelResourceFrequency,
       "mplsTunnelResourceWeight": mplsTunnelResourceWeight,
       "mplsTunnelResourceRowStatus": mplsTunnelResourceRowStatus,
       "mplsTunnelResourceStorageType": mplsTunnelResourceStorageType,
       "mplsTunnelARHopTable": mplsTunnelARHopTable,
       "mplsTunnelARHopEntry": mplsTunnelARHopEntry,
       "mplsTunnelARHopListIndex": mplsTunnelARHopListIndex,
       "mplsTunnelARHopIndex": mplsTunnelARHopIndex,
       "mplsTunnelARHopAddrType": mplsTunnelARHopAddrType,
       "mplsTunnelARHopIpAddr": mplsTunnelARHopIpAddr,
       "mplsTunnelARHopAddrUnnum": mplsTunnelARHopAddrUnnum,
       "mplsTunnelARHopLspId": mplsTunnelARHopLspId,
       "mplsTunnelARHopLabelStatuses": mplsTunnelARHopLabelStatuses,
       "mplsTunnelARHopExpLabelType": mplsTunnelARHopExpLabelType,
       "mplsTunnelARHopExpLabel": mplsTunnelARHopExpLabel,
       "mplsTunnelARHopExpRvrsLabelType": mplsTunnelARHopExpRvrsLabelType,
       "mplsTunnelARHopExpRvrsLabel": mplsTunnelARHopExpRvrsLabel,
       "mplsTunnelARHopProtection": mplsTunnelARHopProtection,
       "mplsTunnelCHopTable": mplsTunnelCHopTable,
       "mplsTunnelCHopEntry": mplsTunnelCHopEntry,
       "mplsTunnelCHopListIndex": mplsTunnelCHopListIndex,
       "mplsTunnelCHopIndex": mplsTunnelCHopIndex,
       "mplsTunnelCHopAddrType": mplsTunnelCHopAddrType,
       "mplsTunnelCHopIpAddr": mplsTunnelCHopIpAddr,
       "mplsTunnelCHopIpPrefixLen": mplsTunnelCHopIpPrefixLen,
       "mplsTunnelCHopAsNumber": mplsTunnelCHopAsNumber,
       "mplsTunnelCHopAddrUnnum": mplsTunnelCHopAddrUnnum,
       "mplsTunnelCHopLspId": mplsTunnelCHopLspId,
       "mplsTunnelCHopType": mplsTunnelCHopType,
       "mplsTunnelCHopLabelStatuses": mplsTunnelCHopLabelStatuses,
       "mplsTunnelCHopExpLabelType": mplsTunnelCHopExpLabelType,
       "mplsTunnelCHopExpLabel": mplsTunnelCHopExpLabel,
       "mplsTunnelCHopExpRvrsLabelType": mplsTunnelCHopExpRvrsLabelType,
       "mplsTunnelCHopExpRvrsLabel": mplsTunnelCHopExpRvrsLabel,
       "mplsTunnelPerfTable": mplsTunnelPerfTable,
       "mplsTunnelPerfEntry": mplsTunnelPerfEntry,
       "mplsTunnelPerfPackets": mplsTunnelPerfPackets,
       "mplsTunnelPerfHCPackets": mplsTunnelPerfHCPackets,
       "mplsTunnelPerfErrors": mplsTunnelPerfErrors,
       "mplsTunnelPerfBytes": mplsTunnelPerfBytes,
       "mplsTunnelPerfHCBytes": mplsTunnelPerfHCBytes,
       "mplsTunnelCRLDPResTable": mplsTunnelCRLDPResTable,
       "mplsTunnelCRLDPResEntry": mplsTunnelCRLDPResEntry,
       "mplsTunnelCRLDPResMeanBurstSize": mplsTunnelCRLDPResMeanBurstSize,
       "mplsTunnelCRLDPResExBurstSize": mplsTunnelCRLDPResExBurstSize,
       "mplsTunnelCRLDPResFrequency": mplsTunnelCRLDPResFrequency,
       "mplsTunnelCRLDPResWeight": mplsTunnelCRLDPResWeight,
       "mplsTunnelCRLDPResFlags": mplsTunnelCRLDPResFlags,
       "mplsTunnelCRLDPResRowStatus": mplsTunnelCRLDPResRowStatus,
       "mplsTunnelCRLDPResStorageType": mplsTunnelCRLDPResStorageType,
       "mplsDiffServIndexNextTable": mplsDiffServIndexNextTable,
       "mplsDiffServIndexNextEntry": mplsDiffServIndexNextEntry,
       "mplsDiffServIndexNextIndex": mplsDiffServIndexNextIndex,
       "mplsDiffServTable": mplsDiffServTable,
       "mplsDiffServEntry": mplsDiffServEntry,
       "mplsDiffServIndex": mplsDiffServIndex,
       "mplsDiffServType": mplsDiffServType,
       "mplsDiffServLLSPPSC": mplsDiffServLLSPPSC,
       "mplsDiffServELSPNumPHBs": mplsDiffServELSPNumPHBs,
       "mplsDiffServELSPPHB0": mplsDiffServELSPPHB0,
       "mplsDiffServELSPPHB1": mplsDiffServELSPPHB1,
       "mplsDiffServELSPPHB2": mplsDiffServELSPPHB2,
       "mplsDiffServELSPPHB3": mplsDiffServELSPPHB3,
       "mplsDiffServELSPPHB4": mplsDiffServELSPPHB4,
       "mplsDiffServELSPPHB5": mplsDiffServELSPPHB5,
       "mplsDiffServELSPPHB6": mplsDiffServELSPPHB6,
       "mplsDiffServELSPPHB7": mplsDiffServELSPPHB7,
       "mplsDiffServRowStatus": mplsDiffServRowStatus,
       "prvtMplsTunnelUNIDvLstIdxNxtTable": prvtMplsTunnelUNIDvLstIdxNxtTable,
       "prvtMplsTunnelUNIDvLstIdxNxtEntry": prvtMplsTunnelUNIDvLstIdxNxtEntry,
       "prvtMplsTunnelUNIDivListIdxNext": prvtMplsTunnelUNIDivListIdxNext,
       "prvtMplsTunnelUNIDiversityTable": prvtMplsTunnelUNIDiversityTable,
       "prvtMplsTunnelUNIDiversityEntry": prvtMplsTunnelUNIDiversityEntry,
       "prvtMplsTunnelUNIDivListIdx": prvtMplsTunnelUNIDivListIdx,
       "prvtMplsTunnelUNIDivIdx": prvtMplsTunnelUNIDivIdx,
       "prvtMplsTunnelUNIDivRowPointer": prvtMplsTunnelUNIDivRowPointer,
       "prvtMplsTunnelOperStatus": prvtMplsTunnelOperStatus,
       "prvtMplsTunnelUNIDivRowStatus": prvtMplsTunnelUNIDivRowStatus,
       "prvtMplsTunnelUNIDivRequirement": prvtMplsTunnelUNIDivRequirement,
       "prvtMplsTunnelUNIDivAccess": prvtMplsTunnelUNIDivAccess,
       "prvtMplsTunnelTrapEnableTable": prvtMplsTunnelTrapEnableTable,
       "prvtMplsTunnelTrapEnableEntry": prvtMplsTunnelTrapEnableEntry,
       "mplsTunnelTrapEnable": mplsTunnelTrapEnable,
       "mplsTeMibEntityScalarTable": mplsTeMibEntityScalarTable,
       "mplsTeMibEntityScalarEntry": mplsTeMibEntityScalarEntry,
       "mplsTunnelConfigured": mplsTunnelConfigured,
       "mplsTunnelActive": mplsTunnelActive,
       "mplsTunnelTEDistProto": mplsTunnelTEDistProto,
       "mplsTunnelMaxHops": mplsTunnelMaxHops,
       "mplsTunnelNotificationMaxRate": mplsTunnelNotificationMaxRate,
       "mplsTunnelSonetResTable": mplsTunnelSonetResTable,
       "mplsTunnelSonetResEntry": mplsTunnelSonetResEntry,
       "mplsTunnelSonetResRCC": mplsTunnelSonetResRCC,
       "mplsTunnelSonetResNCC": mplsTunnelSonetResNCC,
       "mplsTunnelSonetResNVC": mplsTunnelSonetResNVC,
       "mplsTunnelSonetResMultiplier": mplsTunnelSonetResMultiplier,
       "mplsTunnelSonetResTransparency": mplsTunnelSonetResTransparency,
       "mplsTunnelSonetResRowStatus": mplsTunnelSonetResRowStatus,
       "mplsTunnelSonetResSignalType": mplsTunnelSonetResSignalType,
       "mplsTunnelErrorTable": mplsTunnelErrorTable,
       "mplsTunnelErrorEntry": mplsTunnelErrorEntry,
       "mplsTunnelErrorLastErrorType": mplsTunnelErrorLastErrorType,
       "mplsTunnelErrorLastTime": mplsTunnelErrorLastTime,
       "mplsTunnelErrorReporterType": mplsTunnelErrorReporterType,
       "mplsTunnelErrorReporter": mplsTunnelErrorReporter,
       "mplsTunnelErrorCode": mplsTunnelErrorCode,
       "mplsTunnelErrorSubcode": mplsTunnelErrorSubcode,
       "mplsTunnelErrorTLVs": mplsTunnelErrorTLVs,
       "mplsTunnelErrorHelpString": mplsTunnelErrorHelpString,
       "mplsTunnelHoldTimer": mplsTunnelHoldTimer,
       "mplsTeNotifications": mplsTeNotifications,
       "mplsTeNotifyPrefix": mplsTeNotifyPrefix,
       "mplsTunnelUp": mplsTunnelUp,
       "mplsTunnelDown": mplsTunnelDown,
       "mplsTunnelRerouted": mplsTunnelRerouted,
       "mplsTunnelReoptimized": mplsTunnelReoptimized,
       "mplsTeConformance": mplsTeConformance,
       "mplsTeGroups": mplsTeGroups,
       "mplsTunnelGroup": mplsTunnelGroup,
       "mplsTunnelManualGroup": mplsTunnelManualGroup,
       "mplsTunnelSignaledGroup": mplsTunnelSignaledGroup,
       "mplsTunnelScalarGroup": mplsTunnelScalarGroup,
       "mplsTunnelIsIntfcGroup": mplsTunnelIsIntfcGroup,
       "mplsTunnelIsNotIntfcGroup": mplsTunnelIsNotIntfcGroup,
       "mplsTunnelCRLDPResOptionalGroup": mplsTunnelCRLDPResOptionalGroup,
       "mplsTunnelSonetGroup": mplsTunnelSonetGroup,
       "mplsTunnelUniGroup": mplsTunnelUniGroup,
       "mplsTunnelBackupGroup": mplsTunnelBackupGroup,
       "mplsTunnelARHopGroup": mplsTunnelARHopGroup,
       "mplsTunnelCHopGroup": mplsTunnelCHopGroup,
       "mplsDiffServGroup": mplsDiffServGroup,
       "mplsTeNotificationGroup": mplsTeNotificationGroup,
       "mplsTeCompliances": mplsTeCompliances,
       "mplsTeModuleFullCompliance": mplsTeModuleFullCompliance,
       "mplsTeModuleReadOnlyCompliance": mplsTeModuleReadOnlyCompliance}
)
