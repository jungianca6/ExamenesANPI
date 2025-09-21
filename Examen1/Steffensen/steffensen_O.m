function steffensen_O()

  % Parametros de steffensen
  % Llamo a la funcion para obtener el resultado

    clc; clear;

    f='exp(x)-2*x-10';
    x0=3;
    tol=1e-10; %10^-10
    iterMax=1000;

    tic
    [xk,k,erk]=steffensen(x0,tol,iterMax,f)
    t1=toc

end

function [xk,k,erk]=steffensen(x0,tol,iterMax,f)
  fn=str2func(['@(x)' f]);    %Funcion Numerica (Usar)

  xk=x0;
  for k=0:iterMax
    if abs(fn(xk))<1e-15
      xk="NA";
      k="NA";
      erk="NA";
      break
    end

    xk= xk-((fn(xk)^2)/(fn(xk+fn(xk))-fn(xk)));
    erk=abs(fn(xk));
    if erk<tol
      k=k+1;
      break
    end
  end
end


