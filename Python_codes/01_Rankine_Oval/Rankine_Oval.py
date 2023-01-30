#!/bin/python3

# Rankine -fULL Oval

import numpy as np
import matplotlib.pyplot as plt

# Quadrilateral mesh grid
x,y=np.meshgrid(np.linspace(0,1,200),np.linspace(0,1,200))

# Number of grid ponits in x axis
Nx=len(x)

# Number of grid ponits in y axis
Ny=len(y)

# x directional velocity commponenit array
u=np.zeros([Nx,Ny])

# y directional velocity component array
v=np.zeros([Nx,Ny])

# Free stream velocity
V_inf=10

# Source and sink strength
Lamda=100

# x location of the source
xc1=0.48

# x location of the sink
xc2=0.52

# The distace between the source/sink to the center
b=(xc2-xc1)/2

# location of the center
xc=0.5
yc=0.5

# computing section
# polar coordinate values from the center

# radius
r=np.sqrt((x-xc)**2+(y-yc)**2)
# Angle of the each postion w.r.t center
theta=np.arctan2(y-yc,x-xc)
# Angle of the each postion w.r.t source center
t1=np.arctan2(y-yc,x-xc1)
# Angle of the each postion w.r.t sink center
t2=np.arctan2(y-yc,x-xc2)

# Calculating Stream function 
psi=V_inf*r*np.sin(theta)+(Lamda*(t1-t2)/2/np.pi)


# Numerical computing section
# Calculating velocity components 
for i in range(0,Nx-1):
    for j in range(0,Ny-1):
        u[j,i]=(psi[j+1,i]-psi[j,i])/(y[j+1,i]-y[j,i])
        v[j,i]=-(psi[j,i+1]-psi[j,i])/(x[j,i+1]-x[j,i])

# calculating last grid ponit velocity components
for i in range(0,Nx):
    u[i,Nx-1]=2*u[i,Nx-2]-u[i,Nx-3]
    u[Nx-1,i]=2*u[Nx-2,i]-u[Nx-3,i]
    
    v[i,Nx-1]=2*v[i,Nx-2]-v[i,Nx-3]
    v[Nx-1,i]=2*v[Nx-2,i]-v[Nx-3,i]
    
# Analytical solution 

# Offceting the Coordination
X=x-xc
Y=y-yc

# x component velocity
a1=(X+b)/((X+b)**2+Y**2)
a2=(X-b)/((X-b)**2+Y**2)
ana_u=V_inf+(Lamda*(a1-a2)/2/np.pi)

# y component velocity
a1=Y/((X+b)**2+Y**2)
a2=Y/((X-b)**2+Y**2)
ana_v=Lamda*(a1-a2)/2/np.pi

# plotting section

plt.figure()
# plotting the numerical solution
plt.streamplot(x,y,u,v)
# plotting the analytical solution
plt.streamplot(x,y,ana_u,ana_v)
plt.title("Rankine Oval")
plt.savefig("Result.png",dpi=150)
plt.show()

