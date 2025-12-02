function ejemplo_CG_SYM()
  clc; clear;
  warning('off','all')
  f=@(x) exp(-x^2);
  a=-1;
  b=1;
  n=5;

  [xv,wv]=pesos_xj_cg(n);

  I=0;
  for i=1:n
    I=I+wv(i)*f(xv(i));
  end

  I

end

function [xv,wv]=pesos_xj_cg(n)
  pkg load symbolic
  %Paso 1: Polinomio de Legendre
  syms x
  pn=1/(2^n*factorial(n))*diff((x^2-1)^n,n);
  %Paso 2: pn=0 y obtener vector xv
  xv=double(solve(pn==0));
  %Paso 3: derivada de pn
  pnd=diff(pn);
  pn_dn=matlabFunction(pnd);
  %Paso 4: Calcular vector wv
  wv=2./((1-xv.^2).*(pn_dn(xv)).^2);

end


