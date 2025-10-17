import numpy as np


def metodo_euler(f, a, b, y0, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0

    for k in range(n):
        y[k + 1] = y[k] + h * f(x[k], y[k])

    return x, y