import sys
sys.path.append("Funcoes_importantes")

import zerosfuncoes as zf
import numpy as np
import matplotlib.pyplot as plt

def f(x,forca=1.25,q1=2.e-5,q2=2.e-5,a=0.9,epsilon_0=885.e-14):
    return(((1/(4*np.pi*epsilon_0))*(q1*q2*x)/(np.sqrt((x**2+a**2)**3)))-forca)

x=np.linspace(0,0.5,1000)
plt.plot(x,f(x))
print("x= "+str(zf.bissec(f,0,0.5,0.001,20))+"m")
plt.show()