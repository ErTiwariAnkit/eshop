import re

from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views import View

from home.models.customer import Customer
from home.models.otp import Otp


class Password_reset(View):
    def get(self, request):
        return render(request, 'core/password_reset_confirm.html')

    def post(self, request):
        postData = request.POST
        print(Otp.get_email())
        password1=postData.get('password')
        password2 = postData.get('New_password')
        customer = Customer.get_customer_by_email(Otp.get_email())
        error_message = self.validateCustomer(password1, password2)
        if not error_message:
            customer.password = make_password(password1)
            customer.save()
            return render(request, 'core/password_reset_complete.html')
        return render(request, 'core/password_reset_confirm.html',{'error_message':error_message})
    def isAllPresent(self, str):

        # ReGex to check if a string
        # contains uppercase, lowercase
        # special character & numeric value
        regex = ("^(?=.*[a-z])(?=." +
                 "*[A-Z])(?=.*\\d)" +
                 "(?=.*[-+_!@#$%^&*., ?]).+$")

        # Compile the ReGex
        p = re.compile(regex)

        # Print Yes if string
        # matches ReGex
        if (re.search(p, str)):
            return False
        else:
            return True
    def validateCustomer(self,password1,password2):
        error_message = None;
        if password1!=password2:
            error_message='password and confirm password must be same'
        if len(password1) < 6:
            error_message = 'Password must be 6 char long'
        elif self.isAllPresent(password1):
            error_message = 'Password must be a special character Uppercase lowercase and number'
        # saving

        return error_message
