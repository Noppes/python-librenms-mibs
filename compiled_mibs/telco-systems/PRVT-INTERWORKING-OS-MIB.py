# SNMP MIB module (PRVT-INTERWORKING-OS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-INTERWORKING-OS-MIB

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

(prvt_products,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "prvt-products")

(usmUserSecurityName,) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "usmUserSecurityName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtInterworkOsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1)
)
if mibBuilder.loadTexts:
    prvtInterworkOsMib.setRevisions(
        ("2008-04-09 00:00",
         "2008-03-31 00:00",
         "2008-01-01 00:00",
         "2005-02-16 00:00",
         "2004-12-20 00:00",
         "2004-03-10 00:00",
         "2003-05-08 00:00",
         "2002-12-12 00:00",
         "2002-11-26 00:00",
         "2002-11-17 00:00",
         "2001-04-19 00:00",
         "2001-03-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111)
)
_PrvtInterworkOsNotifications_ObjectIdentity = ObjectIdentity
prvtInterworkOsNotifications = _PrvtInterworkOsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 0)
)
_Version_ObjectIdentity = ObjectIdentity
version = _Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1)
)
_BootVersionNumber_Type = DisplayString
_BootVersionNumber_Object = MibScalar
bootVersionNumber = _BootVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 1),
    _BootVersionNumber_Type()
)
bootVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootVersionNumber.setStatus("current")
_BootVersionDate_Type = DisplayString
_BootVersionDate_Object = MibScalar
bootVersionDate = _BootVersionDate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 2),
    _BootVersionDate_Type()
)
bootVersionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootVersionDate.setStatus("current")
_BootVersionString_Type = DisplayString
_BootVersionString_Object = MibScalar
bootVersionString = _BootVersionString_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 3),
    _BootVersionString_Type()
)
bootVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootVersionString.setStatus("current")
_OSversionNumber_Type = DisplayString
_OSversionNumber_Object = MibScalar
oSversionNumber = _OSversionNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 4),
    _OSversionNumber_Type()
)
oSversionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oSversionNumber.setStatus("current")
_OSversionDate_Type = DisplayString
_OSversionDate_Object = MibScalar
oSversionDate = _OSversionDate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 5),
    _OSversionDate_Type()
)
oSversionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oSversionDate.setStatus("current")
_OSversionString_Type = DisplayString
_OSversionString_Object = MibScalar
oSversionString = _OSversionString_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 6),
    _OSversionString_Type()
)
oSversionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oSversionString.setStatus("current")
_AppletVersionNumber_Type = DisplayString
_AppletVersionNumber_Object = MibScalar
appletVersionNumber = _AppletVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 7),
    _AppletVersionNumber_Type()
)
appletVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appletVersionNumber.setStatus("current")
_AppletVersionDate_Type = DisplayString
_AppletVersionDate_Object = MibScalar
appletVersionDate = _AppletVersionDate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 8),
    _AppletVersionDate_Type()
)
appletVersionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appletVersionDate.setStatus("current")
_Option_ObjectIdentity = ObjectIdentity
option = _Option_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 2)
)
_OptionInstalled_Type = OctetString
_OptionInstalled_Object = MibScalar
optionInstalled = _OptionInstalled_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 2, 1),
    _OptionInstalled_Type()
)
optionInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optionInstalled.setStatus("current")
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3)
)
_ManagementConnectivity_ObjectIdentity = ObjectIdentity
managementConnectivity = _ManagementConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 1)
)
_ManagementConnectivityMACAddr_Type = MacAddress
_ManagementConnectivityMACAddr_Object = MibScalar
managementConnectivityMACAddr = _ManagementConnectivityMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 1, 1),
    _ManagementConnectivityMACAddr_Type()
)
managementConnectivityMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementConnectivityMACAddr.setStatus("current")
_ManagementConnectivityIpAddress_Type = IpAddress
_ManagementConnectivityIpAddress_Object = MibScalar
managementConnectivityIpAddress = _ManagementConnectivityIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 1, 2),
    _ManagementConnectivityIpAddress_Type()
)
managementConnectivityIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementConnectivityIpAddress.setStatus("current")
_ManagementConnectivityIPNetMask_Type = IpAddress
_ManagementConnectivityIPNetMask_Object = MibScalar
managementConnectivityIPNetMask = _ManagementConnectivityIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 1, 3),
    _ManagementConnectivityIPNetMask_Type()
)
managementConnectivityIPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementConnectivityIPNetMask.setStatus("current")
_ManagementIPGateAddress_Type = IpAddress
_ManagementIPGateAddress_Object = MibScalar
managementIPGateAddress = _ManagementIPGateAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 1, 4),
    _ManagementIPGateAddress_Type()
)
managementIPGateAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementIPGateAddress.setStatus("current")


class _ManagementSerialBaud_Type(Integer32):
    """Custom type managementSerialBaud based on Integer32"""
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
        *(("baud2400", 1),
          ("baud9600", 2),
          ("baud19200", 3),
          ("baud38400", 4))
    )


_ManagementSerialBaud_Type.__name__ = "Integer32"
_ManagementSerialBaud_Object = MibScalar
managementSerialBaud = _ManagementSerialBaud_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 1, 5),
    _ManagementSerialBaud_Type()
)
managementSerialBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementSerialBaud.setStatus("current")
_ManagementLoad_ObjectIdentity = ObjectIdentity
managementLoad = _ManagementLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 2)
)
_ManagementLoadTftpServerAddress_Type = IpAddress
_ManagementLoadTftpServerAddress_Object = MibScalar
managementLoadTftpServerAddress = _ManagementLoadTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 2, 1),
    _ManagementLoadTftpServerAddress_Type()
)
managementLoadTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementLoadTftpServerAddress.setStatus("current")


class _ManagementLoadFileName_Type(OctetString):
    """Custom type managementLoadFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ManagementLoadFileName_Type.__name__ = "OctetString"
_ManagementLoadFileName_Object = MibScalar
managementLoadFileName = _ManagementLoadFileName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 2, 2),
    _ManagementLoadFileName_Type()
)
managementLoadFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementLoadFileName.setStatus("current")


class _ManagementLoadType_Type(Integer32):
    """Custom type managementLoadType based on Integer32"""
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
        *(("application", 1),
          ("boot", 2),
          ("configuration", 3),
          ("java", 4),
          ("vdsl-E2", 5))
    )


_ManagementLoadType_Type.__name__ = "Integer32"
_ManagementLoadType_Object = MibScalar
managementLoadType = _ManagementLoadType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 2, 3),
    _ManagementLoadType_Type()
)
managementLoadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementLoadType.setStatus("current")


class _ManagementLoadExecute_Type(Integer32):
    """Custom type managementLoadExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("download", 2),
          ("upload", 3))
    )


_ManagementLoadExecute_Type.__name__ = "Integer32"
_ManagementLoadExecute_Object = MibScalar
managementLoadExecute = _ManagementLoadExecute_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 2, 4),
    _ManagementLoadExecute_Type()
)
managementLoadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementLoadExecute.setStatus("current")


class _ManagementLoadExecuteStatus_Type(Integer32):
    """Custom type managementLoadExecuteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("not-started", 1),
          ("in-progress", 2),
          ("success", 3),
          ("error-connection", 4),
          ("error-filename", 5),
          ("error-fault", 6))
    )


_ManagementLoadExecuteStatus_Type.__name__ = "Integer32"
_ManagementLoadExecuteStatus_Object = MibScalar
managementLoadExecuteStatus = _ManagementLoadExecuteStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 2, 5),
    _ManagementLoadExecuteStatus_Type()
)
managementLoadExecuteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementLoadExecuteStatus.setStatus("current")
_ManagementMisc_ObjectIdentity = ObjectIdentity
managementMisc = _ManagementMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3)
)


class _ManagementMiscSaveToNvm_Type(Integer32):
    """Custom type managementMiscSaveToNvm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("save", 2))
    )


_ManagementMiscSaveToNvm_Type.__name__ = "Integer32"
_ManagementMiscSaveToNvm_Object = MibScalar
managementMiscSaveToNvm = _ManagementMiscSaveToNvm_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3, 1),
    _ManagementMiscSaveToNvm_Type()
)
managementMiscSaveToNvm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementMiscSaveToNvm.setStatus("current")


class _ManagementMiscReset_Type(Integer32):
    """Custom type managementMiscReset based on Integer32"""
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
        *(("noop", 1),
          ("reset", 2),
          ("reset-to-defaults", 3),
          ("save-and-reset", 4))
    )


_ManagementMiscReset_Type.__name__ = "Integer32"
_ManagementMiscReset_Object = MibScalar
managementMiscReset = _ManagementMiscReset_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3, 2),
    _ManagementMiscReset_Type()
)
managementMiscReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementMiscReset.setStatus("current")


class _ManagementMiscReload_Type(Integer32):
    """Custom type managementMiscReload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("save-and-reload", 2))
    )


_ManagementMiscReload_Type.__name__ = "Integer32"
_ManagementMiscReload_Object = MibScalar
managementMiscReload = _ManagementMiscReload_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3, 3),
    _ManagementMiscReload_Type()
)
managementMiscReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementMiscReload.setStatus("current")


class _ManagementMiscReloadInTime_Type(OctetString):
    """Custom type managementMiscReloadInTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ManagementMiscReloadInTime_Type.__name__ = "OctetString"
_ManagementMiscReloadInTime_Object = MibScalar
managementMiscReloadInTime = _ManagementMiscReloadInTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3, 4),
    _ManagementMiscReloadInTime_Type()
)
managementMiscReloadInTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementMiscReloadInTime.setStatus("current")


class _ManagementMiscReloadAtTime_Type(OctetString):
    """Custom type managementMiscReloadAtTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ManagementMiscReloadAtTime_Type.__name__ = "OctetString"
_ManagementMiscReloadAtTime_Object = MibScalar
managementMiscReloadAtTime = _ManagementMiscReloadAtTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3, 5),
    _ManagementMiscReloadAtTime_Type()
)
managementMiscReloadAtTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementMiscReloadAtTime.setStatus("current")


class _ManagementMiscReloadSaveInTime_Type(OctetString):
    """Custom type managementMiscReloadSaveInTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ManagementMiscReloadSaveInTime_Type.__name__ = "OctetString"
_ManagementMiscReloadSaveInTime_Object = MibScalar
managementMiscReloadSaveInTime = _ManagementMiscReloadSaveInTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3, 6),
    _ManagementMiscReloadSaveInTime_Type()
)
managementMiscReloadSaveInTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementMiscReloadSaveInTime.setStatus("current")


class _ManagementMiscReloadSaveAtTime_Type(OctetString):
    """Custom type managementMiscReloadSaveAtTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ManagementMiscReloadSaveAtTime_Type.__name__ = "OctetString"
_ManagementMiscReloadSaveAtTime_Object = MibScalar
managementMiscReloadSaveAtTime = _ManagementMiscReloadSaveAtTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3, 7),
    _ManagementMiscReloadSaveAtTime_Type()
)
managementMiscReloadSaveAtTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementMiscReloadSaveAtTime.setStatus("current")
_ManagementLicense_ObjectIdentity = ObjectIdentity
managementLicense = _ManagementLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 4)
)


class _ManagementOptionSupportStatus_Type(Integer32):
    """Custom type managementOptionSupportStatus based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("reserved0", 0),
          ("reserved1", 1),
          ("reserved2", 2),
          ("reserved3", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved6", 6),
          ("reserved7", 7),
          ("reserved8", 8),
          ("reserved9", 9),
          ("licNotSpecified", 10),
          ("licBasic", 11),
          ("licML", 12),
          ("licAdvML", 13),
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
          ("reserved31", 31))
    )


_ManagementOptionSupportStatus_Type.__name__ = "Integer32"
_ManagementOptionSupportStatus_Object = MibScalar
managementOptionSupportStatus = _ManagementOptionSupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 4, 1),
    _ManagementOptionSupportStatus_Type()
)
managementOptionSupportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementOptionSupportStatus.setStatus("current")


class _ManagementOptionSupportKey_Type(OctetString):
    """Custom type managementOptionSupportKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ManagementOptionSupportKey_Type.__name__ = "OctetString"
_ManagementOptionSupportKey_Object = MibScalar
managementOptionSupportKey = _ManagementOptionSupportKey_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 4, 2),
    _ManagementOptionSupportKey_Type()
)
managementOptionSupportKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementOptionSupportKey.setStatus("current")
_ManagementOptionSupportAddress_Type = IpAddress
_ManagementOptionSupportAddress_Object = MibScalar
managementOptionSupportAddress = _ManagementOptionSupportAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 4, 3),
    _ManagementOptionSupportAddress_Type()
)
managementOptionSupportAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    managementOptionSupportAddress.setStatus("current")


class _ManagementOptionSupportL3Capable_Type(TruthValue):
    """Custom type managementOptionSupportL3Capable based on TruthValue"""
    defaultValue = 1


_ManagementOptionSupportL3Capable_Type.__name__ = "TruthValue"
_ManagementOptionSupportL3Capable_Object = MibScalar
managementOptionSupportL3Capable = _ManagementOptionSupportL3Capable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 4, 4),
    _ManagementOptionSupportL3Capable_Type()
)
managementOptionSupportL3Capable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementOptionSupportL3Capable.setStatus("current")
_PrvtBootConfigUpgrade_ObjectIdentity = ObjectIdentity
prvtBootConfigUpgrade = _PrvtBootConfigUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 5)
)
_PrvtBootUpgradeSrcURI_Type = DisplayString
_PrvtBootUpgradeSrcURI_Object = MibScalar
prvtBootUpgradeSrcURI = _PrvtBootUpgradeSrcURI_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 5, 1),
    _PrvtBootUpgradeSrcURI_Type()
)
prvtBootUpgradeSrcURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtBootUpgradeSrcURI.setStatus("current")
_PrvtBootApplicationNameURI_Type = DisplayString
_PrvtBootApplicationNameURI_Object = MibScalar
prvtBootApplicationNameURI = _PrvtBootApplicationNameURI_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 5, 2),
    _PrvtBootApplicationNameURI_Type()
)
prvtBootApplicationNameURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtBootApplicationNameURI.setStatus("current")
_PrvtBootConfigURI_Type = DisplayString
_PrvtBootConfigURI_Object = MibScalar
prvtBootConfigURI = _PrvtBootConfigURI_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 5, 3),
    _PrvtBootConfigURI_Type()
)
prvtBootConfigURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtBootConfigURI.setStatus("current")


class _PrvtBootUpgradeCmd_Type(Integer32):
    """Custom type prvtBootUpgradeCmd based on Integer32"""
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
        *(("none", 0),
          ("ready", 1),
          ("apply", 2),
          ("applyExec", 3))
    )


_PrvtBootUpgradeCmd_Type.__name__ = "Integer32"
_PrvtBootUpgradeCmd_Object = MibScalar
prvtBootUpgradeCmd = _PrvtBootUpgradeCmd_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 5, 4),
    _PrvtBootUpgradeCmd_Type()
)
prvtBootUpgradeCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtBootUpgradeCmd.setStatus("current")


class _PrvtBootOperStatus_Type(Integer32):
    """Custom type prvtBootOperStatus based on Integer32"""
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
        *(("unknown", 0),
          ("ready", 1),
          ("notReady", 2),
          ("upgradeInProgress", 3))
    )


_PrvtBootOperStatus_Type.__name__ = "Integer32"
_PrvtBootOperStatus_Object = MibScalar
prvtBootOperStatus = _PrvtBootOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 5, 5),
    _PrvtBootOperStatus_Type()
)
prvtBootOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtBootOperStatus.setStatus("current")


class _PrvtBootErrorCondition_Type(Integer32):
    """Custom type prvtBootErrorCondition based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("genericError", 1),
          ("copyFailed", 2),
          ("downloadFailed", 3),
          ("freeSpaceError", 4),
          ("validationFailed", 5),
          ("backupFailed", 6),
          ("inProgressError", 7),
          ("consistencyError", 8),
          ("fileSystemError", 9),
          ("profileNameError", 10),
          ("profileError", 11),
          ("fileNameError", 12),
          ("pathError", 13),
          ("zFileError", 14),
          ("cannotFindFile", 15),
          ("defApplicationProfileError", 16),
          ("configProfileError", 17),
          ("bootDevProfileError", 18),
          ("ftpServerProfileError", 19),
          ("ftpUserProfileError", 20),
          ("ftpPassProfileError", 21))
    )


_PrvtBootErrorCondition_Type.__name__ = "Integer32"
_PrvtBootErrorCondition_Object = MibScalar
prvtBootErrorCondition = _PrvtBootErrorCondition_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 5, 6),
    _PrvtBootErrorCondition_Type()
)
prvtBootErrorCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtBootErrorCondition.setStatus("current")
_Cpu_ObjectIdentity = ObjectIdentity
cpu = _Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4)
)
_CpuMonitoring_ObjectIdentity = ObjectIdentity
cpuMonitoring = _CpuMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 1)
)


class _CpuMonitoringStatus_Type(Integer32):
    """Custom type cpuMonitoringStatus based on Integer32"""
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


_CpuMonitoringStatus_Type.__name__ = "Integer32"
_CpuMonitoringStatus_Object = MibScalar
cpuMonitoringStatus = _CpuMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 1, 1),
    _CpuMonitoringStatus_Type()
)
cpuMonitoringStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuMonitoringStatus.setStatus("current")
_CpuMonitoringUtilization_Type = Integer32
_CpuMonitoringUtilization_Object = MibScalar
cpuMonitoringUtilization = _CpuMonitoringUtilization_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 1, 2),
    _CpuMonitoringUtilization_Type()
)
cpuMonitoringUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuMonitoringUtilization.setStatus("current")
_CpuRedundancy_ObjectIdentity = ObjectIdentity
cpuRedundancy = _CpuRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2)
)
_CpuHwRedundancySupport_Type = TruthValue
_CpuHwRedundancySupport_Object = MibScalar
cpuHwRedundancySupport = _CpuHwRedundancySupport_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 1),
    _CpuHwRedundancySupport_Type()
)
cpuHwRedundancySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuHwRedundancySupport.setStatus("current")
_CpuRedundancyTable_Object = MibTable
cpuRedundancyTable = _CpuRedundancyTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    cpuRedundancyTable.setStatus("current")
_CpuRedundancyEntry_Object = MibTableRow
cpuRedundancyEntry = _CpuRedundancyEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 2, 1)
)
cpuRedundancyEntry.setIndexNames(
    (0, "PRVT-INTERWORKING-OS-MIB", "cpuId"),
)
if mibBuilder.loadTexts:
    cpuRedundancyEntry.setStatus("current")


class _CpuId_Type(Integer32):
    """Custom type cpuId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CpuId_Type.__name__ = "Integer32"
_CpuId_Object = MibTableColumn
cpuId = _CpuId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 2, 1, 1),
    _CpuId_Type()
)
cpuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpuId.setStatus("current")
_CpuName_Type = DisplayString
_CpuName_Object = MibTableColumn
cpuName = _CpuName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 2, 1, 2),
    _CpuName_Type()
)
cpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuName.setStatus("current")


class _CpuStatus_Type(Integer32):
    """Custom type cpuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_CpuStatus_Type.__name__ = "Integer32"
_CpuStatus_Object = MibTableColumn
cpuStatus = _CpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 2, 1, 3),
    _CpuStatus_Type()
)
cpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatus.setStatus("current")
_CpuRedundancySupport_Type = TruthValue
_CpuRedundancySupport_Object = MibTableColumn
cpuRedundancySupport = _CpuRedundancySupport_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 2, 1, 4),
    _CpuRedundancySupport_Type()
)
cpuRedundancySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRedundancySupport.setStatus("current")
_CpuSWVersionString_Type = DisplayString
_CpuSWVersionString_Object = MibTableColumn
cpuSWVersionString = _CpuSWVersionString_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 2, 1, 5),
    _CpuSWVersionString_Type()
)
cpuSWVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuSWVersionString.setStatus("current")
_CpuHW_ObjectIdentity = ObjectIdentity
cpuHW = _CpuHW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 3)
)
_CpuRAMsize_Type = Integer32
_CpuRAMsize_Object = MibScalar
cpuRAMsize = _CpuRAMsize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 3, 1),
    _CpuRAMsize_Type()
)
cpuRAMsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRAMsize.setStatus("current")
_PrvtInterworkOsConformance_ObjectIdentity = ObjectIdentity
prvtInterworkOsConformance = _PrvtInterworkOsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 5)
)

# Managed Objects groups


# Notification objects

imageCrcCheckFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 0, 1)
)
imageCrcCheckFailed.setObjects(
      *(("PRVT-INTERWORKING-OS-MIB", "managementLoadTftpServerAddress"),
        ("PRVT-INTERWORKING-OS-MIB", "managementLoadFileName"))
)
if mibBuilder.loadTexts:
    imageCrcCheckFailed.setStatus(
        "current"
    )

configurationLoadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 0, 2)
)
configurationLoadFailed.setObjects(
      *(("PRVT-INTERWORKING-OS-MIB", "managementLoadTftpServerAddress"),
        ("PRVT-INTERWORKING-OS-MIB", "managementLoadFileName"))
)
if mibBuilder.loadTexts:
    configurationLoadFailed.setStatus(
        "current"
    )

unauthorizedAccessViaCLI = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 0, 3)
)
if mibBuilder.loadTexts:
    unauthorizedAccessViaCLI.setStatus(
        "current"
    )

snmpSetExecuted = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 0, 4)
)
snmpSetExecuted.setObjects(
    ("SNMP-USER-BASED-SM-MIB", "usmUserSecurityName")
)
if mibBuilder.loadTexts:
    snmpSetExecuted.setStatus(
        "current"
    )

managementOptionSupportChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 0, 5)
)
managementOptionSupportChanged.setObjects(
      *(("PRVT-INTERWORKING-OS-MIB", "managementOptionSupportStatus"),
        ("PRVT-INTERWORKING-OS-MIB", "managementOptionSupportAddress"))
)
if mibBuilder.loadTexts:
    managementOptionSupportChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-INTERWORKING-OS-MIB",
    **{"software": software,
       "prvtInterworkOsMib": prvtInterworkOsMib,
       "prvtInterworkOsNotifications": prvtInterworkOsNotifications,
       "imageCrcCheckFailed": imageCrcCheckFailed,
       "configurationLoadFailed": configurationLoadFailed,
       "unauthorizedAccessViaCLI": unauthorizedAccessViaCLI,
       "snmpSetExecuted": snmpSetExecuted,
       "managementOptionSupportChanged": managementOptionSupportChanged,
       "version": version,
       "bootVersionNumber": bootVersionNumber,
       "bootVersionDate": bootVersionDate,
       "bootVersionString": bootVersionString,
       "oSversionNumber": oSversionNumber,
       "oSversionDate": oSversionDate,
       "oSversionString": oSversionString,
       "appletVersionNumber": appletVersionNumber,
       "appletVersionDate": appletVersionDate,
       "option": option,
       "optionInstalled": optionInstalled,
       "management": management,
       "managementConnectivity": managementConnectivity,
       "managementConnectivityMACAddr": managementConnectivityMACAddr,
       "managementConnectivityIpAddress": managementConnectivityIpAddress,
       "managementConnectivityIPNetMask": managementConnectivityIPNetMask,
       "managementIPGateAddress": managementIPGateAddress,
       "managementSerialBaud": managementSerialBaud,
       "managementLoad": managementLoad,
       "managementLoadTftpServerAddress": managementLoadTftpServerAddress,
       "managementLoadFileName": managementLoadFileName,
       "managementLoadType": managementLoadType,
       "managementLoadExecute": managementLoadExecute,
       "managementLoadExecuteStatus": managementLoadExecuteStatus,
       "managementMisc": managementMisc,
       "managementMiscSaveToNvm": managementMiscSaveToNvm,
       "managementMiscReset": managementMiscReset,
       "managementMiscReload": managementMiscReload,
       "managementMiscReloadInTime": managementMiscReloadInTime,
       "managementMiscReloadAtTime": managementMiscReloadAtTime,
       "managementMiscReloadSaveInTime": managementMiscReloadSaveInTime,
       "managementMiscReloadSaveAtTime": managementMiscReloadSaveAtTime,
       "managementLicense": managementLicense,
       "managementOptionSupportStatus": managementOptionSupportStatus,
       "managementOptionSupportKey": managementOptionSupportKey,
       "managementOptionSupportAddress": managementOptionSupportAddress,
       "managementOptionSupportL3Capable": managementOptionSupportL3Capable,
       "prvtBootConfigUpgrade": prvtBootConfigUpgrade,
       "prvtBootUpgradeSrcURI": prvtBootUpgradeSrcURI,
       "prvtBootApplicationNameURI": prvtBootApplicationNameURI,
       "prvtBootConfigURI": prvtBootConfigURI,
       "prvtBootUpgradeCmd": prvtBootUpgradeCmd,
       "prvtBootOperStatus": prvtBootOperStatus,
       "prvtBootErrorCondition": prvtBootErrorCondition,
       "cpu": cpu,
       "cpuMonitoring": cpuMonitoring,
       "cpuMonitoringStatus": cpuMonitoringStatus,
       "cpuMonitoringUtilization": cpuMonitoringUtilization,
       "cpuRedundancy": cpuRedundancy,
       "cpuHwRedundancySupport": cpuHwRedundancySupport,
       "cpuRedundancyTable": cpuRedundancyTable,
       "cpuRedundancyEntry": cpuRedundancyEntry,
       "cpuId": cpuId,
       "cpuName": cpuName,
       "cpuStatus": cpuStatus,
       "cpuRedundancySupport": cpuRedundancySupport,
       "cpuSWVersionString": cpuSWVersionString,
       "cpuHW": cpuHW,
       "cpuRAMsize": cpuRAMsize,
       "prvtInterworkOsConformance": prvtInterworkOsConformance}
)
