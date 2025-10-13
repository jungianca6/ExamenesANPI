import numpy as np

# Ejemplo del método de la potencia
A = np.array([[4, 1, 1], [1, 3, 0], [1, 0, 2]])
d = np.linalg.eig(A)[0]  # Valores propios
print("Valores propios:", d)

x0 = np.random.rand(3, 1)  # Valor inicial (puede ser cualquier valor inicial como [1,1,1]'. Es solo para el ejemplo
xk = x0.copy()
iterMax = 100
tol = 1e-8

for k in range(iterMax):
    yk = A @ xk
    alphak = np.linalg.norm(yk, ord=np.inf)
    xk = (1/alphak) * yk
    erk = np.linalg.norm(A @ xk - alphak * xk, ord=np.inf)
    if erk < tol:
        break

print("\nResultados:")
print("alphak:", alphak)
print("xk:", xk.flatten())
print("k:", k + 1)
print("erk:", erk)