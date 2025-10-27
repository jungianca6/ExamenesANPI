function [x,y]=metodo_adams2(f,a,b,y0,n)
  h=(b-a)/n;
  x=a:h:b;
  y=zeros(1,n+1);
  y(1)=y0;


  for k=1:1
    K1=f(x(k),y(k));
    K2=f(x(k)+h/2,y(k)+(h/2)*K1);
    K3=f(x(k)+h/2,y(k)+(h/2)*K2);
    K4=f(x(k)+h,y(k)+h*K3);
    y(k+1)=y(k)+(h/6)*(K1+2*K2+2*K3+K4);
  end


  for k=2:n
    y(k+1)=y(k)+(h/2)*(3*f(x(k),y(k))-f(x(k-1),y(k-1)));
  end
end

