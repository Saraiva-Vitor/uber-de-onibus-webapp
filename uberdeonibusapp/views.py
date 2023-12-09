from django.shortcuts import render
from .models import *
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        email = request.POST.get('email')
        confirma_email = request.POST.get('confirma_email')
        telefone = request.POST.get('telefone')
        password = request.POST.get('password')
        confirma_password = request.POST.get('confirma_password')
        cep = request.POST.get('cep')
        endereco = request.POST.get('endereco')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        estado = request.POST.get('estado')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')

        if email := confirma_email:
            if password := confirma_password:
                CustomUser = get_user_model()
                try:
                    user = CustomUser.objects.create_user(username=email, password=password)
                    user.nome = nome
                    user.cpf = cpf
                    user.data_nascimento = data_nascimento
                    user.telefone = telefone
                    user.cep = cep
                    user.endereco = endereco
                    user.numero = numero
                    user.complemento = complemento
                    user.estado = estado
                    user.bairro = bairro
                    user.cidade = cidade
                    user.save()
                    return redirect('login') 
                except Exception as e:
                    return render(request, 'cadastro.html', {'error_message': 'Erro ao criar usuário. Tente novamente.'})
            else: 
                return render(request, 'cadastro.html', {'error_message': 'Senhas Não Conferem. Tente novamente.'})
        else:
            return render(request, 'cadastro.html', {'error_message': 'Emails Não Conferem. Tente novamente.'})
    return render(request, 'cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        return redirect('home') 
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


        return render(request, 'pesquisa.html', {'locais': locais,'rotas':rotas, 'dinamico': dinamico})
    
def pagamento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        numero_cartao = request.POST.get('card_number')
        cvc_cartao = request.POST.get('cvc')
        parcelamento = request.POST.get('times')
    return render(request, 'pagamento.html')
