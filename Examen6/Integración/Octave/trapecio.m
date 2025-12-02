function y=trapecio(f,a,b)

  fn=str2func(['@(x)' f]);
  y=(fn(a)+fn(b))*(b-a)/2;

end


