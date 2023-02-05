program Area_Mach

    implicit None

    ! defining variables
    ! M is Mach number
    ! Aris Area ratio
    ! g is specific heat ratio

    ! real :: M,Ar,g,a,b,res,x,y,z
    real*16 :: M,Ar,g,a,b,res,x,y,z

    ! input Area_ratio
    g = 1.4
    Ar = 61.21
    
    ! inital value for bi_section method
    a=1
    b=10

    M=(a+b)/2
    
    x=2/(g+1)
    y=(g-1)/(g+1)
    z=1/(2*y)

    res=(((x+(y*M**2))**z)/M)-Ar
    print*,M,res
    ! Begining the loop

    do while (abs(res) >= (1e-6))
        if (res>0) then
            b=M
        else
            a=M
        end if

        M=(a+b)/2
        x=2/(g+1)
        y=(g-1)/(g+1)
        z=1/(2*y)
    
        res=(((x+(y*M**2))**z)/M)-Ar
    end do
    print*, M 
end program Area_Mach

