function [x,y]=metodo_euler(f,a,b,y0,n)
  h=(b-a)/n;
  x=a:h:b;
  y=zeros(1,n+1);
  y(1)=y0;
  for k=1:n
    y(k+1)=y(k)+h*f(x(k),y(k));
  end
end


