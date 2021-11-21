from django.shortcuts import render , redirect , HttpResponseRedirect,HttpResponse
from home.models.product import Product
from home.models.category import Category
from home.models import product
from django.views import View


# Create your views here.
class Index(View):
    def get(self , request):
        #productID=request.GET.get('product')
        #print('product id is',productID)
        #product = Product.get_products_by_id(productID)
        productID = request.GET.get('product')
        product=Product.get_products_by_id(productID)
        print('product id is--------------',product)
        #return render(request, 'product_detail.html',{'product':product})