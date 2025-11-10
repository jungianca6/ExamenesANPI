import numpy as np
import sympy as sp
from matplotlib import pyplot as plt


def f(x):
    return np.log(np.arcsin(x)) / np.log(x)

def newtonSimbolico(x,y,n):

    tabla=np.zeros([(n+1),(n+1)],dtype=float)

    for i in range(n+1):
        tabla[i,0] = y[i]

    for j in range(1,n+1):
        for i in range((n+1)-j):
            tabla[i,j]=(tabla[i+1,j-1]-tabla[i,j-1])/(x[i+j]-x[i])


    #Paso 2
    X = sp.symbols('X')
    polinomio=tabla[0,0]
    termino = 1

    for k in range(1,n+1):

        termino = termino*(X-x[k-1])
        polinomio = polinomio + tabla[0,k]*termino

    polinomio=sp.expand(polinomio)

    return polinomio

def main():
    x= np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8])
    y= np.array([f(0.1),f(0.2),f(0.3),f(0.4),f(0.5),f(0.6),f(0.7),f(0.8)])
    n=7
    return newtonSimbolico(x,y,n)

p=main()
print(p)
"""
print("Puntos x:", x)
print("Aproximación y:", y_aprox)

# Gráfica de la solución exacta (equivalente a Octave)
x_exact = np.linspace(0.1, 0.8, 1000)  # Equivalente a a:0.0001:b
y_exact = np.log(np.arcsin(x_exact)) / np.log(x_exact)

# Crear la gráfica
plt.figure(figsize=(10, 6))

# Graficar solución exacta (línea azul)
plt.plot(x_exact, y_exact, 'b', label='Solución exacta: $y = 2e^x - x - 1$', linewidth=2)

# Graficar solución aproximada (stem plot rojo)
plt.stem(x, y_aprox, linefmt='r-', markerfmt='ro', basefmt=' ', label='Método de Euler')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Solución de EDO: $y\' = x + y$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

"""


