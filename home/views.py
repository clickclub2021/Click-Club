from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .forms import *

# superuser
# username - man
# password - man

def index(request):
    return render(request, 'index.html')

def team(request):
    return render(request, 'team.html')

def events(request):
    return render(request, 'events.html')
    
def calendar(request):
    return render(request, 'calendar.html')

def contact(request):
    return render(request, 'contact.html')

def pixellane2022(request):
    return render(request, 'pixellane2022.html')
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
  
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully")
            return render(request, 'contact.html', {'form' : form})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form' : form})

def userlogin(request):
    return render(request, 'login.html')

def usersignup(request):
    return render(request, 'signup.html')

def handlesignup(request):
    if request.method == 'POST':
        #post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        #check for incorrect inputs

        if len(username)>20:
            messages.error(request, "Username cannot exceed 20 characters")
            return redirect('usersignup')

        if not username.isalnum():
            messages.error(request, "Username must contain only letters and numbers")
            return redirect('usersignup')

        if password!=confirm_password:
            messages.error(request, "Incorrect password")
            return redirect('usersignup')

        #create user
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "You have successfully created your account!")
        return redirect('home')
    else:
        return HttpResponse("404 not found")

def handlelogin(request):
    if request.method == 'POST':
        lusername = request.POST['loginusername']
        lpassword = request.POST['loginpassword']

        user = authenticate(username=lusername, password=lpassword)

        if user is not None:
            login(request, user)
            messages.success(request,"You have succesfully logged in!")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials, please try again!")
            return redirect('userlogin')

def handlelogout(request):
    logout(request)
    messages.success(request, "You have been successfully Logged out!")
    return redirect('home')