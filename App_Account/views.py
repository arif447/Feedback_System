from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from App_Account.forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,  login, logout


# Create your views here.
def home(request):
    return render(request, 'home.html', context={})


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Account:signin'))
    diction = {'form': form}
    return render(request, 'accounts/signup.html', context=diction)


def signin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Account:home'))
    diction = {'form': form}
    return render(request, 'accounts/login.html', context=diction)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Account:signin'))


