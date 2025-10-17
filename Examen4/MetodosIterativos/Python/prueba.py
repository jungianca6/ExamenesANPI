import numpy as np

m = 100

# Índices desde 1 hasta 100
i = np.arange(1, m+1).reshape(-1, 1)  # columna (100x1)
j = np.arange(1, m+1)                 # fila (1x100)
print(i)
print(j)

# Construcción de C
C = i / (j + 1)**2

# Matriz identidad
I = np.eye(m)

# Construcción de A
A = (10**-2) * C + 3 * I

print(A)
