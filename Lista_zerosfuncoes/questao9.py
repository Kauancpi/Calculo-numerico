import sys
sys.path.append("Funcoes_importantes")

import zerosfuncoes as zf
import numpy as np
import matplotlib.pyplot as plt

def Area(x):
    return(x*np.cos(x))

def der(x):
    return(np.cos(x)-x*np.sin(x))


x=zf.bissec(der,0,(np.pi)/2,0.01,20)
print("Area maxima sera quando x=",x, "\nEla valera:",Area(x))

y=np.linspace(0,np.pi/2,1000)
plt.plot(y,Area(y))
plt.xlabel("x")
plt.ylabel("Area")
plt.show()