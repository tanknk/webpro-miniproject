from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.forms import UserCreationForm
from authen.forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", { 'form' : form })