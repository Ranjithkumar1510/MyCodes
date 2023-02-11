subroutine csv()
     
    use params

    ! writing the formate
    25 format(1x,*(g0,","))

    ! Write the data into the file
    open(unit=1,file="data.csv")
    write(unit=1,fmt=*) "x,y,z,T"
    do j=1,Ny
        do i=1,Nx 
            write(unit=1,fmt=25) x(j,i),y(j,i),z(j,i),T(j,i)
        end do
    end do

    close(unit=1)

    open(unit=2,file="data_2.csv")
    do i=1,iter
        write(unit=2,fmt=25) S_no(i),conv(i)
    end do

    close(unit=2)
end subroutine csv
