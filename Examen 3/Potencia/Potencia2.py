import numpy as np


# Método de la potencia
def potencia(A, x0=None, iterMax=100, tol=1e-8):
    n = A.shape[0]
    if x0 is None:
        x0 = np.random.rand(n, 1)

    xk = x0.copy()
    for k in range(iterMax):
        yk = A @ xk
        alphak = np.linalg.norm(yk, ord=np.inf)
        xk = yk / alphak
        erk = np.linalg.norm(A @ xk - alphak * xk, ord=np.inf)
        if erk < tol:
            break

    return alphak, xk, k + 1, erk


# Ejemplo de uso
A = np.array([[4, 1, 1], [1, 3, 0], [1, 0, 2]])
d = np.linalg.eig(A)[0]
print("Valores propios:", d)

alphak, xk, iteraciones, error = potencia(A)
print("\nResultados:")
print("alphak:", alphak)
print("xk:", xk.flatten())
print("Iteraciones:", iteraciones)
print("Error:", error)