from django.urls import path

from .views import views
from .views import views1
from .views import views2

urlpatterns = [
    path('', views.Password_reset.as_view(), name='password_reset'),
    path('password_reset_done/', views1.Password_reset.as_view(), name='password_reset_done'),
    path('password_reset_confirm/', views2.Password_reset.as_view(), name='password_reset_confirm'),
]
