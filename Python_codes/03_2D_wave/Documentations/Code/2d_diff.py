# /bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

Lx = 2.0
Ly = 2.0
max_t = 0.5
nu = 0.1
a,b = 0.5,1.0

Nx = 21
Ny = 21
Nt = 51

[x,y] = [np.linspace(0,2,Nx),np.linspace(0,2,Ny)]
X,Y = np.meshgrid(x,y)

dt = max_t/(Nt-1)
dx = Lx/(Nx-1)
dy = Ly/(Ny-1)

#-------------------------------------------------------------------------------
# Boundary condition
u = np.ones([Nt,Ny,Nx])
v = np.ones([Nt,Ny,Nx])

for i in range(Nx):
    u[0,0,i] = 1.0
    v[0,0,i] = 1.0

for i in range(Nx):
    u[0,Ny-1,i] = 1.0
    v[0,Ny-1,i] = 1.0

for j in range(Ny):
    u[0,j,0] = 1.0
    v[0,j,0] = 1.0

for j in range(Nx):
    u[0,j,Nx-1] = 1.0
    v[0,j,Nx-1] = 1.0

#-------------------------------------------------------------------------------
# initial condition
for i in range(Nx):
    if x[i]==a:
        x1 = i
        print(x1)
    if x[i]==b:
        x2 = i
        print(x2)

for j in range(Ny):
    if y[j]==a:
        y1 = j
    if y[j]==b:
        y2 = j

for i in range(x1,x2+1):
    for j in range(y1,y2+1):
        u[0,j,i] = 2.0
        v[0,j,i] = 2.0

#-------------------------------------------------------------------------------
# computing section
alpha = nu*dt*(1/dx**2+1/dy**2)
print(alpha)
for k in range(1,Nt):
    for j in range(1,Ny-1):
        for i in range(1,Nx-1):
            u[k,j,i] = u[k-1,j,i]+alpha*(u[k-1,j,i+1]-2*u[k-1,j,i]+u[k-1,j,i-1])
            v[k,j,i] = v[k-1,j,i]+alpha*(v[k-1,j,i+1]-2*v[k-1,j,i]+v[k-1,j,i-1])

#-------------------------------------------------------------------------------
# ploting section
fig = plt.figure()

ax = fig.gca(projection ='3d')
l1=ax.plot_surface(X,Y,v[00],color ='b')
ax.set_title("v vale at t=0")
plt.show()

fig = plt.figure()

ax = fig.gca(projection ='3d')
l1=ax.plot_surface(X,Y,v[00],color ='b')
l2=ax.plot_surface(X,Y,v[10],color ='r')
l3=ax.plot_surface(X,Y,v[20],color ='y')
l4=ax.plot_surface(X,Y,v[30],color ='k')
l5=ax.plot_surface(X,Y,v[40],color ='m')
l6=ax.plot_surface(X,Y,v[50],color ='g')
ax.set_title("Change in v with respect to time")
plt.show()

fig = plt.figure()

ax = fig.gca(projection ='3d')
l1=ax.plot_surface(X,Y, u[00],color ='b')
ax.set_title(" u vale at t=0")
plt.show()

fig = plt.figure()

ax = fig.gca(projection ='3d')
l1=ax.plot_surface(X,Y,u[00],color ='b')
l2=ax.plot_surface(X,Y,u[10],color ='r')
l3=ax.plot_surface(X,Y,u[20],color ='y')
l4=ax.plot_surface(X,Y,u[30],color ='k')
l5=ax.plot_surface(X,Y,u[40],color ='m')
l6=ax.plot_surface(X,Y,u[50],color ='g')
plt.title("Change in u with respect to time")
plt.show()
