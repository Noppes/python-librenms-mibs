# SNMP MIB module (VMW-TUNNEL-SERVER-AGENTCAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMW-TUNNEL-SERVER-AGENTCAP-MIB

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

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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

(vmwareAgentCapabilities,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwareAgentCapabilities")


# MODULE-IDENTITY

vmwTunnelServerAgentCapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70, 28)
)
if mibBuilder.loadTexts:
    vmwTunnelServerAgentCapMIB.setRevisions(
        ("2022-10-28 00:00",
         "2020-07-21 00:00",
         "2019-10-30 00:00",
         "2018-09-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwTunnelServerCapability_ObjectIdentity = ObjectIdentity
vmwTunnelServerCapability = _VmwTunnelServerCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70, 28, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

vmwTunnelServer2018_400 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 28, 1, 1)
)
if mibBuilder.loadTexts:
    vmwTunnelServer2018_400.setProductRelease("4.0.0")
if mibBuilder.loadTexts:
    vmwTunnelServer2018_400.setStatus(
        "current"
    )

vmwTunnelServer2019_420 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 28, 1, 2)
)
if mibBuilder.loadTexts:
    vmwTunnelServer2019_420.setProductRelease("4.2.0")
if mibBuilder.loadTexts:
    vmwTunnelServer2019_420.setStatus(
        "current"
    )

vmwTunnelServer2020_200900 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 28, 1, 3)
)
if mibBuilder.loadTexts:
    vmwTunnelServer2020_200900.setProductRelease("20.09.00")
if mibBuilder.loadTexts:
    vmwTunnelServer2020_200900.setStatus(
        "current"
    )

vmwTunnelServer2022_221200 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 28, 1, 4)
)
if mibBuilder.loadTexts:
    vmwTunnelServer2022_221200.setProductRelease("22.12.00")
if mibBuilder.loadTexts:
    vmwTunnelServer2022_221200.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMW-TUNNEL-SERVER-AGENTCAP-MIB",
    **{"vmwTunnelServerAgentCapMIB": vmwTunnelServerAgentCapMIB,
       "vmwTunnelServerCapability": vmwTunnelServerCapability,
       "vmwTunnelServer2018-400": vmwTunnelServer2018_400,
       "vmwTunnelServer2019-420": vmwTunnelServer2019_420,
       "vmwTunnelServer2020-200900": vmwTunnelServer2020_200900,
       "vmwTunnelServer2022-221200": vmwTunnelServer2022_221200}
)
