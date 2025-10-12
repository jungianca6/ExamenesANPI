import sympy as sp
import numpy as np
from scipy.optimize import fsolve

# Ejemplo Recurrencia de Sturm

# Definir la variable simbólica
x = sp.symbols('x')

# Matriz tridiagonal simétrica
T = np.array([[2, 1, 0, 0, 0],
              [1, 2, 1, 0, 0],
              [0, 1, 2, 1, 0],
              [0, 0, 1, 2, 1],
              [0, 0, 0, 1, 2]])

a = np.diag(T)
b = np.diag(T, 1)  # b = diag(T,1) y como T es simétrica, b = diag(T,-1) sería igual

m = len(a)

p0 = 1
p1 = a[0] - x

for k in range(1, m):
    pk = (a[k] - x) * p1 - (b[k-1])**2 * p0
    p0 = p1
    p1 = pk

z = sp.expand(pk)
print("Polinomio característico expandido:")
print(z)


# Convertir a función numérica
fdn = sp.lambdify(x, z, 'numpy')
print("\nFunción numérica creada correctamente")


# Ejemplo de evaluación
print(f"\nEvaluación en x=0: {fdn(0)}")
print(f"Evaluación en x=1: {fdn(1)}")