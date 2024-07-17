from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate ,login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import numpy as np
import pickle

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
            return redirect('/analysis',name='username')
        
    return render(request, 'login.html')

def register(request):

    if request.method != "POST":
        return render(request, 'register.html')

    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    gender = request.POST.get('gender')

    user = User.objects.filter(username=username)


    if user.exists():
        messages.info(request, "Username Already Exists")
        return redirect('/register')

    elif User.objects.filter(email=email).exists():
        messages.info(request, "Email Already Taken")
        return redirect('/register')

    user = User.objects.create(
        first_name= first_name, 
        last_name= last_name,
        username=username,
        email=email,
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

def predict(request):
    if request.method == 'POST':
        pregnancies = request.POST['pregnancies']
        glucose = request.POST['glucose']
        blood = request.POST['blood']
        skin = request.POST['skin']
        insulin = request.POST['insulin']
        bmi = float(request.POST['bmi'])
        dia = float(request.POST['dia'])
        age = request.POST['age']

        with open('classifier.pkl','rb') as f:
            classifier = pickle.load(f)
        
        with open('scaler.pkl','rb') as f:
            scaler = pickle.load(f)

        input_data=(pregnancies, glucose, blood, skin, insulin, bmi, dia, age)
        input_data_as_nuumpy_array=np.asarray(input_data)
        input_data_reshaped=input_data_as_nuumpy_array.reshape(1,-1)
        std_data=scaler.transform(input_data_reshaped)
        prediction=classifier.predict(std_data)
        if(prediction[0]==0):
            return render(request, 'result1.html')
        else:
            return render(request,'result2.html')
    else:
        return render(request, 'analysis.html')