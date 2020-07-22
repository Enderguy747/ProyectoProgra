from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'ProyectoPrograApp/index.html')

def registro(request):
    return render(request, 'ProyectoPrograApp/registro.html')

def login(request):
    return render(request, 'ProyectoPrograApp/login.html')

def galeria(request):
    return render(request, 'ProyectoPrograApp/galeria.html')

def cargar(request):
    return render(request, 'ProyectoPrograApp/cargar.html')
