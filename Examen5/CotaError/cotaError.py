import numpy as np
import sympy as sp
import scipy.optimize as opt

def cota_interpolacion(f,a,b,xv,x_0):
    x = sp.symbols('x')

    fs= f(x)
    nPlusOne = len(xv)
    fds= sp.diff(fs,x,nPlusOne)
    fdn= sp.lambdify(x,fds, 'numpy')

    # Calcular el máximo
    def newfun(x):
        return -fdn(x)

    xmax = opt.fminbound(newfun, a, b)

    alphamax= abs(fdn(xmax))

    n= nPlusOne - 1
    mult=1
    for j in range(n+1):
        mult = mult * (x_0-xv[j])

    ct = (alphamax/sp.factorial(nPlusOne)) * abs(mult)

    return ct

def f(x):
    return sp.log(sp.asin(x)) / sp.log(x)

a=0.1
b=0.8
xv= np.array([0.1, 0.2, 0.3, 0.4 ,0.5 ,0.6, 0.7, 0.8])
x_0= 0.55

cota=cota_interpolacion(f,a,b,xv,x_0)
print(cota)