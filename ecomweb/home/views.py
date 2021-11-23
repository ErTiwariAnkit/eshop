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
    print('category id is',categoryID)
    productID = request.GET.get('product')
    customerID = request.session.get('customer')
    sort = request.GET.get('drop1')
    print('sort is',sort)
    customer = Customer.get_customer_by_id(customerID)
    print(customer)
    print('productid is', productID)
    if sort!=None:
        if int(sort)==1:
            products_sort_name=Product.get_product_sort_name()
            data={}
            data['categories'] = categories
            data['customer'] = customer
            data['products_sort_name']=products_sort_name
            print('sort run')
            return render(request,'sort_by_name.html',data)
        elif int(sort)==2:
            products_sort_price=Product.get_product_sort_price()
            data={}
            data['categories'] = categories
            data['customer'] = customer
            data['products_sort_name']=products_sort_price
            print('sort run')
            return render(request,'sort_by_name.html',data)
    if productID != None:
        products = Product.get_products_by_id(productID)
        print('products is', products)
        cart = request.session.get('cart')
        print('cart product detail is',sum(cart.values()))
        if cart:
            sum1=sum(cart.values())
            sum1=str(sum1)+' items'
        else:
            sum1='is empty'
        return render(request, 'product_detail.html', {'product': products,'cart_values':sum1})
    elif categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    products_sort_name=Product.get_product_sort_name()
    if 'search' in request.GET:
        data = {}
        search_term = request.GET['search']
        search_products=Product.get_search_product(search_term=search_term,categoryid=categoryID)
        data['products'] = search_products
        data['categories'] = categories
        data['customer'] = customer
        print('search product',search_products)
        return render(request, 'index.html', data)

   
        
         

    

    data = {}
    data['products'] = products
    data['categories'] = categories
    data['customer'] = customer
    data['products_sort_name']=products_sort_name

    print('you are : ', request.session.get('email'))
    print(data)
    return render(request, 'index.html', data)
