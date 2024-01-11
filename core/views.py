from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def analysis(request):
    return render(request, 'analysis.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def result1(request):
    return render(request, 'result1.html')

def result2(request):
    return render(request, 'result2.html')