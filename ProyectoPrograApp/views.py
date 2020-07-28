from django.core.files.uploadhandler import MemoryFileUploadHandler
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import Foto, Etiqueta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from.forms import CreateUserForm, TagForm, ImgForm

# Create your views here.


def registro(request):
    if request.user.is_authenticated:
        return redirect('galeria')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

    context = {'form': form}
    return render(request, 'ProyectoPrograApp/registro.html', context)


def index(request):
    return render(request, 'ProyectoPrograApp/index.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('galeria')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('galeria')
            else:
                messages.info(request, 'Usuario y/o Contraseña incorrectos')
                return render(request, 'ProyectoPrograApp/login.html')
    return render(request, 'ProyectoPrograApp/login.html')


def logoutUser(request):
    logout(request)

    return redirect('login')


@login_required(login_url='login')
def galeria(request):
    id = request.user
    foto = Foto.objects.filter(idUsuario_id=id)
    context = {'fotos': foto}
    return render(request, 'ProyectoPrograApp/galeria.html', context)


@login_required(login_url='login')
def cargar(request):
    form = ImgForm()
    etiqueta = Etiqueta.objects.all()
    if request.method == 'POST':
        form = ImgForm(request.POST,request.FILES )
        if form.is_valid():
            form.save()
            return redirect('galeria')
    Etiqueta.objects.all()
    context = {'etiqueta': etiqueta , 'form':form}
    return render(request, 'ProyectoPrograApp/cargar.html', context)


@login_required(login_url='login')
def shit(request):
    form = ImgForm()
    user = request.user
    if request.method == 'POST':

        form = ImgForm(request.POST , request.FILES )
        if form.is_valid():
            form.save()
            return redirect('galeria')

    context = {'form': form}
    return render(request, 'ProyectoPrograApp/try.html', context)


@login_required(login_url='login')
def guardarEtiquetas(request):
    
    
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'ProyectoPrograApp/etiqueta.html', context)
