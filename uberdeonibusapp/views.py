from django.shortcuts import render
from .models import Location, BusRoute

# Create your views here.
def home(request):
    locations = Location.objects.all()
    routes = BusRoute.objects.all()
    selected_destination = None

    if request.method == 'POST':
        selected_origin_id = request.POST.get('origin')
        selected_destination_id = request.POST.get('destination')

        # Se a origem e o destino forem selecionados, obtenha o destino selecionado
        if selected_origin_id and selected_destination_id:
            selected_destination = Location.objects.get(
                id=selected_destination_id)

    return render(request, 'home.html', {'routes': routes, 'locations': locations, 'selected_destination': selected_destination})


def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')