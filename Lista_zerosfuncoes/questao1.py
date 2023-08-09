import sys
sys.path.append("Funcoes_importantes")


import zerosfuncoes as zf
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return(1-((20**2)/((9.81*(3*x+(x**2)/2)**3)))*(3+x))

    

x=np.linspace(0.5,2.6,100)
plt.plot(x,f(x),"b--")
print("A raiz encontrada pelo metodo da bissecção:",zf.bissec(f,0.5,2,0.01,10))
print("A raiz encontrada pelo metodo da falsa posicao:",zf.fakeposition(f,0.5,2.5,0.01,10))
plt.show()

