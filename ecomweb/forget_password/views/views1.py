from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from ecomweb.settings import EMAIL_HOST_USER
import math, random
from django.core.mail import send_mail
from home.models.customer import Customer
from home.models.otp import Otp
from django.views import View
import re

class Password_reset(View):
    def get(self, request):
        return render(request, 'core/password_reset_done.html')

    def post(self, request):
        postData = request.POST
        otp=postData.get('otp')
        otp_get = Otp.get_otp()
        print(type(otp))
        print(type(otp_get))
        if int(otp)==otp_get:
            return redirect('password_reset_confirm')
        else:
            return render(request, 'core/password_reset_done.html')