# SNMP MIB module (STORMSHIELD-HEALTH-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-HEALTH-MONITOR-MIB

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

(stormshieldMIB,) = mibBuilder.importSymbols(
    "STORMSHIELD-SMI-MIB",
    "stormshieldMIB")


# MODULE-IDENTITY

snsHealthMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16)
)
if mibBuilder.loadTexts:
    snsHealthMonitor.setRevisions(
        ("2021-05-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SnsGlobalHealth_Type(DisplayString):
    """Custom type snsGlobalHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsGlobalHealth_Type.__name__ = "DisplayString"
_SnsGlobalHealth_Object = MibScalar
snsGlobalHealth = _SnsGlobalHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 1),
    _SnsGlobalHealth_Type()
)
snsGlobalHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsGlobalHealth.setStatus("current")
_SnsFirewallHealthTable_Object = MibTable
snsFirewallHealthTable = _SnsFirewallHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2)
)
if mibBuilder.loadTexts:
    snsFirewallHealthTable.setStatus("current")
_SnsFirewallHealthEntry_Object = MibTableRow
snsFirewallHealthEntry = _SnsFirewallHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1)
)
snsFirewallHealthEntry.setIndexNames(
    (0, "STORMSHIELD-HEALTH-MONITOR-MIB", "snsFirewallIndex"),
)
if mibBuilder.loadTexts:
    snsFirewallHealthEntry.setStatus("current")


class _SnsFirewallIndex_Type(Integer32):
    """Custom type snsFirewallIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnsFirewallIndex_Type.__name__ = "Integer32"
_SnsFirewallIndex_Object = MibTableColumn
snsFirewallIndex = _SnsFirewallIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 1),
    _SnsFirewallIndex_Type()
)
snsFirewallIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snsFirewallIndex.setStatus("current")


class _SnsSerialHealth_Type(DisplayString):
    """Custom type snsSerialHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSerialHealth_Type.__name__ = "DisplayString"
_SnsSerialHealth_Object = MibTableColumn
snsSerialHealth = _SnsSerialHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 2),
    _SnsSerialHealth_Type()
)
snsSerialHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSerialHealth.setStatus("current")


class _SnsHaModeHealth_Type(DisplayString):
    """Custom type snsHaModeHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsHaModeHealth_Type.__name__ = "DisplayString"
_SnsHaModeHealth_Object = MibTableColumn
snsHaModeHealth = _SnsHaModeHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 3),
    _SnsHaModeHealth_Type()
)
snsHaModeHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsHaModeHealth.setStatus("current")


class _SnsHaLinkHealth_Type(DisplayString):
    """Custom type snsHaLinkHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsHaLinkHealth_Type.__name__ = "DisplayString"
_SnsHaLinkHealth_Object = MibTableColumn
snsHaLinkHealth = _SnsHaLinkHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 4),
    _SnsHaLinkHealth_Type()
)
snsHaLinkHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsHaLinkHealth.setStatus("current")


class _SnsPowerSupplyHealth_Type(DisplayString):
    """Custom type snsPowerSupplyHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsPowerSupplyHealth_Type.__name__ = "DisplayString"
_SnsPowerSupplyHealth_Object = MibTableColumn
snsPowerSupplyHealth = _SnsPowerSupplyHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 5),
    _SnsPowerSupplyHealth_Type()
)
snsPowerSupplyHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsPowerSupplyHealth.setStatus("current")


class _SnsFanHealth_Type(DisplayString):
    """Custom type snsFanHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsFanHealth_Type.__name__ = "DisplayString"
_SnsFanHealth_Object = MibTableColumn
snsFanHealth = _SnsFanHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 6),
    _SnsFanHealth_Type()
)
snsFanHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsFanHealth.setStatus("current")


class _SnsCpuHealth_Type(DisplayString):
    """Custom type snsCpuHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsCpuHealth_Type.__name__ = "DisplayString"
_SnsCpuHealth_Object = MibTableColumn
snsCpuHealth = _SnsCpuHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 7),
    _SnsCpuHealth_Type()
)
snsCpuHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsCpuHealth.setStatus("current")


class _SnsMemHealth_Type(DisplayString):
    """Custom type snsMemHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsMemHealth_Type.__name__ = "DisplayString"
_SnsMemHealth_Object = MibTableColumn
snsMemHealth = _SnsMemHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 8),
    _SnsMemHealth_Type()
)
snsMemHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsMemHealth.setStatus("current")


class _SnsDiskHealth_Type(DisplayString):
    """Custom type snsDiskHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsDiskHealth_Type.__name__ = "DisplayString"
_SnsDiskHealth_Object = MibTableColumn
snsDiskHealth = _SnsDiskHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 9),
    _SnsDiskHealth_Type()
)
snsDiskHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsDiskHealth.setStatus("current")


class _SnsRaidHealth_Type(DisplayString):
    """Custom type snsRaidHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsRaidHealth_Type.__name__ = "DisplayString"
_SnsRaidHealth_Object = MibTableColumn
snsRaidHealth = _SnsRaidHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 10),
    _SnsRaidHealth_Type()
)
snsRaidHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRaidHealth.setStatus("current")


class _SnsCertHealth_Type(DisplayString):
    """Custom type snsCertHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsCertHealth_Type.__name__ = "DisplayString"
_SnsCertHealth_Object = MibTableColumn
snsCertHealth = _SnsCertHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 11),
    _SnsCertHealth_Type()
)
snsCertHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsCertHealth.setStatus("current")


class _SnsCRLHealth_Type(DisplayString):
    """Custom type snsCRLHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsCRLHealth_Type.__name__ = "DisplayString"
_SnsCRLHealth_Object = MibTableColumn
snsCRLHealth = _SnsCRLHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 12),
    _SnsCRLHealth_Type()
)
snsCRLHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsCRLHealth.setStatus("current")


class _SnsTPMHealth_Type(DisplayString):
    """Custom type snsTPMHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsTPMHealth_Type.__name__ = "DisplayString"
_SnsTPMHealth_Object = MibTableColumn
snsTPMHealth = _SnsTPMHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 13),
    _SnsTPMHealth_Type()
)
snsTPMHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsTPMHealth.setStatus("current")


class _SnsPasswdHealth_Type(DisplayString):
    """Custom type snsPasswdHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsPasswdHealth_Type.__name__ = "DisplayString"
_SnsPasswdHealth_Object = MibTableColumn
snsPasswdHealth = _SnsPasswdHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 14),
    _SnsPasswdHealth_Type()
)
snsPasswdHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsPasswdHealth.setStatus("current")


class _SnsCpuTempHealth_Type(DisplayString):
    """Custom type snsCpuTempHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsCpuTempHealth_Type.__name__ = "DisplayString"
_SnsCpuTempHealth_Object = MibTableColumn
snsCpuTempHealth = _SnsCpuTempHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 15),
    _SnsCpuTempHealth_Type()
)
snsCpuTempHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsCpuTempHealth.setStatus("current")


class _SnsRouterHealth_Type(DisplayString):
    """Custom type snsRouterHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsRouterHealth_Type.__name__ = "DisplayString"
_SnsRouterHealth_Object = MibTableColumn
snsRouterHealth = _SnsRouterHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 16),
    _SnsRouterHealth_Type()
)
snsRouterHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouterHealth.setStatus("current")


class _SnsNTPHealth_Type(DisplayString):
    """Custom type snsNTPHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsNTPHealth_Type.__name__ = "DisplayString"
_SnsNTPHealth_Object = MibTableColumn
snsNTPHealth = _SnsNTPHealth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 16, 2, 1, 17),
    _SnsNTPHealth_Type()
)
snsNTPHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsNTPHealth.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-HEALTH-MONITOR-MIB",
    **{"snsHealthMonitor": snsHealthMonitor,
       "snsGlobalHealth": snsGlobalHealth,
       "snsFirewallHealthTable": snsFirewallHealthTable,
       "snsFirewallHealthEntry": snsFirewallHealthEntry,
       "snsFirewallIndex": snsFirewallIndex,
       "snsSerialHealth": snsSerialHealth,
       "snsHaModeHealth": snsHaModeHealth,
       "snsHaLinkHealth": snsHaLinkHealth,
       "snsPowerSupplyHealth": snsPowerSupplyHealth,
       "snsFanHealth": snsFanHealth,
       "snsCpuHealth": snsCpuHealth,
       "snsMemHealth": snsMemHealth,
       "snsDiskHealth": snsDiskHealth,
       "snsRaidHealth": snsRaidHealth,
       "snsCertHealth": snsCertHealth,
       "snsCRLHealth": snsCRLHealth,
       "snsTPMHealth": snsTPMHealth,
       "snsPasswdHealth": snsPasswdHealth,
       "snsCpuTempHealth": snsCpuTempHealth,
       "snsRouterHealth": snsRouterHealth,
       "snsNTPHealth": snsNTPHealth}
)
