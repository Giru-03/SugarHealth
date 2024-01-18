from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

@login_required(login_url="/login")
def about(request):
    return render(request, 'about.html')

@login_required(login_url="/login")
def analysis(request):
    return render(request, 'analysis.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username")
            return redirect('/login')
        
        user = authenticate(username = username, password = password)

        if user is None:    
            messages.info(request, "Invalid Password")
            return redirect('/login')
        
        else:
            login(request,user)        
            return redirect('/analysis')
        
    return render(request, 'login.html')

def register(request):

    if request.method != "POST":
        return render(request, 'register.html')

    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.filter(username=username)


    if user.exists():
        messages.info(request, "Username Already Exists")
        return redirect('/register')


    user = User.objects.create(
        first_name= first_name, 
        last_name= last_name,
        username=username,
        email=email
        # password=password  we cant directly add password so we have encrypt it
        )

    user.set_password(password)    # this method is already thier in django
    user.save()
    messages.info(request, "Account created successfully")

    return redirect('/login')

def result1(request):
    return render(request, 'result1.html')

def result2(request):
    return render(request, 'result2.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

@login_required(login_url="/login")
def contact(request):
    return render(request, 'contact.html')