from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path("", views.index, name='home'),
    path("home", views.index, name='home'),
    path("about", views.about, name='about'),
    path("cakes", views.cakes, name='cakes')
]
