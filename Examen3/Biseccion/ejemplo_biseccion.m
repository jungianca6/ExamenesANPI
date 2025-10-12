%Calculo de los valores propios de la matriz
%T2=[1 4 0;4 -2 -5;0 -5 3]
%usando el metodo de la bisección

clc; clear;

%Polinomio Característicom (Sturm)
p=@(x) -x^3+2*x^2+46*x-79;

%Intervalo donde se encuentran los valores propios (Gershgorin)
a=-11;
b=8;

%Discretizar el intervalo [-11,8]
h=1;
x_val=[a:h:b];

n=length(x_val);

vect_val_pro=[];

for i=1:n-1
  %Preguntar si se cumple el teorema de Bolzano
  xi=x_val(i);
  xim1=x_val(i+1);
  if p(xi)*p(xim1)<0
    val_prop=biseccion(p,xi,xim1);
    vect_val_pro=[vect_val_pro val_prop];
  end
end

disp('Aproxmacion valores propios')
vect_val_pro

disp('Valores propios exactos')
T2=[1 4 0;4 -2 -5;0 -5 3];
eig(T2)




