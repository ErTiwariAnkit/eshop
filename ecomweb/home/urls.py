from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('store', views.store, name='store'),
    path('login/', include('login.urls')),
    path('logout/', include('logout.urls')),
    path('reset_password/',include('forget_password.urls')),
    path('orders/', include('order_page.urls')),
    path('profile/', include('profile_page.urls')),
    path('registration/', include('registration.urls')),
    path('cart/', include('cart_page.urls')),
    path('checkout/', include('checkout.urls')),
]
