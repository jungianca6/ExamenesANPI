function x=sust_atras(A,b)
  m=length(b);
  x=zeros(m,1);
  for i=m:-1:1
    aux=0;
    for j=i+1:m
      aux+=A(i,j)*x(j);
    end
    x(i)=(1/A(i,i))*(b(i)-aux);
  end
end

