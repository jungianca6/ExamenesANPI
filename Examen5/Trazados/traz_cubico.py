import numpy as np


def traz_cubico(xv,yv):
    m = len(xv)
    n = (m - 1) #(m - 2) = (n - 1)
    h = np.zeros(n)

    #Calcular vector h
    for j in range(n):
        h[j] = xv[j+1]-xv[j]

    #Crear matriz A
    A=np.zeros((n-1,n-1))
    #Fila 1
    A[0,0]=2*(h[0]+h[1])
    A[0,1]=h[1]
    #Fila n-1
    A[n-2,n-3]=h[n-2]
    A[n-2,n-2]=2*(h[n-2]+h[n-1])

    for k in range(1,n-2):
        A[k,k-1] = h[k]
        A[k,k] = 2*(h[k]+h[k+1])
        A[k,k+1] = h[k+1]

    #Calcular vector U
    u=np.zeros(n-1)
    for k in range(n-1):
        u[k] = 6*((yv[k+2]-yv[k+1])/h[k+1]-(yv[k+1]-yv[k])/h[k])

    #Calcular vector M
    g=np.linalg.solve(A,u)
    M = np.concatenate(([0], g, [0]))

    #Calcular constantes
    Z=np.zeros((n,4))

    for j in range(n):
        aj= (M[j+1]-M[j])/(6*h[j])
        bj=M[j]/2
        cj=(yv[j+1]-yv[j])/(h[j])-(h[j]/6)*(M[j+1]+2*M[j])
        dj=yv[j]

        Z[j, :] = np.array([aj, bj, cj, dj])

    return Z

def f(x):
    return 3*x*np.exp(x)-2*np.exp(x)

xv=np.array([1,1.05,1.07,1.1])
yv=f(xv)

Z=traz_cubico(xv,yv)
print(Z)