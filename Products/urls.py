from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='homepage'),
    path("about/", views.about, name='about'),
    path("products/", views.products, name='products'),
    path("contact/", views.contact, name='contact'),
    path("products/details/<int:product_id>", views.details, name='details'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("signin/", views.signin_user, name='signin'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("products/addcart/", views.addcart, name='addcart'),
    path("remove_item/<int:item_id>", views.removeitem, name="removeitem"),
    path("cart/", views.cart, name='cart'),
    path("purchase/", views.purchase, name='purchase'),
    path("placed/", views.placed, name='placed'),
    path("success/", views.success, name='success'),
]
