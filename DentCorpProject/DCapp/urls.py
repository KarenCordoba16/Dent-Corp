from django.urls import path
from DCapp import views


urlpatterns = [
    path('', views.home, name="home"),
]