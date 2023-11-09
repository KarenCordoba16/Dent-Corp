from django.urls import path
from calendario_app import views

urlpatterns = [
    path('', views.calendario_view, name='calendario'),
    path('agregar_turno/', views.agregar_turno, name='agregar_turno'),
]
