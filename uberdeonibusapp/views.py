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
        destino = request.GET.get('destino')
        horario = request.GET.get('horario')

    return render(request, 'checkout.html', {'origem': origem, 'destino': destino, 'horario': horario})

def home(request):
    locais = Location.objects.all()
    routes = BusRoute.objects.all()

    return render(request, 'home.html', {'locais': locais, 'routes': routes})

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


        return render(request, 'pesquisa.html', {'locais': locais,'rotas':rotas, 'dinamico': dinamico})
