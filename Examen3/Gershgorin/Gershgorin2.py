import numpy as np


def gershgorin_intervals(T):
    """
    Calcula los intervalos de Gershgorin para una matriz tridiagonal
    """
    m = T.shape[0]
    Ints = np.zeros((m, 2))

    # Primer fila
    R1 = abs(T[0, 1])
    Ints[0, 0] = T[0, 0] - R1
    Ints[0, 1] = T[0, 0] + R1

    # Última fila
    Rm = abs(T[m - 1, m - 2])
    Ints[m - 1, 0] = T[m - 1, m - 1] - Rm
    Ints[m - 1, 1] = T[m - 1, m - 1] + Rm

    # Filas intermedias
    for k in range(1, m - 1):
        Rk = abs(T[k, k - 1]) + abs(T[k, k + 1])
        Ints[k, 0] = T[k, k] - Rk
        Ints[k, 1] = T[k, k] + Rk

    intervalo_global = [np.min(Ints[:, 0]), np.max(Ints[:, 1])]

    return Ints, intervalo_global


# Ejemplo de uso
T2 = np.array([[-5, 0.1, 0, 0, 0],
               [0.1, -5, 0.1, 0, 0],
               [0, 0.1, 0, 0.1, 0],
               [0, 0, 0.1, 5, 0.1],
               [0, 0, 0, 0.1, 5]])

print("Matriz T2:")
print(T2)

Ints, intervalo_global = gershgorin_intervals(T2)

print("\nIntervalos de Gershgorin:")
for i in range(len(Ints)):
    print(f"Disco {i + 1}: [{Ints[i, 0]:.4f}, {Ints[i, 1]:.4f}]")

print(f"\nIntervalo global: [{intervalo_global[0]:.4f}, {intervalo_global[1]:.4f}]")

# Verificación con valores propios reales
valores_propios = np.linalg.eigvals(T2)
print(f"\nValores propios reales: {np.sort(valores_propios)}")
print("Todos los valores propios están dentro de los intervalos de Gershgorin:",
      all(intervalo_global[0] <= vp <= intervalo_global[1] for vp in valores_propios))