%Ejemplo del método iterativo
%Newton-Schultz para aproximar la
%pseudoinversa de una matriz

clc; clear;

A=[2 1 1; 1 1 1; 1 1 1];

%Vector inicial
Y0=1/norm(A,'fro')^2*A.';

tol=1e-10;
iterMax=100;

Yk=Y0;
m=size(A,1); %#Filas de A
Im=eye(m);

for k=1:iterMax
  Yk=Yk*(2*Im-A*Yk);
  er=norm(A*Yk*A-A,'fro');
  if er<tol
    break
  end
end

