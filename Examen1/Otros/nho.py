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



def nho (fun, x0, tol, max_iter):
    """
    Encuentra una raíz de la función utilizando el metodo de Newton-Hermite-Ostrowski.

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

    # Derivada simbólica
    dfs = sp.diff(f_sym, x)
    dfn = sp.lambdify(x, dfs, 'numpy')

    for k in range(max_iter):
        fpx = dfn(xk)

        # Evitar división por cero con tolerancia
        if abs(fpx) < 1e-15:
            return None, k, None

        #Newton-Raphson
        zn = xk - fun(xk) / fpx
        fz = fun(zn)
        fpz = dfn (zn)

        # Evitar división por cero en H
        if abs(3 * fpz - fpx) < 1e-15:
            return None, k, None

        H = (fpx - fpz) / (3 * fpz - fpx)

        # Fórmula NHO
        xnew = zn - H * (fz / fpx)
        erk = abs(fun(xnew))

        # Criterio de parada
        if erk < tol:
            return xnew, k + 1, erk
        xk = xnew
    return xk, max_iter, erk


nho_raiz, nho_iteraciones, nho_error = nho (fun, -0.1, 1e-8, 10000)
