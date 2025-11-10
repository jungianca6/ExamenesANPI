import numpy as np
import sympy as sp
import scipy.optimize as opt
import matplotlib.pyplot as plt

def hermite(xv,yv,yvd):
    x = sp.symbols('x')
    n = len(xv) - 1
    pol=0

    for j in range(n+1):
        Lj = Lk(xv,j)
        Lj2d = sp.diff(Lj, x)

        Lj2n= sp.lambdify(x, Lj2d, "numpy")
        Lj2= Lj2n(xv[j])

        Hj = (1 - 2 * (x - xv[j]) * Lj2) * Lj ** 2
        Kj = (x - xv[j]) * Lj**2

        pol= pol + (yv[j]*Hj + yvd[j]*Kj)

    pol = sp.simplify(pol)

    return pol

def Lk(xv,j):
    x= sp.symbols('x')
    n = len(xv) - 1
    L=1
    for m in range(n+1):
        if m != j:
            L = L * (x-xv[m]) / (xv[j]-xv[m])

    return L


#Parametros
a=-1
b=2
xv= np.array([-1,0,2])
yv = np.array([5, 2, -40])
yvd = np.array([12, -7, -51])

pol= hermite(xv,yv,yvd)

# Mostrar el polinomio en la terminal
print("Polinomio de Hermite p(x):")
print(pol)

x = sp.symbols('x')
# ---- Graficar ----
px = sp.lambdify(x, pol, 'numpy')
x_graf = np.linspace(a, b, 200)
y_graf = px(x_graf)

plt.plot(x_graf, y_graf, label="Polinomio de Hermite")
plt.scatter(xv, yv, color='red', label="Puntos dados")
plt.title("Interpolación de Hermite")
plt.grid()
plt.legend()
plt.show()