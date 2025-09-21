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




def secante(fun, x0, x1, tol, max_iter):
    """
    Encuentra una raíz de la función utilizando el metodo de la secante.

    Parámetros:
        fun : función
            Función cuya raíz se busca
        x0 : float
            Primer valor inicial
        x1 : float
            Segundo valor inicial
        tol : float
            Tolerancia para el criterio de parada
        max_iter : int
            Número máximo de iteraciones permitidas

    Retorna:
        tuple: (Aproximación de la raíz, número de iteraciones, error absoluto)
    """

    for k in range(max_iter):
        if abs(fun(x1) - fun(x0)) < 1e-15:  # Evitar división por cero
            return None, k, None
        else:
            xk = x1-fun(x1)*(x1-x0)/(fun(x1)-fun(x0)) # Actualiza xk usando la fórmula de la secante
            np.seterr(over='ignore')
            x0,x1 = x1,xk
            erk = abs(fun(xk)) # Calcula el error absoluto
            if erk < tol:  # Criterio de parada
                k = k + 1
                break
    return xk, k + 1, erk


sec_raiz, sec_iteraciones, sec_error = secante(fun, -0.3, -0.1, 1e-8, 10000)

print(sec_raiz, sec_iteraciones, sec_error)
