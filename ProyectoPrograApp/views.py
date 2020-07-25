from django.shortcuts import render
from django.http import HttpRequest
from .forms import FormRegistro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Foto

# Create your views here.

def registro(request):
        form = FormRegistro()

        if request.method == 'POST':
            form = FormRegistro(request.POST)
            if form.is_valid():
                form.save()
        context = {'form':form}
        return render(request, 'ProyectoPrograApp/registro.html',context)



def index(request):
    return render(request, 'ProyectoPrograApp/index.html')


def login(request):
    return render(request, 'ProyectoPrograApp/login.html')


def galeria(request):

    return render(request, 'ProyectoPrograApp/galeria.html')


def cargar(request):
    return render(request, 'ProyectoPrograApp/cargar.html')


def shit(request):
    fotos = Foto.objects.all()
    return render(request,'ProyectoPrograApp/try.html',{'fotos':foto})