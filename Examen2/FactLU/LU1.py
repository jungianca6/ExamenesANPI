import numpy as np


def factorizacion_LU(A):
    """
    Factorización LU con manejo básico de errores
    """
    n = len(A)
    L = np.zeros((n, n))
    U = np.copy(A).astype(float)

    for i in range(n):
        # Verificar que el pivote no sea cero
        if abs(U[i, i]) < 1e-12:
            raise ValueError(f"Pivote cero en posición ({i},{i}). Se requiere pivoteo.")

        L[i, i] = 1.0
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            for k in range(i, n):
                U[j, k] -= factor * U[i, k]

    return L, U


def sust_adelante(L, b):
    """
    Sustitución hacia adelante: L y = b
    """
    n = len(L)
    y = np.zeros_like(b, dtype=float)

    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i, j] * y[j]
        y[i] /= L[i, i]  # ¡IMPORTANTE!

    return y


def sust_atras(U, y):
    """
    Sustitución hacia atrás: U x = y
    """
    n = len(U)
    x = np.zeros_like(y, dtype=float)

    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]

    return x


def resolver_LU(A, b):
    """
    Resuelve Ax = b usando factorización LU
    """
    L, U = factorizacion_LU(A)
    y = sust_adelante(L, b)
    x = sust_atras(U, y)
    return x


# PRUEBA COMPLETA
A = np.array([[3, 2, 3], [1, 3, 1], [5, 1, 3]]).astype(float)
b = np.array([10, 8, 12]).astype(float)

print("Matriz A:")
print(A)

L, U = factorizacion_LU(A)
print("\nMatriz L:")
print(L)
print("\nMatriz U:")
print(U)
print("\nVerificación L*U:")
print(np.dot(L, U))
print("\n¿L*U = A?", np.allclose(np.dot(L, U), A))

# Resolver sistema
x = resolver_LU(A, b)
print(f"\nSolución x: {x}")
print(f"Verificación Ax = b: {np.dot(A, x)}")
print(f"¿Ax = b? {np.allclose(np.dot(A, x), b)}")