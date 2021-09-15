from django.urls import path
from .views import ProfileView, UpdateView
from django.contrib.auth.models import User

urlpatterns =[ 
     path('<str:username>/', ProfileView, name = 'profile'),
     path('<str:username>/S/', UpdateView, name = 'update')

]