import sys
sys.path.append("Funcoes_importantes")

import zerosfuncoes as zf
import numpy as np

def f(y,x):
    return(y-np.sin(y)*0.9-x)

def der(y):
    return(1-0.9*np.cos(y))

def calculo_de_y(f,der,x,i):
    def g(y):
        return(f(y,x))
    y=zf.metodo_newton(g,der,0.1*i,0.001,10)
    return(y)

for i in range(0,30):
    k=((np.pi)/29)*i
    print("Para x=",k,"y=",calculo_de_y(f,der,k,i))