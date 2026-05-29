# SNMP MIB module (BEGEMOT-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pfsense\BEGEMOT-ATM-MIB

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

(begemot,) = mibBuilder.importSymbols(
    "BEGEMOT-MIB",
    "begemot")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

begemotAtm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AtmESI(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



# MIB Managed Objects in the order of their OIDs

_BegemotAtmObjects_ObjectIdentity = ObjectIdentity
begemotAtmObjects = _BegemotAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1)
)
_BegemotAtmIfTable_Object = MibTable
begemotAtmIfTable = _BegemotAtmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1)
)
if mibBuilder.loadTexts:
    begemotAtmIfTable.setStatus("current")
_BegemotAtmIfEntry_Object = MibTableRow
begemotAtmIfEntry = _BegemotAtmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1)
)
begemotAtmIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    begemotAtmIfEntry.setStatus("current")


class _BegemotAtmIfName_Type(DisplayString):
    """Custom type begemotAtmIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_BegemotAtmIfName_Type.__name__ = "DisplayString"
_BegemotAtmIfName_Object = MibTableColumn
begemotAtmIfName = _BegemotAtmIfName_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 1),
    _BegemotAtmIfName_Type()
)
begemotAtmIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmIfName.setStatus("current")
_BegemotAtmIfPcr_Type = Unsigned32
_BegemotAtmIfPcr_Object = MibTableColumn
begemotAtmIfPcr = _BegemotAtmIfPcr_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 2),
    _BegemotAtmIfPcr_Type()
)
begemotAtmIfPcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmIfPcr.setStatus("current")


class _BegemotAtmIfMedia_Type(Integer32):
    """Custom type begemotAtmIfMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 3),
          ("utp25", 4),
          ("taxi100", 5),
          ("taxi140", 6),
          ("mm155", 7),
          ("sm155", 8),
          ("utp155", 9),
          ("mm622", 10),
          ("sm622", 11),
          ("virtual", 12))
    )


_BegemotAtmIfMedia_Type.__name__ = "Integer32"
_BegemotAtmIfMedia_Object = MibTableColumn
begemotAtmIfMedia = _BegemotAtmIfMedia_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 3),
    _BegemotAtmIfMedia_Type()
)
begemotAtmIfMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmIfMedia.setStatus("current")


class _BegemotAtmIfVpiBits_Type(Unsigned32):
    """Custom type begemotAtmIfVpiBits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_BegemotAtmIfVpiBits_Type.__name__ = "Unsigned32"
_BegemotAtmIfVpiBits_Object = MibTableColumn
begemotAtmIfVpiBits = _BegemotAtmIfVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 4),
    _BegemotAtmIfVpiBits_Type()
)
begemotAtmIfVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmIfVpiBits.setStatus("current")


class _BegemotAtmIfVciBits_Type(Unsigned32):
    """Custom type begemotAtmIfVciBits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_BegemotAtmIfVciBits_Type.__name__ = "Unsigned32"
_BegemotAtmIfVciBits_Object = MibTableColumn
begemotAtmIfVciBits = _BegemotAtmIfVciBits_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 5),
    _BegemotAtmIfVciBits_Type()
)
begemotAtmIfVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmIfVciBits.setStatus("current")


class _BegemotAtmIfMaxVpcs_Type(Unsigned32):
    """Custom type begemotAtmIfMaxVpcs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_BegemotAtmIfMaxVpcs_Type.__name__ = "Unsigned32"
_BegemotAtmIfMaxVpcs_Object = MibTableColumn
begemotAtmIfMaxVpcs = _BegemotAtmIfMaxVpcs_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 6),
    _BegemotAtmIfMaxVpcs_Type()
)
begemotAtmIfMaxVpcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmIfMaxVpcs.setStatus("current")


class _BegemotAtmIfMaxVccs_Type(Unsigned32):
    """Custom type begemotAtmIfMaxVccs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777216),
    )


_BegemotAtmIfMaxVccs_Type.__name__ = "Unsigned32"
_BegemotAtmIfMaxVccs_Object = MibTableColumn
begemotAtmIfMaxVccs = _BegemotAtmIfMaxVccs_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 7),
    _BegemotAtmIfMaxVccs_Type()
)
begemotAtmIfMaxVccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmIfMaxVccs.setStatus("current")
_BegemotAtmIfEsi_Type = AtmESI
_BegemotAtmIfEsi_Object = MibTableColumn
begemotAtmIfEsi = _BegemotAtmIfEsi_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 8),
    _BegemotAtmIfEsi_Type()
)
begemotAtmIfEsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmIfEsi.setStatus("current")


class _BegemotAtmIfCarrierStatus_Type(Integer32):
    """Custom type begemotAtmIfCarrierStatus based on Integer32"""
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
        *(("carrierOn", 1),
          ("carrierOff", 2),
          ("unknown", 3),
          ("none", 4))
    )


_BegemotAtmIfCarrierStatus_Type.__name__ = "Integer32"
_BegemotAtmIfCarrierStatus_Object = MibTableColumn
begemotAtmIfCarrierStatus = _BegemotAtmIfCarrierStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 9),
    _BegemotAtmIfCarrierStatus_Type()
)
begemotAtmIfCarrierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmIfCarrierStatus.setStatus("current")


class _BegemotAtmIfMode_Type(Integer32):
    """Custom type begemotAtmIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sonet", 1),
          ("sdh", 2),
          ("unknown", 3))
    )


_BegemotAtmIfMode_Type.__name__ = "Integer32"
_BegemotAtmIfMode_Object = MibTableColumn
begemotAtmIfMode = _BegemotAtmIfMode_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 10),
    _BegemotAtmIfMode_Type()
)
begemotAtmIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotAtmIfMode.setStatus("current")
_BegemotAtmIfTableLastChange_Type = TimeTicks
_BegemotAtmIfTableLastChange_Object = MibScalar
begemotAtmIfTableLastChange = _BegemotAtmIfTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 2),
    _BegemotAtmIfTableLastChange_Type()
)
begemotAtmIfTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmIfTableLastChange.setStatus("current")
_BegemotAtmHWTable_Object = MibTable
begemotAtmHWTable = _BegemotAtmHWTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3)
)
if mibBuilder.loadTexts:
    begemotAtmHWTable.setStatus("current")
_BegemotAtmHWEntry_Object = MibTableRow
begemotAtmHWEntry = _BegemotAtmHWEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1)
)
if mibBuilder.loadTexts:
    begemotAtmHWEntry.setStatus("current")
_BegemotAtmHWVendor_Type = DisplayString
_BegemotAtmHWVendor_Object = MibTableColumn
begemotAtmHWVendor = _BegemotAtmHWVendor_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 1),
    _BegemotAtmHWVendor_Type()
)
begemotAtmHWVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmHWVendor.setStatus("current")
_BegemotAtmHWDevice_Type = DisplayString
_BegemotAtmHWDevice_Object = MibTableColumn
begemotAtmHWDevice = _BegemotAtmHWDevice_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 2),
    _BegemotAtmHWDevice_Type()
)
begemotAtmHWDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmHWDevice.setStatus("current")
_BegemotAtmHWSerial_Type = Unsigned32
_BegemotAtmHWSerial_Object = MibTableColumn
begemotAtmHWSerial = _BegemotAtmHWSerial_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 3),
    _BegemotAtmHWSerial_Type()
)
begemotAtmHWSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmHWSerial.setStatus("current")
_BegemotAtmHWVersion_Type = Unsigned32
_BegemotAtmHWVersion_Object = MibTableColumn
begemotAtmHWVersion = _BegemotAtmHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 4),
    _BegemotAtmHWVersion_Type()
)
begemotAtmHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmHWVersion.setStatus("current")
_BegemotAtmHWSoftVersion_Type = Unsigned32
_BegemotAtmHWSoftVersion_Object = MibTableColumn
begemotAtmHWSoftVersion = _BegemotAtmHWSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 5),
    _BegemotAtmHWSoftVersion_Type()
)
begemotAtmHWSoftVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmHWSoftVersion.setStatus("current")
_BegemotAtmSysGroup_ObjectIdentity = ObjectIdentity
begemotAtmSysGroup = _BegemotAtmSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4)
)
begemotAtmIfEntry.registerAugmentions(
    ("BEGEMOT-ATM-MIB",
     "begemotAtmHWEntry")
)
begemotAtmHWEntry.setIndexNames(*begemotAtmIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BEGEMOT-ATM-MIB",
    **{"AtmESI": AtmESI,
       "begemotAtm": begemotAtm,
       "begemotAtmObjects": begemotAtmObjects,
       "begemotAtmIfTable": begemotAtmIfTable,
       "begemotAtmIfEntry": begemotAtmIfEntry,
       "begemotAtmIfName": begemotAtmIfName,
       "begemotAtmIfPcr": begemotAtmIfPcr,
       "begemotAtmIfMedia": begemotAtmIfMedia,
       "begemotAtmIfVpiBits": begemotAtmIfVpiBits,
       "begemotAtmIfVciBits": begemotAtmIfVciBits,
       "begemotAtmIfMaxVpcs": begemotAtmIfMaxVpcs,
       "begemotAtmIfMaxVccs": begemotAtmIfMaxVccs,
       "begemotAtmIfEsi": begemotAtmIfEsi,
       "begemotAtmIfCarrierStatus": begemotAtmIfCarrierStatus,
       "begemotAtmIfMode": begemotAtmIfMode,
       "begemotAtmIfTableLastChange": begemotAtmIfTableLastChange,
       "begemotAtmHWTable": begemotAtmHWTable,
       "begemotAtmHWEntry": begemotAtmHWEntry,
       "begemotAtmHWVendor": begemotAtmHWVendor,
       "begemotAtmHWDevice": begemotAtmHWDevice,
       "begemotAtmHWSerial": begemotAtmHWSerial,
       "begemotAtmHWVersion": begemotAtmHWVersion,
       "begemotAtmHWSoftVersion": begemotAtmHWSoftVersion,
       "begemotAtmSysGroup": begemotAtmSysGroup}
)
