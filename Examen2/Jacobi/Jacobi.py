import numpy as np


def sol_Jacobi(A, b):
    """
    Resuelve el sistema Ax = b usando el método de Jacobi

    Parámetros:
    A: matriz cuadrada del sistema
    b: vector término independiente

    Retorna:
    xk: solución aproximada del sistema
    """
    tol = 1e-10
    iterMax = 1000
    m = len(b)
    xk = np.zeros(m)  # Vector inicial

    # Paso 1: Extraer diagonal principal
    d1 = np.diag(A)
    D = np.diag(d1)

    # Paso 2: Inversa de la matriz diagonal
    Dinv = np.diag(1.0 / d1)

    # Paso 3: Matriz L + U (A - D)
    LmU = A - D

    # Paso 4: Término independiente transformado
    d = Dinv @ b

    # Paso 5: Matriz de iteración T
    T = -Dinv @ LmU

    # Paso 6: Iteraciones
    for k in range(iterMax):
        # Paso 7: Actualizar solución
        xk = T @ xk + d

        # Paso 8: Calcular error residual
        er = np.linalg.norm(A @ xk - b)

        # Paso 9: Verificar convergencia
        if er < tol:
            print(f"Convergió en {k + 1} iteraciones")
            break

    return xk


# Versión más eficiente (sin crear matrices completas)
def sol_Jacobi_eficiente(A, b):
    """
    Versión más eficiente del método de Jacobi
    Evita crear matrices completas D, Dinv, LmU, T
    """
    tol = 1e-10
    iterMax = 1000
    m = len(b)
    xk = np.zeros(m)  # Vector inicial
    xk_nuevo = np.zeros(m)  # Para la nueva iteración

    # Extraer diagonal principal
    d1 = np.diag(A)

    for k in range(iterMax):
        # Actualizar cada componente
        for i in range(m):
            suma = 0.0
            for j in range(m):
                if i != j:
                    suma += A[i, j] * xk[j]
            xk_nuevo[i] = (b[i] - suma) / d1[i]

        # Actualizar solución
        xk = xk_nuevo.copy()

        # Calcular error residual
        er = np.linalg.norm(A @ xk - b)

        # Verificar convergencia
        if er < tol:
            print(f"Convergió en {k + 1} iteraciones")
            break

    return xk


# EJEMPLO DE USO
if __name__ == "__main__":
    # Sistema de ejemplo (diagonalmente dominante para garantizar convergencia)
    A = np.array([
        [4.0, 1.0, 1.0],
        [1.0, 5.0, 2.0],
        [1.0, 2.0, 6.0]
    ])

    b = np.array([7.0, 8.0, 9.0])

    print("Matriz A:")
    print(A)
    print("\nVector b:", b)

    # Resolver con Jacobi (versión matricial)
    print("\n--- Método de Jacobi (versión matricial) ---")
    x1 = sol_Jacobi(A, b)
    print(f"Solución: {x1}")
    print(f"Error: {np.linalg.norm(A @ x1 - b)}")

    # Resolver con Jacobi (versión eficiente)
    print("\n--- Método de Jacobi (versión eficiente) ---")
    x2 = sol_Jacobi_eficiente(A, b)
    print(f"Solución: {x2}")
    print(f"Error: {np.linalg.norm(A @ x2 - b)}")

    # Comparar con solución de numpy
    print("\n--- Solución NumPy (referencia) ---")
    x_ref = np.linalg.solve(A, b)
    print(f"Solución: {x_ref}")
    print(f"Error: {np.linalg.norm(A @ x_ref - b)}")

    # Verificar diferencias
    print(f"\nDiferencia entre versiones: {np.linalg.norm(x1 - x2)}")
    print(f"Diferencia con NumPy: {np.linalg.norm(x1 - x_ref)}")