%Solucion EDO 2do orden con Euler
clc; clear; close all
f=@(x,y,yp) x-yp-y;

y_v=[1];
z_v=[0];

a=0; b=2; m=10000;
h=(b-a)/m;


x_v=a:h:b;

for k=1:m
  ykN=y_v(k)+h*z_v(k);
  zkN=z_v(k)+h*f(x_v(k),y_v(k),z_v(k));
  y_v=[y_v ykN];
  z_v=[z_v zkN];
end


plot(x_v,y_v,'r')


%Grafica de la solucion para comparar

solF=@(x) 2*exp(-x/2).*cos(sqrt(3)/2*x)+x-1;

xSol=a:0.001:b;
ySol=solF(xSol);

hold on

plot(xSol,ySol,'b')

legend('Euler','Solucion')


