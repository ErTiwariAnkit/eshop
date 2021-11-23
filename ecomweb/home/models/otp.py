from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Otp(models.Model):
    otp = models.IntegerField()
    @staticmethod
    def get_otp():
        return list(Otp.objects.values_list('otp', flat = True))[0]