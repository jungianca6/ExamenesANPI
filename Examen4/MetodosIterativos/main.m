%Comparacion de metodos
clc; clear; close all
pkg load symbolic  % Cargar paquete simbólico

syms x y


f=@(x,y) x+y;
a=0;
b=1;
y0=1;
n=10;

%Gráfica de la solución
hold on
xDisct=a:0.0001:b;
yDisct=2*exp(xDisct)-xDisct-1;
hold on
plot(xDisct,yDisct,'b')

[x_1,y_1]=metodo_adams2(f,a,b,y0,n);
stem(x_1,y_1,'r')
[x_2,y_2]=metodo_adams3(f,a,b,y0,n);
stem(x_2,y_2,'g')
[x_3,y_3]=metodo_adams4(f,a,b,y0,n);
stem(x_3,y_3,'m')

legend('Solucion Analitica','Adams-Bashforth 2', 'Adams-Bashforth 3', 'Adams-Bashforth 4')
