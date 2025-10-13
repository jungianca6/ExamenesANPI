import numpy as np


def biseccion(f, a, b):
    """
    Método de bisección para encontrar raíces
    f = una función f
    a,b son los extremos del intervalo [a,b]
    """
    tol = 1e-12
    iterMax = 10000

    if f(a) * f(b) < 0:  # Paso 1
        for k in range(iterMax):
            x = (a + b) / 2  # Paso 2: Dos intervalos [a,x] y [x,b]
            if f(a) * f(x) < 0:  # Paso 3
                b = x
            else:  # f(x)*f(b)<0
                a = x
            error = abs(f(x))
            if error < tol:  # Paso 4
                break
        return x
    else:
        print('No cumple el teorema de Bolzano')
        return 'N/A'


# Cálculo de los valores propios de la matriz
# T2 = [[1, 4, 0], [4, -2, -5], [0, -5, 3]]
# usando el método de la bisección

# Polinomio Característico (Sturm)
def p(x):
    return -x ** 3 + 2 * x ** 2 + 46 * x - 79


# Intervalo donde se encuentran los valores propios (Gershgorin)
a = -11
b = 8

# Discretizar el intervalo [-11,8]
h = 1
x_val = np.arange(a, b + h, h)

n = len(x_val)

vect_val_pro = []

for i in range(n - 1):
    # Preguntar si se cumple el teorema de Bolzano
    xi = x_val[i]
    xim1 = x_val[i + 1]
    if p(xi) * p(xim1) < 0:
        val_prop = biseccion(p, xi, xim1)
        vect_val_pro.append(val_prop)

print('Aproximación valores propios')
print(vect_val_pro)

print('\nValores propios exactos')
T2 = np.array([[1, 4, 0], [4, -2, -5], [0, -5, 3]])
valores_exactos = np.linalg.eigvals(T2)
print(valores_exactos)

# Verificación de la precisión
print('\nComparación:')
for i, (aprox, exacto) in enumerate(zip(sorted(vect_val_pro), sorted(valores_exactos))):
    print(f'Valor propio {i + 1}: Aprox = {aprox:.10f}, Exacto = {exacto:.10f}, Error = {abs(aprox - exacto):.2e}')