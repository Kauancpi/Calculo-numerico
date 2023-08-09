import sys
sys.path.append("Funcoes_importantes")


import zerosfuncoes as zf
from erro_relativo import erro_percentual
import matplotlib.pyplot as plt
import numpy as np

def g(x):
    return(2*(x**3)-11.7*(x**2)+17.7*x-5)

def phi(x):
    return(np.cbrt(11.7*(x**2)-x**3-17.7*x+5))

def der(x):
    return(6*(x**2)-23.4*(x)+17.7)



x=np.linspace(3,4,1000)
plt.plot(x,g(x))
print("Graficamente vemos que a raiz eh 3.56 aproximadamente")
print("A raiz encontrada pelo metodo do ponto fixo:" , zf.pontofixo(g,phi,3,0.01,100))
print("Erro aproximado: "+ str(erro_percentual(zf.pontofixo(g,phi,3,0.01,100),zf.metodo_newton(g,der,3,0.01,100)))+"%")
print("A raiz encontrada pelo metodo de newton:",zf.metodo_newton(g,der,3,0.01,100))
print("Erro aproximado: "+ str(erro_percentual(zf.metodo_newton(g,der,3,0.001,100),zf.metodo_newton(g,der,3,0.001,100)))+"%")
print("A raiz encontrada pelo metodo das secantes:", zf.metodo_secante(g,4,3,0.01,100))
print("Erro aproximado: "+ str(erro_percentual(zf.metodo_secante(g,3,4,0.01,3),zf.metodo_newton(g,der,3,0.01,100)))+"%")
plt.show()


