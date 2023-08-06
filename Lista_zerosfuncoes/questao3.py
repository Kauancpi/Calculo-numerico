import sys
sys.path.append("Funcoes_importantes")

import zerosfuncoes as zf
import numpy as np
from erro_relativo import erro_percentual

def f(x):
    return(np.pi*(x**2)*(3-(x/3))-30)

def der(x):
    return(np.pi*x*(6-x))

raiz_real=zf.metodo_newton(f,der,3,0.001,30)
for i in range(1,4):
    x=zf.metodo_newton(f,der,3,0.0001,i)
    print("iteracao",i,": h="+str(x))
    print("erro percentual:",erro_percentual(x,raiz_real),"%")
    