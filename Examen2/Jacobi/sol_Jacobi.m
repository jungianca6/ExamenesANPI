function xk=sol_Jacobi(A,b)
  tol=1e-10; iterMax=1000;
  m=length(b); xk=zeros(m,1); %Vector inicial

  d1=diag(A); D=diag(d1); %Paso 1
  Dinv=diag(1./d1); %Paso 2
  LmU=A-D; %Paso 3
  d=Dinv*b; %Paso 4
  T=-Dinv*LmU; %Paso 5
  for k=1:iterMax %Paso 6
    xk=T*xk+d;    %Paso 7
    er=norm(A*xk-b); %Paso 8
    if er<tol    %Paso 9
      k=k+1;
      break
    end
  end
end
