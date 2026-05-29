# SNMP MIB module (STORMSHIELD-MODEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-MODEL-MIB

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(stormshieldMIB,) = mibBuilder.importSymbols(
    "STORMSHIELD-SMI-MIB",
    "stormshieldMIB")


# MODULE-IDENTITY

snsModelName = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20)
)
if mibBuilder.loadTexts:
    snsModelName.setRevisions(
        ("2024-09-25 00:00",
         "2023-12-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SnsSN160_Type(DisplayString):
    """Custom type snsSN160 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN160_Type.__name__ = "DisplayString"
_SnsSN160_Object = MibScalar
snsSN160 = _SnsSN160_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 1),
    _SnsSN160_Type()
)
snsSN160.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN160.setStatus("current")


class _SnsSN160W_Type(DisplayString):
    """Custom type snsSN160W based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN160W_Type.__name__ = "DisplayString"
_SnsSN160W_Object = MibScalar
snsSN160W = _SnsSN160W_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 2),
    _SnsSN160W_Type()
)
snsSN160W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN160W.setStatus("current")


class _SnsSN210_Type(DisplayString):
    """Custom type snsSN210 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN210_Type.__name__ = "DisplayString"
_SnsSN210_Object = MibScalar
snsSN210 = _SnsSN210_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 3),
    _SnsSN210_Type()
)
snsSN210.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN210.setStatus("current")


class _SnsSN210W_Type(DisplayString):
    """Custom type snsSN210W based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN210W_Type.__name__ = "DisplayString"
_SnsSN210W_Object = MibScalar
snsSN210W = _SnsSN210W_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 4),
    _SnsSN210W_Type()
)
snsSN210W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN210W.setStatus("current")


class _SnsSN_S_Series_220_Type(DisplayString):
    """Custom type snsSN_S_Series_220 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN_S_Series_220_Type.__name__ = "DisplayString"
_SnsSN_S_Series_220_Object = MibScalar
snsSN_S_Series_220 = _SnsSN_S_Series_220_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 5),
    _SnsSN_S_Series_220_Type()
)
snsSN_S_Series_220.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN_S_Series_220.setStatus("current")


class _SnsSN310_Type(DisplayString):
    """Custom type snsSN310 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN310_Type.__name__ = "DisplayString"
_SnsSN310_Object = MibScalar
snsSN310 = _SnsSN310_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 6),
    _SnsSN310_Type()
)
snsSN310.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN310.setStatus("current")


class _SnsSN_S_Series_320_Type(DisplayString):
    """Custom type snsSN_S_Series_320 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN_S_Series_320_Type.__name__ = "DisplayString"
_SnsSN_S_Series_320_Object = MibScalar
snsSN_S_Series_320 = _SnsSN_S_Series_320_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 7),
    _SnsSN_S_Series_320_Type()
)
snsSN_S_Series_320.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN_S_Series_320.setStatus("current")


class _SnsSN510_Type(DisplayString):
    """Custom type snsSN510 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN510_Type.__name__ = "DisplayString"
_SnsSN510_Object = MibScalar
snsSN510 = _SnsSN510_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 8),
    _SnsSN510_Type()
)
snsSN510.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN510.setStatus("current")


class _SnsSN520_Type(DisplayString):
    """Custom type snsSN520 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN520_Type.__name__ = "DisplayString"
_SnsSN520_Object = MibScalar
snsSN520 = _SnsSN520_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 9),
    _SnsSN520_Type()
)
snsSN520.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN520.setStatus("current")


class _SnsSN710_Type(DisplayString):
    """Custom type snsSN710 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN710_Type.__name__ = "DisplayString"
_SnsSN710_Object = MibScalar
snsSN710 = _SnsSN710_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 10),
    _SnsSN710_Type()
)
snsSN710.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN710.setStatus("current")


class _SnsSN_M_Series_720_Type(DisplayString):
    """Custom type snsSN_M_Series_720 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN_M_Series_720_Type.__name__ = "DisplayString"
_SnsSN_M_Series_720_Object = MibScalar
snsSN_M_Series_720 = _SnsSN_M_Series_720_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 11),
    _SnsSN_M_Series_720_Type()
)
snsSN_M_Series_720.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN_M_Series_720.setStatus("current")


class _SnsSNi20_Type(DisplayString):
    """Custom type snsSNi20 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSNi20_Type.__name__ = "DisplayString"
_SnsSNi20_Object = MibScalar
snsSNi20 = _SnsSNi20_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 12),
    _SnsSNi20_Type()
)
snsSNi20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSNi20.setStatus("current")


class _SnsSNi40_Type(DisplayString):
    """Custom type snsSNi40 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSNi40_Type.__name__ = "DisplayString"
_SnsSNi40_Object = MibScalar
snsSNi40 = _SnsSNi40_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 13),
    _SnsSNi40_Type()
)
snsSNi40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSNi40.setStatus("current")


class _SnsSNxr1200_Type(DisplayString):
    """Custom type snsSNxr1200 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSNxr1200_Type.__name__ = "DisplayString"
_SnsSNxr1200_Object = MibScalar
snsSNxr1200 = _SnsSNxr1200_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 14),
    _SnsSNxr1200_Type()
)
snsSNxr1200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSNxr1200.setStatus("current")


class _SnsSN910_Type(DisplayString):
    """Custom type snsSN910 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN910_Type.__name__ = "DisplayString"
_SnsSN910_Object = MibScalar
snsSN910 = _SnsSN910_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 15),
    _SnsSN910_Type()
)
snsSN910.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN910.setStatus("current")


class _SnsSN_M_Series_920_Type(DisplayString):
    """Custom type snsSN_M_Series_920 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN_M_Series_920_Type.__name__ = "DisplayString"
_SnsSN_M_Series_920_Object = MibScalar
snsSN_M_Series_920 = _SnsSN_M_Series_920_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 16),
    _SnsSN_M_Series_920_Type()
)
snsSN_M_Series_920.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN_M_Series_920.setStatus("current")


class _SnsSN1100_Type(DisplayString):
    """Custom type snsSN1100 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN1100_Type.__name__ = "DisplayString"
_SnsSN1100_Object = MibScalar
snsSN1100 = _SnsSN1100_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 17),
    _SnsSN1100_Type()
)
snsSN1100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN1100.setStatus("current")


class _SnsSN2000_Type(DisplayString):
    """Custom type snsSN2000 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN2000_Type.__name__ = "DisplayString"
_SnsSN2000_Object = MibScalar
snsSN2000 = _SnsSN2000_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 18),
    _SnsSN2000_Type()
)
snsSN2000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN2000.setStatus("current")


class _SnsSN2100_Type(DisplayString):
    """Custom type snsSN2100 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN2100_Type.__name__ = "DisplayString"
_SnsSN2100_Object = MibScalar
snsSN2100 = _SnsSN2100_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 19),
    _SnsSN2100_Type()
)
snsSN2100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN2100.setStatus("current")


class _SnsSN3000_Type(DisplayString):
    """Custom type snsSN3000 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN3000_Type.__name__ = "DisplayString"
_SnsSN3000_Object = MibScalar
snsSN3000 = _SnsSN3000_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 20),
    _SnsSN3000_Type()
)
snsSN3000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN3000.setStatus("current")


class _SnsSN3100_Type(DisplayString):
    """Custom type snsSN3100 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN3100_Type.__name__ = "DisplayString"
_SnsSN3100_Object = MibScalar
snsSN3100 = _SnsSN3100_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 21),
    _SnsSN3100_Type()
)
snsSN3100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN3100.setStatus("current")


class _SnsSN6000_Type(DisplayString):
    """Custom type snsSN6000 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN6000_Type.__name__ = "DisplayString"
_SnsSN6000_Object = MibScalar
snsSN6000 = _SnsSN6000_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 22),
    _SnsSN6000_Type()
)
snsSN6000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN6000.setStatus("current")


class _SnsSN6100_Type(DisplayString):
    """Custom type snsSN6100 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN6100_Type.__name__ = "DisplayString"
_SnsSN6100_Object = MibScalar
snsSN6100 = _SnsSN6100_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 23),
    _SnsSN6100_Type()
)
snsSN6100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN6100.setStatus("current")


class _SnsEVA1_Type(DisplayString):
    """Custom type snsEVA1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsEVA1_Type.__name__ = "DisplayString"
_SnsEVA1_Object = MibScalar
snsEVA1 = _SnsEVA1_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 24),
    _SnsEVA1_Type()
)
snsEVA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsEVA1.setStatus("current")


class _SnsEVA2_Type(DisplayString):
    """Custom type snsEVA2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsEVA2_Type.__name__ = "DisplayString"
_SnsEVA2_Object = MibScalar
snsEVA2 = _SnsEVA2_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 25),
    _SnsEVA2_Type()
)
snsEVA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsEVA2.setStatus("current")


class _SnsEVA3_Type(DisplayString):
    """Custom type snsEVA3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsEVA3_Type.__name__ = "DisplayString"
_SnsEVA3_Object = MibScalar
snsEVA3 = _SnsEVA3_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 26),
    _SnsEVA3_Type()
)
snsEVA3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsEVA3.setStatus("current")


class _SnsEVA4_Type(DisplayString):
    """Custom type snsEVA4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsEVA4_Type.__name__ = "DisplayString"
_SnsEVA4_Object = MibScalar
snsEVA4 = _SnsEVA4_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 27),
    _SnsEVA4_Type()
)
snsEVA4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsEVA4.setStatus("current")


class _SnsEVAU_Type(DisplayString):
    """Custom type snsEVAU based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsEVAU_Type.__name__ = "DisplayString"
_SnsEVAU_Object = MibScalar
snsEVAU = _SnsEVAU_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 28),
    _SnsEVAU_Type()
)
snsEVAU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsEVAU.setStatus("current")


class _SnsVPAYG_Type(DisplayString):
    """Custom type snsVPAYG based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsVPAYG_Type.__name__ = "DisplayString"
_SnsVPAYG_Object = MibScalar
snsVPAYG = _SnsVPAYG_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 29),
    _SnsVPAYG_Type()
)
snsVPAYG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPAYG.setStatus("current")


class _SnsSNi10_Type(DisplayString):
    """Custom type snsSNi10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSNi10_Type.__name__ = "DisplayString"
_SnsSNi10_Object = MibScalar
snsSNi10 = _SnsSNi10_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 30),
    _SnsSNi10_Type()
)
snsSNi10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSNi10.setStatus("current")


class _SnsSN_XS_Series_170_Type(DisplayString):
    """Custom type snsSN_XS_Series_170 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN_XS_Series_170_Type.__name__ = "DisplayString"
_SnsSN_XS_Series_170_Object = MibScalar
snsSN_XS_Series_170 = _SnsSN_XS_Series_170_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 31),
    _SnsSN_XS_Series_170_Type()
)
snsSN_XS_Series_170.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN_XS_Series_170.setStatus("current")


class _SnsSN_L_Series_2200_Type(DisplayString):
    """Custom type snsSN_L_Series_2200 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN_L_Series_2200_Type.__name__ = "DisplayString"
_SnsSN_L_Series_2200_Object = MibScalar
snsSN_L_Series_2200 = _SnsSN_L_Series_2200_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 32),
    _SnsSN_L_Series_2200_Type()
)
snsSN_L_Series_2200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN_L_Series_2200.setStatus("current")


class _SnsSN_L_Series_3200_Type(DisplayString):
    """Custom type snsSN_L_Series_3200 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN_L_Series_3200_Type.__name__ = "DisplayString"
_SnsSN_L_Series_3200_Object = MibScalar
snsSN_L_Series_3200 = _SnsSN_L_Series_3200_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 33),
    _SnsSN_L_Series_3200_Type()
)
snsSN_L_Series_3200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN_L_Series_3200.setStatus("current")


class _SnsSN_XL_Series_5200_Type(DisplayString):
    """Custom type snsSN_XL_Series_5200 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN_XL_Series_5200_Type.__name__ = "DisplayString"
_SnsSN_XL_Series_5200_Object = MibScalar
snsSN_XL_Series_5200 = _SnsSN_XL_Series_5200_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 34),
    _SnsSN_XL_Series_5200_Type()
)
snsSN_XL_Series_5200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN_XL_Series_5200.setStatus("current")


class _SnsSN_XL_Series_6200_Type(DisplayString):
    """Custom type snsSN_XL_Series_6200 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsSN_XL_Series_6200_Type.__name__ = "DisplayString"
_SnsSN_XL_Series_6200_Object = MibScalar
snsSN_XL_Series_6200 = _SnsSN_XL_Series_6200_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 20, 35),
    _SnsSN_XL_Series_6200_Type()
)
snsSN_XL_Series_6200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsSN_XL_Series_6200.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-MODEL-MIB",
    **{"snsModelName": snsModelName,
       "snsSN160": snsSN160,
       "snsSN160W": snsSN160W,
       "snsSN210": snsSN210,
       "snsSN210W": snsSN210W,
       "snsSN-S-Series-220": snsSN_S_Series_220,
       "snsSN310": snsSN310,
       "snsSN-S-Series-320": snsSN_S_Series_320,
       "snsSN510": snsSN510,
       "snsSN520": snsSN520,
       "snsSN710": snsSN710,
       "snsSN-M-Series-720": snsSN_M_Series_720,
       "snsSNi20": snsSNi20,
       "snsSNi40": snsSNi40,
       "snsSNxr1200": snsSNxr1200,
       "snsSN910": snsSN910,
       "snsSN-M-Series-920": snsSN_M_Series_920,
       "snsSN1100": snsSN1100,
       "snsSN2000": snsSN2000,
       "snsSN2100": snsSN2100,
       "snsSN3000": snsSN3000,
       "snsSN3100": snsSN3100,
       "snsSN6000": snsSN6000,
       "snsSN6100": snsSN6100,
       "snsEVA1": snsEVA1,
       "snsEVA2": snsEVA2,
       "snsEVA3": snsEVA3,
       "snsEVA4": snsEVA4,
       "snsEVAU": snsEVAU,
       "snsVPAYG": snsVPAYG,
       "snsSNi10": snsSNi10,
       "snsSN-XS-Series-170": snsSN_XS_Series_170,
       "snsSN-L-Series-2200": snsSN_L_Series_2200,
       "snsSN-L-Series-3200": snsSN_L_Series_3200,
       "snsSN-XL-Series-5200": snsSN_XL_Series_5200,
       "snsSN-XL-Series-6200": snsSN_XL_Series_6200}
)
