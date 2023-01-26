program filereader
implicit none
character(len=10),allocatable:: a(:),b(:),c(:)
real,allocatable ::p(:),q(:),x(:),y(:),z(:),k(:),l(:)
integer::N,i,num
real :: moda=0,modb=0,dot_prod=0,var
real :: veca(3),vecb(3)
N = 0
OPEN (1, file ='protein.pdb')
DO
	READ (1,*, END=10)
	N = N + 1
END DO
10 CLOSE (1)
!print*,N   
allocate (a(N),p(N),b(N),c(N),q(N),x(N),y(N),z(N),k(N),l(N))  !allocate the arrays from the text file

open (unit = 1, file ='protein.pdb', status ='old')
do i = 1,N
 	read (1,*) a(i),p(i),b(i),c(i),q(i),x(i),y(i),z(i),k(i),l(i)
end do
close (1)

!File contents 
!do i =1,N
 !	write(*,*) x(i),y(i),z(i)
!end do

veca=(/x(1)-x(N),y(1)-y(N),z(1)-z(N)/)
vecb=(/0,0,1/)                
do i =1,3
 	write(*,*) veca(i)
end do
do i=1,3
  dot_prod=dot_prod+veca(i)*vecb(i)
  moda=moda+veca(i)**2
  modb=modb+vecb(i)**2
end do  

write(*,*) SQRT(moda),SQRT(modb),dot_prod
var = (dot_prod)/(SQRT(moda)*SQRT(modb))
write(*,*) var
write(*,*) ACOS(var)

end program filereader
