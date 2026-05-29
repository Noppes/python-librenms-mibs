# SNMP MIB module (HH3C-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-STACK-MIB

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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cStack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91)
)
if mibBuilder.loadTexts:
    hh3cStack.setRevisions(
        ("2021-03-25 09:43",
         "2014-11-20 08:50",
         "2014-08-11 06:41",
         "2013-10-23 00:00",
         "2013-08-16 00:00",
         "2012-02-24 00:00",
         "2008-04-30 16:50")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cStackGlobalConfig_ObjectIdentity = ObjectIdentity
hh3cStackGlobalConfig = _Hh3cStackGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1)
)
_Hh3cStackMaxMember_Type = Integer32
_Hh3cStackMaxMember_Object = MibScalar
hh3cStackMaxMember = _Hh3cStackMaxMember_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 1),
    _Hh3cStackMaxMember_Type()
)
hh3cStackMaxMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackMaxMember.setStatus("current")
_Hh3cStackMemberNum_Type = Integer32
_Hh3cStackMemberNum_Object = MibScalar
hh3cStackMemberNum = _Hh3cStackMemberNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 2),
    _Hh3cStackMemberNum_Type()
)
hh3cStackMemberNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackMemberNum.setStatus("current")
_Hh3cStackMaxConfigPriority_Type = Integer32
_Hh3cStackMaxConfigPriority_Object = MibScalar
hh3cStackMaxConfigPriority = _Hh3cStackMaxConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 3),
    _Hh3cStackMaxConfigPriority_Type()
)
hh3cStackMaxConfigPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackMaxConfigPriority.setStatus("current")


class _Hh3cStackAutoUpdate_Type(Integer32):
    """Custom type hh3cStackAutoUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Hh3cStackAutoUpdate_Type.__name__ = "Integer32"
_Hh3cStackAutoUpdate_Object = MibScalar
hh3cStackAutoUpdate = _Hh3cStackAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 4),
    _Hh3cStackAutoUpdate_Type()
)
hh3cStackAutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStackAutoUpdate.setStatus("current")


class _Hh3cStackMacPersistence_Type(Integer32):
    """Custom type hh3cStackMacPersistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPersist", 1),
          ("persistForSixMin", 2),
          ("persistForever", 3))
    )


_Hh3cStackMacPersistence_Type.__name__ = "Integer32"
_Hh3cStackMacPersistence_Object = MibScalar
hh3cStackMacPersistence = _Hh3cStackMacPersistence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 5),
    _Hh3cStackMacPersistence_Type()
)
hh3cStackMacPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStackMacPersistence.setStatus("current")


class _Hh3cStackLinkDelayInterval_Type(Integer32):
    """Custom type hh3cStackLinkDelayInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cStackLinkDelayInterval_Type.__name__ = "Integer32"
_Hh3cStackLinkDelayInterval_Object = MibScalar
hh3cStackLinkDelayInterval = _Hh3cStackLinkDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 6),
    _Hh3cStackLinkDelayInterval_Type()
)
hh3cStackLinkDelayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStackLinkDelayInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cStackLinkDelayInterval.setUnits("millisecond")


class _Hh3cStackTopology_Type(Integer32):
    """Custom type hh3cStackTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chainConn", 1),
          ("ringConn", 2))
    )


_Hh3cStackTopology_Type.__name__ = "Integer32"
_Hh3cStackTopology_Object = MibScalar
hh3cStackTopology = _Hh3cStackTopology_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 7),
    _Hh3cStackTopology_Type()
)
hh3cStackTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackTopology.setStatus("current")


class _Hh3cStackDomainId_Type(Unsigned32):
    """Custom type hh3cStackDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cStackDomainId_Type.__name__ = "Unsigned32"
_Hh3cStackDomainId_Object = MibScalar
hh3cStackDomainId = _Hh3cStackDomainId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 8),
    _Hh3cStackDomainId_Type()
)
hh3cStackDomainId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStackDomainId.setStatus("current")


class _Hh3cStackPortConfigActivate_Type(Integer32):
    """Custom type hh3cStackPortConfigActivate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("set", 2))
    )


_Hh3cStackPortConfigActivate_Type.__name__ = "Integer32"
_Hh3cStackPortConfigActivate_Object = MibScalar
hh3cStackPortConfigActivate = _Hh3cStackPortConfigActivate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 1, 9),
    _Hh3cStackPortConfigActivate_Type()
)
hh3cStackPortConfigActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStackPortConfigActivate.setStatus("current")
_Hh3cStackDeviceConfigTable_Object = MibTable
hh3cStackDeviceConfigTable = _Hh3cStackDeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 2)
)
if mibBuilder.loadTexts:
    hh3cStackDeviceConfigTable.setStatus("current")
_Hh3cStackDeviceConfigEntry_Object = MibTableRow
hh3cStackDeviceConfigEntry = _Hh3cStackDeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 2, 1)
)
hh3cStackDeviceConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cStackDeviceConfigEntry.setStatus("current")
_Hh3cStackMemberID_Type = Integer32
_Hh3cStackMemberID_Object = MibTableColumn
hh3cStackMemberID = _Hh3cStackMemberID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 2, 1, 1),
    _Hh3cStackMemberID_Type()
)
hh3cStackMemberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackMemberID.setStatus("current")
_Hh3cStackConfigMemberID_Type = Integer32
_Hh3cStackConfigMemberID_Object = MibTableColumn
hh3cStackConfigMemberID = _Hh3cStackConfigMemberID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 2, 1, 2),
    _Hh3cStackConfigMemberID_Type()
)
hh3cStackConfigMemberID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStackConfigMemberID.setStatus("current")
_Hh3cStackPriority_Type = Integer32
_Hh3cStackPriority_Object = MibTableColumn
hh3cStackPriority = _Hh3cStackPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 2, 1, 3),
    _Hh3cStackPriority_Type()
)
hh3cStackPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStackPriority.setStatus("current")
_Hh3cStackPortNum_Type = Integer32
_Hh3cStackPortNum_Object = MibTableColumn
hh3cStackPortNum = _Hh3cStackPortNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 2, 1, 4),
    _Hh3cStackPortNum_Type()
)
hh3cStackPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackPortNum.setStatus("current")
_Hh3cStackPortMaxNum_Type = Integer32
_Hh3cStackPortMaxNum_Object = MibTableColumn
hh3cStackPortMaxNum = _Hh3cStackPortMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 2, 1, 5),
    _Hh3cStackPortMaxNum_Type()
)
hh3cStackPortMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackPortMaxNum.setStatus("current")
_Hh3cStackBoardConfigTable_Object = MibTable
hh3cStackBoardConfigTable = _Hh3cStackBoardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 3)
)
if mibBuilder.loadTexts:
    hh3cStackBoardConfigTable.setStatus("current")
_Hh3cStackBoardConfigEntry_Object = MibTableRow
hh3cStackBoardConfigEntry = _Hh3cStackBoardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 3, 1)
)
hh3cStackBoardConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cStackBoardConfigEntry.setStatus("current")


class _Hh3cStackBoardRole_Type(Integer32):
    """Custom type hh3cStackBoardRole based on Integer32"""
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
        *(("slave", 1),
          ("master", 2),
          ("loading", 3),
          ("other", 4))
    )


_Hh3cStackBoardRole_Type.__name__ = "Integer32"
_Hh3cStackBoardRole_Object = MibTableColumn
hh3cStackBoardRole = _Hh3cStackBoardRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 3, 1, 1),
    _Hh3cStackBoardRole_Type()
)
hh3cStackBoardRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackBoardRole.setStatus("current")
_Hh3cStackBoardBelongtoMember_Type = Integer32
_Hh3cStackBoardBelongtoMember_Object = MibTableColumn
hh3cStackBoardBelongtoMember = _Hh3cStackBoardBelongtoMember_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 3, 1, 2),
    _Hh3cStackBoardBelongtoMember_Type()
)
hh3cStackBoardBelongtoMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackBoardBelongtoMember.setStatus("current")
_Hh3cStackPortInfoTable_Object = MibTable
hh3cStackPortInfoTable = _Hh3cStackPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 4)
)
if mibBuilder.loadTexts:
    hh3cStackPortInfoTable.setStatus("current")
_Hh3cStackPortInfoEntry_Object = MibTableRow
hh3cStackPortInfoEntry = _Hh3cStackPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 4, 1)
)
hh3cStackPortInfoEntry.setIndexNames(
    (0, "HH3C-STACK-MIB", "hh3cStackMemberID"),
    (0, "HH3C-STACK-MIB", "hh3cStackPortIndex"),
)
if mibBuilder.loadTexts:
    hh3cStackPortInfoEntry.setStatus("current")
_Hh3cStackPortIndex_Type = Integer32
_Hh3cStackPortIndex_Object = MibTableColumn
hh3cStackPortIndex = _Hh3cStackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 4, 1, 1),
    _Hh3cStackPortIndex_Type()
)
hh3cStackPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cStackPortIndex.setStatus("current")


class _Hh3cStackPortEnable_Type(Integer32):
    """Custom type hh3cStackPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Hh3cStackPortEnable_Type.__name__ = "Integer32"
_Hh3cStackPortEnable_Object = MibTableColumn
hh3cStackPortEnable = _Hh3cStackPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 4, 1, 2),
    _Hh3cStackPortEnable_Type()
)
hh3cStackPortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackPortEnable.setStatus("current")


class _Hh3cStackPortStatus_Type(Integer32):
    """Custom type hh3cStackPortStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("silent", 3),
          ("disabled", 4))
    )


_Hh3cStackPortStatus_Type.__name__ = "Integer32"
_Hh3cStackPortStatus_Object = MibTableColumn
hh3cStackPortStatus = _Hh3cStackPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 4, 1, 3),
    _Hh3cStackPortStatus_Type()
)
hh3cStackPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackPortStatus.setStatus("current")
_Hh3cStackNeighbor_Type = Integer32
_Hh3cStackNeighbor_Object = MibTableColumn
hh3cStackNeighbor = _Hh3cStackNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 4, 1, 4),
    _Hh3cStackNeighbor_Type()
)
hh3cStackNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackNeighbor.setStatus("current")


class _Hh3cStackPortForwardingPath_Type(OctetString):
    """Custom type hh3cStackPortForwardingPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_Hh3cStackPortForwardingPath_Type.__name__ = "OctetString"
_Hh3cStackPortForwardingPath_Object = MibTableColumn
hh3cStackPortForwardingPath = _Hh3cStackPortForwardingPath_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 4, 1, 5),
    _Hh3cStackPortForwardingPath_Type()
)
hh3cStackPortForwardingPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStackPortForwardingPath.setStatus("current")
_Hh3cStackPhyPortInfoTable_Object = MibTable
hh3cStackPhyPortInfoTable = _Hh3cStackPhyPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 5)
)
if mibBuilder.loadTexts:
    hh3cStackPhyPortInfoTable.setStatus("current")
_Hh3cStackPhyPortInfoEntry_Object = MibTableRow
hh3cStackPhyPortInfoEntry = _Hh3cStackPhyPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 5, 1)
)
hh3cStackPhyPortInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cStackPhyPortInfoEntry.setStatus("current")
_Hh3cStackBelongtoPort_Type = Integer32
_Hh3cStackBelongtoPort_Object = MibTableColumn
hh3cStackBelongtoPort = _Hh3cStackBelongtoPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 5, 1, 1),
    _Hh3cStackBelongtoPort_Type()
)
hh3cStackBelongtoPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStackBelongtoPort.setStatus("current")
_Hh3cStackTrap_ObjectIdentity = ObjectIdentity
hh3cStackTrap = _Hh3cStackTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6)
)
_Hh3cStackTrapOjbects_ObjectIdentity = ObjectIdentity
hh3cStackTrapOjbects = _Hh3cStackTrapOjbects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 0)
)
_Hh3cStackTrapObjectDefinitions_ObjectIdentity = ObjectIdentity
hh3cStackTrapObjectDefinitions = _Hh3cStackTrapObjectDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 1)
)


class _Hh3cStackPhysicalIntfName_Type(OctetString):
    """Custom type hh3cStackPhysicalIntfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3cStackPhysicalIntfName_Type.__name__ = "OctetString"
_Hh3cStackPhysicalIntfName_Object = MibScalar
hh3cStackPhysicalIntfName = _Hh3cStackPhysicalIntfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 1, 1),
    _Hh3cStackPhysicalIntfName_Type()
)
hh3cStackPhysicalIntfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cStackPhysicalIntfName.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cStackPortLinkStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 0, 1)
)
hh3cStackPortLinkStatusChange.setObjects(
      *(("HH3C-STACK-MIB", "hh3cStackMemberID"),
        ("HH3C-STACK-MIB", "hh3cStackPortIndex"),
        ("HH3C-STACK-MIB", "hh3cStackPortStatus"))
)
if mibBuilder.loadTexts:
    hh3cStackPortLinkStatusChange.setStatus(
        "current"
    )

hh3cStackTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 0, 2)
)
hh3cStackTopologyChange.setObjects(
    ("HH3C-STACK-MIB", "hh3cStackTopology")
)
if mibBuilder.loadTexts:
    hh3cStackTopologyChange.setStatus(
        "current"
    )

hh3cStackMadBfdChangeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 0, 3)
)
hh3cStackMadBfdChangeNormal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cStackMadBfdChangeNormal.setStatus(
        "current"
    )

hh3cStackMadBfdChangeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 0, 4)
)
hh3cStackMadBfdChangeFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cStackMadBfdChangeFailure.setStatus(
        "current"
    )

hh3cStackMadLacpChangeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 0, 5)
)
hh3cStackMadLacpChangeNormal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cStackMadLacpChangeNormal.setStatus(
        "current"
    )

hh3cStackMadLacpChangeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 0, 6)
)
hh3cStackMadLacpChangeFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cStackMadLacpChangeFailure.setStatus(
        "current"
    )

hh3cStackPhysicalIntfLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 0, 7)
)
hh3cStackPhysicalIntfLinkUp.setObjects(
      *(("HH3C-STACK-MIB", "hh3cStackMemberID"),
        ("HH3C-STACK-MIB", "hh3cStackPortIndex"),
        ("HH3C-STACK-MIB", "hh3cStackPhysicalIntfName"))
)
if mibBuilder.loadTexts:
    hh3cStackPhysicalIntfLinkUp.setStatus(
        "current"
    )

hh3cStackPhysicalIntfLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 0, 8)
)
hh3cStackPhysicalIntfLinkDown.setObjects(
      *(("HH3C-STACK-MIB", "hh3cStackMemberID"),
        ("HH3C-STACK-MIB", "hh3cStackPortIndex"),
        ("HH3C-STACK-MIB", "hh3cStackPhysicalIntfName"))
)
if mibBuilder.loadTexts:
    hh3cStackPhysicalIntfLinkDown.setStatus(
        "current"
    )

hh3cStackPhysicalIntfRxTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 91, 6, 0, 9)
)
hh3cStackPhysicalIntfRxTimeout.setObjects(
      *(("HH3C-STACK-MIB", "hh3cStackMemberID"),
        ("HH3C-STACK-MIB", "hh3cStackPortIndex"),
        ("HH3C-STACK-MIB", "hh3cStackPhysicalIntfName"))
)
if mibBuilder.loadTexts:
    hh3cStackPhysicalIntfRxTimeout.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-STACK-MIB",
    **{"hh3cStack": hh3cStack,
       "hh3cStackGlobalConfig": hh3cStackGlobalConfig,
       "hh3cStackMaxMember": hh3cStackMaxMember,
       "hh3cStackMemberNum": hh3cStackMemberNum,
       "hh3cStackMaxConfigPriority": hh3cStackMaxConfigPriority,
       "hh3cStackAutoUpdate": hh3cStackAutoUpdate,
       "hh3cStackMacPersistence": hh3cStackMacPersistence,
       "hh3cStackLinkDelayInterval": hh3cStackLinkDelayInterval,
       "hh3cStackTopology": hh3cStackTopology,
       "hh3cStackDomainId": hh3cStackDomainId,
       "hh3cStackPortConfigActivate": hh3cStackPortConfigActivate,
       "hh3cStackDeviceConfigTable": hh3cStackDeviceConfigTable,
       "hh3cStackDeviceConfigEntry": hh3cStackDeviceConfigEntry,
       "hh3cStackMemberID": hh3cStackMemberID,
       "hh3cStackConfigMemberID": hh3cStackConfigMemberID,
       "hh3cStackPriority": hh3cStackPriority,
       "hh3cStackPortNum": hh3cStackPortNum,
       "hh3cStackPortMaxNum": hh3cStackPortMaxNum,
       "hh3cStackBoardConfigTable": hh3cStackBoardConfigTable,
       "hh3cStackBoardConfigEntry": hh3cStackBoardConfigEntry,
       "hh3cStackBoardRole": hh3cStackBoardRole,
       "hh3cStackBoardBelongtoMember": hh3cStackBoardBelongtoMember,
       "hh3cStackPortInfoTable": hh3cStackPortInfoTable,
       "hh3cStackPortInfoEntry": hh3cStackPortInfoEntry,
       "hh3cStackPortIndex": hh3cStackPortIndex,
       "hh3cStackPortEnable": hh3cStackPortEnable,
       "hh3cStackPortStatus": hh3cStackPortStatus,
       "hh3cStackNeighbor": hh3cStackNeighbor,
       "hh3cStackPortForwardingPath": hh3cStackPortForwardingPath,
       "hh3cStackPhyPortInfoTable": hh3cStackPhyPortInfoTable,
       "hh3cStackPhyPortInfoEntry": hh3cStackPhyPortInfoEntry,
       "hh3cStackBelongtoPort": hh3cStackBelongtoPort,
       "hh3cStackTrap": hh3cStackTrap,
       "hh3cStackTrapOjbects": hh3cStackTrapOjbects,
       "hh3cStackPortLinkStatusChange": hh3cStackPortLinkStatusChange,
       "hh3cStackTopologyChange": hh3cStackTopologyChange,
       "hh3cStackMadBfdChangeNormal": hh3cStackMadBfdChangeNormal,
       "hh3cStackMadBfdChangeFailure": hh3cStackMadBfdChangeFailure,
       "hh3cStackMadLacpChangeNormal": hh3cStackMadLacpChangeNormal,
       "hh3cStackMadLacpChangeFailure": hh3cStackMadLacpChangeFailure,
       "hh3cStackPhysicalIntfLinkUp": hh3cStackPhysicalIntfLinkUp,
       "hh3cStackPhysicalIntfLinkDown": hh3cStackPhysicalIntfLinkDown,
       "hh3cStackPhysicalIntfRxTimeout": hh3cStackPhysicalIntfRxTimeout,
       "hh3cStackTrapObjectDefinitions": hh3cStackTrapObjectDefinitions,
       "hh3cStackPhysicalIntfName": hh3cStackPhysicalIntfName}
)
