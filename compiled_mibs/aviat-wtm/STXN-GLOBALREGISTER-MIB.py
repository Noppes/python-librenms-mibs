# SNMP MIB module (STXN-GLOBALREGISTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\aviat-wtm\STXN-GLOBALREGISTER-MIB

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

stxnGlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 6, 1)
)
if mibBuilder.loadTexts:
    stxnGlobalRegModule.setRevisions(
        ("2014-01-21 03:58",
         "2011-11-28 00:07",
         "2011-03-14 01:19",
         "2009-07-23 04:15",
         "2009-04-16 23:58",
         "2004-02-20 00:55",
         "2003-01-29 03:31",
         "2002-11-28 23:58",
         "2002-10-08 19:35",
         "2002-09-03 23:15",
         "2001-11-15 01:10",
         "2001-03-14 20:41",
         "2001-02-13 20:21")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dmc_ObjectIdentity = ObjectIdentity
dmc = _Dmc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509)
)
if mibBuilder.loadTexts:
    dmc.setStatus("current")
_DmcNet_ObjectIdentity = ObjectIdentity
dmcNet = _DmcNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 1)
)
if mibBuilder.loadTexts:
    dmcNet.setStatus("current")
_ProxyAgent_ObjectIdentity = ObjectIdentity
proxyAgent = _ProxyAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 1, 1)
)
if mibBuilder.loadTexts:
    proxyAgent.setStatus("current")
_NonsnmpRadio_ObjectIdentity = ObjectIdentity
nonsnmpRadio = _NonsnmpRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 1, 2)
)
if mibBuilder.loadTexts:
    nonsnmpRadio.setStatus("current")
_SnmpRadio_ObjectIdentity = ObjectIdentity
snmpRadio = _SnmpRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 1, 3)
)
if mibBuilder.loadTexts:
    snmpRadio.setStatus("current")
_Sp2Radio_ObjectIdentity = ObjectIdentity
sp2Radio = _Sp2Radio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sp2Radio.setStatus("current")
_Altium_ObjectIdentity = ObjectIdentity
altium = _Altium_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 1, 3, 2)
)
if mibBuilder.loadTexts:
    altium.setStatus("current")
_DmcEvents_ObjectIdentity = ObjectIdentity
dmcEvents = _DmcEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 1, 4)
)
if mibBuilder.loadTexts:
    dmcEvents.setStatus("current")
_DmcSecurity_ObjectIdentity = ObjectIdentity
dmcSecurity = _DmcSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 1, 5)
)
if mibBuilder.loadTexts:
    dmcSecurity.setStatus("current")
_DmcModules_ObjectIdentity = ObjectIdentity
dmcModules = _DmcModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 2)
)
if mibBuilder.loadTexts:
    dmcModules.setStatus("current")
_StxnEngineering_ObjectIdentity = ObjectIdentity
stxnEngineering = _StxnEngineering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 4)
)
if mibBuilder.loadTexts:
    stxnEngineering.setStatus("current")
_StxnProducts_ObjectIdentity = ObjectIdentity
stxnProducts = _StxnProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 5)
)
if mibBuilder.loadTexts:
    stxnProducts.setStatus("current")
_StxnLMCDR_ObjectIdentity = ObjectIdentity
stxnLMCDR = _StxnLMCDR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 5, 1)
)
if mibBuilder.loadTexts:
    stxnLMCDR.setStatus("current")
_StxnAOU_ObjectIdentity = ObjectIdentity
stxnAOU = _StxnAOU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 5, 2)
)
if mibBuilder.loadTexts:
    stxnAOU.setStatus("current")
_StxnCTU_ObjectIdentity = ObjectIdentity
stxnCTU = _StxnCTU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 5, 3)
)
if mibBuilder.loadTexts:
    stxnCTU.setStatus("current")
_StxnUNITY_ObjectIdentity = ObjectIdentity
stxnUNITY = _StxnUNITY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 5, 4)
)
if mibBuilder.loadTexts:
    stxnUNITY.setStatus("current")
_StxnProVision_ObjectIdentity = ObjectIdentity
stxnProVision = _StxnProVision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 5, 5)
)
if mibBuilder.loadTexts:
    stxnProVision.setStatus("current")
_StxnEfficientSite_ObjectIdentity = ObjectIdentity
stxnEfficientSite = _StxnEfficientSite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 5, 6)
)
if mibBuilder.loadTexts:
    stxnEfficientSite.setStatus("current")
_StxnEfficientSiteControllerUnit_ObjectIdentity = ObjectIdentity
stxnEfficientSiteControllerUnit = _StxnEfficientSiteControllerUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 5, 6, 1)
)
if mibBuilder.loadTexts:
    stxnEfficientSiteControllerUnit.setStatus("current")
_StxnProductOIDs_ObjectIdentity = ObjectIdentity
stxnProductOIDs = _StxnProductOIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 5, 10)
)
if mibBuilder.loadTexts:
    stxnProductOIDs.setStatus("current")
_StxnModules_ObjectIdentity = ObjectIdentity
stxnModules = _StxnModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 6)
)
if mibBuilder.loadTexts:
    stxnModules.setStatus("current")
_StxnEvents_ObjectIdentity = ObjectIdentity
stxnEvents = _StxnEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 7)
)
if mibBuilder.loadTexts:
    stxnEvents.setStatus("current")
_StxnOvationEvents_ObjectIdentity = ObjectIdentity
stxnOvationEvents = _StxnOvationEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 7, 1)
)
if mibBuilder.loadTexts:
    stxnOvationEvents.setStatus("current")
_StxnUnityAOUEvents_ObjectIdentity = ObjectIdentity
stxnUnityAOUEvents = _StxnUnityAOUEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 7, 2)
)
if mibBuilder.loadTexts:
    stxnUnityAOUEvents.setStatus("current")
_StxnUnityCTUEvents_ObjectIdentity = ObjectIdentity
stxnUnityCTUEvents = _StxnUnityCTUEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 7, 3)
)
if mibBuilder.loadTexts:
    stxnUnityCTUEvents.setStatus("current")
_StxnUnityIDUEvents_ObjectIdentity = ObjectIdentity
stxnUnityIDUEvents = _StxnUnityIDUEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 7, 4)
)
if mibBuilder.loadTexts:
    stxnUnityIDUEvents.setStatus("current")
_StxnEfficientSiteEvents_ObjectIdentity = ObjectIdentity
stxnEfficientSiteEvents = _StxnEfficientSiteEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 7, 5)
)
if mibBuilder.loadTexts:
    stxnEfficientSiteEvents.setStatus("current")
_StxnGeneric_ObjectIdentity = ObjectIdentity
stxnGeneric = _StxnGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 8)
)
if mibBuilder.loadTexts:
    stxnGeneric.setStatus("current")
_AviatModules_ObjectIdentity = ObjectIdentity
aviatModules = _AviatModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9)
)
if mibBuilder.loadTexts:
    aviatModules.setStatus("current")
_AviatAfModules_ObjectIdentity = ObjectIdentity
aviatAfModules = _AviatAfModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 1000)
)
if mibBuilder.loadTexts:
    aviatAfModules.setStatus("current")
_AviatAaModules_ObjectIdentity = ObjectIdentity
aviatAaModules = _AviatAaModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 1001)
)
if mibBuilder.loadTexts:
    aviatAaModules.setStatus("current")
_AviatAlModules_ObjectIdentity = ObjectIdentity
aviatAlModules = _AviatAlModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 1002)
)
if mibBuilder.loadTexts:
    aviatAlModules.setStatus("current")
_AviatAmModules_ObjectIdentity = ObjectIdentity
aviatAmModules = _AviatAmModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 1003)
)
if mibBuilder.loadTexts:
    aviatAmModules.setStatus("current")
_AviatEvents_ObjectIdentity = ObjectIdentity
aviatEvents = _AviatEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 10)
)
if mibBuilder.loadTexts:
    aviatEvents.setStatus("current")
_AviatProducts_ObjectIdentity = ObjectIdentity
aviatProducts = _AviatProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 11)
)
if mibBuilder.loadTexts:
    aviatProducts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STXN-GLOBALREGISTER-MIB",
    **{"dmc": dmc,
       "dmcNet": dmcNet,
       "proxyAgent": proxyAgent,
       "nonsnmpRadio": nonsnmpRadio,
       "snmpRadio": snmpRadio,
       "sp2Radio": sp2Radio,
       "altium": altium,
       "dmcEvents": dmcEvents,
       "dmcSecurity": dmcSecurity,
       "dmcModules": dmcModules,
       "stxnEngineering": stxnEngineering,
       "stxnProducts": stxnProducts,
       "stxnLMCDR": stxnLMCDR,
       "stxnAOU": stxnAOU,
       "stxnCTU": stxnCTU,
       "stxnUNITY": stxnUNITY,
       "stxnProVision": stxnProVision,
       "stxnEfficientSite": stxnEfficientSite,
       "stxnEfficientSiteControllerUnit": stxnEfficientSiteControllerUnit,
       "stxnProductOIDs": stxnProductOIDs,
       "stxnModules": stxnModules,
       "stxnGlobalRegModule": stxnGlobalRegModule,
       "stxnEvents": stxnEvents,
       "stxnOvationEvents": stxnOvationEvents,
       "stxnUnityAOUEvents": stxnUnityAOUEvents,
       "stxnUnityCTUEvents": stxnUnityCTUEvents,
       "stxnUnityIDUEvents": stxnUnityIDUEvents,
       "stxnEfficientSiteEvents": stxnEfficientSiteEvents,
       "stxnGeneric": stxnGeneric,
       "aviatModules": aviatModules,
       "aviatAfModules": aviatAfModules,
       "aviatAaModules": aviatAaModules,
       "aviatAlModules": aviatAlModules,
       "aviatAmModules": aviatAmModules,
       "aviatEvents": aviatEvents,
       "aviatProducts": aviatProducts}
)
