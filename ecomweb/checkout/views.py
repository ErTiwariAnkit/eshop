from django.core.mail import send_mail
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View

from ecomweb.settings import EMAIL_HOST_USER
from home.models.customer import Customer
from home.models.orders import Order
from home.models.product import Product


def function1(request):
    return HttpResponse('checkout')


class CheckOut(View):
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        address = postData.get('address')
        postal = postData.get('postal')
        city = postData.get('city')
        customerID = request.session.get('customer')
        cart = request.session.get('cart')
        cart_list = list(cart.keys())
        products = []
        for productID in cart_list:
            product = Product.get_products_by_id(int(productID))
            products.append(product)
        # print(address, phone, customerID, cart, products)
        order_ids = []
        for product in products:
            order = Order(customer=Customer(id=customerID),
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
            # print('product quantity is', product.quantity)
            product.quantity -= cart.get(str(product.id))
            print('product quantity is after reduce', product.quantity)
            if product.quantity <= 0:
                product.avail = False
            product.save()
            order.save()
            order_id = order.get_order_id()
            order_ids.append(order_id)
        # customerID = request.session.get('customer')
        customer = Customer.get_customer_by_id(customerID)
        self.send_mail1(customer.first_name, customer.last_name, customer.email, order_ids)
        print(order_ids)

        request.session['cart'] = {}
        return render(request, 'final.html', {'id1': order_ids})

    def send_mail1(self, first_name, last_name, email, order_ids):
        subject = 'welcome to Ankit Tiwari E-commerce Websites'
        message = f'Hi {first_name} {last_name}, Your order has been done Your order id is {order_ids}'
        email_from = EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)

    def get(self, request):
        products = []
        customerID = request.session.get('customer')
        cart = request.session.get('cart')
        # print(len(cart))
        if customerID and len(cart):  # if user want to access checkout page without login redirec home page
            address = Customer.get_customer_default_address(request)
            # print('address is', address)
            product_ids = list(request.session.get('cart').keys())
            for product_id in product_ids:
                product = Product.get_products_by_id(product_id)
                products.append(product)
            return render(request, 'checkout.html',
                          {'address': address, 'products': products, 'cart_quantity': sum(cart.values())})
        else:
            return render(request, 'cart.html', {'error': 'Your cart is empty click continue shopping for Buy item'})
