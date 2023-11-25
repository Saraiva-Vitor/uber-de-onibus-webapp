from .models import *
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CadastroForm
from django.core.management import call_command

# Create your views here.
@csrf_protect
def logout_view(request):
    logout(request)
    return redirect('home')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['nome']
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Chama o comando createuser para criar o usuário no Django Admin
            call_command("createuser", user.email, form.cleaned_data['password'], user.first_name)

            messages.success(request, 'Cadastro realizado com sucesso. Faça o login.')
            return redirect('login')
        else:
            messages.error(request, 'Erro no formulário. Corrija os campos destacados.')

    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Tenta autenticar o usuário usando email ou CPF
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
 


        return render(request, 'pesquisa.html', {'locais': locais,'rotas':rotas, 'dinamico': dinamico,'nome_rota':rotas[0].name})
