function y=simpson(f,a,b)

  fn=str2func(['@(x)' f]);
  y=(b-a)/6*(fn(a)+4*fn((a+b)/2)+fn(b));

end


