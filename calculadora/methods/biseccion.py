def metodo_biseccion(f, a, b, tol=1e-5, max_iter=50):
    resultado = []
    if f(a) * f(b) >= 0:
        return [("Error", "No hay cambio de signo", "")], None

    for i in range(max_iter):
        c = (a + b) / 2.0
        fc = f(c)
        error = abs(b - a) / 2.0

        resultado.append((c, error, fc))

        if abs(fc) < tol or error < tol:
            return resultado, c

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return resultado, c
