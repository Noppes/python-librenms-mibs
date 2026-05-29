# SNMP MIB module (OG-LIGHTHOUSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\opengear\OG-LIGHTHOUSE-MIB

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

(ogSpecific,) = mibBuilder.importSymbols(
    "OG-SMI-MIB",
    "ogSpecific")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ogLighthouseMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1)
)
if mibBuilder.loadTexts:
    ogLighthouseMib.setRevisions(
        ("2021-05-20 00:00",
         "2019-03-20 00:00",
         "2018-01-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgLhStatus_ObjectIdentity = ObjectIdentity
ogLhStatus = _OgLhStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1)
)


class _OgLhVersion_Type(DisplayString):
    """Custom type ogLhVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgLhVersion_Type.__name__ = "DisplayString"
_OgLhVersion_Object = MibScalar
ogLhVersion = _OgLhVersion_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 1),
    _OgLhVersion_Type()
)
ogLhVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhVersion.setStatus("current")
_OgLhNodes_ObjectIdentity = ObjectIdentity
ogLhNodes = _OgLhNodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2)
)


class _OgLhNodesTotal_Type(Integer32):
    """Custom type ogLhNodesTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgLhNodesTotal_Type.__name__ = "Integer32"
_OgLhNodesTotal_Object = MibScalar
ogLhNodesTotal = _OgLhNodesTotal_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 1),
    _OgLhNodesTotal_Type()
)
ogLhNodesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodesTotal.setStatus("current")


class _OgLhNodesPending_Type(Integer32):
    """Custom type ogLhNodesPending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgLhNodesPending_Type.__name__ = "Integer32"
_OgLhNodesPending_Object = MibScalar
ogLhNodesPending = _OgLhNodesPending_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 2),
    _OgLhNodesPending_Type()
)
ogLhNodesPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodesPending.setStatus("current")


class _OgLhNodesConnected_Type(Integer32):
    """Custom type ogLhNodesConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgLhNodesConnected_Type.__name__ = "Integer32"
_OgLhNodesConnected_Object = MibScalar
ogLhNodesConnected = _OgLhNodesConnected_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 3),
    _OgLhNodesConnected_Type()
)
ogLhNodesConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodesConnected.setStatus("current")


class _OgLhNodesDisconnected_Type(Integer32):
    """Custom type ogLhNodesDisconnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgLhNodesDisconnected_Type.__name__ = "Integer32"
_OgLhNodesDisconnected_Object = MibScalar
ogLhNodesDisconnected = _OgLhNodesDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 4),
    _OgLhNodesDisconnected_Type()
)
ogLhNodesDisconnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodesDisconnected.setStatus("current")
_OgLhNodesTable_Object = MibTable
ogLhNodesTable = _OgLhNodesTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ogLhNodesTable.setStatus("current")
_OgLhNodeEntry_Object = MibTableRow
ogLhNodeEntry = _OgLhNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1)
)
ogLhNodeEntry.setIndexNames(
    (0, "OG-LIGHTHOUSE-MIB", "ogLhNodeIndex"),
)
if mibBuilder.loadTexts:
    ogLhNodeEntry.setStatus("current")
_OgLhNodeIndex_Type = IpAddress
_OgLhNodeIndex_Object = MibTableColumn
ogLhNodeIndex = _OgLhNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 1),
    _OgLhNodeIndex_Type()
)
ogLhNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodeIndex.setStatus("current")


class _OgLhNodeName_Type(DisplayString):
    """Custom type ogLhNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgLhNodeName_Type.__name__ = "DisplayString"
_OgLhNodeName_Object = MibTableColumn
ogLhNodeName = _OgLhNodeName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 2),
    _OgLhNodeName_Type()
)
ogLhNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodeName.setStatus("current")


class _OgLhNodeModel_Type(DisplayString):
    """Custom type ogLhNodeModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_OgLhNodeModel_Type.__name__ = "DisplayString"
_OgLhNodeModel_Object = MibTableColumn
ogLhNodeModel = _OgLhNodeModel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 3),
    _OgLhNodeModel_Type()
)
ogLhNodeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodeModel.setStatus("current")


class _OgLhNodeProductType_Type(DisplayString):
    """Custom type ogLhNodeProductType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgLhNodeProductType_Type.__name__ = "DisplayString"
_OgLhNodeProductType_Object = MibTableColumn
ogLhNodeProductType = _OgLhNodeProductType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 4),
    _OgLhNodeProductType_Type()
)
ogLhNodeProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodeProductType.setStatus("current")


class _OgLhNodeVpnAddress_Type(DisplayString):
    """Custom type ogLhNodeVpnAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgLhNodeVpnAddress_Type.__name__ = "DisplayString"
_OgLhNodeVpnAddress_Object = MibTableColumn
ogLhNodeVpnAddress = _OgLhNodeVpnAddress_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 5),
    _OgLhNodeVpnAddress_Type()
)
ogLhNodeVpnAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodeVpnAddress.setStatus("current")


class _OgLhNodeSerialNumber_Type(DisplayString):
    """Custom type ogLhNodeSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgLhNodeSerialNumber_Type.__name__ = "DisplayString"
_OgLhNodeSerialNumber_Object = MibTableColumn
ogLhNodeSerialNumber = _OgLhNodeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 6),
    _OgLhNodeSerialNumber_Type()
)
ogLhNodeSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodeSerialNumber.setStatus("current")


class _OgLhNodeUptime_Type(DisplayString):
    """Custom type ogLhNodeUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgLhNodeUptime_Type.__name__ = "DisplayString"
_OgLhNodeUptime_Object = MibTableColumn
ogLhNodeUptime = _OgLhNodeUptime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 7),
    _OgLhNodeUptime_Type()
)
ogLhNodeUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodeUptime.setStatus("current")


class _OgLhNodeConnStatus_Type(Integer32):
    """Custom type ogLhNodeConnStatus based on Integer32"""
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
        *(("notAvailable", 0),
          ("connected", 1),
          ("disconnected", 2),
          ("unknown", 3))
    )


_OgLhNodeConnStatus_Type.__name__ = "Integer32"
_OgLhNodeConnStatus_Object = MibTableColumn
ogLhNodeConnStatus = _OgLhNodeConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 8),
    _OgLhNodeConnStatus_Type()
)
ogLhNodeConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodeConnStatus.setStatus("current")
_OgLhNodePortsContainer_Type = ObjectIdentifier
_OgLhNodePortsContainer_Object = MibTableColumn
ogLhNodePortsContainer = _OgLhNodePortsContainer_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 9),
    _OgLhNodePortsContainer_Type()
)
ogLhNodePortsContainer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodePortsContainer.setStatus("current")
_OgLhNodePortsTable_Object = MibTable
ogLhNodePortsTable = _OgLhNodePortsTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 9, 1)
)
if mibBuilder.loadTexts:
    ogLhNodePortsTable.setStatus("current")
_OgLhNodePortEntry_Object = MibTableRow
ogLhNodePortEntry = _OgLhNodePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 9, 1, 1)
)
ogLhNodePortEntry.setIndexNames(
    (0, "OG-LIGHTHOUSE-MIB", "ogLhNodeIndex"),
    (0, "OG-LIGHTHOUSE-MIB", "ogLhPortIndex"),
)
if mibBuilder.loadTexts:
    ogLhNodePortEntry.setStatus("current")


class _OgLhPortIndex_Type(Integer32):
    """Custom type ogLhPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgLhPortIndex_Type.__name__ = "Integer32"
_OgLhPortIndex_Object = MibTableColumn
ogLhPortIndex = _OgLhPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 9, 1, 1, 1),
    _OgLhPortIndex_Type()
)
ogLhPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhPortIndex.setStatus("current")


class _OgLhPortLabel_Type(DisplayString):
    """Custom type ogLhPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_OgLhPortLabel_Type.__name__ = "DisplayString"
_OgLhPortLabel_Object = MibTableColumn
ogLhPortLabel = _OgLhPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 9, 1, 1, 2),
    _OgLhPortLabel_Type()
)
ogLhPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhPortLabel.setStatus("current")


class _OgLhPortID_Type(DisplayString):
    """Custom type ogLhPortID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_OgLhPortID_Type.__name__ = "DisplayString"
_OgLhPortID_Object = MibTableColumn
ogLhPortID = _OgLhPortID_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 9, 1, 1, 3),
    _OgLhPortID_Type()
)
ogLhPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhPortID.setStatus("current")
_OgLhNodeInterfacesContainer_Type = ObjectIdentifier
_OgLhNodeInterfacesContainer_Object = MibTableColumn
ogLhNodeInterfacesContainer = _OgLhNodeInterfacesContainer_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 10),
    _OgLhNodeInterfacesContainer_Type()
)
ogLhNodeInterfacesContainer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodeInterfacesContainer.setStatus("current")
_OgLhNodeInterfacesTable_Object = MibTable
ogLhNodeInterfacesTable = _OgLhNodeInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 10, 1)
)
if mibBuilder.loadTexts:
    ogLhNodeInterfacesTable.setStatus("current")
_OgLhNodeInterfaceEntry_Object = MibTableRow
ogLhNodeInterfaceEntry = _OgLhNodeInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 10, 1, 1)
)
ogLhNodeInterfaceEntry.setIndexNames(
    (0, "OG-LIGHTHOUSE-MIB", "ogLhNodeIndex"),
    (0, "OG-LIGHTHOUSE-MIB", "ogLhNodeInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ogLhNodeInterfaceEntry.setStatus("current")


class _OgLhNodeInterfaceIndex_Type(Integer32):
    """Custom type ogLhNodeInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgLhNodeInterfaceIndex_Type.__name__ = "Integer32"
_OgLhNodeInterfaceIndex_Object = MibTableColumn
ogLhNodeInterfaceIndex = _OgLhNodeInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 10, 1, 1, 1),
    _OgLhNodeInterfaceIndex_Type()
)
ogLhNodeInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodeInterfaceIndex.setStatus("current")


class _OgLhNodeInterfaceName_Type(DisplayString):
    """Custom type ogLhNodeInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_OgLhNodeInterfaceName_Type.__name__ = "DisplayString"
_OgLhNodeInterfaceName_Object = MibTableColumn
ogLhNodeInterfaceName = _OgLhNodeInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 10, 1, 1, 2),
    _OgLhNodeInterfaceName_Type()
)
ogLhNodeInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodeInterfaceName.setStatus("current")


class _OgLhNodeInterfaceAddress_Type(DisplayString):
    """Custom type ogLhNodeInterfaceAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_OgLhNodeInterfaceAddress_Type.__name__ = "DisplayString"
_OgLhNodeInterfaceAddress_Object = MibTableColumn
ogLhNodeInterfaceAddress = _OgLhNodeInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 10, 1, 1, 3),
    _OgLhNodeInterfaceAddress_Type()
)
ogLhNodeInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodeInterfaceAddress.setStatus("current")


class _OgLhNodeCellularHealth_Type(Integer32):
    """Custom type ogLhNodeCellularHealth based on Integer32"""
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
          ("pending", 1),
          ("bad", 2),
          ("moderate", 3),
          ("good", 4),
          ("simissues", 5),
          ("connectivitytestfailed", 6))
    )


_OgLhNodeCellularHealth_Type.__name__ = "Integer32"
_OgLhNodeCellularHealth_Object = MibTableColumn
ogLhNodeCellularHealth = _OgLhNodeCellularHealth_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 5, 1, 11),
    _OgLhNodeCellularHealth_Type()
)
ogLhNodeCellularHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodeCellularHealth.setStatus("current")
_OgLhThirdPartyNodesTable_Object = MibTable
ogLhThirdPartyNodesTable = _OgLhThirdPartyNodesTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ogLhThirdPartyNodesTable.setStatus("current")
_OgLhThirdPartyNodeEntry_Object = MibTableRow
ogLhThirdPartyNodeEntry = _OgLhThirdPartyNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1)
)
ogLhThirdPartyNodeEntry.setIndexNames(
    (0, "OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeIndex"),
)
if mibBuilder.loadTexts:
    ogLhThirdPartyNodeEntry.setStatus("current")


class _OgLhThirdPartyNodeIndex_Type(Integer32):
    """Custom type ogLhThirdPartyNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483645),
    )


_OgLhThirdPartyNodeIndex_Type.__name__ = "Integer32"
_OgLhThirdPartyNodeIndex_Object = MibTableColumn
ogLhThirdPartyNodeIndex = _OgLhThirdPartyNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 1),
    _OgLhThirdPartyNodeIndex_Type()
)
ogLhThirdPartyNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyNodeIndex.setStatus("current")


class _OgLhThirdPartyNodeSSHPort_Type(Integer32):
    """Custom type ogLhThirdPartyNodeSSHPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgLhThirdPartyNodeSSHPort_Type.__name__ = "Integer32"
_OgLhThirdPartyNodeSSHPort_Object = MibTableColumn
ogLhThirdPartyNodeSSHPort = _OgLhThirdPartyNodeSSHPort_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 2),
    _OgLhThirdPartyNodeSSHPort_Type()
)
ogLhThirdPartyNodeSSHPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyNodeSSHPort.setStatus("current")


class _OgLhThirdPartyNodeName_Type(DisplayString):
    """Custom type ogLhThirdPartyNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgLhThirdPartyNodeName_Type.__name__ = "DisplayString"
_OgLhThirdPartyNodeName_Object = MibTableColumn
ogLhThirdPartyNodeName = _OgLhThirdPartyNodeName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 3),
    _OgLhThirdPartyNodeName_Type()
)
ogLhThirdPartyNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyNodeName.setStatus("current")


class _OgLhThirdPartyNodeModel_Type(DisplayString):
    """Custom type ogLhThirdPartyNodeModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_OgLhThirdPartyNodeModel_Type.__name__ = "DisplayString"
_OgLhThirdPartyNodeModel_Object = MibTableColumn
ogLhThirdPartyNodeModel = _OgLhThirdPartyNodeModel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 4),
    _OgLhThirdPartyNodeModel_Type()
)
ogLhThirdPartyNodeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyNodeModel.setStatus("current")


class _OgLhThirdPartyNodeProductType_Type(DisplayString):
    """Custom type ogLhThirdPartyNodeProductType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgLhThirdPartyNodeProductType_Type.__name__ = "DisplayString"
_OgLhThirdPartyNodeProductType_Object = MibTableColumn
ogLhThirdPartyNodeProductType = _OgLhThirdPartyNodeProductType_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 5),
    _OgLhThirdPartyNodeProductType_Type()
)
ogLhThirdPartyNodeProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyNodeProductType.setStatus("current")


class _OgLhThirdPartyNodeAddress_Type(DisplayString):
    """Custom type ogLhThirdPartyNodeAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgLhThirdPartyNodeAddress_Type.__name__ = "DisplayString"
_OgLhThirdPartyNodeAddress_Object = MibTableColumn
ogLhThirdPartyNodeAddress = _OgLhThirdPartyNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 6),
    _OgLhThirdPartyNodeAddress_Type()
)
ogLhThirdPartyNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyNodeAddress.setStatus("current")


class _OgLhThirdPartyNodeSerialNumber_Type(DisplayString):
    """Custom type ogLhThirdPartyNodeSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgLhThirdPartyNodeSerialNumber_Type.__name__ = "DisplayString"
_OgLhThirdPartyNodeSerialNumber_Object = MibTableColumn
ogLhThirdPartyNodeSerialNumber = _OgLhThirdPartyNodeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 7),
    _OgLhThirdPartyNodeSerialNumber_Type()
)
ogLhThirdPartyNodeSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyNodeSerialNumber.setStatus("current")


class _OgLhThirdPartyNodeUptime_Type(DisplayString):
    """Custom type ogLhThirdPartyNodeUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgLhThirdPartyNodeUptime_Type.__name__ = "DisplayString"
_OgLhThirdPartyNodeUptime_Object = MibTableColumn
ogLhThirdPartyNodeUptime = _OgLhThirdPartyNodeUptime_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 8),
    _OgLhThirdPartyNodeUptime_Type()
)
ogLhThirdPartyNodeUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyNodeUptime.setStatus("current")


class _OgLhThirdPartyNodeConnStatus_Type(Integer32):
    """Custom type ogLhThirdPartyNodeConnStatus based on Integer32"""
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
        *(("notAvailable", 0),
          ("connected", 1),
          ("disconnected", 2),
          ("unknown", 3))
    )


_OgLhThirdPartyNodeConnStatus_Type.__name__ = "Integer32"
_OgLhThirdPartyNodeConnStatus_Object = MibTableColumn
ogLhThirdPartyNodeConnStatus = _OgLhThirdPartyNodeConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 9),
    _OgLhThirdPartyNodeConnStatus_Type()
)
ogLhThirdPartyNodeConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyNodeConnStatus.setStatus("current")
_OgLhThirdPartyNodePortsContainer_Type = ObjectIdentifier
_OgLhThirdPartyNodePortsContainer_Object = MibTableColumn
ogLhThirdPartyNodePortsContainer = _OgLhThirdPartyNodePortsContainer_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 10),
    _OgLhThirdPartyNodePortsContainer_Type()
)
ogLhThirdPartyNodePortsContainer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyNodePortsContainer.setStatus("current")
_OgLhThirdPartyNodePortsTable_Object = MibTable
ogLhThirdPartyNodePortsTable = _OgLhThirdPartyNodePortsTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 10, 1)
)
if mibBuilder.loadTexts:
    ogLhThirdPartyNodePortsTable.setStatus("current")
_OgLhThirdPartyNodePortEntry_Object = MibTableRow
ogLhThirdPartyNodePortEntry = _OgLhThirdPartyNodePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 10, 1, 1)
)
ogLhThirdPartyNodePortEntry.setIndexNames(
    (0, "OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeIndex"),
    (0, "OG-LIGHTHOUSE-MIB", "ogLhPortIndex"),
)
if mibBuilder.loadTexts:
    ogLhThirdPartyNodePortEntry.setStatus("current")


class _OgLhThirdPartyPortIndex_Type(Integer32):
    """Custom type ogLhThirdPartyPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgLhThirdPartyPortIndex_Type.__name__ = "Integer32"
_OgLhThirdPartyPortIndex_Object = MibTableColumn
ogLhThirdPartyPortIndex = _OgLhThirdPartyPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 10, 1, 1, 1),
    _OgLhThirdPartyPortIndex_Type()
)
ogLhThirdPartyPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyPortIndex.setStatus("current")


class _OgLhThirdPartyPortLabel_Type(DisplayString):
    """Custom type ogLhThirdPartyPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_OgLhThirdPartyPortLabel_Type.__name__ = "DisplayString"
_OgLhThirdPartyPortLabel_Object = MibTableColumn
ogLhThirdPartyPortLabel = _OgLhThirdPartyPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 10, 1, 1, 2),
    _OgLhThirdPartyPortLabel_Type()
)
ogLhThirdPartyPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyPortLabel.setStatus("current")


class _OgLhThirdPartyPortConnectionMethod_Type(DisplayString):
    """Custom type ogLhThirdPartyPortConnectionMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OgLhThirdPartyPortConnectionMethod_Type.__name__ = "DisplayString"
_OgLhThirdPartyPortConnectionMethod_Object = MibTableColumn
ogLhThirdPartyPortConnectionMethod = _OgLhThirdPartyPortConnectionMethod_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 10, 1, 1, 3),
    _OgLhThirdPartyPortConnectionMethod_Type()
)
ogLhThirdPartyPortConnectionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyPortConnectionMethod.setStatus("current")


class _OgLhThirdPartyPortMode_Type(DisplayString):
    """Custom type ogLhThirdPartyPortMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgLhThirdPartyPortMode_Type.__name__ = "DisplayString"
_OgLhThirdPartyPortMode_Object = MibTableColumn
ogLhThirdPartyPortMode = _OgLhThirdPartyPortMode_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 10, 1, 1, 4),
    _OgLhThirdPartyPortMode_Type()
)
ogLhThirdPartyPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyPortMode.setStatus("current")


class _OgLhThirdPartyRemotePort_Type(Integer32):
    """Custom type ogLhThirdPartyRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgLhThirdPartyRemotePort_Type.__name__ = "Integer32"
_OgLhThirdPartyRemotePort_Object = MibTableColumn
ogLhThirdPartyRemotePort = _OgLhThirdPartyRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 10, 1, 1, 5),
    _OgLhThirdPartyRemotePort_Type()
)
ogLhThirdPartyRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyRemotePort.setStatus("current")


class _OgLhThirdPartyPortLineID_Type(DisplayString):
    """Custom type ogLhThirdPartyPortLineID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgLhThirdPartyPortLineID_Type.__name__ = "DisplayString"
_OgLhThirdPartyPortLineID_Object = MibTableColumn
ogLhThirdPartyPortLineID = _OgLhThirdPartyPortLineID_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 6, 1, 10, 1, 1, 6),
    _OgLhThirdPartyPortLineID_Type()
)
ogLhThirdPartyPortLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhThirdPartyPortLineID.setStatus("current")


class _OgLhNodesRejected_Type(Integer32):
    """Custom type ogLhNodesRejected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgLhNodesRejected_Type.__name__ = "Integer32"
_OgLhNodesRejected_Object = MibScalar
ogLhNodesRejected = _OgLhNodesRejected_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 2, 7),
    _OgLhNodesRejected_Type()
)
ogLhNodesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhNodesRejected.setStatus("current")
_OgLhLicenseStatus_ObjectIdentity = ObjectIdentity
ogLhLicenseStatus = _OgLhLicenseStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 3)
)


class _OgLhLicInstalled_Type(Integer32):
    """Custom type ogLhLicInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgLhLicInstalled_Type.__name__ = "Integer32"
_OgLhLicInstalled_Object = MibScalar
ogLhLicInstalled = _OgLhLicInstalled_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 3, 1),
    _OgLhLicInstalled_Type()
)
ogLhLicInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhLicInstalled.setStatus("current")


class _OgLhLicSupported_Type(Integer32):
    """Custom type ogLhLicSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgLhLicSupported_Type.__name__ = "Integer32"
_OgLhLicSupported_Object = MibScalar
ogLhLicSupported = _OgLhLicSupported_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 3, 2),
    _OgLhLicSupported_Type()
)
ogLhLicSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhLicSupported.setStatus("current")
_OgLhLicExpiry_Type = DateAndTime
_OgLhLicExpiry_Object = MibScalar
ogLhLicExpiry = _OgLhLicExpiry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 3, 3),
    _OgLhLicExpiry_Type()
)
ogLhLicExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhLicExpiry.setStatus("current")


class _OgLhLicStatus_Type(DisplayString):
    """Custom type ogLhLicStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_OgLhLicStatus_Type.__name__ = "DisplayString"
_OgLhLicStatus_Object = MibScalar
ogLhLicStatus = _OgLhLicStatus_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 3, 4),
    _OgLhLicStatus_Type()
)
ogLhLicStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhLicStatus.setStatus("current")
_OgLhLicFeaturesTable_Object = MibTable
ogLhLicFeaturesTable = _OgLhLicFeaturesTable_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    ogLhLicFeaturesTable.setStatus("current")
_OgLhLicFeatureEntry_Object = MibTableRow
ogLhLicFeatureEntry = _OgLhLicFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 3, 5, 1)
)
ogLhLicFeatureEntry.setIndexNames(
    (0, "OG-LIGHTHOUSE-MIB", "ogLhLicFeatureIndex"),
)
if mibBuilder.loadTexts:
    ogLhLicFeatureEntry.setStatus("current")


class _OgLhLicFeatureIndex_Type(Integer32):
    """Custom type ogLhLicFeatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OgLhLicFeatureIndex_Type.__name__ = "Integer32"
_OgLhLicFeatureIndex_Object = MibTableColumn
ogLhLicFeatureIndex = _OgLhLicFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 3, 5, 1, 1),
    _OgLhLicFeatureIndex_Type()
)
ogLhLicFeatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ogLhLicFeatureIndex.setStatus("current")


class _OgLhLicFeatureName_Type(DisplayString):
    """Custom type ogLhLicFeatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_OgLhLicFeatureName_Type.__name__ = "DisplayString"
_OgLhLicFeatureName_Object = MibTableColumn
ogLhLicFeatureName = _OgLhLicFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 1, 3, 5, 1, 2),
    _OgLhLicFeatureName_Type()
)
ogLhLicFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhLicFeatureName.setStatus("current")
_NodeTraps_ObjectIdentity = ObjectIdentity
nodeTraps = _NodeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 100)
)
_NodeNotifs_ObjectIdentity = ObjectIdentity
nodeNotifs = _NodeNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 100, 0)
)
_OgLhConfigFields_ObjectIdentity = ObjectIdentity
ogLhConfigFields = _OgLhConfigFields_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 101)
)


class _OgLhConfigName_Type(DisplayString):
    """Custom type ogLhConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OgLhConfigName_Type.__name__ = "DisplayString"
_OgLhConfigName_Object = MibScalar
ogLhConfigName = _OgLhConfigName_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 101, 1),
    _OgLhConfigName_Type()
)
ogLhConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhConfigName.setStatus("current")


class _OgLhConfigStatus_Type(Integer32):
    """Custom type ogLhConfigStatus based on Integer32"""
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
        *(("okay", 0),
          ("outOfSync", 1),
          ("error", 2),
          ("unknown", 3))
    )


_OgLhConfigStatus_Type.__name__ = "Integer32"
_OgLhConfigStatus_Object = MibScalar
ogLhConfigStatus = _OgLhConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 101, 2),
    _OgLhConfigStatus_Type()
)
ogLhConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogLhConfigStatus.setStatus("current")
_OgLighthouseConformance_ObjectIdentity = ObjectIdentity
ogLighthouseConformance = _OgLighthouseConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 65535)
)
_OgLighthouseCompliances_ObjectIdentity = ObjectIdentity
ogLighthouseCompliances = _OgLighthouseCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 65535, 1)
)
_OgLighthouseGroups_ObjectIdentity = ObjectIdentity
ogLighthouseGroups = _OgLighthouseGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 65535, 2)
)

# Managed Objects groups

ogLhStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 65535, 2, 1)
)
ogLhStatusGroup.setObjects(
      *(("OG-LIGHTHOUSE-MIB", "ogLhVersion"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodesTotal"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodesPending"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodesRejected"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodesConnected"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodesDisconnected"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeIndex"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeName"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeModel"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeProductType"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeVpnAddress"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeSerialNumber"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeUptime"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeConnStatus"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodePortsContainer"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeCellularHealth"),
        ("OG-LIGHTHOUSE-MIB", "ogLhPortIndex"),
        ("OG-LIGHTHOUSE-MIB", "ogLhPortLabel"),
        ("OG-LIGHTHOUSE-MIB", "ogLhPortID"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeInterfacesContainer"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeInterfaceIndex"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeInterfaceName"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeInterfaceAddress"),
        ("OG-LIGHTHOUSE-MIB", "ogLhLicFeatureName"),
        ("OG-LIGHTHOUSE-MIB", "ogLhLicInstalled"),
        ("OG-LIGHTHOUSE-MIB", "ogLhLicSupported"),
        ("OG-LIGHTHOUSE-MIB", "ogLhLicExpiry"),
        ("OG-LIGHTHOUSE-MIB", "ogLhLicStatus"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeIndex"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeSSHPort"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeName"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeModel"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeProductType"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeAddress"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeSerialNumber"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeUptime"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeConnStatus"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodePortsContainer"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyPortIndex"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyPortLabel"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyPortConnectionMethod"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyPortMode"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyRemotePort"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyPortLineID"),
        ("OG-LIGHTHOUSE-MIB", "ogLhConfigName"),
        ("OG-LIGHTHOUSE-MIB", "ogLhConfigStatus"))
)
if mibBuilder.loadTexts:
    ogLhStatusGroup.setStatus("current")


# Notification objects

nodeStatusNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 100, 0, 1)
)
nodeStatusNotif.setObjects(
      *(("OG-LIGHTHOUSE-MIB", "ogLhNodeName"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeIndex"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeConnStatus"))
)
if mibBuilder.loadTexts:
    nodeStatusNotif.setStatus(
        "current"
    )

thirdPartyNodeStatusNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 100, 0, 2)
)
thirdPartyNodeStatusNotif.setObjects(
      *(("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeName"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeIndex"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeAddress"),
        ("OG-LIGHTHOUSE-MIB", "ogLhThirdPartyNodeConnStatus"))
)
if mibBuilder.loadTexts:
    thirdPartyNodeStatusNotif.setStatus(
        "current"
    )

cellularHealthStatusNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 100, 0, 3)
)
cellularHealthStatusNotif.setObjects(
      *(("OG-LIGHTHOUSE-MIB", "ogLhNodeName"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeIndex"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNodeCellularHealth"))
)
if mibBuilder.loadTexts:
    cellularHealthStatusNotif.setStatus(
        "current"
    )

secondaryReplicationStatusNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 100, 0, 4)
)
secondaryReplicationStatusNotif.setObjects(
      *(("OG-LIGHTHOUSE-MIB", "ogLhConfigName"),
        ("OG-LIGHTHOUSE-MIB", "ogLhConfigStatus"))
)
if mibBuilder.loadTexts:
    secondaryReplicationStatusNotif.setStatus(
        "current"
    )


# Notifications groups

ogLhNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 65535, 2, 2)
)
ogLhNotificationGroup.setObjects(
      *(("OG-LIGHTHOUSE-MIB", "nodeStatusNotif"),
        ("OG-LIGHTHOUSE-MIB", "thirdPartyNodeStatusNotif"),
        ("OG-LIGHTHOUSE-MIB", "cellularHealthStatusNotif"),
        ("OG-LIGHTHOUSE-MIB", "secondaryReplicationStatusNotif"))
)
if mibBuilder.loadTexts:
    ogLhNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ogLighthouseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25049, 18, 1, 65535, 1, 1)
)
ogLighthouseCompliance.setObjects(
      *(("OG-LIGHTHOUSE-MIB", "ogLhStatusGroup"),
        ("OG-LIGHTHOUSE-MIB", "ogLhNotificationGroup"))
)
if mibBuilder.loadTexts:
    ogLighthouseCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-LIGHTHOUSE-MIB",
    **{"ogLighthouseMib": ogLighthouseMib,
       "ogLhStatus": ogLhStatus,
       "ogLhVersion": ogLhVersion,
       "ogLhNodes": ogLhNodes,
       "ogLhNodesTotal": ogLhNodesTotal,
       "ogLhNodesPending": ogLhNodesPending,
       "ogLhNodesConnected": ogLhNodesConnected,
       "ogLhNodesDisconnected": ogLhNodesDisconnected,
       "ogLhNodesTable": ogLhNodesTable,
       "ogLhNodeEntry": ogLhNodeEntry,
       "ogLhNodeIndex": ogLhNodeIndex,
       "ogLhNodeName": ogLhNodeName,
       "ogLhNodeModel": ogLhNodeModel,
       "ogLhNodeProductType": ogLhNodeProductType,
       "ogLhNodeVpnAddress": ogLhNodeVpnAddress,
       "ogLhNodeSerialNumber": ogLhNodeSerialNumber,
       "ogLhNodeUptime": ogLhNodeUptime,
       "ogLhNodeConnStatus": ogLhNodeConnStatus,
       "ogLhNodePortsContainer": ogLhNodePortsContainer,
       "ogLhNodePortsTable": ogLhNodePortsTable,
       "ogLhNodePortEntry": ogLhNodePortEntry,
       "ogLhPortIndex": ogLhPortIndex,
       "ogLhPortLabel": ogLhPortLabel,
       "ogLhPortID": ogLhPortID,
       "ogLhNodeInterfacesContainer": ogLhNodeInterfacesContainer,
       "ogLhNodeInterfacesTable": ogLhNodeInterfacesTable,
       "ogLhNodeInterfaceEntry": ogLhNodeInterfaceEntry,
       "ogLhNodeInterfaceIndex": ogLhNodeInterfaceIndex,
       "ogLhNodeInterfaceName": ogLhNodeInterfaceName,
       "ogLhNodeInterfaceAddress": ogLhNodeInterfaceAddress,
       "ogLhNodeCellularHealth": ogLhNodeCellularHealth,
       "ogLhThirdPartyNodesTable": ogLhThirdPartyNodesTable,
       "ogLhThirdPartyNodeEntry": ogLhThirdPartyNodeEntry,
       "ogLhThirdPartyNodeIndex": ogLhThirdPartyNodeIndex,
       "ogLhThirdPartyNodeSSHPort": ogLhThirdPartyNodeSSHPort,
       "ogLhThirdPartyNodeName": ogLhThirdPartyNodeName,
       "ogLhThirdPartyNodeModel": ogLhThirdPartyNodeModel,
       "ogLhThirdPartyNodeProductType": ogLhThirdPartyNodeProductType,
       "ogLhThirdPartyNodeAddress": ogLhThirdPartyNodeAddress,
       "ogLhThirdPartyNodeSerialNumber": ogLhThirdPartyNodeSerialNumber,
       "ogLhThirdPartyNodeUptime": ogLhThirdPartyNodeUptime,
       "ogLhThirdPartyNodeConnStatus": ogLhThirdPartyNodeConnStatus,
       "ogLhThirdPartyNodePortsContainer": ogLhThirdPartyNodePortsContainer,
       "ogLhThirdPartyNodePortsTable": ogLhThirdPartyNodePortsTable,
       "ogLhThirdPartyNodePortEntry": ogLhThirdPartyNodePortEntry,
       "ogLhThirdPartyPortIndex": ogLhThirdPartyPortIndex,
       "ogLhThirdPartyPortLabel": ogLhThirdPartyPortLabel,
       "ogLhThirdPartyPortConnectionMethod": ogLhThirdPartyPortConnectionMethod,
       "ogLhThirdPartyPortMode": ogLhThirdPartyPortMode,
       "ogLhThirdPartyRemotePort": ogLhThirdPartyRemotePort,
       "ogLhThirdPartyPortLineID": ogLhThirdPartyPortLineID,
       "ogLhNodesRejected": ogLhNodesRejected,
       "ogLhLicenseStatus": ogLhLicenseStatus,
       "ogLhLicInstalled": ogLhLicInstalled,
       "ogLhLicSupported": ogLhLicSupported,
       "ogLhLicExpiry": ogLhLicExpiry,
       "ogLhLicStatus": ogLhLicStatus,
       "ogLhLicFeaturesTable": ogLhLicFeaturesTable,
       "ogLhLicFeatureEntry": ogLhLicFeatureEntry,
       "ogLhLicFeatureIndex": ogLhLicFeatureIndex,
       "ogLhLicFeatureName": ogLhLicFeatureName,
       "nodeTraps": nodeTraps,
       "nodeNotifs": nodeNotifs,
       "nodeStatusNotif": nodeStatusNotif,
       "thirdPartyNodeStatusNotif": thirdPartyNodeStatusNotif,
       "cellularHealthStatusNotif": cellularHealthStatusNotif,
       "secondaryReplicationStatusNotif": secondaryReplicationStatusNotif,
       "ogLhConfigFields": ogLhConfigFields,
       "ogLhConfigName": ogLhConfigName,
       "ogLhConfigStatus": ogLhConfigStatus,
       "ogLighthouseConformance": ogLighthouseConformance,
       "ogLighthouseCompliances": ogLighthouseCompliances,
       "ogLighthouseCompliance": ogLighthouseCompliance,
       "ogLighthouseGroups": ogLighthouseGroups,
       "ogLhStatusGroup": ogLhStatusGroup,
       "ogLhNotificationGroup": ogLhNotificationGroup}
)
