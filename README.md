#  Calculadora Web de Raíces de Polinomios con Métodos Numéricos

Este proyecto es una aplicación web desarrollada en **Django + Python** que permite calcular raíces de funciones utilizando los métodos numéricos:

- Método de Bisección
- Método de Newton-Raphson
- Método de Newton-Raphson Modificado

Cuenta con una interfaz moderna, validación de datos y visualización gráfica interactiva de la función.

---

##  Tecnologías utilizadas

- Python 3.11+
- Django 5.2.1
- Bootstrap 5 (CSS)
- SymPy, NumPy, Matplotlib

---

##  Requisitos funcionales

1. Permitir ingresar funciones (ej: `x**3 - x - 2`) en un formulario web.
2. Permitir seleccionar el método a aplicar.
3. Solicitar los parámetros necesarios según el método:
   - **Bisección**: extremos `a`, `b`, tolerancia, iteraciones.
   - **Newton** y **Modificado**: valor inicial `x0`, tolerancia, iteraciones.
4. Ejecutar el método y mostrar:
   - Tabla de iteraciones con valores relevantes.
   - Valor final de la raíz aproximada.
   - Gráfica de la función con sombreado visual.
5. Validar errores como divisiones por cero, derivadas nulas o ausencia de cambio de signo.

---

##  Instalación local

``bash
# Clona el repositorio o crea una carpeta
cd tu_carpeta/
py -m venv venv_calculadora
venv_calculadora\Scripts\activate

# Instala dependencias
pip install django sympy matplotlib numpy

# CorreR el servidor
cd calculadora_proyecto
py manage.py runserver
