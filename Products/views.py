from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import cred

# Create your views here.

productAdded = False
contact = False


def home(request):
    products = Product.objects.all()
    return render(request, 'base.html', {'products': products})


def products(request):
    global productAdded
    products = Product.objects.all()
    productAdded = True
    return render(request, 'products.html', {'products': products, 'addedcart': productAdded})


def details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'details.html', {'product': product})


def contact(request):
    global contact
    contact = False
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        query = request.POST['query']

        message = MIMEMultipart()
        message['from'] = "PYSHOP SUPPORT TEAM"
        message['to'] = "vedantgune@gmail.com"
        message['subject'] = "Assistance Required !"
        message.attach(MIMEText((f"Name : { name }\n") +
                                (f"Email : { email }\n") +
                                (f"Phone : { phone }\n") +
                                (f"Message : { query }\n"))
                       )
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(cred.email, cred.password)
            smtp.send_message(message)
            contact = True

    return render(request, 'contact.html', {'contact': contact})


def about(request):
    return render(request, 'about.html')


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
        message = MIMEMultipart()
        message['from'] = f"Registration Successful!"
        message['to'] = email
        message['subject'] = f"{request.user} Registered Successfully!"
        message.attach(MIMEText(
            (f"Name : { name }\n") +
            (f"Username : { username }\n") +
            (f"Address : { email }\n") +
            (f"Phone No. : { phone }\n") +
            (f"State : { password }\n")
        ))

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(cred.email, cred.password)
            smtp.send_message(message)

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
    cartItems = Cart.objects.filter(user=request.user)
    total_items = 0
    total_price = 0

    for item in cartItems:
        total_items += item.quantity
        total_price += item.price * item.quantity

    return render(request, 'cart.html', {'addedcart': productAdded, 'CartProducts': cartItems, 'price': total_price, 'items': total_items})


def addcart(request):
    global productAdded
    if request.method == "POST":
        product_id = request.POST['id']
        product_quantity = request.POST['quantity']

        product = Product.objects.get(id=product_id)
        cartList = Cart.objects.filter(user=request.user)
        CartQuantity = int(product_quantity)

        if (Cart.objects.filter(cart_id=product_id).exists()):
            # cartList.quantity += CartQuantity
            mycart = Cart.objects.get(cart_id=product_id)
            mycart.quantity = CartQuantity + 1
            mycart.save()

        else:
            Cart(
                cart_id=product_id,
                title=product.title,
                quantity=CartQuantity,
                price=int(product.price),
                user=request.user
            ).save()

        messages.success(request, 'Cart item added successfully!')
        productAdded = True
        return redirect('products')


def removeitem(request, item_id):
    Cart.objects.filter(id=item_id).delete()
    return redirect('cart')


def purchase(request):
    cartItems = Cart.objects.filter(user=request.user)
    total_items = 0
    total_price = 0
    for item in cartItems:
        total_items += item.quantity
        total_price += item.price

    return render(request, 'purchase.html', {'CartProducts': cartItems, 'price': total_price, 'items': total_items})


def placed(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        add1 = request.POST['add1']
        add2 = request.POST['add2']
        state = request.POST['state']
        city = request.POST['city']
        zipcode = request.POST['zipcode']

        message = MIMEMultipart()
        message['from'] = f"ORDER PLACED SUCCESSFULLY!"
        message['to'] = f"vedantgune@gmail.com, {request.user.email}"
        message['subject'] = f"ORDER PLACED BY {name}"
        message.attach(MIMEText((f"Name : { name }\n") +
                                (f"Email : { email }\n") +
                                (f"Address : { add1 }\n") +
                                (f"Address 2 : { add2 }\n") +
                                (f"State : { state }\n") +
                                (f"City : { city }\n") +
                                (f"Postal Address : { zipcode }\n"))
                       )
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(cred.email, cred.password)
            smtp.send_message(message)
    return render(request, 'placed.html')
