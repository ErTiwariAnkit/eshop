import re

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View

from ecomweb.settings import EMAIL_HOST_USER
from home.models.customer import Customer


class Signup(View):
    def get(self, request):
        customerID = request.session.get('customer')
        if customerID:  # if user want to access registration page after login redirec home page
            return redirect('/')
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        address = postData.get('address')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
            'address': address
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password,
                            address=address)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            self.send_mail1(first_name, last_name, email)
            customer.register()
            return redirect('home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    # Function checks if the input string(test)
    # contains any special character or not
    def send_mail1(self, first_name, last_name, email):
        subject = 'welcome to Ankit Tiwari E-commerce Websites'
        message = f'Hi {first_name} {last_name}, thank you for registering in E-Shop'
        email_from = EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)

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

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif self.isAllPresent(customer.password):
            error_message = 'Password must be a special character Uppercase lowercase and number'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
