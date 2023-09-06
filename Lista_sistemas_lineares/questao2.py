import numpy as np

def auxiliar_elim_gauss(matriz_inicial,b,n):
    
    matriz_b=b.astype(float)
    matriz_b.reshape(1,n)
    matriz=matriz_inicial.astype(float)
    matriz=matriz.reshape(n,n)
    
    for i in range(0,n-1):
        k=i
        l= max(abs(matriz[i:,i]))
        while(abs(matriz[i,i])<l):
           matriz[[i,k+1],:]=matriz[[k+1,i],:]
           matriz_b[i],matriz_b[k+1]=matriz_b[k+1],matriz_b[i]
           k+=1
        
        for j in range(i+1,n):
            
            mult=(matriz[j,i]/matriz[i,i])
            mult=round(mult,10)
            matriz[j,:]=matriz[j,:]-mult*matriz[i,:]
            matriz_b[j]=matriz_b[j]-mult*matriz_b[i]
    
    return(matriz,matriz_b)              


def matriz_L_e_U(matriz_inicial,b,n):
    
    matriz_b=b.astype(float)
    matriz_b.reshape(1,n)
    matriz=matriz_inicial.astype(float)
    matriz=matriz.reshape(n,n)
    matriz_L=np.identity(n)
    
    for i in range(0,n-1):
        k=i
        l= max(abs(matriz[i:,i]))
        while(abs(matriz[i,i])<l):
           matriz[[i,k+1],:]=matriz[[k+1,i],:]
           matriz_b[i],matriz_b[k+1]=matriz_b[k+1],matriz_b[i]
           k+=1
        
        matriz=matriz.astype(float)
        
        for j in range(i+1,n):
            
            mult=(matriz[j,i]/matriz[i,i])
            matriz_L[j,i]=mult
            matriz[j,:]=matriz[j,:]-mult*matriz[i,:]
            
    
    return(matriz,matriz_L,matriz_b)   
    



def eliminacao_gauss(A,b,n):
    
    matriz_a,c=auxiliar_elim_gauss(A,b,n) 
    valores_de_x= np.ones(n)
    valores_de_x[-1]=c[-1]/matriz_a[-1,-1]
    for i in range(n-2,-1,-1):
        
        k=c[i]
        
        for j in range(i+1,n):
            y=matriz_a[i,j]*valores_de_x[j]
            k= k-y
            k=round(k,15)
        
        valores_de_x[i]=k/matriz_a[i,i]
    
    return(valores_de_x)


def metodo_LU(A,b,n):
    
    U,L,matriz_b=matriz_L_e_U(A,b,n)
    y=eliminacao_gauss(L,matriz_b,n)
    x=eliminacao_gauss(U,y,n)
    return(x)


def matriz_do_problema(n):
    A=np.identity(n)
    b=np.zeros(n) 
    for i in range(0,n):
        b[i]=i+2
        for j in range(0,n):
            A[i,j]=i+1+j+1
    return(A,b)

a,b=matriz_do_problema(5)
print(auxiliar_elim_gauss(a,b,5))
    
    
