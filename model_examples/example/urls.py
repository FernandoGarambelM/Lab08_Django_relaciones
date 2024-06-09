from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generar_pdf/', views.generar_pdf, name='generar_pdf'),
    path('enviar_correo/', views.enviar_correo, name='enviar_correo'),
]
