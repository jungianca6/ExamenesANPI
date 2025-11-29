import numpy as np

def trapecio(f,a,b):
    I= (b-a)*(f(a)+f(b))/2
    return I

def trapecio_comp(f,a,b,n):
    h=(b-a)/n
    x = np.linspace(a,b,n+1)
    I=0
    for j in range(n):
        I=I+trapecio(f,x[j],x[j+1])
    return I

def trapecio_iter(f,a,b):
    iterMax=1e10
    tol=1e-10
    Sk=trapecio_comp(f,a,b,1)
    for k in range(2,int(iterMax)):
        SkN=trapecio_comp(f,a,b,k)
        er=abs(SkN-Sk)
        if er<tol:
            Sk=SkN
            break
        Sk=SkN
    return Sk


def f(x):
    return np.exp(-x**2)

a=-2
b=2
n=100

I_Trapecio= trapecio(f,a,b)
I_Trapecio_Comp= trapecio_comp(f,a,b,n)
I_Trapecio_Iter= trapecio_iter(f,a,b)

print("Trapecio:")
print(I_Trapecio)
print("Trapecio Compuesto")
print(I_Trapecio_Comp)
print("Trapecio Iterativo")
print(I_Trapecio_Iter)
