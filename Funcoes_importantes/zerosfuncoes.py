from math import fabs
import numpy as np

#metodo da bisseccao
#f= funcao, a = menor valor, b = maior valor, dx= tolerancia, iteracoes = iteracoes
def bissec(f,a,b, dx, iteracoes):
    x=0
    media = (b+a)/2
    while ((f(media)>dx or f(media)<-dx) and x<iteracoes ):
        if f(media)*f(a)<0:
            b=media
            media = (media+a)/2
            x+=1
            continue
        elif f(media)*f(b)<0:
            a=media
            media = (b+media)/2
            x+=1
            continue
    else:
        return(media)
    
#Metodo da Falsa posicao
#f=funcao, a = menor valor, b= maior valor, dx= tolerancia, iteracoes = iteracoes
def fakeposition(f,a,b,dx,iteracoes):
    if f(a)*f(b) > 0:
        print("Não dá pra usar esse método")
        return(False)
    x=0
    mediap = (a*fabs(f(b))+b*fabs(f(a)))/(fabs(f(a))+fabs(f(b)))
    while (f(mediap)>(dx) or f(mediap)<-(dx)) and x<iteracoes:
        if f(mediap)*f(a)<0:
            b=mediap
            mediap = (a*fabs(f(mediap))+mediap*fabs(f(a)))/(fabs(f(a))+fabs(f(mediap)))
            x+=1
            continue
        elif f(mediap)*f(b)<0:
            a=mediap
            mediap = (b*fabs(f(mediap))+mediap*fabs(f(b)))/(fabs(f(b))+fabs(f(mediap)))
            x+=1
            continue
    else:
        return(mediap) 
    
# Metodo do ponto fixo
#f=funcao, phi = funcao de iteracao, inicial=chute inicial, dx = tolerancia, iteracoes = iteracoes
def pontofixo(f,phi,inicial,dx,iteracoes):
    x_k=[inicial]
    x=0
    while((fabs(f(x_k[-1]))>dx)and x<iteracoes):
        x_next=phi(x_k[-1])
        x_k.append(x_next)
        x+=1
    return(x_k[-1])

# Funcao de iteracao utilizada no metodo de newton
def phinewton(x,f,der):
    return(x-f(x)/der(x))

# metodo de Newton
#f= funcao, der = derivada da funcao, inicial = chute inicial, dx = tolerancia, iteracoes= iteracoes
def metodo_newton(f,der,inicial,dx,iteracoes):
    x_k=[inicial]
    x=0
    while((fabs(f(x_k[-1]))>dx) and x<iteracoes):
        x_next=phinewton(x_k[-1],f,der)
        x_k.append(x_next)
        x+=1
    return(x_k[-1])
    
# Funcao de iteracao metodo da secante
def iteracao_secante(f,x0,x1):
    return(x1-f(x1)*(x1-x0)/(f(x1)-f(x0)))

# Metodo da secante
#f= funcao, x0,x1=intervalo, x0<x1, dx=tolerancia, iteracoes=iteracoes
def metodo_secante(f,x0,x1,dx,iteracoes):
    x_k=[x0,x1]
    x=0
    while((fabs(f(x_k[-1]))>dx)and x<iteracoes):
        x_next=iteracao_secante(f,x_k[-2],x_k[-1])
        x_k.append(x_next)
        x+=1
    return(x_k[-1])
