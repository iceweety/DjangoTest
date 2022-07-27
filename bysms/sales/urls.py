# coding=utf-8
from django.contrib import admin
from django.urls import path
from sales.views import listorders
from sales.views import listcustomers
urlpatterns = [

    path('orders/',listorders),
    path('customers/',listcustomers)
]

