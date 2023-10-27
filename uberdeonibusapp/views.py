from django.shortcuts import render
from .models import Location, BusRoute

# Create your views here.
def home(request):
    locations = Location.objects.all()
    routes = BusRoute.objects.all()

    return render(request, 'home.html', {'routes': routes, 'locations': locations})


def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def pesquisa(request):
    locations = Location.objects.all()
    
    return render(request, 'pesquisa.html', {'locations': locations})
