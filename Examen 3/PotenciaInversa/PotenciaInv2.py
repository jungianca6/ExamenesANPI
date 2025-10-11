import numpy as np


# Método de la potencia inversa
def potencia_inversa(A, x0=None, iterMax=1000, tol=1e-8):
    n = A.shape[0]
    if x0 is None:
        x0 = np.ones((n, 1))

    xk = x0.copy()
    for k in range(iterMax):
        yk = np.linalg.solve(A, xk)  # yk = A^-1 * xk
        alphak = np.linalg.norm(yk, ord=np.inf)
        xk = yk / alphak
        erk = np.linalg.norm(xk / alphak - A @ xk, ord=np.inf)
        if erk < tol:
            break

    valor_propio = 1 / alphak
    return valor_propio, xk, k + 1, erk


# Ejemplo de uso
A = np.array([[4, 1, 1], [1, 3, 0], [1, 0, 2]])
d = np.linalg.eig(A)[0]
print("Valores propios:", d)

valor_propio, xk, iteraciones, error = potencia_inversa(A)
print("\nResultados:")
print("Valor propio:", valor_propio)
print("Vector propio:", xk.flatten())
print("Iteraciones:", iteraciones)
print("Error:", error)