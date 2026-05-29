# SNMP MIB module (HH3C-LswDHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-LswDHCP-MIB

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

(hh3clswCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3clswCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cLswDhcpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8)
)
if mibBuilder.loadTexts:
    hh3cLswDhcpMib.setRevisions(
        ("2001-06-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cLswDhcpMibObject_ObjectIdentity = ObjectIdentity
hh3cLswDhcpMibObject = _Hh3cLswDhcpMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1)
)
_Hh3cDhcpGroupTable_Object = MibTable
hh3cDhcpGroupTable = _Hh3cDhcpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDhcpGroupTable.setStatus("current")
_Hh3cDhcpGroupEntry_Object = MibTableRow
hh3cDhcpGroupEntry = _Hh3cDhcpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 1, 1)
)
hh3cDhcpGroupEntry.setIndexNames(
    (0, "HH3C-LswDHCP-MIB", "hh3cDhcpGroupID"),
)
if mibBuilder.loadTexts:
    hh3cDhcpGroupEntry.setStatus("current")


class _Hh3cDhcpGroupID_Type(Integer32):
    """Custom type hh3cDhcpGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_Hh3cDhcpGroupID_Type.__name__ = "Integer32"
_Hh3cDhcpGroupID_Object = MibTableColumn
hh3cDhcpGroupID = _Hh3cDhcpGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 1, 1, 1),
    _Hh3cDhcpGroupID_Type()
)
hh3cDhcpGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpGroupID.setStatus("current")
_Hh3cIpDhcpServerAddress1_Type = IpAddress
_Hh3cIpDhcpServerAddress1_Object = MibTableColumn
hh3cIpDhcpServerAddress1 = _Hh3cIpDhcpServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 1, 1, 2),
    _Hh3cIpDhcpServerAddress1_Type()
)
hh3cIpDhcpServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpDhcpServerAddress1.setStatus("current")
_Hh3cIpDhcpServerAddress2_Type = IpAddress
_Hh3cIpDhcpServerAddress2_Object = MibTableColumn
hh3cIpDhcpServerAddress2 = _Hh3cIpDhcpServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 1, 1, 3),
    _Hh3cIpDhcpServerAddress2_Type()
)
hh3cIpDhcpServerAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpDhcpServerAddress2.setStatus("current")
_Hh3cDhcpRowStatus_Type = RowStatus
_Hh3cDhcpRowStatus_Object = MibTableColumn
hh3cDhcpRowStatus = _Hh3cDhcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 1, 1, 4),
    _Hh3cDhcpRowStatus_Type()
)
hh3cDhcpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpRowStatus.setStatus("current")
_Hh3cDhcpSecurityTable_Object = MibTable
hh3cDhcpSecurityTable = _Hh3cDhcpSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDhcpSecurityTable.setStatus("current")
_Hh3cDhcpSecurityEntry_Object = MibTableRow
hh3cDhcpSecurityEntry = _Hh3cDhcpSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 2, 1)
)
hh3cDhcpSecurityEntry.setIndexNames(
    (0, "HH3C-LswDHCP-MIB", "hh3cDhcpClientIpAddress"),
)
if mibBuilder.loadTexts:
    hh3cDhcpSecurityEntry.setStatus("current")
_Hh3cDhcpClientIpAddress_Type = IpAddress
_Hh3cDhcpClientIpAddress_Object = MibTableColumn
hh3cDhcpClientIpAddress = _Hh3cDhcpClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 2, 1, 1),
    _Hh3cDhcpClientIpAddress_Type()
)
hh3cDhcpClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpClientIpAddress.setStatus("current")
_Hh3cDhcpClientMacAddress_Type = MacAddress
_Hh3cDhcpClientMacAddress_Object = MibTableColumn
hh3cDhcpClientMacAddress = _Hh3cDhcpClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 2, 1, 2),
    _Hh3cDhcpClientMacAddress_Type()
)
hh3cDhcpClientMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpClientMacAddress.setStatus("current")


class _Hh3cDhcpClientProperty_Type(Integer32):
    """Custom type hh3cDhcpClientProperty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_Hh3cDhcpClientProperty_Type.__name__ = "Integer32"
_Hh3cDhcpClientProperty_Object = MibTableColumn
hh3cDhcpClientProperty = _Hh3cDhcpClientProperty_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 2, 1, 3),
    _Hh3cDhcpClientProperty_Type()
)
hh3cDhcpClientProperty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpClientProperty.setStatus("current")
_Hh3cDhcpClientRowStatus_Type = RowStatus
_Hh3cDhcpClientRowStatus_Object = MibTableColumn
hh3cDhcpClientRowStatus = _Hh3cDhcpClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 2, 1, 4),
    _Hh3cDhcpClientRowStatus_Type()
)
hh3cDhcpClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpClientRowStatus.setStatus("current")
_Hh3cDhcpToL3IfTable_Object = MibTable
hh3cDhcpToL3IfTable = _Hh3cDhcpToL3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDhcpToL3IfTable.setStatus("current")
_Hh3cDhcpToL3IfEntry_Object = MibTableRow
hh3cDhcpToL3IfEntry = _Hh3cDhcpToL3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 3, 1)
)
hh3cDhcpToL3IfEntry.setIndexNames(
    (0, "HH3C-LswDHCP-MIB", "hh3cDhcpToL3VlanIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cDhcpToL3IfEntry.setStatus("current")
_Hh3cDhcpToL3VlanIfIndex_Type = Integer32
_Hh3cDhcpToL3VlanIfIndex_Object = MibTableColumn
hh3cDhcpToL3VlanIfIndex = _Hh3cDhcpToL3VlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 3, 1, 1),
    _Hh3cDhcpToL3VlanIfIndex_Type()
)
hh3cDhcpToL3VlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpToL3VlanIfIndex.setStatus("current")


class _Hh3cDhcpToL3GroupId_Type(Integer32):
    """Custom type hh3cDhcpToL3GroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_Hh3cDhcpToL3GroupId_Type.__name__ = "Integer32"
_Hh3cDhcpToL3GroupId_Object = MibTableColumn
hh3cDhcpToL3GroupId = _Hh3cDhcpToL3GroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 3, 1, 2),
    _Hh3cDhcpToL3GroupId_Type()
)
hh3cDhcpToL3GroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpToL3GroupId.setStatus("current")


class _Hh3cDhcpToL3AddressCheck_Type(Integer32):
    """Custom type hh3cDhcpToL3AddressCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_Hh3cDhcpToL3AddressCheck_Type.__name__ = "Integer32"
_Hh3cDhcpToL3AddressCheck_Object = MibTableColumn
hh3cDhcpToL3AddressCheck = _Hh3cDhcpToL3AddressCheck_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 3, 1, 3),
    _Hh3cDhcpToL3AddressCheck_Type()
)
hh3cDhcpToL3AddressCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpToL3AddressCheck.setStatus("current")
_Hh3cDhcpToL3RowStatus_Type = RowStatus
_Hh3cDhcpToL3RowStatus_Object = MibTableColumn
hh3cDhcpToL3RowStatus = _Hh3cDhcpToL3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 8, 1, 3, 1, 4),
    _Hh3cDhcpToL3RowStatus_Type()
)
hh3cDhcpToL3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpToL3RowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LswDHCP-MIB",
    **{"hh3cLswDhcpMib": hh3cLswDhcpMib,
       "hh3cLswDhcpMibObject": hh3cLswDhcpMibObject,
       "hh3cDhcpGroupTable": hh3cDhcpGroupTable,
       "hh3cDhcpGroupEntry": hh3cDhcpGroupEntry,
       "hh3cDhcpGroupID": hh3cDhcpGroupID,
       "hh3cIpDhcpServerAddress1": hh3cIpDhcpServerAddress1,
       "hh3cIpDhcpServerAddress2": hh3cIpDhcpServerAddress2,
       "hh3cDhcpRowStatus": hh3cDhcpRowStatus,
       "hh3cDhcpSecurityTable": hh3cDhcpSecurityTable,
       "hh3cDhcpSecurityEntry": hh3cDhcpSecurityEntry,
       "hh3cDhcpClientIpAddress": hh3cDhcpClientIpAddress,
       "hh3cDhcpClientMacAddress": hh3cDhcpClientMacAddress,
       "hh3cDhcpClientProperty": hh3cDhcpClientProperty,
       "hh3cDhcpClientRowStatus": hh3cDhcpClientRowStatus,
       "hh3cDhcpToL3IfTable": hh3cDhcpToL3IfTable,
       "hh3cDhcpToL3IfEntry": hh3cDhcpToL3IfEntry,
       "hh3cDhcpToL3VlanIfIndex": hh3cDhcpToL3VlanIfIndex,
       "hh3cDhcpToL3GroupId": hh3cDhcpToL3GroupId,
       "hh3cDhcpToL3AddressCheck": hh3cDhcpToL3AddressCheck,
       "hh3cDhcpToL3RowStatus": hh3cDhcpToL3RowStatus}
)
