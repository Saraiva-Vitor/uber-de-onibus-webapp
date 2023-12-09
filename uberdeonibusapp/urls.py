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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
