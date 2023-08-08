import numpy as np


#funcao pra triangular matrizes quadradas
def triangular_superior(matriz_inicial,n):
    matriz=matriz_inicial.astype(float)
    matriz=matriz.reshape(n,n)
    for i in range(0,n-1):
        k=i
        while(matriz[i,i]==0):
           if k==n:
               return("Não dá pra triangular")
           matriz[i,:],matriz[k+1,:]=matriz[k+1,:],matriz[i,:]
           k+=1
        for j in range(i+1,n):
            mult=(matriz[j,i]/matriz[i,i])
            matriz[j,:]=matriz[j,:]-mult*matriz[i,:]
    return(matriz)


def auxiliar_elim_gauss(matriz_inicial,b,n):
    matriz_b=b.astype(float)
    matriz_b.reshape(1,n)
    matriz=matriz_inicial.astype(float)
    matriz=matriz.reshape(n,n)
    for i in range(0,n-1):
        k=i
        while(matriz[i,i]==0):
           if k==n:
               return("Não dá pra triangular")
           matriz[i,:],matriz[k+1,:]=matriz[k+1,:],matriz[i,:]
           k+=1
        for j in range(i+1,n):
            mult=(matriz[j,i]/matriz[i,i])
            matriz[j,:]=matriz[j,:]-mult*matriz[i,:]
            matriz_b[j]=matriz_b[j]-mult*matriz_b[i]
    return(matriz,matriz_b)              



def eliminacao_gauss(A,b,n):
    matriz_b=b.astype(float)
    matriz_b.reshape(1,n)
    matriz_a,c=auxiliar_elim_gauss(A,matriz_b,n)
    valores_de_x= np.ones(n)
    valores_de_x[-1]=c[-1]/matriz_a[-1,-1]
    for i in range(n-2,-1,-1):
        k=c[i]
        for j in range(i+1,n):
            k-=matriz_a[i,j]*valores_de_x[j]
        valores_de_x[i]=k/matriz_a[i,i]
    return(valores_de_x)