from django.shortcuts import render, redirect
from .methods.biseccion import metodo_biseccion
from .methods.newton import metodo_newton
from .methods.newton_modificado import metodo_newton_modificado
import sympy as sp
import matplotlib.pyplot as plt
import io, urllib, base64

def index(request):
    return render(request, 'calculadora/index.html')

def resultado(request):
    if request.method == 'POST':
        try:
            metodo = request.POST.get('metodo')
            funcion = request.POST.get('funcion')
            max_iter = int(request.POST.get('max_iter', 50))
            tol = float(request.POST.get('tolerancia', 1e-5))

            if tol <= 0 or max_iter <= 0:
                raise ValueError("Tolerancia e iteraciones deben ser positivas.")

            x = sp.symbols('x')
            f = sp.sympify(funcion)  # puede fallar si la expresión es inválida
            fx = sp.lambdify(x, f)

            resultado = []
            raiz = None

            if metodo == 'biseccion':
                a = float(request.POST.get('a'))
                b = float(request.POST.get('b'))
                if fx(a) * fx(b) >= 0:
                    raise ValueError("No hay cambio de signo entre a y b.")
                resultado, raiz = metodo_biseccion(fx, a, b, tol, max_iter)

            elif metodo == 'newton':
                x0 = float(request.POST.get('x0'))
                resultado, raiz = metodo_newton(f, x0, tol, max_iter)

            elif metodo == 'newton_modificado':
                x0 = float(request.POST.get('x0'))
                resultado, raiz = metodo_newton_modificado(f, x0, tol, max_iter)

            # Graficar
            x_vals = [i / 10.0 for i in range(-100, 101)]
            y_vals = [fx(i) for i in x_vals]
            plt.figure(figsize=(8, 4))
            plt.plot(x_vals, y_vals, label='f(x)')
            plt.axhline(0, color='black', linestyle='--')
            plt.fill_between(x_vals, y_vals, 0, where=[y > 0 for y in y_vals], interpolate=True, alpha=0.1, color='blue')
            plt.fill_between(x_vals, y_vals, 0, where=[y < 0 for y in y_vals], interpolate=True, alpha=0.1, color='red')
            plt.grid(True)
            plt.legend()

            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()
            grafica = base64.b64encode(image_png).decode('utf-8')

            return render(request, 'calculadora/resultado.html', {
                'raiz': raiz,
                'resultado': resultado,
                'grafica': grafica
            })

        except Exception as e:
            return render(request, 'calculadora/index.html', {
                'error': f"Ocurrió un error: {e}"
            })

    return redirect('index')
