from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('store', views.store, name='store'),
    path('login/', include('login.urls')),
    path('logout/', include('logout.urls')),
    path('orders/', include('order_page.urls')),
    path('product_detail/', include('product_detail_page.urls')),
    path('profile/', include('profile_page.urls')),
    path('registration/', include('registration.urls')),
    path('cart/', include('cart_page.urls')),
    path('checkout/', include('checkout.urls')),
    path('final/', include('final.urls')),
]
