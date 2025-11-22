function ejemplo1()
  clc; clear;
  f=@(x) exp(-x.^2);
  a=-2; b=2;
  n=100;
  I_PM=Rect_PM(f,a,b)
  I_T=Trapecio(f,a,b)
  I_PMC=Rect_PM_Comp(f,a,b,n)
  I_TC=Trapecio_Comp(f,a,b,n)
  [I_1,k_1,er_1]=Rect_PM_Iter(f,a,b)
  [I_2,k_2,er_2]=Trapecio_Iter(f,a,b)
end

function I=Rect_PM(f,a,b)
  I=(b-a)*f((a+b)/2);
end

function I=Trapecio(f,a,b)
  I=(b-a)*(f(a)+f(b))/2;
end

function I=Rect_PM_Comp(f,a,b,n)
  h=(b-a)/n;
  x=a:h:b;
  I=0;
  for j=1:n
    I=I+Rect_PM(f,x(j),x(j+1));
  end
end

function I=Trapecio_Comp(f,a,b,n)
  h=(b-a)/n;
  x=a:h:b;
  I=0;
  for j=1:n
    I=I+Trapecio(f,x(j),x(j+1));
  end
end

function [Sk,k,er]=Rect_PM_Iter(f,a,b)
  iterMax=1e10;
  tol=1e-10;
  Sk=Rect_PM_Comp(f,a,b,1);
  for k=2:iterMax
    SkN=Rect_PM_Comp(f,a,b,k);
    er=abs(SkN-Sk);
    if er<tol
      Sk=SkN;
      break
    endif
    Sk=SkN;
  end
end

function [Sk,k,er]=Trapecio_Iter(f,a,b)
  iterMax=1e10;
  tol=1e-10;
  Sk=Trapecio_Comp(f,a,b,1);
  for k=2:iterMax
    SkN=Trapecio_Comp(f,a,b,k);
    er=abs(SkN-Sk);
    if er<tol
      Sk=SkN;
      break
    endif
    Sk=SkN;
  end
end

