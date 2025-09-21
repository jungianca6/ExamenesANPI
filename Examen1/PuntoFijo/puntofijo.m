%Ejemplo aproximar punto fijo
%usando el metodo iterativo
clc; clear;

f='((x-3)*exp(x-2))/2+2';
x0=1; %x0 en [0,7/3];
fn=str2func(['@(x)' f]);
iterMax=100;
tol=1e-10;
xk=x0;

for k=1:iterMax
  xkN=fn(xk);
  er=abs(xkN-xk);
  if er<tol
    xk=xkN;
    break
  end
  xk=xkN;
end

xk
k
er

