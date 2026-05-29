# SNMP MIB module (POWERSUPPLY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\hp\POWERSUPPLY-MIB

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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

hpicfPsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55)
)
if mibBuilder.loadTexts:
    hpicfPsMIB.setRevisions(
        ("2008-08-27 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class HpicfDcPsIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class HpicfDcPsState(TextualConvention, Integer32):
    status = "current"
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
        *(("psNotPresent", 1),
          ("psNotPlugged", 2),
          ("psPowered", 3),
          ("psFailed", 4),
          ("psPermFailure", 5),
          ("psMax", 6))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfEntityPs_ObjectIdentity = ObjectIdentity
hpicfEntityPs = _HpicfEntityPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1)
)
_HpicfPsTable_Object = MibTable
hpicfPsTable = _HpicfPsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfPsTable.setStatus("current")
_HpicfPsEntry_Object = MibTableRow
hpicfPsEntry = _HpicfPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1)
)
hpicfPsEntry.setIndexNames(
    (0, "POWERSUPPLY-MIB", "hpicfPsBayNum"),
)
if mibBuilder.loadTexts:
    hpicfPsEntry.setStatus("current")
_HpicfPsBayNum_Type = HpicfDcPsIndex
_HpicfPsBayNum_Object = MibTableColumn
hpicfPsBayNum = _HpicfPsBayNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 1),
    _HpicfPsBayNum_Type()
)
hpicfPsBayNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPsBayNum.setStatus("current")
_HpicfPsState_Type = HpicfDcPsState
_HpicfPsState_Object = MibTableColumn
hpicfPsState = _HpicfPsState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 2),
    _HpicfPsState_Type()
)
hpicfPsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsState.setStatus("current")
_HpicfPsFailures_Type = Counter32
_HpicfPsFailures_Object = MibTableColumn
hpicfPsFailures = _HpicfPsFailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 3),
    _HpicfPsFailures_Type()
)
hpicfPsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsFailures.setStatus("current")
_HpicfPsTemp_Type = Integer32
_HpicfPsTemp_Object = MibTableColumn
hpicfPsTemp = _HpicfPsTemp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 4),
    _HpicfPsTemp_Type()
)
hpicfPsTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsTemp.setStatus("current")


class _HpicfPsVoltageInfo_Type(SnmpAdminString):
    """Custom type hpicfPsVoltageInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpicfPsVoltageInfo_Type.__name__ = "SnmpAdminString"
_HpicfPsVoltageInfo_Object = MibTableColumn
hpicfPsVoltageInfo = _HpicfPsVoltageInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 5),
    _HpicfPsVoltageInfo_Type()
)
hpicfPsVoltageInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsVoltageInfo.setStatus("current")
_HpicfPsWattageCur_Type = Integer32
_HpicfPsWattageCur_Object = MibTableColumn
hpicfPsWattageCur = _HpicfPsWattageCur_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 6),
    _HpicfPsWattageCur_Type()
)
hpicfPsWattageCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsWattageCur.setStatus("current")
_HpicfPsWattageMax_Type = Integer32
_HpicfPsWattageMax_Object = MibTableColumn
hpicfPsWattageMax = _HpicfPsWattageMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 7),
    _HpicfPsWattageMax_Type()
)
hpicfPsWattageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsWattageMax.setStatus("current")
_HpicfPsLastCall_Type = Counter32
_HpicfPsLastCall_Object = MibTableColumn
hpicfPsLastCall = _HpicfPsLastCall_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 8),
    _HpicfPsLastCall_Type()
)
hpicfPsLastCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsLastCall.setStatus("current")
_HpicfPsConformance_ObjectIdentity = ObjectIdentity
hpicfPsConformance = _HpicfPsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2)
)
_HpicfPsCompliance_ObjectIdentity = ObjectIdentity
hpicfPsCompliance = _HpicfPsCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 1)
)
_HpicfPsGroups_ObjectIdentity = ObjectIdentity
hpicfPsGroups = _HpicfPsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 2)
)

# Managed Objects groups

hpicfPsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 2, 1)
)
hpicfPsGroup.setObjects(
      *(("POWERSUPPLY-MIB", "hpicfPsState"),
        ("POWERSUPPLY-MIB", "hpicfPsFailures"),
        ("POWERSUPPLY-MIB", "hpicfPsTemp"),
        ("POWERSUPPLY-MIB", "hpicfPsVoltageInfo"),
        ("POWERSUPPLY-MIB", "hpicfPsWattageCur"),
        ("POWERSUPPLY-MIB", "hpicfPsWattageMax"),
        ("POWERSUPPLY-MIB", "hpicfPsLastCall"))
)
if mibBuilder.loadTexts:
    hpicfPsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfDcPsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 1, 1)
)
hpicfDcPsCompliance.setObjects(
      *(("POWERSUPPLY-MIB", "hpicfPsGroup"),
        ("POWERSUPPLY-MIB", "hpicfPsGroup"))
)
if mibBuilder.loadTexts:
    hpicfDcPsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POWERSUPPLY-MIB",
    **{"HpicfDcPsIndex": HpicfDcPsIndex,
       "HpicfDcPsState": HpicfDcPsState,
       "hpicfPsMIB": hpicfPsMIB,
       "hpicfEntityPs": hpicfEntityPs,
       "hpicfPsTable": hpicfPsTable,
       "hpicfPsEntry": hpicfPsEntry,
       "hpicfPsBayNum": hpicfPsBayNum,
       "hpicfPsState": hpicfPsState,
       "hpicfPsFailures": hpicfPsFailures,
       "hpicfPsTemp": hpicfPsTemp,
       "hpicfPsVoltageInfo": hpicfPsVoltageInfo,
       "hpicfPsWattageCur": hpicfPsWattageCur,
       "hpicfPsWattageMax": hpicfPsWattageMax,
       "hpicfPsLastCall": hpicfPsLastCall,
       "hpicfPsConformance": hpicfPsConformance,
       "hpicfPsCompliance": hpicfPsCompliance,
       "hpicfDcPsCompliance": hpicfDcPsCompliance,
       "hpicfPsGroups": hpicfPsGroups,
       "hpicfPsGroup": hpicfPsGroup}
)
