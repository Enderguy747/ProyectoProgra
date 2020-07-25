from django.shortcuts import render
from django.http import HttpRequest
from .forms import FormRegistro
# Create your views here.


class Form_registro(HttpRequest):

    def registro(request):
        registro = FormRegistro()
        return render(request, 'ProyectoPrograApp/registro.html', {"form": registro})

    def ProcesarForm(request):
        registro = FormRegistro(request.POST)
        if registro.is_valid():
            registro.save()
            registro = FormRegistro()
        return render(request, 'ProyectoPrograApp/registro.html',{"form":registro,"mensaje":"ok"})


def index(request):
    return render(request, 'ProyectoPrograApp/index.html')

"""
def login(request):
    return render(request, 'ProyectoPrograApp/login.html')
"""

def galeria(request):
    return render(request, 'ProyectoPrograApp/galeria.html')


def cargar(request):
    return render(request, 'ProyectoPrograApp/cargar.html')
