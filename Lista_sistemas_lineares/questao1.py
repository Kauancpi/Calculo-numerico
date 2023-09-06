import numpy as np

def auxiliar_elim_gauss(matriz_inicial,b,n,aproximacao):
    
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
            mult=round(mult,aproximacao)
            matriz[j,:]=matriz[j,:]-mult*matriz[i,:]
            matriz_b[j]=matriz_b[j]-mult*matriz_b[i]
    
    return(matriz,matriz_b)    


def eliminacao_gauss(A,b,n,aproximacao):
    
    matriz_a,c=auxiliar_elim_gauss(A,b,n,aproximacao) 
    valores_de_x= np.ones(n)
    valores_de_x[-1]=c[-1]/matriz_a[-1,-1]
    for i in range(n-2,-1,-1):
        
        k=c[i]
        
        for j in range(i+1,n):
            y=matriz_a[i,j]*valores_de_x[j]
            k= k-y
            k=round(k,aproximacao)
        y=k/matriz_a[i,i]
        valores_de_x[i]=round(y)
        
    
    return(valores_de_x)

#letra a
A_a=np.array([0.0001,1,1,1])
b_a=np.array([1,2])

x_a=eliminacao_gauss(A_a,b_a,2,3)
print(x_a)

print("Erro do x1:" ,abs(x_a[0]-1.0001)/1.0001)
print("Erro do x2:" ,(x_a[1]-0.99989999)/0.99989999)

#letra b
A_b=np.array([0.0001,1,1,1])
b_b=np.array([2,1])

x_b=eliminacao_gauss(A_b,b_b,2,3)
x_correto_b=eliminacao_gauss(A_b,b_b,2,15)
print(x_b)
print(x_correto_b)

print("Erro do x1:" ,abs(x_b[0]-x_correto_b[0])/x_correto_b[0])
print("Erro do x2:" ,abs(x_b[1]-x_correto_b[1])/x_correto_b[1])

#letra c
def auxiliar_elim_gauss_sem_pivotear(matriz_inicial,b,n,aproximacao):
    
    matriz_b=b.astype(float)
    matriz_b.reshape(1,n)
    matriz=matriz_inicial.astype(float)
    matriz=matriz.reshape(n,n)
    
    for i in range(0,n-1):
        
        for j in range(i+1,n):
            
            mult=(matriz[j,i]/matriz[i,i])
            mult=round(mult,aproximacao)
            matriz[j,:]=matriz[j,:]-mult*matriz[i,:]
            matriz_b[j]=matriz_b[j]-mult*matriz_b[i]
    
    return(matriz,matriz_b) 

def eliminacao_gauss_sem_pivotear(A,b,n,aproximacao):
    
    matriz_a,c=auxiliar_elim_gauss_sem_pivotear(A,b,n,aproximacao) 
    valores_de_x= np.ones(n)
    valores_de_x[-1]=c[-1]/matriz_a[-1,-1]
    for i in range(n-2,-1,-1):
        
        k=c[i]
        
        for j in range(i+1,n):
            y=matriz_a[i,j]*valores_de_x[j]
            k= k-y
            k=round(k,aproximacao)
        y=k/matriz_a[i,i]
        valores_de_x[i]=round(y)
        
    
    return(valores_de_x) 



A_c=np.array([0.0001,1,1,1])
b_c=np.array([1,1])

xc=eliminacao_gauss_sem_pivotear(A_c,b_c,2,15)
print(xc)
