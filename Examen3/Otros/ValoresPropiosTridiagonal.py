import numpy as np
import sympy as sp


def sturm_polinomio(T):
    """
    Calcula el polinomio característico usando la recurrencia de Sturm
    para una matriz tridiagonal simétrica
    """
    x = sp.Symbol('x')
    a = np.diag(T)
    b = np.diag(T, 1)
    m = len(a)

    p0 = 1
    p1 = a[0] - x

    for k in range(1, m):
        pk = (a[k] - x) * p1 - (b[k - 1]) ** 2 * p0
        p0 = p1
        p1 = pk

    polinomio = sp.expand(p1)
    return polinomio, x


def gershgorin_intervalos(T):
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


def biseccion(f, a, b, tol=1e-12, iterMax=10000):
    """
    Método de bisección para encontrar raíces
    """
    if f(a) * f(b) < 0:
        for k in range(iterMax):
            x = (a + b) / 2
            if f(a) * f(x) < 0:
                b = x
            else:
                a = x
            error = abs(f(x))
            if error < tol:
                break
        return x
    else:
        return None


def calcular_valores_propios(T, h=1):
    """
    Calcula todos los valores propios de una matriz tridiagonal
    integrando Sturm, Gershgorin y Bisección
    """
    print("=" * 60)
    print("CÁLCULO DE VALORES PROPIOS - MÉTODO INTEGRADO")
    print("=" * 60)

    # 1. Obtener polinomio característico (Sturm)
    print("\n1. POLINOMIO CARACTERÍSTICO (Sturm):")
    polinomio, x_sym = sturm_polinomio(T)
    print(f"P(x) = {polinomio}")

    # Convertir a función numérica
    p_func = sp.lambdify(x_sym, polinomio, 'numpy')

    # 2. Obtener intervalos (Gershgorin)
    print("\n2. INTERVALOS DE GERsHGORIN:")
    Ints, intervalo_global = gershgorin_intervalos(T)

    for i in range(len(Ints)):
        print(f"   Disco {i + 1}: [{Ints[i, 0]:.4f}, {Ints[i, 1]:.4f}]")

    print(f"\n   Intervalo global: [{intervalo_global[0]:.4f}, {intervalo_global[1]:.4f}]")

    # 3. Calcular valores propios (Bisección)
    print("\n3. CÁLCULO DE VALORES PROPIOS (Bisección):")
    a_global, b_global = intervalo_global

    # Discretizar el intervalo global
    x_val = np.arange(a_global, b_global + h, h)
    vect_val_pro = []

    print(f"   Buscando raíces en intervalo [{a_global:.4f}, {b_global:.4f}] con h = {h}")

    for i in range(len(x_val) - 1):
        xi = x_val[i]
        xim1 = x_val[i + 1]

        if p_func(xi) * p_func(xim1) < 0:
            val_prop = biseccion(p_func, xi, xim1)
            if val_prop is not None:
                vect_val_pro.append(val_prop)
                print(f"   ✓ Raíz encontrada en [{xi:.4f}, {xim1:.4f}] → {val_prop:.8f}")

    # Ordenar los valores propios
    vect_val_pro.sort()

    return vect_val_pro, polinomio


# =============================================================================
# EJEMPLOS DE USO
# =============================================================================

print("EJEMPLO 1: Matriz 3x3")
T1 = np.array([[1, 4, 0],
               [4, -2, -5],
               [0, -5, 3]])

valores_calculados1, pol1 = calcular_valores_propios(T1)
valores_exactos1 = np.linalg.eigvals(T1)
valores_exactos1.sort()

print(f"\nRESULTADOS - Matriz 3x3:")
print(f"Valores propios calculados: {[f'{v:.8f}' for v in valores_calculados1]}")
print(f"Valores propios exactos:    {[f'{v:.8f}' for v in valores_exactos1]}")

print("\n" + "=" * 60)
print("EJEMPLO 2: Matriz 5x5 (tridiagonal simétrica)")
T2 = np.array([[2, 1, 0, 0, 0],
               [1, 2, 1, 0, 0],
               [0, 1, 2, 1, 0],
               [0, 0, 1, 2, 1],
               [0, 0, 0, 1, 2]])

valores_calculados2, pol2 = calcular_valores_propios(T2, h=0.2)
valores_exactos2 = np.linalg.eigvals(T2)
valores_exactos2.sort()

print(f"\nRESULTADOS - Matriz 5x5:")
print(f"Valores propios calculados: {[f'{v:.8f}' for v in valores_calculados2]}")
print(f"Valores propios exactos:    {[f'{v:.8f}' for v in valores_exactos2]}")

print("\n" + "=" * 60)
print("EJEMPLO 3: Matriz 5x5 (no simétrica)")
T3 = np.array([[-5, 0.1, 0, 0, 0],
               [0.1, -5, 0.1, 0, 0],
               [0, 0.1, 0, 0.1, 0],
               [0, 0, 0.1, 5, 0.1],
               [0, 0, 0, 0.1, 5]])

valores_calculados3, pol3 = calcular_valores_propios(T3, h=0.5)
valores_exactos3 = np.linalg.eigvals(T3)
valores_exactos3.sort()

print(f"\nRESULTADOS - Matriz 5x5 no simétrica:")
print(f"Valores propios calculados: {[f'{v:.8f}' for v in valores_calculados3]}")
print(f"Valores propios exactos:    {[f'{v:.8f}' for v in valores_exactos3]}")

# =============================================================================
# VERIFICACIÓN DE PRECISIÓN
# =============================================================================
print("\n" + "=" * 60)
print("VERIFICACIÓN DE PRECISIÓN")
print("=" * 60)

matrices = [("3x3", T1, valores_calculados1, valores_exactos1),
            ("5x5 simétrica", T2, valores_calculados2, valores_exactos2),
            ("5x5 no simétrica", T3, valores_calculados3, valores_exactos3)]

for nombre, T, calculados, exactos in matrices:
    print(f"\nMatriz {nombre}:")
    if len(calculados) == len(exactos):
        for i, (calc, exac) in enumerate(zip(calculados, exactos)):
            error = abs(calc - exac)
            print(f"  λ{i + 1}: calc = {calc:.8f}, exact = {exac:.8f}, error = {error:.2e}")
    else:
        print(f"  ⚠️  No se encontraron todas las raíces ({len(calculados)}/{len(exactos)})")