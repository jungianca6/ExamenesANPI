function Sk=trapecio_iterativo(f,a,b)

  tol=1e-16;
  numInterMax=10000000;
  Sk=trapecio_compuesto(f,a,b,2);

  for k=3:numInterMax
    Sk_N=trapecio_compuesto(f,a,b,k);
    er=abs(Sk_N-Sk);
    if er<tol
      Sk=Sk_N;
      k
      break
    endif
    Sk=Sk_N;
  end
end

