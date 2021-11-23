from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    avail=models.BooleanField(default=False)
    quantity=models.IntegerField(default=0)
    seller=models.CharField(max_length=100,default='')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.get(id=ids)
    @staticmethod
    def get_search_product(search_term,categoryid):
        products=Product.get_all_products_by_categoryid(category_id=categoryid)
        return products.filter(name__contains=search_term)
    @staticmethod
    def get_product_sort_name():
        return Product.objects.order_by('name')
    @staticmethod
    def get_product_sort_price():
        return Product.objects.order_by('price')
        

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();