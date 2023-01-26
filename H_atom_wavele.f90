module vaseline
    implicit none
contains
    real function wavelu(n1,n2)
        real, intent(in) :: n1,n2
        real,parameter :: uR_h=912E-10 !1/R= 912 Angstrom
        wavelu = (1/((1/(n1**2))-(1/(n2**2))))*uR_h
    end function 
end module vaseline

program bohrmodel
   #Piyush 21msphcp02
   use vaseline
   real :: n1,n2
   n1 =1 ; n2 =2
   a = wavelu(n1,n2)
   print*,"Energy levels"
   print*,"n1=",int(n1),"n2=",int(n2)
   print*,"Wavelength =",a,"m"
   print*,"Frequency  =",(3E+8/a),"Hz"
end program bohrmodel
