function [x,y]=predictor_corrector(f,a,b,y0,n)
  h=(b-a)/n;
  x=a:h:b;
  y=zeros(1,n+1);
  y(1)=y0;
  for k=1:n
    K1=f(x(k),y(k));
    K2=f(x(k)+h,y(k)+h*K1);
    y(k+1)=y(k)+h/2*(K1 + K2);
  end
end

