from django.shortcuts import render, redirect
from django.views import View

from home.models.orders import Order


class OrderView(View):

    def get(self, request):
        customerID = request.session.get('customer')
        if customerID:  # if user want to access order page without login redirec home page
            orders = Order.get_orders_by_customer(customerID)
            print(orders)
            return render(request, 'orders.html', {'orders': orders})
        else:
            return redirect('/')
