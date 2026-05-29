# SNMP MIB module (PRVT-SYS-MON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-SYS-MON-MIB

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

(prvt_products,
 reportsIfJackIndex,
 reportsL2IfacePort,
 reportsL2IfaceSlot,
 reportsL2IfaceUnit) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "prvt-products",
    "reportsIfJackIndex",
    "reportsL2IfacePort",
    "reportsL2IfaceSlot",
    "reportsL2IfaceUnit")

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

prvtSysMonMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3)
)
if mibBuilder.loadTexts:
    prvtSysMonMib.setRevisions(
        ("2007-12-27 00:00",
         "2005-02-16 00:00",
         "2003-11-18 00:00",
         "2003-05-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnableStatus(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111)
)
_PrvtSysMonNotifications_ObjectIdentity = ObjectIdentity
prvtSysMonNotifications = _PrvtSysMonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0)
)
_PrvtSysMonObjects_ObjectIdentity = ObjectIdentity
prvtSysMonObjects = _PrvtSysMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1)
)
_SysMonThreshold_ObjectIdentity = ObjectIdentity
sysMonThreshold = _SysMonThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1)
)
_CpuUtilizationThreshold_Type = Integer32
_CpuUtilizationThreshold_Object = MibScalar
cpuUtilizationThreshold = _CpuUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 1),
    _CpuUtilizationThreshold_Type()
)
cpuUtilizationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilizationThreshold.setStatus("current")
_RamBytesFreeThreshold_Type = Integer32
_RamBytesFreeThreshold_Object = MibScalar
ramBytesFreeThreshold = _RamBytesFreeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 2),
    _RamBytesFreeThreshold_Type()
)
ramBytesFreeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ramBytesFreeThreshold.setStatus("current")
_PortErrorsThreshold_Type = Integer32
_PortErrorsThreshold_Object = MibScalar
portErrorsThreshold = _PortErrorsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 3),
    _PortErrorsThreshold_Type()
)
portErrorsThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portErrorsThreshold.setStatus("current")
_PortsBroadcastThreshold_Type = Integer32
_PortsBroadcastThreshold_Object = MibScalar
portsBroadcastThreshold = _PortsBroadcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 4),
    _PortsBroadcastThreshold_Type()
)
portsBroadcastThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsBroadcastThreshold.setStatus("current")
_PortsCRCErrThreshold_Type = Integer32
_PortsCRCErrThreshold_Object = MibScalar
portsCRCErrThreshold = _PortsCRCErrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 5),
    _PortsCRCErrThreshold_Type()
)
portsCRCErrThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsCRCErrThreshold.setStatus("current")
_PortsRuntsThreshold_Type = Integer32
_PortsRuntsThreshold_Object = MibScalar
portsRuntsThreshold = _PortsRuntsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 6),
    _PortsRuntsThreshold_Type()
)
portsRuntsThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsRuntsThreshold.setStatus("current")
_PortsOverSizeThreshold_Type = Integer32
_PortsOverSizeThreshold_Object = MibScalar
portsOverSizeThreshold = _PortsOverSizeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 7),
    _PortsOverSizeThreshold_Type()
)
portsOverSizeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsOverSizeThreshold.setStatus("current")
_LaserPortThresholdTable_Object = MibTable
laserPortThresholdTable = _LaserPortThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    laserPortThresholdTable.setStatus("current")
_LaserPortThresholdEntry_Object = MibTableRow
laserPortThresholdEntry = _LaserPortThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1)
)
laserPortThresholdEntry.setIndexNames(
    (0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"),
    (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"),
    (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"),
    (0, "PRVT-SWITCH-MIB", "reportsIfJackIndex"),
)
if mibBuilder.loadTexts:
    laserPortThresholdEntry.setStatus("current")
_LaserTemperatureHighThreshold_Type = Integer32
_LaserTemperatureHighThreshold_Object = MibTableColumn
laserTemperatureHighThreshold = _LaserTemperatureHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 1),
    _LaserTemperatureHighThreshold_Type()
)
laserTemperatureHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laserTemperatureHighThreshold.setStatus("current")
_LaserTemperatureLowThreshold_Type = Integer32
_LaserTemperatureLowThreshold_Object = MibTableColumn
laserTemperatureLowThreshold = _LaserTemperatureLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 2),
    _LaserTemperatureLowThreshold_Type()
)
laserTemperatureLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laserTemperatureLowThreshold.setStatus("current")
_LaserTxPowerHighThreshold_Type = Integer32
_LaserTxPowerHighThreshold_Object = MibTableColumn
laserTxPowerHighThreshold = _LaserTxPowerHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 3),
    _LaserTxPowerHighThreshold_Type()
)
laserTxPowerHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laserTxPowerHighThreshold.setStatus("current")
_LaserTxPowerLowThreshold_Type = Integer32
_LaserTxPowerLowThreshold_Object = MibTableColumn
laserTxPowerLowThreshold = _LaserTxPowerLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 4),
    _LaserTxPowerLowThreshold_Type()
)
laserTxPowerLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laserTxPowerLowThreshold.setStatus("current")
_LaserRxPowerHighThreshold_Type = Integer32
_LaserRxPowerHighThreshold_Object = MibTableColumn
laserRxPowerHighThreshold = _LaserRxPowerHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 5),
    _LaserRxPowerHighThreshold_Type()
)
laserRxPowerHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laserRxPowerHighThreshold.setStatus("current")
_LaserRxPowerLowThreshold_Type = Integer32
_LaserRxPowerLowThreshold_Object = MibTableColumn
laserRxPowerLowThreshold = _LaserRxPowerLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 1, 8, 1, 6),
    _LaserRxPowerLowThreshold_Type()
)
laserRxPowerLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laserRxPowerLowThreshold.setStatus("current")
_SysMonValues_ObjectIdentity = ObjectIdentity
sysMonValues = _SysMonValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2)
)
_MonCpuUtilization_Type = Integer32
_MonCpuUtilization_Object = MibScalar
monCpuUtilization = _MonCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 1),
    _MonCpuUtilization_Type()
)
monCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monCpuUtilization.setStatus("current")
_MonRamBytesFree_Type = Integer32
_MonRamBytesFree_Object = MibScalar
monRamBytesFree = _MonRamBytesFree_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 2),
    _MonRamBytesFree_Type()
)
monRamBytesFree.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    monRamBytesFree.setStatus("current")
_MonPortsTable_Object = MibTable
monPortsTable = _MonPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    monPortsTable.setStatus("current")
_MonPortsEntry_Object = MibTableRow
monPortsEntry = _MonPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1)
)
monPortsEntry.setIndexNames(
    (0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"),
    (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"),
    (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"),
)
if mibBuilder.loadTexts:
    monPortsEntry.setStatus("current")
_MonPortErrors_Type = Integer32
_MonPortErrors_Object = MibTableColumn
monPortErrors = _MonPortErrors_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 1),
    _MonPortErrors_Type()
)
monPortErrors.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    monPortErrors.setStatus("current")
_MonPortBroadcast_Type = Integer32
_MonPortBroadcast_Object = MibTableColumn
monPortBroadcast = _MonPortBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 2),
    _MonPortBroadcast_Type()
)
monPortBroadcast.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    monPortBroadcast.setStatus("current")
_MonPortCRCErr_Type = Integer32
_MonPortCRCErr_Object = MibTableColumn
monPortCRCErr = _MonPortCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 3),
    _MonPortCRCErr_Type()
)
monPortCRCErr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    monPortCRCErr.setStatus("current")
_MonPortRunts_Type = Integer32
_MonPortRunts_Object = MibTableColumn
monPortRunts = _MonPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 4),
    _MonPortRunts_Type()
)
monPortRunts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    monPortRunts.setStatus("current")
_MonPortOverSize_Type = Integer32
_MonPortOverSize_Object = MibTableColumn
monPortOverSize = _MonPortOverSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 3, 1, 5),
    _MonPortOverSize_Type()
)
monPortOverSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    monPortOverSize.setStatus("current")
_LaserPortValueTable_Object = MibTable
laserPortValueTable = _LaserPortValueTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    laserPortValueTable.setStatus("current")
_LaserPortValueEntry_Object = MibTableRow
laserPortValueEntry = _LaserPortValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1)
)
laserPortValueEntry.setIndexNames(
    (0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"),
    (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"),
    (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"),
    (0, "PRVT-SWITCH-MIB", "reportsIfJackIndex"),
)
if mibBuilder.loadTexts:
    laserPortValueEntry.setStatus("current")


class _SfpStatus_Type(Integer32):
    """Custom type sfpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lm-supported", 1),
          ("lm-not-supported", 2),
          ("extracted", 3))
    )


_SfpStatus_Type.__name__ = "Integer32"
_SfpStatus_Object = MibTableColumn
sfpStatus = _SfpStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1, 1),
    _SfpStatus_Type()
)
sfpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpStatus.setStatus("current")
_LaserTemperature_Type = Integer32
_LaserTemperature_Object = MibTableColumn
laserTemperature = _LaserTemperature_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1, 2),
    _LaserTemperature_Type()
)
laserTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laserTemperature.setStatus("current")
_LaserTxPower_Type = Integer32
_LaserTxPower_Object = MibTableColumn
laserTxPower = _LaserTxPower_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1, 3),
    _LaserTxPower_Type()
)
laserTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laserTxPower.setStatus("current")
_LaserRxPower_Type = Integer32
_LaserRxPower_Object = MibTableColumn
laserRxPower = _LaserRxPower_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 4, 1, 4),
    _LaserRxPower_Type()
)
laserRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laserRxPower.setStatus("current")
_SfpPortManTable_Object = MibTable
sfpPortManTable = _SfpPortManTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5)
)
if mibBuilder.loadTexts:
    sfpPortManTable.setStatus("current")
_SfpPortManEntry_Object = MibTableRow
sfpPortManEntry = _SfpPortManEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1)
)
sfpPortManEntry.setIndexNames(
    (0, "PRVT-SWITCH-MIB", "reportsL2IfaceUnit"),
    (0, "PRVT-SWITCH-MIB", "reportsL2IfaceSlot"),
    (0, "PRVT-SWITCH-MIB", "reportsL2IfacePort"),
    (0, "PRVT-SWITCH-MIB", "reportsIfJackIndex"),
)
if mibBuilder.loadTexts:
    sfpPortManEntry.setStatus("current")


class _SfpMonStatus_Type(Integer32):
    """Custom type sfpMonStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sfpInserted", 1),
          ("sfpExtracted", 2),
          ("sfpUnknown", 3))
    )


_SfpMonStatus_Type.__name__ = "Integer32"
_SfpMonStatus_Object = MibTableColumn
sfpMonStatus = _SfpMonStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 1),
    _SfpMonStatus_Type()
)
sfpMonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpMonStatus.setStatus("current")


class _SfpVendor_Type(DisplayString):
    """Custom type sfpVendor based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_SfpVendor_Type.__name__ = "DisplayString"
_SfpVendor_Object = MibTableColumn
sfpVendor = _SfpVendor_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 2),
    _SfpVendor_Type()
)
sfpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendor.setStatus("current")


class _SfpPN_Type(DisplayString):
    """Custom type sfpPN based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_SfpPN_Type.__name__ = "DisplayString"
_SfpPN_Object = MibTableColumn
sfpPN = _SfpPN_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 3),
    _SfpPN_Type()
)
sfpPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpPN.setStatus("current")


class _SfpRevision_Type(DisplayString):
    """Custom type sfpRevision based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_SfpRevision_Type.__name__ = "DisplayString"
_SfpRevision_Object = MibTableColumn
sfpRevision = _SfpRevision_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 4),
    _SfpRevision_Type()
)
sfpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRevision.setStatus("current")


class _SfpLenght_Type(DisplayString):
    """Custom type sfpLenght based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_SfpLenght_Type.__name__ = "DisplayString"
_SfpLenght_Object = MibTableColumn
sfpLenght = _SfpLenght_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 5),
    _SfpLenght_Type()
)
sfpLenght.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLenght.setStatus("current")


class _SfpConnector_Type(DisplayString):
    """Custom type sfpConnector based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_SfpConnector_Type.__name__ = "DisplayString"
_SfpConnector_Object = MibTableColumn
sfpConnector = _SfpConnector_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 2, 5, 1, 6),
    _SfpConnector_Type()
)
sfpConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConnector.setStatus("current")
_SysMonConfig_ObjectIdentity = ObjectIdentity
sysMonConfig = _SysMonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3)
)
_SysMonConfigTable_Object = MibTable
sysMonConfigTable = _SysMonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sysMonConfigTable.setStatus("current")
_SysMonConfigEntry_Object = MibTableRow
sysMonConfigEntry = _SysMonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1)
)
sysMonConfigEntry.setIndexNames(
    (0, "PRVT-SYS-MON-MIB", "sysMonIndicator"),
)
if mibBuilder.loadTexts:
    sysMonConfigEntry.setStatus("current")


class _SysMonIndicator_Type(Integer32):
    """Custom type sysMonIndicator based on Integer32"""
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
        *(("cpu-usage", 1),
          ("ram-usage", 2),
          ("power-supply", 3),
          ("onboard-power", 4),
          ("fan", 5),
          ("temperature", 6),
          ("laser", 7))
    )


_SysMonIndicator_Type.__name__ = "Integer32"
_SysMonIndicator_Object = MibTableColumn
sysMonIndicator = _SysMonIndicator_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 1),
    _SysMonIndicator_Type()
)
sysMonIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMonIndicator.setStatus("current")
_SysMonEnable_Type = EnableStatus
_SysMonEnable_Object = MibTableColumn
sysMonEnable = _SysMonEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 2),
    _SysMonEnable_Type()
)
sysMonEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMonEnable.setStatus("current")
_SysMonPeriod_Type = Integer32
_SysMonPeriod_Object = MibTableColumn
sysMonPeriod = _SysMonPeriod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 3),
    _SysMonPeriod_Type()
)
sysMonPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMonPeriod.setStatus("current")
_SysMonTrap_Type = EnableStatus
_SysMonTrap_Object = MibTableColumn
sysMonTrap = _SysMonTrap_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 4),
    _SysMonTrap_Type()
)
sysMonTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMonTrap.setStatus("current")
_SysMonLog_Type = EnableStatus
_SysMonLog_Object = MibTableColumn
sysMonLog = _SysMonLog_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 5),
    _SysMonLog_Type()
)
sysMonLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMonLog.setStatus("current")
_SysMonLed_Type = EnableStatus
_SysMonLed_Object = MibTableColumn
sysMonLed = _SysMonLed_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 6),
    _SysMonLed_Type()
)
sysMonLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMonLed.setStatus("current")


class _SysMonDefaults_Type(Integer32):
    """Custom type sysMonDefaults based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noop", 0),
          ("reset", 1))
    )


_SysMonDefaults_Type.__name__ = "Integer32"
_SysMonDefaults_Object = MibTableColumn
sysMonDefaults = _SysMonDefaults_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 1, 3, 1, 1, 7),
    _SysMonDefaults_Type()
)
sysMonDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMonDefaults.setStatus("current")
_PrvtSysMonConformance_ObjectIdentity = ObjectIdentity
prvtSysMonConformance = _PrvtSysMonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 2)
)
_SysMonMIBGroups_ObjectIdentity = ObjectIdentity
sysMonMIBGroups = _SysMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 2, 2)
)

# Managed Objects groups


# Notification objects

cpuUtilizationExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 1)
)
cpuUtilizationExceeded.setObjects(
      *(("PRVT-SYS-MON-MIB", "monCpuUtilization"),
        ("PRVT-SYS-MON-MIB", "cpuUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    cpuUtilizationExceeded.setStatus(
        "current"
    )

ramFreeSpaceExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 2)
)
ramFreeSpaceExceeded.setObjects(
      *(("PRVT-SYS-MON-MIB", "monRamBytesFree"),
        ("PRVT-SYS-MON-MIB", "ramBytesFreeThreshold"))
)
if mibBuilder.loadTexts:
    ramFreeSpaceExceeded.setStatus(
        "current"
    )

portErrorsExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 3)
)
portErrorsExceeded.setObjects(
      *(("PRVT-SYS-MON-MIB", "monPortErrors"),
        ("PRVT-SYS-MON-MIB", "portErrorsThreshold"))
)
if mibBuilder.loadTexts:
    portErrorsExceeded.setStatus(
        "current"
    )

portsBroadcastExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 4)
)
portsBroadcastExceeded.setObjects(
      *(("PRVT-SYS-MON-MIB", "monPortBroadcast"),
        ("PRVT-SYS-MON-MIB", "portsBroadcastThreshold"))
)
if mibBuilder.loadTexts:
    portsBroadcastExceeded.setStatus(
        "current"
    )

portsCRCErrExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 5)
)
portsCRCErrExceeded.setObjects(
      *(("PRVT-SYS-MON-MIB", "monPortCRCErr"),
        ("PRVT-SYS-MON-MIB", "portsCRCErrThreshold"))
)
if mibBuilder.loadTexts:
    portsCRCErrExceeded.setStatus(
        "current"
    )

portsRuntsExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 6)
)
portsRuntsExceeded.setObjects(
      *(("PRVT-SYS-MON-MIB", "monPortRunts"),
        ("PRVT-SYS-MON-MIB", "portsRuntsThreshold"))
)
if mibBuilder.loadTexts:
    portsRuntsExceeded.setStatus(
        "current"
    )

portsOverSizeExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 7)
)
portsOverSizeExceeded.setObjects(
      *(("PRVT-SYS-MON-MIB", "monPortOverSize"),
        ("PRVT-SYS-MON-MIB", "portsOverSizeThreshold"))
)
if mibBuilder.loadTexts:
    portsOverSizeExceeded.setStatus(
        "current"
    )

laserTemperatureThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 8)
)
laserTemperatureThresholdCrossed.setObjects(
      *(("PRVT-SYS-MON-MIB", "laserTemperature"),
        ("PRVT-SYS-MON-MIB", "laserTemperatureHighThreshold"),
        ("PRVT-SYS-MON-MIB", "laserTemperatureLowThreshold"))
)
if mibBuilder.loadTexts:
    laserTemperatureThresholdCrossed.setStatus(
        "current"
    )

laserTxPowerThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 9)
)
laserTxPowerThresholdCrossed.setObjects(
      *(("PRVT-SYS-MON-MIB", "laserTxPower"),
        ("PRVT-SYS-MON-MIB", "laserTxPowerHighThreshold"),
        ("PRVT-SYS-MON-MIB", "laserTxPowerLowThreshold"))
)
if mibBuilder.loadTexts:
    laserTxPowerThresholdCrossed.setStatus(
        "current"
    )

laserRxPowerThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 10)
)
laserRxPowerThresholdCrossed.setObjects(
      *(("PRVT-SYS-MON-MIB", "laserRxPower"),
        ("PRVT-SYS-MON-MIB", "laserRxPowerHighThreshold"),
        ("PRVT-SYS-MON-MIB", "laserRxPowerLowThreshold"))
)
if mibBuilder.loadTexts:
    laserRxPowerThresholdCrossed.setStatus(
        "current"
    )

sfpMonStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 0, 11)
)
sfpMonStatusChanged.setObjects(
    ("PRVT-SYS-MON-MIB", "sfpMonStatus")
)
if mibBuilder.loadTexts:
    sfpMonStatusChanged.setStatus(
        "current"
    )


# Notifications groups

sysMonNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 3, 2, 2, 3)
)
sysMonNotificationGroup.setObjects(
      *(("PRVT-SYS-MON-MIB", "cpuUtilizationExceeded"),
        ("PRVT-SYS-MON-MIB", "ramFreeSpaceExceeded"),
        ("PRVT-SYS-MON-MIB", "portErrorsExceeded"),
        ("PRVT-SYS-MON-MIB", "portsBroadcastExceeded"),
        ("PRVT-SYS-MON-MIB", "portsCRCErrExceeded"),
        ("PRVT-SYS-MON-MIB", "portsRuntsExceeded"),
        ("PRVT-SYS-MON-MIB", "portsOverSizeExceeded"))
)
if mibBuilder.loadTexts:
    sysMonNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-SYS-MON-MIB",
    **{"EnableStatus": EnableStatus,
       "software": software,
       "prvtSysMonMib": prvtSysMonMib,
       "prvtSysMonNotifications": prvtSysMonNotifications,
       "cpuUtilizationExceeded": cpuUtilizationExceeded,
       "ramFreeSpaceExceeded": ramFreeSpaceExceeded,
       "portErrorsExceeded": portErrorsExceeded,
       "portsBroadcastExceeded": portsBroadcastExceeded,
       "portsCRCErrExceeded": portsCRCErrExceeded,
       "portsRuntsExceeded": portsRuntsExceeded,
       "portsOverSizeExceeded": portsOverSizeExceeded,
       "laserTemperatureThresholdCrossed": laserTemperatureThresholdCrossed,
       "laserTxPowerThresholdCrossed": laserTxPowerThresholdCrossed,
       "laserRxPowerThresholdCrossed": laserRxPowerThresholdCrossed,
       "sfpMonStatusChanged": sfpMonStatusChanged,
       "prvtSysMonObjects": prvtSysMonObjects,
       "sysMonThreshold": sysMonThreshold,
       "cpuUtilizationThreshold": cpuUtilizationThreshold,
       "ramBytesFreeThreshold": ramBytesFreeThreshold,
       "portErrorsThreshold": portErrorsThreshold,
       "portsBroadcastThreshold": portsBroadcastThreshold,
       "portsCRCErrThreshold": portsCRCErrThreshold,
       "portsRuntsThreshold": portsRuntsThreshold,
       "portsOverSizeThreshold": portsOverSizeThreshold,
       "laserPortThresholdTable": laserPortThresholdTable,
       "laserPortThresholdEntry": laserPortThresholdEntry,
       "laserTemperatureHighThreshold": laserTemperatureHighThreshold,
       "laserTemperatureLowThreshold": laserTemperatureLowThreshold,
       "laserTxPowerHighThreshold": laserTxPowerHighThreshold,
       "laserTxPowerLowThreshold": laserTxPowerLowThreshold,
       "laserRxPowerHighThreshold": laserRxPowerHighThreshold,
       "laserRxPowerLowThreshold": laserRxPowerLowThreshold,
       "sysMonValues": sysMonValues,
       "monCpuUtilization": monCpuUtilization,
       "monRamBytesFree": monRamBytesFree,
       "monPortsTable": monPortsTable,
       "monPortsEntry": monPortsEntry,
       "monPortErrors": monPortErrors,
       "monPortBroadcast": monPortBroadcast,
       "monPortCRCErr": monPortCRCErr,
       "monPortRunts": monPortRunts,
       "monPortOverSize": monPortOverSize,
       "laserPortValueTable": laserPortValueTable,
       "laserPortValueEntry": laserPortValueEntry,
       "sfpStatus": sfpStatus,
       "laserTemperature": laserTemperature,
       "laserTxPower": laserTxPower,
       "laserRxPower": laserRxPower,
       "sfpPortManTable": sfpPortManTable,
       "sfpPortManEntry": sfpPortManEntry,
       "sfpMonStatus": sfpMonStatus,
       "sfpVendor": sfpVendor,
       "sfpPN": sfpPN,
       "sfpRevision": sfpRevision,
       "sfpLenght": sfpLenght,
       "sfpConnector": sfpConnector,
       "sysMonConfig": sysMonConfig,
       "sysMonConfigTable": sysMonConfigTable,
       "sysMonConfigEntry": sysMonConfigEntry,
       "sysMonIndicator": sysMonIndicator,
       "sysMonEnable": sysMonEnable,
       "sysMonPeriod": sysMonPeriod,
       "sysMonTrap": sysMonTrap,
       "sysMonLog": sysMonLog,
       "sysMonLed": sysMonLed,
       "sysMonDefaults": sysMonDefaults,
       "prvtSysMonConformance": prvtSysMonConformance,
       "sysMonMIBGroups": sysMonMIBGroups,
       "sysMonNotificationGroup": sysMonNotificationGroup}
)
