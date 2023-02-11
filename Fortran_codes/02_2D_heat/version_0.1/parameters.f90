module params

    implicit None

    integer,parameter :: ikd = selected_int_kind(8)
    integer,parameter :: rkd = selected_real_kind(8,8)

    ! grid size in x and y direction and iteration
    ! Number of Node should be +1
    integer (kind=ikd),parameter ::Nx=5,Ny=5, iter=100
    integer :: i,j,m
    
    ! Needed Matrix 
    real(kind=rkd) ::T(Ny,Nx),x(Ny,Nx),y(Ny,Nx),z(Ny,Nx)
    
    ! Boundary Condition
    real(kind=rkd),parameter :: Tw=500,Te=100,Tn=100,Ts=100

end module params

