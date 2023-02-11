subroutine step()

    use params 

    ! Initial Values for grid
    x = 0
    y = 0
    z = 0

    ! computing section of co-ordinates
    !do j=2,Ny
    !    do i=2,Nx
    !        x(j,i) = i-1 
    !        y(j,i) = j-1 
    !end do
    do j=1,Ny
        do i=2,Nx
            x(j,i) = i-1
        end do
    end do

    do j=2,Ny
        do i=1,Nx
            y(j,i) = j-1
        end do
    end do


    ! computing Temprature
    do m=1,iter
        do j=2,(Ny-1)
            do i=2,(Nx-1)
                T(j,i)=(T((j+1),i)+T((j-1),i)+T(j,(i+1))+T(j,(i-1)))/4
            end do
        end do
    end do

end subroutine step
