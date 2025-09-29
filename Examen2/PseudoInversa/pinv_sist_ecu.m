%Ejemplo solucion sistema de ecuaciones
% Resolver el sistema Ax=b

clc; clear;

%Caso 1: Solución única
%A=[1 2;3 5]; b=[-3;-8];

%Caso 2: Infinitas soluciones
A=[1 2 3;4 5 6]; b=[6; 15];

%Caso 3: No tiene solución
A=[1 2; -2 -4; 5 3]; b=[1; 2; 3];


%Vector inicial
Y0=1/norm(A,'fro')^2*A.';

tol=1e-10; iterMax=100;

Yk=Y0;
m=size(A,1); %#Filas de A
Im=eye(m);

%Aproximacion de la solucion con valor incial
xk=Yk*b;

for k=1:iterMax
  Yk=Yk*(2*Im-A*Yk);
  xkN=Yk*b;
  er=norm(xkN-xk);
  if er<tol
    xk=xkN;
    break
  end
  xk=xkN;
end

xk
k
er
norm(A*xk-b)

