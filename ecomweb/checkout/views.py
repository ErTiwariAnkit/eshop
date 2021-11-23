from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from ecomweb.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from django.contrib.auth.hashers import check_password
from home.models.customer import Customer
from django.views import View

from home.models.product import Product
from home.models.orders import Order


def function1(request):
    return HttpResponse('checkout')


class CheckOut(View):
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        address = request.POST.get('address')
        address_all = request.POST.get('address')
        postal = request.POST.get('postal')
        city = request.POST.get('city')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        cart_list = list(cart.keys())
        products = []
        for cart1 in cart_list:
            products1 = Product.get_products_by_id(int(cart1))
            products.append(products1)
        print(address, phone, customer, cart, products)
        print('cart is')
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
            'address': address,
            'postal': postal,
            'city': city,

        }
        id1 = []
        for product in products:
            print(cart)
            # print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          first_name=first_name,
                          last_name=last_name,
                          email=email,
                          postal=postal,
                          city=city,
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id))
                          )
            print('product quantity is', product.quantity)
            product.quantity -= cart.get(str(product.id))
            print('product quantity is after reduce', product.quantity)
            if product.quantity <= 0:
                product.avail = False
            product.save()
            order.save()
            order_id = order.get_order_id()
            id1.append(order_id)
        customerID = request.session.get('customer')
        customer = Customer.get_customer_by_id(customerID)
        self.send_mail1(customer.first_name, customer.last_name, customer.email)
        print(id1)

        request.session['cart'] = {}
        # id=request.session['order_id']=Order.id
        # print(id)

        return render(request, 'final.html', {'id1': id1})

    def send_mail1(self, first_name, last_name, email):
        subject = 'welcome to Ankit Tiwari E-commerce Websites'
        message = f'Hi {first_name} {last_name}, Your order has been done'
        email_from = EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)

    def get(self, request):
        products = []
        customerID = request.session.get('customer')
        cart = request.session.get('cart')
        print(len(cart))
        if customerID:  # if user want to access checkout page without login redirec home page
            address = Customer.get_customer_default_address(request)
            print('address is', address)
            ids = list(request.session.get('cart').keys())
            for id in ids:
                products1 = Product.get_products_by_id(id)
                products.append(products1)
            return render(request, 'checkout.html',
                          {'address': address, 'products': products, 'cart_quantity': sum(cart.values())})
        else:
            return redirect('/')
