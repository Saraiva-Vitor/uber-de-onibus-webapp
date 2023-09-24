from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')

def home2(request):
    return render(request, 'home2.html')

def teste(request):
    return render(request, 'teste.html')