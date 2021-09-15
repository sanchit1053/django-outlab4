from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.models import User

def ExploreView(requests):
    context = {'users' : User.objects.all()}
    return render(requests, 'explore.html', context)