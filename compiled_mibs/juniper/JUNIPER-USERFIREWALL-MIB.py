# SNMP MIB module (JUNIPER-USERFIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\juniper\junos\JUNIPER-USERFIREWALL-MIB

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

(jnxUserFirewallsRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxUserFirewallsRoot")

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

jnxUserFirewalls = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1)
)
if mibBuilder.loadTexts:
    jnxUserFirewalls.setRevisions(
        ("2019-09-26 15:53",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxUserFwTable_ObjectIdentity = ObjectIdentity
jnxUserFwTable = _JnxUserFwTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1)
)
_JnxUserFwDomainAuthTable_Object = MibTable
jnxUserFwDomainAuthTable = _JnxUserFwDomainAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxUserFwDomainAuthTable.setStatus("current")
_JnxUserFwDomainAuthEntry_Object = MibTableRow
jnxUserFwDomainAuthEntry = _JnxUserFwDomainAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 1, 1)
)
jnxUserFwDomainAuthEntry.setIndexNames(
    (0, "JUNIPER-USERFIREWALL-MIB", "jnxUserFwDomain"),
)
if mibBuilder.loadTexts:
    jnxUserFwDomainAuthEntry.setStatus("current")
_JnxUserFwDomain_Type = DisplayString
_JnxUserFwDomain_Object = MibTableColumn
jnxUserFwDomain = _JnxUserFwDomain_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 1, 1, 1),
    _JnxUserFwDomain_Type()
)
jnxUserFwDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwDomain.setStatus("current")
_JnxUserFwAuthCPCounter_Type = Unsigned32
_JnxUserFwAuthCPCounter_Object = MibTableColumn
jnxUserFwAuthCPCounter = _JnxUserFwAuthCPCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 1, 1, 2),
    _JnxUserFwAuthCPCounter_Type()
)
jnxUserFwAuthCPCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwAuthCPCounter.setStatus("current")
_JnxUserFwAuthJIMSCounter_Type = Unsigned32
_JnxUserFwAuthJIMSCounter_Object = MibTableColumn
jnxUserFwAuthJIMSCounter = _JnxUserFwAuthJIMSCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 1, 1, 3),
    _JnxUserFwAuthJIMSCounter_Type()
)
jnxUserFwAuthJIMSCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwAuthJIMSCounter.setStatus("current")
_JnxUserFwAuthValidCounter_Type = Unsigned32
_JnxUserFwAuthValidCounter_Object = MibTableColumn
jnxUserFwAuthValidCounter = _JnxUserFwAuthValidCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 1, 1, 4),
    _JnxUserFwAuthValidCounter_Type()
)
jnxUserFwAuthValidCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwAuthValidCounter.setStatus("current")
_JnxUserFwAuthPendingCounter_Type = Unsigned32
_JnxUserFwAuthPendingCounter_Object = MibTableColumn
jnxUserFwAuthPendingCounter = _JnxUserFwAuthPendingCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 1, 1, 5),
    _JnxUserFwAuthPendingCounter_Type()
)
jnxUserFwAuthPendingCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwAuthPendingCounter.setStatus("current")
_JnxUserFwAuthInvalidCounter_Type = Unsigned32
_JnxUserFwAuthInvalidCounter_Object = MibTableColumn
jnxUserFwAuthInvalidCounter = _JnxUserFwAuthInvalidCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 1, 1, 6),
    _JnxUserFwAuthInvalidCounter_Type()
)
jnxUserFwAuthInvalidCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwAuthInvalidCounter.setStatus("current")
_JnxUserFwAuthTotalCounter_Type = Unsigned32
_JnxUserFwAuthTotalCounter_Object = MibTableColumn
jnxUserFwAuthTotalCounter = _JnxUserFwAuthTotalCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 1, 1, 7),
    _JnxUserFwAuthTotalCounter_Type()
)
jnxUserFwAuthTotalCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwAuthTotalCounter.setStatus("current")
_JnxUserFwAuthADCounter_Type = Unsigned32
_JnxUserFwAuthADCounter_Object = MibTableColumn
jnxUserFwAuthADCounter = _JnxUserFwAuthADCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 1, 1, 8),
    _JnxUserFwAuthADCounter_Type()
)
jnxUserFwAuthADCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwAuthADCounter.setStatus("current")
_JnxUserFwADDomCtlrTable_Object = MibTable
jnxUserFwADDomCtlrTable = _JnxUserFwADDomCtlrTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxUserFwADDomCtlrTable.setStatus("current")
_JnxUserFwADDomCtlrEntry_Object = MibTableRow
jnxUserFwADDomCtlrEntry = _JnxUserFwADDomCtlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 2, 1)
)
jnxUserFwADDomCtlrEntry.setIndexNames(
    (0, "JUNIPER-USERFIREWALL-MIB", "jnxUserFwADDomain"),
    (0, "JUNIPER-USERFIREWALL-MIB", "jnxUserFwADDomCtrlerAddr"),
)
if mibBuilder.loadTexts:
    jnxUserFwADDomCtlrEntry.setStatus("current")
_JnxUserFwADDomain_Type = DisplayString
_JnxUserFwADDomain_Object = MibTableColumn
jnxUserFwADDomain = _JnxUserFwADDomain_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 2, 1, 1),
    _JnxUserFwADDomain_Type()
)
jnxUserFwADDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwADDomain.setStatus("current")
_JnxUserFwADDomCtrlerAddr_Type = DisplayString
_JnxUserFwADDomCtrlerAddr_Object = MibTableColumn
jnxUserFwADDomCtrlerAddr = _JnxUserFwADDomCtrlerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 2, 1, 2),
    _JnxUserFwADDomCtrlerAddr_Type()
)
jnxUserFwADDomCtrlerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwADDomCtrlerAddr.setStatus("current")
_JnxUserFwADDomCtrlerName_Type = DisplayString
_JnxUserFwADDomCtrlerName_Object = MibTableColumn
jnxUserFwADDomCtrlerName = _JnxUserFwADDomCtrlerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 2, 1, 3),
    _JnxUserFwADDomCtrlerName_Type()
)
jnxUserFwADDomCtrlerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwADDomCtrlerName.setStatus("current")
_JnxUserFwADDomCtrlerConnStatus_Type = DisplayString
_JnxUserFwADDomCtrlerConnStatus_Object = MibTableColumn
jnxUserFwADDomCtrlerConnStatus = _JnxUserFwADDomCtrlerConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 2, 1, 4),
    _JnxUserFwADDomCtrlerConnStatus_Type()
)
jnxUserFwADDomCtrlerConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwADDomCtrlerConnStatus.setStatus("current")
_JnxUserFwADDomTotalLogQuery_Type = Unsigned32
_JnxUserFwADDomTotalLogQuery_Object = MibTableColumn
jnxUserFwADDomTotalLogQuery = _JnxUserFwADDomTotalLogQuery_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 2, 1, 5),
    _JnxUserFwADDomTotalLogQuery_Type()
)
jnxUserFwADDomTotalLogQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwADDomTotalLogQuery.setStatus("current")
_JnxUserFwADDomFailedLogQuery_Type = Unsigned32
_JnxUserFwADDomFailedLogQuery_Object = MibTableColumn
jnxUserFwADDomFailedLogQuery = _JnxUserFwADDomFailedLogQuery_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 2, 1, 6),
    _JnxUserFwADDomFailedLogQuery_Type()
)
jnxUserFwADDomFailedLogQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwADDomFailedLogQuery.setStatus("current")
_JnxUserFwADDomRecordsFetched_Type = Unsigned32
_JnxUserFwADDomRecordsFetched_Object = MibTableColumn
jnxUserFwADDomRecordsFetched = _JnxUserFwADDomRecordsFetched_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 2, 1, 7),
    _JnxUserFwADDomRecordsFetched_Type()
)
jnxUserFwADDomRecordsFetched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwADDomRecordsFetched.setStatus("current")
_JnxUserFwLDAPTable_Object = MibTable
jnxUserFwLDAPTable = _JnxUserFwLDAPTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxUserFwLDAPTable.setStatus("current")
_JnxUserFwLDAPEntry_Object = MibTableRow
jnxUserFwLDAPEntry = _JnxUserFwLDAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 3, 1)
)
jnxUserFwLDAPEntry.setIndexNames(
    (0, "JUNIPER-USERFIREWALL-MIB", "jnxUserFwLDAPDomain"),
    (0, "JUNIPER-USERFIREWALL-MIB", "jnxUserFwLDAPHost"),
)
if mibBuilder.loadTexts:
    jnxUserFwLDAPEntry.setStatus("current")
_JnxUserFwLDAPDomain_Type = DisplayString
_JnxUserFwLDAPDomain_Object = MibTableColumn
jnxUserFwLDAPDomain = _JnxUserFwLDAPDomain_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 3, 1, 1),
    _JnxUserFwLDAPDomain_Type()
)
jnxUserFwLDAPDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwLDAPDomain.setStatus("current")
_JnxUserFwLDAPHost_Type = DisplayString
_JnxUserFwLDAPHost_Object = MibTableColumn
jnxUserFwLDAPHost = _JnxUserFwLDAPHost_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 3, 1, 2),
    _JnxUserFwLDAPHost_Type()
)
jnxUserFwLDAPHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwLDAPHost.setStatus("current")
_JnxUserFwLDAPTotalQuery_Type = Unsigned32
_JnxUserFwLDAPTotalQuery_Object = MibTableColumn
jnxUserFwLDAPTotalQuery = _JnxUserFwLDAPTotalQuery_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 3, 1, 3),
    _JnxUserFwLDAPTotalQuery_Type()
)
jnxUserFwLDAPTotalQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwLDAPTotalQuery.setStatus("current")
_JnxUserFwLDAPFailedQuery_Type = Unsigned32
_JnxUserFwLDAPFailedQuery_Object = MibTableColumn
jnxUserFwLDAPFailedQuery = _JnxUserFwLDAPFailedQuery_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 3, 1, 4),
    _JnxUserFwLDAPFailedQuery_Type()
)
jnxUserFwLDAPFailedQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwLDAPFailedQuery.setStatus("current")
_JnxUserFwProbeTable_Object = MibTable
jnxUserFwProbeTable = _JnxUserFwProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxUserFwProbeTable.setStatus("current")
_JnxUserFwProbeEntry_Object = MibTableRow
jnxUserFwProbeEntry = _JnxUserFwProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 4, 1)
)
jnxUserFwProbeEntry.setIndexNames(
    (0, "JUNIPER-USERFIREWALL-MIB", "jnxUserFwDomainName"),
)
if mibBuilder.loadTexts:
    jnxUserFwProbeEntry.setStatus("current")
_JnxUserFwDomainName_Type = DisplayString
_JnxUserFwDomainName_Object = MibTableColumn
jnxUserFwDomainName = _JnxUserFwDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 4, 1, 1),
    _JnxUserFwDomainName_Type()
)
jnxUserFwDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwDomainName.setStatus("current")
_JnxUserFwTotalUserProbeNum_Type = Unsigned32
_JnxUserFwTotalUserProbeNum_Object = MibTableColumn
jnxUserFwTotalUserProbeNum = _JnxUserFwTotalUserProbeNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 4, 1, 2),
    _JnxUserFwTotalUserProbeNum_Type()
)
jnxUserFwTotalUserProbeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwTotalUserProbeNum.setStatus("current")
_JnxUserFwFailedUserProbeNum_Type = Unsigned32
_JnxUserFwFailedUserProbeNum_Object = MibTableColumn
jnxUserFwFailedUserProbeNum = _JnxUserFwFailedUserProbeNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 1, 4, 1, 3),
    _JnxUserFwFailedUserProbeNum_Type()
)
jnxUserFwFailedUserProbeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwFailedUserProbeNum.setStatus("current")
_JnxUserFwJIMSServerScalar_ObjectIdentity = ObjectIdentity
jnxUserFwJIMSServerScalar = _JnxUserFwJIMSServerScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2)
)
_JnxUserFwPriServAddress_Type = DisplayString
_JnxUserFwPriServAddress_Object = MibScalar
jnxUserFwPriServAddress = _JnxUserFwPriServAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2, 1),
    _JnxUserFwPriServAddress_Type()
)
jnxUserFwPriServAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwPriServAddress.setStatus("current")
_JnxUserFwPriServQuerySentNum_Type = Unsigned32
_JnxUserFwPriServQuerySentNum_Object = MibScalar
jnxUserFwPriServQuerySentNum = _JnxUserFwPriServQuerySentNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2, 2),
    _JnxUserFwPriServQuerySentNum_Type()
)
jnxUserFwPriServQuerySentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwPriServQuerySentNum.setStatus("current")
_JnxUserFwPriServQueryRespNum_Type = Unsigned32
_JnxUserFwPriServQueryRespNum_Object = MibScalar
jnxUserFwPriServQueryRespNum = _JnxUserFwPriServQueryRespNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2, 3),
    _JnxUserFwPriServQueryRespNum_Type()
)
jnxUserFwPriServQueryRespNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwPriServQueryRespNum.setStatus("current")
_JnxUserFwPriServQueryErrNum_Type = Unsigned32
_JnxUserFwPriServQueryErrNum_Object = MibScalar
jnxUserFwPriServQueryErrNum = _JnxUserFwPriServQueryErrNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2, 4),
    _JnxUserFwPriServQueryErrNum_Type()
)
jnxUserFwPriServQueryErrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwPriServQueryErrNum.setStatus("current")
_JnxUserFwPriServIPQuerySentNum_Type = Unsigned32
_JnxUserFwPriServIPQuerySentNum_Object = MibScalar
jnxUserFwPriServIPQuerySentNum = _JnxUserFwPriServIPQuerySentNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2, 5),
    _JnxUserFwPriServIPQuerySentNum_Type()
)
jnxUserFwPriServIPQuerySentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwPriServIPQuerySentNum.setStatus("current")
_JnxUserFwPriServIPQueryRespNum_Type = Unsigned32
_JnxUserFwPriServIPQueryRespNum_Object = MibScalar
jnxUserFwPriServIPQueryRespNum = _JnxUserFwPriServIPQueryRespNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2, 6),
    _JnxUserFwPriServIPQueryRespNum_Type()
)
jnxUserFwPriServIPQueryRespNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwPriServIPQueryRespNum.setStatus("current")
_JnxUserFwPriServIPQueryErrNum_Type = Unsigned32
_JnxUserFwPriServIPQueryErrNum_Object = MibScalar
jnxUserFwPriServIPQueryErrNum = _JnxUserFwPriServIPQueryErrNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2, 7),
    _JnxUserFwPriServIPQueryErrNum_Type()
)
jnxUserFwPriServIPQueryErrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwPriServIPQueryErrNum.setStatus("current")
_JnxUserFwSecServAddress_Type = DisplayString
_JnxUserFwSecServAddress_Object = MibScalar
jnxUserFwSecServAddress = _JnxUserFwSecServAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2, 8),
    _JnxUserFwSecServAddress_Type()
)
jnxUserFwSecServAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwSecServAddress.setStatus("current")
_JnxUserFwSecServQuerySentNum_Type = Unsigned32
_JnxUserFwSecServQuerySentNum_Object = MibScalar
jnxUserFwSecServQuerySentNum = _JnxUserFwSecServQuerySentNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2, 9),
    _JnxUserFwSecServQuerySentNum_Type()
)
jnxUserFwSecServQuerySentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwSecServQuerySentNum.setStatus("current")
_JnxUserFwSecServQueryRespNum_Type = Unsigned32
_JnxUserFwSecServQueryRespNum_Object = MibScalar
jnxUserFwSecServQueryRespNum = _JnxUserFwSecServQueryRespNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2, 10),
    _JnxUserFwSecServQueryRespNum_Type()
)
jnxUserFwSecServQueryRespNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwSecServQueryRespNum.setStatus("current")
_JnxUserFwSecServQueryErrNum_Type = Unsigned32
_JnxUserFwSecServQueryErrNum_Object = MibScalar
jnxUserFwSecServQueryErrNum = _JnxUserFwSecServQueryErrNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2, 11),
    _JnxUserFwSecServQueryErrNum_Type()
)
jnxUserFwSecServQueryErrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwSecServQueryErrNum.setStatus("current")
_JnxUserFwSecServIPQuerySentNum_Type = Unsigned32
_JnxUserFwSecServIPQuerySentNum_Object = MibScalar
jnxUserFwSecServIPQuerySentNum = _JnxUserFwSecServIPQuerySentNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2, 12),
    _JnxUserFwSecServIPQuerySentNum_Type()
)
jnxUserFwSecServIPQuerySentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwSecServIPQuerySentNum.setStatus("current")
_JnxUserFwSecServIPQueryRespNum_Type = Unsigned32
_JnxUserFwSecServIPQueryRespNum_Object = MibScalar
jnxUserFwSecServIPQueryRespNum = _JnxUserFwSecServIPQueryRespNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2, 13),
    _JnxUserFwSecServIPQueryRespNum_Type()
)
jnxUserFwSecServIPQueryRespNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwSecServIPQueryRespNum.setStatus("current")
_JnxUserFwSecServIPQueryErrNum_Type = Unsigned32
_JnxUserFwSecServIPQueryErrNum_Object = MibScalar
jnxUserFwSecServIPQueryErrNum = _JnxUserFwSecServIPQueryErrNum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 89, 1, 2, 14),
    _JnxUserFwSecServIPQueryErrNum_Type()
)
jnxUserFwSecServIPQueryErrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserFwSecServIPQueryErrNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-USERFIREWALL-MIB",
    **{"jnxUserFirewalls": jnxUserFirewalls,
       "jnxUserFwTable": jnxUserFwTable,
       "jnxUserFwDomainAuthTable": jnxUserFwDomainAuthTable,
       "jnxUserFwDomainAuthEntry": jnxUserFwDomainAuthEntry,
       "jnxUserFwDomain": jnxUserFwDomain,
       "jnxUserFwAuthCPCounter": jnxUserFwAuthCPCounter,
       "jnxUserFwAuthJIMSCounter": jnxUserFwAuthJIMSCounter,
       "jnxUserFwAuthValidCounter": jnxUserFwAuthValidCounter,
       "jnxUserFwAuthPendingCounter": jnxUserFwAuthPendingCounter,
       "jnxUserFwAuthInvalidCounter": jnxUserFwAuthInvalidCounter,
       "jnxUserFwAuthTotalCounter": jnxUserFwAuthTotalCounter,
       "jnxUserFwAuthADCounter": jnxUserFwAuthADCounter,
       "jnxUserFwADDomCtlrTable": jnxUserFwADDomCtlrTable,
       "jnxUserFwADDomCtlrEntry": jnxUserFwADDomCtlrEntry,
       "jnxUserFwADDomain": jnxUserFwADDomain,
       "jnxUserFwADDomCtrlerAddr": jnxUserFwADDomCtrlerAddr,
       "jnxUserFwADDomCtrlerName": jnxUserFwADDomCtrlerName,
       "jnxUserFwADDomCtrlerConnStatus": jnxUserFwADDomCtrlerConnStatus,
       "jnxUserFwADDomTotalLogQuery": jnxUserFwADDomTotalLogQuery,
       "jnxUserFwADDomFailedLogQuery": jnxUserFwADDomFailedLogQuery,
       "jnxUserFwADDomRecordsFetched": jnxUserFwADDomRecordsFetched,
       "jnxUserFwLDAPTable": jnxUserFwLDAPTable,
       "jnxUserFwLDAPEntry": jnxUserFwLDAPEntry,
       "jnxUserFwLDAPDomain": jnxUserFwLDAPDomain,
       "jnxUserFwLDAPHost": jnxUserFwLDAPHost,
       "jnxUserFwLDAPTotalQuery": jnxUserFwLDAPTotalQuery,
       "jnxUserFwLDAPFailedQuery": jnxUserFwLDAPFailedQuery,
       "jnxUserFwProbeTable": jnxUserFwProbeTable,
       "jnxUserFwProbeEntry": jnxUserFwProbeEntry,
       "jnxUserFwDomainName": jnxUserFwDomainName,
       "jnxUserFwTotalUserProbeNum": jnxUserFwTotalUserProbeNum,
       "jnxUserFwFailedUserProbeNum": jnxUserFwFailedUserProbeNum,
       "jnxUserFwJIMSServerScalar": jnxUserFwJIMSServerScalar,
       "jnxUserFwPriServAddress": jnxUserFwPriServAddress,
       "jnxUserFwPriServQuerySentNum": jnxUserFwPriServQuerySentNum,
       "jnxUserFwPriServQueryRespNum": jnxUserFwPriServQueryRespNum,
       "jnxUserFwPriServQueryErrNum": jnxUserFwPriServQueryErrNum,
       "jnxUserFwPriServIPQuerySentNum": jnxUserFwPriServIPQuerySentNum,
       "jnxUserFwPriServIPQueryRespNum": jnxUserFwPriServIPQueryRespNum,
       "jnxUserFwPriServIPQueryErrNum": jnxUserFwPriServIPQueryErrNum,
       "jnxUserFwSecServAddress": jnxUserFwSecServAddress,
       "jnxUserFwSecServQuerySentNum": jnxUserFwSecServQuerySentNum,
       "jnxUserFwSecServQueryRespNum": jnxUserFwSecServQueryRespNum,
       "jnxUserFwSecServQueryErrNum": jnxUserFwSecServQueryErrNum,
       "jnxUserFwSecServIPQuerySentNum": jnxUserFwSecServIPQuerySentNum,
       "jnxUserFwSecServIPQueryRespNum": jnxUserFwSecServIPQueryRespNum,
       "jnxUserFwSecServIPQueryErrNum": jnxUserFwSecServIPQueryErrNum}
)
