import numpy as np
import scipy.optimize as opt

def fun(x):
    return np.exp(x) - 2*x - 10


# Encontrar el mínimo de una función f(x) en un intervalo [a, b]
a, b = -2, 2
xmin = opt.fminbound(fun, a, b)
print(xmin)

# Calcular el máximo
def newfun(x):
    return -fun(x)

a, b = 0, 3
xmax = opt.fminbound(newfun, a, b)
print(xmax)