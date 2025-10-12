import numpy as np


def bolzano(f, a, b):
    """
    Verifica si se cumple el teorema de Bolzano para una función en un intervalo.
    """
    return f(a) * f(b) < 0


def biseccion(fun, a, b, tol=1e-12, max_iter=10000):
    """
    Encuentra una raíz de la función utilizando el metodo de bisección.
    Versión compatible con el código de Octave.
    """
    if not bolzano(fun, a, b):
        print('No cumple el teorema de Bolzano')
        return 'N/A'

    for k in range(max_iter):
        xk = (a + b) / 2

        if bolzano(fun, a, xk):
            b = xk
        else:
            a = xk

        error = abs(fun(xk))
        if error < tol:
            return xk

    return xk


# Cálculo de valores propios
def p(x):
    return -x ** 3 + 2 * x ** 2 + 46 * x - 79


# Intervalo de Gershgorin
a = -11
b = 8

# Discretizar el intervalo
h = 1
x_val = np.arange(a, b + h, h)

vect_val_pro = []

for i in range(len(x_val) - 1):
    xi = x_val[i]
    xim1 = x_val[i + 1]
    if p(xi) * p(xim1) < 0:
        val_prop = biseccion(p, xi, xim1)
        if val_prop != 'N/A':
            vect_val_pro.append(val_prop)

print('Aproximación valores propios:')
print(vect_val_pro)

print('\nValores propios exactos:')
T2 = np.array([[1, 4, 0], [4, -2, -5], [0, -5, 3]])
valores_exactos = np.linalg.eigvals(T2)
print(valores_exactos)

# Mostrar los polinomios en cada subintervalo donde hay raíz
print('\nBúsqueda en subintervalos:')
for i in range(len(x_val) - 1):
    xi = x_val[i]
    xim1 = x_val[i + 1]
    if p(xi) * p(xim1) < 0:
        print(f'Raíz en [{xi:.1f}, {xim1:.1f}]: p({xi:.1f}) = {p(xi):.2f}, p({xim1:.1f}) = {p(xim1):.2f}')