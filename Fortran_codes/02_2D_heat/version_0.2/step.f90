subroutine scheme()

    use params 

    ! computing Temprature
    do m=1,iter
        T_old = T
        do j=2,(Ny-1)
            do i=2,(Nx-1)
                T(j,i)=(T((j+1),i)+T((j-1),i)+T(j,(i+1))+T(j,(i-1)))/4
            end do
        end do
        S_no(m) = m
        conv(m) = ABS(MAXVAL(T_old-T))
    end do

end subroutine scheme

subroutine mesh()
    
    use params 

    ! small distance calculation
    dx = Lx/(Nx-1)
    dy = Ly/(Ny-1)

    ! Initial Values for grid
    x = 0
    y = 0
    z = 0

    ! computing section of co-ordinates
    do j=1,Ny
        do i=2,Nx
            x(j,i) = x(j,i-1)+dx
        end do
    end do

    do j=2,Ny
        do i=1,Nx
            y(j,i) = y(j-1,i)+dy
        end do
    end do
end subroutine mesh
