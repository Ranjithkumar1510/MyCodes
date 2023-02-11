program heat    
    
    use params

    implicit None
    
    ! Initial Values
    T = 250 

    ! assigning the Boundary value
    do i=1,Nx
        T(1,i) = Ts
    end do
    
    do i=1,Nx
        T(Ny,i) = Tn
    end do
   
    do j=1,Ny
        T(j,1) = Tw
    end do

    do j=1,Ny
        T(j,Nx) = Te
    end do
    
    call mesh()

    call scheme()

    call csv()

end program heat
