from django.contrib import admin
from django.urls import path
from core import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("analysis", views.analysis, name='analysis'),
    path("login", views.login, name='login')
]
