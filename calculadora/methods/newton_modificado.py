import sympy as sp

def metodo_newton_modificado(funcion, x0, tol=1e-5, max_iter=50):
    x = sp.symbols('x')
    f = funcion
    f_prime = sp.diff(f, x)
    f_double_prime = sp.diff(f_prime, x)

    f_lamb = sp.lambdify(x, f)
    f_prime_lamb = sp.lambdify(x, f_prime)
    f_double_prime_lamb = sp.lambdify(x, f_double_prime)

    resultado = []

    for i in range(max_iter):
        fx = f_lamb(x0)
        dfx = f_prime_lamb(x0)
        d2fx = f_double_prime_lamb(x0)

        if dfx == 0:
            return [("Error", "Derivada primera cero", fx, dfx, d2fx)], None

        x1 = x0 - (fx * dfx) / (dfx**2 - fx * d2fx)
        error = abs(x1 - x0)
        resultado.append((x1, error, f_lamb(x1), f_prime_lamb(x1), f_double_prime_lamb(x1)))

        if error < tol:
            return resultado, x1

        x0 = x1

    return resultado, x1
