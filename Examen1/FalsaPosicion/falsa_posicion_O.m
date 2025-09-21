function falsa_posicion_O()

    % Parametros de falsa posicion
    % Llamo a la funcion para obtener el resultado

    clc; clear;

    f = 'x * exp(-x) - 5 - (cos(x) / x)';
    a = -0.3;
    b = -0.1;
    tol = 1e-8;
    iterMax = 10000;

    tic
    [xk, k, erk] = falsa_posicion(a, b, tol, iterMax, f)
    t1 = toc

end

function [xk, k, erk] = falsa_posicion(a, b, tol, iterMax, f)
    fn = str2func(['@(x)' f]);    % Funcion Numerica (Usar)

    % Verificar teorema de Bolzano
    if fn(a) * fn(b) >= 0
        xk = "NA";
        k = "NA";
        erk = "NA";
        return
    end

    xk = a;
    for k = 0:iterMax
        % Calcular la falsa posición
        xk = a - (fn(a) * (a - b)) / (fn(a) - fn(b));

        % Verificar división por cero
        if abs(fn(a) - fn(b)) < 1e-15
            xk = "NA";
            erk = "NA";
            break
        end

        % Validar teorema de Bolzano y actualizar intervalo
        if fn(a) * fn(xk) < 0
            b = xk;
        else
            a = xk;
        end

        % Calcular error
        erk = abs(fn(xk));

        % Criterio de parada
        if erk < tol
            k = k + 1;
            break
        end
    end
end
