from django.shortcuts import redirect, render

from home.models.customer import Customer
from home.models.orders import Order


def profile_page(request):
    customerID = request.session.get('customer')
    customer = Customer.get_customer_by_id(customerID)
    if customerID:
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'profile.html', {'customer': customer, 'orders': orders})
    else:
        return redirect('/')
