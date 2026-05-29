# SNMP MIB module (PRVT-CR-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-CR-LDP-MIB

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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(ipSwitch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "ipSwitch")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtCrLdp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3)
)
if mibBuilder.loadTexts:
    prvtCrLdp.setRevisions(
        ("2008-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrvtCrldpAdminStatus(TextualConvention, Integer32):
    status = "current"
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



class PrvtCrldpOperStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("up", 1),
          ("down", 2),
          ("goingUp", 3),
          ("goingDown", 4),
          ("actFailed", 5))
    )



class PrvtCrldpIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_Mpls_ObjectIdentity = ObjectIdentity
mpls = _Mpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5)
)
_PrvtCrLdpObjects_ObjectIdentity = ObjectIdentity
prvtCrLdpObjects = _PrvtCrLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1)
)
_PrvtcrldpSigTable_Object = MibTable
prvtcrldpSigTable = _PrvtcrldpSigTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    prvtcrldpSigTable.setStatus("current")
_PrvtcrldpSigEntry_Object = MibTableRow
prvtcrldpSigEntry = _PrvtcrldpSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1)
)
prvtcrldpSigEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpSigIndex"),
)
if mibBuilder.loadTexts:
    prvtcrldpSigEntry.setStatus("current")
_PrvtcrldpSigIndex_Type = PrvtCrldpIndex
_PrvtcrldpSigIndex_Object = MibTableColumn
prvtcrldpSigIndex = _PrvtcrldpSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 1),
    _PrvtcrldpSigIndex_Type()
)
prvtcrldpSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtcrldpSigIndex.setStatus("current")
_PrvtcrldpSigPathManagerIndex_Type = PrvtCrldpIndex
_PrvtcrldpSigPathManagerIndex_Object = MibTableColumn
prvtcrldpSigPathManagerIndex = _PrvtcrldpSigPathManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 2),
    _PrvtcrldpSigPathManagerIndex_Type()
)
prvtcrldpSigPathManagerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpSigPathManagerIndex.setStatus("current")
_PrvtcrldpSigLsrIndex_Type = Unsigned32
_PrvtcrldpSigLsrIndex_Object = MibTableColumn
prvtcrldpSigLsrIndex = _PrvtcrldpSigLsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 3),
    _PrvtcrldpSigLsrIndex_Type()
)
prvtcrldpSigLsrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpSigLsrIndex.setStatus("current")
_PrvtcrldpSigSocketIfIndex_Type = InterfaceIndexOrZero
_PrvtcrldpSigSocketIfIndex_Object = MibTableColumn
prvtcrldpSigSocketIfIndex = _PrvtcrldpSigSocketIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 4),
    _PrvtcrldpSigSocketIfIndex_Type()
)
prvtcrldpSigSocketIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpSigSocketIfIndex.setStatus("current")


class _PrvtcrldpSigSessionBufPoolSize_Type(Integer32):
    """Custom type prvtcrldpSigSessionBufPoolSize based on Integer32"""
    defaultValue = 8


_PrvtcrldpSigSessionBufPoolSize_Type.__name__ = "Integer32"
_PrvtcrldpSigSessionBufPoolSize_Object = MibTableColumn
prvtcrldpSigSessionBufPoolSize = _PrvtcrldpSigSessionBufPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 5),
    _PrvtcrldpSigSessionBufPoolSize_Type()
)
prvtcrldpSigSessionBufPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpSigSessionBufPoolSize.setStatus("current")


class _PrvtcrldpSigEMBufPoolSize_Type(Integer32):
    """Custom type prvtcrldpSigEMBufPoolSize based on Integer32"""
    defaultValue = 8


_PrvtcrldpSigEMBufPoolSize_Type.__name__ = "Integer32"
_PrvtcrldpSigEMBufPoolSize_Object = MibTableColumn
prvtcrldpSigEMBufPoolSize = _PrvtcrldpSigEMBufPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 6),
    _PrvtcrldpSigEMBufPoolSize_Type()
)
prvtcrldpSigEMBufPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpSigEMBufPoolSize.setStatus("current")


class _PrvtcrldpSigAMBufPoolSize_Type(Integer32):
    """Custom type prvtcrldpSigAMBufPoolSize based on Integer32"""
    defaultValue = 8


_PrvtcrldpSigAMBufPoolSize_Type.__name__ = "Integer32"
_PrvtcrldpSigAMBufPoolSize_Object = MibTableColumn
prvtcrldpSigAMBufPoolSize = _PrvtcrldpSigAMBufPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 7),
    _PrvtcrldpSigAMBufPoolSize_Type()
)
prvtcrldpSigAMBufPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpSigAMBufPoolSize.setStatus("current")


class _PrvtcrldpSigAdminStatus_Type(PrvtCrldpAdminStatus):
    """Custom type prvtcrldpSigAdminStatus based on PrvtCrldpAdminStatus"""
    defaultValue = 1


_PrvtcrldpSigAdminStatus_Type.__name__ = "PrvtCrldpAdminStatus"
_PrvtcrldpSigAdminStatus_Object = MibTableColumn
prvtcrldpSigAdminStatus = _PrvtcrldpSigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 8),
    _PrvtcrldpSigAdminStatus_Type()
)
prvtcrldpSigAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpSigAdminStatus.setStatus("current")
_PrvtcrldpSigOperStatus_Type = PrvtCrldpOperStatus
_PrvtcrldpSigOperStatus_Object = MibTableColumn
prvtcrldpSigOperStatus = _PrvtcrldpSigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 9),
    _PrvtcrldpSigOperStatus_Type()
)
prvtcrldpSigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtcrldpSigOperStatus.setStatus("current")
_PrvtcrldpSigRowStatus_Type = RowStatus
_PrvtcrldpSigRowStatus_Object = MibTableColumn
prvtcrldpSigRowStatus = _PrvtcrldpSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 10),
    _PrvtcrldpSigRowStatus_Type()
)
prvtcrldpSigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpSigRowStatus.setStatus("current")


class _PrvtcrldpSigUseI3Interface_Type(TruthValue):
    """Custom type prvtcrldpSigUseI3Interface based on TruthValue"""
    defaultValue = 2


_PrvtcrldpSigUseI3Interface_Type.__name__ = "TruthValue"
_PrvtcrldpSigUseI3Interface_Object = MibTableColumn
prvtcrldpSigUseI3Interface = _PrvtcrldpSigUseI3Interface_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 11),
    _PrvtcrldpSigUseI3Interface_Type()
)
prvtcrldpSigUseI3Interface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpSigUseI3Interface.setStatus("current")


class _PrvtcrldpSigConformanceFlags_Type(Bits):
    """Custom type prvtcrldpSigConformanceFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("maxPduLen", 0)
    )

_PrvtcrldpSigConformanceFlags_Type.__name__ = "Bits"
_PrvtcrldpSigConformanceFlags_Object = MibTableColumn
prvtcrldpSigConformanceFlags = _PrvtcrldpSigConformanceFlags_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 12),
    _PrvtcrldpSigConformanceFlags_Type()
)
prvtcrldpSigConformanceFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpSigConformanceFlags.setStatus("current")


class _PrvtcrldpSigUseIPv6Transport_Type(TruthValue):
    """Custom type prvtcrldpSigUseIPv6Transport based on TruthValue"""
    defaultValue = 2


_PrvtcrldpSigUseIPv6Transport_Type.__name__ = "TruthValue"
_PrvtcrldpSigUseIPv6Transport_Object = MibTableColumn
prvtcrldpSigUseIPv6Transport = _PrvtcrldpSigUseIPv6Transport_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 13),
    _PrvtcrldpSigUseIPv6Transport_Type()
)
prvtcrldpSigUseIPv6Transport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpSigUseIPv6Transport.setStatus("current")


class _PrvtcrldpSigSessStatusTrapEnable_Type(TruthValue):
    """Custom type prvtcrldpSigSessStatusTrapEnable based on TruthValue"""
    defaultValue = 2


_PrvtcrldpSigSessStatusTrapEnable_Type.__name__ = "TruthValue"
_PrvtcrldpSigSessStatusTrapEnable_Object = MibTableColumn
prvtcrldpSigSessStatusTrapEnable = _PrvtcrldpSigSessStatusTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 14),
    _PrvtcrldpSigSessStatusTrapEnable_Type()
)
prvtcrldpSigSessStatusTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpSigSessStatusTrapEnable.setStatus("current")


class _PrvtcrldpSigSessThreshTrapEnable_Type(TruthValue):
    """Custom type prvtcrldpSigSessThreshTrapEnable based on TruthValue"""
    defaultValue = 2


_PrvtcrldpSigSessThreshTrapEnable_Type.__name__ = "TruthValue"
_PrvtcrldpSigSessThreshTrapEnable_Object = MibTableColumn
prvtcrldpSigSessThreshTrapEnable = _PrvtcrldpSigSessThreshTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 15),
    _PrvtcrldpSigSessThreshTrapEnable_Type()
)
prvtcrldpSigSessThreshTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpSigSessThreshTrapEnable.setStatus("current")


class _PrvtcrldpSigPathVecLimitTrapEnable_Type(TruthValue):
    """Custom type prvtcrldpSigPathVecLimitTrapEnable based on TruthValue"""
    defaultValue = 2


_PrvtcrldpSigPathVecLimitTrapEnable_Type.__name__ = "TruthValue"
_PrvtcrldpSigPathVecLimitTrapEnable_Object = MibTableColumn
prvtcrldpSigPathVecLimitTrapEnable = _PrvtcrldpSigPathVecLimitTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 1, 1, 16),
    _PrvtcrldpSigPathVecLimitTrapEnable_Type()
)
prvtcrldpSigPathVecLimitTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpSigPathVecLimitTrapEnable.setStatus("current")
_PrvtcrldpPmTable_Object = MibTable
prvtcrldpPmTable = _PrvtcrldpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2)
)
if mibBuilder.loadTexts:
    prvtcrldpPmTable.setStatus("current")
_PrvtcrldpPmEntry_Object = MibTableRow
prvtcrldpPmEntry = _PrvtcrldpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1)
)
prvtcrldpPmEntry.setIndexNames(
    (0, "PRVT-CR-LDP-MIB", "prvtcrldpPmIndex"),
)
if mibBuilder.loadTexts:
    prvtcrldpPmEntry.setStatus("current")
_PrvtcrldpPmIndex_Type = PrvtCrldpIndex
_PrvtcrldpPmIndex_Object = MibTableColumn
prvtcrldpPmIndex = _PrvtcrldpPmIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 1),
    _PrvtcrldpPmIndex_Type()
)
prvtcrldpPmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtcrldpPmIndex.setStatus("current")
_PrvtcrldpPmLsrIndex_Type = Unsigned32
_PrvtcrldpPmLsrIndex_Object = MibTableColumn
prvtcrldpPmLsrIndex = _PrvtcrldpPmLsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 2),
    _PrvtcrldpPmLsrIndex_Type()
)
prvtcrldpPmLsrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmLsrIndex.setStatus("current")


class _PrvtcrldpPmLdpEntityAutoCreate_Type(TruthValue):
    """Custom type prvtcrldpPmLdpEntityAutoCreate based on TruthValue"""
    defaultValue = 1


_PrvtcrldpPmLdpEntityAutoCreate_Type.__name__ = "TruthValue"
_PrvtcrldpPmLdpEntityAutoCreate_Object = MibTableColumn
prvtcrldpPmLdpEntityAutoCreate = _PrvtcrldpPmLdpEntityAutoCreate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 3),
    _PrvtcrldpPmLdpEntityAutoCreate_Type()
)
prvtcrldpPmLdpEntityAutoCreate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmLdpEntityAutoCreate.setStatus("current")


class _PrvtcrldpPmLdpEntityAutoStart_Type(TruthValue):
    """Custom type prvtcrldpPmLdpEntityAutoStart based on TruthValue"""
    defaultValue = 1


_PrvtcrldpPmLdpEntityAutoStart_Type.__name__ = "TruthValue"
_PrvtcrldpPmLdpEntityAutoStart_Object = MibTableColumn
prvtcrldpPmLdpEntityAutoStart = _PrvtcrldpPmLdpEntityAutoStart_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 4),
    _PrvtcrldpPmLdpEntityAutoStart_Type()
)
prvtcrldpPmLdpEntityAutoStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmLdpEntityAutoStart.setStatus("current")


class _PrvtcrldpPmLdpEntityReuse_Type(TruthValue):
    """Custom type prvtcrldpPmLdpEntityReuse based on TruthValue"""
    defaultValue = 1


_PrvtcrldpPmLdpEntityReuse_Type.__name__ = "TruthValue"
_PrvtcrldpPmLdpEntityReuse_Object = MibTableColumn
prvtcrldpPmLdpEntityReuse = _PrvtcrldpPmLdpEntityReuse_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 5),
    _PrvtcrldpPmLdpEntityReuse_Type()
)
prvtcrldpPmLdpEntityReuse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmLdpEntityReuse.setStatus("current")


class _PrvtcrldpPmLdpVersion_Type(Integer32):
    """Custom type prvtcrldpPmLdpVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version1", 1)
    )


_PrvtcrldpPmLdpVersion_Type.__name__ = "Integer32"
_PrvtcrldpPmLdpVersion_Object = MibTableColumn
prvtcrldpPmLdpVersion = _PrvtcrldpPmLdpVersion_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 6),
    _PrvtcrldpPmLdpVersion_Type()
)
prvtcrldpPmLdpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmLdpVersion.setStatus("current")


class _PrvtcrldpPmUseLdpFt_Type(TruthValue):
    """Custom type prvtcrldpPmUseLdpFt based on TruthValue"""
    defaultValue = 2


_PrvtcrldpPmUseLdpFt_Type.__name__ = "TruthValue"
_PrvtcrldpPmUseLdpFt_Object = MibTableColumn
prvtcrldpPmUseLdpFt = _PrvtcrldpPmUseLdpFt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 7),
    _PrvtcrldpPmUseLdpFt_Type()
)
prvtcrldpPmUseLdpFt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmUseLdpFt.setStatus("current")


class _PrvtcrldpPmAsNumber_Type(Integer32):
    """Custom type prvtcrldpPmAsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtcrldpPmAsNumber_Type.__name__ = "Integer32"
_PrvtcrldpPmAsNumber_Object = MibTableColumn
prvtcrldpPmAsNumber = _PrvtcrldpPmAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 8),
    _PrvtcrldpPmAsNumber_Type()
)
prvtcrldpPmAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmAsNumber.setStatus("current")


class _PrvtcrldpPmIprBufPoolSize_Type(Integer32):
    """Custom type prvtcrldpPmIprBufPoolSize based on Integer32"""
    defaultValue = 8


_PrvtcrldpPmIprBufPoolSize_Type.__name__ = "Integer32"
_PrvtcrldpPmIprBufPoolSize_Object = MibTableColumn
prvtcrldpPmIprBufPoolSize = _PrvtcrldpPmIprBufPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 9),
    _PrvtcrldpPmIprBufPoolSize_Type()
)
prvtcrldpPmIprBufPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmIprBufPoolSize.setStatus("current")


class _PrvtcrldpPmLdpSupported_Type(TruthValue):
    """Custom type prvtcrldpPmLdpSupported based on TruthValue"""
    defaultValue = 2


_PrvtcrldpPmLdpSupported_Type.__name__ = "TruthValue"
_PrvtcrldpPmLdpSupported_Object = MibTableColumn
prvtcrldpPmLdpSupported = _PrvtcrldpPmLdpSupported_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 10),
    _PrvtcrldpPmLdpSupported_Type()
)
prvtcrldpPmLdpSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmLdpSupported.setStatus("current")


class _PrvtcrldpPmCrLdpSupported_Type(TruthValue):
    """Custom type prvtcrldpPmCrLdpSupported based on TruthValue"""
    defaultValue = 2


_PrvtcrldpPmCrLdpSupported_Type.__name__ = "TruthValue"
_PrvtcrldpPmCrLdpSupported_Object = MibTableColumn
prvtcrldpPmCrLdpSupported = _PrvtcrldpPmCrLdpSupported_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 11),
    _PrvtcrldpPmCrLdpSupported_Type()
)
prvtcrldpPmCrLdpSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmCrLdpSupported.setStatus("current")


class _PrvtcrldpPmQueryFECSupported_Type(TruthValue):
    """Custom type prvtcrldpPmQueryFECSupported based on TruthValue"""
    defaultValue = 2


_PrvtcrldpPmQueryFECSupported_Type.__name__ = "TruthValue"
_PrvtcrldpPmQueryFECSupported_Object = MibTableColumn
prvtcrldpPmQueryFECSupported = _PrvtcrldpPmQueryFECSupported_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 12),
    _PrvtcrldpPmQueryFECSupported_Type()
)
prvtcrldpPmQueryFECSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmQueryFECSupported.setStatus("current")


class _PrvtcrldpPmAdminStatus_Type(PrvtCrldpAdminStatus):
    """Custom type prvtcrldpPmAdminStatus based on PrvtCrldpAdminStatus"""
    defaultValue = 1


_PrvtcrldpPmAdminStatus_Type.__name__ = "PrvtCrldpAdminStatus"
_PrvtcrldpPmAdminStatus_Object = MibTableColumn
prvtcrldpPmAdminStatus = _PrvtcrldpPmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 13),
    _PrvtcrldpPmAdminStatus_Type()
)
prvtcrldpPmAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmAdminStatus.setStatus("current")
_PrvtcrldpPmOperStatus_Type = PrvtCrldpOperStatus
_PrvtcrldpPmOperStatus_Object = MibTableColumn
prvtcrldpPmOperStatus = _PrvtcrldpPmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 14),
    _PrvtcrldpPmOperStatus_Type()
)
prvtcrldpPmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtcrldpPmOperStatus.setStatus("current")
_PrvtcrldpPmRowStatus_Type = RowStatus
_PrvtcrldpPmRowStatus_Object = MibTableColumn
prvtcrldpPmRowStatus = _PrvtcrldpPmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 15),
    _PrvtcrldpPmRowStatus_Type()
)
prvtcrldpPmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmRowStatus.setStatus("current")


class _PrvtcrldpPmRestartCapable_Type(TruthValue):
    """Custom type prvtcrldpPmRestartCapable based on TruthValue"""
    defaultValue = 2


_PrvtcrldpPmRestartCapable_Type.__name__ = "TruthValue"
_PrvtcrldpPmRestartCapable_Object = MibTableColumn
prvtcrldpPmRestartCapable = _PrvtcrldpPmRestartCapable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 16),
    _PrvtcrldpPmRestartCapable_Type()
)
prvtcrldpPmRestartCapable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmRestartCapable.setStatus("current")


class _PrvtcrldpPmReconnectTime_Type(Integer32):
    """Custom type prvtcrldpPmReconnectTime based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrvtcrldpPmReconnectTime_Type.__name__ = "Integer32"
_PrvtcrldpPmReconnectTime_Object = MibTableColumn
prvtcrldpPmReconnectTime = _PrvtcrldpPmReconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 17),
    _PrvtcrldpPmReconnectTime_Type()
)
prvtcrldpPmReconnectTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmReconnectTime.setStatus("current")


class _PrvtcrldpPmRecoveryTime_Type(Integer32):
    """Custom type prvtcrldpPmRecoveryTime based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrvtcrldpPmRecoveryTime_Type.__name__ = "Integer32"
_PrvtcrldpPmRecoveryTime_Object = MibTableColumn
prvtcrldpPmRecoveryTime = _PrvtcrldpPmRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 18),
    _PrvtcrldpPmRecoveryTime_Type()
)
prvtcrldpPmRecoveryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmRecoveryTime.setStatus("current")


class _PrvtcrldpPmMaxPeerReconnect_Type(Integer32):
    """Custom type prvtcrldpPmMaxPeerReconnect based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrvtcrldpPmMaxPeerReconnect_Type.__name__ = "Integer32"
_PrvtcrldpPmMaxPeerReconnect_Object = MibTableColumn
prvtcrldpPmMaxPeerReconnect = _PrvtcrldpPmMaxPeerReconnect_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 19),
    _PrvtcrldpPmMaxPeerReconnect_Type()
)
prvtcrldpPmMaxPeerReconnect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmMaxPeerReconnect.setStatus("current")


class _PrvtcrldpPmMaxPeerRecovery_Type(Integer32):
    """Custom type prvtcrldpPmMaxPeerRecovery based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrvtcrldpPmMaxPeerRecovery_Type.__name__ = "Integer32"
_PrvtcrldpPmMaxPeerRecovery_Object = MibTableColumn
prvtcrldpPmMaxPeerRecovery = _PrvtcrldpPmMaxPeerRecovery_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 20),
    _PrvtcrldpPmMaxPeerRecovery_Type()
)
prvtcrldpPmMaxPeerRecovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmMaxPeerRecovery.setStatus("current")


class _PrvtcrldpPmAdjDwnHoldTime_Type(Integer32):
    """Custom type prvtcrldpPmAdjDwnHoldTime based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrvtcrldpPmAdjDwnHoldTime_Type.__name__ = "Integer32"
_PrvtcrldpPmAdjDwnHoldTime_Object = MibTableColumn
prvtcrldpPmAdjDwnHoldTime = _PrvtcrldpPmAdjDwnHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 21),
    _PrvtcrldpPmAdjDwnHoldTime_Type()
)
prvtcrldpPmAdjDwnHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmAdjDwnHoldTime.setStatus("current")


class _PrvtcrldpPmOutSegProgOrder_Type(Integer32):
    """Custom type prvtcrldpPmOutSegProgOrder based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("connFirst", 1))
    )


_PrvtcrldpPmOutSegProgOrder_Type.__name__ = "Integer32"
_PrvtcrldpPmOutSegProgOrder_Object = MibTableColumn
prvtcrldpPmOutSegProgOrder = _PrvtcrldpPmOutSegProgOrder_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 22),
    _PrvtcrldpPmOutSegProgOrder_Type()
)
prvtcrldpPmOutSegProgOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmOutSegProgOrder.setStatus("current")


class _PrvtcrldpPmSupportIpv6_Type(TruthValue):
    """Custom type prvtcrldpPmSupportIpv6 based on TruthValue"""
    defaultValue = 2


_PrvtcrldpPmSupportIpv6_Type.__name__ = "TruthValue"
_PrvtcrldpPmSupportIpv6_Object = MibTableColumn
prvtcrldpPmSupportIpv6 = _PrvtcrldpPmSupportIpv6_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 23),
    _PrvtcrldpPmSupportIpv6_Type()
)
prvtcrldpPmSupportIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmSupportIpv6.setStatus("current")


class _PrvtcrldpPmPolicySupportFlags_Type(Bits):
    """Custom type prvtcrldpPmPolicySupportFlags based on Bits"""
    namedValues = NamedValues(
        *(("policySupported", 0),
          ("perFecOptimizationSupported", 1),
          ("suppressAddressPolicy", 2))
    )

_PrvtcrldpPmPolicySupportFlags_Type.__name__ = "Bits"
_PrvtcrldpPmPolicySupportFlags_Object = MibTableColumn
prvtcrldpPmPolicySupportFlags = _PrvtcrldpPmPolicySupportFlags_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 24),
    _PrvtcrldpPmPolicySupportFlags_Type()
)
prvtcrldpPmPolicySupportFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmPolicySupportFlags.setStatus("current")


class _PrvtcrldpPmCheckOutSegIntfaceStat_Type(TruthValue):
    """Custom type prvtcrldpPmCheckOutSegIntfaceStat based on TruthValue"""
    defaultValue = 2


_PrvtcrldpPmCheckOutSegIntfaceStat_Type.__name__ = "TruthValue"
_PrvtcrldpPmCheckOutSegIntfaceStat_Object = MibTableColumn
prvtcrldpPmCheckOutSegIntfaceStat = _PrvtcrldpPmCheckOutSegIntfaceStat_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 3, 1, 2, 1, 25),
    _PrvtcrldpPmCheckOutSegIntfaceStat_Type()
)
prvtcrldpPmCheckOutSegIntfaceStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtcrldpPmCheckOutSegIntfaceStat.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-CR-LDP-MIB",
    **{"PrvtCrldpAdminStatus": PrvtCrldpAdminStatus,
       "PrvtCrldpOperStatus": PrvtCrldpOperStatus,
       "PrvtCrldpIndex": PrvtCrldpIndex,
       "mpls": mpls,
       "prvtCrLdp": prvtCrLdp,
       "prvtCrLdpObjects": prvtCrLdpObjects,
       "prvtcrldpSigTable": prvtcrldpSigTable,
       "prvtcrldpSigEntry": prvtcrldpSigEntry,
       "prvtcrldpSigIndex": prvtcrldpSigIndex,
       "prvtcrldpSigPathManagerIndex": prvtcrldpSigPathManagerIndex,
       "prvtcrldpSigLsrIndex": prvtcrldpSigLsrIndex,
       "prvtcrldpSigSocketIfIndex": prvtcrldpSigSocketIfIndex,
       "prvtcrldpSigSessionBufPoolSize": prvtcrldpSigSessionBufPoolSize,
       "prvtcrldpSigEMBufPoolSize": prvtcrldpSigEMBufPoolSize,
       "prvtcrldpSigAMBufPoolSize": prvtcrldpSigAMBufPoolSize,
       "prvtcrldpSigAdminStatus": prvtcrldpSigAdminStatus,
       "prvtcrldpSigOperStatus": prvtcrldpSigOperStatus,
       "prvtcrldpSigRowStatus": prvtcrldpSigRowStatus,
       "prvtcrldpSigUseI3Interface": prvtcrldpSigUseI3Interface,
       "prvtcrldpSigConformanceFlags": prvtcrldpSigConformanceFlags,
       "prvtcrldpSigUseIPv6Transport": prvtcrldpSigUseIPv6Transport,
       "prvtcrldpSigSessStatusTrapEnable": prvtcrldpSigSessStatusTrapEnable,
       "prvtcrldpSigSessThreshTrapEnable": prvtcrldpSigSessThreshTrapEnable,
       "prvtcrldpSigPathVecLimitTrapEnable": prvtcrldpSigPathVecLimitTrapEnable,
       "prvtcrldpPmTable": prvtcrldpPmTable,
       "prvtcrldpPmEntry": prvtcrldpPmEntry,
       "prvtcrldpPmIndex": prvtcrldpPmIndex,
       "prvtcrldpPmLsrIndex": prvtcrldpPmLsrIndex,
       "prvtcrldpPmLdpEntityAutoCreate": prvtcrldpPmLdpEntityAutoCreate,
       "prvtcrldpPmLdpEntityAutoStart": prvtcrldpPmLdpEntityAutoStart,
       "prvtcrldpPmLdpEntityReuse": prvtcrldpPmLdpEntityReuse,
       "prvtcrldpPmLdpVersion": prvtcrldpPmLdpVersion,
       "prvtcrldpPmUseLdpFt": prvtcrldpPmUseLdpFt,
       "prvtcrldpPmAsNumber": prvtcrldpPmAsNumber,
       "prvtcrldpPmIprBufPoolSize": prvtcrldpPmIprBufPoolSize,
       "prvtcrldpPmLdpSupported": prvtcrldpPmLdpSupported,
       "prvtcrldpPmCrLdpSupported": prvtcrldpPmCrLdpSupported,
       "prvtcrldpPmQueryFECSupported": prvtcrldpPmQueryFECSupported,
       "prvtcrldpPmAdminStatus": prvtcrldpPmAdminStatus,
       "prvtcrldpPmOperStatus": prvtcrldpPmOperStatus,
       "prvtcrldpPmRowStatus": prvtcrldpPmRowStatus,
       "prvtcrldpPmRestartCapable": prvtcrldpPmRestartCapable,
       "prvtcrldpPmReconnectTime": prvtcrldpPmReconnectTime,
       "prvtcrldpPmRecoveryTime": prvtcrldpPmRecoveryTime,
       "prvtcrldpPmMaxPeerReconnect": prvtcrldpPmMaxPeerReconnect,
       "prvtcrldpPmMaxPeerRecovery": prvtcrldpPmMaxPeerRecovery,
       "prvtcrldpPmAdjDwnHoldTime": prvtcrldpPmAdjDwnHoldTime,
       "prvtcrldpPmOutSegProgOrder": prvtcrldpPmOutSegProgOrder,
       "prvtcrldpPmSupportIpv6": prvtcrldpPmSupportIpv6,
       "prvtcrldpPmPolicySupportFlags": prvtcrldpPmPolicySupportFlags,
       "prvtcrldpPmCheckOutSegIntfaceStat": prvtcrldpPmCheckOutSegIntfaceStat}
)
