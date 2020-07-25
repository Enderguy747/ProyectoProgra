from django.urls import path
from .views import Login

urlpatterns=[
path('accounts/login/',Login.as_view(),name='login'),
]