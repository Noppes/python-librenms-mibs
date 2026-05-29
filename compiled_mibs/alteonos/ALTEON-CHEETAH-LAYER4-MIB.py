# SNMP MIB module (ALTEON-CHEETAH-LAYER4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alteonos\ALTEON-CHEETAH-LAYER4-MIB

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

(aws_switch,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "aws-switch")

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

layer4 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4)
)
if mibBuilder.loadTexts:
    layer4.setRevisions(
        ("2004-09-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Layer4Configs_ObjectIdentity = ObjectIdentity
layer4Configs = _Layer4Configs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1)
)
_SlbCfg_ObjectIdentity = ObjectIdentity
slbCfg = _SlbCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1)
)
_SlbGeneralCfg_ObjectIdentity = ObjectIdentity
slbGeneralCfg = _SlbGeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1)
)


class _SlbCurCfgGlobalControl_Type(Integer32):
    """Custom type slbCurCfgGlobalControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("disabled", 3))
    )


_SlbCurCfgGlobalControl_Type.__name__ = "Integer32"
_SlbCurCfgGlobalControl_Object = MibScalar
slbCurCfgGlobalControl = _SlbCurCfgGlobalControl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 1),
    _SlbCurCfgGlobalControl_Type()
)
slbCurCfgGlobalControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGlobalControl.setStatus("current")


class _SlbNewCfgGlobalControl_Type(Integer32):
    """Custom type slbNewCfgGlobalControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("disabled", 3))
    )


_SlbNewCfgGlobalControl_Type.__name__ = "Integer32"
_SlbNewCfgGlobalControl_Object = MibScalar
slbNewCfgGlobalControl = _SlbNewCfgGlobalControl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 2),
    _SlbNewCfgGlobalControl_Type()
)
slbNewCfgGlobalControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGlobalControl.setStatus("current")
_SlbCurCfgImask_Type = IpAddress
_SlbCurCfgImask_Object = MibScalar
slbCurCfgImask = _SlbCurCfgImask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 3),
    _SlbCurCfgImask_Type()
)
slbCurCfgImask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgImask.setStatus("current")
_SlbNewCfgImask_Type = IpAddress
_SlbNewCfgImask_Object = MibScalar
slbNewCfgImask = _SlbNewCfgImask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 4),
    _SlbNewCfgImask_Type()
)
slbNewCfgImask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgImask.setStatus("current")
_SlbCurCfgMnet_Type = IpAddress
_SlbCurCfgMnet_Object = MibScalar
slbCurCfgMnet = _SlbCurCfgMnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 5),
    _SlbCurCfgMnet_Type()
)
slbCurCfgMnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgMnet.setStatus("current")
_SlbNewCfgMnet_Type = IpAddress
_SlbNewCfgMnet_Object = MibScalar
slbNewCfgMnet = _SlbNewCfgMnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 6),
    _SlbNewCfgMnet_Type()
)
slbNewCfgMnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgMnet.setStatus("current")
_SlbCurCfgMmask_Type = IpAddress
_SlbCurCfgMmask_Object = MibScalar
slbCurCfgMmask = _SlbCurCfgMmask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 7),
    _SlbCurCfgMmask_Type()
)
slbCurCfgMmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgMmask.setStatus("current")
_SlbNewCfgMmask_Type = IpAddress
_SlbNewCfgMmask_Object = MibScalar
slbNewCfgMmask = _SlbNewCfgMmask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 8),
    _SlbNewCfgMmask_Type()
)
slbNewCfgMmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgMmask.setStatus("current")


class _SlbCurCfgRadiusAuthenString_Type(DisplayString):
    """Custom type slbCurCfgRadiusAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgRadiusAuthenString_Type.__name__ = "DisplayString"
_SlbCurCfgRadiusAuthenString_Object = MibScalar
slbCurCfgRadiusAuthenString = _SlbCurCfgRadiusAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 9),
    _SlbCurCfgRadiusAuthenString_Type()
)
slbCurCfgRadiusAuthenString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRadiusAuthenString.setStatus("current")


class _SlbNewCfgRadiusAuthenString_Type(DisplayString):
    """Custom type slbNewCfgRadiusAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbNewCfgRadiusAuthenString_Type.__name__ = "DisplayString"
_SlbNewCfgRadiusAuthenString_Object = MibScalar
slbNewCfgRadiusAuthenString = _SlbNewCfgRadiusAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 10),
    _SlbNewCfgRadiusAuthenString_Type()
)
slbNewCfgRadiusAuthenString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRadiusAuthenString.setStatus("current")


class _SlbCurCfgDirectMode_Type(Integer32):
    """Custom type slbCurCfgDirectMode based on Integer32"""
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


_SlbCurCfgDirectMode_Type.__name__ = "Integer32"
_SlbCurCfgDirectMode_Object = MibScalar
slbCurCfgDirectMode = _SlbCurCfgDirectMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 11),
    _SlbCurCfgDirectMode_Type()
)
slbCurCfgDirectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgDirectMode.setStatus("current")


class _SlbNewCfgDirectMode_Type(Integer32):
    """Custom type slbNewCfgDirectMode based on Integer32"""
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


_SlbNewCfgDirectMode_Type.__name__ = "Integer32"
_SlbNewCfgDirectMode_Object = MibScalar
slbNewCfgDirectMode = _SlbNewCfgDirectMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 12),
    _SlbNewCfgDirectMode_Type()
)
slbNewCfgDirectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgDirectMode.setStatus("current")
_SlbCurCfgPmask_Type = IpAddress
_SlbCurCfgPmask_Object = MibScalar
slbCurCfgPmask = _SlbCurCfgPmask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 13),
    _SlbCurCfgPmask_Type()
)
slbCurCfgPmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPmask.setStatus("current")
_SlbNewCfgPmask_Type = IpAddress
_SlbNewCfgPmask_Object = MibScalar
slbNewCfgPmask = _SlbNewCfgPmask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 14),
    _SlbNewCfgPmask_Type()
)
slbNewCfgPmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPmask.setStatus("current")


class _SlbCurCfgGrace_Type(Integer32):
    """Custom type slbCurCfgGrace based on Integer32"""
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


_SlbCurCfgGrace_Type.__name__ = "Integer32"
_SlbCurCfgGrace_Object = MibScalar
slbCurCfgGrace = _SlbCurCfgGrace_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 15),
    _SlbCurCfgGrace_Type()
)
slbCurCfgGrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGrace.setStatus("current")


class _SlbNewCfgGrace_Type(Integer32):
    """Custom type slbNewCfgGrace based on Integer32"""
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


_SlbNewCfgGrace_Type.__name__ = "Integer32"
_SlbNewCfgGrace_Object = MibScalar
slbNewCfgGrace = _SlbNewCfgGrace_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 16),
    _SlbNewCfgGrace_Type()
)
slbNewCfgGrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGrace.setStatus("current")


class _SlbCurCfgVirtMatrixArch_Type(Integer32):
    """Custom type slbCurCfgVirtMatrixArch based on Integer32"""
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


_SlbCurCfgVirtMatrixArch_Type.__name__ = "Integer32"
_SlbCurCfgVirtMatrixArch_Object = MibScalar
slbCurCfgVirtMatrixArch = _SlbCurCfgVirtMatrixArch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 17),
    _SlbCurCfgVirtMatrixArch_Type()
)
slbCurCfgVirtMatrixArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtMatrixArch.setStatus("current")


class _SlbNewCfgVirtMatrixArch_Type(Integer32):
    """Custom type slbNewCfgVirtMatrixArch based on Integer32"""
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


_SlbNewCfgVirtMatrixArch_Type.__name__ = "Integer32"
_SlbNewCfgVirtMatrixArch_Object = MibScalar
slbNewCfgVirtMatrixArch = _SlbNewCfgVirtMatrixArch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 18),
    _SlbNewCfgVirtMatrixArch_Type()
)
slbNewCfgVirtMatrixArch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtMatrixArch.setStatus("current")


class _SlbCurCfgFastage_Type(Integer32):
    """Custom type slbCurCfgFastage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SlbCurCfgFastage_Type.__name__ = "Integer32"
_SlbCurCfgFastage_Object = MibScalar
slbCurCfgFastage = _SlbCurCfgFastage_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 19),
    _SlbCurCfgFastage_Type()
)
slbCurCfgFastage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgFastage.setStatus("current")


class _SlbNewCfgFastage_Type(Integer32):
    """Custom type slbNewCfgFastage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SlbNewCfgFastage_Type.__name__ = "Integer32"
_SlbNewCfgFastage_Object = MibScalar
slbNewCfgFastage = _SlbNewCfgFastage_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 20),
    _SlbNewCfgFastage_Type()
)
slbNewCfgFastage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgFastage.setStatus("current")


class _SlbCurCfgSlowage_Type(Integer32):
    """Custom type slbCurCfgSlowage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlbCurCfgSlowage_Type.__name__ = "Integer32"
_SlbCurCfgSlowage_Object = MibScalar
slbCurCfgSlowage = _SlbCurCfgSlowage_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 21),
    _SlbCurCfgSlowage_Type()
)
slbCurCfgSlowage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSlowage.setStatus("obsolete")


class _SlbNewCfgSlowage_Type(Integer32):
    """Custom type slbNewCfgSlowage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlbNewCfgSlowage_Type.__name__ = "Integer32"
_SlbNewCfgSlowage_Object = MibScalar
slbNewCfgSlowage = _SlbNewCfgSlowage_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 22),
    _SlbNewCfgSlowage_Type()
)
slbNewCfgSlowage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSlowage.setStatus("obsolete")


class _SlbCurCfgTpcp_Type(Integer32):
    """Custom type slbCurCfgTpcp based on Integer32"""
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


_SlbCurCfgTpcp_Type.__name__ = "Integer32"
_SlbCurCfgTpcp_Object = MibScalar
slbCurCfgTpcp = _SlbCurCfgTpcp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 23),
    _SlbCurCfgTpcp_Type()
)
slbCurCfgTpcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgTpcp.setStatus("current")


class _SlbNewCfgTpcp_Type(Integer32):
    """Custom type slbNewCfgTpcp based on Integer32"""
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


_SlbNewCfgTpcp_Type.__name__ = "Integer32"
_SlbNewCfgTpcp_Object = MibScalar
slbNewCfgTpcp = _SlbNewCfgTpcp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 24),
    _SlbNewCfgTpcp_Type()
)
slbNewCfgTpcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgTpcp.setStatus("current")


class _SlbCurCfgMetricInterval_Type(Integer32):
    """Custom type slbCurCfgMetricInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SlbCurCfgMetricInterval_Type.__name__ = "Integer32"
_SlbCurCfgMetricInterval_Object = MibScalar
slbCurCfgMetricInterval = _SlbCurCfgMetricInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 25),
    _SlbCurCfgMetricInterval_Type()
)
slbCurCfgMetricInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgMetricInterval.setStatus("current")


class _SlbNewCfgMetricInterval_Type(Integer32):
    """Custom type slbNewCfgMetricInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SlbNewCfgMetricInterval_Type.__name__ = "Integer32"
_SlbNewCfgMetricInterval_Object = MibScalar
slbNewCfgMetricInterval = _SlbNewCfgMetricInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 26),
    _SlbNewCfgMetricInterval_Type()
)
slbNewCfgMetricInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgMetricInterval.setStatus("current")


class _SlbCurCfgLdapVersion_Type(Integer32):
    """Custom type slbCurCfgLdapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version2", 1),
          ("version3", 2))
    )


_SlbCurCfgLdapVersion_Type.__name__ = "Integer32"
_SlbCurCfgLdapVersion_Object = MibScalar
slbCurCfgLdapVersion = _SlbCurCfgLdapVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 27),
    _SlbCurCfgLdapVersion_Type()
)
slbCurCfgLdapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgLdapVersion.setStatus("current")


class _SlbNewCfgLdapVersion_Type(Integer32):
    """Custom type slbNewCfgLdapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version2", 1),
          ("version3", 2))
    )


_SlbNewCfgLdapVersion_Type.__name__ = "Integer32"
_SlbNewCfgLdapVersion_Object = MibScalar
slbNewCfgLdapVersion = _SlbNewCfgLdapVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 28),
    _SlbNewCfgLdapVersion_Type()
)
slbNewCfgLdapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgLdapVersion.setStatus("current")


class _SlbCurCfgAllowHttpHc_Type(Integer32):
    """Custom type slbCurCfgAllowHttpHc based on Integer32"""
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


_SlbCurCfgAllowHttpHc_Type.__name__ = "Integer32"
_SlbCurCfgAllowHttpHc_Object = MibScalar
slbCurCfgAllowHttpHc = _SlbCurCfgAllowHttpHc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 29),
    _SlbCurCfgAllowHttpHc_Type()
)
slbCurCfgAllowHttpHc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgAllowHttpHc.setStatus("current")


class _SlbNewCfgAllowHttpHc_Type(Integer32):
    """Custom type slbNewCfgAllowHttpHc based on Integer32"""
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


_SlbNewCfgAllowHttpHc_Type.__name__ = "Integer32"
_SlbNewCfgAllowHttpHc_Object = MibScalar
slbNewCfgAllowHttpHc = _SlbNewCfgAllowHttpHc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 30),
    _SlbNewCfgAllowHttpHc_Type()
)
slbNewCfgAllowHttpHc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgAllowHttpHc.setStatus("current")


class _SlbCurCfgSubmac_Type(Integer32):
    """Custom type slbCurCfgSubmac based on Integer32"""
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


_SlbCurCfgSubmac_Type.__name__ = "Integer32"
_SlbCurCfgSubmac_Object = MibScalar
slbCurCfgSubmac = _SlbCurCfgSubmac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 31),
    _SlbCurCfgSubmac_Type()
)
slbCurCfgSubmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSubmac.setStatus("current")


class _SlbNewCfgSubmac_Type(Integer32):
    """Custom type slbNewCfgSubmac based on Integer32"""
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


_SlbNewCfgSubmac_Type.__name__ = "Integer32"
_SlbNewCfgSubmac_Object = MibScalar
slbNewCfgSubmac = _SlbNewCfgSubmac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 32),
    _SlbNewCfgSubmac_Type()
)
slbNewCfgSubmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSubmac.setStatus("current")


class _SlbCurCfgProxyGratArp_Type(Integer32):
    """Custom type slbCurCfgProxyGratArp based on Integer32"""
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


_SlbCurCfgProxyGratArp_Type.__name__ = "Integer32"
_SlbCurCfgProxyGratArp_Object = MibScalar
slbCurCfgProxyGratArp = _SlbCurCfgProxyGratArp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 33),
    _SlbCurCfgProxyGratArp_Type()
)
slbCurCfgProxyGratArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgProxyGratArp.setStatus("obsolete")


class _SlbNewCfgProxyGratArp_Type(Integer32):
    """Custom type slbNewCfgProxyGratArp based on Integer32"""
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


_SlbNewCfgProxyGratArp_Type.__name__ = "Integer32"
_SlbNewCfgProxyGratArp_Object = MibScalar
slbNewCfgProxyGratArp = _SlbNewCfgProxyGratArp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 34),
    _SlbNewCfgProxyGratArp_Type()
)
slbNewCfgProxyGratArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgProxyGratArp.setStatus("obsolete")


class _SlbCurCfgRtsVlan_Type(Integer32):
    """Custom type slbCurCfgRtsVlan based on Integer32"""
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


_SlbCurCfgRtsVlan_Type.__name__ = "Integer32"
_SlbCurCfgRtsVlan_Object = MibScalar
slbCurCfgRtsVlan = _SlbCurCfgRtsVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 35),
    _SlbCurCfgRtsVlan_Type()
)
slbCurCfgRtsVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRtsVlan.setStatus("current")


class _SlbNewCfgRtsVlan_Type(Integer32):
    """Custom type slbNewCfgRtsVlan based on Integer32"""
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


_SlbNewCfgRtsVlan_Type.__name__ = "Integer32"
_SlbNewCfgRtsVlan_Object = MibScalar
slbNewCfgRtsVlan = _SlbNewCfgRtsVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 36),
    _SlbNewCfgRtsVlan_Type()
)
slbNewCfgRtsVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRtsVlan.setStatus("current")


class _SlbCurCfgVirtualServiceStats_Type(Integer32):
    """Custom type slbCurCfgVirtualServiceStats based on Integer32"""
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


_SlbCurCfgVirtualServiceStats_Type.__name__ = "Integer32"
_SlbCurCfgVirtualServiceStats_Object = MibScalar
slbCurCfgVirtualServiceStats = _SlbCurCfgVirtualServiceStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 37),
    _SlbCurCfgVirtualServiceStats_Type()
)
slbCurCfgVirtualServiceStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtualServiceStats.setStatus("current")


class _SlbNewCfgVirtualServiceStats_Type(Integer32):
    """Custom type slbNewCfgVirtualServiceStats based on Integer32"""
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


_SlbNewCfgVirtualServiceStats_Type.__name__ = "Integer32"
_SlbNewCfgVirtualServiceStats_Object = MibScalar
slbNewCfgVirtualServiceStats = _SlbNewCfgVirtualServiceStats_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 38),
    _SlbNewCfgVirtualServiceStats_Type()
)
slbNewCfgVirtualServiceStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtualServiceStats.setStatus("current")


class _SlbCurCfgSlbSessAtkIntrval_Type(Integer32):
    """Custom type slbCurCfgSlbSessAtkIntrval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SlbCurCfgSlbSessAtkIntrval_Type.__name__ = "Integer32"
_SlbCurCfgSlbSessAtkIntrval_Object = MibScalar
slbCurCfgSlbSessAtkIntrval = _SlbCurCfgSlbSessAtkIntrval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 39),
    _SlbCurCfgSlbSessAtkIntrval_Type()
)
slbCurCfgSlbSessAtkIntrval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSlbSessAtkIntrval.setStatus("current")


class _SlbNewCfgSlbSessAtkIntrval_Type(Integer32):
    """Custom type slbNewCfgSlbSessAtkIntrval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SlbNewCfgSlbSessAtkIntrval_Type.__name__ = "Integer32"
_SlbNewCfgSlbSessAtkIntrval_Object = MibScalar
slbNewCfgSlbSessAtkIntrval = _SlbNewCfgSlbSessAtkIntrval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 40),
    _SlbNewCfgSlbSessAtkIntrval_Type()
)
slbNewCfgSlbSessAtkIntrval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSlbSessAtkIntrval.setStatus("current")


class _SlbCurCfgSlbSessAtkAllowlim_Type(Integer32):
    """Custom type slbCurCfgSlbSessAtkAllowlim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2097100),
    )


_SlbCurCfgSlbSessAtkAllowlim_Type.__name__ = "Integer32"
_SlbCurCfgSlbSessAtkAllowlim_Object = MibScalar
slbCurCfgSlbSessAtkAllowlim = _SlbCurCfgSlbSessAtkAllowlim_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 41),
    _SlbCurCfgSlbSessAtkAllowlim_Type()
)
slbCurCfgSlbSessAtkAllowlim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSlbSessAtkAllowlim.setStatus("current")


class _SlbNewCfgSlbSessAtkAllowlim_Type(Integer32):
    """Custom type slbNewCfgSlbSessAtkAllowlim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2097100),
    )


_SlbNewCfgSlbSessAtkAllowlim_Type.__name__ = "Integer32"
_SlbNewCfgSlbSessAtkAllowlim_Object = MibScalar
slbNewCfgSlbSessAtkAllowlim = _SlbNewCfgSlbSessAtkAllowlim_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 42),
    _SlbNewCfgSlbSessAtkAllowlim_Type()
)
slbNewCfgSlbSessAtkAllowlim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSlbSessAtkAllowlim.setStatus("current")


class _SlbCurCfgNewSlowage_Type(Integer32):
    """Custom type slbCurCfgNewSlowage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_SlbCurCfgNewSlowage_Type.__name__ = "Integer32"
_SlbCurCfgNewSlowage_Object = MibScalar
slbCurCfgNewSlowage = _SlbCurCfgNewSlowage_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 43),
    _SlbCurCfgNewSlowage_Type()
)
slbCurCfgNewSlowage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgNewSlowage.setStatus("current")


class _SlbNewCfgNewSlowage_Type(Integer32):
    """Custom type slbNewCfgNewSlowage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_SlbNewCfgNewSlowage_Type.__name__ = "Integer32"
_SlbNewCfgNewSlowage_Object = MibScalar
slbNewCfgNewSlowage = _SlbNewCfgNewSlowage_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 44),
    _SlbNewCfgNewSlowage_Type()
)
slbNewCfgNewSlowage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgNewSlowage.setStatus("current")


class _SlbCurCfgPortBind_Type(Integer32):
    """Custom type slbCurCfgPortBind based on Integer32"""
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


_SlbCurCfgPortBind_Type.__name__ = "Integer32"
_SlbCurCfgPortBind_Object = MibScalar
slbCurCfgPortBind = _SlbCurCfgPortBind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 45),
    _SlbCurCfgPortBind_Type()
)
slbCurCfgPortBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortBind.setStatus("current")


class _SlbNewCfgPortBind_Type(Integer32):
    """Custom type slbNewCfgPortBind based on Integer32"""
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


_SlbNewCfgPortBind_Type.__name__ = "Integer32"
_SlbNewCfgPortBind_Object = MibScalar
slbNewCfgPortBind = _SlbNewCfgPortBind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 46),
    _SlbNewCfgPortBind_Type()
)
slbNewCfgPortBind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortBind.setStatus("current")


class _SlbCurCfgVmaSrcPort_Type(Integer32):
    """Custom type slbCurCfgVmaSrcPort based on Integer32"""
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


_SlbCurCfgVmaSrcPort_Type.__name__ = "Integer32"
_SlbCurCfgVmaSrcPort_Object = MibScalar
slbCurCfgVmaSrcPort = _SlbCurCfgVmaSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 47),
    _SlbCurCfgVmaSrcPort_Type()
)
slbCurCfgVmaSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVmaSrcPort.setStatus("current")


class _SlbNewCfgVmaSrcPort_Type(Integer32):
    """Custom type slbNewCfgVmaSrcPort based on Integer32"""
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


_SlbNewCfgVmaSrcPort_Type.__name__ = "Integer32"
_SlbNewCfgVmaSrcPort_Object = MibScalar
slbNewCfgVmaSrcPort = _SlbNewCfgVmaSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 48),
    _SlbNewCfgVmaSrcPort_Type()
)
slbNewCfgVmaSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVmaSrcPort.setStatus("current")


class _SlbCurCfgIpTcpCksum_Type(Integer32):
    """Custom type slbCurCfgIpTcpCksum based on Integer32"""
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


_SlbCurCfgIpTcpCksum_Type.__name__ = "Integer32"
_SlbCurCfgIpTcpCksum_Object = MibScalar
slbCurCfgIpTcpCksum = _SlbCurCfgIpTcpCksum_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 49),
    _SlbCurCfgIpTcpCksum_Type()
)
slbCurCfgIpTcpCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgIpTcpCksum.setStatus("current")


class _SlbNewCfgIpTcpCksum_Type(Integer32):
    """Custom type slbNewCfgIpTcpCksum based on Integer32"""
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


_SlbNewCfgIpTcpCksum_Type.__name__ = "Integer32"
_SlbNewCfgIpTcpCksum_Object = MibScalar
slbNewCfgIpTcpCksum = _SlbNewCfgIpTcpCksum_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 1, 50),
    _SlbNewCfgIpTcpCksum_Type()
)
slbNewCfgIpTcpCksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgIpTcpCksum.setStatus("current")
_RealServerCfg_ObjectIdentity = ObjectIdentity
realServerCfg = _RealServerCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2)
)
_SlbRealServerMaxSize_Type = Integer32
_SlbRealServerMaxSize_Object = MibScalar
slbRealServerMaxSize = _SlbRealServerMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 1),
    _SlbRealServerMaxSize_Type()
)
slbRealServerMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerMaxSize.setStatus("current")
_SlbCurCfgRealServerTable_Object = MibTable
slbCurCfgRealServerTable = _SlbCurCfgRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    slbCurCfgRealServerTable.setStatus("current")
_SlbCurCfgRealServerEntry_Object = MibTableRow
slbCurCfgRealServerEntry = _SlbCurCfgRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1)
)
slbCurCfgRealServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServerIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgRealServerEntry.setStatus("current")
_SlbCurCfgRealServerIndex_Type = Integer32
_SlbCurCfgRealServerIndex_Object = MibTableColumn
slbCurCfgRealServerIndex = _SlbCurCfgRealServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 1),
    _SlbCurCfgRealServerIndex_Type()
)
slbCurCfgRealServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerIndex.setStatus("current")
_SlbCurCfgRealServerIpAddr_Type = IpAddress
_SlbCurCfgRealServerIpAddr_Object = MibTableColumn
slbCurCfgRealServerIpAddr = _SlbCurCfgRealServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 2),
    _SlbCurCfgRealServerIpAddr_Type()
)
slbCurCfgRealServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerIpAddr.setStatus("current")


class _SlbCurCfgRealServerWeight_Type(Integer32):
    """Custom type slbCurCfgRealServerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SlbCurCfgRealServerWeight_Type.__name__ = "Integer32"
_SlbCurCfgRealServerWeight_Object = MibTableColumn
slbCurCfgRealServerWeight = _SlbCurCfgRealServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 3),
    _SlbCurCfgRealServerWeight_Type()
)
slbCurCfgRealServerWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerWeight.setStatus("current")


class _SlbCurCfgRealServerMaxConns_Type(Integer32):
    """Custom type slbCurCfgRealServerMaxConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_SlbCurCfgRealServerMaxConns_Type.__name__ = "Integer32"
_SlbCurCfgRealServerMaxConns_Object = MibTableColumn
slbCurCfgRealServerMaxConns = _SlbCurCfgRealServerMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 4),
    _SlbCurCfgRealServerMaxConns_Type()
)
slbCurCfgRealServerMaxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerMaxConns.setStatus("current")


class _SlbCurCfgRealServerTimeOut_Type(Integer32):
    """Custom type slbCurCfgRealServerTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32768),
    )


_SlbCurCfgRealServerTimeOut_Type.__name__ = "Integer32"
_SlbCurCfgRealServerTimeOut_Object = MibTableColumn
slbCurCfgRealServerTimeOut = _SlbCurCfgRealServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 5),
    _SlbCurCfgRealServerTimeOut_Type()
)
slbCurCfgRealServerTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerTimeOut.setStatus("current")
_SlbCurCfgRealServerBackUp_Type = Integer32
_SlbCurCfgRealServerBackUp_Object = MibTableColumn
slbCurCfgRealServerBackUp = _SlbCurCfgRealServerBackUp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 6),
    _SlbCurCfgRealServerBackUp_Type()
)
slbCurCfgRealServerBackUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerBackUp.setStatus("current")


class _SlbCurCfgRealServerPingInterval_Type(Integer32):
    """Custom type slbCurCfgRealServerPingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SlbCurCfgRealServerPingInterval_Type.__name__ = "Integer32"
_SlbCurCfgRealServerPingInterval_Object = MibTableColumn
slbCurCfgRealServerPingInterval = _SlbCurCfgRealServerPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 7),
    _SlbCurCfgRealServerPingInterval_Type()
)
slbCurCfgRealServerPingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerPingInterval.setStatus("current")


class _SlbCurCfgRealServerFailRetry_Type(Integer32):
    """Custom type slbCurCfgRealServerFailRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbCurCfgRealServerFailRetry_Type.__name__ = "Integer32"
_SlbCurCfgRealServerFailRetry_Object = MibTableColumn
slbCurCfgRealServerFailRetry = _SlbCurCfgRealServerFailRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 8),
    _SlbCurCfgRealServerFailRetry_Type()
)
slbCurCfgRealServerFailRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerFailRetry.setStatus("current")


class _SlbCurCfgRealServerSuccRetry_Type(Integer32):
    """Custom type slbCurCfgRealServerSuccRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbCurCfgRealServerSuccRetry_Type.__name__ = "Integer32"
_SlbCurCfgRealServerSuccRetry_Object = MibTableColumn
slbCurCfgRealServerSuccRetry = _SlbCurCfgRealServerSuccRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 9),
    _SlbCurCfgRealServerSuccRetry_Type()
)
slbCurCfgRealServerSuccRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerSuccRetry.setStatus("current")


class _SlbCurCfgRealServerState_Type(Integer32):
    """Custom type slbCurCfgRealServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("disabled", 3))
    )


_SlbCurCfgRealServerState_Type.__name__ = "Integer32"
_SlbCurCfgRealServerState_Object = MibTableColumn
slbCurCfgRealServerState = _SlbCurCfgRealServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 10),
    _SlbCurCfgRealServerState_Type()
)
slbCurCfgRealServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerState.setStatus("current")


class _SlbCurCfgRealServerType_Type(Integer32):
    """Custom type slbCurCfgRealServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-server", 1),
          ("remote-server", 2))
    )


_SlbCurCfgRealServerType_Type.__name__ = "Integer32"
_SlbCurCfgRealServerType_Object = MibTableColumn
slbCurCfgRealServerType = _SlbCurCfgRealServerType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 11),
    _SlbCurCfgRealServerType_Type()
)
slbCurCfgRealServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerType.setStatus("current")


class _SlbCurCfgRealServerName_Type(DisplayString):
    """Custom type slbCurCfgRealServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlbCurCfgRealServerName_Type.__name__ = "DisplayString"
_SlbCurCfgRealServerName_Object = MibTableColumn
slbCurCfgRealServerName = _SlbCurCfgRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 12),
    _SlbCurCfgRealServerName_Type()
)
slbCurCfgRealServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerName.setStatus("current")
_SlbCurCfgRealServerUrlBmap_Type = OctetString
_SlbCurCfgRealServerUrlBmap_Object = MibTableColumn
slbCurCfgRealServerUrlBmap = _SlbCurCfgRealServerUrlBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 13),
    _SlbCurCfgRealServerUrlBmap_Type()
)
slbCurCfgRealServerUrlBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerUrlBmap.setStatus("current")


class _SlbCurCfgRealServerCookie_Type(Integer32):
    """Custom type slbCurCfgRealServerCookie based on Integer32"""
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


_SlbCurCfgRealServerCookie_Type.__name__ = "Integer32"
_SlbCurCfgRealServerCookie_Object = MibTableColumn
slbCurCfgRealServerCookie = _SlbCurCfgRealServerCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 14),
    _SlbCurCfgRealServerCookie_Type()
)
slbCurCfgRealServerCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerCookie.setStatus("current")


class _SlbCurCfgRealServerExcludeStr_Type(Integer32):
    """Custom type slbCurCfgRealServerExcludeStr based on Integer32"""
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


_SlbCurCfgRealServerExcludeStr_Type.__name__ = "Integer32"
_SlbCurCfgRealServerExcludeStr_Object = MibTableColumn
slbCurCfgRealServerExcludeStr = _SlbCurCfgRealServerExcludeStr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 15),
    _SlbCurCfgRealServerExcludeStr_Type()
)
slbCurCfgRealServerExcludeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerExcludeStr.setStatus("current")


class _SlbCurCfgRealServerSubmac_Type(Integer32):
    """Custom type slbCurCfgRealServerSubmac based on Integer32"""
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


_SlbCurCfgRealServerSubmac_Type.__name__ = "Integer32"
_SlbCurCfgRealServerSubmac_Object = MibTableColumn
slbCurCfgRealServerSubmac = _SlbCurCfgRealServerSubmac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 16),
    _SlbCurCfgRealServerSubmac_Type()
)
slbCurCfgRealServerSubmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerSubmac.setStatus("current")


class _SlbCurCfgRealServerProxy_Type(Integer32):
    """Custom type slbCurCfgRealServerProxy based on Integer32"""
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


_SlbCurCfgRealServerProxy_Type.__name__ = "Integer32"
_SlbCurCfgRealServerProxy_Object = MibTableColumn
slbCurCfgRealServerProxy = _SlbCurCfgRealServerProxy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 17),
    _SlbCurCfgRealServerProxy_Type()
)
slbCurCfgRealServerProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerProxy.setStatus("current")


class _SlbCurCfgRealServerLdapwr_Type(Integer32):
    """Custom type slbCurCfgRealServerLdapwr based on Integer32"""
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


_SlbCurCfgRealServerLdapwr_Type.__name__ = "Integer32"
_SlbCurCfgRealServerLdapwr_Object = MibTableColumn
slbCurCfgRealServerLdapwr = _SlbCurCfgRealServerLdapwr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 18),
    _SlbCurCfgRealServerLdapwr_Type()
)
slbCurCfgRealServerLdapwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerLdapwr.setStatus("current")


class _SlbCurCfgRealServerOid_Type(DisplayString):
    """Custom type slbCurCfgRealServerOid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SlbCurCfgRealServerOid_Type.__name__ = "DisplayString"
_SlbCurCfgRealServerOid_Object = MibTableColumn
slbCurCfgRealServerOid = _SlbCurCfgRealServerOid_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 19),
    _SlbCurCfgRealServerOid_Type()
)
slbCurCfgRealServerOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerOid.setStatus("current")


class _SlbCurCfgRealServerCommString_Type(DisplayString):
    """Custom type slbCurCfgRealServerCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgRealServerCommString_Type.__name__ = "DisplayString"
_SlbCurCfgRealServerCommString_Object = MibTableColumn
slbCurCfgRealServerCommString = _SlbCurCfgRealServerCommString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 20),
    _SlbCurCfgRealServerCommString_Type()
)
slbCurCfgRealServerCommString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerCommString.setStatus("current")


class _SlbCurCfgRealServerIdsvlan_Type(Integer32):
    """Custom type slbCurCfgRealServerIdsvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4090),
    )


_SlbCurCfgRealServerIdsvlan_Type.__name__ = "Integer32"
_SlbCurCfgRealServerIdsvlan_Object = MibTableColumn
slbCurCfgRealServerIdsvlan = _SlbCurCfgRealServerIdsvlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 21),
    _SlbCurCfgRealServerIdsvlan_Type()
)
slbCurCfgRealServerIdsvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerIdsvlan.setStatus("current")
_SlbCurCfgRealServerIdsport_Type = Integer32
_SlbCurCfgRealServerIdsport_Object = MibTableColumn
slbCurCfgRealServerIdsport = _SlbCurCfgRealServerIdsport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 22),
    _SlbCurCfgRealServerIdsport_Type()
)
slbCurCfgRealServerIdsport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerIdsport.setStatus("current")


class _SlbCurCfgRealServerAvail_Type(Integer32):
    """Custom type slbCurCfgRealServerAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SlbCurCfgRealServerAvail_Type.__name__ = "Integer32"
_SlbCurCfgRealServerAvail_Object = MibTableColumn
slbCurCfgRealServerAvail = _SlbCurCfgRealServerAvail_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 23),
    _SlbCurCfgRealServerAvail_Type()
)
slbCurCfgRealServerAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerAvail.setStatus("current")


class _SlbCurCfgRealServerFastHealthCheck_Type(Integer32):
    """Custom type slbCurCfgRealServerFastHealthCheck based on Integer32"""
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


_SlbCurCfgRealServerFastHealthCheck_Type.__name__ = "Integer32"
_SlbCurCfgRealServerFastHealthCheck_Object = MibTableColumn
slbCurCfgRealServerFastHealthCheck = _SlbCurCfgRealServerFastHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 24),
    _SlbCurCfgRealServerFastHealthCheck_Type()
)
slbCurCfgRealServerFastHealthCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerFastHealthCheck.setStatus("current")


class _SlbCurCfgRealServerSubdmac_Type(Integer32):
    """Custom type slbCurCfgRealServerSubdmac based on Integer32"""
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


_SlbCurCfgRealServerSubdmac_Type.__name__ = "Integer32"
_SlbCurCfgRealServerSubdmac_Object = MibTableColumn
slbCurCfgRealServerSubdmac = _SlbCurCfgRealServerSubdmac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 25),
    _SlbCurCfgRealServerSubdmac_Type()
)
slbCurCfgRealServerSubdmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerSubdmac.setStatus("current")


class _SlbCurCfgRealServerOverflow_Type(Integer32):
    """Custom type slbCurCfgRealServerOverflow based on Integer32"""
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


_SlbCurCfgRealServerOverflow_Type.__name__ = "Integer32"
_SlbCurCfgRealServerOverflow_Object = MibTableColumn
slbCurCfgRealServerOverflow = _SlbCurCfgRealServerOverflow_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 2, 1, 26),
    _SlbCurCfgRealServerOverflow_Type()
)
slbCurCfgRealServerOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerOverflow.setStatus("current")
_SlbNewCfgRealServerTable_Object = MibTable
slbNewCfgRealServerTable = _SlbNewCfgRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    slbNewCfgRealServerTable.setStatus("current")
_SlbNewCfgRealServerEntry_Object = MibTableRow
slbNewCfgRealServerEntry = _SlbNewCfgRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1)
)
slbNewCfgRealServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgRealServerIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgRealServerEntry.setStatus("current")
_SlbNewCfgRealServerIndex_Type = Integer32
_SlbNewCfgRealServerIndex_Object = MibTableColumn
slbNewCfgRealServerIndex = _SlbNewCfgRealServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 1),
    _SlbNewCfgRealServerIndex_Type()
)
slbNewCfgRealServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgRealServerIndex.setStatus("current")
_SlbNewCfgRealServerIpAddr_Type = IpAddress
_SlbNewCfgRealServerIpAddr_Object = MibTableColumn
slbNewCfgRealServerIpAddr = _SlbNewCfgRealServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 2),
    _SlbNewCfgRealServerIpAddr_Type()
)
slbNewCfgRealServerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerIpAddr.setStatus("current")


class _SlbNewCfgRealServerWeight_Type(Integer32):
    """Custom type slbNewCfgRealServerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SlbNewCfgRealServerWeight_Type.__name__ = "Integer32"
_SlbNewCfgRealServerWeight_Object = MibTableColumn
slbNewCfgRealServerWeight = _SlbNewCfgRealServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 3),
    _SlbNewCfgRealServerWeight_Type()
)
slbNewCfgRealServerWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerWeight.setStatus("current")


class _SlbNewCfgRealServerMaxConns_Type(Integer32):
    """Custom type slbNewCfgRealServerMaxConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_SlbNewCfgRealServerMaxConns_Type.__name__ = "Integer32"
_SlbNewCfgRealServerMaxConns_Object = MibTableColumn
slbNewCfgRealServerMaxConns = _SlbNewCfgRealServerMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 4),
    _SlbNewCfgRealServerMaxConns_Type()
)
slbNewCfgRealServerMaxConns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerMaxConns.setStatus("current")


class _SlbNewCfgRealServerTimeOut_Type(Integer32):
    """Custom type slbNewCfgRealServerTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32768),
    )


_SlbNewCfgRealServerTimeOut_Type.__name__ = "Integer32"
_SlbNewCfgRealServerTimeOut_Object = MibTableColumn
slbNewCfgRealServerTimeOut = _SlbNewCfgRealServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 5),
    _SlbNewCfgRealServerTimeOut_Type()
)
slbNewCfgRealServerTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerTimeOut.setStatus("current")
_SlbNewCfgRealServerBackUp_Type = Integer32
_SlbNewCfgRealServerBackUp_Object = MibTableColumn
slbNewCfgRealServerBackUp = _SlbNewCfgRealServerBackUp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 6),
    _SlbNewCfgRealServerBackUp_Type()
)
slbNewCfgRealServerBackUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerBackUp.setStatus("current")


class _SlbNewCfgRealServerPingInterval_Type(Integer32):
    """Custom type slbNewCfgRealServerPingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SlbNewCfgRealServerPingInterval_Type.__name__ = "Integer32"
_SlbNewCfgRealServerPingInterval_Object = MibTableColumn
slbNewCfgRealServerPingInterval = _SlbNewCfgRealServerPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 7),
    _SlbNewCfgRealServerPingInterval_Type()
)
slbNewCfgRealServerPingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerPingInterval.setStatus("current")


class _SlbNewCfgRealServerFailRetry_Type(Integer32):
    """Custom type slbNewCfgRealServerFailRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbNewCfgRealServerFailRetry_Type.__name__ = "Integer32"
_SlbNewCfgRealServerFailRetry_Object = MibTableColumn
slbNewCfgRealServerFailRetry = _SlbNewCfgRealServerFailRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 8),
    _SlbNewCfgRealServerFailRetry_Type()
)
slbNewCfgRealServerFailRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerFailRetry.setStatus("current")


class _SlbNewCfgRealServerSuccRetry_Type(Integer32):
    """Custom type slbNewCfgRealServerSuccRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbNewCfgRealServerSuccRetry_Type.__name__ = "Integer32"
_SlbNewCfgRealServerSuccRetry_Object = MibTableColumn
slbNewCfgRealServerSuccRetry = _SlbNewCfgRealServerSuccRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 9),
    _SlbNewCfgRealServerSuccRetry_Type()
)
slbNewCfgRealServerSuccRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerSuccRetry.setStatus("current")


class _SlbNewCfgRealServerState_Type(Integer32):
    """Custom type slbNewCfgRealServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("disabled", 3))
    )


_SlbNewCfgRealServerState_Type.__name__ = "Integer32"
_SlbNewCfgRealServerState_Object = MibTableColumn
slbNewCfgRealServerState = _SlbNewCfgRealServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 10),
    _SlbNewCfgRealServerState_Type()
)
slbNewCfgRealServerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerState.setStatus("current")


class _SlbNewCfgRealServerDelete_Type(Integer32):
    """Custom type slbNewCfgRealServerDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgRealServerDelete_Type.__name__ = "Integer32"
_SlbNewCfgRealServerDelete_Object = MibTableColumn
slbNewCfgRealServerDelete = _SlbNewCfgRealServerDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 11),
    _SlbNewCfgRealServerDelete_Type()
)
slbNewCfgRealServerDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerDelete.setStatus("current")


class _SlbNewCfgRealServerType_Type(Integer32):
    """Custom type slbNewCfgRealServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-server", 1),
          ("remote-server", 2))
    )


_SlbNewCfgRealServerType_Type.__name__ = "Integer32"
_SlbNewCfgRealServerType_Object = MibTableColumn
slbNewCfgRealServerType = _SlbNewCfgRealServerType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 12),
    _SlbNewCfgRealServerType_Type()
)
slbNewCfgRealServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerType.setStatus("current")


class _SlbNewCfgRealServerName_Type(DisplayString):
    """Custom type slbNewCfgRealServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlbNewCfgRealServerName_Type.__name__ = "DisplayString"
_SlbNewCfgRealServerName_Object = MibTableColumn
slbNewCfgRealServerName = _SlbNewCfgRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 13),
    _SlbNewCfgRealServerName_Type()
)
slbNewCfgRealServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerName.setStatus("current")
_SlbNewCfgRealServerUrlBmap_Type = OctetString
_SlbNewCfgRealServerUrlBmap_Object = MibTableColumn
slbNewCfgRealServerUrlBmap = _SlbNewCfgRealServerUrlBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 14),
    _SlbNewCfgRealServerUrlBmap_Type()
)
slbNewCfgRealServerUrlBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgRealServerUrlBmap.setStatus("current")
_SlbNewCfgRealServerAddUrl_Type = Integer32
_SlbNewCfgRealServerAddUrl_Object = MibTableColumn
slbNewCfgRealServerAddUrl = _SlbNewCfgRealServerAddUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 15),
    _SlbNewCfgRealServerAddUrl_Type()
)
slbNewCfgRealServerAddUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerAddUrl.setStatus("current")
_SlbNewCfgRealServerRemUrl_Type = Integer32
_SlbNewCfgRealServerRemUrl_Object = MibTableColumn
slbNewCfgRealServerRemUrl = _SlbNewCfgRealServerRemUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 16),
    _SlbNewCfgRealServerRemUrl_Type()
)
slbNewCfgRealServerRemUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerRemUrl.setStatus("current")


class _SlbNewCfgRealServerCookie_Type(Integer32):
    """Custom type slbNewCfgRealServerCookie based on Integer32"""
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


_SlbNewCfgRealServerCookie_Type.__name__ = "Integer32"
_SlbNewCfgRealServerCookie_Object = MibTableColumn
slbNewCfgRealServerCookie = _SlbNewCfgRealServerCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 17),
    _SlbNewCfgRealServerCookie_Type()
)
slbNewCfgRealServerCookie.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerCookie.setStatus("current")


class _SlbNewCfgRealServerExcludeStr_Type(Integer32):
    """Custom type slbNewCfgRealServerExcludeStr based on Integer32"""
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


_SlbNewCfgRealServerExcludeStr_Type.__name__ = "Integer32"
_SlbNewCfgRealServerExcludeStr_Object = MibTableColumn
slbNewCfgRealServerExcludeStr = _SlbNewCfgRealServerExcludeStr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 18),
    _SlbNewCfgRealServerExcludeStr_Type()
)
slbNewCfgRealServerExcludeStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerExcludeStr.setStatus("current")


class _SlbNewCfgRealServerSubmac_Type(Integer32):
    """Custom type slbNewCfgRealServerSubmac based on Integer32"""
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


_SlbNewCfgRealServerSubmac_Type.__name__ = "Integer32"
_SlbNewCfgRealServerSubmac_Object = MibTableColumn
slbNewCfgRealServerSubmac = _SlbNewCfgRealServerSubmac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 19),
    _SlbNewCfgRealServerSubmac_Type()
)
slbNewCfgRealServerSubmac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerSubmac.setStatus("current")


class _SlbNewCfgRealServerProxy_Type(Integer32):
    """Custom type slbNewCfgRealServerProxy based on Integer32"""
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


_SlbNewCfgRealServerProxy_Type.__name__ = "Integer32"
_SlbNewCfgRealServerProxy_Object = MibTableColumn
slbNewCfgRealServerProxy = _SlbNewCfgRealServerProxy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 20),
    _SlbNewCfgRealServerProxy_Type()
)
slbNewCfgRealServerProxy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerProxy.setStatus("current")


class _SlbNewCfgRealServerLdapwr_Type(Integer32):
    """Custom type slbNewCfgRealServerLdapwr based on Integer32"""
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


_SlbNewCfgRealServerLdapwr_Type.__name__ = "Integer32"
_SlbNewCfgRealServerLdapwr_Object = MibTableColumn
slbNewCfgRealServerLdapwr = _SlbNewCfgRealServerLdapwr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 21),
    _SlbNewCfgRealServerLdapwr_Type()
)
slbNewCfgRealServerLdapwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerLdapwr.setStatus("current")


class _SlbNewCfgRealServerOid_Type(DisplayString):
    """Custom type slbNewCfgRealServerOid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SlbNewCfgRealServerOid_Type.__name__ = "DisplayString"
_SlbNewCfgRealServerOid_Object = MibTableColumn
slbNewCfgRealServerOid = _SlbNewCfgRealServerOid_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 22),
    _SlbNewCfgRealServerOid_Type()
)
slbNewCfgRealServerOid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerOid.setStatus("current")


class _SlbNewCfgRealServerCommString_Type(DisplayString):
    """Custom type slbNewCfgRealServerCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbNewCfgRealServerCommString_Type.__name__ = "DisplayString"
_SlbNewCfgRealServerCommString_Object = MibTableColumn
slbNewCfgRealServerCommString = _SlbNewCfgRealServerCommString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 23),
    _SlbNewCfgRealServerCommString_Type()
)
slbNewCfgRealServerCommString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerCommString.setStatus("current")


class _SlbNewCfgRealServerIdsvlan_Type(Integer32):
    """Custom type slbNewCfgRealServerIdsvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4090),
    )


_SlbNewCfgRealServerIdsvlan_Type.__name__ = "Integer32"
_SlbNewCfgRealServerIdsvlan_Object = MibTableColumn
slbNewCfgRealServerIdsvlan = _SlbNewCfgRealServerIdsvlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 24),
    _SlbNewCfgRealServerIdsvlan_Type()
)
slbNewCfgRealServerIdsvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerIdsvlan.setStatus("current")
_SlbNewCfgRealServerIdsport_Type = Integer32
_SlbNewCfgRealServerIdsport_Object = MibTableColumn
slbNewCfgRealServerIdsport = _SlbNewCfgRealServerIdsport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 25),
    _SlbNewCfgRealServerIdsport_Type()
)
slbNewCfgRealServerIdsport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerIdsport.setStatus("current")


class _SlbNewCfgRealServerAvail_Type(Integer32):
    """Custom type slbNewCfgRealServerAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SlbNewCfgRealServerAvail_Type.__name__ = "Integer32"
_SlbNewCfgRealServerAvail_Object = MibTableColumn
slbNewCfgRealServerAvail = _SlbNewCfgRealServerAvail_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 26),
    _SlbNewCfgRealServerAvail_Type()
)
slbNewCfgRealServerAvail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerAvail.setStatus("current")


class _SlbNewCfgRealServerFastHealthCheck_Type(Integer32):
    """Custom type slbNewCfgRealServerFastHealthCheck based on Integer32"""
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


_SlbNewCfgRealServerFastHealthCheck_Type.__name__ = "Integer32"
_SlbNewCfgRealServerFastHealthCheck_Object = MibTableColumn
slbNewCfgRealServerFastHealthCheck = _SlbNewCfgRealServerFastHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 27),
    _SlbNewCfgRealServerFastHealthCheck_Type()
)
slbNewCfgRealServerFastHealthCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerFastHealthCheck.setStatus("current")


class _SlbNewCfgRealServerSubdmac_Type(Integer32):
    """Custom type slbNewCfgRealServerSubdmac based on Integer32"""
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


_SlbNewCfgRealServerSubdmac_Type.__name__ = "Integer32"
_SlbNewCfgRealServerSubdmac_Object = MibTableColumn
slbNewCfgRealServerSubdmac = _SlbNewCfgRealServerSubdmac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 28),
    _SlbNewCfgRealServerSubdmac_Type()
)
slbNewCfgRealServerSubdmac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerSubdmac.setStatus("current")


class _SlbNewCfgRealServerOverflow_Type(Integer32):
    """Custom type slbNewCfgRealServerOverflow based on Integer32"""
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


_SlbNewCfgRealServerOverflow_Type.__name__ = "Integer32"
_SlbNewCfgRealServerOverflow_Object = MibTableColumn
slbNewCfgRealServerOverflow = _SlbNewCfgRealServerOverflow_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 3, 1, 29),
    _SlbNewCfgRealServerOverflow_Type()
)
slbNewCfgRealServerOverflow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServerOverflow.setStatus("current")
_SlbRealServPortTableMaxSize_Type = Integer32
_SlbRealServPortTableMaxSize_Object = MibScalar
slbRealServPortTableMaxSize = _SlbRealServPortTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 4),
    _SlbRealServPortTableMaxSize_Type()
)
slbRealServPortTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServPortTableMaxSize.setStatus("current")
_SlbCurCfgRealServPortTable_Object = MibTable
slbCurCfgRealServPortTable = _SlbCurCfgRealServPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    slbCurCfgRealServPortTable.setStatus("current")
_SlbCurCfgRealServPortEntry_Object = MibTableRow
slbCurCfgRealServPortEntry = _SlbCurCfgRealServPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 5, 1)
)
slbCurCfgRealServPortEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServPortIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgRealServPortEntry.setStatus("current")
_SlbCurCfgRealServIndex_Type = Integer32
_SlbCurCfgRealServIndex_Object = MibTableColumn
slbCurCfgRealServIndex = _SlbCurCfgRealServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 5, 1, 1),
    _SlbCurCfgRealServIndex_Type()
)
slbCurCfgRealServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServIndex.setStatus("current")
_SlbCurCfgRealServPortIndex_Type = Integer32
_SlbCurCfgRealServPortIndex_Object = MibTableColumn
slbCurCfgRealServPortIndex = _SlbCurCfgRealServPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 5, 1, 2),
    _SlbCurCfgRealServPortIndex_Type()
)
slbCurCfgRealServPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServPortIndex.setStatus("current")


class _SlbCurCfgRealServRealPort_Type(Integer32):
    """Custom type slbCurCfgRealServRealPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65534),
    )


_SlbCurCfgRealServRealPort_Type.__name__ = "Integer32"
_SlbCurCfgRealServRealPort_Object = MibTableColumn
slbCurCfgRealServRealPort = _SlbCurCfgRealServRealPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 5, 1, 3),
    _SlbCurCfgRealServRealPort_Type()
)
slbCurCfgRealServRealPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServRealPort.setStatus("current")
_SlbNewCfgRealServPortTable_Object = MibTable
slbNewCfgRealServPortTable = _SlbNewCfgRealServPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    slbNewCfgRealServPortTable.setStatus("current")
_SlbNewCfgRealServPortEntry_Object = MibTableRow
slbNewCfgRealServPortEntry = _SlbNewCfgRealServPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 6, 1)
)
slbNewCfgRealServPortEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgRealServIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgRealServPortIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgRealServPortEntry.setStatus("current")
_SlbNewCfgRealServIndex_Type = Integer32
_SlbNewCfgRealServIndex_Object = MibTableColumn
slbNewCfgRealServIndex = _SlbNewCfgRealServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 6, 1, 1),
    _SlbNewCfgRealServIndex_Type()
)
slbNewCfgRealServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgRealServIndex.setStatus("current")
_SlbNewCfgRealServPortIndex_Type = Integer32
_SlbNewCfgRealServPortIndex_Object = MibTableColumn
slbNewCfgRealServPortIndex = _SlbNewCfgRealServPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 6, 1, 2),
    _SlbNewCfgRealServPortIndex_Type()
)
slbNewCfgRealServPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgRealServPortIndex.setStatus("current")


class _SlbNewCfgRealServRealPort_Type(Integer32):
    """Custom type slbNewCfgRealServRealPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65534),
    )


_SlbNewCfgRealServRealPort_Type.__name__ = "Integer32"
_SlbNewCfgRealServRealPort_Object = MibTableColumn
slbNewCfgRealServRealPort = _SlbNewCfgRealServRealPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 6, 1, 3),
    _SlbNewCfgRealServRealPort_Type()
)
slbNewCfgRealServRealPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServRealPort.setStatus("current")


class _SlbNewCfgRealServPortDelete_Type(Integer32):
    """Custom type slbNewCfgRealServPortDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgRealServPortDelete_Type.__name__ = "Integer32"
_SlbNewCfgRealServPortDelete_Object = MibTableColumn
slbNewCfgRealServPortDelete = _SlbNewCfgRealServPortDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 6, 1, 4),
    _SlbNewCfgRealServPortDelete_Type()
)
slbNewCfgRealServPortDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgRealServPortDelete.setStatus("current")
_SlbBuddyTableMaxSize_Type = Integer32
_SlbBuddyTableMaxSize_Object = MibScalar
slbBuddyTableMaxSize = _SlbBuddyTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 7),
    _SlbBuddyTableMaxSize_Type()
)
slbBuddyTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbBuddyTableMaxSize.setStatus("current")
_SlbCurCfgBuddyTable_Object = MibTable
slbCurCfgBuddyTable = _SlbCurCfgBuddyTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    slbCurCfgBuddyTable.setStatus("current")
_SlbCurCfgBuddyEntry_Object = MibTableRow
slbCurCfgBuddyEntry = _SlbCurCfgBuddyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 8, 1)
)
slbCurCfgBuddyEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealSerIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgBuddyIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgBuddyEntry.setStatus("current")
_SlbCurCfgRealSerIndex_Type = Integer32
_SlbCurCfgRealSerIndex_Object = MibTableColumn
slbCurCfgRealSerIndex = _SlbCurCfgRealSerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 8, 1, 1),
    _SlbCurCfgRealSerIndex_Type()
)
slbCurCfgRealSerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealSerIndex.setStatus("current")
_SlbCurCfgBuddyIndex_Type = Integer32
_SlbCurCfgBuddyIndex_Object = MibTableColumn
slbCurCfgBuddyIndex = _SlbCurCfgBuddyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 8, 1, 2),
    _SlbCurCfgBuddyIndex_Type()
)
slbCurCfgBuddyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgBuddyIndex.setStatus("current")
_SlbCurCfgBuddyRealIndex_Type = Integer32
_SlbCurCfgBuddyRealIndex_Object = MibTableColumn
slbCurCfgBuddyRealIndex = _SlbCurCfgBuddyRealIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 8, 1, 3),
    _SlbCurCfgBuddyRealIndex_Type()
)
slbCurCfgBuddyRealIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgBuddyRealIndex.setStatus("current")
_SlbCurCfgBuddyGroupIndex_Type = Integer32
_SlbCurCfgBuddyGroupIndex_Object = MibTableColumn
slbCurCfgBuddyGroupIndex = _SlbCurCfgBuddyGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 8, 1, 4),
    _SlbCurCfgBuddyGroupIndex_Type()
)
slbCurCfgBuddyGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgBuddyGroupIndex.setStatus("current")


class _SlbCurCfgBuddyService_Type(Integer32):
    """Custom type slbCurCfgBuddyService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 65534),
    )


_SlbCurCfgBuddyService_Type.__name__ = "Integer32"
_SlbCurCfgBuddyService_Object = MibTableColumn
slbCurCfgBuddyService = _SlbCurCfgBuddyService_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 8, 1, 5),
    _SlbCurCfgBuddyService_Type()
)
slbCurCfgBuddyService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgBuddyService.setStatus("current")
_SlbNewCfgBuddyTable_Object = MibTable
slbNewCfgBuddyTable = _SlbNewCfgBuddyTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    slbNewCfgBuddyTable.setStatus("current")
_SlbNewCfgBuddyEntry_Object = MibTableRow
slbNewCfgBuddyEntry = _SlbNewCfgBuddyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 9, 1)
)
slbNewCfgBuddyEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgRealSerIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgBuddyIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgBuddyEntry.setStatus("current")
_SlbNewCfgRealSerIndex_Type = Integer32
_SlbNewCfgRealSerIndex_Object = MibTableColumn
slbNewCfgRealSerIndex = _SlbNewCfgRealSerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 9, 1, 1),
    _SlbNewCfgRealSerIndex_Type()
)
slbNewCfgRealSerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgRealSerIndex.setStatus("current")
_SlbNewCfgBuddyIndex_Type = Integer32
_SlbNewCfgBuddyIndex_Object = MibTableColumn
slbNewCfgBuddyIndex = _SlbNewCfgBuddyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 9, 1, 2),
    _SlbNewCfgBuddyIndex_Type()
)
slbNewCfgBuddyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgBuddyIndex.setStatus("current")
_SlbNewCfgBuddyRealIndex_Type = Integer32
_SlbNewCfgBuddyRealIndex_Object = MibTableColumn
slbNewCfgBuddyRealIndex = _SlbNewCfgBuddyRealIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 9, 1, 3),
    _SlbNewCfgBuddyRealIndex_Type()
)
slbNewCfgBuddyRealIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgBuddyRealIndex.setStatus("current")
_SlbNewCfgBuddyGroupIndex_Type = Integer32
_SlbNewCfgBuddyGroupIndex_Object = MibTableColumn
slbNewCfgBuddyGroupIndex = _SlbNewCfgBuddyGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 9, 1, 4),
    _SlbNewCfgBuddyGroupIndex_Type()
)
slbNewCfgBuddyGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgBuddyGroupIndex.setStatus("current")


class _SlbNewCfgBuddyService_Type(Integer32):
    """Custom type slbNewCfgBuddyService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 65534),
    )


_SlbNewCfgBuddyService_Type.__name__ = "Integer32"
_SlbNewCfgBuddyService_Object = MibTableColumn
slbNewCfgBuddyService = _SlbNewCfgBuddyService_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 9, 1, 5),
    _SlbNewCfgBuddyService_Type()
)
slbNewCfgBuddyService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgBuddyService.setStatus("current")


class _SlbNewCfgBuddyDelete_Type(Integer32):
    """Custom type slbNewCfgBuddyDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgBuddyDelete_Type.__name__ = "Integer32"
_SlbNewCfgBuddyDelete_Object = MibTableColumn
slbNewCfgBuddyDelete = _SlbNewCfgBuddyDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 2, 9, 1, 6),
    _SlbNewCfgBuddyDelete_Type()
)
slbNewCfgBuddyDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgBuddyDelete.setStatus("current")
_RealServerGroupCfg_ObjectIdentity = ObjectIdentity
realServerGroupCfg = _RealServerGroupCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3)
)
_SlbGroupTableMaxSize_Type = Integer32
_SlbGroupTableMaxSize_Object = MibScalar
slbGroupTableMaxSize = _SlbGroupTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 1),
    _SlbGroupTableMaxSize_Type()
)
slbGroupTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbGroupTableMaxSize.setStatus("current")
_SlbGroupMaxIdsSize_Type = Integer32
_SlbGroupMaxIdsSize_Object = MibScalar
slbGroupMaxIdsSize = _SlbGroupMaxIdsSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 2),
    _SlbGroupMaxIdsSize_Type()
)
slbGroupMaxIdsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbGroupMaxIdsSize.setStatus("current")
_SlbCurCfgGroupTable_Object = MibTable
slbCurCfgGroupTable = _SlbCurCfgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    slbCurCfgGroupTable.setStatus("current")
_SlbCurCfgGroupEntry_Object = MibTableRow
slbCurCfgGroupEntry = _SlbCurCfgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1)
)
slbCurCfgGroupEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgGroupIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgGroupEntry.setStatus("current")
_SlbCurCfgGroupIndex_Type = Integer32
_SlbCurCfgGroupIndex_Object = MibTableColumn
slbCurCfgGroupIndex = _SlbCurCfgGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 1),
    _SlbCurCfgGroupIndex_Type()
)
slbCurCfgGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupIndex.setStatus("current")
_SlbCurCfgGroupRealServers_Type = OctetString
_SlbCurCfgGroupRealServers_Object = MibTableColumn
slbCurCfgGroupRealServers = _SlbCurCfgGroupRealServers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 2),
    _SlbCurCfgGroupRealServers_Type()
)
slbCurCfgGroupRealServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupRealServers.setStatus("current")


class _SlbCurCfgGroupMetric_Type(Integer32):
    """Custom type slbCurCfgGroupMetric based on Integer32"""
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
        *(("roundRobin", 1),
          ("leastConnections", 2),
          ("minMisses", 3),
          ("hash", 4),
          ("response", 5),
          ("bandwidth", 6),
          ("phash", 7))
    )


_SlbCurCfgGroupMetric_Type.__name__ = "Integer32"
_SlbCurCfgGroupMetric_Object = MibTableColumn
slbCurCfgGroupMetric = _SlbCurCfgGroupMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 3),
    _SlbCurCfgGroupMetric_Type()
)
slbCurCfgGroupMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupMetric.setStatus("current")
_SlbCurCfgGroupBackupServer_Type = Integer32
_SlbCurCfgGroupBackupServer_Object = MibTableColumn
slbCurCfgGroupBackupServer = _SlbCurCfgGroupBackupServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 4),
    _SlbCurCfgGroupBackupServer_Type()
)
slbCurCfgGroupBackupServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupBackupServer.setStatus("current")
_SlbCurCfgGroupBackupGroup_Type = Integer32
_SlbCurCfgGroupBackupGroup_Object = MibTableColumn
slbCurCfgGroupBackupGroup = _SlbCurCfgGroupBackupGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 5),
    _SlbCurCfgGroupBackupGroup_Type()
)
slbCurCfgGroupBackupGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupBackupGroup.setStatus("current")


class _SlbCurCfgGroupHealthCheckUrl_Type(DisplayString):
    """Custom type slbCurCfgGroupHealthCheckUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SlbCurCfgGroupHealthCheckUrl_Type.__name__ = "DisplayString"
_SlbCurCfgGroupHealthCheckUrl_Object = MibTableColumn
slbCurCfgGroupHealthCheckUrl = _SlbCurCfgGroupHealthCheckUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 6),
    _SlbCurCfgGroupHealthCheckUrl_Type()
)
slbCurCfgGroupHealthCheckUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupHealthCheckUrl.setStatus("current")


class _SlbCurCfgGroupHealthCheckLayer_Type(Integer32):
    """Custom type slbCurCfgGroupHealthCheckLayer based on Integer32"""
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("tcp", 2),
          ("http", 3),
          ("dns", 4),
          ("smtp", 5),
          ("pop3", 6),
          ("nntp", 7),
          ("ftp", 8),
          ("imap", 9),
          ("radius", 10),
          ("sslh", 11),
          ("script1", 12),
          ("script2", 13),
          ("script3", 14),
          ("script4", 15),
          ("script5", 16),
          ("script6", 17),
          ("script7", 18),
          ("script8", 19),
          ("script9", 20),
          ("script10", 21),
          ("script11", 22),
          ("script12", 23),
          ("script13", 24),
          ("script14", 25),
          ("script15", 26),
          ("script16", 27),
          ("link", 28),
          ("wsp", 29),
          ("wtls", 30),
          ("ldap", 31),
          ("udpdns", 32),
          ("arp", 33),
          ("snmp1", 34),
          ("snmp2", 35),
          ("snmp3", 36),
          ("snmp4", 37),
          ("snmp5", 38),
          ("radiusacs", 39),
          ("tftp", 40),
          ("wtp", 41),
          ("rtsp", 42),
          ("sipping", 43),
          ("httphead", 44),
          ("sipoptions", 45),
          ("wts", 46),
          ("script17", 116),
          ("script18", 117),
          ("script19", 118),
          ("script20", 119),
          ("script21", 120),
          ("script22", 121),
          ("script23", 122),
          ("script24", 123),
          ("script25", 124),
          ("script26", 125),
          ("script27", 126),
          ("script28", 127),
          ("script29", 128),
          ("script30", 129),
          ("script31", 130),
          ("script32", 131),
          ("script33", 132),
          ("script34", 133),
          ("script35", 134),
          ("script36", 135),
          ("script37", 136),
          ("script38", 137),
          ("script39", 138),
          ("script40", 139),
          ("script41", 140),
          ("script42", 141),
          ("script43", 142),
          ("script44", 143),
          ("script45", 144),
          ("script46", 145),
          ("script47", 146),
          ("script48", 147),
          ("script49", 148),
          ("script50", 149),
          ("script51", 150),
          ("script52", 151),
          ("script53", 152),
          ("script54", 153),
          ("script55", 154),
          ("script56", 155),
          ("script57", 156),
          ("script58", 157),
          ("script59", 158),
          ("script60", 159),
          ("script61", 160),
          ("script62", 161),
          ("script63", 162),
          ("script64", 163))
    )


_SlbCurCfgGroupHealthCheckLayer_Type.__name__ = "Integer32"
_SlbCurCfgGroupHealthCheckLayer_Object = MibTableColumn
slbCurCfgGroupHealthCheckLayer = _SlbCurCfgGroupHealthCheckLayer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 7),
    _SlbCurCfgGroupHealthCheckLayer_Type()
)
slbCurCfgGroupHealthCheckLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupHealthCheckLayer.setStatus("current")


class _SlbCurCfgGroupName_Type(DisplayString):
    """Custom type slbCurCfgGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlbCurCfgGroupName_Type.__name__ = "DisplayString"
_SlbCurCfgGroupName_Object = MibTableColumn
slbCurCfgGroupName = _SlbCurCfgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 8),
    _SlbCurCfgGroupName_Type()
)
slbCurCfgGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupName.setStatus("current")


class _SlbCurCfgGroupRealThreshold_Type(Integer32):
    """Custom type slbCurCfgGroupRealThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlbCurCfgGroupRealThreshold_Type.__name__ = "Integer32"
_SlbCurCfgGroupRealThreshold_Object = MibTableColumn
slbCurCfgGroupRealThreshold = _SlbCurCfgGroupRealThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 9),
    _SlbCurCfgGroupRealThreshold_Type()
)
slbCurCfgGroupRealThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupRealThreshold.setStatus("current")


class _SlbCurCfgGroupVipHealthCheck_Type(Integer32):
    """Custom type slbCurCfgGroupVipHealthCheck based on Integer32"""
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


_SlbCurCfgGroupVipHealthCheck_Type.__name__ = "Integer32"
_SlbCurCfgGroupVipHealthCheck_Object = MibTableColumn
slbCurCfgGroupVipHealthCheck = _SlbCurCfgGroupVipHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 10),
    _SlbCurCfgGroupVipHealthCheck_Type()
)
slbCurCfgGroupVipHealthCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupVipHealthCheck.setStatus("current")


class _SlbCurCfgGroupIdsState_Type(Integer32):
    """Custom type slbCurCfgGroupIdsState based on Integer32"""
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


_SlbCurCfgGroupIdsState_Type.__name__ = "Integer32"
_SlbCurCfgGroupIdsState_Object = MibTableColumn
slbCurCfgGroupIdsState = _SlbCurCfgGroupIdsState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 11),
    _SlbCurCfgGroupIdsState_Type()
)
slbCurCfgGroupIdsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupIdsState.setStatus("current")


class _SlbCurCfgGroupIdsPort_Type(Integer32):
    """Custom type slbCurCfgGroupIdsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbCurCfgGroupIdsPort_Type.__name__ = "Integer32"
_SlbCurCfgGroupIdsPort_Object = MibTableColumn
slbCurCfgGroupIdsPort = _SlbCurCfgGroupIdsPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 12),
    _SlbCurCfgGroupIdsPort_Type()
)
slbCurCfgGroupIdsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupIdsPort.setStatus("current")


class _SlbCurCfgGroupIdsFlood_Type(Integer32):
    """Custom type slbCurCfgGroupIdsFlood based on Integer32"""
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


_SlbCurCfgGroupIdsFlood_Type.__name__ = "Integer32"
_SlbCurCfgGroupIdsFlood_Object = MibTableColumn
slbCurCfgGroupIdsFlood = _SlbCurCfgGroupIdsFlood_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 13),
    _SlbCurCfgGroupIdsFlood_Type()
)
slbCurCfgGroupIdsFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupIdsFlood.setStatus("current")


class _SlbCurCfgGroupMinmissHash_Type(Integer32):
    """Custom type slbCurCfgGroupMinmissHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("minmiss-24", 1),
          ("minmiss-32", 2))
    )


_SlbCurCfgGroupMinmissHash_Type.__name__ = "Integer32"
_SlbCurCfgGroupMinmissHash_Object = MibTableColumn
slbCurCfgGroupMinmissHash = _SlbCurCfgGroupMinmissHash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 14),
    _SlbCurCfgGroupMinmissHash_Type()
)
slbCurCfgGroupMinmissHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupMinmissHash.setStatus("current")
_SlbCurCfgGroupPhashMask_Type = IpAddress
_SlbCurCfgGroupPhashMask_Object = MibTableColumn
slbCurCfgGroupPhashMask = _SlbCurCfgGroupPhashMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 15),
    _SlbCurCfgGroupPhashMask_Type()
)
slbCurCfgGroupPhashMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupPhashMask.setStatus("current")


class _SlbCurCfgGroupRmetric_Type(Integer32):
    """Custom type slbCurCfgGroupRmetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roundRobin", 1),
          ("hash", 2))
    )


_SlbCurCfgGroupRmetric_Type.__name__ = "Integer32"
_SlbCurCfgGroupRmetric_Object = MibTableColumn
slbCurCfgGroupRmetric = _SlbCurCfgGroupRmetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 16),
    _SlbCurCfgGroupRmetric_Type()
)
slbCurCfgGroupRmetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupRmetric.setStatus("current")


class _SlbCurCfgGroupHealthCheckFormula_Type(DisplayString):
    """Custom type slbCurCfgGroupHealthCheckFormula based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlbCurCfgGroupHealthCheckFormula_Type.__name__ = "DisplayString"
_SlbCurCfgGroupHealthCheckFormula_Object = MibTableColumn
slbCurCfgGroupHealthCheckFormula = _SlbCurCfgGroupHealthCheckFormula_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 17),
    _SlbCurCfgGroupHealthCheckFormula_Type()
)
slbCurCfgGroupHealthCheckFormula.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupHealthCheckFormula.setStatus("current")


class _SlbCurCfgGroupOperatorAccess_Type(Integer32):
    """Custom type slbCurCfgGroupOperatorAccess based on Integer32"""
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


_SlbCurCfgGroupOperatorAccess_Type.__name__ = "Integer32"
_SlbCurCfgGroupOperatorAccess_Object = MibTableColumn
slbCurCfgGroupOperatorAccess = _SlbCurCfgGroupOperatorAccess_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 18),
    _SlbCurCfgGroupOperatorAccess_Type()
)
slbCurCfgGroupOperatorAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupOperatorAccess.setStatus("current")
_SlbCurCfgGroupWlm_Type = Integer32
_SlbCurCfgGroupWlm_Object = MibTableColumn
slbCurCfgGroupWlm = _SlbCurCfgGroupWlm_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 3, 1, 19),
    _SlbCurCfgGroupWlm_Type()
)
slbCurCfgGroupWlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupWlm.setStatus("current")
_SlbNewCfgGroupTable_Object = MibTable
slbNewCfgGroupTable = _SlbNewCfgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    slbNewCfgGroupTable.setStatus("current")
_SlbNewCfgGroupEntry_Object = MibTableRow
slbNewCfgGroupEntry = _SlbNewCfgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1)
)
slbNewCfgGroupEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgGroupIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgGroupEntry.setStatus("current")
_SlbNewCfgGroupIndex_Type = Integer32
_SlbNewCfgGroupIndex_Object = MibTableColumn
slbNewCfgGroupIndex = _SlbNewCfgGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 1),
    _SlbNewCfgGroupIndex_Type()
)
slbNewCfgGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgGroupIndex.setStatus("current")
_SlbNewCfgGroupRealServers_Type = OctetString
_SlbNewCfgGroupRealServers_Object = MibTableColumn
slbNewCfgGroupRealServers = _SlbNewCfgGroupRealServers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 2),
    _SlbNewCfgGroupRealServers_Type()
)
slbNewCfgGroupRealServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgGroupRealServers.setStatus("current")
_SlbNewCfgGroupAddServer_Type = Integer32
_SlbNewCfgGroupAddServer_Object = MibTableColumn
slbNewCfgGroupAddServer = _SlbNewCfgGroupAddServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 3),
    _SlbNewCfgGroupAddServer_Type()
)
slbNewCfgGroupAddServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupAddServer.setStatus("current")
_SlbNewCfgGroupRemoveServer_Type = Integer32
_SlbNewCfgGroupRemoveServer_Object = MibTableColumn
slbNewCfgGroupRemoveServer = _SlbNewCfgGroupRemoveServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 4),
    _SlbNewCfgGroupRemoveServer_Type()
)
slbNewCfgGroupRemoveServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupRemoveServer.setStatus("current")


class _SlbNewCfgGroupMetric_Type(Integer32):
    """Custom type slbNewCfgGroupMetric based on Integer32"""
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
        *(("roundRobin", 1),
          ("leastConnections", 2),
          ("minMisses", 3),
          ("hash", 4),
          ("response", 5),
          ("bandwidth", 6),
          ("phash", 7))
    )


_SlbNewCfgGroupMetric_Type.__name__ = "Integer32"
_SlbNewCfgGroupMetric_Object = MibTableColumn
slbNewCfgGroupMetric = _SlbNewCfgGroupMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 5),
    _SlbNewCfgGroupMetric_Type()
)
slbNewCfgGroupMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupMetric.setStatus("current")
_SlbNewCfgGroupBackupServer_Type = Integer32
_SlbNewCfgGroupBackupServer_Object = MibTableColumn
slbNewCfgGroupBackupServer = _SlbNewCfgGroupBackupServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 6),
    _SlbNewCfgGroupBackupServer_Type()
)
slbNewCfgGroupBackupServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupBackupServer.setStatus("current")
_SlbNewCfgGroupBackupGroup_Type = Integer32
_SlbNewCfgGroupBackupGroup_Object = MibTableColumn
slbNewCfgGroupBackupGroup = _SlbNewCfgGroupBackupGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 7),
    _SlbNewCfgGroupBackupGroup_Type()
)
slbNewCfgGroupBackupGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupBackupGroup.setStatus("current")


class _SlbNewCfgGroupHealthCheckUrl_Type(DisplayString):
    """Custom type slbNewCfgGroupHealthCheckUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SlbNewCfgGroupHealthCheckUrl_Type.__name__ = "DisplayString"
_SlbNewCfgGroupHealthCheckUrl_Object = MibTableColumn
slbNewCfgGroupHealthCheckUrl = _SlbNewCfgGroupHealthCheckUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 8),
    _SlbNewCfgGroupHealthCheckUrl_Type()
)
slbNewCfgGroupHealthCheckUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupHealthCheckUrl.setStatus("current")


class _SlbNewCfgGroupHealthCheckLayer_Type(Integer32):
    """Custom type slbNewCfgGroupHealthCheckLayer based on Integer32"""
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
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("tcp", 2),
          ("http", 3),
          ("dns", 4),
          ("smtp", 5),
          ("pop3", 6),
          ("nntp", 7),
          ("ftp", 8),
          ("imap", 9),
          ("radius", 10),
          ("sslh", 11),
          ("script1", 12),
          ("script2", 13),
          ("script3", 14),
          ("script4", 15),
          ("script5", 16),
          ("script6", 17),
          ("script7", 18),
          ("script8", 19),
          ("script9", 20),
          ("script10", 21),
          ("script11", 22),
          ("script12", 23),
          ("script13", 24),
          ("script14", 25),
          ("script15", 26),
          ("script16", 27),
          ("link", 28),
          ("wsp", 29),
          ("wtls", 30),
          ("ldap", 31),
          ("udpdns", 32),
          ("arp", 33),
          ("snmp1", 34),
          ("snmp2", 35),
          ("snmp3", 36),
          ("snmp4", 37),
          ("snmp5", 38),
          ("radiusacs", 39),
          ("tftp", 40),
          ("wtp", 41),
          ("rtsp", 42),
          ("sipping", 43),
          ("httphead", 44),
          ("sipoptions", 45),
          ("wts", 46),
          ("script17", 116),
          ("script18", 117),
          ("script19", 118),
          ("script20", 119),
          ("script21", 120),
          ("script22", 121),
          ("script23", 122),
          ("script24", 123),
          ("script25", 124),
          ("script26", 125),
          ("script27", 126),
          ("script28", 127),
          ("script29", 128),
          ("script30", 129),
          ("script31", 130),
          ("script32", 131),
          ("script33", 132),
          ("script34", 133),
          ("script35", 134),
          ("script36", 135),
          ("script37", 136),
          ("script38", 137),
          ("script39", 138),
          ("script40", 139),
          ("script41", 140),
          ("script42", 141),
          ("script43", 142),
          ("script44", 143),
          ("script45", 144),
          ("script46", 145),
          ("script47", 146),
          ("script48", 147),
          ("script49", 148),
          ("script50", 149),
          ("script51", 150),
          ("script52", 151),
          ("script53", 152),
          ("script54", 153),
          ("script55", 154),
          ("script56", 155),
          ("script57", 156),
          ("script58", 157),
          ("script59", 158),
          ("script60", 159),
          ("script61", 160),
          ("script62", 161),
          ("script63", 162),
          ("script64", 163))
    )


_SlbNewCfgGroupHealthCheckLayer_Type.__name__ = "Integer32"
_SlbNewCfgGroupHealthCheckLayer_Object = MibTableColumn
slbNewCfgGroupHealthCheckLayer = _SlbNewCfgGroupHealthCheckLayer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 9),
    _SlbNewCfgGroupHealthCheckLayer_Type()
)
slbNewCfgGroupHealthCheckLayer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupHealthCheckLayer.setStatus("current")


class _SlbNewCfgGroupName_Type(DisplayString):
    """Custom type slbNewCfgGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlbNewCfgGroupName_Type.__name__ = "DisplayString"
_SlbNewCfgGroupName_Object = MibTableColumn
slbNewCfgGroupName = _SlbNewCfgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 10),
    _SlbNewCfgGroupName_Type()
)
slbNewCfgGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupName.setStatus("current")


class _SlbNewCfgGroupRealThreshold_Type(Integer32):
    """Custom type slbNewCfgGroupRealThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlbNewCfgGroupRealThreshold_Type.__name__ = "Integer32"
_SlbNewCfgGroupRealThreshold_Object = MibTableColumn
slbNewCfgGroupRealThreshold = _SlbNewCfgGroupRealThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 11),
    _SlbNewCfgGroupRealThreshold_Type()
)
slbNewCfgGroupRealThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupRealThreshold.setStatus("current")


class _SlbNewCfgGroupVipHealthCheck_Type(Integer32):
    """Custom type slbNewCfgGroupVipHealthCheck based on Integer32"""
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


_SlbNewCfgGroupVipHealthCheck_Type.__name__ = "Integer32"
_SlbNewCfgGroupVipHealthCheck_Object = MibTableColumn
slbNewCfgGroupVipHealthCheck = _SlbNewCfgGroupVipHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 12),
    _SlbNewCfgGroupVipHealthCheck_Type()
)
slbNewCfgGroupVipHealthCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupVipHealthCheck.setStatus("current")


class _SlbNewCfgGroupIdsState_Type(Integer32):
    """Custom type slbNewCfgGroupIdsState based on Integer32"""
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


_SlbNewCfgGroupIdsState_Type.__name__ = "Integer32"
_SlbNewCfgGroupIdsState_Object = MibTableColumn
slbNewCfgGroupIdsState = _SlbNewCfgGroupIdsState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 13),
    _SlbNewCfgGroupIdsState_Type()
)
slbNewCfgGroupIdsState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupIdsState.setStatus("current")


class _SlbNewCfgGroupIdsPort_Type(Integer32):
    """Custom type slbNewCfgGroupIdsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbNewCfgGroupIdsPort_Type.__name__ = "Integer32"
_SlbNewCfgGroupIdsPort_Object = MibTableColumn
slbNewCfgGroupIdsPort = _SlbNewCfgGroupIdsPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 14),
    _SlbNewCfgGroupIdsPort_Type()
)
slbNewCfgGroupIdsPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupIdsPort.setStatus("current")


class _SlbNewCfgGroupDelete_Type(Integer32):
    """Custom type slbNewCfgGroupDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgGroupDelete_Type.__name__ = "Integer32"
_SlbNewCfgGroupDelete_Object = MibTableColumn
slbNewCfgGroupDelete = _SlbNewCfgGroupDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 15),
    _SlbNewCfgGroupDelete_Type()
)
slbNewCfgGroupDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupDelete.setStatus("current")


class _SlbNewCfgGroupIdsFlood_Type(Integer32):
    """Custom type slbNewCfgGroupIdsFlood based on Integer32"""
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


_SlbNewCfgGroupIdsFlood_Type.__name__ = "Integer32"
_SlbNewCfgGroupIdsFlood_Object = MibTableColumn
slbNewCfgGroupIdsFlood = _SlbNewCfgGroupIdsFlood_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 16),
    _SlbNewCfgGroupIdsFlood_Type()
)
slbNewCfgGroupIdsFlood.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupIdsFlood.setStatus("current")


class _SlbNewCfgGroupMinmissHash_Type(Integer32):
    """Custom type slbNewCfgGroupMinmissHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("minmiss-24", 1),
          ("minmiss-32", 2))
    )


_SlbNewCfgGroupMinmissHash_Type.__name__ = "Integer32"
_SlbNewCfgGroupMinmissHash_Object = MibTableColumn
slbNewCfgGroupMinmissHash = _SlbNewCfgGroupMinmissHash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 17),
    _SlbNewCfgGroupMinmissHash_Type()
)
slbNewCfgGroupMinmissHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupMinmissHash.setStatus("current")
_SlbNewCfgGroupPhashMask_Type = IpAddress
_SlbNewCfgGroupPhashMask_Object = MibTableColumn
slbNewCfgGroupPhashMask = _SlbNewCfgGroupPhashMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 18),
    _SlbNewCfgGroupPhashMask_Type()
)
slbNewCfgGroupPhashMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupPhashMask.setStatus("current")


class _SlbNewCfgGroupRmetric_Type(Integer32):
    """Custom type slbNewCfgGroupRmetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roundRobin", 1),
          ("hash", 2))
    )


_SlbNewCfgGroupRmetric_Type.__name__ = "Integer32"
_SlbNewCfgGroupRmetric_Object = MibTableColumn
slbNewCfgGroupRmetric = _SlbNewCfgGroupRmetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 19),
    _SlbNewCfgGroupRmetric_Type()
)
slbNewCfgGroupRmetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupRmetric.setStatus("current")


class _SlbNewCfgGroupHealthCheckFormula_Type(DisplayString):
    """Custom type slbNewCfgGroupHealthCheckFormula based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlbNewCfgGroupHealthCheckFormula_Type.__name__ = "DisplayString"
_SlbNewCfgGroupHealthCheckFormula_Object = MibTableColumn
slbNewCfgGroupHealthCheckFormula = _SlbNewCfgGroupHealthCheckFormula_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 20),
    _SlbNewCfgGroupHealthCheckFormula_Type()
)
slbNewCfgGroupHealthCheckFormula.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupHealthCheckFormula.setStatus("current")


class _SlbNewCfgGroupOperatorAccess_Type(Integer32):
    """Custom type slbNewCfgGroupOperatorAccess based on Integer32"""
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


_SlbNewCfgGroupOperatorAccess_Type.__name__ = "Integer32"
_SlbNewCfgGroupOperatorAccess_Object = MibTableColumn
slbNewCfgGroupOperatorAccess = _SlbNewCfgGroupOperatorAccess_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 21),
    _SlbNewCfgGroupOperatorAccess_Type()
)
slbNewCfgGroupOperatorAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupOperatorAccess.setStatus("current")
_SlbNewCfgGroupWlm_Type = Integer32
_SlbNewCfgGroupWlm_Object = MibTableColumn
slbNewCfgGroupWlm = _SlbNewCfgGroupWlm_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 4, 1, 22),
    _SlbNewCfgGroupWlm_Type()
)
slbNewCfgGroupWlm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupWlm.setStatus("current")
_SlbCurCfgGroupRealServerTable_Object = MibTable
slbCurCfgGroupRealServerTable = _SlbCurCfgGroupRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    slbCurCfgGroupRealServerTable.setStatus("current")
_SlbCurCfgGroupRealServerEntry_Object = MibTableRow
slbCurCfgGroupRealServerEntry = _SlbCurCfgGroupRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 5, 1)
)
slbCurCfgGroupRealServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgRealServGroupIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgGroupRealServIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgGroupRealServerEntry.setStatus("current")
_SlbCurCfgRealServGroupIndex_Type = Integer32
_SlbCurCfgRealServGroupIndex_Object = MibTableColumn
slbCurCfgRealServGroupIndex = _SlbCurCfgRealServGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 5, 1, 1),
    _SlbCurCfgRealServGroupIndex_Type()
)
slbCurCfgRealServGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServGroupIndex.setStatus("current")
_SlbCurCfgGroupRealServIndex_Type = Integer32
_SlbCurCfgGroupRealServIndex_Object = MibTableColumn
slbCurCfgGroupRealServIndex = _SlbCurCfgGroupRealServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 5, 1, 2),
    _SlbCurCfgGroupRealServIndex_Type()
)
slbCurCfgGroupRealServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupRealServIndex.setStatus("current")


class _SlbCurCfgGroupRealServerState_Type(Integer32):
    """Custom type slbCurCfgGroupRealServerState based on Integer32"""
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


_SlbCurCfgGroupRealServerState_Type.__name__ = "Integer32"
_SlbCurCfgGroupRealServerState_Object = MibTableColumn
slbCurCfgGroupRealServerState = _SlbCurCfgGroupRealServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 5, 1, 3),
    _SlbCurCfgGroupRealServerState_Type()
)
slbCurCfgGroupRealServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupRealServerState.setStatus("current")
_SlbNewCfgGroupRealServerTable_Object = MibTable
slbNewCfgGroupRealServerTable = _SlbNewCfgGroupRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    slbNewCfgGroupRealServerTable.setStatus("current")
_SlbNewCfgGroupRealServerEntry_Object = MibTableRow
slbNewCfgGroupRealServerEntry = _SlbNewCfgGroupRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 6, 1)
)
slbNewCfgGroupRealServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgRealServGroupIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgGroupRealServIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgGroupRealServerEntry.setStatus("current")
_SlbNewCfgRealServGroupIndex_Type = Integer32
_SlbNewCfgRealServGroupIndex_Object = MibTableColumn
slbNewCfgRealServGroupIndex = _SlbNewCfgRealServGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 6, 1, 1),
    _SlbNewCfgRealServGroupIndex_Type()
)
slbNewCfgRealServGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgRealServGroupIndex.setStatus("current")
_SlbNewCfgGroupRealServIndex_Type = Integer32
_SlbNewCfgGroupRealServIndex_Object = MibTableColumn
slbNewCfgGroupRealServIndex = _SlbNewCfgGroupRealServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 6, 1, 2),
    _SlbNewCfgGroupRealServIndex_Type()
)
slbNewCfgGroupRealServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgGroupRealServIndex.setStatus("current")


class _SlbNewCfgGroupRealServerState_Type(Integer32):
    """Custom type slbNewCfgGroupRealServerState based on Integer32"""
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


_SlbNewCfgGroupRealServerState_Type.__name__ = "Integer32"
_SlbNewCfgGroupRealServerState_Object = MibTableColumn
slbNewCfgGroupRealServerState = _SlbNewCfgGroupRealServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 3, 6, 1, 3),
    _SlbNewCfgGroupRealServerState_Type()
)
slbNewCfgGroupRealServerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgGroupRealServerState.setStatus("current")
_VirtualServerCfg_ObjectIdentity = ObjectIdentity
virtualServerCfg = _VirtualServerCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4)
)
_SlbVirtServerTableMaxSize_Type = Integer32
_SlbVirtServerTableMaxSize_Object = MibScalar
slbVirtServerTableMaxSize = _SlbVirtServerTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 1),
    _SlbVirtServerTableMaxSize_Type()
)
slbVirtServerTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtServerTableMaxSize.setStatus("current")
_SlbCurCfgVirtServerTable_Object = MibTable
slbCurCfgVirtServerTable = _SlbCurCfgVirtServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    slbCurCfgVirtServerTable.setStatus("current")
_SlbCurCfgVirtualServerEntry_Object = MibTableRow
slbCurCfgVirtualServerEntry = _SlbCurCfgVirtualServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 2, 1)
)
slbCurCfgVirtualServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgVirtServerIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgVirtualServerEntry.setStatus("current")
_SlbCurCfgVirtServerIndex_Type = Integer32
_SlbCurCfgVirtServerIndex_Object = MibTableColumn
slbCurCfgVirtServerIndex = _SlbCurCfgVirtServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 2, 1, 1),
    _SlbCurCfgVirtServerIndex_Type()
)
slbCurCfgVirtServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerIndex.setStatus("current")
_SlbCurCfgVirtServerIpAddress_Type = IpAddress
_SlbCurCfgVirtServerIpAddress_Object = MibTableColumn
slbCurCfgVirtServerIpAddress = _SlbCurCfgVirtServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 2, 1, 2),
    _SlbCurCfgVirtServerIpAddress_Type()
)
slbCurCfgVirtServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerIpAddress.setStatus("current")


class _SlbCurCfgVirtServerLayer3Only_Type(Integer32):
    """Custom type slbCurCfgVirtServerLayer3Only based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer3Only", 1),
          ("disabled", 2))
    )


_SlbCurCfgVirtServerLayer3Only_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerLayer3Only_Object = MibTableColumn
slbCurCfgVirtServerLayer3Only = _SlbCurCfgVirtServerLayer3Only_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 2, 1, 3),
    _SlbCurCfgVirtServerLayer3Only_Type()
)
slbCurCfgVirtServerLayer3Only.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerLayer3Only.setStatus("current")


class _SlbCurCfgVirtServerState_Type(Integer32):
    """Custom type slbCurCfgVirtServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("disabled", 3))
    )


_SlbCurCfgVirtServerState_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerState_Object = MibTableColumn
slbCurCfgVirtServerState = _SlbCurCfgVirtServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 2, 1, 4),
    _SlbCurCfgVirtServerState_Type()
)
slbCurCfgVirtServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerState.setStatus("current")


class _SlbCurCfgVirtServerDname_Type(DisplayString):
    """Custom type slbCurCfgVirtServerDname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlbCurCfgVirtServerDname_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServerDname_Object = MibTableColumn
slbCurCfgVirtServerDname = _SlbCurCfgVirtServerDname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 2, 1, 5),
    _SlbCurCfgVirtServerDname_Type()
)
slbCurCfgVirtServerDname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerDname.setStatus("current")
_SlbCurCfgVirtServerBwmContract_Type = Integer32
_SlbCurCfgVirtServerBwmContract_Object = MibTableColumn
slbCurCfgVirtServerBwmContract = _SlbCurCfgVirtServerBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 2, 1, 6),
    _SlbCurCfgVirtServerBwmContract_Type()
)
slbCurCfgVirtServerBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerBwmContract.setStatus("current")


class _SlbCurCfgVirtServerWeight_Type(Integer32):
    """Custom type slbCurCfgVirtServerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SlbCurCfgVirtServerWeight_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerWeight_Object = MibTableColumn
slbCurCfgVirtServerWeight = _SlbCurCfgVirtServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 2, 1, 7),
    _SlbCurCfgVirtServerWeight_Type()
)
slbCurCfgVirtServerWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerWeight.setStatus("current")


class _SlbCurCfgVirtServerAvail_Type(Integer32):
    """Custom type slbCurCfgVirtServerAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SlbCurCfgVirtServerAvail_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerAvail_Object = MibTableColumn
slbCurCfgVirtServerAvail = _SlbCurCfgVirtServerAvail_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 2, 1, 8),
    _SlbCurCfgVirtServerAvail_Type()
)
slbCurCfgVirtServerAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerAvail.setStatus("current")
_SlbCurCfgVirtServerRule_Type = OctetString
_SlbCurCfgVirtServerRule_Object = MibTableColumn
slbCurCfgVirtServerRule = _SlbCurCfgVirtServerRule_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 2, 1, 9),
    _SlbCurCfgVirtServerRule_Type()
)
slbCurCfgVirtServerRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerRule.setStatus("current")


class _SlbCurCfgVirtServerVname_Type(DisplayString):
    """Custom type slbCurCfgVirtServerVname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgVirtServerVname_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServerVname_Object = MibTableColumn
slbCurCfgVirtServerVname = _SlbCurCfgVirtServerVname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 2, 1, 10),
    _SlbCurCfgVirtServerVname_Type()
)
slbCurCfgVirtServerVname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerVname.setStatus("current")


class _SlbCurCfgVirtServerIpVer_Type(Integer32):
    """Custom type slbCurCfgVirtServerIpVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SlbCurCfgVirtServerIpVer_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerIpVer_Object = MibTableColumn
slbCurCfgVirtServerIpVer = _SlbCurCfgVirtServerIpVer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 2, 1, 11),
    _SlbCurCfgVirtServerIpVer_Type()
)
slbCurCfgVirtServerIpVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerIpVer.setStatus("current")


class _SlbCurCfgVirtServerIpv6Addr_Type(DisplayString):
    """Custom type slbCurCfgVirtServerIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlbCurCfgVirtServerIpv6Addr_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServerIpv6Addr_Object = MibTableColumn
slbCurCfgVirtServerIpv6Addr = _SlbCurCfgVirtServerIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 2, 1, 12),
    _SlbCurCfgVirtServerIpv6Addr_Type()
)
slbCurCfgVirtServerIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerIpv6Addr.setStatus("current")
_SlbNewCfgVirtServerTable_Object = MibTable
slbNewCfgVirtServerTable = _SlbNewCfgVirtServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    slbNewCfgVirtServerTable.setStatus("current")
_SlbNewCfgVirtualServerEntry_Object = MibTableRow
slbNewCfgVirtualServerEntry = _SlbNewCfgVirtualServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1)
)
slbNewCfgVirtualServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgVirtServerIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgVirtualServerEntry.setStatus("current")
_SlbNewCfgVirtServerIndex_Type = Integer32
_SlbNewCfgVirtServerIndex_Object = MibTableColumn
slbNewCfgVirtServerIndex = _SlbNewCfgVirtServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 1),
    _SlbNewCfgVirtServerIndex_Type()
)
slbNewCfgVirtServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerIndex.setStatus("current")
_SlbNewCfgVirtServerIpAddress_Type = IpAddress
_SlbNewCfgVirtServerIpAddress_Object = MibTableColumn
slbNewCfgVirtServerIpAddress = _SlbNewCfgVirtServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 2),
    _SlbNewCfgVirtServerIpAddress_Type()
)
slbNewCfgVirtServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerIpAddress.setStatus("current")


class _SlbNewCfgVirtServerLayer3Only_Type(Integer32):
    """Custom type slbNewCfgVirtServerLayer3Only based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer3Only", 1),
          ("disabled", 2))
    )


_SlbNewCfgVirtServerLayer3Only_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerLayer3Only_Object = MibTableColumn
slbNewCfgVirtServerLayer3Only = _SlbNewCfgVirtServerLayer3Only_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 3),
    _SlbNewCfgVirtServerLayer3Only_Type()
)
slbNewCfgVirtServerLayer3Only.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerLayer3Only.setStatus("current")


class _SlbNewCfgVirtServerState_Type(Integer32):
    """Custom type slbNewCfgVirtServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("disabled", 3))
    )


_SlbNewCfgVirtServerState_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerState_Object = MibTableColumn
slbNewCfgVirtServerState = _SlbNewCfgVirtServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 4),
    _SlbNewCfgVirtServerState_Type()
)
slbNewCfgVirtServerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerState.setStatus("current")


class _SlbNewCfgVirtServerDname_Type(DisplayString):
    """Custom type slbNewCfgVirtServerDname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlbNewCfgVirtServerDname_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServerDname_Object = MibTableColumn
slbNewCfgVirtServerDname = _SlbNewCfgVirtServerDname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 6),
    _SlbNewCfgVirtServerDname_Type()
)
slbNewCfgVirtServerDname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerDname.setStatus("current")
_SlbNewCfgVirtServerBwmContract_Type = Integer32
_SlbNewCfgVirtServerBwmContract_Object = MibTableColumn
slbNewCfgVirtServerBwmContract = _SlbNewCfgVirtServerBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 7),
    _SlbNewCfgVirtServerBwmContract_Type()
)
slbNewCfgVirtServerBwmContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerBwmContract.setStatus("current")


class _SlbNewCfgVirtServerDelete_Type(Integer32):
    """Custom type slbNewCfgVirtServerDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgVirtServerDelete_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerDelete_Object = MibTableColumn
slbNewCfgVirtServerDelete = _SlbNewCfgVirtServerDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 8),
    _SlbNewCfgVirtServerDelete_Type()
)
slbNewCfgVirtServerDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerDelete.setStatus("current")


class _SlbNewCfgVirtServerWeight_Type(Integer32):
    """Custom type slbNewCfgVirtServerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SlbNewCfgVirtServerWeight_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerWeight_Object = MibTableColumn
slbNewCfgVirtServerWeight = _SlbNewCfgVirtServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 9),
    _SlbNewCfgVirtServerWeight_Type()
)
slbNewCfgVirtServerWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerWeight.setStatus("current")


class _SlbNewCfgVirtServerAvail_Type(Integer32):
    """Custom type slbNewCfgVirtServerAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SlbNewCfgVirtServerAvail_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerAvail_Object = MibTableColumn
slbNewCfgVirtServerAvail = _SlbNewCfgVirtServerAvail_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 10),
    _SlbNewCfgVirtServerAvail_Type()
)
slbNewCfgVirtServerAvail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerAvail.setStatus("current")
_SlbNewCfgVirtServerRule_Type = OctetString
_SlbNewCfgVirtServerRule_Object = MibTableColumn
slbNewCfgVirtServerRule = _SlbNewCfgVirtServerRule_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 11),
    _SlbNewCfgVirtServerRule_Type()
)
slbNewCfgVirtServerRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerRule.setStatus("current")
_SlbNewCfgVirtServerAddRule_Type = Integer32
_SlbNewCfgVirtServerAddRule_Object = MibTableColumn
slbNewCfgVirtServerAddRule = _SlbNewCfgVirtServerAddRule_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 12),
    _SlbNewCfgVirtServerAddRule_Type()
)
slbNewCfgVirtServerAddRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerAddRule.setStatus("current")
_SlbNewCfgVirtServerRemoveRule_Type = Integer32
_SlbNewCfgVirtServerRemoveRule_Object = MibTableColumn
slbNewCfgVirtServerRemoveRule = _SlbNewCfgVirtServerRemoveRule_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 13),
    _SlbNewCfgVirtServerRemoveRule_Type()
)
slbNewCfgVirtServerRemoveRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerRemoveRule.setStatus("current")


class _SlbNewCfgVirtServerVname_Type(DisplayString):
    """Custom type slbNewCfgVirtServerVname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbNewCfgVirtServerVname_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServerVname_Object = MibTableColumn
slbNewCfgVirtServerVname = _SlbNewCfgVirtServerVname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 14),
    _SlbNewCfgVirtServerVname_Type()
)
slbNewCfgVirtServerVname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerVname.setStatus("current")


class _SlbNewCfgVirtServerIpVer_Type(Integer32):
    """Custom type slbNewCfgVirtServerIpVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SlbNewCfgVirtServerIpVer_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerIpVer_Object = MibTableColumn
slbNewCfgVirtServerIpVer = _SlbNewCfgVirtServerIpVer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 15),
    _SlbNewCfgVirtServerIpVer_Type()
)
slbNewCfgVirtServerIpVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerIpVer.setStatus("current")


class _SlbNewCfgVirtServerIpv6Addr_Type(DisplayString):
    """Custom type slbNewCfgVirtServerIpv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlbNewCfgVirtServerIpv6Addr_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServerIpv6Addr_Object = MibTableColumn
slbNewCfgVirtServerIpv6Addr = _SlbNewCfgVirtServerIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 3, 1, 16),
    _SlbNewCfgVirtServerIpv6Addr_Type()
)
slbNewCfgVirtServerIpv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerIpv6Addr.setStatus("current")
_SlbVirtServicesTableMaxSize_Type = Integer32
_SlbVirtServicesTableMaxSize_Object = MibScalar
slbVirtServicesTableMaxSize = _SlbVirtServicesTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 4),
    _SlbVirtServicesTableMaxSize_Type()
)
slbVirtServicesTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtServicesTableMaxSize.setStatus("current")
_SlbCurCfgVirtServicesTable_Object = MibTable
slbCurCfgVirtServicesTable = _SlbCurCfgVirtServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    slbCurCfgVirtServicesTable.setStatus("current")
_SlbCurCfgVirtServicesEntry_Object = MibTableRow
slbCurCfgVirtServicesEntry = _SlbCurCfgVirtServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1)
)
slbCurCfgVirtServicesEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgVirtServIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgVirtServiceIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgVirtServicesEntry.setStatus("current")
_SlbCurCfgVirtServIndex_Type = Integer32
_SlbCurCfgVirtServIndex_Object = MibTableColumn
slbCurCfgVirtServIndex = _SlbCurCfgVirtServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 1),
    _SlbCurCfgVirtServIndex_Type()
)
slbCurCfgVirtServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServIndex.setStatus("current")
_SlbCurCfgVirtServiceIndex_Type = Integer32
_SlbCurCfgVirtServiceIndex_Object = MibTableColumn
slbCurCfgVirtServiceIndex = _SlbCurCfgVirtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 2),
    _SlbCurCfgVirtServiceIndex_Type()
)
slbCurCfgVirtServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceIndex.setStatus("current")


class _SlbCurCfgVirtServiceVirtPort_Type(Integer32):
    """Custom type slbCurCfgVirtServiceVirtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 65534),
    )


_SlbCurCfgVirtServiceVirtPort_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceVirtPort_Object = MibTableColumn
slbCurCfgVirtServiceVirtPort = _SlbCurCfgVirtServiceVirtPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 3),
    _SlbCurCfgVirtServiceVirtPort_Type()
)
slbCurCfgVirtServiceVirtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceVirtPort.setStatus("current")
_SlbCurCfgVirtServiceRealGroup_Type = Integer32
_SlbCurCfgVirtServiceRealGroup_Object = MibTableColumn
slbCurCfgVirtServiceRealGroup = _SlbCurCfgVirtServiceRealGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 4),
    _SlbCurCfgVirtServiceRealGroup_Type()
)
slbCurCfgVirtServiceRealGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceRealGroup.setStatus("current")


class _SlbCurCfgVirtServiceRealPort_Type(Integer32):
    """Custom type slbCurCfgVirtServiceRealPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbCurCfgVirtServiceRealPort_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceRealPort_Object = MibTableColumn
slbCurCfgVirtServiceRealPort = _SlbCurCfgVirtServiceRealPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 5),
    _SlbCurCfgVirtServiceRealPort_Type()
)
slbCurCfgVirtServiceRealPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceRealPort.setStatus("current")


class _SlbCurCfgVirtServiceUDPBalance_Type(Integer32):
    """Custom type slbCurCfgVirtServiceUDPBalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("disabled", 3),
          ("stateless", 4))
    )


_SlbCurCfgVirtServiceUDPBalance_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceUDPBalance_Object = MibTableColumn
slbCurCfgVirtServiceUDPBalance = _SlbCurCfgVirtServiceUDPBalance_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 6),
    _SlbCurCfgVirtServiceUDPBalance_Type()
)
slbCurCfgVirtServiceUDPBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceUDPBalance.setStatus("current")


class _SlbCurCfgVirtServiceHname_Type(DisplayString):
    """Custom type slbCurCfgVirtServiceHname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_SlbCurCfgVirtServiceHname_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServiceHname_Object = MibTableColumn
slbCurCfgVirtServiceHname = _SlbCurCfgVirtServiceHname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 7),
    _SlbCurCfgVirtServiceHname_Type()
)
slbCurCfgVirtServiceHname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceHname.setStatus("current")
_SlbCurCfgVirtServiceBwmContract_Type = Integer32
_SlbCurCfgVirtServiceBwmContract_Object = MibTableColumn
slbCurCfgVirtServiceBwmContract = _SlbCurCfgVirtServiceBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 8),
    _SlbCurCfgVirtServiceBwmContract_Type()
)
slbCurCfgVirtServiceBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceBwmContract.setStatus("current")


class _SlbCurCfgVirtServiceDirServerRtn_Type(Integer32):
    """Custom type slbCurCfgVirtServiceDirServerRtn based on Integer32"""
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


_SlbCurCfgVirtServiceDirServerRtn_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceDirServerRtn_Object = MibTableColumn
slbCurCfgVirtServiceDirServerRtn = _SlbCurCfgVirtServiceDirServerRtn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 9),
    _SlbCurCfgVirtServiceDirServerRtn_Type()
)
slbCurCfgVirtServiceDirServerRtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceDirServerRtn.setStatus("current")


class _SlbCurCfgVirtServiceRtspUrlParse_Type(Integer32):
    """Custom type slbCurCfgVirtServiceRtspUrlParse based on Integer32"""
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
        *(("none", 1),
          ("l4hash", 2),
          ("hash", 3),
          ("patternMatch", 4))
    )


_SlbCurCfgVirtServiceRtspUrlParse_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceRtspUrlParse_Object = MibTableColumn
slbCurCfgVirtServiceRtspUrlParse = _SlbCurCfgVirtServiceRtspUrlParse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 10),
    _SlbCurCfgVirtServiceRtspUrlParse_Type()
)
slbCurCfgVirtServiceRtspUrlParse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceRtspUrlParse.setStatus("current")


class _SlbCurCfgVirtServiceDBind_Type(Integer32):
    """Custom type slbCurCfgVirtServiceDBind based on Integer32"""
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


_SlbCurCfgVirtServiceDBind_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceDBind_Object = MibTableColumn
slbCurCfgVirtServiceDBind = _SlbCurCfgVirtServiceDBind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 11),
    _SlbCurCfgVirtServiceDBind_Type()
)
slbCurCfgVirtServiceDBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceDBind.setStatus("current")


class _SlbCurCfgVirtServiceFtpParsing_Type(Integer32):
    """Custom type slbCurCfgVirtServiceFtpParsing based on Integer32"""
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


_SlbCurCfgVirtServiceFtpParsing_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceFtpParsing_Object = MibTableColumn
slbCurCfgVirtServiceFtpParsing = _SlbCurCfgVirtServiceFtpParsing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 12),
    _SlbCurCfgVirtServiceFtpParsing_Type()
)
slbCurCfgVirtServiceFtpParsing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceFtpParsing.setStatus("current")


class _SlbCurCfgVirtServiceRemapUDPFrags_Type(Integer32):
    """Custom type slbCurCfgVirtServiceRemapUDPFrags based on Integer32"""
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


_SlbCurCfgVirtServiceRemapUDPFrags_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceRemapUDPFrags_Object = MibTableColumn
slbCurCfgVirtServiceRemapUDPFrags = _SlbCurCfgVirtServiceRemapUDPFrags_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 13),
    _SlbCurCfgVirtServiceRemapUDPFrags_Type()
)
slbCurCfgVirtServiceRemapUDPFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceRemapUDPFrags.setStatus("current")


class _SlbCurCfgVirtServiceDnsSlb_Type(Integer32):
    """Custom type slbCurCfgVirtServiceDnsSlb based on Integer32"""
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


_SlbCurCfgVirtServiceDnsSlb_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceDnsSlb_Object = MibTableColumn
slbCurCfgVirtServiceDnsSlb = _SlbCurCfgVirtServiceDnsSlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 14),
    _SlbCurCfgVirtServiceDnsSlb_Type()
)
slbCurCfgVirtServiceDnsSlb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceDnsSlb.setStatus("current")


class _SlbCurCfgVirtServiceResponseCount_Type(Integer32):
    """Custom type slbCurCfgVirtServiceResponseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SlbCurCfgVirtServiceResponseCount_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceResponseCount_Object = MibTableColumn
slbCurCfgVirtServiceResponseCount = _SlbCurCfgVirtServiceResponseCount_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 15),
    _SlbCurCfgVirtServiceResponseCount_Type()
)
slbCurCfgVirtServiceResponseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceResponseCount.setStatus("current")


class _SlbCurCfgVirtServicePBind_Type(Integer32):
    """Custom type slbCurCfgVirtServicePBind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clientip", 2),
          ("disabled", 3),
          ("sslid", 4),
          ("cookie", 5))
    )


_SlbCurCfgVirtServicePBind_Type.__name__ = "Integer32"
_SlbCurCfgVirtServicePBind_Object = MibTableColumn
slbCurCfgVirtServicePBind = _SlbCurCfgVirtServicePBind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 16),
    _SlbCurCfgVirtServicePBind_Type()
)
slbCurCfgVirtServicePBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServicePBind.setStatus("current")


class _SlbCurCfgVirtServiceCname_Type(DisplayString):
    """Custom type slbCurCfgVirtServiceCname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlbCurCfgVirtServiceCname_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServiceCname_Object = MibTableColumn
slbCurCfgVirtServiceCname = _SlbCurCfgVirtServiceCname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 17),
    _SlbCurCfgVirtServiceCname_Type()
)
slbCurCfgVirtServiceCname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceCname.setStatus("current")


class _SlbCurCfgVirtServiceCoffset_Type(Integer32):
    """Custom type slbCurCfgVirtServiceCoffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SlbCurCfgVirtServiceCoffset_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceCoffset_Object = MibTableColumn
slbCurCfgVirtServiceCoffset = _SlbCurCfgVirtServiceCoffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 18),
    _SlbCurCfgVirtServiceCoffset_Type()
)
slbCurCfgVirtServiceCoffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceCoffset.setStatus("current")


class _SlbCurCfgVirtServiceClength_Type(Integer32):
    """Custom type slbCurCfgVirtServiceClength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SlbCurCfgVirtServiceClength_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceClength_Object = MibTableColumn
slbCurCfgVirtServiceClength = _SlbCurCfgVirtServiceClength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 19),
    _SlbCurCfgVirtServiceClength_Type()
)
slbCurCfgVirtServiceClength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceClength.setStatus("current")


class _SlbCurCfgVirtServiceUriCookie_Type(Integer32):
    """Custom type slbCurCfgVirtServiceUriCookie based on Integer32"""
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


_SlbCurCfgVirtServiceUriCookie_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceUriCookie_Object = MibTableColumn
slbCurCfgVirtServiceUriCookie = _SlbCurCfgVirtServiceUriCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 20),
    _SlbCurCfgVirtServiceUriCookie_Type()
)
slbCurCfgVirtServiceUriCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceUriCookie.setStatus("current")


class _SlbCurCfgVirtServiceCExpire_Type(DisplayString):
    """Custom type slbCurCfgVirtServiceCExpire based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlbCurCfgVirtServiceCExpire_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServiceCExpire_Object = MibTableColumn
slbCurCfgVirtServiceCExpire = _SlbCurCfgVirtServiceCExpire_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 21),
    _SlbCurCfgVirtServiceCExpire_Type()
)
slbCurCfgVirtServiceCExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceCExpire.setStatus("current")


class _SlbCurCfgVirtServiceCookieMode_Type(Integer32):
    """Custom type slbCurCfgVirtServiceCookieMode based on Integer32"""
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
        *(("rewrite", 1),
          ("passive", 2),
          ("insert", 3),
          ("disabled", 4))
    )


_SlbCurCfgVirtServiceCookieMode_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceCookieMode_Object = MibTableColumn
slbCurCfgVirtServiceCookieMode = _SlbCurCfgVirtServiceCookieMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 22),
    _SlbCurCfgVirtServiceCookieMode_Type()
)
slbCurCfgVirtServiceCookieMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceCookieMode.setStatus("current")


class _SlbCurCfgVirtServiceHttpSlb_Type(Integer32):
    """Custom type slbCurCfgVirtServiceHttpSlb based on Integer32"""
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
        *(("disabled", 1),
          ("urlslb", 2),
          ("urlhash", 3),
          ("cookie", 4),
          ("host", 5),
          ("browser", 6),
          ("others", 7),
          ("headerhash", 8))
    )


_SlbCurCfgVirtServiceHttpSlb_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceHttpSlb_Object = MibTableColumn
slbCurCfgVirtServiceHttpSlb = _SlbCurCfgVirtServiceHttpSlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 23),
    _SlbCurCfgVirtServiceHttpSlb_Type()
)
slbCurCfgVirtServiceHttpSlb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceHttpSlb.setStatus("current")


class _SlbCurCfgVirtServiceHttpSlbOption_Type(Integer32):
    """Custom type slbCurCfgVirtServiceHttpSlbOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("and", 1),
          ("or", 2),
          ("none", 3))
    )


_SlbCurCfgVirtServiceHttpSlbOption_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceHttpSlbOption_Object = MibTableColumn
slbCurCfgVirtServiceHttpSlbOption = _SlbCurCfgVirtServiceHttpSlbOption_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 24),
    _SlbCurCfgVirtServiceHttpSlbOption_Type()
)
slbCurCfgVirtServiceHttpSlbOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceHttpSlbOption.setStatus("current")


class _SlbCurCfgVirtServiceHttpSlb2_Type(Integer32):
    """Custom type slbCurCfgVirtServiceHttpSlb2 based on Integer32"""
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
        *(("disabled", 1),
          ("urlslb", 2),
          ("urlhash", 3),
          ("cookie", 4),
          ("host", 5),
          ("browser", 6),
          ("others", 7),
          ("headerhash", 8))
    )


_SlbCurCfgVirtServiceHttpSlb2_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceHttpSlb2_Object = MibTableColumn
slbCurCfgVirtServiceHttpSlb2 = _SlbCurCfgVirtServiceHttpSlb2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 25),
    _SlbCurCfgVirtServiceHttpSlb2_Type()
)
slbCurCfgVirtServiceHttpSlb2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceHttpSlb2.setStatus("current")


class _SlbCurCfgVirtServiceHttpHdrName_Type(DisplayString):
    """Custom type slbCurCfgVirtServiceHttpHdrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgVirtServiceHttpHdrName_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServiceHttpHdrName_Object = MibTableColumn
slbCurCfgVirtServiceHttpHdrName = _SlbCurCfgVirtServiceHttpHdrName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 26),
    _SlbCurCfgVirtServiceHttpHdrName_Type()
)
slbCurCfgVirtServiceHttpHdrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceHttpHdrName.setStatus("current")


class _SlbCurCfgVirtServiceUrlHashLen_Type(Integer32):
    """Custom type slbCurCfgVirtServiceUrlHashLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbCurCfgVirtServiceUrlHashLen_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceUrlHashLen_Object = MibTableColumn
slbCurCfgVirtServiceUrlHashLen = _SlbCurCfgVirtServiceUrlHashLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 27),
    _SlbCurCfgVirtServiceUrlHashLen_Type()
)
slbCurCfgVirtServiceUrlHashLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceUrlHashLen.setStatus("current")


class _SlbCurCfgVirtServiceDirect_Type(Integer32):
    """Custom type slbCurCfgVirtServiceDirect based on Integer32"""
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


_SlbCurCfgVirtServiceDirect_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceDirect_Object = MibTableColumn
slbCurCfgVirtServiceDirect = _SlbCurCfgVirtServiceDirect_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 28),
    _SlbCurCfgVirtServiceDirect_Type()
)
slbCurCfgVirtServiceDirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceDirect.setStatus("current")


class _SlbCurCfgVirtServiceThash_Type(Integer32):
    """Custom type slbCurCfgVirtServiceThash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sip", 1),
          ("sip-sport", 2))
    )


_SlbCurCfgVirtServiceThash_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceThash_Object = MibTableColumn
slbCurCfgVirtServiceThash = _SlbCurCfgVirtServiceThash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 29),
    _SlbCurCfgVirtServiceThash_Type()
)
slbCurCfgVirtServiceThash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceThash.setStatus("current")


class _SlbCurCfgVirtServiceLdapreset_Type(Integer32):
    """Custom type slbCurCfgVirtServiceLdapreset based on Integer32"""
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


_SlbCurCfgVirtServiceLdapreset_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceLdapreset_Object = MibTableColumn
slbCurCfgVirtServiceLdapreset = _SlbCurCfgVirtServiceLdapreset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 30),
    _SlbCurCfgVirtServiceLdapreset_Type()
)
slbCurCfgVirtServiceLdapreset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceLdapreset.setStatus("current")


class _SlbCurCfgVirtServiceLdapslb_Type(Integer32):
    """Custom type slbCurCfgVirtServiceLdapslb based on Integer32"""
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


_SlbCurCfgVirtServiceLdapslb_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceLdapslb_Object = MibTableColumn
slbCurCfgVirtServiceLdapslb = _SlbCurCfgVirtServiceLdapslb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 31),
    _SlbCurCfgVirtServiceLdapslb_Type()
)
slbCurCfgVirtServiceLdapslb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceLdapslb.setStatus("current")


class _SlbCurCfgVirtServiceSip_Type(Integer32):
    """Custom type slbCurCfgVirtServiceSip based on Integer32"""
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


_SlbCurCfgVirtServiceSip_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceSip_Object = MibTableColumn
slbCurCfgVirtServiceSip = _SlbCurCfgVirtServiceSip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 32),
    _SlbCurCfgVirtServiceSip_Type()
)
slbCurCfgVirtServiceSip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceSip.setStatus("current")


class _SlbCurCfgVirtServiceXForwardedFor_Type(Integer32):
    """Custom type slbCurCfgVirtServiceXForwardedFor based on Integer32"""
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


_SlbCurCfgVirtServiceXForwardedFor_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceXForwardedFor_Object = MibTableColumn
slbCurCfgVirtServiceXForwardedFor = _SlbCurCfgVirtServiceXForwardedFor_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 33),
    _SlbCurCfgVirtServiceXForwardedFor_Type()
)
slbCurCfgVirtServiceXForwardedFor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceXForwardedFor.setStatus("current")


class _SlbCurCfgVirtServiceHttpRedir_Type(Integer32):
    """Custom type slbCurCfgVirtServiceHttpRedir based on Integer32"""
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


_SlbCurCfgVirtServiceHttpRedir_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceHttpRedir_Object = MibTableColumn
slbCurCfgVirtServiceHttpRedir = _SlbCurCfgVirtServiceHttpRedir_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 34),
    _SlbCurCfgVirtServiceHttpRedir_Type()
)
slbCurCfgVirtServiceHttpRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceHttpRedir.setStatus("current")


class _SlbCurCfgVirtServicePbindRport_Type(Integer32):
    """Custom type slbCurCfgVirtServicePbindRport based on Integer32"""
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


_SlbCurCfgVirtServicePbindRport_Type.__name__ = "Integer32"
_SlbCurCfgVirtServicePbindRport_Object = MibTableColumn
slbCurCfgVirtServicePbindRport = _SlbCurCfgVirtServicePbindRport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 35),
    _SlbCurCfgVirtServicePbindRport_Type()
)
slbCurCfgVirtServicePbindRport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServicePbindRport.setStatus("current")


class _SlbCurCfgVirtServiceEgressPip_Type(Integer32):
    """Custom type slbCurCfgVirtServiceEgressPip based on Integer32"""
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


_SlbCurCfgVirtServiceEgressPip_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceEgressPip_Object = MibTableColumn
slbCurCfgVirtServiceEgressPip = _SlbCurCfgVirtServiceEgressPip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 36),
    _SlbCurCfgVirtServiceEgressPip_Type()
)
slbCurCfgVirtServiceEgressPip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceEgressPip.setStatus("current")


class _SlbCurCfgVirtServiceCookieDname_Type(Integer32):
    """Custom type slbCurCfgVirtServiceCookieDname based on Integer32"""
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


_SlbCurCfgVirtServiceCookieDname_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceCookieDname_Object = MibTableColumn
slbCurCfgVirtServiceCookieDname = _SlbCurCfgVirtServiceCookieDname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 37),
    _SlbCurCfgVirtServiceCookieDname_Type()
)
slbCurCfgVirtServiceCookieDname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceCookieDname.setStatus("current")


class _SlbCurCfgVirtServiceWts_Type(Integer32):
    """Custom type slbCurCfgVirtServiceWts based on Integer32"""
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


_SlbCurCfgVirtServiceWts_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceWts_Object = MibTableColumn
slbCurCfgVirtServiceWts = _SlbCurCfgVirtServiceWts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 38),
    _SlbCurCfgVirtServiceWts_Type()
)
slbCurCfgVirtServiceWts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceWts.setStatus("current")


class _SlbCurCfgVirtServiceUhash_Type(Integer32):
    """Custom type slbCurCfgVirtServiceUhash based on Integer32"""
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


_SlbCurCfgVirtServiceUhash_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceUhash_Object = MibTableColumn
slbCurCfgVirtServiceUhash = _SlbCurCfgVirtServiceUhash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 39),
    _SlbCurCfgVirtServiceUhash_Type()
)
slbCurCfgVirtServiceUhash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceUhash.setStatus("current")


class _SlbCurCfgVirtServiceTimeOut_Type(Integer32):
    """Custom type slbCurCfgVirtServiceTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_SlbCurCfgVirtServiceTimeOut_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceTimeOut_Object = MibTableColumn
slbCurCfgVirtServiceTimeOut = _SlbCurCfgVirtServiceTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 40),
    _SlbCurCfgVirtServiceTimeOut_Type()
)
slbCurCfgVirtServiceTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceTimeOut.setStatus("current")


class _SlbCurCfgVirtServiceSdpNat_Type(Integer32):
    """Custom type slbCurCfgVirtServiceSdpNat based on Integer32"""
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


_SlbCurCfgVirtServiceSdpNat_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceSdpNat_Object = MibTableColumn
slbCurCfgVirtServiceSdpNat = _SlbCurCfgVirtServiceSdpNat_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 41),
    _SlbCurCfgVirtServiceSdpNat_Type()
)
slbCurCfgVirtServiceSdpNat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceSdpNat.setStatus("current")


class _SlbCurCfgVirtServiceSessionMirror_Type(Integer32):
    """Custom type slbCurCfgVirtServiceSessionMirror based on Integer32"""
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


_SlbCurCfgVirtServiceSessionMirror_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceSessionMirror_Object = MibTableColumn
slbCurCfgVirtServiceSessionMirror = _SlbCurCfgVirtServiceSessionMirror_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 42),
    _SlbCurCfgVirtServiceSessionMirror_Type()
)
slbCurCfgVirtServiceSessionMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceSessionMirror.setStatus("current")


class _SlbCurCfgVirtServiceSoftGrid_Type(Integer32):
    """Custom type slbCurCfgVirtServiceSoftGrid based on Integer32"""
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


_SlbCurCfgVirtServiceSoftGrid_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceSoftGrid_Object = MibTableColumn
slbCurCfgVirtServiceSoftGrid = _SlbCurCfgVirtServiceSoftGrid_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 43),
    _SlbCurCfgVirtServiceSoftGrid_Type()
)
slbCurCfgVirtServiceSoftGrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceSoftGrid.setStatus("current")


class _SlbCurCfgVirtServiceConnPooling_Type(Integer32):
    """Custom type slbCurCfgVirtServiceConnPooling based on Integer32"""
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


_SlbCurCfgVirtServiceConnPooling_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceConnPooling_Object = MibTableColumn
slbCurCfgVirtServiceConnPooling = _SlbCurCfgVirtServiceConnPooling_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 5, 1, 44),
    _SlbCurCfgVirtServiceConnPooling_Type()
)
slbCurCfgVirtServiceConnPooling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceConnPooling.setStatus("current")
_SlbNewCfgVirtServicesTable_Object = MibTable
slbNewCfgVirtServicesTable = _SlbNewCfgVirtServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6)
)
if mibBuilder.loadTexts:
    slbNewCfgVirtServicesTable.setStatus("current")
_SlbNewCfgVirtServicesEntry_Object = MibTableRow
slbNewCfgVirtServicesEntry = _SlbNewCfgVirtServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1)
)
slbNewCfgVirtServicesEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgVirtServIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgVirtServiceIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgVirtServicesEntry.setStatus("current")
_SlbNewCfgVirtServIndex_Type = Integer32
_SlbNewCfgVirtServIndex_Object = MibTableColumn
slbNewCfgVirtServIndex = _SlbNewCfgVirtServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 1),
    _SlbNewCfgVirtServIndex_Type()
)
slbNewCfgVirtServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgVirtServIndex.setStatus("current")
_SlbNewCfgVirtServiceIndex_Type = Integer32
_SlbNewCfgVirtServiceIndex_Object = MibTableColumn
slbNewCfgVirtServiceIndex = _SlbNewCfgVirtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 2),
    _SlbNewCfgVirtServiceIndex_Type()
)
slbNewCfgVirtServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceIndex.setStatus("current")


class _SlbNewCfgVirtServiceVirtPort_Type(Integer32):
    """Custom type slbNewCfgVirtServiceVirtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 65534),
    )


_SlbNewCfgVirtServiceVirtPort_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceVirtPort_Object = MibTableColumn
slbNewCfgVirtServiceVirtPort = _SlbNewCfgVirtServiceVirtPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 3),
    _SlbNewCfgVirtServiceVirtPort_Type()
)
slbNewCfgVirtServiceVirtPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceVirtPort.setStatus("current")
_SlbNewCfgVirtServiceRealGroup_Type = Integer32
_SlbNewCfgVirtServiceRealGroup_Object = MibTableColumn
slbNewCfgVirtServiceRealGroup = _SlbNewCfgVirtServiceRealGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 4),
    _SlbNewCfgVirtServiceRealGroup_Type()
)
slbNewCfgVirtServiceRealGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceRealGroup.setStatus("current")


class _SlbNewCfgVirtServiceRealPort_Type(Integer32):
    """Custom type slbNewCfgVirtServiceRealPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbNewCfgVirtServiceRealPort_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceRealPort_Object = MibTableColumn
slbNewCfgVirtServiceRealPort = _SlbNewCfgVirtServiceRealPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 5),
    _SlbNewCfgVirtServiceRealPort_Type()
)
slbNewCfgVirtServiceRealPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceRealPort.setStatus("current")


class _SlbNewCfgVirtServiceUDPBalance_Type(Integer32):
    """Custom type slbNewCfgVirtServiceUDPBalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("disabled", 3),
          ("stateless", 4))
    )


_SlbNewCfgVirtServiceUDPBalance_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceUDPBalance_Object = MibTableColumn
slbNewCfgVirtServiceUDPBalance = _SlbNewCfgVirtServiceUDPBalance_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 6),
    _SlbNewCfgVirtServiceUDPBalance_Type()
)
slbNewCfgVirtServiceUDPBalance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceUDPBalance.setStatus("current")


class _SlbNewCfgVirtServiceHname_Type(DisplayString):
    """Custom type slbNewCfgVirtServiceHname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_SlbNewCfgVirtServiceHname_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServiceHname_Object = MibTableColumn
slbNewCfgVirtServiceHname = _SlbNewCfgVirtServiceHname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 7),
    _SlbNewCfgVirtServiceHname_Type()
)
slbNewCfgVirtServiceHname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceHname.setStatus("current")
_SlbNewCfgVirtServiceBwmContract_Type = Integer32
_SlbNewCfgVirtServiceBwmContract_Object = MibTableColumn
slbNewCfgVirtServiceBwmContract = _SlbNewCfgVirtServiceBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 8),
    _SlbNewCfgVirtServiceBwmContract_Type()
)
slbNewCfgVirtServiceBwmContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceBwmContract.setStatus("current")


class _SlbNewCfgVirtServiceDirServerRtn_Type(Integer32):
    """Custom type slbNewCfgVirtServiceDirServerRtn based on Integer32"""
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


_SlbNewCfgVirtServiceDirServerRtn_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceDirServerRtn_Object = MibTableColumn
slbNewCfgVirtServiceDirServerRtn = _SlbNewCfgVirtServiceDirServerRtn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 9),
    _SlbNewCfgVirtServiceDirServerRtn_Type()
)
slbNewCfgVirtServiceDirServerRtn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceDirServerRtn.setStatus("current")


class _SlbNewCfgVirtServiceRtspUrlParse_Type(Integer32):
    """Custom type slbNewCfgVirtServiceRtspUrlParse based on Integer32"""
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
        *(("none", 1),
          ("l4hash", 2),
          ("hash", 3),
          ("patternMatch", 4))
    )


_SlbNewCfgVirtServiceRtspUrlParse_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceRtspUrlParse_Object = MibTableColumn
slbNewCfgVirtServiceRtspUrlParse = _SlbNewCfgVirtServiceRtspUrlParse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 10),
    _SlbNewCfgVirtServiceRtspUrlParse_Type()
)
slbNewCfgVirtServiceRtspUrlParse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceRtspUrlParse.setStatus("current")


class _SlbNewCfgVirtServiceDBind_Type(Integer32):
    """Custom type slbNewCfgVirtServiceDBind based on Integer32"""
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


_SlbNewCfgVirtServiceDBind_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceDBind_Object = MibTableColumn
slbNewCfgVirtServiceDBind = _SlbNewCfgVirtServiceDBind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 11),
    _SlbNewCfgVirtServiceDBind_Type()
)
slbNewCfgVirtServiceDBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceDBind.setStatus("current")


class _SlbNewCfgVirtServiceFtpParsing_Type(Integer32):
    """Custom type slbNewCfgVirtServiceFtpParsing based on Integer32"""
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


_SlbNewCfgVirtServiceFtpParsing_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceFtpParsing_Object = MibTableColumn
slbNewCfgVirtServiceFtpParsing = _SlbNewCfgVirtServiceFtpParsing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 12),
    _SlbNewCfgVirtServiceFtpParsing_Type()
)
slbNewCfgVirtServiceFtpParsing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceFtpParsing.setStatus("current")


class _SlbNewCfgVirtServiceRemapUDPFrags_Type(Integer32):
    """Custom type slbNewCfgVirtServiceRemapUDPFrags based on Integer32"""
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


_SlbNewCfgVirtServiceRemapUDPFrags_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceRemapUDPFrags_Object = MibTableColumn
slbNewCfgVirtServiceRemapUDPFrags = _SlbNewCfgVirtServiceRemapUDPFrags_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 13),
    _SlbNewCfgVirtServiceRemapUDPFrags_Type()
)
slbNewCfgVirtServiceRemapUDPFrags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceRemapUDPFrags.setStatus("current")


class _SlbNewCfgVirtServiceDnsSlb_Type(Integer32):
    """Custom type slbNewCfgVirtServiceDnsSlb based on Integer32"""
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


_SlbNewCfgVirtServiceDnsSlb_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceDnsSlb_Object = MibTableColumn
slbNewCfgVirtServiceDnsSlb = _SlbNewCfgVirtServiceDnsSlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 14),
    _SlbNewCfgVirtServiceDnsSlb_Type()
)
slbNewCfgVirtServiceDnsSlb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceDnsSlb.setStatus("current")


class _SlbNewCfgVirtServiceResponseCount_Type(Integer32):
    """Custom type slbNewCfgVirtServiceResponseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SlbNewCfgVirtServiceResponseCount_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceResponseCount_Object = MibTableColumn
slbNewCfgVirtServiceResponseCount = _SlbNewCfgVirtServiceResponseCount_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 15),
    _SlbNewCfgVirtServiceResponseCount_Type()
)
slbNewCfgVirtServiceResponseCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceResponseCount.setStatus("current")


class _SlbNewCfgVirtServicePBind_Type(Integer32):
    """Custom type slbNewCfgVirtServicePBind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clientip", 2),
          ("disabled", 3),
          ("sslid", 4),
          ("cookie", 5))
    )


_SlbNewCfgVirtServicePBind_Type.__name__ = "Integer32"
_SlbNewCfgVirtServicePBind_Object = MibTableColumn
slbNewCfgVirtServicePBind = _SlbNewCfgVirtServicePBind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 16),
    _SlbNewCfgVirtServicePBind_Type()
)
slbNewCfgVirtServicePBind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServicePBind.setStatus("current")


class _SlbNewCfgVirtServiceCname_Type(DisplayString):
    """Custom type slbNewCfgVirtServiceCname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlbNewCfgVirtServiceCname_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServiceCname_Object = MibTableColumn
slbNewCfgVirtServiceCname = _SlbNewCfgVirtServiceCname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 17),
    _SlbNewCfgVirtServiceCname_Type()
)
slbNewCfgVirtServiceCname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceCname.setStatus("current")


class _SlbNewCfgVirtServiceCoffset_Type(Integer32):
    """Custom type slbNewCfgVirtServiceCoffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SlbNewCfgVirtServiceCoffset_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceCoffset_Object = MibTableColumn
slbNewCfgVirtServiceCoffset = _SlbNewCfgVirtServiceCoffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 18),
    _SlbNewCfgVirtServiceCoffset_Type()
)
slbNewCfgVirtServiceCoffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceCoffset.setStatus("current")


class _SlbNewCfgVirtServiceClength_Type(Integer32):
    """Custom type slbNewCfgVirtServiceClength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SlbNewCfgVirtServiceClength_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceClength_Object = MibTableColumn
slbNewCfgVirtServiceClength = _SlbNewCfgVirtServiceClength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 19),
    _SlbNewCfgVirtServiceClength_Type()
)
slbNewCfgVirtServiceClength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceClength.setStatus("current")


class _SlbNewCfgVirtServiceUriCookie_Type(Integer32):
    """Custom type slbNewCfgVirtServiceUriCookie based on Integer32"""
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


_SlbNewCfgVirtServiceUriCookie_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceUriCookie_Object = MibTableColumn
slbNewCfgVirtServiceUriCookie = _SlbNewCfgVirtServiceUriCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 20),
    _SlbNewCfgVirtServiceUriCookie_Type()
)
slbNewCfgVirtServiceUriCookie.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceUriCookie.setStatus("current")


class _SlbNewCfgVirtServiceCExpire_Type(DisplayString):
    """Custom type slbNewCfgVirtServiceCExpire based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlbNewCfgVirtServiceCExpire_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServiceCExpire_Object = MibTableColumn
slbNewCfgVirtServiceCExpire = _SlbNewCfgVirtServiceCExpire_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 21),
    _SlbNewCfgVirtServiceCExpire_Type()
)
slbNewCfgVirtServiceCExpire.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceCExpire.setStatus("current")


class _SlbNewCfgVirtServiceCookieMode_Type(Integer32):
    """Custom type slbNewCfgVirtServiceCookieMode based on Integer32"""
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
        *(("rewrite", 1),
          ("passive", 2),
          ("insert", 3),
          ("disabled", 4))
    )


_SlbNewCfgVirtServiceCookieMode_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceCookieMode_Object = MibTableColumn
slbNewCfgVirtServiceCookieMode = _SlbNewCfgVirtServiceCookieMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 22),
    _SlbNewCfgVirtServiceCookieMode_Type()
)
slbNewCfgVirtServiceCookieMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceCookieMode.setStatus("current")


class _SlbNewCfgVirtServiceHttpSlb_Type(Integer32):
    """Custom type slbNewCfgVirtServiceHttpSlb based on Integer32"""
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
        *(("disabled", 1),
          ("urlslb", 2),
          ("urlhash", 3),
          ("cookie", 4),
          ("host", 5),
          ("browser", 6),
          ("others", 7),
          ("headerhash", 8))
    )


_SlbNewCfgVirtServiceHttpSlb_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceHttpSlb_Object = MibTableColumn
slbNewCfgVirtServiceHttpSlb = _SlbNewCfgVirtServiceHttpSlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 23),
    _SlbNewCfgVirtServiceHttpSlb_Type()
)
slbNewCfgVirtServiceHttpSlb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceHttpSlb.setStatus("current")


class _SlbNewCfgVirtServiceHttpSlbOption_Type(Integer32):
    """Custom type slbNewCfgVirtServiceHttpSlbOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("and", 1),
          ("or", 2),
          ("none", 3))
    )


_SlbNewCfgVirtServiceHttpSlbOption_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceHttpSlbOption_Object = MibTableColumn
slbNewCfgVirtServiceHttpSlbOption = _SlbNewCfgVirtServiceHttpSlbOption_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 24),
    _SlbNewCfgVirtServiceHttpSlbOption_Type()
)
slbNewCfgVirtServiceHttpSlbOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceHttpSlbOption.setStatus("current")


class _SlbNewCfgVirtServiceHttpSlb2_Type(Integer32):
    """Custom type slbNewCfgVirtServiceHttpSlb2 based on Integer32"""
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
        *(("disabled", 1),
          ("urlslb", 2),
          ("urlhash", 3),
          ("cookie", 4),
          ("host", 5),
          ("browser", 6),
          ("others", 7),
          ("headerhash", 8))
    )


_SlbNewCfgVirtServiceHttpSlb2_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceHttpSlb2_Object = MibTableColumn
slbNewCfgVirtServiceHttpSlb2 = _SlbNewCfgVirtServiceHttpSlb2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 25),
    _SlbNewCfgVirtServiceHttpSlb2_Type()
)
slbNewCfgVirtServiceHttpSlb2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceHttpSlb2.setStatus("current")


class _SlbNewCfgVirtServiceHttpHdrName_Type(DisplayString):
    """Custom type slbNewCfgVirtServiceHttpHdrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbNewCfgVirtServiceHttpHdrName_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServiceHttpHdrName_Object = MibTableColumn
slbNewCfgVirtServiceHttpHdrName = _SlbNewCfgVirtServiceHttpHdrName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 26),
    _SlbNewCfgVirtServiceHttpHdrName_Type()
)
slbNewCfgVirtServiceHttpHdrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceHttpHdrName.setStatus("current")


class _SlbNewCfgVirtServiceUrlHashLen_Type(Integer32):
    """Custom type slbNewCfgVirtServiceUrlHashLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbNewCfgVirtServiceUrlHashLen_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceUrlHashLen_Object = MibTableColumn
slbNewCfgVirtServiceUrlHashLen = _SlbNewCfgVirtServiceUrlHashLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 27),
    _SlbNewCfgVirtServiceUrlHashLen_Type()
)
slbNewCfgVirtServiceUrlHashLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceUrlHashLen.setStatus("current")


class _SlbNewCfgVirtServiceDelete_Type(Integer32):
    """Custom type slbNewCfgVirtServiceDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgVirtServiceDelete_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceDelete_Object = MibTableColumn
slbNewCfgVirtServiceDelete = _SlbNewCfgVirtServiceDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 28),
    _SlbNewCfgVirtServiceDelete_Type()
)
slbNewCfgVirtServiceDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceDelete.setStatus("current")


class _SlbNewCfgVirtServiceDirect_Type(Integer32):
    """Custom type slbNewCfgVirtServiceDirect based on Integer32"""
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


_SlbNewCfgVirtServiceDirect_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceDirect_Object = MibTableColumn
slbNewCfgVirtServiceDirect = _SlbNewCfgVirtServiceDirect_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 29),
    _SlbNewCfgVirtServiceDirect_Type()
)
slbNewCfgVirtServiceDirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceDirect.setStatus("current")


class _SlbNewCfgVirtServiceThash_Type(Integer32):
    """Custom type slbNewCfgVirtServiceThash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sip", 1),
          ("sip-sport", 2))
    )


_SlbNewCfgVirtServiceThash_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceThash_Object = MibTableColumn
slbNewCfgVirtServiceThash = _SlbNewCfgVirtServiceThash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 30),
    _SlbNewCfgVirtServiceThash_Type()
)
slbNewCfgVirtServiceThash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceThash.setStatus("current")


class _SlbNewCfgVirtServiceLdapreset_Type(Integer32):
    """Custom type slbNewCfgVirtServiceLdapreset based on Integer32"""
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


_SlbNewCfgVirtServiceLdapreset_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceLdapreset_Object = MibTableColumn
slbNewCfgVirtServiceLdapreset = _SlbNewCfgVirtServiceLdapreset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 31),
    _SlbNewCfgVirtServiceLdapreset_Type()
)
slbNewCfgVirtServiceLdapreset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceLdapreset.setStatus("current")


class _SlbNewCfgVirtServiceLdapslb_Type(Integer32):
    """Custom type slbNewCfgVirtServiceLdapslb based on Integer32"""
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


_SlbNewCfgVirtServiceLdapslb_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceLdapslb_Object = MibTableColumn
slbNewCfgVirtServiceLdapslb = _SlbNewCfgVirtServiceLdapslb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 32),
    _SlbNewCfgVirtServiceLdapslb_Type()
)
slbNewCfgVirtServiceLdapslb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceLdapslb.setStatus("current")


class _SlbNewCfgVirtServiceSip_Type(Integer32):
    """Custom type slbNewCfgVirtServiceSip based on Integer32"""
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


_SlbNewCfgVirtServiceSip_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceSip_Object = MibTableColumn
slbNewCfgVirtServiceSip = _SlbNewCfgVirtServiceSip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 33),
    _SlbNewCfgVirtServiceSip_Type()
)
slbNewCfgVirtServiceSip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceSip.setStatus("current")


class _SlbNewCfgVirtServiceXForwardedFor_Type(Integer32):
    """Custom type slbNewCfgVirtServiceXForwardedFor based on Integer32"""
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


_SlbNewCfgVirtServiceXForwardedFor_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceXForwardedFor_Object = MibTableColumn
slbNewCfgVirtServiceXForwardedFor = _SlbNewCfgVirtServiceXForwardedFor_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 34),
    _SlbNewCfgVirtServiceXForwardedFor_Type()
)
slbNewCfgVirtServiceXForwardedFor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceXForwardedFor.setStatus("current")


class _SlbNewCfgVirtServiceHttpRedir_Type(Integer32):
    """Custom type slbNewCfgVirtServiceHttpRedir based on Integer32"""
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


_SlbNewCfgVirtServiceHttpRedir_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceHttpRedir_Object = MibTableColumn
slbNewCfgVirtServiceHttpRedir = _SlbNewCfgVirtServiceHttpRedir_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 35),
    _SlbNewCfgVirtServiceHttpRedir_Type()
)
slbNewCfgVirtServiceHttpRedir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceHttpRedir.setStatus("current")


class _SlbNewCfgVirtServicePbindRport_Type(Integer32):
    """Custom type slbNewCfgVirtServicePbindRport based on Integer32"""
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


_SlbNewCfgVirtServicePbindRport_Type.__name__ = "Integer32"
_SlbNewCfgVirtServicePbindRport_Object = MibTableColumn
slbNewCfgVirtServicePbindRport = _SlbNewCfgVirtServicePbindRport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 36),
    _SlbNewCfgVirtServicePbindRport_Type()
)
slbNewCfgVirtServicePbindRport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServicePbindRport.setStatus("current")


class _SlbNewCfgVirtServiceEgressPip_Type(Integer32):
    """Custom type slbNewCfgVirtServiceEgressPip based on Integer32"""
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


_SlbNewCfgVirtServiceEgressPip_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceEgressPip_Object = MibTableColumn
slbNewCfgVirtServiceEgressPip = _SlbNewCfgVirtServiceEgressPip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 37),
    _SlbNewCfgVirtServiceEgressPip_Type()
)
slbNewCfgVirtServiceEgressPip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceEgressPip.setStatus("current")


class _SlbNewCfgVirtServiceCookieDname_Type(Integer32):
    """Custom type slbNewCfgVirtServiceCookieDname based on Integer32"""
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


_SlbNewCfgVirtServiceCookieDname_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceCookieDname_Object = MibTableColumn
slbNewCfgVirtServiceCookieDname = _SlbNewCfgVirtServiceCookieDname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 38),
    _SlbNewCfgVirtServiceCookieDname_Type()
)
slbNewCfgVirtServiceCookieDname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceCookieDname.setStatus("current")


class _SlbNewCfgVirtServiceWts_Type(Integer32):
    """Custom type slbNewCfgVirtServiceWts based on Integer32"""
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


_SlbNewCfgVirtServiceWts_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceWts_Object = MibTableColumn
slbNewCfgVirtServiceWts = _SlbNewCfgVirtServiceWts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 39),
    _SlbNewCfgVirtServiceWts_Type()
)
slbNewCfgVirtServiceWts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceWts.setStatus("current")


class _SlbNewCfgVirtServiceUhash_Type(Integer32):
    """Custom type slbNewCfgVirtServiceUhash based on Integer32"""
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


_SlbNewCfgVirtServiceUhash_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceUhash_Object = MibTableColumn
slbNewCfgVirtServiceUhash = _SlbNewCfgVirtServiceUhash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 40),
    _SlbNewCfgVirtServiceUhash_Type()
)
slbNewCfgVirtServiceUhash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceUhash.setStatus("current")


class _SlbNewCfgVirtServiceTimeOut_Type(Integer32):
    """Custom type slbNewCfgVirtServiceTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_SlbNewCfgVirtServiceTimeOut_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceTimeOut_Object = MibTableColumn
slbNewCfgVirtServiceTimeOut = _SlbNewCfgVirtServiceTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 41),
    _SlbNewCfgVirtServiceTimeOut_Type()
)
slbNewCfgVirtServiceTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceTimeOut.setStatus("current")


class _SlbNewCfgVirtServiceSdpNat_Type(Integer32):
    """Custom type slbNewCfgVirtServiceSdpNat based on Integer32"""
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


_SlbNewCfgVirtServiceSdpNat_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceSdpNat_Object = MibTableColumn
slbNewCfgVirtServiceSdpNat = _SlbNewCfgVirtServiceSdpNat_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 42),
    _SlbNewCfgVirtServiceSdpNat_Type()
)
slbNewCfgVirtServiceSdpNat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceSdpNat.setStatus("current")


class _SlbNewCfgVirtServiceSessionMirror_Type(Integer32):
    """Custom type slbNewCfgVirtServiceSessionMirror based on Integer32"""
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


_SlbNewCfgVirtServiceSessionMirror_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceSessionMirror_Object = MibTableColumn
slbNewCfgVirtServiceSessionMirror = _SlbNewCfgVirtServiceSessionMirror_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 43),
    _SlbNewCfgVirtServiceSessionMirror_Type()
)
slbNewCfgVirtServiceSessionMirror.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceSessionMirror.setStatus("current")


class _SlbNewCfgVirtServiceSoftGrid_Type(Integer32):
    """Custom type slbNewCfgVirtServiceSoftGrid based on Integer32"""
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


_SlbNewCfgVirtServiceSoftGrid_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceSoftGrid_Object = MibTableColumn
slbNewCfgVirtServiceSoftGrid = _SlbNewCfgVirtServiceSoftGrid_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 44),
    _SlbNewCfgVirtServiceSoftGrid_Type()
)
slbNewCfgVirtServiceSoftGrid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceSoftGrid.setStatus("current")


class _SlbNewCfgVirtServiceConnPooling_Type(Integer32):
    """Custom type slbNewCfgVirtServiceConnPooling based on Integer32"""
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


_SlbNewCfgVirtServiceConnPooling_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceConnPooling_Object = MibTableColumn
slbNewCfgVirtServiceConnPooling = _SlbNewCfgVirtServiceConnPooling_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 6, 1, 45),
    _SlbNewCfgVirtServiceConnPooling_Type()
)
slbNewCfgVirtServiceConnPooling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceConnPooling.setStatus("current")
_SlbUrlBwmTableMaxSize_Type = Integer32
_SlbUrlBwmTableMaxSize_Object = MibScalar
slbUrlBwmTableMaxSize = _SlbUrlBwmTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 7),
    _SlbUrlBwmTableMaxSize_Type()
)
slbUrlBwmTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbUrlBwmTableMaxSize.setStatus("current")
_SlbCurCfgUrlBwmTable_Object = MibTable
slbCurCfgUrlBwmTable = _SlbCurCfgUrlBwmTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 8)
)
if mibBuilder.loadTexts:
    slbCurCfgUrlBwmTable.setStatus("current")
_SlbCurCfgUrlBwmEntry_Object = MibTableRow
slbCurCfgUrlBwmEntry = _SlbCurCfgUrlBwmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 8, 1)
)
slbCurCfgUrlBwmEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgUrlBwmVirtServIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgUrlBwmVirtServiceIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgUrlBwmUrlId"),
)
if mibBuilder.loadTexts:
    slbCurCfgUrlBwmEntry.setStatus("current")
_SlbCurCfgUrlBwmVirtServIndex_Type = Integer32
_SlbCurCfgUrlBwmVirtServIndex_Object = MibTableColumn
slbCurCfgUrlBwmVirtServIndex = _SlbCurCfgUrlBwmVirtServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 8, 1, 1),
    _SlbCurCfgUrlBwmVirtServIndex_Type()
)
slbCurCfgUrlBwmVirtServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlBwmVirtServIndex.setStatus("current")
_SlbCurCfgUrlBwmVirtServiceIndex_Type = Integer32
_SlbCurCfgUrlBwmVirtServiceIndex_Object = MibTableColumn
slbCurCfgUrlBwmVirtServiceIndex = _SlbCurCfgUrlBwmVirtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 8, 1, 2),
    _SlbCurCfgUrlBwmVirtServiceIndex_Type()
)
slbCurCfgUrlBwmVirtServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlBwmVirtServiceIndex.setStatus("current")
_SlbCurCfgUrlBwmUrlId_Type = Integer32
_SlbCurCfgUrlBwmUrlId_Object = MibTableColumn
slbCurCfgUrlBwmUrlId = _SlbCurCfgUrlBwmUrlId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 8, 1, 3),
    _SlbCurCfgUrlBwmUrlId_Type()
)
slbCurCfgUrlBwmUrlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlBwmUrlId.setStatus("current")
_SlbCurCfgUrlBwmContract_Type = Integer32
_SlbCurCfgUrlBwmContract_Object = MibTableColumn
slbCurCfgUrlBwmContract = _SlbCurCfgUrlBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 8, 1, 4),
    _SlbCurCfgUrlBwmContract_Type()
)
slbCurCfgUrlBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlBwmContract.setStatus("current")
_SlbNewCfgUrlBwmTable_Object = MibTable
slbNewCfgUrlBwmTable = _SlbNewCfgUrlBwmTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 9)
)
if mibBuilder.loadTexts:
    slbNewCfgUrlBwmTable.setStatus("current")
_SlbNewCfgUrlBwmEntry_Object = MibTableRow
slbNewCfgUrlBwmEntry = _SlbNewCfgUrlBwmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 9, 1)
)
slbNewCfgUrlBwmEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgUrlBwmVirtServIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgUrlBwmVirtServiceIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgUrlBwmUrlId"),
)
if mibBuilder.loadTexts:
    slbNewCfgUrlBwmEntry.setStatus("current")
_SlbNewCfgUrlBwmVirtServIndex_Type = Integer32
_SlbNewCfgUrlBwmVirtServIndex_Object = MibTableColumn
slbNewCfgUrlBwmVirtServIndex = _SlbNewCfgUrlBwmVirtServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 9, 1, 1),
    _SlbNewCfgUrlBwmVirtServIndex_Type()
)
slbNewCfgUrlBwmVirtServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlBwmVirtServIndex.setStatus("current")
_SlbNewCfgUrlBwmVirtServiceIndex_Type = Integer32
_SlbNewCfgUrlBwmVirtServiceIndex_Object = MibTableColumn
slbNewCfgUrlBwmVirtServiceIndex = _SlbNewCfgUrlBwmVirtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 9, 1, 2),
    _SlbNewCfgUrlBwmVirtServiceIndex_Type()
)
slbNewCfgUrlBwmVirtServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlBwmVirtServiceIndex.setStatus("current")
_SlbNewCfgUrlBwmUrlId_Type = Integer32
_SlbNewCfgUrlBwmUrlId_Object = MibTableColumn
slbNewCfgUrlBwmUrlId = _SlbNewCfgUrlBwmUrlId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 9, 1, 3),
    _SlbNewCfgUrlBwmUrlId_Type()
)
slbNewCfgUrlBwmUrlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlBwmUrlId.setStatus("current")
_SlbNewCfgUrlBwmContract_Type = Integer32
_SlbNewCfgUrlBwmContract_Object = MibTableColumn
slbNewCfgUrlBwmContract = _SlbNewCfgUrlBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 9, 1, 4),
    _SlbNewCfgUrlBwmContract_Type()
)
slbNewCfgUrlBwmContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlBwmContract.setStatus("current")


class _SlbNewCfgUrlBwmDelete_Type(Integer32):
    """Custom type slbNewCfgUrlBwmDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgUrlBwmDelete_Type.__name__ = "Integer32"
_SlbNewCfgUrlBwmDelete_Object = MibTableColumn
slbNewCfgUrlBwmDelete = _SlbNewCfgUrlBwmDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 4, 9, 1, 5),
    _SlbNewCfgUrlBwmDelete_Type()
)
slbNewCfgUrlBwmDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlBwmDelete.setStatus("current")
_PortCfg_ObjectIdentity = ObjectIdentity
portCfg = _PortCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5)
)
_SlbPortTableMaxSize_Type = Integer32
_SlbPortTableMaxSize_Object = MibScalar
slbPortTableMaxSize = _SlbPortTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 1),
    _SlbPortTableMaxSize_Type()
)
slbPortTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPortTableMaxSize.setStatus("current")
_SlbCurCfgPortTable_Object = MibTable
slbCurCfgPortTable = _SlbCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    slbCurCfgPortTable.setStatus("current")
_SlbCurCfgPortEntry_Object = MibTableRow
slbCurCfgPortEntry = _SlbCurCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 2, 1)
)
slbCurCfgPortEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgPortIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgPortEntry.setStatus("current")
_SlbCurCfgPortIndex_Type = Integer32
_SlbCurCfgPortIndex_Object = MibTableColumn
slbCurCfgPortIndex = _SlbCurCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 2, 1, 1),
    _SlbCurCfgPortIndex_Type()
)
slbCurCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortIndex.setStatus("current")


class _SlbCurCfgPortSlbState_Type(Integer32):
    """Custom type slbCurCfgPortSlbState based on Integer32"""
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
        *(("none", 1),
          ("client", 2),
          ("server", 3),
          ("client-server", 4))
    )


_SlbCurCfgPortSlbState_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbState_Object = MibTableColumn
slbCurCfgPortSlbState = _SlbCurCfgPortSlbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 2, 1, 2),
    _SlbCurCfgPortSlbState_Type()
)
slbCurCfgPortSlbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbState.setStatus("current")


class _SlbCurCfgPortSlbHotStandby_Type(Integer32):
    """Custom type slbCurCfgPortSlbHotStandby based on Integer32"""
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


_SlbCurCfgPortSlbHotStandby_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbHotStandby_Object = MibTableColumn
slbCurCfgPortSlbHotStandby = _SlbCurCfgPortSlbHotStandby_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 2, 1, 3),
    _SlbCurCfgPortSlbHotStandby_Type()
)
slbCurCfgPortSlbHotStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbHotStandby.setStatus("current")


class _SlbCurCfgPortSlbInterSwitch_Type(Integer32):
    """Custom type slbCurCfgPortSlbInterSwitch based on Integer32"""
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


_SlbCurCfgPortSlbInterSwitch_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbInterSwitch_Object = MibTableColumn
slbCurCfgPortSlbInterSwitch = _SlbCurCfgPortSlbInterSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 2, 1, 4),
    _SlbCurCfgPortSlbInterSwitch_Type()
)
slbCurCfgPortSlbInterSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbInterSwitch.setStatus("current")


class _SlbCurCfgPortSlbPipState_Type(Integer32):
    """Custom type slbCurCfgPortSlbPipState based on Integer32"""
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


_SlbCurCfgPortSlbPipState_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbPipState_Object = MibTableColumn
slbCurCfgPortSlbPipState = _SlbCurCfgPortSlbPipState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 2, 1, 5),
    _SlbCurCfgPortSlbPipState_Type()
)
slbCurCfgPortSlbPipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbPipState.setStatus("current")


class _SlbCurCfgPortSlbRtsState_Type(Integer32):
    """Custom type slbCurCfgPortSlbRtsState based on Integer32"""
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


_SlbCurCfgPortSlbRtsState_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbRtsState_Object = MibTableColumn
slbCurCfgPortSlbRtsState = _SlbCurCfgPortSlbRtsState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 2, 1, 6),
    _SlbCurCfgPortSlbRtsState_Type()
)
slbCurCfgPortSlbRtsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbRtsState.setStatus("current")


class _SlbCurCfgPortSlbIdslbState_Type(Integer32):
    """Custom type slbCurCfgPortSlbIdslbState based on Integer32"""
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


_SlbCurCfgPortSlbIdslbState_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbIdslbState_Object = MibTableColumn
slbCurCfgPortSlbIdslbState = _SlbCurCfgPortSlbIdslbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 2, 1, 7),
    _SlbCurCfgPortSlbIdslbState_Type()
)
slbCurCfgPortSlbIdslbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbIdslbState.setStatus("current")
_SlbNewCfgPortTable_Object = MibTable
slbNewCfgPortTable = _SlbNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    slbNewCfgPortTable.setStatus("current")
_SlbNewCfgPortEntry_Object = MibTableRow
slbNewCfgPortEntry = _SlbNewCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 3, 1)
)
slbNewCfgPortEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgPortIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgPortEntry.setStatus("current")
_SlbNewCfgPortIndex_Type = Integer32
_SlbNewCfgPortIndex_Object = MibTableColumn
slbNewCfgPortIndex = _SlbNewCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 3, 1, 1),
    _SlbNewCfgPortIndex_Type()
)
slbNewCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgPortIndex.setStatus("current")


class _SlbNewCfgPortSlbState_Type(Integer32):
    """Custom type slbNewCfgPortSlbState based on Integer32"""
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
        *(("none", 1),
          ("client", 2),
          ("server", 3),
          ("client-server", 4))
    )


_SlbNewCfgPortSlbState_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbState_Object = MibTableColumn
slbNewCfgPortSlbState = _SlbNewCfgPortSlbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 3, 1, 2),
    _SlbNewCfgPortSlbState_Type()
)
slbNewCfgPortSlbState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbState.setStatus("current")


class _SlbNewCfgPortSlbHotStandby_Type(Integer32):
    """Custom type slbNewCfgPortSlbHotStandby based on Integer32"""
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


_SlbNewCfgPortSlbHotStandby_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbHotStandby_Object = MibTableColumn
slbNewCfgPortSlbHotStandby = _SlbNewCfgPortSlbHotStandby_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 3, 1, 3),
    _SlbNewCfgPortSlbHotStandby_Type()
)
slbNewCfgPortSlbHotStandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbHotStandby.setStatus("current")


class _SlbNewCfgPortSlbInterSwitch_Type(Integer32):
    """Custom type slbNewCfgPortSlbInterSwitch based on Integer32"""
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


_SlbNewCfgPortSlbInterSwitch_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbInterSwitch_Object = MibTableColumn
slbNewCfgPortSlbInterSwitch = _SlbNewCfgPortSlbInterSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 3, 1, 4),
    _SlbNewCfgPortSlbInterSwitch_Type()
)
slbNewCfgPortSlbInterSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbInterSwitch.setStatus("current")


class _SlbNewCfgPortSlbPipState_Type(Integer32):
    """Custom type slbNewCfgPortSlbPipState based on Integer32"""
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


_SlbNewCfgPortSlbPipState_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbPipState_Object = MibTableColumn
slbNewCfgPortSlbPipState = _SlbNewCfgPortSlbPipState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 3, 1, 5),
    _SlbNewCfgPortSlbPipState_Type()
)
slbNewCfgPortSlbPipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbPipState.setStatus("current")


class _SlbNewCfgPortSlbRtsState_Type(Integer32):
    """Custom type slbNewCfgPortSlbRtsState based on Integer32"""
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


_SlbNewCfgPortSlbRtsState_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbRtsState_Object = MibTableColumn
slbNewCfgPortSlbRtsState = _SlbNewCfgPortSlbRtsState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 3, 1, 6),
    _SlbNewCfgPortSlbRtsState_Type()
)
slbNewCfgPortSlbRtsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbRtsState.setStatus("current")


class _SlbNewCfgPortDelete_Type(Integer32):
    """Custom type slbNewCfgPortDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgPortDelete_Type.__name__ = "Integer32"
_SlbNewCfgPortDelete_Object = MibTableColumn
slbNewCfgPortDelete = _SlbNewCfgPortDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 3, 1, 7),
    _SlbNewCfgPortDelete_Type()
)
slbNewCfgPortDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortDelete.setStatus("current")


class _SlbNewCfgPortSlbIdslbState_Type(Integer32):
    """Custom type slbNewCfgPortSlbIdslbState based on Integer32"""
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


_SlbNewCfgPortSlbIdslbState_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbIdslbState_Object = MibTableColumn
slbNewCfgPortSlbIdslbState = _SlbNewCfgPortSlbIdslbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 5, 3, 1, 8),
    _SlbNewCfgPortSlbIdslbState_Type()
)
slbNewCfgPortSlbIdslbState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbIdslbState.setStatus("current")
_SyncCfg_ObjectIdentity = ObjectIdentity
syncCfg = _SyncCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6)
)
_SyncGeneralCfg_ObjectIdentity = ObjectIdentity
syncGeneralCfg = _SyncGeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1)
)


class _SlbCurCfgSyncFilt_Type(Integer32):
    """Custom type slbCurCfgSyncFilt based on Integer32"""
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


_SlbCurCfgSyncFilt_Type.__name__ = "Integer32"
_SlbCurCfgSyncFilt_Object = MibScalar
slbCurCfgSyncFilt = _SlbCurCfgSyncFilt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 1),
    _SlbCurCfgSyncFilt_Type()
)
slbCurCfgSyncFilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncFilt.setStatus("current")


class _SlbNewCfgSyncFilt_Type(Integer32):
    """Custom type slbNewCfgSyncFilt based on Integer32"""
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


_SlbNewCfgSyncFilt_Type.__name__ = "Integer32"
_SlbNewCfgSyncFilt_Object = MibScalar
slbNewCfgSyncFilt = _SlbNewCfgSyncFilt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 2),
    _SlbNewCfgSyncFilt_Type()
)
slbNewCfgSyncFilt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncFilt.setStatus("current")


class _SlbCurCfgSyncPort_Type(Integer32):
    """Custom type slbCurCfgSyncPort based on Integer32"""
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


_SlbCurCfgSyncPort_Type.__name__ = "Integer32"
_SlbCurCfgSyncPort_Object = MibScalar
slbCurCfgSyncPort = _SlbCurCfgSyncPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 3),
    _SlbCurCfgSyncPort_Type()
)
slbCurCfgSyncPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncPort.setStatus("current")


class _SlbNewCfgSyncPort_Type(Integer32):
    """Custom type slbNewCfgSyncPort based on Integer32"""
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


_SlbNewCfgSyncPort_Type.__name__ = "Integer32"
_SlbNewCfgSyncPort_Object = MibScalar
slbNewCfgSyncPort = _SlbNewCfgSyncPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 4),
    _SlbNewCfgSyncPort_Type()
)
slbNewCfgSyncPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncPort.setStatus("current")


class _SlbCurCfgSyncVrrp_Type(Integer32):
    """Custom type slbCurCfgSyncVrrp based on Integer32"""
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


_SlbCurCfgSyncVrrp_Type.__name__ = "Integer32"
_SlbCurCfgSyncVrrp_Object = MibScalar
slbCurCfgSyncVrrp = _SlbCurCfgSyncVrrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 5),
    _SlbCurCfgSyncVrrp_Type()
)
slbCurCfgSyncVrrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncVrrp.setStatus("current")


class _SlbNewCfgSyncVrrp_Type(Integer32):
    """Custom type slbNewCfgSyncVrrp based on Integer32"""
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


_SlbNewCfgSyncVrrp_Type.__name__ = "Integer32"
_SlbNewCfgSyncVrrp_Object = MibScalar
slbNewCfgSyncVrrp = _SlbNewCfgSyncVrrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 6),
    _SlbNewCfgSyncVrrp_Type()
)
slbNewCfgSyncVrrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncVrrp.setStatus("current")


class _SlbCurCfgSyncPip_Type(Integer32):
    """Custom type slbCurCfgSyncPip based on Integer32"""
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


_SlbCurCfgSyncPip_Type.__name__ = "Integer32"
_SlbCurCfgSyncPip_Object = MibScalar
slbCurCfgSyncPip = _SlbCurCfgSyncPip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 7),
    _SlbCurCfgSyncPip_Type()
)
slbCurCfgSyncPip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncPip.setStatus("current")


class _SlbNewCfgSyncPip_Type(Integer32):
    """Custom type slbNewCfgSyncPip based on Integer32"""
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


_SlbNewCfgSyncPip_Type.__name__ = "Integer32"
_SlbNewCfgSyncPip_Object = MibScalar
slbNewCfgSyncPip = _SlbNewCfgSyncPip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 8),
    _SlbNewCfgSyncPip_Type()
)
slbNewCfgSyncPip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncPip.setStatus("current")


class _SlbCurCfgSyncSfo_Type(Integer32):
    """Custom type slbCurCfgSyncSfo based on Integer32"""
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


_SlbCurCfgSyncSfo_Type.__name__ = "Integer32"
_SlbCurCfgSyncSfo_Object = MibScalar
slbCurCfgSyncSfo = _SlbCurCfgSyncSfo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 9),
    _SlbCurCfgSyncSfo_Type()
)
slbCurCfgSyncSfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncSfo.setStatus("current")


class _SlbNewCfgSyncSfo_Type(Integer32):
    """Custom type slbNewCfgSyncSfo based on Integer32"""
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


_SlbNewCfgSyncSfo_Type.__name__ = "Integer32"
_SlbNewCfgSyncSfo_Object = MibScalar
slbNewCfgSyncSfo = _SlbNewCfgSyncSfo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 10),
    _SlbNewCfgSyncSfo_Type()
)
slbNewCfgSyncSfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncSfo.setStatus("current")


class _SlbCurCfgSyncSfoUpdatePeriod_Type(Integer32):
    """Custom type slbCurCfgSyncSfoUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SlbCurCfgSyncSfoUpdatePeriod_Type.__name__ = "Integer32"
_SlbCurCfgSyncSfoUpdatePeriod_Object = MibScalar
slbCurCfgSyncSfoUpdatePeriod = _SlbCurCfgSyncSfoUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 11),
    _SlbCurCfgSyncSfoUpdatePeriod_Type()
)
slbCurCfgSyncSfoUpdatePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncSfoUpdatePeriod.setStatus("current")


class _SlbNewCfgSyncSfoUpdatePeriod_Type(Integer32):
    """Custom type slbNewCfgSyncSfoUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SlbNewCfgSyncSfoUpdatePeriod_Type.__name__ = "Integer32"
_SlbNewCfgSyncSfoUpdatePeriod_Object = MibScalar
slbNewCfgSyncSfoUpdatePeriod = _SlbNewCfgSyncSfoUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 12),
    _SlbNewCfgSyncSfoUpdatePeriod_Type()
)
slbNewCfgSyncSfoUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncSfoUpdatePeriod.setStatus("current")


class _SlbCurCfgSyncBwm_Type(Integer32):
    """Custom type slbCurCfgSyncBwm based on Integer32"""
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


_SlbCurCfgSyncBwm_Type.__name__ = "Integer32"
_SlbCurCfgSyncBwm_Object = MibScalar
slbCurCfgSyncBwm = _SlbCurCfgSyncBwm_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 13),
    _SlbCurCfgSyncBwm_Type()
)
slbCurCfgSyncBwm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncBwm.setStatus("current")


class _SlbNewCfgSyncBwm_Type(Integer32):
    """Custom type slbNewCfgSyncBwm based on Integer32"""
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


_SlbNewCfgSyncBwm_Type.__name__ = "Integer32"
_SlbNewCfgSyncBwm_Object = MibScalar
slbNewCfgSyncBwm = _SlbNewCfgSyncBwm_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 14),
    _SlbNewCfgSyncBwm_Type()
)
slbNewCfgSyncBwm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncBwm.setStatus("current")


class _SlbCurCfgSyncPeerPip_Type(Integer32):
    """Custom type slbCurCfgSyncPeerPip based on Integer32"""
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


_SlbCurCfgSyncPeerPip_Type.__name__ = "Integer32"
_SlbCurCfgSyncPeerPip_Object = MibScalar
slbCurCfgSyncPeerPip = _SlbCurCfgSyncPeerPip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 15),
    _SlbCurCfgSyncPeerPip_Type()
)
slbCurCfgSyncPeerPip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncPeerPip.setStatus("current")


class _SlbNewCfgSyncPeerPip_Type(Integer32):
    """Custom type slbNewCfgSyncPeerPip based on Integer32"""
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


_SlbNewCfgSyncPeerPip_Type.__name__ = "Integer32"
_SlbNewCfgSyncPeerPip_Object = MibScalar
slbNewCfgSyncPeerPip = _SlbNewCfgSyncPeerPip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 1, 16),
    _SlbNewCfgSyncPeerPip_Type()
)
slbNewCfgSyncPeerPip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncPeerPip.setStatus("current")
_SlbPeerTableMaxSize_Type = Integer32
_SlbPeerTableMaxSize_Object = MibScalar
slbPeerTableMaxSize = _SlbPeerTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 2),
    _SlbPeerTableMaxSize_Type()
)
slbPeerTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPeerTableMaxSize.setStatus("current")
_SlbCurCfgPeerTable_Object = MibTable
slbCurCfgPeerTable = _SlbCurCfgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    slbCurCfgPeerTable.setStatus("current")
_SlbCurCfgPeerEntry_Object = MibTableRow
slbCurCfgPeerEntry = _SlbCurCfgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 3, 1)
)
slbCurCfgPeerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgPeerIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgPeerEntry.setStatus("current")
_SlbCurCfgPeerIndex_Type = Integer32
_SlbCurCfgPeerIndex_Object = MibTableColumn
slbCurCfgPeerIndex = _SlbCurCfgPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 3, 1, 1),
    _SlbCurCfgPeerIndex_Type()
)
slbCurCfgPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPeerIndex.setStatus("current")
_SlbCurCfgPeerIpAddr_Type = IpAddress
_SlbCurCfgPeerIpAddr_Object = MibTableColumn
slbCurCfgPeerIpAddr = _SlbCurCfgPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 3, 1, 2),
    _SlbCurCfgPeerIpAddr_Type()
)
slbCurCfgPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPeerIpAddr.setStatus("current")


class _SlbCurCfgPeerState_Type(Integer32):
    """Custom type slbCurCfgPeerState based on Integer32"""
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


_SlbCurCfgPeerState_Type.__name__ = "Integer32"
_SlbCurCfgPeerState_Object = MibTableColumn
slbCurCfgPeerState = _SlbCurCfgPeerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 3, 1, 3),
    _SlbCurCfgPeerState_Type()
)
slbCurCfgPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPeerState.setStatus("current")
_SlbNewCfgPeerTable_Object = MibTable
slbNewCfgPeerTable = _SlbNewCfgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    slbNewCfgPeerTable.setStatus("current")
_SlbNewCfgPeerEntry_Object = MibTableRow
slbNewCfgPeerEntry = _SlbNewCfgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 4, 1)
)
slbNewCfgPeerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgPeerIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgPeerEntry.setStatus("current")
_SlbNewCfgPeerIndex_Type = Integer32
_SlbNewCfgPeerIndex_Object = MibTableColumn
slbNewCfgPeerIndex = _SlbNewCfgPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 4, 1, 1),
    _SlbNewCfgPeerIndex_Type()
)
slbNewCfgPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgPeerIndex.setStatus("current")
_SlbNewCfgPeerIpAddr_Type = IpAddress
_SlbNewCfgPeerIpAddr_Object = MibTableColumn
slbNewCfgPeerIpAddr = _SlbNewCfgPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 4, 1, 2),
    _SlbNewCfgPeerIpAddr_Type()
)
slbNewCfgPeerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgPeerIpAddr.setStatus("current")


class _SlbNewCfgPeerState_Type(Integer32):
    """Custom type slbNewCfgPeerState based on Integer32"""
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


_SlbNewCfgPeerState_Type.__name__ = "Integer32"
_SlbNewCfgPeerState_Object = MibTableColumn
slbNewCfgPeerState = _SlbNewCfgPeerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 4, 1, 3),
    _SlbNewCfgPeerState_Type()
)
slbNewCfgPeerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgPeerState.setStatus("current")


class _SlbNewCfgPeerDelete_Type(Integer32):
    """Custom type slbNewCfgPeerDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgPeerDelete_Type.__name__ = "Integer32"
_SlbNewCfgPeerDelete_Object = MibTableColumn
slbNewCfgPeerDelete = _SlbNewCfgPeerDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 6, 4, 1, 4),
    _SlbNewCfgPeerDelete_Type()
)
slbNewCfgPeerDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgPeerDelete.setStatus("current")
_WapCfg_ObjectIdentity = ObjectIdentity
wapCfg = _WapCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 7)
)


class _SlbCurCfgWapTpcp_Type(Integer32):
    """Custom type slbCurCfgWapTpcp based on Integer32"""
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


_SlbCurCfgWapTpcp_Type.__name__ = "Integer32"
_SlbCurCfgWapTpcp_Object = MibScalar
slbCurCfgWapTpcp = _SlbCurCfgWapTpcp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 7, 1),
    _SlbCurCfgWapTpcp_Type()
)
slbCurCfgWapTpcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWapTpcp.setStatus("current")


class _SlbNewCfgWapTpcp_Type(Integer32):
    """Custom type slbNewCfgWapTpcp based on Integer32"""
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


_SlbNewCfgWapTpcp_Type.__name__ = "Integer32"
_SlbNewCfgWapTpcp_Object = MibScalar
slbNewCfgWapTpcp = _SlbNewCfgWapTpcp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 7, 2),
    _SlbNewCfgWapTpcp_Type()
)
slbNewCfgWapTpcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWapTpcp.setStatus("current")


class _SlbCurCfgWapDebug_Type(Integer32):
    """Custom type slbCurCfgWapDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SlbCurCfgWapDebug_Type.__name__ = "Integer32"
_SlbCurCfgWapDebug_Object = MibScalar
slbCurCfgWapDebug = _SlbCurCfgWapDebug_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 7, 3),
    _SlbCurCfgWapDebug_Type()
)
slbCurCfgWapDebug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWapDebug.setStatus("current")


class _SlbNewCfgWapDebug_Type(Integer32):
    """Custom type slbNewCfgWapDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SlbNewCfgWapDebug_Type.__name__ = "Integer32"
_SlbNewCfgWapDebug_Object = MibScalar
slbNewCfgWapDebug = _SlbNewCfgWapDebug_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 7, 4),
    _SlbNewCfgWapDebug_Type()
)
slbNewCfgWapDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWapDebug.setStatus("current")
_WaphcCfg_ObjectIdentity = ObjectIdentity
waphcCfg = _WaphcCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8)
)


class _SlbCurCfgWaphcWSPPort_Type(Integer32):
    """Custom type slbCurCfgWaphcWSPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbCurCfgWaphcWSPPort_Type.__name__ = "Integer32"
_SlbCurCfgWaphcWSPPort_Object = MibScalar
slbCurCfgWaphcWSPPort = _SlbCurCfgWaphcWSPPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 1),
    _SlbCurCfgWaphcWSPPort_Type()
)
slbCurCfgWaphcWSPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcWSPPort.setStatus("current")


class _SlbNewCfgWaphcWSPPort_Type(Integer32):
    """Custom type slbNewCfgWaphcWSPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbNewCfgWaphcWSPPort_Type.__name__ = "Integer32"
_SlbNewCfgWaphcWSPPort_Object = MibScalar
slbNewCfgWaphcWSPPort = _SlbNewCfgWaphcWSPPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 2),
    _SlbNewCfgWaphcWSPPort_Type()
)
slbNewCfgWaphcWSPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcWSPPort.setStatus("current")


class _SlbCurCfgWaphcOffset_Type(Integer32):
    """Custom type slbCurCfgWaphcOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SlbCurCfgWaphcOffset_Type.__name__ = "Integer32"
_SlbCurCfgWaphcOffset_Object = MibScalar
slbCurCfgWaphcOffset = _SlbCurCfgWaphcOffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 3),
    _SlbCurCfgWaphcOffset_Type()
)
slbCurCfgWaphcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcOffset.setStatus("current")


class _SlbNewCfgWaphcOffset_Type(Integer32):
    """Custom type slbNewCfgWaphcOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SlbNewCfgWaphcOffset_Type.__name__ = "Integer32"
_SlbNewCfgWaphcOffset_Object = MibScalar
slbNewCfgWaphcOffset = _SlbNewCfgWaphcOffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 4),
    _SlbNewCfgWaphcOffset_Type()
)
slbNewCfgWaphcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcOffset.setStatus("current")


class _SlbCurCfgWaphcSndContent_Type(OctetString):
    """Custom type slbCurCfgWaphcSndContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SlbCurCfgWaphcSndContent_Type.__name__ = "OctetString"
_SlbCurCfgWaphcSndContent_Object = MibScalar
slbCurCfgWaphcSndContent = _SlbCurCfgWaphcSndContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 5),
    _SlbCurCfgWaphcSndContent_Type()
)
slbCurCfgWaphcSndContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcSndContent.setStatus("current")


class _SlbNewCfgWaphcSndContent_Type(OctetString):
    """Custom type slbNewCfgWaphcSndContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SlbNewCfgWaphcSndContent_Type.__name__ = "OctetString"
_SlbNewCfgWaphcSndContent_Object = MibScalar
slbNewCfgWaphcSndContent = _SlbNewCfgWaphcSndContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 6),
    _SlbNewCfgWaphcSndContent_Type()
)
slbNewCfgWaphcSndContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcSndContent.setStatus("current")


class _SlbCurCfgWaphcRcvContent_Type(OctetString):
    """Custom type slbCurCfgWaphcRcvContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SlbCurCfgWaphcRcvContent_Type.__name__ = "OctetString"
_SlbCurCfgWaphcRcvContent_Object = MibScalar
slbCurCfgWaphcRcvContent = _SlbCurCfgWaphcRcvContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 7),
    _SlbCurCfgWaphcRcvContent_Type()
)
slbCurCfgWaphcRcvContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcRcvContent.setStatus("current")


class _SlbNewCfgWaphcRcvContent_Type(OctetString):
    """Custom type slbNewCfgWaphcRcvContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SlbNewCfgWaphcRcvContent_Type.__name__ = "OctetString"
_SlbNewCfgWaphcRcvContent_Object = MibScalar
slbNewCfgWaphcRcvContent = _SlbNewCfgWaphcRcvContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 8),
    _SlbNewCfgWaphcRcvContent_Type()
)
slbNewCfgWaphcRcvContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcRcvContent.setStatus("current")


class _SlbCurCfgWaphcWTLSPort_Type(Integer32):
    """Custom type slbCurCfgWaphcWTLSPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbCurCfgWaphcWTLSPort_Type.__name__ = "Integer32"
_SlbCurCfgWaphcWTLSPort_Object = MibScalar
slbCurCfgWaphcWTLSPort = _SlbCurCfgWaphcWTLSPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 9),
    _SlbCurCfgWaphcWTLSPort_Type()
)
slbCurCfgWaphcWTLSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcWTLSPort.setStatus("current")


class _SlbNewCfgWaphcWTLSPort_Type(Integer32):
    """Custom type slbNewCfgWaphcWTLSPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbNewCfgWaphcWTLSPort_Type.__name__ = "Integer32"
_SlbNewCfgWaphcWTLSPort_Object = MibScalar
slbNewCfgWaphcWTLSPort = _SlbNewCfgWaphcWTLSPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 10),
    _SlbNewCfgWaphcWTLSPort_Type()
)
slbNewCfgWaphcWTLSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcWTLSPort.setStatus("current")


class _SlbCurCfgWaphcWTPSndContent_Type(OctetString):
    """Custom type slbCurCfgWaphcWTPSndContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SlbCurCfgWaphcWTPSndContent_Type.__name__ = "OctetString"
_SlbCurCfgWaphcWTPSndContent_Object = MibScalar
slbCurCfgWaphcWTPSndContent = _SlbCurCfgWaphcWTPSndContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 11),
    _SlbCurCfgWaphcWTPSndContent_Type()
)
slbCurCfgWaphcWTPSndContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcWTPSndContent.setStatus("current")


class _SlbNewCfgWaphcWTPSndContent_Type(OctetString):
    """Custom type slbNewCfgWaphcWTPSndContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SlbNewCfgWaphcWTPSndContent_Type.__name__ = "OctetString"
_SlbNewCfgWaphcWTPSndContent_Object = MibScalar
slbNewCfgWaphcWTPSndContent = _SlbNewCfgWaphcWTPSndContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 12),
    _SlbNewCfgWaphcWTPSndContent_Type()
)
slbNewCfgWaphcWTPSndContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcWTPSndContent.setStatus("current")


class _SlbCurCfgWaphcWTPRcvContent_Type(OctetString):
    """Custom type slbCurCfgWaphcWTPRcvContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SlbCurCfgWaphcWTPRcvContent_Type.__name__ = "OctetString"
_SlbCurCfgWaphcWTPRcvContent_Object = MibScalar
slbCurCfgWaphcWTPRcvContent = _SlbCurCfgWaphcWTPRcvContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 13),
    _SlbCurCfgWaphcWTPRcvContent_Type()
)
slbCurCfgWaphcWTPRcvContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcWTPRcvContent.setStatus("current")


class _SlbNewCfgWaphcWTPRcvContent_Type(OctetString):
    """Custom type slbNewCfgWaphcWTPRcvContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SlbNewCfgWaphcWTPRcvContent_Type.__name__ = "OctetString"
_SlbNewCfgWaphcWTPRcvContent_Object = MibScalar
slbNewCfgWaphcWTPRcvContent = _SlbNewCfgWaphcWTPRcvContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 14),
    _SlbNewCfgWaphcWTPRcvContent_Type()
)
slbNewCfgWaphcWTPRcvContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcWTPRcvContent.setStatus("current")


class _SlbCurCfgWaphcWTPConnContent_Type(OctetString):
    """Custom type slbCurCfgWaphcWTPConnContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SlbCurCfgWaphcWTPConnContent_Type.__name__ = "OctetString"
_SlbCurCfgWaphcWTPConnContent_Object = MibScalar
slbCurCfgWaphcWTPConnContent = _SlbCurCfgWaphcWTPConnContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 15),
    _SlbCurCfgWaphcWTPConnContent_Type()
)
slbCurCfgWaphcWTPConnContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcWTPConnContent.setStatus("current")


class _SlbNewCfgWaphcWTPConnContent_Type(OctetString):
    """Custom type slbNewCfgWaphcWTPConnContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SlbNewCfgWaphcWTPConnContent_Type.__name__ = "OctetString"
_SlbNewCfgWaphcWTPConnContent_Object = MibScalar
slbNewCfgWaphcWTPConnContent = _SlbNewCfgWaphcWTPConnContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 16),
    _SlbNewCfgWaphcWTPConnContent_Type()
)
slbNewCfgWaphcWTPConnContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcWTPConnContent.setStatus("current")


class _SlbCurCfgWaphcWTPPort_Type(Integer32):
    """Custom type slbCurCfgWaphcWTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbCurCfgWaphcWTPPort_Type.__name__ = "Integer32"
_SlbCurCfgWaphcWTPPort_Object = MibScalar
slbCurCfgWaphcWTPPort = _SlbCurCfgWaphcWTPPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 17),
    _SlbCurCfgWaphcWTPPort_Type()
)
slbCurCfgWaphcWTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcWTPPort.setStatus("current")


class _SlbNewCfgWaphcWTPPort_Type(Integer32):
    """Custom type slbNewCfgWaphcWTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbNewCfgWaphcWTPPort_Type.__name__ = "Integer32"
_SlbNewCfgWaphcWTPPort_Object = MibScalar
slbNewCfgWaphcWTPPort = _SlbNewCfgWaphcWTPPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 18),
    _SlbNewCfgWaphcWTPPort_Type()
)
slbNewCfgWaphcWTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcWTPPort.setStatus("current")


class _SlbCurCfgWaphcWTLSWSPPort_Type(Integer32):
    """Custom type slbCurCfgWaphcWTLSWSPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbCurCfgWaphcWTLSWSPPort_Type.__name__ = "Integer32"
_SlbCurCfgWaphcWTLSWSPPort_Object = MibScalar
slbCurCfgWaphcWTLSWSPPort = _SlbCurCfgWaphcWTLSWSPPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 19),
    _SlbCurCfgWaphcWTLSWSPPort_Type()
)
slbCurCfgWaphcWTLSWSPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcWTLSWSPPort.setStatus("current")


class _SlbNewCfgWaphcWTLSWSPPort_Type(Integer32):
    """Custom type slbNewCfgWaphcWTLSWSPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbNewCfgWaphcWTLSWSPPort_Type.__name__ = "Integer32"
_SlbNewCfgWaphcWTLSWSPPort_Object = MibScalar
slbNewCfgWaphcWTLSWSPPort = _SlbNewCfgWaphcWTLSWSPPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 20),
    _SlbNewCfgWaphcWTLSWSPPort_Type()
)
slbNewCfgWaphcWTLSWSPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcWTLSWSPPort.setStatus("current")


class _SlbCurCfgWaphcWTPOffset_Type(Integer32):
    """Custom type slbCurCfgWaphcWTPOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SlbCurCfgWaphcWTPOffset_Type.__name__ = "Integer32"
_SlbCurCfgWaphcWTPOffset_Object = MibScalar
slbCurCfgWaphcWTPOffset = _SlbCurCfgWaphcWTPOffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 21),
    _SlbCurCfgWaphcWTPOffset_Type()
)
slbCurCfgWaphcWTPOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcWTPOffset.setStatus("current")


class _SlbNewCfgWaphcWTPOffset_Type(Integer32):
    """Custom type slbNewCfgWaphcWTPOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SlbNewCfgWaphcWTPOffset_Type.__name__ = "Integer32"
_SlbNewCfgWaphcWTPOffset_Object = MibScalar
slbNewCfgWaphcWTPOffset = _SlbNewCfgWaphcWTPOffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 22),
    _SlbNewCfgWaphcWTPOffset_Type()
)
slbNewCfgWaphcWTPOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcWTPOffset.setStatus("current")


class _SlbCurCfgWaphcCouple_Type(Integer32):
    """Custom type slbCurCfgWaphcCouple based on Integer32"""
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


_SlbCurCfgWaphcCouple_Type.__name__ = "Integer32"
_SlbCurCfgWaphcCouple_Object = MibScalar
slbCurCfgWaphcCouple = _SlbCurCfgWaphcCouple_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 23),
    _SlbCurCfgWaphcCouple_Type()
)
slbCurCfgWaphcCouple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcCouple.setStatus("current")


class _SlbNewCfgWaphcCouple_Type(Integer32):
    """Custom type slbNewCfgWaphcCouple based on Integer32"""
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


_SlbNewCfgWaphcCouple_Type.__name__ = "Integer32"
_SlbNewCfgWaphcCouple_Object = MibScalar
slbNewCfgWaphcCouple = _SlbNewCfgWaphcCouple_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 8, 24),
    _SlbNewCfgWaphcCouple_Type()
)
slbNewCfgWaphcCouple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcCouple.setStatus("current")
_SynAttackDetCfg_ObjectIdentity = ObjectIdentity
synAttackDetCfg = _SynAttackDetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 9)
)


class _SynAttackCurCfgInterval_Type(Integer32):
    """Custom type synAttackCurCfgInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_SynAttackCurCfgInterval_Type.__name__ = "Integer32"
_SynAttackCurCfgInterval_Object = MibScalar
synAttackCurCfgInterval = _SynAttackCurCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 9, 1),
    _SynAttackCurCfgInterval_Type()
)
synAttackCurCfgInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    synAttackCurCfgInterval.setStatus("current")


class _SynAttackNewCfgInterval_Type(Integer32):
    """Custom type synAttackNewCfgInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_SynAttackNewCfgInterval_Type.__name__ = "Integer32"
_SynAttackNewCfgInterval_Object = MibScalar
synAttackNewCfgInterval = _SynAttackNewCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 9, 2),
    _SynAttackNewCfgInterval_Type()
)
synAttackNewCfgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synAttackNewCfgInterval.setStatus("current")


class _SynAttackCurCfgThreshhold_Type(Integer32):
    """Custom type synAttackCurCfgThreshhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_SynAttackCurCfgThreshhold_Type.__name__ = "Integer32"
_SynAttackCurCfgThreshhold_Object = MibScalar
synAttackCurCfgThreshhold = _SynAttackCurCfgThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 9, 3),
    _SynAttackCurCfgThreshhold_Type()
)
synAttackCurCfgThreshhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    synAttackCurCfgThreshhold.setStatus("current")


class _SynAttackNewCfgThreshhold_Type(Integer32):
    """Custom type synAttackNewCfgThreshhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_SynAttackNewCfgThreshhold_Type.__name__ = "Integer32"
_SynAttackNewCfgThreshhold_Object = MibScalar
synAttackNewCfgThreshhold = _SynAttackNewCfgThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 9, 4),
    _SynAttackNewCfgThreshhold_Type()
)
synAttackNewCfgThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synAttackNewCfgThreshhold.setStatus("current")
_HcsCfg_ObjectIdentity = ObjectIdentity
hcsCfg = _HcsCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13)
)
_HcsTableMaxSize_Type = Integer32
_HcsTableMaxSize_Object = MibScalar
hcsTableMaxSize = _HcsTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 1),
    _HcsTableMaxSize_Type()
)
hcsTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcsTableMaxSize.setStatus("current")
_HcsCurCfgTable_Object = MibTable
hcsCurCfgTable = _HcsCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 2)
)
if mibBuilder.loadTexts:
    hcsCurCfgTable.setStatus("current")
_HcsCurCfgTableEntry_Object = MibTableRow
hcsCurCfgTableEntry = _HcsCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 2, 1)
)
hcsCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "hcsCurCfgScriptIndex"),
)
if mibBuilder.loadTexts:
    hcsCurCfgTableEntry.setStatus("current")
_HcsCurCfgScriptIndex_Type = Integer32
_HcsCurCfgScriptIndex_Object = MibTableColumn
hcsCurCfgScriptIndex = _HcsCurCfgScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 2, 1, 1),
    _HcsCurCfgScriptIndex_Type()
)
hcsCurCfgScriptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcsCurCfgScriptIndex.setStatus("current")
_HcsCurCfgScriptString_Type = OctetString
_HcsCurCfgScriptString_Object = MibTableColumn
hcsCurCfgScriptString = _HcsCurCfgScriptString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 2, 1, 2),
    _HcsCurCfgScriptString_Type()
)
hcsCurCfgScriptString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcsCurCfgScriptString.setStatus("current")
_HcsNewCfgTable_Object = MibTable
hcsNewCfgTable = _HcsNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3)
)
if mibBuilder.loadTexts:
    hcsNewCfgTable.setStatus("current")
_HcsNewCfgTableEntry_Object = MibTableRow
hcsNewCfgTableEntry = _HcsNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1)
)
hcsNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "hcsNewCfgScriptIndex"),
)
if mibBuilder.loadTexts:
    hcsNewCfgTableEntry.setStatus("current")
_HcsNewCfgScriptIndex_Type = Integer32
_HcsNewCfgScriptIndex_Object = MibTableColumn
hcsNewCfgScriptIndex = _HcsNewCfgScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 1),
    _HcsNewCfgScriptIndex_Type()
)
hcsNewCfgScriptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcsNewCfgScriptIndex.setStatus("current")
_HcsNewCfgScriptString_Type = OctetString
_HcsNewCfgScriptString_Object = MibTableColumn
hcsNewCfgScriptString = _HcsNewCfgScriptString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 2),
    _HcsNewCfgScriptString_Type()
)
hcsNewCfgScriptString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcsNewCfgScriptString.setStatus("current")


class _HcsNewCfgAddSendCmd_Type(DisplayString):
    """Custom type hcsNewCfgAddSendCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HcsNewCfgAddSendCmd_Type.__name__ = "DisplayString"
_HcsNewCfgAddSendCmd_Object = MibTableColumn
hcsNewCfgAddSendCmd = _HcsNewCfgAddSendCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 4),
    _HcsNewCfgAddSendCmd_Type()
)
hcsNewCfgAddSendCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddSendCmd.setStatus("obsolete")


class _HcsNewCfgAddExpectCmd_Type(DisplayString):
    """Custom type hcsNewCfgAddExpectCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HcsNewCfgAddExpectCmd_Type.__name__ = "DisplayString"
_HcsNewCfgAddExpectCmd_Object = MibTableColumn
hcsNewCfgAddExpectCmd = _HcsNewCfgAddExpectCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 5),
    _HcsNewCfgAddExpectCmd_Type()
)
hcsNewCfgAddExpectCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddExpectCmd.setStatus("obsolete")


class _HcsNewCfgAddCloseCmd_Type(Integer32):
    """Custom type hcsNewCfgAddCloseCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("close", 2))
    )


_HcsNewCfgAddCloseCmd_Type.__name__ = "Integer32"
_HcsNewCfgAddCloseCmd_Object = MibTableColumn
hcsNewCfgAddCloseCmd = _HcsNewCfgAddCloseCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 6),
    _HcsNewCfgAddCloseCmd_Type()
)
hcsNewCfgAddCloseCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddCloseCmd.setStatus("current")


class _HcsNewCfgRemLastCmd_Type(Integer32):
    """Custom type hcsNewCfgRemLastCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("remove", 2))
    )


_HcsNewCfgRemLastCmd_Type.__name__ = "Integer32"
_HcsNewCfgRemLastCmd_Object = MibTableColumn
hcsNewCfgRemLastCmd = _HcsNewCfgRemLastCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 7),
    _HcsNewCfgRemLastCmd_Type()
)
hcsNewCfgRemLastCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgRemLastCmd.setStatus("current")


class _HcsNewCfgDeleteScript_Type(Integer32):
    """Custom type hcsNewCfgDeleteScript based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_HcsNewCfgDeleteScript_Type.__name__ = "Integer32"
_HcsNewCfgDeleteScript_Object = MibTableColumn
hcsNewCfgDeleteScript = _HcsNewCfgDeleteScript_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 8),
    _HcsNewCfgDeleteScript_Type()
)
hcsNewCfgDeleteScript.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgDeleteScript.setStatus("current")


class _HcsNewCfgAddOffsetCmd_Type(Integer32):
    """Custom type hcsNewCfgAddOffsetCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1464),
    )


_HcsNewCfgAddOffsetCmd_Type.__name__ = "Integer32"
_HcsNewCfgAddOffsetCmd_Object = MibTableColumn
hcsNewCfgAddOffsetCmd = _HcsNewCfgAddOffsetCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 9),
    _HcsNewCfgAddOffsetCmd_Type()
)
hcsNewCfgAddOffsetCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddOffsetCmd.setStatus("current")


class _HcsNewCfgAddWaitCmd_Type(Integer32):
    """Custom type hcsNewCfgAddWaitCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HcsNewCfgAddWaitCmd_Type.__name__ = "Integer32"
_HcsNewCfgAddWaitCmd_Object = MibTableColumn
hcsNewCfgAddWaitCmd = _HcsNewCfgAddWaitCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 10),
    _HcsNewCfgAddWaitCmd_Type()
)
hcsNewCfgAddWaitCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddWaitCmd.setStatus("current")


class _HcsNewCfgAddOpenProtCmd_Type(DisplayString):
    """Custom type hcsNewCfgAddOpenProtCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HcsNewCfgAddOpenProtCmd_Type.__name__ = "DisplayString"
_HcsNewCfgAddOpenProtCmd_Object = MibTableColumn
hcsNewCfgAddOpenProtCmd = _HcsNewCfgAddOpenProtCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 11),
    _HcsNewCfgAddOpenProtCmd_Type()
)
hcsNewCfgAddOpenProtCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddOpenProtCmd.setStatus("current")


class _HcsNewCfgAddNsendCmd_Type(DisplayString):
    """Custom type hcsNewCfgAddNsendCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HcsNewCfgAddNsendCmd_Type.__name__ = "DisplayString"
_HcsNewCfgAddNsendCmd_Object = MibTableColumn
hcsNewCfgAddNsendCmd = _HcsNewCfgAddNsendCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 12),
    _HcsNewCfgAddNsendCmd_Type()
)
hcsNewCfgAddNsendCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddNsendCmd.setStatus("obsolete")


class _HcsNewCfgAddNexpectCmd_Type(DisplayString):
    """Custom type hcsNewCfgAddNexpectCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HcsNewCfgAddNexpectCmd_Type.__name__ = "DisplayString"
_HcsNewCfgAddNexpectCmd_Object = MibTableColumn
hcsNewCfgAddNexpectCmd = _HcsNewCfgAddNexpectCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 13),
    _HcsNewCfgAddNexpectCmd_Type()
)
hcsNewCfgAddNexpectCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddNexpectCmd.setStatus("obsolete")


class _HcsNewCfgAddDepthCmd_Type(Integer32):
    """Custom type hcsNewCfgAddDepthCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1464),
    )


_HcsNewCfgAddDepthCmd_Type.__name__ = "Integer32"
_HcsNewCfgAddDepthCmd_Object = MibTableColumn
hcsNewCfgAddDepthCmd = _HcsNewCfgAddDepthCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 14),
    _HcsNewCfgAddDepthCmd_Type()
)
hcsNewCfgAddDepthCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddDepthCmd.setStatus("current")


class _HcsNewCfgAddLongBsendCmd_Type(OctetString):
    """Custom type hcsNewCfgAddLongBsendCmd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 506),
    )


_HcsNewCfgAddLongBsendCmd_Type.__name__ = "OctetString"
_HcsNewCfgAddLongBsendCmd_Object = MibTableColumn
hcsNewCfgAddLongBsendCmd = _HcsNewCfgAddLongBsendCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 15),
    _HcsNewCfgAddLongBsendCmd_Type()
)
hcsNewCfgAddLongBsendCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddLongBsendCmd.setStatus("current")


class _HcsNewCfgAddLongBexpectCmd_Type(OctetString):
    """Custom type hcsNewCfgAddLongBexpectCmd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 504),
    )


_HcsNewCfgAddLongBexpectCmd_Type.__name__ = "OctetString"
_HcsNewCfgAddLongBexpectCmd_Object = MibTableColumn
hcsNewCfgAddLongBexpectCmd = _HcsNewCfgAddLongBexpectCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 16),
    _HcsNewCfgAddLongBexpectCmd_Type()
)
hcsNewCfgAddLongBexpectCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddLongBexpectCmd.setStatus("current")


class _HcsNewCfgAddLongSendCmd_Type(OctetString):
    """Custom type hcsNewCfgAddLongSendCmd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 507),
    )


_HcsNewCfgAddLongSendCmd_Type.__name__ = "OctetString"
_HcsNewCfgAddLongSendCmd_Object = MibTableColumn
hcsNewCfgAddLongSendCmd = _HcsNewCfgAddLongSendCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 17),
    _HcsNewCfgAddLongSendCmd_Type()
)
hcsNewCfgAddLongSendCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddLongSendCmd.setStatus("current")


class _HcsNewCfgAddLongExpectCmd_Type(OctetString):
    """Custom type hcsNewCfgAddLongExpectCmd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 505),
    )


_HcsNewCfgAddLongExpectCmd_Type.__name__ = "OctetString"
_HcsNewCfgAddLongExpectCmd_Object = MibTableColumn
hcsNewCfgAddLongExpectCmd = _HcsNewCfgAddLongExpectCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 18),
    _HcsNewCfgAddLongExpectCmd_Type()
)
hcsNewCfgAddLongExpectCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddLongExpectCmd.setStatus("current")


class _HcsNewCfgAddLongNsendCmd_Type(OctetString):
    """Custom type hcsNewCfgAddLongNsendCmd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 506),
    )


_HcsNewCfgAddLongNsendCmd_Type.__name__ = "OctetString"
_HcsNewCfgAddLongNsendCmd_Object = MibTableColumn
hcsNewCfgAddLongNsendCmd = _HcsNewCfgAddLongNsendCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 19),
    _HcsNewCfgAddLongNsendCmd_Type()
)
hcsNewCfgAddLongNsendCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddLongNsendCmd.setStatus("current")


class _HcsNewCfgAddLongNexpectCmd_Type(OctetString):
    """Custom type hcsNewCfgAddLongNexpectCmd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 504),
    )


_HcsNewCfgAddLongNexpectCmd_Type.__name__ = "OctetString"
_HcsNewCfgAddLongNexpectCmd_Object = MibTableColumn
hcsNewCfgAddLongNexpectCmd = _HcsNewCfgAddLongNexpectCmd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 13, 3, 1, 20),
    _HcsNewCfgAddLongNexpectCmd_Type()
)
hcsNewCfgAddLongNexpectCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcsNewCfgAddLongNexpectCmd.setStatus("current")
_SnmphcCfg_ObjectIdentity = ObjectIdentity
snmphcCfg = _SnmphcCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14)
)
_SnmphcTableMaxSize_Type = Integer32
_SnmphcTableMaxSize_Object = MibScalar
snmphcTableMaxSize = _SnmphcTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 1),
    _SnmphcTableMaxSize_Type()
)
snmphcTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmphcTableMaxSize.setStatus("current")
_SnmphcCurCfgTable_Object = MibTable
snmphcCurCfgTable = _SnmphcCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 2)
)
if mibBuilder.loadTexts:
    snmphcCurCfgTable.setStatus("current")
_SnmphcCurCfgTableEntry_Object = MibTableRow
snmphcCurCfgTableEntry = _SnmphcCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 2, 1)
)
snmphcCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "snmphcCurCfgIndex"),
)
if mibBuilder.loadTexts:
    snmphcCurCfgTableEntry.setStatus("current")
_SnmphcCurCfgIndex_Type = Integer32
_SnmphcCurCfgIndex_Object = MibTableColumn
snmphcCurCfgIndex = _SnmphcCurCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 2, 1, 1),
    _SnmphcCurCfgIndex_Type()
)
snmphcCurCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmphcCurCfgIndex.setStatus("current")


class _SnmphcCurCfgOid_Type(DisplayString):
    """Custom type snmphcCurCfgOid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnmphcCurCfgOid_Type.__name__ = "DisplayString"
_SnmphcCurCfgOid_Object = MibTableColumn
snmphcCurCfgOid = _SnmphcCurCfgOid_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 2, 1, 2),
    _SnmphcCurCfgOid_Type()
)
snmphcCurCfgOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmphcCurCfgOid.setStatus("current")


class _SnmphcCurCfgCommString_Type(DisplayString):
    """Custom type snmphcCurCfgCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmphcCurCfgCommString_Type.__name__ = "DisplayString"
_SnmphcCurCfgCommString_Object = MibTableColumn
snmphcCurCfgCommString = _SnmphcCurCfgCommString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 2, 1, 3),
    _SnmphcCurCfgCommString_Type()
)
snmphcCurCfgCommString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmphcCurCfgCommString.setStatus("current")


class _SnmphcCurCfgRcvContent_Type(DisplayString):
    """Custom type snmphcCurCfgRcvContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmphcCurCfgRcvContent_Type.__name__ = "DisplayString"
_SnmphcCurCfgRcvContent_Object = MibTableColumn
snmphcCurCfgRcvContent = _SnmphcCurCfgRcvContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 2, 1, 4),
    _SnmphcCurCfgRcvContent_Type()
)
snmphcCurCfgRcvContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmphcCurCfgRcvContent.setStatus("current")


class _SnmphcCurCfgInvert_Type(Integer32):
    """Custom type snmphcCurCfgInvert based on Integer32"""
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


_SnmphcCurCfgInvert_Type.__name__ = "Integer32"
_SnmphcCurCfgInvert_Object = MibTableColumn
snmphcCurCfgInvert = _SnmphcCurCfgInvert_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 2, 1, 5),
    _SnmphcCurCfgInvert_Type()
)
snmphcCurCfgInvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmphcCurCfgInvert.setStatus("current")


class _SnmphcCurCfgUseWeight_Type(Integer32):
    """Custom type snmphcCurCfgUseWeight based on Integer32"""
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


_SnmphcCurCfgUseWeight_Type.__name__ = "Integer32"
_SnmphcCurCfgUseWeight_Object = MibTableColumn
snmphcCurCfgUseWeight = _SnmphcCurCfgUseWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 2, 1, 6),
    _SnmphcCurCfgUseWeight_Type()
)
snmphcCurCfgUseWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmphcCurCfgUseWeight.setStatus("current")
_SnmphcNewCfgTable_Object = MibTable
snmphcNewCfgTable = _SnmphcNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 3)
)
if mibBuilder.loadTexts:
    snmphcNewCfgTable.setStatus("current")
_SnmphcNewCfgTableEntry_Object = MibTableRow
snmphcNewCfgTableEntry = _SnmphcNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 3, 1)
)
snmphcNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "snmphcNewCfgIndex"),
)
if mibBuilder.loadTexts:
    snmphcNewCfgTableEntry.setStatus("current")
_SnmphcNewCfgIndex_Type = Integer32
_SnmphcNewCfgIndex_Object = MibTableColumn
snmphcNewCfgIndex = _SnmphcNewCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 3, 1, 1),
    _SnmphcNewCfgIndex_Type()
)
snmphcNewCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmphcNewCfgIndex.setStatus("current")


class _SnmphcNewCfgOid_Type(DisplayString):
    """Custom type snmphcNewCfgOid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnmphcNewCfgOid_Type.__name__ = "DisplayString"
_SnmphcNewCfgOid_Object = MibTableColumn
snmphcNewCfgOid = _SnmphcNewCfgOid_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 3, 1, 2),
    _SnmphcNewCfgOid_Type()
)
snmphcNewCfgOid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmphcNewCfgOid.setStatus("current")


class _SnmphcNewCfgCommString_Type(DisplayString):
    """Custom type snmphcNewCfgCommString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmphcNewCfgCommString_Type.__name__ = "DisplayString"
_SnmphcNewCfgCommString_Object = MibTableColumn
snmphcNewCfgCommString = _SnmphcNewCfgCommString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 3, 1, 3),
    _SnmphcNewCfgCommString_Type()
)
snmphcNewCfgCommString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmphcNewCfgCommString.setStatus("current")


class _SnmphcNewCfgRcvContent_Type(DisplayString):
    """Custom type snmphcNewCfgRcvContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmphcNewCfgRcvContent_Type.__name__ = "DisplayString"
_SnmphcNewCfgRcvContent_Object = MibTableColumn
snmphcNewCfgRcvContent = _SnmphcNewCfgRcvContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 3, 1, 4),
    _SnmphcNewCfgRcvContent_Type()
)
snmphcNewCfgRcvContent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmphcNewCfgRcvContent.setStatus("current")


class _SnmphcNewCfgInvert_Type(Integer32):
    """Custom type snmphcNewCfgInvert based on Integer32"""
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


_SnmphcNewCfgInvert_Type.__name__ = "Integer32"
_SnmphcNewCfgInvert_Object = MibTableColumn
snmphcNewCfgInvert = _SnmphcNewCfgInvert_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 3, 1, 5),
    _SnmphcNewCfgInvert_Type()
)
snmphcNewCfgInvert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmphcNewCfgInvert.setStatus("current")


class _SnmphcNewCfgDeleteHc_Type(Integer32):
    """Custom type snmphcNewCfgDeleteHc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SnmphcNewCfgDeleteHc_Type.__name__ = "Integer32"
_SnmphcNewCfgDeleteHc_Object = MibTableColumn
snmphcNewCfgDeleteHc = _SnmphcNewCfgDeleteHc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 3, 1, 6),
    _SnmphcNewCfgDeleteHc_Type()
)
snmphcNewCfgDeleteHc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmphcNewCfgDeleteHc.setStatus("current")


class _SnmphcNewCfgUseWeight_Type(Integer32):
    """Custom type snmphcNewCfgUseWeight based on Integer32"""
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


_SnmphcNewCfgUseWeight_Type.__name__ = "Integer32"
_SnmphcNewCfgUseWeight_Object = MibTableColumn
snmphcNewCfgUseWeight = _SnmphcNewCfgUseWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 14, 3, 1, 7),
    _SnmphcNewCfgUseWeight_Type()
)
snmphcNewCfgUseWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmphcNewCfgUseWeight.setStatus("current")
_PipTblCfg_ObjectIdentity = ObjectIdentity
pipTblCfg = _PipTblCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15)
)
_PipTableMaxSize_Type = Integer32
_PipTableMaxSize_Object = MibScalar
pipTableMaxSize = _PipTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 1),
    _PipTableMaxSize_Type()
)
pipTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipTableMaxSize.setStatus("current")


class _PipCurCfgBaseType_Type(Integer32):
    """Custom type pipCurCfgBaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("vlan", 2))
    )


_PipCurCfgBaseType_Type.__name__ = "Integer32"
_PipCurCfgBaseType_Object = MibScalar
pipCurCfgBaseType = _PipCurCfgBaseType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 2),
    _PipCurCfgBaseType_Type()
)
pipCurCfgBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipCurCfgBaseType.setStatus("current")
_PipCurCfgTable_Object = MibTable
pipCurCfgTable = _PipCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 3)
)
if mibBuilder.loadTexts:
    pipCurCfgTable.setStatus("current")
_PipCurCfgTableEntry_Object = MibTableRow
pipCurCfgTableEntry = _PipCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 3, 1)
)
pipCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "pipCurCfgPip"),
)
if mibBuilder.loadTexts:
    pipCurCfgTableEntry.setStatus("current")
_PipCurCfgPip_Type = IpAddress
_PipCurCfgPip_Object = MibTableColumn
pipCurCfgPip = _PipCurCfgPip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 3, 1, 1),
    _PipCurCfgPip_Type()
)
pipCurCfgPip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipCurCfgPip.setStatus("current")


class _PipCurCfgPortMap_Type(OctetString):
    """Custom type pipCurCfgPortMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PipCurCfgPortMap_Type.__name__ = "OctetString"
_PipCurCfgPortMap_Object = MibTableColumn
pipCurCfgPortMap = _PipCurCfgPortMap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 3, 1, 2),
    _PipCurCfgPortMap_Type()
)
pipCurCfgPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipCurCfgPortMap.setStatus("current")


class _PipCurCfgVlanMap_Type(OctetString):
    """Custom type pipCurCfgVlanMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PipCurCfgVlanMap_Type.__name__ = "OctetString"
_PipCurCfgVlanMap_Object = MibTableColumn
pipCurCfgVlanMap = _PipCurCfgVlanMap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 3, 1, 3),
    _PipCurCfgVlanMap_Type()
)
pipCurCfgVlanMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipCurCfgVlanMap.setStatus("current")


class _PipNewCfgBaseType_Type(Integer32):
    """Custom type pipNewCfgBaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("vlan", 2))
    )


_PipNewCfgBaseType_Type.__name__ = "Integer32"
_PipNewCfgBaseType_Object = MibScalar
pipNewCfgBaseType = _PipNewCfgBaseType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 4),
    _PipNewCfgBaseType_Type()
)
pipNewCfgBaseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pipNewCfgBaseType.setStatus("current")
_PipNewCfgTable_Object = MibTable
pipNewCfgTable = _PipNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 5)
)
if mibBuilder.loadTexts:
    pipNewCfgTable.setStatus("current")
_PipNewCfgTableEntry_Object = MibTableRow
pipNewCfgTableEntry = _PipNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 5, 1)
)
pipNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "pipNewCfgPip"),
)
if mibBuilder.loadTexts:
    pipNewCfgTableEntry.setStatus("current")
_PipNewCfgPip_Type = IpAddress
_PipNewCfgPip_Object = MibTableColumn
pipNewCfgPip = _PipNewCfgPip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 5, 1, 1),
    _PipNewCfgPip_Type()
)
pipNewCfgPip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipNewCfgPip.setStatus("current")


class _PipNewCfgPortMap_Type(OctetString):
    """Custom type pipNewCfgPortMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PipNewCfgPortMap_Type.__name__ = "OctetString"
_PipNewCfgPortMap_Object = MibTableColumn
pipNewCfgPortMap = _PipNewCfgPortMap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 5, 1, 2),
    _PipNewCfgPortMap_Type()
)
pipNewCfgPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipNewCfgPortMap.setStatus("current")


class _PipNewCfgVlanMap_Type(OctetString):
    """Custom type pipNewCfgVlanMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PipNewCfgVlanMap_Type.__name__ = "OctetString"
_PipNewCfgVlanMap_Object = MibTableColumn
pipNewCfgVlanMap = _PipNewCfgVlanMap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 5, 1, 3),
    _PipNewCfgVlanMap_Type()
)
pipNewCfgVlanMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipNewCfgVlanMap.setStatus("current")


class _PipNewCfgDelete_Type(Integer32):
    """Custom type pipNewCfgDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_PipNewCfgDelete_Type.__name__ = "Integer32"
_PipNewCfgDelete_Object = MibTableColumn
pipNewCfgDelete = _PipNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 5, 1, 4),
    _PipNewCfgDelete_Type()
)
pipNewCfgDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pipNewCfgDelete.setStatus("current")
_PipNewCfgAddPortVlan_Type = Integer32
_PipNewCfgAddPortVlan_Object = MibTableColumn
pipNewCfgAddPortVlan = _PipNewCfgAddPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 5, 1, 5),
    _PipNewCfgAddPortVlan_Type()
)
pipNewCfgAddPortVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pipNewCfgAddPortVlan.setStatus("current")
_PipNewCfgRemovePortVlan_Type = Integer32
_PipNewCfgRemovePortVlan_Object = MibTableColumn
pipNewCfgRemovePortVlan = _PipNewCfgRemovePortVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 15, 5, 1, 6),
    _PipNewCfgRemovePortVlan_Type()
)
pipNewCfgRemovePortVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pipNewCfgRemovePortVlan.setStatus("current")
_LinklbCfg_ObjectIdentity = ObjectIdentity
linklbCfg = _LinklbCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16)
)


class _SlbCurCfgLinklbState_Type(Integer32):
    """Custom type slbCurCfgLinklbState based on Integer32"""
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


_SlbCurCfgLinklbState_Type.__name__ = "Integer32"
_SlbCurCfgLinklbState_Object = MibScalar
slbCurCfgLinklbState = _SlbCurCfgLinklbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 1),
    _SlbCurCfgLinklbState_Type()
)
slbCurCfgLinklbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgLinklbState.setStatus("current")


class _SlbNewCfgLinklbState_Type(Integer32):
    """Custom type slbNewCfgLinklbState based on Integer32"""
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


_SlbNewCfgLinklbState_Type.__name__ = "Integer32"
_SlbNewCfgLinklbState_Object = MibScalar
slbNewCfgLinklbState = _SlbNewCfgLinklbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 2),
    _SlbNewCfgLinklbState_Type()
)
slbNewCfgLinklbState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgLinklbState.setStatus("current")
_SlbCurCfgLinklbRealGroup_Type = Integer32
_SlbCurCfgLinklbRealGroup_Object = MibScalar
slbCurCfgLinklbRealGroup = _SlbCurCfgLinklbRealGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 3),
    _SlbCurCfgLinklbRealGroup_Type()
)
slbCurCfgLinklbRealGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgLinklbRealGroup.setStatus("current")
_SlbNewCfgLinklbRealGroup_Type = Integer32
_SlbNewCfgLinklbRealGroup_Object = MibScalar
slbNewCfgLinklbRealGroup = _SlbNewCfgLinklbRealGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 4),
    _SlbNewCfgLinklbRealGroup_Type()
)
slbNewCfgLinklbRealGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgLinklbRealGroup.setStatus("current")
_SlbLinklbDrecord_ObjectIdentity = ObjectIdentity
slbLinklbDrecord = _SlbLinklbDrecord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5)
)
_SlbDrecordTableMaxSize_Type = Integer32
_SlbDrecordTableMaxSize_Object = MibScalar
slbDrecordTableMaxSize = _SlbDrecordTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 1),
    _SlbDrecordTableMaxSize_Type()
)
slbDrecordTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbDrecordTableMaxSize.setStatus("current")
_SlbCurCfgDrecordTable_Object = MibTable
slbCurCfgDrecordTable = _SlbCurCfgDrecordTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 2)
)
if mibBuilder.loadTexts:
    slbCurCfgDrecordTable.setStatus("current")
_SlbCurCfgDrecordEntry_Object = MibTableRow
slbCurCfgDrecordEntry = _SlbCurCfgDrecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 2, 1)
)
slbCurCfgDrecordEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgDrecordIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgDrecordEntry.setStatus("current")


class _SlbCurCfgDrecordIndex_Type(Integer32):
    """Custom type slbCurCfgDrecordIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SlbCurCfgDrecordIndex_Type.__name__ = "Integer32"
_SlbCurCfgDrecordIndex_Object = MibTableColumn
slbCurCfgDrecordIndex = _SlbCurCfgDrecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 2, 1, 1),
    _SlbCurCfgDrecordIndex_Type()
)
slbCurCfgDrecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgDrecordIndex.setStatus("current")


class _SlbCurCfgDomainRecordState_Type(Integer32):
    """Custom type slbCurCfgDomainRecordState based on Integer32"""
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


_SlbCurCfgDomainRecordState_Type.__name__ = "Integer32"
_SlbCurCfgDomainRecordState_Object = MibTableColumn
slbCurCfgDomainRecordState = _SlbCurCfgDomainRecordState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 2, 1, 2),
    _SlbCurCfgDomainRecordState_Type()
)
slbCurCfgDomainRecordState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgDomainRecordState.setStatus("current")


class _SlbCurCfgDomainRecordName_Type(DisplayString):
    """Custom type slbCurCfgDomainRecordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_SlbCurCfgDomainRecordName_Type.__name__ = "DisplayString"
_SlbCurCfgDomainRecordName_Object = MibTableColumn
slbCurCfgDomainRecordName = _SlbCurCfgDomainRecordName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 2, 1, 3),
    _SlbCurCfgDomainRecordName_Type()
)
slbCurCfgDomainRecordName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgDomainRecordName.setStatus("current")
_SlbNewCfgDrecordTable_Object = MibTable
slbNewCfgDrecordTable = _SlbNewCfgDrecordTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 3)
)
if mibBuilder.loadTexts:
    slbNewCfgDrecordTable.setStatus("current")
_SlbNewCfgDrecordEntry_Object = MibTableRow
slbNewCfgDrecordEntry = _SlbNewCfgDrecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 3, 1)
)
slbNewCfgDrecordEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgDrecordIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgDrecordEntry.setStatus("current")


class _SlbNewCfgDrecordIndex_Type(Integer32):
    """Custom type slbNewCfgDrecordIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SlbNewCfgDrecordIndex_Type.__name__ = "Integer32"
_SlbNewCfgDrecordIndex_Object = MibTableColumn
slbNewCfgDrecordIndex = _SlbNewCfgDrecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 3, 1, 1),
    _SlbNewCfgDrecordIndex_Type()
)
slbNewCfgDrecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgDrecordIndex.setStatus("current")


class _SlbNewCfgDomainRecordState_Type(Integer32):
    """Custom type slbNewCfgDomainRecordState based on Integer32"""
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


_SlbNewCfgDomainRecordState_Type.__name__ = "Integer32"
_SlbNewCfgDomainRecordState_Object = MibTableColumn
slbNewCfgDomainRecordState = _SlbNewCfgDomainRecordState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 3, 1, 2),
    _SlbNewCfgDomainRecordState_Type()
)
slbNewCfgDomainRecordState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgDomainRecordState.setStatus("current")


class _SlbNewCfgDomainRecordName_Type(DisplayString):
    """Custom type slbNewCfgDomainRecordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_SlbNewCfgDomainRecordName_Type.__name__ = "DisplayString"
_SlbNewCfgDomainRecordName_Object = MibTableColumn
slbNewCfgDomainRecordName = _SlbNewCfgDomainRecordName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 3, 1, 3),
    _SlbNewCfgDomainRecordName_Type()
)
slbNewCfgDomainRecordName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgDomainRecordName.setStatus("current")


class _SlbNewCfgDrecordDelete_Type(Integer32):
    """Custom type slbNewCfgDrecordDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgDrecordDelete_Type.__name__ = "Integer32"
_SlbNewCfgDrecordDelete_Object = MibTableColumn
slbNewCfgDrecordDelete = _SlbNewCfgDrecordDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 3, 1, 4),
    _SlbNewCfgDrecordDelete_Type()
)
slbNewCfgDrecordDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgDrecordDelete.setStatus("current")
_SlbDrecordVirtRealMappingTableMaxSize_Type = Integer32
_SlbDrecordVirtRealMappingTableMaxSize_Object = MibScalar
slbDrecordVirtRealMappingTableMaxSize = _SlbDrecordVirtRealMappingTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 4),
    _SlbDrecordVirtRealMappingTableMaxSize_Type()
)
slbDrecordVirtRealMappingTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbDrecordVirtRealMappingTableMaxSize.setStatus("current")
_SlbCurCfgDrecordVirtRealMappingTable_Object = MibTable
slbCurCfgDrecordVirtRealMappingTable = _SlbCurCfgDrecordVirtRealMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 5)
)
if mibBuilder.loadTexts:
    slbCurCfgDrecordVirtRealMappingTable.setStatus("current")
_SlbCurCfgDrecordVirtRealMappingEntry_Object = MibTableRow
slbCurCfgDrecordVirtRealMappingEntry = _SlbCurCfgDrecordVirtRealMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 5, 1)
)
slbCurCfgDrecordVirtRealMappingEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgDomainRecordIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgEntryIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgDrecordVirtRealMappingEntry.setStatus("current")


class _SlbCurCfgDomainRecordIndex_Type(Integer32):
    """Custom type slbCurCfgDomainRecordIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SlbCurCfgDomainRecordIndex_Type.__name__ = "Integer32"
_SlbCurCfgDomainRecordIndex_Object = MibTableColumn
slbCurCfgDomainRecordIndex = _SlbCurCfgDomainRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 5, 1, 1),
    _SlbCurCfgDomainRecordIndex_Type()
)
slbCurCfgDomainRecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgDomainRecordIndex.setStatus("current")


class _SlbCurCfgEntryIndex_Type(Integer32):
    """Custom type slbCurCfgEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SlbCurCfgEntryIndex_Type.__name__ = "Integer32"
_SlbCurCfgEntryIndex_Object = MibTableColumn
slbCurCfgEntryIndex = _SlbCurCfgEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 5, 1, 2),
    _SlbCurCfgEntryIndex_Type()
)
slbCurCfgEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgEntryIndex.setStatus("current")
_SlbCurCfgDrecordVirtServer_Type = Integer32
_SlbCurCfgDrecordVirtServer_Object = MibTableColumn
slbCurCfgDrecordVirtServer = _SlbCurCfgDrecordVirtServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 5, 1, 3),
    _SlbCurCfgDrecordVirtServer_Type()
)
slbCurCfgDrecordVirtServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgDrecordVirtServer.setStatus("current")
_SlbCurCfgDrecordRealServer_Type = Integer32
_SlbCurCfgDrecordRealServer_Object = MibTableColumn
slbCurCfgDrecordRealServer = _SlbCurCfgDrecordRealServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 5, 1, 4),
    _SlbCurCfgDrecordRealServer_Type()
)
slbCurCfgDrecordRealServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgDrecordRealServer.setStatus("current")


class _SlbCurCfgDrecordEntryState_Type(Integer32):
    """Custom type slbCurCfgDrecordEntryState based on Integer32"""
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


_SlbCurCfgDrecordEntryState_Type.__name__ = "Integer32"
_SlbCurCfgDrecordEntryState_Object = MibTableColumn
slbCurCfgDrecordEntryState = _SlbCurCfgDrecordEntryState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 5, 1, 5),
    _SlbCurCfgDrecordEntryState_Type()
)
slbCurCfgDrecordEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgDrecordEntryState.setStatus("current")
_SlbNewCfgDrecordVirtRealMappingTable_Object = MibTable
slbNewCfgDrecordVirtRealMappingTable = _SlbNewCfgDrecordVirtRealMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 6)
)
if mibBuilder.loadTexts:
    slbNewCfgDrecordVirtRealMappingTable.setStatus("current")
_SlbNewCfgDrecordVirtRealMappingEntry_Object = MibTableRow
slbNewCfgDrecordVirtRealMappingEntry = _SlbNewCfgDrecordVirtRealMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 6, 1)
)
slbNewCfgDrecordVirtRealMappingEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgDomainRecordIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgEntryIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgDrecordVirtRealMappingEntry.setStatus("current")


class _SlbNewCfgDomainRecordIndex_Type(Integer32):
    """Custom type slbNewCfgDomainRecordIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SlbNewCfgDomainRecordIndex_Type.__name__ = "Integer32"
_SlbNewCfgDomainRecordIndex_Object = MibTableColumn
slbNewCfgDomainRecordIndex = _SlbNewCfgDomainRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 6, 1, 1),
    _SlbNewCfgDomainRecordIndex_Type()
)
slbNewCfgDomainRecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgDomainRecordIndex.setStatus("current")


class _SlbNewCfgEntryIndex_Type(Integer32):
    """Custom type slbNewCfgEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SlbNewCfgEntryIndex_Type.__name__ = "Integer32"
_SlbNewCfgEntryIndex_Object = MibTableColumn
slbNewCfgEntryIndex = _SlbNewCfgEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 6, 1, 2),
    _SlbNewCfgEntryIndex_Type()
)
slbNewCfgEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgEntryIndex.setStatus("current")
_SlbNewCfgDrecordVirtServer_Type = Integer32
_SlbNewCfgDrecordVirtServer_Object = MibTableColumn
slbNewCfgDrecordVirtServer = _SlbNewCfgDrecordVirtServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 6, 1, 3),
    _SlbNewCfgDrecordVirtServer_Type()
)
slbNewCfgDrecordVirtServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgDrecordVirtServer.setStatus("current")
_SlbNewCfgDrecordRealServer_Type = Integer32
_SlbNewCfgDrecordRealServer_Object = MibTableColumn
slbNewCfgDrecordRealServer = _SlbNewCfgDrecordRealServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 6, 1, 4),
    _SlbNewCfgDrecordRealServer_Type()
)
slbNewCfgDrecordRealServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgDrecordRealServer.setStatus("current")


class _SlbNewCfgDrecordEntryState_Type(Integer32):
    """Custom type slbNewCfgDrecordEntryState based on Integer32"""
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


_SlbNewCfgDrecordEntryState_Type.__name__ = "Integer32"
_SlbNewCfgDrecordEntryState_Object = MibTableColumn
slbNewCfgDrecordEntryState = _SlbNewCfgDrecordEntryState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 6, 1, 5),
    _SlbNewCfgDrecordEntryState_Type()
)
slbNewCfgDrecordEntryState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgDrecordEntryState.setStatus("current")


class _SlbNewCfgDrecordEntryDelete_Type(Integer32):
    """Custom type slbNewCfgDrecordEntryDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgDrecordEntryDelete_Type.__name__ = "Integer32"
_SlbNewCfgDrecordEntryDelete_Object = MibTableColumn
slbNewCfgDrecordEntryDelete = _SlbNewCfgDrecordEntryDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 5, 6, 1, 6),
    _SlbNewCfgDrecordEntryDelete_Type()
)
slbNewCfgDrecordEntryDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgDrecordEntryDelete.setStatus("current")


class _SlbCurCfgLinklbTTL_Type(Integer32):
    """Custom type slbCurCfgLinklbTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlbCurCfgLinklbTTL_Type.__name__ = "Integer32"
_SlbCurCfgLinklbTTL_Object = MibScalar
slbCurCfgLinklbTTL = _SlbCurCfgLinklbTTL_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 6),
    _SlbCurCfgLinklbTTL_Type()
)
slbCurCfgLinklbTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgLinklbTTL.setStatus("current")


class _SlbNewCfgLinklbTTL_Type(Integer32):
    """Custom type slbNewCfgLinklbTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlbNewCfgLinklbTTL_Type.__name__ = "Integer32"
_SlbNewCfgLinklbTTL_Object = MibScalar
slbNewCfgLinklbTTL = _SlbNewCfgLinklbTTL_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 16, 7),
    _SlbNewCfgLinklbTTL_Type()
)
slbNewCfgLinklbTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgLinklbTTL.setStatus("current")
_SmtportCfg_ObjectIdentity = ObjectIdentity
smtportCfg = _SmtportCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 17)
)
_SlbSmtportTableMaxSize_Type = Integer32
_SlbSmtportTableMaxSize_Object = MibScalar
slbSmtportTableMaxSize = _SlbSmtportTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 17, 1),
    _SlbSmtportTableMaxSize_Type()
)
slbSmtportTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSmtportTableMaxSize.setStatus("current")
_SlbCurCfgSmtportTable_Object = MibTable
slbCurCfgSmtportTable = _SlbCurCfgSmtportTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 17, 2)
)
if mibBuilder.loadTexts:
    slbCurCfgSmtportTable.setStatus("current")
_SlbCurCfgSmtportEntry_Object = MibTableRow
slbCurCfgSmtportEntry = _SlbCurCfgSmtportEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 17, 2, 1)
)
slbCurCfgSmtportEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgSmtportIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgSmtportEntry.setStatus("current")
_SlbCurCfgSmtportIndex_Type = Integer32
_SlbCurCfgSmtportIndex_Object = MibTableColumn
slbCurCfgSmtportIndex = _SlbCurCfgSmtportIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 17, 2, 1, 1),
    _SlbCurCfgSmtportIndex_Type()
)
slbCurCfgSmtportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSmtportIndex.setStatus("current")


class _SlbCurCfgSmtportNum_Type(Integer32):
    """Custom type slbCurCfgSmtportNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65534),
    )


_SlbCurCfgSmtportNum_Type.__name__ = "Integer32"
_SlbCurCfgSmtportNum_Object = MibTableColumn
slbCurCfgSmtportNum = _SlbCurCfgSmtportNum_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 17, 2, 1, 2),
    _SlbCurCfgSmtportNum_Type()
)
slbCurCfgSmtportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSmtportNum.setStatus("current")
_SlbNewCfgSmtportTable_Object = MibTable
slbNewCfgSmtportTable = _SlbNewCfgSmtportTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 17, 3)
)
if mibBuilder.loadTexts:
    slbNewCfgSmtportTable.setStatus("current")
_SlbNewCfgSmtportEntry_Object = MibTableRow
slbNewCfgSmtportEntry = _SlbNewCfgSmtportEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 17, 3, 1)
)
slbNewCfgSmtportEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgSmtportIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgSmtportEntry.setStatus("current")
_SlbNewCfgSmtportIndex_Type = Integer32
_SlbNewCfgSmtportIndex_Object = MibTableColumn
slbNewCfgSmtportIndex = _SlbNewCfgSmtportIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 17, 3, 1, 1),
    _SlbNewCfgSmtportIndex_Type()
)
slbNewCfgSmtportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgSmtportIndex.setStatus("current")


class _SlbNewCfgSmtportNum_Type(Integer32):
    """Custom type slbNewCfgSmtportNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65534),
    )


_SlbNewCfgSmtportNum_Type.__name__ = "Integer32"
_SlbNewCfgSmtportNum_Object = MibTableColumn
slbNewCfgSmtportNum = _SlbNewCfgSmtportNum_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 17, 3, 1, 2),
    _SlbNewCfgSmtportNum_Type()
)
slbNewCfgSmtportNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSmtportNum.setStatus("current")


class _SlbNewCfgSmtportDelete_Type(Integer32):
    """Custom type slbNewCfgSmtportDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgSmtportDelete_Type.__name__ = "Integer32"
_SlbNewCfgSmtportDelete_Object = MibTableColumn
slbNewCfgSmtportDelete = _SlbNewCfgSmtportDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 1, 17, 3, 1, 3),
    _SlbNewCfgSmtportDelete_Type()
)
slbNewCfgSmtportDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSmtportDelete.setStatus("current")
_FilterCfg_ObjectIdentity = ObjectIdentity
filterCfg = _FilterCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2)
)
_FltCfgTableMaxSize_Type = Integer32
_FltCfgTableMaxSize_Object = MibScalar
fltCfgTableMaxSize = _FltCfgTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 1),
    _FltCfgTableMaxSize_Type()
)
fltCfgTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCfgTableMaxSize.setStatus("current")
_FltCurCfgTable_Object = MibTable
fltCurCfgTable = _FltCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fltCurCfgTable.setStatus("current")
_FltCurCfgTableEntry_Object = MibTableRow
fltCurCfgTableEntry = _FltCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1)
)
fltCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "fltCurCfgIndx"),
)
if mibBuilder.loadTexts:
    fltCurCfgTableEntry.setStatus("current")
_FltCurCfgIndx_Type = Integer32
_FltCurCfgIndx_Object = MibTableColumn
fltCurCfgIndx = _FltCurCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 1),
    _FltCurCfgIndx_Type()
)
fltCurCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgIndx.setStatus("current")
_FltCurCfgSrcIp_Type = IpAddress
_FltCurCfgSrcIp_Object = MibTableColumn
fltCurCfgSrcIp = _FltCurCfgSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 2),
    _FltCurCfgSrcIp_Type()
)
fltCurCfgSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgSrcIp.setStatus("current")
_FltCurCfgSrcIpMask_Type = IpAddress
_FltCurCfgSrcIpMask_Object = MibTableColumn
fltCurCfgSrcIpMask = _FltCurCfgSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 3),
    _FltCurCfgSrcIpMask_Type()
)
fltCurCfgSrcIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgSrcIpMask.setStatus("current")
_FltCurCfgDstIp_Type = IpAddress
_FltCurCfgDstIp_Object = MibTableColumn
fltCurCfgDstIp = _FltCurCfgDstIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 4),
    _FltCurCfgDstIp_Type()
)
fltCurCfgDstIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgDstIp.setStatus("current")
_FltCurCfgDstIpMask_Type = IpAddress
_FltCurCfgDstIpMask_Object = MibTableColumn
fltCurCfgDstIpMask = _FltCurCfgDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 5),
    _FltCurCfgDstIpMask_Type()
)
fltCurCfgDstIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgDstIpMask.setStatus("current")


class _FltCurCfgProtocol_Type(Integer32):
    """Custom type fltCurCfgProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltCurCfgProtocol_Type.__name__ = "Integer32"
_FltCurCfgProtocol_Object = MibTableColumn
fltCurCfgProtocol = _FltCurCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 6),
    _FltCurCfgProtocol_Type()
)
fltCurCfgProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgProtocol.setStatus("current")


class _FltCurCfgRangeHighSrcPort_Type(Integer32):
    """Custom type fltCurCfgRangeHighSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltCurCfgRangeHighSrcPort_Type.__name__ = "Integer32"
_FltCurCfgRangeHighSrcPort_Object = MibTableColumn
fltCurCfgRangeHighSrcPort = _FltCurCfgRangeHighSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 7),
    _FltCurCfgRangeHighSrcPort_Type()
)
fltCurCfgRangeHighSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRangeHighSrcPort.setStatus("current")


class _FltCurCfgRangeLowSrcPort_Type(Integer32):
    """Custom type fltCurCfgRangeLowSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltCurCfgRangeLowSrcPort_Type.__name__ = "Integer32"
_FltCurCfgRangeLowSrcPort_Object = MibTableColumn
fltCurCfgRangeLowSrcPort = _FltCurCfgRangeLowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 8),
    _FltCurCfgRangeLowSrcPort_Type()
)
fltCurCfgRangeLowSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRangeLowSrcPort.setStatus("current")


class _FltCurCfgRangeLowDstPort_Type(Integer32):
    """Custom type fltCurCfgRangeLowDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltCurCfgRangeLowDstPort_Type.__name__ = "Integer32"
_FltCurCfgRangeLowDstPort_Object = MibTableColumn
fltCurCfgRangeLowDstPort = _FltCurCfgRangeLowDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 9),
    _FltCurCfgRangeLowDstPort_Type()
)
fltCurCfgRangeLowDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRangeLowDstPort.setStatus("current")


class _FltCurCfgRangeHighDstPort_Type(Integer32):
    """Custom type fltCurCfgRangeHighDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltCurCfgRangeHighDstPort_Type.__name__ = "Integer32"
_FltCurCfgRangeHighDstPort_Object = MibTableColumn
fltCurCfgRangeHighDstPort = _FltCurCfgRangeHighDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 10),
    _FltCurCfgRangeHighDstPort_Type()
)
fltCurCfgRangeHighDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRangeHighDstPort.setStatus("current")


class _FltCurCfgAction_Type(Integer32):
    """Custom type fltCurCfgAction based on Integer32"""
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
        *(("allow", 1),
          ("deny", 2),
          ("redirect", 3),
          ("nat", 4),
          ("goto", 5))
    )


_FltCurCfgAction_Type.__name__ = "Integer32"
_FltCurCfgAction_Object = MibTableColumn
fltCurCfgAction = _FltCurCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 11),
    _FltCurCfgAction_Type()
)
fltCurCfgAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAction.setStatus("current")


class _FltCurCfgRedirPort_Type(Integer32):
    """Custom type fltCurCfgRedirPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltCurCfgRedirPort_Type.__name__ = "Integer32"
_FltCurCfgRedirPort_Object = MibTableColumn
fltCurCfgRedirPort = _FltCurCfgRedirPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 12),
    _FltCurCfgRedirPort_Type()
)
fltCurCfgRedirPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRedirPort.setStatus("current")
_FltCurCfgRedirGroup_Type = Integer32
_FltCurCfgRedirGroup_Object = MibTableColumn
fltCurCfgRedirGroup = _FltCurCfgRedirGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 13),
    _FltCurCfgRedirGroup_Type()
)
fltCurCfgRedirGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRedirGroup.setStatus("current")


class _FltCurCfgLog_Type(Integer32):
    """Custom type fltCurCfgLog based on Integer32"""
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


_FltCurCfgLog_Type.__name__ = "Integer32"
_FltCurCfgLog_Object = MibTableColumn
fltCurCfgLog = _FltCurCfgLog_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 14),
    _FltCurCfgLog_Type()
)
fltCurCfgLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgLog.setStatus("current")


class _FltCurCfgState_Type(Integer32):
    """Custom type fltCurCfgState based on Integer32"""
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


_FltCurCfgState_Type.__name__ = "Integer32"
_FltCurCfgState_Object = MibTableColumn
fltCurCfgState = _FltCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 15),
    _FltCurCfgState_Type()
)
fltCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgState.setStatus("current")


class _FltCurCfgNat_Type(Integer32):
    """Custom type fltCurCfgNat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination-address", 1),
          ("source-address", 2))
    )


_FltCurCfgNat_Type.__name__ = "Integer32"
_FltCurCfgNat_Object = MibTableColumn
fltCurCfgNat = _FltCurCfgNat_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 16),
    _FltCurCfgNat_Type()
)
fltCurCfgNat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgNat.setStatus("current")


class _FltCurCfgCache_Type(Integer32):
    """Custom type fltCurCfgCache based on Integer32"""
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


_FltCurCfgCache_Type.__name__ = "Integer32"
_FltCurCfgCache_Object = MibTableColumn
fltCurCfgCache = _FltCurCfgCache_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 17),
    _FltCurCfgCache_Type()
)
fltCurCfgCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgCache.setStatus("current")


class _FltCurCfgInvert_Type(Integer32):
    """Custom type fltCurCfgInvert based on Integer32"""
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


_FltCurCfgInvert_Type.__name__ = "Integer32"
_FltCurCfgInvert_Object = MibTableColumn
fltCurCfgInvert = _FltCurCfgInvert_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 18),
    _FltCurCfgInvert_Type()
)
fltCurCfgInvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgInvert.setStatus("current")


class _FltCurCfgClientProxy_Type(Integer32):
    """Custom type fltCurCfgClientProxy based on Integer32"""
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


_FltCurCfgClientProxy_Type.__name__ = "Integer32"
_FltCurCfgClientProxy_Object = MibTableColumn
fltCurCfgClientProxy = _FltCurCfgClientProxy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 19),
    _FltCurCfgClientProxy_Type()
)
fltCurCfgClientProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgClientProxy.setStatus("current")


class _FltCurCfgTcpAck_Type(Integer32):
    """Custom type fltCurCfgTcpAck based on Integer32"""
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


_FltCurCfgTcpAck_Type.__name__ = "Integer32"
_FltCurCfgTcpAck_Object = MibTableColumn
fltCurCfgTcpAck = _FltCurCfgTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 20),
    _FltCurCfgTcpAck_Type()
)
fltCurCfgTcpAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgTcpAck.setStatus("current")
_FltCurCfgSrcMac_Type = PhysAddress
_FltCurCfgSrcMac_Object = MibTableColumn
fltCurCfgSrcMac = _FltCurCfgSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 22),
    _FltCurCfgSrcMac_Type()
)
fltCurCfgSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgSrcMac.setStatus("current")
_FltCurCfgDstMac_Type = PhysAddress
_FltCurCfgDstMac_Object = MibTableColumn
fltCurCfgDstMac = _FltCurCfgDstMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 23),
    _FltCurCfgDstMac_Type()
)
fltCurCfgDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgDstMac.setStatus("current")


class _FltCurCfgFtpNatActive_Type(Integer32):
    """Custom type fltCurCfgFtpNatActive based on Integer32"""
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


_FltCurCfgFtpNatActive_Type.__name__ = "Integer32"
_FltCurCfgFtpNatActive_Object = MibTableColumn
fltCurCfgFtpNatActive = _FltCurCfgFtpNatActive_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 24),
    _FltCurCfgFtpNatActive_Type()
)
fltCurCfgFtpNatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgFtpNatActive.setStatus("current")


class _FltCurCfgAclTcpUrg_Type(Integer32):
    """Custom type fltCurCfgAclTcpUrg based on Integer32"""
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


_FltCurCfgAclTcpUrg_Type.__name__ = "Integer32"
_FltCurCfgAclTcpUrg_Object = MibTableColumn
fltCurCfgAclTcpUrg = _FltCurCfgAclTcpUrg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 25),
    _FltCurCfgAclTcpUrg_Type()
)
fltCurCfgAclTcpUrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpUrg.setStatus("current")


class _FltCurCfgAclTcpAck_Type(Integer32):
    """Custom type fltCurCfgAclTcpAck based on Integer32"""
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


_FltCurCfgAclTcpAck_Type.__name__ = "Integer32"
_FltCurCfgAclTcpAck_Object = MibTableColumn
fltCurCfgAclTcpAck = _FltCurCfgAclTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 26),
    _FltCurCfgAclTcpAck_Type()
)
fltCurCfgAclTcpAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpAck.setStatus("current")


class _FltCurCfgAclTcpPsh_Type(Integer32):
    """Custom type fltCurCfgAclTcpPsh based on Integer32"""
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


_FltCurCfgAclTcpPsh_Type.__name__ = "Integer32"
_FltCurCfgAclTcpPsh_Object = MibTableColumn
fltCurCfgAclTcpPsh = _FltCurCfgAclTcpPsh_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 27),
    _FltCurCfgAclTcpPsh_Type()
)
fltCurCfgAclTcpPsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpPsh.setStatus("current")


class _FltCurCfgAclTcpRst_Type(Integer32):
    """Custom type fltCurCfgAclTcpRst based on Integer32"""
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


_FltCurCfgAclTcpRst_Type.__name__ = "Integer32"
_FltCurCfgAclTcpRst_Object = MibTableColumn
fltCurCfgAclTcpRst = _FltCurCfgAclTcpRst_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 28),
    _FltCurCfgAclTcpRst_Type()
)
fltCurCfgAclTcpRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpRst.setStatus("current")


class _FltCurCfgAclTcpSyn_Type(Integer32):
    """Custom type fltCurCfgAclTcpSyn based on Integer32"""
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


_FltCurCfgAclTcpSyn_Type.__name__ = "Integer32"
_FltCurCfgAclTcpSyn_Object = MibTableColumn
fltCurCfgAclTcpSyn = _FltCurCfgAclTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 29),
    _FltCurCfgAclTcpSyn_Type()
)
fltCurCfgAclTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpSyn.setStatus("current")


class _FltCurCfgAclTcpFin_Type(Integer32):
    """Custom type fltCurCfgAclTcpFin based on Integer32"""
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


_FltCurCfgAclTcpFin_Type.__name__ = "Integer32"
_FltCurCfgAclTcpFin_Object = MibTableColumn
fltCurCfgAclTcpFin = _FltCurCfgAclTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 30),
    _FltCurCfgAclTcpFin_Type()
)
fltCurCfgAclTcpFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpFin.setStatus("current")


class _FltCurCfgAclIcmp_Type(Integer32):
    """Custom type fltCurCfgAclIcmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltCurCfgAclIcmp_Type.__name__ = "Integer32"
_FltCurCfgAclIcmp_Object = MibTableColumn
fltCurCfgAclIcmp = _FltCurCfgAclIcmp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 31),
    _FltCurCfgAclIcmp_Type()
)
fltCurCfgAclIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIcmp.setStatus("current")


class _FltCurCfgAclIpOption_Type(Integer32):
    """Custom type fltCurCfgAclIpOption based on Integer32"""
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


_FltCurCfgAclIpOption_Type.__name__ = "Integer32"
_FltCurCfgAclIpOption_Object = MibTableColumn
fltCurCfgAclIpOption = _FltCurCfgAclIpOption_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 32),
    _FltCurCfgAclIpOption_Type()
)
fltCurCfgAclIpOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIpOption.setStatus("current")
_FltCurCfgBwmContract_Type = Integer32
_FltCurCfgBwmContract_Object = MibTableColumn
fltCurCfgBwmContract = _FltCurCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 33),
    _FltCurCfgBwmContract_Type()
)
fltCurCfgBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgBwmContract.setStatus("current")


class _FltCurCfgAclIpTos_Type(Integer32):
    """Custom type fltCurCfgAclIpTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltCurCfgAclIpTos_Type.__name__ = "Integer32"
_FltCurCfgAclIpTos_Object = MibTableColumn
fltCurCfgAclIpTos = _FltCurCfgAclIpTos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 34),
    _FltCurCfgAclIpTos_Type()
)
fltCurCfgAclIpTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIpTos.setStatus("current")


class _FltCurCfgAclIpTosMask_Type(Integer32):
    """Custom type fltCurCfgAclIpTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltCurCfgAclIpTosMask_Type.__name__ = "Integer32"
_FltCurCfgAclIpTosMask_Object = MibTableColumn
fltCurCfgAclIpTosMask = _FltCurCfgAclIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 35),
    _FltCurCfgAclIpTosMask_Type()
)
fltCurCfgAclIpTosMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIpTosMask.setStatus("current")


class _FltCurCfgAclIpTosNew_Type(Integer32):
    """Custom type fltCurCfgAclIpTosNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltCurCfgAclIpTosNew_Type.__name__ = "Integer32"
_FltCurCfgAclIpTosNew_Object = MibTableColumn
fltCurCfgAclIpTosNew = _FltCurCfgAclIpTosNew_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 36),
    _FltCurCfgAclIpTosNew_Type()
)
fltCurCfgAclIpTosNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIpTosNew.setStatus("current")


class _FltCurCfgFwlb_Type(Integer32):
    """Custom type fltCurCfgFwlb based on Integer32"""
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


_FltCurCfgFwlb_Type.__name__ = "Integer32"
_FltCurCfgFwlb_Object = MibTableColumn
fltCurCfgFwlb = _FltCurCfgFwlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 37),
    _FltCurCfgFwlb_Type()
)
fltCurCfgFwlb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgFwlb.setStatus("current")


class _FltCurCfgNatTimeout_Type(Integer32):
    """Custom type fltCurCfgNatTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 32768),
    )


_FltCurCfgNatTimeout_Type.__name__ = "Integer32"
_FltCurCfgNatTimeout_Object = MibTableColumn
fltCurCfgNatTimeout = _FltCurCfgNatTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 38),
    _FltCurCfgNatTimeout_Type()
)
fltCurCfgNatTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgNatTimeout.setStatus("current")


class _FltCurCfgLinklb_Type(Integer32):
    """Custom type fltCurCfgLinklb based on Integer32"""
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


_FltCurCfgLinklb_Type.__name__ = "Integer32"
_FltCurCfgLinklb_Object = MibTableColumn
fltCurCfgLinklb = _FltCurCfgLinklb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 39),
    _FltCurCfgLinklb_Type()
)
fltCurCfgLinklb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgLinklb.setStatus("current")


class _FltCurCfgWapRadiusSnoop_Type(Integer32):
    """Custom type fltCurCfgWapRadiusSnoop based on Integer32"""
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


_FltCurCfgWapRadiusSnoop_Type.__name__ = "Integer32"
_FltCurCfgWapRadiusSnoop_Object = MibTableColumn
fltCurCfgWapRadiusSnoop = _FltCurCfgWapRadiusSnoop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 40),
    _FltCurCfgWapRadiusSnoop_Type()
)
fltCurCfgWapRadiusSnoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgWapRadiusSnoop.setStatus("current")


class _FltCurCfgSrcIpMac_Type(Integer32):
    """Custom type fltCurCfgSrcIpMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2))
    )


_FltCurCfgSrcIpMac_Type.__name__ = "Integer32"
_FltCurCfgSrcIpMac_Object = MibTableColumn
fltCurCfgSrcIpMac = _FltCurCfgSrcIpMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 41),
    _FltCurCfgSrcIpMac_Type()
)
fltCurCfgSrcIpMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgSrcIpMac.setStatus("current")


class _FltCurCfgDstIpMac_Type(Integer32):
    """Custom type fltCurCfgDstIpMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2))
    )


_FltCurCfgDstIpMac_Type.__name__ = "Integer32"
_FltCurCfgDstIpMac_Object = MibTableColumn
fltCurCfgDstIpMac = _FltCurCfgDstIpMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 42),
    _FltCurCfgDstIpMac_Type()
)
fltCurCfgDstIpMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgDstIpMac.setStatus("current")


class _FltCurCfgIdslbHash_Type(Integer32):
    """Custom type fltCurCfgIdslbHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sip", 1),
          ("dip", 2),
          ("both", 3))
    )


_FltCurCfgIdslbHash_Type.__name__ = "Integer32"
_FltCurCfgIdslbHash_Object = MibTableColumn
fltCurCfgIdslbHash = _FltCurCfgIdslbHash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 43),
    _FltCurCfgIdslbHash_Type()
)
fltCurCfgIdslbHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgIdslbHash.setStatus("current")


class _FltCurCfgVlan_Type(Integer32):
    """Custom type fltCurCfgVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4090),
    )


_FltCurCfgVlan_Type.__name__ = "Integer32"
_FltCurCfgVlan_Object = MibTableColumn
fltCurCfgVlan = _FltCurCfgVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 44),
    _FltCurCfgVlan_Type()
)
fltCurCfgVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgVlan.setStatus("current")


class _FltCurCfgName_Type(DisplayString):
    """Custom type fltCurCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FltCurCfgName_Type.__name__ = "DisplayString"
_FltCurCfgName_Object = MibTableColumn
fltCurCfgName = _FltCurCfgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 45),
    _FltCurCfgName_Type()
)
fltCurCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgName.setStatus("current")


class _FltCurCfgTcpRateLimit_Type(Integer32):
    """Custom type fltCurCfgTcpRateLimit based on Integer32"""
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


_FltCurCfgTcpRateLimit_Type.__name__ = "Integer32"
_FltCurCfgTcpRateLimit_Object = MibTableColumn
fltCurCfgTcpRateLimit = _FltCurCfgTcpRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 46),
    _FltCurCfgTcpRateLimit_Type()
)
fltCurCfgTcpRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgTcpRateLimit.setStatus("current")


class _FltCurCfgTcpRateMaxConn_Type(Integer32):
    """Custom type fltCurCfgTcpRateMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltCurCfgTcpRateMaxConn_Type.__name__ = "Integer32"
_FltCurCfgTcpRateMaxConn_Object = MibTableColumn
fltCurCfgTcpRateMaxConn = _FltCurCfgTcpRateMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 47),
    _FltCurCfgTcpRateMaxConn_Type()
)
fltCurCfgTcpRateMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgTcpRateMaxConn.setStatus("current")


class _FltCurCfgHash_Type(Integer32):
    """Custom type fltCurCfgHash based on Integer32"""
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
        *(("auto", 1),
          ("sip", 2),
          ("dip", 3),
          ("both", 4),
          ("sipsport", 5))
    )


_FltCurCfgHash_Type.__name__ = "Integer32"
_FltCurCfgHash_Object = MibTableColumn
fltCurCfgHash = _FltCurCfgHash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 48),
    _FltCurCfgHash_Type()
)
fltCurCfgHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgHash.setStatus("current")


class _FltCurCfgLayer7DenyState_Type(Integer32):
    """Custom type fltCurCfgLayer7DenyState based on Integer32"""
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


_FltCurCfgLayer7DenyState_Type.__name__ = "Integer32"
_FltCurCfgLayer7DenyState_Object = MibTableColumn
fltCurCfgLayer7DenyState = _FltCurCfgLayer7DenyState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 50),
    _FltCurCfgLayer7DenyState_Type()
)
fltCurCfgLayer7DenyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgLayer7DenyState.setStatus("current")
_FltCurCfgLayer7DenyUrlBmap_Type = OctetString
_FltCurCfgLayer7DenyUrlBmap_Object = MibTableColumn
fltCurCfgLayer7DenyUrlBmap = _FltCurCfgLayer7DenyUrlBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 51),
    _FltCurCfgLayer7DenyUrlBmap_Type()
)
fltCurCfgLayer7DenyUrlBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgLayer7DenyUrlBmap.setStatus("current")
_FltCurCfgGotoFilter_Type = Integer32
_FltCurCfgGotoFilter_Object = MibTableColumn
fltCurCfgGotoFilter = _FltCurCfgGotoFilter_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 52),
    _FltCurCfgGotoFilter_Type()
)
fltCurCfgGotoFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgGotoFilter.setStatus("current")


class _FltCurCfgRadiusWapPersist_Type(Integer32):
    """Custom type fltCurCfgRadiusWapPersist based on Integer32"""
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


_FltCurCfgRadiusWapPersist_Type.__name__ = "Integer32"
_FltCurCfgRadiusWapPersist_Object = MibTableColumn
fltCurCfgRadiusWapPersist = _FltCurCfgRadiusWapPersist_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 53),
    _FltCurCfgRadiusWapPersist_Type()
)
fltCurCfgRadiusWapPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRadiusWapPersist.setStatus("current")


class _FltCurCfgPbind_Type(Integer32):
    """Custom type fltCurCfgPbind based on Integer32"""
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


_FltCurCfgPbind_Type.__name__ = "Integer32"
_FltCurCfgPbind_Object = MibTableColumn
fltCurCfgPbind = _FltCurCfgPbind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 54),
    _FltCurCfgPbind_Type()
)
fltCurCfgPbind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgPbind.setStatus("current")


class _FltCurCfgTimeWindow_Type(Integer32):
    """Custom type fltCurCfgTimeWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FltCurCfgTimeWindow_Type.__name__ = "Integer32"
_FltCurCfgTimeWindow_Object = MibTableColumn
fltCurCfgTimeWindow = _FltCurCfgTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 55),
    _FltCurCfgTimeWindow_Type()
)
fltCurCfgTimeWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgTimeWindow.setStatus("current")


class _FltCurCfgHoldDuration_Type(Integer32):
    """Custom type fltCurCfgHoldDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_FltCurCfgHoldDuration_Type.__name__ = "Integer32"
_FltCurCfgHoldDuration_Object = MibTableColumn
fltCurCfgHoldDuration = _FltCurCfgHoldDuration_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 56),
    _FltCurCfgHoldDuration_Type()
)
fltCurCfgHoldDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgHoldDuration.setStatus("current")


class _FltCurCfgPatternMatch_Type(Integer32):
    """Custom type fltCurCfgPatternMatch based on Integer32"""
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


_FltCurCfgPatternMatch_Type.__name__ = "Integer32"
_FltCurCfgPatternMatch_Object = MibTableColumn
fltCurCfgPatternMatch = _FltCurCfgPatternMatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 57),
    _FltCurCfgPatternMatch_Type()
)
fltCurCfgPatternMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgPatternMatch.setStatus("current")


class _FltCurCfgLayer7DenyMatchAll_Type(Integer32):
    """Custom type fltCurCfgLayer7DenyMatchAll based on Integer32"""
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


_FltCurCfgLayer7DenyMatchAll_Type.__name__ = "Integer32"
_FltCurCfgLayer7DenyMatchAll_Object = MibTableColumn
fltCurCfgLayer7DenyMatchAll = _FltCurCfgLayer7DenyMatchAll_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 58),
    _FltCurCfgLayer7DenyMatchAll_Type()
)
fltCurCfgLayer7DenyMatchAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgLayer7DenyMatchAll.setStatus("current")
_FltCurCfgProxyIp_Type = IpAddress
_FltCurCfgProxyIp_Object = MibTableColumn
fltCurCfgProxyIp = _FltCurCfgProxyIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 59),
    _FltCurCfgProxyIp_Type()
)
fltCurCfgProxyIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgProxyIp.setStatus("current")


class _FltCurCfgLayer7ParseAll_Type(Integer32):
    """Custom type fltCurCfgLayer7ParseAll based on Integer32"""
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


_FltCurCfgLayer7ParseAll_Type.__name__ = "Integer32"
_FltCurCfgLayer7ParseAll_Object = MibTableColumn
fltCurCfgLayer7ParseAll = _FltCurCfgLayer7ParseAll_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 60),
    _FltCurCfgLayer7ParseAll_Type()
)
fltCurCfgLayer7ParseAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgLayer7ParseAll.setStatus("current")


class _FltCurCfgSecurityParseAll_Type(Integer32):
    """Custom type fltCurCfgSecurityParseAll based on Integer32"""
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


_FltCurCfgSecurityParseAll_Type.__name__ = "Integer32"
_FltCurCfgSecurityParseAll_Object = MibTableColumn
fltCurCfgSecurityParseAll = _FltCurCfgSecurityParseAll_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 61),
    _FltCurCfgSecurityParseAll_Type()
)
fltCurCfgSecurityParseAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgSecurityParseAll.setStatus("current")
_FltCurCfgPatternMatchGroupBmap_Type = OctetString
_FltCurCfgPatternMatchGroupBmap_Object = MibTableColumn
fltCurCfgPatternMatchGroupBmap = _FltCurCfgPatternMatchGroupBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 62),
    _FltCurCfgPatternMatchGroupBmap_Type()
)
fltCurCfgPatternMatchGroupBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgPatternMatchGroupBmap.setStatus("current")


class _FltCurCfg8021pBitsValue_Type(Integer32):
    """Custom type fltCurCfg8021pBitsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FltCurCfg8021pBitsValue_Type.__name__ = "Integer32"
_FltCurCfg8021pBitsValue_Object = MibTableColumn
fltCurCfg8021pBitsValue = _FltCurCfg8021pBitsValue_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 63),
    _FltCurCfg8021pBitsValue_Type()
)
fltCurCfg8021pBitsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfg8021pBitsValue.setStatus("current")


class _FltCurCfg8021pBitsMatch_Type(Integer32):
    """Custom type fltCurCfg8021pBitsMatch based on Integer32"""
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


_FltCurCfg8021pBitsMatch_Type.__name__ = "Integer32"
_FltCurCfg8021pBitsMatch_Object = MibTableColumn
fltCurCfg8021pBitsMatch = _FltCurCfg8021pBitsMatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 64),
    _FltCurCfg8021pBitsMatch_Type()
)
fltCurCfg8021pBitsMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfg8021pBitsMatch.setStatus("current")


class _FltCurCfgAclIpLength_Type(Integer32):
    """Custom type fltCurCfgAclIpLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FltCurCfgAclIpLength_Type.__name__ = "Integer32"
_FltCurCfgAclIpLength_Object = MibTableColumn
fltCurCfgAclIpLength = _FltCurCfgAclIpLength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 65),
    _FltCurCfgAclIpLength_Type()
)
fltCurCfgAclIpLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIpLength.setStatus("current")
_FltCurCfgIdsGroup_Type = Integer32
_FltCurCfgIdsGroup_Object = MibTableColumn
fltCurCfgIdsGroup = _FltCurCfgIdsGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 66),
    _FltCurCfgIdsGroup_Type()
)
fltCurCfgIdsGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgIdsGroup.setStatus("current")


class _FltCurCfgEgressPip_Type(Integer32):
    """Custom type fltCurCfgEgressPip based on Integer32"""
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


_FltCurCfgEgressPip_Type.__name__ = "Integer32"
_FltCurCfgEgressPip_Object = MibTableColumn
fltCurCfgEgressPip = _FltCurCfgEgressPip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 67),
    _FltCurCfgEgressPip_Type()
)
fltCurCfgEgressPip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgEgressPip.setStatus("current")


class _FltCurCfgDbind_Type(Integer32):
    """Custom type fltCurCfgDbind based on Integer32"""
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


_FltCurCfgDbind_Type.__name__ = "Integer32"
_FltCurCfgDbind_Object = MibTableColumn
fltCurCfgDbind = _FltCurCfgDbind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 68),
    _FltCurCfgDbind_Type()
)
fltCurCfgDbind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgDbind.setStatus("current")
_FltCurCfgRevBwmContract_Type = Integer32
_FltCurCfgRevBwmContract_Object = MibTableColumn
fltCurCfgRevBwmContract = _FltCurCfgRevBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 69),
    _FltCurCfgRevBwmContract_Type()
)
fltCurCfgRevBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRevBwmContract.setStatus("current")


class _FltCurCfgReverse_Type(Integer32):
    """Custom type fltCurCfgReverse based on Integer32"""
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


_FltCurCfgReverse_Type.__name__ = "Integer32"
_FltCurCfgReverse_Object = MibTableColumn
fltCurCfgReverse = _FltCurCfgReverse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 70),
    _FltCurCfgReverse_Type()
)
fltCurCfgReverse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgReverse.setStatus("current")


class _FltCurCfgParseChn_Type(Integer32):
    """Custom type fltCurCfgParseChn based on Integer32"""
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


_FltCurCfgParseChn_Type.__name__ = "Integer32"
_FltCurCfgParseChn_Object = MibTableColumn
fltCurCfgParseChn = _FltCurCfgParseChn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 71),
    _FltCurCfgParseChn_Type()
)
fltCurCfgParseChn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgParseChn.setStatus("current")
_FltCurCfgRtpBwmContract_Type = Integer32
_FltCurCfgRtpBwmContract_Object = MibTableColumn
fltCurCfgRtpBwmContract = _FltCurCfgRtpBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 72),
    _FltCurCfgRtpBwmContract_Type()
)
fltCurCfgRtpBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRtpBwmContract.setStatus("current")


class _FltCurCfgSipParsing_Type(Integer32):
    """Custom type fltCurCfgSipParsing based on Integer32"""
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


_FltCurCfgSipParsing_Type.__name__ = "Integer32"
_FltCurCfgSipParsing_Object = MibTableColumn
fltCurCfgSipParsing = _FltCurCfgSipParsing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 73),
    _FltCurCfgSipParsing_Type()
)
fltCurCfgSipParsing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgSipParsing.setStatus("current")


class _FltCurCfgSessionMirror_Type(Integer32):
    """Custom type fltCurCfgSessionMirror based on Integer32"""
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


_FltCurCfgSessionMirror_Type.__name__ = "Integer32"
_FltCurCfgSessionMirror_Object = MibTableColumn
fltCurCfgSessionMirror = _FltCurCfgSessionMirror_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 74),
    _FltCurCfgSessionMirror_Type()
)
fltCurCfgSessionMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgSessionMirror.setStatus("current")


class _FltCurCfgIpVer_Type(Integer32):
    """Custom type fltCurCfgIpVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_FltCurCfgIpVer_Type.__name__ = "Integer32"
_FltCurCfgIpVer_Object = MibTableColumn
fltCurCfgIpVer = _FltCurCfgIpVer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 75),
    _FltCurCfgIpVer_Type()
)
fltCurCfgIpVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgIpVer.setStatus("current")


class _FltCurCfgIpv6Sip_Type(DisplayString):
    """Custom type fltCurCfgIpv6Sip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FltCurCfgIpv6Sip_Type.__name__ = "DisplayString"
_FltCurCfgIpv6Sip_Object = MibTableColumn
fltCurCfgIpv6Sip = _FltCurCfgIpv6Sip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 76),
    _FltCurCfgIpv6Sip_Type()
)
fltCurCfgIpv6Sip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgIpv6Sip.setStatus("current")


class _FltCurCfgIpv6Sprefix_Type(Integer32):
    """Custom type fltCurCfgIpv6Sprefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FltCurCfgIpv6Sprefix_Type.__name__ = "Integer32"
_FltCurCfgIpv6Sprefix_Object = MibTableColumn
fltCurCfgIpv6Sprefix = _FltCurCfgIpv6Sprefix_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 77),
    _FltCurCfgIpv6Sprefix_Type()
)
fltCurCfgIpv6Sprefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgIpv6Sprefix.setStatus("current")


class _FltCurCfgIpv6Dip_Type(DisplayString):
    """Custom type fltCurCfgIpv6Dip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FltCurCfgIpv6Dip_Type.__name__ = "DisplayString"
_FltCurCfgIpv6Dip_Object = MibTableColumn
fltCurCfgIpv6Dip = _FltCurCfgIpv6Dip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 78),
    _FltCurCfgIpv6Dip_Type()
)
fltCurCfgIpv6Dip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgIpv6Dip.setStatus("current")


class _FltCurCfgIpv6Dprefix_Type(Integer32):
    """Custom type fltCurCfgIpv6Dprefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FltCurCfgIpv6Dprefix_Type.__name__ = "Integer32"
_FltCurCfgIpv6Dprefix_Object = MibTableColumn
fltCurCfgIpv6Dprefix = _FltCurCfgIpv6Dprefix_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 2, 1, 79),
    _FltCurCfgIpv6Dprefix_Type()
)
fltCurCfgIpv6Dprefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgIpv6Dprefix.setStatus("current")
_FltNewCfgTable_Object = MibTable
fltNewCfgTable = _FltNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fltNewCfgTable.setStatus("current")
_FltNewCfgTableEntry_Object = MibTableRow
fltNewCfgTableEntry = _FltNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1)
)
fltNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "fltNewCfgIndx"),
)
if mibBuilder.loadTexts:
    fltNewCfgTableEntry.setStatus("current")
_FltNewCfgIndx_Type = Integer32
_FltNewCfgIndx_Object = MibTableColumn
fltNewCfgIndx = _FltNewCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 1),
    _FltNewCfgIndx_Type()
)
fltNewCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgIndx.setStatus("current")
_FltNewCfgSrcIp_Type = IpAddress
_FltNewCfgSrcIp_Object = MibTableColumn
fltNewCfgSrcIp = _FltNewCfgSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 2),
    _FltNewCfgSrcIp_Type()
)
fltNewCfgSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgSrcIp.setStatus("current")
_FltNewCfgSrcIpMask_Type = IpAddress
_FltNewCfgSrcIpMask_Object = MibTableColumn
fltNewCfgSrcIpMask = _FltNewCfgSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 3),
    _FltNewCfgSrcIpMask_Type()
)
fltNewCfgSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgSrcIpMask.setStatus("current")
_FltNewCfgDstIp_Type = IpAddress
_FltNewCfgDstIp_Object = MibTableColumn
fltNewCfgDstIp = _FltNewCfgDstIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 4),
    _FltNewCfgDstIp_Type()
)
fltNewCfgDstIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgDstIp.setStatus("current")
_FltNewCfgDstIpMask_Type = IpAddress
_FltNewCfgDstIpMask_Object = MibTableColumn
fltNewCfgDstIpMask = _FltNewCfgDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 5),
    _FltNewCfgDstIpMask_Type()
)
fltNewCfgDstIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgDstIpMask.setStatus("current")


class _FltNewCfgProtocol_Type(Integer32):
    """Custom type fltNewCfgProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltNewCfgProtocol_Type.__name__ = "Integer32"
_FltNewCfgProtocol_Object = MibTableColumn
fltNewCfgProtocol = _FltNewCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 6),
    _FltNewCfgProtocol_Type()
)
fltNewCfgProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgProtocol.setStatus("current")


class _FltNewCfgRangeHighSrcPort_Type(Integer32):
    """Custom type fltNewCfgRangeHighSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltNewCfgRangeHighSrcPort_Type.__name__ = "Integer32"
_FltNewCfgRangeHighSrcPort_Object = MibTableColumn
fltNewCfgRangeHighSrcPort = _FltNewCfgRangeHighSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 7),
    _FltNewCfgRangeHighSrcPort_Type()
)
fltNewCfgRangeHighSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgRangeHighSrcPort.setStatus("current")


class _FltNewCfgRangeLowSrcPort_Type(Integer32):
    """Custom type fltNewCfgRangeLowSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltNewCfgRangeLowSrcPort_Type.__name__ = "Integer32"
_FltNewCfgRangeLowSrcPort_Object = MibTableColumn
fltNewCfgRangeLowSrcPort = _FltNewCfgRangeLowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 8),
    _FltNewCfgRangeLowSrcPort_Type()
)
fltNewCfgRangeLowSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgRangeLowSrcPort.setStatus("current")


class _FltNewCfgRangeLowDstPort_Type(Integer32):
    """Custom type fltNewCfgRangeLowDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltNewCfgRangeLowDstPort_Type.__name__ = "Integer32"
_FltNewCfgRangeLowDstPort_Object = MibTableColumn
fltNewCfgRangeLowDstPort = _FltNewCfgRangeLowDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 9),
    _FltNewCfgRangeLowDstPort_Type()
)
fltNewCfgRangeLowDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgRangeLowDstPort.setStatus("current")


class _FltNewCfgRangeHighDstPort_Type(Integer32):
    """Custom type fltNewCfgRangeHighDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltNewCfgRangeHighDstPort_Type.__name__ = "Integer32"
_FltNewCfgRangeHighDstPort_Object = MibTableColumn
fltNewCfgRangeHighDstPort = _FltNewCfgRangeHighDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 10),
    _FltNewCfgRangeHighDstPort_Type()
)
fltNewCfgRangeHighDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgRangeHighDstPort.setStatus("current")


class _FltNewCfgAction_Type(Integer32):
    """Custom type fltNewCfgAction based on Integer32"""
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
        *(("allow", 1),
          ("deny", 2),
          ("redirect", 3),
          ("nat", 4),
          ("goto", 5))
    )


_FltNewCfgAction_Type.__name__ = "Integer32"
_FltNewCfgAction_Object = MibTableColumn
fltNewCfgAction = _FltNewCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 11),
    _FltNewCfgAction_Type()
)
fltNewCfgAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgAction.setStatus("current")


class _FltNewCfgRedirPort_Type(Integer32):
    """Custom type fltNewCfgRedirPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltNewCfgRedirPort_Type.__name__ = "Integer32"
_FltNewCfgRedirPort_Object = MibTableColumn
fltNewCfgRedirPort = _FltNewCfgRedirPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 12),
    _FltNewCfgRedirPort_Type()
)
fltNewCfgRedirPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgRedirPort.setStatus("current")
_FltNewCfgRedirGroup_Type = Integer32
_FltNewCfgRedirGroup_Object = MibTableColumn
fltNewCfgRedirGroup = _FltNewCfgRedirGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 13),
    _FltNewCfgRedirGroup_Type()
)
fltNewCfgRedirGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgRedirGroup.setStatus("current")


class _FltNewCfgLog_Type(Integer32):
    """Custom type fltNewCfgLog based on Integer32"""
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


_FltNewCfgLog_Type.__name__ = "Integer32"
_FltNewCfgLog_Object = MibTableColumn
fltNewCfgLog = _FltNewCfgLog_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 14),
    _FltNewCfgLog_Type()
)
fltNewCfgLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgLog.setStatus("current")


class _FltNewCfgState_Type(Integer32):
    """Custom type fltNewCfgState based on Integer32"""
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


_FltNewCfgState_Type.__name__ = "Integer32"
_FltNewCfgState_Object = MibTableColumn
fltNewCfgState = _FltNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 15),
    _FltNewCfgState_Type()
)
fltNewCfgState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgState.setStatus("current")


class _FltNewCfgDelete_Type(Integer32):
    """Custom type fltNewCfgDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_FltNewCfgDelete_Type.__name__ = "Integer32"
_FltNewCfgDelete_Object = MibTableColumn
fltNewCfgDelete = _FltNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 16),
    _FltNewCfgDelete_Type()
)
fltNewCfgDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgDelete.setStatus("current")


class _FltNewCfgNat_Type(Integer32):
    """Custom type fltNewCfgNat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination-address", 1),
          ("source-address", 2))
    )


_FltNewCfgNat_Type.__name__ = "Integer32"
_FltNewCfgNat_Object = MibTableColumn
fltNewCfgNat = _FltNewCfgNat_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 17),
    _FltNewCfgNat_Type()
)
fltNewCfgNat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgNat.setStatus("current")


class _FltNewCfgCache_Type(Integer32):
    """Custom type fltNewCfgCache based on Integer32"""
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


_FltNewCfgCache_Type.__name__ = "Integer32"
_FltNewCfgCache_Object = MibTableColumn
fltNewCfgCache = _FltNewCfgCache_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 18),
    _FltNewCfgCache_Type()
)
fltNewCfgCache.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgCache.setStatus("current")


class _FltNewCfgInvert_Type(Integer32):
    """Custom type fltNewCfgInvert based on Integer32"""
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


_FltNewCfgInvert_Type.__name__ = "Integer32"
_FltNewCfgInvert_Object = MibTableColumn
fltNewCfgInvert = _FltNewCfgInvert_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 19),
    _FltNewCfgInvert_Type()
)
fltNewCfgInvert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgInvert.setStatus("current")


class _FltNewCfgClientProxy_Type(Integer32):
    """Custom type fltNewCfgClientProxy based on Integer32"""
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


_FltNewCfgClientProxy_Type.__name__ = "Integer32"
_FltNewCfgClientProxy_Object = MibTableColumn
fltNewCfgClientProxy = _FltNewCfgClientProxy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 20),
    _FltNewCfgClientProxy_Type()
)
fltNewCfgClientProxy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgClientProxy.setStatus("current")


class _FltNewCfgTcpAck_Type(Integer32):
    """Custom type fltNewCfgTcpAck based on Integer32"""
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


_FltNewCfgTcpAck_Type.__name__ = "Integer32"
_FltNewCfgTcpAck_Object = MibTableColumn
fltNewCfgTcpAck = _FltNewCfgTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 21),
    _FltNewCfgTcpAck_Type()
)
fltNewCfgTcpAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgTcpAck.setStatus("current")
_FltNewCfgSrcMac_Type = PhysAddress
_FltNewCfgSrcMac_Object = MibTableColumn
fltNewCfgSrcMac = _FltNewCfgSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 23),
    _FltNewCfgSrcMac_Type()
)
fltNewCfgSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgSrcMac.setStatus("current")
_FltNewCfgDstMac_Type = PhysAddress
_FltNewCfgDstMac_Object = MibTableColumn
fltNewCfgDstMac = _FltNewCfgDstMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 24),
    _FltNewCfgDstMac_Type()
)
fltNewCfgDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgDstMac.setStatus("current")


class _FltNewCfgFtpNatActive_Type(Integer32):
    """Custom type fltNewCfgFtpNatActive based on Integer32"""
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


_FltNewCfgFtpNatActive_Type.__name__ = "Integer32"
_FltNewCfgFtpNatActive_Object = MibTableColumn
fltNewCfgFtpNatActive = _FltNewCfgFtpNatActive_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 25),
    _FltNewCfgFtpNatActive_Type()
)
fltNewCfgFtpNatActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgFtpNatActive.setStatus("current")


class _FltNewCfgAclTcpUrg_Type(Integer32):
    """Custom type fltNewCfgAclTcpUrg based on Integer32"""
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


_FltNewCfgAclTcpUrg_Type.__name__ = "Integer32"
_FltNewCfgAclTcpUrg_Object = MibTableColumn
fltNewCfgAclTcpUrg = _FltNewCfgAclTcpUrg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 26),
    _FltNewCfgAclTcpUrg_Type()
)
fltNewCfgAclTcpUrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpUrg.setStatus("current")


class _FltNewCfgAclTcpAck_Type(Integer32):
    """Custom type fltNewCfgAclTcpAck based on Integer32"""
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


_FltNewCfgAclTcpAck_Type.__name__ = "Integer32"
_FltNewCfgAclTcpAck_Object = MibTableColumn
fltNewCfgAclTcpAck = _FltNewCfgAclTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 27),
    _FltNewCfgAclTcpAck_Type()
)
fltNewCfgAclTcpAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpAck.setStatus("current")


class _FltNewCfgAclTcpPsh_Type(Integer32):
    """Custom type fltNewCfgAclTcpPsh based on Integer32"""
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


_FltNewCfgAclTcpPsh_Type.__name__ = "Integer32"
_FltNewCfgAclTcpPsh_Object = MibTableColumn
fltNewCfgAclTcpPsh = _FltNewCfgAclTcpPsh_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 28),
    _FltNewCfgAclTcpPsh_Type()
)
fltNewCfgAclTcpPsh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpPsh.setStatus("current")


class _FltNewCfgAclTcpRst_Type(Integer32):
    """Custom type fltNewCfgAclTcpRst based on Integer32"""
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


_FltNewCfgAclTcpRst_Type.__name__ = "Integer32"
_FltNewCfgAclTcpRst_Object = MibTableColumn
fltNewCfgAclTcpRst = _FltNewCfgAclTcpRst_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 29),
    _FltNewCfgAclTcpRst_Type()
)
fltNewCfgAclTcpRst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpRst.setStatus("current")


class _FltNewCfgAclTcpSyn_Type(Integer32):
    """Custom type fltNewCfgAclTcpSyn based on Integer32"""
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


_FltNewCfgAclTcpSyn_Type.__name__ = "Integer32"
_FltNewCfgAclTcpSyn_Object = MibTableColumn
fltNewCfgAclTcpSyn = _FltNewCfgAclTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 30),
    _FltNewCfgAclTcpSyn_Type()
)
fltNewCfgAclTcpSyn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpSyn.setStatus("current")


class _FltNewCfgAclTcpFin_Type(Integer32):
    """Custom type fltNewCfgAclTcpFin based on Integer32"""
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


_FltNewCfgAclTcpFin_Type.__name__ = "Integer32"
_FltNewCfgAclTcpFin_Object = MibTableColumn
fltNewCfgAclTcpFin = _FltNewCfgAclTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 31),
    _FltNewCfgAclTcpFin_Type()
)
fltNewCfgAclTcpFin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpFin.setStatus("current")


class _FltNewCfgAclIcmp_Type(Integer32):
    """Custom type fltNewCfgAclIcmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltNewCfgAclIcmp_Type.__name__ = "Integer32"
_FltNewCfgAclIcmp_Object = MibTableColumn
fltNewCfgAclIcmp = _FltNewCfgAclIcmp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 32),
    _FltNewCfgAclIcmp_Type()
)
fltNewCfgAclIcmp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgAclIcmp.setStatus("current")


class _FltNewCfgAclIpOption_Type(Integer32):
    """Custom type fltNewCfgAclIpOption based on Integer32"""
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


_FltNewCfgAclIpOption_Type.__name__ = "Integer32"
_FltNewCfgAclIpOption_Object = MibTableColumn
fltNewCfgAclIpOption = _FltNewCfgAclIpOption_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 33),
    _FltNewCfgAclIpOption_Type()
)
fltNewCfgAclIpOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgAclIpOption.setStatus("current")
_FltNewCfgBwmContract_Type = Integer32
_FltNewCfgBwmContract_Object = MibTableColumn
fltNewCfgBwmContract = _FltNewCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 34),
    _FltNewCfgBwmContract_Type()
)
fltNewCfgBwmContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgBwmContract.setStatus("current")


class _FltNewCfgAclIpTos_Type(Integer32):
    """Custom type fltNewCfgAclIpTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltNewCfgAclIpTos_Type.__name__ = "Integer32"
_FltNewCfgAclIpTos_Object = MibTableColumn
fltNewCfgAclIpTos = _FltNewCfgAclIpTos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 35),
    _FltNewCfgAclIpTos_Type()
)
fltNewCfgAclIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgAclIpTos.setStatus("current")


class _FltNewCfgAclIpTosMask_Type(Integer32):
    """Custom type fltNewCfgAclIpTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltNewCfgAclIpTosMask_Type.__name__ = "Integer32"
_FltNewCfgAclIpTosMask_Object = MibTableColumn
fltNewCfgAclIpTosMask = _FltNewCfgAclIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 36),
    _FltNewCfgAclIpTosMask_Type()
)
fltNewCfgAclIpTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgAclIpTosMask.setStatus("current")


class _FltNewCfgAclIpTosNew_Type(Integer32):
    """Custom type fltNewCfgAclIpTosNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltNewCfgAclIpTosNew_Type.__name__ = "Integer32"
_FltNewCfgAclIpTosNew_Object = MibTableColumn
fltNewCfgAclIpTosNew = _FltNewCfgAclIpTosNew_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 37),
    _FltNewCfgAclIpTosNew_Type()
)
fltNewCfgAclIpTosNew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgAclIpTosNew.setStatus("current")


class _FltNewCfgFwlb_Type(Integer32):
    """Custom type fltNewCfgFwlb based on Integer32"""
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


_FltNewCfgFwlb_Type.__name__ = "Integer32"
_FltNewCfgFwlb_Object = MibTableColumn
fltNewCfgFwlb = _FltNewCfgFwlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 38),
    _FltNewCfgFwlb_Type()
)
fltNewCfgFwlb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgFwlb.setStatus("current")


class _FltNewCfgNatTimeout_Type(Integer32):
    """Custom type fltNewCfgNatTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 32768),
    )


_FltNewCfgNatTimeout_Type.__name__ = "Integer32"
_FltNewCfgNatTimeout_Object = MibTableColumn
fltNewCfgNatTimeout = _FltNewCfgNatTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 39),
    _FltNewCfgNatTimeout_Type()
)
fltNewCfgNatTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgNatTimeout.setStatus("current")


class _FltNewCfgLinklb_Type(Integer32):
    """Custom type fltNewCfgLinklb based on Integer32"""
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


_FltNewCfgLinklb_Type.__name__ = "Integer32"
_FltNewCfgLinklb_Object = MibTableColumn
fltNewCfgLinklb = _FltNewCfgLinklb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 40),
    _FltNewCfgLinklb_Type()
)
fltNewCfgLinklb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgLinklb.setStatus("current")


class _FltNewCfgWapRadiusSnoop_Type(Integer32):
    """Custom type fltNewCfgWapRadiusSnoop based on Integer32"""
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


_FltNewCfgWapRadiusSnoop_Type.__name__ = "Integer32"
_FltNewCfgWapRadiusSnoop_Object = MibTableColumn
fltNewCfgWapRadiusSnoop = _FltNewCfgWapRadiusSnoop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 41),
    _FltNewCfgWapRadiusSnoop_Type()
)
fltNewCfgWapRadiusSnoop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgWapRadiusSnoop.setStatus("current")


class _FltNewCfgSrcIpMac_Type(Integer32):
    """Custom type fltNewCfgSrcIpMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2))
    )


_FltNewCfgSrcIpMac_Type.__name__ = "Integer32"
_FltNewCfgSrcIpMac_Object = MibTableColumn
fltNewCfgSrcIpMac = _FltNewCfgSrcIpMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 42),
    _FltNewCfgSrcIpMac_Type()
)
fltNewCfgSrcIpMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgSrcIpMac.setStatus("current")


class _FltNewCfgDstIpMac_Type(Integer32):
    """Custom type fltNewCfgDstIpMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2))
    )


_FltNewCfgDstIpMac_Type.__name__ = "Integer32"
_FltNewCfgDstIpMac_Object = MibTableColumn
fltNewCfgDstIpMac = _FltNewCfgDstIpMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 43),
    _FltNewCfgDstIpMac_Type()
)
fltNewCfgDstIpMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgDstIpMac.setStatus("current")


class _FltNewCfgIdslbHash_Type(Integer32):
    """Custom type fltNewCfgIdslbHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sip", 1),
          ("dip", 2),
          ("both", 3))
    )


_FltNewCfgIdslbHash_Type.__name__ = "Integer32"
_FltNewCfgIdslbHash_Object = MibTableColumn
fltNewCfgIdslbHash = _FltNewCfgIdslbHash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 44),
    _FltNewCfgIdslbHash_Type()
)
fltNewCfgIdslbHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgIdslbHash.setStatus("current")


class _FltNewCfgVlan_Type(Integer32):
    """Custom type fltNewCfgVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4090),
    )


_FltNewCfgVlan_Type.__name__ = "Integer32"
_FltNewCfgVlan_Object = MibTableColumn
fltNewCfgVlan = _FltNewCfgVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 45),
    _FltNewCfgVlan_Type()
)
fltNewCfgVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgVlan.setStatus("current")


class _FltNewCfgName_Type(DisplayString):
    """Custom type fltNewCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FltNewCfgName_Type.__name__ = "DisplayString"
_FltNewCfgName_Object = MibTableColumn
fltNewCfgName = _FltNewCfgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 46),
    _FltNewCfgName_Type()
)
fltNewCfgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgName.setStatus("current")


class _FltNewCfgTcpRateLimit_Type(Integer32):
    """Custom type fltNewCfgTcpRateLimit based on Integer32"""
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


_FltNewCfgTcpRateLimit_Type.__name__ = "Integer32"
_FltNewCfgTcpRateLimit_Object = MibTableColumn
fltNewCfgTcpRateLimit = _FltNewCfgTcpRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 47),
    _FltNewCfgTcpRateLimit_Type()
)
fltNewCfgTcpRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgTcpRateLimit.setStatus("current")


class _FltNewCfgTcpRateMaxConn_Type(Integer32):
    """Custom type fltNewCfgTcpRateMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltNewCfgTcpRateMaxConn_Type.__name__ = "Integer32"
_FltNewCfgTcpRateMaxConn_Object = MibTableColumn
fltNewCfgTcpRateMaxConn = _FltNewCfgTcpRateMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 48),
    _FltNewCfgTcpRateMaxConn_Type()
)
fltNewCfgTcpRateMaxConn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgTcpRateMaxConn.setStatus("current")


class _FltNewCfgHash_Type(Integer32):
    """Custom type fltNewCfgHash based on Integer32"""
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
        *(("auto", 1),
          ("sip", 2),
          ("dip", 3),
          ("both", 4),
          ("sipsport", 5))
    )


_FltNewCfgHash_Type.__name__ = "Integer32"
_FltNewCfgHash_Object = MibTableColumn
fltNewCfgHash = _FltNewCfgHash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 49),
    _FltNewCfgHash_Type()
)
fltNewCfgHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgHash.setStatus("current")


class _FltNewCfgLayer7DenyState_Type(Integer32):
    """Custom type fltNewCfgLayer7DenyState based on Integer32"""
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


_FltNewCfgLayer7DenyState_Type.__name__ = "Integer32"
_FltNewCfgLayer7DenyState_Object = MibTableColumn
fltNewCfgLayer7DenyState = _FltNewCfgLayer7DenyState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 51),
    _FltNewCfgLayer7DenyState_Type()
)
fltNewCfgLayer7DenyState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgLayer7DenyState.setStatus("current")
_FltNewCfgLayer7DenyUrlBmap_Type = OctetString
_FltNewCfgLayer7DenyUrlBmap_Object = MibTableColumn
fltNewCfgLayer7DenyUrlBmap = _FltNewCfgLayer7DenyUrlBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 52),
    _FltNewCfgLayer7DenyUrlBmap_Type()
)
fltNewCfgLayer7DenyUrlBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgLayer7DenyUrlBmap.setStatus("current")
_FltNewCfgLayer7DenyAddUrl_Type = Integer32
_FltNewCfgLayer7DenyAddUrl_Object = MibTableColumn
fltNewCfgLayer7DenyAddUrl = _FltNewCfgLayer7DenyAddUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 53),
    _FltNewCfgLayer7DenyAddUrl_Type()
)
fltNewCfgLayer7DenyAddUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgLayer7DenyAddUrl.setStatus("current")
_FltNewCfgLayer7DenyRemUrl_Type = Integer32
_FltNewCfgLayer7DenyRemUrl_Object = MibTableColumn
fltNewCfgLayer7DenyRemUrl = _FltNewCfgLayer7DenyRemUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 54),
    _FltNewCfgLayer7DenyRemUrl_Type()
)
fltNewCfgLayer7DenyRemUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgLayer7DenyRemUrl.setStatus("current")
_FltNewCfgGotoFilter_Type = Integer32
_FltNewCfgGotoFilter_Object = MibTableColumn
fltNewCfgGotoFilter = _FltNewCfgGotoFilter_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 55),
    _FltNewCfgGotoFilter_Type()
)
fltNewCfgGotoFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgGotoFilter.setStatus("current")


class _FltNewCfgRadiusWapPersist_Type(Integer32):
    """Custom type fltNewCfgRadiusWapPersist based on Integer32"""
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


_FltNewCfgRadiusWapPersist_Type.__name__ = "Integer32"
_FltNewCfgRadiusWapPersist_Object = MibTableColumn
fltNewCfgRadiusWapPersist = _FltNewCfgRadiusWapPersist_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 56),
    _FltNewCfgRadiusWapPersist_Type()
)
fltNewCfgRadiusWapPersist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgRadiusWapPersist.setStatus("current")


class _FltNewCfgPbind_Type(Integer32):
    """Custom type fltNewCfgPbind based on Integer32"""
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


_FltNewCfgPbind_Type.__name__ = "Integer32"
_FltNewCfgPbind_Object = MibTableColumn
fltNewCfgPbind = _FltNewCfgPbind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 57),
    _FltNewCfgPbind_Type()
)
fltNewCfgPbind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgPbind.setStatus("current")


class _FltNewCfgTimeWindow_Type(Integer32):
    """Custom type fltNewCfgTimeWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FltNewCfgTimeWindow_Type.__name__ = "Integer32"
_FltNewCfgTimeWindow_Object = MibTableColumn
fltNewCfgTimeWindow = _FltNewCfgTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 58),
    _FltNewCfgTimeWindow_Type()
)
fltNewCfgTimeWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgTimeWindow.setStatus("current")


class _FltNewCfgHoldDuration_Type(Integer32):
    """Custom type fltNewCfgHoldDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_FltNewCfgHoldDuration_Type.__name__ = "Integer32"
_FltNewCfgHoldDuration_Object = MibTableColumn
fltNewCfgHoldDuration = _FltNewCfgHoldDuration_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 59),
    _FltNewCfgHoldDuration_Type()
)
fltNewCfgHoldDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgHoldDuration.setStatus("current")


class _FltNewCfgPatternMatch_Type(Integer32):
    """Custom type fltNewCfgPatternMatch based on Integer32"""
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


_FltNewCfgPatternMatch_Type.__name__ = "Integer32"
_FltNewCfgPatternMatch_Object = MibTableColumn
fltNewCfgPatternMatch = _FltNewCfgPatternMatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 60),
    _FltNewCfgPatternMatch_Type()
)
fltNewCfgPatternMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgPatternMatch.setStatus("current")


class _FltNewCfgLayer7DenyMatchAll_Type(Integer32):
    """Custom type fltNewCfgLayer7DenyMatchAll based on Integer32"""
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


_FltNewCfgLayer7DenyMatchAll_Type.__name__ = "Integer32"
_FltNewCfgLayer7DenyMatchAll_Object = MibTableColumn
fltNewCfgLayer7DenyMatchAll = _FltNewCfgLayer7DenyMatchAll_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 61),
    _FltNewCfgLayer7DenyMatchAll_Type()
)
fltNewCfgLayer7DenyMatchAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgLayer7DenyMatchAll.setStatus("current")
_FltNewCfgProxyIp_Type = IpAddress
_FltNewCfgProxyIp_Object = MibTableColumn
fltNewCfgProxyIp = _FltNewCfgProxyIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 62),
    _FltNewCfgProxyIp_Type()
)
fltNewCfgProxyIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgProxyIp.setStatus("current")


class _FltNewCfgLayer7ParseAll_Type(Integer32):
    """Custom type fltNewCfgLayer7ParseAll based on Integer32"""
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


_FltNewCfgLayer7ParseAll_Type.__name__ = "Integer32"
_FltNewCfgLayer7ParseAll_Object = MibTableColumn
fltNewCfgLayer7ParseAll = _FltNewCfgLayer7ParseAll_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 63),
    _FltNewCfgLayer7ParseAll_Type()
)
fltNewCfgLayer7ParseAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgLayer7ParseAll.setStatus("current")


class _FltNewCfgSecurityParseAll_Type(Integer32):
    """Custom type fltNewCfgSecurityParseAll based on Integer32"""
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


_FltNewCfgSecurityParseAll_Type.__name__ = "Integer32"
_FltNewCfgSecurityParseAll_Object = MibTableColumn
fltNewCfgSecurityParseAll = _FltNewCfgSecurityParseAll_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 64),
    _FltNewCfgSecurityParseAll_Type()
)
fltNewCfgSecurityParseAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgSecurityParseAll.setStatus("current")
_FltNewCfgPatternMatchGroupBmap_Type = OctetString
_FltNewCfgPatternMatchGroupBmap_Object = MibTableColumn
fltNewCfgPatternMatchGroupBmap = _FltNewCfgPatternMatchGroupBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 65),
    _FltNewCfgPatternMatchGroupBmap_Type()
)
fltNewCfgPatternMatchGroupBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgPatternMatchGroupBmap.setStatus("current")
_FltNewCfgAddPatternMatchGroup_Type = Integer32
_FltNewCfgAddPatternMatchGroup_Object = MibTableColumn
fltNewCfgAddPatternMatchGroup = _FltNewCfgAddPatternMatchGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 66),
    _FltNewCfgAddPatternMatchGroup_Type()
)
fltNewCfgAddPatternMatchGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgAddPatternMatchGroup.setStatus("current")
_FltNewCfgRemPatternMatchGroup_Type = Integer32
_FltNewCfgRemPatternMatchGroup_Object = MibTableColumn
fltNewCfgRemPatternMatchGroup = _FltNewCfgRemPatternMatchGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 67),
    _FltNewCfgRemPatternMatchGroup_Type()
)
fltNewCfgRemPatternMatchGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgRemPatternMatchGroup.setStatus("current")


class _FltNewCfg8021pBitsValue_Type(Integer32):
    """Custom type fltNewCfg8021pBitsValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FltNewCfg8021pBitsValue_Type.__name__ = "Integer32"
_FltNewCfg8021pBitsValue_Object = MibTableColumn
fltNewCfg8021pBitsValue = _FltNewCfg8021pBitsValue_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 68),
    _FltNewCfg8021pBitsValue_Type()
)
fltNewCfg8021pBitsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfg8021pBitsValue.setStatus("current")


class _FltNewCfg8021pBitsMatch_Type(Integer32):
    """Custom type fltNewCfg8021pBitsMatch based on Integer32"""
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


_FltNewCfg8021pBitsMatch_Type.__name__ = "Integer32"
_FltNewCfg8021pBitsMatch_Object = MibTableColumn
fltNewCfg8021pBitsMatch = _FltNewCfg8021pBitsMatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 69),
    _FltNewCfg8021pBitsMatch_Type()
)
fltNewCfg8021pBitsMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfg8021pBitsMatch.setStatus("current")


class _FltNewCfgAclIpLength_Type(Integer32):
    """Custom type fltNewCfgAclIpLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FltNewCfgAclIpLength_Type.__name__ = "Integer32"
_FltNewCfgAclIpLength_Object = MibTableColumn
fltNewCfgAclIpLength = _FltNewCfgAclIpLength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 70),
    _FltNewCfgAclIpLength_Type()
)
fltNewCfgAclIpLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgAclIpLength.setStatus("current")
_FltNewCfgIdsGroup_Type = Integer32
_FltNewCfgIdsGroup_Object = MibTableColumn
fltNewCfgIdsGroup = _FltNewCfgIdsGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 71),
    _FltNewCfgIdsGroup_Type()
)
fltNewCfgIdsGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgIdsGroup.setStatus("current")


class _FltNewCfgEgressPip_Type(Integer32):
    """Custom type fltNewCfgEgressPip based on Integer32"""
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


_FltNewCfgEgressPip_Type.__name__ = "Integer32"
_FltNewCfgEgressPip_Object = MibTableColumn
fltNewCfgEgressPip = _FltNewCfgEgressPip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 72),
    _FltNewCfgEgressPip_Type()
)
fltNewCfgEgressPip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgEgressPip.setStatus("current")


class _FltNewCfgDbind_Type(Integer32):
    """Custom type fltNewCfgDbind based on Integer32"""
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


_FltNewCfgDbind_Type.__name__ = "Integer32"
_FltNewCfgDbind_Object = MibTableColumn
fltNewCfgDbind = _FltNewCfgDbind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 73),
    _FltNewCfgDbind_Type()
)
fltNewCfgDbind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgDbind.setStatus("current")
_FltNewCfgRevBwmContract_Type = Integer32
_FltNewCfgRevBwmContract_Object = MibTableColumn
fltNewCfgRevBwmContract = _FltNewCfgRevBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 74),
    _FltNewCfgRevBwmContract_Type()
)
fltNewCfgRevBwmContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgRevBwmContract.setStatus("current")


class _FltNewCfgReverse_Type(Integer32):
    """Custom type fltNewCfgReverse based on Integer32"""
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


_FltNewCfgReverse_Type.__name__ = "Integer32"
_FltNewCfgReverse_Object = MibTableColumn
fltNewCfgReverse = _FltNewCfgReverse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 75),
    _FltNewCfgReverse_Type()
)
fltNewCfgReverse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgReverse.setStatus("current")


class _FltNewCfgParseChn_Type(Integer32):
    """Custom type fltNewCfgParseChn based on Integer32"""
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


_FltNewCfgParseChn_Type.__name__ = "Integer32"
_FltNewCfgParseChn_Object = MibTableColumn
fltNewCfgParseChn = _FltNewCfgParseChn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 76),
    _FltNewCfgParseChn_Type()
)
fltNewCfgParseChn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgParseChn.setStatus("current")
_FltNewCfgRtpBwmContract_Type = Integer32
_FltNewCfgRtpBwmContract_Object = MibTableColumn
fltNewCfgRtpBwmContract = _FltNewCfgRtpBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 77),
    _FltNewCfgRtpBwmContract_Type()
)
fltNewCfgRtpBwmContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgRtpBwmContract.setStatus("current")


class _FltNewCfgSipParsing_Type(Integer32):
    """Custom type fltNewCfgSipParsing based on Integer32"""
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


_FltNewCfgSipParsing_Type.__name__ = "Integer32"
_FltNewCfgSipParsing_Object = MibTableColumn
fltNewCfgSipParsing = _FltNewCfgSipParsing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 78),
    _FltNewCfgSipParsing_Type()
)
fltNewCfgSipParsing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgSipParsing.setStatus("current")


class _FltNewCfgSessionMirror_Type(Integer32):
    """Custom type fltNewCfgSessionMirror based on Integer32"""
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


_FltNewCfgSessionMirror_Type.__name__ = "Integer32"
_FltNewCfgSessionMirror_Object = MibTableColumn
fltNewCfgSessionMirror = _FltNewCfgSessionMirror_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 79),
    _FltNewCfgSessionMirror_Type()
)
fltNewCfgSessionMirror.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgSessionMirror.setStatus("current")


class _FltNewCfgIpVer_Type(Integer32):
    """Custom type fltNewCfgIpVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_FltNewCfgIpVer_Type.__name__ = "Integer32"
_FltNewCfgIpVer_Object = MibTableColumn
fltNewCfgIpVer = _FltNewCfgIpVer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 80),
    _FltNewCfgIpVer_Type()
)
fltNewCfgIpVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgIpVer.setStatus("current")


class _FltNewCfgIpv6Sip_Type(DisplayString):
    """Custom type fltNewCfgIpv6Sip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FltNewCfgIpv6Sip_Type.__name__ = "DisplayString"
_FltNewCfgIpv6Sip_Object = MibTableColumn
fltNewCfgIpv6Sip = _FltNewCfgIpv6Sip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 81),
    _FltNewCfgIpv6Sip_Type()
)
fltNewCfgIpv6Sip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgIpv6Sip.setStatus("current")


class _FltNewCfgIpv6Sprefix_Type(Integer32):
    """Custom type fltNewCfgIpv6Sprefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FltNewCfgIpv6Sprefix_Type.__name__ = "Integer32"
_FltNewCfgIpv6Sprefix_Object = MibTableColumn
fltNewCfgIpv6Sprefix = _FltNewCfgIpv6Sprefix_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 82),
    _FltNewCfgIpv6Sprefix_Type()
)
fltNewCfgIpv6Sprefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgIpv6Sprefix.setStatus("current")


class _FltNewCfgIpv6Dip_Type(DisplayString):
    """Custom type fltNewCfgIpv6Dip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FltNewCfgIpv6Dip_Type.__name__ = "DisplayString"
_FltNewCfgIpv6Dip_Object = MibTableColumn
fltNewCfgIpv6Dip = _FltNewCfgIpv6Dip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 83),
    _FltNewCfgIpv6Dip_Type()
)
fltNewCfgIpv6Dip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgIpv6Dip.setStatus("current")


class _FltNewCfgIpv6Dprefix_Type(Integer32):
    """Custom type fltNewCfgIpv6Dprefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FltNewCfgIpv6Dprefix_Type.__name__ = "Integer32"
_FltNewCfgIpv6Dprefix_Object = MibTableColumn
fltNewCfgIpv6Dprefix = _FltNewCfgIpv6Dprefix_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 3, 1, 84),
    _FltNewCfgIpv6Dprefix_Type()
)
fltNewCfgIpv6Dprefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgIpv6Dprefix.setStatus("current")
_FltCurCfgPortTable_Object = MibTable
fltCurCfgPortTable = _FltCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 4)
)
if mibBuilder.loadTexts:
    fltCurCfgPortTable.setStatus("current")
_FltCurCfgPortTableEntry_Object = MibTableRow
fltCurCfgPortTableEntry = _FltCurCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 4, 1)
)
fltCurCfgPortTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "fltCurCfgPortIndx"),
)
if mibBuilder.loadTexts:
    fltCurCfgPortTableEntry.setStatus("current")
_FltCurCfgPortIndx_Type = Integer32
_FltCurCfgPortIndx_Object = MibTableColumn
fltCurCfgPortIndx = _FltCurCfgPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 4, 1, 1),
    _FltCurCfgPortIndx_Type()
)
fltCurCfgPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgPortIndx.setStatus("current")


class _FltCurCfgPortState_Type(Integer32):
    """Custom type fltCurCfgPortState based on Integer32"""
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


_FltCurCfgPortState_Type.__name__ = "Integer32"
_FltCurCfgPortState_Object = MibTableColumn
fltCurCfgPortState = _FltCurCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 4, 1, 2),
    _FltCurCfgPortState_Type()
)
fltCurCfgPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgPortState.setStatus("current")


class _FltCurCfgPortFiltBmap_Type(OctetString):
    """Custom type fltCurCfgPortFiltBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FltCurCfgPortFiltBmap_Type.__name__ = "OctetString"
_FltCurCfgPortFiltBmap_Object = MibTableColumn
fltCurCfgPortFiltBmap = _FltCurCfgPortFiltBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 4, 1, 3),
    _FltCurCfgPortFiltBmap_Type()
)
fltCurCfgPortFiltBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgPortFiltBmap.setStatus("current")
_FltNewCfgPortTable_Object = MibTable
fltNewCfgPortTable = _FltNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 5)
)
if mibBuilder.loadTexts:
    fltNewCfgPortTable.setStatus("current")
_FltNewCfgPortTableEntry_Object = MibTableRow
fltNewCfgPortTableEntry = _FltNewCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 5, 1)
)
fltNewCfgPortTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "fltNewCfgPortIndx"),
)
if mibBuilder.loadTexts:
    fltNewCfgPortTableEntry.setStatus("current")
_FltNewCfgPortIndx_Type = Integer32
_FltNewCfgPortIndx_Object = MibTableColumn
fltNewCfgPortIndx = _FltNewCfgPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 5, 1, 1),
    _FltNewCfgPortIndx_Type()
)
fltNewCfgPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgPortIndx.setStatus("current")


class _FltNewCfgPortState_Type(Integer32):
    """Custom type fltNewCfgPortState based on Integer32"""
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


_FltNewCfgPortState_Type.__name__ = "Integer32"
_FltNewCfgPortState_Object = MibTableColumn
fltNewCfgPortState = _FltNewCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 5, 1, 2),
    _FltNewCfgPortState_Type()
)
fltNewCfgPortState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgPortState.setStatus("current")


class _FltNewCfgPortFiltBmap_Type(OctetString):
    """Custom type fltNewCfgPortFiltBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FltNewCfgPortFiltBmap_Type.__name__ = "OctetString"
_FltNewCfgPortFiltBmap_Object = MibTableColumn
fltNewCfgPortFiltBmap = _FltNewCfgPortFiltBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 5, 1, 3),
    _FltNewCfgPortFiltBmap_Type()
)
fltNewCfgPortFiltBmap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgPortFiltBmap.setStatus("current")
_FltNewCfgPortAddFiltRule_Type = Integer32
_FltNewCfgPortAddFiltRule_Object = MibTableColumn
fltNewCfgPortAddFiltRule = _FltNewCfgPortAddFiltRule_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 5, 1, 4),
    _FltNewCfgPortAddFiltRule_Type()
)
fltNewCfgPortAddFiltRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgPortAddFiltRule.setStatus("current")
_FltNewCfgPortRemFiltRule_Type = Integer32
_FltNewCfgPortRemFiltRule_Object = MibTableColumn
fltNewCfgPortRemFiltRule = _FltNewCfgPortRemFiltRule_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 5, 1, 5),
    _FltNewCfgPortRemFiltRule_Type()
)
fltNewCfgPortRemFiltRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgPortRemFiltRule.setStatus("current")
_FltUrlBwmTableMaxSize_Type = Integer32
_FltUrlBwmTableMaxSize_Object = MibScalar
fltUrlBwmTableMaxSize = _FltUrlBwmTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 6),
    _FltUrlBwmTableMaxSize_Type()
)
fltUrlBwmTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltUrlBwmTableMaxSize.setStatus("current")
_FltCurCfgUrlBwmTable_Object = MibTable
fltCurCfgUrlBwmTable = _FltCurCfgUrlBwmTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 7)
)
if mibBuilder.loadTexts:
    fltCurCfgUrlBwmTable.setStatus("current")
_FltCurCfgUrlBwmEntry_Object = MibTableRow
fltCurCfgUrlBwmEntry = _FltCurCfgUrlBwmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 7, 1)
)
fltCurCfgUrlBwmEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "fltCurCfgUrlBwmFltIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "fltCurCfgUrlBwmUrlId"),
)
if mibBuilder.loadTexts:
    fltCurCfgUrlBwmEntry.setStatus("current")
_FltCurCfgUrlBwmFltIndex_Type = Integer32
_FltCurCfgUrlBwmFltIndex_Object = MibTableColumn
fltCurCfgUrlBwmFltIndex = _FltCurCfgUrlBwmFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 7, 1, 1),
    _FltCurCfgUrlBwmFltIndex_Type()
)
fltCurCfgUrlBwmFltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgUrlBwmFltIndex.setStatus("current")
_FltCurCfgUrlBwmUrlId_Type = Integer32
_FltCurCfgUrlBwmUrlId_Object = MibTableColumn
fltCurCfgUrlBwmUrlId = _FltCurCfgUrlBwmUrlId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 7, 1, 2),
    _FltCurCfgUrlBwmUrlId_Type()
)
fltCurCfgUrlBwmUrlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgUrlBwmUrlId.setStatus("current")
_FltCurCfgUrlBwmContract_Type = Integer32
_FltCurCfgUrlBwmContract_Object = MibTableColumn
fltCurCfgUrlBwmContract = _FltCurCfgUrlBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 7, 1, 3),
    _FltCurCfgUrlBwmContract_Type()
)
fltCurCfgUrlBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgUrlBwmContract.setStatus("current")
_FltCurCfgUrlReverseBwmContract_Type = Integer32
_FltCurCfgUrlReverseBwmContract_Object = MibTableColumn
fltCurCfgUrlReverseBwmContract = _FltCurCfgUrlReverseBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 7, 1, 4),
    _FltCurCfgUrlReverseBwmContract_Type()
)
fltCurCfgUrlReverseBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgUrlReverseBwmContract.setStatus("current")
_FltNewCfgUrlBwmTable_Object = MibTable
fltNewCfgUrlBwmTable = _FltNewCfgUrlBwmTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 8)
)
if mibBuilder.loadTexts:
    fltNewCfgUrlBwmTable.setStatus("current")
_FltNewCfgUrlBwmEntry_Object = MibTableRow
fltNewCfgUrlBwmEntry = _FltNewCfgUrlBwmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 8, 1)
)
fltNewCfgUrlBwmEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "fltNewCfgUrlBwmFltIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "fltNewCfgUrlBwmUrlId"),
)
if mibBuilder.loadTexts:
    fltNewCfgUrlBwmEntry.setStatus("current")
_FltNewCfgUrlBwmFltIndex_Type = Integer32
_FltNewCfgUrlBwmFltIndex_Object = MibTableColumn
fltNewCfgUrlBwmFltIndex = _FltNewCfgUrlBwmFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 8, 1, 1),
    _FltNewCfgUrlBwmFltIndex_Type()
)
fltNewCfgUrlBwmFltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgUrlBwmFltIndex.setStatus("current")
_FltNewCfgUrlBwmUrlId_Type = Integer32
_FltNewCfgUrlBwmUrlId_Object = MibTableColumn
fltNewCfgUrlBwmUrlId = _FltNewCfgUrlBwmUrlId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 8, 1, 2),
    _FltNewCfgUrlBwmUrlId_Type()
)
fltNewCfgUrlBwmUrlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgUrlBwmUrlId.setStatus("current")
_FltNewCfgUrlBwmContract_Type = Integer32
_FltNewCfgUrlBwmContract_Object = MibTableColumn
fltNewCfgUrlBwmContract = _FltNewCfgUrlBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 8, 1, 3),
    _FltNewCfgUrlBwmContract_Type()
)
fltNewCfgUrlBwmContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgUrlBwmContract.setStatus("current")


class _FltNewCfgUrlBwmDelete_Type(Integer32):
    """Custom type fltNewCfgUrlBwmDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_FltNewCfgUrlBwmDelete_Type.__name__ = "Integer32"
_FltNewCfgUrlBwmDelete_Object = MibTableColumn
fltNewCfgUrlBwmDelete = _FltNewCfgUrlBwmDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 8, 1, 4),
    _FltNewCfgUrlBwmDelete_Type()
)
fltNewCfgUrlBwmDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgUrlBwmDelete.setStatus("current")
_FltNewCfgUrlReverseBwmContract_Type = Integer32
_FltNewCfgUrlReverseBwmContract_Object = MibTableColumn
fltNewCfgUrlReverseBwmContract = _FltNewCfgUrlReverseBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 8, 1, 5),
    _FltNewCfgUrlReverseBwmContract_Type()
)
fltNewCfgUrlReverseBwmContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgUrlReverseBwmContract.setStatus("current")
_FltCfgHttpRedirMappingTableMaxSize_Type = Integer32
_FltCfgHttpRedirMappingTableMaxSize_Object = MibScalar
fltCfgHttpRedirMappingTableMaxSize = _FltCfgHttpRedirMappingTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 9),
    _FltCfgHttpRedirMappingTableMaxSize_Type()
)
fltCfgHttpRedirMappingTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCfgHttpRedirMappingTableMaxSize.setStatus("current")
_FltCurCfgHttpRedirMappingTable_Object = MibTable
fltCurCfgHttpRedirMappingTable = _FltCurCfgHttpRedirMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 10)
)
if mibBuilder.loadTexts:
    fltCurCfgHttpRedirMappingTable.setStatus("current")
_FltCurCfgHttpRedirMappingEntry_Object = MibTableRow
fltCurCfgHttpRedirMappingEntry = _FltCurCfgHttpRedirMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 10, 1)
)
fltCurCfgHttpRedirMappingEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "fltCurCfgHttpRedirMappingFilter"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "fltCurCfgHttpRedirMappingFromStr"),
)
if mibBuilder.loadTexts:
    fltCurCfgHttpRedirMappingEntry.setStatus("current")
_FltCurCfgHttpRedirMappingFilter_Type = Integer32
_FltCurCfgHttpRedirMappingFilter_Object = MibTableColumn
fltCurCfgHttpRedirMappingFilter = _FltCurCfgHttpRedirMappingFilter_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 10, 1, 1),
    _FltCurCfgHttpRedirMappingFilter_Type()
)
fltCurCfgHttpRedirMappingFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgHttpRedirMappingFilter.setStatus("current")


class _FltCurCfgHttpRedirMappingFromStr_Type(Integer32):
    """Custom type fltCurCfgHttpRedirMappingFromStr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FltCurCfgHttpRedirMappingFromStr_Type.__name__ = "Integer32"
_FltCurCfgHttpRedirMappingFromStr_Object = MibTableColumn
fltCurCfgHttpRedirMappingFromStr = _FltCurCfgHttpRedirMappingFromStr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 10, 1, 2),
    _FltCurCfgHttpRedirMappingFromStr_Type()
)
fltCurCfgHttpRedirMappingFromStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgHttpRedirMappingFromStr.setStatus("current")


class _FltCurCfgHttpRedirMappingToStr_Type(Integer32):
    """Custom type fltCurCfgHttpRedirMappingToStr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_FltCurCfgHttpRedirMappingToStr_Type.__name__ = "Integer32"
_FltCurCfgHttpRedirMappingToStr_Object = MibTableColumn
fltCurCfgHttpRedirMappingToStr = _FltCurCfgHttpRedirMappingToStr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 10, 1, 3),
    _FltCurCfgHttpRedirMappingToStr_Type()
)
fltCurCfgHttpRedirMappingToStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgHttpRedirMappingToStr.setStatus("current")
_FltNewCfgHttpRedirMappingTable_Object = MibTable
fltNewCfgHttpRedirMappingTable = _FltNewCfgHttpRedirMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 11)
)
if mibBuilder.loadTexts:
    fltNewCfgHttpRedirMappingTable.setStatus("current")
_FltNewCfgHttpRedirMappingEntry_Object = MibTableRow
fltNewCfgHttpRedirMappingEntry = _FltNewCfgHttpRedirMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 11, 1)
)
fltNewCfgHttpRedirMappingEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "fltNewCfgHttpRedirMappingFilter"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "fltNewCfgHttpRedirMappingFromStr"),
)
if mibBuilder.loadTexts:
    fltNewCfgHttpRedirMappingEntry.setStatus("current")
_FltNewCfgHttpRedirMappingFilter_Type = Integer32
_FltNewCfgHttpRedirMappingFilter_Object = MibTableColumn
fltNewCfgHttpRedirMappingFilter = _FltNewCfgHttpRedirMappingFilter_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 11, 1, 1),
    _FltNewCfgHttpRedirMappingFilter_Type()
)
fltNewCfgHttpRedirMappingFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgHttpRedirMappingFilter.setStatus("current")


class _FltNewCfgHttpRedirMappingFromStr_Type(Integer32):
    """Custom type fltNewCfgHttpRedirMappingFromStr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FltNewCfgHttpRedirMappingFromStr_Type.__name__ = "Integer32"
_FltNewCfgHttpRedirMappingFromStr_Object = MibTableColumn
fltNewCfgHttpRedirMappingFromStr = _FltNewCfgHttpRedirMappingFromStr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 11, 1, 2),
    _FltNewCfgHttpRedirMappingFromStr_Type()
)
fltNewCfgHttpRedirMappingFromStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgHttpRedirMappingFromStr.setStatus("current")


class _FltNewCfgHttpRedirMappingToStr_Type(Integer32):
    """Custom type fltNewCfgHttpRedirMappingToStr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_FltNewCfgHttpRedirMappingToStr_Type.__name__ = "Integer32"
_FltNewCfgHttpRedirMappingToStr_Object = MibTableColumn
fltNewCfgHttpRedirMappingToStr = _FltNewCfgHttpRedirMappingToStr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 11, 1, 4),
    _FltNewCfgHttpRedirMappingToStr_Type()
)
fltNewCfgHttpRedirMappingToStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgHttpRedirMappingToStr.setStatus("current")


class _FltNewCfgHttpRedirMappingDelete_Type(Integer32):
    """Custom type fltNewCfgHttpRedirMappingDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_FltNewCfgHttpRedirMappingDelete_Type.__name__ = "Integer32"
_FltNewCfgHttpRedirMappingDelete_Object = MibTableColumn
fltNewCfgHttpRedirMappingDelete = _FltNewCfgHttpRedirMappingDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 2, 11, 1, 6),
    _FltNewCfgHttpRedirMappingDelete_Type()
)
fltNewCfgHttpRedirMappingDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fltNewCfgHttpRedirMappingDelete.setStatus("current")
_GslbCfg_ObjectIdentity = ObjectIdentity
gslbCfg = _GslbCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3)
)
_GslbGeneralCfg_ObjectIdentity = ObjectIdentity
gslbGeneralCfg = _GslbGeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1)
)


class _GslbCurCfgGenState_Type(Integer32):
    """Custom type gslbCurCfgGenState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_GslbCurCfgGenState_Type.__name__ = "Integer32"
_GslbCurCfgGenState_Object = MibScalar
gslbCurCfgGenState = _GslbCurCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 1),
    _GslbCurCfgGenState_Type()
)
gslbCurCfgGenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenState.setStatus("current")


class _GslbNewCfgGenState_Type(Integer32):
    """Custom type gslbNewCfgGenState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_GslbNewCfgGenState_Type.__name__ = "Integer32"
_GslbNewCfgGenState_Object = MibScalar
gslbNewCfgGenState = _GslbNewCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 2),
    _GslbNewCfgGenState_Type()
)
gslbNewCfgGenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenState.setStatus("current")


class _GslbCurCfgGenHttpRedirect_Type(Integer32):
    """Custom type gslbCurCfgGenHttpRedirect based on Integer32"""
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


_GslbCurCfgGenHttpRedirect_Type.__name__ = "Integer32"
_GslbCurCfgGenHttpRedirect_Object = MibScalar
gslbCurCfgGenHttpRedirect = _GslbCurCfgGenHttpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 7),
    _GslbCurCfgGenHttpRedirect_Type()
)
gslbCurCfgGenHttpRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenHttpRedirect.setStatus("current")


class _GslbNewCfgGenHttpRedirect_Type(Integer32):
    """Custom type gslbNewCfgGenHttpRedirect based on Integer32"""
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


_GslbNewCfgGenHttpRedirect_Type.__name__ = "Integer32"
_GslbNewCfgGenHttpRedirect_Object = MibScalar
gslbNewCfgGenHttpRedirect = _GslbNewCfgGenHttpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 8),
    _GslbNewCfgGenHttpRedirect_Type()
)
gslbNewCfgGenHttpRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenHttpRedirect.setStatus("current")


class _GslbCurCfgGenMinco_Type(Integer32):
    """Custom type gslbCurCfgGenMinco based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GslbCurCfgGenMinco_Type.__name__ = "Integer32"
_GslbCurCfgGenMinco_Object = MibScalar
gslbCurCfgGenMinco = _GslbCurCfgGenMinco_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 13),
    _GslbCurCfgGenMinco_Type()
)
gslbCurCfgGenMinco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenMinco.setStatus("current")


class _GslbNewCfgGenMinco_Type(Integer32):
    """Custom type gslbNewCfgGenMinco based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GslbNewCfgGenMinco_Type.__name__ = "Integer32"
_GslbNewCfgGenMinco_Object = MibScalar
gslbNewCfgGenMinco = _GslbNewCfgGenMinco_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 14),
    _GslbNewCfgGenMinco_Type()
)
gslbNewCfgGenMinco.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenMinco.setStatus("current")


class _GslbCurCfgGenUsern_Type(Integer32):
    """Custom type gslbCurCfgGenUsern based on Integer32"""
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


_GslbCurCfgGenUsern_Type.__name__ = "Integer32"
_GslbCurCfgGenUsern_Object = MibScalar
gslbCurCfgGenUsern = _GslbCurCfgGenUsern_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 17),
    _GslbCurCfgGenUsern_Type()
)
gslbCurCfgGenUsern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenUsern.setStatus("current")


class _GslbNewCfgGenUsern_Type(Integer32):
    """Custom type gslbNewCfgGenUsern based on Integer32"""
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


_GslbNewCfgGenUsern_Type.__name__ = "Integer32"
_GslbNewCfgGenUsern_Object = MibScalar
gslbNewCfgGenUsern = _GslbNewCfgGenUsern_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 18),
    _GslbNewCfgGenUsern_Type()
)
gslbNewCfgGenUsern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenUsern.setStatus("current")


class _GslbCurCfgGenNoremote_Type(Integer32):
    """Custom type gslbCurCfgGenNoremote based on Integer32"""
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


_GslbCurCfgGenNoremote_Type.__name__ = "Integer32"
_GslbCurCfgGenNoremote_Object = MibScalar
gslbCurCfgGenNoremote = _GslbCurCfgGenNoremote_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 25),
    _GslbCurCfgGenNoremote_Type()
)
gslbCurCfgGenNoremote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenNoremote.setStatus("current")


class _GslbNewCfgGenNoremote_Type(Integer32):
    """Custom type gslbNewCfgGenNoremote based on Integer32"""
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


_GslbNewCfgGenNoremote_Type.__name__ = "Integer32"
_GslbNewCfgGenNoremote_Object = MibScalar
gslbNewCfgGenNoremote = _GslbNewCfgGenNoremote_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 26),
    _GslbNewCfgGenNoremote_Type()
)
gslbNewCfgGenNoremote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenNoremote.setStatus("current")


class _GslbCurCfgGenEncrypt_Type(Integer32):
    """Custom type gslbCurCfgGenEncrypt based on Integer32"""
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


_GslbCurCfgGenEncrypt_Type.__name__ = "Integer32"
_GslbCurCfgGenEncrypt_Object = MibScalar
gslbCurCfgGenEncrypt = _GslbCurCfgGenEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 27),
    _GslbCurCfgGenEncrypt_Type()
)
gslbCurCfgGenEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenEncrypt.setStatus("current")


class _GslbNewCfgGenEncrypt_Type(Integer32):
    """Custom type gslbNewCfgGenEncrypt based on Integer32"""
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


_GslbNewCfgGenEncrypt_Type.__name__ = "Integer32"
_GslbNewCfgGenEncrypt_Object = MibScalar
gslbNewCfgGenEncrypt = _GslbNewCfgGenEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 28),
    _GslbNewCfgGenEncrypt_Type()
)
gslbNewCfgGenEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenEncrypt.setStatus("current")


class _GslbCurCfgGenRemSiteUpdatePort_Type(Integer32):
    """Custom type gslbCurCfgGenRemSiteUpdatePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GslbCurCfgGenRemSiteUpdatePort_Type.__name__ = "Integer32"
_GslbCurCfgGenRemSiteUpdatePort_Object = MibScalar
gslbCurCfgGenRemSiteUpdatePort = _GslbCurCfgGenRemSiteUpdatePort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 29),
    _GslbCurCfgGenRemSiteUpdatePort_Type()
)
gslbCurCfgGenRemSiteUpdatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenRemSiteUpdatePort.setStatus("current")


class _GslbNewCfgGenRemSiteUpdatePort_Type(Integer32):
    """Custom type gslbNewCfgGenRemSiteUpdatePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GslbNewCfgGenRemSiteUpdatePort_Type.__name__ = "Integer32"
_GslbNewCfgGenRemSiteUpdatePort_Object = MibScalar
gslbNewCfgGenRemSiteUpdatePort = _GslbNewCfgGenRemSiteUpdatePort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 30),
    _GslbNewCfgGenRemSiteUpdatePort_Type()
)
gslbNewCfgGenRemSiteUpdatePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenRemSiteUpdatePort.setStatus("current")


class _GslbCurCfgGenSessUtilCap_Type(Integer32):
    """Custom type gslbCurCfgGenSessUtilCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_GslbCurCfgGenSessUtilCap_Type.__name__ = "Integer32"
_GslbCurCfgGenSessUtilCap_Object = MibScalar
gslbCurCfgGenSessUtilCap = _GslbCurCfgGenSessUtilCap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 31),
    _GslbCurCfgGenSessUtilCap_Type()
)
gslbCurCfgGenSessUtilCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenSessUtilCap.setStatus("current")


class _GslbNewCfgGenSessUtilCap_Type(Integer32):
    """Custom type gslbNewCfgGenSessUtilCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_GslbNewCfgGenSessUtilCap_Type.__name__ = "Integer32"
_GslbNewCfgGenSessUtilCap_Object = MibScalar
gslbNewCfgGenSessUtilCap = _GslbNewCfgGenSessUtilCap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 32),
    _GslbNewCfgGenSessUtilCap_Type()
)
gslbNewCfgGenSessUtilCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenSessUtilCap.setStatus("current")


class _GslbCurCfgGenCpuUtilCap_Type(Integer32):
    """Custom type gslbCurCfgGenCpuUtilCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_GslbCurCfgGenCpuUtilCap_Type.__name__ = "Integer32"
_GslbCurCfgGenCpuUtilCap_Object = MibScalar
gslbCurCfgGenCpuUtilCap = _GslbCurCfgGenCpuUtilCap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 33),
    _GslbCurCfgGenCpuUtilCap_Type()
)
gslbCurCfgGenCpuUtilCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenCpuUtilCap.setStatus("current")


class _GslbNewCfgGenCpuUtilCap_Type(Integer32):
    """Custom type gslbNewCfgGenCpuUtilCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_GslbNewCfgGenCpuUtilCap_Type.__name__ = "Integer32"
_GslbNewCfgGenCpuUtilCap_Object = MibScalar
gslbNewCfgGenCpuUtilCap = _GslbNewCfgGenCpuUtilCap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 34),
    _GslbNewCfgGenCpuUtilCap_Type()
)
gslbNewCfgGenCpuUtilCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenCpuUtilCap.setStatus("current")
_GslbCurCfgGenSourceIpNetmask_Type = IpAddress
_GslbCurCfgGenSourceIpNetmask_Object = MibScalar
gslbCurCfgGenSourceIpNetmask = _GslbCurCfgGenSourceIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 35),
    _GslbCurCfgGenSourceIpNetmask_Type()
)
gslbCurCfgGenSourceIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenSourceIpNetmask.setStatus("current")
_GslbNewCfgGenSourceIpNetmask_Type = IpAddress
_GslbNewCfgGenSourceIpNetmask_Object = MibScalar
gslbNewCfgGenSourceIpNetmask = _GslbNewCfgGenSourceIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 36),
    _GslbNewCfgGenSourceIpNetmask_Type()
)
gslbNewCfgGenSourceIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenSourceIpNetmask.setStatus("current")


class _GslbCurCfgGenTimeout_Type(Integer32):
    """Custom type gslbCurCfgGenTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_GslbCurCfgGenTimeout_Type.__name__ = "Integer32"
_GslbCurCfgGenTimeout_Object = MibScalar
gslbCurCfgGenTimeout = _GslbCurCfgGenTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 37),
    _GslbCurCfgGenTimeout_Type()
)
gslbCurCfgGenTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenTimeout.setStatus("current")


class _GslbNewCfgGenTimeout_Type(Integer32):
    """Custom type gslbNewCfgGenTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_GslbNewCfgGenTimeout_Type.__name__ = "Integer32"
_GslbNewCfgGenTimeout_Object = MibScalar
gslbNewCfgGenTimeout = _GslbNewCfgGenTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 38),
    _GslbNewCfgGenTimeout_Type()
)
gslbNewCfgGenTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenTimeout.setStatus("current")


class _GslbCurCfgGenDnsDirect_Type(Integer32):
    """Custom type gslbCurCfgGenDnsDirect based on Integer32"""
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


_GslbCurCfgGenDnsDirect_Type.__name__ = "Integer32"
_GslbCurCfgGenDnsDirect_Object = MibScalar
gslbCurCfgGenDnsDirect = _GslbCurCfgGenDnsDirect_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 39),
    _GslbCurCfgGenDnsDirect_Type()
)
gslbCurCfgGenDnsDirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenDnsDirect.setStatus("current")


class _GslbNewCfgGenDnsDirect_Type(Integer32):
    """Custom type gslbNewCfgGenDnsDirect based on Integer32"""
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


_GslbNewCfgGenDnsDirect_Type.__name__ = "Integer32"
_GslbNewCfgGenDnsDirect_Object = MibScalar
gslbNewCfgGenDnsDirect = _GslbNewCfgGenDnsDirect_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 40),
    _GslbNewCfgGenDnsDirect_Type()
)
gslbNewCfgGenDnsDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenDnsDirect.setStatus("current")


class _GslbCurCfgGenRemSiteUpdateVersion_Type(Integer32):
    """Custom type gslbCurCfgGenRemSiteUpdateVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GslbCurCfgGenRemSiteUpdateVersion_Type.__name__ = "Integer32"
_GslbCurCfgGenRemSiteUpdateVersion_Object = MibScalar
gslbCurCfgGenRemSiteUpdateVersion = _GslbCurCfgGenRemSiteUpdateVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 41),
    _GslbCurCfgGenRemSiteUpdateVersion_Type()
)
gslbCurCfgGenRemSiteUpdateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenRemSiteUpdateVersion.setStatus("current")


class _GslbNewCfgGenRemSiteUpdateVersion_Type(Integer32):
    """Custom type gslbNewCfgGenRemSiteUpdateVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GslbNewCfgGenRemSiteUpdateVersion_Type.__name__ = "Integer32"
_GslbNewCfgGenRemSiteUpdateVersion_Object = MibScalar
gslbNewCfgGenRemSiteUpdateVersion = _GslbNewCfgGenRemSiteUpdateVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 42),
    _GslbNewCfgGenRemSiteUpdateVersion_Type()
)
gslbNewCfgGenRemSiteUpdateVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenRemSiteUpdateVersion.setStatus("current")


class _GslbCurCfgGenHostname_Type(Integer32):
    """Custom type gslbCurCfgGenHostname based on Integer32"""
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


_GslbCurCfgGenHostname_Type.__name__ = "Integer32"
_GslbCurCfgGenHostname_Object = MibScalar
gslbCurCfgGenHostname = _GslbCurCfgGenHostname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 43),
    _GslbCurCfgGenHostname_Type()
)
gslbCurCfgGenHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenHostname.setStatus("current")


class _GslbNewCfgGenHostname_Type(Integer32):
    """Custom type gslbNewCfgGenHostname based on Integer32"""
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


_GslbNewCfgGenHostname_Type.__name__ = "Integer32"
_GslbNewCfgGenHostname_Object = MibScalar
gslbNewCfgGenHostname = _GslbNewCfgGenHostname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 44),
    _GslbNewCfgGenHostname_Type()
)
gslbNewCfgGenHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenHostname.setStatus("current")


class _GslbCurCfgGenRemSiteUpdateIntervalSeconds_Type(Integer32):
    """Custom type gslbCurCfgGenRemSiteUpdateIntervalSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 7200),
    )


_GslbCurCfgGenRemSiteUpdateIntervalSeconds_Type.__name__ = "Integer32"
_GslbCurCfgGenRemSiteUpdateIntervalSeconds_Object = MibScalar
gslbCurCfgGenRemSiteUpdateIntervalSeconds = _GslbCurCfgGenRemSiteUpdateIntervalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 45),
    _GslbCurCfgGenRemSiteUpdateIntervalSeconds_Type()
)
gslbCurCfgGenRemSiteUpdateIntervalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenRemSiteUpdateIntervalSeconds.setStatus("current")


class _GslbNewCfgGenRemSiteUpdateIntervalSeconds_Type(Integer32):
    """Custom type gslbNewCfgGenRemSiteUpdateIntervalSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 7200),
    )


_GslbNewCfgGenRemSiteUpdateIntervalSeconds_Type.__name__ = "Integer32"
_GslbNewCfgGenRemSiteUpdateIntervalSeconds_Object = MibScalar
gslbNewCfgGenRemSiteUpdateIntervalSeconds = _GslbNewCfgGenRemSiteUpdateIntervalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 46),
    _GslbNewCfgGenRemSiteUpdateIntervalSeconds_Type()
)
gslbNewCfgGenRemSiteUpdateIntervalSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenRemSiteUpdateIntervalSeconds.setStatus("current")


class _GslbCurCfgGenNoResp_Type(Integer32):
    """Custom type gslbCurCfgGenNoResp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_GslbCurCfgGenNoResp_Type.__name__ = "Integer32"
_GslbCurCfgGenNoResp_Object = MibScalar
gslbCurCfgGenNoResp = _GslbCurCfgGenNoResp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 47),
    _GslbCurCfgGenNoResp_Type()
)
gslbCurCfgGenNoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenNoResp.setStatus("current")


class _GslbNewCfgGenNoResp_Type(Integer32):
    """Custom type gslbNewCfgGenNoResp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_GslbNewCfgGenNoResp_Type.__name__ = "Integer32"
_GslbNewCfgGenNoResp_Object = MibScalar
gslbNewCfgGenNoResp = _GslbNewCfgGenNoResp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 1, 48),
    _GslbNewCfgGenNoResp_Type()
)
gslbNewCfgGenNoResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenNoResp.setStatus("current")
_GslbSitesCfg_ObjectIdentity = ObjectIdentity
gslbSitesCfg = _GslbSitesCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2)
)
_GslbRemSiteTableMaxSize_Type = Integer32
_GslbRemSiteTableMaxSize_Object = MibScalar
gslbRemSiteTableMaxSize = _GslbRemSiteTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 1),
    _GslbRemSiteTableMaxSize_Type()
)
gslbRemSiteTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbRemSiteTableMaxSize.setStatus("current")
_GslbCurCfgRemSiteTable_Object = MibTable
gslbCurCfgRemSiteTable = _GslbCurCfgRemSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteTable.setStatus("current")
_GslbCurCfgRemSiteTableEntry_Object = MibTableRow
gslbCurCfgRemSiteTableEntry = _GslbCurCfgRemSiteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 2, 1)
)
gslbCurCfgRemSiteTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbCurCfgRemSiteIndx"),
)
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteTableEntry.setStatus("current")
_GslbCurCfgRemSiteIndx_Type = Integer32
_GslbCurCfgRemSiteIndx_Object = MibTableColumn
gslbCurCfgRemSiteIndx = _GslbCurCfgRemSiteIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 2, 1, 1),
    _GslbCurCfgRemSiteIndx_Type()
)
gslbCurCfgRemSiteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteIndx.setStatus("current")
_GslbCurCfgRemSitePrimaryIp_Type = IpAddress
_GslbCurCfgRemSitePrimaryIp_Object = MibTableColumn
gslbCurCfgRemSitePrimaryIp = _GslbCurCfgRemSitePrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 2, 1, 2),
    _GslbCurCfgRemSitePrimaryIp_Type()
)
gslbCurCfgRemSitePrimaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSitePrimaryIp.setStatus("current")
_GslbCurCfgRemSiteSecondaryIp_Type = IpAddress
_GslbCurCfgRemSiteSecondaryIp_Object = MibTableColumn
gslbCurCfgRemSiteSecondaryIp = _GslbCurCfgRemSiteSecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 2, 1, 3),
    _GslbCurCfgRemSiteSecondaryIp_Type()
)
gslbCurCfgRemSiteSecondaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteSecondaryIp.setStatus("current")


class _GslbCurCfgRemSiteState_Type(Integer32):
    """Custom type gslbCurCfgRemSiteState based on Integer32"""
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


_GslbCurCfgRemSiteState_Type.__name__ = "Integer32"
_GslbCurCfgRemSiteState_Object = MibTableColumn
gslbCurCfgRemSiteState = _GslbCurCfgRemSiteState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 2, 1, 4),
    _GslbCurCfgRemSiteState_Type()
)
gslbCurCfgRemSiteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteState.setStatus("current")


class _GslbCurCfgRemSiteUpdate_Type(Integer32):
    """Custom type gslbCurCfgRemSiteUpdate based on Integer32"""
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


_GslbCurCfgRemSiteUpdate_Type.__name__ = "Integer32"
_GslbCurCfgRemSiteUpdate_Object = MibTableColumn
gslbCurCfgRemSiteUpdate = _GslbCurCfgRemSiteUpdate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 2, 1, 5),
    _GslbCurCfgRemSiteUpdate_Type()
)
gslbCurCfgRemSiteUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteUpdate.setStatus("current")


class _GslbCurCfgRemSiteName_Type(DisplayString):
    """Custom type gslbCurCfgRemSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GslbCurCfgRemSiteName_Type.__name__ = "DisplayString"
_GslbCurCfgRemSiteName_Object = MibTableColumn
gslbCurCfgRemSiteName = _GslbCurCfgRemSiteName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 2, 1, 6),
    _GslbCurCfgRemSiteName_Type()
)
gslbCurCfgRemSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteName.setStatus("current")
_GslbNewCfgRemSiteTable_Object = MibTable
gslbNewCfgRemSiteTable = _GslbNewCfgRemSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteTable.setStatus("current")
_GslbNewCfgRemSiteTableEntry_Object = MibTableRow
gslbNewCfgRemSiteTableEntry = _GslbNewCfgRemSiteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 3, 1)
)
gslbNewCfgRemSiteTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbNewCfgRemSiteIndx"),
)
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteTableEntry.setStatus("current")
_GslbNewCfgRemSiteIndx_Type = Integer32
_GslbNewCfgRemSiteIndx_Object = MibTableColumn
gslbNewCfgRemSiteIndx = _GslbNewCfgRemSiteIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 3, 1, 1),
    _GslbNewCfgRemSiteIndx_Type()
)
gslbNewCfgRemSiteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteIndx.setStatus("current")
_GslbNewCfgRemSitePrimaryIp_Type = IpAddress
_GslbNewCfgRemSitePrimaryIp_Object = MibTableColumn
gslbNewCfgRemSitePrimaryIp = _GslbNewCfgRemSitePrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 3, 1, 2),
    _GslbNewCfgRemSitePrimaryIp_Type()
)
gslbNewCfgRemSitePrimaryIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgRemSitePrimaryIp.setStatus("current")
_GslbNewCfgRemSiteSecondaryIp_Type = IpAddress
_GslbNewCfgRemSiteSecondaryIp_Object = MibTableColumn
gslbNewCfgRemSiteSecondaryIp = _GslbNewCfgRemSiteSecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 3, 1, 3),
    _GslbNewCfgRemSiteSecondaryIp_Type()
)
gslbNewCfgRemSiteSecondaryIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteSecondaryIp.setStatus("current")


class _GslbNewCfgRemSiteState_Type(Integer32):
    """Custom type gslbNewCfgRemSiteState based on Integer32"""
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


_GslbNewCfgRemSiteState_Type.__name__ = "Integer32"
_GslbNewCfgRemSiteState_Object = MibTableColumn
gslbNewCfgRemSiteState = _GslbNewCfgRemSiteState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 3, 1, 4),
    _GslbNewCfgRemSiteState_Type()
)
gslbNewCfgRemSiteState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteState.setStatus("current")


class _GslbNewCfgRemSiteUpdate_Type(Integer32):
    """Custom type gslbNewCfgRemSiteUpdate based on Integer32"""
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


_GslbNewCfgRemSiteUpdate_Type.__name__ = "Integer32"
_GslbNewCfgRemSiteUpdate_Object = MibTableColumn
gslbNewCfgRemSiteUpdate = _GslbNewCfgRemSiteUpdate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 3, 1, 5),
    _GslbNewCfgRemSiteUpdate_Type()
)
gslbNewCfgRemSiteUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteUpdate.setStatus("current")


class _GslbNewCfgRemSiteDelete_Type(Integer32):
    """Custom type gslbNewCfgRemSiteDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_GslbNewCfgRemSiteDelete_Type.__name__ = "Integer32"
_GslbNewCfgRemSiteDelete_Object = MibTableColumn
gslbNewCfgRemSiteDelete = _GslbNewCfgRemSiteDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 3, 1, 6),
    _GslbNewCfgRemSiteDelete_Type()
)
gslbNewCfgRemSiteDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteDelete.setStatus("current")


class _GslbNewCfgRemSiteName_Type(DisplayString):
    """Custom type gslbNewCfgRemSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GslbNewCfgRemSiteName_Type.__name__ = "DisplayString"
_GslbNewCfgRemSiteName_Object = MibTableColumn
gslbNewCfgRemSiteName = _GslbNewCfgRemSiteName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 2, 3, 1, 7),
    _GslbNewCfgRemSiteName_Type()
)
gslbNewCfgRemSiteName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteName.setStatus("current")
_GslbEnhNetworkCfg_ObjectIdentity = ObjectIdentity
gslbEnhNetworkCfg = _GslbEnhNetworkCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4)
)
_GslbEnhNetworkTableMaxSize_Type = Integer32
_GslbEnhNetworkTableMaxSize_Object = MibScalar
gslbEnhNetworkTableMaxSize = _GslbEnhNetworkTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 1),
    _GslbEnhNetworkTableMaxSize_Type()
)
gslbEnhNetworkTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbEnhNetworkTableMaxSize.setStatus("current")
_GslbCurCfgEnhNetworkTable_Object = MibTable
gslbCurCfgEnhNetworkTable = _GslbCurCfgEnhNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    gslbCurCfgEnhNetworkTable.setStatus("current")
_GslbCurCfgEnhNetworkTableEntry_Object = MibTableRow
gslbCurCfgEnhNetworkTableEntry = _GslbCurCfgEnhNetworkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 2, 1)
)
gslbCurCfgEnhNetworkTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbCurCfgEnhNetworkIndx"),
)
if mibBuilder.loadTexts:
    gslbCurCfgEnhNetworkTableEntry.setStatus("current")
_GslbCurCfgEnhNetworkIndx_Type = Integer32
_GslbCurCfgEnhNetworkIndx_Object = MibTableColumn
gslbCurCfgEnhNetworkIndx = _GslbCurCfgEnhNetworkIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 2, 1, 1),
    _GslbCurCfgEnhNetworkIndx_Type()
)
gslbCurCfgEnhNetworkIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgEnhNetworkIndx.setStatus("current")


class _GslbCurCfgEnhNetworkState_Type(Integer32):
    """Custom type gslbCurCfgEnhNetworkState based on Integer32"""
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


_GslbCurCfgEnhNetworkState_Type.__name__ = "Integer32"
_GslbCurCfgEnhNetworkState_Object = MibTableColumn
gslbCurCfgEnhNetworkState = _GslbCurCfgEnhNetworkState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 2, 1, 2),
    _GslbCurCfgEnhNetworkState_Type()
)
gslbCurCfgEnhNetworkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgEnhNetworkState.setStatus("current")
_GslbCurCfgEnhNetworkSourceIp_Type = IpAddress
_GslbCurCfgEnhNetworkSourceIp_Object = MibTableColumn
gslbCurCfgEnhNetworkSourceIp = _GslbCurCfgEnhNetworkSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 2, 1, 3),
    _GslbCurCfgEnhNetworkSourceIp_Type()
)
gslbCurCfgEnhNetworkSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgEnhNetworkSourceIp.setStatus("current")
_GslbCurCfgEnhNetworkNetMask_Type = IpAddress
_GslbCurCfgEnhNetworkNetMask_Object = MibTableColumn
gslbCurCfgEnhNetworkNetMask = _GslbCurCfgEnhNetworkNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 2, 1, 4),
    _GslbCurCfgEnhNetworkNetMask_Type()
)
gslbCurCfgEnhNetworkNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgEnhNetworkNetMask.setStatus("current")
_GslbCurCfgEnhNetworkVirtServer_Type = OctetString
_GslbCurCfgEnhNetworkVirtServer_Object = MibTableColumn
gslbCurCfgEnhNetworkVirtServer = _GslbCurCfgEnhNetworkVirtServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 2, 1, 5),
    _GslbCurCfgEnhNetworkVirtServer_Type()
)
gslbCurCfgEnhNetworkVirtServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgEnhNetworkVirtServer.setStatus("current")
_GslbCurCfgEnhNetworkRemRealServer_Type = OctetString
_GslbCurCfgEnhNetworkRemRealServer_Object = MibTableColumn
gslbCurCfgEnhNetworkRemRealServer = _GslbCurCfgEnhNetworkRemRealServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 2, 1, 6),
    _GslbCurCfgEnhNetworkRemRealServer_Type()
)
gslbCurCfgEnhNetworkRemRealServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgEnhNetworkRemRealServer.setStatus("current")
_GslbNewCfgEnhNetworkTable_Object = MibTable
gslbNewCfgEnhNetworkTable = _GslbNewCfgEnhNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    gslbNewCfgEnhNetworkTable.setStatus("current")
_GslbNewCfgEnhNetworkTableEntry_Object = MibTableRow
gslbNewCfgEnhNetworkTableEntry = _GslbNewCfgEnhNetworkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 3, 1)
)
gslbNewCfgEnhNetworkTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbNewCfgEnhNetworkIndx"),
)
if mibBuilder.loadTexts:
    gslbNewCfgEnhNetworkTableEntry.setStatus("current")
_GslbNewCfgEnhNetworkIndx_Type = Integer32
_GslbNewCfgEnhNetworkIndx_Object = MibTableColumn
gslbNewCfgEnhNetworkIndx = _GslbNewCfgEnhNetworkIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 3, 1, 1),
    _GslbNewCfgEnhNetworkIndx_Type()
)
gslbNewCfgEnhNetworkIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbNewCfgEnhNetworkIndx.setStatus("current")


class _GslbNewCfgEnhNetworkState_Type(Integer32):
    """Custom type gslbNewCfgEnhNetworkState based on Integer32"""
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


_GslbNewCfgEnhNetworkState_Type.__name__ = "Integer32"
_GslbNewCfgEnhNetworkState_Object = MibTableColumn
gslbNewCfgEnhNetworkState = _GslbNewCfgEnhNetworkState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 3, 1, 2),
    _GslbNewCfgEnhNetworkState_Type()
)
gslbNewCfgEnhNetworkState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgEnhNetworkState.setStatus("current")
_GslbNewCfgEnhNetworkSourceIp_Type = IpAddress
_GslbNewCfgEnhNetworkSourceIp_Object = MibTableColumn
gslbNewCfgEnhNetworkSourceIp = _GslbNewCfgEnhNetworkSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 3, 1, 3),
    _GslbNewCfgEnhNetworkSourceIp_Type()
)
gslbNewCfgEnhNetworkSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgEnhNetworkSourceIp.setStatus("current")
_GslbNewCfgEnhNetworkNetMask_Type = IpAddress
_GslbNewCfgEnhNetworkNetMask_Object = MibTableColumn
gslbNewCfgEnhNetworkNetMask = _GslbNewCfgEnhNetworkNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 3, 1, 4),
    _GslbNewCfgEnhNetworkNetMask_Type()
)
gslbNewCfgEnhNetworkNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgEnhNetworkNetMask.setStatus("current")


class _GslbNewCfgEnhNetworkDelete_Type(Integer32):
    """Custom type gslbNewCfgEnhNetworkDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_GslbNewCfgEnhNetworkDelete_Type.__name__ = "Integer32"
_GslbNewCfgEnhNetworkDelete_Object = MibTableColumn
gslbNewCfgEnhNetworkDelete = _GslbNewCfgEnhNetworkDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 3, 1, 5),
    _GslbNewCfgEnhNetworkDelete_Type()
)
gslbNewCfgEnhNetworkDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgEnhNetworkDelete.setStatus("current")
_GslbNewCfgEnhNetworkVirtServer_Type = OctetString
_GslbNewCfgEnhNetworkVirtServer_Object = MibTableColumn
gslbNewCfgEnhNetworkVirtServer = _GslbNewCfgEnhNetworkVirtServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 3, 1, 6),
    _GslbNewCfgEnhNetworkVirtServer_Type()
)
gslbNewCfgEnhNetworkVirtServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbNewCfgEnhNetworkVirtServer.setStatus("current")
_GslbNewCfgEnhNetworkRemRealServer_Type = OctetString
_GslbNewCfgEnhNetworkRemRealServer_Object = MibTableColumn
gslbNewCfgEnhNetworkRemRealServer = _GslbNewCfgEnhNetworkRemRealServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 3, 1, 7),
    _GslbNewCfgEnhNetworkRemRealServer_Type()
)
gslbNewCfgEnhNetworkRemRealServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbNewCfgEnhNetworkRemRealServer.setStatus("current")
_GslbNewCfgEnhNetworkAddVirtServer_Type = Integer32
_GslbNewCfgEnhNetworkAddVirtServer_Object = MibTableColumn
gslbNewCfgEnhNetworkAddVirtServer = _GslbNewCfgEnhNetworkAddVirtServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 3, 1, 8),
    _GslbNewCfgEnhNetworkAddVirtServer_Type()
)
gslbNewCfgEnhNetworkAddVirtServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgEnhNetworkAddVirtServer.setStatus("current")
_GslbNewCfgEnhNetworkRemoveVirtServer_Type = Integer32
_GslbNewCfgEnhNetworkRemoveVirtServer_Object = MibTableColumn
gslbNewCfgEnhNetworkRemoveVirtServer = _GslbNewCfgEnhNetworkRemoveVirtServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 3, 1, 9),
    _GslbNewCfgEnhNetworkRemoveVirtServer_Type()
)
gslbNewCfgEnhNetworkRemoveVirtServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgEnhNetworkRemoveVirtServer.setStatus("current")
_GslbNewCfgEnhNetworkAddRemRealServer_Type = Integer32
_GslbNewCfgEnhNetworkAddRemRealServer_Object = MibTableColumn
gslbNewCfgEnhNetworkAddRemRealServer = _GslbNewCfgEnhNetworkAddRemRealServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 3, 1, 10),
    _GslbNewCfgEnhNetworkAddRemRealServer_Type()
)
gslbNewCfgEnhNetworkAddRemRealServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgEnhNetworkAddRemRealServer.setStatus("current")
_GslbNewCfgEnhNetworkRemoveRemRealServer_Type = Integer32
_GslbNewCfgEnhNetworkRemoveRemRealServer_Object = MibTableColumn
gslbNewCfgEnhNetworkRemoveRemRealServer = _GslbNewCfgEnhNetworkRemoveRemRealServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 4, 3, 1, 11),
    _GslbNewCfgEnhNetworkRemoveRemRealServer_Type()
)
gslbNewCfgEnhNetworkRemoveRemRealServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgEnhNetworkRemoveRemRealServer.setStatus("current")
_GslbRuleCfg_ObjectIdentity = ObjectIdentity
gslbRuleCfg = _GslbRuleCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5)
)
_GslbRuleTableMaxSize_Type = Integer32
_GslbRuleTableMaxSize_Object = MibScalar
gslbRuleTableMaxSize = _GslbRuleTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 1),
    _GslbRuleTableMaxSize_Type()
)
gslbRuleTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbRuleTableMaxSize.setStatus("current")
_GslbCurCfgRuleTable_Object = MibTable
gslbCurCfgRuleTable = _GslbCurCfgRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    gslbCurCfgRuleTable.setStatus("current")
_GslbCurCfgRuleTableEntry_Object = MibTableRow
gslbCurCfgRuleTableEntry = _GslbCurCfgRuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 2, 1)
)
gslbCurCfgRuleTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbCurCfgRuleIndx"),
)
if mibBuilder.loadTexts:
    gslbCurCfgRuleTableEntry.setStatus("current")
_GslbCurCfgRuleIndx_Type = Integer32
_GslbCurCfgRuleIndx_Object = MibTableColumn
gslbCurCfgRuleIndx = _GslbCurCfgRuleIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 2, 1, 1),
    _GslbCurCfgRuleIndx_Type()
)
gslbCurCfgRuleIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRuleIndx.setStatus("current")


class _GslbCurCfgRuleState_Type(Integer32):
    """Custom type gslbCurCfgRuleState based on Integer32"""
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


_GslbCurCfgRuleState_Type.__name__ = "Integer32"
_GslbCurCfgRuleState_Object = MibTableColumn
gslbCurCfgRuleState = _GslbCurCfgRuleState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 2, 1, 2),
    _GslbCurCfgRuleState_Type()
)
gslbCurCfgRuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRuleState.setStatus("current")


class _GslbCurCfgRuleStartHour_Type(Integer32):
    """Custom type gslbCurCfgRuleStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_GslbCurCfgRuleStartHour_Type.__name__ = "Integer32"
_GslbCurCfgRuleStartHour_Object = MibTableColumn
gslbCurCfgRuleStartHour = _GslbCurCfgRuleStartHour_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 2, 1, 3),
    _GslbCurCfgRuleStartHour_Type()
)
gslbCurCfgRuleStartHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRuleStartHour.setStatus("current")


class _GslbCurCfgRuleStartMin_Type(Integer32):
    """Custom type gslbCurCfgRuleStartMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_GslbCurCfgRuleStartMin_Type.__name__ = "Integer32"
_GslbCurCfgRuleStartMin_Object = MibTableColumn
gslbCurCfgRuleStartMin = _GslbCurCfgRuleStartMin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 2, 1, 4),
    _GslbCurCfgRuleStartMin_Type()
)
gslbCurCfgRuleStartMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRuleStartMin.setStatus("current")


class _GslbCurCfgRuleEndHour_Type(Integer32):
    """Custom type gslbCurCfgRuleEndHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_GslbCurCfgRuleEndHour_Type.__name__ = "Integer32"
_GslbCurCfgRuleEndHour_Object = MibTableColumn
gslbCurCfgRuleEndHour = _GslbCurCfgRuleEndHour_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 2, 1, 5),
    _GslbCurCfgRuleEndHour_Type()
)
gslbCurCfgRuleEndHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRuleEndHour.setStatus("current")


class _GslbCurCfgRuleEndMin_Type(Integer32):
    """Custom type gslbCurCfgRuleEndMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_GslbCurCfgRuleEndMin_Type.__name__ = "Integer32"
_GslbCurCfgRuleEndMin_Object = MibTableColumn
gslbCurCfgRuleEndMin = _GslbCurCfgRuleEndMin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 2, 1, 6),
    _GslbCurCfgRuleEndMin_Type()
)
gslbCurCfgRuleEndMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRuleEndMin.setStatus("current")


class _GslbCurCfgRuleTTL_Type(Integer32):
    """Custom type gslbCurCfgRuleTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GslbCurCfgRuleTTL_Type.__name__ = "Integer32"
_GslbCurCfgRuleTTL_Object = MibTableColumn
gslbCurCfgRuleTTL = _GslbCurCfgRuleTTL_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 2, 1, 7),
    _GslbCurCfgRuleTTL_Type()
)
gslbCurCfgRuleTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRuleTTL.setStatus("current")


class _GslbCurCfgRuleRR_Type(Integer32):
    """Custom type gslbCurCfgRuleRR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_GslbCurCfgRuleRR_Type.__name__ = "Integer32"
_GslbCurCfgRuleRR_Object = MibTableColumn
gslbCurCfgRuleRR = _GslbCurCfgRuleRR_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 2, 1, 8),
    _GslbCurCfgRuleRR_Type()
)
gslbCurCfgRuleRR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRuleRR.setStatus("current")
_GslbNewCfgRuleTable_Object = MibTable
gslbNewCfgRuleTable = _GslbNewCfgRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 3)
)
if mibBuilder.loadTexts:
    gslbNewCfgRuleTable.setStatus("current")
_GslbNewCfgRuleTableEntry_Object = MibTableRow
gslbNewCfgRuleTableEntry = _GslbNewCfgRuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 3, 1)
)
gslbNewCfgRuleTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbNewCfgRuleIndx"),
)
if mibBuilder.loadTexts:
    gslbNewCfgRuleTableEntry.setStatus("current")
_GslbNewCfgRuleIndx_Type = Integer32
_GslbNewCfgRuleIndx_Object = MibTableColumn
gslbNewCfgRuleIndx = _GslbNewCfgRuleIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 3, 1, 1),
    _GslbNewCfgRuleIndx_Type()
)
gslbNewCfgRuleIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbNewCfgRuleIndx.setStatus("current")


class _GslbNewCfgRuleState_Type(Integer32):
    """Custom type gslbNewCfgRuleState based on Integer32"""
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


_GslbNewCfgRuleState_Type.__name__ = "Integer32"
_GslbNewCfgRuleState_Object = MibTableColumn
gslbNewCfgRuleState = _GslbNewCfgRuleState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 3, 1, 2),
    _GslbNewCfgRuleState_Type()
)
gslbNewCfgRuleState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgRuleState.setStatus("current")


class _GslbNewCfgRuleStartHour_Type(Integer32):
    """Custom type gslbNewCfgRuleStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_GslbNewCfgRuleStartHour_Type.__name__ = "Integer32"
_GslbNewCfgRuleStartHour_Object = MibTableColumn
gslbNewCfgRuleStartHour = _GslbNewCfgRuleStartHour_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 3, 1, 3),
    _GslbNewCfgRuleStartHour_Type()
)
gslbNewCfgRuleStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRuleStartHour.setStatus("current")


class _GslbNewCfgRuleStartMin_Type(Integer32):
    """Custom type gslbNewCfgRuleStartMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_GslbNewCfgRuleStartMin_Type.__name__ = "Integer32"
_GslbNewCfgRuleStartMin_Object = MibTableColumn
gslbNewCfgRuleStartMin = _GslbNewCfgRuleStartMin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 3, 1, 4),
    _GslbNewCfgRuleStartMin_Type()
)
gslbNewCfgRuleStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRuleStartMin.setStatus("current")


class _GslbNewCfgRuleEndHour_Type(Integer32):
    """Custom type gslbNewCfgRuleEndHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_GslbNewCfgRuleEndHour_Type.__name__ = "Integer32"
_GslbNewCfgRuleEndHour_Object = MibTableColumn
gslbNewCfgRuleEndHour = _GslbNewCfgRuleEndHour_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 3, 1, 5),
    _GslbNewCfgRuleEndHour_Type()
)
gslbNewCfgRuleEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRuleEndHour.setStatus("current")


class _GslbNewCfgRuleEndMin_Type(Integer32):
    """Custom type gslbNewCfgRuleEndMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_GslbNewCfgRuleEndMin_Type.__name__ = "Integer32"
_GslbNewCfgRuleEndMin_Object = MibTableColumn
gslbNewCfgRuleEndMin = _GslbNewCfgRuleEndMin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 3, 1, 6),
    _GslbNewCfgRuleEndMin_Type()
)
gslbNewCfgRuleEndMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRuleEndMin.setStatus("current")


class _GslbNewCfgRuleTTL_Type(Integer32):
    """Custom type gslbNewCfgRuleTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GslbNewCfgRuleTTL_Type.__name__ = "Integer32"
_GslbNewCfgRuleTTL_Object = MibTableColumn
gslbNewCfgRuleTTL = _GslbNewCfgRuleTTL_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 3, 1, 7),
    _GslbNewCfgRuleTTL_Type()
)
gslbNewCfgRuleTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRuleTTL.setStatus("current")


class _GslbNewCfgRuleRR_Type(Integer32):
    """Custom type gslbNewCfgRuleRR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_GslbNewCfgRuleRR_Type.__name__ = "Integer32"
_GslbNewCfgRuleRR_Object = MibTableColumn
gslbNewCfgRuleRR = _GslbNewCfgRuleRR_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 3, 1, 8),
    _GslbNewCfgRuleRR_Type()
)
gslbNewCfgRuleRR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRuleRR.setStatus("current")


class _GslbNewCfgRuleDelete_Type(Integer32):
    """Custom type gslbNewCfgRuleDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_GslbNewCfgRuleDelete_Type.__name__ = "Integer32"
_GslbNewCfgRuleDelete_Object = MibTableColumn
gslbNewCfgRuleDelete = _GslbNewCfgRuleDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 3, 1, 9),
    _GslbNewCfgRuleDelete_Type()
)
gslbNewCfgRuleDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gslbNewCfgRuleDelete.setStatus("current")
_GslbMetricTableMaxSize_Type = Integer32
_GslbMetricTableMaxSize_Object = MibScalar
gslbMetricTableMaxSize = _GslbMetricTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 4),
    _GslbMetricTableMaxSize_Type()
)
gslbMetricTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbMetricTableMaxSize.setStatus("current")
_GslbCurCfgMetricTable_Object = MibTable
gslbCurCfgMetricTable = _GslbCurCfgMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 5)
)
if mibBuilder.loadTexts:
    gslbCurCfgMetricTable.setStatus("current")
_GslbCurCfgMetricTableEntry_Object = MibTableRow
gslbCurCfgMetricTableEntry = _GslbCurCfgMetricTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 5, 1)
)
gslbCurCfgMetricTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbCurCfgRuleMetricIndx"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbCurCfgMetricIndx"),
)
if mibBuilder.loadTexts:
    gslbCurCfgMetricTableEntry.setStatus("current")
_GslbCurCfgRuleMetricIndx_Type = Integer32
_GslbCurCfgRuleMetricIndx_Object = MibTableColumn
gslbCurCfgRuleMetricIndx = _GslbCurCfgRuleMetricIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 5, 1, 1),
    _GslbCurCfgRuleMetricIndx_Type()
)
gslbCurCfgRuleMetricIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRuleMetricIndx.setStatus("current")
_GslbCurCfgMetricIndx_Type = Integer32
_GslbCurCfgMetricIndx_Object = MibTableColumn
gslbCurCfgMetricIndx = _GslbCurCfgMetricIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 5, 1, 2),
    _GslbCurCfgMetricIndx_Type()
)
gslbCurCfgMetricIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgMetricIndx.setStatus("current")


class _GslbCurCfgMetricMetric_Type(Integer32):
    """Custom type gslbCurCfgMetricMetric based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("leastconns", 1),
          ("roundrobin", 2),
          ("response", 3),
          ("geographical", 4),
          ("network", 5),
          ("random", 6),
          ("availability", 7),
          ("qos", 8),
          ("minmisses", 9),
          ("hash", 10),
          ("local", 11),
          ("always", 12),
          ("remote", 13),
          ("none", 14),
          ("persistence", 15))
    )


_GslbCurCfgMetricMetric_Type.__name__ = "Integer32"
_GslbCurCfgMetricMetric_Object = MibTableColumn
gslbCurCfgMetricMetric = _GslbCurCfgMetricMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 5, 1, 3),
    _GslbCurCfgMetricMetric_Type()
)
gslbCurCfgMetricMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgMetricMetric.setStatus("current")
_GslbCurCfgMetricNetworkBmap_Type = OctetString
_GslbCurCfgMetricNetworkBmap_Object = MibTableColumn
gslbCurCfgMetricNetworkBmap = _GslbCurCfgMetricNetworkBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 5, 1, 4),
    _GslbCurCfgMetricNetworkBmap_Type()
)
gslbCurCfgMetricNetworkBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgMetricNetworkBmap.setStatus("current")
_GslbNewCfgMetricTable_Object = MibTable
gslbNewCfgMetricTable = _GslbNewCfgMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 6)
)
if mibBuilder.loadTexts:
    gslbNewCfgMetricTable.setStatus("current")
_GslbNewCfgMetricTableEntry_Object = MibTableRow
gslbNewCfgMetricTableEntry = _GslbNewCfgMetricTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 6, 1)
)
gslbNewCfgMetricTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbNewCfgRuleMetricIndx"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbNewCfgMetricIndx"),
)
if mibBuilder.loadTexts:
    gslbNewCfgMetricTableEntry.setStatus("current")
_GslbNewCfgRuleMetricIndx_Type = Integer32
_GslbNewCfgRuleMetricIndx_Object = MibTableColumn
gslbNewCfgRuleMetricIndx = _GslbNewCfgRuleMetricIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 6, 1, 1),
    _GslbNewCfgRuleMetricIndx_Type()
)
gslbNewCfgRuleMetricIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbNewCfgRuleMetricIndx.setStatus("current")
_GslbNewCfgMetricIndx_Type = Integer32
_GslbNewCfgMetricIndx_Object = MibTableColumn
gslbNewCfgMetricIndx = _GslbNewCfgMetricIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 6, 1, 2),
    _GslbNewCfgMetricIndx_Type()
)
gslbNewCfgMetricIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbNewCfgMetricIndx.setStatus("current")


class _GslbNewCfgMetricMetric_Type(Integer32):
    """Custom type gslbNewCfgMetricMetric based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("leastconns", 1),
          ("roundrobin", 2),
          ("response", 3),
          ("geographical", 4),
          ("network", 5),
          ("random", 6),
          ("availability", 7),
          ("qos", 8),
          ("minmisses", 9),
          ("hash", 10),
          ("local", 11),
          ("always", 12),
          ("remote", 13),
          ("none", 14),
          ("persistence", 15))
    )


_GslbNewCfgMetricMetric_Type.__name__ = "Integer32"
_GslbNewCfgMetricMetric_Object = MibTableColumn
gslbNewCfgMetricMetric = _GslbNewCfgMetricMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 6, 1, 3),
    _GslbNewCfgMetricMetric_Type()
)
gslbNewCfgMetricMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgMetricMetric.setStatus("current")
_GslbNewCfgMetricNetworkBmap_Type = OctetString
_GslbNewCfgMetricNetworkBmap_Object = MibTableColumn
gslbNewCfgMetricNetworkBmap = _GslbNewCfgMetricNetworkBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 6, 1, 4),
    _GslbNewCfgMetricNetworkBmap_Type()
)
gslbNewCfgMetricNetworkBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbNewCfgMetricNetworkBmap.setStatus("current")
_GslbNewCfgMetricAddNetwork_Type = Integer32
_GslbNewCfgMetricAddNetwork_Object = MibTableColumn
gslbNewCfgMetricAddNetwork = _GslbNewCfgMetricAddNetwork_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 6, 1, 5),
    _GslbNewCfgMetricAddNetwork_Type()
)
gslbNewCfgMetricAddNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgMetricAddNetwork.setStatus("current")
_GslbNewCfgMetricRemNetwork_Type = Integer32
_GslbNewCfgMetricRemNetwork_Object = MibTableColumn
gslbNewCfgMetricRemNetwork = _GslbNewCfgMetricRemNetwork_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 3, 5, 6, 1, 6),
    _GslbNewCfgMetricRemNetwork_Type()
)
gslbNewCfgMetricRemNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgMetricRemNetwork.setStatus("current")
_Layer4TableSize_ObjectIdentity = ObjectIdentity
layer4TableSize = _Layer4TableSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 4)
)
_CurCfgFilterTableSize_Type = Integer32
_CurCfgFilterTableSize_Object = MibScalar
curCfgFilterTableSize = _CurCfgFilterTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 4, 1),
    _CurCfgFilterTableSize_Type()
)
curCfgFilterTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curCfgFilterTableSize.setStatus("current")
_NewCfgFilterTableSize_Type = Integer32
_NewCfgFilterTableSize_Object = MibScalar
newCfgFilterTableSize = _NewCfgFilterTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 4, 2),
    _NewCfgFilterTableSize_Type()
)
newCfgFilterTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newCfgFilterTableSize.setStatus("current")
_CurCfgRealServerTableSize_Type = Integer32
_CurCfgRealServerTableSize_Object = MibScalar
curCfgRealServerTableSize = _CurCfgRealServerTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 4, 3),
    _CurCfgRealServerTableSize_Type()
)
curCfgRealServerTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curCfgRealServerTableSize.setStatus("current")
_NewCfgRealServerTableSize_Type = Integer32
_NewCfgRealServerTableSize_Object = MibScalar
newCfgRealServerTableSize = _NewCfgRealServerTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 4, 4),
    _NewCfgRealServerTableSize_Type()
)
newCfgRealServerTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newCfgRealServerTableSize.setStatus("current")
_CurCfgRealServerGroupTableSize_Type = Integer32
_CurCfgRealServerGroupTableSize_Object = MibScalar
curCfgRealServerGroupTableSize = _CurCfgRealServerGroupTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 4, 5),
    _CurCfgRealServerGroupTableSize_Type()
)
curCfgRealServerGroupTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curCfgRealServerGroupTableSize.setStatus("current")
_NewCfgRealServerGroupTableSize_Type = Integer32
_NewCfgRealServerGroupTableSize_Object = MibScalar
newCfgRealServerGroupTableSize = _NewCfgRealServerGroupTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 4, 6),
    _NewCfgRealServerGroupTableSize_Type()
)
newCfgRealServerGroupTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newCfgRealServerGroupTableSize.setStatus("current")
_CurCfgVirtServerTableSize_Type = Integer32
_CurCfgVirtServerTableSize_Object = MibScalar
curCfgVirtServerTableSize = _CurCfgVirtServerTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 4, 7),
    _CurCfgVirtServerTableSize_Type()
)
curCfgVirtServerTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curCfgVirtServerTableSize.setStatus("current")
_NewCfgVirtServerTableSize_Type = Integer32
_NewCfgVirtServerTableSize_Object = MibScalar
newCfgVirtServerTableSize = _NewCfgVirtServerTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 4, 8),
    _NewCfgVirtServerTableSize_Type()
)
newCfgVirtServerTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newCfgVirtServerTableSize.setStatus("current")
_WlmCfg_ObjectIdentity = ObjectIdentity
wlmCfg = _WlmCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 6)
)
_SlbWlmTableMaxSize_Type = Integer32
_SlbWlmTableMaxSize_Object = MibScalar
slbWlmTableMaxSize = _SlbWlmTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 6, 1),
    _SlbWlmTableMaxSize_Type()
)
slbWlmTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbWlmTableMaxSize.setStatus("current")
_SlbCurCfgWlmTable_Object = MibTable
slbCurCfgWlmTable = _SlbCurCfgWlmTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 6, 2)
)
if mibBuilder.loadTexts:
    slbCurCfgWlmTable.setStatus("current")
_SlbCurCfgWlmEntry_Object = MibTableRow
slbCurCfgWlmEntry = _SlbCurCfgWlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 6, 2, 1)
)
slbCurCfgWlmEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbCurCfgWlmIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgWlmEntry.setStatus("current")
_SlbCurCfgWlmIndex_Type = Integer32
_SlbCurCfgWlmIndex_Object = MibTableColumn
slbCurCfgWlmIndex = _SlbCurCfgWlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 6, 2, 1, 1),
    _SlbCurCfgWlmIndex_Type()
)
slbCurCfgWlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWlmIndex.setStatus("current")
_SlbCurCfgWlmIpAddr_Type = IpAddress
_SlbCurCfgWlmIpAddr_Object = MibTableColumn
slbCurCfgWlmIpAddr = _SlbCurCfgWlmIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 6, 2, 1, 2),
    _SlbCurCfgWlmIpAddr_Type()
)
slbCurCfgWlmIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWlmIpAddr.setStatus("current")


class _SlbCurCfgWlmPort_Type(Integer32):
    """Custom type slbCurCfgWlmPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbCurCfgWlmPort_Type.__name__ = "Integer32"
_SlbCurCfgWlmPort_Object = MibTableColumn
slbCurCfgWlmPort = _SlbCurCfgWlmPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 6, 2, 1, 3),
    _SlbCurCfgWlmPort_Type()
)
slbCurCfgWlmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWlmPort.setStatus("current")
_SlbNewCfgWlmTable_Object = MibTable
slbNewCfgWlmTable = _SlbNewCfgWlmTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 6, 3)
)
if mibBuilder.loadTexts:
    slbNewCfgWlmTable.setStatus("current")
_SlbNewCfgWlmEntry_Object = MibTableRow
slbNewCfgWlmEntry = _SlbNewCfgWlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 6, 3, 1)
)
slbNewCfgWlmEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbNewCfgWlmIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgWlmEntry.setStatus("current")
_SlbNewCfgWlmIndex_Type = Integer32
_SlbNewCfgWlmIndex_Object = MibTableColumn
slbNewCfgWlmIndex = _SlbNewCfgWlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 6, 3, 1, 1),
    _SlbNewCfgWlmIndex_Type()
)
slbNewCfgWlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgWlmIndex.setStatus("current")
_SlbNewCfgWlmIpAddr_Type = IpAddress
_SlbNewCfgWlmIpAddr_Object = MibTableColumn
slbNewCfgWlmIpAddr = _SlbNewCfgWlmIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 6, 3, 1, 2),
    _SlbNewCfgWlmIpAddr_Type()
)
slbNewCfgWlmIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgWlmIpAddr.setStatus("current")


class _SlbNewCfgWlmPort_Type(Integer32):
    """Custom type slbNewCfgWlmPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbNewCfgWlmPort_Type.__name__ = "Integer32"
_SlbNewCfgWlmPort_Object = MibTableColumn
slbNewCfgWlmPort = _SlbNewCfgWlmPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 6, 3, 1, 3),
    _SlbNewCfgWlmPort_Type()
)
slbNewCfgWlmPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgWlmPort.setStatus("current")


class _SlbNewCfgWlmDelete_Type(Integer32):
    """Custom type slbNewCfgWlmDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgWlmDelete_Type.__name__ = "Integer32"
_SlbNewCfgWlmDelete_Object = MibTableColumn
slbNewCfgWlmDelete = _SlbNewCfgWlmDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 1, 6, 3, 1, 4),
    _SlbNewCfgWlmDelete_Type()
)
slbNewCfgWlmDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgWlmDelete.setStatus("current")
_Layer4Stats_ObjectIdentity = ObjectIdentity
layer4Stats = _Layer4Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2)
)
_SlbSpStats_ObjectIdentity = ObjectIdentity
slbSpStats = _SlbSpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1)
)
_SlbStatSpRealServerTable_Object = MibTable
slbStatSpRealServerTable = _SlbStatSpRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    slbStatSpRealServerTable.setStatus("current")
_SlbStatSpRealServerEntry_Object = MibTableRow
slbStatSpRealServerEntry = _SlbStatSpRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 1, 1)
)
slbStatSpRealServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatSpRealServerSpIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatSpRealServerServerIndex"),
)
if mibBuilder.loadTexts:
    slbStatSpRealServerEntry.setStatus("current")
_SlbStatSpRealServerSpIndex_Type = Integer32
_SlbStatSpRealServerSpIndex_Object = MibTableColumn
slbStatSpRealServerSpIndex = _SlbStatSpRealServerSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 1, 1, 1),
    _SlbStatSpRealServerSpIndex_Type()
)
slbStatSpRealServerSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpRealServerSpIndex.setStatus("current")
_SlbStatSpRealServerServerIndex_Type = Integer32
_SlbStatSpRealServerServerIndex_Object = MibTableColumn
slbStatSpRealServerServerIndex = _SlbStatSpRealServerServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 1, 1, 2),
    _SlbStatSpRealServerServerIndex_Type()
)
slbStatSpRealServerServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpRealServerServerIndex.setStatus("current")
_SlbStatSpRealServerCurrSessions_Type = Gauge32
_SlbStatSpRealServerCurrSessions_Object = MibTableColumn
slbStatSpRealServerCurrSessions = _SlbStatSpRealServerCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 1, 1, 3),
    _SlbStatSpRealServerCurrSessions_Type()
)
slbStatSpRealServerCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpRealServerCurrSessions.setStatus("current")
_SlbStatSpRealServerTotalSessions_Type = Counter32
_SlbStatSpRealServerTotalSessions_Object = MibTableColumn
slbStatSpRealServerTotalSessions = _SlbStatSpRealServerTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 1, 1, 4),
    _SlbStatSpRealServerTotalSessions_Type()
)
slbStatSpRealServerTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpRealServerTotalSessions.setStatus("current")
_SlbStatSpRealServerHCOctetsLow32_Type = Counter32
_SlbStatSpRealServerHCOctetsLow32_Object = MibTableColumn
slbStatSpRealServerHCOctetsLow32 = _SlbStatSpRealServerHCOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 1, 1, 5),
    _SlbStatSpRealServerHCOctetsLow32_Type()
)
slbStatSpRealServerHCOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpRealServerHCOctetsLow32.setStatus("current")
_SlbStatSpRealServerHCOctetsHigh32_Type = Counter32
_SlbStatSpRealServerHCOctetsHigh32_Object = MibTableColumn
slbStatSpRealServerHCOctetsHigh32 = _SlbStatSpRealServerHCOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 1, 1, 6),
    _SlbStatSpRealServerHCOctetsHigh32_Type()
)
slbStatSpRealServerHCOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpRealServerHCOctetsHigh32.setStatus("current")
_SlbStatSpRealServerHCOctets_Type = Counter64
_SlbStatSpRealServerHCOctets_Object = MibTableColumn
slbStatSpRealServerHCOctets = _SlbStatSpRealServerHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 1, 1, 7),
    _SlbStatSpRealServerHCOctets_Type()
)
slbStatSpRealServerHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpRealServerHCOctets.setStatus("current")
_SlbStatSpFltTable_Object = MibTable
slbStatSpFltTable = _SlbStatSpFltTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 4)
)
if mibBuilder.loadTexts:
    slbStatSpFltTable.setStatus("current")
_SlbStatSpFltEntry_Object = MibTableRow
slbStatSpFltEntry = _SlbStatSpFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 4, 1)
)
slbStatSpFltEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatSpFltSpIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatSpFltIndex"),
)
if mibBuilder.loadTexts:
    slbStatSpFltEntry.setStatus("current")
_SlbStatSpFltSpIndex_Type = Integer32
_SlbStatSpFltSpIndex_Object = MibTableColumn
slbStatSpFltSpIndex = _SlbStatSpFltSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 4, 1, 1),
    _SlbStatSpFltSpIndex_Type()
)
slbStatSpFltSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpFltSpIndex.setStatus("current")
_SlbStatSpFltIndex_Type = Integer32
_SlbStatSpFltIndex_Object = MibTableColumn
slbStatSpFltIndex = _SlbStatSpFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 4, 1, 2),
    _SlbStatSpFltIndex_Type()
)
slbStatSpFltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpFltIndex.setStatus("current")
_SlbStatSpFltFirings_Type = Counter32
_SlbStatSpFltFirings_Object = MibTableColumn
slbStatSpFltFirings = _SlbStatSpFltFirings_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 4, 1, 3),
    _SlbStatSpFltFirings_Type()
)
slbStatSpFltFirings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpFltFirings.setStatus("current")
_SlbStatSpMaintTable_Object = MibTable
slbStatSpMaintTable = _SlbStatSpMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5)
)
if mibBuilder.loadTexts:
    slbStatSpMaintTable.setStatus("current")
_SlbStatSpMaintEntry_Object = MibTableRow
slbStatSpMaintEntry = _SlbStatSpMaintEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1)
)
slbStatSpMaintEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatSpMaintSpIndex"),
)
if mibBuilder.loadTexts:
    slbStatSpMaintEntry.setStatus("current")
_SlbStatSpMaintSpIndex_Type = Integer32
_SlbStatSpMaintSpIndex_Object = MibTableColumn
slbStatSpMaintSpIndex = _SlbStatSpMaintSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 1),
    _SlbStatSpMaintSpIndex_Type()
)
slbStatSpMaintSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSpIndex.setStatus("current")
_SlbStatSpMaintMaximumSessions_Type = Integer32
_SlbStatSpMaintMaximumSessions_Object = MibTableColumn
slbStatSpMaintMaximumSessions = _SlbStatSpMaintMaximumSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 2),
    _SlbStatSpMaintMaximumSessions_Type()
)
slbStatSpMaintMaximumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintMaximumSessions.setStatus("current")
_SlbStatSpMaintCurBindings_Type = Gauge32
_SlbStatSpMaintCurBindings_Object = MibTableColumn
slbStatSpMaintCurBindings = _SlbStatSpMaintCurBindings_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 3),
    _SlbStatSpMaintCurBindings_Type()
)
slbStatSpMaintCurBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintCurBindings.setStatus("current")
_SlbStatSpMaintCurBindings4Seconds_Type = Gauge32
_SlbStatSpMaintCurBindings4Seconds_Object = MibTableColumn
slbStatSpMaintCurBindings4Seconds = _SlbStatSpMaintCurBindings4Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 4),
    _SlbStatSpMaintCurBindings4Seconds_Type()
)
slbStatSpMaintCurBindings4Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintCurBindings4Seconds.setStatus("current")
_SlbStatSpMaintCurBindings64Seconds_Type = Gauge32
_SlbStatSpMaintCurBindings64Seconds_Object = MibTableColumn
slbStatSpMaintCurBindings64Seconds = _SlbStatSpMaintCurBindings64Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 5),
    _SlbStatSpMaintCurBindings64Seconds_Type()
)
slbStatSpMaintCurBindings64Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintCurBindings64Seconds.setStatus("current")
_SlbStatSpMaintTerminatedSessions_Type = Counter32
_SlbStatSpMaintTerminatedSessions_Object = MibTableColumn
slbStatSpMaintTerminatedSessions = _SlbStatSpMaintTerminatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 6),
    _SlbStatSpMaintTerminatedSessions_Type()
)
slbStatSpMaintTerminatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintTerminatedSessions.setStatus("current")
_SlbStatSpMaintBindingFails_Type = Counter32
_SlbStatSpMaintBindingFails_Object = MibTableColumn
slbStatSpMaintBindingFails = _SlbStatSpMaintBindingFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 7),
    _SlbStatSpMaintBindingFails_Type()
)
slbStatSpMaintBindingFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintBindingFails.setStatus("current")
_SlbStatSpMaintNonTcpFrames_Type = Counter32
_SlbStatSpMaintNonTcpFrames_Object = MibTableColumn
slbStatSpMaintNonTcpFrames = _SlbStatSpMaintNonTcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 8),
    _SlbStatSpMaintNonTcpFrames_Type()
)
slbStatSpMaintNonTcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintNonTcpFrames.setStatus("current")
_SlbStatSpMaintTcpFragments_Type = Counter32
_SlbStatSpMaintTcpFragments_Object = MibTableColumn
slbStatSpMaintTcpFragments = _SlbStatSpMaintTcpFragments_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 9),
    _SlbStatSpMaintTcpFragments_Type()
)
slbStatSpMaintTcpFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintTcpFragments.setStatus("obsolete")
_SlbStatSpMaintUdpDatagrams_Type = Counter32
_SlbStatSpMaintUdpDatagrams_Object = MibTableColumn
slbStatSpMaintUdpDatagrams = _SlbStatSpMaintUdpDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 10),
    _SlbStatSpMaintUdpDatagrams_Type()
)
slbStatSpMaintUdpDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintUdpDatagrams.setStatus("current")
_SlbStatSpMaintIncorrectVIPs_Type = Counter32
_SlbStatSpMaintIncorrectVIPs_Object = MibTableColumn
slbStatSpMaintIncorrectVIPs = _SlbStatSpMaintIncorrectVIPs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 11),
    _SlbStatSpMaintIncorrectVIPs_Type()
)
slbStatSpMaintIncorrectVIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintIncorrectVIPs.setStatus("current")
_SlbStatSpMaintIncorrectVports_Type = Counter32
_SlbStatSpMaintIncorrectVports_Object = MibTableColumn
slbStatSpMaintIncorrectVports = _SlbStatSpMaintIncorrectVports_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 12),
    _SlbStatSpMaintIncorrectVports_Type()
)
slbStatSpMaintIncorrectVports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintIncorrectVports.setStatus("current")
_SlbStatSpMaintRealServerNoAvails_Type = Counter32
_SlbStatSpMaintRealServerNoAvails_Object = MibTableColumn
slbStatSpMaintRealServerNoAvails = _SlbStatSpMaintRealServerNoAvails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 13),
    _SlbStatSpMaintRealServerNoAvails_Type()
)
slbStatSpMaintRealServerNoAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintRealServerNoAvails.setStatus("current")
_SlbStatSpMaintFilteredDeniedFrames_Type = Counter32
_SlbStatSpMaintFilteredDeniedFrames_Object = MibTableColumn
slbStatSpMaintFilteredDeniedFrames = _SlbStatSpMaintFilteredDeniedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 14),
    _SlbStatSpMaintFilteredDeniedFrames_Type()
)
slbStatSpMaintFilteredDeniedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintFilteredDeniedFrames.setStatus("current")
_SlbStatSpMaintLandAttacks_Type = Counter32
_SlbStatSpMaintLandAttacks_Object = MibTableColumn
slbStatSpMaintLandAttacks = _SlbStatSpMaintLandAttacks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 15),
    _SlbStatSpMaintLandAttacks_Type()
)
slbStatSpMaintLandAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintLandAttacks.setStatus("current")
_SlbStatSpMaintIpFragTotalSessions_Type = Counter32
_SlbStatSpMaintIpFragTotalSessions_Object = MibTableColumn
slbStatSpMaintIpFragTotalSessions = _SlbStatSpMaintIpFragTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 16),
    _SlbStatSpMaintIpFragTotalSessions_Type()
)
slbStatSpMaintIpFragTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintIpFragTotalSessions.setStatus("current")
_SlbStatSpMaintIpFragCurSessions_Type = Gauge32
_SlbStatSpMaintIpFragCurSessions_Object = MibTableColumn
slbStatSpMaintIpFragCurSessions = _SlbStatSpMaintIpFragCurSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 17),
    _SlbStatSpMaintIpFragCurSessions_Type()
)
slbStatSpMaintIpFragCurSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintIpFragCurSessions.setStatus("current")
_SlbStatSpMaintIpFragDiscards_Type = Counter32
_SlbStatSpMaintIpFragDiscards_Object = MibTableColumn
slbStatSpMaintIpFragDiscards = _SlbStatSpMaintIpFragDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 18),
    _SlbStatSpMaintIpFragDiscards_Type()
)
slbStatSpMaintIpFragDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintIpFragDiscards.setStatus("current")
_SlbStatSpMaintIpFragTableFull_Type = Counter32
_SlbStatSpMaintIpFragTableFull_Object = MibTableColumn
slbStatSpMaintIpFragTableFull = _SlbStatSpMaintIpFragTableFull_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 19),
    _SlbStatSpMaintIpFragTableFull_Type()
)
slbStatSpMaintIpFragTableFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintIpFragTableFull.setStatus("current")


class _SlbStatSpMaintClear_Type(Integer32):
    """Custom type slbStatSpMaintClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_SlbStatSpMaintClear_Type.__name__ = "Integer32"
_SlbStatSpMaintClear_Object = MibTableColumn
slbStatSpMaintClear = _SlbStatSpMaintClear_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 20),
    _SlbStatSpMaintClear_Type()
)
slbStatSpMaintClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbStatSpMaintClear.setStatus("current")
_SlbStatSpMaintOOSFinPktDrops_Type = Counter32
_SlbStatSpMaintOOSFinPktDrops_Object = MibTableColumn
slbStatSpMaintOOSFinPktDrops = _SlbStatSpMaintOOSFinPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 21),
    _SlbStatSpMaintOOSFinPktDrops_Type()
)
slbStatSpMaintOOSFinPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintOOSFinPktDrops.setStatus("current")
_SlbStatSpMaintSymSessions_Type = Counter32
_SlbStatSpMaintSymSessions_Object = MibTableColumn
slbStatSpMaintSymSessions = _SlbStatSpMaintSymSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 22),
    _SlbStatSpMaintSymSessions_Type()
)
slbStatSpMaintSymSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymSessions.setStatus("current")
_SlbStatSpMaintSymValidSegments_Type = Counter32
_SlbStatSpMaintSymValidSegments_Object = MibTableColumn
slbStatSpMaintSymValidSegments = _SlbStatSpMaintSymValidSegments_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 23),
    _SlbStatSpMaintSymValidSegments_Type()
)
slbStatSpMaintSymValidSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymValidSegments.setStatus("current")
_SlbStatSpMaintSymFragSessions_Type = Counter32
_SlbStatSpMaintSymFragSessions_Object = MibTableColumn
slbStatSpMaintSymFragSessions = _SlbStatSpMaintSymFragSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 24),
    _SlbStatSpMaintSymFragSessions_Type()
)
slbStatSpMaintSymFragSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymFragSessions.setStatus("current")
_SlbStatSpMaintSymSegAllocFails_Type = Counter32
_SlbStatSpMaintSymSegAllocFails_Object = MibTableColumn
slbStatSpMaintSymSegAllocFails = _SlbStatSpMaintSymSegAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 25),
    _SlbStatSpMaintSymSegAllocFails_Type()
)
slbStatSpMaintSymSegAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymSegAllocFails.setStatus("current")
_SlbStatSpMaintSymBufferAllocFails_Type = Counter32
_SlbStatSpMaintSymBufferAllocFails_Object = MibTableColumn
slbStatSpMaintSymBufferAllocFails = _SlbStatSpMaintSymBufferAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 26),
    _SlbStatSpMaintSymBufferAllocFails_Type()
)
slbStatSpMaintSymBufferAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymBufferAllocFails.setStatus("current")
_SlbStatSpMaintSymConnAllocFails_Type = Counter32
_SlbStatSpMaintSymConnAllocFails_Object = MibTableColumn
slbStatSpMaintSymConnAllocFails = _SlbStatSpMaintSymConnAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 27),
    _SlbStatSpMaintSymConnAllocFails_Type()
)
slbStatSpMaintSymConnAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymConnAllocFails.setStatus("current")
_SlbStatSpMaintSymInvalidBuffers_Type = Counter32
_SlbStatSpMaintSymInvalidBuffers_Object = MibTableColumn
slbStatSpMaintSymInvalidBuffers = _SlbStatSpMaintSymInvalidBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 28),
    _SlbStatSpMaintSymInvalidBuffers_Type()
)
slbStatSpMaintSymInvalidBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymInvalidBuffers.setStatus("current")
_SlbStatSpMaintSymSegReallocFails_Type = Counter32
_SlbStatSpMaintSymSegReallocFails_Object = MibTableColumn
slbStatSpMaintSymSegReallocFails = _SlbStatSpMaintSymSegReallocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 29),
    _SlbStatSpMaintSymSegReallocFails_Type()
)
slbStatSpMaintSymSegReallocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymSegReallocFails.setStatus("current")
_SlbStatSpMaintSymPacketsIn_Type = Counter32
_SlbStatSpMaintSymPacketsIn_Object = MibTableColumn
slbStatSpMaintSymPacketsIn = _SlbStatSpMaintSymPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 30),
    _SlbStatSpMaintSymPacketsIn_Type()
)
slbStatSpMaintSymPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymPacketsIn.setStatus("current")
_SlbStatSpMaintSymPacketsWithNoData_Type = Counter32
_SlbStatSpMaintSymPacketsWithNoData_Object = MibTableColumn
slbStatSpMaintSymPacketsWithNoData = _SlbStatSpMaintSymPacketsWithNoData_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 31),
    _SlbStatSpMaintSymPacketsWithNoData_Type()
)
slbStatSpMaintSymPacketsWithNoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymPacketsWithNoData.setStatus("current")
_SlbStatSpMaintSymTcpPackets_Type = Counter32
_SlbStatSpMaintSymTcpPackets_Object = MibTableColumn
slbStatSpMaintSymTcpPackets = _SlbStatSpMaintSymTcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 32),
    _SlbStatSpMaintSymTcpPackets_Type()
)
slbStatSpMaintSymTcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymTcpPackets.setStatus("current")
_SlbStatSpMaintSymUdpPackets_Type = Counter32
_SlbStatSpMaintSymUdpPackets_Object = MibTableColumn
slbStatSpMaintSymUdpPackets = _SlbStatSpMaintSymUdpPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 33),
    _SlbStatSpMaintSymUdpPackets_Type()
)
slbStatSpMaintSymUdpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymUdpPackets.setStatus("current")
_SlbStatSpMaintSymIcmpPackets_Type = Counter32
_SlbStatSpMaintSymIcmpPackets_Object = MibTableColumn
slbStatSpMaintSymIcmpPackets = _SlbStatSpMaintSymIcmpPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 34),
    _SlbStatSpMaintSymIcmpPackets_Type()
)
slbStatSpMaintSymIcmpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymIcmpPackets.setStatus("current")
_SlbStatSpMaintSymOtherPackets_Type = Counter32
_SlbStatSpMaintSymOtherPackets_Object = MibTableColumn
slbStatSpMaintSymOtherPackets = _SlbStatSpMaintSymOtherPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 35),
    _SlbStatSpMaintSymOtherPackets_Type()
)
slbStatSpMaintSymOtherPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymOtherPackets.setStatus("current")
_SlbStatSpMaintSymMatchCount_Type = Counter32
_SlbStatSpMaintSymMatchCount_Object = MibTableColumn
slbStatSpMaintSymMatchCount = _SlbStatSpMaintSymMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 36),
    _SlbStatSpMaintSymMatchCount_Type()
)
slbStatSpMaintSymMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymMatchCount.setStatus("current")
_SlbStatSpMaintSymFetchErrors_Type = Counter32
_SlbStatSpMaintSymFetchErrors_Object = MibTableColumn
slbStatSpMaintSymFetchErrors = _SlbStatSpMaintSymFetchErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 37),
    _SlbStatSpMaintSymFetchErrors_Type()
)
slbStatSpMaintSymFetchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymFetchErrors.setStatus("current")
_SlbStatSpMaintSymTruncPayloadToMp_Type = Counter32
_SlbStatSpMaintSymTruncPayloadToMp_Object = MibTableColumn
slbStatSpMaintSymTruncPayloadToMp = _SlbStatSpMaintSymTruncPayloadToMp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 38),
    _SlbStatSpMaintSymTruncPayloadToMp_Type()
)
slbStatSpMaintSymTruncPayloadToMp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymTruncPayloadToMp.setStatus("current")
_SlbStatSpMaintSymPacketsInFastPath_Type = Counter32
_SlbStatSpMaintSymPacketsInFastPath_Object = MibTableColumn
slbStatSpMaintSymPacketsInFastPath = _SlbStatSpMaintSymPacketsInFastPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 5, 1, 39),
    _SlbStatSpMaintSymPacketsInFastPath_Type()
)
slbStatSpMaintSymPacketsInFastPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpMaintSymPacketsInFastPath.setStatus("current")
_SlbStatSpAuxSessTable_Object = MibTable
slbStatSpAuxSessTable = _SlbStatSpAuxSessTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 6)
)
if mibBuilder.loadTexts:
    slbStatSpAuxSessTable.setStatus("current")
_SlbStatSpAuxSessEntry_Object = MibTableRow
slbStatSpAuxSessEntry = _SlbStatSpAuxSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 6, 1)
)
slbStatSpAuxSessEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatSpAuxSessSpIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatSpAuxSessIndex"),
)
if mibBuilder.loadTexts:
    slbStatSpAuxSessEntry.setStatus("current")
_SlbStatSpAuxSessSpIndex_Type = Integer32
_SlbStatSpAuxSessSpIndex_Object = MibTableColumn
slbStatSpAuxSessSpIndex = _SlbStatSpAuxSessSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 6, 1, 1),
    _SlbStatSpAuxSessSpIndex_Type()
)
slbStatSpAuxSessSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpAuxSessSpIndex.setStatus("current")
_SlbStatSpAuxSessIndex_Type = Integer32
_SlbStatSpAuxSessIndex_Object = MibTableColumn
slbStatSpAuxSessIndex = _SlbStatSpAuxSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 6, 1, 2),
    _SlbStatSpAuxSessIndex_Type()
)
slbStatSpAuxSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpAuxSessIndex.setStatus("current")
_SlbStatSpAuxSessCurConn_Type = Gauge32
_SlbStatSpAuxSessCurConn_Object = MibTableColumn
slbStatSpAuxSessCurConn = _SlbStatSpAuxSessCurConn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 6, 1, 3),
    _SlbStatSpAuxSessCurConn_Type()
)
slbStatSpAuxSessCurConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpAuxSessCurConn.setStatus("current")
_SlbStatSpAuxSessMaxConn_Type = Integer32
_SlbStatSpAuxSessMaxConn_Object = MibTableColumn
slbStatSpAuxSessMaxConn = _SlbStatSpAuxSessMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 6, 1, 4),
    _SlbStatSpAuxSessMaxConn_Type()
)
slbStatSpAuxSessMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpAuxSessMaxConn.setStatus("current")
_SlbStatSpAuxSessAllocFails_Type = Counter32
_SlbStatSpAuxSessAllocFails_Object = MibTableColumn
slbStatSpAuxSessAllocFails = _SlbStatSpAuxSessAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 1, 6, 1, 5),
    _SlbStatSpAuxSessAllocFails_Type()
)
slbStatSpAuxSessAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatSpAuxSessAllocFails.setStatus("current")
_SlbStatRServerTable_Object = MibTable
slbStatRServerTable = _SlbStatRServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 2)
)
if mibBuilder.loadTexts:
    slbStatRServerTable.setStatus("current")
_SlbStatRServerEntry_Object = MibTableRow
slbStatRServerEntry = _SlbStatRServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 2, 1)
)
slbStatRServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatRServerIndex"),
)
if mibBuilder.loadTexts:
    slbStatRServerEntry.setStatus("current")
_SlbStatRServerIndex_Type = Integer32
_SlbStatRServerIndex_Object = MibTableColumn
slbStatRServerIndex = _SlbStatRServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 2, 1, 1),
    _SlbStatRServerIndex_Type()
)
slbStatRServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerIndex.setStatus("current")
_SlbStatRServerCurrSessions_Type = Gauge32
_SlbStatRServerCurrSessions_Object = MibTableColumn
slbStatRServerCurrSessions = _SlbStatRServerCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 2, 1, 2),
    _SlbStatRServerCurrSessions_Type()
)
slbStatRServerCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerCurrSessions.setStatus("current")
_SlbStatRServerTotalSessions_Type = Counter32
_SlbStatRServerTotalSessions_Object = MibTableColumn
slbStatRServerTotalSessions = _SlbStatRServerTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 2, 1, 3),
    _SlbStatRServerTotalSessions_Type()
)
slbStatRServerTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerTotalSessions.setStatus("current")
_SlbStatRServerFailures_Type = Counter32
_SlbStatRServerFailures_Object = MibTableColumn
slbStatRServerFailures = _SlbStatRServerFailures_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 2, 1, 4),
    _SlbStatRServerFailures_Type()
)
slbStatRServerFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerFailures.setStatus("current")
_SlbStatRServerHighestSessions_Type = Counter32
_SlbStatRServerHighestSessions_Object = MibTableColumn
slbStatRServerHighestSessions = _SlbStatRServerHighestSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 2, 1, 5),
    _SlbStatRServerHighestSessions_Type()
)
slbStatRServerHighestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerHighestSessions.setStatus("current")
_SlbStatRServerHCOctetsLow32_Type = Counter32
_SlbStatRServerHCOctetsLow32_Object = MibTableColumn
slbStatRServerHCOctetsLow32 = _SlbStatRServerHCOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 2, 1, 6),
    _SlbStatRServerHCOctetsLow32_Type()
)
slbStatRServerHCOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerHCOctetsLow32.setStatus("current")
_SlbStatRServerHCOctetsHigh32_Type = Counter32
_SlbStatRServerHCOctetsHigh32_Object = MibTableColumn
slbStatRServerHCOctetsHigh32 = _SlbStatRServerHCOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 2, 1, 7),
    _SlbStatRServerHCOctetsHigh32_Type()
)
slbStatRServerHCOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerHCOctetsHigh32.setStatus("current")
_SlbStatRServerHCOctets_Type = Counter64
_SlbStatRServerHCOctets_Object = MibTableColumn
slbStatRServerHCOctets = _SlbStatRServerHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 2, 1, 8),
    _SlbStatRServerHCOctets_Type()
)
slbStatRServerHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerHCOctets.setStatus("current")
_SlbStatGroupTable_Object = MibTable
slbStatGroupTable = _SlbStatGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 3)
)
if mibBuilder.loadTexts:
    slbStatGroupTable.setStatus("current")
_SlbStatGroupEntry_Object = MibTableRow
slbStatGroupEntry = _SlbStatGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 3, 1)
)
slbStatGroupEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatGroupIndex"),
)
if mibBuilder.loadTexts:
    slbStatGroupEntry.setStatus("current")
_SlbStatGroupIndex_Type = Integer32
_SlbStatGroupIndex_Object = MibTableColumn
slbStatGroupIndex = _SlbStatGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 3, 1, 1),
    _SlbStatGroupIndex_Type()
)
slbStatGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupIndex.setStatus("current")
_SlbStatGroupCurrSessions_Type = Gauge32
_SlbStatGroupCurrSessions_Object = MibTableColumn
slbStatGroupCurrSessions = _SlbStatGroupCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 3, 1, 2),
    _SlbStatGroupCurrSessions_Type()
)
slbStatGroupCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupCurrSessions.setStatus("current")
_SlbStatGroupTotalSessions_Type = Counter32
_SlbStatGroupTotalSessions_Object = MibTableColumn
slbStatGroupTotalSessions = _SlbStatGroupTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 3, 1, 3),
    _SlbStatGroupTotalSessions_Type()
)
slbStatGroupTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupTotalSessions.setStatus("current")
_SlbStatGroupHighestSessions_Type = Counter32
_SlbStatGroupHighestSessions_Object = MibTableColumn
slbStatGroupHighestSessions = _SlbStatGroupHighestSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 3, 1, 4),
    _SlbStatGroupHighestSessions_Type()
)
slbStatGroupHighestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupHighestSessions.setStatus("current")
_SlbStatGroupHCOctetsLow32_Type = Counter32
_SlbStatGroupHCOctetsLow32_Object = MibTableColumn
slbStatGroupHCOctetsLow32 = _SlbStatGroupHCOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 3, 1, 5),
    _SlbStatGroupHCOctetsLow32_Type()
)
slbStatGroupHCOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupHCOctetsLow32.setStatus("current")
_SlbStatGroupHCOctetsHigh32_Type = Counter32
_SlbStatGroupHCOctetsHigh32_Object = MibTableColumn
slbStatGroupHCOctetsHigh32 = _SlbStatGroupHCOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 3, 1, 6),
    _SlbStatGroupHCOctetsHigh32_Type()
)
slbStatGroupHCOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupHCOctetsHigh32.setStatus("current")
_SlbStatGroupHCOctets_Type = Counter64
_SlbStatGroupHCOctets_Object = MibTableColumn
slbStatGroupHCOctets = _SlbStatGroupHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 3, 1, 7),
    _SlbStatGroupHCOctets_Type()
)
slbStatGroupHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupHCOctets.setStatus("current")
_SlbStatGroupWlmUpdates_Type = Counter32
_SlbStatGroupWlmUpdates_Object = MibTableColumn
slbStatGroupWlmUpdates = _SlbStatGroupWlmUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 3, 1, 8),
    _SlbStatGroupWlmUpdates_Type()
)
slbStatGroupWlmUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupWlmUpdates.setStatus("current")
_SlbStatVServerTable_Object = MibTable
slbStatVServerTable = _SlbStatVServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4)
)
if mibBuilder.loadTexts:
    slbStatVServerTable.setStatus("current")
_SlbStatVServerEntry_Object = MibTableRow
slbStatVServerEntry = _SlbStatVServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4, 1)
)
slbStatVServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatVServerIndex"),
)
if mibBuilder.loadTexts:
    slbStatVServerEntry.setStatus("current")
_SlbStatVServerIndex_Type = Integer32
_SlbStatVServerIndex_Object = MibTableColumn
slbStatVServerIndex = _SlbStatVServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4, 1, 1),
    _SlbStatVServerIndex_Type()
)
slbStatVServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerIndex.setStatus("current")
_SlbStatVServerCurrSessions_Type = Gauge32
_SlbStatVServerCurrSessions_Object = MibTableColumn
slbStatVServerCurrSessions = _SlbStatVServerCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4, 1, 2),
    _SlbStatVServerCurrSessions_Type()
)
slbStatVServerCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerCurrSessions.setStatus("current")
_SlbStatVServerTotalSessions_Type = Counter32
_SlbStatVServerTotalSessions_Object = MibTableColumn
slbStatVServerTotalSessions = _SlbStatVServerTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4, 1, 3),
    _SlbStatVServerTotalSessions_Type()
)
slbStatVServerTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerTotalSessions.setStatus("current")
_SlbStatVServerHighestSessions_Type = Counter32
_SlbStatVServerHighestSessions_Object = MibTableColumn
slbStatVServerHighestSessions = _SlbStatVServerHighestSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4, 1, 4),
    _SlbStatVServerHighestSessions_Type()
)
slbStatVServerHighestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHighestSessions.setStatus("current")
_SlbStatVServerHCOctetsLow32_Type = Counter32
_SlbStatVServerHCOctetsLow32_Object = MibTableColumn
slbStatVServerHCOctetsLow32 = _SlbStatVServerHCOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4, 1, 5),
    _SlbStatVServerHCOctetsLow32_Type()
)
slbStatVServerHCOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHCOctetsLow32.setStatus("current")
_SlbStatVServerHCOctetsHigh32_Type = Counter32
_SlbStatVServerHCOctetsHigh32_Object = MibTableColumn
slbStatVServerHCOctetsHigh32 = _SlbStatVServerHCOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4, 1, 6),
    _SlbStatVServerHCOctetsHigh32_Type()
)
slbStatVServerHCOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHCOctetsHigh32.setStatus("current")
_SlbStatVServerHeaderHits_Type = Counter32
_SlbStatVServerHeaderHits_Object = MibTableColumn
slbStatVServerHeaderHits = _SlbStatVServerHeaderHits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4, 1, 8),
    _SlbStatVServerHeaderHits_Type()
)
slbStatVServerHeaderHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHeaderHits.setStatus("current")
_SlbStatVServerHeaderMisses_Type = Counter32
_SlbStatVServerHeaderMisses_Object = MibTableColumn
slbStatVServerHeaderMisses = _SlbStatVServerHeaderMisses_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4, 1, 9),
    _SlbStatVServerHeaderMisses_Type()
)
slbStatVServerHeaderMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHeaderMisses.setStatus("current")
_SlbStatVServerHeaderTotalSessions_Type = Counter32
_SlbStatVServerHeaderTotalSessions_Object = MibTableColumn
slbStatVServerHeaderTotalSessions = _SlbStatVServerHeaderTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4, 1, 10),
    _SlbStatVServerHeaderTotalSessions_Type()
)
slbStatVServerHeaderTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHeaderTotalSessions.setStatus("current")
_SlbStatVServerCookieRewrites_Type = Counter32
_SlbStatVServerCookieRewrites_Object = MibTableColumn
slbStatVServerCookieRewrites = _SlbStatVServerCookieRewrites_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4, 1, 11),
    _SlbStatVServerCookieRewrites_Type()
)
slbStatVServerCookieRewrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerCookieRewrites.setStatus("current")
_SlbStatVServerCookieInserts_Type = Counter32
_SlbStatVServerCookieInserts_Object = MibTableColumn
slbStatVServerCookieInserts = _SlbStatVServerCookieInserts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4, 1, 12),
    _SlbStatVServerCookieInserts_Type()
)
slbStatVServerCookieInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerCookieInserts.setStatus("current")
_SlbStatVServerHCOctets_Type = Counter64
_SlbStatVServerHCOctets_Object = MibTableColumn
slbStatVServerHCOctets = _SlbStatVServerHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4, 1, 13),
    _SlbStatVServerHCOctets_Type()
)
slbStatVServerHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHCOctets.setStatus("current")
_SlbStatVServerIpAddress_Type = DisplayString
_SlbStatVServerIpAddress_Object = MibTableColumn
slbStatVServerIpAddress = _SlbStatVServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 4, 1, 14),
    _SlbStatVServerIpAddress_Type()
)
slbStatVServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerIpAddress.setStatus("current")
_SlbMaintStats_ObjectIdentity = ObjectIdentity
slbMaintStats = _SlbMaintStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5)
)
_SlbStatMaintMaximumSessions_Type = Integer32
_SlbStatMaintMaximumSessions_Object = MibScalar
slbStatMaintMaximumSessions = _SlbStatMaintMaximumSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 1),
    _SlbStatMaintMaximumSessions_Type()
)
slbStatMaintMaximumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintMaximumSessions.setStatus("current")
_SlbStatMaintCurBindings_Type = Gauge32
_SlbStatMaintCurBindings_Object = MibScalar
slbStatMaintCurBindings = _SlbStatMaintCurBindings_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 2),
    _SlbStatMaintCurBindings_Type()
)
slbStatMaintCurBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintCurBindings.setStatus("current")
_SlbStatMaintCurBindings4Seconds_Type = Gauge32
_SlbStatMaintCurBindings4Seconds_Object = MibScalar
slbStatMaintCurBindings4Seconds = _SlbStatMaintCurBindings4Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 3),
    _SlbStatMaintCurBindings4Seconds_Type()
)
slbStatMaintCurBindings4Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintCurBindings4Seconds.setStatus("current")
_SlbStatMaintCurBindings64Seconds_Type = Gauge32
_SlbStatMaintCurBindings64Seconds_Object = MibScalar
slbStatMaintCurBindings64Seconds = _SlbStatMaintCurBindings64Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 4),
    _SlbStatMaintCurBindings64Seconds_Type()
)
slbStatMaintCurBindings64Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintCurBindings64Seconds.setStatus("current")
_SlbStatMaintTerminatedSessions_Type = Counter32
_SlbStatMaintTerminatedSessions_Object = MibScalar
slbStatMaintTerminatedSessions = _SlbStatMaintTerminatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 5),
    _SlbStatMaintTerminatedSessions_Type()
)
slbStatMaintTerminatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintTerminatedSessions.setStatus("current")
_SlbStatMaintAllocFailures_Type = Counter32
_SlbStatMaintAllocFailures_Object = MibScalar
slbStatMaintAllocFailures = _SlbStatMaintAllocFailures_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 6),
    _SlbStatMaintAllocFailures_Type()
)
slbStatMaintAllocFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintAllocFailures.setStatus("current")
_SlbStatMaintNonTcpFrames_Type = Counter32
_SlbStatMaintNonTcpFrames_Object = MibScalar
slbStatMaintNonTcpFrames = _SlbStatMaintNonTcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 7),
    _SlbStatMaintNonTcpFrames_Type()
)
slbStatMaintNonTcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintNonTcpFrames.setStatus("current")
_SlbStatMaintTcpFragments_Type = Counter32
_SlbStatMaintTcpFragments_Object = MibScalar
slbStatMaintTcpFragments = _SlbStatMaintTcpFragments_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 8),
    _SlbStatMaintTcpFragments_Type()
)
slbStatMaintTcpFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintTcpFragments.setStatus("current")
_SlbStatMaintUdpDatagrams_Type = Counter32
_SlbStatMaintUdpDatagrams_Object = MibScalar
slbStatMaintUdpDatagrams = _SlbStatMaintUdpDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 9),
    _SlbStatMaintUdpDatagrams_Type()
)
slbStatMaintUdpDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintUdpDatagrams.setStatus("current")
_SlbIncorrectVirtServs_Type = Counter32
_SlbIncorrectVirtServs_Object = MibScalar
slbIncorrectVirtServs = _SlbIncorrectVirtServs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 10),
    _SlbIncorrectVirtServs_Type()
)
slbIncorrectVirtServs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbIncorrectVirtServs.setStatus("current")
_SlbIncorrectVports_Type = Counter32
_SlbIncorrectVports_Object = MibScalar
slbIncorrectVports = _SlbIncorrectVports_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 11),
    _SlbIncorrectVports_Type()
)
slbIncorrectVports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbIncorrectVports.setStatus("current")
_SlbNoRealServs_Type = Counter32
_SlbNoRealServs_Object = MibScalar
slbNoRealServs = _SlbNoRealServs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 12),
    _SlbNoRealServs_Type()
)
slbNoRealServs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNoRealServs.setStatus("current")
_SlbStatMaintBackupServActs_Type = Counter32
_SlbStatMaintBackupServActs_Object = MibScalar
slbStatMaintBackupServActs = _SlbStatMaintBackupServActs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 13),
    _SlbStatMaintBackupServActs_Type()
)
slbStatMaintBackupServActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintBackupServActs.setStatus("current")
_SlbStatMaintOverflowServActs_Type = Counter32
_SlbStatMaintOverflowServActs_Object = MibScalar
slbStatMaintOverflowServActs = _SlbStatMaintOverflowServActs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 14),
    _SlbStatMaintOverflowServActs_Type()
)
slbStatMaintOverflowServActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintOverflowServActs.setStatus("current")
_SlbStatMaintFilteredDeniedFrames_Type = Counter32
_SlbStatMaintFilteredDeniedFrames_Object = MibScalar
slbStatMaintFilteredDeniedFrames = _SlbStatMaintFilteredDeniedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 15),
    _SlbStatMaintFilteredDeniedFrames_Type()
)
slbStatMaintFilteredDeniedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintFilteredDeniedFrames.setStatus("current")
_SlbStatMaintLandAttacks_Type = Counter32
_SlbStatMaintLandAttacks_Object = MibScalar
slbStatMaintLandAttacks = _SlbStatMaintLandAttacks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 16),
    _SlbStatMaintLandAttacks_Type()
)
slbStatMaintLandAttacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintLandAttacks.setStatus("current")
_SlbStatMaintIpFragTotalSessions_Type = Counter32
_SlbStatMaintIpFragTotalSessions_Object = MibScalar
slbStatMaintIpFragTotalSessions = _SlbStatMaintIpFragTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 17),
    _SlbStatMaintIpFragTotalSessions_Type()
)
slbStatMaintIpFragTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintIpFragTotalSessions.setStatus("current")
_SlbStatMaintIpFragCurSessions_Type = Gauge32
_SlbStatMaintIpFragCurSessions_Object = MibScalar
slbStatMaintIpFragCurSessions = _SlbStatMaintIpFragCurSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 18),
    _SlbStatMaintIpFragCurSessions_Type()
)
slbStatMaintIpFragCurSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintIpFragCurSessions.setStatus("current")
_SlbStatMaintIpFragDiscards_Type = Counter32
_SlbStatMaintIpFragDiscards_Object = MibScalar
slbStatMaintIpFragDiscards = _SlbStatMaintIpFragDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 19),
    _SlbStatMaintIpFragDiscards_Type()
)
slbStatMaintIpFragDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintIpFragDiscards.setStatus("current")
_SlbStatMaintIpFragTableFull_Type = Counter32
_SlbStatMaintIpFragTableFull_Object = MibScalar
slbStatMaintIpFragTableFull = _SlbStatMaintIpFragTableFull_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 20),
    _SlbStatMaintIpFragTableFull_Type()
)
slbStatMaintIpFragTableFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintIpFragTableFull.setStatus("current")
_SlbStatMaintIp6CurrSessions_Type = Counter32
_SlbStatMaintIp6CurrSessions_Object = MibScalar
slbStatMaintIp6CurrSessions = _SlbStatMaintIp6CurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 21),
    _SlbStatMaintIp6CurrSessions_Type()
)
slbStatMaintIp6CurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintIp6CurrSessions.setStatus("current")
_SlbIncorrectIp6Vip_Type = Counter32
_SlbIncorrectIp6Vip_Object = MibScalar
slbIncorrectIp6Vip = _SlbIncorrectIp6Vip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 22),
    _SlbIncorrectIp6Vip_Type()
)
slbIncorrectIp6Vip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbIncorrectIp6Vip.setStatus("current")
_SlbIncorrectIp6Vports_Type = Counter32
_SlbIncorrectIp6Vports_Object = MibScalar
slbIncorrectIp6Vports = _SlbIncorrectIp6Vports_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 23),
    _SlbIncorrectIp6Vports_Type()
)
slbIncorrectIp6Vports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbIncorrectIp6Vports.setStatus("current")
_SlbStatMaintIp6PktDropped_Type = Counter32
_SlbStatMaintIp6PktDropped_Object = MibScalar
slbStatMaintIp6PktDropped = _SlbStatMaintIp6PktDropped_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 24),
    _SlbStatMaintIp6PktDropped_Type()
)
slbStatMaintIp6PktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintIp6PktDropped.setStatus("current")
_SlbStatMaintOOSFinPktDrops_Type = Counter32
_SlbStatMaintOOSFinPktDrops_Object = MibScalar
slbStatMaintOOSFinPktDrops = _SlbStatMaintOOSFinPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 25),
    _SlbStatMaintOOSFinPktDrops_Type()
)
slbStatMaintOOSFinPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintOOSFinPktDrops.setStatus("current")
_SlbStatMaintSymSessions_Type = Counter32
_SlbStatMaintSymSessions_Object = MibScalar
slbStatMaintSymSessions = _SlbStatMaintSymSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 26),
    _SlbStatMaintSymSessions_Type()
)
slbStatMaintSymSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymSessions.setStatus("current")
_SlbStatMaintSymValidSegments_Type = Counter32
_SlbStatMaintSymValidSegments_Object = MibScalar
slbStatMaintSymValidSegments = _SlbStatMaintSymValidSegments_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 27),
    _SlbStatMaintSymValidSegments_Type()
)
slbStatMaintSymValidSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymValidSegments.setStatus("current")
_SlbStatMaintSymFragSessions_Type = Counter32
_SlbStatMaintSymFragSessions_Object = MibScalar
slbStatMaintSymFragSessions = _SlbStatMaintSymFragSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 28),
    _SlbStatMaintSymFragSessions_Type()
)
slbStatMaintSymFragSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymFragSessions.setStatus("current")
_SlbStatMaintSymSegAllocFails_Type = Counter32
_SlbStatMaintSymSegAllocFails_Object = MibScalar
slbStatMaintSymSegAllocFails = _SlbStatMaintSymSegAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 29),
    _SlbStatMaintSymSegAllocFails_Type()
)
slbStatMaintSymSegAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymSegAllocFails.setStatus("current")
_SlbStatMaintSymBufferAllocFails_Type = Counter32
_SlbStatMaintSymBufferAllocFails_Object = MibScalar
slbStatMaintSymBufferAllocFails = _SlbStatMaintSymBufferAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 30),
    _SlbStatMaintSymBufferAllocFails_Type()
)
slbStatMaintSymBufferAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymBufferAllocFails.setStatus("current")
_SlbStatMaintSymConnAllocFails_Type = Counter32
_SlbStatMaintSymConnAllocFails_Object = MibScalar
slbStatMaintSymConnAllocFails = _SlbStatMaintSymConnAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 31),
    _SlbStatMaintSymConnAllocFails_Type()
)
slbStatMaintSymConnAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymConnAllocFails.setStatus("current")
_SlbStatMaintSymInvalidBuffers_Type = Counter32
_SlbStatMaintSymInvalidBuffers_Object = MibScalar
slbStatMaintSymInvalidBuffers = _SlbStatMaintSymInvalidBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 32),
    _SlbStatMaintSymInvalidBuffers_Type()
)
slbStatMaintSymInvalidBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymInvalidBuffers.setStatus("current")
_SlbStatMaintSymSegReallocFails_Type = Counter32
_SlbStatMaintSymSegReallocFails_Object = MibScalar
slbStatMaintSymSegReallocFails = _SlbStatMaintSymSegReallocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 33),
    _SlbStatMaintSymSegReallocFails_Type()
)
slbStatMaintSymSegReallocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymSegReallocFails.setStatus("current")
_SlbStatMaintSymPacketsIn_Type = Counter32
_SlbStatMaintSymPacketsIn_Object = MibScalar
slbStatMaintSymPacketsIn = _SlbStatMaintSymPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 34),
    _SlbStatMaintSymPacketsIn_Type()
)
slbStatMaintSymPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymPacketsIn.setStatus("current")
_SlbStatMaintSymPacketsWithNoData_Type = Counter32
_SlbStatMaintSymPacketsWithNoData_Object = MibScalar
slbStatMaintSymPacketsWithNoData = _SlbStatMaintSymPacketsWithNoData_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 35),
    _SlbStatMaintSymPacketsWithNoData_Type()
)
slbStatMaintSymPacketsWithNoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymPacketsWithNoData.setStatus("current")
_SlbStatMaintSymTcpPackets_Type = Counter32
_SlbStatMaintSymTcpPackets_Object = MibScalar
slbStatMaintSymTcpPackets = _SlbStatMaintSymTcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 36),
    _SlbStatMaintSymTcpPackets_Type()
)
slbStatMaintSymTcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymTcpPackets.setStatus("current")
_SlbStatMaintSymUdpPackets_Type = Counter32
_SlbStatMaintSymUdpPackets_Object = MibScalar
slbStatMaintSymUdpPackets = _SlbStatMaintSymUdpPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 37),
    _SlbStatMaintSymUdpPackets_Type()
)
slbStatMaintSymUdpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymUdpPackets.setStatus("current")
_SlbStatMaintSymIcmpPackets_Type = Counter32
_SlbStatMaintSymIcmpPackets_Object = MibScalar
slbStatMaintSymIcmpPackets = _SlbStatMaintSymIcmpPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 38),
    _SlbStatMaintSymIcmpPackets_Type()
)
slbStatMaintSymIcmpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymIcmpPackets.setStatus("current")
_SlbStatMaintSymOtherPackets_Type = Counter32
_SlbStatMaintSymOtherPackets_Object = MibScalar
slbStatMaintSymOtherPackets = _SlbStatMaintSymOtherPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 39),
    _SlbStatMaintSymOtherPackets_Type()
)
slbStatMaintSymOtherPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymOtherPackets.setStatus("current")
_SlbStatMaintSymMatchCount_Type = Counter32
_SlbStatMaintSymMatchCount_Object = MibScalar
slbStatMaintSymMatchCount = _SlbStatMaintSymMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 40),
    _SlbStatMaintSymMatchCount_Type()
)
slbStatMaintSymMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymMatchCount.setStatus("current")
_SlbStatMaintSymFetchErrors_Type = Counter32
_SlbStatMaintSymFetchErrors_Object = MibScalar
slbStatMaintSymFetchErrors = _SlbStatMaintSymFetchErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 41),
    _SlbStatMaintSymFetchErrors_Type()
)
slbStatMaintSymFetchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymFetchErrors.setStatus("current")
_SlbStatMaintSymTruncPayloadToMp_Type = Counter32
_SlbStatMaintSymTruncPayloadToMp_Object = MibScalar
slbStatMaintSymTruncPayloadToMp = _SlbStatMaintSymTruncPayloadToMp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 42),
    _SlbStatMaintSymTruncPayloadToMp_Type()
)
slbStatMaintSymTruncPayloadToMp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymTruncPayloadToMp.setStatus("current")
_SlbStatMaintSymPacketsInFastPath_Type = Counter32
_SlbStatMaintSymPacketsInFastPath_Object = MibScalar
slbStatMaintSymPacketsInFastPath = _SlbStatMaintSymPacketsInFastPath_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 5, 43),
    _SlbStatMaintSymPacketsInFastPath_Type()
)
slbStatMaintSymPacketsInFastPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintSymPacketsInFastPath.setStatus("current")
_FilterStats_ObjectIdentity = ObjectIdentity
filterStats = _FilterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 6)
)
_FltStatTable_Object = MibTable
fltStatTable = _FltStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 6, 1)
)
if mibBuilder.loadTexts:
    fltStatTable.setStatus("current")
_FltStatTableEntry_Object = MibTableRow
fltStatTableEntry = _FltStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 6, 1, 1)
)
fltStatTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "fltStatFltIndex"),
)
if mibBuilder.loadTexts:
    fltStatTableEntry.setStatus("current")
_FltStatFltIndex_Type = Integer32
_FltStatFltIndex_Object = MibTableColumn
fltStatFltIndex = _FltStatFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 6, 1, 1, 1),
    _FltStatFltIndex_Type()
)
fltStatFltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatFltIndex.setStatus("current")
_FltStatFltFirings_Type = Counter32
_FltStatFltFirings_Object = MibTableColumn
fltStatFltFirings = _FltStatFltFirings_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 6, 1, 1, 2),
    _FltStatFltFirings_Type()
)
fltStatFltFirings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatFltFirings.setStatus("current")
_GslbStats_ObjectIdentity = ObjectIdentity
gslbStats = _GslbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7)
)
_GslbStatRemRealServerTable_Object = MibTable
gslbStatRemRealServerTable = _GslbStatRemRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 1)
)
if mibBuilder.loadTexts:
    gslbStatRemRealServerTable.setStatus("current")
_GslbStatRemRealServerEntry_Object = MibTableRow
gslbStatRemRealServerEntry = _GslbStatRemRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 1, 1)
)
gslbStatRemRealServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbStatRemRealServerIndex"),
)
if mibBuilder.loadTexts:
    gslbStatRemRealServerEntry.setStatus("current")
_GslbStatRemRealServerIndex_Type = Integer32
_GslbStatRemRealServerIndex_Object = MibTableColumn
gslbStatRemRealServerIndex = _GslbStatRemRealServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 1, 1, 1),
    _GslbStatRemRealServerIndex_Type()
)
gslbStatRemRealServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemRealServerIndex.setStatus("current")
_GslbStatRemRealServerDnsHandoffs_Type = Counter32
_GslbStatRemRealServerDnsHandoffs_Object = MibTableColumn
gslbStatRemRealServerDnsHandoffs = _GslbStatRemRealServerDnsHandoffs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 1, 1, 2),
    _GslbStatRemRealServerDnsHandoffs_Type()
)
gslbStatRemRealServerDnsHandoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemRealServerDnsHandoffs.setStatus("current")
_GslbStatRemRealServerHttpRedirs_Type = Counter32
_GslbStatRemRealServerHttpRedirs_Object = MibTableColumn
gslbStatRemRealServerHttpRedirs = _GslbStatRemRealServerHttpRedirs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 1, 1, 3),
    _GslbStatRemRealServerHttpRedirs_Type()
)
gslbStatRemRealServerHttpRedirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemRealServerHttpRedirs.setStatus("current")
_GslbMaintStats_ObjectIdentity = ObjectIdentity
gslbMaintStats = _GslbMaintStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2)
)
_GslbStatMaintInGoodSiteUpdates_Type = Counter32
_GslbStatMaintInGoodSiteUpdates_Object = MibScalar
gslbStatMaintInGoodSiteUpdates = _GslbStatMaintInGoodSiteUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 1),
    _GslbStatMaintInGoodSiteUpdates_Type()
)
gslbStatMaintInGoodSiteUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintInGoodSiteUpdates.setStatus("current")
_GslbStatMaintInBadSiteUpdates_Type = Counter32
_GslbStatMaintInBadSiteUpdates_Object = MibScalar
gslbStatMaintInBadSiteUpdates = _GslbStatMaintInBadSiteUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 2),
    _GslbStatMaintInBadSiteUpdates_Type()
)
gslbStatMaintInBadSiteUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintInBadSiteUpdates.setStatus("current")
_GslbStatMaintOutSiteUpdates_Type = Counter32
_GslbStatMaintOutSiteUpdates_Object = MibScalar
gslbStatMaintOutSiteUpdates = _GslbStatMaintOutSiteUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 3),
    _GslbStatMaintOutSiteUpdates_Type()
)
gslbStatMaintOutSiteUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintOutSiteUpdates.setStatus("current")
_GslbStatMaintInGoodSiteUpdates2_Type = Counter32
_GslbStatMaintInGoodSiteUpdates2_Object = MibScalar
gslbStatMaintInGoodSiteUpdates2 = _GslbStatMaintInGoodSiteUpdates2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 4),
    _GslbStatMaintInGoodSiteUpdates2_Type()
)
gslbStatMaintInGoodSiteUpdates2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintInGoodSiteUpdates2.setStatus("current")
_GslbStatMaintOutSiteUpdates2_Type = Counter32
_GslbStatMaintOutSiteUpdates2_Object = MibScalar
gslbStatMaintOutSiteUpdates2 = _GslbStatMaintOutSiteUpdates2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 5),
    _GslbStatMaintOutSiteUpdates2_Type()
)
gslbStatMaintOutSiteUpdates2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintOutSiteUpdates2.setStatus("current")
_GslbStatMaintLocalSitePers_Type = Counter32
_GslbStatMaintLocalSitePers_Object = MibScalar
gslbStatMaintLocalSitePers = _GslbStatMaintLocalSitePers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 8),
    _GslbStatMaintLocalSitePers_Type()
)
gslbStatMaintLocalSitePers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintLocalSitePers.setStatus("current")
_GslbStatMaintInDns_Type = Counter32
_GslbStatMaintInDns_Object = MibScalar
gslbStatMaintInDns = _GslbStatMaintInDns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 10),
    _GslbStatMaintInDns_Type()
)
gslbStatMaintInDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintInDns.setStatus("current")
_GslbStatMaintInBadDns_Type = Counter32
_GslbStatMaintInBadDns_Object = MibScalar
gslbStatMaintInBadDns = _GslbStatMaintInBadDns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 11),
    _GslbStatMaintInBadDns_Type()
)
gslbStatMaintInBadDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintInBadDns.setStatus("current")
_GslbStatMaintOutDns_Type = Counter32
_GslbStatMaintOutDns_Object = MibScalar
gslbStatMaintOutDns = _GslbStatMaintOutDns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 12),
    _GslbStatMaintOutDns_Type()
)
gslbStatMaintOutDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintOutDns.setStatus("current")
_GslbStatMaintInHttp_Type = Counter32
_GslbStatMaintInHttp_Object = MibScalar
gslbStatMaintInHttp = _GslbStatMaintInHttp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 13),
    _GslbStatMaintInHttp_Type()
)
gslbStatMaintInHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintInHttp.setStatus("current")
_GslbStatMaintInBadHttp_Type = Counter32
_GslbStatMaintInBadHttp_Object = MibScalar
gslbStatMaintInBadHttp = _GslbStatMaintInBadHttp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 14),
    _GslbStatMaintInBadHttp_Type()
)
gslbStatMaintInBadHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintInBadHttp.setStatus("current")
_GslbStatMaintOutHttp_Type = Counter32
_GslbStatMaintOutHttp_Object = MibScalar
gslbStatMaintOutHttp = _GslbStatMaintOutHttp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 15),
    _GslbStatMaintOutHttp_Type()
)
gslbStatMaintOutHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintOutHttp.setStatus("current")
_GslbStatMaintNoServer_Type = Counter32
_GslbStatMaintNoServer_Object = MibScalar
gslbStatMaintNoServer = _GslbStatMaintNoServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 16),
    _GslbStatMaintNoServer_Type()
)
gslbStatMaintNoServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintNoServer.setStatus("current")
_GslbStatMaintNoDomain_Type = Counter32
_GslbStatMaintNoDomain_Object = MibScalar
gslbStatMaintNoDomain = _GslbStatMaintNoDomain_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 17),
    _GslbStatMaintNoDomain_Type()
)
gslbStatMaintNoDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintNoDomain.setStatus("current")
_GslbStatMaintHostHits_Type = Counter32
_GslbStatMaintHostHits_Object = MibScalar
gslbStatMaintHostHits = _GslbStatMaintHostHits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 18),
    _GslbStatMaintHostHits_Type()
)
gslbStatMaintHostHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintHostHits.setStatus("current")
_GslbStatMaintRuleHits_Type = Counter32
_GslbStatMaintRuleHits_Object = MibScalar
gslbStatMaintRuleHits = _GslbStatMaintRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 19),
    _GslbStatMaintRuleHits_Type()
)
gslbStatMaintRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintRuleHits.setStatus("current")
_GslbStatMaintVirtHits_Type = Counter32
_GslbStatMaintVirtHits_Object = MibScalar
gslbStatMaintVirtHits = _GslbStatMaintVirtHits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 20),
    _GslbStatMaintVirtHits_Type()
)
gslbStatMaintVirtHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintVirtHits.setStatus("current")
_GslbStatMaintNoServerHost_Type = Counter32
_GslbStatMaintNoServerHost_Object = MibScalar
gslbStatMaintNoServerHost = _GslbStatMaintNoServerHost_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 21),
    _GslbStatMaintNoServerHost_Type()
)
gslbStatMaintNoServerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintNoServerHost.setStatus("current")
_GslbStatMaintNoServerRule_Type = Counter32
_GslbStatMaintNoServerRule_Object = MibScalar
gslbStatMaintNoServerRule = _GslbStatMaintNoServerRule_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 22),
    _GslbStatMaintNoServerRule_Type()
)
gslbStatMaintNoServerRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintNoServerRule.setStatus("current")
_GslbStatMaintNoServerVirt_Type = Counter32
_GslbStatMaintNoServerVirt_Object = MibScalar
gslbStatMaintNoServerVirt = _GslbStatMaintNoServerVirt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 23),
    _GslbStatMaintNoServerVirt_Type()
)
gslbStatMaintNoServerVirt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintNoServerVirt.setStatus("current")


class _GslbStatMaintLastNoResultDomain_Type(DisplayString):
    """Custom type gslbStatMaintLastNoResultDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GslbStatMaintLastNoResultDomain_Type.__name__ = "DisplayString"
_GslbStatMaintLastNoResultDomain_Object = MibScalar
gslbStatMaintLastNoResultDomain = _GslbStatMaintLastNoResultDomain_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 24),
    _GslbStatMaintLastNoResultDomain_Type()
)
gslbStatMaintLastNoResultDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintLastNoResultDomain.setStatus("current")
_GslbStatMaintLastSrcIp_Type = IpAddress
_GslbStatMaintLastSrcIp_Object = MibScalar
gslbStatMaintLastSrcIp = _GslbStatMaintLastSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 25),
    _GslbStatMaintLastSrcIp_Type()
)
gslbStatMaintLastSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintLastSrcIp.setStatus("current")
_GslbStatMaintThresholdHits_Type = Counter32
_GslbStatMaintThresholdHits_Object = MibScalar
gslbStatMaintThresholdHits = _GslbStatMaintThresholdHits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 2, 26),
    _GslbStatMaintThresholdHits_Type()
)
gslbStatMaintThresholdHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintThresholdHits.setStatus("current")
_GslbStatGroupTable_Object = MibTable
gslbStatGroupTable = _GslbStatGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 3)
)
if mibBuilder.loadTexts:
    gslbStatGroupTable.setStatus("current")
_GslbStatGroupEntry_Object = MibTableRow
gslbStatGroupEntry = _GslbStatGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 3, 1)
)
gslbStatGroupEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbStatGroupIndex"),
)
if mibBuilder.loadTexts:
    gslbStatGroupEntry.setStatus("current")
_GslbStatGroupIndex_Type = Integer32
_GslbStatGroupIndex_Object = MibTableColumn
gslbStatGroupIndex = _GslbStatGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 3, 1, 1),
    _GslbStatGroupIndex_Type()
)
gslbStatGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatGroupIndex.setStatus("current")
_GslbStatGroupDnsHandoffs_Type = Counter32
_GslbStatGroupDnsHandoffs_Object = MibTableColumn
gslbStatGroupDnsHandoffs = _GslbStatGroupDnsHandoffs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 3, 1, 2),
    _GslbStatGroupDnsHandoffs_Type()
)
gslbStatGroupDnsHandoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatGroupDnsHandoffs.setStatus("current")
_GslbStatGroupHttpRedirs_Type = Counter32
_GslbStatGroupHttpRedirs_Object = MibTableColumn
gslbStatGroupHttpRedirs = _GslbStatGroupHttpRedirs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 3, 1, 3),
    _GslbStatGroupHttpRedirs_Type()
)
gslbStatGroupHttpRedirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatGroupHttpRedirs.setStatus("current")
_GslbStatVirtServerTable_Object = MibTable
gslbStatVirtServerTable = _GslbStatVirtServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 4)
)
if mibBuilder.loadTexts:
    gslbStatVirtServerTable.setStatus("current")
_GslbStatVirtServerEntry_Object = MibTableRow
gslbStatVirtServerEntry = _GslbStatVirtServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 4, 1)
)
gslbStatVirtServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbStatVirtServerIdx"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbStatVirtServerServiceIdx"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbStatVirtServerRserverIdx"),
)
if mibBuilder.loadTexts:
    gslbStatVirtServerEntry.setStatus("current")
_GslbStatVirtServerIdx_Type = Integer32
_GslbStatVirtServerIdx_Object = MibTableColumn
gslbStatVirtServerIdx = _GslbStatVirtServerIdx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 4, 1, 1),
    _GslbStatVirtServerIdx_Type()
)
gslbStatVirtServerIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatVirtServerIdx.setStatus("current")
_GslbStatVirtServerServiceIdx_Type = Integer32
_GslbStatVirtServerServiceIdx_Object = MibTableColumn
gslbStatVirtServerServiceIdx = _GslbStatVirtServerServiceIdx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 4, 1, 2),
    _GslbStatVirtServerServiceIdx_Type()
)
gslbStatVirtServerServiceIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatVirtServerServiceIdx.setStatus("current")
_GslbStatVirtServerRserverIdx_Type = Integer32
_GslbStatVirtServerRserverIdx_Object = MibTableColumn
gslbStatVirtServerRserverIdx = _GslbStatVirtServerRserverIdx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 4, 1, 3),
    _GslbStatVirtServerRserverIdx_Type()
)
gslbStatVirtServerRserverIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatVirtServerRserverIdx.setStatus("current")
_GslbStatVirtServerVirtPort_Type = Integer32
_GslbStatVirtServerVirtPort_Object = MibTableColumn
gslbStatVirtServerVirtPort = _GslbStatVirtServerVirtPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 4, 1, 4),
    _GslbStatVirtServerVirtPort_Type()
)
gslbStatVirtServerVirtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatVirtServerVirtPort.setStatus("current")
_GslbStatVirtServerIpAddress_Type = IpAddress
_GslbStatVirtServerIpAddress_Object = MibTableColumn
gslbStatVirtServerIpAddress = _GslbStatVirtServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 4, 1, 5),
    _GslbStatVirtServerIpAddress_Type()
)
gslbStatVirtServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatVirtServerIpAddress.setStatus("current")
_GslbStatVirtServerResponseTime_Type = Integer32
_GslbStatVirtServerResponseTime_Object = MibTableColumn
gslbStatVirtServerResponseTime = _GslbStatVirtServerResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 4, 1, 6),
    _GslbStatVirtServerResponseTime_Type()
)
gslbStatVirtServerResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatVirtServerResponseTime.setStatus("current")
_GslbStatVirtServerMinSessAvail_Type = Gauge32
_GslbStatVirtServerMinSessAvail_Object = MibTableColumn
gslbStatVirtServerMinSessAvail = _GslbStatVirtServerMinSessAvail_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 4, 1, 7),
    _GslbStatVirtServerMinSessAvail_Type()
)
gslbStatVirtServerMinSessAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatVirtServerMinSessAvail.setStatus("current")


class _GslbStatVirtServerDname_Type(DisplayString):
    """Custom type gslbStatVirtServerDname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GslbStatVirtServerDname_Type.__name__ = "DisplayString"
_GslbStatVirtServerDname_Object = MibTableColumn
gslbStatVirtServerDname = _GslbStatVirtServerDname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 4, 1, 8),
    _GslbStatVirtServerDname_Type()
)
gslbStatVirtServerDname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatVirtServerDname.setStatus("current")
_GslbStatVirtServerRemSite_Type = Integer32
_GslbStatVirtServerRemSite_Object = MibTableColumn
gslbStatVirtServerRemSite = _GslbStatVirtServerRemSite_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 4, 1, 9),
    _GslbStatVirtServerRemSite_Type()
)
gslbStatVirtServerRemSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatVirtServerRemSite.setStatus("current")
_GslbStatVirtDnsDirect_Type = Counter32
_GslbStatVirtDnsDirect_Object = MibTableColumn
gslbStatVirtDnsDirect = _GslbStatVirtDnsDirect_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 4, 1, 10),
    _GslbStatVirtDnsDirect_Type()
)
gslbStatVirtDnsDirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatVirtDnsDirect.setStatus("current")
_GslbStatRemSiteTable_Object = MibTable
gslbStatRemSiteTable = _GslbStatRemSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 5)
)
if mibBuilder.loadTexts:
    gslbStatRemSiteTable.setStatus("current")
_GslbStatRemSiteTableEntry_Object = MibTableRow
gslbStatRemSiteTableEntry = _GslbStatRemSiteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 5, 1)
)
gslbStatRemSiteTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbStatRemSiteIdx"),
)
if mibBuilder.loadTexts:
    gslbStatRemSiteTableEntry.setStatus("current")
_GslbStatRemSiteIdx_Type = Integer32
_GslbStatRemSiteIdx_Object = MibTableColumn
gslbStatRemSiteIdx = _GslbStatRemSiteIdx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 5, 1, 1),
    _GslbStatRemSiteIdx_Type()
)
gslbStatRemSiteIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemSiteIdx.setStatus("current")
_GslbStatRemSiteOutUpdates_Type = Counter32
_GslbStatRemSiteOutUpdates_Object = MibTableColumn
gslbStatRemSiteOutUpdates = _GslbStatRemSiteOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 5, 1, 2),
    _GslbStatRemSiteOutUpdates_Type()
)
gslbStatRemSiteOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemSiteOutUpdates.setStatus("current")
_GslbStatRemSiteInUpdates_Type = Counter32
_GslbStatRemSiteInUpdates_Object = MibTableColumn
gslbStatRemSiteInUpdates = _GslbStatRemSiteInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 5, 1, 3),
    _GslbStatRemSiteInUpdates_Type()
)
gslbStatRemSiteInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemSiteInUpdates.setStatus("current")
_GslbStatRemSiteOutUpdates2_Type = Counter32
_GslbStatRemSiteOutUpdates2_Object = MibTableColumn
gslbStatRemSiteOutUpdates2 = _GslbStatRemSiteOutUpdates2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 5, 1, 4),
    _GslbStatRemSiteOutUpdates2_Type()
)
gslbStatRemSiteOutUpdates2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemSiteOutUpdates2.setStatus("current")
_GslbStatRemSiteInUpdates2_Type = Counter32
_GslbStatRemSiteInUpdates2_Object = MibTableColumn
gslbStatRemSiteInUpdates2 = _GslbStatRemSiteInUpdates2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 5, 1, 5),
    _GslbStatRemSiteInUpdates2_Type()
)
gslbStatRemSiteInUpdates2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemSiteInUpdates2.setStatus("current")
_GslbStatRemSiteInBadUpdates_Type = Counter32
_GslbStatRemSiteInBadUpdates_Object = MibTableColumn
gslbStatRemSiteInBadUpdates = _GslbStatRemSiteInBadUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 5, 1, 6),
    _GslbStatRemSiteInBadUpdates_Type()
)
gslbStatRemSiteInBadUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemSiteInBadUpdates.setStatus("current")
_GslbStatEnhNetworkTable_Object = MibTable
gslbStatEnhNetworkTable = _GslbStatEnhNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 6)
)
if mibBuilder.loadTexts:
    gslbStatEnhNetworkTable.setStatus("current")
_GslbStatEnhNetworkTableEntry_Object = MibTableRow
gslbStatEnhNetworkTableEntry = _GslbStatEnhNetworkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 6, 1)
)
gslbStatEnhNetworkTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbStatEnhNetworkIdx"),
)
if mibBuilder.loadTexts:
    gslbStatEnhNetworkTableEntry.setStatus("current")
_GslbStatEnhNetworkIdx_Type = Integer32
_GslbStatEnhNetworkIdx_Object = MibTableColumn
gslbStatEnhNetworkIdx = _GslbStatEnhNetworkIdx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 6, 1, 1),
    _GslbStatEnhNetworkIdx_Type()
)
gslbStatEnhNetworkIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatEnhNetworkIdx.setStatus("current")
_GslbStatEnhNetworkHit_Type = Counter32
_GslbStatEnhNetworkHit_Object = MibTableColumn
gslbStatEnhNetworkHit = _GslbStatEnhNetworkHit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 6, 1, 2),
    _GslbStatEnhNetworkHit_Type()
)
gslbStatEnhNetworkHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatEnhNetworkHit.setStatus("current")
_GslbStatRuleTable_Object = MibTable
gslbStatRuleTable = _GslbStatRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7)
)
if mibBuilder.loadTexts:
    gslbStatRuleTable.setStatus("current")
_GslbStatRuleTableEntry_Object = MibTableRow
gslbStatRuleTableEntry = _GslbStatRuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1)
)
gslbStatRuleTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbStatRuleIdx"),
)
if mibBuilder.loadTexts:
    gslbStatRuleTableEntry.setStatus("current")
_GslbStatRuleIdx_Type = Integer32
_GslbStatRuleIdx_Object = MibTableColumn
gslbStatRuleIdx = _GslbStatRuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 1),
    _GslbStatRuleIdx_Type()
)
gslbStatRuleIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleIdx.setStatus("current")
_GslbStatRuleLeastconns_Type = Counter32
_GslbStatRuleLeastconns_Object = MibTableColumn
gslbStatRuleLeastconns = _GslbStatRuleLeastconns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 2),
    _GslbStatRuleLeastconns_Type()
)
gslbStatRuleLeastconns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleLeastconns.setStatus("current")
_GslbStatRuleRoundrobin_Type = Counter32
_GslbStatRuleRoundrobin_Object = MibTableColumn
gslbStatRuleRoundrobin = _GslbStatRuleRoundrobin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 3),
    _GslbStatRuleRoundrobin_Type()
)
gslbStatRuleRoundrobin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleRoundrobin.setStatus("current")
_GslbStatRuleMinmisses_Type = Counter32
_GslbStatRuleMinmisses_Object = MibTableColumn
gslbStatRuleMinmisses = _GslbStatRuleMinmisses_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 4),
    _GslbStatRuleMinmisses_Type()
)
gslbStatRuleMinmisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleMinmisses.setStatus("current")
_GslbStatRuleHash_Type = Counter32
_GslbStatRuleHash_Object = MibTableColumn
gslbStatRuleHash = _GslbStatRuleHash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 5),
    _GslbStatRuleHash_Type()
)
gslbStatRuleHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleHash.setStatus("current")
_GslbStatRuleResponse_Type = Counter32
_GslbStatRuleResponse_Object = MibTableColumn
gslbStatRuleResponse = _GslbStatRuleResponse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 6),
    _GslbStatRuleResponse_Type()
)
gslbStatRuleResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleResponse.setStatus("current")
_GslbStatRuleGeographical_Type = Counter32
_GslbStatRuleGeographical_Object = MibTableColumn
gslbStatRuleGeographical = _GslbStatRuleGeographical_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 7),
    _GslbStatRuleGeographical_Type()
)
gslbStatRuleGeographical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleGeographical.setStatus("current")
_GslbStatRuleNetwork_Type = Counter32
_GslbStatRuleNetwork_Object = MibTableColumn
gslbStatRuleNetwork = _GslbStatRuleNetwork_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 8),
    _GslbStatRuleNetwork_Type()
)
gslbStatRuleNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleNetwork.setStatus("current")
_GslbStatRuleRandom_Type = Counter32
_GslbStatRuleRandom_Object = MibTableColumn
gslbStatRuleRandom = _GslbStatRuleRandom_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 9),
    _GslbStatRuleRandom_Type()
)
gslbStatRuleRandom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleRandom.setStatus("current")
_GslbStatRuleAvailability_Type = Counter32
_GslbStatRuleAvailability_Object = MibTableColumn
gslbStatRuleAvailability = _GslbStatRuleAvailability_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 10),
    _GslbStatRuleAvailability_Type()
)
gslbStatRuleAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleAvailability.setStatus("current")
_GslbStatRuleQos_Type = Counter32
_GslbStatRuleQos_Object = MibTableColumn
gslbStatRuleQos = _GslbStatRuleQos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 11),
    _GslbStatRuleQos_Type()
)
gslbStatRuleQos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleQos.setStatus("current")
_GslbStatRulePersistence_Type = Counter32
_GslbStatRulePersistence_Object = MibTableColumn
gslbStatRulePersistence = _GslbStatRulePersistence_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 12),
    _GslbStatRulePersistence_Type()
)
gslbStatRulePersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRulePersistence.setStatus("current")
_GslbStatRuleLocal_Type = Counter32
_GslbStatRuleLocal_Object = MibTableColumn
gslbStatRuleLocal = _GslbStatRuleLocal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 13),
    _GslbStatRuleLocal_Type()
)
gslbStatRuleLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleLocal.setStatus("current")
_GslbStatRuleAlways_Type = Counter32
_GslbStatRuleAlways_Object = MibTableColumn
gslbStatRuleAlways = _GslbStatRuleAlways_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 14),
    _GslbStatRuleAlways_Type()
)
gslbStatRuleAlways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleAlways.setStatus("current")
_GslbStatRuleRemote_Type = Counter32
_GslbStatRuleRemote_Object = MibTableColumn
gslbStatRuleRemote = _GslbStatRuleRemote_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 15),
    _GslbStatRuleRemote_Type()
)
gslbStatRuleRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleRemote.setStatus("current")
_GslbStatRuleTotal_Type = Counter32
_GslbStatRuleTotal_Object = MibTableColumn
gslbStatRuleTotal = _GslbStatRuleTotal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 7, 1, 16),
    _GslbStatRuleTotal_Type()
)
gslbStatRuleTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRuleTotal.setStatus("current")
_GslbStatGeo_ObjectIdentity = ObjectIdentity
gslbStatGeo = _GslbStatGeo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 8)
)
_GslbStatGeoNA_Type = Counter32
_GslbStatGeoNA_Object = MibScalar
gslbStatGeoNA = _GslbStatGeoNA_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 8, 1),
    _GslbStatGeoNA_Type()
)
gslbStatGeoNA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatGeoNA.setStatus("current")
_GslbStatGeoSA_Type = Counter32
_GslbStatGeoSA_Object = MibScalar
gslbStatGeoSA = _GslbStatGeoSA_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 8, 2),
    _GslbStatGeoSA_Type()
)
gslbStatGeoSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatGeoSA.setStatus("current")
_GslbStatGeoEU_Type = Counter32
_GslbStatGeoEU_Object = MibScalar
gslbStatGeoEU = _GslbStatGeoEU_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 8, 3),
    _GslbStatGeoEU_Type()
)
gslbStatGeoEU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatGeoEU.setStatus("current")
_GslbStatGeoCA_Type = Counter32
_GslbStatGeoCA_Object = MibScalar
gslbStatGeoCA = _GslbStatGeoCA_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 8, 4),
    _GslbStatGeoCA_Type()
)
gslbStatGeoCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatGeoCA.setStatus("current")
_GslbStatGeoPR_Type = Counter32
_GslbStatGeoPR_Object = MibScalar
gslbStatGeoPR = _GslbStatGeoPR_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 8, 5),
    _GslbStatGeoPR_Type()
)
gslbStatGeoPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatGeoPR.setStatus("current")
_GslbStatGeoSS_Type = Counter32
_GslbStatGeoSS_Object = MibScalar
gslbStatGeoSS = _GslbStatGeoSS_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 8, 6),
    _GslbStatGeoSS_Type()
)
gslbStatGeoSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatGeoSS.setStatus("current")
_GslbStatGeoJP_Type = Counter32
_GslbStatGeoJP_Object = MibScalar
gslbStatGeoJP = _GslbStatGeoJP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 8, 7),
    _GslbStatGeoJP_Type()
)
gslbStatGeoJP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatGeoJP.setStatus("current")
_GslbStatGeoTotal_Type = Counter32
_GslbStatGeoTotal_Object = MibScalar
gslbStatGeoTotal = _GslbStatGeoTotal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 8, 8),
    _GslbStatGeoTotal_Type()
)
gslbStatGeoTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatGeoTotal.setStatus("current")
_GslbStatGeoAF_Type = Counter32
_GslbStatGeoAF_Object = MibScalar
gslbStatGeoAF = _GslbStatGeoAF_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 8, 9),
    _GslbStatGeoAF_Type()
)
gslbStatGeoAF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatGeoAF.setStatus("current")
_GslbStatPers_ObjectIdentity = ObjectIdentity
gslbStatPers = _GslbStatPers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 9)
)
_GslbStatPersCurrent_Type = Counter32
_GslbStatPersCurrent_Object = MibScalar
gslbStatPersCurrent = _GslbStatPersCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 9, 1),
    _GslbStatPersCurrent_Type()
)
gslbStatPersCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatPersCurrent.setStatus("current")
_GslbStatPersHiwat_Type = Counter32
_GslbStatPersHiwat_Object = MibScalar
gslbStatPersHiwat = _GslbStatPersHiwat_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 9, 2),
    _GslbStatPersHiwat_Type()
)
gslbStatPersHiwat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatPersHiwat.setStatus("current")
_GslbStatPersMax_Type = Counter32
_GslbStatPersMax_Object = MibScalar
gslbStatPersMax = _GslbStatPersMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 7, 9, 3),
    _GslbStatPersMax_Type()
)
gslbStatPersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatPersMax.setStatus("current")
_WapStats_ObjectIdentity = ObjectIdentity
wapStats = _WapStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8)
)
_RadiusAcctReqsStats_ObjectIdentity = ObjectIdentity
radiusAcctReqsStats = _RadiusAcctReqsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 1)
)
_RadiusAcctReqs_Type = Counter32
_RadiusAcctReqs_Object = MibScalar
radiusAcctReqs = _RadiusAcctReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 1, 1),
    _RadiusAcctReqs_Type()
)
radiusAcctReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctReqs.setStatus("current")
_RadiusAcctWrapReqs_Type = Counter32
_RadiusAcctWrapReqs_Object = MibScalar
radiusAcctWrapReqs = _RadiusAcctWrapReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 1, 2),
    _RadiusAcctWrapReqs_Type()
)
radiusAcctWrapReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctWrapReqs.setStatus("current")
_RadiusAcctStartReqs_Type = Counter32
_RadiusAcctStartReqs_Object = MibScalar
radiusAcctStartReqs = _RadiusAcctStartReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 1, 3),
    _RadiusAcctStartReqs_Type()
)
radiusAcctStartReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctStartReqs.setStatus("current")
_RadiusAcctUpdateReqs_Type = Counter32
_RadiusAcctUpdateReqs_Object = MibScalar
radiusAcctUpdateReqs = _RadiusAcctUpdateReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 1, 4),
    _RadiusAcctUpdateReqs_Type()
)
radiusAcctUpdateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctUpdateReqs.setStatus("current")
_RadiusAcctStopReqs_Type = Counter32
_RadiusAcctStopReqs_Object = MibScalar
radiusAcctStopReqs = _RadiusAcctStopReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 1, 5),
    _RadiusAcctStopReqs_Type()
)
radiusAcctStopReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctStopReqs.setStatus("current")
_RadiusAcctBadReqs_Type = Counter32
_RadiusAcctBadReqs_Object = MibScalar
radiusAcctBadReqs = _RadiusAcctBadReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 1, 6),
    _RadiusAcctBadReqs_Type()
)
radiusAcctBadReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctBadReqs.setStatus("current")
_RadiusAcctAddSessionReqs_Type = Counter32
_RadiusAcctAddSessionReqs_Object = MibScalar
radiusAcctAddSessionReqs = _RadiusAcctAddSessionReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 1, 7),
    _RadiusAcctAddSessionReqs_Type()
)
radiusAcctAddSessionReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctAddSessionReqs.setStatus("current")
_RadiusAcctDeleteSessionReqs_Type = Counter32
_RadiusAcctDeleteSessionReqs_Object = MibScalar
radiusAcctDeleteSessionReqs = _RadiusAcctDeleteSessionReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 1, 8),
    _RadiusAcctDeleteSessionReqs_Type()
)
radiusAcctDeleteSessionReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctDeleteSessionReqs.setStatus("current")
_RadiusAcctReqFailsSPDead_Type = Counter32
_RadiusAcctReqFailsSPDead_Object = MibScalar
radiusAcctReqFailsSPDead = _RadiusAcctReqFailsSPDead_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 1, 10),
    _RadiusAcctReqFailsSPDead_Type()
)
radiusAcctReqFailsSPDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctReqFailsSPDead.setStatus("current")
_RadiusAcctReqFailsDMAFails_Type = Counter32
_RadiusAcctReqFailsDMAFails_Object = MibScalar
radiusAcctReqFailsDMAFails = _RadiusAcctReqFailsDMAFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 1, 11),
    _RadiusAcctReqFailsDMAFails_Type()
)
radiusAcctReqFailsDMAFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctReqFailsDMAFails.setStatus("current")
_RadiusAcctReqWithFramedIp_Type = Counter32
_RadiusAcctReqWithFramedIp_Object = MibScalar
radiusAcctReqWithFramedIp = _RadiusAcctReqWithFramedIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 1, 12),
    _RadiusAcctReqWithFramedIp_Type()
)
radiusAcctReqWithFramedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctReqWithFramedIp.setStatus("current")
_RadiusAcctReqWithoutFramedIp_Type = Counter32
_RadiusAcctReqWithoutFramedIp_Object = MibScalar
radiusAcctReqWithoutFramedIp = _RadiusAcctReqWithoutFramedIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 1, 13),
    _RadiusAcctReqWithoutFramedIp_Type()
)
radiusAcctReqWithoutFramedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctReqWithoutFramedIp.setStatus("current")
_TpcpAddSessReqsStats_ObjectIdentity = ObjectIdentity
tpcpAddSessReqsStats = _TpcpAddSessReqsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 2)
)
_TpcpAddSessReqs_Type = Counter32
_TpcpAddSessReqs_Object = MibScalar
tpcpAddSessReqs = _TpcpAddSessReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 2, 1),
    _TpcpAddSessReqs_Type()
)
tpcpAddSessReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcpAddSessReqs.setStatus("current")
_TpcpAddSessReqsFailsSPDead_Type = Counter32
_TpcpAddSessReqsFailsSPDead_Object = MibScalar
tpcpAddSessReqsFailsSPDead = _TpcpAddSessReqsFailsSPDead_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 2, 3),
    _TpcpAddSessReqsFailsSPDead_Type()
)
tpcpAddSessReqsFailsSPDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcpAddSessReqsFailsSPDead.setStatus("current")
_TpcpDeleteSessReqsStats_ObjectIdentity = ObjectIdentity
tpcpDeleteSessReqsStats = _TpcpDeleteSessReqsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 3)
)
_TpcpDeleteSessReqs_Type = Counter32
_TpcpDeleteSessReqs_Object = MibScalar
tpcpDeleteSessReqs = _TpcpDeleteSessReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 3, 1),
    _TpcpDeleteSessReqs_Type()
)
tpcpDeleteSessReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcpDeleteSessReqs.setStatus("current")
_TpcpDeleteSessReqsFailsSPDead_Type = Counter32
_TpcpDeleteSessReqsFailsSPDead_Object = MibScalar
tpcpDeleteSessReqsFailsSPDead = _TpcpDeleteSessReqsFailsSPDead_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 3, 3),
    _TpcpDeleteSessReqsFailsSPDead_Type()
)
tpcpDeleteSessReqsFailsSPDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcpDeleteSessReqsFailsSPDead.setStatus("current")
_WapRequestToWrongSP_Type = Counter32
_WapRequestToWrongSP_Object = MibScalar
wapRequestToWrongSP = _WapRequestToWrongSP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 8, 4),
    _WapRequestToWrongSP_Type()
)
wapRequestToWrongSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapRequestToWrongSP.setStatus("current")
_FtpStats_ObjectIdentity = ObjectIdentity
ftpStats = _FtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 10)
)
_FtpSlbStatTotal_Type = Counter32
_FtpSlbStatTotal_Object = MibScalar
ftpSlbStatTotal = _FtpSlbStatTotal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 10, 1),
    _FtpSlbStatTotal_Type()
)
ftpSlbStatTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpSlbStatTotal.setStatus("current")
_FtpNatStatTotal_Type = Counter32
_FtpNatStatTotal_Object = MibScalar
ftpNatStatTotal = _FtpNatStatTotal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 10, 2),
    _FtpNatStatTotal_Type()
)
ftpNatStatTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpNatStatTotal.setStatus("current")
_FtpStatActiveNatIndex_Type = Counter32
_FtpStatActiveNatIndex_Object = MibScalar
ftpStatActiveNatIndex = _FtpStatActiveNatIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 10, 3),
    _FtpStatActiveNatIndex_Type()
)
ftpStatActiveNatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatActiveNatIndex.setStatus("current")
_FtpStatNatAckSeqDiff_Type = Counter32
_FtpStatNatAckSeqDiff_Object = MibScalar
ftpStatNatAckSeqDiff = _FtpStatNatAckSeqDiff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 10, 4),
    _FtpStatNatAckSeqDiff_Type()
)
ftpStatNatAckSeqDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatNatAckSeqDiff.setStatus("current")
_FtpStatSlbParseIndex_Type = Counter32
_FtpStatSlbParseIndex_Object = MibScalar
ftpStatSlbParseIndex = _FtpStatSlbParseIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 10, 5),
    _FtpStatSlbParseIndex_Type()
)
ftpStatSlbParseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatSlbParseIndex.setStatus("current")
_FtpStatSlbParseAckSeqDiff_Type = Counter32
_FtpStatSlbParseAckSeqDiff_Object = MibScalar
ftpStatSlbParseAckSeqDiff = _FtpStatSlbParseAckSeqDiff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 10, 6),
    _FtpStatSlbParseAckSeqDiff_Type()
)
ftpStatSlbParseAckSeqDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatSlbParseAckSeqDiff.setStatus("current")
_FtpStatModeSwitchError_Type = Counter32
_FtpStatModeSwitchError_Object = MibScalar
ftpStatModeSwitchError = _FtpStatModeSwitchError_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 10, 7),
    _FtpStatModeSwitchError_Type()
)
ftpStatModeSwitchError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatModeSwitchError.setStatus("current")
_RtspStats_ObjectIdentity = ObjectIdentity
rtspStats = _RtspStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 11)
)
_RtspStatControlConns_Type = Gauge32
_RtspStatControlConns_Object = MibScalar
rtspStatControlConns = _RtspStatControlConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 11, 1),
    _RtspStatControlConns_Type()
)
rtspStatControlConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspStatControlConns.setStatus("current")
_RtspStatUDPStreams_Type = Gauge32
_RtspStatUDPStreams_Object = MibScalar
rtspStatUDPStreams = _RtspStatUDPStreams_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 11, 2),
    _RtspStatUDPStreams_Type()
)
rtspStatUDPStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspStatUDPStreams.setStatus("current")
_RtspStatRedirects_Type = Counter32
_RtspStatRedirects_Object = MibScalar
rtspStatRedirects = _RtspStatRedirects_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 11, 3),
    _RtspStatRedirects_Type()
)
rtspStatRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspStatRedirects.setStatus("current")
_RtspStatConnDenied_Type = Counter32
_RtspStatConnDenied_Object = MibScalar
rtspStatConnDenied = _RtspStatConnDenied_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 11, 4),
    _RtspStatConnDenied_Type()
)
rtspStatConnDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspStatConnDenied.setStatus("current")
_RtspStatAllocFails_Type = Counter32
_RtspStatAllocFails_Object = MibScalar
rtspStatAllocFails = _RtspStatAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 11, 5),
    _RtspStatAllocFails_Type()
)
rtspStatAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspStatAllocFails.setStatus("current")
_RtspStatBufferAllocs_Type = Gauge32
_RtspStatBufferAllocs_Object = MibScalar
rtspStatBufferAllocs = _RtspStatBufferAllocs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 11, 6),
    _RtspStatBufferAllocs_Type()
)
rtspStatBufferAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspStatBufferAllocs.setStatus("current")
_TcpLimitStats_ObjectIdentity = ObjectIdentity
tcpLimitStats = _TcpLimitStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 12)
)
_TcpLimitStatHoldDowns_Type = Counter32
_TcpLimitStatHoldDowns_Object = MibScalar
tcpLimitStatHoldDowns = _TcpLimitStatHoldDowns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 12, 1),
    _TcpLimitStatHoldDowns_Type()
)
tcpLimitStatHoldDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpLimitStatHoldDowns.setStatus("current")
_TcpLimitStatClientEntries_Type = Gauge32
_TcpLimitStatClientEntries_Object = MibScalar
tcpLimitStatClientEntries = _TcpLimitStatClientEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 12, 2),
    _TcpLimitStatClientEntries_Type()
)
tcpLimitStatClientEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpLimitStatClientEntries.setStatus("current")
_UdpLimitStatHoldDowns_Type = Counter32
_UdpLimitStatHoldDowns_Object = MibScalar
udpLimitStatHoldDowns = _UdpLimitStatHoldDowns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 12, 3),
    _UdpLimitStatHoldDowns_Type()
)
udpLimitStatHoldDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpLimitStatHoldDowns.setStatus("current")
_IcmpLimitStatHoldDowns_Type = Counter32
_IcmpLimitStatHoldDowns_Object = MibScalar
icmpLimitStatHoldDowns = _IcmpLimitStatHoldDowns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 12, 4),
    _IcmpLimitStatHoldDowns_Type()
)
icmpLimitStatHoldDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpLimitStatHoldDowns.setStatus("current")
_UdpLimitStatClientEntries_Type = Gauge32
_UdpLimitStatClientEntries_Object = MibScalar
udpLimitStatClientEntries = _UdpLimitStatClientEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 12, 5),
    _UdpLimitStatClientEntries_Type()
)
udpLimitStatClientEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpLimitStatClientEntries.setStatus("current")
_IcmpLimitStatClientEntries_Type = Gauge32
_IcmpLimitStatClientEntries_Object = MibScalar
icmpLimitStatClientEntries = _IcmpLimitStatClientEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 12, 6),
    _IcmpLimitStatClientEntries_Type()
)
icmpLimitStatClientEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpLimitStatClientEntries.setStatus("current")
_DnsSlbStats_ObjectIdentity = ObjectIdentity
dnsSlbStats = _DnsSlbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 13)
)
_DnsSlbStatTCPQueries_Type = Counter32
_DnsSlbStatTCPQueries_Object = MibScalar
dnsSlbStatTCPQueries = _DnsSlbStatTCPQueries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 13, 1),
    _DnsSlbStatTCPQueries_Type()
)
dnsSlbStatTCPQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSlbStatTCPQueries.setStatus("current")
_DnsSlbStatUDPQueries_Type = Counter32
_DnsSlbStatUDPQueries_Object = MibScalar
dnsSlbStatUDPQueries = _DnsSlbStatUDPQueries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 13, 2),
    _DnsSlbStatUDPQueries_Type()
)
dnsSlbStatUDPQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSlbStatUDPQueries.setStatus("current")
_DnsSlbStatInvalidQueries_Type = Counter32
_DnsSlbStatInvalidQueries_Object = MibScalar
dnsSlbStatInvalidQueries = _DnsSlbStatInvalidQueries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 13, 3),
    _DnsSlbStatInvalidQueries_Type()
)
dnsSlbStatInvalidQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSlbStatInvalidQueries.setStatus("current")
_DnsSlbStatMultipleQueries_Type = Counter32
_DnsSlbStatMultipleQueries_Object = MibScalar
dnsSlbStatMultipleQueries = _DnsSlbStatMultipleQueries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 13, 4),
    _DnsSlbStatMultipleQueries_Type()
)
dnsSlbStatMultipleQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSlbStatMultipleQueries.setStatus("current")
_DnsSlbStatDnameParseErrors_Type = Counter32
_DnsSlbStatDnameParseErrors_Object = MibScalar
dnsSlbStatDnameParseErrors = _DnsSlbStatDnameParseErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 13, 5),
    _DnsSlbStatDnameParseErrors_Type()
)
dnsSlbStatDnameParseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSlbStatDnameParseErrors.setStatus("current")
_DnsSlbStatFailedMatches_Type = Counter32
_DnsSlbStatFailedMatches_Object = MibScalar
dnsSlbStatFailedMatches = _DnsSlbStatFailedMatches_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 13, 6),
    _DnsSlbStatFailedMatches_Type()
)
dnsSlbStatFailedMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSlbStatFailedMatches.setStatus("current")
_DnsSlbStatInternalErrors_Type = Counter32
_DnsSlbStatInternalErrors_Object = MibScalar
dnsSlbStatInternalErrors = _DnsSlbStatInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 13, 7),
    _DnsSlbStatInternalErrors_Type()
)
dnsSlbStatInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSlbStatInternalErrors.setStatus("current")


class _SlbStatsClear_Type(Integer32):
    """Custom type slbStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_SlbStatsClear_Type.__name__ = "Integer32"
_SlbStatsClear_Object = MibScalar
slbStatsClear = _SlbStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 15),
    _SlbStatsClear_Type()
)
slbStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbStatsClear.setStatus("current")
_SslSlbStats_ObjectIdentity = ObjectIdentity
sslSlbStats = _SslSlbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 16)
)
_SslSlbStatSessIdAllocFails_Type = Counter32
_SslSlbStatSessIdAllocFails_Object = MibScalar
sslSlbStatSessIdAllocFails = _SslSlbStatSessIdAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 16, 1),
    _SslSlbStatSessIdAllocFails_Type()
)
sslSlbStatSessIdAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSlbStatSessIdAllocFails.setStatus("current")
_SslSlbStatCurSessions_Type = Gauge32
_SslSlbStatCurSessions_Object = MibScalar
sslSlbStatCurSessions = _SslSlbStatCurSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 16, 2),
    _SslSlbStatCurSessions_Type()
)
sslSlbStatCurSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSlbStatCurSessions.setStatus("current")
_SslSlbStatTotalSessions_Type = Counter32
_SslSlbStatTotalSessions_Object = MibScalar
sslSlbStatTotalSessions = _SslSlbStatTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 16, 3),
    _SslSlbStatTotalSessions_Type()
)
sslSlbStatTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSlbStatTotalSessions.setStatus("current")
_SslSlbStatHighestSessions_Type = Counter32
_SslSlbStatHighestSessions_Object = MibScalar
sslSlbStatHighestSessions = _SslSlbStatHighestSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 16, 4),
    _SslSlbStatHighestSessions_Type()
)
sslSlbStatHighestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSlbStatHighestSessions.setStatus("current")
_SslSlbStatUniqCurSessions_Type = Gauge32
_SslSlbStatUniqCurSessions_Object = MibScalar
sslSlbStatUniqCurSessions = _SslSlbStatUniqCurSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 16, 5),
    _SslSlbStatUniqCurSessions_Type()
)
sslSlbStatUniqCurSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSlbStatUniqCurSessions.setStatus("current")
_SslSlbStatUniqTotalSessions_Type = Counter32
_SslSlbStatUniqTotalSessions_Object = MibScalar
sslSlbStatUniqTotalSessions = _SslSlbStatUniqTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 16, 6),
    _SslSlbStatUniqTotalSessions_Type()
)
sslSlbStatUniqTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSlbStatUniqTotalSessions.setStatus("current")
_SslSlbStatUniqHighestSessions_Type = Counter32
_SslSlbStatUniqHighestSessions_Object = MibScalar
sslSlbStatUniqHighestSessions = _SslSlbStatUniqHighestSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 16, 7),
    _SslSlbStatUniqHighestSessions_Type()
)
sslSlbStatUniqHighestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSlbStatUniqHighestSessions.setStatus("current")
_SslSlbStatPersistPortCurSessions_Type = Gauge32
_SslSlbStatPersistPortCurSessions_Object = MibScalar
sslSlbStatPersistPortCurSessions = _SslSlbStatPersistPortCurSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 16, 8),
    _SslSlbStatPersistPortCurSessions_Type()
)
sslSlbStatPersistPortCurSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSlbStatPersistPortCurSessions.setStatus("current")
_SslSlbStatPersistPortTotalSessions_Type = Counter32
_SslSlbStatPersistPortTotalSessions_Object = MibScalar
sslSlbStatPersistPortTotalSessions = _SslSlbStatPersistPortTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 16, 9),
    _SslSlbStatPersistPortTotalSessions_Type()
)
sslSlbStatPersistPortTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSlbStatPersistPortTotalSessions.setStatus("current")
_SslSlbStatPersistPortHighestSessions_Type = Counter32
_SslSlbStatPersistPortHighestSessions_Object = MibScalar
sslSlbStatPersistPortHighestSessions = _SslSlbStatPersistPortHighestSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 16, 10),
    _SslSlbStatPersistPortHighestSessions_Type()
)
sslSlbStatPersistPortHighestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslSlbStatPersistPortHighestSessions.setStatus("current")
_SlbStatAuxSessTable_Object = MibTable
slbStatAuxSessTable = _SlbStatAuxSessTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 17)
)
if mibBuilder.loadTexts:
    slbStatAuxSessTable.setStatus("current")
_SlbStatAuxSessEntry_Object = MibTableRow
slbStatAuxSessEntry = _SlbStatAuxSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 17, 1)
)
slbStatAuxSessEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatAuxSessIndex"),
)
if mibBuilder.loadTexts:
    slbStatAuxSessEntry.setStatus("current")
_SlbStatAuxSessIndex_Type = Integer32
_SlbStatAuxSessIndex_Object = MibTableColumn
slbStatAuxSessIndex = _SlbStatAuxSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 17, 1, 1),
    _SlbStatAuxSessIndex_Type()
)
slbStatAuxSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatAuxSessIndex.setStatus("current")
_SlbStatAuxSessCurConn_Type = Gauge32
_SlbStatAuxSessCurConn_Object = MibTableColumn
slbStatAuxSessCurConn = _SlbStatAuxSessCurConn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 17, 1, 2),
    _SlbStatAuxSessCurConn_Type()
)
slbStatAuxSessCurConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatAuxSessCurConn.setStatus("current")
_SlbStatAuxSessMaxConn_Type = Integer32
_SlbStatAuxSessMaxConn_Object = MibTableColumn
slbStatAuxSessMaxConn = _SlbStatAuxSessMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 17, 1, 3),
    _SlbStatAuxSessMaxConn_Type()
)
slbStatAuxSessMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatAuxSessMaxConn.setStatus("current")
_SlbStatAuxSessAllocFails_Type = Counter32
_SlbStatAuxSessAllocFails_Object = MibTableColumn
slbStatAuxSessAllocFails = _SlbStatAuxSessAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 17, 1, 4),
    _SlbStatAuxSessAllocFails_Type()
)
slbStatAuxSessAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatAuxSessAllocFails.setStatus("current")
_SlbStatVirtServiceTable_Object = MibTable
slbStatVirtServiceTable = _SlbStatVirtServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 18)
)
if mibBuilder.loadTexts:
    slbStatVirtServiceTable.setStatus("current")
_SlbStatVirtServiceEntry_Object = MibTableRow
slbStatVirtServiceEntry = _SlbStatVirtServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 18, 1)
)
slbStatVirtServiceEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatVirtServerIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatVirtServiceIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatRealServerIndex"),
)
if mibBuilder.loadTexts:
    slbStatVirtServiceEntry.setStatus("current")
_SlbStatVirtServerIndex_Type = Integer32
_SlbStatVirtServerIndex_Object = MibTableColumn
slbStatVirtServerIndex = _SlbStatVirtServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 18, 1, 1),
    _SlbStatVirtServerIndex_Type()
)
slbStatVirtServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVirtServerIndex.setStatus("current")
_SlbStatVirtServiceIndex_Type = Integer32
_SlbStatVirtServiceIndex_Object = MibTableColumn
slbStatVirtServiceIndex = _SlbStatVirtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 18, 1, 2),
    _SlbStatVirtServiceIndex_Type()
)
slbStatVirtServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVirtServiceIndex.setStatus("current")
_SlbStatRealServerIndex_Type = Integer32
_SlbStatRealServerIndex_Object = MibTableColumn
slbStatRealServerIndex = _SlbStatRealServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 18, 1, 3),
    _SlbStatRealServerIndex_Type()
)
slbStatRealServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRealServerIndex.setStatus("current")
_SlbStatVirtServiceCurrSessions_Type = Gauge32
_SlbStatVirtServiceCurrSessions_Object = MibTableColumn
slbStatVirtServiceCurrSessions = _SlbStatVirtServiceCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 18, 1, 4),
    _SlbStatVirtServiceCurrSessions_Type()
)
slbStatVirtServiceCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVirtServiceCurrSessions.setStatus("current")
_SlbStatVirtServiceTotalSessions_Type = Counter32
_SlbStatVirtServiceTotalSessions_Object = MibTableColumn
slbStatVirtServiceTotalSessions = _SlbStatVirtServiceTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 18, 1, 5),
    _SlbStatVirtServiceTotalSessions_Type()
)
slbStatVirtServiceTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVirtServiceTotalSessions.setStatus("current")
_SlbStatVirtServiceHighestSessions_Type = Counter32
_SlbStatVirtServiceHighestSessions_Object = MibTableColumn
slbStatVirtServiceHighestSessions = _SlbStatVirtServiceHighestSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 18, 1, 6),
    _SlbStatVirtServiceHighestSessions_Type()
)
slbStatVirtServiceHighestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVirtServiceHighestSessions.setStatus("current")
_SlbStatVirtServiceHCOctetsLow32_Type = Counter32
_SlbStatVirtServiceHCOctetsLow32_Object = MibTableColumn
slbStatVirtServiceHCOctetsLow32 = _SlbStatVirtServiceHCOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 18, 1, 7),
    _SlbStatVirtServiceHCOctetsLow32_Type()
)
slbStatVirtServiceHCOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVirtServiceHCOctetsLow32.setStatus("current")
_SlbStatVirtServiceHCOctetsHigh32_Type = Counter32
_SlbStatVirtServiceHCOctetsHigh32_Object = MibTableColumn
slbStatVirtServiceHCOctetsHigh32 = _SlbStatVirtServiceHCOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 18, 1, 8),
    _SlbStatVirtServiceHCOctetsHigh32_Type()
)
slbStatVirtServiceHCOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVirtServiceHCOctetsHigh32.setStatus("current")
_SlbStatVirtServiceHCOctets_Type = Counter64
_SlbStatVirtServiceHCOctets_Object = MibTableColumn
slbStatVirtServiceHCOctets = _SlbStatVirtServiceHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 18, 1, 9),
    _SlbStatVirtServiceHCOctets_Type()
)
slbStatVirtServiceHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVirtServiceHCOctets.setStatus("current")
_SipStats_ObjectIdentity = ObjectIdentity
sipStats = _SipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 20)
)
_SipTotalClientParseErrors_Type = Counter32
_SipTotalClientParseErrors_Object = MibScalar
sipTotalClientParseErrors = _SipTotalClientParseErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 20, 1),
    _SipTotalClientParseErrors_Type()
)
sipTotalClientParseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTotalClientParseErrors.setStatus("current")
_SipTotalServerParseErrors_Type = Counter32
_SipTotalServerParseErrors_Object = MibScalar
sipTotalServerParseErrors = _SipTotalServerParseErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 20, 2),
    _SipTotalServerParseErrors_Type()
)
sipTotalServerParseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTotalServerParseErrors.setStatus("current")
_SipTotalUnknownMethodReq_Type = Counter32
_SipTotalUnknownMethodReq_Object = MibScalar
sipTotalUnknownMethodReq = _SipTotalUnknownMethodReq_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 20, 3),
    _SipTotalUnknownMethodReq_Type()
)
sipTotalUnknownMethodReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTotalUnknownMethodReq.setStatus("current")
_SipTotalIncompleteMsgs_Type = Counter32
_SipTotalIncompleteMsgs_Object = MibScalar
sipTotalIncompleteMsgs = _SipTotalIncompleteMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 20, 4),
    _SipTotalIncompleteMsgs_Type()
)
sipTotalIncompleteMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTotalIncompleteMsgs.setStatus("current")
_SipTotalSdpNatPackets_Type = Counter32
_SipTotalSdpNatPackets_Object = MibScalar
sipTotalSdpNatPackets = _SipTotalSdpNatPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 20, 5),
    _SipTotalSdpNatPackets_Type()
)
sipTotalSdpNatPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTotalSdpNatPackets.setStatus("current")
_WlmStats_ObjectIdentity = ObjectIdentity
wlmStats = _WlmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21)
)
_SlbStatWlmTable_Object = MibTable
slbStatWlmTable = _SlbStatWlmTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1)
)
if mibBuilder.loadTexts:
    slbStatWlmTable.setStatus("current")
_SlbStatWlmEntry_Object = MibTableRow
slbStatWlmEntry = _SlbStatWlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1)
)
slbStatWlmEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbStatWlmIndex"),
)
if mibBuilder.loadTexts:
    slbStatWlmEntry.setStatus("current")
_SlbStatWlmIndex_Type = Integer32
_SlbStatWlmIndex_Object = MibTableColumn
slbStatWlmIndex = _SlbStatWlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 1),
    _SlbStatWlmIndex_Type()
)
slbStatWlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmIndex.setStatus("current")
_SlbStatWlmRegReq_Type = Counter32
_SlbStatWlmRegReq_Object = MibTableColumn
slbStatWlmRegReq = _SlbStatWlmRegReq_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 2),
    _SlbStatWlmRegReq_Type()
)
slbStatWlmRegReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmRegReq.setStatus("current")
_SlbStatWlmRegRep_Type = Counter32
_SlbStatWlmRegRep_Object = MibTableColumn
slbStatWlmRegRep = _SlbStatWlmRegRep_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 3),
    _SlbStatWlmRegRep_Type()
)
slbStatWlmRegRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmRegRep.setStatus("current")
_SlbStatWlmRegRepErr_Type = Counter32
_SlbStatWlmRegRepErr_Object = MibTableColumn
slbStatWlmRegRepErr = _SlbStatWlmRegRepErr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 4),
    _SlbStatWlmRegRepErr_Type()
)
slbStatWlmRegRepErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmRegRepErr.setStatus("current")
_SlbStatWlmDeregReq_Type = Counter32
_SlbStatWlmDeregReq_Object = MibTableColumn
slbStatWlmDeregReq = _SlbStatWlmDeregReq_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 5),
    _SlbStatWlmDeregReq_Type()
)
slbStatWlmDeregReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmDeregReq.setStatus("current")
_SlbStatWlmDeregRep_Type = Counter32
_SlbStatWlmDeregRep_Object = MibTableColumn
slbStatWlmDeregRep = _SlbStatWlmDeregRep_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 6),
    _SlbStatWlmDeregRep_Type()
)
slbStatWlmDeregRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmDeregRep.setStatus("current")
_SlbStatWlmDeregRepErr_Type = Counter32
_SlbStatWlmDeregRepErr_Object = MibTableColumn
slbStatWlmDeregRepErr = _SlbStatWlmDeregRepErr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 7),
    _SlbStatWlmDeregRepErr_Type()
)
slbStatWlmDeregRepErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmDeregRepErr.setStatus("current")
_SlbStatWlmLbStateReq_Type = Counter32
_SlbStatWlmLbStateReq_Object = MibTableColumn
slbStatWlmLbStateReq = _SlbStatWlmLbStateReq_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 8),
    _SlbStatWlmLbStateReq_Type()
)
slbStatWlmLbStateReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmLbStateReq.setStatus("current")
_SlbStatWlmLbStateRep_Type = Counter32
_SlbStatWlmLbStateRep_Object = MibTableColumn
slbStatWlmLbStateRep = _SlbStatWlmLbStateRep_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 9),
    _SlbStatWlmLbStateRep_Type()
)
slbStatWlmLbStateRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmLbStateRep.setStatus("current")
_SlbStatWlmLbStateRepErr_Type = Counter32
_SlbStatWlmLbStateRepErr_Object = MibTableColumn
slbStatWlmLbStateRepErr = _SlbStatWlmLbStateRepErr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 10),
    _SlbStatWlmLbStateRepErr_Type()
)
slbStatWlmLbStateRepErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmLbStateRepErr.setStatus("current")
_SlbStatWlmMembStateReq_Type = Counter32
_SlbStatWlmMembStateReq_Object = MibTableColumn
slbStatWlmMembStateReq = _SlbStatWlmMembStateReq_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 11),
    _SlbStatWlmMembStateReq_Type()
)
slbStatWlmMembStateReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmMembStateReq.setStatus("current")
_SlbStatWlmMembStateRep_Type = Counter32
_SlbStatWlmMembStateRep_Object = MibTableColumn
slbStatWlmMembStateRep = _SlbStatWlmMembStateRep_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 12),
    _SlbStatWlmMembStateRep_Type()
)
slbStatWlmMembStateRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmMembStateRep.setStatus("current")
_SlbStatWlmMembStateRepErr_Type = Counter32
_SlbStatWlmMembStateRepErr_Object = MibTableColumn
slbStatWlmMembStateRepErr = _SlbStatWlmMembStateRepErr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 13),
    _SlbStatWlmMembStateRepErr_Type()
)
slbStatWlmMembStateRepErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmMembStateRepErr.setStatus("current")
_SlbStatWlmWtMsgRecv_Type = Counter32
_SlbStatWlmWtMsgRecv_Object = MibTableColumn
slbStatWlmWtMsgRecv = _SlbStatWlmWtMsgRecv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 14),
    _SlbStatWlmWtMsgRecv_Type()
)
slbStatWlmWtMsgRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmWtMsgRecv.setStatus("current")
_SlbStatWlmWtMsgParErr_Type = Counter32
_SlbStatWlmWtMsgParErr_Object = MibTableColumn
slbStatWlmWtMsgParErr = _SlbStatWlmWtMsgParErr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 15),
    _SlbStatWlmWtMsgParErr_Type()
)
slbStatWlmWtMsgParErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmWtMsgParErr.setStatus("current")
_SlbStatWlmTotInvalidLb_Type = Counter32
_SlbStatWlmTotInvalidLb_Object = MibTableColumn
slbStatWlmTotInvalidLb = _SlbStatWlmTotInvalidLb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 16),
    _SlbStatWlmTotInvalidLb_Type()
)
slbStatWlmTotInvalidLb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmTotInvalidLb.setStatus("current")
_SlbStatWlmTotInvalidGrp_Type = Counter32
_SlbStatWlmTotInvalidGrp_Object = MibTableColumn
slbStatWlmTotInvalidGrp = _SlbStatWlmTotInvalidGrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 17),
    _SlbStatWlmTotInvalidGrp_Type()
)
slbStatWlmTotInvalidGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmTotInvalidGrp.setStatus("current")
_SlbStatWlmTotInvalidRealSer_Type = Counter32
_SlbStatWlmTotInvalidRealSer_Object = MibTableColumn
slbStatWlmTotInvalidRealSer = _SlbStatWlmTotInvalidRealSer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 18),
    _SlbStatWlmTotInvalidRealSer_Type()
)
slbStatWlmTotInvalidRealSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmTotInvalidRealSer.setStatus("current")
_SlbStatWlmMsgInvalidSASPHeader_Type = Counter32
_SlbStatWlmMsgInvalidSASPHeader_Object = MibTableColumn
slbStatWlmMsgInvalidSASPHeader = _SlbStatWlmMsgInvalidSASPHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 19),
    _SlbStatWlmMsgInvalidSASPHeader_Type()
)
slbStatWlmMsgInvalidSASPHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmMsgInvalidSASPHeader.setStatus("current")
_SlbStatWlmMsgParseErr_Type = Counter32
_SlbStatWlmMsgParseErr_Object = MibTableColumn
slbStatWlmMsgParseErr = _SlbStatWlmMsgParseErr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 20),
    _SlbStatWlmMsgParseErr_Type()
)
slbStatWlmMsgParseErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmMsgParseErr.setStatus("current")
_SlbStatWlmMsgUnsupMsgType_Type = Counter32
_SlbStatWlmMsgUnsupMsgType_Object = MibTableColumn
slbStatWlmMsgUnsupMsgType = _SlbStatWlmMsgUnsupMsgType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 21, 1, 1, 21),
    _SlbStatWlmMsgUnsupMsgType_Type()
)
slbStatWlmMsgUnsupMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatWlmMsgUnsupMsgType.setStatus("current")
_SessMirrorStats_ObjectIdentity = ObjectIdentity
sessMirrorStats = _SessMirrorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22)
)
_SessMirrorTotalCreateSessionMsgRx_Type = Counter32
_SessMirrorTotalCreateSessionMsgRx_Object = MibScalar
sessMirrorTotalCreateSessionMsgRx = _SessMirrorTotalCreateSessionMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 1),
    _SessMirrorTotalCreateSessionMsgRx_Type()
)
sessMirrorTotalCreateSessionMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalCreateSessionMsgRx.setStatus("current")
_SessMirrorTotalCreateSessionMsgTx_Type = Counter32
_SessMirrorTotalCreateSessionMsgTx_Object = MibScalar
sessMirrorTotalCreateSessionMsgTx = _SessMirrorTotalCreateSessionMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 2),
    _SessMirrorTotalCreateSessionMsgTx_Type()
)
sessMirrorTotalCreateSessionMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalCreateSessionMsgTx.setStatus("current")
_SessMirrorTotalCreateDataSessionMsgRx_Type = Counter32
_SessMirrorTotalCreateDataSessionMsgRx_Object = MibScalar
sessMirrorTotalCreateDataSessionMsgRx = _SessMirrorTotalCreateDataSessionMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 3),
    _SessMirrorTotalCreateDataSessionMsgRx_Type()
)
sessMirrorTotalCreateDataSessionMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalCreateDataSessionMsgRx.setStatus("current")
_SessMirrorTotalCreateDataSessionMsgTx_Type = Counter32
_SessMirrorTotalCreateDataSessionMsgTx_Object = MibScalar
sessMirrorTotalCreateDataSessionMsgTx = _SessMirrorTotalCreateDataSessionMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 4),
    _SessMirrorTotalCreateDataSessionMsgTx_Type()
)
sessMirrorTotalCreateDataSessionMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalCreateDataSessionMsgTx.setStatus("current")
_SessMirrorTotalUpdateSessionMsgRx_Type = Counter32
_SessMirrorTotalUpdateSessionMsgRx_Object = MibScalar
sessMirrorTotalUpdateSessionMsgRx = _SessMirrorTotalUpdateSessionMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 5),
    _SessMirrorTotalUpdateSessionMsgRx_Type()
)
sessMirrorTotalUpdateSessionMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalUpdateSessionMsgRx.setStatus("current")
_SessMirrorTotalUpdateSessionMsgTx_Type = Counter32
_SessMirrorTotalUpdateSessionMsgTx_Object = MibScalar
sessMirrorTotalUpdateSessionMsgTx = _SessMirrorTotalUpdateSessionMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 6),
    _SessMirrorTotalUpdateSessionMsgTx_Type()
)
sessMirrorTotalUpdateSessionMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalUpdateSessionMsgTx.setStatus("current")
_SessMirrorTotalUpdateDataSessionMsgRx_Type = Counter32
_SessMirrorTotalUpdateDataSessionMsgRx_Object = MibScalar
sessMirrorTotalUpdateDataSessionMsgRx = _SessMirrorTotalUpdateDataSessionMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 7),
    _SessMirrorTotalUpdateDataSessionMsgRx_Type()
)
sessMirrorTotalUpdateDataSessionMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalUpdateDataSessionMsgRx.setStatus("current")
_SessMirrorTotalUpdateDataSessionMsgTx_Type = Counter32
_SessMirrorTotalUpdateDataSessionMsgTx_Object = MibScalar
sessMirrorTotalUpdateDataSessionMsgTx = _SessMirrorTotalUpdateDataSessionMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 8),
    _SessMirrorTotalUpdateDataSessionMsgTx_Type()
)
sessMirrorTotalUpdateDataSessionMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalUpdateDataSessionMsgTx.setStatus("current")
_SessMirrorTotalDeleteSessionMsgRx_Type = Counter32
_SessMirrorTotalDeleteSessionMsgRx_Object = MibScalar
sessMirrorTotalDeleteSessionMsgRx = _SessMirrorTotalDeleteSessionMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 9),
    _SessMirrorTotalDeleteSessionMsgRx_Type()
)
sessMirrorTotalDeleteSessionMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalDeleteSessionMsgRx.setStatus("current")
_SessMirrorTotalDeleteSessionMsgTx_Type = Counter32
_SessMirrorTotalDeleteSessionMsgTx_Object = MibScalar
sessMirrorTotalDeleteSessionMsgTx = _SessMirrorTotalDeleteSessionMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 10),
    _SessMirrorTotalDeleteSessionMsgTx_Type()
)
sessMirrorTotalDeleteSessionMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalDeleteSessionMsgTx.setStatus("current")
_SessMirrorTotalDeleteDataSessionMsgRx_Type = Counter32
_SessMirrorTotalDeleteDataSessionMsgRx_Object = MibScalar
sessMirrorTotalDeleteDataSessionMsgRx = _SessMirrorTotalDeleteDataSessionMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 11),
    _SessMirrorTotalDeleteDataSessionMsgRx_Type()
)
sessMirrorTotalDeleteDataSessionMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalDeleteDataSessionMsgRx.setStatus("current")
_SessMirrorTotalDeleteDataSessionMsgTx_Type = Counter32
_SessMirrorTotalDeleteDataSessionMsgTx_Object = MibScalar
sessMirrorTotalDeleteDataSessionMsgTx = _SessMirrorTotalDeleteDataSessionMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 12),
    _SessMirrorTotalDeleteDataSessionMsgTx_Type()
)
sessMirrorTotalDeleteDataSessionMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalDeleteDataSessionMsgTx.setStatus("current")
_SessMirrorTotalSessionsCreated_Type = Counter32
_SessMirrorTotalSessionsCreated_Object = MibScalar
sessMirrorTotalSessionsCreated = _SessMirrorTotalSessionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 13),
    _SessMirrorTotalSessionsCreated_Type()
)
sessMirrorTotalSessionsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalSessionsCreated.setStatus("current")
_SessMirrorTotalDataSessionsCreated_Type = Counter32
_SessMirrorTotalDataSessionsCreated_Object = MibScalar
sessMirrorTotalDataSessionsCreated = _SessMirrorTotalDataSessionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 14),
    _SessMirrorTotalDataSessionsCreated_Type()
)
sessMirrorTotalDataSessionsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalDataSessionsCreated.setStatus("current")
_SessMirrorTotalSessionsUpdated_Type = Counter32
_SessMirrorTotalSessionsUpdated_Object = MibScalar
sessMirrorTotalSessionsUpdated = _SessMirrorTotalSessionsUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 15),
    _SessMirrorTotalSessionsUpdated_Type()
)
sessMirrorTotalSessionsUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalSessionsUpdated.setStatus("current")
_SessMirrorTotalDataSessionsUpdated_Type = Counter32
_SessMirrorTotalDataSessionsUpdated_Object = MibScalar
sessMirrorTotalDataSessionsUpdated = _SessMirrorTotalDataSessionsUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 16),
    _SessMirrorTotalDataSessionsUpdated_Type()
)
sessMirrorTotalDataSessionsUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalDataSessionsUpdated.setStatus("current")
_SessMirrorTotalSessionsDeleted_Type = Counter32
_SessMirrorTotalSessionsDeleted_Object = MibScalar
sessMirrorTotalSessionsDeleted = _SessMirrorTotalSessionsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 17),
    _SessMirrorTotalSessionsDeleted_Type()
)
sessMirrorTotalSessionsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalSessionsDeleted.setStatus("current")
_SessMirrorTotalDataSessionsDeleted_Type = Counter32
_SessMirrorTotalDataSessionsDeleted_Object = MibScalar
sessMirrorTotalDataSessionsDeleted = _SessMirrorTotalDataSessionsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 18),
    _SessMirrorTotalDataSessionsDeleted_Type()
)
sessMirrorTotalDataSessionsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorTotalDataSessionsDeleted.setStatus("current")
_SessMirrorSessionTableFullErr_Type = Counter32
_SessMirrorSessionTableFullErr_Object = MibScalar
sessMirrorSessionTableFullErr = _SessMirrorSessionTableFullErr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 19),
    _SessMirrorSessionTableFullErr_Type()
)
sessMirrorSessionTableFullErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorSessionTableFullErr.setStatus("current")
_SessMirrorNoPortErr_Type = Counter32
_SessMirrorNoPortErr_Object = MibScalar
sessMirrorNoPortErr = _SessMirrorNoPortErr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 20),
    _SessMirrorNoPortErr_Type()
)
sessMirrorNoPortErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorNoPortErr.setStatus("current")
_SessMirrorSessionPresentErr_Type = Counter32
_SessMirrorSessionPresentErr_Object = MibScalar
sessMirrorSessionPresentErr = _SessMirrorSessionPresentErr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 21),
    _SessMirrorSessionPresentErr_Type()
)
sessMirrorSessionPresentErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorSessionPresentErr.setStatus("current")
_SessMirrorSessionNotFoundErr_Type = Counter32
_SessMirrorSessionNotFoundErr_Object = MibScalar
sessMirrorSessionNotFoundErr = _SessMirrorSessionNotFoundErr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 22),
    _SessMirrorSessionNotFoundErr_Type()
)
sessMirrorSessionNotFoundErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorSessionNotFoundErr.setStatus("current")
_SessMirrorCtrlSessionNotFoundErr_Type = Counter32
_SessMirrorCtrlSessionNotFoundErr_Object = MibScalar
sessMirrorCtrlSessionNotFoundErr = _SessMirrorCtrlSessionNotFoundErr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 2, 22, 23),
    _SessMirrorCtrlSessionNotFoundErr_Type()
)
sessMirrorCtrlSessionNotFoundErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessMirrorCtrlSessionNotFoundErr.setStatus("current")
_Layer4Info_ObjectIdentity = ObjectIdentity
layer4Info = _Layer4Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3)
)
_SlbRealServerInfoTable_Object = MibTable
slbRealServerInfoTable = _SlbRealServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 1)
)
if mibBuilder.loadTexts:
    slbRealServerInfoTable.setStatus("current")
_SlbRealServerInfoEntry_Object = MibTableRow
slbRealServerInfoEntry = _SlbRealServerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 1, 1)
)
slbRealServerInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbRealServerInfoIndex"),
)
if mibBuilder.loadTexts:
    slbRealServerInfoEntry.setStatus("current")
_SlbRealServerInfoIndex_Type = Integer32
_SlbRealServerInfoIndex_Object = MibTableColumn
slbRealServerInfoIndex = _SlbRealServerInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 1, 1, 1),
    _SlbRealServerInfoIndex_Type()
)
slbRealServerInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoIndex.setStatus("current")
_SlbRealServerInfoIpAddr_Type = IpAddress
_SlbRealServerInfoIpAddr_Object = MibTableColumn
slbRealServerInfoIpAddr = _SlbRealServerInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 1, 1, 2),
    _SlbRealServerInfoIpAddr_Type()
)
slbRealServerInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoIpAddr.setStatus("current")
_SlbRealServerMacAddr_Type = PhysAddress
_SlbRealServerMacAddr_Object = MibTableColumn
slbRealServerMacAddr = _SlbRealServerMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 1, 1, 3),
    _SlbRealServerMacAddr_Type()
)
slbRealServerMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerMacAddr.setStatus("current")
_SlbRealServerInfoSwitchPort_Type = Integer32
_SlbRealServerInfoSwitchPort_Object = MibTableColumn
slbRealServerInfoSwitchPort = _SlbRealServerInfoSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 1, 1, 4),
    _SlbRealServerInfoSwitchPort_Type()
)
slbRealServerInfoSwitchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoSwitchPort.setStatus("current")


class _SlbRealServerInfoHealthLayer_Type(Integer32):
    """Custom type slbRealServerInfoHealthLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("layer1", 1),
          ("layer3", 3),
          ("layer4", 4))
    )


_SlbRealServerInfoHealthLayer_Type.__name__ = "Integer32"
_SlbRealServerInfoHealthLayer_Object = MibTableColumn
slbRealServerInfoHealthLayer = _SlbRealServerInfoHealthLayer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 1, 1, 5),
    _SlbRealServerInfoHealthLayer_Type()
)
slbRealServerInfoHealthLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoHealthLayer.setStatus("current")


class _SlbRealServerInfoOverflow_Type(Integer32):
    """Custom type slbRealServerInfoOverflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("overflow", 1),
          ("no-overflow", 2))
    )


_SlbRealServerInfoOverflow_Type.__name__ = "Integer32"
_SlbRealServerInfoOverflow_Object = MibTableColumn
slbRealServerInfoOverflow = _SlbRealServerInfoOverflow_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 1, 1, 6),
    _SlbRealServerInfoOverflow_Type()
)
slbRealServerInfoOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoOverflow.setStatus("current")


class _SlbRealServerInfoState_Type(Integer32):
    """Custom type slbRealServerInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("running", 2),
          ("failed", 3),
          ("disabled", 4))
    )


_SlbRealServerInfoState_Type.__name__ = "Integer32"
_SlbRealServerInfoState_Object = MibTableColumn
slbRealServerInfoState = _SlbRealServerInfoState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 1, 1, 7),
    _SlbRealServerInfoState_Type()
)
slbRealServerInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoState.setStatus("current")
_SlbRealServerInfoVlan_Type = Integer32
_SlbRealServerInfoVlan_Object = MibTableColumn
slbRealServerInfoVlan = _SlbRealServerInfoVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 1, 1, 8),
    _SlbRealServerInfoVlan_Type()
)
slbRealServerInfoVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoVlan.setStatus("current")
_SlbRealServerRportInfoTable_Object = MibTable
slbRealServerRportInfoTable = _SlbRealServerRportInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 3)
)
if mibBuilder.loadTexts:
    slbRealServerRportInfoTable.setStatus("current")
_SlbRealServerRportInfoEntry_Object = MibTableRow
slbRealServerRportInfoEntry = _SlbRealServerRportInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 3, 1)
)
slbRealServerRportInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbRealServerRportRealIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbRealServerRportServIndex"),
)
if mibBuilder.loadTexts:
    slbRealServerRportInfoEntry.setStatus("current")
_SlbRealServerRportRealIndex_Type = Integer32
_SlbRealServerRportRealIndex_Object = MibTableColumn
slbRealServerRportRealIndex = _SlbRealServerRportRealIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 3, 1, 1),
    _SlbRealServerRportRealIndex_Type()
)
slbRealServerRportRealIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerRportRealIndex.setStatus("current")
_SlbRealServerRportServIndex_Type = Integer32
_SlbRealServerRportServIndex_Object = MibTableColumn
slbRealServerRportServIndex = _SlbRealServerRportServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 3, 1, 2),
    _SlbRealServerRportServIndex_Type()
)
slbRealServerRportServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerRportServIndex.setStatus("current")
_SlbRealServerRportInfoRport_Type = Integer32
_SlbRealServerRportInfoRport_Object = MibTableColumn
slbRealServerRportInfoRport = _SlbRealServerRportInfoRport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 3, 1, 3),
    _SlbRealServerRportInfoRport_Type()
)
slbRealServerRportInfoRport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerRportInfoRport.setStatus("current")


class _SlbRealServerRportInfoState_Type(Integer32):
    """Custom type slbRealServerRportInfoState based on Integer32"""
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


_SlbRealServerRportInfoState_Type.__name__ = "Integer32"
_SlbRealServerRportInfoState_Object = MibTableColumn
slbRealServerRportInfoState = _SlbRealServerRportInfoState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 3, 1, 4),
    _SlbRealServerRportInfoState_Type()
)
slbRealServerRportInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerRportInfoState.setStatus("current")
_SlbVirtServicesInfoTable_Object = MibTable
slbVirtServicesInfoTable = _SlbVirtServicesInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 4)
)
if mibBuilder.loadTexts:
    slbVirtServicesInfoTable.setStatus("current")
_SlbVirtServicesInfoEntry_Object = MibTableRow
slbVirtServicesInfoEntry = _SlbVirtServicesInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 4, 1)
)
slbVirtServicesInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbVirtServicesInfoVirtServIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbVirtServicesInfoSvcIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbVirtServicesInfoRealServIndex"),
)
if mibBuilder.loadTexts:
    slbVirtServicesInfoEntry.setStatus("current")
_SlbVirtServicesInfoVirtServIndex_Type = Integer32
_SlbVirtServicesInfoVirtServIndex_Object = MibTableColumn
slbVirtServicesInfoVirtServIndex = _SlbVirtServicesInfoVirtServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 4, 1, 1),
    _SlbVirtServicesInfoVirtServIndex_Type()
)
slbVirtServicesInfoVirtServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtServicesInfoVirtServIndex.setStatus("current")
_SlbVirtServicesInfoSvcIndex_Type = Integer32
_SlbVirtServicesInfoSvcIndex_Object = MibTableColumn
slbVirtServicesInfoSvcIndex = _SlbVirtServicesInfoSvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 4, 1, 2),
    _SlbVirtServicesInfoSvcIndex_Type()
)
slbVirtServicesInfoSvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtServicesInfoSvcIndex.setStatus("current")
_SlbVirtServicesInfoRealServIndex_Type = Integer32
_SlbVirtServicesInfoRealServIndex_Object = MibTableColumn
slbVirtServicesInfoRealServIndex = _SlbVirtServicesInfoRealServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 4, 1, 3),
    _SlbVirtServicesInfoRealServIndex_Type()
)
slbVirtServicesInfoRealServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtServicesInfoRealServIndex.setStatus("current")
_SlbVirtServicesInfoVport_Type = Integer32
_SlbVirtServicesInfoVport_Object = MibTableColumn
slbVirtServicesInfoVport = _SlbVirtServicesInfoVport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 4, 1, 4),
    _SlbVirtServicesInfoVport_Type()
)
slbVirtServicesInfoVport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtServicesInfoVport.setStatus("current")
_SlbVirtServicesInfoRport_Type = Integer32
_SlbVirtServicesInfoRport_Object = MibTableColumn
slbVirtServicesInfoRport = _SlbVirtServicesInfoRport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 4, 1, 5),
    _SlbVirtServicesInfoRport_Type()
)
slbVirtServicesInfoRport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtServicesInfoRport.setStatus("current")


class _SlbVirtServicesInfoState_Type(Integer32):
    """Custom type slbVirtServicesInfoState based on Integer32"""
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
        *(("blocked", 1),
          ("running", 2),
          ("failed", 3),
          ("disabled", 4))
    )


_SlbVirtServicesInfoState_Type.__name__ = "Integer32"
_SlbVirtServicesInfoState_Object = MibTableColumn
slbVirtServicesInfoState = _SlbVirtServicesInfoState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 4, 1, 6),
    _SlbVirtServicesInfoState_Type()
)
slbVirtServicesInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtServicesInfoState.setStatus("current")
_SlbVirtServicesInfoResponseTime_Type = Integer32
_SlbVirtServicesInfoResponseTime_Object = MibTableColumn
slbVirtServicesInfoResponseTime = _SlbVirtServicesInfoResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 4, 1, 7),
    _SlbVirtServicesInfoResponseTime_Type()
)
slbVirtServicesInfoResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtServicesInfoResponseTime.setStatus("current")
_SlbVirtServicesInfoWeight_Type = Integer32
_SlbVirtServicesInfoWeight_Object = MibTableColumn
slbVirtServicesInfoWeight = _SlbVirtServicesInfoWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 4, 1, 8),
    _SlbVirtServicesInfoWeight_Type()
)
slbVirtServicesInfoWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtServicesInfoWeight.setStatus("current")
_SlbSessionInfo_ObjectIdentity = ObjectIdentity
slbSessionInfo = _SlbSessionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 5)
)


class _SlbSessionInfoState_Type(Integer32):
    """Custom type slbSessionInfoState based on Integer32"""
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
        *(("start", 1),
          ("idle", 2),
          ("inprogress", 3),
          ("complete", 4))
    )


_SlbSessionInfoState_Type.__name__ = "Integer32"
_SlbSessionInfoState_Object = MibScalar
slbSessionInfoState = _SlbSessionInfoState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 5, 1),
    _SlbSessionInfoState_Type()
)
slbSessionInfoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbSessionInfoState.setStatus("current")


class _SlbSessionInfoType_Type(Integer32):
    """Custom type slbSessionInfoType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("cip", 2),
          ("cport", 3),
          ("dip", 4),
          ("dport", 5),
          ("pip", 6),
          ("pport", 7),
          ("filter", 8),
          ("flag", 9),
          ("port", 10),
          ("real", 11))
    )


_SlbSessionInfoType_Type.__name__ = "Integer32"
_SlbSessionInfoType_Object = MibScalar
slbSessionInfoType = _SlbSessionInfoType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 5, 2),
    _SlbSessionInfoType_Type()
)
slbSessionInfoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbSessionInfoType.setStatus("current")
_SlbSessionInfoIpAddr_Type = IpAddress
_SlbSessionInfoIpAddr_Object = MibScalar
slbSessionInfoIpAddr = _SlbSessionInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 5, 3),
    _SlbSessionInfoIpAddr_Type()
)
slbSessionInfoIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbSessionInfoIpAddr.setStatus("current")
_SlbSessionInfoFilterId_Type = Integer32
_SlbSessionInfoFilterId_Object = MibScalar
slbSessionInfoFilterId = _SlbSessionInfoFilterId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 5, 4),
    _SlbSessionInfoFilterId_Type()
)
slbSessionInfoFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbSessionInfoFilterId.setStatus("current")
_SlbSessionInfoPortId_Type = Integer32
_SlbSessionInfoPortId_Object = MibScalar
slbSessionInfoPortId = _SlbSessionInfoPortId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 5, 5),
    _SlbSessionInfoPortId_Type()
)
slbSessionInfoPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbSessionInfoPortId.setStatus("current")


class _SlbSessionInfoFlag_Type(Integer32):
    """Custom type slbSessionInfoFlag based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("eFlag", 1),
          ("lFlag", 2),
          ("nFlag", 3),
          ("pFlag", 4),
          ("sFlag", 5),
          ("tFlag", 6),
          ("uFlag", 7),
          ("wFlag", 8),
          ("ruFlag", 9),
          ("riFlag", 10),
          ("viFlag", 11),
          ("vrFlag", 12),
          ("vsFlag", 13),
          ("vmFlag", 14),
          ("vdFlag", 15),
          ("none", 20))
    )


_SlbSessionInfoFlag_Type.__name__ = "Integer32"
_SlbSessionInfoFlag_Object = MibScalar
slbSessionInfoFlag = _SlbSessionInfoFlag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 5, 6),
    _SlbSessionInfoFlag_Type()
)
slbSessionInfoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbSessionInfoFlag.setStatus("current")


class _SlbSessionInfoStringFormatFlag_Type(Integer32):
    """Custom type slbSessionInfoStringFormatFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("formatted", 1),
          ("none", 2))
    )


_SlbSessionInfoStringFormatFlag_Type.__name__ = "Integer32"
_SlbSessionInfoStringFormatFlag_Object = MibScalar
slbSessionInfoStringFormatFlag = _SlbSessionInfoStringFormatFlag_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 5, 7),
    _SlbSessionInfoStringFormatFlag_Type()
)
slbSessionInfoStringFormatFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbSessionInfoStringFormatFlag.setStatus("current")
_SlbSessionInfoTable_Object = MibTable
slbSessionInfoTable = _SlbSessionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 5, 8)
)
if mibBuilder.loadTexts:
    slbSessionInfoTable.setStatus("current")
_SlbSessionInfoEntry_Object = MibTableRow
slbSessionInfoEntry = _SlbSessionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 5, 8, 1)
)
slbSessionInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbSessionInfoSpIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbSessionInfoIndex"),
)
if mibBuilder.loadTexts:
    slbSessionInfoEntry.setStatus("current")
_SlbSessionInfoSpIndex_Type = Integer32
_SlbSessionInfoSpIndex_Object = MibTableColumn
slbSessionInfoSpIndex = _SlbSessionInfoSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 5, 8, 1, 1),
    _SlbSessionInfoSpIndex_Type()
)
slbSessionInfoSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSessionInfoSpIndex.setStatus("current")
_SlbSessionInfoIndex_Type = Integer32
_SlbSessionInfoIndex_Object = MibTableColumn
slbSessionInfoIndex = _SlbSessionInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 5, 8, 1, 2),
    _SlbSessionInfoIndex_Type()
)
slbSessionInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSessionInfoIndex.setStatus("current")
_SlbSessionInfoString_Type = OctetString
_SlbSessionInfoString_Object = MibTableColumn
slbSessionInfoString = _SlbSessionInfoString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 5, 8, 1, 3),
    _SlbSessionInfoString_Type()
)
slbSessionInfoString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSessionInfoString.setStatus("current")
_SlbSessionInfoMaxSessDump_Type = Integer32
_SlbSessionInfoMaxSessDump_Object = MibScalar
slbSessionInfoMaxSessDump = _SlbSessionInfoMaxSessDump_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 5, 9),
    _SlbSessionInfoMaxSessDump_Type()
)
slbSessionInfoMaxSessDump.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSessionInfoMaxSessDump.setStatus("current")
_GslbInfo_ObjectIdentity = ObjectIdentity
gslbInfo = _GslbInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6)
)
_GslbInfoRemRealServerTable_Object = MibTable
gslbInfoRemRealServerTable = _GslbInfoRemRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 1)
)
if mibBuilder.loadTexts:
    gslbInfoRemRealServerTable.setStatus("current")
_GslbInfoRemRealServerEntry_Object = MibTableRow
gslbInfoRemRealServerEntry = _GslbInfoRemRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 1, 1)
)
gslbInfoRemRealServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbInfoRemRealServerIdx"),
)
if mibBuilder.loadTexts:
    gslbInfoRemRealServerEntry.setStatus("current")
_GslbInfoRemRealServerIdx_Type = Integer32
_GslbInfoRemRealServerIdx_Object = MibTableColumn
gslbInfoRemRealServerIdx = _GslbInfoRemRealServerIdx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 1, 1, 1),
    _GslbInfoRemRealServerIdx_Type()
)
gslbInfoRemRealServerIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoRemRealServerIdx.setStatus("current")
_GslbInfoRemRealServerIpAddr_Type = IpAddress
_GslbInfoRemRealServerIpAddr_Object = MibTableColumn
gslbInfoRemRealServerIpAddr = _GslbInfoRemRealServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 1, 1, 2),
    _GslbInfoRemRealServerIpAddr_Type()
)
gslbInfoRemRealServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoRemRealServerIpAddr.setStatus("current")


class _GslbInfoRemRealServerName_Type(DisplayString):
    """Custom type gslbInfoRemRealServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GslbInfoRemRealServerName_Type.__name__ = "DisplayString"
_GslbInfoRemRealServerName_Object = MibTableColumn
gslbInfoRemRealServerName = _GslbInfoRemRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 1, 1, 3),
    _GslbInfoRemRealServerName_Type()
)
gslbInfoRemRealServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoRemRealServerName.setStatus("current")


class _GslbInfoRemRealServerState_Type(Integer32):
    """Custom type gslbInfoRemRealServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("running", 2),
          ("failed", 3),
          ("disabled", 4))
    )


_GslbInfoRemRealServerState_Type.__name__ = "Integer32"
_GslbInfoRemRealServerState_Object = MibTableColumn
gslbInfoRemRealServerState = _GslbInfoRemRealServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 1, 1, 4),
    _GslbInfoRemRealServerState_Type()
)
gslbInfoRemRealServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoRemRealServerState.setStatus("current")
_GslbInfoVirtServerTable_Object = MibTable
gslbInfoVirtServerTable = _GslbInfoVirtServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2)
)
if mibBuilder.loadTexts:
    gslbInfoVirtServerTable.setStatus("current")
_GslbInfoVirtServerEntry_Object = MibTableRow
gslbInfoVirtServerEntry = _GslbInfoVirtServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1)
)
gslbInfoVirtServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbInfoVirtServerIdx"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbInfoVirtServerServiceIdx"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbInfoVirtServerRserverIdx"),
)
if mibBuilder.loadTexts:
    gslbInfoVirtServerEntry.setStatus("current")
_GslbInfoVirtServerIdx_Type = Integer32
_GslbInfoVirtServerIdx_Object = MibTableColumn
gslbInfoVirtServerIdx = _GslbInfoVirtServerIdx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 1),
    _GslbInfoVirtServerIdx_Type()
)
gslbInfoVirtServerIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerIdx.setStatus("current")
_GslbInfoVirtServerServiceIdx_Type = Integer32
_GslbInfoVirtServerServiceIdx_Object = MibTableColumn
gslbInfoVirtServerServiceIdx = _GslbInfoVirtServerServiceIdx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 2),
    _GslbInfoVirtServerServiceIdx_Type()
)
gslbInfoVirtServerServiceIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerServiceIdx.setStatus("current")
_GslbInfoVirtServerRserverIdx_Type = Integer32
_GslbInfoVirtServerRserverIdx_Object = MibTableColumn
gslbInfoVirtServerRserverIdx = _GslbInfoVirtServerRserverIdx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 3),
    _GslbInfoVirtServerRserverIdx_Type()
)
gslbInfoVirtServerRserverIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerRserverIdx.setStatus("current")


class _GslbInfoVirtServerDname_Type(DisplayString):
    """Custom type gslbInfoVirtServerDname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GslbInfoVirtServerDname_Type.__name__ = "DisplayString"
_GslbInfoVirtServerDname_Object = MibTableColumn
gslbInfoVirtServerDname = _GslbInfoVirtServerDname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 4),
    _GslbInfoVirtServerDname_Type()
)
gslbInfoVirtServerDname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerDname.setStatus("current")
_GslbInfoVirtServerVirtPort_Type = Integer32
_GslbInfoVirtServerVirtPort_Object = MibTableColumn
gslbInfoVirtServerVirtPort = _GslbInfoVirtServerVirtPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 5),
    _GslbInfoVirtServerVirtPort_Type()
)
gslbInfoVirtServerVirtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerVirtPort.setStatus("current")
_GslbInfoVirtServerIpAddress_Type = IpAddress
_GslbInfoVirtServerIpAddress_Object = MibTableColumn
gslbInfoVirtServerIpAddress = _GslbInfoVirtServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 6),
    _GslbInfoVirtServerIpAddress_Type()
)
gslbInfoVirtServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerIpAddress.setStatus("current")
_GslbInfoVirtServerResponse_Type = Integer32
_GslbInfoVirtServerResponse_Object = MibTableColumn
gslbInfoVirtServerResponse = _GslbInfoVirtServerResponse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 7),
    _GslbInfoVirtServerResponse_Type()
)
gslbInfoVirtServerResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerResponse.setStatus("current")
_GslbInfoVirtServerSessAvail_Type = Integer32
_GslbInfoVirtServerSessAvail_Object = MibTableColumn
gslbInfoVirtServerSessAvail = _GslbInfoVirtServerSessAvail_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 8),
    _GslbInfoVirtServerSessAvail_Type()
)
gslbInfoVirtServerSessAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerSessAvail.setStatus("current")
_GslbInfoVirtServerSessCur_Type = Integer32
_GslbInfoVirtServerSessCur_Object = MibTableColumn
gslbInfoVirtServerSessCur = _GslbInfoVirtServerSessCur_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 9),
    _GslbInfoVirtServerSessCur_Type()
)
gslbInfoVirtServerSessCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerSessCur.setStatus("current")
_GslbInfoVirtServerSessMax_Type = Integer32
_GslbInfoVirtServerSessMax_Object = MibTableColumn
gslbInfoVirtServerSessMax = _GslbInfoVirtServerSessMax_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 10),
    _GslbInfoVirtServerSessMax_Type()
)
gslbInfoVirtServerSessMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerSessMax.setStatus("current")


class _GslbInfoVirtServerSessUtil_Type(Integer32):
    """Custom type gslbInfoVirtServerSessUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_GslbInfoVirtServerSessUtil_Type.__name__ = "Integer32"
_GslbInfoVirtServerSessUtil_Object = MibTableColumn
gslbInfoVirtServerSessUtil = _GslbInfoVirtServerSessUtil_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 11),
    _GslbInfoVirtServerSessUtil_Type()
)
gslbInfoVirtServerSessUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerSessUtil.setStatus("current")


class _GslbInfoVirtServerCpuUtil_Type(Integer32):
    """Custom type gslbInfoVirtServerCpuUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_GslbInfoVirtServerCpuUtil_Type.__name__ = "Integer32"
_GslbInfoVirtServerCpuUtil_Object = MibTableColumn
gslbInfoVirtServerCpuUtil = _GslbInfoVirtServerCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 12),
    _GslbInfoVirtServerCpuUtil_Type()
)
gslbInfoVirtServerCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerCpuUtil.setStatus("current")
_GslbInfoVirtServerRemSite_Type = Integer32
_GslbInfoVirtServerRemSite_Object = MibTableColumn
gslbInfoVirtServerRemSite = _GslbInfoVirtServerRemSite_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 13),
    _GslbInfoVirtServerRemSite_Type()
)
gslbInfoVirtServerRemSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerRemSite.setStatus("current")


class _GslbInfoVirtServerWeight_Type(Integer32):
    """Custom type gslbInfoVirtServerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_GslbInfoVirtServerWeight_Type.__name__ = "Integer32"
_GslbInfoVirtServerWeight_Object = MibTableColumn
gslbInfoVirtServerWeight = _GslbInfoVirtServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 14),
    _GslbInfoVirtServerWeight_Type()
)
gslbInfoVirtServerWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerWeight.setStatus("current")


class _GslbInfoVirtServerAvail_Type(Integer32):
    """Custom type gslbInfoVirtServerAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_GslbInfoVirtServerAvail_Type.__name__ = "Integer32"
_GslbInfoVirtServerAvail_Object = MibTableColumn
gslbInfoVirtServerAvail = _GslbInfoVirtServerAvail_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 15),
    _GslbInfoVirtServerAvail_Type()
)
gslbInfoVirtServerAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerAvail.setStatus("current")


class _GslbInfoVirtServerRegion_Type(Integer32):
    """Custom type gslbInfoVirtServerRegion based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("northamerica", 1),
          ("southamerica", 2),
          ("europe", 3),
          ("caribbean", 4),
          ("pacificrim", 5),
          ("subsahara", 6),
          ("japan", 7),
          ("caribbeansubsahara", 8),
          ("africa", 9))
    )


_GslbInfoVirtServerRegion_Type.__name__ = "Integer32"
_GslbInfoVirtServerRegion_Object = MibTableColumn
gslbInfoVirtServerRegion = _GslbInfoVirtServerRegion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 2, 1, 16),
    _GslbInfoVirtServerRegion_Type()
)
gslbInfoVirtServerRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoVirtServerRegion.setStatus("current")
_GslbInfoRemSiteTable_Object = MibTable
gslbInfoRemSiteTable = _GslbInfoRemSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 3)
)
if mibBuilder.loadTexts:
    gslbInfoRemSiteTable.setStatus("current")
_GslbInfoRemSiteEntry_Object = MibTableRow
gslbInfoRemSiteEntry = _GslbInfoRemSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 3, 1)
)
gslbInfoRemSiteEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "gslbInfoRemSiteIdx"),
)
if mibBuilder.loadTexts:
    gslbInfoRemSiteEntry.setStatus("current")
_GslbInfoRemSiteIdx_Type = Integer32
_GslbInfoRemSiteIdx_Object = MibTableColumn
gslbInfoRemSiteIdx = _GslbInfoRemSiteIdx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 3, 1, 1),
    _GslbInfoRemSiteIdx_Type()
)
gslbInfoRemSiteIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoRemSiteIdx.setStatus("current")
_GslbInfoRemSitePrimaryIp_Type = IpAddress
_GslbInfoRemSitePrimaryIp_Object = MibTableColumn
gslbInfoRemSitePrimaryIp = _GslbInfoRemSitePrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 3, 1, 2),
    _GslbInfoRemSitePrimaryIp_Type()
)
gslbInfoRemSitePrimaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoRemSitePrimaryIp.setStatus("current")
_GslbInfoRemSiteSecondaryIp_Type = IpAddress
_GslbInfoRemSiteSecondaryIp_Object = MibTableColumn
gslbInfoRemSiteSecondaryIp = _GslbInfoRemSiteSecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 3, 1, 3),
    _GslbInfoRemSiteSecondaryIp_Type()
)
gslbInfoRemSiteSecondaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoRemSiteSecondaryIp.setStatus("current")


class _GslbInfoRemSiteName_Type(DisplayString):
    """Custom type gslbInfoRemSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GslbInfoRemSiteName_Type.__name__ = "DisplayString"
_GslbInfoRemSiteName_Object = MibTableColumn
gslbInfoRemSiteName = _GslbInfoRemSiteName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 3, 1, 4),
    _GslbInfoRemSiteName_Type()
)
gslbInfoRemSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoRemSiteName.setStatus("current")


class _GslbInfoRemSiteState_Type(Integer32):
    """Custom type gslbInfoRemSiteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("running", 2),
          ("failed", 3),
          ("disabled", 4))
    )


_GslbInfoRemSiteState_Type.__name__ = "Integer32"
_GslbInfoRemSiteState_Object = MibTableColumn
gslbInfoRemSiteState = _GslbInfoRemSiteState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 6, 3, 1, 5),
    _GslbInfoRemSiteState_Type()
)
gslbInfoRemSiteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbInfoRemSiteState.setStatus("current")
_WlmInfo_ObjectIdentity = ObjectIdentity
wlmInfo = _WlmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 7)
)
_SlbWlmInfoTable_Object = MibTable
slbWlmInfoTable = _SlbWlmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 7, 1)
)
if mibBuilder.loadTexts:
    slbWlmInfoTable.setStatus("current")
_SlbWlmInfoEntry_Object = MibTableRow
slbWlmInfoEntry = _SlbWlmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 7, 1, 1)
)
slbWlmInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbWlmInfoIndex"),
)
if mibBuilder.loadTexts:
    slbWlmInfoEntry.setStatus("current")
_SlbWlmInfoIndex_Type = Integer32
_SlbWlmInfoIndex_Object = MibTableColumn
slbWlmInfoIndex = _SlbWlmInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 7, 1, 1, 1),
    _SlbWlmInfoIndex_Type()
)
slbWlmInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbWlmInfoIndex.setStatus("current")
_SlbWlmInfoIpAddr_Type = IpAddress
_SlbWlmInfoIpAddr_Object = MibTableColumn
slbWlmInfoIpAddr = _SlbWlmInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 7, 1, 1, 2),
    _SlbWlmInfoIpAddr_Type()
)
slbWlmInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbWlmInfoIpAddr.setStatus("current")


class _SlbWlmInfoPort_Type(Integer32):
    """Custom type slbWlmInfoPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbWlmInfoPort_Type.__name__ = "Integer32"
_SlbWlmInfoPort_Object = MibTableColumn
slbWlmInfoPort = _SlbWlmInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 7, 1, 1, 3),
    _SlbWlmInfoPort_Type()
)
slbWlmInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbWlmInfoPort.setStatus("current")


class _SlbWlmInfoState_Type(Integer32):
    """Custom type slbWlmInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notconnected", 2))
    )


_SlbWlmInfoState_Type.__name__ = "Integer32"
_SlbWlmInfoState_Object = MibTableColumn
slbWlmInfoState = _SlbWlmInfoState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 7, 1, 1, 4),
    _SlbWlmInfoState_Type()
)
slbWlmInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbWlmInfoState.setStatus("current")
_SlbPortInfo_ObjectIdentity = ObjectIdentity
slbPortInfo = _SlbPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 8)
)
_SlbPortInfoTable_Object = MibTable
slbPortInfoTable = _SlbPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 8, 1)
)
if mibBuilder.loadTexts:
    slbPortInfoTable.setStatus("current")
_SlbPortInfoEntry_Object = MibTableRow
slbPortInfoEntry = _SlbPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 8, 1, 1)
)
slbPortInfoEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbPortInfoIndex"),
)
if mibBuilder.loadTexts:
    slbPortInfoEntry.setStatus("current")
_SlbPortInfoIndex_Type = Integer32
_SlbPortInfoIndex_Object = MibTableColumn
slbPortInfoIndex = _SlbPortInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 8, 1, 1, 1),
    _SlbPortInfoIndex_Type()
)
slbPortInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPortInfoIndex.setStatus("current")


class _SlbPortClientState_Type(Integer32):
    """Custom type slbPortClientState based on Integer32"""
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


_SlbPortClientState_Type.__name__ = "Integer32"
_SlbPortClientState_Object = MibTableColumn
slbPortClientState = _SlbPortClientState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 8, 1, 1, 2),
    _SlbPortClientState_Type()
)
slbPortClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPortClientState.setStatus("current")


class _SlbPortSerState_Type(Integer32):
    """Custom type slbPortSerState based on Integer32"""
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


_SlbPortSerState_Type.__name__ = "Integer32"
_SlbPortSerState_Object = MibTableColumn
slbPortSerState = _SlbPortSerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 8, 1, 1, 3),
    _SlbPortSerState_Type()
)
slbPortSerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPortSerState.setStatus("current")


class _SlbPortFltState_Type(Integer32):
    """Custom type slbPortFltState based on Integer32"""
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


_SlbPortFltState_Type.__name__ = "Integer32"
_SlbPortFltState_Object = MibTableColumn
slbPortFltState = _SlbPortFltState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 8, 1, 1, 4),
    _SlbPortFltState_Type()
)
slbPortFltState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPortFltState.setStatus("current")


class _SlbPortRTSState_Type(Integer32):
    """Custom type slbPortRTSState based on Integer32"""
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


_SlbPortRTSState_Type.__name__ = "Integer32"
_SlbPortRTSState_Object = MibTableColumn
slbPortRTSState = _SlbPortRTSState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 8, 1, 1, 5),
    _SlbPortRTSState_Type()
)
slbPortRTSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPortRTSState.setStatus("current")


class _SlbPortHotStandbyState_Type(Integer32):
    """Custom type slbPortHotStandbyState based on Integer32"""
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


_SlbPortHotStandbyState_Type.__name__ = "Integer32"
_SlbPortHotStandbyState_Object = MibTableColumn
slbPortHotStandbyState = _SlbPortHotStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 8, 1, 1, 6),
    _SlbPortHotStandbyState_Type()
)
slbPortHotStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPortHotStandbyState.setStatus("current")


class _SlbPortInterSWState_Type(Integer32):
    """Custom type slbPortInterSWState based on Integer32"""
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


_SlbPortInterSWState_Type.__name__ = "Integer32"
_SlbPortInterSWState_Object = MibTableColumn
slbPortInterSWState = _SlbPortInterSWState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 8, 1, 1, 7),
    _SlbPortInterSWState_Type()
)
slbPortInterSWState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPortInterSWState.setStatus("current")


class _SlbPortProxyState_Type(Integer32):
    """Custom type slbPortProxyState based on Integer32"""
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


_SlbPortProxyState_Type.__name__ = "Integer32"
_SlbPortProxyState_Object = MibTableColumn
slbPortProxyState = _SlbPortProxyState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 8, 1, 1, 8),
    _SlbPortProxyState_Type()
)
slbPortProxyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPortProxyState.setStatus("current")


class _SlbPortIdSlbState_Type(Integer32):
    """Custom type slbPortIdSlbState based on Integer32"""
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


_SlbPortIdSlbState_Type.__name__ = "Integer32"
_SlbPortIdSlbState_Object = MibTableColumn
slbPortIdSlbState = _SlbPortIdSlbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 8, 1, 1, 9),
    _SlbPortIdSlbState_Type()
)
slbPortIdSlbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPortIdSlbState.setStatus("current")


class _SlbPortSymantecState_Type(Integer32):
    """Custom type slbPortSymantecState based on Integer32"""
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


_SlbPortSymantecState_Type.__name__ = "Integer32"
_SlbPortSymantecState_Object = MibTableColumn
slbPortSymantecState = _SlbPortSymantecState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 8, 1, 1, 10),
    _SlbPortSymantecState_Type()
)
slbPortSymantecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPortSymantecState.setStatus("current")


class _SlbPortFitersAdded_Type(OctetString):
    """Custom type slbPortFitersAdded based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SlbPortFitersAdded_Type.__name__ = "OctetString"
_SlbPortFitersAdded_Object = MibTableColumn
slbPortFitersAdded = _SlbPortFitersAdded_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 8, 1, 1, 11),
    _SlbPortFitersAdded_Type()
)
slbPortFitersAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPortFitersAdded.setStatus("current")
_SynAttackInfo_ObjectIdentity = ObjectIdentity
synAttackInfo = _SynAttackInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 9)
)


class _SynAtkState_Type(Integer32):
    """Custom type synAtkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SynAtkState_Type.__name__ = "Integer32"
_SynAtkState_Object = MibScalar
synAtkState = _SynAtkState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 9, 1),
    _SynAtkState_Type()
)
synAtkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    synAtkState.setStatus("current")
_SynAtkInterval_Type = Integer32
_SynAtkInterval_Object = MibScalar
synAtkInterval = _SynAtkInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 9, 2),
    _SynAtkInterval_Type()
)
synAtkInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    synAtkInterval.setStatus("current")
_SynAtkThreshhold_Type = Integer32
_SynAtkThreshhold_Object = MibScalar
synAtkThreshhold = _SynAtkThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 9, 3),
    _SynAtkThreshhold_Type()
)
synAtkThreshhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    synAtkThreshhold.setStatus("current")
_SynAtkWarningFired_Type = Integer32
_SynAtkWarningFired_Object = MibScalar
synAtkWarningFired = _SynAtkWarningFired_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 3, 9, 4),
    _SynAtkWarningFired_Type()
)
synAtkWarningFired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    synAtkWarningFired.setStatus("current")
_Layer4Oper_ObjectIdentity = ObjectIdentity
layer4Oper = _Layer4Oper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 4)
)
_SlbOperRealServerTable_Object = MibTable
slbOperRealServerTable = _SlbOperRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 4, 1)
)
if mibBuilder.loadTexts:
    slbOperRealServerTable.setStatus("current")
_SlbOperRealServerEntry_Object = MibTableRow
slbOperRealServerEntry = _SlbOperRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 4, 1, 1)
)
slbOperRealServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbOperRealServerIndex"),
)
if mibBuilder.loadTexts:
    slbOperRealServerEntry.setStatus("current")
_SlbOperRealServerIndex_Type = Integer32
_SlbOperRealServerIndex_Object = MibTableColumn
slbOperRealServerIndex = _SlbOperRealServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 4, 1, 1, 1),
    _SlbOperRealServerIndex_Type()
)
slbOperRealServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbOperRealServerIndex.setStatus("current")


class _SlbOperRealServerStatus_Type(Integer32):
    """Custom type slbOperRealServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("cookiepersistent", 3))
    )


_SlbOperRealServerStatus_Type.__name__ = "Integer32"
_SlbOperRealServerStatus_Object = MibTableColumn
slbOperRealServerStatus = _SlbOperRealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 4, 1, 1, 2),
    _SlbOperRealServerStatus_Type()
)
slbOperRealServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbOperRealServerStatus.setStatus("current")


class _SlbOperClearSessionTable_Type(Integer32):
    """Custom type slbOperClearSessionTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_SlbOperClearSessionTable_Type.__name__ = "Integer32"
_SlbOperClearSessionTable_Object = MibScalar
slbOperClearSessionTable = _SlbOperClearSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 4, 2),
    _SlbOperClearSessionTable_Type()
)
slbOperClearSessionTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbOperClearSessionTable.setStatus("current")


class _SlbOperConfigSync_Type(Integer32):
    """Custom type slbOperConfigSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("sync", 2))
    )


_SlbOperConfigSync_Type.__name__ = "Integer32"
_SlbOperConfigSync_Object = MibScalar
slbOperConfigSync = _SlbOperConfigSync_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 4, 3),
    _SlbOperConfigSync_Type()
)
slbOperConfigSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbOperConfigSync.setStatus("current")
_GslbOper_ObjectIdentity = ObjectIdentity
gslbOper = _GslbOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 4, 4)
)
_SlbOperGroupRealServerTable_Object = MibTable
slbOperGroupRealServerTable = _SlbOperGroupRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 4, 5)
)
if mibBuilder.loadTexts:
    slbOperGroupRealServerTable.setStatus("current")
_SlbOperGroupRealServerEntry_Object = MibTableRow
slbOperGroupRealServerEntry = _SlbOperGroupRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 4, 5, 1)
)
slbOperGroupRealServerEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbOperRealServGroupIndex"),
    (0, "ALTEON-CHEETAH-LAYER4-MIB", "slbOperGroupRealServIndex"),
)
if mibBuilder.loadTexts:
    slbOperGroupRealServerEntry.setStatus("current")
_SlbOperRealServGroupIndex_Type = Integer32
_SlbOperRealServGroupIndex_Object = MibTableColumn
slbOperRealServGroupIndex = _SlbOperRealServGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 4, 5, 1, 1),
    _SlbOperRealServGroupIndex_Type()
)
slbOperRealServGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbOperRealServGroupIndex.setStatus("current")
_SlbOperGroupRealServIndex_Type = Integer32
_SlbOperGroupRealServIndex_Object = MibTableColumn
slbOperGroupRealServIndex = _SlbOperGroupRealServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 4, 5, 1, 2),
    _SlbOperGroupRealServIndex_Type()
)
slbOperGroupRealServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbOperGroupRealServIndex.setStatus("current")


class _SlbOperGroupRealServerState_Type(Integer32):
    """Custom type slbOperGroupRealServerState based on Integer32"""
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


_SlbOperGroupRealServerState_Type.__name__ = "Integer32"
_SlbOperGroupRealServerState_Object = MibTableColumn
slbOperGroupRealServerState = _SlbOperGroupRealServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 4, 4, 5, 1, 3),
    _SlbOperGroupRealServerState_Type()
)
slbOperGroupRealServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbOperGroupRealServerState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-CHEETAH-LAYER4-MIB",
    **{"layer4": layer4,
       "layer4Configs": layer4Configs,
       "slbCfg": slbCfg,
       "slbGeneralCfg": slbGeneralCfg,
       "slbCurCfgGlobalControl": slbCurCfgGlobalControl,
       "slbNewCfgGlobalControl": slbNewCfgGlobalControl,
       "slbCurCfgImask": slbCurCfgImask,
       "slbNewCfgImask": slbNewCfgImask,
       "slbCurCfgMnet": slbCurCfgMnet,
       "slbNewCfgMnet": slbNewCfgMnet,
       "slbCurCfgMmask": slbCurCfgMmask,
       "slbNewCfgMmask": slbNewCfgMmask,
       "slbCurCfgRadiusAuthenString": slbCurCfgRadiusAuthenString,
       "slbNewCfgRadiusAuthenString": slbNewCfgRadiusAuthenString,
       "slbCurCfgDirectMode": slbCurCfgDirectMode,
       "slbNewCfgDirectMode": slbNewCfgDirectMode,
       "slbCurCfgPmask": slbCurCfgPmask,
       "slbNewCfgPmask": slbNewCfgPmask,
       "slbCurCfgGrace": slbCurCfgGrace,
       "slbNewCfgGrace": slbNewCfgGrace,
       "slbCurCfgVirtMatrixArch": slbCurCfgVirtMatrixArch,
       "slbNewCfgVirtMatrixArch": slbNewCfgVirtMatrixArch,
       "slbCurCfgFastage": slbCurCfgFastage,
       "slbNewCfgFastage": slbNewCfgFastage,
       "slbCurCfgSlowage": slbCurCfgSlowage,
       "slbNewCfgSlowage": slbNewCfgSlowage,
       "slbCurCfgTpcp": slbCurCfgTpcp,
       "slbNewCfgTpcp": slbNewCfgTpcp,
       "slbCurCfgMetricInterval": slbCurCfgMetricInterval,
       "slbNewCfgMetricInterval": slbNewCfgMetricInterval,
       "slbCurCfgLdapVersion": slbCurCfgLdapVersion,
       "slbNewCfgLdapVersion": slbNewCfgLdapVersion,
       "slbCurCfgAllowHttpHc": slbCurCfgAllowHttpHc,
       "slbNewCfgAllowHttpHc": slbNewCfgAllowHttpHc,
       "slbCurCfgSubmac": slbCurCfgSubmac,
       "slbNewCfgSubmac": slbNewCfgSubmac,
       "slbCurCfgProxyGratArp": slbCurCfgProxyGratArp,
       "slbNewCfgProxyGratArp": slbNewCfgProxyGratArp,
       "slbCurCfgRtsVlan": slbCurCfgRtsVlan,
       "slbNewCfgRtsVlan": slbNewCfgRtsVlan,
       "slbCurCfgVirtualServiceStats": slbCurCfgVirtualServiceStats,
       "slbNewCfgVirtualServiceStats": slbNewCfgVirtualServiceStats,
       "slbCurCfgSlbSessAtkIntrval": slbCurCfgSlbSessAtkIntrval,
       "slbNewCfgSlbSessAtkIntrval": slbNewCfgSlbSessAtkIntrval,
       "slbCurCfgSlbSessAtkAllowlim": slbCurCfgSlbSessAtkAllowlim,
       "slbNewCfgSlbSessAtkAllowlim": slbNewCfgSlbSessAtkAllowlim,
       "slbCurCfgNewSlowage": slbCurCfgNewSlowage,
       "slbNewCfgNewSlowage": slbNewCfgNewSlowage,
       "slbCurCfgPortBind": slbCurCfgPortBind,
       "slbNewCfgPortBind": slbNewCfgPortBind,
       "slbCurCfgVmaSrcPort": slbCurCfgVmaSrcPort,
       "slbNewCfgVmaSrcPort": slbNewCfgVmaSrcPort,
       "slbCurCfgIpTcpCksum": slbCurCfgIpTcpCksum,
       "slbNewCfgIpTcpCksum": slbNewCfgIpTcpCksum,
       "realServerCfg": realServerCfg,
       "slbRealServerMaxSize": slbRealServerMaxSize,
       "slbCurCfgRealServerTable": slbCurCfgRealServerTable,
       "slbCurCfgRealServerEntry": slbCurCfgRealServerEntry,
       "slbCurCfgRealServerIndex": slbCurCfgRealServerIndex,
       "slbCurCfgRealServerIpAddr": slbCurCfgRealServerIpAddr,
       "slbCurCfgRealServerWeight": slbCurCfgRealServerWeight,
       "slbCurCfgRealServerMaxConns": slbCurCfgRealServerMaxConns,
       "slbCurCfgRealServerTimeOut": slbCurCfgRealServerTimeOut,
       "slbCurCfgRealServerBackUp": slbCurCfgRealServerBackUp,
       "slbCurCfgRealServerPingInterval": slbCurCfgRealServerPingInterval,
       "slbCurCfgRealServerFailRetry": slbCurCfgRealServerFailRetry,
       "slbCurCfgRealServerSuccRetry": slbCurCfgRealServerSuccRetry,
       "slbCurCfgRealServerState": slbCurCfgRealServerState,
       "slbCurCfgRealServerType": slbCurCfgRealServerType,
       "slbCurCfgRealServerName": slbCurCfgRealServerName,
       "slbCurCfgRealServerUrlBmap": slbCurCfgRealServerUrlBmap,
       "slbCurCfgRealServerCookie": slbCurCfgRealServerCookie,
       "slbCurCfgRealServerExcludeStr": slbCurCfgRealServerExcludeStr,
       "slbCurCfgRealServerSubmac": slbCurCfgRealServerSubmac,
       "slbCurCfgRealServerProxy": slbCurCfgRealServerProxy,
       "slbCurCfgRealServerLdapwr": slbCurCfgRealServerLdapwr,
       "slbCurCfgRealServerOid": slbCurCfgRealServerOid,
       "slbCurCfgRealServerCommString": slbCurCfgRealServerCommString,
       "slbCurCfgRealServerIdsvlan": slbCurCfgRealServerIdsvlan,
       "slbCurCfgRealServerIdsport": slbCurCfgRealServerIdsport,
       "slbCurCfgRealServerAvail": slbCurCfgRealServerAvail,
       "slbCurCfgRealServerFastHealthCheck": slbCurCfgRealServerFastHealthCheck,
       "slbCurCfgRealServerSubdmac": slbCurCfgRealServerSubdmac,
       "slbCurCfgRealServerOverflow": slbCurCfgRealServerOverflow,
       "slbNewCfgRealServerTable": slbNewCfgRealServerTable,
       "slbNewCfgRealServerEntry": slbNewCfgRealServerEntry,
       "slbNewCfgRealServerIndex": slbNewCfgRealServerIndex,
       "slbNewCfgRealServerIpAddr": slbNewCfgRealServerIpAddr,
       "slbNewCfgRealServerWeight": slbNewCfgRealServerWeight,
       "slbNewCfgRealServerMaxConns": slbNewCfgRealServerMaxConns,
       "slbNewCfgRealServerTimeOut": slbNewCfgRealServerTimeOut,
       "slbNewCfgRealServerBackUp": slbNewCfgRealServerBackUp,
       "slbNewCfgRealServerPingInterval": slbNewCfgRealServerPingInterval,
       "slbNewCfgRealServerFailRetry": slbNewCfgRealServerFailRetry,
       "slbNewCfgRealServerSuccRetry": slbNewCfgRealServerSuccRetry,
       "slbNewCfgRealServerState": slbNewCfgRealServerState,
       "slbNewCfgRealServerDelete": slbNewCfgRealServerDelete,
       "slbNewCfgRealServerType": slbNewCfgRealServerType,
       "slbNewCfgRealServerName": slbNewCfgRealServerName,
       "slbNewCfgRealServerUrlBmap": slbNewCfgRealServerUrlBmap,
       "slbNewCfgRealServerAddUrl": slbNewCfgRealServerAddUrl,
       "slbNewCfgRealServerRemUrl": slbNewCfgRealServerRemUrl,
       "slbNewCfgRealServerCookie": slbNewCfgRealServerCookie,
       "slbNewCfgRealServerExcludeStr": slbNewCfgRealServerExcludeStr,
       "slbNewCfgRealServerSubmac": slbNewCfgRealServerSubmac,
       "slbNewCfgRealServerProxy": slbNewCfgRealServerProxy,
       "slbNewCfgRealServerLdapwr": slbNewCfgRealServerLdapwr,
       "slbNewCfgRealServerOid": slbNewCfgRealServerOid,
       "slbNewCfgRealServerCommString": slbNewCfgRealServerCommString,
       "slbNewCfgRealServerIdsvlan": slbNewCfgRealServerIdsvlan,
       "slbNewCfgRealServerIdsport": slbNewCfgRealServerIdsport,
       "slbNewCfgRealServerAvail": slbNewCfgRealServerAvail,
       "slbNewCfgRealServerFastHealthCheck": slbNewCfgRealServerFastHealthCheck,
       "slbNewCfgRealServerSubdmac": slbNewCfgRealServerSubdmac,
       "slbNewCfgRealServerOverflow": slbNewCfgRealServerOverflow,
       "slbRealServPortTableMaxSize": slbRealServPortTableMaxSize,
       "slbCurCfgRealServPortTable": slbCurCfgRealServPortTable,
       "slbCurCfgRealServPortEntry": slbCurCfgRealServPortEntry,
       "slbCurCfgRealServIndex": slbCurCfgRealServIndex,
       "slbCurCfgRealServPortIndex": slbCurCfgRealServPortIndex,
       "slbCurCfgRealServRealPort": slbCurCfgRealServRealPort,
       "slbNewCfgRealServPortTable": slbNewCfgRealServPortTable,
       "slbNewCfgRealServPortEntry": slbNewCfgRealServPortEntry,
       "slbNewCfgRealServIndex": slbNewCfgRealServIndex,
       "slbNewCfgRealServPortIndex": slbNewCfgRealServPortIndex,
       "slbNewCfgRealServRealPort": slbNewCfgRealServRealPort,
       "slbNewCfgRealServPortDelete": slbNewCfgRealServPortDelete,
       "slbBuddyTableMaxSize": slbBuddyTableMaxSize,
       "slbCurCfgBuddyTable": slbCurCfgBuddyTable,
       "slbCurCfgBuddyEntry": slbCurCfgBuddyEntry,
       "slbCurCfgRealSerIndex": slbCurCfgRealSerIndex,
       "slbCurCfgBuddyIndex": slbCurCfgBuddyIndex,
       "slbCurCfgBuddyRealIndex": slbCurCfgBuddyRealIndex,
       "slbCurCfgBuddyGroupIndex": slbCurCfgBuddyGroupIndex,
       "slbCurCfgBuddyService": slbCurCfgBuddyService,
       "slbNewCfgBuddyTable": slbNewCfgBuddyTable,
       "slbNewCfgBuddyEntry": slbNewCfgBuddyEntry,
       "slbNewCfgRealSerIndex": slbNewCfgRealSerIndex,
       "slbNewCfgBuddyIndex": slbNewCfgBuddyIndex,
       "slbNewCfgBuddyRealIndex": slbNewCfgBuddyRealIndex,
       "slbNewCfgBuddyGroupIndex": slbNewCfgBuddyGroupIndex,
       "slbNewCfgBuddyService": slbNewCfgBuddyService,
       "slbNewCfgBuddyDelete": slbNewCfgBuddyDelete,
       "realServerGroupCfg": realServerGroupCfg,
       "slbGroupTableMaxSize": slbGroupTableMaxSize,
       "slbGroupMaxIdsSize": slbGroupMaxIdsSize,
       "slbCurCfgGroupTable": slbCurCfgGroupTable,
       "slbCurCfgGroupEntry": slbCurCfgGroupEntry,
       "slbCurCfgGroupIndex": slbCurCfgGroupIndex,
       "slbCurCfgGroupRealServers": slbCurCfgGroupRealServers,
       "slbCurCfgGroupMetric": slbCurCfgGroupMetric,
       "slbCurCfgGroupBackupServer": slbCurCfgGroupBackupServer,
       "slbCurCfgGroupBackupGroup": slbCurCfgGroupBackupGroup,
       "slbCurCfgGroupHealthCheckUrl": slbCurCfgGroupHealthCheckUrl,
       "slbCurCfgGroupHealthCheckLayer": slbCurCfgGroupHealthCheckLayer,
       "slbCurCfgGroupName": slbCurCfgGroupName,
       "slbCurCfgGroupRealThreshold": slbCurCfgGroupRealThreshold,
       "slbCurCfgGroupVipHealthCheck": slbCurCfgGroupVipHealthCheck,
       "slbCurCfgGroupIdsState": slbCurCfgGroupIdsState,
       "slbCurCfgGroupIdsPort": slbCurCfgGroupIdsPort,
       "slbCurCfgGroupIdsFlood": slbCurCfgGroupIdsFlood,
       "slbCurCfgGroupMinmissHash": slbCurCfgGroupMinmissHash,
       "slbCurCfgGroupPhashMask": slbCurCfgGroupPhashMask,
       "slbCurCfgGroupRmetric": slbCurCfgGroupRmetric,
       "slbCurCfgGroupHealthCheckFormula": slbCurCfgGroupHealthCheckFormula,
       "slbCurCfgGroupOperatorAccess": slbCurCfgGroupOperatorAccess,
       "slbCurCfgGroupWlm": slbCurCfgGroupWlm,
       "slbNewCfgGroupTable": slbNewCfgGroupTable,
       "slbNewCfgGroupEntry": slbNewCfgGroupEntry,
       "slbNewCfgGroupIndex": slbNewCfgGroupIndex,
       "slbNewCfgGroupRealServers": slbNewCfgGroupRealServers,
       "slbNewCfgGroupAddServer": slbNewCfgGroupAddServer,
       "slbNewCfgGroupRemoveServer": slbNewCfgGroupRemoveServer,
       "slbNewCfgGroupMetric": slbNewCfgGroupMetric,
       "slbNewCfgGroupBackupServer": slbNewCfgGroupBackupServer,
       "slbNewCfgGroupBackupGroup": slbNewCfgGroupBackupGroup,
       "slbNewCfgGroupHealthCheckUrl": slbNewCfgGroupHealthCheckUrl,
       "slbNewCfgGroupHealthCheckLayer": slbNewCfgGroupHealthCheckLayer,
       "slbNewCfgGroupName": slbNewCfgGroupName,
       "slbNewCfgGroupRealThreshold": slbNewCfgGroupRealThreshold,
       "slbNewCfgGroupVipHealthCheck": slbNewCfgGroupVipHealthCheck,
       "slbNewCfgGroupIdsState": slbNewCfgGroupIdsState,
       "slbNewCfgGroupIdsPort": slbNewCfgGroupIdsPort,
       "slbNewCfgGroupDelete": slbNewCfgGroupDelete,
       "slbNewCfgGroupIdsFlood": slbNewCfgGroupIdsFlood,
       "slbNewCfgGroupMinmissHash": slbNewCfgGroupMinmissHash,
       "slbNewCfgGroupPhashMask": slbNewCfgGroupPhashMask,
       "slbNewCfgGroupRmetric": slbNewCfgGroupRmetric,
       "slbNewCfgGroupHealthCheckFormula": slbNewCfgGroupHealthCheckFormula,
       "slbNewCfgGroupOperatorAccess": slbNewCfgGroupOperatorAccess,
       "slbNewCfgGroupWlm": slbNewCfgGroupWlm,
       "slbCurCfgGroupRealServerTable": slbCurCfgGroupRealServerTable,
       "slbCurCfgGroupRealServerEntry": slbCurCfgGroupRealServerEntry,
       "slbCurCfgRealServGroupIndex": slbCurCfgRealServGroupIndex,
       "slbCurCfgGroupRealServIndex": slbCurCfgGroupRealServIndex,
       "slbCurCfgGroupRealServerState": slbCurCfgGroupRealServerState,
       "slbNewCfgGroupRealServerTable": slbNewCfgGroupRealServerTable,
       "slbNewCfgGroupRealServerEntry": slbNewCfgGroupRealServerEntry,
       "slbNewCfgRealServGroupIndex": slbNewCfgRealServGroupIndex,
       "slbNewCfgGroupRealServIndex": slbNewCfgGroupRealServIndex,
       "slbNewCfgGroupRealServerState": slbNewCfgGroupRealServerState,
       "virtualServerCfg": virtualServerCfg,
       "slbVirtServerTableMaxSize": slbVirtServerTableMaxSize,
       "slbCurCfgVirtServerTable": slbCurCfgVirtServerTable,
       "slbCurCfgVirtualServerEntry": slbCurCfgVirtualServerEntry,
       "slbCurCfgVirtServerIndex": slbCurCfgVirtServerIndex,
       "slbCurCfgVirtServerIpAddress": slbCurCfgVirtServerIpAddress,
       "slbCurCfgVirtServerLayer3Only": slbCurCfgVirtServerLayer3Only,
       "slbCurCfgVirtServerState": slbCurCfgVirtServerState,
       "slbCurCfgVirtServerDname": slbCurCfgVirtServerDname,
       "slbCurCfgVirtServerBwmContract": slbCurCfgVirtServerBwmContract,
       "slbCurCfgVirtServerWeight": slbCurCfgVirtServerWeight,
       "slbCurCfgVirtServerAvail": slbCurCfgVirtServerAvail,
       "slbCurCfgVirtServerRule": slbCurCfgVirtServerRule,
       "slbCurCfgVirtServerVname": slbCurCfgVirtServerVname,
       "slbCurCfgVirtServerIpVer": slbCurCfgVirtServerIpVer,
       "slbCurCfgVirtServerIpv6Addr": slbCurCfgVirtServerIpv6Addr,
       "slbNewCfgVirtServerTable": slbNewCfgVirtServerTable,
       "slbNewCfgVirtualServerEntry": slbNewCfgVirtualServerEntry,
       "slbNewCfgVirtServerIndex": slbNewCfgVirtServerIndex,
       "slbNewCfgVirtServerIpAddress": slbNewCfgVirtServerIpAddress,
       "slbNewCfgVirtServerLayer3Only": slbNewCfgVirtServerLayer3Only,
       "slbNewCfgVirtServerState": slbNewCfgVirtServerState,
       "slbNewCfgVirtServerDname": slbNewCfgVirtServerDname,
       "slbNewCfgVirtServerBwmContract": slbNewCfgVirtServerBwmContract,
       "slbNewCfgVirtServerDelete": slbNewCfgVirtServerDelete,
       "slbNewCfgVirtServerWeight": slbNewCfgVirtServerWeight,
       "slbNewCfgVirtServerAvail": slbNewCfgVirtServerAvail,
       "slbNewCfgVirtServerRule": slbNewCfgVirtServerRule,
       "slbNewCfgVirtServerAddRule": slbNewCfgVirtServerAddRule,
       "slbNewCfgVirtServerRemoveRule": slbNewCfgVirtServerRemoveRule,
       "slbNewCfgVirtServerVname": slbNewCfgVirtServerVname,
       "slbNewCfgVirtServerIpVer": slbNewCfgVirtServerIpVer,
       "slbNewCfgVirtServerIpv6Addr": slbNewCfgVirtServerIpv6Addr,
       "slbVirtServicesTableMaxSize": slbVirtServicesTableMaxSize,
       "slbCurCfgVirtServicesTable": slbCurCfgVirtServicesTable,
       "slbCurCfgVirtServicesEntry": slbCurCfgVirtServicesEntry,
       "slbCurCfgVirtServIndex": slbCurCfgVirtServIndex,
       "slbCurCfgVirtServiceIndex": slbCurCfgVirtServiceIndex,
       "slbCurCfgVirtServiceVirtPort": slbCurCfgVirtServiceVirtPort,
       "slbCurCfgVirtServiceRealGroup": slbCurCfgVirtServiceRealGroup,
       "slbCurCfgVirtServiceRealPort": slbCurCfgVirtServiceRealPort,
       "slbCurCfgVirtServiceUDPBalance": slbCurCfgVirtServiceUDPBalance,
       "slbCurCfgVirtServiceHname": slbCurCfgVirtServiceHname,
       "slbCurCfgVirtServiceBwmContract": slbCurCfgVirtServiceBwmContract,
       "slbCurCfgVirtServiceDirServerRtn": slbCurCfgVirtServiceDirServerRtn,
       "slbCurCfgVirtServiceRtspUrlParse": slbCurCfgVirtServiceRtspUrlParse,
       "slbCurCfgVirtServiceDBind": slbCurCfgVirtServiceDBind,
       "slbCurCfgVirtServiceFtpParsing": slbCurCfgVirtServiceFtpParsing,
       "slbCurCfgVirtServiceRemapUDPFrags": slbCurCfgVirtServiceRemapUDPFrags,
       "slbCurCfgVirtServiceDnsSlb": slbCurCfgVirtServiceDnsSlb,
       "slbCurCfgVirtServiceResponseCount": slbCurCfgVirtServiceResponseCount,
       "slbCurCfgVirtServicePBind": slbCurCfgVirtServicePBind,
       "slbCurCfgVirtServiceCname": slbCurCfgVirtServiceCname,
       "slbCurCfgVirtServiceCoffset": slbCurCfgVirtServiceCoffset,
       "slbCurCfgVirtServiceClength": slbCurCfgVirtServiceClength,
       "slbCurCfgVirtServiceUriCookie": slbCurCfgVirtServiceUriCookie,
       "slbCurCfgVirtServiceCExpire": slbCurCfgVirtServiceCExpire,
       "slbCurCfgVirtServiceCookieMode": slbCurCfgVirtServiceCookieMode,
       "slbCurCfgVirtServiceHttpSlb": slbCurCfgVirtServiceHttpSlb,
       "slbCurCfgVirtServiceHttpSlbOption": slbCurCfgVirtServiceHttpSlbOption,
       "slbCurCfgVirtServiceHttpSlb2": slbCurCfgVirtServiceHttpSlb2,
       "slbCurCfgVirtServiceHttpHdrName": slbCurCfgVirtServiceHttpHdrName,
       "slbCurCfgVirtServiceUrlHashLen": slbCurCfgVirtServiceUrlHashLen,
       "slbCurCfgVirtServiceDirect": slbCurCfgVirtServiceDirect,
       "slbCurCfgVirtServiceThash": slbCurCfgVirtServiceThash,
       "slbCurCfgVirtServiceLdapreset": slbCurCfgVirtServiceLdapreset,
       "slbCurCfgVirtServiceLdapslb": slbCurCfgVirtServiceLdapslb,
       "slbCurCfgVirtServiceSip": slbCurCfgVirtServiceSip,
       "slbCurCfgVirtServiceXForwardedFor": slbCurCfgVirtServiceXForwardedFor,
       "slbCurCfgVirtServiceHttpRedir": slbCurCfgVirtServiceHttpRedir,
       "slbCurCfgVirtServicePbindRport": slbCurCfgVirtServicePbindRport,
       "slbCurCfgVirtServiceEgressPip": slbCurCfgVirtServiceEgressPip,
       "slbCurCfgVirtServiceCookieDname": slbCurCfgVirtServiceCookieDname,
       "slbCurCfgVirtServiceWts": slbCurCfgVirtServiceWts,
       "slbCurCfgVirtServiceUhash": slbCurCfgVirtServiceUhash,
       "slbCurCfgVirtServiceTimeOut": slbCurCfgVirtServiceTimeOut,
       "slbCurCfgVirtServiceSdpNat": slbCurCfgVirtServiceSdpNat,
       "slbCurCfgVirtServiceSessionMirror": slbCurCfgVirtServiceSessionMirror,
       "slbCurCfgVirtServiceSoftGrid": slbCurCfgVirtServiceSoftGrid,
       "slbCurCfgVirtServiceConnPooling": slbCurCfgVirtServiceConnPooling,
       "slbNewCfgVirtServicesTable": slbNewCfgVirtServicesTable,
       "slbNewCfgVirtServicesEntry": slbNewCfgVirtServicesEntry,
       "slbNewCfgVirtServIndex": slbNewCfgVirtServIndex,
       "slbNewCfgVirtServiceIndex": slbNewCfgVirtServiceIndex,
       "slbNewCfgVirtServiceVirtPort": slbNewCfgVirtServiceVirtPort,
       "slbNewCfgVirtServiceRealGroup": slbNewCfgVirtServiceRealGroup,
       "slbNewCfgVirtServiceRealPort": slbNewCfgVirtServiceRealPort,
       "slbNewCfgVirtServiceUDPBalance": slbNewCfgVirtServiceUDPBalance,
       "slbNewCfgVirtServiceHname": slbNewCfgVirtServiceHname,
       "slbNewCfgVirtServiceBwmContract": slbNewCfgVirtServiceBwmContract,
       "slbNewCfgVirtServiceDirServerRtn": slbNewCfgVirtServiceDirServerRtn,
       "slbNewCfgVirtServiceRtspUrlParse": slbNewCfgVirtServiceRtspUrlParse,
       "slbNewCfgVirtServiceDBind": slbNewCfgVirtServiceDBind,
       "slbNewCfgVirtServiceFtpParsing": slbNewCfgVirtServiceFtpParsing,
       "slbNewCfgVirtServiceRemapUDPFrags": slbNewCfgVirtServiceRemapUDPFrags,
       "slbNewCfgVirtServiceDnsSlb": slbNewCfgVirtServiceDnsSlb,
       "slbNewCfgVirtServiceResponseCount": slbNewCfgVirtServiceResponseCount,
       "slbNewCfgVirtServicePBind": slbNewCfgVirtServicePBind,
       "slbNewCfgVirtServiceCname": slbNewCfgVirtServiceCname,
       "slbNewCfgVirtServiceCoffset": slbNewCfgVirtServiceCoffset,
       "slbNewCfgVirtServiceClength": slbNewCfgVirtServiceClength,
       "slbNewCfgVirtServiceUriCookie": slbNewCfgVirtServiceUriCookie,
       "slbNewCfgVirtServiceCExpire": slbNewCfgVirtServiceCExpire,
       "slbNewCfgVirtServiceCookieMode": slbNewCfgVirtServiceCookieMode,
       "slbNewCfgVirtServiceHttpSlb": slbNewCfgVirtServiceHttpSlb,
       "slbNewCfgVirtServiceHttpSlbOption": slbNewCfgVirtServiceHttpSlbOption,
       "slbNewCfgVirtServiceHttpSlb2": slbNewCfgVirtServiceHttpSlb2,
       "slbNewCfgVirtServiceHttpHdrName": slbNewCfgVirtServiceHttpHdrName,
       "slbNewCfgVirtServiceUrlHashLen": slbNewCfgVirtServiceUrlHashLen,
       "slbNewCfgVirtServiceDelete": slbNewCfgVirtServiceDelete,
       "slbNewCfgVirtServiceDirect": slbNewCfgVirtServiceDirect,
       "slbNewCfgVirtServiceThash": slbNewCfgVirtServiceThash,
       "slbNewCfgVirtServiceLdapreset": slbNewCfgVirtServiceLdapreset,
       "slbNewCfgVirtServiceLdapslb": slbNewCfgVirtServiceLdapslb,
       "slbNewCfgVirtServiceSip": slbNewCfgVirtServiceSip,
       "slbNewCfgVirtServiceXForwardedFor": slbNewCfgVirtServiceXForwardedFor,
       "slbNewCfgVirtServiceHttpRedir": slbNewCfgVirtServiceHttpRedir,
       "slbNewCfgVirtServicePbindRport": slbNewCfgVirtServicePbindRport,
       "slbNewCfgVirtServiceEgressPip": slbNewCfgVirtServiceEgressPip,
       "slbNewCfgVirtServiceCookieDname": slbNewCfgVirtServiceCookieDname,
       "slbNewCfgVirtServiceWts": slbNewCfgVirtServiceWts,
       "slbNewCfgVirtServiceUhash": slbNewCfgVirtServiceUhash,
       "slbNewCfgVirtServiceTimeOut": slbNewCfgVirtServiceTimeOut,
       "slbNewCfgVirtServiceSdpNat": slbNewCfgVirtServiceSdpNat,
       "slbNewCfgVirtServiceSessionMirror": slbNewCfgVirtServiceSessionMirror,
       "slbNewCfgVirtServiceSoftGrid": slbNewCfgVirtServiceSoftGrid,
       "slbNewCfgVirtServiceConnPooling": slbNewCfgVirtServiceConnPooling,
       "slbUrlBwmTableMaxSize": slbUrlBwmTableMaxSize,
       "slbCurCfgUrlBwmTable": slbCurCfgUrlBwmTable,
       "slbCurCfgUrlBwmEntry": slbCurCfgUrlBwmEntry,
       "slbCurCfgUrlBwmVirtServIndex": slbCurCfgUrlBwmVirtServIndex,
       "slbCurCfgUrlBwmVirtServiceIndex": slbCurCfgUrlBwmVirtServiceIndex,
       "slbCurCfgUrlBwmUrlId": slbCurCfgUrlBwmUrlId,
       "slbCurCfgUrlBwmContract": slbCurCfgUrlBwmContract,
       "slbNewCfgUrlBwmTable": slbNewCfgUrlBwmTable,
       "slbNewCfgUrlBwmEntry": slbNewCfgUrlBwmEntry,
       "slbNewCfgUrlBwmVirtServIndex": slbNewCfgUrlBwmVirtServIndex,
       "slbNewCfgUrlBwmVirtServiceIndex": slbNewCfgUrlBwmVirtServiceIndex,
       "slbNewCfgUrlBwmUrlId": slbNewCfgUrlBwmUrlId,
       "slbNewCfgUrlBwmContract": slbNewCfgUrlBwmContract,
       "slbNewCfgUrlBwmDelete": slbNewCfgUrlBwmDelete,
       "portCfg": portCfg,
       "slbPortTableMaxSize": slbPortTableMaxSize,
       "slbCurCfgPortTable": slbCurCfgPortTable,
       "slbCurCfgPortEntry": slbCurCfgPortEntry,
       "slbCurCfgPortIndex": slbCurCfgPortIndex,
       "slbCurCfgPortSlbState": slbCurCfgPortSlbState,
       "slbCurCfgPortSlbHotStandby": slbCurCfgPortSlbHotStandby,
       "slbCurCfgPortSlbInterSwitch": slbCurCfgPortSlbInterSwitch,
       "slbCurCfgPortSlbPipState": slbCurCfgPortSlbPipState,
       "slbCurCfgPortSlbRtsState": slbCurCfgPortSlbRtsState,
       "slbCurCfgPortSlbIdslbState": slbCurCfgPortSlbIdslbState,
       "slbNewCfgPortTable": slbNewCfgPortTable,
       "slbNewCfgPortEntry": slbNewCfgPortEntry,
       "slbNewCfgPortIndex": slbNewCfgPortIndex,
       "slbNewCfgPortSlbState": slbNewCfgPortSlbState,
       "slbNewCfgPortSlbHotStandby": slbNewCfgPortSlbHotStandby,
       "slbNewCfgPortSlbInterSwitch": slbNewCfgPortSlbInterSwitch,
       "slbNewCfgPortSlbPipState": slbNewCfgPortSlbPipState,
       "slbNewCfgPortSlbRtsState": slbNewCfgPortSlbRtsState,
       "slbNewCfgPortDelete": slbNewCfgPortDelete,
       "slbNewCfgPortSlbIdslbState": slbNewCfgPortSlbIdslbState,
       "syncCfg": syncCfg,
       "syncGeneralCfg": syncGeneralCfg,
       "slbCurCfgSyncFilt": slbCurCfgSyncFilt,
       "slbNewCfgSyncFilt": slbNewCfgSyncFilt,
       "slbCurCfgSyncPort": slbCurCfgSyncPort,
       "slbNewCfgSyncPort": slbNewCfgSyncPort,
       "slbCurCfgSyncVrrp": slbCurCfgSyncVrrp,
       "slbNewCfgSyncVrrp": slbNewCfgSyncVrrp,
       "slbCurCfgSyncPip": slbCurCfgSyncPip,
       "slbNewCfgSyncPip": slbNewCfgSyncPip,
       "slbCurCfgSyncSfo": slbCurCfgSyncSfo,
       "slbNewCfgSyncSfo": slbNewCfgSyncSfo,
       "slbCurCfgSyncSfoUpdatePeriod": slbCurCfgSyncSfoUpdatePeriod,
       "slbNewCfgSyncSfoUpdatePeriod": slbNewCfgSyncSfoUpdatePeriod,
       "slbCurCfgSyncBwm": slbCurCfgSyncBwm,
       "slbNewCfgSyncBwm": slbNewCfgSyncBwm,
       "slbCurCfgSyncPeerPip": slbCurCfgSyncPeerPip,
       "slbNewCfgSyncPeerPip": slbNewCfgSyncPeerPip,
       "slbPeerTableMaxSize": slbPeerTableMaxSize,
       "slbCurCfgPeerTable": slbCurCfgPeerTable,
       "slbCurCfgPeerEntry": slbCurCfgPeerEntry,
       "slbCurCfgPeerIndex": slbCurCfgPeerIndex,
       "slbCurCfgPeerIpAddr": slbCurCfgPeerIpAddr,
       "slbCurCfgPeerState": slbCurCfgPeerState,
       "slbNewCfgPeerTable": slbNewCfgPeerTable,
       "slbNewCfgPeerEntry": slbNewCfgPeerEntry,
       "slbNewCfgPeerIndex": slbNewCfgPeerIndex,
       "slbNewCfgPeerIpAddr": slbNewCfgPeerIpAddr,
       "slbNewCfgPeerState": slbNewCfgPeerState,
       "slbNewCfgPeerDelete": slbNewCfgPeerDelete,
       "wapCfg": wapCfg,
       "slbCurCfgWapTpcp": slbCurCfgWapTpcp,
       "slbNewCfgWapTpcp": slbNewCfgWapTpcp,
       "slbCurCfgWapDebug": slbCurCfgWapDebug,
       "slbNewCfgWapDebug": slbNewCfgWapDebug,
       "waphcCfg": waphcCfg,
       "slbCurCfgWaphcWSPPort": slbCurCfgWaphcWSPPort,
       "slbNewCfgWaphcWSPPort": slbNewCfgWaphcWSPPort,
       "slbCurCfgWaphcOffset": slbCurCfgWaphcOffset,
       "slbNewCfgWaphcOffset": slbNewCfgWaphcOffset,
       "slbCurCfgWaphcSndContent": slbCurCfgWaphcSndContent,
       "slbNewCfgWaphcSndContent": slbNewCfgWaphcSndContent,
       "slbCurCfgWaphcRcvContent": slbCurCfgWaphcRcvContent,
       "slbNewCfgWaphcRcvContent": slbNewCfgWaphcRcvContent,
       "slbCurCfgWaphcWTLSPort": slbCurCfgWaphcWTLSPort,
       "slbNewCfgWaphcWTLSPort": slbNewCfgWaphcWTLSPort,
       "slbCurCfgWaphcWTPSndContent": slbCurCfgWaphcWTPSndContent,
       "slbNewCfgWaphcWTPSndContent": slbNewCfgWaphcWTPSndContent,
       "slbCurCfgWaphcWTPRcvContent": slbCurCfgWaphcWTPRcvContent,
       "slbNewCfgWaphcWTPRcvContent": slbNewCfgWaphcWTPRcvContent,
       "slbCurCfgWaphcWTPConnContent": slbCurCfgWaphcWTPConnContent,
       "slbNewCfgWaphcWTPConnContent": slbNewCfgWaphcWTPConnContent,
       "slbCurCfgWaphcWTPPort": slbCurCfgWaphcWTPPort,
       "slbNewCfgWaphcWTPPort": slbNewCfgWaphcWTPPort,
       "slbCurCfgWaphcWTLSWSPPort": slbCurCfgWaphcWTLSWSPPort,
       "slbNewCfgWaphcWTLSWSPPort": slbNewCfgWaphcWTLSWSPPort,
       "slbCurCfgWaphcWTPOffset": slbCurCfgWaphcWTPOffset,
       "slbNewCfgWaphcWTPOffset": slbNewCfgWaphcWTPOffset,
       "slbCurCfgWaphcCouple": slbCurCfgWaphcCouple,
       "slbNewCfgWaphcCouple": slbNewCfgWaphcCouple,
       "synAttackDetCfg": synAttackDetCfg,
       "synAttackCurCfgInterval": synAttackCurCfgInterval,
       "synAttackNewCfgInterval": synAttackNewCfgInterval,
       "synAttackCurCfgThreshhold": synAttackCurCfgThreshhold,
       "synAttackNewCfgThreshhold": synAttackNewCfgThreshhold,
       "hcsCfg": hcsCfg,
       "hcsTableMaxSize": hcsTableMaxSize,
       "hcsCurCfgTable": hcsCurCfgTable,
       "hcsCurCfgTableEntry": hcsCurCfgTableEntry,
       "hcsCurCfgScriptIndex": hcsCurCfgScriptIndex,
       "hcsCurCfgScriptString": hcsCurCfgScriptString,
       "hcsNewCfgTable": hcsNewCfgTable,
       "hcsNewCfgTableEntry": hcsNewCfgTableEntry,
       "hcsNewCfgScriptIndex": hcsNewCfgScriptIndex,
       "hcsNewCfgScriptString": hcsNewCfgScriptString,
       "hcsNewCfgAddSendCmd": hcsNewCfgAddSendCmd,
       "hcsNewCfgAddExpectCmd": hcsNewCfgAddExpectCmd,
       "hcsNewCfgAddCloseCmd": hcsNewCfgAddCloseCmd,
       "hcsNewCfgRemLastCmd": hcsNewCfgRemLastCmd,
       "hcsNewCfgDeleteScript": hcsNewCfgDeleteScript,
       "hcsNewCfgAddOffsetCmd": hcsNewCfgAddOffsetCmd,
       "hcsNewCfgAddWaitCmd": hcsNewCfgAddWaitCmd,
       "hcsNewCfgAddOpenProtCmd": hcsNewCfgAddOpenProtCmd,
       "hcsNewCfgAddNsendCmd": hcsNewCfgAddNsendCmd,
       "hcsNewCfgAddNexpectCmd": hcsNewCfgAddNexpectCmd,
       "hcsNewCfgAddDepthCmd": hcsNewCfgAddDepthCmd,
       "hcsNewCfgAddLongBsendCmd": hcsNewCfgAddLongBsendCmd,
       "hcsNewCfgAddLongBexpectCmd": hcsNewCfgAddLongBexpectCmd,
       "hcsNewCfgAddLongSendCmd": hcsNewCfgAddLongSendCmd,
       "hcsNewCfgAddLongExpectCmd": hcsNewCfgAddLongExpectCmd,
       "hcsNewCfgAddLongNsendCmd": hcsNewCfgAddLongNsendCmd,
       "hcsNewCfgAddLongNexpectCmd": hcsNewCfgAddLongNexpectCmd,
       "snmphcCfg": snmphcCfg,
       "snmphcTableMaxSize": snmphcTableMaxSize,
       "snmphcCurCfgTable": snmphcCurCfgTable,
       "snmphcCurCfgTableEntry": snmphcCurCfgTableEntry,
       "snmphcCurCfgIndex": snmphcCurCfgIndex,
       "snmphcCurCfgOid": snmphcCurCfgOid,
       "snmphcCurCfgCommString": snmphcCurCfgCommString,
       "snmphcCurCfgRcvContent": snmphcCurCfgRcvContent,
       "snmphcCurCfgInvert": snmphcCurCfgInvert,
       "snmphcCurCfgUseWeight": snmphcCurCfgUseWeight,
       "snmphcNewCfgTable": snmphcNewCfgTable,
       "snmphcNewCfgTableEntry": snmphcNewCfgTableEntry,
       "snmphcNewCfgIndex": snmphcNewCfgIndex,
       "snmphcNewCfgOid": snmphcNewCfgOid,
       "snmphcNewCfgCommString": snmphcNewCfgCommString,
       "snmphcNewCfgRcvContent": snmphcNewCfgRcvContent,
       "snmphcNewCfgInvert": snmphcNewCfgInvert,
       "snmphcNewCfgDeleteHc": snmphcNewCfgDeleteHc,
       "snmphcNewCfgUseWeight": snmphcNewCfgUseWeight,
       "pipTblCfg": pipTblCfg,
       "pipTableMaxSize": pipTableMaxSize,
       "pipCurCfgBaseType": pipCurCfgBaseType,
       "pipCurCfgTable": pipCurCfgTable,
       "pipCurCfgTableEntry": pipCurCfgTableEntry,
       "pipCurCfgPip": pipCurCfgPip,
       "pipCurCfgPortMap": pipCurCfgPortMap,
       "pipCurCfgVlanMap": pipCurCfgVlanMap,
       "pipNewCfgBaseType": pipNewCfgBaseType,
       "pipNewCfgTable": pipNewCfgTable,
       "pipNewCfgTableEntry": pipNewCfgTableEntry,
       "pipNewCfgPip": pipNewCfgPip,
       "pipNewCfgPortMap": pipNewCfgPortMap,
       "pipNewCfgVlanMap": pipNewCfgVlanMap,
       "pipNewCfgDelete": pipNewCfgDelete,
       "pipNewCfgAddPortVlan": pipNewCfgAddPortVlan,
       "pipNewCfgRemovePortVlan": pipNewCfgRemovePortVlan,
       "linklbCfg": linklbCfg,
       "slbCurCfgLinklbState": slbCurCfgLinklbState,
       "slbNewCfgLinklbState": slbNewCfgLinklbState,
       "slbCurCfgLinklbRealGroup": slbCurCfgLinklbRealGroup,
       "slbNewCfgLinklbRealGroup": slbNewCfgLinklbRealGroup,
       "slbLinklbDrecord": slbLinklbDrecord,
       "slbDrecordTableMaxSize": slbDrecordTableMaxSize,
       "slbCurCfgDrecordTable": slbCurCfgDrecordTable,
       "slbCurCfgDrecordEntry": slbCurCfgDrecordEntry,
       "slbCurCfgDrecordIndex": slbCurCfgDrecordIndex,
       "slbCurCfgDomainRecordState": slbCurCfgDomainRecordState,
       "slbCurCfgDomainRecordName": slbCurCfgDomainRecordName,
       "slbNewCfgDrecordTable": slbNewCfgDrecordTable,
       "slbNewCfgDrecordEntry": slbNewCfgDrecordEntry,
       "slbNewCfgDrecordIndex": slbNewCfgDrecordIndex,
       "slbNewCfgDomainRecordState": slbNewCfgDomainRecordState,
       "slbNewCfgDomainRecordName": slbNewCfgDomainRecordName,
       "slbNewCfgDrecordDelete": slbNewCfgDrecordDelete,
       "slbDrecordVirtRealMappingTableMaxSize": slbDrecordVirtRealMappingTableMaxSize,
       "slbCurCfgDrecordVirtRealMappingTable": slbCurCfgDrecordVirtRealMappingTable,
       "slbCurCfgDrecordVirtRealMappingEntry": slbCurCfgDrecordVirtRealMappingEntry,
       "slbCurCfgDomainRecordIndex": slbCurCfgDomainRecordIndex,
       "slbCurCfgEntryIndex": slbCurCfgEntryIndex,
       "slbCurCfgDrecordVirtServer": slbCurCfgDrecordVirtServer,
       "slbCurCfgDrecordRealServer": slbCurCfgDrecordRealServer,
       "slbCurCfgDrecordEntryState": slbCurCfgDrecordEntryState,
       "slbNewCfgDrecordVirtRealMappingTable": slbNewCfgDrecordVirtRealMappingTable,
       "slbNewCfgDrecordVirtRealMappingEntry": slbNewCfgDrecordVirtRealMappingEntry,
       "slbNewCfgDomainRecordIndex": slbNewCfgDomainRecordIndex,
       "slbNewCfgEntryIndex": slbNewCfgEntryIndex,
       "slbNewCfgDrecordVirtServer": slbNewCfgDrecordVirtServer,
       "slbNewCfgDrecordRealServer": slbNewCfgDrecordRealServer,
       "slbNewCfgDrecordEntryState": slbNewCfgDrecordEntryState,
       "slbNewCfgDrecordEntryDelete": slbNewCfgDrecordEntryDelete,
       "slbCurCfgLinklbTTL": slbCurCfgLinklbTTL,
       "slbNewCfgLinklbTTL": slbNewCfgLinklbTTL,
       "smtportCfg": smtportCfg,
       "slbSmtportTableMaxSize": slbSmtportTableMaxSize,
       "slbCurCfgSmtportTable": slbCurCfgSmtportTable,
       "slbCurCfgSmtportEntry": slbCurCfgSmtportEntry,
       "slbCurCfgSmtportIndex": slbCurCfgSmtportIndex,
       "slbCurCfgSmtportNum": slbCurCfgSmtportNum,
       "slbNewCfgSmtportTable": slbNewCfgSmtportTable,
       "slbNewCfgSmtportEntry": slbNewCfgSmtportEntry,
       "slbNewCfgSmtportIndex": slbNewCfgSmtportIndex,
       "slbNewCfgSmtportNum": slbNewCfgSmtportNum,
       "slbNewCfgSmtportDelete": slbNewCfgSmtportDelete,
       "filterCfg": filterCfg,
       "fltCfgTableMaxSize": fltCfgTableMaxSize,
       "fltCurCfgTable": fltCurCfgTable,
       "fltCurCfgTableEntry": fltCurCfgTableEntry,
       "fltCurCfgIndx": fltCurCfgIndx,
       "fltCurCfgSrcIp": fltCurCfgSrcIp,
       "fltCurCfgSrcIpMask": fltCurCfgSrcIpMask,
       "fltCurCfgDstIp": fltCurCfgDstIp,
       "fltCurCfgDstIpMask": fltCurCfgDstIpMask,
       "fltCurCfgProtocol": fltCurCfgProtocol,
       "fltCurCfgRangeHighSrcPort": fltCurCfgRangeHighSrcPort,
       "fltCurCfgRangeLowSrcPort": fltCurCfgRangeLowSrcPort,
       "fltCurCfgRangeLowDstPort": fltCurCfgRangeLowDstPort,
       "fltCurCfgRangeHighDstPort": fltCurCfgRangeHighDstPort,
       "fltCurCfgAction": fltCurCfgAction,
       "fltCurCfgRedirPort": fltCurCfgRedirPort,
       "fltCurCfgRedirGroup": fltCurCfgRedirGroup,
       "fltCurCfgLog": fltCurCfgLog,
       "fltCurCfgState": fltCurCfgState,
       "fltCurCfgNat": fltCurCfgNat,
       "fltCurCfgCache": fltCurCfgCache,
       "fltCurCfgInvert": fltCurCfgInvert,
       "fltCurCfgClientProxy": fltCurCfgClientProxy,
       "fltCurCfgTcpAck": fltCurCfgTcpAck,
       "fltCurCfgSrcMac": fltCurCfgSrcMac,
       "fltCurCfgDstMac": fltCurCfgDstMac,
       "fltCurCfgFtpNatActive": fltCurCfgFtpNatActive,
       "fltCurCfgAclTcpUrg": fltCurCfgAclTcpUrg,
       "fltCurCfgAclTcpAck": fltCurCfgAclTcpAck,
       "fltCurCfgAclTcpPsh": fltCurCfgAclTcpPsh,
       "fltCurCfgAclTcpRst": fltCurCfgAclTcpRst,
       "fltCurCfgAclTcpSyn": fltCurCfgAclTcpSyn,
       "fltCurCfgAclTcpFin": fltCurCfgAclTcpFin,
       "fltCurCfgAclIcmp": fltCurCfgAclIcmp,
       "fltCurCfgAclIpOption": fltCurCfgAclIpOption,
       "fltCurCfgBwmContract": fltCurCfgBwmContract,
       "fltCurCfgAclIpTos": fltCurCfgAclIpTos,
       "fltCurCfgAclIpTosMask": fltCurCfgAclIpTosMask,
       "fltCurCfgAclIpTosNew": fltCurCfgAclIpTosNew,
       "fltCurCfgFwlb": fltCurCfgFwlb,
       "fltCurCfgNatTimeout": fltCurCfgNatTimeout,
       "fltCurCfgLinklb": fltCurCfgLinklb,
       "fltCurCfgWapRadiusSnoop": fltCurCfgWapRadiusSnoop,
       "fltCurCfgSrcIpMac": fltCurCfgSrcIpMac,
       "fltCurCfgDstIpMac": fltCurCfgDstIpMac,
       "fltCurCfgIdslbHash": fltCurCfgIdslbHash,
       "fltCurCfgVlan": fltCurCfgVlan,
       "fltCurCfgName": fltCurCfgName,
       "fltCurCfgTcpRateLimit": fltCurCfgTcpRateLimit,
       "fltCurCfgTcpRateMaxConn": fltCurCfgTcpRateMaxConn,
       "fltCurCfgHash": fltCurCfgHash,
       "fltCurCfgLayer7DenyState": fltCurCfgLayer7DenyState,
       "fltCurCfgLayer7DenyUrlBmap": fltCurCfgLayer7DenyUrlBmap,
       "fltCurCfgGotoFilter": fltCurCfgGotoFilter,
       "fltCurCfgRadiusWapPersist": fltCurCfgRadiusWapPersist,
       "fltCurCfgPbind": fltCurCfgPbind,
       "fltCurCfgTimeWindow": fltCurCfgTimeWindow,
       "fltCurCfgHoldDuration": fltCurCfgHoldDuration,
       "fltCurCfgPatternMatch": fltCurCfgPatternMatch,
       "fltCurCfgLayer7DenyMatchAll": fltCurCfgLayer7DenyMatchAll,
       "fltCurCfgProxyIp": fltCurCfgProxyIp,
       "fltCurCfgLayer7ParseAll": fltCurCfgLayer7ParseAll,
       "fltCurCfgSecurityParseAll": fltCurCfgSecurityParseAll,
       "fltCurCfgPatternMatchGroupBmap": fltCurCfgPatternMatchGroupBmap,
       "fltCurCfg8021pBitsValue": fltCurCfg8021pBitsValue,
       "fltCurCfg8021pBitsMatch": fltCurCfg8021pBitsMatch,
       "fltCurCfgAclIpLength": fltCurCfgAclIpLength,
       "fltCurCfgIdsGroup": fltCurCfgIdsGroup,
       "fltCurCfgEgressPip": fltCurCfgEgressPip,
       "fltCurCfgDbind": fltCurCfgDbind,
       "fltCurCfgRevBwmContract": fltCurCfgRevBwmContract,
       "fltCurCfgReverse": fltCurCfgReverse,
       "fltCurCfgParseChn": fltCurCfgParseChn,
       "fltCurCfgRtpBwmContract": fltCurCfgRtpBwmContract,
       "fltCurCfgSipParsing": fltCurCfgSipParsing,
       "fltCurCfgSessionMirror": fltCurCfgSessionMirror,
       "fltCurCfgIpVer": fltCurCfgIpVer,
       "fltCurCfgIpv6Sip": fltCurCfgIpv6Sip,
       "fltCurCfgIpv6Sprefix": fltCurCfgIpv6Sprefix,
       "fltCurCfgIpv6Dip": fltCurCfgIpv6Dip,
       "fltCurCfgIpv6Dprefix": fltCurCfgIpv6Dprefix,
       "fltNewCfgTable": fltNewCfgTable,
       "fltNewCfgTableEntry": fltNewCfgTableEntry,
       "fltNewCfgIndx": fltNewCfgIndx,
       "fltNewCfgSrcIp": fltNewCfgSrcIp,
       "fltNewCfgSrcIpMask": fltNewCfgSrcIpMask,
       "fltNewCfgDstIp": fltNewCfgDstIp,
       "fltNewCfgDstIpMask": fltNewCfgDstIpMask,
       "fltNewCfgProtocol": fltNewCfgProtocol,
       "fltNewCfgRangeHighSrcPort": fltNewCfgRangeHighSrcPort,
       "fltNewCfgRangeLowSrcPort": fltNewCfgRangeLowSrcPort,
       "fltNewCfgRangeLowDstPort": fltNewCfgRangeLowDstPort,
       "fltNewCfgRangeHighDstPort": fltNewCfgRangeHighDstPort,
       "fltNewCfgAction": fltNewCfgAction,
       "fltNewCfgRedirPort": fltNewCfgRedirPort,
       "fltNewCfgRedirGroup": fltNewCfgRedirGroup,
       "fltNewCfgLog": fltNewCfgLog,
       "fltNewCfgState": fltNewCfgState,
       "fltNewCfgDelete": fltNewCfgDelete,
       "fltNewCfgNat": fltNewCfgNat,
       "fltNewCfgCache": fltNewCfgCache,
       "fltNewCfgInvert": fltNewCfgInvert,
       "fltNewCfgClientProxy": fltNewCfgClientProxy,
       "fltNewCfgTcpAck": fltNewCfgTcpAck,
       "fltNewCfgSrcMac": fltNewCfgSrcMac,
       "fltNewCfgDstMac": fltNewCfgDstMac,
       "fltNewCfgFtpNatActive": fltNewCfgFtpNatActive,
       "fltNewCfgAclTcpUrg": fltNewCfgAclTcpUrg,
       "fltNewCfgAclTcpAck": fltNewCfgAclTcpAck,
       "fltNewCfgAclTcpPsh": fltNewCfgAclTcpPsh,
       "fltNewCfgAclTcpRst": fltNewCfgAclTcpRst,
       "fltNewCfgAclTcpSyn": fltNewCfgAclTcpSyn,
       "fltNewCfgAclTcpFin": fltNewCfgAclTcpFin,
       "fltNewCfgAclIcmp": fltNewCfgAclIcmp,
       "fltNewCfgAclIpOption": fltNewCfgAclIpOption,
       "fltNewCfgBwmContract": fltNewCfgBwmContract,
       "fltNewCfgAclIpTos": fltNewCfgAclIpTos,
       "fltNewCfgAclIpTosMask": fltNewCfgAclIpTosMask,
       "fltNewCfgAclIpTosNew": fltNewCfgAclIpTosNew,
       "fltNewCfgFwlb": fltNewCfgFwlb,
       "fltNewCfgNatTimeout": fltNewCfgNatTimeout,
       "fltNewCfgLinklb": fltNewCfgLinklb,
       "fltNewCfgWapRadiusSnoop": fltNewCfgWapRadiusSnoop,
       "fltNewCfgSrcIpMac": fltNewCfgSrcIpMac,
       "fltNewCfgDstIpMac": fltNewCfgDstIpMac,
       "fltNewCfgIdslbHash": fltNewCfgIdslbHash,
       "fltNewCfgVlan": fltNewCfgVlan,
       "fltNewCfgName": fltNewCfgName,
       "fltNewCfgTcpRateLimit": fltNewCfgTcpRateLimit,
       "fltNewCfgTcpRateMaxConn": fltNewCfgTcpRateMaxConn,
       "fltNewCfgHash": fltNewCfgHash,
       "fltNewCfgLayer7DenyState": fltNewCfgLayer7DenyState,
       "fltNewCfgLayer7DenyUrlBmap": fltNewCfgLayer7DenyUrlBmap,
       "fltNewCfgLayer7DenyAddUrl": fltNewCfgLayer7DenyAddUrl,
       "fltNewCfgLayer7DenyRemUrl": fltNewCfgLayer7DenyRemUrl,
       "fltNewCfgGotoFilter": fltNewCfgGotoFilter,
       "fltNewCfgRadiusWapPersist": fltNewCfgRadiusWapPersist,
       "fltNewCfgPbind": fltNewCfgPbind,
       "fltNewCfgTimeWindow": fltNewCfgTimeWindow,
       "fltNewCfgHoldDuration": fltNewCfgHoldDuration,
       "fltNewCfgPatternMatch": fltNewCfgPatternMatch,
       "fltNewCfgLayer7DenyMatchAll": fltNewCfgLayer7DenyMatchAll,
       "fltNewCfgProxyIp": fltNewCfgProxyIp,
       "fltNewCfgLayer7ParseAll": fltNewCfgLayer7ParseAll,
       "fltNewCfgSecurityParseAll": fltNewCfgSecurityParseAll,
       "fltNewCfgPatternMatchGroupBmap": fltNewCfgPatternMatchGroupBmap,
       "fltNewCfgAddPatternMatchGroup": fltNewCfgAddPatternMatchGroup,
       "fltNewCfgRemPatternMatchGroup": fltNewCfgRemPatternMatchGroup,
       "fltNewCfg8021pBitsValue": fltNewCfg8021pBitsValue,
       "fltNewCfg8021pBitsMatch": fltNewCfg8021pBitsMatch,
       "fltNewCfgAclIpLength": fltNewCfgAclIpLength,
       "fltNewCfgIdsGroup": fltNewCfgIdsGroup,
       "fltNewCfgEgressPip": fltNewCfgEgressPip,
       "fltNewCfgDbind": fltNewCfgDbind,
       "fltNewCfgRevBwmContract": fltNewCfgRevBwmContract,
       "fltNewCfgReverse": fltNewCfgReverse,
       "fltNewCfgParseChn": fltNewCfgParseChn,
       "fltNewCfgRtpBwmContract": fltNewCfgRtpBwmContract,
       "fltNewCfgSipParsing": fltNewCfgSipParsing,
       "fltNewCfgSessionMirror": fltNewCfgSessionMirror,
       "fltNewCfgIpVer": fltNewCfgIpVer,
       "fltNewCfgIpv6Sip": fltNewCfgIpv6Sip,
       "fltNewCfgIpv6Sprefix": fltNewCfgIpv6Sprefix,
       "fltNewCfgIpv6Dip": fltNewCfgIpv6Dip,
       "fltNewCfgIpv6Dprefix": fltNewCfgIpv6Dprefix,
       "fltCurCfgPortTable": fltCurCfgPortTable,
       "fltCurCfgPortTableEntry": fltCurCfgPortTableEntry,
       "fltCurCfgPortIndx": fltCurCfgPortIndx,
       "fltCurCfgPortState": fltCurCfgPortState,
       "fltCurCfgPortFiltBmap": fltCurCfgPortFiltBmap,
       "fltNewCfgPortTable": fltNewCfgPortTable,
       "fltNewCfgPortTableEntry": fltNewCfgPortTableEntry,
       "fltNewCfgPortIndx": fltNewCfgPortIndx,
       "fltNewCfgPortState": fltNewCfgPortState,
       "fltNewCfgPortFiltBmap": fltNewCfgPortFiltBmap,
       "fltNewCfgPortAddFiltRule": fltNewCfgPortAddFiltRule,
       "fltNewCfgPortRemFiltRule": fltNewCfgPortRemFiltRule,
       "fltUrlBwmTableMaxSize": fltUrlBwmTableMaxSize,
       "fltCurCfgUrlBwmTable": fltCurCfgUrlBwmTable,
       "fltCurCfgUrlBwmEntry": fltCurCfgUrlBwmEntry,
       "fltCurCfgUrlBwmFltIndex": fltCurCfgUrlBwmFltIndex,
       "fltCurCfgUrlBwmUrlId": fltCurCfgUrlBwmUrlId,
       "fltCurCfgUrlBwmContract": fltCurCfgUrlBwmContract,
       "fltCurCfgUrlReverseBwmContract": fltCurCfgUrlReverseBwmContract,
       "fltNewCfgUrlBwmTable": fltNewCfgUrlBwmTable,
       "fltNewCfgUrlBwmEntry": fltNewCfgUrlBwmEntry,
       "fltNewCfgUrlBwmFltIndex": fltNewCfgUrlBwmFltIndex,
       "fltNewCfgUrlBwmUrlId": fltNewCfgUrlBwmUrlId,
       "fltNewCfgUrlBwmContract": fltNewCfgUrlBwmContract,
       "fltNewCfgUrlBwmDelete": fltNewCfgUrlBwmDelete,
       "fltNewCfgUrlReverseBwmContract": fltNewCfgUrlReverseBwmContract,
       "fltCfgHttpRedirMappingTableMaxSize": fltCfgHttpRedirMappingTableMaxSize,
       "fltCurCfgHttpRedirMappingTable": fltCurCfgHttpRedirMappingTable,
       "fltCurCfgHttpRedirMappingEntry": fltCurCfgHttpRedirMappingEntry,
       "fltCurCfgHttpRedirMappingFilter": fltCurCfgHttpRedirMappingFilter,
       "fltCurCfgHttpRedirMappingFromStr": fltCurCfgHttpRedirMappingFromStr,
       "fltCurCfgHttpRedirMappingToStr": fltCurCfgHttpRedirMappingToStr,
       "fltNewCfgHttpRedirMappingTable": fltNewCfgHttpRedirMappingTable,
       "fltNewCfgHttpRedirMappingEntry": fltNewCfgHttpRedirMappingEntry,
       "fltNewCfgHttpRedirMappingFilter": fltNewCfgHttpRedirMappingFilter,
       "fltNewCfgHttpRedirMappingFromStr": fltNewCfgHttpRedirMappingFromStr,
       "fltNewCfgHttpRedirMappingToStr": fltNewCfgHttpRedirMappingToStr,
       "fltNewCfgHttpRedirMappingDelete": fltNewCfgHttpRedirMappingDelete,
       "gslbCfg": gslbCfg,
       "gslbGeneralCfg": gslbGeneralCfg,
       "gslbCurCfgGenState": gslbCurCfgGenState,
       "gslbNewCfgGenState": gslbNewCfgGenState,
       "gslbCurCfgGenHttpRedirect": gslbCurCfgGenHttpRedirect,
       "gslbNewCfgGenHttpRedirect": gslbNewCfgGenHttpRedirect,
       "gslbCurCfgGenMinco": gslbCurCfgGenMinco,
       "gslbNewCfgGenMinco": gslbNewCfgGenMinco,
       "gslbCurCfgGenUsern": gslbCurCfgGenUsern,
       "gslbNewCfgGenUsern": gslbNewCfgGenUsern,
       "gslbCurCfgGenNoremote": gslbCurCfgGenNoremote,
       "gslbNewCfgGenNoremote": gslbNewCfgGenNoremote,
       "gslbCurCfgGenEncrypt": gslbCurCfgGenEncrypt,
       "gslbNewCfgGenEncrypt": gslbNewCfgGenEncrypt,
       "gslbCurCfgGenRemSiteUpdatePort": gslbCurCfgGenRemSiteUpdatePort,
       "gslbNewCfgGenRemSiteUpdatePort": gslbNewCfgGenRemSiteUpdatePort,
       "gslbCurCfgGenSessUtilCap": gslbCurCfgGenSessUtilCap,
       "gslbNewCfgGenSessUtilCap": gslbNewCfgGenSessUtilCap,
       "gslbCurCfgGenCpuUtilCap": gslbCurCfgGenCpuUtilCap,
       "gslbNewCfgGenCpuUtilCap": gslbNewCfgGenCpuUtilCap,
       "gslbCurCfgGenSourceIpNetmask": gslbCurCfgGenSourceIpNetmask,
       "gslbNewCfgGenSourceIpNetmask": gslbNewCfgGenSourceIpNetmask,
       "gslbCurCfgGenTimeout": gslbCurCfgGenTimeout,
       "gslbNewCfgGenTimeout": gslbNewCfgGenTimeout,
       "gslbCurCfgGenDnsDirect": gslbCurCfgGenDnsDirect,
       "gslbNewCfgGenDnsDirect": gslbNewCfgGenDnsDirect,
       "gslbCurCfgGenRemSiteUpdateVersion": gslbCurCfgGenRemSiteUpdateVersion,
       "gslbNewCfgGenRemSiteUpdateVersion": gslbNewCfgGenRemSiteUpdateVersion,
       "gslbCurCfgGenHostname": gslbCurCfgGenHostname,
       "gslbNewCfgGenHostname": gslbNewCfgGenHostname,
       "gslbCurCfgGenRemSiteUpdateIntervalSeconds": gslbCurCfgGenRemSiteUpdateIntervalSeconds,
       "gslbNewCfgGenRemSiteUpdateIntervalSeconds": gslbNewCfgGenRemSiteUpdateIntervalSeconds,
       "gslbCurCfgGenNoResp": gslbCurCfgGenNoResp,
       "gslbNewCfgGenNoResp": gslbNewCfgGenNoResp,
       "gslbSitesCfg": gslbSitesCfg,
       "gslbRemSiteTableMaxSize": gslbRemSiteTableMaxSize,
       "gslbCurCfgRemSiteTable": gslbCurCfgRemSiteTable,
       "gslbCurCfgRemSiteTableEntry": gslbCurCfgRemSiteTableEntry,
       "gslbCurCfgRemSiteIndx": gslbCurCfgRemSiteIndx,
       "gslbCurCfgRemSitePrimaryIp": gslbCurCfgRemSitePrimaryIp,
       "gslbCurCfgRemSiteSecondaryIp": gslbCurCfgRemSiteSecondaryIp,
       "gslbCurCfgRemSiteState": gslbCurCfgRemSiteState,
       "gslbCurCfgRemSiteUpdate": gslbCurCfgRemSiteUpdate,
       "gslbCurCfgRemSiteName": gslbCurCfgRemSiteName,
       "gslbNewCfgRemSiteTable": gslbNewCfgRemSiteTable,
       "gslbNewCfgRemSiteTableEntry": gslbNewCfgRemSiteTableEntry,
       "gslbNewCfgRemSiteIndx": gslbNewCfgRemSiteIndx,
       "gslbNewCfgRemSitePrimaryIp": gslbNewCfgRemSitePrimaryIp,
       "gslbNewCfgRemSiteSecondaryIp": gslbNewCfgRemSiteSecondaryIp,
       "gslbNewCfgRemSiteState": gslbNewCfgRemSiteState,
       "gslbNewCfgRemSiteUpdate": gslbNewCfgRemSiteUpdate,
       "gslbNewCfgRemSiteDelete": gslbNewCfgRemSiteDelete,
       "gslbNewCfgRemSiteName": gslbNewCfgRemSiteName,
       "gslbEnhNetworkCfg": gslbEnhNetworkCfg,
       "gslbEnhNetworkTableMaxSize": gslbEnhNetworkTableMaxSize,
       "gslbCurCfgEnhNetworkTable": gslbCurCfgEnhNetworkTable,
       "gslbCurCfgEnhNetworkTableEntry": gslbCurCfgEnhNetworkTableEntry,
       "gslbCurCfgEnhNetworkIndx": gslbCurCfgEnhNetworkIndx,
       "gslbCurCfgEnhNetworkState": gslbCurCfgEnhNetworkState,
       "gslbCurCfgEnhNetworkSourceIp": gslbCurCfgEnhNetworkSourceIp,
       "gslbCurCfgEnhNetworkNetMask": gslbCurCfgEnhNetworkNetMask,
       "gslbCurCfgEnhNetworkVirtServer": gslbCurCfgEnhNetworkVirtServer,
       "gslbCurCfgEnhNetworkRemRealServer": gslbCurCfgEnhNetworkRemRealServer,
       "gslbNewCfgEnhNetworkTable": gslbNewCfgEnhNetworkTable,
       "gslbNewCfgEnhNetworkTableEntry": gslbNewCfgEnhNetworkTableEntry,
       "gslbNewCfgEnhNetworkIndx": gslbNewCfgEnhNetworkIndx,
       "gslbNewCfgEnhNetworkState": gslbNewCfgEnhNetworkState,
       "gslbNewCfgEnhNetworkSourceIp": gslbNewCfgEnhNetworkSourceIp,
       "gslbNewCfgEnhNetworkNetMask": gslbNewCfgEnhNetworkNetMask,
       "gslbNewCfgEnhNetworkDelete": gslbNewCfgEnhNetworkDelete,
       "gslbNewCfgEnhNetworkVirtServer": gslbNewCfgEnhNetworkVirtServer,
       "gslbNewCfgEnhNetworkRemRealServer": gslbNewCfgEnhNetworkRemRealServer,
       "gslbNewCfgEnhNetworkAddVirtServer": gslbNewCfgEnhNetworkAddVirtServer,
       "gslbNewCfgEnhNetworkRemoveVirtServer": gslbNewCfgEnhNetworkRemoveVirtServer,
       "gslbNewCfgEnhNetworkAddRemRealServer": gslbNewCfgEnhNetworkAddRemRealServer,
       "gslbNewCfgEnhNetworkRemoveRemRealServer": gslbNewCfgEnhNetworkRemoveRemRealServer,
       "gslbRuleCfg": gslbRuleCfg,
       "gslbRuleTableMaxSize": gslbRuleTableMaxSize,
       "gslbCurCfgRuleTable": gslbCurCfgRuleTable,
       "gslbCurCfgRuleTableEntry": gslbCurCfgRuleTableEntry,
       "gslbCurCfgRuleIndx": gslbCurCfgRuleIndx,
       "gslbCurCfgRuleState": gslbCurCfgRuleState,
       "gslbCurCfgRuleStartHour": gslbCurCfgRuleStartHour,
       "gslbCurCfgRuleStartMin": gslbCurCfgRuleStartMin,
       "gslbCurCfgRuleEndHour": gslbCurCfgRuleEndHour,
       "gslbCurCfgRuleEndMin": gslbCurCfgRuleEndMin,
       "gslbCurCfgRuleTTL": gslbCurCfgRuleTTL,
       "gslbCurCfgRuleRR": gslbCurCfgRuleRR,
       "gslbNewCfgRuleTable": gslbNewCfgRuleTable,
       "gslbNewCfgRuleTableEntry": gslbNewCfgRuleTableEntry,
       "gslbNewCfgRuleIndx": gslbNewCfgRuleIndx,
       "gslbNewCfgRuleState": gslbNewCfgRuleState,
       "gslbNewCfgRuleStartHour": gslbNewCfgRuleStartHour,
       "gslbNewCfgRuleStartMin": gslbNewCfgRuleStartMin,
       "gslbNewCfgRuleEndHour": gslbNewCfgRuleEndHour,
       "gslbNewCfgRuleEndMin": gslbNewCfgRuleEndMin,
       "gslbNewCfgRuleTTL": gslbNewCfgRuleTTL,
       "gslbNewCfgRuleRR": gslbNewCfgRuleRR,
       "gslbNewCfgRuleDelete": gslbNewCfgRuleDelete,
       "gslbMetricTableMaxSize": gslbMetricTableMaxSize,
       "gslbCurCfgMetricTable": gslbCurCfgMetricTable,
       "gslbCurCfgMetricTableEntry": gslbCurCfgMetricTableEntry,
       "gslbCurCfgRuleMetricIndx": gslbCurCfgRuleMetricIndx,
       "gslbCurCfgMetricIndx": gslbCurCfgMetricIndx,
       "gslbCurCfgMetricMetric": gslbCurCfgMetricMetric,
       "gslbCurCfgMetricNetworkBmap": gslbCurCfgMetricNetworkBmap,
       "gslbNewCfgMetricTable": gslbNewCfgMetricTable,
       "gslbNewCfgMetricTableEntry": gslbNewCfgMetricTableEntry,
       "gslbNewCfgRuleMetricIndx": gslbNewCfgRuleMetricIndx,
       "gslbNewCfgMetricIndx": gslbNewCfgMetricIndx,
       "gslbNewCfgMetricMetric": gslbNewCfgMetricMetric,
       "gslbNewCfgMetricNetworkBmap": gslbNewCfgMetricNetworkBmap,
       "gslbNewCfgMetricAddNetwork": gslbNewCfgMetricAddNetwork,
       "gslbNewCfgMetricRemNetwork": gslbNewCfgMetricRemNetwork,
       "layer4TableSize": layer4TableSize,
       "curCfgFilterTableSize": curCfgFilterTableSize,
       "newCfgFilterTableSize": newCfgFilterTableSize,
       "curCfgRealServerTableSize": curCfgRealServerTableSize,
       "newCfgRealServerTableSize": newCfgRealServerTableSize,
       "curCfgRealServerGroupTableSize": curCfgRealServerGroupTableSize,
       "newCfgRealServerGroupTableSize": newCfgRealServerGroupTableSize,
       "curCfgVirtServerTableSize": curCfgVirtServerTableSize,
       "newCfgVirtServerTableSize": newCfgVirtServerTableSize,
       "wlmCfg": wlmCfg,
       "slbWlmTableMaxSize": slbWlmTableMaxSize,
       "slbCurCfgWlmTable": slbCurCfgWlmTable,
       "slbCurCfgWlmEntry": slbCurCfgWlmEntry,
       "slbCurCfgWlmIndex": slbCurCfgWlmIndex,
       "slbCurCfgWlmIpAddr": slbCurCfgWlmIpAddr,
       "slbCurCfgWlmPort": slbCurCfgWlmPort,
       "slbNewCfgWlmTable": slbNewCfgWlmTable,
       "slbNewCfgWlmEntry": slbNewCfgWlmEntry,
       "slbNewCfgWlmIndex": slbNewCfgWlmIndex,
       "slbNewCfgWlmIpAddr": slbNewCfgWlmIpAddr,
       "slbNewCfgWlmPort": slbNewCfgWlmPort,
       "slbNewCfgWlmDelete": slbNewCfgWlmDelete,
       "layer4Stats": layer4Stats,
       "slbSpStats": slbSpStats,
       "slbStatSpRealServerTable": slbStatSpRealServerTable,
       "slbStatSpRealServerEntry": slbStatSpRealServerEntry,
       "slbStatSpRealServerSpIndex": slbStatSpRealServerSpIndex,
       "slbStatSpRealServerServerIndex": slbStatSpRealServerServerIndex,
       "slbStatSpRealServerCurrSessions": slbStatSpRealServerCurrSessions,
       "slbStatSpRealServerTotalSessions": slbStatSpRealServerTotalSessions,
       "slbStatSpRealServerHCOctetsLow32": slbStatSpRealServerHCOctetsLow32,
       "slbStatSpRealServerHCOctetsHigh32": slbStatSpRealServerHCOctetsHigh32,
       "slbStatSpRealServerHCOctets": slbStatSpRealServerHCOctets,
       "slbStatSpFltTable": slbStatSpFltTable,
       "slbStatSpFltEntry": slbStatSpFltEntry,
       "slbStatSpFltSpIndex": slbStatSpFltSpIndex,
       "slbStatSpFltIndex": slbStatSpFltIndex,
       "slbStatSpFltFirings": slbStatSpFltFirings,
       "slbStatSpMaintTable": slbStatSpMaintTable,
       "slbStatSpMaintEntry": slbStatSpMaintEntry,
       "slbStatSpMaintSpIndex": slbStatSpMaintSpIndex,
       "slbStatSpMaintMaximumSessions": slbStatSpMaintMaximumSessions,
       "slbStatSpMaintCurBindings": slbStatSpMaintCurBindings,
       "slbStatSpMaintCurBindings4Seconds": slbStatSpMaintCurBindings4Seconds,
       "slbStatSpMaintCurBindings64Seconds": slbStatSpMaintCurBindings64Seconds,
       "slbStatSpMaintTerminatedSessions": slbStatSpMaintTerminatedSessions,
       "slbStatSpMaintBindingFails": slbStatSpMaintBindingFails,
       "slbStatSpMaintNonTcpFrames": slbStatSpMaintNonTcpFrames,
       "slbStatSpMaintTcpFragments": slbStatSpMaintTcpFragments,
       "slbStatSpMaintUdpDatagrams": slbStatSpMaintUdpDatagrams,
       "slbStatSpMaintIncorrectVIPs": slbStatSpMaintIncorrectVIPs,
       "slbStatSpMaintIncorrectVports": slbStatSpMaintIncorrectVports,
       "slbStatSpMaintRealServerNoAvails": slbStatSpMaintRealServerNoAvails,
       "slbStatSpMaintFilteredDeniedFrames": slbStatSpMaintFilteredDeniedFrames,
       "slbStatSpMaintLandAttacks": slbStatSpMaintLandAttacks,
       "slbStatSpMaintIpFragTotalSessions": slbStatSpMaintIpFragTotalSessions,
       "slbStatSpMaintIpFragCurSessions": slbStatSpMaintIpFragCurSessions,
       "slbStatSpMaintIpFragDiscards": slbStatSpMaintIpFragDiscards,
       "slbStatSpMaintIpFragTableFull": slbStatSpMaintIpFragTableFull,
       "slbStatSpMaintClear": slbStatSpMaintClear,
       "slbStatSpMaintOOSFinPktDrops": slbStatSpMaintOOSFinPktDrops,
       "slbStatSpMaintSymSessions": slbStatSpMaintSymSessions,
       "slbStatSpMaintSymValidSegments": slbStatSpMaintSymValidSegments,
       "slbStatSpMaintSymFragSessions": slbStatSpMaintSymFragSessions,
       "slbStatSpMaintSymSegAllocFails": slbStatSpMaintSymSegAllocFails,
       "slbStatSpMaintSymBufferAllocFails": slbStatSpMaintSymBufferAllocFails,
       "slbStatSpMaintSymConnAllocFails": slbStatSpMaintSymConnAllocFails,
       "slbStatSpMaintSymInvalidBuffers": slbStatSpMaintSymInvalidBuffers,
       "slbStatSpMaintSymSegReallocFails": slbStatSpMaintSymSegReallocFails,
       "slbStatSpMaintSymPacketsIn": slbStatSpMaintSymPacketsIn,
       "slbStatSpMaintSymPacketsWithNoData": slbStatSpMaintSymPacketsWithNoData,
       "slbStatSpMaintSymTcpPackets": slbStatSpMaintSymTcpPackets,
       "slbStatSpMaintSymUdpPackets": slbStatSpMaintSymUdpPackets,
       "slbStatSpMaintSymIcmpPackets": slbStatSpMaintSymIcmpPackets,
       "slbStatSpMaintSymOtherPackets": slbStatSpMaintSymOtherPackets,
       "slbStatSpMaintSymMatchCount": slbStatSpMaintSymMatchCount,
       "slbStatSpMaintSymFetchErrors": slbStatSpMaintSymFetchErrors,
       "slbStatSpMaintSymTruncPayloadToMp": slbStatSpMaintSymTruncPayloadToMp,
       "slbStatSpMaintSymPacketsInFastPath": slbStatSpMaintSymPacketsInFastPath,
       "slbStatSpAuxSessTable": slbStatSpAuxSessTable,
       "slbStatSpAuxSessEntry": slbStatSpAuxSessEntry,
       "slbStatSpAuxSessSpIndex": slbStatSpAuxSessSpIndex,
       "slbStatSpAuxSessIndex": slbStatSpAuxSessIndex,
       "slbStatSpAuxSessCurConn": slbStatSpAuxSessCurConn,
       "slbStatSpAuxSessMaxConn": slbStatSpAuxSessMaxConn,
       "slbStatSpAuxSessAllocFails": slbStatSpAuxSessAllocFails,
       "slbStatRServerTable": slbStatRServerTable,
       "slbStatRServerEntry": slbStatRServerEntry,
       "slbStatRServerIndex": slbStatRServerIndex,
       "slbStatRServerCurrSessions": slbStatRServerCurrSessions,
       "slbStatRServerTotalSessions": slbStatRServerTotalSessions,
       "slbStatRServerFailures": slbStatRServerFailures,
       "slbStatRServerHighestSessions": slbStatRServerHighestSessions,
       "slbStatRServerHCOctetsLow32": slbStatRServerHCOctetsLow32,
       "slbStatRServerHCOctetsHigh32": slbStatRServerHCOctetsHigh32,
       "slbStatRServerHCOctets": slbStatRServerHCOctets,
       "slbStatGroupTable": slbStatGroupTable,
       "slbStatGroupEntry": slbStatGroupEntry,
       "slbStatGroupIndex": slbStatGroupIndex,
       "slbStatGroupCurrSessions": slbStatGroupCurrSessions,
       "slbStatGroupTotalSessions": slbStatGroupTotalSessions,
       "slbStatGroupHighestSessions": slbStatGroupHighestSessions,
       "slbStatGroupHCOctetsLow32": slbStatGroupHCOctetsLow32,
       "slbStatGroupHCOctetsHigh32": slbStatGroupHCOctetsHigh32,
       "slbStatGroupHCOctets": slbStatGroupHCOctets,
       "slbStatGroupWlmUpdates": slbStatGroupWlmUpdates,
       "slbStatVServerTable": slbStatVServerTable,
       "slbStatVServerEntry": slbStatVServerEntry,
       "slbStatVServerIndex": slbStatVServerIndex,
       "slbStatVServerCurrSessions": slbStatVServerCurrSessions,
       "slbStatVServerTotalSessions": slbStatVServerTotalSessions,
       "slbStatVServerHighestSessions": slbStatVServerHighestSessions,
       "slbStatVServerHCOctetsLow32": slbStatVServerHCOctetsLow32,
       "slbStatVServerHCOctetsHigh32": slbStatVServerHCOctetsHigh32,
       "slbStatVServerHeaderHits": slbStatVServerHeaderHits,
       "slbStatVServerHeaderMisses": slbStatVServerHeaderMisses,
       "slbStatVServerHeaderTotalSessions": slbStatVServerHeaderTotalSessions,
       "slbStatVServerCookieRewrites": slbStatVServerCookieRewrites,
       "slbStatVServerCookieInserts": slbStatVServerCookieInserts,
       "slbStatVServerHCOctets": slbStatVServerHCOctets,
       "slbStatVServerIpAddress": slbStatVServerIpAddress,
       "slbMaintStats": slbMaintStats,
       "slbStatMaintMaximumSessions": slbStatMaintMaximumSessions,
       "slbStatMaintCurBindings": slbStatMaintCurBindings,
       "slbStatMaintCurBindings4Seconds": slbStatMaintCurBindings4Seconds,
       "slbStatMaintCurBindings64Seconds": slbStatMaintCurBindings64Seconds,
       "slbStatMaintTerminatedSessions": slbStatMaintTerminatedSessions,
       "slbStatMaintAllocFailures": slbStatMaintAllocFailures,
       "slbStatMaintNonTcpFrames": slbStatMaintNonTcpFrames,
       "slbStatMaintTcpFragments": slbStatMaintTcpFragments,
       "slbStatMaintUdpDatagrams": slbStatMaintUdpDatagrams,
       "slbIncorrectVirtServs": slbIncorrectVirtServs,
       "slbIncorrectVports": slbIncorrectVports,
       "slbNoRealServs": slbNoRealServs,
       "slbStatMaintBackupServActs": slbStatMaintBackupServActs,
       "slbStatMaintOverflowServActs": slbStatMaintOverflowServActs,
       "slbStatMaintFilteredDeniedFrames": slbStatMaintFilteredDeniedFrames,
       "slbStatMaintLandAttacks": slbStatMaintLandAttacks,
       "slbStatMaintIpFragTotalSessions": slbStatMaintIpFragTotalSessions,
       "slbStatMaintIpFragCurSessions": slbStatMaintIpFragCurSessions,
       "slbStatMaintIpFragDiscards": slbStatMaintIpFragDiscards,
       "slbStatMaintIpFragTableFull": slbStatMaintIpFragTableFull,
       "slbStatMaintIp6CurrSessions": slbStatMaintIp6CurrSessions,
       "slbIncorrectIp6Vip": slbIncorrectIp6Vip,
       "slbIncorrectIp6Vports": slbIncorrectIp6Vports,
       "slbStatMaintIp6PktDropped": slbStatMaintIp6PktDropped,
       "slbStatMaintOOSFinPktDrops": slbStatMaintOOSFinPktDrops,
       "slbStatMaintSymSessions": slbStatMaintSymSessions,
       "slbStatMaintSymValidSegments": slbStatMaintSymValidSegments,
       "slbStatMaintSymFragSessions": slbStatMaintSymFragSessions,
       "slbStatMaintSymSegAllocFails": slbStatMaintSymSegAllocFails,
       "slbStatMaintSymBufferAllocFails": slbStatMaintSymBufferAllocFails,
       "slbStatMaintSymConnAllocFails": slbStatMaintSymConnAllocFails,
       "slbStatMaintSymInvalidBuffers": slbStatMaintSymInvalidBuffers,
       "slbStatMaintSymSegReallocFails": slbStatMaintSymSegReallocFails,
       "slbStatMaintSymPacketsIn": slbStatMaintSymPacketsIn,
       "slbStatMaintSymPacketsWithNoData": slbStatMaintSymPacketsWithNoData,
       "slbStatMaintSymTcpPackets": slbStatMaintSymTcpPackets,
       "slbStatMaintSymUdpPackets": slbStatMaintSymUdpPackets,
       "slbStatMaintSymIcmpPackets": slbStatMaintSymIcmpPackets,
       "slbStatMaintSymOtherPackets": slbStatMaintSymOtherPackets,
       "slbStatMaintSymMatchCount": slbStatMaintSymMatchCount,
       "slbStatMaintSymFetchErrors": slbStatMaintSymFetchErrors,
       "slbStatMaintSymTruncPayloadToMp": slbStatMaintSymTruncPayloadToMp,
       "slbStatMaintSymPacketsInFastPath": slbStatMaintSymPacketsInFastPath,
       "filterStats": filterStats,
       "fltStatTable": fltStatTable,
       "fltStatTableEntry": fltStatTableEntry,
       "fltStatFltIndex": fltStatFltIndex,
       "fltStatFltFirings": fltStatFltFirings,
       "gslbStats": gslbStats,
       "gslbStatRemRealServerTable": gslbStatRemRealServerTable,
       "gslbStatRemRealServerEntry": gslbStatRemRealServerEntry,
       "gslbStatRemRealServerIndex": gslbStatRemRealServerIndex,
       "gslbStatRemRealServerDnsHandoffs": gslbStatRemRealServerDnsHandoffs,
       "gslbStatRemRealServerHttpRedirs": gslbStatRemRealServerHttpRedirs,
       "gslbMaintStats": gslbMaintStats,
       "gslbStatMaintInGoodSiteUpdates": gslbStatMaintInGoodSiteUpdates,
       "gslbStatMaintInBadSiteUpdates": gslbStatMaintInBadSiteUpdates,
       "gslbStatMaintOutSiteUpdates": gslbStatMaintOutSiteUpdates,
       "gslbStatMaintInGoodSiteUpdates2": gslbStatMaintInGoodSiteUpdates2,
       "gslbStatMaintOutSiteUpdates2": gslbStatMaintOutSiteUpdates2,
       "gslbStatMaintLocalSitePers": gslbStatMaintLocalSitePers,
       "gslbStatMaintInDns": gslbStatMaintInDns,
       "gslbStatMaintInBadDns": gslbStatMaintInBadDns,
       "gslbStatMaintOutDns": gslbStatMaintOutDns,
       "gslbStatMaintInHttp": gslbStatMaintInHttp,
       "gslbStatMaintInBadHttp": gslbStatMaintInBadHttp,
       "gslbStatMaintOutHttp": gslbStatMaintOutHttp,
       "gslbStatMaintNoServer": gslbStatMaintNoServer,
       "gslbStatMaintNoDomain": gslbStatMaintNoDomain,
       "gslbStatMaintHostHits": gslbStatMaintHostHits,
       "gslbStatMaintRuleHits": gslbStatMaintRuleHits,
       "gslbStatMaintVirtHits": gslbStatMaintVirtHits,
       "gslbStatMaintNoServerHost": gslbStatMaintNoServerHost,
       "gslbStatMaintNoServerRule": gslbStatMaintNoServerRule,
       "gslbStatMaintNoServerVirt": gslbStatMaintNoServerVirt,
       "gslbStatMaintLastNoResultDomain": gslbStatMaintLastNoResultDomain,
       "gslbStatMaintLastSrcIp": gslbStatMaintLastSrcIp,
       "gslbStatMaintThresholdHits": gslbStatMaintThresholdHits,
       "gslbStatGroupTable": gslbStatGroupTable,
       "gslbStatGroupEntry": gslbStatGroupEntry,
       "gslbStatGroupIndex": gslbStatGroupIndex,
       "gslbStatGroupDnsHandoffs": gslbStatGroupDnsHandoffs,
       "gslbStatGroupHttpRedirs": gslbStatGroupHttpRedirs,
       "gslbStatVirtServerTable": gslbStatVirtServerTable,
       "gslbStatVirtServerEntry": gslbStatVirtServerEntry,
       "gslbStatVirtServerIdx": gslbStatVirtServerIdx,
       "gslbStatVirtServerServiceIdx": gslbStatVirtServerServiceIdx,
       "gslbStatVirtServerRserverIdx": gslbStatVirtServerRserverIdx,
       "gslbStatVirtServerVirtPort": gslbStatVirtServerVirtPort,
       "gslbStatVirtServerIpAddress": gslbStatVirtServerIpAddress,
       "gslbStatVirtServerResponseTime": gslbStatVirtServerResponseTime,
       "gslbStatVirtServerMinSessAvail": gslbStatVirtServerMinSessAvail,
       "gslbStatVirtServerDname": gslbStatVirtServerDname,
       "gslbStatVirtServerRemSite": gslbStatVirtServerRemSite,
       "gslbStatVirtDnsDirect": gslbStatVirtDnsDirect,
       "gslbStatRemSiteTable": gslbStatRemSiteTable,
       "gslbStatRemSiteTableEntry": gslbStatRemSiteTableEntry,
       "gslbStatRemSiteIdx": gslbStatRemSiteIdx,
       "gslbStatRemSiteOutUpdates": gslbStatRemSiteOutUpdates,
       "gslbStatRemSiteInUpdates": gslbStatRemSiteInUpdates,
       "gslbStatRemSiteOutUpdates2": gslbStatRemSiteOutUpdates2,
       "gslbStatRemSiteInUpdates2": gslbStatRemSiteInUpdates2,
       "gslbStatRemSiteInBadUpdates": gslbStatRemSiteInBadUpdates,
       "gslbStatEnhNetworkTable": gslbStatEnhNetworkTable,
       "gslbStatEnhNetworkTableEntry": gslbStatEnhNetworkTableEntry,
       "gslbStatEnhNetworkIdx": gslbStatEnhNetworkIdx,
       "gslbStatEnhNetworkHit": gslbStatEnhNetworkHit,
       "gslbStatRuleTable": gslbStatRuleTable,
       "gslbStatRuleTableEntry": gslbStatRuleTableEntry,
       "gslbStatRuleIdx": gslbStatRuleIdx,
       "gslbStatRuleLeastconns": gslbStatRuleLeastconns,
       "gslbStatRuleRoundrobin": gslbStatRuleRoundrobin,
       "gslbStatRuleMinmisses": gslbStatRuleMinmisses,
       "gslbStatRuleHash": gslbStatRuleHash,
       "gslbStatRuleResponse": gslbStatRuleResponse,
       "gslbStatRuleGeographical": gslbStatRuleGeographical,
       "gslbStatRuleNetwork": gslbStatRuleNetwork,
       "gslbStatRuleRandom": gslbStatRuleRandom,
       "gslbStatRuleAvailability": gslbStatRuleAvailability,
       "gslbStatRuleQos": gslbStatRuleQos,
       "gslbStatRulePersistence": gslbStatRulePersistence,
       "gslbStatRuleLocal": gslbStatRuleLocal,
       "gslbStatRuleAlways": gslbStatRuleAlways,
       "gslbStatRuleRemote": gslbStatRuleRemote,
       "gslbStatRuleTotal": gslbStatRuleTotal,
       "gslbStatGeo": gslbStatGeo,
       "gslbStatGeoNA": gslbStatGeoNA,
       "gslbStatGeoSA": gslbStatGeoSA,
       "gslbStatGeoEU": gslbStatGeoEU,
       "gslbStatGeoCA": gslbStatGeoCA,
       "gslbStatGeoPR": gslbStatGeoPR,
       "gslbStatGeoSS": gslbStatGeoSS,
       "gslbStatGeoJP": gslbStatGeoJP,
       "gslbStatGeoTotal": gslbStatGeoTotal,
       "gslbStatGeoAF": gslbStatGeoAF,
       "gslbStatPers": gslbStatPers,
       "gslbStatPersCurrent": gslbStatPersCurrent,
       "gslbStatPersHiwat": gslbStatPersHiwat,
       "gslbStatPersMax": gslbStatPersMax,
       "wapStats": wapStats,
       "radiusAcctReqsStats": radiusAcctReqsStats,
       "radiusAcctReqs": radiusAcctReqs,
       "radiusAcctWrapReqs": radiusAcctWrapReqs,
       "radiusAcctStartReqs": radiusAcctStartReqs,
       "radiusAcctUpdateReqs": radiusAcctUpdateReqs,
       "radiusAcctStopReqs": radiusAcctStopReqs,
       "radiusAcctBadReqs": radiusAcctBadReqs,
       "radiusAcctAddSessionReqs": radiusAcctAddSessionReqs,
       "radiusAcctDeleteSessionReqs": radiusAcctDeleteSessionReqs,
       "radiusAcctReqFailsSPDead": radiusAcctReqFailsSPDead,
       "radiusAcctReqFailsDMAFails": radiusAcctReqFailsDMAFails,
       "radiusAcctReqWithFramedIp": radiusAcctReqWithFramedIp,
       "radiusAcctReqWithoutFramedIp": radiusAcctReqWithoutFramedIp,
       "tpcpAddSessReqsStats": tpcpAddSessReqsStats,
       "tpcpAddSessReqs": tpcpAddSessReqs,
       "tpcpAddSessReqsFailsSPDead": tpcpAddSessReqsFailsSPDead,
       "tpcpDeleteSessReqsStats": tpcpDeleteSessReqsStats,
       "tpcpDeleteSessReqs": tpcpDeleteSessReqs,
       "tpcpDeleteSessReqsFailsSPDead": tpcpDeleteSessReqsFailsSPDead,
       "wapRequestToWrongSP": wapRequestToWrongSP,
       "ftpStats": ftpStats,
       "ftpSlbStatTotal": ftpSlbStatTotal,
       "ftpNatStatTotal": ftpNatStatTotal,
       "ftpStatActiveNatIndex": ftpStatActiveNatIndex,
       "ftpStatNatAckSeqDiff": ftpStatNatAckSeqDiff,
       "ftpStatSlbParseIndex": ftpStatSlbParseIndex,
       "ftpStatSlbParseAckSeqDiff": ftpStatSlbParseAckSeqDiff,
       "ftpStatModeSwitchError": ftpStatModeSwitchError,
       "rtspStats": rtspStats,
       "rtspStatControlConns": rtspStatControlConns,
       "rtspStatUDPStreams": rtspStatUDPStreams,
       "rtspStatRedirects": rtspStatRedirects,
       "rtspStatConnDenied": rtspStatConnDenied,
       "rtspStatAllocFails": rtspStatAllocFails,
       "rtspStatBufferAllocs": rtspStatBufferAllocs,
       "tcpLimitStats": tcpLimitStats,
       "tcpLimitStatHoldDowns": tcpLimitStatHoldDowns,
       "tcpLimitStatClientEntries": tcpLimitStatClientEntries,
       "udpLimitStatHoldDowns": udpLimitStatHoldDowns,
       "icmpLimitStatHoldDowns": icmpLimitStatHoldDowns,
       "udpLimitStatClientEntries": udpLimitStatClientEntries,
       "icmpLimitStatClientEntries": icmpLimitStatClientEntries,
       "dnsSlbStats": dnsSlbStats,
       "dnsSlbStatTCPQueries": dnsSlbStatTCPQueries,
       "dnsSlbStatUDPQueries": dnsSlbStatUDPQueries,
       "dnsSlbStatInvalidQueries": dnsSlbStatInvalidQueries,
       "dnsSlbStatMultipleQueries": dnsSlbStatMultipleQueries,
       "dnsSlbStatDnameParseErrors": dnsSlbStatDnameParseErrors,
       "dnsSlbStatFailedMatches": dnsSlbStatFailedMatches,
       "dnsSlbStatInternalErrors": dnsSlbStatInternalErrors,
       "slbStatsClear": slbStatsClear,
       "sslSlbStats": sslSlbStats,
       "sslSlbStatSessIdAllocFails": sslSlbStatSessIdAllocFails,
       "sslSlbStatCurSessions": sslSlbStatCurSessions,
       "sslSlbStatTotalSessions": sslSlbStatTotalSessions,
       "sslSlbStatHighestSessions": sslSlbStatHighestSessions,
       "sslSlbStatUniqCurSessions": sslSlbStatUniqCurSessions,
       "sslSlbStatUniqTotalSessions": sslSlbStatUniqTotalSessions,
       "sslSlbStatUniqHighestSessions": sslSlbStatUniqHighestSessions,
       "sslSlbStatPersistPortCurSessions": sslSlbStatPersistPortCurSessions,
       "sslSlbStatPersistPortTotalSessions": sslSlbStatPersistPortTotalSessions,
       "sslSlbStatPersistPortHighestSessions": sslSlbStatPersistPortHighestSessions,
       "slbStatAuxSessTable": slbStatAuxSessTable,
       "slbStatAuxSessEntry": slbStatAuxSessEntry,
       "slbStatAuxSessIndex": slbStatAuxSessIndex,
       "slbStatAuxSessCurConn": slbStatAuxSessCurConn,
       "slbStatAuxSessMaxConn": slbStatAuxSessMaxConn,
       "slbStatAuxSessAllocFails": slbStatAuxSessAllocFails,
       "slbStatVirtServiceTable": slbStatVirtServiceTable,
       "slbStatVirtServiceEntry": slbStatVirtServiceEntry,
       "slbStatVirtServerIndex": slbStatVirtServerIndex,
       "slbStatVirtServiceIndex": slbStatVirtServiceIndex,
       "slbStatRealServerIndex": slbStatRealServerIndex,
       "slbStatVirtServiceCurrSessions": slbStatVirtServiceCurrSessions,
       "slbStatVirtServiceTotalSessions": slbStatVirtServiceTotalSessions,
       "slbStatVirtServiceHighestSessions": slbStatVirtServiceHighestSessions,
       "slbStatVirtServiceHCOctetsLow32": slbStatVirtServiceHCOctetsLow32,
       "slbStatVirtServiceHCOctetsHigh32": slbStatVirtServiceHCOctetsHigh32,
       "slbStatVirtServiceHCOctets": slbStatVirtServiceHCOctets,
       "sipStats": sipStats,
       "sipTotalClientParseErrors": sipTotalClientParseErrors,
       "sipTotalServerParseErrors": sipTotalServerParseErrors,
       "sipTotalUnknownMethodReq": sipTotalUnknownMethodReq,
       "sipTotalIncompleteMsgs": sipTotalIncompleteMsgs,
       "sipTotalSdpNatPackets": sipTotalSdpNatPackets,
       "wlmStats": wlmStats,
       "slbStatWlmTable": slbStatWlmTable,
       "slbStatWlmEntry": slbStatWlmEntry,
       "slbStatWlmIndex": slbStatWlmIndex,
       "slbStatWlmRegReq": slbStatWlmRegReq,
       "slbStatWlmRegRep": slbStatWlmRegRep,
       "slbStatWlmRegRepErr": slbStatWlmRegRepErr,
       "slbStatWlmDeregReq": slbStatWlmDeregReq,
       "slbStatWlmDeregRep": slbStatWlmDeregRep,
       "slbStatWlmDeregRepErr": slbStatWlmDeregRepErr,
       "slbStatWlmLbStateReq": slbStatWlmLbStateReq,
       "slbStatWlmLbStateRep": slbStatWlmLbStateRep,
       "slbStatWlmLbStateRepErr": slbStatWlmLbStateRepErr,
       "slbStatWlmMembStateReq": slbStatWlmMembStateReq,
       "slbStatWlmMembStateRep": slbStatWlmMembStateRep,
       "slbStatWlmMembStateRepErr": slbStatWlmMembStateRepErr,
       "slbStatWlmWtMsgRecv": slbStatWlmWtMsgRecv,
       "slbStatWlmWtMsgParErr": slbStatWlmWtMsgParErr,
       "slbStatWlmTotInvalidLb": slbStatWlmTotInvalidLb,
       "slbStatWlmTotInvalidGrp": slbStatWlmTotInvalidGrp,
       "slbStatWlmTotInvalidRealSer": slbStatWlmTotInvalidRealSer,
       "slbStatWlmMsgInvalidSASPHeader": slbStatWlmMsgInvalidSASPHeader,
       "slbStatWlmMsgParseErr": slbStatWlmMsgParseErr,
       "slbStatWlmMsgUnsupMsgType": slbStatWlmMsgUnsupMsgType,
       "sessMirrorStats": sessMirrorStats,
       "sessMirrorTotalCreateSessionMsgRx": sessMirrorTotalCreateSessionMsgRx,
       "sessMirrorTotalCreateSessionMsgTx": sessMirrorTotalCreateSessionMsgTx,
       "sessMirrorTotalCreateDataSessionMsgRx": sessMirrorTotalCreateDataSessionMsgRx,
       "sessMirrorTotalCreateDataSessionMsgTx": sessMirrorTotalCreateDataSessionMsgTx,
       "sessMirrorTotalUpdateSessionMsgRx": sessMirrorTotalUpdateSessionMsgRx,
       "sessMirrorTotalUpdateSessionMsgTx": sessMirrorTotalUpdateSessionMsgTx,
       "sessMirrorTotalUpdateDataSessionMsgRx": sessMirrorTotalUpdateDataSessionMsgRx,
       "sessMirrorTotalUpdateDataSessionMsgTx": sessMirrorTotalUpdateDataSessionMsgTx,
       "sessMirrorTotalDeleteSessionMsgRx": sessMirrorTotalDeleteSessionMsgRx,
       "sessMirrorTotalDeleteSessionMsgTx": sessMirrorTotalDeleteSessionMsgTx,
       "sessMirrorTotalDeleteDataSessionMsgRx": sessMirrorTotalDeleteDataSessionMsgRx,
       "sessMirrorTotalDeleteDataSessionMsgTx": sessMirrorTotalDeleteDataSessionMsgTx,
       "sessMirrorTotalSessionsCreated": sessMirrorTotalSessionsCreated,
       "sessMirrorTotalDataSessionsCreated": sessMirrorTotalDataSessionsCreated,
       "sessMirrorTotalSessionsUpdated": sessMirrorTotalSessionsUpdated,
       "sessMirrorTotalDataSessionsUpdated": sessMirrorTotalDataSessionsUpdated,
       "sessMirrorTotalSessionsDeleted": sessMirrorTotalSessionsDeleted,
       "sessMirrorTotalDataSessionsDeleted": sessMirrorTotalDataSessionsDeleted,
       "sessMirrorSessionTableFullErr": sessMirrorSessionTableFullErr,
       "sessMirrorNoPortErr": sessMirrorNoPortErr,
       "sessMirrorSessionPresentErr": sessMirrorSessionPresentErr,
       "sessMirrorSessionNotFoundErr": sessMirrorSessionNotFoundErr,
       "sessMirrorCtrlSessionNotFoundErr": sessMirrorCtrlSessionNotFoundErr,
       "layer4Info": layer4Info,
       "slbRealServerInfoTable": slbRealServerInfoTable,
       "slbRealServerInfoEntry": slbRealServerInfoEntry,
       "slbRealServerInfoIndex": slbRealServerInfoIndex,
       "slbRealServerInfoIpAddr": slbRealServerInfoIpAddr,
       "slbRealServerMacAddr": slbRealServerMacAddr,
       "slbRealServerInfoSwitchPort": slbRealServerInfoSwitchPort,
       "slbRealServerInfoHealthLayer": slbRealServerInfoHealthLayer,
       "slbRealServerInfoOverflow": slbRealServerInfoOverflow,
       "slbRealServerInfoState": slbRealServerInfoState,
       "slbRealServerInfoVlan": slbRealServerInfoVlan,
       "slbRealServerRportInfoTable": slbRealServerRportInfoTable,
       "slbRealServerRportInfoEntry": slbRealServerRportInfoEntry,
       "slbRealServerRportRealIndex": slbRealServerRportRealIndex,
       "slbRealServerRportServIndex": slbRealServerRportServIndex,
       "slbRealServerRportInfoRport": slbRealServerRportInfoRport,
       "slbRealServerRportInfoState": slbRealServerRportInfoState,
       "slbVirtServicesInfoTable": slbVirtServicesInfoTable,
       "slbVirtServicesInfoEntry": slbVirtServicesInfoEntry,
       "slbVirtServicesInfoVirtServIndex": slbVirtServicesInfoVirtServIndex,
       "slbVirtServicesInfoSvcIndex": slbVirtServicesInfoSvcIndex,
       "slbVirtServicesInfoRealServIndex": slbVirtServicesInfoRealServIndex,
       "slbVirtServicesInfoVport": slbVirtServicesInfoVport,
       "slbVirtServicesInfoRport": slbVirtServicesInfoRport,
       "slbVirtServicesInfoState": slbVirtServicesInfoState,
       "slbVirtServicesInfoResponseTime": slbVirtServicesInfoResponseTime,
       "slbVirtServicesInfoWeight": slbVirtServicesInfoWeight,
       "slbSessionInfo": slbSessionInfo,
       "slbSessionInfoState": slbSessionInfoState,
       "slbSessionInfoType": slbSessionInfoType,
       "slbSessionInfoIpAddr": slbSessionInfoIpAddr,
       "slbSessionInfoFilterId": slbSessionInfoFilterId,
       "slbSessionInfoPortId": slbSessionInfoPortId,
       "slbSessionInfoFlag": slbSessionInfoFlag,
       "slbSessionInfoStringFormatFlag": slbSessionInfoStringFormatFlag,
       "slbSessionInfoTable": slbSessionInfoTable,
       "slbSessionInfoEntry": slbSessionInfoEntry,
       "slbSessionInfoSpIndex": slbSessionInfoSpIndex,
       "slbSessionInfoIndex": slbSessionInfoIndex,
       "slbSessionInfoString": slbSessionInfoString,
       "slbSessionInfoMaxSessDump": slbSessionInfoMaxSessDump,
       "gslbInfo": gslbInfo,
       "gslbInfoRemRealServerTable": gslbInfoRemRealServerTable,
       "gslbInfoRemRealServerEntry": gslbInfoRemRealServerEntry,
       "gslbInfoRemRealServerIdx": gslbInfoRemRealServerIdx,
       "gslbInfoRemRealServerIpAddr": gslbInfoRemRealServerIpAddr,
       "gslbInfoRemRealServerName": gslbInfoRemRealServerName,
       "gslbInfoRemRealServerState": gslbInfoRemRealServerState,
       "gslbInfoVirtServerTable": gslbInfoVirtServerTable,
       "gslbInfoVirtServerEntry": gslbInfoVirtServerEntry,
       "gslbInfoVirtServerIdx": gslbInfoVirtServerIdx,
       "gslbInfoVirtServerServiceIdx": gslbInfoVirtServerServiceIdx,
       "gslbInfoVirtServerRserverIdx": gslbInfoVirtServerRserverIdx,
       "gslbInfoVirtServerDname": gslbInfoVirtServerDname,
       "gslbInfoVirtServerVirtPort": gslbInfoVirtServerVirtPort,
       "gslbInfoVirtServerIpAddress": gslbInfoVirtServerIpAddress,
       "gslbInfoVirtServerResponse": gslbInfoVirtServerResponse,
       "gslbInfoVirtServerSessAvail": gslbInfoVirtServerSessAvail,
       "gslbInfoVirtServerSessCur": gslbInfoVirtServerSessCur,
       "gslbInfoVirtServerSessMax": gslbInfoVirtServerSessMax,
       "gslbInfoVirtServerSessUtil": gslbInfoVirtServerSessUtil,
       "gslbInfoVirtServerCpuUtil": gslbInfoVirtServerCpuUtil,
       "gslbInfoVirtServerRemSite": gslbInfoVirtServerRemSite,
       "gslbInfoVirtServerWeight": gslbInfoVirtServerWeight,
       "gslbInfoVirtServerAvail": gslbInfoVirtServerAvail,
       "gslbInfoVirtServerRegion": gslbInfoVirtServerRegion,
       "gslbInfoRemSiteTable": gslbInfoRemSiteTable,
       "gslbInfoRemSiteEntry": gslbInfoRemSiteEntry,
       "gslbInfoRemSiteIdx": gslbInfoRemSiteIdx,
       "gslbInfoRemSitePrimaryIp": gslbInfoRemSitePrimaryIp,
       "gslbInfoRemSiteSecondaryIp": gslbInfoRemSiteSecondaryIp,
       "gslbInfoRemSiteName": gslbInfoRemSiteName,
       "gslbInfoRemSiteState": gslbInfoRemSiteState,
       "wlmInfo": wlmInfo,
       "slbWlmInfoTable": slbWlmInfoTable,
       "slbWlmInfoEntry": slbWlmInfoEntry,
       "slbWlmInfoIndex": slbWlmInfoIndex,
       "slbWlmInfoIpAddr": slbWlmInfoIpAddr,
       "slbWlmInfoPort": slbWlmInfoPort,
       "slbWlmInfoState": slbWlmInfoState,
       "slbPortInfo": slbPortInfo,
       "slbPortInfoTable": slbPortInfoTable,
       "slbPortInfoEntry": slbPortInfoEntry,
       "slbPortInfoIndex": slbPortInfoIndex,
       "slbPortClientState": slbPortClientState,
       "slbPortSerState": slbPortSerState,
       "slbPortFltState": slbPortFltState,
       "slbPortRTSState": slbPortRTSState,
       "slbPortHotStandbyState": slbPortHotStandbyState,
       "slbPortInterSWState": slbPortInterSWState,
       "slbPortProxyState": slbPortProxyState,
       "slbPortIdSlbState": slbPortIdSlbState,
       "slbPortSymantecState": slbPortSymantecState,
       "slbPortFitersAdded": slbPortFitersAdded,
       "synAttackInfo": synAttackInfo,
       "synAtkState": synAtkState,
       "synAtkInterval": synAtkInterval,
       "synAtkThreshhold": synAtkThreshhold,
       "synAtkWarningFired": synAtkWarningFired,
       "layer4Oper": layer4Oper,
       "slbOperRealServerTable": slbOperRealServerTable,
       "slbOperRealServerEntry": slbOperRealServerEntry,
       "slbOperRealServerIndex": slbOperRealServerIndex,
       "slbOperRealServerStatus": slbOperRealServerStatus,
       "slbOperClearSessionTable": slbOperClearSessionTable,
       "slbOperConfigSync": slbOperConfigSync,
       "gslbOper": gslbOper,
       "slbOperGroupRealServerTable": slbOperGroupRealServerTable,
       "slbOperGroupRealServerEntry": slbOperGroupRealServerEntry,
       "slbOperRealServGroupIndex": slbOperRealServGroupIndex,
       "slbOperGroupRealServIndex": slbOperGroupRealServIndex,
       "slbOperGroupRealServerState": slbOperGroupRealServerState}
)
