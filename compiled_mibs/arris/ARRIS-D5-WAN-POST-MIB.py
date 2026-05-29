# SNMP MIB module (ARRIS-D5-WAN-POST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\d5\ARRIS-D5-WAN-POST-MIB

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

(arrisD5UEQam,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisD5UEQam")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

d5WanPOSTMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class D5WanPOSTTestResult(TextualConvention, Integer32):
    status = "current"
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
        *(("passed", 1),
          ("skipped", 2),
          ("failed", 3),
          ("notYetKnown", 4))
    )



# MIB Managed Objects in the order of their OIDs

_D5WanPOSTObjects_ObjectIdentity = ObjectIdentity
d5WanPOSTObjects = _D5WanPOSTObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1)
)
_D5WanPOSTTable_Object = MibTable
d5WanPOSTTable = _D5WanPOSTTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    d5WanPOSTTable.setStatus("current")
_D5WanPOSTEntry_Object = MibTableRow
d5WanPOSTEntry = _D5WanPOSTEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1, 1, 1)
)
d5WanPOSTEntry.setIndexNames(
    (0, "ARRIS-D5-WAN-POST-MIB", "d5WanPOSTTestId"),
)
if mibBuilder.loadTexts:
    d5WanPOSTEntry.setStatus("current")
_D5WanPOSTTestId_Type = Unsigned32
_D5WanPOSTTestId_Object = MibTableColumn
d5WanPOSTTestId = _D5WanPOSTTestId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1, 1, 1, 1),
    _D5WanPOSTTestId_Type()
)
d5WanPOSTTestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    d5WanPOSTTestId.setStatus("current")
_D5WanPOSTTestDescr_Type = DisplayString
_D5WanPOSTTestDescr_Object = MibTableColumn
d5WanPOSTTestDescr = _D5WanPOSTTestDescr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1, 1, 1, 2),
    _D5WanPOSTTestDescr_Type()
)
d5WanPOSTTestDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5WanPOSTTestDescr.setStatus("current")
_D5WanPOSTTestResult_Type = D5WanPOSTTestResult
_D5WanPOSTTestResult_Object = MibTableColumn
d5WanPOSTTestResult = _D5WanPOSTTestResult_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1, 1, 1, 3),
    _D5WanPOSTTestResult_Type()
)
d5WanPOSTTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5WanPOSTTestResult.setStatus("current")
_D5WanPOSTTestResultDescr_Type = DisplayString
_D5WanPOSTTestResultDescr_Object = MibTableColumn
d5WanPOSTTestResultDescr = _D5WanPOSTTestResultDescr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1, 1, 1, 4),
    _D5WanPOSTTestResultDescr_Type()
)
d5WanPOSTTestResultDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5WanPOSTTestResultDescr.setStatus("current")
_D5WanPOSTDiagnosticTable_Object = MibTable
d5WanPOSTDiagnosticTable = _D5WanPOSTDiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    d5WanPOSTDiagnosticTable.setStatus("current")
_D5WanPOSTDiagnosticEntry_Object = MibTableRow
d5WanPOSTDiagnosticEntry = _D5WanPOSTDiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1, 2, 1)
)
d5WanPOSTDiagnosticEntry.setIndexNames(
    (0, "ARRIS-D5-WAN-POST-MIB", "d5WanPOSTDiagTestId"),
)
if mibBuilder.loadTexts:
    d5WanPOSTDiagnosticEntry.setStatus("current")
_D5WanPOSTDiagTestId_Type = Unsigned32
_D5WanPOSTDiagTestId_Object = MibTableColumn
d5WanPOSTDiagTestId = _D5WanPOSTDiagTestId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1, 2, 1, 1),
    _D5WanPOSTDiagTestId_Type()
)
d5WanPOSTDiagTestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    d5WanPOSTDiagTestId.setStatus("current")
_D5WanPOSTDiagLastTestTimeStamp_Type = TimeStamp
_D5WanPOSTDiagLastTestTimeStamp_Object = MibTableColumn
d5WanPOSTDiagLastTestTimeStamp = _D5WanPOSTDiagLastTestTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1, 2, 1, 2),
    _D5WanPOSTDiagLastTestTimeStamp_Type()
)
d5WanPOSTDiagLastTestTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5WanPOSTDiagLastTestTimeStamp.setStatus("current")
_D5WanPOSTDiagLastTestResult_Type = D5WanPOSTTestResult
_D5WanPOSTDiagLastTestResult_Object = MibTableColumn
d5WanPOSTDiagLastTestResult = _D5WanPOSTDiagLastTestResult_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1, 2, 1, 3),
    _D5WanPOSTDiagLastTestResult_Type()
)
d5WanPOSTDiagLastTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5WanPOSTDiagLastTestResult.setStatus("current")
_D5WanPOSTDiagLastTestResultDescr_Type = DisplayString
_D5WanPOSTDiagLastTestResultDescr_Object = MibTableColumn
d5WanPOSTDiagLastTestResultDescr = _D5WanPOSTDiagLastTestResultDescr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1, 2, 1, 4),
    _D5WanPOSTDiagLastTestResultDescr_Type()
)
d5WanPOSTDiagLastTestResultDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5WanPOSTDiagLastTestResultDescr.setStatus("current")


class _D5WanPOSTDiagExecute_Type(Integer32):
    """Custom type d5WanPOSTDiagExecute based on Integer32"""
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
        *(("start", 0),
          ("running", 1),
          ("idle", 2),
          ("stop", 3))
    )


_D5WanPOSTDiagExecute_Type.__name__ = "Integer32"
_D5WanPOSTDiagExecute_Object = MibTableColumn
d5WanPOSTDiagExecute = _D5WanPOSTDiagExecute_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1, 2, 1, 5),
    _D5WanPOSTDiagExecute_Type()
)
d5WanPOSTDiagExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5WanPOSTDiagExecute.setStatus("current")
_D5WanPOSTDiagParam_Type = Integer32
_D5WanPOSTDiagParam_Object = MibTableColumn
d5WanPOSTDiagParam = _D5WanPOSTDiagParam_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 3, 1, 2, 1, 6),
    _D5WanPOSTDiagParam_Type()
)
d5WanPOSTDiagParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5WanPOSTDiagParam.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-D5-WAN-POST-MIB",
    **{"D5WanPOSTTestResult": D5WanPOSTTestResult,
       "d5WanPOSTMIB": d5WanPOSTMIB,
       "d5WanPOSTObjects": d5WanPOSTObjects,
       "d5WanPOSTTable": d5WanPOSTTable,
       "d5WanPOSTEntry": d5WanPOSTEntry,
       "d5WanPOSTTestId": d5WanPOSTTestId,
       "d5WanPOSTTestDescr": d5WanPOSTTestDescr,
       "d5WanPOSTTestResult": d5WanPOSTTestResult,
       "d5WanPOSTTestResultDescr": d5WanPOSTTestResultDescr,
       "d5WanPOSTDiagnosticTable": d5WanPOSTDiagnosticTable,
       "d5WanPOSTDiagnosticEntry": d5WanPOSTDiagnosticEntry,
       "d5WanPOSTDiagTestId": d5WanPOSTDiagTestId,
       "d5WanPOSTDiagLastTestTimeStamp": d5WanPOSTDiagLastTestTimeStamp,
       "d5WanPOSTDiagLastTestResult": d5WanPOSTDiagLastTestResult,
       "d5WanPOSTDiagLastTestResultDescr": d5WanPOSTDiagLastTestResultDescr,
       "d5WanPOSTDiagExecute": d5WanPOSTDiagExecute,
       "d5WanPOSTDiagParam": d5WanPOSTDiagParam}
)
