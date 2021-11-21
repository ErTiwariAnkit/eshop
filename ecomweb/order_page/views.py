from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from home.models.customer import Customer
from django.views import View
from home.models.orders import Order

from home.models.product import Product
from home.models.orders import Order
from home.middlewares.auth import auth_middleware


class OrderView(View):

    def get(self, request):
        customerID = request.session.get('customer')
        if customerID:  # if user want to access order page without login redirec home page
            orders = Order.get_orders_by_customer(customerID)
            print(orders)
            return render(request, 'orders.html', {'orders': orders})
        else:
            return redirect('/')
