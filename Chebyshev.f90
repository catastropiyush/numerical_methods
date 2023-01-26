PROGRAM CHEBYSHEV
IMPLICIT NONE
REAL           :: A,B,tol,DX,X0,X1,DF,F,D2F
INTEGER        :: I
 
      tol = 1.0E-06
      A  = -3.0 ; B  = 0.0
      DX = B-A
      X0 = (A+B)/2.0 !midpoint
      I = 0
  DO 21 WHILE (ABS(DX).GT.tol)
        X1 = X0 - F(X0)/DF(X0)-0.5*D2F(X0)*((F(X0))**2/DF(X0)**3)
        DX = X1 - X0
        X0 = X1
        I = I + 1  !step
  21 END DO
      WRITE (6,9) I,X0,DX
      STOP
  9 FORMAT (I4,2F16.8)
END PROGRAM CHEBYSHEV

FUNCTION F(X)
  F = X**3-3*X+1
RETURN
END

FUNCTION DF(X)
  DF = 3*X**2-3
RETURN
END

FUNCTION D2F(X)
  D2F = 6*X
RETURN
END
