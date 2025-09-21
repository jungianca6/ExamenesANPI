function secante_O()
  % Parametros del ejemplo_nr
  % Llamo a la funcion para obtener el resultado

    clc; clear;

    f='exp(x)-2*x-10';
    x0=3;
    x1=4;
    tol=1e-10; %10^-10
    iterMax=1000;

    tic
    [xk,k,erk]=secante(x0,x1,tol,iterMax,f)
    t1=toc


end

function [xk,k,erk]=secante(x0,x1,tol,iterMax,f)


  fn=str2func(['@(x)' f]);    %Funcion Numerica (Usar)

  for k=0:iterMax
    if abs(fn(x1)-fn(x0))<1e-15
      xk="NA";
      k="NA";
      erk="NA";
      break
    end

    xk=x1-fn(x1)*(x1-x0)/(fn(x1)-fn(x0));
    erk=abs(fn(xk));
    if erk<tol
      k=k+1;
      break
    end
    x0=x1;
    x1=xk;

  end

end

