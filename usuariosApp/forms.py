from django.contrib.auth.forms import AuthenticationForm


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(FormularioLogin, *args, **kwargs)
        self.files['username'].widget.attrs['class'] = 'form-control'
        self.files['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.files['password'].widget.attrs['class'] = 'form-control'
        self.files['password'].widget.attrs['placeholder'] = 'Contraseña'
        
