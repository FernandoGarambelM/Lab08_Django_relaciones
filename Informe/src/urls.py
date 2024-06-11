from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('gestionar/', views.gestionar_destinos, name="gestionar_destinos"),
    path('gestionar/<int:id>/', views.gestionar_destinos, name="modificar_destino"),
]
