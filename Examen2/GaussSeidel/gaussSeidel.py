import numpy as np


def sustitucion_atras(U, b):
    """
    Resuelve el sistema Ux = b donde U es triangular superior
    usando sustitución hacia atrás
    """
    n = len(b)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        suma = 0.0
        for j in range(i + 1, n):
            suma += U[i, j] * x[j]
        x[i] = (b[i] - suma) / U[i, i]

    return x


def gauss_seidel_profesor(A, b, x0, tol=1e-10, iterMax=1000):
    """
    Implementación EXACTA del método Gauss-Seidel según el pseudocódigo del profesor

    Parámetros:
    A: matriz del sistema
    b: vector término independiente
    x0: vector inicial
    tol: tolerancia
    iterMax: máximo de iteraciones

    Retorna:
    x: solución aproximada
    err: error final
    k: iteraciones realizadas
    """
    n = A.shape[0]

    # P1: Calcular L, D, U tales que A = L + D + U
    L = np.tril(A, -1)  # Triangular inferior estricta (sin diagonal)
    D = np.diag(np.diag(A))  # Matriz diagonal
    U = np.triu(A, 1)  # Triangular superior estricta (sin diagonal)

    # P2: M = D + U (matriz triangular superior)
    M = D + U

    # P3: Calcular d = M^(-1)*b resolviendo M*d = b con sustitución hacia atrás
    d = sustitucion_atras(M, b)

    # P4: Bucle de iteraciones
    x = x0.copy()

    for k in range(iterMax):
        # P5: y^(k) = -L * x^(k)
        y = -L @ x

        # P6: Calcular z^(k) = M^(-1) * y^(k) resolviendo M*z^(k) = y con sustitución hacia atrás
        z = sustitucion_atras(M, y)

        # P7: x^(k+1) = z^(k) + d
        x_new = z + d

        # P8: err_k = ||A * x^(k+1) - b|| / ||b||
        err = np.linalg.norm(A @ x_new - b) / np.linalg.norm(b)

        # P9: Si err < tol, retornar y salir
        if err < tol:
            print(f"Convergió en {k + 1} iteraciones")
            return x_new, err, k + 1

        x = x_new

    print(f"Alcanzó máximo de iteraciones: {iterMax}")
    return x, err, iterMax


# Versión alternativa usando np.linalg.solve (más eficiente para verificación)
def gauss_seidel_profesor_solve(A, b, x0, tol=1e-10, iterMax=1000):
    """
    Misma implementación pero usando solve para verificar que la lógica es correcta
    """
    n = A.shape[0]

    # P1: Descomposición
    L = np.tril(A, -1)
    D = np.diag(np.diag(A))
    U = np.triu(A, 1)

    # P2: M = D + U
    M = D + U

    # P3: Calcular d = M^(-1)*b
    d = np.linalg.solve(M, b)

    # P4: Bucle de iteraciones
    x = x0.copy()

    for k in range(iterMax):
        # P5: y^(k) = -L * x^(k)
        y = -L @ x

        # P6: Calcular z^(k) = M^(-1) * y^(k)
        z = np.linalg.solve(M, y)

        # P7: x^(k+1) = z^(k) + d
        x_new = z + d

        # P8: Error relativo
        err = np.linalg.norm(A @ x_new - b) / np.linalg.norm(b)

        # P9: Verificar convergencia
        if err < tol:
            print(f"Convergió en {k + 1} iteraciones (usando solve)")
            return x_new, err, k + 1

        x = x_new

    print(f"Alcanzó máximo de iteraciones: {iterMax}")
    return x, err, iterMax


# EJEMPLO DE USO
if __name__ == "__main__":
    # Sistema de ejemplo (diagonalmente dominante para garantizar convergencia)
    A = np.array([
        [4.0, 1.0, 1.0],
        [1.0, 5.0, 2.0],
        [1.0, 2.0, 6.0]
    ])

    b = np.array([7.0, 8.0, 9.0])
    x0 = np.zeros(3)  # Vector inicial

    print("=== MÉTODO GAUSS-SEIDEL (PROFESOR) ===")
    print("Matriz A:")
    print(A)
    print(f"\nVector b: {b}")
    print(f"Vector inicial x0: {x0}")

    # Resolver con implementación del profesor
    x1, err1, iter1 = gauss_seidel_profesor(A, b, x0)
    print(f"\n--- Con sustitución hacia atrás ---")
    print(f"Solución: {x1}")
    print(f"Error: {err1:.2e}")
    print(f"Iteraciones: {iter1}")

    # Resolver con solve para verificación
    x2, err2, iter2 = gauss_seidel_profesor_solve(A, b, x0)
    print(f"\n--- Con np.linalg.solve (verificación) ---")
    print(f"Solución: {x2}")
    print(f"Error: {err2:.2e}")
    print(f"Iteraciones: {iter2}")

    # Solución exacta para comparación
    x_exacta = np.linalg.solve(A, b)
    print(f"\n--- Solución exacta (np.linalg.solve) ---")
    print(f"Solución: {x_exacta}")

    # Verificar diferencias
    print(f"\nDiferencias:")
    print(f"Implementación vs exacta: {np.linalg.norm(x1 - x_exacta):.2e}")
    print(f"Solve vs exacta: {np.linalg.norm(x2 - x_exacta):.2e}")
    print(f"Entre implementaciones: {np.linalg.norm(x1 - x2):.2e}")