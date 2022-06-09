from django.shortcuts import render, HttpResponse
from .models import Product
# Create your views here.


def home(request):
    filterProd = Product.objects.all()
    filterList = ', '.join(filterProd)
    print(filterList)
    return render(request, 'base.html', {'filterList': filterList})


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
