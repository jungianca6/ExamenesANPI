%Ejemplo del metodo de la potencia
clc; clear

A=[4 1 1;1 3 0;1 0 2];
d=eig(A)

x0=[1 1 1]'; %Valor inicial
xk=x0;
iterMax=1000;
tol=1e-8;

for k=1:iterMax
  yk=mldivide(A,xk);  %Resolver sistema para obtener yk=A^-1*xk;
  alphak=norm(yk,'inf');
  xk=(1/alphak)*yk;
  erk=norm((1/alphak)*xk-A*xk,'inf');
  if erk<tol
    break
  end
end

1/alphak %valor propio
xk
k
erk




