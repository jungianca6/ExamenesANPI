
import math
import numpy as np
import sympy as sp

def bolzano(f, a, b):
    """
    Verifica si se cumple el teorema de Bolzano para una función en un intervalo.

    Parámetros:
        f : función
            Función a evaluar
        a : float
            Extremo izquierdo del intervalo
        b : float
            Extremo derecho del intervalo

    Retorna:
        bool: True si f(a) y f(b) tienen signos opuestos, False en caso contrario
    """
    return f(a) * f(b) < 0

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


def falsa_posicion(fun, a, b, tol, max_iter):
    """
    Encuentra una raíz de la función utilizando el metodo de la falsa posición.

    Parámetros:
        fun : función
            Función cuya raíz se busca
        a : float
            Extremo izquierdo del intervalo inicial
        b : float
            Extremo derecho del intervalo inicial
        tol : float
            Tolerancia para el criterio de parada
        max_iter : int
            Número máximo de iteraciones permitidas

    Retorna:
        tuple: (Aproximación de la raíz, número de iteraciones, error absoluto)
    """
    if fun(a) * fun(b) > 0:
        return None, 0, None
    for k in range(max_iter):
        xk = a - (fun(a) * (a - b)) / (fun(a) - fun(b)) # calcula la formula de la secante

        if bolzano(fun, a, xk):  #  valida que se cumpla bolzano
            b = xk
        else:
            a = xk

        erk = abs(fun(xk))  # erk
        if erk < tol:  # Criterio de parada
            return xk, k + 1, erk

    return xk, k + 1, erk

#prueba del metodo

fp_raiz, fp_iteraciones, fp_error = falsa_posicion(fun, -0.3, -0.1, 1e-8, 10000)
print(fp_raiz,fp_iteraciones,fp_error)