function [x, y] = metodo_taylor(fsym, a, b, y0, n, p)
  % fsym: función simbólica f(x,y)
  % a,b : intervalo
  % y0  : condición inicial
  % n   : número de pasos
  % p   : orden del método

  pkg load symbolic  % Cargar paquete simbólico

  syms x y

  % Asegurar que f sea simbólica
  f_sym = fsym(x, y);

  % Derivadas sucesivas y almacenar en un vector
  derivs = cell(p, 1);
  derivs{1} = f_sym;
  for k = 2:p
    derivs{k} = diff(derivs{k-1}, x) + diff(derivs{k-1}, y)*f_sym;
  end

  % Convertir derivadas simbólicas a funciones numéricas
  f_funcs = cell(p, 1);
  for k = 1:p
    f_funcs{k} = matlabFunction(derivs{k}, "vars", [x y]);
  end

  % Preparar malla y solución
  h = (b - a)/n;
  x = a:h:b;
  y = zeros(1, n+1);
  y(1) = y0;

  % Iteración de Taylor
  for k = 1:n
    suma = 0;
    for i = 1:p
      suma = suma + (h^i / factorial(i)) * f_funcs{i}(x(k), y(k));
    end
    y(k+1) = y(k) + suma;
  end
end

