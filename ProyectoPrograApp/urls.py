from django.urls import path
from ProyectoPrograApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name ="login"),
    path('galeria',views.galeria,name ="galeria"),
    path('registro',views.registro,name='registro'),
    path('cargar',views.cargar,name ="cargar"),
    path('logout',views.logoutUser,name ="logout"),
    path('img',views.shit,name='img'),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)