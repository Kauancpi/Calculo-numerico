import sys
sys.path.append("Funcoes_importantes")

import zerosfuncoes as zf
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return((9/np.sin((125*np.pi/180)+x))+(7/np.sin(x)))

def der(x):
    return(9*np.sin(x+7*np.pi/36)/np.cos(x+7*np.pi/36)**2-7*np.cos(x)/np.sin(x)**2)

x=np.linspace(0.1,0.8,1000)
plt.plot(x,der(x))
y=zf.bissec(der,0.3,0.7,0.001,20)
print("A derivada vale 0 quando o angulo lambda=",y,"rad")
print("L maximo vale:",f(y),"pes")
plt.show()