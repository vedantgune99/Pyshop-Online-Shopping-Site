from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'base.html')


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
    logout(request)
    return redirect('homepage')


def login_user(request):
    if request.method == "POST":
        username = request.POST['loginusername']
        password = request.POST['loginpass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error("Invalid User!")
        return redirect('homepage')


def signin_user(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confpass = request.POST['conf_pass']

    if (password == confpass):
        myuser = User.objects.create_user(username, email, password)
        myuser.name = name
        myuser.phone = phone
        myuser.save()
        return redirect('homepage')

    else:
        return HttpResponse("404 Not Found!")


def dashboard(request):
    pass


def cart(request):
    CartProducts = Cart.objects.all()
    return render(request, 'cart.html', {'CartProducts': CartProducts})


def addcart(request):
    if request.method == "POST":
        product_id = request.POST['id']
        cart_item = Product.objects.get(id=product_id)
        Cart(title=cart_item.title, image=cart_item.image,
             price=cart_item.price, user=request.user).save()
        return redirect('products')
