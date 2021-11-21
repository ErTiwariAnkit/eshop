from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from home.models.customer import Customer
from django.views import View
from home.models.product import Product


class Cart(View):
    def get(self, request):
        products = []
        customerID = request.session.get('customer')
        if customerID:  # if user want to access cart page without login redirec home page
            ids = list(request.session.get('cart').keys())
            for id in ids:
                products1 = Product.get_products_by_id(id)
                products.append(products1)

                print(products)
            return render(request, 'cart.html', {'products': products})
        else:
            return redirect('/')

    def post(self, request):
        product = request.POST.get('product')
        reduce = request.POST.get('reduce')
        remove = request.POST.get('remove')
        print('remove is', remove)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if reduce:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                elif remove:
                    cart[product] = 0
                    cart.pop(product)
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('cart')
