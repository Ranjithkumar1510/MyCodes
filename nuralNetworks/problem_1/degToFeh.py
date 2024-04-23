# !/bin/python3

import numpy as np
import random
import matplotlib.pyplot as plt
import os

os.system("rm -rf image")
os.system("mkdir image")


degC = np.array([5,7,15,20,25])

F = np.array([41,44.6,59,68,77])

# defining "neuron" function
def f(w,b):
    # Predicting F value

    F_pred = (w*degC)+b

    return F_pred

# needed list
Loss = []

''' Learning Rate '''
LR = 0.001

# initializing c value
w = random.random()
b = random.random()

print("initial weight and bias value = ",w,b)

L = 1.0
while L>=1e-6:
    ''' New prediction value '''
    F_pred = f(w,b)

    ''' calculating Loss '''
    L = np.mean((F-F_pred)**2)
    Loss.append(L)

    print("Loss = ",L)

    ''' Calculating the derivative of Loss '''
    dLdw = -2*np.mean(degC*(F-F_pred))
    dLdb = -2*np.mean((F-F_pred))

    ''' new weight and bias value '''
    w = w - LR*dLdw
    b = b - LR*dLdb

    print("new weight and bias value = ",w,b)

F_pred = f(w,b)

''' Plotting section '''
plt.figure(figsize=(16,8))
plt.plot(Loss,"-r",linewidth=3)
plt.xlabel("N",fontsize=15)
plt.ylabel("Loss",fontsize=15)
plt.grid()
plt.title("Loss plot",fontsize=15)
plt.savefig("image/Loss.png",dpi=150)
plt.close()

plt.figure(figsize=(16,8))
plt.plot(degC,F,"-b",linewidth=3,label="original data")
plt.plot(degC,F_pred,"or",ms=7,label="fitted data")
plt.xlabel(r"$\degree C$",fontsize=15)
plt.ylabel("fahrenheit",fontsize=15)
plt.legend()
plt.grid()
plt.title("model trained data plot",fontsize=15)
plt.savefig("image/data.png",dpi=150)
plt.close()

plt.figure(figsize=(16,8))
plt.plot(np.linspace(0,len(degC)-1,len(degC)),np.abs((F-F_pred))*100/F,"-ob",linewidth=3)
plt.xlabel(r"$N$",fontsize=15)
plt.ylabel("error %",fontsize=15)
plt.grid()
plt.title("error plot",fontsize=15)
plt.savefig("image/error.png",dpi=150)
plt.close()


