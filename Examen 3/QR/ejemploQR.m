%Ejemplo metodo QR

A=[2 2 2 1;2 0 2 0;2 2 0 2;1 0 2 2];

iterMax=1000;
tol=1e-10;

Ak=A;
dk=diag(Ak);
Uk=eye(4);

for k=1:iterMax
  [Qk,Rk]=qr(Ak);
  Ak=Rk*Qk;
  Uk=Uk*Qk;
  dkN=diag(Ak);
  erk=norm(dkN-dk);
  if erk<tol
    dk=dkN;
    break
  end
  dk=dkN;
end

dk
Uk
k
erk
