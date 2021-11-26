from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View

from home.models.customer import Customer
from .models.category import Category
from .models.product import Product


# Create your views here.
class Index(View):

    def post(self, request):
        productID = request.POST.get('product')
        remove = request.POST.get('remove')
        quantity1 = request.POST.get('quantity1')
        product = Product.get_products_by_id(productID)
        # print('quantity is1', quantity1)
        # print('remove is', remove)
        # print('productid', product)
        cart = request.session.get('cart')
        if quantity1 != None:
            print(product.quantity)
            print(quantity1)
            if product.quantity>=int(quantity1):
                cart[productID] = int(quantity1)
                print('cart is', cart)
            else:
                cart = request.session.get('cart')
                print('cart product detail is', sum(cart.values()))
                if cart:
                    sum1 = sum(cart.values())
                    sum1 = str(sum1) + ' items'
                else:
                    sum1 = 'is empty'
                return render(request,'product_detail.html',{'error':'Select quantity is not be more than product quantity','product':product,'cart_value':sum1})
        else:
            if cart:
                quantity = cart.get(productID)
                # print('quantity', quantity)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(productID)
                        else:
                            cart[productID] = quantity - 1
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
        return redirect('home')

    def get(self, request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


def store(request):
    from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent
    print(BASE_DIR)
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    productID = request.GET.get('product')
    customerID = request.session.get('customer')
    sort = request.GET.get('drop1')
    customer = Customer.get_customer_by_id(customerID)
    data = {}
    data['categories'] = categories
    data['customer'] = customer
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
        data['products'] = products

        # print('you are : ', request.session.get('email'))
        # print(data)
        return render(request, 'index.html', data)
    else:
        products = Product.get_all_products()
        if sort != None:
            if int(sort) == 1:  # sort name
                print('category id sort', categoryID)
                products_sort_name = Product.get_product_sort_name()
                data['products_sort_name'] = products_sort_name

            elif int(sort) == 2:  # sort price
                products_sort_price = Product.get_product_sort_price()
                data['products_sort_name'] = products_sort_price

            return render(request, 'sort_by_name.html', data)
        elif 'search' in request.GET:
            search_term = request.GET['search']
            search_products = Product.get_search_product(search_term=search_term, categoryid=categoryID)
            data['products'] = search_products
            # print('search product',search_products)
            return render(request, 'index.html', data)
        elif productID != None:
            product = Product.get_products_by_id(productID)
            # print('products is', products)
            cart = request.session.get('cart')
            print('cart product detail is', sum(cart.values()))
            if cart:
                sum1 = sum(cart.values())
                sum1 = str(sum1) + ' items'
            else:
                sum1 = 'is empty'
            return render(request, 'product_detail.html', {'product': product, 'cart_values': sum1})
        else:
            data['products'] = products
            # print('you are : ', request.session.get('email'))
            # print(data)
            return render(request, 'index.html', data)
