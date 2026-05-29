# SNMP MIB module (XCONNECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sagemcom\XCONNECTION-MIB

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

(SagemBoolean,) = mibBuilder.importSymbols(
    "EQUIPMENT-MIB",
    "SagemBoolean")

(sagemDr,) = mibBuilder.importSymbols(
    "SAGEM-DR-MIB",
    "sagemDr")

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

xconnection = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 108)
)


# Types definitions



class TrafficStatus(Integer32):
    """Custom type TrafficStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("working", 1),
          ("protection", 2))
    )





class ProtectionType(Integer32):
    """Custom type ProtectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("snc", 1))
    )





class ProtectionStatus(Integer32):
    """Custom type ProtectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("used", 1))
    )





class LinkDirection(Integer32):
    """Custom type LinkDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unidirectional", 1),
          ("bidirectional", 2))
    )





class CTPType(Integer32):
    """Custom type CTPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10,
              20,
              50,
              51,
              52,
              53,
              60,
              61,
              62,
              100)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("au", 1),
          ("au4c", 2),
          ("au16c", 3),
          ("tu3", 10),
          ("tu12", 20),
          ("pdh2M", 50),
          ("pdh34M", 51),
          ("pdh45M", 52),
          ("pdh140M", 53),
          ("eth10M", 60),
          ("eth100M", 61),
          ("eth1G", 62),
          ("nspi", 100))
    )





class XconDir(Integer32):
    """Custom type XconDir based on Integer32"""
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
          ("unidirectional", 1),
          ("bidirectional", 2))
    )





class ActionType(Integer32):
    """Custom type ActionType based on Integer32"""
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
          ("creation", 1),
          ("deletion", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Link_ObjectIdentity = ObjectIdentity
link = _Link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10)
)


class _LinkNumber_Type(Integer32):
    """Custom type linkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LinkNumber_Type.__name__ = "Integer32"
_LinkNumber_Object = MibScalar
linkNumber = _LinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 1),
    _LinkNumber_Type()
)
linkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNumber.setStatus("current")
_LinkTable_Object = MibTable
linkTable = _LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 2)
)
if mibBuilder.loadTexts:
    linkTable.setStatus("current")
_LinkEntry_Object = MibTableRow
linkEntry = _LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1)
)
linkEntry.setIndexNames(
    (0, "XCONNECTION-MIB", "linkIndex"),
)
if mibBuilder.loadTexts:
    linkEntry.setStatus("current")


class _LinkIndex_Type(Integer32):
    """Custom type linkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LinkIndex_Type.__name__ = "Integer32"
_LinkIndex_Object = MibTableColumn
linkIndex = _LinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 1),
    _LinkIndex_Type()
)
linkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkIndex.setStatus("current")
_LinkSinkType_Type = CTPType
_LinkSinkType_Object = MibTableColumn
linkSinkType = _LinkSinkType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 2),
    _LinkSinkType_Type()
)
linkSinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSinkType.setStatus("current")
_LinkSrcType_Type = CTPType
_LinkSrcType_Object = MibTableColumn
linkSrcType = _LinkSrcType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 3),
    _LinkSrcType_Type()
)
linkSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSrcType.setStatus("current")


class _LinkCTPSink_Type(Integer32):
    """Custom type linkCTPSink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LinkCTPSink_Type.__name__ = "Integer32"
_LinkCTPSink_Object = MibTableColumn
linkCTPSink = _LinkCTPSink_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 4),
    _LinkCTPSink_Type()
)
linkCTPSink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCTPSink.setStatus("current")


class _LinkCTPSource_Type(Integer32):
    """Custom type linkCTPSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LinkCTPSource_Type.__name__ = "Integer32"
_LinkCTPSource_Object = MibTableColumn
linkCTPSource = _LinkCTPSource_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 5),
    _LinkCTPSource_Type()
)
linkCTPSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkCTPSource.setStatus("current")
_LinkName_Type = DisplayString
_LinkName_Object = MibTableColumn
linkName = _LinkName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 6),
    _LinkName_Type()
)
linkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkName.setStatus("current")


class _LinkGroupId_Type(Integer32):
    """Custom type linkGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LinkGroupId_Type.__name__ = "Integer32"
_LinkGroupId_Object = MibTableColumn
linkGroupId = _LinkGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 7),
    _LinkGroupId_Type()
)
linkGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkGroupId.setStatus("current")
_LinkDirection_Type = LinkDirection
_LinkDirection_Object = MibTableColumn
linkDirection = _LinkDirection_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 8),
    _LinkDirection_Type()
)
linkDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDirection.setStatus("current")
_LinkProtectionType_Type = ProtectionType
_LinkProtectionType_Object = MibTableColumn
linkProtectionType = _LinkProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 9),
    _LinkProtectionType_Type()
)
linkProtectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkProtectionType.setStatus("current")
_LinkProtectionStatus_Type = ProtectionStatus
_LinkProtectionStatus_Object = MibTableColumn
linkProtectionStatus = _LinkProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 10),
    _LinkProtectionStatus_Type()
)
linkProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkProtectionStatus.setStatus("current")
_LinkTrafficStatus_Type = TrafficStatus
_LinkTrafficStatus_Object = MibTableColumn
linkTrafficStatus = _LinkTrafficStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 11),
    _LinkTrafficStatus_Type()
)
linkTrafficStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTrafficStatus.setStatus("current")
_LinkImplementation_Type = SagemBoolean
_LinkImplementation_Object = MibTableColumn
linkImplementation = _LinkImplementation_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 10, 2, 1, 12),
    _LinkImplementation_Type()
)
linkImplementation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkImplementation.setStatus("current")
_Xcon_ObjectIdentity = ObjectIdentity
xcon = _Xcon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 108, 30)
)


class _XconNumber_Type(Integer32):
    """Custom type xconNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XconNumber_Type.__name__ = "Integer32"
_XconNumber_Object = MibScalar
xconNumber = _XconNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 30, 1),
    _XconNumber_Type()
)
xconNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconNumber.setStatus("current")
_XconSinkType_Type = CTPType
_XconSinkType_Object = MibScalar
xconSinkType = _XconSinkType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 30, 2),
    _XconSinkType_Type()
)
xconSinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconSinkType.setStatus("current")


class _XconSinkIndex_Type(Integer32):
    """Custom type xconSinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XconSinkIndex_Type.__name__ = "Integer32"
_XconSinkIndex_Object = MibScalar
xconSinkIndex = _XconSinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 30, 3),
    _XconSinkIndex_Type()
)
xconSinkIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconSinkIndex.setStatus("current")
_XconSrcType_Type = CTPType
_XconSrcType_Object = MibScalar
xconSrcType = _XconSrcType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 30, 4),
    _XconSrcType_Type()
)
xconSrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconSrcType.setStatus("current")


class _XconSrcIndex_Type(Integer32):
    """Custom type xconSrcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XconSrcIndex_Type.__name__ = "Integer32"
_XconSrcIndex_Object = MibScalar
xconSrcIndex = _XconSrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 30, 5),
    _XconSrcIndex_Type()
)
xconSrcIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconSrcIndex.setStatus("current")
_XconDirection_Type = XconDir
_XconDirection_Object = MibScalar
xconDirection = _XconDirection_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 30, 6),
    _XconDirection_Type()
)
xconDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconDirection.setStatus("current")
_XconName_Type = DisplayString
_XconName_Object = MibScalar
xconName = _XconName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 30, 7),
    _XconName_Type()
)
xconName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconName.setStatus("current")
_XconAction_Type = ActionType
_XconAction_Object = MibScalar
xconAction = _XconAction_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 30, 8),
    _XconAction_Type()
)
xconAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconAction.setStatus("current")
_XconProceed_Type = SagemBoolean
_XconProceed_Object = MibScalar
xconProceed = _XconProceed_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 30, 20),
    _XconProceed_Type()
)
xconProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconProceed.setStatus("current")
_XconDiagnostic_Type = DisplayString
_XconDiagnostic_Object = MibScalar
xconDiagnostic = _XconDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 1038, 108, 30, 21),
    _XconDiagnostic_Type()
)
xconDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xconDiagnostic.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XCONNECTION-MIB",
    **{"TrafficStatus": TrafficStatus,
       "ProtectionType": ProtectionType,
       "ProtectionStatus": ProtectionStatus,
       "LinkDirection": LinkDirection,
       "CTPType": CTPType,
       "XconDir": XconDir,
       "ActionType": ActionType,
       "xconnection": xconnection,
       "link": link,
       "linkNumber": linkNumber,
       "linkTable": linkTable,
       "linkEntry": linkEntry,
       "linkIndex": linkIndex,
       "linkSinkType": linkSinkType,
       "linkSrcType": linkSrcType,
       "linkCTPSink": linkCTPSink,
       "linkCTPSource": linkCTPSource,
       "linkName": linkName,
       "linkGroupId": linkGroupId,
       "linkDirection": linkDirection,
       "linkProtectionType": linkProtectionType,
       "linkProtectionStatus": linkProtectionStatus,
       "linkTrafficStatus": linkTrafficStatus,
       "linkImplementation": linkImplementation,
       "xcon": xcon,
       "xconNumber": xconNumber,
       "xconSinkType": xconSinkType,
       "xconSinkIndex": xconSinkIndex,
       "xconSrcType": xconSrcType,
       "xconSrcIndex": xconSrcIndex,
       "xconDirection": xconDirection,
       "xconName": xconName,
       "xconAction": xconAction,
       "xconProceed": xconProceed,
       "xconDiagnostic": xconDiagnostic}
)
