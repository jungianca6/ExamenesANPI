import numpy as np
import sympy as sp
import scipy.optimize as opt
from matplotlib import pyplot as plt


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
    print(xmax)

    alphamax= abs(fdn(xmax))

    n= nPlusOne - 1
    mult=1
    for j in range(n+1):
        mult = mult * (x_0-xv[j])

    ct = (alphamax/sp.factorial(nPlusOne)) * abs(mult)

    return ct

def f(x):
    return sp.exp(x/2)

a=0
b=3
xv= np.array([0,1.25,1.5,2,3])
x_0= 0.2

cota=cota_interpolacion(f,a,b,xv,x_0)
print(cota)


x_exact = np.linspace(a, b, 1000)  # Equivalente a a:0.0001:b
y_exact = np.exp(x_exact/2)  # Solución exacta

plt.plot(x_exact, y_exact, label="Función")
plt.title("Funcion de cota")
plt.grid()
plt.legend()
plt.show()