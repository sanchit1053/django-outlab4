from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import profiles,repository
import requests
from django.contrib.auth.models import User
from datetime import *
from django.utils import timezone
import pytz

def ProfileView(request,username):
    context = {'pro': User.objects.get(username = username)}
    return render(request, 'profile.html',context)


def UpdateView(request,username):
    user = User.objects.get(username = username)
    response = requests.get(f" https://api.github.com/users/{username}")
    response = response.json()
    f = "%Y-%m-%dT%H:%M:%SZ"
    tz = pytz.timezone('Asia/Kolkata')
    if response.get('followers') != None:
        user.profiles.numOfFollowers = response['followers']
        #now = datetime.now()
        #now = now.strftime("%b %-d,%Y %-I:%M%p")
        now = datetime.now(tz)
        #now.setHours(now.getHours()+ 5)
        #now.setMinutes(now.getMinutes()+30)
        #now = now + timedelta(hours = 5, minutes = 30)
        user.profiles.lastUpdated = now
        user.profiles.save()
        #user.profiles.lastUpdated = datetime.strptime(response['updated_at'] , f) 

    profile = user.profiles
    response2 = requests.get(f" https://api.github.com/users/{username}/repos")
    response2 = response2.json()

    if response:
        for repo in response2:
            if repo.get('name'):
                name = repo['name']
                stars = repo['stargazers_count']
                t,c = repository.objects.update_or_create(profiles = profile, name = name , defaults={'name' : name, 'stars' : stars})
    context = {'pro':user}
    return render(request, 'profile.html', context) 