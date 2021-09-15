from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import profiles,repository
import requests
from django.contrib.auth.models import User
from datetime import *

def ProfileView(request,username):
    context = {'user': User.objects.get(username = username)}
    return render(request, 'profile.html',context)


def UpdateView(request,username):
    user = User.objects.get(username = username)
    response = requests.get(f" https://api.github.com/users/{username}")
    response = response.json()
    f = "%Y-%m-%dT%H:%M:%SZ"
    if response:
        user.profiles.numOfFollowers = response['followers']
        user.profiles.lastUpdated = datetime.strptime(response['updated_at'] , f) 

    profile = user.profiles
    response2 = requests.get(f" https://api.github.com/users/{username}/repos")
    response2 = response2.json()
    if response2:
        for repo in response2:
            name = repo['name']
            stars = repo['stargazers_count']
            t,c = repository.objects.update_or_create(profiles = profile, name = name , defaults={'name' : name, 'stars' : stars})
    context = {'user':user}
    return render(request, 'profile.html', context) 