import numpy as np

# Matriz T2
T2 = np.array([[-5,   0.1,  0,    0,    0],
               [0.1, -5,   0.1,  0,    0],
               [0,    0.1,  0,    0.1,  0],
               [0,    0,    0.1,  5,    0.1],
               [0,    0,    0,    0.1,  5]])

m = T2.shape[0]

Ints = np.zeros((m, 2))  # Las filas van a representar los extremos de los intervalos

# Primer intervalo (k=1)
R1 = abs(T2[0, 1])
Ints[0, 0] = T2[0, 0] - R1
Ints[0, 1] = T2[0, 0] + R1

# Último intervalo (k=m)
Rm = abs(T2[m-1, m-2])
Ints[m-1, 0] = T2[m-1, m-1] - Rm
Ints[m-1, 1] = T2[m-1, m-1] + Rm

# Intervalos intermedios (k=2 hasta m-1)
for k in range(1, m-1):  # k=1,2,3 cuando m=5
    Rk = abs(T2[k, k-1]) + abs(T2[k, k+1])
    Ints[k, 0] = T2[k, k] - Rk
    Ints[k, 1] = T2[k, k] + Rk

print("Intervalos de Gershgorin:")
print(Ints)

Intervalo = [np.min(Ints[:, 0]), np.max(Ints[:, 1])]
print("\nIntervalo global:")
print(Intervalo[0], Intervalo[1])
print(Intervalo)