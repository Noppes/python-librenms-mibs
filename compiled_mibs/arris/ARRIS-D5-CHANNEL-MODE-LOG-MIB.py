# SNMP MIB module (ARRIS-D5-CHANNEL-MODE-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\d5\ARRIS-D5-CHANNEL-MODE-LOG-MIB

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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

d5ChannelModeLogMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 23)
)
if mibBuilder.loadTexts:
    d5ChannelModeLogMib.setRevisions(
        ("2009-08-28 08:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class D5ChannelMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("dual", 2),
          ("quad", 4),
          ("hex", 6),
          ("octal", 8))
    )



# MIB Managed Objects in the order of their OIDs

_D5ChannelModeLogTable_Object = MibTable
d5ChannelModeLogTable = _D5ChannelModeLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 23, 1)
)
if mibBuilder.loadTexts:
    d5ChannelModeLogTable.setStatus("current")
_D5ChannelModeLogEntry_Object = MibTableRow
d5ChannelModeLogEntry = _D5ChannelModeLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 23, 1, 1)
)
d5ChannelModeLogEntry.setIndexNames(
    (0, "ARRIS-D5-CHANNEL-MODE-LOG-MIB", "d5ChannelModeLogIndex"),
)
if mibBuilder.loadTexts:
    d5ChannelModeLogEntry.setStatus("current")
_D5ChannelModeLogIndex_Type = Unsigned32
_D5ChannelModeLogIndex_Object = MibTableColumn
d5ChannelModeLogIndex = _D5ChannelModeLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 23, 1, 1, 1),
    _D5ChannelModeLogIndex_Type()
)
d5ChannelModeLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    d5ChannelModeLogIndex.setStatus("current")
_D5ChannelModeLogTimeStamp_Type = Unsigned32
_D5ChannelModeLogTimeStamp_Object = MibTableColumn
d5ChannelModeLogTimeStamp = _D5ChannelModeLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 23, 1, 1, 2),
    _D5ChannelModeLogTimeStamp_Type()
)
d5ChannelModeLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5ChannelModeLogTimeStamp.setStatus("current")
_D5ChannelModeLogIfIndex_Type = InterfaceIndex
_D5ChannelModeLogIfIndex_Object = MibTableColumn
d5ChannelModeLogIfIndex = _D5ChannelModeLogIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 23, 1, 1, 3),
    _D5ChannelModeLogIfIndex_Type()
)
d5ChannelModeLogIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5ChannelModeLogIfIndex.setStatus("current")
_D5ChannelModeCurrentValue_Type = D5ChannelMode
_D5ChannelModeCurrentValue_Object = MibTableColumn
d5ChannelModeCurrentValue = _D5ChannelModeCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 23, 1, 1, 4),
    _D5ChannelModeCurrentValue_Type()
)
d5ChannelModeCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5ChannelModeCurrentValue.setStatus("current")
_D5ChannelModeNewValue_Type = D5ChannelMode
_D5ChannelModeNewValue_Object = MibTableColumn
d5ChannelModeNewValue = _D5ChannelModeNewValue_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 23, 1, 1, 5),
    _D5ChannelModeNewValue_Type()
)
d5ChannelModeNewValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5ChannelModeNewValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-D5-CHANNEL-MODE-LOG-MIB",
    **{"D5ChannelMode": D5ChannelMode,
       "d5ChannelModeLogMib": d5ChannelModeLogMib,
       "d5ChannelModeLogTable": d5ChannelModeLogTable,
       "d5ChannelModeLogEntry": d5ChannelModeLogEntry,
       "d5ChannelModeLogIndex": d5ChannelModeLogIndex,
       "d5ChannelModeLogTimeStamp": d5ChannelModeLogTimeStamp,
       "d5ChannelModeLogIfIndex": d5ChannelModeLogIfIndex,
       "d5ChannelModeCurrentValue": d5ChannelModeCurrentValue,
       "d5ChannelModeNewValue": d5ChannelModeNewValue}
)
