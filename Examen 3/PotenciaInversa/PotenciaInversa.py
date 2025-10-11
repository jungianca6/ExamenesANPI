import numpy as np

# Ejemplo del método de la potencia inversa
A = np.array([[4, 1, 1], [1, 3, 0], [1, 0, 2]])
d = np.linalg.eig(A)[0]  # Valores propios
print("Valores propios:", d)

x0 = np.array([[1], [1], [1]])  # Valor inicial [1,1,1]'
xk = x0.copy()
iterMax = 1000
tol = 1e-8

for k in range(iterMax):
    yk = np.linalg.solve(A, xk)  # Equivalente a mldivide(A,xk) - Resuelve yk = A^-1 * xk
    alphak = np.linalg.norm(yk, ord=np.inf)
    xk = (1/alphak) * yk
    erk = np.linalg.norm((1/alphak) * xk - A @ xk, ord=np.inf)
    if erk < tol:
        break

print("\nResultados:")
print("Valor propio (1/alphak):", 1/alphak)
print("xk:", xk.flatten())
print("k:", k + 1)
print("erk:", erk)