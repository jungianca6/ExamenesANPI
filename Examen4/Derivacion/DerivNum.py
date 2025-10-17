import sympy as sp
import numpy as np

def dif_adel(f, a, h, tol, iterMax):
    h0 = h(0)
    A0 = (f(a + h0) - f(a)) / h0
    Ak = A0
    for k in range(1, iterMax):  # Cambio importante: empezar desde 1
        hk = h(k)
        AK_N = (f(a + hk) - f(a)) / hk
        erk = abs(AK_N - Ak)
        Ak = AK_N
        if erk < tol:
            return Ak, erk, k
    return Ak, erk, iterMax

def dif_cent(f, a, h, tol, iterMax):
    h0 = h(0)
    A0 = (f(a + h0) - f(a - h0)) / (2 * h0)
    Ak = A0
    for k in range(1, iterMax):  # Cambio importante: empezar desde 1
        hk = h(k)
        AK_N = (f(a + hk) - f(a - hk)) / (2 * hk)
        erk = abs(AK_N - Ak)
        Ak = AK_N
        if erk < tol:
            return Ak, erk, k
    return Ak, erk, iterMax

# Definir la función y parámetros
x = sp.symbols('x')
k = sp.symbols('k')
f_expr = sp.sin(x) * x + sp.exp(-2 * x)
h_expr = 1 / (2 ** k)

f = sp.lambdify(x, f_expr, 'numpy')
h_func = sp.lambdify(k, h_expr, 'numpy')  # Cambio de nombre para evitar conflicto

a = 2
tol = 1e-10
iterMax = 1000

# Calcular derivadas
A1, erk1, k1 = dif_adel(f, a, h_func, tol, iterMax)
print("Aproximación hacia adelante")
print("Derivada:", A1)
print("Error:", erk1)
print("Iteraciones:", k1)

A2, erk2, k2 = dif_cent(f, a, h_func, tol, iterMax)
print("\nAproximación hacia el centro")
print("Derivada:", A2)
print("Error:", erk2)
print("Iteraciones:", k2)

# Verificación con derivada exacta
f_prime_expr = sp.diff(f_expr, x)
f_prime = sp.lambdify(x, f_prime_expr, 'numpy')
derivada_exacta = f_prime(a)
print(f"\nDerivada exacta en x={a}: {derivada_exacta}")





