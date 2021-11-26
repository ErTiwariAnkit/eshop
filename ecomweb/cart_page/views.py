from django.shortcuts import render, redirect
from django.views import View

from home.models.product import Product


class Cart(View):
    def get(self, request):
        products = []
        customerID = request.session.get('customer')
        if customerID:  # if user want to access cart page without login redirec home page
            product_ids = list(request.session.get('cart').keys())
            for product_id in product_ids:
                product = Product.get_products_by_id(product_id)
                products.append(product)

                print(products)
            return render(request, 'cart.html', {'products': products})
        else:
            return redirect('/')

    def post(self, request):
        productID = request.POST.get('product')
        reduce = request.POST.get('-')
        product=Product.get_products_by_id(productID)
        remove = request.POST.get('remove')
        print('remove is', remove)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(productID)
            if quantity:
                if reduce:
                    if quantity <= 1:
                        cart.pop(productID)
                    else:
                        cart[productID] = quantity - 1
                elif remove:
                    cart[productID] = 0
                    cart.pop(productID)
                else:
                     if quantity!=product.quantity:
                        cart[productID] = quantity + 1

            else:
                cart[productID] = 1
        else:
            cart = {}
            cart[productID] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('cart')
