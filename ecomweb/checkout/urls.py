from django.urls import path
from . import views

urlpatterns = [
    path('', views.CheckOut.as_view(), name='checkout')
]
