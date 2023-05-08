program Predictor
IMPLICIT NONE
REAL::a,b,h,y_0,f_prime
INTEGER::N,i
character(len=*), parameter :: OUT_FILE = 'data.txt' ! Output file.
character(len=*), parameter :: PLT_FILE = 'plot.plt' ! Gnuplot file.
real, allocatable :: x(:), y(:)
a=0  !Set intervals
b=4
h=0.1 !step size
y_0=0  ! Initial value
N=INT((b-a)/h) !Number of steps
allocate(x(N),y(N))
x(1) = a     !starting of the xgrid 
y(1) = y_0   !starting of y grid
x(2) = a+h   ! x_1=x_0+h
y(2) = y_0+h*f_prime(x(1),y(1)) !Euler Method to determine the second y point

do i=2,N
    y(i+1) = y(i) + (h/2)*(3*f_prime(x(i),y(i))-f_prime(x(i-1),y(i-1)))  ! Adam Bashforth  2 step method  Explicit Method
    x(i+1) = x(i) + h
    y(i+1) = y(i) + (h/2)*(f_prime(x(i+1),y(i+1))+f_prime(x(i),y(i)))    ! Adam Moulton 2 step method   Implicit Method

end do

open (1,action='write', file=OUT_FILE,status='replace')
    do i = 1, N
        write (1, *) x(i), y(i)
        x(i)=x(i)+h
    end do
 close (1)
 
call execute_command_line('gnuplot -p ' // PLT_FILE)
end program Predictor

REAL function f_prime(x1,y1)        !dy/dx
REAL::x1,y1
  f_prime=-0.5*EXP(x1/2)*SIN(5*x1)+5*EXP(x1/2)*COS(5*x1)+y1
return
end function
