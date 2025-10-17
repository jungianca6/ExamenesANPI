import numpy as np


def predictor_corrector(f,a,b,y0,n):
    h=(b-a)/n
    x=np.linspace(a,b,n+1)
    y=np.zeros(n+1)
    y[0]=y0

    for k in range(n):
        K1 = f(x[k], y[k])
        K2 = f(x[k]+h, y[k]+h*K1)
        y[k+1]= y[k] + h/2+(K1+K2)

    return x,y