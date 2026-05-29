# SNMP MIB module (HH3C-3GMODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-3GMODEM-MIB

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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3c3GModem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98)
)
if mibBuilder.loadTexts:
    hh3c3GModem.setRevisions(
        ("2015-12-01 12:00",
         "2014-09-09 12:00",
         "2009-04-30 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cUIMStatusType(TextualConvention, Integer32):
    status = "current"
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
        *(("absent", 1),
          ("initial", 2),
          ("fault", 3),
          ("unprotected", 4),
          ("protected", 5),
          ("pinLocked", 6),
          ("pukLocked", 7),
          ("selfDestruct", 8))
    )



class Hh3cSmsEncodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("ucs2", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3c3GModemObjects_ObjectIdentity = ObjectIdentity
hh3c3GModemObjects = _Hh3c3GModemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1)
)
_Hh3cWirelessCard_ObjectIdentity = ObjectIdentity
hh3cWirelessCard = _Hh3cWirelessCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1)
)
_Hh3cWirelessCardTable_Object = MibTable
hh3cWirelessCardTable = _Hh3cWirelessCardTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cWirelessCardTable.setStatus("current")
_Hh3cWirelessCardEntry_Object = MibTableRow
hh3cWirelessCardEntry = _Hh3cWirelessCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1)
)
hh3cWirelessCardEntry.setIndexNames(
    (0, "HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    hh3cWirelessCardEntry.setStatus("current")


class _Hh3cWirelessCardIndex_Type(Integer32):
    """Custom type hh3cWirelessCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cWirelessCardIndex_Type.__name__ = "Integer32"
_Hh3cWirelessCardIndex_Object = MibTableColumn
hh3cWirelessCardIndex = _Hh3cWirelessCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 1),
    _Hh3cWirelessCardIndex_Type()
)
hh3cWirelessCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardIndex.setStatus("current")


class _Hh3cWirelessCardModelName_Type(SnmpAdminString):
    """Custom type hh3cWirelessCardModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cWirelessCardModelName_Type.__name__ = "SnmpAdminString"
_Hh3cWirelessCardModelName_Object = MibTableColumn
hh3cWirelessCardModelName = _Hh3cWirelessCardModelName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 2),
    _Hh3cWirelessCardModelName_Type()
)
hh3cWirelessCardModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardModelName.setStatus("current")


class _Hh3cWirelessCardMfgName_Type(SnmpAdminString):
    """Custom type hh3cWirelessCardMfgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cWirelessCardMfgName_Type.__name__ = "SnmpAdminString"
_Hh3cWirelessCardMfgName_Object = MibTableColumn
hh3cWirelessCardMfgName = _Hh3cWirelessCardMfgName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 3),
    _Hh3cWirelessCardMfgName_Type()
)
hh3cWirelessCardMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardMfgName.setStatus("current")


class _Hh3cWirelessCardDescription_Type(SnmpAdminString):
    """Custom type hh3cWirelessCardDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cWirelessCardDescription_Type.__name__ = "SnmpAdminString"
_Hh3cWirelessCardDescription_Object = MibTableColumn
hh3cWirelessCardDescription = _Hh3cWirelessCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 4),
    _Hh3cWirelessCardDescription_Type()
)
hh3cWirelessCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardDescription.setStatus("current")


class _Hh3cWirelessCardSerialNumber_Type(SnmpAdminString):
    """Custom type hh3cWirelessCardSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cWirelessCardSerialNumber_Type.__name__ = "SnmpAdminString"
_Hh3cWirelessCardSerialNumber_Object = MibTableColumn
hh3cWirelessCardSerialNumber = _Hh3cWirelessCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 5),
    _Hh3cWirelessCardSerialNumber_Type()
)
hh3cWirelessCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardSerialNumber.setStatus("current")


class _Hh3cWirelessCardCMIIID_Type(SnmpAdminString):
    """Custom type hh3cWirelessCardCMIIID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cWirelessCardCMIIID_Type.__name__ = "SnmpAdminString"
_Hh3cWirelessCardCMIIID_Object = MibTableColumn
hh3cWirelessCardCMIIID = _Hh3cWirelessCardCMIIID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 6),
    _Hh3cWirelessCardCMIIID_Type()
)
hh3cWirelessCardCMIIID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardCMIIID.setStatus("current")


class _Hh3cWirelessCardHardwareVersion_Type(SnmpAdminString):
    """Custom type hh3cWirelessCardHardwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cWirelessCardHardwareVersion_Type.__name__ = "SnmpAdminString"
_Hh3cWirelessCardHardwareVersion_Object = MibTableColumn
hh3cWirelessCardHardwareVersion = _Hh3cWirelessCardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 7),
    _Hh3cWirelessCardHardwareVersion_Type()
)
hh3cWirelessCardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardHardwareVersion.setStatus("current")


class _Hh3cWirelessCardFirmwareVersion_Type(SnmpAdminString):
    """Custom type hh3cWirelessCardFirmwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cWirelessCardFirmwareVersion_Type.__name__ = "SnmpAdminString"
_Hh3cWirelessCardFirmwareVersion_Object = MibTableColumn
hh3cWirelessCardFirmwareVersion = _Hh3cWirelessCardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 8),
    _Hh3cWirelessCardFirmwareVersion_Type()
)
hh3cWirelessCardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardFirmwareVersion.setStatus("current")


class _Hh3cWirelessCardPRLVersion_Type(SnmpAdminString):
    """Custom type hh3cWirelessCardPRLVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cWirelessCardPRLVersion_Type.__name__ = "SnmpAdminString"
_Hh3cWirelessCardPRLVersion_Object = MibTableColumn
hh3cWirelessCardPRLVersion = _Hh3cWirelessCardPRLVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 9),
    _Hh3cWirelessCardPRLVersion_Type()
)
hh3cWirelessCardPRLVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardPRLVersion.setStatus("current")
_Hh3cWirelessCardInterfaceIndex_Type = InterfaceIndex
_Hh3cWirelessCardInterfaceIndex_Object = MibTableColumn
hh3cWirelessCardInterfaceIndex = _Hh3cWirelessCardInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 10),
    _Hh3cWirelessCardInterfaceIndex_Type()
)
hh3cWirelessCardInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardInterfaceIndex.setStatus("current")


class _Hh3cWirelessCardModemStatus_Type(Integer32):
    """Custom type hh3cWirelessCardModemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("onLine", 2),
          ("offLine", 3))
    )


_Hh3cWirelessCardModemStatus_Type.__name__ = "Integer32"
_Hh3cWirelessCardModemStatus_Object = MibTableColumn
hh3cWirelessCardModemStatus = _Hh3cWirelessCardModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 11),
    _Hh3cWirelessCardModemStatus_Type()
)
hh3cWirelessCardModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardModemStatus.setStatus("current")


class _Hh3cWirelessCardModemMode_Type(Integer32):
    """Custom type hh3cWirelessCardModemMode based on Integer32"""
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
        *(("unknown", 1),
          ("tdscdma", 2),
          ("wcdma", 3),
          ("cdma", 4),
          ("lte", 5))
    )


_Hh3cWirelessCardModemMode_Type.__name__ = "Integer32"
_Hh3cWirelessCardModemMode_Object = MibTableColumn
hh3cWirelessCardModemMode = _Hh3cWirelessCardModemMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 12),
    _Hh3cWirelessCardModemMode_Type()
)
hh3cWirelessCardModemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardModemMode.setStatus("current")


class _Hh3cWirelessCardCurNetConn_Type(Integer32):
    """Custom type hh3cWirelessCardCurNetConn based on Integer32"""
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
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("noService", 2),
          ("gsm", 3),
          ("gprs", 4),
          ("edge", 5),
          ("hsdpa", 6),
          ("hsupa", 7),
          ("hsupaAndhsdpa", 8),
          ("hspaPlus", 9),
          ("umts", 10),
          ("dchspaPlus", 11),
          ("lte", 12),
          ("onexrtt", 13),
          ("evdo", 14),
          ("onexrttAndevdo", 15),
          ("tdscdma", 16))
    )


_Hh3cWirelessCardCurNetConn_Type.__name__ = "Integer32"
_Hh3cWirelessCardCurNetConn_Object = MibTableColumn
hh3cWirelessCardCurNetConn = _Hh3cWirelessCardCurNetConn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 1, 1, 13),
    _Hh3cWirelessCardCurNetConn_Type()
)
hh3cWirelessCardCurNetConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardCurNetConn.setStatus("current")
_Hh3cSmsGroup_ObjectIdentity = ObjectIdentity
hh3cSmsGroup = _Hh3cSmsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 2)
)
_Hh3cSmsScalarObjects_ObjectIdentity = ObjectIdentity
hh3cSmsScalarObjects = _Hh3cSmsScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 2, 1)
)
_Hh3cSmsRxNotifSwitch_Type = TruthValue
_Hh3cSmsRxNotifSwitch_Object = MibScalar
hh3cSmsRxNotifSwitch = _Hh3cSmsRxNotifSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 2, 1, 1),
    _Hh3cSmsRxNotifSwitch_Type()
)
hh3cSmsRxNotifSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSmsRxNotifSwitch.setStatus("current")
_Hh3cSmsOperationTable_Object = MibTable
hh3cSmsOperationTable = _Hh3cSmsOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cSmsOperationTable.setStatus("current")
_Hh3cSmsOperationEntry_Object = MibTableRow
hh3cSmsOperationEntry = _Hh3cSmsOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 2, 2, 1)
)
hh3cSmsOperationEntry.setIndexNames(
    (0, "HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    hh3cSmsOperationEntry.setStatus("current")


class _Hh3cSmsDestNumber_Type(SnmpAdminString):
    """Custom type hh3cSmsDestNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Hh3cSmsDestNumber_Type.__name__ = "SnmpAdminString"
_Hh3cSmsDestNumber_Object = MibTableColumn
hh3cSmsDestNumber = _Hh3cSmsDestNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 2, 2, 1, 1),
    _Hh3cSmsDestNumber_Type()
)
hh3cSmsDestNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSmsDestNumber.setStatus("current")


class _Hh3cSmsEncode_Type(Hh3cSmsEncodeType):
    """Custom type hh3cSmsEncode based on Hh3cSmsEncodeType"""
    defaultValue = 1


_Hh3cSmsEncode_Type.__name__ = "Hh3cSmsEncodeType"
_Hh3cSmsEncode_Object = MibTableColumn
hh3cSmsEncode = _Hh3cSmsEncode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 2, 2, 1, 2),
    _Hh3cSmsEncode_Type()
)
hh3cSmsEncode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSmsEncode.setStatus("current")


class _Hh3cSmsContent_Type(OctetString):
    """Custom type hh3cSmsContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSmsContent_Type.__name__ = "OctetString"
_Hh3cSmsContent_Object = MibTableColumn
hh3cSmsContent = _Hh3cSmsContent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 2, 2, 1, 3),
    _Hh3cSmsContent_Type()
)
hh3cSmsContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSmsContent.setStatus("current")


class _Hh3cSmsSendStatus_Type(Integer32):
    """Custom type hh3cSmsSendStatus based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("set2Send", 1),
          ("ready2Send", 2),
          ("sending", 3),
          ("sentAlready", 4),
          ("telnumberInvalid", 5),
          ("paramInvalid", 6),
          ("contentTooLong", 7),
          ("codeError", 8),
          ("unknown", 9),
          ("busy", 10),
          ("notPresent", 11),
          ("notSupport", 12),
          ("initializing", 13),
          ("noCenterNum", 14),
          ("noSim", 15),
          ("simNotReady", 16),
          ("sendAtFailed", 17),
          ("sendDisable", 18))
    )


_Hh3cSmsSendStatus_Type.__name__ = "Integer32"
_Hh3cSmsSendStatus_Object = MibTableColumn
hh3cSmsSendStatus = _Hh3cSmsSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 2, 2, 1, 4),
    _Hh3cSmsSendStatus_Type()
)
hh3cSmsSendStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSmsSendStatus.setStatus("current")
_Hh3cWirelessCardOnlineTable_Object = MibTable
hh3cWirelessCardOnlineTable = _Hh3cWirelessCardOnlineTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cWirelessCardOnlineTable.setStatus("current")
_Hh3cWirelessCardOnlineEntry_Object = MibTableRow
hh3cWirelessCardOnlineEntry = _Hh3cWirelessCardOnlineEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 3, 1)
)
hh3cWirelessCardOnlineEntry.setIndexNames(
    (0, "HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
    (0, "HH3C-3GMODEM-MIB", "hh3cWirelessCardOnlineTime"),
)
if mibBuilder.loadTexts:
    hh3cWirelessCardOnlineEntry.setStatus("current")
_Hh3cWirelessCardOnlineTime_Type = Unsigned32
_Hh3cWirelessCardOnlineTime_Object = MibTableColumn
hh3cWirelessCardOnlineTime = _Hh3cWirelessCardOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 3, 1, 1),
    _Hh3cWirelessCardOnlineTime_Type()
)
hh3cWirelessCardOnlineTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWirelessCardOnlineTime.setStatus("current")


class _Hh3cWirelessCardOnlineType_Type(Integer32):
    """Custom type hh3cWirelessCardOnlineType based on Integer32"""
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


_Hh3cWirelessCardOnlineType_Type.__name__ = "Integer32"
_Hh3cWirelessCardOnlineType_Object = MibTableColumn
hh3cWirelessCardOnlineType = _Hh3cWirelessCardOnlineType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 1, 3, 1, 2),
    _Hh3cWirelessCardOnlineType_Type()
)
hh3cWirelessCardOnlineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWirelessCardOnlineType.setStatus("current")
_Hh3cUIM_ObjectIdentity = ObjectIdentity
hh3cUIM = _Hh3cUIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2)
)
_Hh3cUIMInfoTable_Object = MibTable
hh3cUIMInfoTable = _Hh3cUIMInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cUIMInfoTable.setStatus("current")
_Hh3cUIMInfoEntry_Object = MibTableRow
hh3cUIMInfoEntry = _Hh3cUIMInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1)
)
hh3cUIMInfoEntry.setIndexNames(
    (0, "HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
    (0, "HH3C-3GMODEM-MIB", "hh3cUIMIndex"),
)
if mibBuilder.loadTexts:
    hh3cUIMInfoEntry.setStatus("current")


class _Hh3cUIMIndex_Type(Integer32):
    """Custom type hh3cUIMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cUIMIndex_Type.__name__ = "Integer32"
_Hh3cUIMIndex_Object = MibTableColumn
hh3cUIMIndex = _Hh3cUIMIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 1),
    _Hh3cUIMIndex_Type()
)
hh3cUIMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cUIMIndex.setStatus("current")
_Hh3cUIMStatus_Type = Hh3cUIMStatusType
_Hh3cUIMStatus_Object = MibTableColumn
hh3cUIMStatus = _Hh3cUIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 2),
    _Hh3cUIMStatus_Type()
)
hh3cUIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUIMStatus.setStatus("current")


class _Hh3cUIMImsi_Type(SnmpAdminString):
    """Custom type hh3cUIMImsi based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cUIMImsi_Type.__name__ = "SnmpAdminString"
_Hh3cUIMImsi_Object = MibTableColumn
hh3cUIMImsi = _Hh3cUIMImsi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 3),
    _Hh3cUIMImsi_Type()
)
hh3cUIMImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUIMImsi.setStatus("current")


class _Hh3cUIMPin_Type(SnmpAdminString):
    """Custom type hh3cUIMPin based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_Hh3cUIMPin_Type.__name__ = "SnmpAdminString"
_Hh3cUIMPin_Object = MibTableColumn
hh3cUIMPin = _Hh3cUIMPin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 4),
    _Hh3cUIMPin_Type()
)
hh3cUIMPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUIMPin.setStatus("current")


class _Hh3cUIMVoltage_Type(Unsigned32):
    """Custom type hh3cUIMVoltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cUIMVoltage_Type.__name__ = "Unsigned32"
_Hh3cUIMVoltage_Object = MibTableColumn
hh3cUIMVoltage = _Hh3cUIMVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 5),
    _Hh3cUIMVoltage_Type()
)
hh3cUIMVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUIMVoltage.setStatus("current")
if mibBuilder.loadTexts:
    hh3cUIMVoltage.setUnits("milli-volt")


class _Hh3cUIMProvider_Type(SnmpAdminString):
    """Custom type hh3cUIMProvider based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cUIMProvider_Type.__name__ = "SnmpAdminString"
_Hh3cUIMProvider_Object = MibTableColumn
hh3cUIMProvider = _Hh3cUIMProvider_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 6),
    _Hh3cUIMProvider_Type()
)
hh3cUIMProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUIMProvider.setStatus("current")


class _Hh3cUIMSignal_Type(Integer32):
    """Custom type hh3cUIMSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
        ValueRangeConstraint(99, 99),
    )


_Hh3cUIMSignal_Type.__name__ = "Integer32"
_Hh3cUIMSignal_Object = MibTableColumn
hh3cUIMSignal = _Hh3cUIMSignal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 7),
    _Hh3cUIMSignal_Type()
)
hh3cUIMSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUIMSignal.setStatus("current")


class _Hh3cUIMTryPinPukTimes_Type(Unsigned32):
    """Custom type hh3cUIMTryPinPukTimes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cUIMTryPinPukTimes_Type.__name__ = "Unsigned32"
_Hh3cUIMTryPinPukTimes_Object = MibTableColumn
hh3cUIMTryPinPukTimes = _Hh3cUIMTryPinPukTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 8),
    _Hh3cUIMTryPinPukTimes_Type()
)
hh3cUIMTryPinPukTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUIMTryPinPukTimes.setStatus("current")


class _Hh3cUIMOldPin_Type(SnmpAdminString):
    """Custom type hh3cUIMOldPin based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_Hh3cUIMOldPin_Type.__name__ = "SnmpAdminString"
_Hh3cUIMOldPin_Object = MibTableColumn
hh3cUIMOldPin = _Hh3cUIMOldPin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 2, 1, 1, 9),
    _Hh3cUIMOldPin_Type()
)
hh3cUIMOldPin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cUIMOldPin.setStatus("current")
_Hh3c3GCdma_ObjectIdentity = ObjectIdentity
hh3c3GCdma = _Hh3c3GCdma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3)
)
_Hh3c3GCdma1xRttTable_Object = MibTable
hh3c3GCdma1xRttTable = _Hh3c3GCdma1xRttTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3c3GCdma1xRttTable.setStatus("current")
_Hh3c3GCdma1xRttEntry_Object = MibTableRow
hh3c3GCdma1xRttEntry = _Hh3c3GCdma1xRttEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 1, 1)
)
hh3c3GCdma1xRttEntry.setIndexNames(
    (0, "HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    hh3c3GCdma1xRttEntry.setStatus("current")


class _Hh3c3GCdma1xRttCurrentRssi_Type(Integer32):
    """Custom type hh3c3GCdma1xRttCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_Hh3c3GCdma1xRttCurrentRssi_Type.__name__ = "Integer32"
_Hh3c3GCdma1xRttCurrentRssi_Object = MibTableColumn
hh3c3GCdma1xRttCurrentRssi = _Hh3c3GCdma1xRttCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 1, 1, 1),
    _Hh3c3GCdma1xRttCurrentRssi_Type()
)
hh3c3GCdma1xRttCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GCdma1xRttCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    hh3c3GCdma1xRttCurrentRssi.setUnits("dBm")


class _Hh3c3GCdma1xRttRssiMediumThreshold_Type(Integer32):
    """Custom type hh3c3GCdma1xRttRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Hh3c3GCdma1xRttRssiMediumThreshold_Type.__name__ = "Integer32"
_Hh3c3GCdma1xRttRssiMediumThreshold_Object = MibTableColumn
hh3c3GCdma1xRttRssiMediumThreshold = _Hh3c3GCdma1xRttRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 1, 1, 2),
    _Hh3c3GCdma1xRttRssiMediumThreshold_Type()
)
hh3c3GCdma1xRttRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c3GCdma1xRttRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3c3GCdma1xRttRssiMediumThreshold.setUnits("dBm")


class _Hh3c3GCdma1xRttRssiWeakThreshold_Type(Integer32):
    """Custom type hh3c3GCdma1xRttRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Hh3c3GCdma1xRttRssiWeakThreshold_Type.__name__ = "Integer32"
_Hh3c3GCdma1xRttRssiWeakThreshold_Object = MibTableColumn
hh3c3GCdma1xRttRssiWeakThreshold = _Hh3c3GCdma1xRttRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 1, 1, 3),
    _Hh3c3GCdma1xRttRssiWeakThreshold_Type()
)
hh3c3GCdma1xRttRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c3GCdma1xRttRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3c3GCdma1xRttRssiWeakThreshold.setUnits("dBm")


class _Hh3c3GCdma1xRttCurServiceStatus_Type(Integer32):
    """Custom type hh3c3GCdma1xRttCurServiceStatus based on Integer32"""
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
        *(("unknown", 1),
          ("available", 2),
          ("emergency", 3),
          ("lowPower", 4),
          ("noService", 5))
    )


_Hh3c3GCdma1xRttCurServiceStatus_Type.__name__ = "Integer32"
_Hh3c3GCdma1xRttCurServiceStatus_Object = MibTableColumn
hh3c3GCdma1xRttCurServiceStatus = _Hh3c3GCdma1xRttCurServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 1, 1, 4),
    _Hh3c3GCdma1xRttCurServiceStatus_Type()
)
hh3c3GCdma1xRttCurServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GCdma1xRttCurServiceStatus.setStatus("current")


class _Hh3c3GCdma1xRttCurRoamingStatus_Type(Integer32):
    """Custom type hh3c3GCdma1xRttCurRoamingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("roaming", 2),
          ("home", 3))
    )


_Hh3c3GCdma1xRttCurRoamingStatus_Type.__name__ = "Integer32"
_Hh3c3GCdma1xRttCurRoamingStatus_Object = MibTableColumn
hh3c3GCdma1xRttCurRoamingStatus = _Hh3c3GCdma1xRttCurRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 1, 1, 5),
    _Hh3c3GCdma1xRttCurRoamingStatus_Type()
)
hh3c3GCdma1xRttCurRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GCdma1xRttCurRoamingStatus.setStatus("current")


class _Hh3c3GCdma1xRttBID_Type(Unsigned32):
    """Custom type hh3c3GCdma1xRttBID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3c3GCdma1xRttBID_Type.__name__ = "Unsigned32"
_Hh3c3GCdma1xRttBID_Object = MibTableColumn
hh3c3GCdma1xRttBID = _Hh3c3GCdma1xRttBID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 1, 1, 6),
    _Hh3c3GCdma1xRttBID_Type()
)
hh3c3GCdma1xRttBID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GCdma1xRttBID.setStatus("current")


class _Hh3c3GCdma1xRttSID_Type(Unsigned32):
    """Custom type hh3c3GCdma1xRttSID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3c3GCdma1xRttSID_Type.__name__ = "Unsigned32"
_Hh3c3GCdma1xRttSID_Object = MibTableColumn
hh3c3GCdma1xRttSID = _Hh3c3GCdma1xRttSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 1, 1, 7),
    _Hh3c3GCdma1xRttSID_Type()
)
hh3c3GCdma1xRttSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GCdma1xRttSID.setStatus("current")


class _Hh3c3GCdma1xRttNID_Type(Unsigned32):
    """Custom type hh3c3GCdma1xRttNID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3c3GCdma1xRttNID_Type.__name__ = "Unsigned32"
_Hh3c3GCdma1xRttNID_Object = MibTableColumn
hh3c3GCdma1xRttNID = _Hh3c3GCdma1xRttNID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 1, 1, 8),
    _Hh3c3GCdma1xRttNID_Type()
)
hh3c3GCdma1xRttNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GCdma1xRttNID.setStatus("current")
_Hh3c3GCdmaEvDoTable_Object = MibTable
hh3c3GCdmaEvDoTable = _Hh3c3GCdmaEvDoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hh3c3GCdmaEvDoTable.setStatus("current")
_Hh3c3GCdmaEvDoEntry_Object = MibTableRow
hh3c3GCdmaEvDoEntry = _Hh3c3GCdmaEvDoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 2, 1)
)
hh3c3GCdmaEvDoEntry.setIndexNames(
    (0, "HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    hh3c3GCdmaEvDoEntry.setStatus("current")


class _Hh3c3GCdmaEvDoCurrentRssi_Type(Integer32):
    """Custom type hh3c3GCdmaEvDoCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_Hh3c3GCdmaEvDoCurrentRssi_Type.__name__ = "Integer32"
_Hh3c3GCdmaEvDoCurrentRssi_Object = MibTableColumn
hh3c3GCdmaEvDoCurrentRssi = _Hh3c3GCdmaEvDoCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 2, 1, 1),
    _Hh3c3GCdmaEvDoCurrentRssi_Type()
)
hh3c3GCdmaEvDoCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GCdmaEvDoCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    hh3c3GCdmaEvDoCurrentRssi.setUnits("dBm")


class _Hh3c3GCdmaEvDoRssiMediumThreshold_Type(Integer32):
    """Custom type hh3c3GCdmaEvDoRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Hh3c3GCdmaEvDoRssiMediumThreshold_Type.__name__ = "Integer32"
_Hh3c3GCdmaEvDoRssiMediumThreshold_Object = MibTableColumn
hh3c3GCdmaEvDoRssiMediumThreshold = _Hh3c3GCdmaEvDoRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 2, 1, 2),
    _Hh3c3GCdmaEvDoRssiMediumThreshold_Type()
)
hh3c3GCdmaEvDoRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c3GCdmaEvDoRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3c3GCdmaEvDoRssiMediumThreshold.setUnits("dBm")


class _Hh3c3GCdmaEvDoRssiWeakThreshold_Type(Integer32):
    """Custom type hh3c3GCdmaEvDoRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Hh3c3GCdmaEvDoRssiWeakThreshold_Type.__name__ = "Integer32"
_Hh3c3GCdmaEvDoRssiWeakThreshold_Object = MibTableColumn
hh3c3GCdmaEvDoRssiWeakThreshold = _Hh3c3GCdmaEvDoRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 2, 1, 3),
    _Hh3c3GCdmaEvDoRssiWeakThreshold_Type()
)
hh3c3GCdmaEvDoRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c3GCdmaEvDoRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3c3GCdmaEvDoRssiWeakThreshold.setUnits("dBm")


class _Hh3c3GCdmaEvDoCurServiceStatus_Type(Integer32):
    """Custom type hh3c3GCdmaEvDoCurServiceStatus based on Integer32"""
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
        *(("unknown", 1),
          ("available", 2),
          ("emergency", 3),
          ("lowPower", 4),
          ("noService", 5))
    )


_Hh3c3GCdmaEvDoCurServiceStatus_Type.__name__ = "Integer32"
_Hh3c3GCdmaEvDoCurServiceStatus_Object = MibTableColumn
hh3c3GCdmaEvDoCurServiceStatus = _Hh3c3GCdmaEvDoCurServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 2, 1, 4),
    _Hh3c3GCdmaEvDoCurServiceStatus_Type()
)
hh3c3GCdmaEvDoCurServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GCdmaEvDoCurServiceStatus.setStatus("current")


class _Hh3c3GCdmaEvDoCurRoamingStatus_Type(Integer32):
    """Custom type hh3c3GCdmaEvDoCurRoamingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("roaming", 2),
          ("home", 3))
    )


_Hh3c3GCdmaEvDoCurRoamingStatus_Type.__name__ = "Integer32"
_Hh3c3GCdmaEvDoCurRoamingStatus_Object = MibTableColumn
hh3c3GCdmaEvDoCurRoamingStatus = _Hh3c3GCdmaEvDoCurRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 2, 1, 5),
    _Hh3c3GCdmaEvDoCurRoamingStatus_Type()
)
hh3c3GCdmaEvDoCurRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GCdmaEvDoCurRoamingStatus.setStatus("current")


class _Hh3c3GCdmaEvDoSubNetID_Type(SnmpAdminString):
    """Custom type hh3c3GCdmaEvDoSubNetID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3c3GCdmaEvDoSubNetID_Type.__name__ = "SnmpAdminString"
_Hh3c3GCdmaEvDoSubNetID_Object = MibTableColumn
hh3c3GCdmaEvDoSubNetID = _Hh3c3GCdmaEvDoSubNetID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 3, 2, 1, 6),
    _Hh3c3GCdmaEvDoSubNetID_Type()
)
hh3c3GCdmaEvDoSubNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GCdmaEvDoSubNetID.setStatus("current")
_Hh3c3GGsm_ObjectIdentity = ObjectIdentity
hh3c3GGsm = _Hh3c3GGsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4)
)
_Hh3c3GGsmInfoTable_Object = MibTable
hh3c3GGsmInfoTable = _Hh3c3GGsmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hh3c3GGsmInfoTable.setStatus("current")
_Hh3c3GGsmInfoEntry_Object = MibTableRow
hh3c3GGsmInfoEntry = _Hh3c3GGsmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1)
)
hh3c3GGsmInfoEntry.setIndexNames(
    (0, "HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    hh3c3GGsmInfoEntry.setStatus("current")


class _Hh3c3GGsmCurrentRssi_Type(Integer32):
    """Custom type hh3c3GGsmCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_Hh3c3GGsmCurrentRssi_Type.__name__ = "Integer32"
_Hh3c3GGsmCurrentRssi_Object = MibTableColumn
hh3c3GGsmCurrentRssi = _Hh3c3GGsmCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 1),
    _Hh3c3GGsmCurrentRssi_Type()
)
hh3c3GGsmCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GGsmCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    hh3c3GGsmCurrentRssi.setUnits("dBm")


class _Hh3c3GGsmRssiMediumThreshold_Type(Integer32):
    """Custom type hh3c3GGsmRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Hh3c3GGsmRssiMediumThreshold_Type.__name__ = "Integer32"
_Hh3c3GGsmRssiMediumThreshold_Object = MibTableColumn
hh3c3GGsmRssiMediumThreshold = _Hh3c3GGsmRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 2),
    _Hh3c3GGsmRssiMediumThreshold_Type()
)
hh3c3GGsmRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c3GGsmRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3c3GGsmRssiMediumThreshold.setUnits("dBm")


class _Hh3c3GGsmRssiWeakThreshold_Type(Integer32):
    """Custom type hh3c3GGsmRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Hh3c3GGsmRssiWeakThreshold_Type.__name__ = "Integer32"
_Hh3c3GGsmRssiWeakThreshold_Object = MibTableColumn
hh3c3GGsmRssiWeakThreshold = _Hh3c3GGsmRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 3),
    _Hh3c3GGsmRssiWeakThreshold_Type()
)
hh3c3GGsmRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c3GGsmRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3c3GGsmRssiWeakThreshold.setUnits("dBm")


class _Hh3c3GGsmImsi_Type(SnmpAdminString):
    """Custom type hh3c3GGsmImsi based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3c3GGsmImsi_Type.__name__ = "SnmpAdminString"
_Hh3c3GGsmImsi_Object = MibTableColumn
hh3c3GGsmImsi = _Hh3c3GGsmImsi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 4),
    _Hh3c3GGsmImsi_Type()
)
hh3c3GGsmImsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GGsmImsi.setStatus("current")


class _Hh3c3GGsmImei_Type(SnmpAdminString):
    """Custom type hh3c3GGsmImei based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3c3GGsmImei_Type.__name__ = "SnmpAdminString"
_Hh3c3GGsmImei_Object = MibTableColumn
hh3c3GGsmImei = _Hh3c3GGsmImei_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 5),
    _Hh3c3GGsmImei_Type()
)
hh3c3GGsmImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GGsmImei.setStatus("current")


class _Hh3c3GGsmApn_Type(SnmpAdminString):
    """Custom type hh3c3GGsmApn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_Hh3c3GGsmApn_Type.__name__ = "SnmpAdminString"
_Hh3c3GGsmApn_Object = MibTableColumn
hh3c3GGsmApn = _Hh3c3GGsmApn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 6),
    _Hh3c3GGsmApn_Type()
)
hh3c3GGsmApn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3c3GGsmApn.setStatus("current")


class _Hh3c3GGsmPacketSessionStatus_Type(Integer32):
    """Custom type hh3c3GGsmPacketSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("active", 2),
          ("inactive", 3))
    )


_Hh3c3GGsmPacketSessionStatus_Type.__name__ = "Integer32"
_Hh3c3GGsmPacketSessionStatus_Object = MibTableColumn
hh3c3GGsmPacketSessionStatus = _Hh3c3GGsmPacketSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 7),
    _Hh3c3GGsmPacketSessionStatus_Type()
)
hh3c3GGsmPacketSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GGsmPacketSessionStatus.setStatus("current")


class _Hh3c3GGsmNetworkSelectionMode_Type(Integer32):
    """Custom type hh3c3GGsmNetworkSelectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("automatic", 2),
          ("manual", 3))
    )


_Hh3c3GGsmNetworkSelectionMode_Type.__name__ = "Integer32"
_Hh3c3GGsmNetworkSelectionMode_Object = MibTableColumn
hh3c3GGsmNetworkSelectionMode = _Hh3c3GGsmNetworkSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 8),
    _Hh3c3GGsmNetworkSelectionMode_Type()
)
hh3c3GGsmNetworkSelectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GGsmNetworkSelectionMode.setStatus("current")


class _Hh3c3GGsmMobileNetworkName_Type(SnmpAdminString):
    """Custom type hh3c3GGsmMobileNetworkName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3c3GGsmMobileNetworkName_Type.__name__ = "SnmpAdminString"
_Hh3c3GGsmMobileNetworkName_Object = MibTableColumn
hh3c3GGsmMobileNetworkName = _Hh3c3GGsmMobileNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 9),
    _Hh3c3GGsmMobileNetworkName_Type()
)
hh3c3GGsmMobileNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GGsmMobileNetworkName.setStatus("current")


class _Hh3c3GGsmLac_Type(SnmpAdminString):
    """Custom type hh3c3GGsmLac based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3c3GGsmLac_Type.__name__ = "SnmpAdminString"
_Hh3c3GGsmLac_Object = MibTableColumn
hh3c3GGsmLac = _Hh3c3GGsmLac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 10),
    _Hh3c3GGsmLac_Type()
)
hh3c3GGsmLac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GGsmLac.setStatus("current")


class _Hh3c3GGsmCellId_Type(SnmpAdminString):
    """Custom type hh3c3GGsmCellId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3c3GGsmCellId_Type.__name__ = "SnmpAdminString"
_Hh3c3GGsmCellId_Object = MibTableColumn
hh3c3GGsmCellId = _Hh3c3GGsmCellId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 11),
    _Hh3c3GGsmCellId_Type()
)
hh3c3GGsmCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GGsmCellId.setStatus("current")


class _Hh3c3GGsmSimStatus_Type(Integer32):
    """Custom type hh3c3GGsmSimStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("notInsert", 3),
          ("networkReject", 4),
          ("blocked", 5))
    )


_Hh3c3GGsmSimStatus_Type.__name__ = "Integer32"
_Hh3c3GGsmSimStatus_Object = MibTableColumn
hh3c3GGsmSimStatus = _Hh3c3GGsmSimStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 12),
    _Hh3c3GGsmSimStatus_Type()
)
hh3c3GGsmSimStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GGsmSimStatus.setStatus("current")


class _Hh3c3GGsmCurServiceStatus_Type(Integer32):
    """Custom type hh3c3GGsmCurServiceStatus based on Integer32"""
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
        *(("unknown", 1),
          ("available", 2),
          ("emergency", 3),
          ("lowPower", 4),
          ("noService", 5))
    )


_Hh3c3GGsmCurServiceStatus_Type.__name__ = "Integer32"
_Hh3c3GGsmCurServiceStatus_Object = MibTableColumn
hh3c3GGsmCurServiceStatus = _Hh3c3GGsmCurServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 13),
    _Hh3c3GGsmCurServiceStatus_Type()
)
hh3c3GGsmCurServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GGsmCurServiceStatus.setStatus("current")


class _Hh3c3GGsmCurRoamingStatus_Type(Integer32):
    """Custom type hh3c3GGsmCurRoamingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("roaming", 2),
          ("home", 3))
    )


_Hh3c3GGsmCurRoamingStatus_Type.__name__ = "Integer32"
_Hh3c3GGsmCurRoamingStatus_Object = MibTableColumn
hh3c3GGsmCurRoamingStatus = _Hh3c3GGsmCurRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 14),
    _Hh3c3GGsmCurRoamingStatus_Type()
)
hh3c3GGsmCurRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GGsmCurRoamingStatus.setStatus("current")


class _Hh3c3GGsmMcc_Type(SnmpAdminString):
    """Custom type hh3c3GGsmMcc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3c3GGsmMcc_Type.__name__ = "SnmpAdminString"
_Hh3c3GGsmMcc_Object = MibTableColumn
hh3c3GGsmMcc = _Hh3c3GGsmMcc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 15),
    _Hh3c3GGsmMcc_Type()
)
hh3c3GGsmMcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GGsmMcc.setStatus("current")


class _Hh3c3GGsmMnc_Type(SnmpAdminString):
    """Custom type hh3c3GGsmMnc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3c3GGsmMnc_Type.__name__ = "SnmpAdminString"
_Hh3c3GGsmMnc_Object = MibTableColumn
hh3c3GGsmMnc = _Hh3c3GGsmMnc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 4, 1, 1, 16),
    _Hh3c3GGsmMnc_Type()
)
hh3c3GGsmMnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3c3GGsmMnc.setStatus("current")
_Hh3cLte_ObjectIdentity = ObjectIdentity
hh3cLte = _Hh3cLte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 5)
)
_Hh3cLteInfoTable_Object = MibTable
hh3cLteInfoTable = _Hh3cLteInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cLteInfoTable.setStatus("current")
_Hh3cLteInfoEntry_Object = MibTableRow
hh3cLteInfoEntry = _Hh3cLteInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 5, 1, 1)
)
hh3cLteInfoEntry.setIndexNames(
    (0, "HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
)
if mibBuilder.loadTexts:
    hh3cLteInfoEntry.setStatus("current")
_Hh3cLteCurrentRsrp_Type = Integer32
_Hh3cLteCurrentRsrp_Object = MibTableColumn
hh3cLteCurrentRsrp = _Hh3cLteCurrentRsrp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 5, 1, 1, 1),
    _Hh3cLteCurrentRsrp_Type()
)
hh3cLteCurrentRsrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLteCurrentRsrp.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLteCurrentRsrp.setUnits("dBm")
_Hh3cLteCurrentRsrq_Type = Integer32
_Hh3cLteCurrentRsrq_Object = MibTableColumn
hh3cLteCurrentRsrq = _Hh3cLteCurrentRsrq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 5, 1, 1, 2),
    _Hh3cLteCurrentRsrq_Type()
)
hh3cLteCurrentRsrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLteCurrentRsrq.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLteCurrentRsrq.setUnits("dB")
_Hh3cLteCurrentSinr_Type = Integer32
_Hh3cLteCurrentSinr_Object = MibTableColumn
hh3cLteCurrentSinr = _Hh3cLteCurrentSinr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 5, 1, 1, 3),
    _Hh3cLteCurrentSinr_Type()
)
hh3cLteCurrentSinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLteCurrentSinr.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLteCurrentSinr.setUnits("dB")
_Hh3cLteTxPower_Type = Integer32
_Hh3cLteTxPower_Object = MibTableColumn
hh3cLteTxPower = _Hh3cLteTxPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 5, 1, 1, 4),
    _Hh3cLteTxPower_Type()
)
hh3cLteTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLteTxPower.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLteTxPower.setUnits("dB")


class _Hh3cLteCurrentRssi_Type(Integer32):
    """Custom type hh3cLteCurrentRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_Hh3cLteCurrentRssi_Type.__name__ = "Integer32"
_Hh3cLteCurrentRssi_Object = MibTableColumn
hh3cLteCurrentRssi = _Hh3cLteCurrentRssi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 5, 1, 1, 5),
    _Hh3cLteCurrentRssi_Type()
)
hh3cLteCurrentRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLteCurrentRssi.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLteCurrentRssi.setUnits("dBm")


class _Hh3cLteRssiMediumThreshold_Type(Integer32):
    """Custom type hh3cLteRssiMediumThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Hh3cLteRssiMediumThreshold_Type.__name__ = "Integer32"
_Hh3cLteRssiMediumThreshold_Object = MibTableColumn
hh3cLteRssiMediumThreshold = _Hh3cLteRssiMediumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 5, 1, 1, 6),
    _Hh3cLteRssiMediumThreshold_Type()
)
hh3cLteRssiMediumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLteRssiMediumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLteRssiMediumThreshold.setUnits("dBm")


class _Hh3cLteRssiWeakThreshold_Type(Integer32):
    """Custom type hh3cLteRssiWeakThreshold based on Integer32"""
    defaultValue = -150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Hh3cLteRssiWeakThreshold_Type.__name__ = "Integer32"
_Hh3cLteRssiWeakThreshold_Object = MibTableColumn
hh3cLteRssiWeakThreshold = _Hh3cLteRssiWeakThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 1, 5, 1, 1, 7),
    _Hh3cLteRssiWeakThreshold_Type()
)
hh3cLteRssiWeakThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLteRssiWeakThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cLteRssiWeakThreshold.setUnits("dBm")
_Hh3c3GModemTrap_ObjectIdentity = ObjectIdentity
hh3c3GModemTrap = _Hh3c3GModemTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2)
)


class _Hh3cDevSerialNumber_Type(SnmpAdminString):
    """Custom type hh3cDevSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDevSerialNumber_Type.__name__ = "SnmpAdminString"
_Hh3cDevSerialNumber_Object = MibScalar
hh3cDevSerialNumber = _Hh3cDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 1),
    _Hh3cDevSerialNumber_Type()
)
hh3cDevSerialNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDevSerialNumber.setStatus("current")


class _Hh3cDeviceOUI_Type(SnmpAdminString):
    """Custom type hh3cDeviceOUI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cDeviceOUI_Type.__name__ = "SnmpAdminString"
_Hh3cDeviceOUI_Object = MibScalar
hh3cDeviceOUI = _Hh3cDeviceOUI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 2),
    _Hh3cDeviceOUI_Type()
)
hh3cDeviceOUI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDeviceOUI.setStatus("current")


class _Hh3cAccessMedia_Type(Integer32):
    """Custom type hh3cAccessMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("air", 2),
          ("cable", 3))
    )


_Hh3cAccessMedia_Type.__name__ = "Integer32"
_Hh3cAccessMedia_Object = MibScalar
hh3cAccessMedia = _Hh3cAccessMedia_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 3),
    _Hh3cAccessMedia_Type()
)
hh3cAccessMedia.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAccessMedia.setStatus("current")


class _Hh3c3GCurrentService_Type(Integer32):
    """Custom type hh3c3GCurrentService based on Integer32"""
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
        *(("unknown", 1),
          ("oneXRtt", 2),
          ("evDo", 3),
          ("gsm", 4),
          ("lte", 5))
    )


_Hh3c3GCurrentService_Type.__name__ = "Integer32"
_Hh3c3GCurrentService_Object = MibScalar
hh3c3GCurrentService = _Hh3c3GCurrentService_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 4),
    _Hh3c3GCurrentService_Type()
)
hh3c3GCurrentService.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3c3GCurrentService.setStatus("current")


class _Hh3c3GCurrentRssiBind_Type(Integer32):
    """Custom type hh3c3GCurrentRssiBind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-150, 0),
    )


_Hh3c3GCurrentRssiBind_Type.__name__ = "Integer32"
_Hh3c3GCurrentRssiBind_Object = MibScalar
hh3c3GCurrentRssiBind = _Hh3c3GCurrentRssiBind_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 5),
    _Hh3c3GCurrentRssiBind_Type()
)
hh3c3GCurrentRssiBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3c3GCurrentRssiBind.setStatus("current")
if mibBuilder.loadTexts:
    hh3c3GCurrentRssiBind.setUnits("dBm")


class _Hh3c3GImsiBind_Type(SnmpAdminString):
    """Custom type hh3c3GImsiBind based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3c3GImsiBind_Type.__name__ = "SnmpAdminString"
_Hh3c3GImsiBind_Object = MibScalar
hh3c3GImsiBind = _Hh3c3GImsiBind_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 6),
    _Hh3c3GImsiBind_Type()
)
hh3c3GImsiBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3c3GImsiBind.setStatus("current")


class _Hh3cSmsSrcNumberBind_Type(SnmpAdminString):
    """Custom type hh3cSmsSrcNumberBind based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Hh3cSmsSrcNumberBind_Type.__name__ = "SnmpAdminString"
_Hh3cSmsSrcNumberBind_Object = MibScalar
hh3cSmsSrcNumberBind = _Hh3cSmsSrcNumberBind_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 7),
    _Hh3cSmsSrcNumberBind_Type()
)
hh3cSmsSrcNumberBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSmsSrcNumberBind.setStatus("current")


class _Hh3cSmsTimeBind_Type(SnmpAdminString):
    """Custom type hh3cSmsTimeBind based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3cSmsTimeBind_Type.__name__ = "SnmpAdminString"
_Hh3cSmsTimeBind_Object = MibScalar
hh3cSmsTimeBind = _Hh3cSmsTimeBind_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 8),
    _Hh3cSmsTimeBind_Type()
)
hh3cSmsTimeBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSmsTimeBind.setStatus("current")
_Hh3cSmsEncodeBind_Type = Hh3cSmsEncodeType
_Hh3cSmsEncodeBind_Object = MibScalar
hh3cSmsEncodeBind = _Hh3cSmsEncodeBind_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 9),
    _Hh3cSmsEncodeBind_Type()
)
hh3cSmsEncodeBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSmsEncodeBind.setStatus("current")


class _Hh3cSmsContentBind_Type(OctetString):
    """Custom type hh3cSmsContentBind based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Hh3cSmsContentBind_Type.__name__ = "OctetString"
_Hh3cSmsContentBind_Object = MibScalar
hh3cSmsContentBind = _Hh3cSmsContentBind_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 2, 10),
    _Hh3cSmsContentBind_Type()
)
hh3cSmsContentBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSmsContentBind.setStatus("current")
_Hh3c3GModemTraps_ObjectIdentity = ObjectIdentity
hh3c3GModemTraps = _Hh3c3GModemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3)
)
_Hh3c3GModemTrapPrefix_ObjectIdentity = ObjectIdentity
hh3c3GModemTrapPrefix = _Hh3c3GModemTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cWirelessCardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 1)
)
hh3cWirelessCardInserted.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"),
        ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"))
)
if mibBuilder.loadTexts:
    hh3cWirelessCardInserted.setStatus(
        "current"
    )

hh3cWirelessCardPulledOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 2)
)
hh3cWirelessCardPulledOut.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"),
        ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"))
)
if mibBuilder.loadTexts:
    hh3cWirelessCardPulledOut.setStatus(
        "current"
    )

hh3cUIMPinInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 3)
)
hh3cUIMPinInvalid.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"),
        ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"))
)
if mibBuilder.loadTexts:
    hh3cUIMPinInvalid.setStatus(
        "current"
    )

hh3cUIMPinChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 4)
)
hh3cUIMPinChanged.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"),
        ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"),
        ("HH3C-3GMODEM-MIB", "hh3cUIMOldPin"),
        ("HH3C-3GMODEM-MIB", "hh3cUIMPin"))
)
if mibBuilder.loadTexts:
    hh3cUIMPinChanged.setStatus(
        "current"
    )

hh3cAccessMediaChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 5)
)
hh3cAccessMediaChanged.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"),
        ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cUIMImsi"),
        ("HH3C-3GMODEM-MIB", "hh3cAccessMedia"))
)
if mibBuilder.loadTexts:
    hh3cAccessMediaChanged.setStatus(
        "current"
    )

hh3c3GRssiStrongSignalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 6)
)
hh3c3GRssiStrongSignalTrap.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
        ("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"),
        ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3c3GCurrentService"),
        ("HH3C-3GMODEM-MIB", "hh3c3GCurrentRssiBind"),
        ("HH3C-3GMODEM-MIB", "hh3c3GImsiBind"))
)
if mibBuilder.loadTexts:
    hh3c3GRssiStrongSignalTrap.setStatus(
        "current"
    )

hh3c3GRssiMediumSignalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 7)
)
hh3c3GRssiMediumSignalTrap.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
        ("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"),
        ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3c3GCurrentService"),
        ("HH3C-3GMODEM-MIB", "hh3c3GCurrentRssiBind"),
        ("HH3C-3GMODEM-MIB", "hh3c3GImsiBind"))
)
if mibBuilder.loadTexts:
    hh3c3GRssiMediumSignalTrap.setStatus(
        "current"
    )

hh3c3GRssiWeakSignalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 8)
)
hh3c3GRssiWeakSignalTrap.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
        ("HH3C-3GMODEM-MIB", "hh3cDeviceOUI"),
        ("HH3C-3GMODEM-MIB", "hh3cDevSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3cWirelessCardSerialNumber"),
        ("HH3C-3GMODEM-MIB", "hh3c3GCurrentService"),
        ("HH3C-3GMODEM-MIB", "hh3c3GCurrentRssiBind"),
        ("HH3C-3GMODEM-MIB", "hh3c3GImsiBind"))
)
if mibBuilder.loadTexts:
    hh3c3GRssiWeakSignalTrap.setStatus(
        "current"
    )

hh3cSmsTxNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 9)
)
hh3cSmsTxNotification.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
        ("HH3C-3GMODEM-MIB", "hh3cSmsSendStatus"))
)
if mibBuilder.loadTexts:
    hh3cSmsTxNotification.setStatus(
        "current"
    )

hh3cSmsRxNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 98, 3, 0, 10)
)
hh3cSmsRxNotification.setObjects(
      *(("HH3C-3GMODEM-MIB", "hh3cWirelessCardIndex"),
        ("HH3C-3GMODEM-MIB", "hh3cSmsSrcNumberBind"),
        ("HH3C-3GMODEM-MIB", "hh3cSmsTimeBind"),
        ("HH3C-3GMODEM-MIB", "hh3cSmsEncodeBind"),
        ("HH3C-3GMODEM-MIB", "hh3cSmsContentBind"))
)
if mibBuilder.loadTexts:
    hh3cSmsRxNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-3GMODEM-MIB",
    **{"Hh3cUIMStatusType": Hh3cUIMStatusType,
       "Hh3cSmsEncodeType": Hh3cSmsEncodeType,
       "hh3c3GModem": hh3c3GModem,
       "hh3c3GModemObjects": hh3c3GModemObjects,
       "hh3cWirelessCard": hh3cWirelessCard,
       "hh3cWirelessCardTable": hh3cWirelessCardTable,
       "hh3cWirelessCardEntry": hh3cWirelessCardEntry,
       "hh3cWirelessCardIndex": hh3cWirelessCardIndex,
       "hh3cWirelessCardModelName": hh3cWirelessCardModelName,
       "hh3cWirelessCardMfgName": hh3cWirelessCardMfgName,
       "hh3cWirelessCardDescription": hh3cWirelessCardDescription,
       "hh3cWirelessCardSerialNumber": hh3cWirelessCardSerialNumber,
       "hh3cWirelessCardCMIIID": hh3cWirelessCardCMIIID,
       "hh3cWirelessCardHardwareVersion": hh3cWirelessCardHardwareVersion,
       "hh3cWirelessCardFirmwareVersion": hh3cWirelessCardFirmwareVersion,
       "hh3cWirelessCardPRLVersion": hh3cWirelessCardPRLVersion,
       "hh3cWirelessCardInterfaceIndex": hh3cWirelessCardInterfaceIndex,
       "hh3cWirelessCardModemStatus": hh3cWirelessCardModemStatus,
       "hh3cWirelessCardModemMode": hh3cWirelessCardModemMode,
       "hh3cWirelessCardCurNetConn": hh3cWirelessCardCurNetConn,
       "hh3cSmsGroup": hh3cSmsGroup,
       "hh3cSmsScalarObjects": hh3cSmsScalarObjects,
       "hh3cSmsRxNotifSwitch": hh3cSmsRxNotifSwitch,
       "hh3cSmsOperationTable": hh3cSmsOperationTable,
       "hh3cSmsOperationEntry": hh3cSmsOperationEntry,
       "hh3cSmsDestNumber": hh3cSmsDestNumber,
       "hh3cSmsEncode": hh3cSmsEncode,
       "hh3cSmsContent": hh3cSmsContent,
       "hh3cSmsSendStatus": hh3cSmsSendStatus,
       "hh3cWirelessCardOnlineTable": hh3cWirelessCardOnlineTable,
       "hh3cWirelessCardOnlineEntry": hh3cWirelessCardOnlineEntry,
       "hh3cWirelessCardOnlineTime": hh3cWirelessCardOnlineTime,
       "hh3cWirelessCardOnlineType": hh3cWirelessCardOnlineType,
       "hh3cUIM": hh3cUIM,
       "hh3cUIMInfoTable": hh3cUIMInfoTable,
       "hh3cUIMInfoEntry": hh3cUIMInfoEntry,
       "hh3cUIMIndex": hh3cUIMIndex,
       "hh3cUIMStatus": hh3cUIMStatus,
       "hh3cUIMImsi": hh3cUIMImsi,
       "hh3cUIMPin": hh3cUIMPin,
       "hh3cUIMVoltage": hh3cUIMVoltage,
       "hh3cUIMProvider": hh3cUIMProvider,
       "hh3cUIMSignal": hh3cUIMSignal,
       "hh3cUIMTryPinPukTimes": hh3cUIMTryPinPukTimes,
       "hh3cUIMOldPin": hh3cUIMOldPin,
       "hh3c3GCdma": hh3c3GCdma,
       "hh3c3GCdma1xRttTable": hh3c3GCdma1xRttTable,
       "hh3c3GCdma1xRttEntry": hh3c3GCdma1xRttEntry,
       "hh3c3GCdma1xRttCurrentRssi": hh3c3GCdma1xRttCurrentRssi,
       "hh3c3GCdma1xRttRssiMediumThreshold": hh3c3GCdma1xRttRssiMediumThreshold,
       "hh3c3GCdma1xRttRssiWeakThreshold": hh3c3GCdma1xRttRssiWeakThreshold,
       "hh3c3GCdma1xRttCurServiceStatus": hh3c3GCdma1xRttCurServiceStatus,
       "hh3c3GCdma1xRttCurRoamingStatus": hh3c3GCdma1xRttCurRoamingStatus,
       "hh3c3GCdma1xRttBID": hh3c3GCdma1xRttBID,
       "hh3c3GCdma1xRttSID": hh3c3GCdma1xRttSID,
       "hh3c3GCdma1xRttNID": hh3c3GCdma1xRttNID,
       "hh3c3GCdmaEvDoTable": hh3c3GCdmaEvDoTable,
       "hh3c3GCdmaEvDoEntry": hh3c3GCdmaEvDoEntry,
       "hh3c3GCdmaEvDoCurrentRssi": hh3c3GCdmaEvDoCurrentRssi,
       "hh3c3GCdmaEvDoRssiMediumThreshold": hh3c3GCdmaEvDoRssiMediumThreshold,
       "hh3c3GCdmaEvDoRssiWeakThreshold": hh3c3GCdmaEvDoRssiWeakThreshold,
       "hh3c3GCdmaEvDoCurServiceStatus": hh3c3GCdmaEvDoCurServiceStatus,
       "hh3c3GCdmaEvDoCurRoamingStatus": hh3c3GCdmaEvDoCurRoamingStatus,
       "hh3c3GCdmaEvDoSubNetID": hh3c3GCdmaEvDoSubNetID,
       "hh3c3GGsm": hh3c3GGsm,
       "hh3c3GGsmInfoTable": hh3c3GGsmInfoTable,
       "hh3c3GGsmInfoEntry": hh3c3GGsmInfoEntry,
       "hh3c3GGsmCurrentRssi": hh3c3GGsmCurrentRssi,
       "hh3c3GGsmRssiMediumThreshold": hh3c3GGsmRssiMediumThreshold,
       "hh3c3GGsmRssiWeakThreshold": hh3c3GGsmRssiWeakThreshold,
       "hh3c3GGsmImsi": hh3c3GGsmImsi,
       "hh3c3GGsmImei": hh3c3GGsmImei,
       "hh3c3GGsmApn": hh3c3GGsmApn,
       "hh3c3GGsmPacketSessionStatus": hh3c3GGsmPacketSessionStatus,
       "hh3c3GGsmNetworkSelectionMode": hh3c3GGsmNetworkSelectionMode,
       "hh3c3GGsmMobileNetworkName": hh3c3GGsmMobileNetworkName,
       "hh3c3GGsmLac": hh3c3GGsmLac,
       "hh3c3GGsmCellId": hh3c3GGsmCellId,
       "hh3c3GGsmSimStatus": hh3c3GGsmSimStatus,
       "hh3c3GGsmCurServiceStatus": hh3c3GGsmCurServiceStatus,
       "hh3c3GGsmCurRoamingStatus": hh3c3GGsmCurRoamingStatus,
       "hh3c3GGsmMcc": hh3c3GGsmMcc,
       "hh3c3GGsmMnc": hh3c3GGsmMnc,
       "hh3cLte": hh3cLte,
       "hh3cLteInfoTable": hh3cLteInfoTable,
       "hh3cLteInfoEntry": hh3cLteInfoEntry,
       "hh3cLteCurrentRsrp": hh3cLteCurrentRsrp,
       "hh3cLteCurrentRsrq": hh3cLteCurrentRsrq,
       "hh3cLteCurrentSinr": hh3cLteCurrentSinr,
       "hh3cLteTxPower": hh3cLteTxPower,
       "hh3cLteCurrentRssi": hh3cLteCurrentRssi,
       "hh3cLteRssiMediumThreshold": hh3cLteRssiMediumThreshold,
       "hh3cLteRssiWeakThreshold": hh3cLteRssiWeakThreshold,
       "hh3c3GModemTrap": hh3c3GModemTrap,
       "hh3cDevSerialNumber": hh3cDevSerialNumber,
       "hh3cDeviceOUI": hh3cDeviceOUI,
       "hh3cAccessMedia": hh3cAccessMedia,
       "hh3c3GCurrentService": hh3c3GCurrentService,
       "hh3c3GCurrentRssiBind": hh3c3GCurrentRssiBind,
       "hh3c3GImsiBind": hh3c3GImsiBind,
       "hh3cSmsSrcNumberBind": hh3cSmsSrcNumberBind,
       "hh3cSmsTimeBind": hh3cSmsTimeBind,
       "hh3cSmsEncodeBind": hh3cSmsEncodeBind,
       "hh3cSmsContentBind": hh3cSmsContentBind,
       "hh3c3GModemTraps": hh3c3GModemTraps,
       "hh3c3GModemTrapPrefix": hh3c3GModemTrapPrefix,
       "hh3cWirelessCardInserted": hh3cWirelessCardInserted,
       "hh3cWirelessCardPulledOut": hh3cWirelessCardPulledOut,
       "hh3cUIMPinInvalid": hh3cUIMPinInvalid,
       "hh3cUIMPinChanged": hh3cUIMPinChanged,
       "hh3cAccessMediaChanged": hh3cAccessMediaChanged,
       "hh3c3GRssiStrongSignalTrap": hh3c3GRssiStrongSignalTrap,
       "hh3c3GRssiMediumSignalTrap": hh3c3GRssiMediumSignalTrap,
       "hh3c3GRssiWeakSignalTrap": hh3c3GRssiWeakSignalTrap,
       "hh3cSmsTxNotification": hh3cSmsTxNotification,
       "hh3cSmsRxNotification": hh3cSmsRxNotification}
)
