# Rankine -fULL Oval

import numpy as np
import matplotlib.pyplot as plt

''' Creating a mesh grid'''

x,y=np.meshgrid(np.linspace(0,1,200),np.linspace(0,1,200))
Nx=len(x)
Ny=len(y)

u=np.zeros([Nx,Ny])
v=np.zeros([Nx,Ny])
''' Initial Conditions velocity and Source strength'''

V_inf=10
Lamda=100

''' Center of the Source and sink'''

xc1=0.48
xc2=0.52

b=(xc2-xc1)/2
xc=0.5
yc=0.5

''' Calculating the radius and theta '''
# From the Center
r=np.sqrt((x-xc)**2+(y-yc)**2)
theta=np.arctan2(y-yc,x-xc)
t1=np.arctan2(y-yc,x-xc1)
t2=np.arctan2(y-yc,x-xc2)

'''Computing stream function'''
psi=V_inf*r*np.sin(theta)+(Lamda*(t1-t2)/2/np.pi)
# psi=V_inf*y+(Lamda*b*y/(np.pi*(x**2+y**2-b**2)))

'''plot the stream line'''

# plt.close('all')

# plt.contour(x,y,psi)
# plt.colorbar()
# plt.title("Stream function")
# plt.show()

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
    
''' Analatically Velocity Calculation  mistake is there check'''

X=x-xc
Y=y-yc

a1=(X+b)/((X+b)**2+Y**2)
a2=(X-b)/((X-b)**2+Y**2)
# analytical value of u velocity
ana_u=V_inf+(Lamda*(a1-a2)/2/np.pi)

a1=Y/((X+b)**2+Y**2)
a2=Y/((X-b)**2+Y**2)
# analytical value of v velocity
ana_v=Lamda*(a1-a2)/2/np.pi

plt.figure()
plt.streamplot(x,y,u,v)
# plt.streamplot(x,y,ana_u,ana_v)
plt.title("Rankine Oval")
plt.colorbar()
plt.show()
