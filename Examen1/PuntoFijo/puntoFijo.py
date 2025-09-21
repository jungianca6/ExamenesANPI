import numpy as np

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


def main():
    # Ejemplo aproximar punto fijo
    # usando el metodo iterativo

    #f = '((x-3)*np.exp(x-2))/2+2'
    x0 = 1  # x0 en [0,7/3]
    #fn = eval(f'lambda x: {f}')  # Equivalente a str2func en Octave

    iterMax = 100
    tol = 1e-10
    xk = x0

    for k in range(1, iterMax + 1):
        xkN = fun(xk)
        er = abs(xkN - xk)
        if er < tol:
            xk = xkN
            break
        xk = xkN

    print("xk =", xk)
    print("k =", k)
    print("er =", er)


if __name__ == "__main__":
    main()