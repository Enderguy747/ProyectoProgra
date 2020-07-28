from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.forms import ModelForm
from.models import Etiqueta


class CreateUserForm(UserCreationForm):
    class Meta:
       model = User
       fields = ['username','email','password1','password2']
        

class TagForm(ModelForm):
    class Meta:
        model = Etiqueta
        fields = '__all__'
    