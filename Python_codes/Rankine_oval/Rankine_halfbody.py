# Rankine -semioval

import numpy as np
import matplotlib.pyplot as plt

''' Creating a mesh grid'''

x,y=np.meshgrid(np.linspace(0,1,200),np.linspace(0,1,200))
Nx=len(x)
Ny=len(y)

u=np.zeros([Nx,Ny])
v=np.zeros([Nx,Ny])
''' Initial Conditions velocity and Source strength'''

V_inf=15
Lamda=10

''' Center of the Source and sink'''

xc1=0.8

xc=0.5
yc=0.5

''' Calculating the radius and theta '''
# From the Center
r=np.sqrt((x-xc)**2+(y-yc)**2)
theta=np.arctan2(y-yc,x-xc)
t1=np.arctan2(y-yc,x-xc1)

'''Computing stream function'''
psi=V_inf*r*np.sin(theta)+(Lamda*theta/2/np.pi)

''' Numerical velocity Calculation '''
for i in range(0,Nx-1):
    for j in range(0,Ny-1):
        u[j,i]=(psi[j+1,i]-psi[j,i])/(y[j+1,i]-y[j,i])
        v[j,i]=-(psi[j,i+1]-psi[j,i])/(x[j,i+1]-x[j,i])

for i in range(0,Nx):
    u[i,Nx-1]=2*u[i,Nx-2]-u[i,Nx-3]
    u[Nx-1,i]=2*u[Nx-2,i]-u[Nx-3,i]
    
    v[i,Nx-1]=2*v[i,Nx-2]-v[i,Nx-3]
    v[Nx-1,i]=2*v[Nx-2,i]-v[Nx-3,i]
    
plt.figure(1)
plt.streamplot(x,y,u,v)
plt.title("Rankine half oval Numerical solution")
plt.show()

''' analythical solution '''
vr=V_inf*np.cos(theta)+(Lamda/2/np.pi/r)
vt=-V_inf*np.sin(theta)
ana_u=vr*np.cos(theta)-vt*np.sin(theta)
ana_v=vr*np.sin(theta)+vt*np.cos(theta)

plt.figure(2)
plt.streamplot(x,y,ana_u,ana_v)
plt.title("Rankine half oval analytical solution")
plt.show()

