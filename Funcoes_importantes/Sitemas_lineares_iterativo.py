import numpy as np

def pythag(a,b):
    p=max(abs(a),abs(b))
    q=min(abs(a),abs(b))
    while(abs(q)>0.00000000001):
        r=(q/p)**2
        s=r/(4+r)
        p=p+2*s*p
        q=s*q
    return(p)

def norma_euclidiana(x):
    s=0
    for i in range(0,len(x)):
        s=pythag(s,x[i])
    return(s)

def Gauss_Jacobi(A,b,n,iteracoes,tolerancia):
    valores_x=np.zeros(n)
    matriz_b=b.astype(float)
    matriz_b=matriz_b.reshape(n)
    matriz_a=A.astype(float)
    matriz_a=matriz_a.reshape(n,n)
    for k in range(0,iteracoes):
        x_temp=np.zeros(n)
        for i in range(0,n):
            x=0
            y=0
            
            for j in range(0,i):
                x+=matriz_a[i,j]*valores_x[j]
            
            for j in range(i+1,n):
                y+=matriz_a[i,j]*valores_x[j]
            
            x_temp[i]=(1/matriz_a[i,i])*(matriz_b[i]-x-y)
        if(norma_euclidiana(x_temp-valores_x)<tolerancia):
            valores_x=x_temp
            break
        valores_x=x_temp
    
    return(valores_x)

def Gauss_Seibel(A,b,n,iteracoes,tolerancia):
    valores_x=np.zeros(n)
    matriz_b=b.astype(float)
    matriz_b=matriz_b.reshape(n)
    matriz_a=A.astype(float)
    matriz_a=matriz_a.reshape(n,n)
    for k in range(0,iteracoes):
        x_temp=np.zeros(n)
        for i in range(0,n):
            x=0
            y=0
            
            for j in range(0,i):
                x+=matriz_a[i,j]*x_temp[j]
            
            for j in range(i+1,n):
                y+=matriz_a[i,j]*valores_x[j]
            
            x_temp[i]=(1/matriz_a[i,i])*(matriz_b[i]-x-y)
        if(norma_euclidiana(x_temp-valores_x)<tolerancia):
            valores_x=x_temp
            break
        valores_x=x_temp
    
    return(valores_x)
