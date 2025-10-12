%Ejemplo Recurrencia de Sturm

clc; clear

pkg load symbolic

syms x

T=[2 1 0 0 0;
   1 2 1 0 0;
   0 1 2 1 0;
   0 0 1 2 1;
   0 0 0 1 2];

a=diag(T);
b=diag(T,1); % b=diag(T,-1); Porque T es simetrica

m=length(a);

p0=1;
p1=a(1)-x;

for k=2:m
  pk=(a(k)-x)*p1-(b(k-1))^2*p0;
  p0=p1;
  p1=pk;
end

z=expand(pk)
fdn=matlabFunction(z)



