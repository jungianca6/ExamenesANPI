function newton_raphson_O()
  % Parametros del ejemplo_nr
  % Llamo a la funcion para obtener el resultado

    clc; clear;

    f='exp(x)-2*x-10';
    fd='exp(x)-2';
    x0=2;
    tol=1e-10; %10^-10
    iterMax=1000;

    tic
    [xk,k,erk]=newton_raphson(x0,tol,iterMax,f,fd)
    t1=toc


end

function [xk,k,erk]=newton_raphson(x0,tol,iterMax,f,fd)

  if nargin == 5
    fn=str2func(['@(x)' f]);    %Funcion Numerica (Usar)
    fdn=str2func(['@(x)' fd]);  %Funcion Numerica (Usar)
  end

  if nargin == 4
    pkg load symbolic
    syms x
    fn=str2func(['@(x)' f]);  %Funcion Numerica (Usar)
    fs=sym(f);                %Funcion Simbolica
    fds=diff(fs);             %Funcion Simbolica
    fdn=matlabFunction(fds);  %Funcion Numerica (Usar)
  end

  xk=x0;

  for k=0:iterMax
    if abs(fdn(xk))<1e-15
      xk="NA";
      k="NA";
      erk="NA";
      break
    end

    xk=xk-fn(xk)/fdn(xk);
    erk=abs(fn(xk));
    if erk<tol
      k=k+1;
      break
    end
  end

end
