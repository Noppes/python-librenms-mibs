# SNMP MIB module (AVIAT-TEXTCONVENTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\aviat-wtm\AVIAT-TEXTCONVENTION-MIB

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(aviatModules,) = mibBuilder.importSymbols(
    "STXN-GLOBALREGISTER-MIB",
    "aviatModules")


# MODULE-IDENTITY

aviatTextConventionModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 1)
)
if mibBuilder.loadTexts:
    aviatTextConventionModule.setRevisions(
        ("2017-03-28 23:39",
         "2015-07-29 08:45",
         "2015-01-05 09:10",
         "2014-08-26 23:29",
         "2014-01-21 01:57")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AviatFunctionTimer(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )



class AviatModulationType(TextualConvention, Integer32):
    status = "current"
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("modulationNone", 1),
          ("modulationQpsk", 2),
          ("modulation16qam", 3),
          ("modulation32qam", 4),
          ("modulation64qam", 5),
          ("modulation128qam", 6),
          ("modulation256qam", 7),
          ("modulation512qam", 8),
          ("modulation1024qam", 9),
          ("modulation256qamHG", 10),
          ("modulation512qamHG", 11),
          ("modulation1024qamHG", 12),
          ("modulation2048qam", 13),
          ("modulation4096qam", 14))
    )



class AviatPowerLevel(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class AviatDecibel(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class AviatProtectionType(TextualConvention, Integer32):
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
        *(("nonProtected", 1),
          ("hotStandby", 2),
          ("spaceDiversity", 3),
          ("frequencyDiversity", 4),
          ("monitoredHotStandby", 5))
    )



class AviatPluginModuleType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              41,
              61,
              62,
              81,
              82)
        )
    )
    namedValues = NamedValues(
        *(("pluginModuleNone", 1),
          ("pluginModuleUnsupported", 2),
          ("pluginModulePOEx2", 41),
          ("pluginModulePWR", 61),
          ("pluginModulePWRAUX", 62),
          ("pluginModuleRACx1", 81),
          ("pluginModuleRACx2", 82))
    )



class AviatLoggingProtocolType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protocolUdp", 1),
          ("protocolTcp", 2),
          ("protocolTls", 3))
    )



class AviatTimeOfDay(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d:1d:1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class AviatEnabledStatus(TextualConvention, Integer32):
    status = "current"
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



class AviatTableIndexInteger(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class AviatL1LinkAggregationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l1la", 1),
          ("pla", 2))
    )



class AviatRfuSideBandType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highBand", 1),
          ("lowBand", 2),
          ("fullBand", 3))
    )



class AviatYangIdentityRef(TextualConvention, OctetString):
    status = "current"
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVIAT-TEXTCONVENTION-MIB",
    **{"AviatFunctionTimer": AviatFunctionTimer,
       "AviatModulationType": AviatModulationType,
       "AviatPowerLevel": AviatPowerLevel,
       "AviatDecibel": AviatDecibel,
       "AviatProtectionType": AviatProtectionType,
       "AviatPluginModuleType": AviatPluginModuleType,
       "AviatLoggingProtocolType": AviatLoggingProtocolType,
       "AviatTimeOfDay": AviatTimeOfDay,
       "AviatEnabledStatus": AviatEnabledStatus,
       "AviatTableIndexInteger": AviatTableIndexInteger,
       "AviatL1LinkAggregationType": AviatL1LinkAggregationType,
       "AviatRfuSideBandType": AviatRfuSideBandType,
       "AviatYangIdentityRef": AviatYangIdentityRef,
       "aviatTextConventionModule": aviatTextConventionModule}
)
