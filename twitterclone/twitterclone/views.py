from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .tweets.forms import TweetForm
from .tweets.models import Tweet


class SignUp(View):
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username= data['username'], password= data['password'])
            user.profile.bio = data['bio']
            login(request, user)
            return redirect('/')

    def get(self, request, *args, **kwargs):
        form = SignUpForm()

        return render(request, 'signup.html', {'form': form})
            


# def SignUp(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = User.objects.create_user(username= data['username'], password= data['password'])
#             user.profile.bio = data['bio']
#             login(request, user)
#             return redirect('/')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

class Profile(View):
    def get(self, request, *args, **kwargs):
        form = TweetForm
        return render(request, 'profile.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TweetForm( data = request.POST )
        if form.is_valid():
            data = form.cleaned_data
            user = request.user
            tweet = Tweet.objects.create(tweet = data['tweet'])
            user.profile.tweets.add(tweet)

            redirect_url = request.POST.get('redirect', '/')
            return redirect(redirect_url)






# def Profile(request, username):
#     if request.method == 'GET':
#         form = TweetForm
#         return render(request, 'profile.html', {'form': form})

#     elif request.method == 'POST':
#         form = TweetForm( data = request.POST )
#         if form.is_valid():
#             data = form.cleaned_data
#             user = request.user
#             tweet = Tweet.objects.create(tweet = data['tweet'])
#             user.profile.tweets.add(tweet)

#             redirect_url = request.POST.get('redirect', '/')
#             return redirect(redirect_url)


class Follow(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username = username)
        user.profile.followers.add(request.user.profile)
        return redirect('/'+ user.username + '/', permanent = True)


# def Follow(request, username):
#     if request.method == 'GET':
#         user = User.objects.get(username = username)
#         user.profile.followers.add(request.user.profile)
#         return redirect('/'+ user.username + '/', permanent = True)

class Unfollow(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=username)
        user.profile.followers.remove(request.user.profile)

        return redirect('/' + user.username + '/')


# def unfollow(request, username):
#     user = User.objects.get(username=username)
#     user.profile.followers.remove(request.user.profile)

#     return redirect('/' + user.username + '/')




