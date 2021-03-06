"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("team", views.team, name='team'),
    path("events", views.events, name='events'),
    path("calendar", views.calendar, name='calendar'),
    path("contact", views.contact, name='contact'),
    path("events/pixellane2022", views.pixellane2022, name='pixellane2022'),
    path("login", views.userlogin, name='login'),
    path("signup", views.usersignup, name='signup'),
    path("signupinfo", views.handlesignup, name='signupinfo'),
    path("logininfo", views.handlelogin, name='logininfo'),
    path("logout", views.handlelogout, name='handlelogout')
]