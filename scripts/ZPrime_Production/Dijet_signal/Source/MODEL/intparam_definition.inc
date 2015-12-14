ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

C     Parameters that should not be recomputed event by event.
C     
      IF(READLHA) THEN

        G = 2 * DSQRT(AS*PI)  ! for the first init

        MDL_COS__CABI = COS(MDL_CABI)

        MDL_CKM11 = MDL_COS__CABI

        MDL_SIN__CABI = SIN(MDL_CABI)

        MDL_CKM12 = MDL_SIN__CABI

        MDL_CKM13 = 0.000000D+00

        MDL_CKM21 = -MDL_SIN__CABI

        MDL_CKM22 = MDL_COS__CABI

        MDL_CKM23 = 0.000000D+00

        MDL_CKM31 = 0.000000D+00

        MDL_CKM32 = 0.000000D+00

        MDL_CKM33 = 1.000000D+00

        MDL_GZ__EXP__2 = MDL_GZ**2

        MDL_MT__EXP__2 = MDL_MT**2

        MDL_MZPH__EXP__2 = MDL_MZPH**2

        MDL_WZPH = (MDL_GZ__EXP__2*MDL_MZPH*(5.000000D+00+SQRT(1.000000
     $   D+00-(4.000000D+00*MDL_MT__EXP__2)/MDL_MZPH__EXP__2)))
     $   /(1.440000D+02*PI)

        MDL_WZPL = (5.000000D+00*MDL_GZ__EXP__2*MDL_MZPL)/(1.440000D
     $   +02*PI)

        MDL_MZ__EXP__2 = MDL_MZ**2

        MDL_MZ__EXP__4 = MDL_MZ**4

        MDL_SQRT__2 = SQRT(2.000000D+00)

        MDL_MH__EXP__2 = MDL_MH**2

        MDL_COMPLEXI = (0.000000D+00,1.000000D+00)

        MDL_CONJG__CKM11 = CONJG(DCMPLX(MDL_CKM11))

        MDL_CONJG__CKM12 = CONJG(DCMPLX(MDL_CKM12))

        MDL_CONJG__CKM13 = CONJG(DCMPLX(MDL_CKM13))

        MDL_CONJG__CKM21 = CONJG(DCMPLX(MDL_CKM21))

        MDL_CONJG__CKM22 = CONJG(DCMPLX(MDL_CKM22))

        MDL_CONJG__CKM23 = CONJG(DCMPLX(MDL_CKM23))

        MDL_CONJG__CKM31 = CONJG(DCMPLX(MDL_CKM31))

        MDL_CONJG__CKM32 = CONJG(DCMPLX(MDL_CKM32))

        MDL_CONJG__CKM33 = CONJG(DCMPLX(MDL_CKM33))

        MDL_AEW = 1.000000D+00/AEWM1

        MDL_MW = SQRT(MDL_MZ__EXP__2/2.000000D+00+SQRT(MDL_MZ__EXP__4
     $   /4.000000D+00-(MDL_AEW*PI*MDL_MZ__EXP__2)/(MDL_GF*MDL_SQRT__2
     $   )))

        MDL_SQRT__AEW = SQRT(MDL_AEW)

        MDL_EE = 2.000000D+00*MDL_SQRT__AEW*SQRT(PI)

        MDL_MW__EXP__2 = MDL_MW**2

        MDL_SW2 = 1.000000D+00-MDL_MW__EXP__2/MDL_MZ__EXP__2

        MDL_CW = SQRT(1.000000D+00-MDL_SW2)

        MDL_SQRT__SW2 = SQRT(MDL_SW2)

        MDL_SW = MDL_SQRT__SW2

        MDL_G1 = MDL_EE/MDL_CW

        MDL_GW = MDL_EE/MDL_SW

        MDL_V = (2.000000D+00*MDL_MW*MDL_SW)/MDL_EE

        MDL_V__EXP__2 = MDL_V**2

        MDL_LAM = MDL_MH__EXP__2/(2.000000D+00*MDL_V__EXP__2)

        MDL_YB = (MDL_YMB*MDL_SQRT__2)/MDL_V

        MDL_YC = (MDL_YMC*MDL_SQRT__2)/MDL_V

        MDL_YDO = (MDL_YMDO*MDL_SQRT__2)/MDL_V

        MDL_YE = (MDL_YME*MDL_SQRT__2)/MDL_V

        MDL_YM = (MDL_YMM*MDL_SQRT__2)/MDL_V

        MDL_YS = (MDL_YMS*MDL_SQRT__2)/MDL_V

        MDL_YT = (MDL_YMT*MDL_SQRT__2)/MDL_V

        MDL_YTAU = (MDL_YMTAU*MDL_SQRT__2)/MDL_V

        MDL_YUP = (MDL_YMUP*MDL_SQRT__2)/MDL_V

        MDL_MUH = SQRT(MDL_LAM*MDL_V__EXP__2)

        MDL_GW__EXP__2 = MDL_GW**2

        MDL_CW__EXP__2 = MDL_CW**2

        MDL_EE__EXP__2 = MDL_EE**2

        MDL_SW__EXP__2 = MDL_SW**2

      ENDIF
C     
C     Parameters that should be recomputed at an event by even basis.
C     
      AS = G**2/4/PI

      MDL_SQRT__AS = SQRT(AS)

      MDL_G__EXP__2 = G**2

C     
C     Definition of the EW coupling used in the write out of aqed
C     
      GAL(1) = 3.5449077018110318 / DSQRT(AEWM1)
      GAL(2) = 1D0

