from django.urls import path
from django.contrib.staticfiles import *

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("home2/", views.home2, name="home2"),
]
