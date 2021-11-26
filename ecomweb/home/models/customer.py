from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    address = models.CharField(max_length=50, default='')

    def register(self):
        self.save()

    def get_customer_default_address(request):
        # sample_instance = Customer.objects.get(id=2)
        # value_of_name = sample_instance.address
        value_of_name = request.session['customer_address']
        print(value_of_name)
        return value_of_name

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def get_customer_by_id(id):
        try:
            return Customer.objects.get(id=id)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False
