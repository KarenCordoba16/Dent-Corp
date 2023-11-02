from django.urls import path
from DCapp import views

urlpatterns = [
    path('', views.Inicio, name="inicio"),
]