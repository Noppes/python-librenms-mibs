# SNMP MIB module (TERRA-sti440-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\terra\TERRA-sti440-MIB

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

(DefStatus,) = mibBuilder.importSymbols(
    "TERRA-DEFINITIONS-MIB",
    "DefStatus")

(terraProducts,) = mibBuilder.importSymbols(
    "TERRA-PRODUCTS-MIB",
    "terraProducts")


# MODULE-IDENTITY

terra_sti440 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18)
)
if mibBuilder.loadTexts:
    terra_sti440.setRevisions(
        ("2019-02-06 16:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sti440status_ObjectIdentity = ObjectIdentity
sti440status = _Sti440status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1)
)
_RFinStatus1_ObjectIdentity = ObjectIdentity
rFinStatus1 = _RFinStatus1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 1)
)
_InLock1_Type = Integer32
_InLock1_Object = MibScalar
inLock1 = _InLock1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 1, 1),
    _InLock1_Type()
)
inLock1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLock1.setStatus("current")
_Instd1_Type = DisplayString
_Instd1_Object = MibScalar
instd1 = _Instd1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 1, 2),
    _Instd1_Type()
)
instd1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instd1.setStatus("current")
_Inlevel1_Type = Integer32
_Inlevel1_Object = MibScalar
inlevel1 = _Inlevel1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 1, 3),
    _Inlevel1_Type()
)
inlevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlevel1.setStatus("current")
if mibBuilder.loadTexts:
    inlevel1.setUnits("dbuV")
_Inmod1_Type = DisplayString
_Inmod1_Object = MibScalar
inmod1 = _Inmod1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 1, 4),
    _Inmod1_Type()
)
inmod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inmod1.setStatus("current")
_Insnr1_Type = Integer32
_Insnr1_Object = MibScalar
insnr1 = _Insnr1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 1, 5),
    _Insnr1_Type()
)
insnr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insnr1.setStatus("current")
if mibBuilder.loadTexts:
    insnr1.setUnits("db")
_Inber1_Type = Integer32
_Inber1_Object = MibScalar
inber1 = _Inber1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 1, 6),
    _Inber1_Type()
)
inber1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inber1.setStatus("current")
_Inper1_Type = Integer32
_Inper1_Object = MibScalar
inper1 = _Inper1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 1, 7),
    _Inper1_Type()
)
inper1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inper1.setStatus("current")
_Inuncorr1_Type = Integer32
_Inuncorr1_Object = MibScalar
inuncorr1 = _Inuncorr1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 1, 8),
    _Inuncorr1_Type()
)
inuncorr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inuncorr1.setStatus("current")
_Inbr1_Type = Integer32
_Inbr1_Object = MibScalar
inbr1 = _Inbr1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 1, 9),
    _Inbr1_Type()
)
inbr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbr1.setStatus("current")
if mibBuilder.loadTexts:
    inbr1.setUnits("Kbps")
_Inccerr1_Type = Integer32
_Inccerr1_Object = MibScalar
inccerr1 = _Inccerr1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 1, 10),
    _Inccerr1_Type()
)
inccerr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inccerr1.setStatus("current")
_Intotpack1_Type = Integer32
_Intotpack1_Object = MibScalar
intotpack1 = _Intotpack1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 1, 11),
    _Intotpack1_Type()
)
intotpack1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intotpack1.setStatus("current")
_RFinStatus2_ObjectIdentity = ObjectIdentity
rFinStatus2 = _RFinStatus2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 2)
)
_InLock2_Type = Integer32
_InLock2_Object = MibScalar
inLock2 = _InLock2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 2, 1),
    _InLock2_Type()
)
inLock2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLock2.setStatus("current")
_Instd2_Type = DisplayString
_Instd2_Object = MibScalar
instd2 = _Instd2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 2, 2),
    _Instd2_Type()
)
instd2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instd2.setStatus("current")
_Inlevel2_Type = Integer32
_Inlevel2_Object = MibScalar
inlevel2 = _Inlevel2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 2, 3),
    _Inlevel2_Type()
)
inlevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlevel2.setStatus("current")
if mibBuilder.loadTexts:
    inlevel2.setUnits("dbuV")
_Inmod2_Type = DisplayString
_Inmod2_Object = MibScalar
inmod2 = _Inmod2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 2, 4),
    _Inmod2_Type()
)
inmod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inmod2.setStatus("current")
_Insnr2_Type = Integer32
_Insnr2_Object = MibScalar
insnr2 = _Insnr2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 2, 5),
    _Insnr2_Type()
)
insnr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insnr2.setStatus("current")
if mibBuilder.loadTexts:
    insnr2.setUnits("db")
_Inber2_Type = Integer32
_Inber2_Object = MibScalar
inber2 = _Inber2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 2, 6),
    _Inber2_Type()
)
inber2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inber2.setStatus("current")
_Inper2_Type = Integer32
_Inper2_Object = MibScalar
inper2 = _Inper2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 2, 7),
    _Inper2_Type()
)
inper2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inper2.setStatus("current")
_Inuncorr2_Type = Integer32
_Inuncorr2_Object = MibScalar
inuncorr2 = _Inuncorr2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 2, 8),
    _Inuncorr2_Type()
)
inuncorr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inuncorr2.setStatus("current")
_Inbr2_Type = Integer32
_Inbr2_Object = MibScalar
inbr2 = _Inbr2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 2, 9),
    _Inbr2_Type()
)
inbr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbr2.setStatus("current")
if mibBuilder.loadTexts:
    inbr2.setUnits("Kbps")
_Inccerr2_Type = Integer32
_Inccerr2_Object = MibScalar
inccerr2 = _Inccerr2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 2, 10),
    _Inccerr2_Type()
)
inccerr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inccerr2.setStatus("current")
_Intotpack2_Type = Integer32
_Intotpack2_Object = MibScalar
intotpack2 = _Intotpack2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 2, 11),
    _Intotpack2_Type()
)
intotpack2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intotpack2.setStatus("current")
_RFinStatus3_ObjectIdentity = ObjectIdentity
rFinStatus3 = _RFinStatus3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 3)
)
_InLock3_Type = Integer32
_InLock3_Object = MibScalar
inLock3 = _InLock3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 3, 1),
    _InLock3_Type()
)
inLock3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLock3.setStatus("current")
_Instd3_Type = DisplayString
_Instd3_Object = MibScalar
instd3 = _Instd3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 3, 2),
    _Instd3_Type()
)
instd3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instd3.setStatus("current")
_Inlevel3_Type = Integer32
_Inlevel3_Object = MibScalar
inlevel3 = _Inlevel3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 3, 3),
    _Inlevel3_Type()
)
inlevel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlevel3.setStatus("current")
if mibBuilder.loadTexts:
    inlevel3.setUnits("dbuV")
_Inmod3_Type = DisplayString
_Inmod3_Object = MibScalar
inmod3 = _Inmod3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 3, 4),
    _Inmod3_Type()
)
inmod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inmod3.setStatus("current")
_Insnr3_Type = Integer32
_Insnr3_Object = MibScalar
insnr3 = _Insnr3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 3, 5),
    _Insnr3_Type()
)
insnr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insnr3.setStatus("current")
if mibBuilder.loadTexts:
    insnr3.setUnits("db")
_Inber3_Type = Integer32
_Inber3_Object = MibScalar
inber3 = _Inber3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 3, 6),
    _Inber3_Type()
)
inber3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inber3.setStatus("current")
_Inper3_Type = Integer32
_Inper3_Object = MibScalar
inper3 = _Inper3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 3, 7),
    _Inper3_Type()
)
inper3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inper3.setStatus("current")
_Inuncorr3_Type = Integer32
_Inuncorr3_Object = MibScalar
inuncorr3 = _Inuncorr3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 3, 8),
    _Inuncorr3_Type()
)
inuncorr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inuncorr3.setStatus("current")
_Inbr3_Type = Integer32
_Inbr3_Object = MibScalar
inbr3 = _Inbr3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 3, 9),
    _Inbr3_Type()
)
inbr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbr3.setStatus("current")
if mibBuilder.loadTexts:
    inbr3.setUnits("Kbps")
_Inccerr3_Type = Integer32
_Inccerr3_Object = MibScalar
inccerr3 = _Inccerr3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 3, 10),
    _Inccerr3_Type()
)
inccerr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inccerr3.setStatus("current")
_Intotpack3_Type = Integer32
_Intotpack3_Object = MibScalar
intotpack3 = _Intotpack3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 3, 11),
    _Intotpack3_Type()
)
intotpack3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intotpack3.setStatus("current")
_RFinStatus4_ObjectIdentity = ObjectIdentity
rFinStatus4 = _RFinStatus4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 4)
)
_InLock4_Type = Integer32
_InLock4_Object = MibScalar
inLock4 = _InLock4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 4, 1),
    _InLock4_Type()
)
inLock4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inLock4.setStatus("current")
_Instd4_Type = DisplayString
_Instd4_Object = MibScalar
instd4 = _Instd4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 4, 2),
    _Instd4_Type()
)
instd4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instd4.setStatus("current")
_Inlevel4_Type = Integer32
_Inlevel4_Object = MibScalar
inlevel4 = _Inlevel4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 4, 3),
    _Inlevel4_Type()
)
inlevel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inlevel4.setStatus("current")
if mibBuilder.loadTexts:
    inlevel4.setUnits("dbuV")
_Inmod4_Type = DisplayString
_Inmod4_Object = MibScalar
inmod4 = _Inmod4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 4, 4),
    _Inmod4_Type()
)
inmod4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inmod4.setStatus("current")
_Insnr4_Type = Integer32
_Insnr4_Object = MibScalar
insnr4 = _Insnr4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 4, 5),
    _Insnr4_Type()
)
insnr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insnr4.setStatus("current")
if mibBuilder.loadTexts:
    insnr4.setUnits("db")
_Inber4_Type = Integer32
_Inber4_Object = MibScalar
inber4 = _Inber4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 4, 6),
    _Inber4_Type()
)
inber4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inber4.setStatus("current")
_Inper4_Type = Integer32
_Inper4_Object = MibScalar
inper4 = _Inper4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 4, 7),
    _Inper4_Type()
)
inper4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inper4.setStatus("current")
_Inuncorr4_Type = Integer32
_Inuncorr4_Object = MibScalar
inuncorr4 = _Inuncorr4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 4, 8),
    _Inuncorr4_Type()
)
inuncorr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inuncorr4.setStatus("current")
_Inbr4_Type = Integer32
_Inbr4_Object = MibScalar
inbr4 = _Inbr4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 4, 9),
    _Inbr4_Type()
)
inbr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbr4.setStatus("current")
if mibBuilder.loadTexts:
    inbr4.setUnits("Kbps")
_Inccerr4_Type = Integer32
_Inccerr4_Object = MibScalar
inccerr4 = _Inccerr4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 4, 10),
    _Inccerr4_Type()
)
inccerr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inccerr4.setStatus("current")
_Intotpack4_Type = Integer32
_Intotpack4_Object = MibScalar
intotpack4 = _Intotpack4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 4, 11),
    _Intotpack4_Type()
)
intotpack4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intotpack4.setStatus("current")
_UsbStatus_ObjectIdentity = ObjectIdentity
usbStatus = _UsbStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 5)
)
_UsbinBR_Type = Integer32
_UsbinBR_Object = MibScalar
usbinBR = _UsbinBR_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 5, 1),
    _UsbinBR_Type()
)
usbinBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbinBR.setStatus("current")
if mibBuilder.loadTexts:
    usbinBR.setUnits("tenth of Mbps")
_OutStream1_ObjectIdentity = ObjectIdentity
outStream1 = _OutStream1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 6)
)
_OutBr1_Type = Integer32
_OutBr1_Object = MibScalar
outBr1 = _OutBr1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 6, 1),
    _OutBr1_Type()
)
outBr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr1.setStatus("current")
if mibBuilder.loadTexts:
    outBr1.setUnits("tenth of Mbps")
_OutStream2_ObjectIdentity = ObjectIdentity
outStream2 = _OutStream2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 7)
)
_OutBr2_Type = Integer32
_OutBr2_Object = MibScalar
outBr2 = _OutBr2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 7, 1),
    _OutBr2_Type()
)
outBr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr2.setStatus("current")
if mibBuilder.loadTexts:
    outBr2.setUnits("tenth of Mbps")
_OutStream3_ObjectIdentity = ObjectIdentity
outStream3 = _OutStream3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 8)
)
_OutBr3_Type = Integer32
_OutBr3_Object = MibScalar
outBr3 = _OutBr3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 8, 1),
    _OutBr3_Type()
)
outBr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr3.setStatus("current")
if mibBuilder.loadTexts:
    outBr3.setUnits("tenth of Mbps")
_OutStream4_ObjectIdentity = ObjectIdentity
outStream4 = _OutStream4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 9)
)
_OutBr4_Type = Integer32
_OutBr4_Object = MibScalar
outBr4 = _OutBr4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 9, 1),
    _OutBr4_Type()
)
outBr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr4.setStatus("current")
if mibBuilder.loadTexts:
    outBr4.setUnits("tenth of Mbps")
_OutStream5_ObjectIdentity = ObjectIdentity
outStream5 = _OutStream5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 10)
)
_OutBr5_Type = Integer32
_OutBr5_Object = MibScalar
outBr5 = _OutBr5_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 10, 1),
    _OutBr5_Type()
)
outBr5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr5.setStatus("current")
if mibBuilder.loadTexts:
    outBr5.setUnits("tenth of Mbps")
_OutStream6_ObjectIdentity = ObjectIdentity
outStream6 = _OutStream6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 11)
)
_OutBr6_Type = Integer32
_OutBr6_Object = MibScalar
outBr6 = _OutBr6_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 11, 1),
    _OutBr6_Type()
)
outBr6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr6.setStatus("current")
if mibBuilder.loadTexts:
    outBr6.setUnits("tenth of Mbps")
_OutStream7_ObjectIdentity = ObjectIdentity
outStream7 = _OutStream7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 12)
)
_OutBr7_Type = Integer32
_OutBr7_Object = MibScalar
outBr7 = _OutBr7_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 12, 1),
    _OutBr7_Type()
)
outBr7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr7.setStatus("current")
if mibBuilder.loadTexts:
    outBr7.setUnits("tenth of Mbps")
_OutStream8_ObjectIdentity = ObjectIdentity
outStream8 = _OutStream8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 13)
)
_OutBr8_Type = Integer32
_OutBr8_Object = MibScalar
outBr8 = _OutBr8_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 13, 1),
    _OutBr8_Type()
)
outBr8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr8.setStatus("current")
if mibBuilder.loadTexts:
    outBr8.setUnits("tenth of Mbps")
_OutStream9_ObjectIdentity = ObjectIdentity
outStream9 = _OutStream9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 14)
)
_OutBr9_Type = Integer32
_OutBr9_Object = MibScalar
outBr9 = _OutBr9_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 14, 1),
    _OutBr9_Type()
)
outBr9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr9.setStatus("current")
if mibBuilder.loadTexts:
    outBr9.setUnits("tenth of Mbps")
_OutStream10_ObjectIdentity = ObjectIdentity
outStream10 = _OutStream10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 15)
)
_OutBr10_Type = Integer32
_OutBr10_Object = MibScalar
outBr10 = _OutBr10_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 15, 1),
    _OutBr10_Type()
)
outBr10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr10.setStatus("current")
if mibBuilder.loadTexts:
    outBr10.setUnits("tenth of Mbps")
_OutStream11_ObjectIdentity = ObjectIdentity
outStream11 = _OutStream11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 16)
)
_OutBr11_Type = Integer32
_OutBr11_Object = MibScalar
outBr11 = _OutBr11_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 16, 1),
    _OutBr11_Type()
)
outBr11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr11.setStatus("current")
if mibBuilder.loadTexts:
    outBr11.setUnits("tenth of Mbps")
_OutStream12_ObjectIdentity = ObjectIdentity
outStream12 = _OutStream12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 17)
)
_OutBr12_Type = Integer32
_OutBr12_Object = MibScalar
outBr12 = _OutBr12_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 17, 1),
    _OutBr12_Type()
)
outBr12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr12.setStatus("current")
if mibBuilder.loadTexts:
    outBr12.setUnits("tenth of Mbps")
_OutStream13_ObjectIdentity = ObjectIdentity
outStream13 = _OutStream13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 18)
)
_OutBr13_Type = Integer32
_OutBr13_Object = MibScalar
outBr13 = _OutBr13_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 18, 1),
    _OutBr13_Type()
)
outBr13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr13.setStatus("current")
if mibBuilder.loadTexts:
    outBr13.setUnits("tenth of Mbps")
_OutStream14_ObjectIdentity = ObjectIdentity
outStream14 = _OutStream14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 19)
)
_OutBr14_Type = Integer32
_OutBr14_Object = MibScalar
outBr14 = _OutBr14_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 19, 1),
    _OutBr14_Type()
)
outBr14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr14.setStatus("current")
if mibBuilder.loadTexts:
    outBr14.setUnits("tenth of Mbps")
_OutStream15_ObjectIdentity = ObjectIdentity
outStream15 = _OutStream15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 20)
)
_OutBr15_Type = Integer32
_OutBr15_Object = MibScalar
outBr15 = _OutBr15_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 20, 1),
    _OutBr15_Type()
)
outBr15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr15.setStatus("current")
if mibBuilder.loadTexts:
    outBr15.setUnits("tenth of Mbps")
_OutStream16_ObjectIdentity = ObjectIdentity
outStream16 = _OutStream16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 21)
)
_OutBr16_Type = Integer32
_OutBr16_Object = MibScalar
outBr16 = _OutBr16_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 21, 1),
    _OutBr16_Type()
)
outBr16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr16.setStatus("current")
if mibBuilder.loadTexts:
    outBr16.setUnits("tenth of Mbps")
_OutStream17_ObjectIdentity = ObjectIdentity
outStream17 = _OutStream17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 22)
)
_OutBr17_Type = Integer32
_OutBr17_Object = MibScalar
outBr17 = _OutBr17_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 22, 1),
    _OutBr17_Type()
)
outBr17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr17.setStatus("current")
if mibBuilder.loadTexts:
    outBr17.setUnits("tenth of Mbps")
_OutStream18_ObjectIdentity = ObjectIdentity
outStream18 = _OutStream18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 23)
)
_OutBr18_Type = Integer32
_OutBr18_Object = MibScalar
outBr18 = _OutBr18_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 23, 1),
    _OutBr18_Type()
)
outBr18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr18.setStatus("current")
if mibBuilder.loadTexts:
    outBr18.setUnits("tenth of Mbps")
_OutStream19_ObjectIdentity = ObjectIdentity
outStream19 = _OutStream19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 24)
)
_OutBr19_Type = Integer32
_OutBr19_Object = MibScalar
outBr19 = _OutBr19_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 24, 1),
    _OutBr19_Type()
)
outBr19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr19.setStatus("current")
if mibBuilder.loadTexts:
    outBr19.setUnits("tenth of Mbps")
_OutStream20_ObjectIdentity = ObjectIdentity
outStream20 = _OutStream20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 25)
)
_OutBr20_Type = Integer32
_OutBr20_Object = MibScalar
outBr20 = _OutBr20_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 25, 1),
    _OutBr20_Type()
)
outBr20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr20.setStatus("current")
if mibBuilder.loadTexts:
    outBr20.setUnits("tenth of Mbps")
_OutStream21_ObjectIdentity = ObjectIdentity
outStream21 = _OutStream21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 26)
)
_OutBr21_Type = Integer32
_OutBr21_Object = MibScalar
outBr21 = _OutBr21_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 26, 1),
    _OutBr21_Type()
)
outBr21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr21.setStatus("current")
if mibBuilder.loadTexts:
    outBr21.setUnits("tenth of Mbps")
_OutStream22_ObjectIdentity = ObjectIdentity
outStream22 = _OutStream22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 27)
)
_OutBr22_Type = Integer32
_OutBr22_Object = MibScalar
outBr22 = _OutBr22_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 27, 1),
    _OutBr22_Type()
)
outBr22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr22.setStatus("current")
if mibBuilder.loadTexts:
    outBr22.setUnits("tenth of Mbps")
_OutStream23_ObjectIdentity = ObjectIdentity
outStream23 = _OutStream23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 28)
)
_OutBr23_Type = Integer32
_OutBr23_Object = MibScalar
outBr23 = _OutBr23_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 28, 1),
    _OutBr23_Type()
)
outBr23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr23.setStatus("current")
if mibBuilder.loadTexts:
    outBr23.setUnits("tenth of Mbps")
_OutStream24_ObjectIdentity = ObjectIdentity
outStream24 = _OutStream24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 29)
)
_OutBr24_Type = Integer32
_OutBr24_Object = MibScalar
outBr24 = _OutBr24_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 29, 1),
    _OutBr24_Type()
)
outBr24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr24.setStatus("current")
if mibBuilder.loadTexts:
    outBr24.setUnits("tenth of Mbps")
_OutStream25_ObjectIdentity = ObjectIdentity
outStream25 = _OutStream25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 30)
)
_OutBr25_Type = Integer32
_OutBr25_Object = MibScalar
outBr25 = _OutBr25_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 30, 1),
    _OutBr25_Type()
)
outBr25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr25.setStatus("current")
if mibBuilder.loadTexts:
    outBr25.setUnits("tenth of Mbps")
_OutStream26_ObjectIdentity = ObjectIdentity
outStream26 = _OutStream26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 31)
)
_OutBr26_Type = Integer32
_OutBr26_Object = MibScalar
outBr26 = _OutBr26_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 31, 1),
    _OutBr26_Type()
)
outBr26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr26.setStatus("current")
if mibBuilder.loadTexts:
    outBr26.setUnits("tenth of Mbps")
_OutStream27_ObjectIdentity = ObjectIdentity
outStream27 = _OutStream27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 32)
)
_OutBr27_Type = Integer32
_OutBr27_Object = MibScalar
outBr27 = _OutBr27_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 32, 1),
    _OutBr27_Type()
)
outBr27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr27.setStatus("current")
if mibBuilder.loadTexts:
    outBr27.setUnits("tenth of Mbps")
_OutStream28_ObjectIdentity = ObjectIdentity
outStream28 = _OutStream28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 33)
)
_OutBr28_Type = Integer32
_OutBr28_Object = MibScalar
outBr28 = _OutBr28_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 33, 1),
    _OutBr28_Type()
)
outBr28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr28.setStatus("current")
if mibBuilder.loadTexts:
    outBr28.setUnits("tenth of Mbps")
_OutStream29_ObjectIdentity = ObjectIdentity
outStream29 = _OutStream29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 34)
)
_OutBr29_Type = Integer32
_OutBr29_Object = MibScalar
outBr29 = _OutBr29_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 34, 1),
    _OutBr29_Type()
)
outBr29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr29.setStatus("current")
if mibBuilder.loadTexts:
    outBr29.setUnits("tenth of Mbps")
_OutStream30_ObjectIdentity = ObjectIdentity
outStream30 = _OutStream30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 35)
)
_OutBr30_Type = Integer32
_OutBr30_Object = MibScalar
outBr30 = _OutBr30_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 35, 1),
    _OutBr30_Type()
)
outBr30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr30.setStatus("current")
if mibBuilder.loadTexts:
    outBr30.setUnits("tenth of Mbps")
_OutStream31_ObjectIdentity = ObjectIdentity
outStream31 = _OutStream31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 36)
)
_OutBr31_Type = Integer32
_OutBr31_Object = MibScalar
outBr31 = _OutBr31_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 36, 1),
    _OutBr31_Type()
)
outBr31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr31.setStatus("current")
if mibBuilder.loadTexts:
    outBr31.setUnits("tenth of Mbps")
_OutStream32_ObjectIdentity = ObjectIdentity
outStream32 = _OutStream32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 37)
)
_OutBr32_Type = Integer32
_OutBr32_Object = MibScalar
outBr32 = _OutBr32_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 37, 1),
    _OutBr32_Type()
)
outBr32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr32.setStatus("current")
if mibBuilder.loadTexts:
    outBr32.setUnits("tenth of Mbps")
_OutStream33_ObjectIdentity = ObjectIdentity
outStream33 = _OutStream33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 38)
)
_OutBr33_Type = Integer32
_OutBr33_Object = MibScalar
outBr33 = _OutBr33_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 38, 1),
    _OutBr33_Type()
)
outBr33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr33.setStatus("current")
if mibBuilder.loadTexts:
    outBr33.setUnits("tenth of Mbps")
_OutStream34_ObjectIdentity = ObjectIdentity
outStream34 = _OutStream34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 39)
)
_OutBr34_Type = Integer32
_OutBr34_Object = MibScalar
outBr34 = _OutBr34_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 39, 1),
    _OutBr34_Type()
)
outBr34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr34.setStatus("current")
if mibBuilder.loadTexts:
    outBr34.setUnits("tenth of Mbps")
_OutStream35_ObjectIdentity = ObjectIdentity
outStream35 = _OutStream35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 40)
)
_OutBr35_Type = Integer32
_OutBr35_Object = MibScalar
outBr35 = _OutBr35_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 40, 1),
    _OutBr35_Type()
)
outBr35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr35.setStatus("current")
if mibBuilder.loadTexts:
    outBr35.setUnits("tenth of Mbps")
_OutStream36_ObjectIdentity = ObjectIdentity
outStream36 = _OutStream36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 41)
)
_OutBr36_Type = Integer32
_OutBr36_Object = MibScalar
outBr36 = _OutBr36_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 41, 1),
    _OutBr36_Type()
)
outBr36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr36.setStatus("current")
if mibBuilder.loadTexts:
    outBr36.setUnits("tenth of Mbps")
_OutStream37_ObjectIdentity = ObjectIdentity
outStream37 = _OutStream37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 42)
)
_OutBr37_Type = Integer32
_OutBr37_Object = MibScalar
outBr37 = _OutBr37_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 42, 1),
    _OutBr37_Type()
)
outBr37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr37.setStatus("current")
if mibBuilder.loadTexts:
    outBr37.setUnits("tenth of Mbps")
_OutStream38_ObjectIdentity = ObjectIdentity
outStream38 = _OutStream38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 43)
)
_OutBr38_Type = Integer32
_OutBr38_Object = MibScalar
outBr38 = _OutBr38_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 43, 1),
    _OutBr38_Type()
)
outBr38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr38.setStatus("current")
if mibBuilder.loadTexts:
    outBr38.setUnits("tenth of Mbps")
_OutStream39_ObjectIdentity = ObjectIdentity
outStream39 = _OutStream39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 44)
)
_OutBr39_Type = Integer32
_OutBr39_Object = MibScalar
outBr39 = _OutBr39_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 44, 1),
    _OutBr39_Type()
)
outBr39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr39.setStatus("current")
if mibBuilder.loadTexts:
    outBr39.setUnits("tenth of Mbps")
_OutStream40_ObjectIdentity = ObjectIdentity
outStream40 = _OutStream40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 45)
)
_OutBr40_Type = Integer32
_OutBr40_Object = MibScalar
outBr40 = _OutBr40_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 45, 1),
    _OutBr40_Type()
)
outBr40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr40.setStatus("current")
if mibBuilder.loadTexts:
    outBr40.setUnits("tenth of Mbps")
_OutStream41_ObjectIdentity = ObjectIdentity
outStream41 = _OutStream41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 46)
)
_OutBr41_Type = Integer32
_OutBr41_Object = MibScalar
outBr41 = _OutBr41_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 46, 1),
    _OutBr41_Type()
)
outBr41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr41.setStatus("current")
if mibBuilder.loadTexts:
    outBr41.setUnits("tenth of Mbps")
_OutStream42_ObjectIdentity = ObjectIdentity
outStream42 = _OutStream42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 47)
)
_OutBr42_Type = Integer32
_OutBr42_Object = MibScalar
outBr42 = _OutBr42_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 47, 1),
    _OutBr42_Type()
)
outBr42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr42.setStatus("current")
if mibBuilder.loadTexts:
    outBr42.setUnits("tenth of Mbps")
_OutStream43_ObjectIdentity = ObjectIdentity
outStream43 = _OutStream43_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 48)
)
_OutBr43_Type = Integer32
_OutBr43_Object = MibScalar
outBr43 = _OutBr43_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 48, 1),
    _OutBr43_Type()
)
outBr43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr43.setStatus("current")
if mibBuilder.loadTexts:
    outBr43.setUnits("tenth of Mbps")
_OutStream44_ObjectIdentity = ObjectIdentity
outStream44 = _OutStream44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 49)
)
_OutBr44_Type = Integer32
_OutBr44_Object = MibScalar
outBr44 = _OutBr44_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 49, 1),
    _OutBr44_Type()
)
outBr44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr44.setStatus("current")
if mibBuilder.loadTexts:
    outBr44.setUnits("tenth of Mbps")
_OutStream45_ObjectIdentity = ObjectIdentity
outStream45 = _OutStream45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 50)
)
_OutBr45_Type = Integer32
_OutBr45_Object = MibScalar
outBr45 = _OutBr45_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 50, 1),
    _OutBr45_Type()
)
outBr45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr45.setStatus("current")
if mibBuilder.loadTexts:
    outBr45.setUnits("tenth of Mbps")
_OutStream46_ObjectIdentity = ObjectIdentity
outStream46 = _OutStream46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 51)
)
_OutBr46_Type = Integer32
_OutBr46_Object = MibScalar
outBr46 = _OutBr46_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 51, 1),
    _OutBr46_Type()
)
outBr46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr46.setStatus("current")
if mibBuilder.loadTexts:
    outBr46.setUnits("tenth of Mbps")
_OutStream47_ObjectIdentity = ObjectIdentity
outStream47 = _OutStream47_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 52)
)
_OutBr47_Type = Integer32
_OutBr47_Object = MibScalar
outBr47 = _OutBr47_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 52, 1),
    _OutBr47_Type()
)
outBr47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr47.setStatus("current")
if mibBuilder.loadTexts:
    outBr47.setUnits("tenth of Mbps")
_OutStream48_ObjectIdentity = ObjectIdentity
outStream48 = _OutStream48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 53)
)
_OutBr48_Type = Integer32
_OutBr48_Object = MibScalar
outBr48 = _OutBr48_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 53, 1),
    _OutBr48_Type()
)
outBr48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr48.setStatus("current")
if mibBuilder.loadTexts:
    outBr48.setUnits("tenth of Mbps")
_OutStream49_ObjectIdentity = ObjectIdentity
outStream49 = _OutStream49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 54)
)
_OutBr49_Type = Integer32
_OutBr49_Object = MibScalar
outBr49 = _OutBr49_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 54, 1),
    _OutBr49_Type()
)
outBr49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr49.setStatus("current")
if mibBuilder.loadTexts:
    outBr49.setUnits("tenth of Mbps")
_OutStream50_ObjectIdentity = ObjectIdentity
outStream50 = _OutStream50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 55)
)
_OutBr50_Type = Integer32
_OutBr50_Object = MibScalar
outBr50 = _OutBr50_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 55, 1),
    _OutBr50_Type()
)
outBr50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr50.setStatus("current")
if mibBuilder.loadTexts:
    outBr50.setUnits("tenth of Mbps")
_OutStream51_ObjectIdentity = ObjectIdentity
outStream51 = _OutStream51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 56)
)
_OutBr51_Type = Integer32
_OutBr51_Object = MibScalar
outBr51 = _OutBr51_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 56, 1),
    _OutBr51_Type()
)
outBr51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr51.setStatus("current")
if mibBuilder.loadTexts:
    outBr51.setUnits("tenth of Mbps")
_OutStream52_ObjectIdentity = ObjectIdentity
outStream52 = _OutStream52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 57)
)
_OutBr52_Type = Integer32
_OutBr52_Object = MibScalar
outBr52 = _OutBr52_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 57, 1),
    _OutBr52_Type()
)
outBr52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr52.setStatus("current")
if mibBuilder.loadTexts:
    outBr52.setUnits("tenth of Mbps")
_OutStream53_ObjectIdentity = ObjectIdentity
outStream53 = _OutStream53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 58)
)
_OutBr53_Type = Integer32
_OutBr53_Object = MibScalar
outBr53 = _OutBr53_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 58, 1),
    _OutBr53_Type()
)
outBr53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr53.setStatus("current")
if mibBuilder.loadTexts:
    outBr53.setUnits("tenth of Mbps")
_OutStream54_ObjectIdentity = ObjectIdentity
outStream54 = _OutStream54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 59)
)
_OutBr54_Type = Integer32
_OutBr54_Object = MibScalar
outBr54 = _OutBr54_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 59, 1),
    _OutBr54_Type()
)
outBr54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr54.setStatus("current")
if mibBuilder.loadTexts:
    outBr54.setUnits("tenth of Mbps")
_OutStream55_ObjectIdentity = ObjectIdentity
outStream55 = _OutStream55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 60)
)
_OutBr55_Type = Integer32
_OutBr55_Object = MibScalar
outBr55 = _OutBr55_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 60, 1),
    _OutBr55_Type()
)
outBr55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr55.setStatus("current")
if mibBuilder.loadTexts:
    outBr55.setUnits("tenth of Mbps")
_OutStream56_ObjectIdentity = ObjectIdentity
outStream56 = _OutStream56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 61)
)
_OutBr56_Type = Integer32
_OutBr56_Object = MibScalar
outBr56 = _OutBr56_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 61, 1),
    _OutBr56_Type()
)
outBr56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr56.setStatus("current")
if mibBuilder.loadTexts:
    outBr56.setUnits("tenth of Mbps")
_OutStream57_ObjectIdentity = ObjectIdentity
outStream57 = _OutStream57_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 62)
)
_OutBr57_Type = Integer32
_OutBr57_Object = MibScalar
outBr57 = _OutBr57_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 62, 1),
    _OutBr57_Type()
)
outBr57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr57.setStatus("current")
if mibBuilder.loadTexts:
    outBr57.setUnits("tenth of Mbps")
_OutStream58_ObjectIdentity = ObjectIdentity
outStream58 = _OutStream58_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 63)
)
_OutBr58_Type = Integer32
_OutBr58_Object = MibScalar
outBr58 = _OutBr58_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 63, 1),
    _OutBr58_Type()
)
outBr58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr58.setStatus("current")
if mibBuilder.loadTexts:
    outBr58.setUnits("tenth of Mbps")
_OutStream59_ObjectIdentity = ObjectIdentity
outStream59 = _OutStream59_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 64)
)
_OutBr59_Type = Integer32
_OutBr59_Object = MibScalar
outBr59 = _OutBr59_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 64, 1),
    _OutBr59_Type()
)
outBr59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr59.setStatus("current")
if mibBuilder.loadTexts:
    outBr59.setUnits("tenth of Mbps")
_OutStream60_ObjectIdentity = ObjectIdentity
outStream60 = _OutStream60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 65)
)
_OutBr60_Type = Integer32
_OutBr60_Object = MibScalar
outBr60 = _OutBr60_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 65, 1),
    _OutBr60_Type()
)
outBr60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr60.setStatus("current")
if mibBuilder.loadTexts:
    outBr60.setUnits("tenth of Mbps")
_OutStream61_ObjectIdentity = ObjectIdentity
outStream61 = _OutStream61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 66)
)
_OutBr61_Type = Integer32
_OutBr61_Object = MibScalar
outBr61 = _OutBr61_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 66, 1),
    _OutBr61_Type()
)
outBr61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr61.setStatus("current")
if mibBuilder.loadTexts:
    outBr61.setUnits("tenth of Mbps")
_OutStream62_ObjectIdentity = ObjectIdentity
outStream62 = _OutStream62_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 67)
)
_OutBr62_Type = Integer32
_OutBr62_Object = MibScalar
outBr62 = _OutBr62_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 67, 1),
    _OutBr62_Type()
)
outBr62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr62.setStatus("current")
if mibBuilder.loadTexts:
    outBr62.setUnits("tenth of Mbps")
_OutStream63_ObjectIdentity = ObjectIdentity
outStream63 = _OutStream63_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 68)
)
_OutBr63_Type = Integer32
_OutBr63_Object = MibScalar
outBr63 = _OutBr63_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 68, 1),
    _OutBr63_Type()
)
outBr63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr63.setStatus("current")
if mibBuilder.loadTexts:
    outBr63.setUnits("tenth of Mbps")
_OutStream64_ObjectIdentity = ObjectIdentity
outStream64 = _OutStream64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 69)
)
_OutBr64_Type = Integer32
_OutBr64_Object = MibScalar
outBr64 = _OutBr64_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 69, 1),
    _OutBr64_Type()
)
outBr64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr64.setStatus("current")
if mibBuilder.loadTexts:
    outBr64.setUnits("tenth of Mbps")
_OutStream65_ObjectIdentity = ObjectIdentity
outStream65 = _OutStream65_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 70)
)
_OutBr65_Type = Integer32
_OutBr65_Object = MibScalar
outBr65 = _OutBr65_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 70, 1),
    _OutBr65_Type()
)
outBr65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr65.setStatus("current")
if mibBuilder.loadTexts:
    outBr65.setUnits("tenth of Mbps")
_OutStream66_ObjectIdentity = ObjectIdentity
outStream66 = _OutStream66_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 71)
)
_OutBr66_Type = Integer32
_OutBr66_Object = MibScalar
outBr66 = _OutBr66_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 71, 1),
    _OutBr66_Type()
)
outBr66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr66.setStatus("current")
if mibBuilder.loadTexts:
    outBr66.setUnits("tenth of Mbps")
_OutStream67_ObjectIdentity = ObjectIdentity
outStream67 = _OutStream67_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 72)
)
_OutBr67_Type = Integer32
_OutBr67_Object = MibScalar
outBr67 = _OutBr67_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 72, 1),
    _OutBr67_Type()
)
outBr67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr67.setStatus("current")
if mibBuilder.loadTexts:
    outBr67.setUnits("tenth of Mbps")
_OutStream68_ObjectIdentity = ObjectIdentity
outStream68 = _OutStream68_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 73)
)
_OutBr68_Type = Integer32
_OutBr68_Object = MibScalar
outBr68 = _OutBr68_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 73, 1),
    _OutBr68_Type()
)
outBr68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr68.setStatus("current")
if mibBuilder.loadTexts:
    outBr68.setUnits("tenth of Mbps")
_OutStream69_ObjectIdentity = ObjectIdentity
outStream69 = _OutStream69_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 74)
)
_OutBr69_Type = Integer32
_OutBr69_Object = MibScalar
outBr69 = _OutBr69_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 74, 1),
    _OutBr69_Type()
)
outBr69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr69.setStatus("current")
if mibBuilder.loadTexts:
    outBr69.setUnits("tenth of Mbps")
_OutStream70_ObjectIdentity = ObjectIdentity
outStream70 = _OutStream70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 75)
)
_OutBr70_Type = Integer32
_OutBr70_Object = MibScalar
outBr70 = _OutBr70_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 75, 1),
    _OutBr70_Type()
)
outBr70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr70.setStatus("current")
if mibBuilder.loadTexts:
    outBr70.setUnits("tenth of Mbps")
_OutStream71_ObjectIdentity = ObjectIdentity
outStream71 = _OutStream71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 76)
)
_OutBr71_Type = Integer32
_OutBr71_Object = MibScalar
outBr71 = _OutBr71_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 76, 1),
    _OutBr71_Type()
)
outBr71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr71.setStatus("current")
if mibBuilder.loadTexts:
    outBr71.setUnits("tenth of Mbps")
_OutStream72_ObjectIdentity = ObjectIdentity
outStream72 = _OutStream72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 77)
)
_OutBr72_Type = Integer32
_OutBr72_Object = MibScalar
outBr72 = _OutBr72_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 77, 1),
    _OutBr72_Type()
)
outBr72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr72.setStatus("current")
if mibBuilder.loadTexts:
    outBr72.setUnits("tenth of Mbps")
_OutStream73_ObjectIdentity = ObjectIdentity
outStream73 = _OutStream73_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 78)
)
_OutBr73_Type = Integer32
_OutBr73_Object = MibScalar
outBr73 = _OutBr73_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 78, 1),
    _OutBr73_Type()
)
outBr73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr73.setStatus("current")
if mibBuilder.loadTexts:
    outBr73.setUnits("tenth of Mbps")
_OutStream74_ObjectIdentity = ObjectIdentity
outStream74 = _OutStream74_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 79)
)
_OutBr74_Type = Integer32
_OutBr74_Object = MibScalar
outBr74 = _OutBr74_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 79, 1),
    _OutBr74_Type()
)
outBr74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr74.setStatus("current")
if mibBuilder.loadTexts:
    outBr74.setUnits("tenth of Mbps")
_OutStream75_ObjectIdentity = ObjectIdentity
outStream75 = _OutStream75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 80)
)
_OutBr75_Type = Integer32
_OutBr75_Object = MibScalar
outBr75 = _OutBr75_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 80, 1),
    _OutBr75_Type()
)
outBr75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr75.setStatus("current")
if mibBuilder.loadTexts:
    outBr75.setUnits("tenth of Mbps")
_OutStream76_ObjectIdentity = ObjectIdentity
outStream76 = _OutStream76_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 81)
)
_OutBr76_Type = Integer32
_OutBr76_Object = MibScalar
outBr76 = _OutBr76_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 81, 1),
    _OutBr76_Type()
)
outBr76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr76.setStatus("current")
if mibBuilder.loadTexts:
    outBr76.setUnits("tenth of Mbps")
_OutStream77_ObjectIdentity = ObjectIdentity
outStream77 = _OutStream77_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 82)
)
_OutBr77_Type = Integer32
_OutBr77_Object = MibScalar
outBr77 = _OutBr77_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 82, 1),
    _OutBr77_Type()
)
outBr77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr77.setStatus("current")
if mibBuilder.loadTexts:
    outBr77.setUnits("tenth of Mbps")
_OutStream78_ObjectIdentity = ObjectIdentity
outStream78 = _OutStream78_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 83)
)
_OutBr78_Type = Integer32
_OutBr78_Object = MibScalar
outBr78 = _OutBr78_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 83, 1),
    _OutBr78_Type()
)
outBr78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr78.setStatus("current")
if mibBuilder.loadTexts:
    outBr78.setUnits("tenth of Mbps")
_OutStream79_ObjectIdentity = ObjectIdentity
outStream79 = _OutStream79_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 84)
)
_OutBr79_Type = Integer32
_OutBr79_Object = MibScalar
outBr79 = _OutBr79_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 84, 1),
    _OutBr79_Type()
)
outBr79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr79.setStatus("current")
if mibBuilder.loadTexts:
    outBr79.setUnits("tenth of Mbps")
_OutStream80_ObjectIdentity = ObjectIdentity
outStream80 = _OutStream80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 85)
)
_OutBr80_Type = Integer32
_OutBr80_Object = MibScalar
outBr80 = _OutBr80_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 85, 1),
    _OutBr80_Type()
)
outBr80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr80.setStatus("current")
if mibBuilder.loadTexts:
    outBr80.setUnits("tenth of Mbps")
_OutStream81_ObjectIdentity = ObjectIdentity
outStream81 = _OutStream81_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 86)
)
_OutBr81_Type = Integer32
_OutBr81_Object = MibScalar
outBr81 = _OutBr81_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 86, 1),
    _OutBr81_Type()
)
outBr81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr81.setStatus("current")
if mibBuilder.loadTexts:
    outBr81.setUnits("tenth of Mbps")
_OutStream82_ObjectIdentity = ObjectIdentity
outStream82 = _OutStream82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 87)
)
_OutBr82_Type = Integer32
_OutBr82_Object = MibScalar
outBr82 = _OutBr82_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 87, 1),
    _OutBr82_Type()
)
outBr82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr82.setStatus("current")
if mibBuilder.loadTexts:
    outBr82.setUnits("tenth of Mbps")
_OutStream83_ObjectIdentity = ObjectIdentity
outStream83 = _OutStream83_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 88)
)
_OutBr83_Type = Integer32
_OutBr83_Object = MibScalar
outBr83 = _OutBr83_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 88, 1),
    _OutBr83_Type()
)
outBr83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr83.setStatus("current")
if mibBuilder.loadTexts:
    outBr83.setUnits("tenth of Mbps")
_OutStream84_ObjectIdentity = ObjectIdentity
outStream84 = _OutStream84_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 89)
)
_OutBr84_Type = Integer32
_OutBr84_Object = MibScalar
outBr84 = _OutBr84_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 89, 1),
    _OutBr84_Type()
)
outBr84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr84.setStatus("current")
if mibBuilder.loadTexts:
    outBr84.setUnits("tenth of Mbps")
_OutStream85_ObjectIdentity = ObjectIdentity
outStream85 = _OutStream85_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 90)
)
_OutBr85_Type = Integer32
_OutBr85_Object = MibScalar
outBr85 = _OutBr85_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 90, 1),
    _OutBr85_Type()
)
outBr85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr85.setStatus("current")
if mibBuilder.loadTexts:
    outBr85.setUnits("tenth of Mbps")
_OutStream86_ObjectIdentity = ObjectIdentity
outStream86 = _OutStream86_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 91)
)
_OutBr86_Type = Integer32
_OutBr86_Object = MibScalar
outBr86 = _OutBr86_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 91, 1),
    _OutBr86_Type()
)
outBr86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr86.setStatus("current")
if mibBuilder.loadTexts:
    outBr86.setUnits("tenth of Mbps")
_OutStream87_ObjectIdentity = ObjectIdentity
outStream87 = _OutStream87_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 92)
)
_OutBr87_Type = Integer32
_OutBr87_Object = MibScalar
outBr87 = _OutBr87_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 92, 1),
    _OutBr87_Type()
)
outBr87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr87.setStatus("current")
if mibBuilder.loadTexts:
    outBr87.setUnits("tenth of Mbps")
_OutStream88_ObjectIdentity = ObjectIdentity
outStream88 = _OutStream88_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 93)
)
_OutBr88_Type = Integer32
_OutBr88_Object = MibScalar
outBr88 = _OutBr88_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 93, 1),
    _OutBr88_Type()
)
outBr88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr88.setStatus("current")
if mibBuilder.loadTexts:
    outBr88.setUnits("tenth of Mbps")
_OutStream89_ObjectIdentity = ObjectIdentity
outStream89 = _OutStream89_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 94)
)
_OutBr89_Type = Integer32
_OutBr89_Object = MibScalar
outBr89 = _OutBr89_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 94, 1),
    _OutBr89_Type()
)
outBr89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr89.setStatus("current")
if mibBuilder.loadTexts:
    outBr89.setUnits("tenth of Mbps")
_OutStream90_ObjectIdentity = ObjectIdentity
outStream90 = _OutStream90_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 95)
)
_OutBr90_Type = Integer32
_OutBr90_Object = MibScalar
outBr90 = _OutBr90_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 95, 1),
    _OutBr90_Type()
)
outBr90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr90.setStatus("current")
if mibBuilder.loadTexts:
    outBr90.setUnits("tenth of Mbps")
_OutStream91_ObjectIdentity = ObjectIdentity
outStream91 = _OutStream91_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 96)
)
_OutBr91_Type = Integer32
_OutBr91_Object = MibScalar
outBr91 = _OutBr91_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 96, 1),
    _OutBr91_Type()
)
outBr91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr91.setStatus("current")
if mibBuilder.loadTexts:
    outBr91.setUnits("tenth of Mbps")
_OutStream92_ObjectIdentity = ObjectIdentity
outStream92 = _OutStream92_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 97)
)
_OutBr92_Type = Integer32
_OutBr92_Object = MibScalar
outBr92 = _OutBr92_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 97, 1),
    _OutBr92_Type()
)
outBr92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr92.setStatus("current")
if mibBuilder.loadTexts:
    outBr92.setUnits("tenth of Mbps")
_OutStream93_ObjectIdentity = ObjectIdentity
outStream93 = _OutStream93_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 98)
)
_OutBr93_Type = Integer32
_OutBr93_Object = MibScalar
outBr93 = _OutBr93_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 98, 1),
    _OutBr93_Type()
)
outBr93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr93.setStatus("current")
if mibBuilder.loadTexts:
    outBr93.setUnits("tenth of Mbps")
_OutStream94_ObjectIdentity = ObjectIdentity
outStream94 = _OutStream94_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 99)
)
_OutBr94_Type = Integer32
_OutBr94_Object = MibScalar
outBr94 = _OutBr94_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 99, 1),
    _OutBr94_Type()
)
outBr94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr94.setStatus("current")
if mibBuilder.loadTexts:
    outBr94.setUnits("tenth of Mbps")
_OutStream95_ObjectIdentity = ObjectIdentity
outStream95 = _OutStream95_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 100)
)
_OutBr95_Type = Integer32
_OutBr95_Object = MibScalar
outBr95 = _OutBr95_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 100, 1),
    _OutBr95_Type()
)
outBr95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr95.setStatus("current")
if mibBuilder.loadTexts:
    outBr95.setUnits("tenth of Mbps")
_OutStream96_ObjectIdentity = ObjectIdentity
outStream96 = _OutStream96_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 101)
)
_OutBr96_Type = Integer32
_OutBr96_Object = MibScalar
outBr96 = _OutBr96_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 101, 1),
    _OutBr96_Type()
)
outBr96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr96.setStatus("current")
if mibBuilder.loadTexts:
    outBr96.setUnits("tenth of Mbps")
_OutStream97_ObjectIdentity = ObjectIdentity
outStream97 = _OutStream97_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 102)
)
_OutBr97_Type = Integer32
_OutBr97_Object = MibScalar
outBr97 = _OutBr97_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 102, 1),
    _OutBr97_Type()
)
outBr97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr97.setStatus("current")
if mibBuilder.loadTexts:
    outBr97.setUnits("tenth of Mbps")
_OutStream98_ObjectIdentity = ObjectIdentity
outStream98 = _OutStream98_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 103)
)
_OutBr98_Type = Integer32
_OutBr98_Object = MibScalar
outBr98 = _OutBr98_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 103, 1),
    _OutBr98_Type()
)
outBr98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr98.setStatus("current")
if mibBuilder.loadTexts:
    outBr98.setUnits("tenth of Mbps")
_OutStream99_ObjectIdentity = ObjectIdentity
outStream99 = _OutStream99_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 104)
)
_OutBr99_Type = Integer32
_OutBr99_Object = MibScalar
outBr99 = _OutBr99_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 104, 1),
    _OutBr99_Type()
)
outBr99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr99.setStatus("current")
if mibBuilder.loadTexts:
    outBr99.setUnits("tenth of Mbps")
_OutStream100_ObjectIdentity = ObjectIdentity
outStream100 = _OutStream100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 105)
)
_OutBr100_Type = Integer32
_OutBr100_Object = MibScalar
outBr100 = _OutBr100_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 105, 1),
    _OutBr100_Type()
)
outBr100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr100.setStatus("current")
if mibBuilder.loadTexts:
    outBr100.setUnits("tenth of Mbps")
_OutStream101_ObjectIdentity = ObjectIdentity
outStream101 = _OutStream101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 106)
)
_OutBr101_Type = Integer32
_OutBr101_Object = MibScalar
outBr101 = _OutBr101_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 106, 1),
    _OutBr101_Type()
)
outBr101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr101.setStatus("current")
if mibBuilder.loadTexts:
    outBr101.setUnits("tenth of Mbps")
_OutStream102_ObjectIdentity = ObjectIdentity
outStream102 = _OutStream102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 107)
)
_OutBr102_Type = Integer32
_OutBr102_Object = MibScalar
outBr102 = _OutBr102_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 107, 1),
    _OutBr102_Type()
)
outBr102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr102.setStatus("current")
if mibBuilder.loadTexts:
    outBr102.setUnits("tenth of Mbps")
_OutStream103_ObjectIdentity = ObjectIdentity
outStream103 = _OutStream103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 108)
)
_OutBr103_Type = Integer32
_OutBr103_Object = MibScalar
outBr103 = _OutBr103_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 108, 1),
    _OutBr103_Type()
)
outBr103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr103.setStatus("current")
if mibBuilder.loadTexts:
    outBr103.setUnits("tenth of Mbps")
_OutStream104_ObjectIdentity = ObjectIdentity
outStream104 = _OutStream104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 109)
)
_OutBr104_Type = Integer32
_OutBr104_Object = MibScalar
outBr104 = _OutBr104_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 109, 1),
    _OutBr104_Type()
)
outBr104.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr104.setStatus("current")
if mibBuilder.loadTexts:
    outBr104.setUnits("tenth of Mbps")
_OutStream105_ObjectIdentity = ObjectIdentity
outStream105 = _OutStream105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 110)
)
_OutBr105_Type = Integer32
_OutBr105_Object = MibScalar
outBr105 = _OutBr105_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 110, 1),
    _OutBr105_Type()
)
outBr105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr105.setStatus("current")
if mibBuilder.loadTexts:
    outBr105.setUnits("tenth of Mbps")
_OutStream106_ObjectIdentity = ObjectIdentity
outStream106 = _OutStream106_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 111)
)
_OutBr106_Type = Integer32
_OutBr106_Object = MibScalar
outBr106 = _OutBr106_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 111, 1),
    _OutBr106_Type()
)
outBr106.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr106.setStatus("current")
if mibBuilder.loadTexts:
    outBr106.setUnits("tenth of Mbps")
_OutStream107_ObjectIdentity = ObjectIdentity
outStream107 = _OutStream107_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 112)
)
_OutBr107_Type = Integer32
_OutBr107_Object = MibScalar
outBr107 = _OutBr107_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 112, 1),
    _OutBr107_Type()
)
outBr107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr107.setStatus("current")
if mibBuilder.loadTexts:
    outBr107.setUnits("tenth of Mbps")
_OutStream108_ObjectIdentity = ObjectIdentity
outStream108 = _OutStream108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 113)
)
_OutBr108_Type = Integer32
_OutBr108_Object = MibScalar
outBr108 = _OutBr108_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 113, 1),
    _OutBr108_Type()
)
outBr108.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr108.setStatus("current")
if mibBuilder.loadTexts:
    outBr108.setUnits("tenth of Mbps")
_OutStream109_ObjectIdentity = ObjectIdentity
outStream109 = _OutStream109_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 114)
)
_OutBr109_Type = Integer32
_OutBr109_Object = MibScalar
outBr109 = _OutBr109_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 114, 1),
    _OutBr109_Type()
)
outBr109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr109.setStatus("current")
if mibBuilder.loadTexts:
    outBr109.setUnits("tenth of Mbps")
_OutStream110_ObjectIdentity = ObjectIdentity
outStream110 = _OutStream110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 115)
)
_OutBr110_Type = Integer32
_OutBr110_Object = MibScalar
outBr110 = _OutBr110_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 115, 1),
    _OutBr110_Type()
)
outBr110.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr110.setStatus("current")
if mibBuilder.loadTexts:
    outBr110.setUnits("tenth of Mbps")
_OutStream111_ObjectIdentity = ObjectIdentity
outStream111 = _OutStream111_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 116)
)
_OutBr111_Type = Integer32
_OutBr111_Object = MibScalar
outBr111 = _OutBr111_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 116, 1),
    _OutBr111_Type()
)
outBr111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr111.setStatus("current")
if mibBuilder.loadTexts:
    outBr111.setUnits("tenth of Mbps")
_OutStream112_ObjectIdentity = ObjectIdentity
outStream112 = _OutStream112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 117)
)
_OutBr112_Type = Integer32
_OutBr112_Object = MibScalar
outBr112 = _OutBr112_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 117, 1),
    _OutBr112_Type()
)
outBr112.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr112.setStatus("current")
if mibBuilder.loadTexts:
    outBr112.setUnits("tenth of Mbps")
_OutStream113_ObjectIdentity = ObjectIdentity
outStream113 = _OutStream113_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 118)
)
_OutBr113_Type = Integer32
_OutBr113_Object = MibScalar
outBr113 = _OutBr113_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 118, 1),
    _OutBr113_Type()
)
outBr113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr113.setStatus("current")
if mibBuilder.loadTexts:
    outBr113.setUnits("tenth of Mbps")
_OutStream114_ObjectIdentity = ObjectIdentity
outStream114 = _OutStream114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 119)
)
_OutBr114_Type = Integer32
_OutBr114_Object = MibScalar
outBr114 = _OutBr114_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 119, 1),
    _OutBr114_Type()
)
outBr114.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr114.setStatus("current")
if mibBuilder.loadTexts:
    outBr114.setUnits("tenth of Mbps")
_OutStream115_ObjectIdentity = ObjectIdentity
outStream115 = _OutStream115_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 120)
)
_OutBr115_Type = Integer32
_OutBr115_Object = MibScalar
outBr115 = _OutBr115_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 120, 1),
    _OutBr115_Type()
)
outBr115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr115.setStatus("current")
if mibBuilder.loadTexts:
    outBr115.setUnits("tenth of Mbps")
_OutStream116_ObjectIdentity = ObjectIdentity
outStream116 = _OutStream116_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 121)
)
_OutBr116_Type = Integer32
_OutBr116_Object = MibScalar
outBr116 = _OutBr116_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 121, 1),
    _OutBr116_Type()
)
outBr116.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr116.setStatus("current")
if mibBuilder.loadTexts:
    outBr116.setUnits("tenth of Mbps")
_OutStream117_ObjectIdentity = ObjectIdentity
outStream117 = _OutStream117_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 122)
)
_OutBr117_Type = Integer32
_OutBr117_Object = MibScalar
outBr117 = _OutBr117_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 122, 1),
    _OutBr117_Type()
)
outBr117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr117.setStatus("current")
if mibBuilder.loadTexts:
    outBr117.setUnits("tenth of Mbps")
_OutStream118_ObjectIdentity = ObjectIdentity
outStream118 = _OutStream118_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 123)
)
_OutBr118_Type = Integer32
_OutBr118_Object = MibScalar
outBr118 = _OutBr118_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 123, 1),
    _OutBr118_Type()
)
outBr118.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr118.setStatus("current")
if mibBuilder.loadTexts:
    outBr118.setUnits("tenth of Mbps")
_OutStream119_ObjectIdentity = ObjectIdentity
outStream119 = _OutStream119_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 124)
)
_OutBr119_Type = Integer32
_OutBr119_Object = MibScalar
outBr119 = _OutBr119_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 124, 1),
    _OutBr119_Type()
)
outBr119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr119.setStatus("current")
if mibBuilder.loadTexts:
    outBr119.setUnits("tenth of Mbps")
_OutStream120_ObjectIdentity = ObjectIdentity
outStream120 = _OutStream120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 125)
)
_OutBr120_Type = Integer32
_OutBr120_Object = MibScalar
outBr120 = _OutBr120_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 125, 1),
    _OutBr120_Type()
)
outBr120.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr120.setStatus("current")
if mibBuilder.loadTexts:
    outBr120.setUnits("tenth of Mbps")
_OutStream121_ObjectIdentity = ObjectIdentity
outStream121 = _OutStream121_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 126)
)
_OutBr121_Type = Integer32
_OutBr121_Object = MibScalar
outBr121 = _OutBr121_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 126, 1),
    _OutBr121_Type()
)
outBr121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr121.setStatus("current")
if mibBuilder.loadTexts:
    outBr121.setUnits("tenth of Mbps")
_OutStream122_ObjectIdentity = ObjectIdentity
outStream122 = _OutStream122_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 127)
)
_OutBr122_Type = Integer32
_OutBr122_Object = MibScalar
outBr122 = _OutBr122_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 127, 1),
    _OutBr122_Type()
)
outBr122.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr122.setStatus("current")
if mibBuilder.loadTexts:
    outBr122.setUnits("tenth of Mbps")
_OutStream123_ObjectIdentity = ObjectIdentity
outStream123 = _OutStream123_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 128)
)
_OutBr123_Type = Integer32
_OutBr123_Object = MibScalar
outBr123 = _OutBr123_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 128, 1),
    _OutBr123_Type()
)
outBr123.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr123.setStatus("current")
if mibBuilder.loadTexts:
    outBr123.setUnits("tenth of Mbps")
_OutStream124_ObjectIdentity = ObjectIdentity
outStream124 = _OutStream124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 129)
)
_OutBr124_Type = Integer32
_OutBr124_Object = MibScalar
outBr124 = _OutBr124_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 129, 1),
    _OutBr124_Type()
)
outBr124.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr124.setStatus("current")
if mibBuilder.loadTexts:
    outBr124.setUnits("tenth of Mbps")
_OutStream125_ObjectIdentity = ObjectIdentity
outStream125 = _OutStream125_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 130)
)
_OutBr125_Type = Integer32
_OutBr125_Object = MibScalar
outBr125 = _OutBr125_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 130, 1),
    _OutBr125_Type()
)
outBr125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr125.setStatus("current")
if mibBuilder.loadTexts:
    outBr125.setUnits("tenth of Mbps")
_OutStream126_ObjectIdentity = ObjectIdentity
outStream126 = _OutStream126_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 131)
)
_OutBr126_Type = Integer32
_OutBr126_Object = MibScalar
outBr126 = _OutBr126_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 131, 1),
    _OutBr126_Type()
)
outBr126.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr126.setStatus("current")
if mibBuilder.loadTexts:
    outBr126.setUnits("tenth of Mbps")
_OutStream127_ObjectIdentity = ObjectIdentity
outStream127 = _OutStream127_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 132)
)
_OutBr127_Type = Integer32
_OutBr127_Object = MibScalar
outBr127 = _OutBr127_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 132, 1),
    _OutBr127_Type()
)
outBr127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr127.setStatus("current")
if mibBuilder.loadTexts:
    outBr127.setUnits("tenth of Mbps")
_OutStream128_ObjectIdentity = ObjectIdentity
outStream128 = _OutStream128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 133)
)
_OutBr128_Type = Integer32
_OutBr128_Object = MibScalar
outBr128 = _OutBr128_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 133, 1),
    _OutBr128_Type()
)
outBr128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr128.setStatus("current")
if mibBuilder.loadTexts:
    outBr128.setUnits("tenth of Mbps")
_OutStream129_ObjectIdentity = ObjectIdentity
outStream129 = _OutStream129_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 134)
)
_OutBr129_Type = Integer32
_OutBr129_Object = MibScalar
outBr129 = _OutBr129_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 134, 1),
    _OutBr129_Type()
)
outBr129.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr129.setStatus("current")
if mibBuilder.loadTexts:
    outBr129.setUnits("tenth of Mbps")
_OutStream130_ObjectIdentity = ObjectIdentity
outStream130 = _OutStream130_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 135)
)
_OutBr130_Type = Integer32
_OutBr130_Object = MibScalar
outBr130 = _OutBr130_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 135, 1),
    _OutBr130_Type()
)
outBr130.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr130.setStatus("current")
if mibBuilder.loadTexts:
    outBr130.setUnits("tenth of Mbps")
_OutStream131_ObjectIdentity = ObjectIdentity
outStream131 = _OutStream131_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 136)
)
_OutBr131_Type = Integer32
_OutBr131_Object = MibScalar
outBr131 = _OutBr131_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 136, 1),
    _OutBr131_Type()
)
outBr131.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr131.setStatus("current")
if mibBuilder.loadTexts:
    outBr131.setUnits("tenth of Mbps")
_OutStream132_ObjectIdentity = ObjectIdentity
outStream132 = _OutStream132_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 137)
)
_OutBr132_Type = Integer32
_OutBr132_Object = MibScalar
outBr132 = _OutBr132_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 137, 1),
    _OutBr132_Type()
)
outBr132.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr132.setStatus("current")
if mibBuilder.loadTexts:
    outBr132.setUnits("tenth of Mbps")
_OutStream133_ObjectIdentity = ObjectIdentity
outStream133 = _OutStream133_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 138)
)
_OutBr133_Type = Integer32
_OutBr133_Object = MibScalar
outBr133 = _OutBr133_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 138, 1),
    _OutBr133_Type()
)
outBr133.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr133.setStatus("current")
if mibBuilder.loadTexts:
    outBr133.setUnits("tenth of Mbps")
_OutStream134_ObjectIdentity = ObjectIdentity
outStream134 = _OutStream134_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 139)
)
_OutBr134_Type = Integer32
_OutBr134_Object = MibScalar
outBr134 = _OutBr134_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 139, 1),
    _OutBr134_Type()
)
outBr134.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr134.setStatus("current")
if mibBuilder.loadTexts:
    outBr134.setUnits("tenth of Mbps")
_OutStream135_ObjectIdentity = ObjectIdentity
outStream135 = _OutStream135_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 140)
)
_OutBr135_Type = Integer32
_OutBr135_Object = MibScalar
outBr135 = _OutBr135_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 140, 1),
    _OutBr135_Type()
)
outBr135.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr135.setStatus("current")
if mibBuilder.loadTexts:
    outBr135.setUnits("tenth of Mbps")
_OutStream136_ObjectIdentity = ObjectIdentity
outStream136 = _OutStream136_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 141)
)
_OutBr136_Type = Integer32
_OutBr136_Object = MibScalar
outBr136 = _OutBr136_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 141, 1),
    _OutBr136_Type()
)
outBr136.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr136.setStatus("current")
if mibBuilder.loadTexts:
    outBr136.setUnits("tenth of Mbps")
_OutStream137_ObjectIdentity = ObjectIdentity
outStream137 = _OutStream137_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 142)
)
_OutBr137_Type = Integer32
_OutBr137_Object = MibScalar
outBr137 = _OutBr137_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 142, 1),
    _OutBr137_Type()
)
outBr137.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr137.setStatus("current")
if mibBuilder.loadTexts:
    outBr137.setUnits("tenth of Mbps")
_OutStream138_ObjectIdentity = ObjectIdentity
outStream138 = _OutStream138_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 143)
)
_OutBr138_Type = Integer32
_OutBr138_Object = MibScalar
outBr138 = _OutBr138_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 143, 1),
    _OutBr138_Type()
)
outBr138.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr138.setStatus("current")
if mibBuilder.loadTexts:
    outBr138.setUnits("tenth of Mbps")
_OutStream139_ObjectIdentity = ObjectIdentity
outStream139 = _OutStream139_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 144)
)
_OutBr139_Type = Integer32
_OutBr139_Object = MibScalar
outBr139 = _OutBr139_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 144, 1),
    _OutBr139_Type()
)
outBr139.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr139.setStatus("current")
if mibBuilder.loadTexts:
    outBr139.setUnits("tenth of Mbps")
_OutStream140_ObjectIdentity = ObjectIdentity
outStream140 = _OutStream140_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 145)
)
_OutBr140_Type = Integer32
_OutBr140_Object = MibScalar
outBr140 = _OutBr140_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 145, 1),
    _OutBr140_Type()
)
outBr140.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr140.setStatus("current")
if mibBuilder.loadTexts:
    outBr140.setUnits("tenth of Mbps")
_OutStream141_ObjectIdentity = ObjectIdentity
outStream141 = _OutStream141_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 146)
)
_OutBr141_Type = Integer32
_OutBr141_Object = MibScalar
outBr141 = _OutBr141_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 146, 1),
    _OutBr141_Type()
)
outBr141.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr141.setStatus("current")
if mibBuilder.loadTexts:
    outBr141.setUnits("tenth of Mbps")
_OutStream142_ObjectIdentity = ObjectIdentity
outStream142 = _OutStream142_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 147)
)
_OutBr142_Type = Integer32
_OutBr142_Object = MibScalar
outBr142 = _OutBr142_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 147, 1),
    _OutBr142_Type()
)
outBr142.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr142.setStatus("current")
if mibBuilder.loadTexts:
    outBr142.setUnits("tenth of Mbps")
_OutStream143_ObjectIdentity = ObjectIdentity
outStream143 = _OutStream143_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 148)
)
_OutBr143_Type = Integer32
_OutBr143_Object = MibScalar
outBr143 = _OutBr143_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 148, 1),
    _OutBr143_Type()
)
outBr143.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr143.setStatus("current")
if mibBuilder.loadTexts:
    outBr143.setUnits("tenth of Mbps")
_OutStream144_ObjectIdentity = ObjectIdentity
outStream144 = _OutStream144_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 149)
)
_OutBr144_Type = Integer32
_OutBr144_Object = MibScalar
outBr144 = _OutBr144_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 149, 1),
    _OutBr144_Type()
)
outBr144.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr144.setStatus("current")
if mibBuilder.loadTexts:
    outBr144.setUnits("tenth of Mbps")
_OutStream145_ObjectIdentity = ObjectIdentity
outStream145 = _OutStream145_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 150)
)
_OutBr145_Type = Integer32
_OutBr145_Object = MibScalar
outBr145 = _OutBr145_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 150, 1),
    _OutBr145_Type()
)
outBr145.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr145.setStatus("current")
if mibBuilder.loadTexts:
    outBr145.setUnits("tenth of Mbps")
_OutStream146_ObjectIdentity = ObjectIdentity
outStream146 = _OutStream146_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 151)
)
_OutBr146_Type = Integer32
_OutBr146_Object = MibScalar
outBr146 = _OutBr146_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 151, 1),
    _OutBr146_Type()
)
outBr146.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr146.setStatus("current")
if mibBuilder.loadTexts:
    outBr146.setUnits("tenth of Mbps")
_OutStream147_ObjectIdentity = ObjectIdentity
outStream147 = _OutStream147_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 152)
)
_OutBr147_Type = Integer32
_OutBr147_Object = MibScalar
outBr147 = _OutBr147_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 152, 1),
    _OutBr147_Type()
)
outBr147.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr147.setStatus("current")
if mibBuilder.loadTexts:
    outBr147.setUnits("tenth of Mbps")
_OutStream148_ObjectIdentity = ObjectIdentity
outStream148 = _OutStream148_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 153)
)
_OutBr148_Type = Integer32
_OutBr148_Object = MibScalar
outBr148 = _OutBr148_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 153, 1),
    _OutBr148_Type()
)
outBr148.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr148.setStatus("current")
if mibBuilder.loadTexts:
    outBr148.setUnits("tenth of Mbps")
_OutStream149_ObjectIdentity = ObjectIdentity
outStream149 = _OutStream149_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 154)
)
_OutBr149_Type = Integer32
_OutBr149_Object = MibScalar
outBr149 = _OutBr149_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 154, 1),
    _OutBr149_Type()
)
outBr149.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr149.setStatus("current")
if mibBuilder.loadTexts:
    outBr149.setUnits("tenth of Mbps")
_OutStream150_ObjectIdentity = ObjectIdentity
outStream150 = _OutStream150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 155)
)
_OutBr150_Type = Integer32
_OutBr150_Object = MibScalar
outBr150 = _OutBr150_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 155, 1),
    _OutBr150_Type()
)
outBr150.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr150.setStatus("current")
if mibBuilder.loadTexts:
    outBr150.setUnits("tenth of Mbps")
_OutStream151_ObjectIdentity = ObjectIdentity
outStream151 = _OutStream151_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 156)
)
_OutBr151_Type = Integer32
_OutBr151_Object = MibScalar
outBr151 = _OutBr151_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 156, 1),
    _OutBr151_Type()
)
outBr151.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr151.setStatus("current")
if mibBuilder.loadTexts:
    outBr151.setUnits("tenth of Mbps")
_OutStream152_ObjectIdentity = ObjectIdentity
outStream152 = _OutStream152_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 157)
)
_OutBr152_Type = Integer32
_OutBr152_Object = MibScalar
outBr152 = _OutBr152_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 157, 1),
    _OutBr152_Type()
)
outBr152.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr152.setStatus("current")
if mibBuilder.loadTexts:
    outBr152.setUnits("tenth of Mbps")
_OutStream153_ObjectIdentity = ObjectIdentity
outStream153 = _OutStream153_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 158)
)
_OutBr153_Type = Integer32
_OutBr153_Object = MibScalar
outBr153 = _OutBr153_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 158, 1),
    _OutBr153_Type()
)
outBr153.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr153.setStatus("current")
if mibBuilder.loadTexts:
    outBr153.setUnits("tenth of Mbps")
_OutStream154_ObjectIdentity = ObjectIdentity
outStream154 = _OutStream154_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 159)
)
_OutBr154_Type = Integer32
_OutBr154_Object = MibScalar
outBr154 = _OutBr154_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 159, 1),
    _OutBr154_Type()
)
outBr154.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr154.setStatus("current")
if mibBuilder.loadTexts:
    outBr154.setUnits("tenth of Mbps")
_OutStream155_ObjectIdentity = ObjectIdentity
outStream155 = _OutStream155_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 160)
)
_OutBr155_Type = Integer32
_OutBr155_Object = MibScalar
outBr155 = _OutBr155_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 160, 1),
    _OutBr155_Type()
)
outBr155.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr155.setStatus("current")
if mibBuilder.loadTexts:
    outBr155.setUnits("tenth of Mbps")
_OutStream156_ObjectIdentity = ObjectIdentity
outStream156 = _OutStream156_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 161)
)
_OutBr156_Type = Integer32
_OutBr156_Object = MibScalar
outBr156 = _OutBr156_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 161, 1),
    _OutBr156_Type()
)
outBr156.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr156.setStatus("current")
if mibBuilder.loadTexts:
    outBr156.setUnits("tenth of Mbps")
_OutStream157_ObjectIdentity = ObjectIdentity
outStream157 = _OutStream157_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 162)
)
_OutBr157_Type = Integer32
_OutBr157_Object = MibScalar
outBr157 = _OutBr157_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 162, 1),
    _OutBr157_Type()
)
outBr157.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr157.setStatus("current")
if mibBuilder.loadTexts:
    outBr157.setUnits("tenth of Mbps")
_OutStream158_ObjectIdentity = ObjectIdentity
outStream158 = _OutStream158_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 163)
)
_OutBr158_Type = Integer32
_OutBr158_Object = MibScalar
outBr158 = _OutBr158_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 163, 1),
    _OutBr158_Type()
)
outBr158.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr158.setStatus("current")
if mibBuilder.loadTexts:
    outBr158.setUnits("tenth of Mbps")
_OutStream159_ObjectIdentity = ObjectIdentity
outStream159 = _OutStream159_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 164)
)
_OutBr159_Type = Integer32
_OutBr159_Object = MibScalar
outBr159 = _OutBr159_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 164, 1),
    _OutBr159_Type()
)
outBr159.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr159.setStatus("current")
if mibBuilder.loadTexts:
    outBr159.setUnits("tenth of Mbps")
_OutStream160_ObjectIdentity = ObjectIdentity
outStream160 = _OutStream160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 165)
)
_OutBr160_Type = Integer32
_OutBr160_Object = MibScalar
outBr160 = _OutBr160_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 165, 1),
    _OutBr160_Type()
)
outBr160.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr160.setStatus("current")
if mibBuilder.loadTexts:
    outBr160.setUnits("tenth of Mbps")
_OutStream161_ObjectIdentity = ObjectIdentity
outStream161 = _OutStream161_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 166)
)
_OutBr161_Type = Integer32
_OutBr161_Object = MibScalar
outBr161 = _OutBr161_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 166, 1),
    _OutBr161_Type()
)
outBr161.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr161.setStatus("current")
if mibBuilder.loadTexts:
    outBr161.setUnits("tenth of Mbps")
_OutStream162_ObjectIdentity = ObjectIdentity
outStream162 = _OutStream162_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 167)
)
_OutBr162_Type = Integer32
_OutBr162_Object = MibScalar
outBr162 = _OutBr162_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 167, 1),
    _OutBr162_Type()
)
outBr162.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr162.setStatus("current")
if mibBuilder.loadTexts:
    outBr162.setUnits("tenth of Mbps")
_OutStream163_ObjectIdentity = ObjectIdentity
outStream163 = _OutStream163_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 168)
)
_OutBr163_Type = Integer32
_OutBr163_Object = MibScalar
outBr163 = _OutBr163_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 168, 1),
    _OutBr163_Type()
)
outBr163.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr163.setStatus("current")
if mibBuilder.loadTexts:
    outBr163.setUnits("tenth of Mbps")
_OutStream164_ObjectIdentity = ObjectIdentity
outStream164 = _OutStream164_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 169)
)
_OutBr164_Type = Integer32
_OutBr164_Object = MibScalar
outBr164 = _OutBr164_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 169, 1),
    _OutBr164_Type()
)
outBr164.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr164.setStatus("current")
if mibBuilder.loadTexts:
    outBr164.setUnits("tenth of Mbps")
_OutStream165_ObjectIdentity = ObjectIdentity
outStream165 = _OutStream165_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 170)
)
_OutBr165_Type = Integer32
_OutBr165_Object = MibScalar
outBr165 = _OutBr165_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 170, 1),
    _OutBr165_Type()
)
outBr165.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr165.setStatus("current")
if mibBuilder.loadTexts:
    outBr165.setUnits("tenth of Mbps")
_OutStream166_ObjectIdentity = ObjectIdentity
outStream166 = _OutStream166_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 171)
)
_OutBr166_Type = Integer32
_OutBr166_Object = MibScalar
outBr166 = _OutBr166_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 171, 1),
    _OutBr166_Type()
)
outBr166.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr166.setStatus("current")
if mibBuilder.loadTexts:
    outBr166.setUnits("tenth of Mbps")
_OutStream167_ObjectIdentity = ObjectIdentity
outStream167 = _OutStream167_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 172)
)
_OutBr167_Type = Integer32
_OutBr167_Object = MibScalar
outBr167 = _OutBr167_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 172, 1),
    _OutBr167_Type()
)
outBr167.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr167.setStatus("current")
if mibBuilder.loadTexts:
    outBr167.setUnits("tenth of Mbps")
_OutStream168_ObjectIdentity = ObjectIdentity
outStream168 = _OutStream168_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 173)
)
_OutBr168_Type = Integer32
_OutBr168_Object = MibScalar
outBr168 = _OutBr168_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 173, 1),
    _OutBr168_Type()
)
outBr168.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr168.setStatus("current")
if mibBuilder.loadTexts:
    outBr168.setUnits("tenth of Mbps")
_OutStream169_ObjectIdentity = ObjectIdentity
outStream169 = _OutStream169_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 174)
)
_OutBr169_Type = Integer32
_OutBr169_Object = MibScalar
outBr169 = _OutBr169_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 174, 1),
    _OutBr169_Type()
)
outBr169.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr169.setStatus("current")
if mibBuilder.loadTexts:
    outBr169.setUnits("tenth of Mbps")
_OutStream170_ObjectIdentity = ObjectIdentity
outStream170 = _OutStream170_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 175)
)
_OutBr170_Type = Integer32
_OutBr170_Object = MibScalar
outBr170 = _OutBr170_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 175, 1),
    _OutBr170_Type()
)
outBr170.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr170.setStatus("current")
if mibBuilder.loadTexts:
    outBr170.setUnits("tenth of Mbps")
_OutStream171_ObjectIdentity = ObjectIdentity
outStream171 = _OutStream171_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 176)
)
_OutBr171_Type = Integer32
_OutBr171_Object = MibScalar
outBr171 = _OutBr171_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 176, 1),
    _OutBr171_Type()
)
outBr171.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr171.setStatus("current")
if mibBuilder.loadTexts:
    outBr171.setUnits("tenth of Mbps")
_OutStream172_ObjectIdentity = ObjectIdentity
outStream172 = _OutStream172_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 177)
)
_OutBr172_Type = Integer32
_OutBr172_Object = MibScalar
outBr172 = _OutBr172_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 177, 1),
    _OutBr172_Type()
)
outBr172.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr172.setStatus("current")
if mibBuilder.loadTexts:
    outBr172.setUnits("tenth of Mbps")
_OutStream173_ObjectIdentity = ObjectIdentity
outStream173 = _OutStream173_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 178)
)
_OutBr173_Type = Integer32
_OutBr173_Object = MibScalar
outBr173 = _OutBr173_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 178, 1),
    _OutBr173_Type()
)
outBr173.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr173.setStatus("current")
if mibBuilder.loadTexts:
    outBr173.setUnits("tenth of Mbps")
_OutStream174_ObjectIdentity = ObjectIdentity
outStream174 = _OutStream174_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 179)
)
_OutBr174_Type = Integer32
_OutBr174_Object = MibScalar
outBr174 = _OutBr174_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 179, 1),
    _OutBr174_Type()
)
outBr174.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr174.setStatus("current")
if mibBuilder.loadTexts:
    outBr174.setUnits("tenth of Mbps")
_OutStream175_ObjectIdentity = ObjectIdentity
outStream175 = _OutStream175_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 180)
)
_OutBr175_Type = Integer32
_OutBr175_Object = MibScalar
outBr175 = _OutBr175_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 180, 1),
    _OutBr175_Type()
)
outBr175.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr175.setStatus("current")
if mibBuilder.loadTexts:
    outBr175.setUnits("tenth of Mbps")
_OutStream176_ObjectIdentity = ObjectIdentity
outStream176 = _OutStream176_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 181)
)
_OutBr176_Type = Integer32
_OutBr176_Object = MibScalar
outBr176 = _OutBr176_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 181, 1),
    _OutBr176_Type()
)
outBr176.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr176.setStatus("current")
if mibBuilder.loadTexts:
    outBr176.setUnits("tenth of Mbps")
_OutStream177_ObjectIdentity = ObjectIdentity
outStream177 = _OutStream177_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 182)
)
_OutBr177_Type = Integer32
_OutBr177_Object = MibScalar
outBr177 = _OutBr177_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 182, 1),
    _OutBr177_Type()
)
outBr177.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr177.setStatus("current")
if mibBuilder.loadTexts:
    outBr177.setUnits("tenth of Mbps")
_OutStream178_ObjectIdentity = ObjectIdentity
outStream178 = _OutStream178_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 183)
)
_OutBr178_Type = Integer32
_OutBr178_Object = MibScalar
outBr178 = _OutBr178_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 183, 1),
    _OutBr178_Type()
)
outBr178.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr178.setStatus("current")
if mibBuilder.loadTexts:
    outBr178.setUnits("tenth of Mbps")
_OutStream179_ObjectIdentity = ObjectIdentity
outStream179 = _OutStream179_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 184)
)
_OutBr179_Type = Integer32
_OutBr179_Object = MibScalar
outBr179 = _OutBr179_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 184, 1),
    _OutBr179_Type()
)
outBr179.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr179.setStatus("current")
if mibBuilder.loadTexts:
    outBr179.setUnits("tenth of Mbps")
_OutStream180_ObjectIdentity = ObjectIdentity
outStream180 = _OutStream180_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 185)
)
_OutBr180_Type = Integer32
_OutBr180_Object = MibScalar
outBr180 = _OutBr180_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 185, 1),
    _OutBr180_Type()
)
outBr180.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr180.setStatus("current")
if mibBuilder.loadTexts:
    outBr180.setUnits("tenth of Mbps")
_OutStream181_ObjectIdentity = ObjectIdentity
outStream181 = _OutStream181_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 186)
)
_OutBr181_Type = Integer32
_OutBr181_Object = MibScalar
outBr181 = _OutBr181_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 186, 1),
    _OutBr181_Type()
)
outBr181.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr181.setStatus("current")
if mibBuilder.loadTexts:
    outBr181.setUnits("tenth of Mbps")
_OutStream182_ObjectIdentity = ObjectIdentity
outStream182 = _OutStream182_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 187)
)
_OutBr182_Type = Integer32
_OutBr182_Object = MibScalar
outBr182 = _OutBr182_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 187, 1),
    _OutBr182_Type()
)
outBr182.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr182.setStatus("current")
if mibBuilder.loadTexts:
    outBr182.setUnits("tenth of Mbps")
_OutStream183_ObjectIdentity = ObjectIdentity
outStream183 = _OutStream183_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 188)
)
_OutBr183_Type = Integer32
_OutBr183_Object = MibScalar
outBr183 = _OutBr183_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 188, 1),
    _OutBr183_Type()
)
outBr183.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr183.setStatus("current")
if mibBuilder.loadTexts:
    outBr183.setUnits("tenth of Mbps")
_OutStream184_ObjectIdentity = ObjectIdentity
outStream184 = _OutStream184_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 189)
)
_OutBr184_Type = Integer32
_OutBr184_Object = MibScalar
outBr184 = _OutBr184_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 189, 1),
    _OutBr184_Type()
)
outBr184.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr184.setStatus("current")
if mibBuilder.loadTexts:
    outBr184.setUnits("tenth of Mbps")
_OutStream185_ObjectIdentity = ObjectIdentity
outStream185 = _OutStream185_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 190)
)
_OutBr185_Type = Integer32
_OutBr185_Object = MibScalar
outBr185 = _OutBr185_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 190, 1),
    _OutBr185_Type()
)
outBr185.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr185.setStatus("current")
if mibBuilder.loadTexts:
    outBr185.setUnits("tenth of Mbps")
_OutStream186_ObjectIdentity = ObjectIdentity
outStream186 = _OutStream186_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 191)
)
_OutBr186_Type = Integer32
_OutBr186_Object = MibScalar
outBr186 = _OutBr186_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 191, 1),
    _OutBr186_Type()
)
outBr186.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr186.setStatus("current")
if mibBuilder.loadTexts:
    outBr186.setUnits("tenth of Mbps")
_OutStream187_ObjectIdentity = ObjectIdentity
outStream187 = _OutStream187_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 192)
)
_OutBr187_Type = Integer32
_OutBr187_Object = MibScalar
outBr187 = _OutBr187_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 192, 1),
    _OutBr187_Type()
)
outBr187.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr187.setStatus("current")
if mibBuilder.loadTexts:
    outBr187.setUnits("tenth of Mbps")
_OutStream188_ObjectIdentity = ObjectIdentity
outStream188 = _OutStream188_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 193)
)
_OutBr188_Type = Integer32
_OutBr188_Object = MibScalar
outBr188 = _OutBr188_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 193, 1),
    _OutBr188_Type()
)
outBr188.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr188.setStatus("current")
if mibBuilder.loadTexts:
    outBr188.setUnits("tenth of Mbps")
_OutStream189_ObjectIdentity = ObjectIdentity
outStream189 = _OutStream189_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 194)
)
_OutBr189_Type = Integer32
_OutBr189_Object = MibScalar
outBr189 = _OutBr189_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 194, 1),
    _OutBr189_Type()
)
outBr189.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr189.setStatus("current")
if mibBuilder.loadTexts:
    outBr189.setUnits("tenth of Mbps")
_OutStream190_ObjectIdentity = ObjectIdentity
outStream190 = _OutStream190_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 195)
)
_OutBr190_Type = Integer32
_OutBr190_Object = MibScalar
outBr190 = _OutBr190_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 195, 1),
    _OutBr190_Type()
)
outBr190.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr190.setStatus("current")
if mibBuilder.loadTexts:
    outBr190.setUnits("tenth of Mbps")
_OutStream191_ObjectIdentity = ObjectIdentity
outStream191 = _OutStream191_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 196)
)
_OutBr191_Type = Integer32
_OutBr191_Object = MibScalar
outBr191 = _OutBr191_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 196, 1),
    _OutBr191_Type()
)
outBr191.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr191.setStatus("current")
if mibBuilder.loadTexts:
    outBr191.setUnits("tenth of Mbps")
_OutStream192_ObjectIdentity = ObjectIdentity
outStream192 = _OutStream192_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 197)
)
_OutBr192_Type = Integer32
_OutBr192_Object = MibScalar
outBr192 = _OutBr192_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 197, 1),
    _OutBr192_Type()
)
outBr192.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr192.setStatus("current")
if mibBuilder.loadTexts:
    outBr192.setUnits("tenth of Mbps")
_OutStream193_ObjectIdentity = ObjectIdentity
outStream193 = _OutStream193_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 198)
)
_OutBr193_Type = Integer32
_OutBr193_Object = MibScalar
outBr193 = _OutBr193_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 198, 1),
    _OutBr193_Type()
)
outBr193.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr193.setStatus("current")
if mibBuilder.loadTexts:
    outBr193.setUnits("tenth of Mbps")
_OutStream194_ObjectIdentity = ObjectIdentity
outStream194 = _OutStream194_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 199)
)
_OutBr194_Type = Integer32
_OutBr194_Object = MibScalar
outBr194 = _OutBr194_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 199, 1),
    _OutBr194_Type()
)
outBr194.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr194.setStatus("current")
if mibBuilder.loadTexts:
    outBr194.setUnits("tenth of Mbps")
_OutStream195_ObjectIdentity = ObjectIdentity
outStream195 = _OutStream195_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 200)
)
_OutBr195_Type = Integer32
_OutBr195_Object = MibScalar
outBr195 = _OutBr195_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 200, 1),
    _OutBr195_Type()
)
outBr195.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr195.setStatus("current")
if mibBuilder.loadTexts:
    outBr195.setUnits("tenth of Mbps")
_OutStream196_ObjectIdentity = ObjectIdentity
outStream196 = _OutStream196_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 201)
)
_OutBr196_Type = Integer32
_OutBr196_Object = MibScalar
outBr196 = _OutBr196_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 201, 1),
    _OutBr196_Type()
)
outBr196.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr196.setStatus("current")
if mibBuilder.loadTexts:
    outBr196.setUnits("tenth of Mbps")
_OutStream197_ObjectIdentity = ObjectIdentity
outStream197 = _OutStream197_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 202)
)
_OutBr197_Type = Integer32
_OutBr197_Object = MibScalar
outBr197 = _OutBr197_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 202, 1),
    _OutBr197_Type()
)
outBr197.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr197.setStatus("current")
if mibBuilder.loadTexts:
    outBr197.setUnits("tenth of Mbps")
_OutStream198_ObjectIdentity = ObjectIdentity
outStream198 = _OutStream198_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 203)
)
_OutBr198_Type = Integer32
_OutBr198_Object = MibScalar
outBr198 = _OutBr198_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 203, 1),
    _OutBr198_Type()
)
outBr198.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr198.setStatus("current")
if mibBuilder.loadTexts:
    outBr198.setUnits("tenth of Mbps")
_OutStream199_ObjectIdentity = ObjectIdentity
outStream199 = _OutStream199_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 204)
)
_OutBr199_Type = Integer32
_OutBr199_Object = MibScalar
outBr199 = _OutBr199_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 204, 1),
    _OutBr199_Type()
)
outBr199.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr199.setStatus("current")
if mibBuilder.loadTexts:
    outBr199.setUnits("tenth of Mbps")
_OutStream200_ObjectIdentity = ObjectIdentity
outStream200 = _OutStream200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 205)
)
_OutBr200_Type = Integer32
_OutBr200_Object = MibScalar
outBr200 = _OutBr200_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 205, 1),
    _OutBr200_Type()
)
outBr200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr200.setStatus("current")
if mibBuilder.loadTexts:
    outBr200.setUnits("tenth of Mbps")
_OutStream201_ObjectIdentity = ObjectIdentity
outStream201 = _OutStream201_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 206)
)
_OutBr201_Type = Integer32
_OutBr201_Object = MibScalar
outBr201 = _OutBr201_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 206, 1),
    _OutBr201_Type()
)
outBr201.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr201.setStatus("current")
if mibBuilder.loadTexts:
    outBr201.setUnits("tenth of Mbps")
_OutStream202_ObjectIdentity = ObjectIdentity
outStream202 = _OutStream202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 207)
)
_OutBr202_Type = Integer32
_OutBr202_Object = MibScalar
outBr202 = _OutBr202_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 207, 1),
    _OutBr202_Type()
)
outBr202.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr202.setStatus("current")
if mibBuilder.loadTexts:
    outBr202.setUnits("tenth of Mbps")
_OutStream203_ObjectIdentity = ObjectIdentity
outStream203 = _OutStream203_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 208)
)
_OutBr203_Type = Integer32
_OutBr203_Object = MibScalar
outBr203 = _OutBr203_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 208, 1),
    _OutBr203_Type()
)
outBr203.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr203.setStatus("current")
if mibBuilder.loadTexts:
    outBr203.setUnits("tenth of Mbps")
_OutStream204_ObjectIdentity = ObjectIdentity
outStream204 = _OutStream204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 209)
)
_OutBr204_Type = Integer32
_OutBr204_Object = MibScalar
outBr204 = _OutBr204_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 209, 1),
    _OutBr204_Type()
)
outBr204.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr204.setStatus("current")
if mibBuilder.loadTexts:
    outBr204.setUnits("tenth of Mbps")
_OutStream205_ObjectIdentity = ObjectIdentity
outStream205 = _OutStream205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 210)
)
_OutBr205_Type = Integer32
_OutBr205_Object = MibScalar
outBr205 = _OutBr205_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 210, 1),
    _OutBr205_Type()
)
outBr205.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr205.setStatus("current")
if mibBuilder.loadTexts:
    outBr205.setUnits("tenth of Mbps")
_OutStream206_ObjectIdentity = ObjectIdentity
outStream206 = _OutStream206_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 211)
)
_OutBr206_Type = Integer32
_OutBr206_Object = MibScalar
outBr206 = _OutBr206_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 211, 1),
    _OutBr206_Type()
)
outBr206.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr206.setStatus("current")
if mibBuilder.loadTexts:
    outBr206.setUnits("tenth of Mbps")
_OutStream207_ObjectIdentity = ObjectIdentity
outStream207 = _OutStream207_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 212)
)
_OutBr207_Type = Integer32
_OutBr207_Object = MibScalar
outBr207 = _OutBr207_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 212, 1),
    _OutBr207_Type()
)
outBr207.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr207.setStatus("current")
if mibBuilder.loadTexts:
    outBr207.setUnits("tenth of Mbps")
_OutStream208_ObjectIdentity = ObjectIdentity
outStream208 = _OutStream208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 213)
)
_OutBr208_Type = Integer32
_OutBr208_Object = MibScalar
outBr208 = _OutBr208_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 213, 1),
    _OutBr208_Type()
)
outBr208.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr208.setStatus("current")
if mibBuilder.loadTexts:
    outBr208.setUnits("tenth of Mbps")
_OutStream209_ObjectIdentity = ObjectIdentity
outStream209 = _OutStream209_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 214)
)
_OutBr209_Type = Integer32
_OutBr209_Object = MibScalar
outBr209 = _OutBr209_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 214, 1),
    _OutBr209_Type()
)
outBr209.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr209.setStatus("current")
if mibBuilder.loadTexts:
    outBr209.setUnits("tenth of Mbps")
_OutStream210_ObjectIdentity = ObjectIdentity
outStream210 = _OutStream210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 215)
)
_OutBr210_Type = Integer32
_OutBr210_Object = MibScalar
outBr210 = _OutBr210_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 215, 1),
    _OutBr210_Type()
)
outBr210.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr210.setStatus("current")
if mibBuilder.loadTexts:
    outBr210.setUnits("tenth of Mbps")
_OutStream211_ObjectIdentity = ObjectIdentity
outStream211 = _OutStream211_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 216)
)
_OutBr211_Type = Integer32
_OutBr211_Object = MibScalar
outBr211 = _OutBr211_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 216, 1),
    _OutBr211_Type()
)
outBr211.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr211.setStatus("current")
if mibBuilder.loadTexts:
    outBr211.setUnits("tenth of Mbps")
_OutStream212_ObjectIdentity = ObjectIdentity
outStream212 = _OutStream212_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 217)
)
_OutBr212_Type = Integer32
_OutBr212_Object = MibScalar
outBr212 = _OutBr212_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 217, 1),
    _OutBr212_Type()
)
outBr212.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr212.setStatus("current")
if mibBuilder.loadTexts:
    outBr212.setUnits("tenth of Mbps")
_OutStream213_ObjectIdentity = ObjectIdentity
outStream213 = _OutStream213_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 218)
)
_OutBr213_Type = Integer32
_OutBr213_Object = MibScalar
outBr213 = _OutBr213_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 218, 1),
    _OutBr213_Type()
)
outBr213.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr213.setStatus("current")
if mibBuilder.loadTexts:
    outBr213.setUnits("tenth of Mbps")
_OutStream214_ObjectIdentity = ObjectIdentity
outStream214 = _OutStream214_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 219)
)
_OutBr214_Type = Integer32
_OutBr214_Object = MibScalar
outBr214 = _OutBr214_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 219, 1),
    _OutBr214_Type()
)
outBr214.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr214.setStatus("current")
if mibBuilder.loadTexts:
    outBr214.setUnits("tenth of Mbps")
_OutStream215_ObjectIdentity = ObjectIdentity
outStream215 = _OutStream215_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 220)
)
_OutBr215_Type = Integer32
_OutBr215_Object = MibScalar
outBr215 = _OutBr215_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 220, 1),
    _OutBr215_Type()
)
outBr215.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr215.setStatus("current")
if mibBuilder.loadTexts:
    outBr215.setUnits("tenth of Mbps")
_OutStream216_ObjectIdentity = ObjectIdentity
outStream216 = _OutStream216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 221)
)
_OutBr216_Type = Integer32
_OutBr216_Object = MibScalar
outBr216 = _OutBr216_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 221, 1),
    _OutBr216_Type()
)
outBr216.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr216.setStatus("current")
if mibBuilder.loadTexts:
    outBr216.setUnits("tenth of Mbps")
_OutStream217_ObjectIdentity = ObjectIdentity
outStream217 = _OutStream217_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 222)
)
_OutBr217_Type = Integer32
_OutBr217_Object = MibScalar
outBr217 = _OutBr217_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 222, 1),
    _OutBr217_Type()
)
outBr217.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr217.setStatus("current")
if mibBuilder.loadTexts:
    outBr217.setUnits("tenth of Mbps")
_OutStream218_ObjectIdentity = ObjectIdentity
outStream218 = _OutStream218_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 223)
)
_OutBr218_Type = Integer32
_OutBr218_Object = MibScalar
outBr218 = _OutBr218_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 223, 1),
    _OutBr218_Type()
)
outBr218.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr218.setStatus("current")
if mibBuilder.loadTexts:
    outBr218.setUnits("tenth of Mbps")
_OutStream219_ObjectIdentity = ObjectIdentity
outStream219 = _OutStream219_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 224)
)
_OutBr219_Type = Integer32
_OutBr219_Object = MibScalar
outBr219 = _OutBr219_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 224, 1),
    _OutBr219_Type()
)
outBr219.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr219.setStatus("current")
if mibBuilder.loadTexts:
    outBr219.setUnits("tenth of Mbps")
_OutStream220_ObjectIdentity = ObjectIdentity
outStream220 = _OutStream220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 225)
)
_OutBr220_Type = Integer32
_OutBr220_Object = MibScalar
outBr220 = _OutBr220_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 225, 1),
    _OutBr220_Type()
)
outBr220.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr220.setStatus("current")
if mibBuilder.loadTexts:
    outBr220.setUnits("tenth of Mbps")
_OutStream221_ObjectIdentity = ObjectIdentity
outStream221 = _OutStream221_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 226)
)
_OutBr221_Type = Integer32
_OutBr221_Object = MibScalar
outBr221 = _OutBr221_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 226, 1),
    _OutBr221_Type()
)
outBr221.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr221.setStatus("current")
if mibBuilder.loadTexts:
    outBr221.setUnits("tenth of Mbps")
_OutStream222_ObjectIdentity = ObjectIdentity
outStream222 = _OutStream222_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 227)
)
_OutBr222_Type = Integer32
_OutBr222_Object = MibScalar
outBr222 = _OutBr222_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 227, 1),
    _OutBr222_Type()
)
outBr222.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr222.setStatus("current")
if mibBuilder.loadTexts:
    outBr222.setUnits("tenth of Mbps")
_OutStream223_ObjectIdentity = ObjectIdentity
outStream223 = _OutStream223_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 228)
)
_OutBr223_Type = Integer32
_OutBr223_Object = MibScalar
outBr223 = _OutBr223_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 228, 1),
    _OutBr223_Type()
)
outBr223.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr223.setStatus("current")
if mibBuilder.loadTexts:
    outBr223.setUnits("tenth of Mbps")
_OutStream224_ObjectIdentity = ObjectIdentity
outStream224 = _OutStream224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 229)
)
_OutBr224_Type = Integer32
_OutBr224_Object = MibScalar
outBr224 = _OutBr224_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 229, 1),
    _OutBr224_Type()
)
outBr224.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr224.setStatus("current")
if mibBuilder.loadTexts:
    outBr224.setUnits("tenth of Mbps")
_OutStream225_ObjectIdentity = ObjectIdentity
outStream225 = _OutStream225_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 230)
)
_OutBr225_Type = Integer32
_OutBr225_Object = MibScalar
outBr225 = _OutBr225_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 230, 1),
    _OutBr225_Type()
)
outBr225.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr225.setStatus("current")
if mibBuilder.loadTexts:
    outBr225.setUnits("tenth of Mbps")
_OutStream226_ObjectIdentity = ObjectIdentity
outStream226 = _OutStream226_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 231)
)
_OutBr226_Type = Integer32
_OutBr226_Object = MibScalar
outBr226 = _OutBr226_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 231, 1),
    _OutBr226_Type()
)
outBr226.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr226.setStatus("current")
if mibBuilder.loadTexts:
    outBr226.setUnits("tenth of Mbps")
_OutStream227_ObjectIdentity = ObjectIdentity
outStream227 = _OutStream227_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 232)
)
_OutBr227_Type = Integer32
_OutBr227_Object = MibScalar
outBr227 = _OutBr227_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 232, 1),
    _OutBr227_Type()
)
outBr227.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr227.setStatus("current")
if mibBuilder.loadTexts:
    outBr227.setUnits("tenth of Mbps")
_OutStream228_ObjectIdentity = ObjectIdentity
outStream228 = _OutStream228_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 233)
)
_OutBr228_Type = Integer32
_OutBr228_Object = MibScalar
outBr228 = _OutBr228_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 233, 1),
    _OutBr228_Type()
)
outBr228.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr228.setStatus("current")
if mibBuilder.loadTexts:
    outBr228.setUnits("tenth of Mbps")
_OutStream229_ObjectIdentity = ObjectIdentity
outStream229 = _OutStream229_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 234)
)
_OutBr229_Type = Integer32
_OutBr229_Object = MibScalar
outBr229 = _OutBr229_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 234, 1),
    _OutBr229_Type()
)
outBr229.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr229.setStatus("current")
if mibBuilder.loadTexts:
    outBr229.setUnits("tenth of Mbps")
_OutStream230_ObjectIdentity = ObjectIdentity
outStream230 = _OutStream230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 235)
)
_OutBr230_Type = Integer32
_OutBr230_Object = MibScalar
outBr230 = _OutBr230_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 235, 1),
    _OutBr230_Type()
)
outBr230.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr230.setStatus("current")
if mibBuilder.loadTexts:
    outBr230.setUnits("tenth of Mbps")
_OutStream231_ObjectIdentity = ObjectIdentity
outStream231 = _OutStream231_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 236)
)
_OutBr231_Type = Integer32
_OutBr231_Object = MibScalar
outBr231 = _OutBr231_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 236, 1),
    _OutBr231_Type()
)
outBr231.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr231.setStatus("current")
if mibBuilder.loadTexts:
    outBr231.setUnits("tenth of Mbps")
_OutStream232_ObjectIdentity = ObjectIdentity
outStream232 = _OutStream232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 237)
)
_OutBr232_Type = Integer32
_OutBr232_Object = MibScalar
outBr232 = _OutBr232_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 237, 1),
    _OutBr232_Type()
)
outBr232.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr232.setStatus("current")
if mibBuilder.loadTexts:
    outBr232.setUnits("tenth of Mbps")
_OutStream233_ObjectIdentity = ObjectIdentity
outStream233 = _OutStream233_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 238)
)
_OutBr233_Type = Integer32
_OutBr233_Object = MibScalar
outBr233 = _OutBr233_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 238, 1),
    _OutBr233_Type()
)
outBr233.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr233.setStatus("current")
if mibBuilder.loadTexts:
    outBr233.setUnits("tenth of Mbps")
_OutStream234_ObjectIdentity = ObjectIdentity
outStream234 = _OutStream234_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 239)
)
_OutBr234_Type = Integer32
_OutBr234_Object = MibScalar
outBr234 = _OutBr234_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 239, 1),
    _OutBr234_Type()
)
outBr234.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr234.setStatus("current")
if mibBuilder.loadTexts:
    outBr234.setUnits("tenth of Mbps")
_OutStream235_ObjectIdentity = ObjectIdentity
outStream235 = _OutStream235_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 240)
)
_OutBr235_Type = Integer32
_OutBr235_Object = MibScalar
outBr235 = _OutBr235_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 240, 1),
    _OutBr235_Type()
)
outBr235.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr235.setStatus("current")
if mibBuilder.loadTexts:
    outBr235.setUnits("tenth of Mbps")
_OutStream236_ObjectIdentity = ObjectIdentity
outStream236 = _OutStream236_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 241)
)
_OutBr236_Type = Integer32
_OutBr236_Object = MibScalar
outBr236 = _OutBr236_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 241, 1),
    _OutBr236_Type()
)
outBr236.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr236.setStatus("current")
if mibBuilder.loadTexts:
    outBr236.setUnits("tenth of Mbps")
_OutStream237_ObjectIdentity = ObjectIdentity
outStream237 = _OutStream237_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 242)
)
_OutBr237_Type = Integer32
_OutBr237_Object = MibScalar
outBr237 = _OutBr237_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 242, 1),
    _OutBr237_Type()
)
outBr237.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr237.setStatus("current")
if mibBuilder.loadTexts:
    outBr237.setUnits("tenth of Mbps")
_OutStream238_ObjectIdentity = ObjectIdentity
outStream238 = _OutStream238_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 243)
)
_OutBr238_Type = Integer32
_OutBr238_Object = MibScalar
outBr238 = _OutBr238_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 243, 1),
    _OutBr238_Type()
)
outBr238.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr238.setStatus("current")
if mibBuilder.loadTexts:
    outBr238.setUnits("tenth of Mbps")
_OutStream239_ObjectIdentity = ObjectIdentity
outStream239 = _OutStream239_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 244)
)
_OutBr239_Type = Integer32
_OutBr239_Object = MibScalar
outBr239 = _OutBr239_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 244, 1),
    _OutBr239_Type()
)
outBr239.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr239.setStatus("current")
if mibBuilder.loadTexts:
    outBr239.setUnits("tenth of Mbps")
_OutStream240_ObjectIdentity = ObjectIdentity
outStream240 = _OutStream240_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 245)
)
_OutBr240_Type = Integer32
_OutBr240_Object = MibScalar
outBr240 = _OutBr240_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 245, 1),
    _OutBr240_Type()
)
outBr240.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr240.setStatus("current")
if mibBuilder.loadTexts:
    outBr240.setUnits("tenth of Mbps")
_OutStream241_ObjectIdentity = ObjectIdentity
outStream241 = _OutStream241_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 246)
)
_OutBr241_Type = Integer32
_OutBr241_Object = MibScalar
outBr241 = _OutBr241_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 246, 1),
    _OutBr241_Type()
)
outBr241.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr241.setStatus("current")
if mibBuilder.loadTexts:
    outBr241.setUnits("tenth of Mbps")
_OutStream242_ObjectIdentity = ObjectIdentity
outStream242 = _OutStream242_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 247)
)
_OutBr242_Type = Integer32
_OutBr242_Object = MibScalar
outBr242 = _OutBr242_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 247, 1),
    _OutBr242_Type()
)
outBr242.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr242.setStatus("current")
if mibBuilder.loadTexts:
    outBr242.setUnits("tenth of Mbps")
_OutStream243_ObjectIdentity = ObjectIdentity
outStream243 = _OutStream243_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 248)
)
_OutBr243_Type = Integer32
_OutBr243_Object = MibScalar
outBr243 = _OutBr243_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 248, 1),
    _OutBr243_Type()
)
outBr243.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr243.setStatus("current")
if mibBuilder.loadTexts:
    outBr243.setUnits("tenth of Mbps")
_OutStream244_ObjectIdentity = ObjectIdentity
outStream244 = _OutStream244_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 249)
)
_OutBr244_Type = Integer32
_OutBr244_Object = MibScalar
outBr244 = _OutBr244_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 249, 1),
    _OutBr244_Type()
)
outBr244.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr244.setStatus("current")
if mibBuilder.loadTexts:
    outBr244.setUnits("tenth of Mbps")
_OutStream245_ObjectIdentity = ObjectIdentity
outStream245 = _OutStream245_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 250)
)
_OutBr245_Type = Integer32
_OutBr245_Object = MibScalar
outBr245 = _OutBr245_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 250, 1),
    _OutBr245_Type()
)
outBr245.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr245.setStatus("current")
if mibBuilder.loadTexts:
    outBr245.setUnits("tenth of Mbps")
_OutStream246_ObjectIdentity = ObjectIdentity
outStream246 = _OutStream246_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 251)
)
_OutBr246_Type = Integer32
_OutBr246_Object = MibScalar
outBr246 = _OutBr246_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 251, 1),
    _OutBr246_Type()
)
outBr246.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr246.setStatus("current")
if mibBuilder.loadTexts:
    outBr246.setUnits("tenth of Mbps")
_OutStream247_ObjectIdentity = ObjectIdentity
outStream247 = _OutStream247_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 252)
)
_OutBr247_Type = Integer32
_OutBr247_Object = MibScalar
outBr247 = _OutBr247_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 252, 1),
    _OutBr247_Type()
)
outBr247.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr247.setStatus("current")
if mibBuilder.loadTexts:
    outBr247.setUnits("tenth of Mbps")
_OutStream248_ObjectIdentity = ObjectIdentity
outStream248 = _OutStream248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 253)
)
_OutBr248_Type = Integer32
_OutBr248_Object = MibScalar
outBr248 = _OutBr248_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 253, 1),
    _OutBr248_Type()
)
outBr248.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr248.setStatus("current")
if mibBuilder.loadTexts:
    outBr248.setUnits("tenth of Mbps")
_OutStream249_ObjectIdentity = ObjectIdentity
outStream249 = _OutStream249_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 254)
)
_OutBr249_Type = Integer32
_OutBr249_Object = MibScalar
outBr249 = _OutBr249_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 254, 1),
    _OutBr249_Type()
)
outBr249.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr249.setStatus("current")
if mibBuilder.loadTexts:
    outBr249.setUnits("tenth of Mbps")
_OutStream250_ObjectIdentity = ObjectIdentity
outStream250 = _OutStream250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 255)
)
_OutBr250_Type = Integer32
_OutBr250_Object = MibScalar
outBr250 = _OutBr250_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 255, 1),
    _OutBr250_Type()
)
outBr250.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr250.setStatus("current")
if mibBuilder.loadTexts:
    outBr250.setUnits("tenth of Mbps")
_OutStream251_ObjectIdentity = ObjectIdentity
outStream251 = _OutStream251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 256)
)
_OutBr251_Type = Integer32
_OutBr251_Object = MibScalar
outBr251 = _OutBr251_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 256, 1),
    _OutBr251_Type()
)
outBr251.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr251.setStatus("current")
if mibBuilder.loadTexts:
    outBr251.setUnits("tenth of Mbps")
_OutStream252_ObjectIdentity = ObjectIdentity
outStream252 = _OutStream252_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 257)
)
_OutBr252_Type = Integer32
_OutBr252_Object = MibScalar
outBr252 = _OutBr252_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 257, 1),
    _OutBr252_Type()
)
outBr252.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr252.setStatus("current")
if mibBuilder.loadTexts:
    outBr252.setUnits("tenth of Mbps")
_OutStream253_ObjectIdentity = ObjectIdentity
outStream253 = _OutStream253_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 258)
)
_OutBr253_Type = Integer32
_OutBr253_Object = MibScalar
outBr253 = _OutBr253_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 258, 1),
    _OutBr253_Type()
)
outBr253.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr253.setStatus("current")
if mibBuilder.loadTexts:
    outBr253.setUnits("tenth of Mbps")
_OutStream254_ObjectIdentity = ObjectIdentity
outStream254 = _OutStream254_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 259)
)
_OutBr254_Type = Integer32
_OutBr254_Object = MibScalar
outBr254 = _OutBr254_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 259, 1),
    _OutBr254_Type()
)
outBr254.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr254.setStatus("current")
if mibBuilder.loadTexts:
    outBr254.setUnits("tenth of Mbps")
_OutStream255_ObjectIdentity = ObjectIdentity
outStream255 = _OutStream255_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 260)
)
_OutBr255_Type = Integer32
_OutBr255_Object = MibScalar
outBr255 = _OutBr255_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 260, 1),
    _OutBr255_Type()
)
outBr255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr255.setStatus("current")
if mibBuilder.loadTexts:
    outBr255.setUnits("tenth of Mbps")
_OutStream256_ObjectIdentity = ObjectIdentity
outStream256 = _OutStream256_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 261)
)
_OutBr256_Type = Integer32
_OutBr256_Object = MibScalar
outBr256 = _OutBr256_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 261, 1),
    _OutBr256_Type()
)
outBr256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr256.setStatus("current")
if mibBuilder.loadTexts:
    outBr256.setUnits("tenth of Mbps")
_OutStream257_ObjectIdentity = ObjectIdentity
outStream257 = _OutStream257_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 262)
)
_OutBr257_Type = Integer32
_OutBr257_Object = MibScalar
outBr257 = _OutBr257_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 262, 1),
    _OutBr257_Type()
)
outBr257.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr257.setStatus("current")
if mibBuilder.loadTexts:
    outBr257.setUnits("tenth of Mbps")
_OutStream258_ObjectIdentity = ObjectIdentity
outStream258 = _OutStream258_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 263)
)
_OutBr258_Type = Integer32
_OutBr258_Object = MibScalar
outBr258 = _OutBr258_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 263, 1),
    _OutBr258_Type()
)
outBr258.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr258.setStatus("current")
if mibBuilder.loadTexts:
    outBr258.setUnits("tenth of Mbps")
_OutStream259_ObjectIdentity = ObjectIdentity
outStream259 = _OutStream259_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 264)
)
_OutBr259_Type = Integer32
_OutBr259_Object = MibScalar
outBr259 = _OutBr259_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 264, 1),
    _OutBr259_Type()
)
outBr259.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr259.setStatus("current")
if mibBuilder.loadTexts:
    outBr259.setUnits("tenth of Mbps")
_OutStream260_ObjectIdentity = ObjectIdentity
outStream260 = _OutStream260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 265)
)
_OutBr260_Type = Integer32
_OutBr260_Object = MibScalar
outBr260 = _OutBr260_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 265, 1),
    _OutBr260_Type()
)
outBr260.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr260.setStatus("current")
if mibBuilder.loadTexts:
    outBr260.setUnits("tenth of Mbps")
_OutStream261_ObjectIdentity = ObjectIdentity
outStream261 = _OutStream261_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 266)
)
_OutBr261_Type = Integer32
_OutBr261_Object = MibScalar
outBr261 = _OutBr261_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 266, 1),
    _OutBr261_Type()
)
outBr261.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr261.setStatus("current")
if mibBuilder.loadTexts:
    outBr261.setUnits("tenth of Mbps")
_OutStream262_ObjectIdentity = ObjectIdentity
outStream262 = _OutStream262_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 267)
)
_OutBr262_Type = Integer32
_OutBr262_Object = MibScalar
outBr262 = _OutBr262_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 267, 1),
    _OutBr262_Type()
)
outBr262.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr262.setStatus("current")
if mibBuilder.loadTexts:
    outBr262.setUnits("tenth of Mbps")
_OutStream263_ObjectIdentity = ObjectIdentity
outStream263 = _OutStream263_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 268)
)
_OutBr263_Type = Integer32
_OutBr263_Object = MibScalar
outBr263 = _OutBr263_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 268, 1),
    _OutBr263_Type()
)
outBr263.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr263.setStatus("current")
if mibBuilder.loadTexts:
    outBr263.setUnits("tenth of Mbps")
_OutStream264_ObjectIdentity = ObjectIdentity
outStream264 = _OutStream264_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 269)
)
_OutBr264_Type = Integer32
_OutBr264_Object = MibScalar
outBr264 = _OutBr264_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 269, 1),
    _OutBr264_Type()
)
outBr264.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr264.setStatus("current")
if mibBuilder.loadTexts:
    outBr264.setUnits("tenth of Mbps")
_OutStream265_ObjectIdentity = ObjectIdentity
outStream265 = _OutStream265_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 270)
)
_OutBr265_Type = Integer32
_OutBr265_Object = MibScalar
outBr265 = _OutBr265_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 270, 1),
    _OutBr265_Type()
)
outBr265.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr265.setStatus("current")
if mibBuilder.loadTexts:
    outBr265.setUnits("tenth of Mbps")
_OutStream266_ObjectIdentity = ObjectIdentity
outStream266 = _OutStream266_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 271)
)
_OutBr266_Type = Integer32
_OutBr266_Object = MibScalar
outBr266 = _OutBr266_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 271, 1),
    _OutBr266_Type()
)
outBr266.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr266.setStatus("current")
if mibBuilder.loadTexts:
    outBr266.setUnits("tenth of Mbps")
_OutStream267_ObjectIdentity = ObjectIdentity
outStream267 = _OutStream267_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 272)
)
_OutBr267_Type = Integer32
_OutBr267_Object = MibScalar
outBr267 = _OutBr267_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 272, 1),
    _OutBr267_Type()
)
outBr267.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr267.setStatus("current")
if mibBuilder.loadTexts:
    outBr267.setUnits("tenth of Mbps")
_OutStream268_ObjectIdentity = ObjectIdentity
outStream268 = _OutStream268_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 273)
)
_OutBr268_Type = Integer32
_OutBr268_Object = MibScalar
outBr268 = _OutBr268_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 273, 1),
    _OutBr268_Type()
)
outBr268.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr268.setStatus("current")
if mibBuilder.loadTexts:
    outBr268.setUnits("tenth of Mbps")
_OutStream269_ObjectIdentity = ObjectIdentity
outStream269 = _OutStream269_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 274)
)
_OutBr269_Type = Integer32
_OutBr269_Object = MibScalar
outBr269 = _OutBr269_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 274, 1),
    _OutBr269_Type()
)
outBr269.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr269.setStatus("current")
if mibBuilder.loadTexts:
    outBr269.setUnits("tenth of Mbps")
_OutStream270_ObjectIdentity = ObjectIdentity
outStream270 = _OutStream270_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 275)
)
_OutBr270_Type = Integer32
_OutBr270_Object = MibScalar
outBr270 = _OutBr270_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 275, 1),
    _OutBr270_Type()
)
outBr270.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr270.setStatus("current")
if mibBuilder.loadTexts:
    outBr270.setUnits("tenth of Mbps")
_OutStream271_ObjectIdentity = ObjectIdentity
outStream271 = _OutStream271_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 276)
)
_OutBr271_Type = Integer32
_OutBr271_Object = MibScalar
outBr271 = _OutBr271_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 276, 1),
    _OutBr271_Type()
)
outBr271.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr271.setStatus("current")
if mibBuilder.loadTexts:
    outBr271.setUnits("tenth of Mbps")
_OutStream272_ObjectIdentity = ObjectIdentity
outStream272 = _OutStream272_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 277)
)
_OutBr272_Type = Integer32
_OutBr272_Object = MibScalar
outBr272 = _OutBr272_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 277, 1),
    _OutBr272_Type()
)
outBr272.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr272.setStatus("current")
if mibBuilder.loadTexts:
    outBr272.setUnits("tenth of Mbps")
_OutStream273_ObjectIdentity = ObjectIdentity
outStream273 = _OutStream273_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 278)
)
_OutBr273_Type = Integer32
_OutBr273_Object = MibScalar
outBr273 = _OutBr273_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 278, 1),
    _OutBr273_Type()
)
outBr273.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr273.setStatus("current")
if mibBuilder.loadTexts:
    outBr273.setUnits("tenth of Mbps")
_OutStream274_ObjectIdentity = ObjectIdentity
outStream274 = _OutStream274_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 279)
)
_OutBr274_Type = Integer32
_OutBr274_Object = MibScalar
outBr274 = _OutBr274_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 279, 1),
    _OutBr274_Type()
)
outBr274.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr274.setStatus("current")
if mibBuilder.loadTexts:
    outBr274.setUnits("tenth of Mbps")
_OutStream275_ObjectIdentity = ObjectIdentity
outStream275 = _OutStream275_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 280)
)
_OutBr275_Type = Integer32
_OutBr275_Object = MibScalar
outBr275 = _OutBr275_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 280, 1),
    _OutBr275_Type()
)
outBr275.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr275.setStatus("current")
if mibBuilder.loadTexts:
    outBr275.setUnits("tenth of Mbps")
_OutStream276_ObjectIdentity = ObjectIdentity
outStream276 = _OutStream276_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 281)
)
_OutBr276_Type = Integer32
_OutBr276_Object = MibScalar
outBr276 = _OutBr276_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 281, 1),
    _OutBr276_Type()
)
outBr276.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr276.setStatus("current")
if mibBuilder.loadTexts:
    outBr276.setUnits("tenth of Mbps")
_OutStream277_ObjectIdentity = ObjectIdentity
outStream277 = _OutStream277_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 282)
)
_OutBr277_Type = Integer32
_OutBr277_Object = MibScalar
outBr277 = _OutBr277_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 282, 1),
    _OutBr277_Type()
)
outBr277.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr277.setStatus("current")
if mibBuilder.loadTexts:
    outBr277.setUnits("tenth of Mbps")
_OutStream278_ObjectIdentity = ObjectIdentity
outStream278 = _OutStream278_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 283)
)
_OutBr278_Type = Integer32
_OutBr278_Object = MibScalar
outBr278 = _OutBr278_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 283, 1),
    _OutBr278_Type()
)
outBr278.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr278.setStatus("current")
if mibBuilder.loadTexts:
    outBr278.setUnits("tenth of Mbps")
_OutStream279_ObjectIdentity = ObjectIdentity
outStream279 = _OutStream279_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 284)
)
_OutBr279_Type = Integer32
_OutBr279_Object = MibScalar
outBr279 = _OutBr279_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 284, 1),
    _OutBr279_Type()
)
outBr279.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr279.setStatus("current")
if mibBuilder.loadTexts:
    outBr279.setUnits("tenth of Mbps")
_OutStream280_ObjectIdentity = ObjectIdentity
outStream280 = _OutStream280_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 285)
)
_OutBr280_Type = Integer32
_OutBr280_Object = MibScalar
outBr280 = _OutBr280_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 285, 1),
    _OutBr280_Type()
)
outBr280.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr280.setStatus("current")
if mibBuilder.loadTexts:
    outBr280.setUnits("tenth of Mbps")
_OutStream281_ObjectIdentity = ObjectIdentity
outStream281 = _OutStream281_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 286)
)
_OutBr281_Type = Integer32
_OutBr281_Object = MibScalar
outBr281 = _OutBr281_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 286, 1),
    _OutBr281_Type()
)
outBr281.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr281.setStatus("current")
if mibBuilder.loadTexts:
    outBr281.setUnits("tenth of Mbps")
_OutStream282_ObjectIdentity = ObjectIdentity
outStream282 = _OutStream282_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 287)
)
_OutBr282_Type = Integer32
_OutBr282_Object = MibScalar
outBr282 = _OutBr282_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 287, 1),
    _OutBr282_Type()
)
outBr282.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr282.setStatus("current")
if mibBuilder.loadTexts:
    outBr282.setUnits("tenth of Mbps")
_OutStream283_ObjectIdentity = ObjectIdentity
outStream283 = _OutStream283_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 288)
)
_OutBr283_Type = Integer32
_OutBr283_Object = MibScalar
outBr283 = _OutBr283_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 288, 1),
    _OutBr283_Type()
)
outBr283.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr283.setStatus("current")
if mibBuilder.loadTexts:
    outBr283.setUnits("tenth of Mbps")
_OutStream284_ObjectIdentity = ObjectIdentity
outStream284 = _OutStream284_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 289)
)
_OutBr284_Type = Integer32
_OutBr284_Object = MibScalar
outBr284 = _OutBr284_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 289, 1),
    _OutBr284_Type()
)
outBr284.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr284.setStatus("current")
if mibBuilder.loadTexts:
    outBr284.setUnits("tenth of Mbps")
_OutStream285_ObjectIdentity = ObjectIdentity
outStream285 = _OutStream285_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 290)
)
_OutBr285_Type = Integer32
_OutBr285_Object = MibScalar
outBr285 = _OutBr285_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 290, 1),
    _OutBr285_Type()
)
outBr285.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr285.setStatus("current")
if mibBuilder.loadTexts:
    outBr285.setUnits("tenth of Mbps")
_OutStream286_ObjectIdentity = ObjectIdentity
outStream286 = _OutStream286_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 291)
)
_OutBr286_Type = Integer32
_OutBr286_Object = MibScalar
outBr286 = _OutBr286_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 291, 1),
    _OutBr286_Type()
)
outBr286.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr286.setStatus("current")
if mibBuilder.loadTexts:
    outBr286.setUnits("tenth of Mbps")
_OutStream287_ObjectIdentity = ObjectIdentity
outStream287 = _OutStream287_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 292)
)
_OutBr287_Type = Integer32
_OutBr287_Object = MibScalar
outBr287 = _OutBr287_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 292, 1),
    _OutBr287_Type()
)
outBr287.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr287.setStatus("current")
if mibBuilder.loadTexts:
    outBr287.setUnits("tenth of Mbps")
_OutStream288_ObjectIdentity = ObjectIdentity
outStream288 = _OutStream288_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 293)
)
_OutBr288_Type = Integer32
_OutBr288_Object = MibScalar
outBr288 = _OutBr288_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 293, 1),
    _OutBr288_Type()
)
outBr288.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr288.setStatus("current")
if mibBuilder.loadTexts:
    outBr288.setUnits("tenth of Mbps")
_OutStream289_ObjectIdentity = ObjectIdentity
outStream289 = _OutStream289_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 294)
)
_OutBr289_Type = Integer32
_OutBr289_Object = MibScalar
outBr289 = _OutBr289_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 294, 1),
    _OutBr289_Type()
)
outBr289.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr289.setStatus("current")
if mibBuilder.loadTexts:
    outBr289.setUnits("tenth of Mbps")
_OutStream290_ObjectIdentity = ObjectIdentity
outStream290 = _OutStream290_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 295)
)
_OutBr290_Type = Integer32
_OutBr290_Object = MibScalar
outBr290 = _OutBr290_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 295, 1),
    _OutBr290_Type()
)
outBr290.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr290.setStatus("current")
if mibBuilder.loadTexts:
    outBr290.setUnits("tenth of Mbps")
_OutStream291_ObjectIdentity = ObjectIdentity
outStream291 = _OutStream291_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 296)
)
_OutBr291_Type = Integer32
_OutBr291_Object = MibScalar
outBr291 = _OutBr291_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 296, 1),
    _OutBr291_Type()
)
outBr291.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr291.setStatus("current")
if mibBuilder.loadTexts:
    outBr291.setUnits("tenth of Mbps")
_OutStream292_ObjectIdentity = ObjectIdentity
outStream292 = _OutStream292_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 297)
)
_OutBr292_Type = Integer32
_OutBr292_Object = MibScalar
outBr292 = _OutBr292_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 297, 1),
    _OutBr292_Type()
)
outBr292.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr292.setStatus("current")
if mibBuilder.loadTexts:
    outBr292.setUnits("tenth of Mbps")
_OutStream293_ObjectIdentity = ObjectIdentity
outStream293 = _OutStream293_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 298)
)
_OutBr293_Type = Integer32
_OutBr293_Object = MibScalar
outBr293 = _OutBr293_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 298, 1),
    _OutBr293_Type()
)
outBr293.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr293.setStatus("current")
if mibBuilder.loadTexts:
    outBr293.setUnits("tenth of Mbps")
_OutStream294_ObjectIdentity = ObjectIdentity
outStream294 = _OutStream294_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 299)
)
_OutBr294_Type = Integer32
_OutBr294_Object = MibScalar
outBr294 = _OutBr294_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 299, 1),
    _OutBr294_Type()
)
outBr294.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr294.setStatus("current")
if mibBuilder.loadTexts:
    outBr294.setUnits("tenth of Mbps")
_OutStream295_ObjectIdentity = ObjectIdentity
outStream295 = _OutStream295_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 300)
)
_OutBr295_Type = Integer32
_OutBr295_Object = MibScalar
outBr295 = _OutBr295_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 300, 1),
    _OutBr295_Type()
)
outBr295.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr295.setStatus("current")
if mibBuilder.loadTexts:
    outBr295.setUnits("tenth of Mbps")
_OutStream296_ObjectIdentity = ObjectIdentity
outStream296 = _OutStream296_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 301)
)
_OutBr296_Type = Integer32
_OutBr296_Object = MibScalar
outBr296 = _OutBr296_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 301, 1),
    _OutBr296_Type()
)
outBr296.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr296.setStatus("current")
if mibBuilder.loadTexts:
    outBr296.setUnits("tenth of Mbps")
_OutStream297_ObjectIdentity = ObjectIdentity
outStream297 = _OutStream297_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 302)
)
_OutBr297_Type = Integer32
_OutBr297_Object = MibScalar
outBr297 = _OutBr297_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 302, 1),
    _OutBr297_Type()
)
outBr297.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr297.setStatus("current")
if mibBuilder.loadTexts:
    outBr297.setUnits("tenth of Mbps")
_OutStream298_ObjectIdentity = ObjectIdentity
outStream298 = _OutStream298_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 303)
)
_OutBr298_Type = Integer32
_OutBr298_Object = MibScalar
outBr298 = _OutBr298_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 303, 1),
    _OutBr298_Type()
)
outBr298.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr298.setStatus("current")
if mibBuilder.loadTexts:
    outBr298.setUnits("tenth of Mbps")
_OutStream299_ObjectIdentity = ObjectIdentity
outStream299 = _OutStream299_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 304)
)
_OutBr299_Type = Integer32
_OutBr299_Object = MibScalar
outBr299 = _OutBr299_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 304, 1),
    _OutBr299_Type()
)
outBr299.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr299.setStatus("current")
if mibBuilder.loadTexts:
    outBr299.setUnits("tenth of Mbps")
_OutStream300_ObjectIdentity = ObjectIdentity
outStream300 = _OutStream300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 305)
)
_OutBr300_Type = Integer32
_OutBr300_Object = MibScalar
outBr300 = _OutBr300_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 305, 1),
    _OutBr300_Type()
)
outBr300.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr300.setStatus("current")
if mibBuilder.loadTexts:
    outBr300.setUnits("tenth of Mbps")
_OutStream301_ObjectIdentity = ObjectIdentity
outStream301 = _OutStream301_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 306)
)
_OutBr301_Type = Integer32
_OutBr301_Object = MibScalar
outBr301 = _OutBr301_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 306, 1),
    _OutBr301_Type()
)
outBr301.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr301.setStatus("current")
if mibBuilder.loadTexts:
    outBr301.setUnits("tenth of Mbps")
_OutStream302_ObjectIdentity = ObjectIdentity
outStream302 = _OutStream302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 307)
)
_OutBr302_Type = Integer32
_OutBr302_Object = MibScalar
outBr302 = _OutBr302_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 307, 1),
    _OutBr302_Type()
)
outBr302.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr302.setStatus("current")
if mibBuilder.loadTexts:
    outBr302.setUnits("tenth of Mbps")
_OutStream303_ObjectIdentity = ObjectIdentity
outStream303 = _OutStream303_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 308)
)
_OutBr303_Type = Integer32
_OutBr303_Object = MibScalar
outBr303 = _OutBr303_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 308, 1),
    _OutBr303_Type()
)
outBr303.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr303.setStatus("current")
if mibBuilder.loadTexts:
    outBr303.setUnits("tenth of Mbps")
_OutStream304_ObjectIdentity = ObjectIdentity
outStream304 = _OutStream304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 309)
)
_OutBr304_Type = Integer32
_OutBr304_Object = MibScalar
outBr304 = _OutBr304_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 309, 1),
    _OutBr304_Type()
)
outBr304.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr304.setStatus("current")
if mibBuilder.loadTexts:
    outBr304.setUnits("tenth of Mbps")
_OutStream305_ObjectIdentity = ObjectIdentity
outStream305 = _OutStream305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 310)
)
_OutBr305_Type = Integer32
_OutBr305_Object = MibScalar
outBr305 = _OutBr305_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 310, 1),
    _OutBr305_Type()
)
outBr305.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr305.setStatus("current")
if mibBuilder.loadTexts:
    outBr305.setUnits("tenth of Mbps")
_OutStream306_ObjectIdentity = ObjectIdentity
outStream306 = _OutStream306_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 311)
)
_OutBr306_Type = Integer32
_OutBr306_Object = MibScalar
outBr306 = _OutBr306_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 311, 1),
    _OutBr306_Type()
)
outBr306.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr306.setStatus("current")
if mibBuilder.loadTexts:
    outBr306.setUnits("tenth of Mbps")
_OutStream307_ObjectIdentity = ObjectIdentity
outStream307 = _OutStream307_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 312)
)
_OutBr307_Type = Integer32
_OutBr307_Object = MibScalar
outBr307 = _OutBr307_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 312, 1),
    _OutBr307_Type()
)
outBr307.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr307.setStatus("current")
if mibBuilder.loadTexts:
    outBr307.setUnits("tenth of Mbps")
_OutStream308_ObjectIdentity = ObjectIdentity
outStream308 = _OutStream308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 313)
)
_OutBr308_Type = Integer32
_OutBr308_Object = MibScalar
outBr308 = _OutBr308_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 313, 1),
    _OutBr308_Type()
)
outBr308.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr308.setStatus("current")
if mibBuilder.loadTexts:
    outBr308.setUnits("tenth of Mbps")
_OutStream309_ObjectIdentity = ObjectIdentity
outStream309 = _OutStream309_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 314)
)
_OutBr309_Type = Integer32
_OutBr309_Object = MibScalar
outBr309 = _OutBr309_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 314, 1),
    _OutBr309_Type()
)
outBr309.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr309.setStatus("current")
if mibBuilder.loadTexts:
    outBr309.setUnits("tenth of Mbps")
_OutStream310_ObjectIdentity = ObjectIdentity
outStream310 = _OutStream310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 315)
)
_OutBr310_Type = Integer32
_OutBr310_Object = MibScalar
outBr310 = _OutBr310_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 315, 1),
    _OutBr310_Type()
)
outBr310.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr310.setStatus("current")
if mibBuilder.loadTexts:
    outBr310.setUnits("tenth of Mbps")
_OutStream311_ObjectIdentity = ObjectIdentity
outStream311 = _OutStream311_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 316)
)
_OutBr311_Type = Integer32
_OutBr311_Object = MibScalar
outBr311 = _OutBr311_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 316, 1),
    _OutBr311_Type()
)
outBr311.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr311.setStatus("current")
if mibBuilder.loadTexts:
    outBr311.setUnits("tenth of Mbps")
_OutStream312_ObjectIdentity = ObjectIdentity
outStream312 = _OutStream312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 317)
)
_OutBr312_Type = Integer32
_OutBr312_Object = MibScalar
outBr312 = _OutBr312_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 317, 1),
    _OutBr312_Type()
)
outBr312.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr312.setStatus("current")
if mibBuilder.loadTexts:
    outBr312.setUnits("tenth of Mbps")
_OutStream313_ObjectIdentity = ObjectIdentity
outStream313 = _OutStream313_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 318)
)
_OutBr313_Type = Integer32
_OutBr313_Object = MibScalar
outBr313 = _OutBr313_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 318, 1),
    _OutBr313_Type()
)
outBr313.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr313.setStatus("current")
if mibBuilder.loadTexts:
    outBr313.setUnits("tenth of Mbps")
_OutStream314_ObjectIdentity = ObjectIdentity
outStream314 = _OutStream314_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 319)
)
_OutBr314_Type = Integer32
_OutBr314_Object = MibScalar
outBr314 = _OutBr314_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 319, 1),
    _OutBr314_Type()
)
outBr314.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr314.setStatus("current")
if mibBuilder.loadTexts:
    outBr314.setUnits("tenth of Mbps")
_OutStream315_ObjectIdentity = ObjectIdentity
outStream315 = _OutStream315_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 320)
)
_OutBr315_Type = Integer32
_OutBr315_Object = MibScalar
outBr315 = _OutBr315_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 320, 1),
    _OutBr315_Type()
)
outBr315.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr315.setStatus("current")
if mibBuilder.loadTexts:
    outBr315.setUnits("tenth of Mbps")
_OutStream316_ObjectIdentity = ObjectIdentity
outStream316 = _OutStream316_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 321)
)
_OutBr316_Type = Integer32
_OutBr316_Object = MibScalar
outBr316 = _OutBr316_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 321, 1),
    _OutBr316_Type()
)
outBr316.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr316.setStatus("current")
if mibBuilder.loadTexts:
    outBr316.setUnits("tenth of Mbps")
_OutStream317_ObjectIdentity = ObjectIdentity
outStream317 = _OutStream317_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 322)
)
_OutBr317_Type = Integer32
_OutBr317_Object = MibScalar
outBr317 = _OutBr317_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 322, 1),
    _OutBr317_Type()
)
outBr317.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr317.setStatus("current")
if mibBuilder.loadTexts:
    outBr317.setUnits("tenth of Mbps")
_OutStream318_ObjectIdentity = ObjectIdentity
outStream318 = _OutStream318_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 323)
)
_OutBr318_Type = Integer32
_OutBr318_Object = MibScalar
outBr318 = _OutBr318_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 323, 1),
    _OutBr318_Type()
)
outBr318.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr318.setStatus("current")
if mibBuilder.loadTexts:
    outBr318.setUnits("tenth of Mbps")
_OutStream319_ObjectIdentity = ObjectIdentity
outStream319 = _OutStream319_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 324)
)
_OutBr319_Type = Integer32
_OutBr319_Object = MibScalar
outBr319 = _OutBr319_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 324, 1),
    _OutBr319_Type()
)
outBr319.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr319.setStatus("current")
if mibBuilder.loadTexts:
    outBr319.setUnits("tenth of Mbps")
_OutStream320_ObjectIdentity = ObjectIdentity
outStream320 = _OutStream320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 325)
)
_OutBr320_Type = Integer32
_OutBr320_Object = MibScalar
outBr320 = _OutBr320_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 325, 1),
    _OutBr320_Type()
)
outBr320.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBr320.setStatus("current")
if mibBuilder.loadTexts:
    outBr320.setUnits("tenth of Mbps")
_CommStatus_ObjectIdentity = ObjectIdentity
commStatus = _CommStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 326)
)
_InTotbr_Type = Integer32
_InTotbr_Object = MibScalar
inTotbr = _InTotbr_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 326, 1),
    _InTotbr_Type()
)
inTotbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inTotbr.setStatus("current")
if mibBuilder.loadTexts:
    inTotbr.setUnits("tenth of Mbps")
_OutTotbr_Type = Integer32
_OutTotbr_Object = MibScalar
outTotbr = _OutTotbr_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 326, 2),
    _OutTotbr_Type()
)
outTotbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outTotbr.setStatus("current")
if mibBuilder.loadTexts:
    outTotbr.setUnits("tenth of Mbps")
_CpuLoad_Type = Integer32
_CpuLoad_Object = MibScalar
cpuLoad = _CpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 326, 3),
    _CpuLoad_Type()
)
cpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad.setStatus("current")
if mibBuilder.loadTexts:
    cpuLoad.setUnits("%")
_IntTemp_Type = Integer32
_IntTemp_Object = MibScalar
intTemp = _IntTemp_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 326, 4),
    _IntTemp_Type()
)
intTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intTemp.setStatus("current")
if mibBuilder.loadTexts:
    intTemp.setUnits("deg C")
_Volt_Type = Integer32
_Volt_Object = MibScalar
volt = _Volt_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 1, 326, 5),
    _Volt_Type()
)
volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volt.setStatus("current")
if mibBuilder.loadTexts:
    volt.setUnits("tenth of volt")
_Sti440alarms_ObjectIdentity = ObjectIdentity
sti440alarms = _Sti440alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2)
)
_AlarmStlink_Type = DefStatus
_AlarmStlink_Object = MibScalar
alarmStlink = _AlarmStlink_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 1),
    _AlarmStlink_Type()
)
alarmStlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStlink.setStatus("current")
_AlarmCtrlink_Type = DefStatus
_AlarmCtrlink_Object = MibScalar
alarmCtrlink = _AlarmCtrlink_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 2),
    _AlarmCtrlink_Type()
)
alarmCtrlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCtrlink.setStatus("current")
_AlarmBrovf_Type = DefStatus
_AlarmBrovf_Object = MibScalar
alarmBrovf = _AlarmBrovf_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 3),
    _AlarmBrovf_Type()
)
alarmBrovf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBrovf.setStatus("current")
_AlarmUnlock1_Type = DefStatus
_AlarmUnlock1_Object = MibScalar
alarmUnlock1 = _AlarmUnlock1_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 4),
    _AlarmUnlock1_Type()
)
alarmUnlock1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock1.setStatus("current")
_AlarmUnlock2_Type = DefStatus
_AlarmUnlock2_Object = MibScalar
alarmUnlock2 = _AlarmUnlock2_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 5),
    _AlarmUnlock2_Type()
)
alarmUnlock2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock2.setStatus("current")
_AlarmUnlock3_Type = DefStatus
_AlarmUnlock3_Object = MibScalar
alarmUnlock3 = _AlarmUnlock3_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 6),
    _AlarmUnlock3_Type()
)
alarmUnlock3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock3.setStatus("current")
_AlarmUnlock4_Type = DefStatus
_AlarmUnlock4_Object = MibScalar
alarmUnlock4 = _AlarmUnlock4_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 7),
    _AlarmUnlock4_Type()
)
alarmUnlock4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock4.setStatus("current")
_AlarmUnlock5_Type = DefStatus
_AlarmUnlock5_Object = MibScalar
alarmUnlock5 = _AlarmUnlock5_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 8),
    _AlarmUnlock5_Type()
)
alarmUnlock5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock5.setStatus("current")
_AlarmUnlock6_Type = DefStatus
_AlarmUnlock6_Object = MibScalar
alarmUnlock6 = _AlarmUnlock6_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 9),
    _AlarmUnlock6_Type()
)
alarmUnlock6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock6.setStatus("current")
_AlarmUnlock7_Type = DefStatus
_AlarmUnlock7_Object = MibScalar
alarmUnlock7 = _AlarmUnlock7_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 10),
    _AlarmUnlock7_Type()
)
alarmUnlock7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock7.setStatus("current")
_AlarmUnlock8_Type = DefStatus
_AlarmUnlock8_Object = MibScalar
alarmUnlock8 = _AlarmUnlock8_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 11),
    _AlarmUnlock8_Type()
)
alarmUnlock8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock8.setStatus("current")
_AlarmUnlock9_Type = DefStatus
_AlarmUnlock9_Object = MibScalar
alarmUnlock9 = _AlarmUnlock9_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 12),
    _AlarmUnlock9_Type()
)
alarmUnlock9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUnlock9.setStatus("current")
_AlarmPowerr_Type = DefStatus
_AlarmPowerr_Object = MibScalar
alarmPowerr = _AlarmPowerr_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 13),
    _AlarmPowerr_Type()
)
alarmPowerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPowerr.setStatus("current")
_AlarmTemperr_Type = DefStatus
_AlarmTemperr_Object = MibScalar
alarmTemperr = _AlarmTemperr_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 14),
    _AlarmTemperr_Type()
)
alarmTemperr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTemperr.setStatus("current")
_AlarmIbrer_Type = DefStatus
_AlarmIbrer_Object = MibScalar
alarmIbrer = _AlarmIbrer_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 2, 15),
    _AlarmIbrer_Type()
)
alarmIbrer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIbrer.setStatus("current")
_Sti440notifications_ObjectIdentity = ObjectIdentity
sti440notifications = _Sti440notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3)
)
_Sti440Info_ObjectIdentity = ObjectIdentity
sti440Info = _Sti440Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 4)
)
_InfVersion_Type = DisplayString
_InfVersion_Object = MibScalar
infVersion = _InfVersion_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 4, 1),
    _InfVersion_Type()
)
infVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infVersion.setStatus("current")
_InfSerNum_Type = DisplayString
_InfSerNum_Object = MibScalar
infSerNum = _InfSerNum_Object(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 4, 2),
    _InfSerNum_Type()
)
infSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infSerNum.setStatus("current")
_Terrasti440MIBConformance_ObjectIdentity = ObjectIdentity
terrasti440MIBConformance = _Terrasti440MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 5)
)
_Terrasti440MIBGroups_ObjectIdentity = ObjectIdentity
terrasti440MIBGroups = _Terrasti440MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 5, 1)
)

# Managed Objects groups

sti440TerraMibAllObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 5, 1, 1)
)
sti440TerraMibAllObjects.setObjects(
      *(("TERRA-sti440-MIB", "inLock1"),
        ("TERRA-sti440-MIB", "instd1"),
        ("TERRA-sti440-MIB", "inlevel1"),
        ("TERRA-sti440-MIB", "inmod1"),
        ("TERRA-sti440-MIB", "insnr1"),
        ("TERRA-sti440-MIB", "inber1"),
        ("TERRA-sti440-MIB", "inper1"),
        ("TERRA-sti440-MIB", "inuncorr1"),
        ("TERRA-sti440-MIB", "inbr1"),
        ("TERRA-sti440-MIB", "inccerr1"),
        ("TERRA-sti440-MIB", "intotpack1"),
        ("TERRA-sti440-MIB", "inLock2"),
        ("TERRA-sti440-MIB", "instd2"),
        ("TERRA-sti440-MIB", "inlevel2"),
        ("TERRA-sti440-MIB", "inmod2"),
        ("TERRA-sti440-MIB", "insnr2"),
        ("TERRA-sti440-MIB", "inber2"),
        ("TERRA-sti440-MIB", "inper2"),
        ("TERRA-sti440-MIB", "inuncorr2"),
        ("TERRA-sti440-MIB", "inbr2"),
        ("TERRA-sti440-MIB", "inccerr2"),
        ("TERRA-sti440-MIB", "intotpack2"),
        ("TERRA-sti440-MIB", "inLock3"),
        ("TERRA-sti440-MIB", "instd3"),
        ("TERRA-sti440-MIB", "inlevel3"),
        ("TERRA-sti440-MIB", "inmod3"),
        ("TERRA-sti440-MIB", "insnr3"),
        ("TERRA-sti440-MIB", "inber3"),
        ("TERRA-sti440-MIB", "inper3"),
        ("TERRA-sti440-MIB", "inuncorr3"),
        ("TERRA-sti440-MIB", "inbr3"),
        ("TERRA-sti440-MIB", "inccerr3"),
        ("TERRA-sti440-MIB", "intotpack3"),
        ("TERRA-sti440-MIB", "inLock4"),
        ("TERRA-sti440-MIB", "instd4"),
        ("TERRA-sti440-MIB", "inlevel4"),
        ("TERRA-sti440-MIB", "inmod4"),
        ("TERRA-sti440-MIB", "insnr4"),
        ("TERRA-sti440-MIB", "inber4"),
        ("TERRA-sti440-MIB", "inper4"),
        ("TERRA-sti440-MIB", "inuncorr4"),
        ("TERRA-sti440-MIB", "inbr4"),
        ("TERRA-sti440-MIB", "inccerr4"),
        ("TERRA-sti440-MIB", "intotpack4"),
        ("TERRA-sti440-MIB", "usbinBR"),
        ("TERRA-sti440-MIB", "outBr1"),
        ("TERRA-sti440-MIB", "outBr2"),
        ("TERRA-sti440-MIB", "outBr3"),
        ("TERRA-sti440-MIB", "outBr4"),
        ("TERRA-sti440-MIB", "outBr5"),
        ("TERRA-sti440-MIB", "outBr6"),
        ("TERRA-sti440-MIB", "outBr7"),
        ("TERRA-sti440-MIB", "outBr8"),
        ("TERRA-sti440-MIB", "outBr9"),
        ("TERRA-sti440-MIB", "outBr10"),
        ("TERRA-sti440-MIB", "outBr11"),
        ("TERRA-sti440-MIB", "outBr12"),
        ("TERRA-sti440-MIB", "outBr13"),
        ("TERRA-sti440-MIB", "outBr14"),
        ("TERRA-sti440-MIB", "outBr15"),
        ("TERRA-sti440-MIB", "outBr16"),
        ("TERRA-sti440-MIB", "outBr17"),
        ("TERRA-sti440-MIB", "outBr18"),
        ("TERRA-sti440-MIB", "outBr19"),
        ("TERRA-sti440-MIB", "outBr20"),
        ("TERRA-sti440-MIB", "outBr21"),
        ("TERRA-sti440-MIB", "outBr22"),
        ("TERRA-sti440-MIB", "outBr23"),
        ("TERRA-sti440-MIB", "outBr24"),
        ("TERRA-sti440-MIB", "outBr25"),
        ("TERRA-sti440-MIB", "outBr26"),
        ("TERRA-sti440-MIB", "outBr27"),
        ("TERRA-sti440-MIB", "outBr28"),
        ("TERRA-sti440-MIB", "outBr29"),
        ("TERRA-sti440-MIB", "outBr30"),
        ("TERRA-sti440-MIB", "outBr31"),
        ("TERRA-sti440-MIB", "outBr32"),
        ("TERRA-sti440-MIB", "outBr33"),
        ("TERRA-sti440-MIB", "outBr34"),
        ("TERRA-sti440-MIB", "outBr35"),
        ("TERRA-sti440-MIB", "outBr36"),
        ("TERRA-sti440-MIB", "outBr37"),
        ("TERRA-sti440-MIB", "outBr38"),
        ("TERRA-sti440-MIB", "outBr39"),
        ("TERRA-sti440-MIB", "outBr40"),
        ("TERRA-sti440-MIB", "outBr41"),
        ("TERRA-sti440-MIB", "outBr42"),
        ("TERRA-sti440-MIB", "outBr43"),
        ("TERRA-sti440-MIB", "outBr44"),
        ("TERRA-sti440-MIB", "outBr45"),
        ("TERRA-sti440-MIB", "outBr46"),
        ("TERRA-sti440-MIB", "outBr47"),
        ("TERRA-sti440-MIB", "outBr48"),
        ("TERRA-sti440-MIB", "outBr49"),
        ("TERRA-sti440-MIB", "outBr50"),
        ("TERRA-sti440-MIB", "outBr51"),
        ("TERRA-sti440-MIB", "outBr52"),
        ("TERRA-sti440-MIB", "outBr53"),
        ("TERRA-sti440-MIB", "outBr54"),
        ("TERRA-sti440-MIB", "outBr55"),
        ("TERRA-sti440-MIB", "outBr56"),
        ("TERRA-sti440-MIB", "outBr57"),
        ("TERRA-sti440-MIB", "outBr58"),
        ("TERRA-sti440-MIB", "outBr59"),
        ("TERRA-sti440-MIB", "outBr60"),
        ("TERRA-sti440-MIB", "outBr61"),
        ("TERRA-sti440-MIB", "outBr62"),
        ("TERRA-sti440-MIB", "outBr63"),
        ("TERRA-sti440-MIB", "outBr64"),
        ("TERRA-sti440-MIB", "outBr65"),
        ("TERRA-sti440-MIB", "outBr66"),
        ("TERRA-sti440-MIB", "outBr67"),
        ("TERRA-sti440-MIB", "outBr68"),
        ("TERRA-sti440-MIB", "outBr69"),
        ("TERRA-sti440-MIB", "outBr70"),
        ("TERRA-sti440-MIB", "outBr71"),
        ("TERRA-sti440-MIB", "outBr72"),
        ("TERRA-sti440-MIB", "outBr73"),
        ("TERRA-sti440-MIB", "outBr74"),
        ("TERRA-sti440-MIB", "outBr75"),
        ("TERRA-sti440-MIB", "outBr76"),
        ("TERRA-sti440-MIB", "outBr77"),
        ("TERRA-sti440-MIB", "outBr78"),
        ("TERRA-sti440-MIB", "outBr79"),
        ("TERRA-sti440-MIB", "outBr80"),
        ("TERRA-sti440-MIB", "outBr81"),
        ("TERRA-sti440-MIB", "outBr82"),
        ("TERRA-sti440-MIB", "outBr83"),
        ("TERRA-sti440-MIB", "outBr84"),
        ("TERRA-sti440-MIB", "outBr85"),
        ("TERRA-sti440-MIB", "outBr86"),
        ("TERRA-sti440-MIB", "outBr87"),
        ("TERRA-sti440-MIB", "outBr88"),
        ("TERRA-sti440-MIB", "outBr89"),
        ("TERRA-sti440-MIB", "outBr90"),
        ("TERRA-sti440-MIB", "outBr91"),
        ("TERRA-sti440-MIB", "outBr92"),
        ("TERRA-sti440-MIB", "outBr93"),
        ("TERRA-sti440-MIB", "outBr94"),
        ("TERRA-sti440-MIB", "outBr95"),
        ("TERRA-sti440-MIB", "outBr96"),
        ("TERRA-sti440-MIB", "outBr97"),
        ("TERRA-sti440-MIB", "outBr98"),
        ("TERRA-sti440-MIB", "outBr99"),
        ("TERRA-sti440-MIB", "outBr100"),
        ("TERRA-sti440-MIB", "outBr101"),
        ("TERRA-sti440-MIB", "outBr102"),
        ("TERRA-sti440-MIB", "outBr103"),
        ("TERRA-sti440-MIB", "outBr104"),
        ("TERRA-sti440-MIB", "outBr105"),
        ("TERRA-sti440-MIB", "outBr106"),
        ("TERRA-sti440-MIB", "outBr107"),
        ("TERRA-sti440-MIB", "outBr108"),
        ("TERRA-sti440-MIB", "outBr109"),
        ("TERRA-sti440-MIB", "outBr110"),
        ("TERRA-sti440-MIB", "outBr111"),
        ("TERRA-sti440-MIB", "outBr112"),
        ("TERRA-sti440-MIB", "outBr113"),
        ("TERRA-sti440-MIB", "outBr114"),
        ("TERRA-sti440-MIB", "outBr115"),
        ("TERRA-sti440-MIB", "outBr116"),
        ("TERRA-sti440-MIB", "outBr117"),
        ("TERRA-sti440-MIB", "outBr118"),
        ("TERRA-sti440-MIB", "outBr119"),
        ("TERRA-sti440-MIB", "outBr120"),
        ("TERRA-sti440-MIB", "outBr121"),
        ("TERRA-sti440-MIB", "outBr122"),
        ("TERRA-sti440-MIB", "outBr123"),
        ("TERRA-sti440-MIB", "outBr124"),
        ("TERRA-sti440-MIB", "outBr125"),
        ("TERRA-sti440-MIB", "outBr126"),
        ("TERRA-sti440-MIB", "outBr127"),
        ("TERRA-sti440-MIB", "outBr128"),
        ("TERRA-sti440-MIB", "outBr129"),
        ("TERRA-sti440-MIB", "outBr130"),
        ("TERRA-sti440-MIB", "outBr131"),
        ("TERRA-sti440-MIB", "outBr132"),
        ("TERRA-sti440-MIB", "outBr133"),
        ("TERRA-sti440-MIB", "outBr134"),
        ("TERRA-sti440-MIB", "outBr135"),
        ("TERRA-sti440-MIB", "outBr136"),
        ("TERRA-sti440-MIB", "outBr137"),
        ("TERRA-sti440-MIB", "outBr138"),
        ("TERRA-sti440-MIB", "outBr139"),
        ("TERRA-sti440-MIB", "outBr140"),
        ("TERRA-sti440-MIB", "outBr141"),
        ("TERRA-sti440-MIB", "outBr142"),
        ("TERRA-sti440-MIB", "outBr143"),
        ("TERRA-sti440-MIB", "outBr144"),
        ("TERRA-sti440-MIB", "outBr145"),
        ("TERRA-sti440-MIB", "outBr146"),
        ("TERRA-sti440-MIB", "outBr147"),
        ("TERRA-sti440-MIB", "outBr148"),
        ("TERRA-sti440-MIB", "outBr149"),
        ("TERRA-sti440-MIB", "outBr150"),
        ("TERRA-sti440-MIB", "outBr151"),
        ("TERRA-sti440-MIB", "outBr152"),
        ("TERRA-sti440-MIB", "outBr153"),
        ("TERRA-sti440-MIB", "outBr154"),
        ("TERRA-sti440-MIB", "outBr155"),
        ("TERRA-sti440-MIB", "outBr156"),
        ("TERRA-sti440-MIB", "outBr157"),
        ("TERRA-sti440-MIB", "outBr158"),
        ("TERRA-sti440-MIB", "outBr159"),
        ("TERRA-sti440-MIB", "outBr160"),
        ("TERRA-sti440-MIB", "outBr161"),
        ("TERRA-sti440-MIB", "outBr162"),
        ("TERRA-sti440-MIB", "outBr163"),
        ("TERRA-sti440-MIB", "outBr164"),
        ("TERRA-sti440-MIB", "outBr165"),
        ("TERRA-sti440-MIB", "outBr166"),
        ("TERRA-sti440-MIB", "outBr167"),
        ("TERRA-sti440-MIB", "outBr168"),
        ("TERRA-sti440-MIB", "outBr169"),
        ("TERRA-sti440-MIB", "outBr170"),
        ("TERRA-sti440-MIB", "outBr171"),
        ("TERRA-sti440-MIB", "outBr172"),
        ("TERRA-sti440-MIB", "outBr173"),
        ("TERRA-sti440-MIB", "outBr174"),
        ("TERRA-sti440-MIB", "outBr175"),
        ("TERRA-sti440-MIB", "outBr176"),
        ("TERRA-sti440-MIB", "outBr177"),
        ("TERRA-sti440-MIB", "outBr178"),
        ("TERRA-sti440-MIB", "outBr179"),
        ("TERRA-sti440-MIB", "outBr180"),
        ("TERRA-sti440-MIB", "outBr181"),
        ("TERRA-sti440-MIB", "outBr182"),
        ("TERRA-sti440-MIB", "outBr183"),
        ("TERRA-sti440-MIB", "outBr184"),
        ("TERRA-sti440-MIB", "outBr185"),
        ("TERRA-sti440-MIB", "outBr186"),
        ("TERRA-sti440-MIB", "outBr187"),
        ("TERRA-sti440-MIB", "outBr188"),
        ("TERRA-sti440-MIB", "outBr189"),
        ("TERRA-sti440-MIB", "outBr190"),
        ("TERRA-sti440-MIB", "outBr191"),
        ("TERRA-sti440-MIB", "outBr192"),
        ("TERRA-sti440-MIB", "outBr193"),
        ("TERRA-sti440-MIB", "outBr194"),
        ("TERRA-sti440-MIB", "outBr195"),
        ("TERRA-sti440-MIB", "outBr196"),
        ("TERRA-sti440-MIB", "outBr197"),
        ("TERRA-sti440-MIB", "outBr198"),
        ("TERRA-sti440-MIB", "outBr199"),
        ("TERRA-sti440-MIB", "outBr200"),
        ("TERRA-sti440-MIB", "outBr201"),
        ("TERRA-sti440-MIB", "outBr202"),
        ("TERRA-sti440-MIB", "outBr203"),
        ("TERRA-sti440-MIB", "outBr204"),
        ("TERRA-sti440-MIB", "outBr205"),
        ("TERRA-sti440-MIB", "outBr206"),
        ("TERRA-sti440-MIB", "outBr207"),
        ("TERRA-sti440-MIB", "outBr208"),
        ("TERRA-sti440-MIB", "outBr209"),
        ("TERRA-sti440-MIB", "outBr210"),
        ("TERRA-sti440-MIB", "outBr211"),
        ("TERRA-sti440-MIB", "outBr212"),
        ("TERRA-sti440-MIB", "outBr213"),
        ("TERRA-sti440-MIB", "outBr214"),
        ("TERRA-sti440-MIB", "outBr215"),
        ("TERRA-sti440-MIB", "outBr216"),
        ("TERRA-sti440-MIB", "outBr217"),
        ("TERRA-sti440-MIB", "outBr218"),
        ("TERRA-sti440-MIB", "outBr219"),
        ("TERRA-sti440-MIB", "outBr220"),
        ("TERRA-sti440-MIB", "outBr221"),
        ("TERRA-sti440-MIB", "outBr222"),
        ("TERRA-sti440-MIB", "outBr223"),
        ("TERRA-sti440-MIB", "outBr224"),
        ("TERRA-sti440-MIB", "outBr225"),
        ("TERRA-sti440-MIB", "outBr226"),
        ("TERRA-sti440-MIB", "outBr227"),
        ("TERRA-sti440-MIB", "outBr228"),
        ("TERRA-sti440-MIB", "outBr229"),
        ("TERRA-sti440-MIB", "outBr230"),
        ("TERRA-sti440-MIB", "outBr231"),
        ("TERRA-sti440-MIB", "outBr232"),
        ("TERRA-sti440-MIB", "outBr233"),
        ("TERRA-sti440-MIB", "outBr234"),
        ("TERRA-sti440-MIB", "outBr235"),
        ("TERRA-sti440-MIB", "outBr236"),
        ("TERRA-sti440-MIB", "outBr237"),
        ("TERRA-sti440-MIB", "outBr238"),
        ("TERRA-sti440-MIB", "outBr239"),
        ("TERRA-sti440-MIB", "outBr240"),
        ("TERRA-sti440-MIB", "outBr241"),
        ("TERRA-sti440-MIB", "outBr242"),
        ("TERRA-sti440-MIB", "outBr243"),
        ("TERRA-sti440-MIB", "outBr244"),
        ("TERRA-sti440-MIB", "outBr245"),
        ("TERRA-sti440-MIB", "outBr246"),
        ("TERRA-sti440-MIB", "outBr247"),
        ("TERRA-sti440-MIB", "outBr248"),
        ("TERRA-sti440-MIB", "outBr249"),
        ("TERRA-sti440-MIB", "outBr250"),
        ("TERRA-sti440-MIB", "outBr251"),
        ("TERRA-sti440-MIB", "outBr252"),
        ("TERRA-sti440-MIB", "outBr253"),
        ("TERRA-sti440-MIB", "outBr254"),
        ("TERRA-sti440-MIB", "outBr255"),
        ("TERRA-sti440-MIB", "outBr256"),
        ("TERRA-sti440-MIB", "outBr257"),
        ("TERRA-sti440-MIB", "outBr258"),
        ("TERRA-sti440-MIB", "outBr259"),
        ("TERRA-sti440-MIB", "outBr260"),
        ("TERRA-sti440-MIB", "outBr261"),
        ("TERRA-sti440-MIB", "outBr262"),
        ("TERRA-sti440-MIB", "outBr263"),
        ("TERRA-sti440-MIB", "outBr264"),
        ("TERRA-sti440-MIB", "outBr265"),
        ("TERRA-sti440-MIB", "outBr266"),
        ("TERRA-sti440-MIB", "outBr267"),
        ("TERRA-sti440-MIB", "outBr268"),
        ("TERRA-sti440-MIB", "outBr269"),
        ("TERRA-sti440-MIB", "outBr270"),
        ("TERRA-sti440-MIB", "outBr271"),
        ("TERRA-sti440-MIB", "outBr272"),
        ("TERRA-sti440-MIB", "outBr273"),
        ("TERRA-sti440-MIB", "outBr274"),
        ("TERRA-sti440-MIB", "outBr275"),
        ("TERRA-sti440-MIB", "outBr276"),
        ("TERRA-sti440-MIB", "outBr277"),
        ("TERRA-sti440-MIB", "outBr278"),
        ("TERRA-sti440-MIB", "outBr279"),
        ("TERRA-sti440-MIB", "outBr280"),
        ("TERRA-sti440-MIB", "outBr281"),
        ("TERRA-sti440-MIB", "outBr282"),
        ("TERRA-sti440-MIB", "outBr283"),
        ("TERRA-sti440-MIB", "outBr284"),
        ("TERRA-sti440-MIB", "outBr285"),
        ("TERRA-sti440-MIB", "outBr286"),
        ("TERRA-sti440-MIB", "outBr287"),
        ("TERRA-sti440-MIB", "outBr288"),
        ("TERRA-sti440-MIB", "outBr289"),
        ("TERRA-sti440-MIB", "outBr290"),
        ("TERRA-sti440-MIB", "outBr291"),
        ("TERRA-sti440-MIB", "outBr292"),
        ("TERRA-sti440-MIB", "outBr293"),
        ("TERRA-sti440-MIB", "outBr294"),
        ("TERRA-sti440-MIB", "outBr295"),
        ("TERRA-sti440-MIB", "outBr296"),
        ("TERRA-sti440-MIB", "outBr297"),
        ("TERRA-sti440-MIB", "outBr298"),
        ("TERRA-sti440-MIB", "outBr299"),
        ("TERRA-sti440-MIB", "outBr300"),
        ("TERRA-sti440-MIB", "outBr301"),
        ("TERRA-sti440-MIB", "outBr302"),
        ("TERRA-sti440-MIB", "outBr303"),
        ("TERRA-sti440-MIB", "outBr304"),
        ("TERRA-sti440-MIB", "outBr305"),
        ("TERRA-sti440-MIB", "outBr306"),
        ("TERRA-sti440-MIB", "outBr307"),
        ("TERRA-sti440-MIB", "outBr308"),
        ("TERRA-sti440-MIB", "outBr309"),
        ("TERRA-sti440-MIB", "outBr310"),
        ("TERRA-sti440-MIB", "outBr311"),
        ("TERRA-sti440-MIB", "outBr312"),
        ("TERRA-sti440-MIB", "outBr313"),
        ("TERRA-sti440-MIB", "outBr314"),
        ("TERRA-sti440-MIB", "outBr315"),
        ("TERRA-sti440-MIB", "outBr316"),
        ("TERRA-sti440-MIB", "outBr317"),
        ("TERRA-sti440-MIB", "outBr318"),
        ("TERRA-sti440-MIB", "outBr319"),
        ("TERRA-sti440-MIB", "outBr320"),
        ("TERRA-sti440-MIB", "inTotbr"),
        ("TERRA-sti440-MIB", "outTotbr"),
        ("TERRA-sti440-MIB", "cpuLoad"),
        ("TERRA-sti440-MIB", "intTemp"),
        ("TERRA-sti440-MIB", "volt"),
        ("TERRA-sti440-MIB", "alarmStlink"),
        ("TERRA-sti440-MIB", "alarmCtrlink"),
        ("TERRA-sti440-MIB", "alarmBrovf"),
        ("TERRA-sti440-MIB", "alarmUnlock1"),
        ("TERRA-sti440-MIB", "alarmUnlock2"),
        ("TERRA-sti440-MIB", "alarmUnlock3"),
        ("TERRA-sti440-MIB", "alarmUnlock4"),
        ("TERRA-sti440-MIB", "alarmUnlock5"),
        ("TERRA-sti440-MIB", "alarmUnlock6"),
        ("TERRA-sti440-MIB", "alarmUnlock7"),
        ("TERRA-sti440-MIB", "alarmUnlock8"),
        ("TERRA-sti440-MIB", "alarmUnlock9"),
        ("TERRA-sti440-MIB", "alarmPowerr"),
        ("TERRA-sti440-MIB", "alarmTemperr"),
        ("TERRA-sti440-MIB", "alarmIbrer"),
        ("TERRA-sti440-MIB", "infVersion"),
        ("TERRA-sti440-MIB", "infSerNum"))
)
if mibBuilder.loadTexts:
    sti440TerraMibAllObjects.setStatus("current")


# Notification objects

notifyStlink = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 1)
)
notifyStlink.setObjects(
    ("TERRA-sti440-MIB", "alarmStlink")
)
if mibBuilder.loadTexts:
    notifyStlink.setStatus(
        "current"
    )

notifyCtrlink = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 2)
)
notifyCtrlink.setObjects(
    ("TERRA-sti440-MIB", "alarmCtrlink")
)
if mibBuilder.loadTexts:
    notifyCtrlink.setStatus(
        "current"
    )

notifyBrovf = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 3)
)
notifyBrovf.setObjects(
    ("TERRA-sti440-MIB", "alarmBrovf")
)
if mibBuilder.loadTexts:
    notifyBrovf.setStatus(
        "current"
    )

notifyUnlock1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 4)
)
notifyUnlock1.setObjects(
    ("TERRA-sti440-MIB", "alarmUnlock1")
)
if mibBuilder.loadTexts:
    notifyUnlock1.setStatus(
        "current"
    )

notifyUnlock2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 5)
)
notifyUnlock2.setObjects(
    ("TERRA-sti440-MIB", "alarmUnlock2")
)
if mibBuilder.loadTexts:
    notifyUnlock2.setStatus(
        "current"
    )

notifyUnlock3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 6)
)
notifyUnlock3.setObjects(
    ("TERRA-sti440-MIB", "alarmUnlock3")
)
if mibBuilder.loadTexts:
    notifyUnlock3.setStatus(
        "current"
    )

notifyUnlock4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 7)
)
notifyUnlock4.setObjects(
    ("TERRA-sti440-MIB", "alarmUnlock4")
)
if mibBuilder.loadTexts:
    notifyUnlock4.setStatus(
        "current"
    )

notifyUnlock5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 8)
)
notifyUnlock5.setObjects(
    ("TERRA-sti440-MIB", "alarmUnlock5")
)
if mibBuilder.loadTexts:
    notifyUnlock5.setStatus(
        "current"
    )

notifyUnlock6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 9)
)
notifyUnlock6.setObjects(
    ("TERRA-sti440-MIB", "alarmUnlock6")
)
if mibBuilder.loadTexts:
    notifyUnlock6.setStatus(
        "current"
    )

notifyUnlock7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 10)
)
notifyUnlock7.setObjects(
    ("TERRA-sti440-MIB", "alarmUnlock7")
)
if mibBuilder.loadTexts:
    notifyUnlock7.setStatus(
        "current"
    )

notifyUnlock8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 11)
)
notifyUnlock8.setObjects(
    ("TERRA-sti440-MIB", "alarmUnlock8")
)
if mibBuilder.loadTexts:
    notifyUnlock8.setStatus(
        "current"
    )

notifyUnlock9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 12)
)
notifyUnlock9.setObjects(
    ("TERRA-sti440-MIB", "alarmUnlock9")
)
if mibBuilder.loadTexts:
    notifyUnlock9.setStatus(
        "current"
    )

notifyPowerr = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 13)
)
notifyPowerr.setObjects(
    ("TERRA-sti440-MIB", "alarmPowerr")
)
if mibBuilder.loadTexts:
    notifyPowerr.setStatus(
        "current"
    )

notifyTemperr = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 14)
)
notifyTemperr.setObjects(
    ("TERRA-sti440-MIB", "alarmTemperr")
)
if mibBuilder.loadTexts:
    notifyTemperr.setStatus(
        "current"
    )

notifyIbrer = NotificationType(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 3, 15)
)
notifyIbrer.setObjects(
    ("TERRA-sti440-MIB", "alarmIbrer")
)
if mibBuilder.loadTexts:
    notifyIbrer.setStatus(
        "current"
    )


# Notifications groups

sti440TerraMibAllNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 30631, 1, 18, 5, 1, 2)
)
sti440TerraMibAllNotifications.setObjects(
      *(("TERRA-sti440-MIB", "notifyStlink"),
        ("TERRA-sti440-MIB", "notifyCtrlink"),
        ("TERRA-sti440-MIB", "notifyBrovf"),
        ("TERRA-sti440-MIB", "notifyUnlock1"),
        ("TERRA-sti440-MIB", "notifyUnlock2"),
        ("TERRA-sti440-MIB", "notifyUnlock3"),
        ("TERRA-sti440-MIB", "notifyUnlock4"),
        ("TERRA-sti440-MIB", "notifyUnlock5"),
        ("TERRA-sti440-MIB", "notifyUnlock6"),
        ("TERRA-sti440-MIB", "notifyUnlock7"),
        ("TERRA-sti440-MIB", "notifyUnlock8"),
        ("TERRA-sti440-MIB", "notifyUnlock9"),
        ("TERRA-sti440-MIB", "notifyPowerr"),
        ("TERRA-sti440-MIB", "notifyTemperr"),
        ("TERRA-sti440-MIB", "notifyIbrer"))
)
if mibBuilder.loadTexts:
    sti440TerraMibAllNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERRA-sti440-MIB",
    **{"terra-sti440": terra_sti440,
       "sti440status": sti440status,
       "rFinStatus1": rFinStatus1,
       "inLock1": inLock1,
       "instd1": instd1,
       "inlevel1": inlevel1,
       "inmod1": inmod1,
       "insnr1": insnr1,
       "inber1": inber1,
       "inper1": inper1,
       "inuncorr1": inuncorr1,
       "inbr1": inbr1,
       "inccerr1": inccerr1,
       "intotpack1": intotpack1,
       "rFinStatus2": rFinStatus2,
       "inLock2": inLock2,
       "instd2": instd2,
       "inlevel2": inlevel2,
       "inmod2": inmod2,
       "insnr2": insnr2,
       "inber2": inber2,
       "inper2": inper2,
       "inuncorr2": inuncorr2,
       "inbr2": inbr2,
       "inccerr2": inccerr2,
       "intotpack2": intotpack2,
       "rFinStatus3": rFinStatus3,
       "inLock3": inLock3,
       "instd3": instd3,
       "inlevel3": inlevel3,
       "inmod3": inmod3,
       "insnr3": insnr3,
       "inber3": inber3,
       "inper3": inper3,
       "inuncorr3": inuncorr3,
       "inbr3": inbr3,
       "inccerr3": inccerr3,
       "intotpack3": intotpack3,
       "rFinStatus4": rFinStatus4,
       "inLock4": inLock4,
       "instd4": instd4,
       "inlevel4": inlevel4,
       "inmod4": inmod4,
       "insnr4": insnr4,
       "inber4": inber4,
       "inper4": inper4,
       "inuncorr4": inuncorr4,
       "inbr4": inbr4,
       "inccerr4": inccerr4,
       "intotpack4": intotpack4,
       "usbStatus": usbStatus,
       "usbinBR": usbinBR,
       "outStream1": outStream1,
       "outBr1": outBr1,
       "outStream2": outStream2,
       "outBr2": outBr2,
       "outStream3": outStream3,
       "outBr3": outBr3,
       "outStream4": outStream4,
       "outBr4": outBr4,
       "outStream5": outStream5,
       "outBr5": outBr5,
       "outStream6": outStream6,
       "outBr6": outBr6,
       "outStream7": outStream7,
       "outBr7": outBr7,
       "outStream8": outStream8,
       "outBr8": outBr8,
       "outStream9": outStream9,
       "outBr9": outBr9,
       "outStream10": outStream10,
       "outBr10": outBr10,
       "outStream11": outStream11,
       "outBr11": outBr11,
       "outStream12": outStream12,
       "outBr12": outBr12,
       "outStream13": outStream13,
       "outBr13": outBr13,
       "outStream14": outStream14,
       "outBr14": outBr14,
       "outStream15": outStream15,
       "outBr15": outBr15,
       "outStream16": outStream16,
       "outBr16": outBr16,
       "outStream17": outStream17,
       "outBr17": outBr17,
       "outStream18": outStream18,
       "outBr18": outBr18,
       "outStream19": outStream19,
       "outBr19": outBr19,
       "outStream20": outStream20,
       "outBr20": outBr20,
       "outStream21": outStream21,
       "outBr21": outBr21,
       "outStream22": outStream22,
       "outBr22": outBr22,
       "outStream23": outStream23,
       "outBr23": outBr23,
       "outStream24": outStream24,
       "outBr24": outBr24,
       "outStream25": outStream25,
       "outBr25": outBr25,
       "outStream26": outStream26,
       "outBr26": outBr26,
       "outStream27": outStream27,
       "outBr27": outBr27,
       "outStream28": outStream28,
       "outBr28": outBr28,
       "outStream29": outStream29,
       "outBr29": outBr29,
       "outStream30": outStream30,
       "outBr30": outBr30,
       "outStream31": outStream31,
       "outBr31": outBr31,
       "outStream32": outStream32,
       "outBr32": outBr32,
       "outStream33": outStream33,
       "outBr33": outBr33,
       "outStream34": outStream34,
       "outBr34": outBr34,
       "outStream35": outStream35,
       "outBr35": outBr35,
       "outStream36": outStream36,
       "outBr36": outBr36,
       "outStream37": outStream37,
       "outBr37": outBr37,
       "outStream38": outStream38,
       "outBr38": outBr38,
       "outStream39": outStream39,
       "outBr39": outBr39,
       "outStream40": outStream40,
       "outBr40": outBr40,
       "outStream41": outStream41,
       "outBr41": outBr41,
       "outStream42": outStream42,
       "outBr42": outBr42,
       "outStream43": outStream43,
       "outBr43": outBr43,
       "outStream44": outStream44,
       "outBr44": outBr44,
       "outStream45": outStream45,
       "outBr45": outBr45,
       "outStream46": outStream46,
       "outBr46": outBr46,
       "outStream47": outStream47,
       "outBr47": outBr47,
       "outStream48": outStream48,
       "outBr48": outBr48,
       "outStream49": outStream49,
       "outBr49": outBr49,
       "outStream50": outStream50,
       "outBr50": outBr50,
       "outStream51": outStream51,
       "outBr51": outBr51,
       "outStream52": outStream52,
       "outBr52": outBr52,
       "outStream53": outStream53,
       "outBr53": outBr53,
       "outStream54": outStream54,
       "outBr54": outBr54,
       "outStream55": outStream55,
       "outBr55": outBr55,
       "outStream56": outStream56,
       "outBr56": outBr56,
       "outStream57": outStream57,
       "outBr57": outBr57,
       "outStream58": outStream58,
       "outBr58": outBr58,
       "outStream59": outStream59,
       "outBr59": outBr59,
       "outStream60": outStream60,
       "outBr60": outBr60,
       "outStream61": outStream61,
       "outBr61": outBr61,
       "outStream62": outStream62,
       "outBr62": outBr62,
       "outStream63": outStream63,
       "outBr63": outBr63,
       "outStream64": outStream64,
       "outBr64": outBr64,
       "outStream65": outStream65,
       "outBr65": outBr65,
       "outStream66": outStream66,
       "outBr66": outBr66,
       "outStream67": outStream67,
       "outBr67": outBr67,
       "outStream68": outStream68,
       "outBr68": outBr68,
       "outStream69": outStream69,
       "outBr69": outBr69,
       "outStream70": outStream70,
       "outBr70": outBr70,
       "outStream71": outStream71,
       "outBr71": outBr71,
       "outStream72": outStream72,
       "outBr72": outBr72,
       "outStream73": outStream73,
       "outBr73": outBr73,
       "outStream74": outStream74,
       "outBr74": outBr74,
       "outStream75": outStream75,
       "outBr75": outBr75,
       "outStream76": outStream76,
       "outBr76": outBr76,
       "outStream77": outStream77,
       "outBr77": outBr77,
       "outStream78": outStream78,
       "outBr78": outBr78,
       "outStream79": outStream79,
       "outBr79": outBr79,
       "outStream80": outStream80,
       "outBr80": outBr80,
       "outStream81": outStream81,
       "outBr81": outBr81,
       "outStream82": outStream82,
       "outBr82": outBr82,
       "outStream83": outStream83,
       "outBr83": outBr83,
       "outStream84": outStream84,
       "outBr84": outBr84,
       "outStream85": outStream85,
       "outBr85": outBr85,
       "outStream86": outStream86,
       "outBr86": outBr86,
       "outStream87": outStream87,
       "outBr87": outBr87,
       "outStream88": outStream88,
       "outBr88": outBr88,
       "outStream89": outStream89,
       "outBr89": outBr89,
       "outStream90": outStream90,
       "outBr90": outBr90,
       "outStream91": outStream91,
       "outBr91": outBr91,
       "outStream92": outStream92,
       "outBr92": outBr92,
       "outStream93": outStream93,
       "outBr93": outBr93,
       "outStream94": outStream94,
       "outBr94": outBr94,
       "outStream95": outStream95,
       "outBr95": outBr95,
       "outStream96": outStream96,
       "outBr96": outBr96,
       "outStream97": outStream97,
       "outBr97": outBr97,
       "outStream98": outStream98,
       "outBr98": outBr98,
       "outStream99": outStream99,
       "outBr99": outBr99,
       "outStream100": outStream100,
       "outBr100": outBr100,
       "outStream101": outStream101,
       "outBr101": outBr101,
       "outStream102": outStream102,
       "outBr102": outBr102,
       "outStream103": outStream103,
       "outBr103": outBr103,
       "outStream104": outStream104,
       "outBr104": outBr104,
       "outStream105": outStream105,
       "outBr105": outBr105,
       "outStream106": outStream106,
       "outBr106": outBr106,
       "outStream107": outStream107,
       "outBr107": outBr107,
       "outStream108": outStream108,
       "outBr108": outBr108,
       "outStream109": outStream109,
       "outBr109": outBr109,
       "outStream110": outStream110,
       "outBr110": outBr110,
       "outStream111": outStream111,
       "outBr111": outBr111,
       "outStream112": outStream112,
       "outBr112": outBr112,
       "outStream113": outStream113,
       "outBr113": outBr113,
       "outStream114": outStream114,
       "outBr114": outBr114,
       "outStream115": outStream115,
       "outBr115": outBr115,
       "outStream116": outStream116,
       "outBr116": outBr116,
       "outStream117": outStream117,
       "outBr117": outBr117,
       "outStream118": outStream118,
       "outBr118": outBr118,
       "outStream119": outStream119,
       "outBr119": outBr119,
       "outStream120": outStream120,
       "outBr120": outBr120,
       "outStream121": outStream121,
       "outBr121": outBr121,
       "outStream122": outStream122,
       "outBr122": outBr122,
       "outStream123": outStream123,
       "outBr123": outBr123,
       "outStream124": outStream124,
       "outBr124": outBr124,
       "outStream125": outStream125,
       "outBr125": outBr125,
       "outStream126": outStream126,
       "outBr126": outBr126,
       "outStream127": outStream127,
       "outBr127": outBr127,
       "outStream128": outStream128,
       "outBr128": outBr128,
       "outStream129": outStream129,
       "outBr129": outBr129,
       "outStream130": outStream130,
       "outBr130": outBr130,
       "outStream131": outStream131,
       "outBr131": outBr131,
       "outStream132": outStream132,
       "outBr132": outBr132,
       "outStream133": outStream133,
       "outBr133": outBr133,
       "outStream134": outStream134,
       "outBr134": outBr134,
       "outStream135": outStream135,
       "outBr135": outBr135,
       "outStream136": outStream136,
       "outBr136": outBr136,
       "outStream137": outStream137,
       "outBr137": outBr137,
       "outStream138": outStream138,
       "outBr138": outBr138,
       "outStream139": outStream139,
       "outBr139": outBr139,
       "outStream140": outStream140,
       "outBr140": outBr140,
       "outStream141": outStream141,
       "outBr141": outBr141,
       "outStream142": outStream142,
       "outBr142": outBr142,
       "outStream143": outStream143,
       "outBr143": outBr143,
       "outStream144": outStream144,
       "outBr144": outBr144,
       "outStream145": outStream145,
       "outBr145": outBr145,
       "outStream146": outStream146,
       "outBr146": outBr146,
       "outStream147": outStream147,
       "outBr147": outBr147,
       "outStream148": outStream148,
       "outBr148": outBr148,
       "outStream149": outStream149,
       "outBr149": outBr149,
       "outStream150": outStream150,
       "outBr150": outBr150,
       "outStream151": outStream151,
       "outBr151": outBr151,
       "outStream152": outStream152,
       "outBr152": outBr152,
       "outStream153": outStream153,
       "outBr153": outBr153,
       "outStream154": outStream154,
       "outBr154": outBr154,
       "outStream155": outStream155,
       "outBr155": outBr155,
       "outStream156": outStream156,
       "outBr156": outBr156,
       "outStream157": outStream157,
       "outBr157": outBr157,
       "outStream158": outStream158,
       "outBr158": outBr158,
       "outStream159": outStream159,
       "outBr159": outBr159,
       "outStream160": outStream160,
       "outBr160": outBr160,
       "outStream161": outStream161,
       "outBr161": outBr161,
       "outStream162": outStream162,
       "outBr162": outBr162,
       "outStream163": outStream163,
       "outBr163": outBr163,
       "outStream164": outStream164,
       "outBr164": outBr164,
       "outStream165": outStream165,
       "outBr165": outBr165,
       "outStream166": outStream166,
       "outBr166": outBr166,
       "outStream167": outStream167,
       "outBr167": outBr167,
       "outStream168": outStream168,
       "outBr168": outBr168,
       "outStream169": outStream169,
       "outBr169": outBr169,
       "outStream170": outStream170,
       "outBr170": outBr170,
       "outStream171": outStream171,
       "outBr171": outBr171,
       "outStream172": outStream172,
       "outBr172": outBr172,
       "outStream173": outStream173,
       "outBr173": outBr173,
       "outStream174": outStream174,
       "outBr174": outBr174,
       "outStream175": outStream175,
       "outBr175": outBr175,
       "outStream176": outStream176,
       "outBr176": outBr176,
       "outStream177": outStream177,
       "outBr177": outBr177,
       "outStream178": outStream178,
       "outBr178": outBr178,
       "outStream179": outStream179,
       "outBr179": outBr179,
       "outStream180": outStream180,
       "outBr180": outBr180,
       "outStream181": outStream181,
       "outBr181": outBr181,
       "outStream182": outStream182,
       "outBr182": outBr182,
       "outStream183": outStream183,
       "outBr183": outBr183,
       "outStream184": outStream184,
       "outBr184": outBr184,
       "outStream185": outStream185,
       "outBr185": outBr185,
       "outStream186": outStream186,
       "outBr186": outBr186,
       "outStream187": outStream187,
       "outBr187": outBr187,
       "outStream188": outStream188,
       "outBr188": outBr188,
       "outStream189": outStream189,
       "outBr189": outBr189,
       "outStream190": outStream190,
       "outBr190": outBr190,
       "outStream191": outStream191,
       "outBr191": outBr191,
       "outStream192": outStream192,
       "outBr192": outBr192,
       "outStream193": outStream193,
       "outBr193": outBr193,
       "outStream194": outStream194,
       "outBr194": outBr194,
       "outStream195": outStream195,
       "outBr195": outBr195,
       "outStream196": outStream196,
       "outBr196": outBr196,
       "outStream197": outStream197,
       "outBr197": outBr197,
       "outStream198": outStream198,
       "outBr198": outBr198,
       "outStream199": outStream199,
       "outBr199": outBr199,
       "outStream200": outStream200,
       "outBr200": outBr200,
       "outStream201": outStream201,
       "outBr201": outBr201,
       "outStream202": outStream202,
       "outBr202": outBr202,
       "outStream203": outStream203,
       "outBr203": outBr203,
       "outStream204": outStream204,
       "outBr204": outBr204,
       "outStream205": outStream205,
       "outBr205": outBr205,
       "outStream206": outStream206,
       "outBr206": outBr206,
       "outStream207": outStream207,
       "outBr207": outBr207,
       "outStream208": outStream208,
       "outBr208": outBr208,
       "outStream209": outStream209,
       "outBr209": outBr209,
       "outStream210": outStream210,
       "outBr210": outBr210,
       "outStream211": outStream211,
       "outBr211": outBr211,
       "outStream212": outStream212,
       "outBr212": outBr212,
       "outStream213": outStream213,
       "outBr213": outBr213,
       "outStream214": outStream214,
       "outBr214": outBr214,
       "outStream215": outStream215,
       "outBr215": outBr215,
       "outStream216": outStream216,
       "outBr216": outBr216,
       "outStream217": outStream217,
       "outBr217": outBr217,
       "outStream218": outStream218,
       "outBr218": outBr218,
       "outStream219": outStream219,
       "outBr219": outBr219,
       "outStream220": outStream220,
       "outBr220": outBr220,
       "outStream221": outStream221,
       "outBr221": outBr221,
       "outStream222": outStream222,
       "outBr222": outBr222,
       "outStream223": outStream223,
       "outBr223": outBr223,
       "outStream224": outStream224,
       "outBr224": outBr224,
       "outStream225": outStream225,
       "outBr225": outBr225,
       "outStream226": outStream226,
       "outBr226": outBr226,
       "outStream227": outStream227,
       "outBr227": outBr227,
       "outStream228": outStream228,
       "outBr228": outBr228,
       "outStream229": outStream229,
       "outBr229": outBr229,
       "outStream230": outStream230,
       "outBr230": outBr230,
       "outStream231": outStream231,
       "outBr231": outBr231,
       "outStream232": outStream232,
       "outBr232": outBr232,
       "outStream233": outStream233,
       "outBr233": outBr233,
       "outStream234": outStream234,
       "outBr234": outBr234,
       "outStream235": outStream235,
       "outBr235": outBr235,
       "outStream236": outStream236,
       "outBr236": outBr236,
       "outStream237": outStream237,
       "outBr237": outBr237,
       "outStream238": outStream238,
       "outBr238": outBr238,
       "outStream239": outStream239,
       "outBr239": outBr239,
       "outStream240": outStream240,
       "outBr240": outBr240,
       "outStream241": outStream241,
       "outBr241": outBr241,
       "outStream242": outStream242,
       "outBr242": outBr242,
       "outStream243": outStream243,
       "outBr243": outBr243,
       "outStream244": outStream244,
       "outBr244": outBr244,
       "outStream245": outStream245,
       "outBr245": outBr245,
       "outStream246": outStream246,
       "outBr246": outBr246,
       "outStream247": outStream247,
       "outBr247": outBr247,
       "outStream248": outStream248,
       "outBr248": outBr248,
       "outStream249": outStream249,
       "outBr249": outBr249,
       "outStream250": outStream250,
       "outBr250": outBr250,
       "outStream251": outStream251,
       "outBr251": outBr251,
       "outStream252": outStream252,
       "outBr252": outBr252,
       "outStream253": outStream253,
       "outBr253": outBr253,
       "outStream254": outStream254,
       "outBr254": outBr254,
       "outStream255": outStream255,
       "outBr255": outBr255,
       "outStream256": outStream256,
       "outBr256": outBr256,
       "outStream257": outStream257,
       "outBr257": outBr257,
       "outStream258": outStream258,
       "outBr258": outBr258,
       "outStream259": outStream259,
       "outBr259": outBr259,
       "outStream260": outStream260,
       "outBr260": outBr260,
       "outStream261": outStream261,
       "outBr261": outBr261,
       "outStream262": outStream262,
       "outBr262": outBr262,
       "outStream263": outStream263,
       "outBr263": outBr263,
       "outStream264": outStream264,
       "outBr264": outBr264,
       "outStream265": outStream265,
       "outBr265": outBr265,
       "outStream266": outStream266,
       "outBr266": outBr266,
       "outStream267": outStream267,
       "outBr267": outBr267,
       "outStream268": outStream268,
       "outBr268": outBr268,
       "outStream269": outStream269,
       "outBr269": outBr269,
       "outStream270": outStream270,
       "outBr270": outBr270,
       "outStream271": outStream271,
       "outBr271": outBr271,
       "outStream272": outStream272,
       "outBr272": outBr272,
       "outStream273": outStream273,
       "outBr273": outBr273,
       "outStream274": outStream274,
       "outBr274": outBr274,
       "outStream275": outStream275,
       "outBr275": outBr275,
       "outStream276": outStream276,
       "outBr276": outBr276,
       "outStream277": outStream277,
       "outBr277": outBr277,
       "outStream278": outStream278,
       "outBr278": outBr278,
       "outStream279": outStream279,
       "outBr279": outBr279,
       "outStream280": outStream280,
       "outBr280": outBr280,
       "outStream281": outStream281,
       "outBr281": outBr281,
       "outStream282": outStream282,
       "outBr282": outBr282,
       "outStream283": outStream283,
       "outBr283": outBr283,
       "outStream284": outStream284,
       "outBr284": outBr284,
       "outStream285": outStream285,
       "outBr285": outBr285,
       "outStream286": outStream286,
       "outBr286": outBr286,
       "outStream287": outStream287,
       "outBr287": outBr287,
       "outStream288": outStream288,
       "outBr288": outBr288,
       "outStream289": outStream289,
       "outBr289": outBr289,
       "outStream290": outStream290,
       "outBr290": outBr290,
       "outStream291": outStream291,
       "outBr291": outBr291,
       "outStream292": outStream292,
       "outBr292": outBr292,
       "outStream293": outStream293,
       "outBr293": outBr293,
       "outStream294": outStream294,
       "outBr294": outBr294,
       "outStream295": outStream295,
       "outBr295": outBr295,
       "outStream296": outStream296,
       "outBr296": outBr296,
       "outStream297": outStream297,
       "outBr297": outBr297,
       "outStream298": outStream298,
       "outBr298": outBr298,
       "outStream299": outStream299,
       "outBr299": outBr299,
       "outStream300": outStream300,
       "outBr300": outBr300,
       "outStream301": outStream301,
       "outBr301": outBr301,
       "outStream302": outStream302,
       "outBr302": outBr302,
       "outStream303": outStream303,
       "outBr303": outBr303,
       "outStream304": outStream304,
       "outBr304": outBr304,
       "outStream305": outStream305,
       "outBr305": outBr305,
       "outStream306": outStream306,
       "outBr306": outBr306,
       "outStream307": outStream307,
       "outBr307": outBr307,
       "outStream308": outStream308,
       "outBr308": outBr308,
       "outStream309": outStream309,
       "outBr309": outBr309,
       "outStream310": outStream310,
       "outBr310": outBr310,
       "outStream311": outStream311,
       "outBr311": outBr311,
       "outStream312": outStream312,
       "outBr312": outBr312,
       "outStream313": outStream313,
       "outBr313": outBr313,
       "outStream314": outStream314,
       "outBr314": outBr314,
       "outStream315": outStream315,
       "outBr315": outBr315,
       "outStream316": outStream316,
       "outBr316": outBr316,
       "outStream317": outStream317,
       "outBr317": outBr317,
       "outStream318": outStream318,
       "outBr318": outBr318,
       "outStream319": outStream319,
       "outBr319": outBr319,
       "outStream320": outStream320,
       "outBr320": outBr320,
       "commStatus": commStatus,
       "inTotbr": inTotbr,
       "outTotbr": outTotbr,
       "cpuLoad": cpuLoad,
       "intTemp": intTemp,
       "volt": volt,
       "sti440alarms": sti440alarms,
       "alarmStlink": alarmStlink,
       "alarmCtrlink": alarmCtrlink,
       "alarmBrovf": alarmBrovf,
       "alarmUnlock1": alarmUnlock1,
       "alarmUnlock2": alarmUnlock2,
       "alarmUnlock3": alarmUnlock3,
       "alarmUnlock4": alarmUnlock4,
       "alarmUnlock5": alarmUnlock5,
       "alarmUnlock6": alarmUnlock6,
       "alarmUnlock7": alarmUnlock7,
       "alarmUnlock8": alarmUnlock8,
       "alarmUnlock9": alarmUnlock9,
       "alarmPowerr": alarmPowerr,
       "alarmTemperr": alarmTemperr,
       "alarmIbrer": alarmIbrer,
       "sti440notifications": sti440notifications,
       "notifyStlink": notifyStlink,
       "notifyCtrlink": notifyCtrlink,
       "notifyBrovf": notifyBrovf,
       "notifyUnlock1": notifyUnlock1,
       "notifyUnlock2": notifyUnlock2,
       "notifyUnlock3": notifyUnlock3,
       "notifyUnlock4": notifyUnlock4,
       "notifyUnlock5": notifyUnlock5,
       "notifyUnlock6": notifyUnlock6,
       "notifyUnlock7": notifyUnlock7,
       "notifyUnlock8": notifyUnlock8,
       "notifyUnlock9": notifyUnlock9,
       "notifyPowerr": notifyPowerr,
       "notifyTemperr": notifyTemperr,
       "notifyIbrer": notifyIbrer,
       "sti440Info": sti440Info,
       "infVersion": infVersion,
       "infSerNum": infSerNum,
       "terrasti440MIBConformance": terrasti440MIBConformance,
       "terrasti440MIBGroups": terrasti440MIBGroups,
       "sti440TerraMibAllObjects": sti440TerraMibAllObjects,
       "sti440TerraMibAllNotifications": sti440TerraMibAllNotifications}
)
