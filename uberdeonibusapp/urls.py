from django.urls import path
from django.contrib.staticfiles import *
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("home/", views.home, name="home"),
    path("pesquisa/", views.pesquisa, name="pesquisa"),
    path("checkout/", views.checkout, name="checkout"),
    path("pagamento/", views.pagamento, name="pagamento"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
