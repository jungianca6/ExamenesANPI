%Ejemplo Intervalo de Sturm (usando teorema)

clc; clear;

T2 = [ -5   0.1  0    0    0;
        0.1 -5   0.1  0    0;
        0    0.1  0    0.1  0;
        0    0    0.1  5    0.1;
        0    0    0    0.1  5 ];


m=size(T2,1);

Ints=zeros(m,2); %Las filas van a representar los extremos de los intervalos

R1=abs(T2(1,2));
Ints(1,1)=T2(1,1)-R1;
Ints(1,2)=T2(1,1)+R1;

Rm=abs(T2(m,m-1));
Ints(m,1)=T2(m,m)-Rm;
Ints(m,2)=T2(m,m)+Rm;

for k=2:m-1
  Rk=abs(T2(k,k-1))+abs(T2(k,k+1));
  Ints(k,1)=T2(k,k)-Rk;
  Ints(k,2)=T2(k,k)+Rk;
end

Ints
Intervalo=[min(Ints(:,1)) max(Ints(:,2))]


