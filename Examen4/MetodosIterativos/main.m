%Comparacion de metodos
clc; clear; close all
pkg load symbolic  % Cargar paquete simbólico

syms x y


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

[x_1,y_1]=metodo_taylor(f,a,b,y0,n,5);
stem(x_1,y_1,'r')


legend('Solucion Analitica','Taylor')
