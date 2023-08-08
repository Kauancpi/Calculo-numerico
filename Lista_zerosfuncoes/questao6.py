import sys
sys.path.append("Funcoes_importantes")

import zerosfuncoes as zf
import numpy as np


def f(x,re):
    return(4*np.log10(re*np.sqrt(x))-0.4-1/(np.sqrt(x)))

def determinar_f(f):
    re=float(input("Qual o valor de re?\n"))
    def g(x):
        return(f(x,re))
    return(zf.bissec(g,0.000001,1,0.000005,1000))


print("Valor de f:", determinar_f(f))

