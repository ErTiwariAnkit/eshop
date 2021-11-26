import math
import random

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View

from ecomweb.settings import EMAIL_HOST_USER
from home.models.customer import Customer
from home.models.otp import Otp


class Password_reset(View):
    def get(self, request):
        return render(request, 'core/password_reset.html')

    def post(self, request):
        postData = request.POST
        email = postData.get('email')
        otp=postData.get('otp')
        customer=Customer.get_customer_by_email(email=email)
        if customer:
            otp1=self.generateOTP()
            Otp.objects.all().delete()
            otp2 = Otp(otp=otp1, email=email)
            otp2.save()
            self.send_mail1(email,otp1)
            return redirect('password_reset_done')
        else:
            return render(request, 'core/password_reset.html',{'error':'Email is not Register'})
    def generateOTP(self):
        digits = "0123456789"
        OTP = ""
        for i in range(6):
            OTP += digits[math.floor(random.random() * 10)]
        return OTP
    def validateotp():
        pass

    # Function checks if the input string(test)
    # contains any special character or not
    def send_mail1(self, email,otp):
        subject = 'welcome to Ankit Tiwari E-commerce Websites'
        message = f'Someone asked for password reset for email { email }". Follow the link below:http://127.0.0.1:8000/ to login Your otp is {otp}'
        email_from = EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)