from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("analysis", views.analysis, name='analysis'),
    path("login", views.login_page, name='login_page'),
    path("logout", views.logout_page, name='logout_page'),
    path("register", views.register, name='register'),
    path("result1", views.result1, name='result1'),
    path("result2", views.result2, name='result2'),
    path("home", views.index, name='home'),
    path("contact", views.contact, name='contact'),
    path("predict", views.predict, name='predict'),
]
