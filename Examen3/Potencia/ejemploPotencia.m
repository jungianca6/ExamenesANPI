%Ejemplo del metodo de la potencia

A=[4 1 1;1 3 0;1 0 2];
d=eig(A)

x0=rand(3,1); %Valor inicial
xk=x0;
iterMax=100;
tol=1e-8;

for k=1:iterMax
  yk=A*xk;
  alphak=norm(yk,'inf')
  xk=(1/alphak)*yk;
  erk=norm(A*xk-alphak*xk,'inf');
  if erk<tol
    break
  end
end

alphak
xk
k
erk




