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


def stiffensen(fun, x0, tol, max_iter):
    """
    Encuentra una raíz de la función utilizando el metodo de Steffensen.

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
    for k in range(max_iter):
        if abs(fun(xk)-fun(xk-1)) < 1e-15:  # evitar división por cero
            return None, k, None
        else:
            xk = xk-(fun(xk)**2)/(fun(xk+fun(xk))-fun(xk)) # formula de Steffensen
            erk = abs(fun(xk)) # error absoluto
            if erk < tol:  # Criterio de parada
                k = k + 1
                break
    return xk, k + 1, erk


st_raiz, st_iteraciones, st_error = stiffensen(fun, -0.1, 1e-8, 10000)
print(st_raiz, st_iteraciones, st_error)