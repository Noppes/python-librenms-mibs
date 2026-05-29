# SNMP MIB module (ALCATEL-IND1-E-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\aos6\ALCATEL-IND1-E-SERVICE-MIB

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

(softentIND1eService,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1eService")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1EServiceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1EServiceMIB.setRevisions(
        ("2010-01-19 00:00",
         "2019-10-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaEServiceUNIProfileProtocolTreatment(TextualConvention, Integer32):
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
        *(("tunnel", 1),
          ("drop", 2),
          ("peer", 3),
          ("macTunnel", 4))
    )



class AlaEServiceL2CustomProtocolType(TextualConvention, Integer32):
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
        *(("maskType", 1),
          ("macType", 2),
          ("ssapdsapType", 3),
          ("etherType", 4),
          ("ethersubType", 5))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1eServiceMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1eServiceMIBObjects = _AlcatelIND1eServiceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1eServiceMIBObjects.setStatus("current")
_AlaEService_ObjectIdentity = ObjectIdentity
alaEService = _AlaEService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1)
)
_AlaEServiceInfo_ObjectIdentity = ObjectIdentity
alaEServiceInfo = _AlaEServiceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 1)
)


class _AlaEServiceMode_Type(Integer32):
    """Custom type alaEServiceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("legacyMode", 1),
          ("eServiceMode", 2))
    )


_AlaEServiceMode_Type.__name__ = "Integer32"
_AlaEServiceMode_Object = MibScalar
alaEServiceMode = _AlaEServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 1, 1),
    _AlaEServiceMode_Type()
)
alaEServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServiceMode.setStatus("current")


class _AlaEServiceStatReset_Type(Integer32):
    """Custom type alaEServiceStatReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaEServiceStatReset_Type.__name__ = "Integer32"
_AlaEServiceStatReset_Object = MibScalar
alaEServiceStatReset = _AlaEServiceStatReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 1, 2),
    _AlaEServiceStatReset_Type()
)
alaEServiceStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServiceStatReset.setStatus("current")


class _AlaEServiceL2MacTunnel_Type(Integer32):
    """Custom type alaEServiceL2MacTunnel based on Integer32"""
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


_AlaEServiceL2MacTunnel_Type.__name__ = "Integer32"
_AlaEServiceL2MacTunnel_Object = MibScalar
alaEServiceL2MacTunnel = _AlaEServiceL2MacTunnel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 1, 3),
    _AlaEServiceL2MacTunnel_Type()
)
alaEServiceL2MacTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServiceL2MacTunnel.setStatus("current")


class _AlaEServiceUntaggedMode_Type(Integer32):
    """Custom type alaEServiceUntaggedMode based on Integer32"""
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


_AlaEServiceUntaggedMode_Type.__name__ = "Integer32"
_AlaEServiceUntaggedMode_Object = MibScalar
alaEServiceUntaggedMode = _AlaEServiceUntaggedMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 1, 4),
    _AlaEServiceUntaggedMode_Type()
)
alaEServiceUntaggedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServiceUntaggedMode.setStatus("current")
_AlaEServiceSapProfileTable_Object = MibTable
alaEServiceSapProfileTable = _AlaEServiceSapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaEServiceSapProfileTable.setStatus("current")
_AlaEServiceSapProfileEntry_Object = MibTableRow
alaEServiceSapProfileEntry = _AlaEServiceSapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1)
)
alaEServiceSapProfileEntry.setIndexNames(
    (1, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileID"),
)
if mibBuilder.loadTexts:
    alaEServiceSapProfileEntry.setStatus("current")


class _AlaEServiceSapProfileID_Type(DisplayString):
    """Custom type alaEServiceSapProfileID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServiceSapProfileID_Type.__name__ = "DisplayString"
_AlaEServiceSapProfileID_Object = MibTableColumn
alaEServiceSapProfileID = _AlaEServiceSapProfileID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 1),
    _AlaEServiceSapProfileID_Type()
)
alaEServiceSapProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapProfileID.setStatus("current")


class _AlaEServiceSapProfileCVLANTreatment_Type(Integer32):
    """Custom type alaEServiceSapProfileCVLANTreatment based on Integer32"""
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
        *(("stackSVLAN", 1),
          ("translate", 2),
          ("changeCVLAN", 3))
    )


_AlaEServiceSapProfileCVLANTreatment_Type.__name__ = "Integer32"
_AlaEServiceSapProfileCVLANTreatment_Object = MibTableColumn
alaEServiceSapProfileCVLANTreatment = _AlaEServiceSapProfileCVLANTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 2),
    _AlaEServiceSapProfileCVLANTreatment_Type()
)
alaEServiceSapProfileCVLANTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileCVLANTreatment.setStatus("current")


class _AlaEServiceSapProfileReplacementCVLAN_Type(Integer32):
    """Custom type alaEServiceSapProfileReplacementCVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaEServiceSapProfileReplacementCVLAN_Type.__name__ = "Integer32"
_AlaEServiceSapProfileReplacementCVLAN_Object = MibTableColumn
alaEServiceSapProfileReplacementCVLAN = _AlaEServiceSapProfileReplacementCVLAN_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 3),
    _AlaEServiceSapProfileReplacementCVLAN_Type()
)
alaEServiceSapProfileReplacementCVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileReplacementCVLAN.setStatus("current")


class _AlaEServiceSapProfilePriorityMapMode_Type(Integer32):
    """Custom type alaEServiceSapProfilePriorityMapMode based on Integer32"""
    defaultValue = 3

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
        *(("notAssigned", 0),
          ("mapInnerPtoOuterP", 1),
          ("mapInnerDscpToOuterP", 2),
          ("fixedP", 3))
    )


_AlaEServiceSapProfilePriorityMapMode_Type.__name__ = "Integer32"
_AlaEServiceSapProfilePriorityMapMode_Object = MibTableColumn
alaEServiceSapProfilePriorityMapMode = _AlaEServiceSapProfilePriorityMapMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 4),
    _AlaEServiceSapProfilePriorityMapMode_Type()
)
alaEServiceSapProfilePriorityMapMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfilePriorityMapMode.setStatus("current")


class _AlaEServiceSapProfileFixedPriority_Type(Integer32):
    """Custom type alaEServiceSapProfileFixedPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaEServiceSapProfileFixedPriority_Type.__name__ = "Integer32"
_AlaEServiceSapProfileFixedPriority_Object = MibTableColumn
alaEServiceSapProfileFixedPriority = _AlaEServiceSapProfileFixedPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 5),
    _AlaEServiceSapProfileFixedPriority_Type()
)
alaEServiceSapProfileFixedPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileFixedPriority.setStatus("current")
_AlaEServiceSapProfileIngressBW_Type = Integer32
_AlaEServiceSapProfileIngressBW_Object = MibTableColumn
alaEServiceSapProfileIngressBW = _AlaEServiceSapProfileIngressBW_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 6),
    _AlaEServiceSapProfileIngressBW_Type()
)
alaEServiceSapProfileIngressBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileIngressBW.setStatus("current")


class _AlaEServiceSapProfileBandwidthShare_Type(Integer32):
    """Custom type alaEServiceSapProfileBandwidthShare based on Integer32"""
    defaultValue = 1

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
        *(("notApplicable", 0),
          ("shared", 1),
          ("notShared", 2),
          ("notAssigned", 3))
    )


_AlaEServiceSapProfileBandwidthShare_Type.__name__ = "Integer32"
_AlaEServiceSapProfileBandwidthShare_Object = MibTableColumn
alaEServiceSapProfileBandwidthShare = _AlaEServiceSapProfileBandwidthShare_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 7),
    _AlaEServiceSapProfileBandwidthShare_Type()
)
alaEServiceSapProfileBandwidthShare.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileBandwidthShare.setStatus("current")
_AlaEServiceSapProfileRowStatus_Type = RowStatus
_AlaEServiceSapProfileRowStatus_Object = MibTableColumn
alaEServiceSapProfileRowStatus = _AlaEServiceSapProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 8),
    _AlaEServiceSapProfileRowStatus_Type()
)
alaEServiceSapProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileRowStatus.setStatus("current")


class _AlaEServiceSapProfileEgressBW_Type(Integer32):
    """Custom type alaEServiceSapProfileEgressBW based on Integer32"""
    defaultValue = 0


_AlaEServiceSapProfileEgressBW_Type.__name__ = "Integer32"
_AlaEServiceSapProfileEgressBW_Object = MibTableColumn
alaEServiceSapProfileEgressBW = _AlaEServiceSapProfileEgressBW_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 9),
    _AlaEServiceSapProfileEgressBW_Type()
)
alaEServiceSapProfileEgressBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileEgressBW.setStatus("current")


class _AlaEServiceSapProfileCIR_Type(Integer32):
    """Custom type alaEServiceSapProfileCIR based on Integer32"""
    defaultValue = 0


_AlaEServiceSapProfileCIR_Type.__name__ = "Integer32"
_AlaEServiceSapProfileCIR_Object = MibTableColumn
alaEServiceSapProfileCIR = _AlaEServiceSapProfileCIR_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 10),
    _AlaEServiceSapProfileCIR_Type()
)
alaEServiceSapProfileCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileCIR.setStatus("current")


class _AlaEServiceSapProfileCBS_Type(Integer32):
    """Custom type alaEServiceSapProfileCBS based on Integer32"""
    defaultValue = 0


_AlaEServiceSapProfileCBS_Type.__name__ = "Integer32"
_AlaEServiceSapProfileCBS_Object = MibTableColumn
alaEServiceSapProfileCBS = _AlaEServiceSapProfileCBS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 11),
    _AlaEServiceSapProfileCBS_Type()
)
alaEServiceSapProfileCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileCBS.setStatus("current")


class _AlaEServiceSapProfilePIR_Type(Integer32):
    """Custom type alaEServiceSapProfilePIR based on Integer32"""
    defaultValue = 0


_AlaEServiceSapProfilePIR_Type.__name__ = "Integer32"
_AlaEServiceSapProfilePIR_Object = MibTableColumn
alaEServiceSapProfilePIR = _AlaEServiceSapProfilePIR_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 12),
    _AlaEServiceSapProfilePIR_Type()
)
alaEServiceSapProfilePIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfilePIR.setStatus("current")


class _AlaEServiceSapProfilePBS_Type(Integer32):
    """Custom type alaEServiceSapProfilePBS based on Integer32"""
    defaultValue = 0


_AlaEServiceSapProfilePBS_Type.__name__ = "Integer32"
_AlaEServiceSapProfilePBS_Object = MibTableColumn
alaEServiceSapProfilePBS = _AlaEServiceSapProfilePBS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 13),
    _AlaEServiceSapProfilePBS_Type()
)
alaEServiceSapProfilePBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfilePBS.setStatus("current")


class _AlaEServiceSapProfileDepth_Type(Integer32):
    """Custom type alaEServiceSapProfileDepth based on Integer32"""
    defaultValue = 0


_AlaEServiceSapProfileDepth_Type.__name__ = "Integer32"
_AlaEServiceSapProfileDepth_Object = MibTableColumn
alaEServiceSapProfileDepth = _AlaEServiceSapProfileDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 2, 1, 14),
    _AlaEServiceSapProfileDepth_Type()
)
alaEServiceSapProfileDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileDepth.setStatus("current")
_AlaEServiceUNIProfileTable_Object = MibTable
alaEServiceUNIProfileTable = _AlaEServiceUNIProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileTable.setStatus("current")
_AlaEServiceUNIProfileEntry_Object = MibTableRow
alaEServiceUNIProfileEntry = _AlaEServiceUNIProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1)
)
alaEServiceUNIProfileEntry.setIndexNames(
    (1, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileID"),
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileEntry.setStatus("current")


class _AlaEServiceUNIProfileID_Type(DisplayString):
    """Custom type alaEServiceUNIProfileID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServiceUNIProfileID_Type.__name__ = "DisplayString"
_AlaEServiceUNIProfileID_Object = MibTableColumn
alaEServiceUNIProfileID = _AlaEServiceUNIProfileID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 1),
    _AlaEServiceUNIProfileID_Type()
)
alaEServiceUNIProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileID.setStatus("current")


class _AlaEServiceUNIProfileStpBpduTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileStpBpduTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 1


_AlaEServiceUNIProfileStpBpduTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileStpBpduTreatment_Object = MibTableColumn
alaEServiceUNIProfileStpBpduTreatment = _AlaEServiceUNIProfileStpBpduTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 2),
    _AlaEServiceUNIProfileStpBpduTreatment_Type()
)
alaEServiceUNIProfileStpBpduTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileStpBpduTreatment.setStatus("current")


class _AlaEServiceUNIProfile8021xTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfile8021xTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfile8021xTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfile8021xTreatment_Object = MibTableColumn
alaEServiceUNIProfile8021xTreatment = _AlaEServiceUNIProfile8021xTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 3),
    _AlaEServiceUNIProfile8021xTreatment_Type()
)
alaEServiceUNIProfile8021xTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfile8021xTreatment.setStatus("current")


class _AlaEServiceUNIProfile8021ABTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfile8021ABTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfile8021ABTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfile8021ABTreatment_Object = MibTableColumn
alaEServiceUNIProfile8021ABTreatment = _AlaEServiceUNIProfile8021ABTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 4),
    _AlaEServiceUNIProfile8021ABTreatment_Type()
)
alaEServiceUNIProfile8021ABTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfile8021ABTreatment.setStatus("current")


class _AlaEServiceUNIProfile8023adTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfile8023adTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 3


_AlaEServiceUNIProfile8023adTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfile8023adTreatment_Object = MibTableColumn
alaEServiceUNIProfile8023adTreatment = _AlaEServiceUNIProfile8023adTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 5),
    _AlaEServiceUNIProfile8023adTreatment_Type()
)
alaEServiceUNIProfile8023adTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfile8023adTreatment.setStatus("current")


class _AlaEServiceUNIProfileGvrpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileGvrpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 1


_AlaEServiceUNIProfileGvrpTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileGvrpTreatment_Object = MibTableColumn
alaEServiceUNIProfileGvrpTreatment = _AlaEServiceUNIProfileGvrpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 6),
    _AlaEServiceUNIProfileGvrpTreatment_Type()
)
alaEServiceUNIProfileGvrpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileGvrpTreatment.setStatus("current")


class _AlaEServiceUNIProfileAmapTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileAmapTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileAmapTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileAmapTreatment_Object = MibTableColumn
alaEServiceUNIProfileAmapTreatment = _AlaEServiceUNIProfileAmapTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 7),
    _AlaEServiceUNIProfileAmapTreatment_Type()
)
alaEServiceUNIProfileAmapTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileAmapTreatment.setStatus("current")
_AlaEServiceUNIProfileRowStatus_Type = RowStatus
_AlaEServiceUNIProfileRowStatus_Object = MibTableColumn
alaEServiceUNIProfileRowStatus = _AlaEServiceUNIProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 8),
    _AlaEServiceUNIProfileRowStatus_Type()
)
alaEServiceUNIProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileRowStatus.setStatus("current")


class _AlaEServiceUNIProfileMvrpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileMvrpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 1


_AlaEServiceUNIProfileMvrpTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileMvrpTreatment_Object = MibTableColumn
alaEServiceUNIProfileMvrpTreatment = _AlaEServiceUNIProfileMvrpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 9),
    _AlaEServiceUNIProfileMvrpTreatment_Type()
)
alaEServiceUNIProfileMvrpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileMvrpTreatment.setStatus("current")
_AlaEServiceUNIProfileTunnelMac_Type = MacAddress
_AlaEServiceUNIProfileTunnelMac_Object = MibTableColumn
alaEServiceUNIProfileTunnelMac = _AlaEServiceUNIProfileTunnelMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 10),
    _AlaEServiceUNIProfileTunnelMac_Type()
)
alaEServiceUNIProfileTunnelMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileTunnelMac.setStatus("current")


class _AlaEServiceUNIProfileLacpMarkerTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileLacpMarkerTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 3


_AlaEServiceUNIProfileLacpMarkerTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileLacpMarkerTreatment_Object = MibTableColumn
alaEServiceUNIProfileLacpMarkerTreatment = _AlaEServiceUNIProfileLacpMarkerTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 11),
    _AlaEServiceUNIProfileLacpMarkerTreatment_Type()
)
alaEServiceUNIProfileLacpMarkerTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileLacpMarkerTreatment.setStatus("current")


class _AlaEServiceUNIProfileOamTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileOamTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 3


_AlaEServiceUNIProfileOamTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileOamTreatment_Object = MibTableColumn
alaEServiceUNIProfileOamTreatment = _AlaEServiceUNIProfileOamTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 12),
    _AlaEServiceUNIProfileOamTreatment_Type()
)
alaEServiceUNIProfileOamTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileOamTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoPagpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoPagpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoPagpTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoPagpTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoPagpTreatment = _AlaEServiceUNIProfileCiscoPagpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 13),
    _AlaEServiceUNIProfileCiscoPagpTreatment_Type()
)
alaEServiceUNIProfileCiscoPagpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoPagpTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoUdldTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoUdldTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoUdldTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoUdldTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoUdldTreatment = _AlaEServiceUNIProfileCiscoUdldTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 14),
    _AlaEServiceUNIProfileCiscoUdldTreatment_Type()
)
alaEServiceUNIProfileCiscoUdldTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoUdldTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoCdpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoCdpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoCdpTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoCdpTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoCdpTreatment = _AlaEServiceUNIProfileCiscoCdpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 15),
    _AlaEServiceUNIProfileCiscoCdpTreatment_Type()
)
alaEServiceUNIProfileCiscoCdpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoCdpTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoVtpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoVtpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoVtpTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoVtpTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoVtpTreatment = _AlaEServiceUNIProfileCiscoVtpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 16),
    _AlaEServiceUNIProfileCiscoVtpTreatment_Type()
)
alaEServiceUNIProfileCiscoVtpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoVtpTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoDtpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoDtpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoDtpTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoDtpTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoDtpTreatment = _AlaEServiceUNIProfileCiscoDtpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 17),
    _AlaEServiceUNIProfileCiscoDtpTreatment_Type()
)
alaEServiceUNIProfileCiscoDtpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoDtpTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoPvstTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoPvstTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoPvstTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoPvstTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoPvstTreatment = _AlaEServiceUNIProfileCiscoPvstTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 18),
    _AlaEServiceUNIProfileCiscoPvstTreatment_Type()
)
alaEServiceUNIProfileCiscoPvstTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoPvstTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoVlanTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoVlanTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoVlanTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoVlanTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoVlanTreatment = _AlaEServiceUNIProfileCiscoVlanTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 19),
    _AlaEServiceUNIProfileCiscoVlanTreatment_Type()
)
alaEServiceUNIProfileCiscoVlanTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoVlanTreatment.setStatus("current")


class _AlaEServiceUNIProfileCiscoUplinkTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileCiscoUplinkTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 2


_AlaEServiceUNIProfileCiscoUplinkTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileCiscoUplinkTreatment_Object = MibTableColumn
alaEServiceUNIProfileCiscoUplinkTreatment = _AlaEServiceUNIProfileCiscoUplinkTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 20),
    _AlaEServiceUNIProfileCiscoUplinkTreatment_Type()
)
alaEServiceUNIProfileCiscoUplinkTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCiscoUplinkTreatment.setStatus("current")


class _AlaEServiceUNIProfileIeeeMacTreatment_Type(Integer32):
    """Custom type alaEServiceUNIProfileIeeeMacTreatment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ieeeFwdAll", 1),
          ("ieeeDropAll", 2))
    )


_AlaEServiceUNIProfileIeeeMacTreatment_Type.__name__ = "Integer32"
_AlaEServiceUNIProfileIeeeMacTreatment_Object = MibTableColumn
alaEServiceUNIProfileIeeeMacTreatment = _AlaEServiceUNIProfileIeeeMacTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 3, 1, 21),
    _AlaEServiceUNIProfileIeeeMacTreatment_Type()
)
alaEServiceUNIProfileIeeeMacTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileIeeeMacTreatment.setStatus("current")
_AlaEServiceTable_Object = MibTable
alaEServiceTable = _AlaEServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaEServiceTable.setStatus("current")
_AlaEServiceEntry_Object = MibTableRow
alaEServiceEntry = _AlaEServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1)
)
alaEServiceEntry.setIndexNames(
    (1, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceID"),
)
if mibBuilder.loadTexts:
    alaEServiceEntry.setStatus("current")


class _AlaEServiceID_Type(DisplayString):
    """Custom type alaEServiceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaEServiceID_Type.__name__ = "DisplayString"
_AlaEServiceID_Object = MibTableColumn
alaEServiceID = _AlaEServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 1),
    _AlaEServiceID_Type()
)
alaEServiceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceID.setStatus("current")


class _AlaEServiceSVLAN_Type(Integer32):
    """Custom type alaEServiceSVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaEServiceSVLAN_Type.__name__ = "Integer32"
_AlaEServiceSVLAN_Object = MibTableColumn
alaEServiceSVLAN = _AlaEServiceSVLAN_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 2),
    _AlaEServiceSVLAN_Type()
)
alaEServiceSVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSVLAN.setStatus("current")


class _AlaEServiceVlanType_Type(Integer32):
    """Custom type alaEServiceVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("svlan", 1),
          ("ipmvlan", 2))
    )


_AlaEServiceVlanType_Type.__name__ = "Integer32"
_AlaEServiceVlanType_Object = MibTableColumn
alaEServiceVlanType = _AlaEServiceVlanType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 3),
    _AlaEServiceVlanType_Type()
)
alaEServiceVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceVlanType.setStatus("current")
_AlaEServiceRowStatus_Type = RowStatus
_AlaEServiceRowStatus_Object = MibTableColumn
alaEServiceRowStatus = _AlaEServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 4),
    _AlaEServiceRowStatus_Type()
)
alaEServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceRowStatus.setStatus("current")
_AlaEServiceStatGreenCount_Type = Counter64
_AlaEServiceStatGreenCount_Object = MibTableColumn
alaEServiceStatGreenCount = _AlaEServiceStatGreenCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 5),
    _AlaEServiceStatGreenCount_Type()
)
alaEServiceStatGreenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceStatGreenCount.setStatus("current")
_AlaEServiceStatYellowCount_Type = Counter64
_AlaEServiceStatYellowCount_Object = MibTableColumn
alaEServiceStatYellowCount = _AlaEServiceStatYellowCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 6),
    _AlaEServiceStatYellowCount_Type()
)
alaEServiceStatYellowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceStatYellowCount.setStatus("current")
_AlaEServiceStatRedCount_Type = Counter64
_AlaEServiceStatRedCount_Object = MibTableColumn
alaEServiceStatRedCount = _AlaEServiceStatRedCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 7),
    _AlaEServiceStatRedCount_Type()
)
alaEServiceStatRedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceStatRedCount.setStatus("current")
_AlaEServiceStatTotalCount_Type = Counter64
_AlaEServiceStatTotalCount_Object = MibTableColumn
alaEServiceStatTotalCount = _AlaEServiceStatTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 4, 1, 8),
    _AlaEServiceStatTotalCount_Type()
)
alaEServiceStatTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceStatTotalCount.setStatus("current")
_AlaEServiceSapTable_Object = MibTable
alaEServiceSapTable = _AlaEServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaEServiceSapTable.setStatus("current")
_AlaEServiceSapEntry_Object = MibTableRow
alaEServiceSapEntry = _AlaEServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 5, 1)
)
alaEServiceSapEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapID"),
)
if mibBuilder.loadTexts:
    alaEServiceSapEntry.setStatus("current")


class _AlaEServiceSapID_Type(Integer32):
    """Custom type alaEServiceSapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaEServiceSapID_Type.__name__ = "Integer32"
_AlaEServiceSapID_Object = MibTableColumn
alaEServiceSapID = _AlaEServiceSapID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 5, 1, 1),
    _AlaEServiceSapID_Type()
)
alaEServiceSapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapID.setStatus("current")


class _AlaEServiceSapServiceID_Type(DisplayString):
    """Custom type alaEServiceSapServiceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaEServiceSapServiceID_Type.__name__ = "DisplayString"
_AlaEServiceSapServiceID_Object = MibTableColumn
alaEServiceSapServiceID = _AlaEServiceSapServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 5, 1, 2),
    _AlaEServiceSapServiceID_Type()
)
alaEServiceSapServiceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapServiceID.setStatus("current")


class _AlaEServiceSapProfile_Type(DisplayString):
    """Custom type alaEServiceSapProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaEServiceSapProfile_Type.__name__ = "DisplayString"
_AlaEServiceSapProfile_Object = MibTableColumn
alaEServiceSapProfile = _AlaEServiceSapProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 5, 1, 3),
    _AlaEServiceSapProfile_Type()
)
alaEServiceSapProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfile.setStatus("current")
_AlaEServiceSapRowStatus_Type = RowStatus
_AlaEServiceSapRowStatus_Object = MibTableColumn
alaEServiceSapRowStatus = _AlaEServiceSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 5, 1, 4),
    _AlaEServiceSapRowStatus_Type()
)
alaEServiceSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapRowStatus.setStatus("current")
_AlaEServiceSapCvlanTable_Object = MibTable
alaEServiceSapCvlanTable = _AlaEServiceSapCvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanTable.setStatus("current")
_AlaEServiceSapCvlanEntry_Object = MibTableRow
alaEServiceSapCvlanEntry = _AlaEServiceSapCvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 6, 1)
)
alaEServiceSapCvlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanSapID"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanCvlan"),
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanEntry.setStatus("current")


class _AlaEServiceSapCvlanSapID_Type(Integer32):
    """Custom type alaEServiceSapCvlanSapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaEServiceSapCvlanSapID_Type.__name__ = "Integer32"
_AlaEServiceSapCvlanSapID_Object = MibTableColumn
alaEServiceSapCvlanSapID = _AlaEServiceSapCvlanSapID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 6, 1, 1),
    _AlaEServiceSapCvlanSapID_Type()
)
alaEServiceSapCvlanSapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanSapID.setStatus("current")


class _AlaEServiceSapCvlanCvlan_Type(Integer32):
    """Custom type alaEServiceSapCvlanCvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaEServiceSapCvlanCvlan_Type.__name__ = "Integer32"
_AlaEServiceSapCvlanCvlan_Object = MibTableColumn
alaEServiceSapCvlanCvlan = _AlaEServiceSapCvlanCvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 6, 1, 2),
    _AlaEServiceSapCvlanCvlan_Type()
)
alaEServiceSapCvlanCvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanCvlan.setStatus("current")


class _AlaEServiceSapCvlanMapType_Type(Integer32):
    """Custom type alaEServiceSapCvlanMapType based on Integer32"""
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
        *(("single", 1),
          ("all", 2),
          ("untaggedOnly", 3))
    )


_AlaEServiceSapCvlanMapType_Type.__name__ = "Integer32"
_AlaEServiceSapCvlanMapType_Object = MibTableColumn
alaEServiceSapCvlanMapType = _AlaEServiceSapCvlanMapType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 6, 1, 3),
    _AlaEServiceSapCvlanMapType_Type()
)
alaEServiceSapCvlanMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanMapType.setStatus("current")
_AlaEServiceSapCvlanRowStatus_Type = RowStatus
_AlaEServiceSapCvlanRowStatus_Object = MibTableColumn
alaEServiceSapCvlanRowStatus = _AlaEServiceSapCvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 6, 1, 4),
    _AlaEServiceSapCvlanRowStatus_Type()
)
alaEServiceSapCvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanRowStatus.setStatus("current")
_AlaEServicePortTable_Object = MibTable
alaEServicePortTable = _AlaEServicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaEServicePortTable.setStatus("current")
_AlaEServicePortEntry_Object = MibTableRow
alaEServicePortEntry = _AlaEServicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1)
)
alaEServicePortEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortID"),
)
if mibBuilder.loadTexts:
    alaEServicePortEntry.setStatus("current")
_AlaEServicePortID_Type = InterfaceIndex
_AlaEServicePortID_Object = MibTableColumn
alaEServicePortID = _AlaEServicePortID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 1),
    _AlaEServicePortID_Type()
)
alaEServicePortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServicePortID.setStatus("current")


class _AlaEServicePortType_Type(Integer32):
    """Custom type alaEServicePortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uni", 1),
          ("nni", 3))
    )


_AlaEServicePortType_Type.__name__ = "Integer32"
_AlaEServicePortType_Object = MibTableColumn
alaEServicePortType = _AlaEServicePortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 2),
    _AlaEServicePortType_Type()
)
alaEServicePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServicePortType.setStatus("current")


class _AlaEServicePortVendorTpid_Type(Integer32):
    """Custom type alaEServicePortVendorTpid based on Integer32"""
    defaultValue = 33024


_AlaEServicePortVendorTpid_Type.__name__ = "Integer32"
_AlaEServicePortVendorTpid_Object = MibTableColumn
alaEServicePortVendorTpid = _AlaEServicePortVendorTpid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 3),
    _AlaEServicePortVendorTpid_Type()
)
alaEServicePortVendorTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServicePortVendorTpid.setStatus("current")


class _AlaEServicePortLegacyStpBpdu_Type(Integer32):
    """Custom type alaEServicePortLegacyStpBpdu based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaEServicePortLegacyStpBpdu_Type.__name__ = "Integer32"
_AlaEServicePortLegacyStpBpdu_Object = MibTableColumn
alaEServicePortLegacyStpBpdu = _AlaEServicePortLegacyStpBpdu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 4),
    _AlaEServicePortLegacyStpBpdu_Type()
)
alaEServicePortLegacyStpBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServicePortLegacyStpBpdu.setStatus("current")


class _AlaEServicePortLegacyGvrpPdu_Type(Integer32):
    """Custom type alaEServicePortLegacyGvrpPdu based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaEServicePortLegacyGvrpPdu_Type.__name__ = "Integer32"
_AlaEServicePortLegacyGvrpPdu_Object = MibTableColumn
alaEServicePortLegacyGvrpPdu = _AlaEServicePortLegacyGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 5),
    _AlaEServicePortLegacyGvrpPdu_Type()
)
alaEServicePortLegacyGvrpPdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServicePortLegacyGvrpPdu.setStatus("current")


class _AlaEServicePortUniProfile_Type(DisplayString):
    """Custom type alaEServicePortUniProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServicePortUniProfile_Type.__name__ = "DisplayString"
_AlaEServicePortUniProfile_Object = MibTableColumn
alaEServicePortUniProfile = _AlaEServicePortUniProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 6),
    _AlaEServicePortUniProfile_Type()
)
alaEServicePortUniProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServicePortUniProfile.setStatus("current")


class _AlaEServicePortTransBridging_Type(Integer32):
    """Custom type alaEServicePortTransBridging based on Integer32"""
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


_AlaEServicePortTransBridging_Type.__name__ = "Integer32"
_AlaEServicePortTransBridging_Object = MibTableColumn
alaEServicePortTransBridging = _AlaEServicePortTransBridging_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 7),
    _AlaEServicePortTransBridging_Type()
)
alaEServicePortTransBridging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServicePortTransBridging.setStatus("current")


class _AlaEServicePortLegacyMvrpPdu_Type(Integer32):
    """Custom type alaEServicePortLegacyMvrpPdu based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("enable", 1),
          ("disable", 2))
    )


_AlaEServicePortLegacyMvrpPdu_Type.__name__ = "Integer32"
_AlaEServicePortLegacyMvrpPdu_Object = MibTableColumn
alaEServicePortLegacyMvrpPdu = _AlaEServicePortLegacyMvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 7, 1, 8),
    _AlaEServicePortLegacyMvrpPdu_Type()
)
alaEServicePortLegacyMvrpPdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServicePortLegacyMvrpPdu.setStatus("current")
_AlaEServiceSapUniTable_Object = MibTable
alaEServiceSapUniTable = _AlaEServiceSapUniTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaEServiceSapUniTable.setStatus("current")
_AlaEServiceSapUniEntry_Object = MibTableRow
alaEServiceSapUniEntry = _AlaEServiceSapUniEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 8, 1)
)
alaEServiceSapUniEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapUniSap"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapUniUni"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapUniCvlan"),
)
if mibBuilder.loadTexts:
    alaEServiceSapUniEntry.setStatus("current")


class _AlaEServiceSapUniSap_Type(Integer32):
    """Custom type alaEServiceSapUniSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaEServiceSapUniSap_Type.__name__ = "Integer32"
_AlaEServiceSapUniSap_Object = MibTableColumn
alaEServiceSapUniSap = _AlaEServiceSapUniSap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 8, 1, 1),
    _AlaEServiceSapUniSap_Type()
)
alaEServiceSapUniSap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapUniSap.setStatus("current")
_AlaEServiceSapUniUni_Type = InterfaceIndex
_AlaEServiceSapUniUni_Object = MibTableColumn
alaEServiceSapUniUni = _AlaEServiceSapUniUni_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 8, 1, 2),
    _AlaEServiceSapUniUni_Type()
)
alaEServiceSapUniUni.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapUniUni.setStatus("current")
_AlaEServiceSapUniRowStatus_Type = RowStatus
_AlaEServiceSapUniRowStatus_Object = MibTableColumn
alaEServiceSapUniRowStatus = _AlaEServiceSapUniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 8, 1, 3),
    _AlaEServiceSapUniRowStatus_Type()
)
alaEServiceSapUniRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapUniRowStatus.setStatus("current")
_AlaEServiceSapUniCvlan_Type = InterfaceIndex
_AlaEServiceSapUniCvlan_Object = MibTableColumn
alaEServiceSapUniCvlan = _AlaEServiceSapUniCvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 8, 1, 4),
    _AlaEServiceSapUniCvlan_Type()
)
alaEServiceSapUniCvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapUniCvlan.setStatus("current")
_AlaEServiceNniSvlanTable_Object = MibTable
alaEServiceNniSvlanTable = _AlaEServiceNniSvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaEServiceNniSvlanTable.setStatus("current")
_AlaEServiceNniSvlanEntry_Object = MibTableRow
alaEServiceNniSvlanEntry = _AlaEServiceNniSvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 9, 1)
)
alaEServiceNniSvlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNniSvlanNni"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNniSvlanSvlan"),
)
if mibBuilder.loadTexts:
    alaEServiceNniSvlanEntry.setStatus("current")
_AlaEServiceNniSvlanNni_Type = InterfaceIndex
_AlaEServiceNniSvlanNni_Object = MibTableColumn
alaEServiceNniSvlanNni = _AlaEServiceNniSvlanNni_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 9, 1, 1),
    _AlaEServiceNniSvlanNni_Type()
)
alaEServiceNniSvlanNni.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceNniSvlanNni.setStatus("current")


class _AlaEServiceNniSvlanSvlan_Type(Integer32):
    """Custom type alaEServiceNniSvlanSvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_AlaEServiceNniSvlanSvlan_Type.__name__ = "Integer32"
_AlaEServiceNniSvlanSvlan_Object = MibTableColumn
alaEServiceNniSvlanSvlan = _AlaEServiceNniSvlanSvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 9, 1, 2),
    _AlaEServiceNniSvlanSvlan_Type()
)
alaEServiceNniSvlanSvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceNniSvlanSvlan.setStatus("current")
_AlaEServiceNniSvlanRowStatus_Type = RowStatus
_AlaEServiceNniSvlanRowStatus_Object = MibTableColumn
alaEServiceNniSvlanRowStatus = _AlaEServiceNniSvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 9, 1, 3),
    _AlaEServiceNniSvlanRowStatus_Type()
)
alaEServiceNniSvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceNniSvlanRowStatus.setStatus("current")


class _AlaEServiceNniSvlanVpaType_Type(Integer32):
    """Custom type alaEServiceNniSvlanVpaType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp", 1),
          ("erp", 2))
    )


_AlaEServiceNniSvlanVpaType_Type.__name__ = "Integer32"
_AlaEServiceNniSvlanVpaType_Object = MibTableColumn
alaEServiceNniSvlanVpaType = _AlaEServiceNniSvlanVpaType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 9, 1, 4),
    _AlaEServiceNniSvlanVpaType_Type()
)
alaEServiceNniSvlanVpaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceNniSvlanVpaType.setStatus("current")
_AlaEServiceSapCvlanPortStatTable_Object = MibTable
alaEServiceSapCvlanPortStatTable = _AlaEServiceSapCvlanPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatTable.setStatus("current")
_AlaEServiceSapCvlanPortStatEntry_Object = MibTableRow
alaEServiceSapCvlanPortStatEntry = _AlaEServiceSapCvlanPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1)
)
alaEServiceSapCvlanPortStatEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatSapID"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatCvlanID"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatPortID"),
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatEntry.setStatus("current")


class _AlaEServiceSapCvlanPortStatSapID_Type(Integer32):
    """Custom type alaEServiceSapCvlanPortStatSapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaEServiceSapCvlanPortStatSapID_Type.__name__ = "Integer32"
_AlaEServiceSapCvlanPortStatSapID_Object = MibTableColumn
alaEServiceSapCvlanPortStatSapID = _AlaEServiceSapCvlanPortStatSapID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1, 1),
    _AlaEServiceSapCvlanPortStatSapID_Type()
)
alaEServiceSapCvlanPortStatSapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatSapID.setStatus("current")


class _AlaEServiceSapCvlanPortStatCvlanID_Type(Integer32):
    """Custom type alaEServiceSapCvlanPortStatCvlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaEServiceSapCvlanPortStatCvlanID_Type.__name__ = "Integer32"
_AlaEServiceSapCvlanPortStatCvlanID_Object = MibTableColumn
alaEServiceSapCvlanPortStatCvlanID = _AlaEServiceSapCvlanPortStatCvlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1, 2),
    _AlaEServiceSapCvlanPortStatCvlanID_Type()
)
alaEServiceSapCvlanPortStatCvlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatCvlanID.setStatus("current")
_AlaEServiceSapCvlanPortStatPortID_Type = InterfaceIndex
_AlaEServiceSapCvlanPortStatPortID_Object = MibTableColumn
alaEServiceSapCvlanPortStatPortID = _AlaEServiceSapCvlanPortStatPortID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1, 3),
    _AlaEServiceSapCvlanPortStatPortID_Type()
)
alaEServiceSapCvlanPortStatPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatPortID.setStatus("current")
_AlaEServiceSapCvlanPortStatGreenCount_Type = Counter64
_AlaEServiceSapCvlanPortStatGreenCount_Object = MibTableColumn
alaEServiceSapCvlanPortStatGreenCount = _AlaEServiceSapCvlanPortStatGreenCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1, 4),
    _AlaEServiceSapCvlanPortStatGreenCount_Type()
)
alaEServiceSapCvlanPortStatGreenCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatGreenCount.setStatus("current")
_AlaEServiceSapCvlanPortStatYellowCount_Type = Counter64
_AlaEServiceSapCvlanPortStatYellowCount_Object = MibTableColumn
alaEServiceSapCvlanPortStatYellowCount = _AlaEServiceSapCvlanPortStatYellowCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1, 5),
    _AlaEServiceSapCvlanPortStatYellowCount_Type()
)
alaEServiceSapCvlanPortStatYellowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatYellowCount.setStatus("current")
_AlaEServiceSapCvlanPortStatRedCount_Type = Counter64
_AlaEServiceSapCvlanPortStatRedCount_Object = MibTableColumn
alaEServiceSapCvlanPortStatRedCount = _AlaEServiceSapCvlanPortStatRedCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1, 6),
    _AlaEServiceSapCvlanPortStatRedCount_Type()
)
alaEServiceSapCvlanPortStatRedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatRedCount.setStatus("current")
_AlaEServiceSapCvlanPortStatTotalCount_Type = Counter64
_AlaEServiceSapCvlanPortStatTotalCount_Object = MibTableColumn
alaEServiceSapCvlanPortStatTotalCount = _AlaEServiceSapCvlanPortStatTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 10, 1, 7),
    _AlaEServiceSapCvlanPortStatTotalCount_Type()
)
alaEServiceSapCvlanPortStatTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatTotalCount.setStatus("current")
_AlaEServiceUNIProfileL2CustomProtocolTable_Object = MibTable
alaEServiceUNIProfileL2CustomProtocolTable = _AlaEServiceUNIProfileL2CustomProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileL2CustomProtocolTable.setStatus("current")
_AlaEServiceUNIProfileL2CustomProtocolEntry_Object = MibTableRow
alaEServiceUNIProfileL2CustomProtocolEntry = _AlaEServiceUNIProfileL2CustomProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 11, 1)
)
alaEServiceUNIProfileL2CustomProtocolEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceL2CustomProtocolUNIProfileID"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileL2CustomProtocolID"),
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileL2CustomProtocolEntry.setStatus("current")


class _AlaEServiceL2CustomProtocolUNIProfileID_Type(SnmpAdminString):
    """Custom type alaEServiceL2CustomProtocolUNIProfileID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServiceL2CustomProtocolUNIProfileID_Type.__name__ = "SnmpAdminString"
_AlaEServiceL2CustomProtocolUNIProfileID_Object = MibTableColumn
alaEServiceL2CustomProtocolUNIProfileID = _AlaEServiceL2CustomProtocolUNIProfileID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 11, 1, 1),
    _AlaEServiceL2CustomProtocolUNIProfileID_Type()
)
alaEServiceL2CustomProtocolUNIProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceL2CustomProtocolUNIProfileID.setStatus("current")


class _AlaEServiceUNIProfileL2CustomProtocolID_Type(SnmpAdminString):
    """Custom type alaEServiceUNIProfileL2CustomProtocolID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaEServiceUNIProfileL2CustomProtocolID_Type.__name__ = "SnmpAdminString"
_AlaEServiceUNIProfileL2CustomProtocolID_Object = MibTableColumn
alaEServiceUNIProfileL2CustomProtocolID = _AlaEServiceUNIProfileL2CustomProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 11, 1, 2),
    _AlaEServiceUNIProfileL2CustomProtocolID_Type()
)
alaEServiceUNIProfileL2CustomProtocolID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileL2CustomProtocolID.setStatus("current")


class _AlaEServiceUNIProfileL2CustomProtocolTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileL2CustomProtocolTreatment based on AlaEServiceUNIProfileProtocolTreatment"""
    defaultValue = 1


_AlaEServiceUNIProfileL2CustomProtocolTreatment_Type.__name__ = "AlaEServiceUNIProfileProtocolTreatment"
_AlaEServiceUNIProfileL2CustomProtocolTreatment_Object = MibTableColumn
alaEServiceUNIProfileL2CustomProtocolTreatment = _AlaEServiceUNIProfileL2CustomProtocolTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 11, 1, 3),
    _AlaEServiceUNIProfileL2CustomProtocolTreatment_Type()
)
alaEServiceUNIProfileL2CustomProtocolTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileL2CustomProtocolTreatment.setStatus("current")
_AlaEServiceUNIProfileL2CustomProtocolRowStatus_Type = RowStatus
_AlaEServiceUNIProfileL2CustomProtocolRowStatus_Object = MibTableColumn
alaEServiceUNIProfileL2CustomProtocolRowStatus = _AlaEServiceUNIProfileL2CustomProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 11, 1, 4),
    _AlaEServiceUNIProfileL2CustomProtocolRowStatus_Type()
)
alaEServiceUNIProfileL2CustomProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileL2CustomProtocolRowStatus.setStatus("current")
_AlaEServiceL2CustomProtocolTable_Object = MibTable
alaEServiceL2CustomProtocolTable = _AlaEServiceL2CustomProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaEServiceL2CustomProtocolTable.setStatus("current")
_AlaEServiceL2CustomProtocolEntry_Object = MibTableRow
alaEServiceL2CustomProtocolEntry = _AlaEServiceL2CustomProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 12, 1)
)
alaEServiceL2CustomProtocolEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceL2CustomProtocolID"),
)
if mibBuilder.loadTexts:
    alaEServiceL2CustomProtocolEntry.setStatus("current")


class _AlaEServiceL2CustomProtocolID_Type(SnmpAdminString):
    """Custom type alaEServiceL2CustomProtocolID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaEServiceL2CustomProtocolID_Type.__name__ = "SnmpAdminString"
_AlaEServiceL2CustomProtocolID_Object = MibTableColumn
alaEServiceL2CustomProtocolID = _AlaEServiceL2CustomProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 12, 1, 1),
    _AlaEServiceL2CustomProtocolID_Type()
)
alaEServiceL2CustomProtocolID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceL2CustomProtocolID.setStatus("current")


class _AlaEServiceL2CustomProtocolEntryType_Type(AlaEServiceL2CustomProtocolType):
    """Custom type alaEServiceL2CustomProtocolEntryType based on AlaEServiceL2CustomProtocolType"""
    defaultValue = 2


_AlaEServiceL2CustomProtocolEntryType_Type.__name__ = "AlaEServiceL2CustomProtocolType"
_AlaEServiceL2CustomProtocolEntryType_Object = MibTableColumn
alaEServiceL2CustomProtocolEntryType = _AlaEServiceL2CustomProtocolEntryType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 12, 1, 2),
    _AlaEServiceL2CustomProtocolEntryType_Type()
)
alaEServiceL2CustomProtocolEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceL2CustomProtocolEntryType.setStatus("current")
_AlaEServiceL2CustomProtocolMac_Type = MacAddress
_AlaEServiceL2CustomProtocolMac_Object = MibTableColumn
alaEServiceL2CustomProtocolMac = _AlaEServiceL2CustomProtocolMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 12, 1, 3),
    _AlaEServiceL2CustomProtocolMac_Type()
)
alaEServiceL2CustomProtocolMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceL2CustomProtocolMac.setStatus("current")
_AlaEServiceL2CustomProtocolMask_Type = MacAddress
_AlaEServiceL2CustomProtocolMask_Object = MibTableColumn
alaEServiceL2CustomProtocolMask = _AlaEServiceL2CustomProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 12, 1, 4),
    _AlaEServiceL2CustomProtocolMask_Type()
)
alaEServiceL2CustomProtocolMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceL2CustomProtocolMask.setStatus("current")


class _AlaEServiceL2CustomProtocolEtherType_Type(Integer32):
    """Custom type alaEServiceL2CustomProtocolEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaEServiceL2CustomProtocolEtherType_Type.__name__ = "Integer32"
_AlaEServiceL2CustomProtocolEtherType_Object = MibTableColumn
alaEServiceL2CustomProtocolEtherType = _AlaEServiceL2CustomProtocolEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 12, 1, 5),
    _AlaEServiceL2CustomProtocolEtherType_Type()
)
alaEServiceL2CustomProtocolEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceL2CustomProtocolEtherType.setStatus("current")


class _AlaEServiceL2CustomProtocolEtherSubType_Type(Integer32):
    """Custom type alaEServiceL2CustomProtocolEtherSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaEServiceL2CustomProtocolEtherSubType_Type.__name__ = "Integer32"
_AlaEServiceL2CustomProtocolEtherSubType_Object = MibTableColumn
alaEServiceL2CustomProtocolEtherSubType = _AlaEServiceL2CustomProtocolEtherSubType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 12, 1, 6),
    _AlaEServiceL2CustomProtocolEtherSubType_Type()
)
alaEServiceL2CustomProtocolEtherSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceL2CustomProtocolEtherSubType.setStatus("current")


class _AlaEServiceL2CustomProtocolSsap_Type(Integer32):
    """Custom type alaEServiceL2CustomProtocolSsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaEServiceL2CustomProtocolSsap_Type.__name__ = "Integer32"
_AlaEServiceL2CustomProtocolSsap_Object = MibTableColumn
alaEServiceL2CustomProtocolSsap = _AlaEServiceL2CustomProtocolSsap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 12, 1, 7),
    _AlaEServiceL2CustomProtocolSsap_Type()
)
alaEServiceL2CustomProtocolSsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceL2CustomProtocolSsap.setStatus("current")


class _AlaEServiceL2CustomProtocolDsap_Type(Integer32):
    """Custom type alaEServiceL2CustomProtocolDsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaEServiceL2CustomProtocolDsap_Type.__name__ = "Integer32"
_AlaEServiceL2CustomProtocolDsap_Object = MibTableColumn
alaEServiceL2CustomProtocolDsap = _AlaEServiceL2CustomProtocolDsap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 12, 1, 8),
    _AlaEServiceL2CustomProtocolDsap_Type()
)
alaEServiceL2CustomProtocolDsap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceL2CustomProtocolDsap.setStatus("current")


class _AlaEServiceL2CustomProtocolPid_Type(Integer32):
    """Custom type alaEServiceL2CustomProtocolPid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaEServiceL2CustomProtocolPid_Type.__name__ = "Integer32"
_AlaEServiceL2CustomProtocolPid_Object = MibTableColumn
alaEServiceL2CustomProtocolPid = _AlaEServiceL2CustomProtocolPid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 12, 1, 9),
    _AlaEServiceL2CustomProtocolPid_Type()
)
alaEServiceL2CustomProtocolPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceL2CustomProtocolPid.setStatus("current")
_AlaEServiceL2CustomProtocolRowStatus_Type = RowStatus
_AlaEServiceL2CustomProtocolRowStatus_Object = MibTableColumn
alaEServiceL2CustomProtocolRowStatus = _AlaEServiceL2CustomProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 12, 1, 10),
    _AlaEServiceL2CustomProtocolRowStatus_Type()
)
alaEServiceL2CustomProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceL2CustomProtocolRowStatus.setStatus("current")
_AlaEServiceUNIPortL2ProtocolStatisticsTable_Object = MibTable
alaEServiceUNIPortL2ProtocolStatisticsTable = _AlaEServiceUNIPortL2ProtocolStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2ProtocolStatisticsTable.setStatus("current")
_AlaEServiceUNIPortL2ProtocolStatisticsEntry_Object = MibTableRow
alaEServiceUNIPortL2ProtocolStatisticsEntry = _AlaEServiceUNIPortL2ProtocolStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 13, 1)
)
alaEServiceUNIPortL2ProtocolStatisticsEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIPortID"),
    (1, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIPortL2ProtocolID"),
)
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2ProtocolStatisticsEntry.setStatus("current")
_AlaEServiceUNIPortID_Type = InterfaceIndex
_AlaEServiceUNIPortID_Object = MibTableColumn
alaEServiceUNIPortID = _AlaEServiceUNIPortID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 13, 1, 1),
    _AlaEServiceUNIPortID_Type()
)
alaEServiceUNIPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceUNIPortID.setStatus("current")


class _AlaEServiceUNIPortL2ProtocolID_Type(SnmpAdminString):
    """Custom type alaEServiceUNIPortL2ProtocolID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServiceUNIPortL2ProtocolID_Type.__name__ = "SnmpAdminString"
_AlaEServiceUNIPortL2ProtocolID_Object = MibTableColumn
alaEServiceUNIPortL2ProtocolID = _AlaEServiceUNIPortL2ProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 13, 1, 2),
    _AlaEServiceUNIPortL2ProtocolID_Type()
)
alaEServiceUNIPortL2ProtocolID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2ProtocolID.setStatus("current")
_AlaEServiceUNIPortL2RxFrames_Type = Counter32
_AlaEServiceUNIPortL2RxFrames_Object = MibTableColumn
alaEServiceUNIPortL2RxFrames = _AlaEServiceUNIPortL2RxFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 13, 1, 3),
    _AlaEServiceUNIPortL2RxFrames_Type()
)
alaEServiceUNIPortL2RxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2RxFrames.setStatus("current")
_AlaEServiceUNIPortL2TunneledFrames_Type = Counter32
_AlaEServiceUNIPortL2TunneledFrames_Object = MibTableColumn
alaEServiceUNIPortL2TunneledFrames = _AlaEServiceUNIPortL2TunneledFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 13, 1, 4),
    _AlaEServiceUNIPortL2TunneledFrames_Type()
)
alaEServiceUNIPortL2TunneledFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2TunneledFrames.setStatus("current")
_AlaEServiceUNIPortL2DroppedFrames_Type = Counter32
_AlaEServiceUNIPortL2DroppedFrames_Object = MibTableColumn
alaEServiceUNIPortL2DroppedFrames = _AlaEServiceUNIPortL2DroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 13, 1, 5),
    _AlaEServiceUNIPortL2DroppedFrames_Type()
)
alaEServiceUNIPortL2DroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2DroppedFrames.setStatus("current")
_AlaEServiceUNIPortL2PeeredFrames_Type = Counter32
_AlaEServiceUNIPortL2PeeredFrames_Object = MibTableColumn
alaEServiceUNIPortL2PeeredFrames = _AlaEServiceUNIPortL2PeeredFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 13, 1, 6),
    _AlaEServiceUNIPortL2PeeredFrames_Type()
)
alaEServiceUNIPortL2PeeredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2PeeredFrames.setStatus("current")
_AlaEServiceUNIPortL2MACTunneledFrames_Type = Counter32
_AlaEServiceUNIPortL2MACTunneledFrames_Object = MibTableColumn
alaEServiceUNIPortL2MACTunneledFrames = _AlaEServiceUNIPortL2MACTunneledFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 13, 1, 7),
    _AlaEServiceUNIPortL2MACTunneledFrames_Type()
)
alaEServiceUNIPortL2MACTunneledFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2MACTunneledFrames.setStatus("current")
_AlaEServiceUNIPortL2MACDeTunneledFrames_Type = Counter32
_AlaEServiceUNIPortL2MACDeTunneledFrames_Object = MibTableColumn
alaEServiceUNIPortL2MACDeTunneledFrames = _AlaEServiceUNIPortL2MACDeTunneledFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 13, 1, 8),
    _AlaEServiceUNIPortL2MACDeTunneledFrames_Type()
)
alaEServiceUNIPortL2MACDeTunneledFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2MACDeTunneledFrames.setStatus("current")
_AlaEServiceUNIPortL2LastSourceMAC_Type = MacAddress
_AlaEServiceUNIPortL2LastSourceMAC_Object = MibTableColumn
alaEServiceUNIPortL2LastSourceMAC = _AlaEServiceUNIPortL2LastSourceMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 13, 1, 9),
    _AlaEServiceUNIPortL2LastSourceMAC_Type()
)
alaEServiceUNIPortL2LastSourceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2LastSourceMAC.setStatus("current")
_AlaEServiceNNIPortL2ProtocolStatisticsTable_Object = MibTable
alaEServiceNNIPortL2ProtocolStatisticsTable = _AlaEServiceNNIPortL2ProtocolStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alaEServiceNNIPortL2ProtocolStatisticsTable.setStatus("current")
_AlaEServiceNNIPortL2ProtocolStatisticsEntry_Object = MibTableRow
alaEServiceNNIPortL2ProtocolStatisticsEntry = _AlaEServiceNNIPortL2ProtocolStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 14, 1)
)
alaEServiceNNIPortL2ProtocolStatisticsEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNNIPortID"),
)
if mibBuilder.loadTexts:
    alaEServiceNNIPortL2ProtocolStatisticsEntry.setStatus("current")
_AlaEServiceNNIPortID_Type = InterfaceIndex
_AlaEServiceNNIPortID_Object = MibTableColumn
alaEServiceNNIPortID = _AlaEServiceNNIPortID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 14, 1, 1),
    _AlaEServiceNNIPortID_Type()
)
alaEServiceNNIPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceNNIPortID.setStatus("current")
_AlaEServiceNNIPortL2RxMACTunneledFrames_Type = Counter32
_AlaEServiceNNIPortL2RxMACTunneledFrames_Object = MibTableColumn
alaEServiceNNIPortL2RxMACTunneledFrames = _AlaEServiceNNIPortL2RxMACTunneledFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 14, 1, 2),
    _AlaEServiceNNIPortL2RxMACTunneledFrames_Type()
)
alaEServiceNNIPortL2RxMACTunneledFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceNNIPortL2RxMACTunneledFrames.setStatus("current")
_AlaEServiceNNIPortL2MACTunneledDiscardFrames_Type = Counter32
_AlaEServiceNNIPortL2MACTunneledDiscardFrames_Object = MibTableColumn
alaEServiceNNIPortL2MACTunneledDiscardFrames = _AlaEServiceNNIPortL2MACTunneledDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 14, 1, 3),
    _AlaEServiceNNIPortL2MACTunneledDiscardFrames_Type()
)
alaEServiceNNIPortL2MACTunneledDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceNNIPortL2MACTunneledDiscardFrames.setStatus("current")


class _AlaEServiceNNIPortL2ClearStats_Type(Integer32):
    """Custom type alaEServiceNNIPortL2ClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaEServiceNNIPortL2ClearStats_Type.__name__ = "Integer32"
_AlaEServiceNNIPortL2ClearStats_Object = MibTableColumn
alaEServiceNNIPortL2ClearStats = _AlaEServiceNNIPortL2ClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 14, 1, 4),
    _AlaEServiceNNIPortL2ClearStats_Type()
)
alaEServiceNNIPortL2ClearStats.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceNNIPortL2ClearStats.setStatus("current")
_AlaEServiceUNIProfileL2ProtocolTotalStatisticsTable_Object = MibTable
alaEServiceUNIProfileL2ProtocolTotalStatisticsTable = _AlaEServiceUNIProfileL2ProtocolTotalStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileL2ProtocolTotalStatisticsTable.setStatus("current")
_AlaEServiceUNIProfileL2ProtocolTotalStatisticsEntry_Object = MibTableRow
alaEServiceUNIProfileL2ProtocolTotalStatisticsEntry = _AlaEServiceUNIProfileL2ProtocolTotalStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 15, 1)
)
alaEServiceUNIProfileL2ProtocolTotalStatisticsEntry.setIndexNames(
    (1, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfile"),
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileL2ProtocolTotalStatisticsEntry.setStatus("current")


class _AlaEServiceUNIProfile_Type(SnmpAdminString):
    """Custom type alaEServiceUNIProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServiceUNIProfile_Type.__name__ = "SnmpAdminString"
_AlaEServiceUNIProfile_Object = MibTableColumn
alaEServiceUNIProfile = _AlaEServiceUNIProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 15, 1, 1),
    _AlaEServiceUNIProfile_Type()
)
alaEServiceUNIProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceUNIProfile.setStatus("current")
_AlaEServiceUNIProfileL2ProtocolTotalRxFrames_Type = Counter32
_AlaEServiceUNIProfileL2ProtocolTotalRxFrames_Object = MibTableColumn
alaEServiceUNIProfileL2ProtocolTotalRxFrames = _AlaEServiceUNIProfileL2ProtocolTotalRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 15, 1, 2),
    _AlaEServiceUNIProfileL2ProtocolTotalRxFrames_Type()
)
alaEServiceUNIProfileL2ProtocolTotalRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileL2ProtocolTotalRxFrames.setStatus("current")


class _AlaEServiceUNIProfileL2ProtocolClearStats_Type(Integer32):
    """Custom type alaEServiceUNIProfileL2ProtocolClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaEServiceUNIProfileL2ProtocolClearStats_Type.__name__ = "Integer32"
_AlaEServiceUNIProfileL2ProtocolClearStats_Object = MibTableColumn
alaEServiceUNIProfileL2ProtocolClearStats = _AlaEServiceUNIProfileL2ProtocolClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 15, 1, 3),
    _AlaEServiceUNIProfileL2ProtocolClearStats_Type()
)
alaEServiceUNIProfileL2ProtocolClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileL2ProtocolClearStats.setStatus("current")
_AlaEServiceUNIProfileIEEEL2ProtocolStatisticsTable_Object = MibTable
alaEServiceUNIProfileIEEEL2ProtocolStatisticsTable = _AlaEServiceUNIProfileIEEEL2ProtocolStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileIEEEL2ProtocolStatisticsTable.setStatus("current")
_AlaEServiceUNIProfileIEEEL2ProtocolStatisticsEntry_Object = MibTableRow
alaEServiceUNIProfileIEEEL2ProtocolStatisticsEntry = _AlaEServiceUNIProfileIEEEL2ProtocolStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 16, 1)
)
alaEServiceUNIProfileIEEEL2ProtocolStatisticsEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileIEEEL2ProfileID"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileIEEEL2ProtocolIndex"),
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileIEEEL2ProtocolStatisticsEntry.setStatus("current")


class _AlaEServiceUNIProfileIEEEL2ProfileID_Type(SnmpAdminString):
    """Custom type alaEServiceUNIProfileIEEEL2ProfileID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServiceUNIProfileIEEEL2ProfileID_Type.__name__ = "SnmpAdminString"
_AlaEServiceUNIProfileIEEEL2ProfileID_Object = MibTableColumn
alaEServiceUNIProfileIEEEL2ProfileID = _AlaEServiceUNIProfileIEEEL2ProfileID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 16, 1, 1),
    _AlaEServiceUNIProfileIEEEL2ProfileID_Type()
)
alaEServiceUNIProfileIEEEL2ProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileIEEEL2ProfileID.setStatus("current")


class _AlaEServiceUNIProfileIEEEL2ProtocolIndex_Type(Integer32):
    """Custom type alaEServiceUNIProfileIEEEL2ProtocolIndex based on Integer32"""
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
        *(("lacpLacpmarkerOam", 1),
          ("ieee802dot1x", 2),
          ("lldp", 3),
          ("amap", 4),
          ("cisco", 5),
          ("stp", 6),
          ("gvrpMvrp", 7))
    )


_AlaEServiceUNIProfileIEEEL2ProtocolIndex_Type.__name__ = "Integer32"
_AlaEServiceUNIProfileIEEEL2ProtocolIndex_Object = MibTableColumn
alaEServiceUNIProfileIEEEL2ProtocolIndex = _AlaEServiceUNIProfileIEEEL2ProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 16, 1, 2),
    _AlaEServiceUNIProfileIEEEL2ProtocolIndex_Type()
)
alaEServiceUNIProfileIEEEL2ProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileIEEEL2ProtocolIndex.setStatus("current")
_AlaEServiceUNIProfileIEEEL2ProtocolRxFrames_Type = Counter32
_AlaEServiceUNIProfileIEEEL2ProtocolRxFrames_Object = MibTableColumn
alaEServiceUNIProfileIEEEL2ProtocolRxFrames = _AlaEServiceUNIProfileIEEEL2ProtocolRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 16, 1, 3),
    _AlaEServiceUNIProfileIEEEL2ProtocolRxFrames_Type()
)
alaEServiceUNIProfileIEEEL2ProtocolRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileIEEEL2ProtocolRxFrames.setStatus("current")


class _AlaEServiceUNIProfileIEEEL2ProtocolTreatment_Type(Integer32):
    """Custom type alaEServiceUNIProfileIEEEL2ProtocolTreatment based on Integer32"""
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
        *(("invalid", 0),
          ("fwd", 1),
          ("drop", 2),
          ("cpu", 3))
    )


_AlaEServiceUNIProfileIEEEL2ProtocolTreatment_Type.__name__ = "Integer32"
_AlaEServiceUNIProfileIEEEL2ProtocolTreatment_Object = MibTableColumn
alaEServiceUNIProfileIEEEL2ProtocolTreatment = _AlaEServiceUNIProfileIEEEL2ProtocolTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 16, 1, 4),
    _AlaEServiceUNIProfileIEEEL2ProtocolTreatment_Type()
)
alaEServiceUNIProfileIEEEL2ProtocolTreatment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileIEEEL2ProtocolTreatment.setStatus("current")
_AlaEServiceUNIProfileCustomL2ProtocolStatisticsTable_Object = MibTable
alaEServiceUNIProfileCustomL2ProtocolStatisticsTable = _AlaEServiceUNIProfileCustomL2ProtocolStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 17)
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCustomL2ProtocolStatisticsTable.setStatus("current")
_AlaEServiceUNIProfileCustomL2ProtocolStatisticsEntry_Object = MibTableRow
alaEServiceUNIProfileCustomL2ProtocolStatisticsEntry = _AlaEServiceUNIProfileCustomL2ProtocolStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 17, 1)
)
alaEServiceUNIProfileCustomL2ProtocolStatisticsEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCustomL2StatsProfileID"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCustomL2ProtocolIndex"),
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCustomL2ProtocolStatisticsEntry.setStatus("current")


class _AlaEServiceUNIProfileCustomL2StatsProfileID_Type(SnmpAdminString):
    """Custom type alaEServiceUNIProfileCustomL2StatsProfileID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServiceUNIProfileCustomL2StatsProfileID_Type.__name__ = "SnmpAdminString"
_AlaEServiceUNIProfileCustomL2StatsProfileID_Object = MibTableColumn
alaEServiceUNIProfileCustomL2StatsProfileID = _AlaEServiceUNIProfileCustomL2StatsProfileID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 17, 1, 1),
    _AlaEServiceUNIProfileCustomL2StatsProfileID_Type()
)
alaEServiceUNIProfileCustomL2StatsProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCustomL2StatsProfileID.setStatus("current")


class _AlaEServiceUNIProfileCustomL2ProtocolIndex_Type(SnmpAdminString):
    """Custom type alaEServiceUNIProfileCustomL2ProtocolIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServiceUNIProfileCustomL2ProtocolIndex_Type.__name__ = "SnmpAdminString"
_AlaEServiceUNIProfileCustomL2ProtocolIndex_Object = MibTableColumn
alaEServiceUNIProfileCustomL2ProtocolIndex = _AlaEServiceUNIProfileCustomL2ProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 17, 1, 2),
    _AlaEServiceUNIProfileCustomL2ProtocolIndex_Type()
)
alaEServiceUNIProfileCustomL2ProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCustomL2ProtocolIndex.setStatus("current")
_AlaEServiceUNIProfileCustomL2ProtocolRxFrames_Type = Counter32
_AlaEServiceUNIProfileCustomL2ProtocolRxFrames_Object = MibTableColumn
alaEServiceUNIProfileCustomL2ProtocolRxFrames = _AlaEServiceUNIProfileCustomL2ProtocolRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 17, 1, 3),
    _AlaEServiceUNIProfileCustomL2ProtocolRxFrames_Type()
)
alaEServiceUNIProfileCustomL2ProtocolRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCustomL2ProtocolRxFrames.setStatus("current")


class _AlaEServiceUNIProfileCustomL2ProtocolTreatment_Type(Integer32):
    """Custom type alaEServiceUNIProfileCustomL2ProtocolTreatment based on Integer32"""
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
        *(("invalid", 0),
          ("fwd", 1),
          ("drop", 2),
          ("cpu", 3))
    )


_AlaEServiceUNIProfileCustomL2ProtocolTreatment_Type.__name__ = "Integer32"
_AlaEServiceUNIProfileCustomL2ProtocolTreatment_Object = MibTableColumn
alaEServiceUNIProfileCustomL2ProtocolTreatment = _AlaEServiceUNIProfileCustomL2ProtocolTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 17, 1, 4),
    _AlaEServiceUNIProfileCustomL2ProtocolTreatment_Type()
)
alaEServiceUNIProfileCustomL2ProtocolTreatment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileCustomL2ProtocolTreatment.setStatus("current")
_AlaEServiceL2PTProtocolStatisticsClear_ObjectIdentity = ObjectIdentity
alaEServiceL2PTProtocolStatisticsClear = _AlaEServiceL2PTProtocolStatisticsClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 18)
)


class _AlaEServiceUNIPortL2GlobalClearStatistics_Type(Integer32):
    """Custom type alaEServiceUNIPortL2GlobalClearStatistics based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaEServiceUNIPortL2GlobalClearStatistics_Type.__name__ = "Integer32"
_AlaEServiceUNIPortL2GlobalClearStatistics_Object = MibScalar
alaEServiceUNIPortL2GlobalClearStatistics = _AlaEServiceUNIPortL2GlobalClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 18, 1),
    _AlaEServiceUNIPortL2GlobalClearStatistics_Type()
)
alaEServiceUNIPortL2GlobalClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2GlobalClearStatistics.setStatus("current")


class _AlaEServiceNNIPortL2GlobalClearStatistics_Type(Integer32):
    """Custom type alaEServiceNNIPortL2GlobalClearStatistics based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaEServiceNNIPortL2GlobalClearStatistics_Type.__name__ = "Integer32"
_AlaEServiceNNIPortL2GlobalClearStatistics_Object = MibScalar
alaEServiceNNIPortL2GlobalClearStatistics = _AlaEServiceNNIPortL2GlobalClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 18, 2),
    _AlaEServiceNNIPortL2GlobalClearStatistics_Type()
)
alaEServiceNNIPortL2GlobalClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServiceNNIPortL2GlobalClearStatistics.setStatus("current")


class _AlaEServiceUNIProfileL2GlobalClearStatistics_Type(Integer32):
    """Custom type alaEServiceUNIProfileL2GlobalClearStatistics based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaEServiceUNIProfileL2GlobalClearStatistics_Type.__name__ = "Integer32"
_AlaEServiceUNIProfileL2GlobalClearStatistics_Object = MibScalar
alaEServiceUNIProfileL2GlobalClearStatistics = _AlaEServiceUNIProfileL2GlobalClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 18, 3),
    _AlaEServiceUNIProfileL2GlobalClearStatistics_Type()
)
alaEServiceUNIProfileL2GlobalClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileL2GlobalClearStatistics.setStatus("current")
_AlaEServiceUNIPortL2ProtocolStatisticsClearTable_Object = MibTable
alaEServiceUNIPortL2ProtocolStatisticsClearTable = _AlaEServiceUNIPortL2ProtocolStatisticsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 19)
)
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2ProtocolStatisticsClearTable.setStatus("current")
_AlaEServiceUNIPortL2ProtocolStatisticsClearEntry_Object = MibTableRow
alaEServiceUNIPortL2ProtocolStatisticsClearEntry = _AlaEServiceUNIPortL2ProtocolStatisticsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 19, 1)
)
alaEServiceUNIPortL2ProtocolStatisticsClearEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIPortClearID"),
)
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2ProtocolStatisticsClearEntry.setStatus("current")
_AlaEServiceUNIPortClearID_Type = InterfaceIndex
_AlaEServiceUNIPortClearID_Object = MibTableColumn
alaEServiceUNIPortClearID = _AlaEServiceUNIPortClearID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 19, 1, 1),
    _AlaEServiceUNIPortClearID_Type()
)
alaEServiceUNIPortClearID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceUNIPortClearID.setStatus("current")


class _AlaEServiceUNIPortL2ClearStats_Type(Integer32):
    """Custom type alaEServiceUNIPortL2ClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaEServiceUNIPortL2ClearStats_Type.__name__ = "Integer32"
_AlaEServiceUNIPortL2ClearStats_Object = MibTableColumn
alaEServiceUNIPortL2ClearStats = _AlaEServiceUNIPortL2ClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 19, 1, 2),
    _AlaEServiceUNIPortL2ClearStats_Type()
)
alaEServiceUNIPortL2ClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2ClearStats.setStatus("current")
_AlaEServiceNNIPortL2ProtocolStatisticsClearTable_Object = MibTable
alaEServiceNNIPortL2ProtocolStatisticsClearTable = _AlaEServiceNNIPortL2ProtocolStatisticsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 20)
)
if mibBuilder.loadTexts:
    alaEServiceNNIPortL2ProtocolStatisticsClearTable.setStatus("current")
_AlaEServiceNNIPortL2ProtocolStatisticsClearEntry_Object = MibTableRow
alaEServiceNNIPortL2ProtocolStatisticsClearEntry = _AlaEServiceNNIPortL2ProtocolStatisticsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 20, 1)
)
alaEServiceNNIPortL2ProtocolStatisticsClearEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNNIPortClearID"),
)
if mibBuilder.loadTexts:
    alaEServiceNNIPortL2ProtocolStatisticsClearEntry.setStatus("current")
_AlaEServiceNNIPortClearID_Type = InterfaceIndex
_AlaEServiceNNIPortClearID_Object = MibTableColumn
alaEServiceNNIPortClearID = _AlaEServiceNNIPortClearID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 20, 1, 1),
    _AlaEServiceNNIPortClearID_Type()
)
alaEServiceNNIPortClearID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceNNIPortClearID.setStatus("current")


class _AlaEServiceNNIPortL2ClearStatistics_Type(Integer32):
    """Custom type alaEServiceNNIPortL2ClearStatistics based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaEServiceNNIPortL2ClearStatistics_Type.__name__ = "Integer32"
_AlaEServiceNNIPortL2ClearStatistics_Object = MibTableColumn
alaEServiceNNIPortL2ClearStatistics = _AlaEServiceNNIPortL2ClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 1, 1, 20, 1, 2),
    _AlaEServiceNNIPortL2ClearStatistics_Type()
)
alaEServiceNNIPortL2ClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServiceNNIPortL2ClearStatistics.setStatus("current")
_AlcatelIND1EServiceMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1EServiceMIBConformance = _AlcatelIND1EServiceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1EServiceMIBConformance.setStatus("current")
_AlcatelIND1EServiceMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1EServiceMIBGroups = _AlcatelIND1EServiceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1EServiceMIBGroups.setStatus("current")
_AlcatelIND1EServiceMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1EServiceMIBCompliances = _AlcatelIND1EServiceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1EServiceMIBCompliances.setStatus("current")

# Managed Objects groups

alaEServiceSapProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 1)
)
alaEServiceSapProfileGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileCVLANTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileReplacementCVLAN"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfilePriorityMapMode"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileFixedPriority"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileIngressBW"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileBandwidthShare"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileRowStatus"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileEgressBW"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileCIR"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileCBS"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfilePIR"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfilePBS"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileDepth"))
)
if mibBuilder.loadTexts:
    alaEServiceSapProfileGroup.setStatus("current")

alaEServiceUNIProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 2)
)
alaEServiceUNIProfileGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileStpBpduTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfile8021xTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfile8021ABTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfile8023adTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileGvrpTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileAmapTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileRowStatus"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileMvrpTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileTunnelMac"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileLacpMarkerTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileOamTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoPagpTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoUdldTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoCdpTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoVtpTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoDtpTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoPvstTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoVlanTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCiscoUplinkTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileIeeeMacTreatment"))
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileGroup.setStatus("current")

alaEServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 3)
)
alaEServiceGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSVLAN"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceVlanType"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceRowStatus"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceStatGreenCount"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceStatYellowCount"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceStatRedCount"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceStatTotalCount"))
)
if mibBuilder.loadTexts:
    alaEServiceGroup.setStatus("current")

alaEServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 4)
)
alaEServiceSapGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapServiceID"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfile"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapRowStatus"))
)
if mibBuilder.loadTexts:
    alaEServiceSapGroup.setStatus("current")

alaEServiceSapCvlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 5)
)
alaEServiceSapCvlanGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanMapType"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanRowStatus"))
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanGroup.setStatus("current")

alaEServicePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 6)
)
alaEServicePortGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortType"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortVendorTpid"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortLegacyStpBpdu"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortLegacyGvrpPdu"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortUniProfile"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortTransBridging"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortLegacyMvrpPdu"))
)
if mibBuilder.loadTexts:
    alaEServicePortGroup.setStatus("current")

alaEServiceSapUniGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 7)
)
alaEServiceSapUniGroup.setObjects(
    ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapUniRowStatus")
)
if mibBuilder.loadTexts:
    alaEServiceSapUniGroup.setStatus("current")

alaEServiceNniSvlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 8)
)
alaEServiceNniSvlanGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNniSvlanRowStatus"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNniSvlanVpaType"))
)
if mibBuilder.loadTexts:
    alaEServiceNniSvlanGroup.setStatus("current")

alaEServiceSapCvlanPortStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 9)
)
alaEServiceSapCvlanPortStatGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatGreenCount"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatYellowCount"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatRedCount"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatTotalCount"))
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanPortStatGroup.setStatus("current")

alaEServiceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 10)
)
alaEServiceInfoGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceMode"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceStatReset"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceL2MacTunnel"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUntaggedMode"))
)
if mibBuilder.loadTexts:
    alaEServiceInfoGroup.setStatus("current")

alaEServiceUNIProfileL2CustomProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 11)
)
alaEServiceUNIProfileL2CustomProtocolGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileL2CustomProtocolTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileL2CustomProtocolRowStatus"))
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileL2CustomProtocolGroup.setStatus("current")

alaEServiceL2CustomProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 12)
)
alaEServiceL2CustomProtocolGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceL2CustomProtocolEntryType"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceL2CustomProtocolMac"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceL2CustomProtocolMask"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceL2CustomProtocolEtherType"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceL2CustomProtocolEtherSubType"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceL2CustomProtocolSsap"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceL2CustomProtocolDsap"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceL2CustomProtocolPid"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceL2CustomProtocolRowStatus"))
)
if mibBuilder.loadTexts:
    alaEServiceL2CustomProtocolGroup.setStatus("current")

alaEServiceUNIPortL2StatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 13)
)
alaEServiceUNIPortL2StatisticsGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIPortL2RxFrames"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIPortL2TunneledFrames"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIPortL2DroppedFrames"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIPortL2PeeredFrames"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIPortL2MACTunneledFrames"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIPortL2MACDeTunneledFrames"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIPortL2LastSourceMAC"))
)
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2StatisticsGroup.setStatus("current")

alaEServiceNNIPortL2StatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 14)
)
alaEServiceNNIPortL2StatisticsGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNNIPortL2RxMACTunneledFrames"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNNIPortL2MACTunneledDiscardFrames"))
)
if mibBuilder.loadTexts:
    alaEServiceNNIPortL2StatisticsGroup.setStatus("current")

alaEServiceUNIProfileL2ProtocolTotalStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 15)
)
alaEServiceUNIProfileL2ProtocolTotalStatisticsGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileL2ProtocolTotalRxFrames"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileL2ProtocolClearStats"))
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileL2ProtocolTotalStatisticsGroup.setStatus("current")

alaEServiceUNIProfileIEEEL2ProtocolStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 16)
)
alaEServiceUNIProfileIEEEL2ProtocolStatisticsGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileIEEEL2ProtocolRxFrames"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileIEEEL2ProtocolTreatment"))
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileIEEEL2ProtocolStatisticsGroup.setStatus("current")

alaEServiceUNIProfileL2ProtocolStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 17)
)
alaEServiceUNIProfileL2ProtocolStatisticsGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCustomL2ProtocolRxFrames"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileCustomL2ProtocolTreatment"))
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileL2ProtocolStatisticsGroup.setStatus("current")

alaEServiceL2PTProtocolStatisticsClearGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 18)
)
alaEServiceL2PTProtocolStatisticsClearGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIPortL2GlobalClearStatistics"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNNIPortL2GlobalClearStatistics"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileL2GlobalClearStatistics"))
)
if mibBuilder.loadTexts:
    alaEServiceL2PTProtocolStatisticsClearGroup.setStatus("current")

alaEServiceUNIPortL2StatisticsClearGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 19)
)
alaEServiceUNIPortL2StatisticsClearGroup.setObjects(
    ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIPortL2ClearStats")
)
if mibBuilder.loadTexts:
    alaEServiceUNIPortL2StatisticsClearGroup.setStatus("current")

alaEServiceNNIPortL2StatisticsClearGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 1, 20)
)
alaEServiceNNIPortL2StatisticsClearGroup.setObjects(
    ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNNIPortL2ClearStatistics")
)
if mibBuilder.loadTexts:
    alaEServiceNNIPortL2StatisticsClearGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1EServiceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 50, 1, 2, 2, 1)
)
alcatelIND1EServiceMIBCompliance.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapUniGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNniSvlanGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanPortStatGroup"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceInfoGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1EServiceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-E-SERVICE-MIB",
    **{"AlaEServiceUNIProfileProtocolTreatment": AlaEServiceUNIProfileProtocolTreatment,
       "AlaEServiceL2CustomProtocolType": AlaEServiceL2CustomProtocolType,
       "alcatelIND1EServiceMIB": alcatelIND1EServiceMIB,
       "alcatelIND1eServiceMIBObjects": alcatelIND1eServiceMIBObjects,
       "alaEService": alaEService,
       "alaEServiceInfo": alaEServiceInfo,
       "alaEServiceMode": alaEServiceMode,
       "alaEServiceStatReset": alaEServiceStatReset,
       "alaEServiceL2MacTunnel": alaEServiceL2MacTunnel,
       "alaEServiceUntaggedMode": alaEServiceUntaggedMode,
       "alaEServiceSapProfileTable": alaEServiceSapProfileTable,
       "alaEServiceSapProfileEntry": alaEServiceSapProfileEntry,
       "alaEServiceSapProfileID": alaEServiceSapProfileID,
       "alaEServiceSapProfileCVLANTreatment": alaEServiceSapProfileCVLANTreatment,
       "alaEServiceSapProfileReplacementCVLAN": alaEServiceSapProfileReplacementCVLAN,
       "alaEServiceSapProfilePriorityMapMode": alaEServiceSapProfilePriorityMapMode,
       "alaEServiceSapProfileFixedPriority": alaEServiceSapProfileFixedPriority,
       "alaEServiceSapProfileIngressBW": alaEServiceSapProfileIngressBW,
       "alaEServiceSapProfileBandwidthShare": alaEServiceSapProfileBandwidthShare,
       "alaEServiceSapProfileRowStatus": alaEServiceSapProfileRowStatus,
       "alaEServiceSapProfileEgressBW": alaEServiceSapProfileEgressBW,
       "alaEServiceSapProfileCIR": alaEServiceSapProfileCIR,
       "alaEServiceSapProfileCBS": alaEServiceSapProfileCBS,
       "alaEServiceSapProfilePIR": alaEServiceSapProfilePIR,
       "alaEServiceSapProfilePBS": alaEServiceSapProfilePBS,
       "alaEServiceSapProfileDepth": alaEServiceSapProfileDepth,
       "alaEServiceUNIProfileTable": alaEServiceUNIProfileTable,
       "alaEServiceUNIProfileEntry": alaEServiceUNIProfileEntry,
       "alaEServiceUNIProfileID": alaEServiceUNIProfileID,
       "alaEServiceUNIProfileStpBpduTreatment": alaEServiceUNIProfileStpBpduTreatment,
       "alaEServiceUNIProfile8021xTreatment": alaEServiceUNIProfile8021xTreatment,
       "alaEServiceUNIProfile8021ABTreatment": alaEServiceUNIProfile8021ABTreatment,
       "alaEServiceUNIProfile8023adTreatment": alaEServiceUNIProfile8023adTreatment,
       "alaEServiceUNIProfileGvrpTreatment": alaEServiceUNIProfileGvrpTreatment,
       "alaEServiceUNIProfileAmapTreatment": alaEServiceUNIProfileAmapTreatment,
       "alaEServiceUNIProfileRowStatus": alaEServiceUNIProfileRowStatus,
       "alaEServiceUNIProfileMvrpTreatment": alaEServiceUNIProfileMvrpTreatment,
       "alaEServiceUNIProfileTunnelMac": alaEServiceUNIProfileTunnelMac,
       "alaEServiceUNIProfileLacpMarkerTreatment": alaEServiceUNIProfileLacpMarkerTreatment,
       "alaEServiceUNIProfileOamTreatment": alaEServiceUNIProfileOamTreatment,
       "alaEServiceUNIProfileCiscoPagpTreatment": alaEServiceUNIProfileCiscoPagpTreatment,
       "alaEServiceUNIProfileCiscoUdldTreatment": alaEServiceUNIProfileCiscoUdldTreatment,
       "alaEServiceUNIProfileCiscoCdpTreatment": alaEServiceUNIProfileCiscoCdpTreatment,
       "alaEServiceUNIProfileCiscoVtpTreatment": alaEServiceUNIProfileCiscoVtpTreatment,
       "alaEServiceUNIProfileCiscoDtpTreatment": alaEServiceUNIProfileCiscoDtpTreatment,
       "alaEServiceUNIProfileCiscoPvstTreatment": alaEServiceUNIProfileCiscoPvstTreatment,
       "alaEServiceUNIProfileCiscoVlanTreatment": alaEServiceUNIProfileCiscoVlanTreatment,
       "alaEServiceUNIProfileCiscoUplinkTreatment": alaEServiceUNIProfileCiscoUplinkTreatment,
       "alaEServiceUNIProfileIeeeMacTreatment": alaEServiceUNIProfileIeeeMacTreatment,
       "alaEServiceTable": alaEServiceTable,
       "alaEServiceEntry": alaEServiceEntry,
       "alaEServiceID": alaEServiceID,
       "alaEServiceSVLAN": alaEServiceSVLAN,
       "alaEServiceVlanType": alaEServiceVlanType,
       "alaEServiceRowStatus": alaEServiceRowStatus,
       "alaEServiceStatGreenCount": alaEServiceStatGreenCount,
       "alaEServiceStatYellowCount": alaEServiceStatYellowCount,
       "alaEServiceStatRedCount": alaEServiceStatRedCount,
       "alaEServiceStatTotalCount": alaEServiceStatTotalCount,
       "alaEServiceSapTable": alaEServiceSapTable,
       "alaEServiceSapEntry": alaEServiceSapEntry,
       "alaEServiceSapID": alaEServiceSapID,
       "alaEServiceSapServiceID": alaEServiceSapServiceID,
       "alaEServiceSapProfile": alaEServiceSapProfile,
       "alaEServiceSapRowStatus": alaEServiceSapRowStatus,
       "alaEServiceSapCvlanTable": alaEServiceSapCvlanTable,
       "alaEServiceSapCvlanEntry": alaEServiceSapCvlanEntry,
       "alaEServiceSapCvlanSapID": alaEServiceSapCvlanSapID,
       "alaEServiceSapCvlanCvlan": alaEServiceSapCvlanCvlan,
       "alaEServiceSapCvlanMapType": alaEServiceSapCvlanMapType,
       "alaEServiceSapCvlanRowStatus": alaEServiceSapCvlanRowStatus,
       "alaEServicePortTable": alaEServicePortTable,
       "alaEServicePortEntry": alaEServicePortEntry,
       "alaEServicePortID": alaEServicePortID,
       "alaEServicePortType": alaEServicePortType,
       "alaEServicePortVendorTpid": alaEServicePortVendorTpid,
       "alaEServicePortLegacyStpBpdu": alaEServicePortLegacyStpBpdu,
       "alaEServicePortLegacyGvrpPdu": alaEServicePortLegacyGvrpPdu,
       "alaEServicePortUniProfile": alaEServicePortUniProfile,
       "alaEServicePortTransBridging": alaEServicePortTransBridging,
       "alaEServicePortLegacyMvrpPdu": alaEServicePortLegacyMvrpPdu,
       "alaEServiceSapUniTable": alaEServiceSapUniTable,
       "alaEServiceSapUniEntry": alaEServiceSapUniEntry,
       "alaEServiceSapUniSap": alaEServiceSapUniSap,
       "alaEServiceSapUniUni": alaEServiceSapUniUni,
       "alaEServiceSapUniRowStatus": alaEServiceSapUniRowStatus,
       "alaEServiceSapUniCvlan": alaEServiceSapUniCvlan,
       "alaEServiceNniSvlanTable": alaEServiceNniSvlanTable,
       "alaEServiceNniSvlanEntry": alaEServiceNniSvlanEntry,
       "alaEServiceNniSvlanNni": alaEServiceNniSvlanNni,
       "alaEServiceNniSvlanSvlan": alaEServiceNniSvlanSvlan,
       "alaEServiceNniSvlanRowStatus": alaEServiceNniSvlanRowStatus,
       "alaEServiceNniSvlanVpaType": alaEServiceNniSvlanVpaType,
       "alaEServiceSapCvlanPortStatTable": alaEServiceSapCvlanPortStatTable,
       "alaEServiceSapCvlanPortStatEntry": alaEServiceSapCvlanPortStatEntry,
       "alaEServiceSapCvlanPortStatSapID": alaEServiceSapCvlanPortStatSapID,
       "alaEServiceSapCvlanPortStatCvlanID": alaEServiceSapCvlanPortStatCvlanID,
       "alaEServiceSapCvlanPortStatPortID": alaEServiceSapCvlanPortStatPortID,
       "alaEServiceSapCvlanPortStatGreenCount": alaEServiceSapCvlanPortStatGreenCount,
       "alaEServiceSapCvlanPortStatYellowCount": alaEServiceSapCvlanPortStatYellowCount,
       "alaEServiceSapCvlanPortStatRedCount": alaEServiceSapCvlanPortStatRedCount,
       "alaEServiceSapCvlanPortStatTotalCount": alaEServiceSapCvlanPortStatTotalCount,
       "alaEServiceUNIProfileL2CustomProtocolTable": alaEServiceUNIProfileL2CustomProtocolTable,
       "alaEServiceUNIProfileL2CustomProtocolEntry": alaEServiceUNIProfileL2CustomProtocolEntry,
       "alaEServiceL2CustomProtocolUNIProfileID": alaEServiceL2CustomProtocolUNIProfileID,
       "alaEServiceUNIProfileL2CustomProtocolID": alaEServiceUNIProfileL2CustomProtocolID,
       "alaEServiceUNIProfileL2CustomProtocolTreatment": alaEServiceUNIProfileL2CustomProtocolTreatment,
       "alaEServiceUNIProfileL2CustomProtocolRowStatus": alaEServiceUNIProfileL2CustomProtocolRowStatus,
       "alaEServiceL2CustomProtocolTable": alaEServiceL2CustomProtocolTable,
       "alaEServiceL2CustomProtocolEntry": alaEServiceL2CustomProtocolEntry,
       "alaEServiceL2CustomProtocolID": alaEServiceL2CustomProtocolID,
       "alaEServiceL2CustomProtocolEntryType": alaEServiceL2CustomProtocolEntryType,
       "alaEServiceL2CustomProtocolMac": alaEServiceL2CustomProtocolMac,
       "alaEServiceL2CustomProtocolMask": alaEServiceL2CustomProtocolMask,
       "alaEServiceL2CustomProtocolEtherType": alaEServiceL2CustomProtocolEtherType,
       "alaEServiceL2CustomProtocolEtherSubType": alaEServiceL2CustomProtocolEtherSubType,
       "alaEServiceL2CustomProtocolSsap": alaEServiceL2CustomProtocolSsap,
       "alaEServiceL2CustomProtocolDsap": alaEServiceL2CustomProtocolDsap,
       "alaEServiceL2CustomProtocolPid": alaEServiceL2CustomProtocolPid,
       "alaEServiceL2CustomProtocolRowStatus": alaEServiceL2CustomProtocolRowStatus,
       "alaEServiceUNIPortL2ProtocolStatisticsTable": alaEServiceUNIPortL2ProtocolStatisticsTable,
       "alaEServiceUNIPortL2ProtocolStatisticsEntry": alaEServiceUNIPortL2ProtocolStatisticsEntry,
       "alaEServiceUNIPortID": alaEServiceUNIPortID,
       "alaEServiceUNIPortL2ProtocolID": alaEServiceUNIPortL2ProtocolID,
       "alaEServiceUNIPortL2RxFrames": alaEServiceUNIPortL2RxFrames,
       "alaEServiceUNIPortL2TunneledFrames": alaEServiceUNIPortL2TunneledFrames,
       "alaEServiceUNIPortL2DroppedFrames": alaEServiceUNIPortL2DroppedFrames,
       "alaEServiceUNIPortL2PeeredFrames": alaEServiceUNIPortL2PeeredFrames,
       "alaEServiceUNIPortL2MACTunneledFrames": alaEServiceUNIPortL2MACTunneledFrames,
       "alaEServiceUNIPortL2MACDeTunneledFrames": alaEServiceUNIPortL2MACDeTunneledFrames,
       "alaEServiceUNIPortL2LastSourceMAC": alaEServiceUNIPortL2LastSourceMAC,
       "alaEServiceNNIPortL2ProtocolStatisticsTable": alaEServiceNNIPortL2ProtocolStatisticsTable,
       "alaEServiceNNIPortL2ProtocolStatisticsEntry": alaEServiceNNIPortL2ProtocolStatisticsEntry,
       "alaEServiceNNIPortID": alaEServiceNNIPortID,
       "alaEServiceNNIPortL2RxMACTunneledFrames": alaEServiceNNIPortL2RxMACTunneledFrames,
       "alaEServiceNNIPortL2MACTunneledDiscardFrames": alaEServiceNNIPortL2MACTunneledDiscardFrames,
       "alaEServiceNNIPortL2ClearStats": alaEServiceNNIPortL2ClearStats,
       "alaEServiceUNIProfileL2ProtocolTotalStatisticsTable": alaEServiceUNIProfileL2ProtocolTotalStatisticsTable,
       "alaEServiceUNIProfileL2ProtocolTotalStatisticsEntry": alaEServiceUNIProfileL2ProtocolTotalStatisticsEntry,
       "alaEServiceUNIProfile": alaEServiceUNIProfile,
       "alaEServiceUNIProfileL2ProtocolTotalRxFrames": alaEServiceUNIProfileL2ProtocolTotalRxFrames,
       "alaEServiceUNIProfileL2ProtocolClearStats": alaEServiceUNIProfileL2ProtocolClearStats,
       "alaEServiceUNIProfileIEEEL2ProtocolStatisticsTable": alaEServiceUNIProfileIEEEL2ProtocolStatisticsTable,
       "alaEServiceUNIProfileIEEEL2ProtocolStatisticsEntry": alaEServiceUNIProfileIEEEL2ProtocolStatisticsEntry,
       "alaEServiceUNIProfileIEEEL2ProfileID": alaEServiceUNIProfileIEEEL2ProfileID,
       "alaEServiceUNIProfileIEEEL2ProtocolIndex": alaEServiceUNIProfileIEEEL2ProtocolIndex,
       "alaEServiceUNIProfileIEEEL2ProtocolRxFrames": alaEServiceUNIProfileIEEEL2ProtocolRxFrames,
       "alaEServiceUNIProfileIEEEL2ProtocolTreatment": alaEServiceUNIProfileIEEEL2ProtocolTreatment,
       "alaEServiceUNIProfileCustomL2ProtocolStatisticsTable": alaEServiceUNIProfileCustomL2ProtocolStatisticsTable,
       "alaEServiceUNIProfileCustomL2ProtocolStatisticsEntry": alaEServiceUNIProfileCustomL2ProtocolStatisticsEntry,
       "alaEServiceUNIProfileCustomL2StatsProfileID": alaEServiceUNIProfileCustomL2StatsProfileID,
       "alaEServiceUNIProfileCustomL2ProtocolIndex": alaEServiceUNIProfileCustomL2ProtocolIndex,
       "alaEServiceUNIProfileCustomL2ProtocolRxFrames": alaEServiceUNIProfileCustomL2ProtocolRxFrames,
       "alaEServiceUNIProfileCustomL2ProtocolTreatment": alaEServiceUNIProfileCustomL2ProtocolTreatment,
       "alaEServiceL2PTProtocolStatisticsClear": alaEServiceL2PTProtocolStatisticsClear,
       "alaEServiceUNIPortL2GlobalClearStatistics": alaEServiceUNIPortL2GlobalClearStatistics,
       "alaEServiceNNIPortL2GlobalClearStatistics": alaEServiceNNIPortL2GlobalClearStatistics,
       "alaEServiceUNIProfileL2GlobalClearStatistics": alaEServiceUNIProfileL2GlobalClearStatistics,
       "alaEServiceUNIPortL2ProtocolStatisticsClearTable": alaEServiceUNIPortL2ProtocolStatisticsClearTable,
       "alaEServiceUNIPortL2ProtocolStatisticsClearEntry": alaEServiceUNIPortL2ProtocolStatisticsClearEntry,
       "alaEServiceUNIPortClearID": alaEServiceUNIPortClearID,
       "alaEServiceUNIPortL2ClearStats": alaEServiceUNIPortL2ClearStats,
       "alaEServiceNNIPortL2ProtocolStatisticsClearTable": alaEServiceNNIPortL2ProtocolStatisticsClearTable,
       "alaEServiceNNIPortL2ProtocolStatisticsClearEntry": alaEServiceNNIPortL2ProtocolStatisticsClearEntry,
       "alaEServiceNNIPortClearID": alaEServiceNNIPortClearID,
       "alaEServiceNNIPortL2ClearStatistics": alaEServiceNNIPortL2ClearStatistics,
       "alcatelIND1EServiceMIBConformance": alcatelIND1EServiceMIBConformance,
       "alcatelIND1EServiceMIBGroups": alcatelIND1EServiceMIBGroups,
       "alaEServiceSapProfileGroup": alaEServiceSapProfileGroup,
       "alaEServiceUNIProfileGroup": alaEServiceUNIProfileGroup,
       "alaEServiceGroup": alaEServiceGroup,
       "alaEServiceSapGroup": alaEServiceSapGroup,
       "alaEServiceSapCvlanGroup": alaEServiceSapCvlanGroup,
       "alaEServicePortGroup": alaEServicePortGroup,
       "alaEServiceSapUniGroup": alaEServiceSapUniGroup,
       "alaEServiceNniSvlanGroup": alaEServiceNniSvlanGroup,
       "alaEServiceSapCvlanPortStatGroup": alaEServiceSapCvlanPortStatGroup,
       "alaEServiceInfoGroup": alaEServiceInfoGroup,
       "alaEServiceUNIProfileL2CustomProtocolGroup": alaEServiceUNIProfileL2CustomProtocolGroup,
       "alaEServiceL2CustomProtocolGroup": alaEServiceL2CustomProtocolGroup,
       "alaEServiceUNIPortL2StatisticsGroup": alaEServiceUNIPortL2StatisticsGroup,
       "alaEServiceNNIPortL2StatisticsGroup": alaEServiceNNIPortL2StatisticsGroup,
       "alaEServiceUNIProfileL2ProtocolTotalStatisticsGroup": alaEServiceUNIProfileL2ProtocolTotalStatisticsGroup,
       "alaEServiceUNIProfileIEEEL2ProtocolStatisticsGroup": alaEServiceUNIProfileIEEEL2ProtocolStatisticsGroup,
       "alaEServiceUNIProfileL2ProtocolStatisticsGroup": alaEServiceUNIProfileL2ProtocolStatisticsGroup,
       "alaEServiceL2PTProtocolStatisticsClearGroup": alaEServiceL2PTProtocolStatisticsClearGroup,
       "alaEServiceUNIPortL2StatisticsClearGroup": alaEServiceUNIPortL2StatisticsClearGroup,
       "alaEServiceNNIPortL2StatisticsClearGroup": alaEServiceNNIPortL2StatisticsClearGroup,
       "alcatelIND1EServiceMIBCompliances": alcatelIND1EServiceMIBCompliances,
       "alcatelIND1EServiceMIBCompliance": alcatelIND1EServiceMIBCompliance}
)
