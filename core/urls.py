from django.contrib import admin
from django.urls import path
from core import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("analysis", views.analysis, name='analysis'),
    path("login", views.login, name='login'),
    path("register", views.register, name='register'),
    path("result1", views.result1, name='result1'),
    path("result2", views.result2, name='result2'),
    path("contact", views.contact, name='contact')
]
