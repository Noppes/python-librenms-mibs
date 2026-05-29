# SNMP MIB module (ARRIS-D5-DVB-PSIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\d5\ARRIS-D5-DVB-PSIG-MIB

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

d5DvbCasPsigMuxMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_D5DvbCasPsigMuxObjects_ObjectIdentity = ObjectIdentity
d5DvbCasPsigMuxObjects = _D5DvbCasPsigMuxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1)
)
_D5DvbCasPsigTable_Object = MibTable
d5DvbCasPsigTable = _D5DvbCasPsigTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    d5DvbCasPsigTable.setStatus("current")
_D5DvbCasPsigEntry_Object = MibTableRow
d5DvbCasPsigEntry = _D5DvbCasPsigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 1, 1)
)
d5DvbCasPsigEntry.setIndexNames(
    (0, "ARRIS-D5-DVB-PSIG-MIB", "d5PsigName"),
)
if mibBuilder.loadTexts:
    d5DvbCasPsigEntry.setStatus("current")
_D5PsigName_Type = DisplayString
_D5PsigName_Object = MibTableColumn
d5PsigName = _D5PsigName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 1, 1, 1),
    _D5PsigName_Type()
)
d5PsigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    d5PsigName.setStatus("current")
_D5PsigTcpPort_Type = Unsigned32
_D5PsigTcpPort_Object = MibTableColumn
d5PsigTcpPort = _D5PsigTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 1, 1, 2),
    _D5PsigTcpPort_Type()
)
d5PsigTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    d5PsigTcpPort.setStatus("current")
_D5PsigSrcIp_Type = IpAddress
_D5PsigSrcIp_Object = MibTableColumn
d5PsigSrcIp = _D5PsigSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 1, 1, 3),
    _D5PsigSrcIp_Type()
)
d5PsigSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    d5PsigSrcIp.setStatus("current")
_D5PsigRowStatus_Type = RowStatus
_D5PsigRowStatus_Object = MibTableColumn
d5PsigRowStatus = _D5PsigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 1, 1, 4),
    _D5PsigRowStatus_Type()
)
d5PsigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    d5PsigRowStatus.setStatus("current")
_D5PsigSessionNum_Type = Unsigned32
_D5PsigSessionNum_Object = MibTableColumn
d5PsigSessionNum = _D5PsigSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 1, 1, 5),
    _D5PsigSessionNum_Type()
)
d5PsigSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigSessionNum.setStatus("current")
_D5PsigNumChannels_Type = Unsigned32
_D5PsigNumChannels_Object = MibTableColumn
d5PsigNumChannels = _D5PsigNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 1, 1, 6),
    _D5PsigNumChannels_Type()
)
d5PsigNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigNumChannels.setStatus("current")
_D5PsigNumStreams_Type = Unsigned32
_D5PsigNumStreams_Object = MibTableColumn
d5PsigNumStreams = _D5PsigNumStreams_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 1, 1, 7),
    _D5PsigNumStreams_Type()
)
d5PsigNumStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigNumStreams.setStatus("current")
_D5PsigNumSections_Type = Unsigned32
_D5PsigNumSections_Object = MibTableColumn
d5PsigNumSections = _D5PsigNumSections_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 1, 1, 8),
    _D5PsigNumSections_Type()
)
d5PsigNumSections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigNumSections.setStatus("current")
_D5DvbCasPsigChannelTable_Object = MibTable
d5DvbCasPsigChannelTable = _D5DvbCasPsigChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    d5DvbCasPsigChannelTable.setStatus("current")
_D5DvbCasPsigChannel_Object = MibTableRow
d5DvbCasPsigChannel = _D5DvbCasPsigChannel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 2, 1)
)
d5DvbCasPsigChannel.setIndexNames(
    (0, "ARRIS-D5-DVB-PSIG-MIB", "d5PsigChanPsigName"),
    (0, "ARRIS-D5-DVB-PSIG-MIB", "d5PsigChanChannelId"),
)
if mibBuilder.loadTexts:
    d5DvbCasPsigChannel.setStatus("current")
_D5PsigChanPsigName_Type = DisplayString
_D5PsigChanPsigName_Object = MibTableColumn
d5PsigChanPsigName = _D5PsigChanPsigName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 2, 1, 1),
    _D5PsigChanPsigName_Type()
)
d5PsigChanPsigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigChanPsigName.setStatus("current")


class _D5PsigChanChannelId_Type(Unsigned32):
    """Custom type d5PsigChanChannelId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5PsigChanChannelId_Type.__name__ = "Unsigned32"
_D5PsigChanChannelId_Object = MibTableColumn
d5PsigChanChannelId = _D5PsigChanChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 2, 1, 2),
    _D5PsigChanChannelId_Type()
)
d5PsigChanChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigChanChannelId.setStatus("current")


class _D5PsigChanNetworkId_Type(Unsigned32):
    """Custom type d5PsigChanNetworkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5PsigChanNetworkId_Type.__name__ = "Unsigned32"
_D5PsigChanNetworkId_Object = MibTableColumn
d5PsigChanNetworkId = _D5PsigChanNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 2, 1, 3),
    _D5PsigChanNetworkId_Type()
)
d5PsigChanNetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigChanNetworkId.setStatus("current")


class _D5PsigChanTsId_Type(Unsigned32):
    """Custom type d5PsigChanTsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5PsigChanTsId_Type.__name__ = "Unsigned32"
_D5PsigChanTsId_Object = MibTableColumn
d5PsigChanTsId = _D5PsigChanTsId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 2, 1, 4),
    _D5PsigChanTsId_Type()
)
d5PsigChanTsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigChanTsId.setStatus("current")


class _D5PsigChanTcpPort_Type(Unsigned32):
    """Custom type d5PsigChanTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5PsigChanTcpPort_Type.__name__ = "Unsigned32"
_D5PsigChanTcpPort_Object = MibTableColumn
d5PsigChanTcpPort = _D5PsigChanTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 2, 1, 5),
    _D5PsigChanTcpPort_Type()
)
d5PsigChanTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigChanTcpPort.setStatus("current")
_D5PsigChanNumStreams_Type = Unsigned32
_D5PsigChanNumStreams_Object = MibTableColumn
d5PsigChanNumStreams = _D5PsigChanNumStreams_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 2, 1, 6),
    _D5PsigChanNumStreams_Type()
)
d5PsigChanNumStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigChanNumStreams.setStatus("current")
_D5DvbCasPsigStreamTable_Object = MibTable
d5DvbCasPsigStreamTable = _D5DvbCasPsigStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    d5DvbCasPsigStreamTable.setStatus("current")
_D5DvbCasPsigStream_Object = MibTableRow
d5DvbCasPsigStream = _D5DvbCasPsigStream_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 3, 1)
)
d5DvbCasPsigStream.setIndexNames(
    (0, "ARRIS-D5-DVB-PSIG-MIB", "d5PsigStrPsigName"),
    (0, "ARRIS-D5-DVB-PSIG-MIB", "d5PsigStrChannelId"),
    (0, "ARRIS-D5-DVB-PSIG-MIB", "d5PsigStrPid"),
)
if mibBuilder.loadTexts:
    d5DvbCasPsigStream.setStatus("current")
_D5PsigStrPsigName_Type = DisplayString
_D5PsigStrPsigName_Object = MibTableColumn
d5PsigStrPsigName = _D5PsigStrPsigName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 3, 1, 1),
    _D5PsigStrPsigName_Type()
)
d5PsigStrPsigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigStrPsigName.setStatus("current")


class _D5PsigStrChannelId_Type(Unsigned32):
    """Custom type d5PsigStrChannelId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5PsigStrChannelId_Type.__name__ = "Unsigned32"
_D5PsigStrChannelId_Object = MibTableColumn
d5PsigStrChannelId = _D5PsigStrChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 3, 1, 2),
    _D5PsigStrChannelId_Type()
)
d5PsigStrChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigStrChannelId.setStatus("current")


class _D5PsigStrPid_Type(Unsigned32):
    """Custom type d5PsigStrPid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5PsigStrPid_Type.__name__ = "Unsigned32"
_D5PsigStrPid_Object = MibTableColumn
d5PsigStrPid = _D5PsigStrPid_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 3, 1, 3),
    _D5PsigStrPid_Type()
)
d5PsigStrPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigStrPid.setStatus("current")


class _D5PsigStrStreamId_Type(Unsigned32):
    """Custom type d5PsigStrStreamId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5PsigStrStreamId_Type.__name__ = "Unsigned32"
_D5PsigStrStreamId_Object = MibTableColumn
d5PsigStrStreamId = _D5PsigStrStreamId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 3, 1, 4),
    _D5PsigStrStreamId_Type()
)
d5PsigStrStreamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigStrStreamId.setStatus("current")


class _D5PsigStrNetworkId_Type(Unsigned32):
    """Custom type d5PsigStrNetworkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5PsigStrNetworkId_Type.__name__ = "Unsigned32"
_D5PsigStrNetworkId_Object = MibTableColumn
d5PsigStrNetworkId = _D5PsigStrNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 3, 1, 5),
    _D5PsigStrNetworkId_Type()
)
d5PsigStrNetworkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigStrNetworkId.setStatus("current")


class _D5PsigStrTsId_Type(Unsigned32):
    """Custom type d5PsigStrTsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5PsigStrTsId_Type.__name__ = "Unsigned32"
_D5PsigStrTsId_Object = MibTableColumn
d5PsigStrTsId = _D5PsigStrTsId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 3, 1, 6),
    _D5PsigStrTsId_Type()
)
d5PsigStrTsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigStrTsId.setStatus("current")


class _D5PsigStrTcpPort_Type(Unsigned32):
    """Custom type d5PsigStrTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_D5PsigStrTcpPort_Type.__name__ = "Unsigned32"
_D5PsigStrTcpPort_Object = MibTableColumn
d5PsigStrTcpPort = _D5PsigStrTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 3, 1, 7),
    _D5PsigStrTcpPort_Type()
)
d5PsigStrTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigStrTcpPort.setStatus("current")
_D5PsigStrNumSections_Type = Unsigned32
_D5PsigStrNumSections_Object = MibTableColumn
d5PsigStrNumSections = _D5PsigStrNumSections_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 3, 1, 8),
    _D5PsigStrNumSections_Type()
)
d5PsigStrNumSections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5PsigStrNumSections.setStatus("current")
_D5DvbCasPsigGlobalConfigObjects_ObjectIdentity = ObjectIdentity
d5DvbCasPsigGlobalConfigObjects = _D5DvbCasPsigGlobalConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 4)
)
_D5DvbCasPsigGlobalConfigGroup_ObjectIdentity = ObjectIdentity
d5DvbCasPsigGlobalConfigGroup = _D5DvbCasPsigGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 4, 1)
)
_D5DvbCasPsigMaxChannels_Type = Unsigned32
_D5DvbCasPsigMaxChannels_Object = MibScalar
d5DvbCasPsigMaxChannels = _D5DvbCasPsigMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 4, 1, 1),
    _D5DvbCasPsigMaxChannels_Type()
)
d5DvbCasPsigMaxChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5DvbCasPsigMaxChannels.setStatus("current")
_D5DvbCasPsigMaxStreams_Type = Unsigned32
_D5DvbCasPsigMaxStreams_Object = MibScalar
d5DvbCasPsigMaxStreams = _D5DvbCasPsigMaxStreams_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 4, 1, 2),
    _D5DvbCasPsigMaxStreams_Type()
)
d5DvbCasPsigMaxStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5DvbCasPsigMaxStreams.setStatus("current")
_D5DvbCasPsigMaxSections_Type = Unsigned32
_D5DvbCasPsigMaxSections_Object = MibScalar
d5DvbCasPsigMaxSections = _D5DvbCasPsigMaxSections_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 9, 1, 4, 1, 3),
    _D5DvbCasPsigMaxSections_Type()
)
d5DvbCasPsigMaxSections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5DvbCasPsigMaxSections.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-D5-DVB-PSIG-MIB",
    **{"d5DvbCasPsigMuxMib": d5DvbCasPsigMuxMib,
       "d5DvbCasPsigMuxObjects": d5DvbCasPsigMuxObjects,
       "d5DvbCasPsigTable": d5DvbCasPsigTable,
       "d5DvbCasPsigEntry": d5DvbCasPsigEntry,
       "d5PsigName": d5PsigName,
       "d5PsigTcpPort": d5PsigTcpPort,
       "d5PsigSrcIp": d5PsigSrcIp,
       "d5PsigRowStatus": d5PsigRowStatus,
       "d5PsigSessionNum": d5PsigSessionNum,
       "d5PsigNumChannels": d5PsigNumChannels,
       "d5PsigNumStreams": d5PsigNumStreams,
       "d5PsigNumSections": d5PsigNumSections,
       "d5DvbCasPsigChannelTable": d5DvbCasPsigChannelTable,
       "d5DvbCasPsigChannel": d5DvbCasPsigChannel,
       "d5PsigChanPsigName": d5PsigChanPsigName,
       "d5PsigChanChannelId": d5PsigChanChannelId,
       "d5PsigChanNetworkId": d5PsigChanNetworkId,
       "d5PsigChanTsId": d5PsigChanTsId,
       "d5PsigChanTcpPort": d5PsigChanTcpPort,
       "d5PsigChanNumStreams": d5PsigChanNumStreams,
       "d5DvbCasPsigStreamTable": d5DvbCasPsigStreamTable,
       "d5DvbCasPsigStream": d5DvbCasPsigStream,
       "d5PsigStrPsigName": d5PsigStrPsigName,
       "d5PsigStrChannelId": d5PsigStrChannelId,
       "d5PsigStrPid": d5PsigStrPid,
       "d5PsigStrStreamId": d5PsigStrStreamId,
       "d5PsigStrNetworkId": d5PsigStrNetworkId,
       "d5PsigStrTsId": d5PsigStrTsId,
       "d5PsigStrTcpPort": d5PsigStrTcpPort,
       "d5PsigStrNumSections": d5PsigStrNumSections,
       "d5DvbCasPsigGlobalConfigObjects": d5DvbCasPsigGlobalConfigObjects,
       "d5DvbCasPsigGlobalConfigGroup": d5DvbCasPsigGlobalConfigGroup,
       "d5DvbCasPsigMaxChannels": d5DvbCasPsigMaxChannels,
       "d5DvbCasPsigMaxStreams": d5DvbCasPsigMaxStreams,
       "d5DvbCasPsigMaxSections": d5DvbCasPsigMaxSections}
)
