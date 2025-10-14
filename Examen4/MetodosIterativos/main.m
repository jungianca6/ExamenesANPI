%Comparacion de metodos
clc; clear; close all

f=@(x,y) x+y;
a=0;
b=1;
y0=1;
n=6;

%Gráfica de la solución
hold on
xDisct=a:0.0001:b;
yDisct=2*exp(xDisct)-xDisct-1;
hold on
plot(xDisct,yDisct,'b')

[x_1,y_1]=metodo_euler(f,a,b,y0,n);
stem(x_1,y_1,'r')

[x_2,y_2]=metodo_rk3(f,a,b,y0,n);
stem(x_2,y_2,'g')

legend('Solucion Analitica','Euler','RK3')
