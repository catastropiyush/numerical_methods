!This code is used to calculate the first order derivative of a function
!modularize this code

program deriv
  implicit none
  ! declare variables
  integer             :: i,upper,lower,N
  real                :: step   
  !real, dimension(N) :: x, y, dy 
  real, allocatable :: x(:), y(:),dy(:),dy2(:),diff(:)
  print*,'Enter value of upper'
  read*, upper
  print*,'Enter value of lower'
  read*, lower
  print*,'Enter step size'
  read*,step
  N=(upper-lower)/step
  allocate (x(N),y(N),dy(N),dy2(N),diff(N))    !allocate array size
  !assign data
  do i  =1,N
   x(i) = lower+i*step     !fill grid spaces
  end do
  !x = (/ 0., 0.1, 0.2, 0.3, 0.5, 0.6, 0.8, 0.9, 1. /)    !Array constructor
  do i  =1,N
   y(i) = EXP(-(x(i)**2))
  end do
  ! compute derivatives
  do i = 2, N-1
     dy(i) = (y(i+1) - y(i-1)) / (x(i+1) - x(i-1))  !derivative of function
  end do
  !Use linear extrapolation to determine derivatives at end points
  dy(1) = dy(2) + (dy(3)-dy(2))/(x(3)-x(2))*(x(1)-x(2))
  dy(N) = dy(N-1) + (dy(N-1)-dy(N-2))/(x(N-1)-x(N-2))*(x(N)-x(N-1))
  do i = 1, N
    diff(i)=dy(i)-((-2*x(i))*EXP(-(x(i)**2)))
  end do
 !print the results 
 !write (*,'(4a10)') 'x', 'y=f(x)', 'dy/dx','d2y/dx2'
 write (*,'(5a10)') 'x', 'y=f(x)', 'dy/dx','diff','d2y/dx2'
  do i = 1, N
    write(*,'(5f10.2)') x(i), y(i), dy(i),diff(i),dy2(i)
  end do
end program deriv
