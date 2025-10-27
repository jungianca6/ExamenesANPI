function deriv_num()
  clc; clear;
  f=@(x) sin(x)*x+exp(-2*x);
  a=2;
  %Aproximar el valor de f'(a)
  h=@(k) 1/(2^k);
  tol=1e-10;
  iterMax=1000;
  disp('Aproximacion usando formula hacia adelante')
  [Ak1,erk1,k1]=dif_adel(f,a,h,tol,iterMax)
  disp('Aproximacion usando formula centrada')
  [Ak2,erk2,k2]=dif_cent(f,a,h,tol,iterMax)
end

function [Ak,erk,k]=dif_adel(f,a,h,tol,iterMax)

  h0=h(0);
  A0=(f(a+h0)-f(a))/(h0);
  Ak=A0;
  for k=1:iterMax
    hk=h(k);
    Ak_N=(f(a+hk)-f(a))/(hk);
    erk=abs(Ak_N-Ak);
    Ak=Ak_N;
    if erk<tol
      break
    endif
  end
end

function [Ak,erk,k]=dif_cent(f,a,h,tol,iterMax)

  h0=h(0);
  A0=(f(a+h0)-f(a-h0))/(2*h0);
  Ak=A0;
  for k=1:iterMax
    hk=h(k);
    Ak_N=(f(a+hk)-f(a-hk))/(2*hk);
    erk=abs(Ak_N-Ak);
    Ak=Ak_N;
    if erk<tol
      break
    endif
  end


end
