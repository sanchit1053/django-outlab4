from django.urls import path
from .views import ExploreView

urlpatterns =[ 
     path('explore/', ExploreView, name = 'explore'),

]