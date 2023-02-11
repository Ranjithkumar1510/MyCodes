module params

    implicit None

    integer,parameter :: ikd = selected_int_kind(8)
    integer,parameter :: rkd = selected_real_kind(8,8)

    ! grid size in x and y direction and iteration
    integer (kind=ikd),parameter ::Nx=101,Ny=101, iter= 1500 
    integer :: i,j,m
    real :: dx,dy

    ! Needed Matrix 
    real(kind=rkd) ::T(Ny,Nx),T_old(Ny,Nx),x(Ny,Nx),y(Ny,Nx),z(Ny,Nx)
    real(kind=rkd) ::S_no(iter),conv(iter)
    
    ! Boundary Condition
    real(kind=rkd),parameter ::Lx=3.0,Ly=3.0,Tw=500,Te=250,Tn=300,Ts=100

end module params

