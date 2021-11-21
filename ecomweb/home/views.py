from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse

from home.models.customer import Customer
from .models.product import Product
from .models.category import Category
from django.views import View


# Create your views here.
class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        quantity1 = request.POST.get('quantity1')
        print('quantity is1', quantity1)
        print('remove is', remove)
        print('productid', product)
        cart = request.session.get('cart')
        if quantity1 != None:
            cart[product] = int(quantity1)
            print('cart is', cart)
        else:
            if cart:
                quantity = cart.get(product)
                print('quantity', quantity)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(product)
                        else:
                            cart[product] = quantity - 1
                    else:
                        cart[product] = quantity + 1

                else:
                    cart[product] = 1

            else:
                cart = {}
                cart[product] = 1

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('home')

    def get(self, request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    productID = request.GET.get('product')
    customerID = request.session.get('customer')
    customer = Customer.get_customer_by_id(customerID)
    print(customer)
    print('productid is', productID)
    if productID != None:
        products = Product.get_products_by_id(productID)
        print('products is', products)
        return render(request, 'product_detail.html', {'product': products})
    elif categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories
    data['customer'] = customer

    print('you are : ', request.session.get('email'))
    print(data)
    return render(request, 'index.html', data)
