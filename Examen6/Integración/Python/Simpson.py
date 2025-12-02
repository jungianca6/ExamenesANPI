import numpy as np

def simpson(f,a,b):
    I= (b-a)/6*(f(a)+4*f((a+b)/2)+f(b))
    return I

def simpson_comp(f,a,b,n):
    h=(b-a)/n
    x = np.linspace(a,b,n+1)
    I=0
    for j in range(n):
        I=I+simpson(f,x[j],x[j+1])
    return I

def simpson_iter(f,a,b):
    iterMax=1e10
    tol=1e-10
    Sk=simpson_comp(f,a,b,1)
    for k in range(2,int(iterMax)):
        SkN=simpson_comp(f,a,b,k)
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

I_Simpson= simpson(f,a,b)
I_Simpson_Comp= simpson_comp(f,a,b,n)
I_Simpson_Iter= simpson_iter(f,a,b)

print("Simpson:")
print(I_Simpson)
print("Simpson Compuesto")
print(I_Simpson_Comp)
print("Simpson Iterativo")
print(I_Simpson_Iter)