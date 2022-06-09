from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='homepage'),
    path("about/", views.about, name='about'),
    path("products/", views.products, name='products'),
    path("contact/", views.contact, name='contact'),
    path("products/<int:product_id>", views.details, name='detail'),
]
