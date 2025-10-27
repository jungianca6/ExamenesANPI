import numpy as np
from matplotlib import pyplot as plt


def adams4(f,a,b,y0,n):
    h = (b-a)/n
    x= np.linspace(a,b,n+1)
    y = np.zeros(n+1)

    y[0]= y0

    for k in range(0,3):
        K1 = f(x[k],y[k])
        K2 = f(x[k]+h/2,y[k]+(h/2)*K1)
        K3 = f(x[k]+h/2,y[k]+(h/2)*K2)
        K4 = f(x[k]+h,y[k]+h*K3)

        y[k+1] = y[k] +(h/6)*(K1+2*K2+2*K3+K4)

    for k in range(3,n):
        y[k+1] = y[k] + (h/24) * (55 * f(x[k], y[k])
                                    - 59 * f(x[k-1], y[k-1]) + 37 * f(x[k-2], y[k-2]) - 9 * f(x[k-3], y[k-3]))
    return x,y

def f(x, y):
    return x + y

# Parámetros
a = 0
b = 1
y0 = 1
n = 10

# Calcular solución con Euler
x, y_aprox = adams4(f, a, b, y0, n)

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
plt.stem(x, y_aprox, linefmt='r-', markerfmt='ro', basefmt=' ', label='Método de Adams4')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de EDO: $y\' = x + y$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()