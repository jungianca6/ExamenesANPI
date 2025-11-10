%Implementacion del trazador cúbico (natural)
clc;clear;close all;

f=@(x) 3.*x.*exp(x)-2*exp(x);

xv=[1,1.05,1.07,1.1];
yv=f(xv);

%Primero calcular el vector h

m=length(xv);
n=(m-1);  %(m-2)=(n-1)
h=zeros(n,1);

for j=1:n
  h(j)=xv(j+1)-xv(j);
end

%Crear la matriz A
A=zeros(n-1,n-1);
A(1,1)=2*(h(1)+h(2)); A(1,2)=h(2); %Fila 1
A(n-1,n-2)=h(n-1); A(n-1,n-1)=2*(h(n-1)+h(n)); %Fila n

for k=2:n-2
  A(k,k-1)=h(k); A(k,k)=2*(h(k)+h(k+1)); A(k,k+1)=h(k+1);
end

%Calcular el vector U
u=zeros(n-1,1);
for k=1:n-1
  u(k)=6*((yv(k+2)-yv(k+1))/h(k+1)-(yv(k+1)-yv(k))/h(k));
end

%Calcular vector M=[M0 M1 ...Mn]
g=mldivide(A,u); %M1 M2 ...Mn-1
M=[0; g; 0];

%Calcular constantes aj, bj, cj, dj

Z=zeros(n,4);

for j=1:n
  aj=(M(j+1)-M(j))/(6*h(j));
  bj=M(j)/2;
  cj=(yv(j+1)-yv(j))/h(j)-(h(j)/6)*(M(j+1)+2*M(j));
  dj=yv(j);

  Z(j,:)=[aj bj cj dj];
end
Z
