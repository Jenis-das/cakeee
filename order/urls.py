from django.contrib import admin
from django.urls import path,include
from order import views

urlpatterns = [
    path("", views.order , name="order")
]


