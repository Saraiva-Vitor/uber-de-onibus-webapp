from .models import *
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CadastroForm
from django.core.management import call_command
import folium
from folium import plugins
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from django.http import HttpResponse
from .tasks import reservar_poltrona_assincrona
import asyncio
from asgiref.sync import async_to_sync
from datetime import datetime

# Create your views here.
@csrf_protect
def err400(request):
    return render(request, 'errors/400.html')

def err403(request):
    return render(request, 'errors/403.html')

def err404(request):
    return render(request, 'errors/404.html')

def err500(request):
    return render(request, 'errors/500.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@csrf_protect
def filtroassentos(request):
    rota_id = request.GET.get('rota_id')
    hora_id = request.GET.get('hora_id')
    
    return redirect('detalhes_rota', rota_id=rota_id, hora_id=hora_id)

@csrf_protect
def detalhes_rota(request, rota_id, hora_id):
    rota = get_object_or_404(BusRoute, id=rota_id)
    horarios = BusSchedule.objects.get(id=hora_id)
    poltronas = Poltrona.objects.filter(route=rota, horario=horarios)

    context = {
        'rota': rota,
        'horarios': horarios,
        'poltronas': poltronas,
    }

    return render(request, 'mapaAssentos.html', context)

@csrf_protect
def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['nome']
            user.last_name = form.cleaned_data['cpf']
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Chama o comando createuser para criar o usuário no Django Admin
            call_command("createuser", user.email, form.cleaned_data['password'], user.first_name, user.last_name)

            messages.success(request, 'Cadastro realizado com sucesso. Faça o login.')
            return redirect('login')
        else:
            messages.error(request, 'Erro no formulário. Corrija os campos destacados.')

    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {'form': form})

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Usuário autenticado com sucesso, faz o login
            login(request, user)
            messages.success(request, 'Login realizado com sucesso.')
            return redirect('home')  # Redireciona para a página inicial após o login
        else:
            # Usuário não autenticado
            messages.error(request, 'Credenciais inválidas. Verifique seu email/CPF e senha.')
            return render(request, 'login.html', {'login_failed': True})

    return render(request, 'login.html')

@csrf_protect
def checkout(request):
    if request.method == 'GET':
        origem = request.GET.get('origem')
        origemlat = request.GET.get('origemlat')
        origemlong = request.GET.get('origemlong')
        destino = request.GET.get('destino')
        destinolat = request.GET.get('destinolat')
        destinolong = request.GET.get('destinolong')
        horario = request.GET.get('horario')
        precorota = request.GET.get('precorota')
        precotipo = request.GET.get('precotipo')
        poltrona = request.GET.get('poltrona')
        poltrona_id = request.GET.get('poltrona_id')
        rota_id = request.GET.get('rota_id')
        horario_id = request.GET.get('horario_id')

        poltronas = Poltrona.objects.filter(id=poltrona_id)
        ids = poltronas.values_list('id', flat=True)
        id = ids[0]

        origemlat = origemlat.replace(',', '.')
        origemlong = origemlong.replace(',', '.')
        destinolat = destinolat.replace(',', '.')
        destinolong = destinolong.replace(',', '.')
        precorota = precorota.replace(',', '.')
        precotipo = precotipo.replace(',', '.')

    soma_total = round(float(precorota) + float(precotipo),2)

    async def reservar_poltrona_assincrona_wrapper(poltrona_id):
        await reservar_poltrona_assincrona(poltrona_id)

    async_to_sync(reservar_poltrona_assincrona_wrapper(poltrona_id))

    def calcular_centro(coord1, coord2):
        return ((coord1[0] + coord2[0]) / 2, (coord1[1] + coord2[1]) / 2)

    # Coordenadas para origem e destino (você pode obter essas coordenadas de qualquer maneira que desejar)
    coordenadas_origem = [float(origemlat), float(origemlong)]
    coordenadas_destino = [float(destinolat), float(destinolong)]

    # Crie um mapa centrado em uma localização específica
    mapa = folium.Map(location=coordenadas_origem, zoom_start=5)

    folium.Marker(coordenadas_origem, popup='Origem').add_to(mapa)
    folium.Marker(coordenadas_destino, popup='Destino').add_to(mapa)

    centro = calcular_centro(coordenadas_origem, coordenadas_destino)

    mapa.location = centro

    mapa_html = mapa._repr_html_()

    return render(request, 'checkout.html', {'mapa_html': mapa_html, 'poltrona_id': poltrona_id, 'rota_id': rota_id, 'horario_id': horario_id, 'poltrona': poltrona, 'preco': soma_total, 'origem': origem, 'origemlat': origemlat, 'origemlong': origemlong, 'destino': destino, 'destinolat': destinolat, 'destinolong': destinolong, 'horario': horario})

@csrf_protect
def home(request):
    locais = Location.objects.all()
    routes = BusRoute.objects.all()

    return render(request, 'home.html', {'locais': locais, 'routes': routes})

@csrf_protect
def pesquisa(request):
    locais = Location.objects.all()
    routes = BusRoute.objects.all()

    dinamico = False
    
    if request.method == 'GET':
        origem_id = request.GET.get('origem')
        destino_id = request.GET.get('destino')
        data = request.GET.get('data')

        #fazendo pesquisa sem recarregar a pagina
        if(destino_id==None): 
            dinamico = True
            rotas =  routes.filter(origin=origem_id)
        else:
            rotas = routes.filter(origin_id=origem_id, destination_id=destino_id)
          
    rotas_com_soma = []
    for rota in rotas:
        preco_rota = rota.preco if rota.preco else 0
        preco_tipo_onibus = rota.bus.tipo_onibus.preco if rota.bus and rota.bus.tipo_onibus else 0
        soma_total = preco_rota + preco_tipo_onibus
        rotas_com_soma.append({'rota': rota, 'soma_total': soma_total})

        return render(request, 'pesquisa.html', {'rotas_com_soma': rotas_com_soma, 'locais': locais,'rotas':rotas, 'dinamico': dinamico,'nome_origem':rotas[0].origin.name, 'nome_destino':rotas[0].destination.name, 'nome_rota':rotas[0].name,'origem_id':origem_id,'destino_id':destino_id,'data':data})

def pagamento(request):
    if request.method == 'GET':
        passageiro = request.GET.get('passageiro')
        cpf_passageiro = request.GET.get('cpf_passageiro')
        nascimento_passageiro = request.GET.get('nascimento_passageiro')
        email_passageiro = request.GET.get('email_passageiro')
        tel_passageiro = request.GET.get('tel_passageiro')
        metodo_pagamento = request.GET.get('pagamento')

        origem = request.GET.get('origem')
        destino = request.GET.get('destino')
        horario = request.GET.get('horario')
        poltrona = request.GET.get('poltrona')

        poltrona_id = request.GET.get('poltrona_id')
        rota_id = request.GET.get('rota_id')
        horario_id = request.GET.get('horario_id')

    return render(request, 'pagamento.html', {'poltrona_id': poltrona_id, 'rota_id': rota_id, 'horario_id': horario_id,'origem': origem, 'destino': destino, 'horario': horario, 'poltrona': poltrona,'passageiro': passageiro, 'nascimento_passageiro': nascimento_passageiro, 'cpf_passageiro': cpf_passageiro, 'email_passageiro': email_passageiro, 'tel_passageiro': tel_passageiro, 'metodo_pagamento': metodo_pagamento})

def confirmacao_pagamento(request):
    if request.method == 'GET':
        passageiro = request.GET.get('passageiro')
        cpf_passageiro = request.GET.get('cpf_passageiro')
        origem = request.GET.get('origem')
        destino = request.GET.get('destino')
        horario = request.GET.get('horario')
        poltrona = request.GET.get('poltrona')
        poltrona_id = request.GET.get('poltrona_id')
        rota_id = request.GET.get('rota_id')
        horario_id = request.GET.get('horario_id')
    return render(request, 'confirmacaoPagamento.html', {'poltrona_id': poltrona_id, 'rota_id': rota_id, 'horario_id': horario_id,'origem': origem, 'destino': destino, 'horario': horario, 'poltrona': poltrona,'passageiro': passageiro, 'cpf_passageiro': cpf_passageiro})

def passagem(request):
    if request.method == 'GET':
        passageiro = request.GET.get('passageiro')
        cpf_passageiro = request.GET.get('cpf_passageiro')
        origem = request.GET.get('origem')
        destino = request.GET.get('destino')
        horario = request.GET.get('horario')
        poltrona = request.GET.get('poltrona')
        poltrona_id = request.GET.get('poltrona_id')
        rota_id = request.GET.get('rota_id')
        horario_id = request.GET.get('horario_id')

    assento = Poltrona.objects.filter(id=poltrona_id, route_id=rota_id, horario_id=horario_id)
    assento.ocupada = True
    assento.nome_passageiro = passageiro

    return render(request, 'passagem.html', {'origem': origem, 'destino': destino, 'horario': horario, 'poltrona': poltrona,'passageiro': passageiro, 'cpf_passageiro': cpf_passageiro})