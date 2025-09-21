import math
import numpy as np
import sympy as sp
from scipy.optimize import fsolve


def fun(x):
    """
    Evalúa la función f(x) = x*e^(-x) - 5 - (cos(x)/x) en un punto dado.

    Parámetros:
        x : float
            Punto en el que evaluar la función

    Retorna:
            float: Valor de la función en x, o infinito si x = 0
    """
    return ((x - 3) * np.exp(x - 3) + 2) / 2




def unicidad_pf(fun,a,b):
    x = sp.symbols('x')  # Variable simbólica
    fs = ((x - 3) * sp.exp(x - 3) + 2) / 2  # Función simbólica para derivar


    dfs = sp.diff(fs, x)
    dfs2= sp.diff(dfs, x)
    dfn = sp.lambdify(x, dfs, 'numpy')
    dfn2 = sp.lambdify(x, dfs2, 'numpy')

    #Teorema de Existencia

    # Encontrar puntos críticos de f(x) en [a,b] (cuando f'(x)=0)
    try:
        xsol = fsolve(dfn, (a + b) / 2)[0]  # Similar a fzero en Octave
        # Verificar que la solución esté en el intervalo
        if not (a <= xsol <= b):
            xsol = (a + b) / 2  # Si no está, usar punto medio
    except:
        xsol = (a + b) / 2  # En caso de error, usar punto medio

    #Puntos criticos y extremos
    crit=fun(xsol)
    fa=fun(a)
    fb=fun(b)

    if a <= fa <= b and a <= fb <= b:
        print('f(x) tiene al menos un punto fijo en [a,b] \n')
        existencia = True
    else:
        print('No se cumple el teorema de existencia \n')
        existencia = False


    #Teorema de Unicidad

    if existencia:
        # Encontrar puntos críticos de f'(x) en [a,b] (cuando f''(x)=0)
        try:
            xsol2 = fsolve(dfn2, (a + b) / 2)[0]  # Similar a fzero en Octave
            # Verificar que la solución esté en el intervalo
            if not (a <= xsol2 <= b):
                xsol2 = (a + b) / 2  # Si no está, usar punto medio
        except:
            xsol2 = (a + b) / 2  # En caso de error, usar punto medio

        critfd=fun(xsol2)
        fda=dfn(a)
        fdb=dfn(b)

        if -1 <= fda <= 1 and -1 <= fdb <= 1:
            print('f(x) tiene al menos un punto fijo en [a,b] \n')
            unicidad = 1
        else:
            print('No se cumple el teorema de existencia \n')
            unicidad = 0

    else:
        print('No se cumple el teorema de existencia \n')
        unicidad = 0

    return unicidad


def main():
    a = 0
    b = 7/3

    return unicidad_pf(fun,a,b)

c=main()
print(c)


