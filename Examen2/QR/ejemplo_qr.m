function ejemplo_qr()

  A=[5 1 1;
     1 5 1;
     1 1 5];
  b=[7 7 7].';

  x=solve_qr(A,b)
end

function x=solve_qr(A,b)
  [Q,R]=qr(A);
  y=Q.'*b;
  x=sust_atras(R,y)
end

