from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .tweets.forms import TweetForm
from .tweets.models import Tweet


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username= data['username'], password= data['password'])
            user.profile.bio = data['bio']
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def Profile(request, username):
    if request.method == 'GET':
        form = TweetForm
        return render(request, 'profile.html', {'form': form})

    elif request.method == 'POST':
        form = TweetForm( data = request.POST )
        if form.is_valid():
            data = form.cleaned_data
            user = request.user
            tweet = Tweet.objects.create(tweet = data['tweet'])
            user.profile.tweets.add(tweet)

            redirect_url = request.POST.get('redirect', '/')
            return redirect(redirect_url)

def Follow(request, username):
    if request.method == 'GET':
        user = User.objects.get(username = username)
        user.profile.followers.add(request.user.profile)
        return redirect('/'+ user.username + '/', permanent = True)





