from django.shortcuts import render

from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import re
from django.contrib import messages

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'authentication/home.html')
    else:
        return render(request, 'authentication/signin.html')

EMAIL_REGIX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-copyZ0-9._-]+\.[a-zA-Z]+$')

def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        if not EMAIL_REGIX.match(request.POST["email"]):
            messages.add_message(request, messages.ERROR, "invalid email fromat! ex: test@test.com")
            return render(request, 'authentication/signup.html', context)     
        if User.objects.filter(username=request.POST["name"]).count() > 0:
            messages.add_message(request, messages.ERROR, "A user with this name already exixts!")
            return render(request, 'authentication/signup.html', context)   
        if User.objects.filter(email=request.POST["email"]).count() > 0:
            messages.add_message(request, messages.ERROR, "A user with this email already exixts!")
            return render(request, 'authentication/signup.html', context)
        if request.POST["password"] != request.POST["confirm_password"]:
            messages.add_message(request, messages.ERROR, "password and password comfirmation must match!")
            return render(request, 'authentication/signup.html', context)

        user = User.objects.create_user(name_r, email_r, password_r, )
        if user:
            login(request, user)
            return render(request, 'authentication/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'authentication/signup.html', context)
    else:
        return render(request, 'authentication/signup.html', context)


def signin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            login(request, user)
            # username = request.session['username']
            context["user"] = name_r
            context["id"] = request.user.id
            return render(request, 'authentication/success.html', context)
            # return HttpResponseRedirect('success')
        else:
            messages.add_message(request, messages.ERROR, "invalid username or password!")
            return render(request, 'authentication/signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'authentication/signin.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'authentication/signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'authentication/success.html', context)


def services_page(request):
    return render(request, 'authentication/services.html')

def gallery_page(request):
    return render(request, 'authentication/gallery.html')

def about_page(request):
    return render(request, 'authentication/about.html')

def contact_page(request):
    return render(request, 'authentication/contact.html')