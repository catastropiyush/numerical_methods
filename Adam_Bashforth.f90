program Predictor
IMPLICIT NONE
REAL::a,b,h,y_0,f_prime
INTEGER::N,i
real, allocatable :: x(:), y(:)
a=0
b=4
h=0.1
y_0=0
N=INT((b-a)/h) !Number of steps
allocate(x(N),y(N))
x(1) = a 
y(1) = y_0
x(2) = a+h       !Adam Bashforth 2 Step Method
y(2) = y_0+h*f_prime(x(1),y(1))
do i=2,N
    y(i+1) = y(i) + (h/2)*(3*f_prime(x(i),y(i))-f_prime(x(i-1),y(i-1)))
    x(i+1) = x(i) + h
    y(i+1) = y(i) + (h/2)*(f_prime(x(i+1),y(i+1))+f_prime(x(i),y(i)))

end do
do i = 1,N
    write(*,*) x(i),y(i)
    x(i)=x(i)+h
  end do
end program Predictor

REAL function f_prime(x1,y1)
REAL::x1,y1
  f_prime=-0.5*EXP(x1/2)*SIN(5*x1)+5*EXP(x1/2)*COS(5*x1)+y1
return
end function

