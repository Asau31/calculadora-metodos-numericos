from django.contrib import admin
from django.urls import path
from calculadora import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('resultado/', views.resultado, name='resultado'),
]
