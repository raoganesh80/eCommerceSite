from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('login/', views.login, name='LogIn'),
    path('signup/', views.signup, name='SignUp'),
    path('myprofile/', views.myprofile, name='MyProfile'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('search/', views.search, name='Search'),
    path('productview/', views.productView, name='ProductView'),
    path('checkout/', views.checkout, name='Checkout'),
]