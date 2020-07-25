from django.urls import path
from ProyectoPrograApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name="index"),
   # path('login',views.login,name ="login"),
    path('galeria',views.galeria,name ="galeria"),
    path('cargar',views.cargar,name ="cargar"),
    path('registrarUsuario',views.Form_registro.registro,name='registrarUsuario'),
    path('guardarUsuario',views.Form_registro.ProcesarForm,name='guardarUsuario')
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)