f1=@(x) exp(x)-2*x-10;

%Ejemplo3: 'fminbnd' = Calcular el mínimo de una función f en un intervalo [a,b]
a=-4;
b=-2;
xmin=fminbnd(f1,a,b)

%Ejercicio: Calcular el máximo de una funcion f en un intervalo [a,b]
a=1;
b=3;
newf1=@(x) -1*f1(x); %Reflejar f1 en el eje x
fmaxbnd=@(newf1,a,b) fminbnd(newf1,a,b);
xmax=fmaxbnd(newf1,a,b)
