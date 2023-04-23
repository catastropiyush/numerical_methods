!read a PDB file and coordinates and determine Center of Mass of a protein
!curently this code determines only the dot product
! need to be updated for all different PDB files and determine COM

program filereader
implicit none
character(len=10),allocatable:: a(:),b(:),c(:),d_1(n),last(:)
real,allocatable ::p(:),q(:),x(:),y(:),z(:),k(:),l(:),d(:),m(:)
integer::N,i,num
REAL ::H_m,C_m,N_m,O_m,F_m,P_m,S_m,Cl_m 
real :: moda=0,modb=0,dot_prod=0,var
real :: veca(3),vecb(3)

!atomic masses
H_m  =   0.12
C_m  =   0.65
N_m  =   0.155
O_m  =   0.152
F_m  =   0.147
P_m  =   0.18
S_m  =   0.18
Cl_m =   0.175
N = 0
OPEN (1, file ='protein.pdb')
DO
	READ (1,*, END=10)
	N = N + 1
END DO
10 CLOSE (1)
!print*,N   
!           c   n    c    c    c     n   n    n    n    n    n    n    n
allocate (a(N),p(N),b(N),c(N),d(n),q(N),x(N),y(N),z(N),k(N),l(N),d(N),last(n))  !allocate the arrays from the text file

open (unit = 1, file ='protein.pdb', status ='old')
do i = 1,N
 	read (1,*) a(i),p(i),b(i),c(i),d(i),q(i),x(i),y(i),z(i),k(i),l(i),last(i)
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
do i=1,N
   d(i)=SQRT(x(i)**2+y(i)**2+z(i)**2)
end do   

!mass assigner
do i=1,N
    if(last(i)=='C') then
      m(i) = 12.011
    elseif (last(i)=='H') then
      m(i) = 1.00784
    elseif (last(i)=='N') then
      m(i) = 14.0067 
    end if
end do



do i =1,N
 	write(*,*) m(i)
end do

do i =1,N
 	write(*,*) d(i)
end do 



end program filereader
