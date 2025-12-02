function I=simpson_compuesto(f,a,b,n)
  I=0;
  h=(b-a)/n;
  x=a:h:b;
  for k=0:n-1
    I=I+simpson(f,x(k+1),x(k+2));
  end
end

