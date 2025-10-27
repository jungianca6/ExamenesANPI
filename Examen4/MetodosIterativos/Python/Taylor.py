import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def taylor(f,a,b,y0,n,p):

    x, y = sp.symbols('x,y')
    fsym = f(x,y)


    derivs = [0] * p
    derivs[0] = fsym

    for k in range(1, p):
        derivs[k] = sp.diff(derivs[k - 1],x) + (sp.diff(derivs[k - 1],y)*fsym)

    funcs = [0] * p
    for k in range(p):
        funcs[k] = sp.lambdify((x,y), derivs[k], 'numpy')


    h = (b - a) / n
    X = np.linspace(a, b, n + 1)
    Y = np.zeros(n + 1)

    Y[0] = y0

    for k in range(n):
        suma = 0
        for i in range(p):
            suma = suma + (h**(i+1)/sp.factorial(i+1)) * funcs[i](X[k], Y[k])

        Y[k+1] = Y[k] + suma
    return X,Y

def f(x, y):
    return x + y

# Parámetros
a = 0
b = 1
y0 = 1
n = 50
p = 2

# Calcular solución con Euler
x, y_aprox = taylor(f, a, b, y0, n, p)

print("Puntos x:", x)
print("Aproximación y:", y_aprox)

# Gráfica de la solución exacta
x_exact = np.linspace(a, b, 1000)  # Equivalente a a:0.0001:b
y_exact = 2 * np.exp(x_exact) - x_exact - 1  # Solución exacta de y' = x + y

# Crear la gráfica
plt.figure(figsize=(10, 6))

# Graficar solución exacta (línea azul)
plt.plot(x_exact, y_exact, 'b', label='Solución exacta: $y = 2e^x - x - 1$', linewidth=2)

# Graficar solución aproximada (stem plot rojo)
plt.stem(x, y_aprox, linefmt='r-', markerfmt='ro', basefmt=' ', label='Método de Taylor')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de EDO: $y\' = x + y$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()