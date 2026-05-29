# SNMP MIB module (IMMALERT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ibm\IMMALERT-MIB

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_SupportProcessor_ObjectIdentity = ObjectIdentity
supportProcessor = _SupportProcessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 158)
)
_ImmalertMIB_ObjectIdentity = ObjectIdentity
immalertMIB = _ImmalertMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5)
)
_Immtrapg_ObjectIdentity = ObjectIdentity
immtrapg = _Immtrapg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1)
)
_AltDateTime_Type = DisplayString
_AltDateTime_Object = MibScalar
altDateTime = _AltDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 1),
    _AltDateTime_Type()
)
altDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altDateTime.setStatus("mandatory")
_AltSpTxtId_Type = DisplayString
_AltSpTxtId_Object = MibScalar
altSpTxtId = _AltSpTxtId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 3),
    _AltSpTxtId_Type()
)
altSpTxtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altSpTxtId.setStatus("mandatory")
_AltSysUuid_Type = DisplayString
_AltSysUuid_Object = MibScalar
altSysUuid = _AltSysUuid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 5),
    _AltSysUuid_Type()
)
altSysUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altSysUuid.setStatus("mandatory")
_AltSysSern_Type = DisplayString
_AltSysSern_Object = MibScalar
altSysSern = _AltSysSern_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 6),
    _AltSysSern_Type()
)
altSysSern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altSysSern.setStatus("mandatory")


class _AltPriority_Type(Integer32):
    """Custom type altPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AltPriority_Type.__name__ = "Integer32"
_AltPriority_Object = MibScalar
altPriority = _AltPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 8),
    _AltPriority_Type()
)
altPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altPriority.setStatus("mandatory")
_AltMsgText_Type = DisplayString
_AltMsgText_Object = MibScalar
altMsgText = _AltMsgText_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 9),
    _AltMsgText_Type()
)
altMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altMsgText.setStatus("mandatory")
_AltMsgID_Type = Integer32
_AltMsgID_Object = MibScalar
altMsgID = _AltMsgID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 10),
    _AltMsgID_Type()
)
altMsgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altMsgID.setStatus("mandatory")
_AltMsgIDPrefix_Type = DisplayString
_AltMsgIDPrefix_Object = MibScalar
altMsgIDPrefix = _AltMsgIDPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 11),
    _AltMsgIDPrefix_Type()
)
altMsgIDPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altMsgIDPrefix.setStatus("mandatory")
_AltHostContact_Type = DisplayString
_AltHostContact_Object = MibScalar
altHostContact = _AltHostContact_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 12),
    _AltHostContact_Type()
)
altHostContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altHostContact.setStatus("mandatory")
_AltHostLocation_Type = DisplayString
_AltHostLocation_Object = MibScalar
altHostLocation = _AltHostLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 13),
    _AltHostLocation_Type()
)
altHostLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altHostLocation.setStatus("mandatory")
_AltHostRoomID_Type = DisplayString
_AltHostRoomID_Object = MibScalar
altHostRoomID = _AltHostRoomID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 14),
    _AltHostRoomID_Type()
)
altHostRoomID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altHostRoomID.setStatus("mandatory")
_AltHostRackID_Type = DisplayString
_AltHostRackID_Object = MibScalar
altHostRackID = _AltHostRackID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 15),
    _AltHostRackID_Type()
)
altHostRackID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altHostRackID.setStatus("mandatory")
_AltHostLowestUpos_Type = DisplayString
_AltHostLowestUpos_Object = MibScalar
altHostLowestUpos = _AltHostLowestUpos_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 16),
    _AltHostLowestUpos_Type()
)
altHostLowestUpos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altHostLowestUpos.setStatus("mandatory")
_AltHostBladeBay_Type = DisplayString
_AltHostBladeBay_Object = MibScalar
altHostBladeBay = _AltHostBladeBay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 17),
    _AltHostBladeBay_Type()
)
altHostBladeBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altHostBladeBay.setStatus("mandatory")
_AltEventID_Type = DisplayString
_AltEventID_Object = MibScalar
altEventID = _AltEventID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 18),
    _AltEventID_Type()
)
altEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altEventID.setStatus("mandatory")


class _AltServiceable_Type(Integer32):
    """Custom type altServiceable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notServiceable", 0),
          ("serviceableByIBM", 1),
          ("serviceableByCustomer", 2))
    )


_AltServiceable_Type.__name__ = "Integer32"
_AltServiceable_Object = MibScalar
altServiceable = _AltServiceable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 19),
    _AltServiceable_Type()
)
altServiceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altServiceable.setStatus("mandatory")


class _AltTest_Type(Integer32):
    """Custom type altTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AltTest_Type.__name__ = "Integer32"
_AltTest_Object = MibScalar
altTest = _AltTest_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 20),
    _AltTest_Type()
)
altTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altTest.setStatus("mandatory")
_AltFailingFRUs_Type = DisplayString
_AltFailingFRUs_Object = MibScalar
altFailingFRUs = _AltFailingFRUs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 21),
    _AltFailingFRUs_Type()
)
altFailingFRUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altFailingFRUs.setStatus("mandatory")
_AltHostMTM_Type = DisplayString
_AltHostMTM_Object = MibScalar
altHostMTM = _AltHostMTM_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 22),
    _AltHostMTM_Type()
)
altHostMTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altHostMTM.setStatus("mandatory")
_AltAuxData_Type = DisplayString
_AltAuxData_Object = MibScalar
altAuxData = _AltAuxData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 1, 23),
    _AltAuxData_Type()
)
altAuxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altAuxData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ibmSpTrapTempC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 0)
)
ibmSpTrapTempC.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapTempC.setStatus(
        ""
    )

ibmSpTrapVoltC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 1)
)
ibmSpTrapVoltC.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapVoltC.setStatus(
        ""
    )

ibmSpTrapPowerC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 4)
)
ibmSpTrapPowerC.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapPowerC.setStatus(
        ""
    )

ibmSpTrapHdC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 5)
)
ibmSpTrapHdC.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapHdC.setStatus(
        ""
    )

ibmSpTrapRdpsC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 9)
)
ibmSpTrapRdpsC.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapRdpsC.setStatus(
        ""
    )

ibmSpTrapRdpsN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 10)
)
ibmSpTrapRdpsN.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapRdpsN.setStatus(
        ""
    )

ibmSpTrapFanC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 11)
)
ibmSpTrapFanC.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapFanC.setStatus(
        ""
    )

ibmSpTrapTempN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 12)
)
ibmSpTrapTempN.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapTempN.setStatus(
        ""
    )

ibmSpTrapVoltN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 13)
)
ibmSpTrapVoltN.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapVoltN.setStatus(
        ""
    )

ibmSpTrapOsToS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 21)
)
ibmSpTrapOsToS.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapOsToS.setStatus(
        ""
    )

ibmSpTrapAppS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 22)
)
ibmSpTrapAppS.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapAppS.setStatus(
        ""
    )

ibmSpTrapPoffS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 23)
)
ibmSpTrapPoffS.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapPoffS.setStatus(
        ""
    )

ibmSpTrapPonS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 24)
)
ibmSpTrapPonS.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapPonS.setStatus(
        ""
    )

ibmSpTrapBootS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 25)
)
ibmSpTrapBootS.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapBootS.setStatus(
        ""
    )

ibmSpTrapLdrToS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 26)
)
ibmSpTrapLdrToS.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapLdrToS.setStatus(
        ""
    )

ibmSpTrapPFAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 27)
)
ibmSpTrapPFAS.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapPFAS.setStatus(
        ""
    )

ibmSpTrapRLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 30)
)
ibmSpTrapRLogin.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapRLogin.setStatus(
        ""
    )

ibmSpTrapSysLogS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 35)
)
ibmSpTrapSysLogS.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapSysLogS.setStatus(
        ""
    )

ibmSpTrapIhcC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 36)
)
ibmSpTrapIhcC.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapIhcC.setStatus(
        ""
    )

ibmSpTrapNwChangeS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 37)
)
ibmSpTrapNwChangeS.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapNwChangeS.setStatus(
        ""
    )

ibmSpTrapCPUC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 40)
)
ibmSpTrapCPUC.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapCPUC.setStatus(
        ""
    )

ibmSpTrapMemoryC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 41)
)
ibmSpTrapMemoryC.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapMemoryC.setStatus(
        ""
    )

ibmSpTrapCPUN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 42)
)
ibmSpTrapCPUN.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapCPUN.setStatus(
        ""
    )

ibmSpTrapMemoryN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 43)
)
ibmSpTrapMemoryN.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapMemoryN.setStatus(
        ""
    )

ibmSpTrapHardwareC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 50)
)
ibmSpTrapHardwareC.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapHardwareC.setStatus(
        ""
    )

ibmSpTrapHardwareN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 60)
)
ibmSpTrapHardwareN.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapHardwareN.setStatus(
        ""
    )

ibmSpTrapPowerN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 164)
)
ibmSpTrapPowerN.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapPowerN.setStatus(
        ""
    )

ibmSpTrapFanN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 158, 5, 0, 165)
)
ibmSpTrapFanN.setObjects(
      *(("IMMALERT-MIB", "altDateTime"),
        ("IMMALERT-MIB", "altSpTxtId"),
        ("IMMALERT-MIB", "altSysUuid"),
        ("IMMALERT-MIB", "altSysSern"),
        ("IMMALERT-MIB", "altMsgID"),
        ("IMMALERT-MIB", "altMsgIDPrefix"),
        ("IMMALERT-MIB", "altPriority"),
        ("IMMALERT-MIB", "altMsgText"),
        ("IMMALERT-MIB", "altHostContact"),
        ("IMMALERT-MIB", "altHostLocation"),
        ("IMMALERT-MIB", "altHostRoomID"),
        ("IMMALERT-MIB", "altHostRackID"),
        ("IMMALERT-MIB", "altHostLowestUpos"),
        ("IMMALERT-MIB", "altHostBladeBay"),
        ("IMMALERT-MIB", "altEventID"),
        ("IMMALERT-MIB", "altServiceable"),
        ("IMMALERT-MIB", "altTest"),
        ("IMMALERT-MIB", "altFailingFRUs"),
        ("IMMALERT-MIB", "altHostMTM"),
        ("IMMALERT-MIB", "altAuxData"))
)
if mibBuilder.loadTexts:
    ibmSpTrapFanN.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IMMALERT-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "supportProcessor": supportProcessor,
       "immalertMIB": immalertMIB,
       "ibmSpTrapTempC": ibmSpTrapTempC,
       "ibmSpTrapVoltC": ibmSpTrapVoltC,
       "ibmSpTrapPowerC": ibmSpTrapPowerC,
       "ibmSpTrapHdC": ibmSpTrapHdC,
       "ibmSpTrapRdpsC": ibmSpTrapRdpsC,
       "ibmSpTrapRdpsN": ibmSpTrapRdpsN,
       "ibmSpTrapFanC": ibmSpTrapFanC,
       "ibmSpTrapTempN": ibmSpTrapTempN,
       "ibmSpTrapVoltN": ibmSpTrapVoltN,
       "ibmSpTrapOsToS": ibmSpTrapOsToS,
       "ibmSpTrapAppS": ibmSpTrapAppS,
       "ibmSpTrapPoffS": ibmSpTrapPoffS,
       "ibmSpTrapPonS": ibmSpTrapPonS,
       "ibmSpTrapBootS": ibmSpTrapBootS,
       "ibmSpTrapLdrToS": ibmSpTrapLdrToS,
       "ibmSpTrapPFAS": ibmSpTrapPFAS,
       "ibmSpTrapRLogin": ibmSpTrapRLogin,
       "ibmSpTrapSysLogS": ibmSpTrapSysLogS,
       "ibmSpTrapIhcC": ibmSpTrapIhcC,
       "ibmSpTrapNwChangeS": ibmSpTrapNwChangeS,
       "ibmSpTrapCPUC": ibmSpTrapCPUC,
       "ibmSpTrapMemoryC": ibmSpTrapMemoryC,
       "ibmSpTrapCPUN": ibmSpTrapCPUN,
       "ibmSpTrapMemoryN": ibmSpTrapMemoryN,
       "ibmSpTrapHardwareC": ibmSpTrapHardwareC,
       "ibmSpTrapHardwareN": ibmSpTrapHardwareN,
       "ibmSpTrapPowerN": ibmSpTrapPowerN,
       "ibmSpTrapFanN": ibmSpTrapFanN,
       "immtrapg": immtrapg,
       "altDateTime": altDateTime,
       "altSpTxtId": altSpTxtId,
       "altSysUuid": altSysUuid,
       "altSysSern": altSysSern,
       "altPriority": altPriority,
       "altMsgText": altMsgText,
       "altMsgID": altMsgID,
       "altMsgIDPrefix": altMsgIDPrefix,
       "altHostContact": altHostContact,
       "altHostLocation": altHostLocation,
       "altHostRoomID": altHostRoomID,
       "altHostRackID": altHostRackID,
       "altHostLowestUpos": altHostLowestUpos,
       "altHostBladeBay": altHostBladeBay,
       "altEventID": altEventID,
       "altServiceable": altServiceable,
       "altTest": altTest,
       "altFailingFRUs": altFailingFRUs,
       "altHostMTM": altHostMTM,
       "altAuxData": altAuxData}
)
