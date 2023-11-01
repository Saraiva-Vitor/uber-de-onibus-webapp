from django.shortcuts import render
from .models import Location, BusRoute

# Create your views here.
def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def checkout(request):
    if request.method == 'GET':
        origem = request.GET.get('origem')
        origemlat = request.GET.get('origemlat')
        origemlong = request.GET.get('origemlong')
        destino = request.GET.get('destino')
        destinolat = request.GET.get('destinolat')
        destinolong = request.GET.get('destinolong')
        horario = request.GET.get('horario')

    return render(request, 'checkout.html', {'origem': origem, 'origemlat': origemlat, 'origemlong': origemlong, 'destino': destino, 'destinolat': destinolat, 'destinolong': destinolong, 'horario': horario})

def home(request):
    locais = Location.objects.all()
    routes = BusRoute.objects.all()

    return render(request, 'home.html', {'locais': locais, 'routes': routes})

def pesquisa(request):
    locais = Location.objects.all()
    routes = BusRoute.objects.all()
    if request.method == 'GET':
        origem_id = request.GET.get('origem')
        destino_id = request.GET.get('destino')
        data = request.GET.get('data')

        # Filtrando as rotas com base na origem e no destino selecionados
        rotas = BusRoute.objects.filter(origin_id=origem_id, destination_id=destino_id)

        # Poderia ser feita uma filtragem adicional para os horários usando a data

        return render(request, 'pesquisa.html', {'rotas': rotas, 'locais': locais, 'routes': routes})
