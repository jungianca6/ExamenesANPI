import numpy as np

# Ejemplo metodo QR
A = np.array([[2, 2, 2, 1],
              [2, 0, 2, 0],
              [2, 2, 0, 2],
              [1, 0, 2, 2]])

iterMax = 1000
tol = 1e-10

#Verificacion
d = np.linalg.eig(A)[0]
print (d)

m = A.shape[0]  # #Filas de A
Im = np.eye(m)  # identidad

Ak = A.copy()
dk = np.diag(Ak)
Uk = np.eye(4)  # identidad

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

print("Valores propios (dk):")
print(dk)
print("\nVectores propios (columnas de Uk):")
print(Uk)
print("\nk:", k + 1)
print("erk:", erk)