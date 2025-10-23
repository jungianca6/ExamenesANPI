
import numpy as np
from matplotlib import pyplot as plt


def euler(f,a,b,y0,z0,n):
    h = (b-a)/n
    x_v = np.linspace(a,b,n+1)

    y_v = np.zeros(n + 1)
    z_v = np.zeros(n + 1)

    y_v[0]= y0
    z_v[0] = z0

    for k in range(n):
        yKN = y_v[k] + h*z_v[k]
        zKN= z_v[k] + h* f(x_v[k],y_v[k],z_v[k])

        y_v[k+1] = yKN
        z_v[k+1] = zKN

    return x_v, y_v



def f(x,y,yp):
    return x-yp-y

a=0
b=2
n=10000
y0= 1
z0= 0

# Calcular solución con Euler
x, y_aprox = euler(f, a, b, y0, z0, n)

print("Puntos x:", x)
print("Aproximación y:", y_aprox)

# Gráfica de la solución exacta
x_exact = np.linspace(a, b, 1000)  # Equivalente a a:0.0001:b
y_exact = 2 * np.exp(-x_exact/2) * np.cos(np.sqrt(3)/2*x_exact) +x_exact - 1  # Solución exacta

# Crear la gráfica
plt.figure(figsize=(10, 6))

# Graficar solución exacta (línea azul)
plt.plot(x_exact, y_exact, 'b', label='Solución exacta: $y = 2e^x - x - 1$', linewidth=2)

# Graficar solución aproximada (stem plot rojo)
plt.plot(x, y_aprox, 'r', label='Método de Euler 2do Orden',linewidth=2)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de EDO: $y\' = x + y$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()