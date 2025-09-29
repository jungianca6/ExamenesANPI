import numpy as np


def cholesky(A):
    """
    Factorización de Cholesky para matrices simétricas definidas positivas

    Parámetros:
    A: matriz simétrica definida positiva (n x n)

    Retorna:
    L: matriz triangular inferior tal que A = L * L^T
    """
    n = A.shape[0]
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                # Elementos de la diagonal: l_ii = sqrt(a_ii - sum(l_ik^2))
                sum_sq = sum(L[i][k] ** 2 for k in range(j))
                L[i][j] = np.sqrt(A[i][i] - sum_sq)
            else:
                # Elementos fuera de la diagonal: l_ij = (a_ij - sum(l_ik*l_jk)) / l_jj
                sum_prod = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (A[i][j] - sum_prod) / L[j][j]

    return L


def solve_cholesky(A, b):
    """
    Resuelve el sistema Ax = b usando factorización de Cholesky

    Parámetros:
    A: matriz simétrica definida positiva (n x n)
    b: vector término independiente (n)

    Retorna:
    x: solución del sistema (n)
    """
    # Paso 1: Factorización de Cholesky A = L * L^T
    L = cholesky(A)

    # Paso 2: Resolver Ly = b (sustitución hacia adelante)
    n = len(b)
    y = np.zeros(n)

    for i in range(n):
        sum_ly = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_ly) / L[i][i]

    # Paso 3: Resolver L^T x = y (sustitución hacia atrás)
    x = np.zeros(n)
    L_T = L.T  # L transpuesta

    for i in range(n - 1, -1, -1):
        sum_LTx = sum(L_T[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - sum_LTx) / L_T[i][i]

    return x


def is_symmetric_positive_definite(A):
    """
    Verifica si una matriz es simétrica y definida positiva
    """
    # Verificar simetría
    if not np.allclose(A, A.T):
        return False, "La matriz no es simétrica"

    # Verificar definida positiva (autovalores > 0)
    eigenvalues = np.linalg.eigvals(A)
    if np.all(eigenvalues > 0):
        return True, "Matriz simétrica definida positiva"
    else:
        return False, f"Matriz simétrica pero no definida positiva. Autovalores: {eigenvalues}"


# EJEMPLO DEL PDF
def ejemplo_pdf():
    """Ejemplo del PDF página 6"""
    print("=== EJEMPLO DEL PDF ===")

    # Matriz del ejemplo
    A = np.array([
        [25, 15, -5, -10],
        [15, 10, 1, -7],
        [-5, 1, 21, 4],
        [-10, -7, 4, 18]
    ], dtype=float)

    # Vector b del ejemplo
    b = np.array([-25, -19, -21, -5], dtype=float)

    print("Matriz A:")
    print(A)
    print("\nVector b:", b)

    # Verificar si es simétrica definida positiva
    es_spd, mensaje = is_symmetric_positive_definite(A)
    print(f"\nVerificación: {mensaje}")

    if es_spd:
        # Calcular factorización de Cholesky
        L = cholesky(A)
        print("\nMatriz L (Cholesky):")
        print(L)

        # Verificar que A = L * L^T
        A_reconstruida = L @ L.T
        print("\nVerificación A = L * L^T:")
        print("¿Son iguales?", np.allclose(A, A_reconstruida))

        # Resolver el sistema
        x = solve_cholesky(A, b)
        print(f"\nSolución x: {x}")

        # Verificar solución
        b_calculado = A @ x
        print("Verificación Ax = b:")
        print(f"b original: {b}")
        print(f"b calculado: {b_calculado}")
        print("¿Son iguales?", np.allclose(b, b_calculado))


# PRUEBA CON MATRIZ ALEATORIA
def prueba_aleatoria():
    """Prueba con una matriz aleatoria simétrica definida positiva"""
    print("\n\n=== PRUEBA CON MATRIZ ALEATORIA ===")

    # Generar matriz aleatoria simétrica definida positiva
    n = 4
    B = np.random.rand(n, n)
    A_aleatoria = B @ B.T + np.eye(n)  # Hacerla definida positiva

    b_aleatorio = np.random.rand(n)

    print("Matriz aleatoria A:")
    print(A_aleatoria)
    print("\nVector b aleatorio:", b_aleatorio)

    # Resolver con Cholesky
    x_cholesky = solve_cholesky(A_aleatoria, b_aleatorio)

    # Resolver con numpy para comparar
    x_numpy = np.linalg.solve(A_aleatoria, b_aleatorio)

    print(f"\nSolución con Cholesky: {x_cholesky}")
    print(f"Solución con NumPy:    {x_numpy}")
    print("¿Soluciones iguales?", np.allclose(x_cholesky, x_numpy))


if __name__ == "__main__":
    ejemplo_pdf()
    prueba_aleatoria()