import numpy as np

def ejemplo_qr():
    A = np.array([[5, 1, 1],
                  [1, 5, 1],
                  [1, 1, 5]], dtype=float)
    b = np.array([7, 7, 7], dtype=float)

    x = solve_qr(A, b)
    print("Solución del sistema Ax=b con QR:", x)


def solve_qr(A, b):
    # Descomposición QR con numpy
    Q, R = np.linalg.qr(A)

    # Paso intermedio
    y = Q.T @ b

    # Resolver con sustitución hacia atrás
    x = sust_atras(R, y)
    return x


def ejem_sust_atras():
    A = np.array([[1, 1, -1, 3],
                  [0, -1, -1, -5],
                  [0, 0, 3, 13],
                  [0, 0, 0, -13]], dtype=float)
    b = np.array([4, -7, 13, -13], dtype=float)

    x = sust_atras(A, b)
    print("Ejemplo sustitución hacia atrás:", x)


def sust_atras(A, b):
    n = len(b)
    x = np.zeros(n)

    # Recorremos desde la última ecuación hacia la primera
    for i in reversed(range(n)):
        suma = sum(A[i, j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - suma) / A[i, i]
    return x


if __name__ == "__main__":
    print("=== Ejemplo QR ===")
    solucion_qr = ejemplo_qr()

    print("\n=== Ejemplo Sustitución Atrás ===")
    solucion_sust = ejem_sust_atras()

    # Verificación adicional
    print("\n=== Verificación ===")
    A = np.array([[5, 1, 1], [1, 5, 1], [1, 1, 5]])
    b = np.array([7, 7, 7])
    x_calculado = solve_qr(A, b)
    print("Verificación Ax - b:", A @ x_calculado - b)
