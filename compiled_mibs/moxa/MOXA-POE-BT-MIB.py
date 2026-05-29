# SNMP MIB module (MOXA-POE-BT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\moxa\MOXA-POE-BT-MIB

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
 enterprises,
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
    "enterprises",
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

poe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 608)
)
if mibBuilder.loadTexts:
    poe.setRevisions(
        ("2022-08-22 00:00",
         "2022-03-10 00:00",
         "2022-02-23 00:00",
         "2022-02-17 00:00",
         "2020-07-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Moxa_ObjectIdentity = ObjectIdentity
moxa = _Moxa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691)
)
_MxPoeBt_ObjectIdentity = ObjectIdentity
mxPoeBt = _MxPoeBt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2)
)
_PoeBtNotification_ObjectIdentity = ObjectIdentity
poeBtNotification = _PoeBtNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 0)
)
_PoeBtConfiguration_ObjectIdentity = ObjectIdentity
poeBtConfiguration = _PoeBtConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1)
)
_PoeBtConfigGeneral_ObjectIdentity = ObjectIdentity
poeBtConfigGeneral = _PoeBtConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 1)
)
_PoeBtConfigPowerOutput_Type = TruthValue
_PoeBtConfigPowerOutput_Object = MibScalar
poeBtConfigPowerOutput = _PoeBtConfigPowerOutput_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 1, 1),
    _PoeBtConfigPowerOutput_Type()
)
poeBtConfigPowerOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeBtConfigPowerOutput.setStatus("current")
_PoeBtConfigAutoPowerCutting_Type = TruthValue
_PoeBtConfigAutoPowerCutting_Object = MibScalar
poeBtConfigAutoPowerCutting = _PoeBtConfigAutoPowerCutting_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 1, 2),
    _PoeBtConfigAutoPowerCutting_Type()
)
poeBtConfigAutoPowerCutting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeBtConfigAutoPowerCutting.setStatus("current")


class _PoeBtConfigSystemPowerBudget_Type(Integer32):
    """Custom type poeBtConfigSystemPowerBudget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_PoeBtConfigSystemPowerBudget_Type.__name__ = "Integer32"
_PoeBtConfigSystemPowerBudget_Object = MibScalar
poeBtConfigSystemPowerBudget = _PoeBtConfigSystemPowerBudget_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 1, 3),
    _PoeBtConfigSystemPowerBudget_Type()
)
poeBtConfigSystemPowerBudget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeBtConfigSystemPowerBudget.setStatus("current")
_PoeBtConfigPortTable_Object = MibTable
poeBtConfigPortTable = _PoeBtConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    poeBtConfigPortTable.setStatus("current")
_PoeBtConfigPortEntry_Object = MibTableRow
poeBtConfigPortEntry = _PoeBtConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 1, 4, 1)
)
poeBtConfigPortEntry.setIndexNames(
    (0, "MOXA-POE-BT-MIB", "poeBtConfigPortIndex"),
)
if mibBuilder.loadTexts:
    poeBtConfigPortEntry.setStatus("current")
_PoeBtConfigPortIndex_Type = Integer32
_PoeBtConfigPortIndex_Object = MibTableColumn
poeBtConfigPortIndex = _PoeBtConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 1, 4, 1, 1),
    _PoeBtConfigPortIndex_Type()
)
poeBtConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtConfigPortIndex.setStatus("current")
_PoeBtConfigPortPowerOutput_Type = TruthValue
_PoeBtConfigPortPowerOutput_Object = MibTableColumn
poeBtConfigPortPowerOutput = _PoeBtConfigPortPowerOutput_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 1, 4, 1, 2),
    _PoeBtConfigPortPowerOutput_Type()
)
poeBtConfigPortPowerOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeBtConfigPortPowerOutput.setStatus("current")


class _PoeBtConfigOutputMode_Type(Integer32):
    """Custom type poeBtConfigOutputMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("highPower", 1),
          ("force", 2))
    )


_PoeBtConfigOutputMode_Type.__name__ = "Integer32"
_PoeBtConfigOutputMode_Object = MibTableColumn
poeBtConfigOutputMode = _PoeBtConfigOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 1, 4, 1, 3),
    _PoeBtConfigOutputMode_Type()
)
poeBtConfigOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeBtConfigOutputMode.setStatus("current")


class _PoeBtConfigPowerAllocation_Type(Integer32):
    """Custom type poeBtConfigPowerAllocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_PoeBtConfigPowerAllocation_Type.__name__ = "Integer32"
_PoeBtConfigPowerAllocation_Object = MibTableColumn
poeBtConfigPowerAllocation = _PoeBtConfigPowerAllocation_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 1, 4, 1, 4),
    _PoeBtConfigPowerAllocation_Type()
)
poeBtConfigPowerAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeBtConfigPowerAllocation.setStatus("current")
_PoeBtConfigLegacyPdDetection_Type = TruthValue
_PoeBtConfigLegacyPdDetection_Object = MibTableColumn
poeBtConfigLegacyPdDetection = _PoeBtConfigLegacyPdDetection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 1, 4, 1, 5),
    _PoeBtConfigLegacyPdDetection_Type()
)
poeBtConfigLegacyPdDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeBtConfigLegacyPdDetection.setStatus("current")


class _PoeBtConfigPriority_Type(Integer32):
    """Custom type poeBtConfigPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 0),
          ("high", 1),
          ("low", 2))
    )


_PoeBtConfigPriority_Type.__name__ = "Integer32"
_PoeBtConfigPriority_Object = MibTableColumn
poeBtConfigPriority = _PoeBtConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 1, 4, 1, 6),
    _PoeBtConfigPriority_Type()
)
poeBtConfigPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeBtConfigPriority.setStatus("current")


class _PoeBtConfigPowerManagementMode_Type(Integer32):
    """Custom type poeBtConfigPowerManagementMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allocatedPower", 0),
          ("consumedPower", 1))
    )


_PoeBtConfigPowerManagementMode_Type.__name__ = "Integer32"
_PoeBtConfigPowerManagementMode_Object = MibScalar
poeBtConfigPowerManagementMode = _PoeBtConfigPowerManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 1, 5),
    _PoeBtConfigPowerManagementMode_Type()
)
poeBtConfigPowerManagementMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeBtConfigPowerManagementMode.setStatus("current")
_PoeBtConfigFailureCheck_ObjectIdentity = ObjectIdentity
poeBtConfigFailureCheck = _PoeBtConfigFailureCheck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 2)
)
_PoeBtConfigFcPortTable_Object = MibTable
poeBtConfigFcPortTable = _PoeBtConfigFcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    poeBtConfigFcPortTable.setStatus("current")
_PoeBtConfigFcPortEntry_Object = MibTableRow
poeBtConfigFcPortEntry = _PoeBtConfigFcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 2, 1, 1)
)
poeBtConfigFcPortEntry.setIndexNames(
    (0, "MOXA-POE-BT-MIB", "poeBtConfigFcPortIndex"),
)
if mibBuilder.loadTexts:
    poeBtConfigFcPortEntry.setStatus("current")
_PoeBtConfigFcPortIndex_Type = Integer32
_PoeBtConfigFcPortIndex_Object = MibTableColumn
poeBtConfigFcPortIndex = _PoeBtConfigFcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 2, 1, 1, 1),
    _PoeBtConfigFcPortIndex_Type()
)
poeBtConfigFcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtConfigFcPortIndex.setStatus("current")
_PoeBtConfigFcEnable_Type = TruthValue
_PoeBtConfigFcEnable_Object = MibTableColumn
poeBtConfigFcEnable = _PoeBtConfigFcEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 2, 1, 1, 2),
    _PoeBtConfigFcEnable_Type()
)
poeBtConfigFcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeBtConfigFcEnable.setStatus("current")
_PoeBtConfigFcDeviceIp_Type = IpAddress
_PoeBtConfigFcDeviceIp_Object = MibTableColumn
poeBtConfigFcDeviceIp = _PoeBtConfigFcDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 2, 1, 1, 3),
    _PoeBtConfigFcDeviceIp_Type()
)
poeBtConfigFcDeviceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeBtConfigFcDeviceIp.setStatus("current")


class _PoeBtConfigFcNoResponseTimes_Type(Integer32):
    """Custom type poeBtConfigFcNoResponseTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PoeBtConfigFcNoResponseTimes_Type.__name__ = "Integer32"
_PoeBtConfigFcNoResponseTimes_Object = MibTableColumn
poeBtConfigFcNoResponseTimes = _PoeBtConfigFcNoResponseTimes_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 2, 1, 1, 4),
    _PoeBtConfigFcNoResponseTimes_Type()
)
poeBtConfigFcNoResponseTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeBtConfigFcNoResponseTimes.setStatus("current")


class _PoeBtConfigFcCheckFrequency_Type(Integer32):
    """Custom type poeBtConfigFcCheckFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_PoeBtConfigFcCheckFrequency_Type.__name__ = "Integer32"
_PoeBtConfigFcCheckFrequency_Object = MibTableColumn
poeBtConfigFcCheckFrequency = _PoeBtConfigFcCheckFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 2, 1, 1, 5),
    _PoeBtConfigFcCheckFrequency_Type()
)
poeBtConfigFcCheckFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeBtConfigFcCheckFrequency.setStatus("current")


class _PoeBtConfigFcAction_Type(Integer32):
    """Custom type poeBtConfigFcAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("restartPd", 1),
          ("shutdownPd", 2))
    )


_PoeBtConfigFcAction_Type.__name__ = "Integer32"
_PoeBtConfigFcAction_Object = MibTableColumn
poeBtConfigFcAction = _PoeBtConfigFcAction_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 2, 1, 1, 6),
    _PoeBtConfigFcAction_Type()
)
poeBtConfigFcAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeBtConfigFcAction.setStatus("current")
_PoeBtConfigScheduling_ObjectIdentity = ObjectIdentity
poeBtConfigScheduling = _PoeBtConfigScheduling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3)
)
_PoeBtConfigScheRuleTable_Object = MibTable
poeBtConfigScheRuleTable = _PoeBtConfigScheRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    poeBtConfigScheRuleTable.setStatus("current")
_PoeBtConfigScheRuleEntry_Object = MibTableRow
poeBtConfigScheRuleEntry = _PoeBtConfigScheRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1, 1)
)
poeBtConfigScheRuleEntry.setIndexNames(
    (0, "MOXA-POE-BT-MIB", "poeBtConfigRuleIndex"),
)
if mibBuilder.loadTexts:
    poeBtConfigScheRuleEntry.setStatus("current")
_PoeBtConfigRuleIndex_Type = Integer32
_PoeBtConfigRuleIndex_Object = MibTableColumn
poeBtConfigRuleIndex = _PoeBtConfigRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1, 1, 1),
    _PoeBtConfigRuleIndex_Type()
)
poeBtConfigRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtConfigRuleIndex.setStatus("current")


class _PoeBtConfigScheName_Type(DisplayString):
    """Custom type poeBtConfigScheName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PoeBtConfigScheName_Type.__name__ = "DisplayString"
_PoeBtConfigScheName_Object = MibTableColumn
poeBtConfigScheName = _PoeBtConfigScheName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1, 1, 2),
    _PoeBtConfigScheName_Type()
)
poeBtConfigScheName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    poeBtConfigScheName.setStatus("current")
_PoeBtConfigScheEnable_Type = TruthValue
_PoeBtConfigScheEnable_Object = MibTableColumn
poeBtConfigScheEnable = _PoeBtConfigScheEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1, 1, 3),
    _PoeBtConfigScheEnable_Type()
)
poeBtConfigScheEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    poeBtConfigScheEnable.setStatus("current")


class _PoeBtConfigScheStartDateYear_Type(Integer32):
    """Custom type poeBtConfigScheStartDateYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1970, 2038),
    )


_PoeBtConfigScheStartDateYear_Type.__name__ = "Integer32"
_PoeBtConfigScheStartDateYear_Object = MibTableColumn
poeBtConfigScheStartDateYear = _PoeBtConfigScheStartDateYear_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1, 1, 4),
    _PoeBtConfigScheStartDateYear_Type()
)
poeBtConfigScheStartDateYear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    poeBtConfigScheStartDateYear.setStatus("current")


class _PoeBtConfigScheStartDateMonth_Type(Integer32):
    """Custom type poeBtConfigScheStartDateMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_PoeBtConfigScheStartDateMonth_Type.__name__ = "Integer32"
_PoeBtConfigScheStartDateMonth_Object = MibTableColumn
poeBtConfigScheStartDateMonth = _PoeBtConfigScheStartDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1, 1, 5),
    _PoeBtConfigScheStartDateMonth_Type()
)
poeBtConfigScheStartDateMonth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    poeBtConfigScheStartDateMonth.setStatus("current")


class _PoeBtConfigScheStartDateDay_Type(Integer32):
    """Custom type poeBtConfigScheStartDateDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_PoeBtConfigScheStartDateDay_Type.__name__ = "Integer32"
_PoeBtConfigScheStartDateDay_Object = MibTableColumn
poeBtConfigScheStartDateDay = _PoeBtConfigScheStartDateDay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1, 1, 6),
    _PoeBtConfigScheStartDateDay_Type()
)
poeBtConfigScheStartDateDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    poeBtConfigScheStartDateDay.setStatus("current")


class _PoeBtConfigScheStartTimeHour_Type(Integer32):
    """Custom type poeBtConfigScheStartTimeHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_PoeBtConfigScheStartTimeHour_Type.__name__ = "Integer32"
_PoeBtConfigScheStartTimeHour_Object = MibTableColumn
poeBtConfigScheStartTimeHour = _PoeBtConfigScheStartTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1, 1, 7),
    _PoeBtConfigScheStartTimeHour_Type()
)
poeBtConfigScheStartTimeHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    poeBtConfigScheStartTimeHour.setStatus("current")


class _PoeBtConfigScheStartTimeMin_Type(Integer32):
    """Custom type poeBtConfigScheStartTimeMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_PoeBtConfigScheStartTimeMin_Type.__name__ = "Integer32"
_PoeBtConfigScheStartTimeMin_Object = MibTableColumn
poeBtConfigScheStartTimeMin = _PoeBtConfigScheStartTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1, 1, 8),
    _PoeBtConfigScheStartTimeMin_Type()
)
poeBtConfigScheStartTimeMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    poeBtConfigScheStartTimeMin.setStatus("current")


class _PoeBtConfigScheEndTimeHour_Type(Integer32):
    """Custom type poeBtConfigScheEndTimeHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_PoeBtConfigScheEndTimeHour_Type.__name__ = "Integer32"
_PoeBtConfigScheEndTimeHour_Object = MibTableColumn
poeBtConfigScheEndTimeHour = _PoeBtConfigScheEndTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1, 1, 9),
    _PoeBtConfigScheEndTimeHour_Type()
)
poeBtConfigScheEndTimeHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    poeBtConfigScheEndTimeHour.setStatus("current")


class _PoeBtConfigScheEndTimeMin_Type(Integer32):
    """Custom type poeBtConfigScheEndTimeMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_PoeBtConfigScheEndTimeMin_Type.__name__ = "Integer32"
_PoeBtConfigScheEndTimeMin_Object = MibTableColumn
poeBtConfigScheEndTimeMin = _PoeBtConfigScheEndTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1, 1, 10),
    _PoeBtConfigScheEndTimeMin_Type()
)
poeBtConfigScheEndTimeMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    poeBtConfigScheEndTimeMin.setStatus("current")
_PoeBtConfigScheRepeatOn_Type = OctetString
_PoeBtConfigScheRepeatOn_Object = MibTableColumn
poeBtConfigScheRepeatOn = _PoeBtConfigScheRepeatOn_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1, 1, 11),
    _PoeBtConfigScheRepeatOn_Type()
)
poeBtConfigScheRepeatOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    poeBtConfigScheRepeatOn.setStatus("current")
_PoeBtConfigScheAppliedPorts_Type = OctetString
_PoeBtConfigScheAppliedPorts_Object = MibTableColumn
poeBtConfigScheAppliedPorts = _PoeBtConfigScheAppliedPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1, 1, 12),
    _PoeBtConfigScheAppliedPorts_Type()
)
poeBtConfigScheAppliedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    poeBtConfigScheAppliedPorts.setStatus("current")
_PoeBtConfigScheRowStatus_Type = RowStatus
_PoeBtConfigScheRowStatus_Object = MibTableColumn
poeBtConfigScheRowStatus = _PoeBtConfigScheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 1, 3, 1, 1, 13),
    _PoeBtConfigScheRowStatus_Type()
)
poeBtConfigScheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    poeBtConfigScheRowStatus.setStatus("current")
_PoeBtStatus_ObjectIdentity = ObjectIdentity
poeBtStatus = _PoeBtStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2)
)
_PoeBtStatMonitor_ObjectIdentity = ObjectIdentity
poeBtStatMonitor = _PoeBtStatMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1)
)
_PoeBtStatMaxInputPower_Type = Integer32
_PoeBtStatMaxInputPower_Object = MibScalar
poeBtStatMaxInputPower = _PoeBtStatMaxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 1),
    _PoeBtStatMaxInputPower_Type()
)
poeBtStatMaxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatMaxInputPower.setStatus("current")
_PoeBtStatActualPower_Type = Integer32
_PoeBtStatActualPower_Object = MibScalar
poeBtStatActualPower = _PoeBtStatActualPower_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 2),
    _PoeBtStatActualPower_Type()
)
poeBtStatActualPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatActualPower.setStatus("current")
_PoeBtStatBudgetLimit_Type = Integer32
_PoeBtStatBudgetLimit_Object = MibScalar
poeBtStatBudgetLimit = _PoeBtStatBudgetLimit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 3),
    _PoeBtStatBudgetLimit_Type()
)
poeBtStatBudgetLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatBudgetLimit.setStatus("current")
_PoeBtStatConsumedPower_Type = Integer32
_PoeBtStatConsumedPower_Object = MibScalar
poeBtStatConsumedPower = _PoeBtStatConsumedPower_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 4),
    _PoeBtStatConsumedPower_Type()
)
poeBtStatConsumedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatConsumedPower.setStatus("current")
_PoeBtStatRemainingAvailablePower_Type = Integer32
_PoeBtStatRemainingAvailablePower_Object = MibScalar
poeBtStatRemainingAvailablePower = _PoeBtStatRemainingAvailablePower_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 5),
    _PoeBtStatRemainingAvailablePower_Type()
)
poeBtStatRemainingAvailablePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatRemainingAvailablePower.setStatus("current")
_PoeBtStatPortTable_Object = MibTable
poeBtStatPortTable = _PoeBtStatPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    poeBtStatPortTable.setStatus("current")
_PoeBtStatPortEntry_Object = MibTableRow
poeBtStatPortEntry = _PoeBtStatPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 6, 1)
)
poeBtStatPortEntry.setIndexNames(
    (0, "MOXA-POE-BT-MIB", "poeBtStatPortIndex"),
)
if mibBuilder.loadTexts:
    poeBtStatPortEntry.setStatus("current")
_PoeBtStatPortIndex_Type = Integer32
_PoeBtStatPortIndex_Object = MibTableColumn
poeBtStatPortIndex = _PoeBtStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 6, 1, 1),
    _PoeBtStatPortIndex_Type()
)
poeBtStatPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatPortIndex.setStatus("current")
_PoeBtStatPowerOutput_Type = TruthValue
_PoeBtStatPowerOutput_Object = MibTableColumn
poeBtStatPowerOutput = _PoeBtStatPowerOutput_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 6, 1, 2),
    _PoeBtStatPowerOutput_Type()
)
poeBtStatPowerOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatPowerOutput.setStatus("current")
_PoeBtStatClassification_Type = OctetString
_PoeBtStatClassification_Object = MibTableColumn
poeBtStatClassification = _PoeBtStatClassification_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 6, 1, 3),
    _PoeBtStatClassification_Type()
)
poeBtStatClassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatClassification.setStatus("current")
_PoeBtStatCurrent_Type = DisplayString
_PoeBtStatCurrent_Object = MibTableColumn
poeBtStatCurrent = _PoeBtStatCurrent_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 6, 1, 4),
    _PoeBtStatCurrent_Type()
)
poeBtStatCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatCurrent.setStatus("current")
_PoeBtStatVoltage_Type = DisplayString
_PoeBtStatVoltage_Object = MibTableColumn
poeBtStatVoltage = _PoeBtStatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 6, 1, 5),
    _PoeBtStatVoltage_Type()
)
poeBtStatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatVoltage.setStatus("current")
_PoeBtStatConsumption_Type = DisplayString
_PoeBtStatConsumption_Object = MibTableColumn
poeBtStatConsumption = _PoeBtStatConsumption_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 6, 1, 6),
    _PoeBtStatConsumption_Type()
)
poeBtStatConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatConsumption.setStatus("current")


class _PoeBtStatDeviceType_Type(Integer32):
    """Custom type poeBtStatDeviceType based on Integer32"""
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
        *(("notPresent", 0),
          ("legacy", 1),
          ("dot3af", 2),
          ("dot3at", 3),
          ("reserved", 4),
          ("nonPdOrPdShortCircuit", 5),
          ("unknown", 6),
          ("na", 7),
          ("dot3btss", 8),
          ("dot3btds", 9))
    )


_PoeBtStatDeviceType_Type.__name__ = "Integer32"
_PoeBtStatDeviceType_Object = MibTableColumn
poeBtStatDeviceType = _PoeBtStatDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 6, 1, 7),
    _PoeBtStatDeviceType_Type()
)
poeBtStatDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatDeviceType.setStatus("current")


class _PoeBtStatConfigSuggestion_Type(Integer32):
    """Custom type poeBtStatConfigSuggestion based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("noSuggestion", 0),
          ("enablePoe", 1),
          ("disablePoe", 2),
          ("selectAuto", 3),
          ("selectHighPower", 4),
          ("selectForce", 5),
          ("enableLegacy", 6),
          ("raiseEpsVoltage", 7))
    )


_PoeBtStatConfigSuggestion_Type.__name__ = "Integer32"
_PoeBtStatConfigSuggestion_Object = MibTableColumn
poeBtStatConfigSuggestion = _PoeBtStatConfigSuggestion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 6, 1, 8),
    _PoeBtStatConfigSuggestion_Type()
)
poeBtStatConfigSuggestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatConfigSuggestion.setStatus("current")


class _PoeBtStatPdFailureCheckStatus_Type(Integer32):
    """Custom type poeBtStatPdFailureCheckStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAlive", 0),
          ("alive", 1),
          ("disabled", 2))
    )


_PoeBtStatPdFailureCheckStatus_Type.__name__ = "Integer32"
_PoeBtStatPdFailureCheckStatus_Object = MibTableColumn
poeBtStatPdFailureCheckStatus = _PoeBtStatPdFailureCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 6, 1, 9),
    _PoeBtStatPdFailureCheckStatus_Type()
)
poeBtStatPdFailureCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatPdFailureCheckStatus.setStatus("current")
_PoeBtStatAllocatedPower_Type = Integer32
_PoeBtStatAllocatedPower_Object = MibScalar
poeBtStatAllocatedPower = _PoeBtStatAllocatedPower_Object(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 2, 1, 7),
    _PoeBtStatAllocatedPower_Type()
)
poeBtStatAllocatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeBtStatAllocatedPower.setStatus("current")

# Managed Objects groups


# Notification objects

poeBtNotifyPdPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 0, 1)
)
poeBtNotifyPdPowerOn.setObjects(
    ("MOXA-POE-BT-MIB", "poeBtStatPortIndex")
)
if mibBuilder.loadTexts:
    poeBtNotifyPdPowerOn.setStatus(
        "current"
    )

poeBtNotifyPdPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 0, 2)
)
poeBtNotifyPdPowerOff.setObjects(
    ("MOXA-POE-BT-MIB", "poeBtStatPortIndex")
)
if mibBuilder.loadTexts:
    poeBtNotifyPdPowerOff.setStatus(
        "current"
    )

poeBtNotifyLowInputVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 0, 3)
)
if mibBuilder.loadTexts:
    poeBtNotifyLowInputVoltage.setStatus(
        "current"
    )

poeBtNotifyPdOverCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 0, 4)
)
poeBtNotifyPdOverCurrent.setObjects(
    ("MOXA-POE-BT-MIB", "poeBtStatPortIndex")
)
if mibBuilder.loadTexts:
    poeBtNotifyPdOverCurrent.setStatus(
        "current"
    )

poeBtNotifyPdNoResponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 0, 5)
)
poeBtNotifyPdNoResponse.setObjects(
    ("MOXA-POE-BT-MIB", "poeBtStatPortIndex")
)
if mibBuilder.loadTexts:
    poeBtNotifyPdNoResponse.setStatus(
        "current"
    )

poeBtNotifyOverBudgetLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 0, 6)
)
poeBtNotifyOverBudgetLimit.setObjects(
      *(("MOXA-POE-BT-MIB", "poeBtStatConsumedPower"),
        ("MOXA-POE-BT-MIB", "poeBtStatMaxInputPower"))
)
if mibBuilder.loadTexts:
    poeBtNotifyOverBudgetLimit.setStatus(
        "current"
    )

poeBtNotifyPdDetectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 0, 7)
)
poeBtNotifyPdDetectionFailure.setObjects(
      *(("MOXA-POE-BT-MIB", "poeBtStatPortIndex"),
        ("MOXA-POE-BT-MIB", "poeBtStatDeviceType"),
        ("MOXA-POE-BT-MIB", "poeBtStatConfigSuggestion"))
)
if mibBuilder.loadTexts:
    poeBtNotifyPdDetectionFailure.setStatus(
        "current"
    )

poeBtNotifyNonPdOrPdShortCircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 608, 2, 0, 8)
)
poeBtNotifyNonPdOrPdShortCircuit.setObjects(
    ("MOXA-POE-BT-MIB", "poeBtStatPortIndex")
)
if mibBuilder.loadTexts:
    poeBtNotifyNonPdOrPdShortCircuit.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-POE-BT-MIB",
    **{"moxa": moxa,
       "poe": poe,
       "mxPoeBt": mxPoeBt,
       "poeBtNotification": poeBtNotification,
       "poeBtNotifyPdPowerOn": poeBtNotifyPdPowerOn,
       "poeBtNotifyPdPowerOff": poeBtNotifyPdPowerOff,
       "poeBtNotifyLowInputVoltage": poeBtNotifyLowInputVoltage,
       "poeBtNotifyPdOverCurrent": poeBtNotifyPdOverCurrent,
       "poeBtNotifyPdNoResponse": poeBtNotifyPdNoResponse,
       "poeBtNotifyOverBudgetLimit": poeBtNotifyOverBudgetLimit,
       "poeBtNotifyPdDetectionFailure": poeBtNotifyPdDetectionFailure,
       "poeBtNotifyNonPdOrPdShortCircuit": poeBtNotifyNonPdOrPdShortCircuit,
       "poeBtConfiguration": poeBtConfiguration,
       "poeBtConfigGeneral": poeBtConfigGeneral,
       "poeBtConfigPowerOutput": poeBtConfigPowerOutput,
       "poeBtConfigAutoPowerCutting": poeBtConfigAutoPowerCutting,
       "poeBtConfigSystemPowerBudget": poeBtConfigSystemPowerBudget,
       "poeBtConfigPortTable": poeBtConfigPortTable,
       "poeBtConfigPortEntry": poeBtConfigPortEntry,
       "poeBtConfigPortIndex": poeBtConfigPortIndex,
       "poeBtConfigPortPowerOutput": poeBtConfigPortPowerOutput,
       "poeBtConfigOutputMode": poeBtConfigOutputMode,
       "poeBtConfigPowerAllocation": poeBtConfigPowerAllocation,
       "poeBtConfigLegacyPdDetection": poeBtConfigLegacyPdDetection,
       "poeBtConfigPriority": poeBtConfigPriority,
       "poeBtConfigPowerManagementMode": poeBtConfigPowerManagementMode,
       "poeBtConfigFailureCheck": poeBtConfigFailureCheck,
       "poeBtConfigFcPortTable": poeBtConfigFcPortTable,
       "poeBtConfigFcPortEntry": poeBtConfigFcPortEntry,
       "poeBtConfigFcPortIndex": poeBtConfigFcPortIndex,
       "poeBtConfigFcEnable": poeBtConfigFcEnable,
       "poeBtConfigFcDeviceIp": poeBtConfigFcDeviceIp,
       "poeBtConfigFcNoResponseTimes": poeBtConfigFcNoResponseTimes,
       "poeBtConfigFcCheckFrequency": poeBtConfigFcCheckFrequency,
       "poeBtConfigFcAction": poeBtConfigFcAction,
       "poeBtConfigScheduling": poeBtConfigScheduling,
       "poeBtConfigScheRuleTable": poeBtConfigScheRuleTable,
       "poeBtConfigScheRuleEntry": poeBtConfigScheRuleEntry,
       "poeBtConfigRuleIndex": poeBtConfigRuleIndex,
       "poeBtConfigScheName": poeBtConfigScheName,
       "poeBtConfigScheEnable": poeBtConfigScheEnable,
       "poeBtConfigScheStartDateYear": poeBtConfigScheStartDateYear,
       "poeBtConfigScheStartDateMonth": poeBtConfigScheStartDateMonth,
       "poeBtConfigScheStartDateDay": poeBtConfigScheStartDateDay,
       "poeBtConfigScheStartTimeHour": poeBtConfigScheStartTimeHour,
       "poeBtConfigScheStartTimeMin": poeBtConfigScheStartTimeMin,
       "poeBtConfigScheEndTimeHour": poeBtConfigScheEndTimeHour,
       "poeBtConfigScheEndTimeMin": poeBtConfigScheEndTimeMin,
       "poeBtConfigScheRepeatOn": poeBtConfigScheRepeatOn,
       "poeBtConfigScheAppliedPorts": poeBtConfigScheAppliedPorts,
       "poeBtConfigScheRowStatus": poeBtConfigScheRowStatus,
       "poeBtStatus": poeBtStatus,
       "poeBtStatMonitor": poeBtStatMonitor,
       "poeBtStatMaxInputPower": poeBtStatMaxInputPower,
       "poeBtStatActualPower": poeBtStatActualPower,
       "poeBtStatBudgetLimit": poeBtStatBudgetLimit,
       "poeBtStatConsumedPower": poeBtStatConsumedPower,
       "poeBtStatRemainingAvailablePower": poeBtStatRemainingAvailablePower,
       "poeBtStatPortTable": poeBtStatPortTable,
       "poeBtStatPortEntry": poeBtStatPortEntry,
       "poeBtStatPortIndex": poeBtStatPortIndex,
       "poeBtStatPowerOutput": poeBtStatPowerOutput,
       "poeBtStatClassification": poeBtStatClassification,
       "poeBtStatCurrent": poeBtStatCurrent,
       "poeBtStatVoltage": poeBtStatVoltage,
       "poeBtStatConsumption": poeBtStatConsumption,
       "poeBtStatDeviceType": poeBtStatDeviceType,
       "poeBtStatConfigSuggestion": poeBtStatConfigSuggestion,
       "poeBtStatPdFailureCheckStatus": poeBtStatPdFailureCheckStatus,
       "poeBtStatAllocatedPower": poeBtStatAllocatedPower}
)
