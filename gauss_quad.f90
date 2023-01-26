!FORTRAN gauss code
program gaussquad
  implicit none
  ! declare variables
  integer            :: i,N
  real               :: f,integral,a,b
  real, dimension(1) :: x_1,w_1
  real, dimension(2) :: x_2,w_2
  real, dimension(3) :: x_3,w_3
  real, dimension(4) :: x_4,w_4
  
  x_1=(/0/)                         ; w_1 = (/2/)
  x_2=(/-0.577,0.577/)              ; w_2 = (/1.000,1.000/)
  x_3=(/0.000,-0.744,0.744/)        ; w_3 = (/0.888,0.555,0.555/)  
  x_4=(/-0.339,0.339,-0.861,0.861/) ; w_4 = (/0.652,0.652,0.347,0.347/)
  
  a = 0.0
  b = 3.0
  N = 4
  do i = 1,N
     integral = integral+ w_4(i)*(b-a)*0.5*(f((0.5*((b-a)*x_4(i)+(b-a)))))
  end do
 write (6,9) 'I=',integral
9 FORMAT(1a3,2f10.6)
end program gaussquad

REAL function f(x1)
REAL::x1
  f=x1*EXP(x1)
return
end function
