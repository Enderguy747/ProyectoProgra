from django import forms
from .models import Usuario, Foto, Etiqueta


class FormRegistro(forms.ModelForm):
     contraseña = forms.CharField(widget=forms.PasswordInput())
     class Meta:
        model = Usuario
        fields = '__all__'
        
