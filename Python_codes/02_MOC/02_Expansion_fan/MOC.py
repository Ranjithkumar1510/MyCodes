#!/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------
# initial conditions

# specific heat constant of air
g=1.4

# inlet Mach number
Mi= 2 

# Inlet Node points
Ni= 5 

# Total wall points
Nw= 10 

# Theta values for Bottom , top and inlet Nodes
bottom_t=np.radians(0)
top_t=np.radians(12)
inlet_t=0

# Height of the inlet
H=2

#-------------------------------------------------------------------------------
# Prandtl meyer function

def fun_Nu(M):
    a=(g+1)/(g-1)
    b=M**2-1
    nu=np.sqrt(a)*np.arctan(np.sqrt(b/a))-np.arctan(np.sqrt(b))

    return nu

#-------------------------------------------------------------------------------
# Mach number getting from P-M function
    # using Bi-section Method

def fun_M(nu):
    a=0.1
    b=10

    while True:
        c=(a+b)/2
        res=fun_Nu(c)-nu
        if res < 0:
            a=c
        else:
            b=c

        c=(a+b)/2
        res=fun_Nu(c)-nu
        # print(c,res)
        if np.abs(res)<1e-6:
            break

    return c

#-------------------------------------------------------------------------------
# Total number of points
Nt=(Ni*Nw)+((Ni-1)*(Nw-1))

# Needed array for Node
Node=np.zeros(Nt,dtype=int)
btm=np.zeros(Nw,dtype=int)
top=np.zeros(Nw,dtype=int)
inlet=np.zeros(Ni,dtype=int)

# Total Node
for i in range(Nt):
    Node[i]=i

# Inlet Node
for i in range(Ni):
    inlet[i]=i

# Top and Bottom Node
for i in range(Nw):
    btm[i]=i*(2*Ni-1)
    top[i]=btm[i]+(Ni-1)

#-------------------------------------------------------------------------------
# necessary Arrays
M=np.zeros(Nt)
K1=np.zeros(Nt)
K2=np.zeros(Nt)
nu=np.zeros(Nt)
theta=np.zeros(Nt)
Mu=np.zeros(Nt)

# Computing Mach number
for i in range(Nt):
    if i in inlet:
        M[i]=Mi
        theta[i]=inlet_t
        nu[i]=fun_Nu(M[i])
        K1[i]=nu[i]+theta[i]
        K2[i]=nu[i]-theta[i]
        Mu[i]=np.arcsin(1/M[i])
    elif i in btm:
        theta[i]=bottom_t
        K1[i]=K1[i-(Ni-1)]
        K2[i]=K1[i]-(2*theta[i])
        nu[i]=(K1[i-(Ni-1)]+K2[i])/2
        M[i]=fun_M(nu[i])
        Mu[i]=np.arcsin(1/M[i])
    elif i in top:
        theta[i]=top_t
        K2[i]=K2[i-Ni]
        K1[i]=(2*theta[i])+K2[i]
        nu[i]=(K1[i]+K2[i-Ni])/2
        M[i]=fun_M(nu[i])
        Mu[i]=np.arcsin(1/M[i])
    else:
        theta[i]=(K1[i-(Ni-1)]-K2[i-Ni])/2
        nu[i]=(K1[i-(Ni-1)]+K2[i-Ni])/2
        K1[i]=nu[i]+theta[i]
        K2[i]=nu[i]-theta[i]
        M[i]=fun_M(nu[i])
        Mu[i]=np.arcsin(1/M[i])

#-------------------------------------------------------------------------------
# Computing the location
x=np.zeros(Nt)
y=np.zeros(Nt)

# height between the two consicutive points in the inlet
h = H/(Ni-1)
for i in range(Nt):
    if i in inlet:
        x[i]=0
        y[i]=i*h
    elif i in btm:
        # only right running curve present
        S1=np.tan(theta[i-(Ni-1)]-Mu[i-(Ni-1)])
        x[i]=(y[i-(Ni-1)]-x[i-(Ni-1)]*S1)/(np.tan(theta[i])-S1)
        y[i]=x[i]*np.tan(theta[i])
    elif i in top:
        S2=np.tan(theta[i]+Mu[i])
        x[i]=(y[i-Ni]-x[i-Ni]*S2-H)/(np.tan(theta[i])-S2)
        y[i]=(x[i]*np.tan(theta[i]))+H
    else:
        S1=(np.tan(theta[i]+Mu[i])+np.tan(theta[i-Ni]+Mu[i-Ni]))/2
        S2=(np.tan(theta[i]-Mu[i])+np.tan(theta[i-(Ni-1)]-Mu[i-(Ni-1)]))/2
        x[i]=((S2*x[i-(Ni-1)]-S1*x[i-Ni])+(y[i-Ni]-y[i-(Ni-1)]))/(S2-S1)
        y[i]=y[i-(Ni)]+((x[i]-x[i-(Ni)])*S1)
#-------------------------------------------------------------------------------

# DataFrame

df=pd.DataFrame(np.transpose([M,K1,K2,theta,nu,Mu,x,y]),columns=["M","K1","K2","Theta","Nu","Mu","X","Y"])
print(df)

#-------------------------------------------------------------------------------

# plotting section
Yt=np.zeros(Nw)
Xt=np.zeros(Nw)
Xb=np.zeros(Nw) ; Yb=np.zeros(Nw)
for i in range(Nw):
    Xt[i]=x[top[i]]
    Yt[i]=y[top[i]]

for i in range(Nw):
    Xb[i]=x[btm[i]]
    Yb[i]=y[btm[i]]

plt.figure()
plt.plot(df["X"],df["Y"],'ko')
plt.plot(Xt,Yt,'-k',linewidth=2)
plt.plot(Xb,Yb,'-k',linewidth=2)
plt.axis("image")
plt.savefig("Grid.png",dpi=150)
plt.show()

plt.figure()
plt.tricontourf(df["X"],df["Y"],df["M"],100,cmap="jet")
plt.plot(Xt,Yt,'-k',linewidth=2)
plt.plot(Xb,Yb,'-k',linewidth=2)
plt.axis("image")
plt.colorbar(location='top')
plt.savefig("Contour.png",dpi=150)
plt.show()


