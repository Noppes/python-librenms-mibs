# SNMP MIB module (FIREBRICK-VOIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\firebrick\FIREBRICK-VOIP-MIB

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

(firebrickNewStyle,) = mibBuilder.importSymbols(
    "FIREBRICK-MIB",
    "firebrickNewStyle")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fbSipMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060)
)
if mibBuilder.loadTexts:
    fbSipMib.setRevisions(
        ("2022-07-15 00:00",
         "2021-12-08 00:00",
         "2020-06-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FbSipActiveLegs_Type = Integer32
_FbSipActiveLegs_Object = MibScalar
fbSipActiveLegs = _FbSipActiveLegs_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 1),
    _FbSipActiveLegs_Type()
)
fbSipActiveLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbSipActiveLegs.setStatus("current")
_FbSipRadiusRegs_Type = Integer32
_FbSipRadiusRegs_Object = MibScalar
fbSipRadiusRegs = _FbSipRadiusRegs_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 2),
    _FbSipRadiusRegs_Type()
)
fbSipRadiusRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbSipRadiusRegs.setStatus("current")
_FbSipCarrierTable_Object = MibTable
fbSipCarrierTable = _FbSipCarrierTable_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 3)
)
if mibBuilder.loadTexts:
    fbSipCarrierTable.setStatus("current")
_FbSipCarrierEntry_Object = MibTableRow
fbSipCarrierEntry = _FbSipCarrierEntry_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 3, 1)
)
fbSipCarrierEntry.setIndexNames(
    (0, "FIREBRICK-VOIP-MIB", "fbSipCarrierIndex"),
)
if mibBuilder.loadTexts:
    fbSipCarrierEntry.setStatus("current")
_FbSipCarrierName_Type = DisplayString
_FbSipCarrierName_Object = MibTableColumn
fbSipCarrierName = _FbSipCarrierName_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 3, 1, 1),
    _FbSipCarrierName_Type()
)
fbSipCarrierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbSipCarrierName.setStatus("current")
_FbSipCarrierTotalLegs_Type = Integer32
_FbSipCarrierTotalLegs_Object = MibTableColumn
fbSipCarrierTotalLegs = _FbSipCarrierTotalLegs_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 3, 1, 2),
    _FbSipCarrierTotalLegs_Type()
)
fbSipCarrierTotalLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbSipCarrierTotalLegs.setStatus("current")
_FbSipCarrierConnectedLegs_Type = Integer32
_FbSipCarrierConnectedLegs_Object = MibTableColumn
fbSipCarrierConnectedLegs = _FbSipCarrierConnectedLegs_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 3, 1, 3),
    _FbSipCarrierConnectedLegs_Type()
)
fbSipCarrierConnectedLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbSipCarrierConnectedLegs.setStatus("current")


class _FbSipCarrierIndex_Type(Integer32):
    """Custom type fbSipCarrierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FbSipCarrierIndex_Type.__name__ = "Integer32"
_FbSipCarrierIndex_Object = MibTableColumn
fbSipCarrierIndex = _FbSipCarrierIndex_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 3, 1, 4),
    _FbSipCarrierIndex_Type()
)
fbSipCarrierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbSipCarrierIndex.setStatus("current")
_FbSipPhoneTable_Object = MibTable
fbSipPhoneTable = _FbSipPhoneTable_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 4)
)
if mibBuilder.loadTexts:
    fbSipPhoneTable.setStatus("current")
_FbSipPhoneEntry_Object = MibTableRow
fbSipPhoneEntry = _FbSipPhoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 4, 1)
)
fbSipPhoneEntry.setIndexNames(
    (0, "FIREBRICK-VOIP-MIB", "fbSipPhoneIndex"),
)
if mibBuilder.loadTexts:
    fbSipPhoneEntry.setStatus("current")
_FbSipPhoneName_Type = DisplayString
_FbSipPhoneName_Object = MibTableColumn
fbSipPhoneName = _FbSipPhoneName_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 4, 1, 1),
    _FbSipPhoneName_Type()
)
fbSipPhoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbSipPhoneName.setStatus("current")
_FbSipPhoneTotalLegs_Type = Integer32
_FbSipPhoneTotalLegs_Object = MibTableColumn
fbSipPhoneTotalLegs = _FbSipPhoneTotalLegs_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 4, 1, 2),
    _FbSipPhoneTotalLegs_Type()
)
fbSipPhoneTotalLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbSipPhoneTotalLegs.setStatus("current")
_FbSipPhoneConnectedLegs_Type = Integer32
_FbSipPhoneConnectedLegs_Object = MibTableColumn
fbSipPhoneConnectedLegs = _FbSipPhoneConnectedLegs_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 4, 1, 3),
    _FbSipPhoneConnectedLegs_Type()
)
fbSipPhoneConnectedLegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbSipPhoneConnectedLegs.setStatus("current")


class _FbSipPhoneIndex_Type(Integer32):
    """Custom type fbSipPhoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FbSipPhoneIndex_Type.__name__ = "Integer32"
_FbSipPhoneIndex_Object = MibTableColumn
fbSipPhoneIndex = _FbSipPhoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 4, 1, 4),
    _FbSipPhoneIndex_Type()
)
fbSipPhoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbSipPhoneIndex.setStatus("current")
_FbSipMixerUsage_Type = Integer32
_FbSipMixerUsage_Object = MibScalar
fbSipMixerUsage = _FbSipMixerUsage_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 5),
    _FbSipMixerUsage_Type()
)
fbSipMixerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbSipMixerUsage.setStatus("current")
_FbSipMixerHWM_Type = Integer32
_FbSipMixerHWM_Object = MibScalar
fbSipMixerHWM = _FbSipMixerHWM_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 6),
    _FbSipMixerHWM_Type()
)
fbSipMixerHWM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbSipMixerHWM.setStatus("current")
_FbSipCarriers_Type = Integer32
_FbSipCarriers_Object = MibScalar
fbSipCarriers = _FbSipCarriers_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 7),
    _FbSipCarriers_Type()
)
fbSipCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbSipCarriers.setStatus("current")
_FbSipMixerMax_Type = Integer32
_FbSipMixerMax_Object = MibScalar
fbSipMixerMax = _FbSipMixerMax_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 5060, 8),
    _FbSipMixerMax_Type()
)
fbSipMixerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbSipMixerMax.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIREBRICK-VOIP-MIB",
    **{"fbSipMib": fbSipMib,
       "fbSipActiveLegs": fbSipActiveLegs,
       "fbSipRadiusRegs": fbSipRadiusRegs,
       "fbSipCarrierTable": fbSipCarrierTable,
       "fbSipCarrierEntry": fbSipCarrierEntry,
       "fbSipCarrierName": fbSipCarrierName,
       "fbSipCarrierTotalLegs": fbSipCarrierTotalLegs,
       "fbSipCarrierConnectedLegs": fbSipCarrierConnectedLegs,
       "fbSipCarrierIndex": fbSipCarrierIndex,
       "fbSipPhoneTable": fbSipPhoneTable,
       "fbSipPhoneEntry": fbSipPhoneEntry,
       "fbSipPhoneName": fbSipPhoneName,
       "fbSipPhoneTotalLegs": fbSipPhoneTotalLegs,
       "fbSipPhoneConnectedLegs": fbSipPhoneConnectedLegs,
       "fbSipPhoneIndex": fbSipPhoneIndex,
       "fbSipMixerUsage": fbSipMixerUsage,
       "fbSipMixerHWM": fbSipMixerHWM,
       "fbSipCarriers": fbSipCarriers,
       "fbSipMixerMax": fbSipMixerMax}
)
