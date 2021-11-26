import datetime

from django.db import models

from .customer import Customer
from .product import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=15)
    email = models.EmailField(default=None)
    city = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50, default='', blank=True)
    postal = models.IntegerField(default=0)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField()

    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    def new_address(self):
        return self.address

    def get_order_id(self):
        return self.id

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
