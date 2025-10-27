import numpy as np
from matplotlib import pyplot as plt


def RK6(f,a,b,y0,n):
    h = (b-a)/n
    x= np.linspace(a,b,n+1)
    y = np.zeros(n+1)

    y[0]= y0

    for k in range(n):
        k1=  h*f(x[k],y[k])
        k2 = h*f(x[k]+h/3,y[k]+k1/3)
        k3 = h*f(x[k]+(2*h)/5,y[k]+(4*k1+6*k2)/25)
        k4 = h*f(x[k]+h,y[k]+(k1-12*k2+15*k3)/4)
        k5 = h*f(x[k]+(2*h)/3,y[k]+(6*k1+90*k2-50*k3+8*k4)/81)
        k6 = h*f(x[k]+(4*h)/5,y[k]+(6*k1+36*k2+10*k3+8*k4)/75)

        y[k+1] = y[k] + (23*k1+125*k2-81*k5+125*k6)/192

    return x,y
def f(x, y):
    return np.cos(x)*y
# Parámetros
a = -5
b = 5
y0 = 1
n = 50

# Calcular solución con Euler
x, y_aprox = RK6(f, a, b, y0, n)

print("Puntos x:", x)
print("Aproximación y:", y_aprox)

# Gráfica de la solución exacta
x_exact = np.linspace(a, b, 1000)  # Equivalente a a:0.0001:b
y_exact = np.exp(np.sin(x_exact)+np.sin(5))  # Solución exacta de y' = x + y

# Crear la gráfica
plt.figure(figsize=(10, 6))

# Graficar solución exacta (línea azul)
plt.plot(x_exact, y_exact, 'b', label='Solución exacta: $y = 2e^x - x - 1$', linewidth=2)

# Graficar solución aproximada (stem plot rojo)
plt.stem(x, y_aprox, linefmt='r-', markerfmt='ro', basefmt=' ', label='Método de RK4')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de EDO: $y\' = x + y$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()