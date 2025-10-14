function [x,y]=metodo_euler(f,a,b,y0,n)
  h=(b-a)/n;
  x=a:h:b;
  y=zeros(1,n+1);
  y(1)=y0;
  for k=1:n
    K1=f(x(k),y(k));
    K2=f(x(k)+h/2,y(k)+(h/2)*K1);
    K3=f(x(k)+h,y(k)-h*K1+2*h*K2);
    y(k+1)=y(k)+(h/6)*(K1+4*K2+K3);
  end
end


