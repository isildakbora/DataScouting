ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      DOUBLE COMPLEX FUNCTION COND(CONDITION,TRUECASE,FALSECASE)
      IMPLICIT NONE
      DOUBLE COMPLEX CONDITION,TRUECASE,FALSECASE
      IF(CONDITION.EQ.(0.0D0,0.0D0)) THEN
        COND=TRUECASE
      ELSE
        COND=FALSECASE
      ENDIF
      END

      DOUBLE COMPLEX FUNCTION CONDIF(CONDITION,TRUECASE,FALSECASE)
      IMPLICIT NONE
      LOGICAL CONDITION
      DOUBLE COMPLEX TRUECASE,FALSECASE
      IF(CONDITION) THEN
        CONDIF=TRUECASE
      ELSE
        CONDIF=FALSECASE
      ENDIF
      END

      DOUBLE COMPLEX FUNCTION REGLOG(ARG)
      IMPLICIT NONE
      DOUBLE COMPLEX ARG
      IF(ARG.EQ.(0.0D0,0.0D0)) THEN
        REGLOG=(0.0D0,0.0D0)
      ELSE
        REGLOG=LOG(ARG)
      ENDIF
      END

      DOUBLE COMPLEX FUNCTION ARG(COMNUM)
      IMPLICIT NONE
      DOUBLE COMPLEX COMNUM
      DOUBLE COMPLEX IIM
      IIM = (0.0D0,1.0D0)
      IF(COMNUM.EQ.(0.0D0,0.0D0)) THEN
        ARG=(0.0D0,0.0D0)
      ELSE
        ARG=LOG(COMNUM/ABS(COMNUM))/IIM
      ENDIF
      END
