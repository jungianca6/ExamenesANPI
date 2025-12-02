import numpy as np

def rectangulo(f,a,b):
    I= (b-a)*f((a+b)/2)
    return I

def rectangulo_comp(f,a,b,n):
    h=(b-a)/n
    x = np.linspace(a,b,n+1)
    I=0
    for j in range(n):
        I=I+rectangulo(f,x[j],x[j+1])
    return I

def rectangulo_iter(f,a,b):
    iterMax=1e10
    tol=1e-10
    Sk=rectangulo_comp(f,a,b,1)
    for k in range(2,int(iterMax)):
        SkN=rectangulo_comp(f,a,b,k)
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

I_Rectangulo= rectangulo(f,a,b)
I_Rectangulo_Comp= rectangulo_comp(f,a,b,n)
I_Rectangulo_Iter= rectangulo_iter(f,a,b)

print("Rectangulo:")
print(I_Rectangulo)
print("Rectangulo Compuesto")
print(I_Rectangulo_Comp)
print("rectangulo Iterativo")
print(I_Rectangulo_Iter)