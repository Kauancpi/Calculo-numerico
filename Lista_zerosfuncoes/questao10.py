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


print("teste com 3,4:",pythag(3,4))
print("teste com -5,12:",pythag(-5,12))
print("teste com 7,24:",pythag(7,24))
print("teste norma euclidiana 3,4,5,6,7,8:",norma_euclidiana([3,4,5,6,7,8]))