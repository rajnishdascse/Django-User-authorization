from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginForm, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logoutForm, name='logout'),
    


]