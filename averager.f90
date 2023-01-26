program averager
implicit none 
real(kind=8),allocatable ::a(:),b(:),c(:),aver(:)
character,allocatable :: d(:)
integer::N,i,num

N = 0
OPEN (1, file ='data.txt')
DO
    READ (1,*, END=10)
    N = N + 1
END DO
10 CLOSE (1)

allocate (a(N),b(N),c(N),d(N))  !allocate the arrays from the text file
!Reading the coefficients from the file

open (unit = 1, file ='data.txt', status ='old')
do i = 1,N 
     read (1,*) a(i),b(i),c(i),d(i)
end do
close (1)

do i = 1,N 
 print*,(a(i)+b(i)+c(i))/3
end do
end program averager
