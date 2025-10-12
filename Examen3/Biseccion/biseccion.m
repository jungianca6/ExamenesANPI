function x=biseccion(f,a,b)
%f = una funcion f y es texto (f1(x)=0)
%a,b son los extremos del intervalo [a,b]


tol=1e-12;
iterMax=10000;


if f(a)*f(b)<0    %Paso 1
  for k=1:iterMax
    x=(a+b)/2;      %Paso 2: Dos intervalos [a,x] y [x,b]
    if f(a)*f(x)<0  %Paso 3
      b=x;
    else %f(x)*f(b)<0
      a=x;
    end
    error=abs(f(x));
    if error<tol  %Paso 4
      break
    end
  end
else
  display('No cumple el teorema de Bolzano')
  x='N/A';
  k='N/A';
  error='N/A';
end

end
