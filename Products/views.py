from django.shortcuts import render, HttpResponse, redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

isRegistered = False
isLoggedIn = False
isLoggedOut = False
activeUser = None


def home(request):
    return render(request, 'base.html', {'isRegistered': isRegistered, 'isLoggedIn': isLoggedIn, 'isLoggedOut': isLoggedOut, 'activeUser': activeUser})


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'details.html', {'product': product})


def contact(request):
    return HttpResponse("Hello, contacts")


def about(request):
    return HttpResponse("Hello, About")


def logout_user(request):
    global isLoggedIn, isRegistered, isLoggedOut
    logout(request)
    isLoggedIn = False
    isRegistered = False
    isLoggedOut = True
    return redirect('homepage')


def login_user(request):
    global isLoggedIn, activeUser
    if request.method == "POST":
        username = request.POST['loginusername']
        password = request.POST['loginpass']
        user = authenticate(request, username=username, password=password)
        activeUser = username
        if user is not None:
            login(request, user)
            isLoggedIn = True
        else:
            messages.error("Invalid User!")
        return redirect('homepage')


def signin_user(request):
    global isRegistered
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confpass = request.POST['conf_pass']

    # if (password == confpass) and (username != User.objects.get(username)):
        myuser = User.objects.create_user(username, email, password)
        myuser.name = name
        myuser.phone = phone
        myuser.save()
        isRegistered = True
        return redirect('homepage')

    else:
        return HttpResponse("404 Not Found!")


def dashboard(request):
    pass
