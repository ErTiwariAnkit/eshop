from django.db import models


class Otp(models.Model):
    otp = models.IntegerField()
    email = models.EmailField()

    @staticmethod
    def get_otp():
        return list(Otp.objects.values_list('otp', flat=True))[0]

    @staticmethod
    def get_email():
        return list(Otp.objects.values_list('email', flat=True))[0]
