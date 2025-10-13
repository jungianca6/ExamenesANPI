import numpy as np


# Método QR para valores y vectores propios
def metodo_qr(A, iterMax=1000, tol=1e-10):
    m = A.shape[0]
    Ak = A.copy()
    Uk = np.eye(m)
    dk = np.diag(Ak)

    for k in range(iterMax):
        Qk, Rk = np.linalg.qr(Ak)
        Ak = Rk @ Qk
        Uk = Uk @ Qk
        dkN = np.diag(Ak)
        erk = np.linalg.norm(dkN - dk)
        if erk < tol:
            dk = dkN
            break
        dk = dkN

    return dk, Uk, k + 1, erk


# Ejemplo de uso
A = np.array([[2, 2, 2, 1],
              [2, 0, 2, 0],
              [2, 2, 0, 2],
              [1, 0, 2, 2]])

valores_propios, vectores_propios, iteraciones, error = metodo_qr(A)

print("Valores propios:")
print(valores_propios)
print("\nVectores propios (columnas):")
print(vectores_propios)
print("\nIteraciones:", iteraciones)
print("Error:", error)

# Verificación con numpy
print("\nVerificación con numpy.linalg.eig:")
valores_np, vectores_np = np.linalg.eig(A)
print("Valores propios numpy:", valores_np)
print("Vectores propios numpy:")
print(vectores_np)