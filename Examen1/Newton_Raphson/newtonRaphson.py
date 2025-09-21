import math
import numpy as np
import sympy as sp

def fun(x):
    """
    Evalúa la función f(x) = x*e^(-x) - 5 - (cos(x)/x) en un punto dado.

    Parámetros:
        x : float
            Punto en el que evaluar la función

    Retorna:
            float: Valor de la función en x, o infinito si x = 0
    """

    if x == 0:
        return float('inf')  # si hay un valor muy grande, no revienta
    return x * np.exp(-x) - 5 - (np.cos(x) / x)


def newton_raphson(fun, x0, tol, max_iter):
    """
    Encuentra una raíz de la función utilizando el metodo de Newton-Raphson.

    Parámetros:
        fun : función
            Función cuya raíz se busca
        x0 : float
            Valor inicial para comenzar las iteraciones
        tol : float
            Tolerancia para el criterio de parada
        max_iter : int
            Número máximo de iteraciones permitidas

    Retorna:
        tuple: (Aproximación de la raíz, número de iteraciones, error absoluto)
    """

    xk = x0
    x = sp.symbols('x')  # Variable simbólica
    f_sym = x * sp.exp(-x) - 5 - (sp.cos(x) / x)  # Función simbólica para derivar

    # Derivada simbólica y luego convertirla en función numérica
    dfs = sp.diff(f_sym, x)
    dfn = sp.lambdify(x, dfs, 'numpy')

    for k in range(max_iter):
        if dfn(xk) == 0:  # Evitar división por cero
            return None, k, None
        else:
            xk = xk - fun(xk) / dfn(xk)  # Actualiza xk usando la fórmula de Newton-Raphson
            erk = abs(fun(xk))  # Calcula el error absoluto
            if erk < tol:  # Criterio de parada
                k = k + 1
                break
    return xk, k + 1, erk  # Retorna la aproximación, número de iteraciones y el error


nr_raiz, nr_iteraciones, nr_error = newton_raphson(fun, -0.1, 1e-8, 10000)

print (nr_raiz),
print(nr_iteraciones),
print(nr_error)

