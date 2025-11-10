import sympy as sp
import numpy as np

def pol_lagrange(xv,yv):
    n = len(xv) - 1
    p = 0
    for k in range(n+1):
        p = p + yv[k]*Lk(xv,k)

    p = sp.expand(p)
    return p

def Lk(xv,k):
    x= sp.symbols('x')
    n = len(xv) - 1
    L=1
    for j in range(n+1):
        if j != k:
            L = L * (x-xv[j]) / (xv[k]-xv[j])

    return L

def main():
    xv= np.array([-2,0,1])
    yv= np.array([0,1,-1])

    return pol_lagrange(xv,yv)

p=main()
print(p)




