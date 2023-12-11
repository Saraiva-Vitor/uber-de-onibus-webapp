from django.urls import path
from django.contrib.staticfiles import *
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("pesquisa/", views.pesquisa, name="pesquisa"),
    path("mapa-de-assentos/", views.filtroassentos, name="filtroassentos"),
    path('mapa-de-assentos/<int:rota_id>/<int:hora_id>/', views.detalhes_rota, name='detalhes_rota'),
    path("checkout/", views.checkout, name="checkout"),
    path("pagamento/", views.pagamento, name="pagamento"),
    path("confirmacao-pagamento/", views.confirmacao_pagamento, name="confirmacao_pagamento"),
    path("passagem/", views.passagem, name="passagem"),
    path("400/", views.err400, name="400"),
    path("403/", views.err403, name="403"),
    path("404/", views.err404, name="404"),
    path("500/", views.err500, name="500"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
