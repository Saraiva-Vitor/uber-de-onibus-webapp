from django.shortcuts import render
from .models import Location, BusRoute

# Create your views here.
def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

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
