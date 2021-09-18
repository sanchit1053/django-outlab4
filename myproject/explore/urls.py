from django.urls import path
from .views import ExploreView

urlpatterns =[ 
     path('', ExploreView, name = 'explore'),

]