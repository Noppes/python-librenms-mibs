# SNMP MIB module (HH3C-HPEOC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-HPEOC-MIB

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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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

hh3cHPEOC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cHPEOCSystem_ObjectIdentity = ObjectIdentity
hh3cHPEOCSystem = _Hh3cHPEOCSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1)
)


class _Hh3cHPEOCCltVlanType_Type(Integer32):
    """Custom type hh3cHPEOCCltVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021q", 1),
          ("portbased", 2))
    )


_Hh3cHPEOCCltVlanType_Type.__name__ = "Integer32"
_Hh3cHPEOCCltVlanType_Object = MibScalar
hh3cHPEOCCltVlanType = _Hh3cHPEOCCltVlanType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 1),
    _Hh3cHPEOCCltVlanType_Type()
)
hh3cHPEOCCltVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCltVlanType.setStatus("current")
_Hh3cHPEOCCltVlanManTable_Object = MibTable
hh3cHPEOCCltVlanManTable = _Hh3cHPEOCCltVlanManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cHPEOCCltVlanManTable.setStatus("current")
_Hh3cHPEOCCltVlanManEntry_Object = MibTableRow
hh3cHPEOCCltVlanManEntry = _Hh3cHPEOCCltVlanManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 2, 1)
)
hh3cHPEOCCltVlanManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cHPEOCCltVlanManEntry.setStatus("current")


class _Hh3cHPEOCCltEthPortType_Type(Integer32):
    """Custom type hh3cHPEOCCltEthPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("debug", 2))
    )


_Hh3cHPEOCCltEthPortType_Type.__name__ = "Integer32"
_Hh3cHPEOCCltEthPortType_Object = MibTableColumn
hh3cHPEOCCltEthPortType = _Hh3cHPEOCCltEthPortType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 2, 1, 1),
    _Hh3cHPEOCCltEthPortType_Type()
)
hh3cHPEOCCltEthPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCltEthPortType.setStatus("current")
_Hh3cHPEOCCltSysManTable_Object = MibTable
hh3cHPEOCCltSysManTable = _Hh3cHPEOCCltSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cHPEOCCltSysManTable.setStatus("current")
_Hh3cHPEOCCltSysManEntry_Object = MibTableRow
hh3cHPEOCCltSysManEntry = _Hh3cHPEOCCltSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 3, 1)
)
hh3cHPEOCCltSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cHPEOCCltSysManEntry.setStatus("current")


class _Hh3cHPEOCCltDescr_Type(DisplayString):
    """Custom type hh3cHPEOCCltDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_Hh3cHPEOCCltDescr_Type.__name__ = "DisplayString"
_Hh3cHPEOCCltDescr_Object = MibTableColumn
hh3cHPEOCCltDescr = _Hh3cHPEOCCltDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 3, 1, 1),
    _Hh3cHPEOCCltDescr_Type()
)
hh3cHPEOCCltDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCltDescr.setStatus("current")
_Hh3cHPEOCCltFwVersion_Type = DisplayString
_Hh3cHPEOCCltFwVersion_Object = MibTableColumn
hh3cHPEOCCltFwVersion = _Hh3cHPEOCCltFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 3, 1, 2),
    _Hh3cHPEOCCltFwVersion_Type()
)
hh3cHPEOCCltFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCCltFwVersion.setStatus("current")


class _Hh3cHPEOCCltLinkState_Type(Integer32):
    """Custom type hh3cHPEOCCltLinkState based on Integer32"""
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
        *(("physicaldown", 1),
          ("linkdown", 2),
          ("linkup", 3),
          ("loopback", 4))
    )


_Hh3cHPEOCCltLinkState_Type.__name__ = "Integer32"
_Hh3cHPEOCCltLinkState_Object = MibTableColumn
hh3cHPEOCCltLinkState = _Hh3cHPEOCCltLinkState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 3, 1, 3),
    _Hh3cHPEOCCltLinkState_Type()
)
hh3cHPEOCCltLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCCltLinkState.setStatus("current")
_Hh3cHPEOCCnuSysManTable_Object = MibTable
hh3cHPEOCCnuSysManTable = _Hh3cHPEOCCnuSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cHPEOCCnuSysManTable.setStatus("current")
_Hh3cHPEOCCnuSysManEntry_Object = MibTableRow
hh3cHPEOCCnuSysManEntry = _Hh3cHPEOCCnuSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 4, 1)
)
hh3cHPEOCCnuSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cHPEOCCnuSysManEntry.setStatus("current")
_Hh3cHPEOCCnuBcastControl_Type = TruthValue
_Hh3cHPEOCCnuBcastControl_Object = MibTableColumn
hh3cHPEOCCnuBcastControl = _Hh3cHPEOCCnuBcastControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 4, 1, 1),
    _Hh3cHPEOCCnuBcastControl_Type()
)
hh3cHPEOCCnuBcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCnuBcastControl.setStatus("current")
_Hh3cHPEOCCnuAnonymStatus_Type = TruthValue
_Hh3cHPEOCCnuAnonymStatus_Object = MibTableColumn
hh3cHPEOCCnuAnonymStatus = _Hh3cHPEOCCnuAnonymStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 4, 1, 2),
    _Hh3cHPEOCCnuAnonymStatus_Type()
)
hh3cHPEOCCnuAnonymStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCCnuAnonymStatus.setStatus("current")
_Hh3cHPEOCCnuMacLimit_Type = Unsigned32
_Hh3cHPEOCCnuMacLimit_Object = MibTableColumn
hh3cHPEOCCnuMacLimit = _Hh3cHPEOCCnuMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 4, 1, 3),
    _Hh3cHPEOCCnuMacLimit_Type()
)
hh3cHPEOCCnuMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCnuMacLimit.setStatus("current")


class _Hh3cHPEOCCltAutoUpgrade_Type(TruthValue):
    """Custom type hh3cHPEOCCltAutoUpgrade based on TruthValue"""
    defaultValue = 2


_Hh3cHPEOCCltAutoUpgrade_Type.__name__ = "TruthValue"
_Hh3cHPEOCCltAutoUpgrade_Object = MibScalar
hh3cHPEOCCltAutoUpgrade = _Hh3cHPEOCCltAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 5),
    _Hh3cHPEOCCltAutoUpgrade_Type()
)
hh3cHPEOCCltAutoUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCltAutoUpgrade.setStatus("current")
_Hh3cHPEOCOnLineCnuNumber_Type = Integer32
_Hh3cHPEOCOnLineCnuNumber_Object = MibScalar
hh3cHPEOCOnLineCnuNumber = _Hh3cHPEOCOnLineCnuNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 6),
    _Hh3cHPEOCOnLineCnuNumber_Type()
)
hh3cHPEOCOnLineCnuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCOnLineCnuNumber.setStatus("current")
_Hh3cHPEOCCpuMacAddress_Type = MacAddress
_Hh3cHPEOCCpuMacAddress_Object = MibScalar
hh3cHPEOCCpuMacAddress = _Hh3cHPEOCCpuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 7),
    _Hh3cHPEOCCpuMacAddress_Type()
)
hh3cHPEOCCpuMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCCpuMacAddress.setStatus("current")
_Hh3cHPEOCOffLineCnuNumber_Type = Integer32
_Hh3cHPEOCOffLineCnuNumber_Object = MibScalar
hh3cHPEOCOffLineCnuNumber = _Hh3cHPEOCOffLineCnuNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 8),
    _Hh3cHPEOCOffLineCnuNumber_Type()
)
hh3cHPEOCOffLineCnuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCOffLineCnuNumber.setStatus("current")
_Hh3cHPEOCDownLoadCNUFWResult_Type = DisplayString
_Hh3cHPEOCDownLoadCNUFWResult_Object = MibScalar
hh3cHPEOCDownLoadCNUFWResult = _Hh3cHPEOCDownLoadCNUFWResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 9),
    _Hh3cHPEOCDownLoadCNUFWResult_Type()
)
hh3cHPEOCDownLoadCNUFWResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cHPEOCDownLoadCNUFWResult.setStatus("current")


class _Hh3cHPEOCCltAutoUpgradeType_Type(Integer32):
    """Custom type hh3cHPEOCCltAutoUpgradeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("ftp", 2),
          ("tftp", 3))
    )


_Hh3cHPEOCCltAutoUpgradeType_Type.__name__ = "Integer32"
_Hh3cHPEOCCltAutoUpgradeType_Object = MibScalar
hh3cHPEOCCltAutoUpgradeType = _Hh3cHPEOCCltAutoUpgradeType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 10),
    _Hh3cHPEOCCltAutoUpgradeType_Type()
)
hh3cHPEOCCltAutoUpgradeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCltAutoUpgradeType.setStatus("current")
_Hh3cHPEOCAutoUpObjects_ObjectIdentity = ObjectIdentity
hh3cHPEOCAutoUpObjects = _Hh3cHPEOCAutoUpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 11)
)
_Hh3cHPEOCServerAddress_Type = IpAddress
_Hh3cHPEOCServerAddress_Object = MibScalar
hh3cHPEOCServerAddress = _Hh3cHPEOCServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 11, 1),
    _Hh3cHPEOCServerAddress_Type()
)
hh3cHPEOCServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCServerAddress.setStatus("current")
_Hh3cHPEOCServerUser_Type = DisplayString
_Hh3cHPEOCServerUser_Object = MibScalar
hh3cHPEOCServerUser = _Hh3cHPEOCServerUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 11, 2),
    _Hh3cHPEOCServerUser_Type()
)
hh3cHPEOCServerUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCServerUser.setStatus("current")
_Hh3cHPEOCServerPassword_Type = DisplayString
_Hh3cHPEOCServerPassword_Object = MibScalar
hh3cHPEOCServerPassword = _Hh3cHPEOCServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 11, 3),
    _Hh3cHPEOCServerPassword_Type()
)
hh3cHPEOCServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCServerPassword.setStatus("current")


class _Hh3cHPEOCCltLoopbackDetect_Type(Integer32):
    """Custom type hh3cHPEOCCltLoopbackDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Hh3cHPEOCCltLoopbackDetect_Type.__name__ = "Integer32"
_Hh3cHPEOCCltLoopbackDetect_Object = MibScalar
hh3cHPEOCCltLoopbackDetect = _Hh3cHPEOCCltLoopbackDetect_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 12),
    _Hh3cHPEOCCltLoopbackDetect_Type()
)
hh3cHPEOCCltLoopbackDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCltLoopbackDetect.setStatus("current")


class _Hh3cHPEOCTemplateEnable_Type(Integer32):
    """Custom type hh3cHPEOCTemplateEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Hh3cHPEOCTemplateEnable_Type.__name__ = "Integer32"
_Hh3cHPEOCTemplateEnable_Object = MibScalar
hh3cHPEOCTemplateEnable = _Hh3cHPEOCTemplateEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 1, 13),
    _Hh3cHPEOCTemplateEnable_Type()
)
hh3cHPEOCTemplateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateEnable.setStatus("current")
_Hh3cHPEOCCableInfo_ObjectIdentity = ObjectIdentity
hh3cHPEOCCableInfo = _Hh3cHPEOCCableInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2)
)
_Hh3cHPEOCCableInfoTable_Object = MibTable
hh3cHPEOCCableInfoTable = _Hh3cHPEOCCableInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cHPEOCCableInfoTable.setStatus("current")
_Hh3cHPEOCCableInfoEntry_Object = MibTableRow
hh3cHPEOCCableInfoEntry = _Hh3cHPEOCCableInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1)
)
hh3cHPEOCCableInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cHPEOCCableInfoEntry.setStatus("current")
_Hh3cHPEOCFECErrors_Type = Counter64
_Hh3cHPEOCFECErrors_Object = MibTableColumn
hh3cHPEOCFECErrors = _Hh3cHPEOCFECErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 1),
    _Hh3cHPEOCFECErrors_Type()
)
hh3cHPEOCFECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCFECErrors.setStatus("current")
_Hh3cHPEOCAvgBitsPerCarrier_Type = Unsigned32
_Hh3cHPEOCAvgBitsPerCarrier_Object = MibTableColumn
hh3cHPEOCAvgBitsPerCarrier = _Hh3cHPEOCAvgBitsPerCarrier_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 2),
    _Hh3cHPEOCAvgBitsPerCarrier_Type()
)
hh3cHPEOCAvgBitsPerCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCAvgBitsPerCarrier.setStatus("current")
_Hh3cHPEOCAvgSNRPerCarrier_Type = Integer32
_Hh3cHPEOCAvgSNRPerCarrier_Object = MibTableColumn
hh3cHPEOCAvgSNRPerCarrier = _Hh3cHPEOCAvgSNRPerCarrier_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 3),
    _Hh3cHPEOCAvgSNRPerCarrier_Type()
)
hh3cHPEOCAvgSNRPerCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCAvgSNRPerCarrier.setStatus("current")
_Hh3cHPEOCAvgInPBCRCErrors_Type = Unsigned32
_Hh3cHPEOCAvgInPBCRCErrors_Object = MibTableColumn
hh3cHPEOCAvgInPBCRCErrors = _Hh3cHPEOCAvgInPBCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 4),
    _Hh3cHPEOCAvgInPBCRCErrors_Type()
)
hh3cHPEOCAvgInPBCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCAvgInPBCRCErrors.setStatus("current")
_Hh3cHPEOCInTotalPkts_Type = Counter64
_Hh3cHPEOCInTotalPkts_Object = MibTableColumn
hh3cHPEOCInTotalPkts = _Hh3cHPEOCInTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 5),
    _Hh3cHPEOCInTotalPkts_Type()
)
hh3cHPEOCInTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCInTotalPkts.setStatus("current")
_Hh3cHPEOCAvgOutPower_Type = Integer32
_Hh3cHPEOCAvgOutPower_Object = MibTableColumn
hh3cHPEOCAvgOutPower = _Hh3cHPEOCAvgOutPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 6),
    _Hh3cHPEOCAvgOutPower_Type()
)
hh3cHPEOCAvgOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCAvgOutPower.setStatus("current")
_Hh3cHPEOCAvgOutPBCRCErrors_Type = Unsigned32
_Hh3cHPEOCAvgOutPBCRCErrors_Object = MibTableColumn
hh3cHPEOCAvgOutPBCRCErrors = _Hh3cHPEOCAvgOutPBCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 7),
    _Hh3cHPEOCAvgOutPBCRCErrors_Type()
)
hh3cHPEOCAvgOutPBCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCAvgOutPBCRCErrors.setStatus("current")
_Hh3cHPEOCOutTotalPkts_Type = Counter64
_Hh3cHPEOCOutTotalPkts_Object = MibTableColumn
hh3cHPEOCOutTotalPkts = _Hh3cHPEOCOutTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 1, 1, 8),
    _Hh3cHPEOCOutTotalPkts_Type()
)
hh3cHPEOCOutTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCOutTotalPkts.setStatus("current")
_Hh3cHPEOCBitPerSymbolTable_Object = MibTable
hh3cHPEOCBitPerSymbolTable = _Hh3cHPEOCBitPerSymbolTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cHPEOCBitPerSymbolTable.setStatus("current")
_Hh3cHPEOCBitPerSymbolEntry_Object = MibTableRow
hh3cHPEOCBitPerSymbolEntry = _Hh3cHPEOCBitPerSymbolEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 2, 1)
)
hh3cHPEOCBitPerSymbolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-HPEOC-MIB", "hh3cHPEOCBitPerSymbolIndex"),
)
if mibBuilder.loadTexts:
    hh3cHPEOCBitPerSymbolEntry.setStatus("current")
_Hh3cHPEOCBitPerSymbolIndex_Type = Unsigned32
_Hh3cHPEOCBitPerSymbolIndex_Object = MibTableColumn
hh3cHPEOCBitPerSymbolIndex = _Hh3cHPEOCBitPerSymbolIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 2, 1, 1),
    _Hh3cHPEOCBitPerSymbolIndex_Type()
)
hh3cHPEOCBitPerSymbolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cHPEOCBitPerSymbolIndex.setStatus("current")
_Hh3cHPEOCBitPerSymbol_Type = OctetString
_Hh3cHPEOCBitPerSymbol_Object = MibTableColumn
hh3cHPEOCBitPerSymbol = _Hh3cHPEOCBitPerSymbol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 2, 2, 1, 2),
    _Hh3cHPEOCBitPerSymbol_Type()
)
hh3cHPEOCBitPerSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cHPEOCBitPerSymbol.setStatus("current")
_Hh3cHPEOCTemplate_ObjectIdentity = ObjectIdentity
hh3cHPEOCTemplate = _Hh3cHPEOCTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3)
)
_Hh3cHPEOCTemplateGlobalTable_Object = MibTable
hh3cHPEOCTemplateGlobalTable = _Hh3cHPEOCTemplateGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateGlobalTable.setStatus("current")
_Hh3cHPEOCTemplateGlobalEntry_Object = MibTableRow
hh3cHPEOCTemplateGlobalEntry = _Hh3cHPEOCTemplateGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 1, 1)
)
hh3cHPEOCTemplateGlobalEntry.setIndexNames(
    (0, "HH3C-HPEOC-MIB", "hh3cHPEOCTemplateIndex"),
)
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateGlobalEntry.setStatus("current")
_Hh3cHPEOCTemplateIndex_Type = Integer32
_Hh3cHPEOCTemplateIndex_Object = MibTableColumn
hh3cHPEOCTemplateIndex = _Hh3cHPEOCTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 1, 1, 1),
    _Hh3cHPEOCTemplateIndex_Type()
)
hh3cHPEOCTemplateIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateIndex.setStatus("current")


class _Hh3cHPEOCTemplateType_Type(Integer32):
    """Custom type hh3cHPEOCTemplateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch", 1),
          ("gateway", 2))
    )


_Hh3cHPEOCTemplateType_Type.__name__ = "Integer32"
_Hh3cHPEOCTemplateType_Object = MibTableColumn
hh3cHPEOCTemplateType = _Hh3cHPEOCTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 1, 1, 2),
    _Hh3cHPEOCTemplateType_Type()
)
hh3cHPEOCTemplateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateType.setStatus("current")
_Hh3cHPEOCTemplateName_Type = DisplayString
_Hh3cHPEOCTemplateName_Object = MibTableColumn
hh3cHPEOCTemplateName = _Hh3cHPEOCTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 1, 1, 3),
    _Hh3cHPEOCTemplateName_Type()
)
hh3cHPEOCTemplateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateName.setStatus("current")
_Hh3cHPEOCTemplateDescr_Type = DisplayString
_Hh3cHPEOCTemplateDescr_Object = MibTableColumn
hh3cHPEOCTemplateDescr = _Hh3cHPEOCTemplateDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 1, 1, 4),
    _Hh3cHPEOCTemplateDescr_Type()
)
hh3cHPEOCTemplateDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateDescr.setStatus("current")
_Hh3cHPEOCTemplateCnuMaxDownBW_Type = Integer32
_Hh3cHPEOCTemplateCnuMaxDownBW_Object = MibTableColumn
hh3cHPEOCTemplateCnuMaxDownBW = _Hh3cHPEOCTemplateCnuMaxDownBW_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 1, 1, 5),
    _Hh3cHPEOCTemplateCnuMaxDownBW_Type()
)
hh3cHPEOCTemplateCnuMaxDownBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateCnuMaxDownBW.setStatus("current")
_Hh3cHPEOCTemplateCnuMaxUpBW_Type = Integer32
_Hh3cHPEOCTemplateCnuMaxUpBW_Object = MibTableColumn
hh3cHPEOCTemplateCnuMaxUpBW = _Hh3cHPEOCTemplateCnuMaxUpBW_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 1, 1, 6),
    _Hh3cHPEOCTemplateCnuMaxUpBW_Type()
)
hh3cHPEOCTemplateCnuMaxUpBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateCnuMaxUpBW.setStatus("current")
_Hh3cHPEOCTemplateCnuBcastControl_Type = TruthValue
_Hh3cHPEOCTemplateCnuBcastControl_Object = MibTableColumn
hh3cHPEOCTemplateCnuBcastControl = _Hh3cHPEOCTemplateCnuBcastControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 1, 1, 7),
    _Hh3cHPEOCTemplateCnuBcastControl_Type()
)
hh3cHPEOCTemplateCnuBcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateCnuBcastControl.setStatus("current")
_Hh3cHPEOCTemplateCnuMacLimit_Type = Unsigned32
_Hh3cHPEOCTemplateCnuMacLimit_Object = MibTableColumn
hh3cHPEOCTemplateCnuMacLimit = _Hh3cHPEOCTemplateCnuMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 1, 1, 8),
    _Hh3cHPEOCTemplateCnuMacLimit_Type()
)
hh3cHPEOCTemplateCnuMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateCnuMacLimit.setStatus("current")
_Hh3cHPEOCTemplateCb201VlanEn_Type = TruthValue
_Hh3cHPEOCTemplateCb201VlanEn_Object = MibTableColumn
hh3cHPEOCTemplateCb201VlanEn = _Hh3cHPEOCTemplateCb201VlanEn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 1, 1, 9),
    _Hh3cHPEOCTemplateCb201VlanEn_Type()
)
hh3cHPEOCTemplateCb201VlanEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateCb201VlanEn.setStatus("current")
_Hh3cHPEOCTemplateRowStatus_Type = RowStatus
_Hh3cHPEOCTemplateRowStatus_Object = MibTableColumn
hh3cHPEOCTemplateRowStatus = _Hh3cHPEOCTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 1, 1, 10),
    _Hh3cHPEOCTemplateRowStatus_Type()
)
hh3cHPEOCTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateRowStatus.setStatus("current")
_Hh3cHPEOCTemplateSwitchTable_Object = MibTable
hh3cHPEOCTemplateSwitchTable = _Hh3cHPEOCTemplateSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateSwitchTable.setStatus("current")
_Hh3cHPEOCTemplateSwitchEntry_Object = MibTableRow
hh3cHPEOCTemplateSwitchEntry = _Hh3cHPEOCTemplateSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 2, 1)
)
hh3cHPEOCTemplateSwitchEntry.setIndexNames(
    (0, "HH3C-HPEOC-MIB", "hh3cHPEOCTemplateIndex"),
    (0, "HH3C-HPEOC-MIB", "hh3cHPEOCTemplateUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateSwitchEntry.setStatus("current")
_Hh3cHPEOCTemplateUniIndex_Type = Integer32
_Hh3cHPEOCTemplateUniIndex_Object = MibTableColumn
hh3cHPEOCTemplateUniIndex = _Hh3cHPEOCTemplateUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 2, 1, 1),
    _Hh3cHPEOCTemplateUniIndex_Type()
)
hh3cHPEOCTemplateUniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateUniIndex.setStatus("current")


class _Hh3cHPEOCTemplateUniSpeed_Type(Integer32):
    """Custom type hh3cHPEOCTemplateUniSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("s10M", 10),
          ("s100M", 100))
    )


_Hh3cHPEOCTemplateUniSpeed_Type.__name__ = "Integer32"
_Hh3cHPEOCTemplateUniSpeed_Object = MibTableColumn
hh3cHPEOCTemplateUniSpeed = _Hh3cHPEOCTemplateUniSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 2, 1, 2),
    _Hh3cHPEOCTemplateUniSpeed_Type()
)
hh3cHPEOCTemplateUniSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateUniSpeed.setStatus("current")


class _Hh3cHPEOCTemplateUniDuplex_Type(Integer32):
    """Custom type hh3cHPEOCTemplateUniDuplex based on Integer32"""
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


_Hh3cHPEOCTemplateUniDuplex_Type.__name__ = "Integer32"
_Hh3cHPEOCTemplateUniDuplex_Object = MibTableColumn
hh3cHPEOCTemplateUniDuplex = _Hh3cHPEOCTemplateUniDuplex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 2, 1, 3),
    _Hh3cHPEOCTemplateUniDuplex_Type()
)
hh3cHPEOCTemplateUniDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateUniDuplex.setStatus("current")


class _Hh3cHPEOCTemplateUniPriority_Type(Integer32):
    """Custom type hh3cHPEOCTemplateUniPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cHPEOCTemplateUniPriority_Type.__name__ = "Integer32"
_Hh3cHPEOCTemplateUniPriority_Object = MibTableColumn
hh3cHPEOCTemplateUniPriority = _Hh3cHPEOCTemplateUniPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 2, 1, 4),
    _Hh3cHPEOCTemplateUniPriority_Type()
)
hh3cHPEOCTemplateUniPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateUniPriority.setStatus("current")


class _Hh3cHPEOCTemplateUniFlowControl_Type(TruthValue):
    """Custom type hh3cHPEOCTemplateUniFlowControl based on TruthValue"""
    defaultValue = 2


_Hh3cHPEOCTemplateUniFlowControl_Type.__name__ = "TruthValue"
_Hh3cHPEOCTemplateUniFlowControl_Object = MibTableColumn
hh3cHPEOCTemplateUniFlowControl = _Hh3cHPEOCTemplateUniFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 2, 1, 5),
    _Hh3cHPEOCTemplateUniFlowControl_Type()
)
hh3cHPEOCTemplateUniFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateUniFlowControl.setStatus("current")
_Hh3cHPEOCTemplateUniUpLineRate_Type = Unsigned32
_Hh3cHPEOCTemplateUniUpLineRate_Object = MibTableColumn
hh3cHPEOCTemplateUniUpLineRate = _Hh3cHPEOCTemplateUniUpLineRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 2, 1, 6),
    _Hh3cHPEOCTemplateUniUpLineRate_Type()
)
hh3cHPEOCTemplateUniUpLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateUniUpLineRate.setStatus("current")
_Hh3cHPEOCTemplateUniDownLineRate_Type = Unsigned32
_Hh3cHPEOCTemplateUniDownLineRate_Object = MibTableColumn
hh3cHPEOCTemplateUniDownLineRate = _Hh3cHPEOCTemplateUniDownLineRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 2, 1, 7),
    _Hh3cHPEOCTemplateUniDownLineRate_Type()
)
hh3cHPEOCTemplateUniDownLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateUniDownLineRate.setStatus("current")


class _Hh3cHPEOCTemplateUniAdminStatus_Type(Integer32):
    """Custom type hh3cHPEOCTemplateUniAdminStatus based on Integer32"""
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


_Hh3cHPEOCTemplateUniAdminStatus_Type.__name__ = "Integer32"
_Hh3cHPEOCTemplateUniAdminStatus_Object = MibTableColumn
hh3cHPEOCTemplateUniAdminStatus = _Hh3cHPEOCTemplateUniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 2, 1, 8),
    _Hh3cHPEOCTemplateUniAdminStatus_Type()
)
hh3cHPEOCTemplateUniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateUniAdminStatus.setStatus("current")


class _Hh3cHPEOCTemplateUniVLANType_Type(Integer32):
    """Custom type hh3cHPEOCTemplateUniVLANType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("trunk", 2),
          ("hybrid", 3))
    )


_Hh3cHPEOCTemplateUniVLANType_Type.__name__ = "Integer32"
_Hh3cHPEOCTemplateUniVLANType_Object = MibTableColumn
hh3cHPEOCTemplateUniVLANType = _Hh3cHPEOCTemplateUniVLANType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 2, 1, 9),
    _Hh3cHPEOCTemplateUniVLANType_Type()
)
hh3cHPEOCTemplateUniVLANType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateUniVLANType.setStatus("current")


class _Hh3cHPEOCTemplateUniPvid_Type(Integer32):
    """Custom type hh3cHPEOCTemplateUniPvid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cHPEOCTemplateUniPvid_Type.__name__ = "Integer32"
_Hh3cHPEOCTemplateUniPvid_Object = MibTableColumn
hh3cHPEOCTemplateUniPvid = _Hh3cHPEOCTemplateUniPvid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 2, 1, 10),
    _Hh3cHPEOCTemplateUniPvid_Type()
)
hh3cHPEOCTemplateUniPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateUniPvid.setStatus("current")


class _Hh3cHPEOCTemplateUniVlanTag_Type(Integer32):
    """Custom type hh3cHPEOCTemplateUniVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_Hh3cHPEOCTemplateUniVlanTag_Type.__name__ = "Integer32"
_Hh3cHPEOCTemplateUniVlanTag_Object = MibTableColumn
hh3cHPEOCTemplateUniVlanTag = _Hh3cHPEOCTemplateUniVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 3, 2, 1, 11),
    _Hh3cHPEOCTemplateUniVlanTag_Type()
)
hh3cHPEOCTemplateUniVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCTemplateUniVlanTag.setStatus("current")
_Hh3cHPEOCCnuAccess_ObjectIdentity = ObjectIdentity
hh3cHPEOCCnuAccess = _Hh3cHPEOCCnuAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 4)
)
_Hh3cHPEOCCnuAccessTable_Object = MibTable
hh3cHPEOCCnuAccessTable = _Hh3cHPEOCCnuAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cHPEOCCnuAccessTable.setStatus("current")
_Hh3cHPEOCCnuAccessEntry_Object = MibTableRow
hh3cHPEOCCnuAccessEntry = _Hh3cHPEOCCnuAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 4, 1, 1)
)
hh3cHPEOCCnuAccessEntry.setIndexNames(
    (0, "HH3C-HPEOC-MIB", "hh3cHPEOCCnuAccessIndex"),
)
if mibBuilder.loadTexts:
    hh3cHPEOCCnuAccessEntry.setStatus("current")
_Hh3cHPEOCCnuAccessIndex_Type = Integer32
_Hh3cHPEOCCnuAccessIndex_Object = MibTableColumn
hh3cHPEOCCnuAccessIndex = _Hh3cHPEOCCnuAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 4, 1, 1, 1),
    _Hh3cHPEOCCnuAccessIndex_Type()
)
hh3cHPEOCCnuAccessIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cHPEOCCnuAccessIndex.setStatus("current")
_Hh3cHPEOCCnuHFID_Type = DisplayString
_Hh3cHPEOCCnuHFID_Object = MibTableColumn
hh3cHPEOCCnuHFID = _Hh3cHPEOCCnuHFID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 4, 1, 1, 2),
    _Hh3cHPEOCCnuHFID_Type()
)
hh3cHPEOCCnuHFID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCnuHFID.setStatus("current")
_Hh3cHPEOCManuInfo_Type = DisplayString
_Hh3cHPEOCManuInfo_Object = MibTableColumn
hh3cHPEOCManuInfo = _Hh3cHPEOCManuInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 4, 1, 1, 3),
    _Hh3cHPEOCManuInfo_Type()
)
hh3cHPEOCManuInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCManuInfo.setStatus("current")


class _Hh3cHPEOCCnuType_Type(Integer32):
    """Custom type hh3cHPEOCCnuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch", 1),
          ("gateway", 2))
    )


_Hh3cHPEOCCnuType_Type.__name__ = "Integer32"
_Hh3cHPEOCCnuType_Object = MibTableColumn
hh3cHPEOCCnuType = _Hh3cHPEOCCnuType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 4, 1, 1, 4),
    _Hh3cHPEOCCnuType_Type()
)
hh3cHPEOCCnuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCnuType.setStatus("current")


class _Hh3cHPEOCCnuSwitchType_Type(Integer32):
    """Custom type hh3cHPEOCCnuSwitchType based on Integer32"""
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
        *(("rtl8306e", 1),
          ("ar8236", 2),
          ("mv6061", 3),
          ("mv6031", 4))
    )


_Hh3cHPEOCCnuSwitchType_Type.__name__ = "Integer32"
_Hh3cHPEOCCnuSwitchType_Object = MibTableColumn
hh3cHPEOCCnuSwitchType = _Hh3cHPEOCCnuSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 4, 1, 1, 5),
    _Hh3cHPEOCCnuSwitchType_Type()
)
hh3cHPEOCCnuSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCnuSwitchType.setStatus("current")
_Hh3cHPEOCCnuUniNum_Type = Integer32
_Hh3cHPEOCCnuUniNum_Object = MibTableColumn
hh3cHPEOCCnuUniNum = _Hh3cHPEOCCnuUniNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 4, 1, 1, 6),
    _Hh3cHPEOCCnuUniNum_Type()
)
hh3cHPEOCCnuUniNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCnuUniNum.setStatus("current")
_Hh3cHPEOCCnuPhy2Uni_Type = OctetString
_Hh3cHPEOCCnuPhy2Uni_Object = MibTableColumn
hh3cHPEOCCnuPhy2Uni = _Hh3cHPEOCCnuPhy2Uni_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 4, 1, 1, 7),
    _Hh3cHPEOCCnuPhy2Uni_Type()
)
hh3cHPEOCCnuPhy2Uni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cHPEOCCnuPhy2Uni.setStatus("current")
_Hh3cHPEOCCnuAccessRowStatus_Type = RowStatus
_Hh3cHPEOCCnuAccessRowStatus_Object = MibTableColumn
hh3cHPEOCCnuAccessRowStatus = _Hh3cHPEOCCnuAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 84, 4, 1, 1, 8),
    _Hh3cHPEOCCnuAccessRowStatus_Type()
)
hh3cHPEOCCnuAccessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cHPEOCCnuAccessRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-HPEOC-MIB",
    **{"hh3cHPEOC": hh3cHPEOC,
       "hh3cHPEOCSystem": hh3cHPEOCSystem,
       "hh3cHPEOCCltVlanType": hh3cHPEOCCltVlanType,
       "hh3cHPEOCCltVlanManTable": hh3cHPEOCCltVlanManTable,
       "hh3cHPEOCCltVlanManEntry": hh3cHPEOCCltVlanManEntry,
       "hh3cHPEOCCltEthPortType": hh3cHPEOCCltEthPortType,
       "hh3cHPEOCCltSysManTable": hh3cHPEOCCltSysManTable,
       "hh3cHPEOCCltSysManEntry": hh3cHPEOCCltSysManEntry,
       "hh3cHPEOCCltDescr": hh3cHPEOCCltDescr,
       "hh3cHPEOCCltFwVersion": hh3cHPEOCCltFwVersion,
       "hh3cHPEOCCltLinkState": hh3cHPEOCCltLinkState,
       "hh3cHPEOCCnuSysManTable": hh3cHPEOCCnuSysManTable,
       "hh3cHPEOCCnuSysManEntry": hh3cHPEOCCnuSysManEntry,
       "hh3cHPEOCCnuBcastControl": hh3cHPEOCCnuBcastControl,
       "hh3cHPEOCCnuAnonymStatus": hh3cHPEOCCnuAnonymStatus,
       "hh3cHPEOCCnuMacLimit": hh3cHPEOCCnuMacLimit,
       "hh3cHPEOCCltAutoUpgrade": hh3cHPEOCCltAutoUpgrade,
       "hh3cHPEOCOnLineCnuNumber": hh3cHPEOCOnLineCnuNumber,
       "hh3cHPEOCCpuMacAddress": hh3cHPEOCCpuMacAddress,
       "hh3cHPEOCOffLineCnuNumber": hh3cHPEOCOffLineCnuNumber,
       "hh3cHPEOCDownLoadCNUFWResult": hh3cHPEOCDownLoadCNUFWResult,
       "hh3cHPEOCCltAutoUpgradeType": hh3cHPEOCCltAutoUpgradeType,
       "hh3cHPEOCAutoUpObjects": hh3cHPEOCAutoUpObjects,
       "hh3cHPEOCServerAddress": hh3cHPEOCServerAddress,
       "hh3cHPEOCServerUser": hh3cHPEOCServerUser,
       "hh3cHPEOCServerPassword": hh3cHPEOCServerPassword,
       "hh3cHPEOCCltLoopbackDetect": hh3cHPEOCCltLoopbackDetect,
       "hh3cHPEOCTemplateEnable": hh3cHPEOCTemplateEnable,
       "hh3cHPEOCCableInfo": hh3cHPEOCCableInfo,
       "hh3cHPEOCCableInfoTable": hh3cHPEOCCableInfoTable,
       "hh3cHPEOCCableInfoEntry": hh3cHPEOCCableInfoEntry,
       "hh3cHPEOCFECErrors": hh3cHPEOCFECErrors,
       "hh3cHPEOCAvgBitsPerCarrier": hh3cHPEOCAvgBitsPerCarrier,
       "hh3cHPEOCAvgSNRPerCarrier": hh3cHPEOCAvgSNRPerCarrier,
       "hh3cHPEOCAvgInPBCRCErrors": hh3cHPEOCAvgInPBCRCErrors,
       "hh3cHPEOCInTotalPkts": hh3cHPEOCInTotalPkts,
       "hh3cHPEOCAvgOutPower": hh3cHPEOCAvgOutPower,
       "hh3cHPEOCAvgOutPBCRCErrors": hh3cHPEOCAvgOutPBCRCErrors,
       "hh3cHPEOCOutTotalPkts": hh3cHPEOCOutTotalPkts,
       "hh3cHPEOCBitPerSymbolTable": hh3cHPEOCBitPerSymbolTable,
       "hh3cHPEOCBitPerSymbolEntry": hh3cHPEOCBitPerSymbolEntry,
       "hh3cHPEOCBitPerSymbolIndex": hh3cHPEOCBitPerSymbolIndex,
       "hh3cHPEOCBitPerSymbol": hh3cHPEOCBitPerSymbol,
       "hh3cHPEOCTemplate": hh3cHPEOCTemplate,
       "hh3cHPEOCTemplateGlobalTable": hh3cHPEOCTemplateGlobalTable,
       "hh3cHPEOCTemplateGlobalEntry": hh3cHPEOCTemplateGlobalEntry,
       "hh3cHPEOCTemplateIndex": hh3cHPEOCTemplateIndex,
       "hh3cHPEOCTemplateType": hh3cHPEOCTemplateType,
       "hh3cHPEOCTemplateName": hh3cHPEOCTemplateName,
       "hh3cHPEOCTemplateDescr": hh3cHPEOCTemplateDescr,
       "hh3cHPEOCTemplateCnuMaxDownBW": hh3cHPEOCTemplateCnuMaxDownBW,
       "hh3cHPEOCTemplateCnuMaxUpBW": hh3cHPEOCTemplateCnuMaxUpBW,
       "hh3cHPEOCTemplateCnuBcastControl": hh3cHPEOCTemplateCnuBcastControl,
       "hh3cHPEOCTemplateCnuMacLimit": hh3cHPEOCTemplateCnuMacLimit,
       "hh3cHPEOCTemplateCb201VlanEn": hh3cHPEOCTemplateCb201VlanEn,
       "hh3cHPEOCTemplateRowStatus": hh3cHPEOCTemplateRowStatus,
       "hh3cHPEOCTemplateSwitchTable": hh3cHPEOCTemplateSwitchTable,
       "hh3cHPEOCTemplateSwitchEntry": hh3cHPEOCTemplateSwitchEntry,
       "hh3cHPEOCTemplateUniIndex": hh3cHPEOCTemplateUniIndex,
       "hh3cHPEOCTemplateUniSpeed": hh3cHPEOCTemplateUniSpeed,
       "hh3cHPEOCTemplateUniDuplex": hh3cHPEOCTemplateUniDuplex,
       "hh3cHPEOCTemplateUniPriority": hh3cHPEOCTemplateUniPriority,
       "hh3cHPEOCTemplateUniFlowControl": hh3cHPEOCTemplateUniFlowControl,
       "hh3cHPEOCTemplateUniUpLineRate": hh3cHPEOCTemplateUniUpLineRate,
       "hh3cHPEOCTemplateUniDownLineRate": hh3cHPEOCTemplateUniDownLineRate,
       "hh3cHPEOCTemplateUniAdminStatus": hh3cHPEOCTemplateUniAdminStatus,
       "hh3cHPEOCTemplateUniVLANType": hh3cHPEOCTemplateUniVLANType,
       "hh3cHPEOCTemplateUniPvid": hh3cHPEOCTemplateUniPvid,
       "hh3cHPEOCTemplateUniVlanTag": hh3cHPEOCTemplateUniVlanTag,
       "hh3cHPEOCCnuAccess": hh3cHPEOCCnuAccess,
       "hh3cHPEOCCnuAccessTable": hh3cHPEOCCnuAccessTable,
       "hh3cHPEOCCnuAccessEntry": hh3cHPEOCCnuAccessEntry,
       "hh3cHPEOCCnuAccessIndex": hh3cHPEOCCnuAccessIndex,
       "hh3cHPEOCCnuHFID": hh3cHPEOCCnuHFID,
       "hh3cHPEOCManuInfo": hh3cHPEOCManuInfo,
       "hh3cHPEOCCnuType": hh3cHPEOCCnuType,
       "hh3cHPEOCCnuSwitchType": hh3cHPEOCCnuSwitchType,
       "hh3cHPEOCCnuUniNum": hh3cHPEOCCnuUniNum,
       "hh3cHPEOCCnuPhy2Uni": hh3cHPEOCCnuPhy2Uni,
       "hh3cHPEOCCnuAccessRowStatus": hh3cHPEOCCnuAccessRowStatus}
)
