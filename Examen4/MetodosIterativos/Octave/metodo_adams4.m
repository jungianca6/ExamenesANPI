function [x,y]=metodo_adams4(f,a,b,y0,n)
  h=(b-a)/n;
  x=a:h:b;
  y=zeros(1,n+1);
  y(1)=y0;


  for k=1:3
    K1=f(x(k),y(k));
    K2=f(x(k)+h/2,y(k)+(h/2)*K1);
    K3=f(x(k)+h/2,y(k)+(h/2)*K2);
    K4=f(x(k)+h,y(k)+h*K3);
    y(k+1)=y(k)+(h/6)*(K1+2*K2+2*K3+K4);
  end

  for k=4:n
     y(k+1)=y(k)+(h/24)*(55*f(x(k),y(k))-59*f(x(k-1),y(k-1))+37*f(x(k-2),y(k-2))-9*f(x(k-3),y(k-3)));
  end
end
