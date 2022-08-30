from django.urls import path
from . import views

urlpatterns = [
    path('formulario_registro/', views.formulario_registro, name='Formulario_Registro'),
    path('reportes_poesia/', views.reportes_poesia, name='Reportes_Poesia')
]