import sys
sys.path.append("Funcoes_importantes")

import zerosfuncoes as zf
import numpy as np
import matplotlib.pyplot as plt

def f(x,k1=50000.0,k2=40.0,m=90.0,g=9.81,h=0.45):
    return(((2*k2*np.sqrt(x**5))/5)+((k1*(x**2))/2)-m*g*x-m*g*h)

x=np.linspace(0,0.3,1000)
plt.plot(x,f(x))
print("d= "+str(zf.bissec(f,0.1,0.2,0.001,20))+"m")
plt.show()



