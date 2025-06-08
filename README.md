# Calculadora Web 

## Descripción General

Este proyecto es una aplicación web desarrollada con Django que permite calcular raíces reales aproximadas de funciones polinomiales y trascendentales utilizando métodos numéricos. El sistema está diseñado como una herramienta académica y didáctica que presenta resultados de forma visual, interactiva y modular.

Los métodos implementados son:

- Método de Bisección  
- Método de Newton-Raphson  
- Método de Newton-Raphson Modificado  

La aplicación permite al usuario ingresar una función, elegir un método de solución, establecer parámetros de precisión y visualizar el resultado mediante una tabla de iteraciones y una gráfica de la función.

## Objetivos del Proyecto

- Brindar una herramienta interactiva para aplicar métodos numéricos de resolución de raíces.
- Visualizar el comportamiento de las funciones y el proceso de convergencia.
- Facilitar el análisis y comparación de métodos clásicos en análisis numérico.
- Aplicar el framework Django para integrar backend lógico y frontend dinámico.

## Tecnologías Utilizadas

- Python 3.10+
- Django 4.2+
- SymPy
- Matplotlib
- Bootstrap 5
- HTML5 / CSS3 / JavaScript

## Requisitos Previos

Antes de ejecutar este proyecto, asegúrate de tener instalado:

- Python 3.10 o superior
- pip (instalador de paquetes de Python)
- Git (opcional para clonar el repositorio)

## Instalación

1. Clona el repositorio:

```
git clone https://github.com/tu_usuario/calculadora-raices.git
cd calculadora-raices
```

2. Crea un entorno virtual:

```
py -m venv env
```

3. Activa el entorno virtual:

- En Windows:
```
env\Scripts\activate
```

4. Instala dependencias:

```
pip install django
pip install sympy
pip install matplotlib
```

5. Ejecuta migraciones:

```
python manage.py migrate
```

6. Inicia el servidor:

```
python manage.py runserver
```

7. Abre el navegador en:

```
http://127.0.0.1:8000/
```

## Estructura del Proyecto

```
calculadora_raices/
├── calculadora/
│   ├── methods/
│   │   ├── biseccion.py
│   │   ├── newton.py
│   │   └── newton_modificado.py
│   ├── templates/calculadora/
│   │   ├── index.html
│   │   └── resultado.html
│   ├── static/
│   ├── views.py
│   ├── urls.py
│   └── ...
├── manage.py
└── db.sqlite3
```

## Funcionamiento

1. El usuario accede a la interfaz principal y escribe una función en notación Python.
2. Selecciona el método numérico a aplicar.
3. El sistema ajusta dinámicamente los campos necesarios.
4. Al enviar el formulario:
   - Se interpreta la función simbólicamente.
   - Se ejecuta el método correspondiente.
   - Se almacena la tabla de resultados.
   - Se genera una gráfica.
5. Se muestra la vista de resultados.

## Métodos Numéricos Implementados

### Método de Bisección

- Requiere extremos `a` y `b` donde `f(a)*f(b)<0`.
- Reduce el intervalo en cada iteración.

### Método de Newton-Raphson

- Requiere valor inicial `x0`.
- Utiliza derivadas para mejorar la convergencia.

### Método de Newton-Raphson Modificado

- Incluye segunda derivada `f′′(x)`.

## Validación y Manejo de Errores

- Validación de campos completos.
- Verificación de cambio de signo.
- Derivadas no nulas.
- Sintaxis válida en la función.
- Alertas y bloques try-except.

## Resultados

- Gráfica generada con Matplotlib.
- Tabla con iteraciones adaptada al método.
- Resultados claros con mensajes interpretables.

