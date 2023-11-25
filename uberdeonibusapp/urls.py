from django.urls import path
from django.contrib.staticfiles import *
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path('poltronas/', views.lista_poltronas, name='lista_poltronas'),
    path('poltronas/selecionar/', views.selecionar_poltrona, name='selecionar_poltrona'),
    path('logout/', views.logout_view, name='logout'),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("home/", views.home, name="home"),
    path("pesquisa/", views.pesquisa, name="pesquisa"),
    path("checkout/", views.checkout, name="checkout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
