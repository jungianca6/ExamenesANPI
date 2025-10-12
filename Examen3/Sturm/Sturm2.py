import sympy as sp
import numpy as np


# Método de Sturm para polinomio característico de matriz tridiagonal
def sturm_tridiagonal(T):
    x = sp.Symbol('x')

    a = np.diag(T)
    b = np.diag(T, 1)
    m = len(a)

    # Secuencia de Sturm
    polinomios = []
    p0 = 1
    p1 = a[0] - x
    polinomios.append(p0)
    polinomios.append(p1)

    for k in range(1, m):
        pk = (a[k] - x) * p1 - (b[k - 1]) ** 2 * p0
        polinomios.append(pk)
        p0 = p1
        p1 = pk

    polinomio_caracteristico = sp.expand(pk)
    return polinomio_caracteristico, polinomios


# Ejemplo de uso
T = np.array([[2, 1, 0, 0, 0],
              [1, 2, 1, 0, 0],
              [0, 1, 2, 1, 0],
              [0, 0, 1, 2, 1],
              [0, 0, 0, 1, 2]])

print("Matriz T:")
print(T)

pol_caract, secuencia = sturm_tridiagonal(T)

print("\nSecuencia de Sturm:")
for i, p in enumerate(secuencia):
    print(f"p{i} = {p}")

print(f"\nPolinomio característico expandido:")
print(pol_caract)

# Convertir a función numérica
fdn = sp.lambdify(sp.Symbol('x'), pol_caract, 'numpy')
print(f"\nEvaluación del polinomio en varios puntos:")
for val in [0, 1, 2, 3]:
    print(f"P({val}) = {fdn(val)}")