function A=matriz_tridiag(m)
  %Matriz tridiagonal con valor de 5 en la diagonal principal
  % y 1 en sus diagonales adyacentes.
  a=5*ones(m,1);
  b=ones(m-1,1);
  A=diag(a,0)+diag(b,1)+diag(b,-1);
end

