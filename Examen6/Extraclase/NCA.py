import numpy as np

def NCA(f,a,b):
    h = (b - a) / 5

    x1= a+h
    x2=a+2*h
    x3=a+3*h
    x4=a+4*h

    I= (5*h/24)*(11*f(x1)+f(x2)+f(x3)+11*f(x4))
    return I

def NCA_comp(f,a,b,n):
    h=(b-a)/n
    x = np.linspace(a,b,n+1)
    I=0
    for j in range(n):
        I=I+NCA(f,x[j],x[j+1])
    return I

def NCA_iter(f,a,b):
    iterMax=1e10
    tol=1e-10
    Sk=NCA_comp(f,a,b,1)
    for k in range(2,int(iterMax)):
        SkN=NCA_comp(f,a,b,k)
        er=abs(SkN-Sk)
        if er<tol:
            Sk=SkN
            break
        Sk=SkN
    return Sk


def f(x):
    return x**2*np.exp(x**2)

a=0
b=2
n=50

I_NCA= NCA(f,a,b)
I_NCA_Comp= NCA_comp(f,a,b,n)
I_NCA_Iter= NCA_iter(f,a,b)

print("NCA:")
print(I_NCA)
print("NCA Compuesto")
print(I_NCA_Comp)
print("NCA Iterativo")
print(I_NCA_Iter)